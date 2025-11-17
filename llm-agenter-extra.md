# Extra Material 📚

[← Tillbaka till huvudguiden](./llm-agenter-guide.md)

---

## 🛠️ Plattformsjämförelse

### Fullständig tabell: Ramverk och Verktyg (November 2025)

| Plattform | Typ | Pris | Svårighet | Bäst för | Status 2025 |
|-----------|-----|------|-----------|----------|-------------|
| **LangChain 1.0** | Framework | Free | Medium | RAG, Chains, Agents | ✅ Stabil! Ingen breaking changes till 2.0 |
| **LangGraph 1.0** | Framework | Free | Hög | Durable agents, State machines | ✅ Production-ready! |
| **LangSmith Deployment** | Platform | Varies | Medium | Deploy LangGraph agents | 🆕 Tidigare "LangGraph Platform" |
| **Microsoft Agent Framework** | Framework | Free | Medium | Enterprise multi-agent | 🆕 Public Preview Nov 2025 |
| **Magentic-One** | Multi-Agent | Open-source | Hög | Orchestrated 4-agent system | 🆕 Nov 2025 - Microsoft Research |
| **AutoGen** | Framework | Free | Medium | Multi-agent conversations | ⚠️ Maintenance mode (use Agent Framework) |
| **CrewAI** | Framework | Free | Låg-Medium | Role-based automation | ✅ Aktiv utveckling 2025 |
| **Claude Agent SDK** | SDK | Usage-based | Medium | Agentic coding, Computer Use | 🆕 Tidigare "Claude Code SDK" |
| **OpenAI Assistants** | API | Usage-based | Låg | Enkel agent-bygge | ✅ Structured outputs support |
| **Google Gemini 2.0** | API | Usage-based | Låg | Multimodal, Coding | 🆕 Flash allmänt tillgänglig Nov 2025 |
| **Vercel AI SDK 6** | Framework | Free | Låg-Medium | Next.js, Agent abstraction | 🆕 Beta Oktober 2025 |
| **n8n** | No-code | €20/mån | Låg | Workflow automation | ✅ Stabil |
| **Zapier Central** | No-code | $20-240/mån | Låg | Quick integrations | ✅ Stabil |
| **Make** | No-code | €9-299/mån | Låg | Visual workflows | ✅ Stabil |
| **Flowise** | Low-code | Free (self-host) | Låg | LangChain UI | ✅ Stabil |
| **LangFlow** | Low-code | Free | Låg | Visual agent builder | ✅ Aktiv utveckling |
| **Haystack** | Framework | Free | Medium | RAG pipelines | ✅ Stabil |
| **LlamaIndex** | Framework | Free | Medium | Data indexing & retrieval | ✅ Stabil |
| **DSPy 2.5+** | Framework | Free | Hög | Prompt optimization (GEPA) | ✅ Beyond 2.0, SOTA optimizers |
| **Semantic Kernel** | Framework | Free | Medium | Microsoft .NET stack | ✅ Magentic support |
| **Langfuse** | Observability | Free-$99/mån | Låg | Open-source tracing | ⭐ 50K events/mån gratis |
| **LangSmith** | Observability | $Free-Enterprise | Låg-Medium | LangChain-native tracing | ⭐ 5K traces/mån gratis |
| **Braintrust** | Evaluation | Free-Enterprise | Medium | LLM eval & monitoring | ⭐ Bäst för TypeScript/JS |
| **LiteLLM** | Proxy | Free (self-host) | Låg | Unified multi-provider API | ✅ Load balancing |
| **Amazon Nova** | Embeddings | Usage-based | Låg | Multimodal embeddings | 🆕 Text, video, audio support |
| **Devtron 2.0** | DevOps | Free-Paid | Medium | Agentic SRE för Kubernetes | 🆕 Nov 2025 |

**🔥 Hot Picks November 2025:**
- **Production Agents**: LangGraph 1.0 + Claude Sonnet 4.5 + Langfuse
- **Rapid Prototyping**: Flowise + GPT-4o mini + gratis tier
- **Enterprise**: Microsoft Agent Framework + Azure OpenAI
- **Multi-Agent**: Magentic-One (open-source) eller CrewAI (enklare)
- **JavaScript**: Vercel AI SDK 6 + Next.js + Braintrust
- **Observability**: Langfuse (budget) eller LangSmith (LangChain-heavy)

**⚠️ Stora Förändringar 2025:**
1. **AutoGen** → maintenance mode, ersätts av **Microsoft Agent Framework**
2. **LangGraph Platform** → omdöpt till **LangSmith Deployment**
3. **Claude Code** → nu **Claude Agent SDK** med bredare capabilities
4. **LangGraph 1.0** är första stabila durable agent framework
5. **Structured Outputs** nu standard (ej function calling)

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

