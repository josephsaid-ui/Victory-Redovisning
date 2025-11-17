# LangChain Medical Agent - Ögonsekreterare

## Arkitektur

```
┌─────────────────────────────────────────────────────┐
│  REAL-TIME TRANSCRIPTION STREAM                     │
│  "Patient klagar på suddig syn sedan 2 veckor..."   │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│  LANGCHAIN STREAMING AGENT                          │
│  ┌───────────────────────────────────────────┐     │
│  │  Agent Executor (Streaming)               │     │
│  │  • Tar emot transcription chunks          │     │
│  │  • Analyserar i realtid                   │     │
│  │  • Bestämmer vilka tools att använda      │     │
│  └───────────────────────────────────────────┘     │
│                                                      │
│  ┌───────────────────────────────────────────┐     │
│  │  TOOLS (Agent kan anropa dessa)           │     │
│  │  1. search_eye_diseases                   │     │
│  │  2. search_treatments                     │     │
│  │  3. search_medications                    │     │
│  │  4. suggest_anamnesis_questions           │     │
│  │  5. analyze_symptoms                      │     │
│  └───────────────────────────────────────────┘     │
└─────────────────┬───────────────────────────────────┘
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
┌───────────────┐   ┌──────────────────┐
│ LLAMAINDEX    │   │ CLAUDE API       │
│ RAG SYSTEM    │   │ • Reasoning      │
│ • Medical KB  │   │ • Question gen   │
│ • pgvector    │   │ • Analysis       │
└───────────────┘   └──────────────────┘
        │
        ▼
┌──────────────────────────────────────┐
│  REAL-TIME OUTPUT                    │
│  • Hittade sjukdomar: [Katarakt]    │
│  • Förslag behandling: [Operation]   │
│  • Anamnes frågor:                   │
│    - Ser du halos runt lampor?      │
│    - Har du svårt att köra bil?     │
└──────────────────────────────────────┘
```

## Projektstruktur

```
langchain-medical-agent/
├── src/
│   ├── agent/
│   │   ├── medical-agent.ts          # Huvud-agent
│   │   ├── streaming-agent.ts        # Real-time streaming
│   │   └── agent-config.ts           # Agent configuration
│   │
│   ├── tools/
│   │   ├── search-diseases.tool.ts   # Sök ögonsjukdomar
│   │   ├── search-treatments.tool.ts # Sök behandlingar
│   │   ├── search-medications.tool.ts # Sök läkemedel
│   │   ├── anamnesis.tool.ts         # Generera frågor
│   │   └── symptoms.tool.ts          # Analysera symptom
│   │
│   ├── memory/
│   │   ├── conversation-memory.ts    # Minns kontext
│   │   └── medical-context.ts        # Medical kontext
│   │
│   ├── prompts/
│   │   ├── system-prompts.ts         # System prompts
│   │   └── ophthalmology-prompt.ts   # Ögonspecifika prompts
│   │
│   ├── rag/
│   │   └── llamaindex-integration.ts # LlamaIndex RAG
│   │
│   └── types/
│       └── medical.types.ts          # TypeScript types
│
├── examples/
│   └── real-time-example.ts          # Användningsexempel
│
└── package.json
```

## Features

### 1. Real-time Streaming Agent
- Tar emot transcription chunks i realtid
- Analyserar kontinuerligt under samtalet
- Streamar suggestions tillbaka till UI

### 2. Medical Knowledge Tools
- Söker ögonsjukdomar baserat på symptom
- Hittar behandlingar och läkemedel
- Använder LlamaIndex RAG för svensk medicinsk data

### 3. Intelligent Anamnesis Questions
- Genererar relevanta följdfrågor
- Baserat på kontext och redan nämnda symptom
- Ögonspecifika frågor

### 4. Context-Aware
- Minns hela samtalet
- Bygger upp patient-kontext
- Undviker att upprepa frågor

## Installation

```bash
npm install langchain @langchain/anthropic @langchain/core
npm install llamaindex zod
npm install @supabase/supabase-js
```

## Quick Start

```typescript
import { MedicalAgent } from './src/agent/medical-agent';

const agent = new MedicalAgent({
  llm: 'claude-3-5-sonnet-20241022',
  streaming: true
});

// Stream transcription chunks
agent.processTranscription('Patient klagar på suddig syn...');

// Get real-time suggestions
agent.on('suggestion', (suggestion) => {
  console.log(suggestion);
});
```
