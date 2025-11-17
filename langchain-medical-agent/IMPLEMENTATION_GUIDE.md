# LangChain Medical Agent - Implementation Guide

## 📋 Innehåll

1. [Översikt](#översikt)
2. [Installation](#installation)
3. [Konfiguration](#konfiguration)
4. [Användning](#användning)
5. [Arkitektur](#arkitektur)
6. [API Integration](#api-integration)
7. [Deployment](#deployment)
8. [Troubleshooting](#troubleshooting)

---

## Översikt

LangChain Medical Agent är kärnan i ögonsekreterare-appen. Den:

- ✅ Analyserar transkriberad text i realtid
- ✅ Identifierar ögonsjukdomar med RAG (LlamaIndex)
- ✅ Föreslår behandlingar
- ✅ Genererar intelligenta anamnesfrågor
- ✅ Streamar suggestions till frontend
- ✅ Genererar strukturerad journaltext

---

## Installation

### 1. Förutsättningar

```bash
node >= 18.0.0
npm eller yarn
```

### 2. Installera dependencies

```bash
cd langchain-medical-agent
npm install
```

### 3. Setup environment variables

```bash
cp .env.example .env
# Redigera .env med dina API-nycklar
```

### 4. API-nycklar du behöver

#### Anthropic Claude (REQUIRED)
1. Gå till https://console.anthropic.com/
2. Skapa account
3. Generera API key
4. Lägg till i .env: `ANTHROPIC_API_KEY=sk-ant-xxx`

#### Supabase (REQUIRED)
1. Gå till https://supabase.com/
2. Skapa nytt projekt
3. Hämta URL och keys från Settings → API
4. Lägg till i .env

#### AssemblyAI (REQUIRED för transcription)
1. Gå till https://www.assemblyai.com/
2. Skapa account
3. Hämta API key
4. Lägg till i .env: `ASSEMBLYAI_API_KEY=xxx`

---

## Konfiguration

### Supabase Database Setup

Kör följande SQL i Supabase SQL Editor:

```sql
-- 1. Enable UUID extension
create extension if not exists "uuid-ossp";

-- 2. Patient Sessions
create table patient_sessions (
  id uuid primary key default uuid_generate_v4(),
  user_id text not null,
  started_at timestamp with time zone not null,
  ended_at timestamp with time zone,
  status text not null check (status in ('active', 'completed', 'cancelled')),
  created_at timestamp with time zone default now()
);

-- 3. Journal Entries
create table journal_entries (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  content text not null,
  generated_at timestamp with time zone not null,
  edited_content text,
  created_at timestamp with time zone default now()
);

-- 4. Agent Suggestions
create table agent_suggestions (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  type text not null,
  content jsonb not null,
  confidence decimal(3,2),
  created_at timestamp with time zone default now()
);

-- 5. Transcriptions
create table transcriptions (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  text text not null,
  timestamp timestamp with time zone default now()
);

-- 6. Enable pgvector for RAG
create extension if not exists vector;

-- 7. Medical Knowledge Base
create table medical_documents (
  id uuid primary key default uuid_generate_v4(),
  type text not null check (type in ('disease', 'treatment', 'medication')),
  name text not null,
  content text not null,
  metadata jsonb,
  embedding vector(1536),
  created_at timestamp with time zone default now()
);

-- 8. Index för vector search
create index on medical_documents using ivfflat (embedding vector_cosine_ops);

-- 9. Row Level Security
alter table patient_sessions enable row level security;
alter table journal_entries enable row level security;
alter table agent_suggestions enable row level security;
alter table transcriptions enable row level security;

-- 10. Policies (exempel - anpassa för din auth)
create policy "Users can view own sessions"
  on patient_sessions for select
  using (auth.uid()::text = user_id);

create policy "Users can view own journals"
  on journal_entries for select
  using (
    session_id in (
      select id from patient_sessions where user_id = auth.uid()::text
    )
  );
```

---

## Användning

### Basic Usage

```typescript
import { MedicalAgent } from './src/agent/medical-agent';

// 1. Skapa agent
const agent = new MedicalAgent();

// 2. Initialisera (laddar RAG knowledge base)
await agent.initialize();

// 3. Processa transcription
const suggestions = await agent.processTranscription(
  "Patient klagar på suddig syn sedan 2 veckor..."
);

// 4. Hämta context
const context = agent.getContext();

// 5. Generera journal
const journal = await agent.generateJournalEntry();
```

### Streaming Usage (Real-time)

```typescript
import { StreamingMedicalAgent } from './src/agent/streaming-agent';

// 1. Skapa streaming agent
const agent = new StreamingMedicalAgent();
await agent.initialize();

// 2. Lyssna på events
agent.on('suggestion', (suggestion) => {
  console.log('New suggestion:', suggestion);
  // Skicka till frontend via WebSocket
});

agent.on('context_update', (context) => {
  console.log('Context updated:', context);
});

// 3. Starta streaming
agent.startStreaming(2000); // Process var 2:a sekund

// 4. Lägg till transcription chunks (från AssemblyAI)
agent.addTranscriptionChunk('Patient klagar på');
agent.addTranscriptionChunk('suddig syn');
// ... mer chunks

// 5. Stoppa när klar
agent.stopStreaming();
```

### Kör Exempel

```bash
# Basic example
npm run example:basic

# Streaming example
npm run example:streaming

# Full integration example
npm run example:integration
```

---

## Arkitektur

### Component Overview

```
┌─────────────────────────────────────────┐
│  StreamingMedicalAgent                  │
│  (Event Emitter)                        │
│  • Tar emot transcription chunks        │
│  • Emiterar suggestions i realtid       │
└────────────┬────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────┐
│  MedicalAgent                           │
│  (Core Agent Logic)                     │
│  • AgentExecutor (LangChain)            │
│  • Context Management                   │
│  • Journal Generation                   │
└────┬───────────┬────────────────────────┘
     │           │
     ▼           ▼
┌─────────┐  ┌──────────────────────────┐
│ TOOLS   │  │  MedicalContextManager   │
└─────────┘  └──────────────────────────┘
     │
     ├─→ search_eye_diseases
     ├─→ search_treatments
     └─→ suggest_anamnesis_questions
         │
         ▼
    ┌──────────────────┐
    │ LlamaIndex RAG   │
    │ • Medical KB     │
    │ • pgvector       │
    └──────────────────┘
```

### Data Flow

```
1. Audio Recording (React Native)
   ↓
2. AssemblyAI Transcription (WebSocket)
   ↓
3. Backend receives chunks
   ↓
4. StreamingMedicalAgent.addTranscriptionChunk()
   ↓
5. Agent processes (var 2s)
   ↓
6. Tools körs (RAG search, question generation)
   ↓
7. Suggestions emiteras
   ↓
8. Backend → WebSocket → Frontend
   ↓
9. UI uppdateras i realtid
```

---

## API Integration

### AssemblyAI Integration

```typescript
import { AssemblyAI } from 'assemblyai';

const client = new AssemblyAI({
  apiKey: process.env.ASSEMBLYAI_API_KEY!,
});

// Real-time transcription
const transcriber = client.realtime.transcriber({
  sampleRate: 16000,
});

transcriber.on('transcript', (transcript) => {
  if (transcript.message_type === 'PartialTranscript') {
    // Skicka till agent
    agent.addTranscriptionChunk(transcript.text);
  }
});

// Connect audio stream
transcriber.connect();
audioStream.pipe(transcriber);
```

### WebSocket Backend

```typescript
import { WebSocketServer } from 'ws';

const wss = new WebSocketServer({ port: 8080 });

wss.on('connection', (ws) => {
  // När agent genererar suggestion
  agent.on('suggestion', (suggestion) => {
    ws.send(JSON.stringify({
      type: 'suggestion',
      data: suggestion
    }));
  });

  // Ta emot från frontend
  ws.on('message', (data) => {
    const message = JSON.parse(data);

    if (message.type === 'transcription_chunk') {
      agent.addTranscriptionChunk(message.text);
    }
  });
});
```

### React Native Frontend

```typescript
// useWebSocket hook
import { useEffect, useState } from 'react';

export function useWebSocket(url: string) {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    const socket = new WebSocket(url);

    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);

      if (message.type === 'suggestion') {
        setSuggestions(prev => [...prev, message.data]);
      }
    };

    setWs(socket);
    return () => socket.close();
  }, [url]);

  return { ws, suggestions };
}

// Använd i komponent
function ConsultationScreen() {
  const { ws, suggestions } = useWebSocket('ws://localhost:8080');

  return (
    <View>
      {suggestions.map((s, i) => (
        <SuggestionCard key={i} suggestion={s} />
      ))}
    </View>
  );
}
```

---

## Deployment

### Development

```bash
# Kör lokalt
npm run dev
```

### Production

#### Option 1: Supabase Edge Functions

```bash
# Deploy agent som Supabase Edge Function
supabase functions deploy medical-agent
```

#### Option 2: Docker

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY . .

RUN npm run build

EXPOSE 8080

CMD ["node", "dist/examples/integration-example.js"]
```

```bash
docker build -t medical-agent .
docker run -p 8080:8080 --env-file .env medical-agent
```

#### Option 3: Railway/Render

1. Push till GitHub
2. Connect repo till Railway/Render
3. Sätt environment variables
4. Deploy

---

## Troubleshooting

### Problem: RAG returnerar inga resultat

**Lösning:** Kontrollera att medical knowledge base är initialiserad

```typescript
// Kolla om RAG är initialiserad
await medicalRAG.initialize();

// Testa sökning
const results = await medicalRAG.searchDiseases(['suddig syn']);
console.log('Results:', results);
```

### Problem: Agent använder inte tools

**Lösning:** Kontrollera tool descriptions och prompts

```typescript
// Öka verbose för debugging
const agent = new MedicalAgent({
  verbose: true // Se alla tool calls
});
```

### Problem: Transcription chunks saknas

**Lösning:** Kontrollera WebSocket connection

```typescript
// Lägg till logging
agent.on('transcription_update', (data) => {
  console.log('Chunk received:', data.chunk);
});
```

### Problem: Låg performance

**Lösning:**

1. Öka processing interval
```typescript
agent.startStreaming(5000); // 5 sekunder istället för 2
```

2. Använd Haiku för snabbare svar
```typescript
const agent = new MedicalAgent({
  modelName: 'claude-3-haiku-20240307' // Snabbare, billigare
});
```

3. Cacha RAG results
```typescript
// Implementera caching i LlamaIndex
```

---

## Best Practices

### 1. Error Handling

```typescript
agent.on('error', async (error) => {
  // Logga error
  console.error('Agent error:', error);

  // Notifiera användare
  notifyUser('Ett fel uppstod. Försök igen.');

  // Spara error i databas
  await supabase.from('errors').insert({
    type: 'agent_error',
    message: error.message,
    timestamp: new Date()
  });
});
```

### 2. Context Cleanup

```typescript
// Reset context mellan sessioner
agent.on('session_end', () => {
  agent.reset();
});
```

### 3. Rate Limiting

```typescript
// Begränsa antal requests till Claude
import { RateLimiter } from 'limiter';

const limiter = new RateLimiter({
  tokensPerInterval: 50,
  interval: 'minute'
});

await limiter.removeTokens(1);
await agent.processTranscription(text);
```

### 4. Monitoring

```typescript
// Använd Sentry för error tracking
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
});

// Wrap agent i try-catch
try {
  await agent.processTranscription(text);
} catch (error) {
  Sentry.captureException(error);
  throw error;
}
```

---

## Next Steps

1. ✅ Implementera fler tools (search_medications, analyze_symptoms)
2. ✅ Lägg till unit tests
3. ✅ Optimera RAG med fler medicinska dokument
4. ✅ Implementera caching
5. ✅ Lägg till monitoring och metrics

---

## Support

- GitHub Issues: [länk]
- Documentation: [länk]
- Email: [din email]
