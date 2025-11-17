# Extra Material 📚

[← Tillbaka till huvudguiden](./llm-agenter-guide.md)

---

## 🛠️ Plattformsjämförelse

### Fullständig tabell: Ramverk och Verktyg

| Plattform | Typ | Pris | Svårighet | Bäst för | Begränsningar |
|-----------|-----|------|-----------|----------|---------------|
| **LangChain** | Framework | Free | Medium | RAG, Chains, Basic agents | Brant lärkurva, verbose |
| **LangGraph** | Framework | Free | Hög | State machines, Komplexa workflows | Kräver LangChain |
| **AutoGen** | Framework | Free | Medium | Multi-agent conversations | Microsoft-fokuserad |
| **CrewAI** | Framework | Free | Låg-Medium | Role-based automation | Mindre flexibelt |
| **OpenAI Assistants** | API | Usage-based | Låg | Enkel agent-bygge | API-lock-in |
| **Claude (Anthropic)** | API | Usage-based | Låg | Kvalitet, lång context | API-lock-in |
| **Google Gemini** | API | Usage-based | Låg-Medium | Multimodal | Begränsad tillgänglighet |
| **n8n** | No-code | €20/mån | Låg | Workflow automation | Mindre kontroll |
| **Zapier Central** | No-code | $20-240/mån | Låg | Quick integrations | Dyrt för komplext |
| **Make** | No-code | €9-299/mån | Låg | Visual workflows | Kan bli dyrt |
| **Flowise** | Low-code | Free (self-host) | Låg | LangChain UI | Begränsad till LangChain |
| **LangFlow** | Low-code | Free | Låg | Visual agent builder | Under utveckling |
| **Haystack** | Framework | Free | Medium | RAG pipelines | Specifik för RAG |
| **LlamaIndex** | Framework | Free | Medium | Data indexing | Fokus på retrieval |
| **DSPy** | Framework | Free | Hög | Prompt optimization | Ny, färre exempel |
| **Semantic Kernel** | Framework | Free | Medium | Microsoft stack | .NET-fokuserad |

---

### Beslutträd: Vilket verktyg ska jag välja?

```
Kan du koda?
├─ Nej → No-code
│  ├─ Simpla workflows → Zapier
│  ├─ Komplexa workflows → n8n
│  └─ LangChain-baserat → Flowise
│
└─ Ja → Kod-baserat
   │
   ├─ Use case?
   │  ├─ RAG/Dokumentsökning
   │  │  ├─ Snabb start → LlamaIndex
   │  │  └─ Flexibilitet → LangChain + Chroma/Pinecone
   │  │
   │  ├─ Multi-agent
   │  │  ├─ Conversational → AutoGen
   │  │  ├─ Role-based → CrewAI
   │  │  └─ Custom logic → LangGraph
   │  │
   │  ├─ Enkel chatbot
   │  │  ├─ OpenAI-only → OpenAI Assistants API
   │  │  ├─ Anthropic → Claude API
   │  │  └─ Flexibelt → LangChain
   │  │
   │  └─ Komplexa workflows med loopar
   │     → LangGraph
   │
   └─ Ekosystem?
      ├─ Python → LangChain, AutoGen, CrewAI
      ├─ .NET → Semantic Kernel
      └─ JavaScript → LangChain.js
```

---

### Cost Comparison (per 1M tokens)

| LLM | Input | Output | Sweet spot |
|-----|-------|--------|------------|
| **GPT-4 Turbo** | $10 | $30 | Kvalitet viktigt |
| **GPT-3.5 Turbo** | $0.50 | $1.50 | Bulk operations |
| **Claude 3 Opus** | $15 | $75 | Analys, lång context |
| **Claude 3 Sonnet** | $3 | $15 | Balans kvalitet/pris |
| **Claude 3 Haiku** | $0.25 | $1.25 | Hög volym |
| **Gemini Pro** | $0.50 | $1.50 | Google-ekosystem |

---

## 🎓 Självutvärdering

