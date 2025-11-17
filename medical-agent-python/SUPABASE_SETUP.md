# Supabase Database Setup Guide

Komplett guide för att sätta upp Supabase database med pgvector för Medical AI Agent.

## 📋 Innehåll

1. [Skapa Supabase Projekt](#steg-1-skapa-supabase-projekt)
2. [Konfigurera Database](#steg-2-konfigurera-database)
3. [Skapa Database Schema](#steg-3-skapa-database-schema)
4. [Setup pgvector](#steg-4-setup-pgvector-för-rag)
5. [Row Level Security (GDPR)](#steg-5-row-level-security-rls)
6. [Konfigurera App](#steg-6-konfigurera-app)
7. [Testa Anslutning](#steg-7-testa-anslutning)
8. [Backup & Maintenance](#steg-8-backup--maintenance)

---

## Steg 1: Skapa Supabase Projekt

### 1.1 Sign Up

1. Gå till https://supabase.com/
2. Klicka "Start your project"
3. Sign up med GitHub (rekommenderat för Git integration)

### 1.2 Skapa Nytt Projekt

1. Klicka "New Project"
2. Fyll i:
   - **Name:** `medical-agent-prod`
   - **Database Password:** Generera stark password (spara denna!)
   - **Region:** `North EU (Stockholm)` eller `West EU (Frankfurt)` för GDPR
   - **Pricing Plan:**
     - **Free Tier:** Bra för development/testing (500MB database, 2GB bandwidth)
     - **Pro ($25/mån):** Rekommenderat för production (8GB database, 50GB bandwidth)

3. Klicka "Create new project"
4. Vänta ~2 minuter medan projektet sätts upp

### 1.3 Hämta Connection Details

När projektet är klart:

1. Gå till **Settings** → **Database**
2. Spara följande information:

```bash
# Connection string
postgres://postgres:[YOUR-PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres

# Connection pooling (rekommenderat för production)
postgres://postgres.[PROJECT-REF]:[YOUR-PASSWORD]@aws-0-eu-north-1.pooler.supabase.com:6543/postgres
```

3. Gå till **Settings** → **API**
4. Spara API credentials:

```bash
Project URL: https://[PROJECT-REF].supabase.co
anon public key: eyJhbGc...
service_role key: eyJhbGc... (Hemlig! Använd endast på backend)
```

---

## Steg 2: Konfigurera Database

### 2.1 Öppna SQL Editor

1. I Supabase dashboard → **SQL Editor**
2. Klicka "New query"

### 2.2 Enable Required Extensions

Kör följande SQL:

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable pgvector för RAG embeddings
CREATE EXTENSION IF NOT EXISTS vector;

-- Enable pg_trgm för text search
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Verify extensions
SELECT * FROM pg_extension;
```

**Expected output:**
```
uuid-ossp | pgvector | pg_trgm
```

---

## Steg 3: Skapa Database Schema

### 3.1 Core Tables

Kör följande SQL för att skapa alla tabeller:

```sql
-- ============================================================================
-- PATIENT SESSIONS
-- ============================================================================
CREATE TABLE patient_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id TEXT NOT NULL,
    started_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    ended_at TIMESTAMP WITH TIME ZONE,
    status TEXT NOT NULL CHECK (status IN ('active', 'completed', 'cancelled')) DEFAULT 'active',

    -- Metadata
    patient_age INTEGER,
    patient_gender TEXT,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index för snabbare queries
CREATE INDEX idx_patient_sessions_user_id ON patient_sessions(user_id);
CREATE INDEX idx_patient_sessions_status ON patient_sessions(status);
CREATE INDEX idx_patient_sessions_started_at ON patient_sessions(started_at DESC);

-- Update timestamp trigger
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_patient_sessions_updated_at
    BEFORE UPDATE ON patient_sessions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- TRANSCRIPTIONS
-- ============================================================================
CREATE TABLE transcriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Transcription data
    text TEXT NOT NULL,
    chunk_index INTEGER NOT NULL DEFAULT 0,
    is_final BOOLEAN DEFAULT false,

    -- Speaker identification (optional)
    speaker TEXT, -- 'doctor' or 'patient'

    -- Timestamps
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index
CREATE INDEX idx_transcriptions_session_id ON transcriptions(session_id);
CREATE INDEX idx_transcriptions_timestamp ON transcriptions(timestamp);

-- ============================================================================
-- JOURNAL ENTRIES
-- ============================================================================
CREATE TABLE journal_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Journal content
    content TEXT NOT NULL,
    generated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    -- Structured sections (JSONB)
    sections JSONB DEFAULT '{}'::jsonb,
    -- Example: {"aktuellt": "...", "status": "...", "bedömning": "...", "planering": "..."}

    -- Editing
    edited_content TEXT,
    edited_at TIMESTAMP WITH TIME ZONE,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index
CREATE INDEX idx_journal_entries_session_id ON journal_entries(session_id);
CREATE INDEX idx_journal_entries_generated_at ON journal_entries(generated_at DESC);

-- Update trigger
CREATE TRIGGER update_journal_entries_updated_at
    BEFORE UPDATE ON journal_entries
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- AGENT SUGGESTIONS
-- ============================================================================
CREATE TABLE agent_suggestions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Suggestion data
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'question', 'analysis')),
    content JSONB NOT NULL,
    confidence DECIMAL(3,2) CHECK (confidence >= 0 AND confidence <= 1),

    -- User interaction
    accepted BOOLEAN,
    dismissed BOOLEAN DEFAULT false,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index
CREATE INDEX idx_agent_suggestions_session_id ON agent_suggestions(session_id);
CREATE INDEX idx_agent_suggestions_type ON agent_suggestions(type);
CREATE INDEX idx_agent_suggestions_created_at ON agent_suggestions(created_at);

-- ============================================================================
-- MEDICAL CONTEXT (per session)
-- ============================================================================
CREATE TABLE medical_contexts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL UNIQUE REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Context data (JSONB för flexibilitet)
    symptoms JSONB DEFAULT '[]'::jsonb,
    suspected_diseases JSONB DEFAULT '[]'::jsonb,
    current_medications JSONB DEFAULT '[]'::jsonb,
    asked_questions JSONB DEFAULT '[]'::jsonb,
    medical_history JSONB DEFAULT '[]'::jsonb,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Index
CREATE INDEX idx_medical_contexts_session_id ON medical_contexts(session_id);

-- Update trigger
CREATE TRIGGER update_medical_contexts_updated_at
    BEFORE UPDATE ON medical_contexts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

### 3.2 Verifiera Tables

```sql
-- Lista alla tabeller
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
```

**Expected output:**
```
patient_sessions
transcriptions
journal_entries
agent_suggestions
medical_contexts
```

---

## Steg 4: Setup pgvector för RAG

### 4.1 Skapa Medical Documents Table

```sql
-- ============================================================================
-- MEDICAL DOCUMENTS (för RAG knowledge base)
-- ============================================================================
CREATE TABLE medical_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Document metadata
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'protocol')),
    name TEXT NOT NULL,

    -- Content
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,

    -- Vector embedding (1536 dimensions för OpenAI embeddings)
    -- Använd 768 för PubMedBERT
    embedding vector(768),

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vector similarity search index (HNSW för bästa performance)
CREATE INDEX ON medical_documents
USING hnsw (embedding vector_cosine_ops);

-- Index för metadata queries
CREATE INDEX idx_medical_documents_type ON medical_documents(type);
CREATE INDEX idx_medical_documents_name ON medical_documents(name);
CREATE INDEX idx_medical_documents_metadata ON medical_documents USING GIN (metadata);

-- Full-text search index
CREATE INDEX idx_medical_documents_content ON medical_documents USING GIN (to_tsvector('swedish', content));

-- Update trigger
CREATE TRIGGER update_medical_documents_updated_at
    BEFORE UPDATE ON medical_documents
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

### 4.2 Populera Medical Knowledge Base

```sql
-- Insert exempel-sjukdomar (vi kan lägga till embeddings senare)
INSERT INTO medical_documents (type, name, content, metadata) VALUES
(
    'disease',
    'Katarakt (Grå starr)',
    'Katarakt är en grumling av ögats lins som leder till gradvis synförsämring. Vanliga symptom inkluderar suddig syn, halos runt lampor, svårt att köra bil i mörker, och färger som verkar blekare. Främst äldre över 60 år. Behandling: Kataraktoperation med inläggning av konstgjord lins (IOL). KVÅ: CJE00',
    '{"icd10": "H25-H28", "age_group": "främst äldre >60 år", "symptoms": ["suddig syn", "halos runt lampor", "gradvis synförsämring"]}'::jsonb
),
(
    'disease',
    'Glaukom (Grön starr)',
    'Glaukom är progressiv skada på synnerven, ofta kopplad till förhöjt ögontryck. Kan leda till permanent synförlust om obehandlad. Symptom: synfältsbortfall (perifer syn först), förhöjt ögontryck, ofta symtomfritt tidigt. Behandling: Ögondroppar (trycknedsättande), laserbehandling (SLT), kirurgi (trabekulektomi KVÅ: CJD00)',
    '{"icd10": "H40-H42", "age_group": "främst >40 år", "symptoms": ["synfältsbortfall", "förhöjt ögontryck", "tunnelseende"]}'::jsonb
),
(
    'disease',
    'Åldersrelaterad Makuladegeneration (AMD)',
    'AMD är degeneration av makula (gula fläcken) som ger central synförlust. Finns i torr och våt form. Symptom: böjda linjer (Amsler grid), central synförlust, svårt att läsa, förvrängd syn. Behandling: Våt AMD: Anti-VEGF injektioner (KVÅ: CJB10). Torr AMD: Kosttillskott (AREDS2), rökstopp',
    '{"icd10": "H35.3", "age_group": ">50 år, mest >65 år", "symptoms": ["böjda linjer", "central synförlust", "svårt att läsa"]}'::jsonb
);

-- Verify
SELECT name, type, metadata->>'icd10' as icd10
FROM medical_documents;
```

### 4.3 Vector Search Function

```sql
-- Function för vector similarity search
CREATE OR REPLACE FUNCTION search_similar_documents(
    query_embedding vector(768),
    match_threshold float DEFAULT 0.7,
    match_count int DEFAULT 5,
    filter_type text DEFAULT NULL
)
RETURNS TABLE (
    id uuid,
    name text,
    content text,
    type text,
    metadata jsonb,
    similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        medical_documents.id,
        medical_documents.name,
        medical_documents.content,
        medical_documents.type,
        medical_documents.metadata,
        1 - (medical_documents.embedding <=> query_embedding) as similarity
    FROM medical_documents
    WHERE
        (filter_type IS NULL OR medical_documents.type = filter_type)
        AND (1 - (medical_documents.embedding <=> query_embedding)) > match_threshold
    ORDER BY medical_documents.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;
```

---

## Steg 5: Row Level Security (RLS)

För GDPR-compliance måste vi säkerställa att användare endast kan se sin egen data.

### 5.1 Enable RLS

```sql
-- Enable RLS på alla tabeller med user data
ALTER TABLE patient_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE transcriptions ENABLE ROW LEVEL SECURITY;
ALTER TABLE journal_entries ENABLE ROW LEVEL SECURITY;
ALTER TABLE agent_suggestions ENABLE ROW LEVEL SECURITY;
ALTER TABLE medical_contexts ENABLE ROW LEVEL SECURITY;

-- Medical documents är public knowledge - ingen RLS
```

### 5.2 Skapa RLS Policies

```sql
-- ============================================================================
-- PATIENT SESSIONS POLICIES
-- ============================================================================

-- Users can only view their own sessions
CREATE POLICY "Users can view own sessions"
    ON patient_sessions FOR SELECT
    USING (auth.uid()::text = user_id);

-- Users can create sessions
CREATE POLICY "Users can create own sessions"
    ON patient_sessions FOR INSERT
    WITH CHECK (auth.uid()::text = user_id);

-- Users can update their own sessions
CREATE POLICY "Users can update own sessions"
    ON patient_sessions FOR UPDATE
    USING (auth.uid()::text = user_id);

-- ============================================================================
-- TRANSCRIPTIONS POLICIES
-- ============================================================================

CREATE POLICY "Users can view own transcriptions"
    ON transcriptions FOR SELECT
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can insert own transcriptions"
    ON transcriptions FOR INSERT
    WITH CHECK (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

-- ============================================================================
-- JOURNAL ENTRIES POLICIES
-- ============================================================================

CREATE POLICY "Users can view own journals"
    ON journal_entries FOR SELECT
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can create own journals"
    ON journal_entries FOR INSERT
    WITH CHECK (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can update own journals"
    ON journal_entries FOR UPDATE
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

-- ============================================================================
-- AGENT SUGGESTIONS POLICIES
-- ============================================================================

CREATE POLICY "Users can view own suggestions"
    ON agent_suggestions FOR SELECT
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can insert own suggestions"
    ON agent_suggestions FOR INSERT
    WITH CHECK (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

-- ============================================================================
-- MEDICAL CONTEXTS POLICIES
-- ============================================================================

CREATE POLICY "Users can view own context"
    ON medical_contexts FOR SELECT
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can create own context"
    ON medical_contexts FOR INSERT
    WITH CHECK (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );

CREATE POLICY "Users can update own context"
    ON medical_contexts FOR UPDATE
    USING (
        session_id IN (
            SELECT id FROM patient_sessions WHERE user_id = auth.uid()::text
        )
    );
```

### 5.3 Service Role Bypass

Backend använder `service_role` key som bypasses RLS automatiskt.

---

## Steg 6: Konfigurera App

### 6.1 Hämta Credentials

Från Supabase dashboard → Settings → API:

```bash
SUPABASE_URL=https://[PROJECT-REF].supabase.co
SUPABASE_ANON_KEY=eyJhbGc... (för frontend)
SUPABASE_SERVICE_KEY=eyJhbGc... (för backend - HEMLIG!)
```

### 6.2 Uppdatera .env

```bash
# medical-agent-python/.env
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_DB_PASSWORD=your-database-password
```

### 6.3 Test Connection

```python
# test_supabase.py
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

# Test query
result = supabase.table("medical_documents").select("*").limit(5).execute()
print(f"Found {len(result.data)} documents")
```

```bash
python test_supabase.py
```

---

## Steg 7: Testa Anslutning

### 7.1 Från Python App

```python
# examples/test_database.py
import asyncio
from dotenv import load_dotenv
from app.rag.llamaindex_rag import medical_rag

load_dotenv()

async def test_database():
    print("Testing Supabase connection...")

    # Initialize RAG (will connect to Supabase)
    await medical_rag.initialize()
    print("✅ RAG initialized")

    # Test vector search
    diseases = await medical_rag.search_diseases(["suddig syn", "halos"])
    print(f"✅ Found {len(diseases)} diseases")

    print("\n✅ All tests passed!")

if __name__ == "__main__":
    asyncio.run(test_database())
```

```bash
python examples/test_database.py
```

### 7.2 Från Supabase Dashboard

1. Gå till **Table Editor**
2. Välj `medical_documents`
3. Du bör se de 3 sjukdomar vi lade till
4. Försök lägg till en rad manuellt

### 7.3 Vector Search Test

```sql
-- Test vector search (utan embeddings än)
SELECT name, type
FROM medical_documents
WHERE type = 'disease';
```

---

## Steg 8: Backup & Maintenance

### 8.1 Automatic Backups

Supabase Pro inkluderar:
- **Daily backups** (retained 7 days)
- **Point-in-time recovery** (up to 7 days)

Aktivera i: **Settings** → **Database** → **Backups**

### 8.2 Manual Backup

```bash
# Från command line
pg_dump "postgres://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres" > backup.sql

# Restore
psql "postgres://postgres:[PASSWORD]@db.[PROJECT-REF].supabase.co:5432/postgres" < backup.sql
```

### 8.3 Database Monitoring

1. **Supabase Dashboard** → **Reports**
   - Query performance
   - Table sizes
   - Connection stats

2. **Enable Realtime** (optional)
   - **Database** → **Replication**
   - Enable för tabeller du vill ha realtime updates på

### 8.4 Maintenance Tasks

```sql
-- Vacuum analyze (run monthly)
VACUUM ANALYZE;

-- Reindex (if queries slow down)
REINDEX TABLE medical_documents;

-- Check table sizes
SELECT
    table_name,
    pg_size_pretty(pg_total_relation_size(quote_ident(table_name))) as size
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY pg_total_relation_size(quote_ident(table_name)) DESC;
```

---

## Nästa Steg

✅ Database är nu setup!

**Du kan nu:**

1. **Köra app lokalt** mot Supabase
   ```bash
   python examples/basic_example.py
   ```

2. **Deploy backend** (se [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md))

3. **Lägg till fler medicinska dokument** i `medical_documents`

4. **Generera embeddings** för RAG:
   ```python
   # Kommer automatiskt när du kör agent.initialize()
   ```

---

## Troubleshooting

### Problem: "relation does not exist"

**Lösning:** Kör SQL queries igen i SQL Editor

### Problem: "permission denied"

**Lösning:**
- Använd `service_role` key (inte `anon` key) från backend
- Check RLS policies

### Problem: Vector search returnerar inga resultat

**Lösning:**
- Embeddings är inte genererade än (normalt första gången)
- Agent kommer generera embeddings när `initialize()` körs

### Problem: Connection timeout

**Lösning:**
- Check firewall
- Använd connection pooling URL istället för direct connection
- Öka timeout i client:
  ```python
  supabase = create_client(url, key, options={"timeout": 30})
  ```

---

## GDPR Compliance Checklist

- [x] Row Level Security (RLS) enabled
- [x] User data isolation via policies
- [x] Automatic backups enabled
- [x] EU region (Stockholm/Frankfurt)
- [ ] Data retention policy (implement själv)
- [ ] Data export functionality (implement själv)
- [ ] Data deletion on user request (implement själv)

**Implementera data retention:**

```python
# Scheduled job (run daily)
async def cleanup_old_data():
    # Delete sessions older than 2 years
    await supabase.table("patient_sessions").delete().lt("created_at", "2 years ago")
```

---

## Sammanfattning

Du har nu:
- ✅ Supabase projekt setup
- ✅ Database schema skapat
- ✅ pgvector för RAG
- ✅ RLS för GDPR compliance
- ✅ Medical knowledge base
- ✅ Connection testad

**Kostar:** $25/mån (Pro plan) eller $0 (Free tier för testing)

**Nästa:** Deploy din app (se [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md))