### Cost Comparison (per 1M tokens) - Uppdaterad November 2025

| LLM | Input | Output | Context | Sweet spot | Nytt 2025 |
|-----|-------|--------|---------|------------|-----------|
| **GPT-4o** | $2.50 | $10 | 128K | Balans pris/kvalitet | 83% prisfall! |
| **GPT-4o mini** | $0.15 | $0.60 | 128K | Bulk operations | Bäst för höga volymer |
| **GPT-4 Turbo** | $10 | $30 | 128K | Extremt komplexa tasks | Legacy, använd sällan |
| **Claude Sonnet 4.5** | $3 | $15 | 200K | Bäst för agents | "Världens bästa agent-modell" |
| **Claude Sonnet 3.7** | $3 | $15 | 200K | Inkl. thinking tokens | Stabil production |
| **Claude Haiku 4.5** | $0.8 | $4 | 200K | 90% av Sonnet, 2x snabbare | NYHET Okt 2025 |
| **Claude Opus 3** | $15 | $75 | 200K | Extremt komplexa uppgifter | Premium tier |
| **Gemini 2.0 Flash** | $0.35 | $1.50 | 1M | Production-ready | NYHET Nov 2025 |
| **Gemini 2.0 Flash-Lite** | $0.20 | $0.80 | 1M | Billigaste multimodal | Public Preview |
| **Gemini 2.0 Pro** | $1.25 | $5 | 2M | Coding & komplex reasoning | Experimental |
| **Gemini 1.5 Flash** | $0.075 | $0.30 | 1M | Snabbaste/billigaste | Fortfarande konkurrenskraftig |

**🔥 Hot Picks November 2025:**
- **Prototyping**: GPT-4o mini ($0.15/$0.60) eller Gemini 2.0 Flash-Lite
- **Production Agents**: Claude Sonnet 4.5 ($3/$15) eller Claude Haiku 4.5 för cost/performance
- **High Volume**: Gemini 2.0 Flash ($0.35/$1.50) - bra balans mellan kostnad och kvalitet
- **Max Quality**: Claude Opus 3 ($15/$75) när kostnad inte spelar roll

**💡 Cost Optimization Tips:**
- **Batch API**: 50% rabatt på alla OpenAI-modeller (asynkrona requests)
- **Prompt Caching**: 90% besparing på input tokens (Claude, OpenAI)
- **Model Routing**: Start billigt (mini/Haiku), escalera till dyrare vid behov
- **Context Optimization**: Använd bara nödvändig kontext

**📊 Prisfall sedan 2024:**
- GPT-4 output: 83% billigare ($60 → $10 per 1M tokens)
- GPT-4 input: 90% billigare ($30 → $2.50 per 1M tokens)
- Kombinerat med prompt caching: **Upp till 95% totalbesparing** för RAG use cases!

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

### Q1 2025 Updates

**Q: Vad är structured outputs och varför ska jag använda det?**
A: Structured outputs (OpenAI, Anthropic) garanterar att LLM:en följer ett JSON schema - 100% type-safe. Bättre än function calling eftersom outputs ALLTID följer schema. Använd med Pydantic:
```python
class Output(BaseModel):
    result: str
    confidence: float

response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    response_format=Output
)
# Garanterat Output-kompatibel!
```

**Q: Hur fungerar prompt caching och hur mycket sparar jag?**
A: Prompt caching (Anthropic, OpenAI) cachar stora delar av din prompt mellan requests:
- **Spar 90%** på input tokens för cachade delar
- Perfekt för RAG där dokument är samma
- Cache varar 5-15 minuter
- Exempel: RAG med 10K token kontext → Från $0.30 till $0.03 per request

**Q: Vad är skillnaden mellan GPT-4 och GPT-4o?**
A: GPT-4o (Omni) från maj 2024:
- 75% billigare ($2.50 vs $10 per 1M input tokens)
- 2x snabbare
- Bättre på structured outputs
- Multimodal (text, bild, ljud)
→ Använd GPT-4o för 95% av use cases, endast GPT-4 Turbo för extremt komplexa tasks

**Q: När ska jag använda Gemini istället för OpenAI/Anthropic?**
A: Använd Gemini 1.5 när:
- Du behöver extremt långa contexts (upp till 2M tokens)
- Budget är tight (Flash är billigaste modellen)
- Du är i Google Cloud ekosystemet
- Multimodal är viktigt (native video understanding)

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

### 🆕 November 2025 Updates