### Kan du nu...?

#### Efter Nivå 1 (Grundkoncept)
- [ ] Förklara vad en LLM-agent är för någon som aldrig hört talas om det?
- [ ] Ge 3 exempel på var agenter används idag?
- [ ] Beskriva skillnaden mellan en chatbot och en agent?

#### Efter Nivå 2 (Termer)
- [ ] Förklara vad LLM, Prompt, Tool, Memory och Chain betyder?
- [ ] Ge exempel på vad en "tool" kan vara?
- [ ] Skriva en bra prompt (tydlig och detaljerad)?
- [ ] Förklara skillnaden mellan kort- och långtidsminne?
- [ ] Rita en enkel chain (steg-för-steg)?

#### Efter Nivå 3 (Tekniskt)
- [ ] Förklara skillnaden mellan ReAct och Plan-and-Execute?
- [ ] Skapa ett eget verktyg med `@tool`?
- [ ] Sätta upp en agent med LangChain?
- [ ] Implementera minst ett av projekten?
- [ ] Debugga agent-fel med verbose mode?

#### Efter Nivå 4 (Avancerat)
- [ ] Förklara hur RAG fungerar steg-för-steg?
- [ ] Bygga en multi-agent med minst 2 agents?
- [ ] Implementera ett LangGraph workflow med loopar?
- [ ] Välja rätt chunk size för ett dokument?
- [ ] Sätta upp hybrid search (semantic + keyword)?
- [ ] Integrera RAG i en conversational chain?

#### Efter Nivå 5 (Expert)
- [ ] Containerize en agent med Docker?
- [ ] Bygga ett production-ready API med FastAPI?
- [ ] Implementera säkerhetsåtgärder (guardrails, validation)?
- [ ] Sätta upp observability (LangSmith, logging)?
- [ ] Optimera kostnader med caching och model cascading?
- [ ] Deploya en full agent platform?

**40-48 bockar**: 🏆 Grattis! Du är expert!
**30-39 bockar**: 🌟 Mycket bra! Repetera några områden.
**20-29 bockar**: 💪 Bra grund! Gör fler övningar.
**10-19 bockar**: 📚 Fortsätt studera, du är på rätt väg!
**0-9 bockar**: 🎯 Börja om från nivå 1, ta din tid!

---

## ❓ Vanliga Frågor (FAQ)

### Grundläggande

**Q: Vad är skillnaden mellan en LLM och en agent?**
A: En LLM (som ChatGPT) kan bara generera text. En agent kan använda LLM:en PLUS verktyg för att utföra uppgifter (söka på webben, skriva till databaser, etc.).

**Q: Kostar det pengar att köra agenter?**
A: Ja, de flesta LLM:er kostar per token. GPT-4: ~$0.03-0.06 per 1K tokens. För prototyper kan du använda gratis tier, men produktion kostar.

**Q: Kan jag bygga agenter utan att koda?**
A: Ja! Verktyg som n8n, Zapier, Flowise låter dig bygga agenter visuellt utan kod.

**Q: Vilken plattform ska jag börja med?**
A: För nybörjare: Flowise (no-code). För kodare: LangChain (mest populär, bra docs).

---

### Tekniska

**Q: Hur förhindrar jag infinite loops?**
A: Sätt alltid `max_iterations` på din AgentExecutor:
```python
agent_executor = AgentExecutor(
    agent=agent,
    max_iterations=10  # Stoppar efter 10 steg
)
```

**Q: Hur hanterar jag rate limits från OpenAI?**
A: Implementera exponential backoff:
```python
from tenacity import retry, wait_exponential
@retry(wait=wait_exponential(min=2, max=60))
def call_llm(prompt):
    return llm.predict(prompt)
```

**Q: Vad är bästa sättet att spara agent-memory?**
A: För korta sessioner: ConversationBufferMemory. För långa: ConversationSummaryMemory. För persistent: Spara till Redis eller databas.

