# Medical AI Agent - Python + FastAPI

**En komplett LangChain-baserad medicinsk AI-agent för ögonsekreterare**

> 🐍 Python-version med FastAPI - Optimerad för AI/ML workloads

## ✨ Varför Python-versionen?

- ✅ **Bättre AI/ML Support** - LangChain, LlamaIndex är Python-first
- ✅ **Medicinsk NLP** - PubMedBERT, BioBERT, medspaCy
- ✅ **Snabbare Development** - Jupyter notebooks, lättare experimentation
- ✅ **Bättre Performance** - Native ML libraries (NumPy, PyTorch)
- ✅ **Större Community** - Mer resurser för medical AI

## 🚀 Features

### 1. Real-time Streaming Agent
- Tar emot transcription chunks i realtid
- Analyserar kontinuerligt under samtalet
- Streamar suggestions tillbaka till frontend via WebSocket

### 2. Medical Knowledge Tools
- **search_eye_diseases**: Söker ögonsjukdomar med RAG
- **search_treatments**: Hittar behandlingsalternativ
- **suggest_anamnesis_questions**: Genererar smarta följdfrågor

### 3. RAG System (LlamaIndex)
- Svensk medicinsk kunskapsbas (ögonsjukdomar)
- Vector search med pgvector
- PubMedBERT embeddings för medical terminologi

### 4. Context-Aware
- Håller koll på symptom, diagnoser, läkemedel
- Undviker att upprepa frågor
- Bygger upp patient-kontext

### 5. Journal Generation
- Genererar strukturerad journaltext (SOAP-format)
- ICD-10, KVÅ, ATC-koder
- Svensk medicinsk terminologi

## 📦 Installation

### Förutsättningar
```bash
python >= 3.11
pip eller poetry
```

### Installera dependencies
```bash
cd medical-agent-python
pip install -r requirements.txt
```

### Setup environment
```bash
cp .env.example .env
# Lägg till API keys
```

## 🎯 Quick Start

### Basic Usage
```python
from app.agents.medical_agent import MedicalAgent

# Skapa agent
agent = MedicalAgent()
await agent.initialize()

# Processa transcription
suggestions = await agent.process_transcription(
    "Patient klagar på suddig syn sedan 2 veckor..."
)

# Generera journal
journal = await agent.generate_journal_entry()
print(journal)
```

### Streaming Usage
```python
from app.agents.streaming_agent import StreamingMedicalAgent

# Skapa streaming agent
agent = StreamingMedicalAgent()
await agent.initialize()

# Lyssna på events
@agent.on("suggestion")
async def handle_suggestion(suggestion):
    print(f"New suggestion: {suggestion}")

# Starta streaming
await agent.start_streaming()

# Lägg till chunks
agent.add_transcription_chunk("Patient klagar på suddig syn...")
```

### Run FastAPI Server
```bash
# Development
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 📁 Projekt Struktur

```
medical-agent-python/
├── app/
│   ├── main.py                      # FastAPI application
│   ├── agents/
│   │   ├── medical_agent.py         # Core agent logic
│   │   └── streaming_agent.py       # Real-time streaming
│   ├── tools/
│   │   ├── search_diseases.py       # Sök ögonsjukdomar
│   │   ├── search_treatments.py     # Sök behandlingar
│   │   └── anamnesis.py             # Generera frågor
│   ├── rag/
│   │   └── llamaindex_rag.py        # RAG integration
│   ├── models/
│   │   └── medical_types.py         # Pydantic models
│   ├── prompts/
│   │   └── ophthalmology.py         # Expert prompts
│   └── memory/
│       └── medical_context.py       # Context manager
├── examples/
│   ├── basic_example.py
│   ├── streaming_example.py
│   └── integration_example.py
├── tests/
│   └── test_agent.py
├── requirements.txt
├── .env.example
└── README.md
```

## 🔌 API Endpoints

### WebSocket
```
ws://localhost:8000/ws/{session_id}
```

### REST Endpoints
```
POST   /sessions/start          - Starta ny session
POST   /sessions/{id}/end       - Avsluta session
POST   /sessions/{id}/journal   - Generera journal
GET    /sessions/{id}/context   - Hämta context
```

## 🧪 Run Examples

```bash
# Basic example
python examples/basic_example.py

# Streaming example
python examples/streaming_example.py

# Full integration
python examples/integration_example.py
```

## 🔧 API Keys

Du behöver:
- **Anthropic Claude API** - https://console.anthropic.com/
- **Supabase** - https://supabase.com/
- **AssemblyAI** (optional) - https://www.assemblyai.com/

## 📚 Documentation

Se [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) för:
- Detaljerad installation
- API integration
- Deployment instruktioner
- Troubleshooting
- Best practices

## 🆚 Python vs TypeScript Version

| Feature | Python | TypeScript |
|---------|--------|------------|
| AI/ML Libraries | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Medical NLP | ⭐⭐⭐⭐⭐ | ⭐ |
| Development Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Type Safety | ⭐⭐⭐⭐ (Pydantic) | ⭐⭐⭐⭐⭐ |
| Performance (AI) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**Rekommendation:** Python för medical AI applications!

## 📄 License

MIT

## 🤝 Contributing

Contributions welcome! Se CONTRIBUTING.md

## 📞 Support

- Issues: GitHub Issues
- Email: [din email]