**Q: Vad är Claude Agent SDK och hur använder jag det?**
A: Claude Agent SDK (tidigare "Claude Code SDK") är Anthropics officiella SDK för att bygga agenter med Claude. Nytt November 2025:
- **CLAUDE.md-filer**: Lägg till `.claude/CLAUDE.md` i ditt repo - Claude läser automatiskt detta som kontext
- **Extended Thinking Mode**: Använd "think", "think hard", "think harder", eller "ultrathink" för olika reasoning-nivåer
- **Computer Use**: Agenter kan kontrollera browsers och datorer
- Bäst för agentic coding, test-driven development, och deep research

Exempel CLAUDE.md:
```markdown
# Repository Etiquette

- Använd pytest för alla tester
- Skriv docstrings för alla funktioner
- Max 80 tecken per rad
- Kör `ruff` före commit
```

**Q: Vilken modell ska jag välja November 2025: GPT-4o, Claude Sonnet 4.5, eller Gemini 2.0?**
A: Beror på use case:
- **Agents & Agentic Coding**: Claude Sonnet 4.5 ($3/$15) - "världens bästa agent-modell"
- **Cost/Performance Balance**: Claude Haiku 4.5 ($0.8/$4) - 90% av Sonnet, 2x snabbare, 3x billigare
- **Budget/High Volume**: Gemini 2.0 Flash ($0.35/$1.50) eller GPT-4o mini ($0.15/$0.60)
- **Max Context (2M tokens)**: Gemini 2.0 Pro
- **Batch Processing**: GPT-4o med Batch API (50% rabatt)

**Q: Hur mycket sparar jag VERKLIGEN med prompt caching?**
A: Konkreta exempel från November 2025:
- **RAG med 10K kontext**: $0.30 → $0.03 (90% besparing) per request
- **100K token bok**: Latency 11.5s → 2.4s (79% snabbare)
- **Cache TTL**: 5 minuter standard, 1 timme premium
- **Minimikrav**: Claude 3.5 (1024 tokens), Haiku 4.5 (4096 tokens)

Tips: Cache system prompts, dokument, och tool definitions - inte dynamiskt innehåll!

**Q: AutoGen är i maintenance mode - vad ska jag använda istället?**
A: Microsoft fokuserar nu på **Microsoft Agent Framework** (public preview November 2025):
- **Magentic-One**: Open-source multi-agent system med Orchestrator + 4 specialagenter
- **Agent2Agent (A2A) protokoll**: Agents kommunicerar mellan olika runtimes
- **Semantic Kernel**: Fortsätter utvecklas, har Magentic-support
- **Alternativ**: CrewAI (enklare), LangGraph 1.0 (mer kontroll)

AutoGen funkar fortfarande men får inga nya features.

**Q: Är prompt injection verkligen olösligt? Hur skyddar jag mig November 2025?**
A: Tyvärr ja - OpenAI CISO kallar det "frontier, unsolved security problem". Senaste hot:
- **EchoGram** (Nov 2025): Enkel string som "=coffee" kan bypassa guardrails
- **OpenAI Guardrails**: Bypassade inom veckor efter Oct 2025 release
- **Multimodal Injection**: Emoji-sekvenser och rebus puzzles

**Best Defenses 2025:**
1. **Output-Level Controls**: Filtrera outputs, inte bara inputs
2. **Layered Defense**: Flera säkerhetslager (AWS Bedrock Guardrails, custom filters)
3. **Human-in-the-Loop**: Tool execution approval (Vercel AI SDK 6)
4. **Structured Testing**: Test alla agents med adversarial inputs
5. **Never Trust Agent Output**: Validera allt innan execution

**Q: LangGraph Platform vs LangSmith Deployment - vad hände?**
A: Oktober 2025: **LangGraph Platform omdöpt till LangSmith Deployment**
- Samma funktionalitet: Deploy long-running, stateful agents
- Integrerat i LangSmith för unified observability + deployment
- Stöd för Cloud, Hybrid, och Self-Hosted
- LangGraph 1.0 är stabilt - inga breaking changes till 2.0

**Q: Structured Outputs vs Function Calling - vilken ska jag använda 2025?**
A: **Structured Outputs vinner**:
- OpenAI: Native Pydantic-support, 100% schema-compliance
- Anthropic: Kräver "tool call trick", ~14-20% failure rate annars
- Garanterad type safety vs "best effort" function calling

Använd Function Calling endast för legacy-kod. Nya projekt: structured outputs.

**Q: Vilken vector database ska jag välja November 2025?**
A: Migration pattern: **Chroma → Weaviate → Pinecone**
- **Prototyping**: Chroma (gratis, enkelt, LangChain-integration)
- **Medium Scale**: Weaviate (hybrid search, multimodal, open-source option)
- **Production/Scale**: Pinecone (sub-50ms vid 1 billion vectors, managed, pricey)