**Q: Hur debuggar jag agent-beslut?**
A: Sätt `verbose=True` och använd LangSmith för full tracing.

**Q: Skillnad mellan LangChain och LangGraph?**
A: LangChain: Linjära chains och basic agents. LangGraph: State machines med loopar och villkor.

---

### Avancerade

**Q: När ska jag använda multi-agent vs single agent?**
A: Multi-agent när:
- Uppgiften har tydliga sub-domains (research, writing, review)
- Du vill parallellisera arbete
- Specialisering ger bättre kvalitet

**Q: Hur skalar jag till 1000+ användare?**
A:
1. Använd Redis för caching och session management
2. Load balancer framför flera API-instanser
3. Queue system (Celery) för långvariga tasks
4. Vector DB (Pinecone, Weaviate) för RAG skalning

**Q: Best practices för prompt injection-skydd?**
A:
1. Input validation med regex/allow lists
2. Guardrails (NeMo Guardrails)
3. Output sanitization
4. Separate system prompts från user input
5. Aldrig inkludera känslig data i prompts

**Q: Hur mäter jag agent-prestanda?**
A: Tracka:
- Success rate (% tasks completed)
- Average latency
- Token usage / cost
- Tool usage patterns
- Error rates

**Q: Kan agenter lära sig över tid?**
A: Delvis:
- Kortsiktigt: Memory mellan meddelanden i samma session
- Långsiktigt: Spara tidigare interaktioner i vector DB för retrieval
- Äkta learning: Kräver fine-tuning av modellen (dyrt, komplext)

**Q: ROI för agent-automation?**
A: Räkna:
- Manuell tid sparad × timpris
- Minus: LLM costs + development + maintenance
- Typisk break-even: 3-6 månader för repetitiva uppgifter

---

## 📖 Ordlista (A-Ö)

**Agent**: AI-system som autonomt kan utföra uppgifter med verktyg

**AgentExecutor**: LangChain-klass som kör en agent med error handling

**API**: Application Programming Interface - hur program pratar med varandra

**AutoGen**: Microsoft's framework för multi-agent conversations

**Chain**: Sekvens av LLM-anrop eller operations (A→B→C)

**Chatbot**: AI som bara pratar, utan verktyg (jfr Agent)

**Chunk**: Del av ett dokument (vid text splitting för RAG)

**Claude**: Anthropic's LLM-familj (Opus, Sonnet, Haiku)

**Context Window**: Max antal tokens LLM:en kan hantera (t.ex. 128K för GPT-4)

**ConversationalAgent**: Agent fokuserad på dialog och kontext

**CrewAI**: Framework för role-based multi-agent systems

**DSPy**: Framework för programmatic prompt optimization

**Embeddings**: Vektor-representation av text (för semantic search)

**FAISS**: Facebook's vector database (gratis, lokalt)

**Fine-tuning**: Träna om en LLM på egen data (dyrt)

**Function Calling**: LLM returnerar strukturerad output för tool-användning

