# Local PostgreSQL Database Setup Guide

Komplett guide för att köra PostgreSQL lokalt med pgvector för development.

## 📋 Innehåll

1. [Installation (Mac/Linux/Windows)](#installation)
2. [Setup pgvector Extension](#setup-pgvector)
3. [Skapa Database](#skapa-database)
4. [Run Database Schema](#run-database-schema)
5. [Connection Configuration](#connection-configuration)
6. [Docker Compose Setup](#docker-compose-setup-rekommenderat)
7. [GUI Tools](#gui-tools)
8. [Troubleshooting](#troubleshooting)

---

## Installation

### **Option 1: Docker Compose (Rekommenderat)**

Enklast och fungerar på alla plattformar.

#### 1.1 Installera Docker

- **Mac:** https://docs.docker.com/desktop/install/mac-install/
- **Windows:** https://docs.docker.com/desktop/install/windows-install/
- **Linux:** https://docs.docker.com/engine/install/ubuntu/

#### 1.2 Verifiera Installation

```bash
docker --version
docker-compose --version
```

➡️ **Gå till [Docker Compose Setup](#docker-compose-setup-rekommenderat)** nedan

---

### **Option 2: Native Installation**

#### **macOS**

```bash
# Installera med Homebrew
brew install postgresql@15

# Starta PostgreSQL service
brew services start postgresql@15

# Verifiera
psql --version
```

#### **Ubuntu/Debian Linux**

```bash
# Lägg till PostgreSQL repo
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Installera PostgreSQL
sudo apt update
sudo apt install postgresql-15 postgresql-contrib-15

# Starta service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Verifiera
psql --version
```

#### **Windows**

1. Ladda ner från https://www.postgresql.org/download/windows/
2. Kör installer (välj PostgreSQL 15)
3. Sätt password för `postgres` user
4. Starta PostgreSQL från Services

```powershell
# Verifiera i PowerShell
psql --version
```

---

## Setup pgvector

pgvector är required för RAG embeddings.

### **Med Docker (Automatic)**

Om du använder Docker Compose nedan är pgvector redan inkluderat ✅

### **Native Installation**

#### **macOS**

```bash
# Klona pgvector repo
cd /tmp
git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
cd pgvector

# Build & Install
make
make install # Kan kräva sudo

# Verifiera
psql -U postgres -c "CREATE EXTENSION vector;"
```

#### **Ubuntu/Debian**

```bash
# Install build dependencies
sudo apt install build-essential postgresql-server-dev-15

# Klona och build
cd /tmp
git clone --branch v0.5.1 https://github.com/pgvector/pgvector.git
cd pgvector
make
sudo make install

# Verifiera
sudo -u postgres psql -c "CREATE EXTENSION vector;"
```

#### **Windows**

1. Ladda ner pre-built binary från https://github.com/pgvector/pgvector/releases
2. Följ installation instructions i README
3. ELLER använd Docker (enklare)

---

## Skapa Database

### **Steg 1: Anslut till PostgreSQL**

```bash
# macOS/Linux
psql -U postgres

# Windows (om path är setup)
psql -U postgres

# Om du får "peer authentication failed", använd:
sudo -u postgres psql
```

### **Steg 2: Skapa Database**

```sql
-- Skapa database för development
CREATE DATABASE medical_agent_dev;

-- Skapa database för testing
CREATE DATABASE medical_agent_test;

-- Lista databases
\l

-- Anslut till dev database
\c medical_agent_dev
```

### **Steg 3: Enable Extensions**

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Enable text search
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Verifiera
\dx

-- Expected output:
-- uuid-ossp | vector | pg_trgm
```

### **Steg 4: Skapa Database User (Optional)**

```sql
-- Skapa application user
CREATE USER medical_agent WITH PASSWORD 'dev_password_123';

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE medical_agent_dev TO medical_agent;
GRANT ALL PRIVILEGES ON DATABASE medical_agent_test TO medical_agent;

-- Exit
\q
```

---

## Run Database Schema

### **Steg 1: Ladda ner Schema**

Skapa fil: `medical-agent-python/database/schema.sql`

```sql
-- ============================================================================
-- DATABASE SCHEMA FÖR MEDICAL AI AGENT
-- ============================================================================

-- Enable Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ============================================================================
-- PATIENT SESSIONS
-- ============================================================================
CREATE TABLE patient_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id TEXT NOT NULL,
    started_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    ended_at TIMESTAMP WITH TIME ZONE,
    status TEXT NOT NULL CHECK (status IN ('active', 'completed', 'cancelled')) DEFAULT 'active',
    patient_age INTEGER,
    patient_gender TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_patient_sessions_user_id ON patient_sessions(user_id);
CREATE INDEX idx_patient_sessions_status ON patient_sessions(status);
CREATE INDEX idx_patient_sessions_started_at ON patient_sessions(started_at DESC);

-- Update timestamp function
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
    text TEXT NOT NULL,
    chunk_index INTEGER NOT NULL DEFAULT 0,
    is_final BOOLEAN DEFAULT false,
    speaker TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_transcriptions_session_id ON transcriptions(session_id);
CREATE INDEX idx_transcriptions_timestamp ON transcriptions(timestamp);

-- ============================================================================
-- JOURNAL ENTRIES
-- ============================================================================
CREATE TABLE journal_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    generated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    sections JSONB DEFAULT '{}'::jsonb,
    edited_content TEXT,
    edited_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_journal_entries_session_id ON journal_entries(session_id);
CREATE INDEX idx_journal_entries_generated_at ON journal_entries(generated_at DESC);

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
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'question', 'analysis')),
    content JSONB NOT NULL,
    confidence DECIMAL(3,2) CHECK (confidence >= 0 AND confidence <= 1),
    accepted BOOLEAN,
    dismissed BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_agent_suggestions_session_id ON agent_suggestions(session_id);
CREATE INDEX idx_agent_suggestions_type ON agent_suggestions(type);
CREATE INDEX idx_agent_suggestions_created_at ON agent_suggestions(created_at);

-- ============================================================================
-- MEDICAL CONTEXT
-- ============================================================================
CREATE TABLE medical_contexts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL UNIQUE REFERENCES patient_sessions(id) ON DELETE CASCADE,
    symptoms JSONB DEFAULT '[]'::jsonb,
    suspected_diseases JSONB DEFAULT '[]'::jsonb,
    current_medications JSONB DEFAULT '[]'::jsonb,
    asked_questions JSONB DEFAULT '[]'::jsonb,
    medical_history JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX idx_medical_contexts_session_id ON medical_contexts(session_id);

CREATE TRIGGER update_medical_contexts_updated_at
    BEFORE UPDATE ON medical_contexts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- MEDICAL DOCUMENTS (RAG Knowledge Base)
-- ============================================================================
CREATE TABLE medical_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'protocol')),
    name TEXT NOT NULL,
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,
    embedding vector(768),  -- PubMedBERT embeddings
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vector similarity search index
CREATE INDEX ON medical_documents USING hnsw (embedding vector_cosine_ops);
CREATE INDEX idx_medical_documents_type ON medical_documents(type);
CREATE INDEX idx_medical_documents_name ON medical_documents(name);
CREATE INDEX idx_medical_documents_metadata ON medical_documents USING GIN (metadata);
CREATE INDEX idx_medical_documents_content ON medical_documents USING GIN (to_tsvector('swedish', content));

CREATE TRIGGER update_medical_documents_updated_at
    BEFORE UPDATE ON medical_documents
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- SEED DATA - Medical Knowledge Base
-- ============================================================================
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

-- ============================================================================
-- VECTOR SEARCH FUNCTION
-- ============================================================================
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

### **Steg 2: Run Schema**

```bash
# Från medical-agent-python/ directory
psql -U postgres -d medical_agent_dev -f database/schema.sql

# ELLER om du skapade en application user:
psql -U medical_agent -d medical_agent_dev -f database/schema.sql
```

### **Steg 3: Verifiera**

```sql
-- Anslut
psql -U postgres medical_agent_dev

-- Lista tabeller
\dt

-- Check medical documents
SELECT name, type FROM medical_documents;

-- Exit
\q
```

---

## Connection Configuration

### **Steg 1: Uppdatera .env**

```bash
# medical-agent-python/.env.local

# PostgreSQL Connection
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/medical_agent_dev

# ELLER med application user
DATABASE_URL=postgresql://medical_agent:dev_password_123@localhost:5432/medical_agent_dev

# For pgvector
PGVECTOR_CONNECTION=postgresql://postgres:your_password@localhost:5432/medical_agent_dev
```

### **Steg 2: Test Connection från Python**

```python
# test_local_db.py
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv('.env.local')

# Test connection
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()

# Test query
cur.execute("SELECT name, type FROM medical_documents")
results = cur.fetchall()

print(f"✅ Found {len(results)} medical documents:")
for name, type in results:
    print(f"  - {name} ({type})")

cur.close()
conn.close()
```

```bash
pip install psycopg2-binary
python test_local_db.py
```

---

## Docker Compose Setup (Rekommenderat)

Enklaste sättet att köra PostgreSQL med pgvector lokalt.

### **Steg 1: Skapa docker-compose.yml**

```yaml
# medical-agent-python/docker-compose.dev.yml
version: '3.8'

services:
  postgres:
    image: pgvector/pgvector:pg15
    container_name: medical-agent-postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: dev_password_123
      POSTGRES_DB: medical_agent_dev
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./database/schema.sql:/docker-entrypoint-initdb.d/schema.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Optional: pgAdmin for GUI
  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: medical-agent-pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@medical-agent.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - postgres

volumes:
  postgres_data:
```

### **Steg 2: Starta Services**

```bash
# Starta PostgreSQL + pgAdmin
docker-compose -f docker-compose.dev.yml up -d

# View logs
docker-compose -f docker-compose.dev.yml logs -f postgres

# Stop
docker-compose -f docker-compose.dev.yml down

# Stop och ta bort data
docker-compose -f docker-compose.dev.yml down -v
```

### **Steg 3: Access Database**

```bash
# Via psql
docker exec -it medical-agent-postgres psql -U postgres -d medical_agent_dev

# Via pgAdmin
# Öppna http://localhost:5050
# Login: admin@medical-agent.com / admin
# Add Server:
#   Host: postgres (container name)
#   Port: 5432
#   User: postgres
#   Password: dev_password_123
```

### **Steg 4: Run Schema (om inte auto-loaded)**

```bash
docker exec -i medical-agent-postgres psql -U postgres -d medical_agent_dev < database/schema.sql
```

---

## GUI Tools

### **pgAdmin (Web-based)**

Redan inkluderat i Docker Compose ovan.

Access: http://localhost:5050

### **DBeaver (Desktop)**

1. Ladda ner: https://dbeaver.io/download/
2. Install och öppna
3. Database → New Database Connection
4. Select PostgreSQL
5. Fill in:
   ```
   Host: localhost
   Port: 5432
   Database: medical_agent_dev
   User: postgres
   Password: your_password
   ```
6. Test Connection → Finish

### **Postico (macOS)**

1. Ladda ner: https://eggerapps.at/postico/
2. Install och öppna
3. New Favorite
4. Fill in connection details
5. Connect

### **psql (Command Line)**

```bash
# Anslut
psql -U postgres -d medical_agent_dev

# Användbara kommandon:
\dt          # Lista tabeller
\d tablename # Describe table
\l           # Lista databases
\du          # Lista users
\q           # Exit

# Run SQL file
\i database/schema.sql

# Export table
\copy medical_documents TO 'documents.csv' CSV HEADER
```

---

## Troubleshooting

### Problem: "psql: command not found"

**Lösning:**

```bash
# macOS - Lägg till till PATH
echo 'export PATH="/usr/local/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Linux - Reinstall
sudo apt install postgresql-client

# Windows - Lägg till till PATH:
# C:\Program Files\PostgreSQL\15\bin
```

### Problem: "peer authentication failed"

**Lösning:**

Ändra authentication method:

```bash
# Hitta pg_hba.conf
sudo find / -name pg_hba.conf 2>/dev/null

# Edit (macOS/Linux)
sudo nano /path/to/pg_hba.conf

# Ändra:
# local   all   postgres   peer
# Till:
# local   all   postgres   md5

# Restart PostgreSQL
sudo systemctl restart postgresql  # Linux
brew services restart postgresql@15  # macOS
```

### Problem: "extension "vector" does not exist"

**Lösning:**

pgvector är inte installerad. Se [Setup pgvector](#setup-pgvector).

### Problem: Port 5432 redan används

**Lösning:**

```bash
# Hitta vad som använder port
lsof -i :5432  # macOS/Linux
netstat -ano | findstr :5432  # Windows

# Kill processen
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# ELLER ändra port i docker-compose:
ports:
  - "5433:5432"  # Map till 5433 istället
```

### Problem: Container inte startar

**Lösning:**

```bash
# Check logs
docker logs medical-agent-postgres

# Remove volume och försök igen
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml up -d
```

### Problem: Slow queries

**Lösning:**

```sql
-- Enable query logging
ALTER DATABASE medical_agent_dev SET log_statement = 'all';
ALTER DATABASE medical_agent_dev SET log_min_duration_statement = 1000; -- Log queries > 1s

-- Analyze slow query
EXPLAIN ANALYZE SELECT * FROM medical_documents WHERE type = 'disease';

-- Reindex
REINDEX TABLE medical_documents;

-- Vacuum
VACUUM ANALYZE;
```

---

## Development Workflow

### **Daily Workflow**

```bash
# 1. Starta database
docker-compose -f docker-compose.dev.yml up -d

# 2. Run migrations (om du har nya)
psql -U postgres -d medical_agent_dev -f database/migrations/001_add_column.sql

# 3. Utveckla & testa
python app/main.py

# 4. Stoppa när klar
docker-compose -f docker-compose.dev.yml down
```

### **Reset Database**

```bash
# Drop och återskapa
docker-compose -f docker-compose.dev.yml down -v
docker-compose -f docker-compose.dev.yml up -d

# ELLER via psql:
psql -U postgres -c "DROP DATABASE medical_agent_dev;"
psql -U postgres -c "CREATE DATABASE medical_agent_dev;"
psql -U postgres -d medical_agent_dev -f database/schema.sql
```

### **Backup & Restore**

```bash
# Backup
pg_dump -U postgres medical_agent_dev > backup_$(date +%Y%m%d).sql

# Restore
psql -U postgres medical_agent_dev < backup_20240115.sql
```

---

## Migrations

### **Skapa Migration File**

```bash
# database/migrations/001_add_patient_notes.sql
-- Add patient_notes column to patient_sessions
ALTER TABLE patient_sessions
ADD COLUMN patient_notes TEXT;

-- Create index
CREATE INDEX idx_patient_sessions_notes ON patient_sessions USING GIN (to_tsvector('swedish', patient_notes));
```

### **Run Migration**

```bash
psql -U postgres -d medical_agent_dev -f database/migrations/001_add_patient_notes.sql
```

### **Migration Tool (Alembic)**

```bash
pip install alembic

# Initialize
alembic init database/migrations

# Create migration
alembic revision -m "add patient notes"

# Run migrations
alembic upgrade head
```

---

## Sammanfattning

Du har nu:
- ✅ PostgreSQL installerat (Docker eller native)
- ✅ pgvector extension enabled
- ✅ Database schema skapat
- ✅ Test data insertad
- ✅ Connection testad från Python

**Nästa steg:**

1. **Run app lokalt**
   ```bash
   python examples/basic_example.py
   ```

2. **Eller använd Supabase för produktion**
   Se [SUPABASE_SETUP.md](./SUPABASE_SETUP.md)

**Kostnad:** $0 (gratis!)

**Performance:** Samma som Supabase för local development