**Benchmarks (1B vectors):**
- Pinecone p99: ~47ms
- Weaviate p99: ~123ms
- Chroma: Max ~10M vectors praktiskt

**Q: Vad är agentic chunking och ska jag använda det?**
A: **Agentic chunking** = LLM bestämmer chunking-strategi per dokument:
- Markdown file → split by headers
- Dense document → propositional chunking
- Code file → split by functions

**Bättre än fixed chunking** eftersom olika dokument behöver olika strategier.

**Alternativ 2025:**
- **Semantic Chunking**: Gruppera baserad på embedding similarity
- **Amazon Nova**: Automatic segmentation in multimodal embeddings

**Q: Ska jag deploya på Kubernetes eller köra serverless?**
A: **Kubernetes vinner för production agents 2025:**
- Docker Desktop 4.50: Direct K8s deployment
- Google Agent Sandbox: Sub-second latency (90% förbättring)
- Devtron 2.0: "Agentic SRE" - AI managerar K8s för dig
- Monitoring: Prometheus + Loki standard

**Serverless** funkar för:
- Låg volym (<1000 requests/dag)
- Sporadisk användning
- Quick prototypes

**Q: LangSmith vs Langfuse vs Braintrust för observability?**
A: **November 2025 recommendations:**
- **LangSmith**: Bäst om du är all-in på LangChain, djup integration, 5K traces/mån gratis
- **Langfuse**: Open-source, 50K events/mån gratis, budget-friendly, self-hostable
- **Braintrust**: Bäst för TypeScript/JavaScript, unified eval+monitoring, enterprise features

**Alla tre** stödjer multi-step agent tracing med nested spans (LangGraph, AutoGen).

**Q: Hur gör jag model routing för cost optimization?**
A: **Fallback chain pattern 2025:**
```python
def intelligent_routing(query: str, complexity: str):
    # Level 1: Billigaste
    if complexity == "simple":
        return gpt_4o_mini.invoke(query)  # $0.15/$0.60

    # Level 2: Balanced
    elif complexity == "medium":
        try:
            return claude_haiku_45.invoke(query)  # $0.8/$4
        except Exception:
            return gpt_4o.invoke(query)  # Fallback

    # Level 3: Max quality
    else:
        return claude_sonnet_45.invoke(query)  # $3/$15
```

**Spara 60-80%** genom att endast använda dyra modeller när nödvändigt.

**Q: Vad är Vercel AI SDK 6 och varför pratar alla om det?**
A: **Vercel AI SDK 6 Beta** (Oktober 2025):
- **Agent Abstraction Layer**: Definiera agents en gång, återanvänd överallt
- **Tool Execution Approval**: Human-in-the-loop för säkerhet
- **Workflow Support**: Durable workflows med retries (like Temporal)
- **Python SDK**: Nu även FastAPI/Flask (tidigare bara Next.js)
- **Marketplace Agents**: Installera CodeRabbit, Corridor, Sourcery m.fl.

**Perfect för** TypeScript/JavaScript developers som vill ha Next.js-first agentic AI.

**Q: Vad är skillnaden mellan Gemini 1.5 och 2.0?**
A: **Gemini 2.0** (November 2025):
- **Flash**: $0.35/$1.50 - allmänt tillgänglig, production-ready
- **Flash-Lite**: $0.20/$0.80 - billigaste multimodal (public preview)
- **Pro**: $1.25/$5 - bäst för coding och complex reasoning (experimental)
- **Förenklad pricing**: Ingen short vs long context-skillnad längre

**Gemini 1.5 Flash** ($0.075/$0.30) fortfarande billigast för höga volymer!

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

### Research Papers (Cutting-Edge 2024-2025)

1. **"ReAct: Synergizing Reasoning and Acting"** (2023)
   - https://arxiv.org/abs/2210.03629
   - Foundation för moderna agents

2. **"Tree of Thoughts"** (2023)
   - https://arxiv.org/abs/2305.10601
   - Multi-path reasoning

3. **"Reflexion: Language Agents with Verbal Reinforcement Learning"** (2023)
   - https://arxiv.org/abs/2303.11366
   - Self-improvement patterns

4. **"AutoGen: Enabling Next-Gen LLM Applications"** (2023)
   - Microsoft Research
   - Multi-agent frameworks

5. **"The Landscape of Emerging AI Agent Architectures"** (2024)
   - https://arxiv.org/abs/2404.11584
   - State-of-the-art översikt

6. **"Agents: An Open-source Framework for Autonomous LLM Agents"** (2024)
   - Latest production patterns

7. **"Prompt Caching for Large Language Models"** (Q4 2024)
   - Cost optimization techniques

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