**GPT**: Generative Pre-trained Transformer (OpenAI's modeller)

**Guardrails**: Regler som begränsar vad agent får göra

**Hallucination**: När LLM hittar på fakta

**Haystack**: Framework för RAG pipelines

**LangChain**: Populäraste framework för att bygga LLM-appar

**LangGraph**: LangChains tool för state machines och komplexa workflows

**LangSmith**: Observability-plattform för LangChain (tracing, debugging)

**LlamaIndex**: Framework för data indexing och retrieval

**LLM**: Large Language Model (GPT, Claude, Gemini etc.)

**Memory**: Agents förmåga att komma ihåg tidigare konversation

**Multi-agent**: System där flera agenter samarbetar

**n8n**: No-code workflow automation platform

**OpenAI**: Företag bakom ChatGPT, GPT-4

**Orchestration**: Koordinera flera agents eller workflows

**Plan-and-Execute**: Agent-typ som planerar alla steg först

**Planner**: Komponent som bryter ner uppgifter i steg

**Prompt**: Text du skickar till LLM:en

**Prompt Engineering**: Konst att skriva bra prompts

**Prompt Injection**: Säkerhetsattack där man manipulerar agent via prompt

**RAG**: Retrieval-Augmented Generation - ge LLM tillgång till dokument

**ReAct**: Agent-typ som växlar mellan reasoning och acting

**Reflexion**: Agent som lär från misstag

**Semantic Kernel**: Microsoft's LLM framework (.NET)

**Semantic Search**: Sökning baserad på betydelse, inte nyckelord

**Temperature**: Parameter som styr hur kreativ/slumpmässig LLM är (0-1)

**Token**: Minsta enhet text (ca 0.75 ord på engelska)

**Tool**: Funktion/verktyg som agent kan använda

**Tree-of-Thoughts**: Teknik där LLM utforskar flera lösningsvägar

**Vector Database**: Databas för semantic search (Pinecone, Chroma, Qdrant)

**Vectorstore**: Samma som Vector Database

**Verbose Mode**: Debug-läge som visar agents tankar steg-för-steg

**Workflow**: Serie av steg för att utföra en uppgift

---

## 🔗 Resurser för Fördjupning

### Officiell Dokumentation

1. **LangChain** - https://python.langchain.com/
   - Mest omfattande docs för agent-building
   - 1000+ exempel

2. **LangGraph** - https://langchain-ai.github.io/langgraph/
   - State machines och workflows
   - Tutorials för multi-agent

3. **OpenAI Platform** - https://platform.openai.com/docs
   - Assistants API
   - Function calling
   - Best practices

4. **Anthropic Claude** - https://docs.anthropic.com/
   - Claude API
   - Tool use
   - Prompt engineering

5. **AutoGen** - https://microsoft.github.io/autogen/
   - Multi-agent conversations
   - Code execution

6. **CrewAI** - https://docs.crewai.com/
   - Role-based agents
   - Task delegation

7. **n8n** - https://docs.n8n.io/
   - Workflow automation
   - AI integrations

8. **Haystack** - https://haystack.deepset.ai/
   - RAG pipelines
   - Document search

9. **LlamaIndex** - https://docs.llamaindex.ai/
   - Data indexing
   - Query engines

10. **Pinecone** - https://docs.pinecone.io/
    - Vector database
    - Semantic search

---

### Online-Kurser

1. **"LangChain for LLM Application Development"** - DeepLearning.AI
   - Gratis, ~2 timmar
   - Hands-on med notebook
   - https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/

2. **"Building Systems with ChatGPT API"** - DeepLearning.AI
   - Gratis, ~1 timme
   - Multi-step systems

3. **"LangChain Masterclass"** - Udemy
   - €14.99
   - 8+ timmar video
   - Projekt-baserad

4. **"AI Agents in LangGraph"** - DeepLearning.AI
   - Gratis, ny 2024
   - State machines

5. **"Prompt Engineering for Developers"** - DeepLearning.AI
   - Gratis fundamental

---

### GitHub-Repositories (Exempel & Templates)

1. **awesome-ai-agents**
   - https://github.com/e2b-dev/awesome-ai-agents
   - Curated list of AI agents

2. **langchain-examples**
   - https://github.com/gkamradt/langchain-tutorials
   - 50+ notebooks med exempel

3. **agent-templates**
   - https://github.com/langchain-ai/langchain/tree/master/templates
   - Production-ready templates

4. **autogen-examples**
   - https://github.com/microsoft/autogen/tree/main/notebook
   - Multi-agent examples

5. **crewai-examples**
   - https://github.com/joaomdmoura/crewAI-examples
   - Role-based workflows

---

### Communities & Forum

1. **LangChain Discord** - https://discord.gg/cU2adEyC7w
   - 50K+ medlemmar
   - Support och diskussion

2. **r/LangChain** - https://reddit.com/r/LangChain
   - Reddit community

3. **AI Engineers** - https://www.latent.space/
   - Podcast + community

4. **Prompt Engineering Discord**
   - Fokus på prompts

5. **AutoGen Discord** - Microsoft-community

---

### YouTube-Kanaler

1. **AI Jason**
   - https://youtube.com/@AIJasonZ
   - LangChain tutorials

2. **Sam Witteveen**
   - https://youtube.com/@samwitteveenai
   - Wekly AI updates

3. **David Ondrej**
   - LangGraph deep-dives

4. **Matt Williams**
   - RAG och vector DBs

---

### Podcasts

1. **Latent Space** - https://latent.space/
   - Intervjuer med AI builders
   - Senaste trends

2. **Practical AI** - https://changelog.com/practicalai
   - Applied AI discussions

3. **The TWIML AI Podcast**
   - Machine learning focus

---

### Böcker

1. **"Building LLM Apps"** - Valentina Alto (2024)
   - Praktisk guide
   - LangChain focus

2. **"Hands-On Large Language Models"** - Jay Alammar, Maarten Grootendorst (2024)
   - O'Reilly
   - From basics to advanced

3. **"Prompt Engineering for Generative AI"** - James Phoenix, Mike Taylor (2024)
   - O'Reilly
   - Prompt strategies

---

### Research Papers (Cutting-Edge)

1. **"ReAct: Synergizing Reasoning and Acting"** (2023)
   - https://arxiv.org/abs/2210.03629

2. **"Tree of Thoughts"** (2023)
   - https://arxiv.org/abs/2305.10601

3. **"Reflexion: Language Agents with Verbal Reinforcement Learning"** (2023)
   - https://arxiv.org/abs/2303.11366

4. **"AutoGen: Enabling Next-Gen LLM Applications"** (2023)
   - Microsoft Research

---

## 🗺️ Din Agent-Roadmap

### Nybörjare (Månad 1-2)

**Vecka 1-2: Basics**
- [ ] Gå igenom Nivå 1-2
- [ ] Prova ChatGPT Plugins eller Custom GPTs
- [ ] Testa Flowise (no-code)

**Vecka 3-4: Första koden**
- [ ] Installera Python + LangChain
- [ ] Gör övningar Nivå 3
- [ ] Bygg din första simple agent

**Vecka 5-8: Grundläggande projekt**
- [ ] FAQ-bot med memory
- [ ] Simpel RAG-applikation
- [ ] Deploy på Streamlit Community Cloud

---

### Mellan (Månad 3-4)

**Månad 3: Multi-agent & RAG**
- [ ] Gå igenom Nivå 4
- [ ] Bygg multi-agent system (AutoGen ELLER CrewAI)
- [ ] Enterprise RAG med 50+ dokument
- [ ] Lär dig vector databases (Pinecone/Chroma)

**Månad 4: Production basics**
- [ ] Dockerize en agent
- [ ] FastAPI endpoint
- [ ] Basic monitoring
- [ ] Cost tracking

---

### Avancerad (Månad 5-6)

**Månad 5: Komplexitet**
- [ ] LangGraph workflows
- [ ] Hybrid multi-agent systems
- [ ] Advanced RAG (hybrid search, reranking)

**Månad 6: Production**
- [ ] Gå igenom Nivå 5
- [ ] Full CI/CD pipeline
- [ ] Security audit
- [ ] Deploy till AWS/GCP/Azure

---

### Expert (Månad 7+)

- [ ] Bidra till open-source (LangChain, AutoGen)
- [ ] Publicera egna templates
- [ ] Optimera för edge cases
- [ ] Research papers och blogginlägg

---

## 🎉 Grattis!

Du har nu tillgång till en komplett guide om LLM-agenter från grunderna till expert-nivå!

**Nästa steg:**
1. Välj din startpunkt baserat på självutvärdering
2. Gör övningarna praktiskt
3. Bygg minst 2-3 projekt
4. Dela med community
5. Fortsätt lära - området utvecklas snabbt!

**Lycka till på din agent-resa! 🚀**

---

[← Tillbaka till huvudguiden](./llm-agenter-guide.md)