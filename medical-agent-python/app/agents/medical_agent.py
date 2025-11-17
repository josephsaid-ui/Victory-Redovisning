"""
Medical AI Agent för ögonläkare

Analyserar transkriberat patientsamtal i realtid och ger:
- Identifiering av ögonsjukdomar
- Förslag på behandlingar
- Smarta anamnesfrågor
"""
import logging
from typing import List, Optional

from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

from app.tools.search_diseases import search_eye_diseases_tool
from app.tools.anamnesis import suggest_anamnesis_questions_tool
from app.memory.medical_context import MedicalContextManager
from app.rag.llamaindex_rag import medical_rag
from app.prompts.ophthalmology import OPHTHALMOLOGY_SYSTEM_PROMPT, JOURNAL_GENERATION_PROMPT
from app.models.medical_types import AgentSuggestion

logger = logging.getLogger(__name__)


class MedicalAgent:
    """
    Medical AI Agent för ögonläkare

    Använder LangChain för agent orchestration
    och LlamaIndex för RAG-baserad kunskapsökning
    """

    def __init__(
        self,
        model_name: str = "claude-3-5-sonnet-20241022",
        temperature: float = 0.2,
        streaming: bool = True
    ):
        self.llm = ChatAnthropic(
            model=model_name,
            temperature=temperature,
            streaming=streaming,
            max_tokens=4096
        )

        self.context_manager = MedicalContextManager()
        self.agent: Optional[AgentExecutor] = None
        self.initialized = False

    async def initialize(self):
        """Initialisera agenten"""
        if self.initialized:
            logger.info("Agent already initialized")
            return

        logger.info("🤖 Initializing Medical Agent...")

        # 1. Initialisera RAG
        await medical_rag.initialize()
        logger.info("✓ RAG initialized")

        # 2. Samla alla tools
        tools = [
            search_eye_diseases_tool,
            suggest_anamnesis_questions_tool,
        ]

        # 3. Skapa prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", OPHTHALMOLOGY_SYSTEM_PROMPT),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ])

        # 4. Skapa agent
        agent = create_tool_calling_agent(
            llm=self.llm,
            tools=tools,
            prompt=prompt
        )

        # 5. Skapa executor
        self.agent = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=5
        )

        self.initialized = True
        logger.info("✓ Medical Agent ready!")

    async def process_transcription(
        self,
        transcription_chunk: str
    ) -> List[AgentSuggestion]:
        """
        Processa transkriberad text och returnera suggestions
        """
        if not self.initialized:
            raise RuntimeError("Agent not initialized. Call initialize() first.")

        logger.info(f"\n📝 Processing transcription: {transcription_chunk}")

        # 1. Extrahera symptom från transcription
        symptoms = self.context_manager.extract_symptoms_from_text(transcription_chunk)
        for symptom in symptoms:
            duration = self.context_manager.extract_duration(transcription_chunk)
            if duration:
                symptom.duration = duration
            self.context_manager.add_symptom(symptom)

        # 2. Bygg input till agenten
        context = self.context_manager.get_context()
        agent_input = self._build_agent_input(transcription_chunk, context)

        # 3. Kör agenten
        result = await self.agent.ainvoke({"input": agent_input})

        logger.info(f"\n🤖 Agent response: {result['output']}")

        # 4. Parse och returnera suggestions
        # I produktion: Parse structured output
        suggestions = []

        return suggestions

    def _build_agent_input(self, transcription: str, context) -> str:
        """Bygg input till agenten"""
        parts = []

        parts.append("## NY TRANSCRIPTION:")
        parts.append(transcription)
        parts.append("")

        if context.symptoms:
            parts.append("## IDENTIFIERADE SYMPTOM:")
            for s in context.symptoms:
                parts.append(
                    f"- {s.name}" +
                    (f" ({s.duration})" if s.duration else "") +
                    (f" [{s.severity}]" if s.severity else "")
                )
            parts.append("")

        if context.suspected_diseases:
            parts.append("## MISSTÄNKTA SJUKDOMAR:")
            for d in context.suspected_diseases:
                parts.append(f"- {d.name} (sannolikhet: {int(d.probability * 100)}%)")
            parts.append("")

        parts.append("## UPPGIFT:")
        parts.append("Analysera transcriptionen och:")
        parts.append("1. Använd search_eye_diseases om nya symptom nämnts")
        parts.append("2. Använd suggest_anamnesis_questions för relevanta följdfrågor")
        parts.append("3. Ge konkreta, actionable suggestions")

        return "\n".join(parts)

    async def generate_journal_entry(self) -> str:
        """Generera journaltext baserat på conversation"""
        context = self.context_manager.get_context()

        prompt = f"""{JOURNAL_GENERATION_PROMPT}

## SYMPTOM:
{chr(10).join(f"- {s.name}" + (f" ({s.duration})" if s.duration else "") for s in context.symptoms)}

## MISSTÄNKTA DIAGNOSER:
{chr(10).join(f"- {d.name} ({d.icd10})" for d in context.suspected_diseases)}

## AKTUELLA LÄKEMEDEL:
{chr(10).join(f"- {m.name}" for m in context.current_medications) or "Inga"}

Generera en strukturerad ögonjournal enligt SOAP-format ovan.
"""

        response = await self.llm.ainvoke(prompt)
        return response.content

    def get_context(self):
        """Hämta nuvarande kontext"""
        return self.context_manager.get_context()

    def get_summary(self) -> str:
        """Hämta sammanfattning"""
        return self.context_manager.get_summary()

    def reset(self):
        """Rensa kontext (nytt samtal)"""
        self.context_manager.reset()
