"""
LangChain tool för att generera anamnesfrågor
"""
import logging
from typing import List
from langchain.tools import StructuredTool
from langchain_anthropic import ChatAnthropic
from pydantic import Field

from app.models.medical_types import MedicalContext, AnamnesisQuestion
from app.prompts.ophthalmology import ANAMNESIS_QUESTION_PROMPT, FALLBACK_QUESTIONS

logger = logging.getLogger(__name__)


async def suggest_anamnesis_questions_func(
    current_context: dict = Field(..., description="Nuvarande medicinsk kontext"),
    focus: str = Field("general", description="Fokusområde för frågorna")
) -> str:
    """
    Generera relevanta anamnesfrågor baserat på nuvarande samtal

    Använd detta tool när:
    - Du behöver mer information för att avgränsa diagnoser
    - Patienten har nämnt symptom som behöver utforskas djupare
    - Du vill följa upp på tidigare svar
    """
    try:
        logger.info("💭 Generating anamnesis questions...")

        # Konvertera dict till MedicalContext
        context = MedicalContext(**current_context)

        # Använd Claude för att generera frågor
        llm = ChatAnthropic(
            model="claude-3-5-sonnet-20241022",
            temperature=0.3
        )

        prompt = _build_question_prompt(context, focus)
        response = await llm.ainvoke(prompt)

        # Parse questions
        questions = _parse_questions(response.content)

        result = {
            "questions": [q.model_dump() for q in questions],
            "context_summary": context.get_summary(),
            "focus_area": focus
        }

        return str(result)

    except Exception as e:
        logger.error(f"Error generating questions: {e}")
        # Fallback till pre-defined questions
        return str({"questions": FALLBACK_QUESTIONS.get("blurry_vision", [])})


def _build_question_prompt(context: MedicalContext, focus: str) -> str:
    """Bygg prompt för question generation"""
    parts = [ANAMNESIS_QUESTION_PROMPT]
    parts.append("\n## NUVARANDE KONTEXT:\n")

    if context.symptoms:
        parts.append("### Nämnda symptom:")
        for s in context.symptoms:
            parts.append(f"- {s.name}" + (f" ({s.duration})" if s.duration else ""))
    else:
        parts.append("Inga symptom nämnda än")

    if context.suspected_diseases:
        parts.append("\n### Misstänkta sjukdomar:")
        for d in context.suspected_diseases:
            parts.append(f"- {d.name} (sannolikhet: {d.probability})")

    if context.asked_questions:
        parts.append("\n### Redan ställda frågor:")
        parts.extend(context.asked_questions)

    parts.append(f"\n### Fokusområde: {focus}")
    parts.append("\n## UPPGIFT:")
    parts.append("Generera 3-5 relevanta anamnesfrågor som:")
    parts.append("1. INTE upprepar redan ställda frågor")
    parts.append("2. Hjälper till att avgränsa mellan de misstänkta diagnoserna")
    parts.append("3. Följer upp på nämnda symptom")
    parts.append("4. Är naturliga i samtalsflödet")
    parts.append("5. Prioriterar allvarliga tillstånd")

    return "\n".join(parts)


def _parse_questions(response: str) -> List[AnamnesisQuestion]:
    """Parse frågor från LLM response"""
    questions = []

    # Simple parsing - i produktion använd structured output
    # För demo returnerar vi exempel-frågor
    if "suddig" in response.lower():
        questions.append(AnamnesisQuestion(
            question="Ser du halos eller ringar runt lampor?",
            category="related_symptoms",
            priority="high",
            rationale="Klassiskt tecken på katarakt"
        ))

    return questions[:5]


# Skapa LangChain tool
suggest_anamnesis_questions_tool = StructuredTool.from_function(
    coroutine=suggest_anamnesis_questions_func,
    name="suggest_anamnesis_questions",
    description="Generera intelligenta anamnesfrågor baserat på nuvarande kontext"
)
