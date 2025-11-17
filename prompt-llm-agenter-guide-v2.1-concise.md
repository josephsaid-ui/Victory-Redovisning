# LLM-Agenter Guide Prompt v2.1 (Concise)
*Förbättrad version - praktiskt användbar*

---

## 🎯 KRITISKA FÖRBÄTTRINGAR vs Original

### 1. RESEARCH-FÖRST (VIKTIGAST!)

**FÖRE du skriver:**
```bash
# Kör dessa sökningar:
- "OpenAI GPT-4o pricing November 2025"
- "Claude Sonnet 4.5 pricing November 2025"
- "LangGraph 1.0 release November 2025"
- "AutoGen maintenance mode 2025"
- "AI agent security prompt injection 2025"
- "vector database benchmarks Pinecone Weaviate 2025"

# Verifiera:
✓ Alla priser från officiella källor
✓ Tool status (aktiv/maintenance/deprecated)
✓ Konkreta benchmarks med siffror
✓ Datum på all information
```

**Varför**: AI:s träningsdata är gammal. Online-sökning = aktuell info.

---

### 2. ANVÄND KONKRETA SIFFROR

❌ **FEL**: "Prompt caching kan spara pengar"
✅ **RÄTT**: "Prompt caching: $0.30 → $0.03 per request (90% besparing)"

❌ **FEL**: "GPT-4o är billigare"
✅ **RÄTT**: "GPT-4o: $2.50/$10 (83% billigare än GPT-4 Turbo: $10/$30)"

❌ **FEL**: "Pinecone är snabbt"
✅ **RÄTT**: "Pinecone p99: 47ms vs Weaviate: 123ms (vid 1B vectors)"

---

### 3. NYA OBLIGATORISKA SEKTIONER

#### A. Säkerhet (2000+ ord)

**Måste täcka:**
- Prompt injection: "Frontier, unsolved problem" (OpenAI CISO)
- EchoGram attack (Nov 2025): `"=coffee"` bypasses guardrails
- OpenAI Guardrails: Bypassade inom veckor (Okt 2025)
- 5 defense strategies MED KOD:
  1. Output-level controls
  2. Layered defenses (AWS Bedrock + custom)
  3. Human-in-the-loop (Vercel AI SDK 6)
  4. Structured testing
  5. Never trust agent output

#### B. Cost Optimization (1500+ ord)

**Måste inkludera:**
- **Prompt caching**: Konkret exempel med $0.30 → $0.03
- **Model routing**: Kod för billig→dyr fallback (60-80% savings)
- **Batch API**: 50% rabatt exempel
- **ROI calculations**: Före/efter cost comparisons

#### C. Observability (1000+ ord)

**Platform comparison:**
| Platform | Free Tier | Best For |
|----------|-----------|----------|
| LangSmith | 5K traces/mån | LangChain-heavy |
| Langfuse | 50K events/mån | Budget, open-source |
| Braintrust | Varies | TypeScript/JS |

**Include**: När välja vilken + implementation examples

#### D. Vector Databases (1000+ ord)

**Benchmarks (obligatoriskt!):**
- Pinecone: 47ms p99 @ 1B vectors → Production
- Weaviate: 123ms p99 @ 100M vectors → Medium scale
- Chroma: 89ms @ 10M vectors → Prototyping

**Migration pattern**: Chroma → Weaviate → Pinecone

#### E. Claude Agent SDK (1000+ ord)

**Cover:**
- CLAUDE.md files (auto-read by Claude!)
- Extended Thinking: "think" → "ultrathink"
- TDD best practices
- Security: Sandboxing requirements

---

### 4. UPPDATERA PRISER (November 2025)

```markdown
## LLM-priser (November 2025)

| Model | Input | Output | Use Case |
|-------|-------|--------|----------|
| GPT-4o | $2.50 | $10 | Standard |
| GPT-4o mini | $0.15 | $0.60 | Budget |
| Claude Sonnet 4.5 | $3 | $15 | Agents |
| Claude Haiku 4.5 | $0.8 | $4 | Cost/Performance |
| Gemini 2.0 Flash | $0.35 | $1.50 | High volume |

**Batch API**: 50% rabatt alla OpenAI
**Prompt Caching**: 90% rabatt på cached tokens
```

---

### 5. TOOL STATUS MARKERS

```markdown
| Tool | Status |
|------|--------|
| LangGraph 1.0 | ✅ Production-ready |
| AutoGen | ⚠️ **MAINTENANCE MODE** |
| Microsoft Agent Framework | 🆕 Replacement för AutoGen |
| Magentic-One | 🆕 Nov 2025 |
| Claude Agent SDK | 🆕 Renamed från "Claude Code" |
| Vercel AI SDK 6 | 🆕 Beta Okt 2025 |
```

---

### 6. ANTI-PATTERNS (Lägg till i varje nivå)

**Nivå 3**:
- ❌ Ingen max_iterations → infinite loops
- ❌ Hardkodade API keys
- ❌ Ingen error handling

**Nivå 4**:
- ❌ För stora chunks (>2000 tokens)
- ❌ Ingen hybrid search för RAG
- ❌ Ignorera prompt caching

**Nivå 5**:
- ❌ Lita på agent output utan validation (SÄKERHET!)
- ❌ Ingen observability i production
- ❌ Använd bara dyra modeller för allt

---

### 7. MIGRATION PATHS

**Document these transitions:**
- AutoGen → Microsoft Agent Framework / CrewAI / LangGraph
- Function Calling → Structured Outputs
- LangGraph Platform → LangSmith Deployment
- Chroma → Weaviate → Pinecone (vector DBs)

---

### 8. EXPANDED FAQ (30+ frågor)

**November 2025-specifika:**
```markdown
Q: Vilken modell ska jag välja November 2025?
A:
- Agents: Claude Sonnet 4.5 ($3/$15)
- Budget: Claude Haiku 4.5 ($0.8/$4) eller GPT-4o mini ($0.15/$0.60)
- High volume: Gemini 2.0 Flash ($0.35/$1.50)

Q: Hur mycket sparar jag med prompt caching?
A: 90% på cached tokens. Exempel: RAG 10K context:
   $0.30 → $0.03 per request

Q: AutoGen eller Microsoft Agent Framework?
A: AutoGen = maintenance mode. Använd Microsoft Agent Framework,
   CrewAI, eller LangGraph 1.0 för nya projekt.

Q: Är prompt injection olösligt?
A: Ja, enligt OpenAI CISO. EchoGram (Nov 2025) och andra
   attacks fortsätter bypassa guardrails. Använd layered defense.
```

---

### 9. PRE-PUBLISH CHECKLIST

**Essentials:**
- [ ] Alla priser verifierade från officiella källor?
- [ ] Datumstämplar på all 2025-info?
- [ ] AutoGen markerat som maintenance mode?
- [ ] LangGraph 1.0 nämnt som production-ready?
- [ ] Säkerhetssektion >= 1500 ord?
- [ ] Konkreta siffror i 70%+ av påståenden?
- [ ] Vector DB benchmarks inkluderade?
- [ ] Claude CLAUDE.md exempel?
- [ ] Model routing kod-exempel?
- [ ] Anti-patterns i varje nivå?

---

## 📋 ORIGINAL STRUKTUR (behåll denna!)

### 5 Nivåer (från original prompt)
1. Nivå 1: 5-åring (500 ord, 3 övningar)
2. Nivå 2: 10-åring (800 ord, 5 övningar)
3. Nivå 3: Gymnasiet (1500 ord, 7 övningar, 2 projekt)
4. Nivå 4: Universitet (2000 ord, 10 övningar, 2 projekt)
5. Nivå 5: Expert (2500 ord, 10 övningar, 2 projekt)

### Plattformar att täcka (från original)
- LangChain, LangGraph, AutoGen (⚠️), CrewAI
- OpenAI, Claude, Gemini
- n8n, Zapier, Flowise
- LlamaIndex, Haystack, DSPy

**PLUS lägg till:**
- Microsoft Agent Framework 🆕
- Magentic-One 🆕
- Vercel AI SDK 6 🆕
- Langfuse, LangSmith, Braintrust (observability)
- Amazon Nova (embeddings)

---

## ⚡ QUICK REFERENCE: Vad är nytt?

```markdown
PRISER (Nov 2025):
- GPT-4o: $2.50/$10 (83% cheaper!)
- Claude Haiku 4.5: $0.8/$4 (NEW!)
- Gemini 2.0 Flash: $0.35/$1.50 (NEW!)

TOOLS:
- LangGraph 1.0: Production-ready ✅
- AutoGen: Maintenance mode ⚠️
- Microsoft Agent Framework: Replacement 🆕
- Magentic-One: Multi-agent system 🆕

TECHNIQUES:
- Prompt caching: 90% savings
- Structured outputs > function calling
- Agentic chunking for RAG
- Model routing: 60-80% cost reduction

SECURITY:
- Prompt injection: Still unsolved
- EchoGram attack (Nov 2025)
- Defense: Layered approach required

OBSERVABILITY:
- LangSmith: 5K traces/mån
- Langfuse: 50K events/mån (open-source)
- Braintrust: Best for TS/JS
```

---

## 🎯 EXEMPEL: Apply These Learnings

### BEFORE (vague):
```markdown
**Q: Hur optimerar jag costs?**
A: Använd caching och billiga modeller när möjligt.
```

### AFTER (concrete):
```markdown
**Q: Hur optimerar jag costs? (November 2025)**
A: Tre strategier:

1. **Prompt Caching** (90% saving):
   ```python
   # Cache 10K context i RAG
   # Cost: $0.30 → $0.03 per request
   system=[{
       "text": large_context,
       "cache_control": {"type": "ephemeral"}
   }]
   ```

2. **Model Routing** (60-80% saving):
   ```python
   if simple_query:
       return gpt_4o_mini(query)  # $0.15/$0.60
   elif medium:
       return claude_haiku_45(query)  # $0.8/$4
   else:
       return claude_sonnet_45(query)  # $3/$15
   ```

3. **Batch API** (50% saving):
   - For non-urgent processing
   - OpenAI Batch API: 50% rabatt
```

---

## 📏 LENGTH TARGET

**Total guide:**
- ~22,000 ord (vs 20,000 original)
- 50+ övningar
- 30+ FAQ
- 6 projekt
- Konkreta siffror i 70%+ av påståenden

**Nya sektioner:**
- Säkerhet: 2000 ord
- Cost optimization: 1500 ord
- Observability: 1000 ord
- Vector DBs: 1000 ord
- Claude SDK: 1000 ord

**= +6500 ord av aktuell, research-baserad info**

---

## ✅ SUCCESS CRITERIA

Din guide är klar när:
- ✅ Alla priser från november 2025
- ✅ Konkreta siffror i 70%+ påståenden
- ✅ AutoGen markerat som maintenance mode
- ✅ Security sektion >= 1500 ord
- ✅ Vector DB benchmarks inkluderade
- ✅ Model routing kod-exempel
- ✅ CLAUDE.md exempel
- ✅ Migration paths dokumenterade
- ✅ 30+ FAQ med November 2025-fokus

---

**Version**: 2.1 Concise
**Längd**: ~300 rader (vs 2000 i v2.0)
**Användbar**: ✅ JA!
**Innehåller kritiska förbättringar**: ✅ JA!

**Use this instead of v2.0!**
