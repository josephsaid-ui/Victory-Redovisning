# PostgreSQL från Noll till Expert
## Bonuskapitel: RAG & Vector Search med pgvector 🤖

### Introduktion
Välkommen till bonuskapitlet om AI och PostgreSQL! I denna nivå lär du dig hur PostgreSQL kan användas som en kraftfull vector database för AI-applikationer. Du kommer att förstå RAG (Retrieval-Augmented Generation), implementera semantic search med pgvector, och jämföra PostgreSQL med dedikerade vector databases som Pinecone och Weaviate. Detta är cutting-edge teknologi från 2024-2025 som används i produktions-AI-applikationer världen över!

**Förkunskaper**: Nivå 3-4 av denna guide (grundläggande PostgreSQL-kunskap)

---

## 1. Vad är RAG? (Förklarat enkelt)

### Problemet med vanliga LLM:er

När du frågar ChatGPT eller Claude något, har de en "knowledge cutoff" – de vet bara saker upp till sitt träningsdatum. De kan inte:
- Känna till din företagsdata
- Komma ihåg tidigare konversationer (utan kontext)
- Få tillgång till realtidsinformation

**Exempel:**
```
Användare: "Vad sa vi om projektet i måndags?"
LLM: "Jag har ingen information om dina tidigare konversationer."
```

### Lösningen: RAG (Retrieval-Augmented Generation)

RAG kombinerar databassökning med AI-generering:

```
┌─────────────────────────────────────────────────────────────┐
│                    RAG-FLÖDE                                │
└─────────────────────────────────────────────────────────────┘

1. ANVÄNDARE stället en fråga:
   "Vad sa vi om projektet i måndags?"
                ↓
2. SYSTEMET söker i din databas (PostgreSQL med pgvector)
   Hittar: "Måndag: Beslut att använda Next.js för frontend"
                ↓
3. SYSTEMET skickar BÅDE frågan OCH relevant kontext till LLM:
   "Kontext: Måndag: Beslut att använda Next.js för frontend
    Fråga: Vad sa vi om projektet i måndags?"
                ↓
4. LLM genererar svar BASERAT på den faktiska informationen:
   "Ni beslutade att använda Next.js för frontend."
```

**Enkelt förklarat**: RAG = Din egen "Google" + ChatGPT kombinerat!

---

## 2. Vad är Vector Search?

### Traditionell sökning vs. Semantic Search

**Traditionell sökning** (LIKE, full-text search):
```sql
SELECT * FROM dokument WHERE innehåll LIKE '%katt%';
```
Hittar: "katt", "katter", "katten"
Missar: "husdjur", "djur", "kattdjur"

**Semantic Search** (vector search):
Förstår MENING, inte bara ord!

```
Fråga: "husdjur"
Hittar även: "katt", "hund", "fisk i akvarium", "kanin"
Eftersom de har LIKNANDE BETYDELSE!
```

### Hur fungerar det? (Embeddings)

**Embeddings** = Matematik-representation av ord/text

```
"katt"  → [0.2, 0.8, 0.1, 0.5, ...]  (1536 tal)
"hund"  → [0.3, 0.7, 0.2, 0.4, ...]  (nära katt!)
"bil"   → [0.9, 0.1, 0.8, 0.1, ...]  (långt från katt)
```

**Visualisering (förenklad till 2D)**:
```
       Husdjur
         │
    katt●  ●hund
         │
    kanin●
─────────┼─────────── Fordon
         │
         │    bil●
         │   ●lastbil
       Möbler
```

Ord som betyder liknande saker hamnar nära varandra i detta "matematiska rum"!

---

## 3. pgvector: PostgreSQL som Vector Database

### Installation

**Med Docker** (enklast):
```bash
docker run --name postgres-ai \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -d ankane/pgvector
```

**Med befintlig PostgreSQL**:
```sql
-- Installera extension (kräver superuser)
CREATE EXTENSION vector;
```

**Verifiera installation**:
```sql
SELECT * FROM pg_extension WHERE extname = 'vector';
```

---

### Skapa din första vector-tabell

```sql
-- Tabell för att lagra dokument med embeddings
CREATE TABLE dokument (
    id SERIAL PRIMARY KEY,
    titel VARCHAR(200),
    innehåll TEXT,
    -- Embedding från OpenAI text-embedding-3-small (1536 dimensioner)
    embedding vector(1536),
    skapad_datum TIMESTAMP DEFAULT NOW()
);

-- Exempel med mindre dimensioner (för demo)
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100),
    beskrivning TEXT,
    embedding vector(384)  -- t.ex. sentence-transformers
);
```

**Vad är `vector(1536)`?**
- `vector` = datatyp från pgvector extension
- `1536` = antal dimensioner (beror på embedding-modell)
- OpenAI `text-embedding-3-small` → 1536 dimensioner
- OpenAI `text-embedding-3-large` → 3072 dimensioner
- Sentence-transformers `all-MiniLM-L6-v2` → 384 dimensioner

---

### Lägg in data med embeddings

```python
# Python-exempel med OpenAI
import openai
import psycopg2

# Skapa embedding
def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Anslut till PostgreSQL
conn = psycopg2.connect("dbname=aidb user=postgres password=secret")
cur = conn.cursor()

# Dokument att lagra
dokument = [
    ("Guide till katter", "Katter är populära husdjur som älskar att jaga och sova."),
    ("Bilens historia", "Bilen revolutionerade transport och gjorde resor snabbare."),
    ("Hunduppfostran", "Hundar behöver träning och social stimulans för att må bra.")
]

# Lägg in varje dokument
for titel, innehåll in dokument:
    embedding = get_embedding(innehåll)

    cur.execute(
        "INSERT INTO dokument (titel, innehåll, embedding) VALUES (%s, %s, %s)",
        (titel, innehåll, embedding)
    )

conn.commit()
```

---

### Söka med Vector Similarity

**Tre distance-metoder i pgvector:**

| Operator | Metod | Användning |
|----------|-------|-----------|
| `<->` | Euclidean (L2) | Fysisk distans |
| `<=>` | Cosine distance | Semantic similarity (REKOMMENDERAT) |
| `<#>` | Inner product | Vissa ML-modeller |

**Exempel: Hitta dokument liknande en fråga**

```python
# Användarfråga
query = "Information om husdjur"
query_embedding = get_embedding(query)

# Sök efter liknande dokument
cur.execute("""
    SELECT titel, innehåll,
           (embedding <=> %s::vector) AS distance
    FROM dokument
    ORDER BY embedding <=> %s::vector
    LIMIT 5
""", (query_embedding, query_embedding))

results = cur.fetchall()
for titel, innehåll, distance in results:
    print(f"{titel} (distance: {distance:.4f})")
    print(f"  {innehåll[:100]}...\n")
```

**Output:**
```
Guide till katter (distance: 0.1523)
  Katter är populära husdjur som älskar att jaga och sova...

Hunduppfostran (distance: 0.1891)
  Hundar behöver träning och social stimulans för att må bra...

Bilens historia (distance: 0.8234)
  Bilen revolutionerade transport och gjorde resor snabbare...
```

**Lägre distance = mer liknande!**

---

## 4. Indexering för Prestanda (KRITISKT!)

### Utan index: LÅNGSAMT

```sql
-- Full table scan för varje sökning
EXPLAIN ANALYZE SELECT * FROM dokument
ORDER BY embedding <=> '[0.1, 0.2, ...]'::vector
LIMIT 10;

-- Resultat: 5000ms för 1 miljon rader
```

### Med index: SNABBT!

**HNSW Index** (rekommenderat 2024-2025):

```sql
-- Skapa HNSW index (Hierarchical Navigable Small World)
CREATE INDEX ON dokument USING hnsw (embedding vector_cosine_ops);

-- Nu är sökningen 100-1000x snabbare!
-- Resultat: 10ms för 1 miljon rader
```

**IVFFlat Index** (äldre, men fungerar):

```sql
-- Skapa IVFFlat index
-- lists = antal clusters (tumregel: rows / 1000)
CREATE INDEX ON dokument USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- OBS: Kräver training data först!
```

### Index-typer jämförelse

| Index-typ | Prestanda | Precision | När använda |
|-----------|-----------|-----------|-------------|
| **HNSW** | Mycket snabb | Hög | Standard för 2024-2025 |
| **IVFFlat** | Snabb | Medium-hög | Äldre installationer |
| **Inget index** | Långsam | Perfekt | < 10,000 rader |

**Best Practice 2024-2025**: Använd HNSW med cosine distance!

```sql
-- RÄTT: Matcha index och query
CREATE INDEX idx_hnsw ON dokument USING hnsw (embedding vector_cosine_ops);
SELECT * FROM dokument ORDER BY embedding <=> '[...]'::vector;  -- Använder index!

-- FEL: Mismatch mellan index och query
CREATE INDEX idx_hnsw ON dokument USING hnsw (embedding vector_cosine_ops);
SELECT * FROM dokument ORDER BY embedding <-> '[...]'::vector;  -- Använder INTE index!
```

---

## 5. Komplett RAG-implementation

### Arkitektur

```
┌──────────────────────────────────────────────────────────┐
│                    RAG SYSTEM                            │
└──────────────────────────────────────────────────────────┘

[User Query] ──────────────────────────┐
      │                                │
      ↓                                ↓
┌──────────────┐              ┌─────────────────┐
│  Embedding   │              │  Embed Query    │
│   Model      │              │  (same model)   │
│  (OpenAI)    │              └────────┬────────┘
└──────┬───────┘                       │
       │                               ↓
       │                      ┌────────────────┐
       ↓                      │  PostgreSQL    │
┌──────────────┐              │  + pgvector    │
│  Documents   │              │                │
│  + Embeddings│◄─────────────│  Vector Search │
│  Storage     │              └────────┬───────┘
└──────────────┘                       │
                                       ↓
                              ┌────────────────┐
                              │  Top K Similar │
                              │  Documents     │
                              └────────┬───────┘
                                       │
                                       ↓
                              ┌────────────────┐
                              │  LLM (GPT-4)   │
                              │  with Context  │
                              └────────┬───────┘
                                       │
                                       ↓
                              [Generated Answer]
```

### Steg-för-steg implementation

#### Steg 1: Förbered dokument (chunking)

```python
def chunk_text(text, chunk_size=1500, overlap=300):
    """
    Dela upp lång text i chunks med overlap.

    Best practice 2024-2025:
    - chunk_size: 1500 tokens (~6000 tecken)
    - overlap: 300 tokens för kontext
    """
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks

# Exempel
long_document = "..." # Din långa text
chunks = chunk_text(long_document)
```

#### Steg 2: Skapa och lagra embeddings

```python
import openai
import psycopg2
from pgvector.psycopg2 import register_vector

conn = psycopg2.connect("dbname=rag_db user=postgres")
register_vector(conn)
cur = conn.cursor()

# Skapa tabell
cur.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id SERIAL PRIMARY KEY,
        source VARCHAR(200),
        chunk_text TEXT,
        chunk_index INTEGER,
        embedding vector(1536),
        metadata JSONB,
        created_at TIMESTAMP DEFAULT NOW()
    )
""")

def store_document(source, text):
    chunks = chunk_text(text)

    for idx, chunk in enumerate(chunks):
        # Skapa embedding
        response = openai.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embedding = response.data[0].embedding

        # Lagra i PostgreSQL
        cur.execute("""
            INSERT INTO knowledge_base (source, chunk_text, chunk_index, embedding, metadata)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            source,
            chunk,
            idx,
            embedding,
            {'chunk_size': len(chunk), 'total_chunks': len(chunks)}
        ))

    conn.commit()

# Lägg in dokument
store_document("PostgreSQL Guide Level 5", "Din guide-text här...")
```

#### Steg 3: Skapa index

```sql
-- HNSW index för snabb sökning
CREATE INDEX ON knowledge_base USING hnsw (embedding vector_cosine_ops);

-- Index för metadata-filtrering
CREATE INDEX ON knowledge_base USING GIN (metadata);
CREATE INDEX ON knowledge_base (source);
```

#### Steg 4: Retrieval-funktion

```python
def retrieve_context(query, top_k=5):
    """
    Hämta mest relevanta chunks för en query.
    """
    # Skapa query embedding
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    query_embedding = response.data[0].embedding

    # Sök liknande chunks
    cur.execute("""
        SELECT
            chunk_text,
            source,
            1 - (embedding <=> %s::vector) AS similarity
        FROM knowledge_base
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """, (query_embedding, query_embedding, top_k))

    results = cur.fetchall()

    # Formatera kontext
    context = "\n\n---\n\n".join([
        f"Källa: {source}\n{text}"
        for text, source, sim in results
    ])

    return context, results
```

#### Steg 5: RAG-query med LLM

```python
def rag_query(user_question):
    """
    Komplett RAG-pipeline.
    """
    # 1. Hämta relevant kontext
    context, sources = retrieve_context(user_question, top_k=3)

    # 2. Skapa prompt med kontext
    prompt = f"""Du är en hjälpsam assistent som svarar baserat på given kontext.

KONTEXT:
{context}

FRÅGA: {user_question}

Svara endast baserat på kontexten ovan. Om kontexten inte innehåller svaret, säg det.
"""

    # 3. Skicka till LLM
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en expertassistent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # Lägre = mer faktabaserat
    )

    answer = response.choices[0].message.content

    # 4. Returnera svar med källor
    return {
        'answer': answer,
        'sources': [{'source': s[1], 'similarity': s[2]} for s in sources]
    }

# Använd systemet
result = rag_query("Hur använder jag pgvector för vector search?")
print(result['answer'])
print("\nKällor:")
for src in result['sources']:
    print(f"  - {src['source']} (similarity: {src['similarity']:.2%})")
```

---

## 6. Avancerade tekniker

### Hybrid Search (Keyword + Vector)

Kombinera traditionell full-text search med vector search:

```sql
-- Lägg till full-text search
ALTER TABLE knowledge_base ADD COLUMN search_vector tsvector
    GENERATED ALWAYS AS (to_tsvector('swedish', chunk_text)) STORED;

CREATE INDEX ON knowledge_base USING GIN (search_vector);

-- Hybrid query (både keyword och semantic)
SELECT
    chunk_text,
    source,
    ts_rank(search_vector, query) AS keyword_score,
    1 - (embedding <=> %s::vector) AS semantic_score,
    -- Kombinerad score (justera vikter)
    (0.3 * ts_rank(search_vector, query) +
     0.7 * (1 - (embedding <=> %s::vector))) AS combined_score
FROM knowledge_base, to_tsquery('swedish', 'pgvector & search') query
WHERE search_vector @@ query
   OR (embedding <=> %s::vector) < 0.5
ORDER BY combined_score DESC
LIMIT 10;
```

### Metadata-filtrering

Filtrera vektorsökning baserat på metadata:

```python
def retrieve_with_filter(query, source_filter=None, date_filter=None):
    """
    Retrieval med metadata-filter.
    """
    query_embedding = get_embedding(query)

    sql = """
        SELECT chunk_text, source, metadata
        FROM knowledge_base
        WHERE 1=1
    """
    params = []

    # Lägg till filters
    if source_filter:
        sql += " AND source = %s"
        params.append(source_filter)

    if date_filter:
        sql += " AND created_at > %s"
        params.append(date_filter)

    sql += """
        ORDER BY embedding <=> %s::vector
        LIMIT 5
    """
    params.append(query_embedding)

    cur.execute(sql, params)
    return cur.fetchall()

# Använd
results = retrieve_with_filter(
    "PostgreSQL optimering",
    source_filter="PostgreSQL Guide Level 4",
    date_filter="2025-01-01"
)
```

### Re-ranking (2024-2025 Best Practice)

Använd en re-ranking-modell för bättre precision:

```python
from sentence_transformers import CrossEncoder

# Ladda re-ranking-modell
reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

def retrieve_with_rerank(query, initial_k=20, final_k=5):
    """
    1. Hämta top-20 med vector search
    2. Re-rank med cross-encoder
    3. Returnera top-5
    """
    # Steg 1: Initial retrieval
    context, results = retrieve_context(query, top_k=initial_k)

    # Steg 2: Re-rank
    pairs = [(query, r[0]) for r in results]
    scores = reranker.predict(pairs)

    # Steg 3: Sortera om
    reranked = sorted(
        zip(results, scores),
        key=lambda x: x[1],
        reverse=True
    )[:final_k]

    return reranked
```

---

## 7. pgvector vs. Dedikerade Vector Databases

### Jämförelse-tabell (2024-2025)

| Feature | pgvector | Pinecone | Weaviate | Qdrant |
|---------|----------|----------|----------|--------|
| **Typ** | Extension | Managed service | Open-source/Cloud | Open-source/Cloud |
| **Max vectors** | ~10M* | Billions | Billions | Billions |
| **Latency (1M vecs)** | 10-50ms | 5-15ms | 10-30ms | 5-20ms |
| **Setup-komplexitet** | Mycket låg | Mycket låg | Medium | Medium |
| **Kostnad (1M vecs)** | ~$0-10/mån | ~$20-30/mån | ~$50/mån | ~$25-100/mån |
| **ACID-transaktioner** | ✅ Ja | ❌ Nej | ❌ Nej | ❌ Nej |
| **SQL-queries** | ✅ Ja | ❌ Nej | Begränsat | ❌ Nej |
| **Metadata-filtrering** | ✅ Full SQL | ✅ Bra | ✅ Utmärkt | ✅ Utmärkt |
| **Hybrid search** | ✅ Med full-text | ✅ Med tillägg | ✅ Native | ✅ Med tillägg |
| **Self-hosted** | ✅ Ja | ❌ Nej | ✅ Ja | ✅ Ja |
| **Learning curve** | Låg (om du kan SQL) | Låg | Medium | Medium |
| **Community** | PostgreSQL (stor) | Växande | Växande | Växande |

*Realistisk gräns för bra prestanda

### När använda vad?

#### ✅ Använd **pgvector** om:
- Du redan har PostgreSQL
- < 5M vectors
- Du vill ha ACID-transaktioner
- Budget är begränsad
- Du älskar SQL och relationsdata
- Prototyp/MVP-fas

**Exempel**: Intern kunskapsbas, customer support chatbot (litet företag)

#### ✅ Använd **Pinecone** om:
- Du vill ha minsta möjliga setup
- Skala till miljarder vectors
- Managed service önskas
- Budget finns ($$)
- Produktion från dag 1

**Exempel**: Stor e-handelsrekommendation, produktionssystem med hög trafik

#### ✅ Använd **Weaviate** om:
- Du behöver kraftfull hybrid search
- Flexibel schema-design
- Open-source viktigt (men cloud ok)
- Multi-modal data (text + bilder)

**Exempel**: Multi-modal sökmotor, komplex metadata-sökning

#### ✅ Använd **Qdrant** om:
- Högsta prestanda krävs
- Kostnadseffektivitet viktig
- Avancerad filtering behövs
- Open-source + cloud-option

**Exempel**: Real-time-rekommendationer, högtrafik-applikationer

---

## 8. Verkliga Case Studies

### Case Study 1: Customer Support Chatbot

**Företag**: SaaS-startup med 1000 kunder
**Problem**: 100+ support-tickets/dag om samma frågor
**Lösning**: RAG med pgvector

```python
# Setup
# 1. Lagra alla support-tickets och svar i PostgreSQL
# 2. Skapa embeddings för varje ticket + svar
# 3. När ny fråga kommer: Hitta liknande gamla tickets
# 4. Föreslå svar baserat på tidigare lösningar

# Resultat:
# - 60% av tickets automatiskt besvarade
# - Svarstid: 5 sekunder (tidigare: 2 timmar)
# - Kostnad: $50/månad (tidigare: $5000/månad i personalkostnad)
```

### Case Study 2: Intern Kunskapsbas (Enterprise)

**Företag**: 500-personersföretag
**Problem**: Information spretat i 1000+ dokument (PDF, Confluence, Google Docs)
**Lösning**: RAG med pgvector + metadata

**Implementation:**
```sql
CREATE TABLE enterprise_knowledge (
    id SERIAL PRIMARY KEY,
    document_type VARCHAR(50),  -- PDF, Confluence, etc.
    department VARCHAR(50),
    title VARCHAR(200),
    chunk_text TEXT,
    embedding vector(1536),
    metadata JSONB,
    access_control JSONB  -- Vem får se detta?
);

-- RLS för säkerhet
ALTER TABLE enterprise_knowledge ENABLE ROW LEVEL SECURITY;

CREATE POLICY department_access ON enterprise_knowledge
    USING (
        metadata->>'department' = current_setting('app.user_department')
        OR metadata->>'public' = 'true'
    );
```

**Resultat:**
- 90% hittar svar på < 30 sekunder
- 3x snabbare onboarding av nya medarbetare
- ROI: 6 månader

### Case Study 3: E-handel Product Discovery

**Företag**: Online-butik med 500,000 produkter
**Problem**: Traditionell sökning missar semantiskt liknande produkter
**Lösning**: Hybrid search (keyword + vector)

**Före:**
```
Sökning: "laptop för studenter"
Resultat: Bara produkter med exakt "laptop" och "studenter" i beskrivning
```

**Efter:**
```
Sökning: "laptop för studenter"
Resultat:
- Billiga laptops
- Chromebooks
- Lätta notebooks
- Student-paket
(Även utan exakta ord!)
```

**Implementation highlights:**
- HNSW-index på produkt-beskrivningar
- Real-time updates (100+ nya produkter/dag)
- A/B-test visade +22% conversion rate

---

## 9. Prestandaoptimering

### Konfigurationstuning för pgvector

```sql
-- PostgreSQL-konfiguration för pgvector (postgresql.conf)

-- Öka shared buffers
shared_buffers = 8GB              -- 25% av RAM

-- Effektivt cacheutrymme
effective_cache_size = 24GB       -- 75% av RAM

-- Work memory för vector operations
work_mem = 256MB                  -- Högre än vanligt

-- Maintenance för index-byggning
maintenance_work_mem = 4GB

-- Disable JIT för bättre prestanda
jit = off

-- Parallel workers för stora queries
max_parallel_workers_per_gather = 4
```

### Index-tuning

```sql
-- För HNSW-index, justera m och ef_construction
CREATE INDEX ON knowledge_base
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- m = antal kanter per nod (högre = bättre precision, mer minne)
-- ef_construction = sökstorlekt vid byggning (högre = bättre kvalitet, långsammare)

-- Default: m=16, ef_construction=64
-- Hög precision: m=32, ef_construction=128
-- Snabb byggning: m=8, ef_construction=32
```

### Query-optimering

```sql
-- Använd SET LOCAL för att justera search scope
BEGIN;
SET LOCAL hnsw.ef_search = 200;  -- Default: 40
-- Högre = bättre precision, långsammare

SELECT * FROM knowledge_base
ORDER BY embedding <=> '[...]'::vector
LIMIT 10;

COMMIT;
```

### Batch-processing för inserts

```python
# Ineffektivt: En åt gången
for doc in documents:
    embedding = get_embedding(doc)
    insert_to_db(doc, embedding)

# Effektivt: Batch embeddings
embeddings = openai.embeddings.create(
    model="text-embedding-3-small",
    input=[doc for doc in documents]  # Batch!
).data

# Batch insert
cur.executemany(
    "INSERT INTO knowledge_base (text, embedding) VALUES (%s, %s)",
    [(doc, emb.embedding) for doc, emb in zip(documents, embeddings)]
)
```

---

## 10. Moderna Stack-exempel

### Next.js + pgvector + OpenAI

```typescript
// app/api/chat/route.ts
import { OpenAI } from 'openai';
import { Pool } from 'pg';

const openai = new OpenAI();
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

export async function POST(req: Request) {
  const { question } = await req.json();

  // 1. Skapa embedding för frågan
  const embeddingResponse = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: question,
  });
  const queryEmbedding = embeddingResponse.data[0].embedding;

  // 2. Sök i PostgreSQL
  const client = await pool.connect();
  const { rows } = await client.query(`
    SELECT chunk_text, source
    FROM knowledge_base
    ORDER BY embedding <=> $1::vector
    LIMIT 3
  `, [JSON.stringify(queryEmbedding)]);
  client.release();

  // 3. Bygg kontext
  const context = rows.map(r => r.chunk_text).join('\n\n---\n\n');

  // 4. Generera svar
  const completion = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [
      {
        role: 'system',
        content: 'Svara baserat på given kontext.'
      },
      {
        role: 'user',
        content: `Kontext:\n${context}\n\nFråga: ${question}`
      }
    ],
  });

  return Response.json({
    answer: completion.choices[0].message.content,
    sources: rows.map(r => r.source),
  });
}
```

### Python FastAPI + pgvector

```python
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import asyncpg

app = FastAPI()

class Question(BaseModel):
    question: str

@app.on_event("startup")
async def startup():
    app.state.pool = await asyncpg.create_pool(
        'postgresql://user:pass@localhost/ragdb'
    )

@app.post("/chat")
async def chat(q: Question):
    # Embedding
    emb_response = await openai.embeddings.acreate(
        model="text-embedding-3-small",
        input=q.question
    )
    query_emb = emb_response.data[0].embedding

    # Retrieval
    async with app.state.pool.acquire() as conn:
        rows = await conn.fetch("""
            SELECT chunk_text, source
            FROM knowledge_base
            ORDER BY embedding <=> $1::vector
            LIMIT 3
        """, query_emb)

    context = "\n\n---\n\n".join([r['chunk_text'] for r in rows])

    # Generation
    response = await openai.chat.completions.acreate(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Du är en hjälpsam assistent."},
            {"role": "user", "content": f"Kontext:\n{context}\n\nFråga: {q.question}"}
        ]
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": [r['source'] for r in rows]
    }
```

---

## 🎯 Övningar

### Övning 1: Installera och testa pgvector
1. Starta PostgreSQL med pgvector (Docker)
2. Skapa en enkel tabell med embeddings
3. Lägg in 5 test-dokument med fake embeddings
4. Testa cosine similarity search

**Facit:**
```bash
# 1. Docker
docker run --name pgvector-test -e POSTGRES_PASSWORD=test -p 5432:5432 -d ankane/pgvector

# 2. SQL
docker exec -it pgvector-test psql -U postgres

CREATE EXTENSION vector;

CREATE TABLE test_docs (
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding vector(3)  -- 3D för demo
);

# 3. Insert test data
INSERT INTO test_docs (text, embedding) VALUES
    ('Katter är söta', '[1, 0, 0]'),
    ('Hundar är lojala', '[0.9, 0.1, 0]'),
    ('Bilar är snabba', '[0, 0, 1]'),
    ('Motorcyklar är snabba', '[0, 0.1, 0.9]'),
    ('Fåglar kan flyga', '[0.5, 0.5, 0.5]');

# 4. Search
SELECT text, embedding <=> '[1, 0, 0]'::vector AS distance
FROM test_docs
ORDER BY distance
LIMIT 3;
```

### Övning 2: Bygg en mini-RAG med OpenAI
Skapa ett enkelt RAG-system som:
1. Läser 3 textfiler
2. Chunkar dem
3. Skapar embeddings
4. Lagrar i PostgreSQL
5. Kan svara på frågor

**Tips:**
```python
# Använd koden från "Komplett RAG-implementation"
# Anpassa för dina textfiler
```

### Övning 3: Hybrid Search
Implementera hybrid search som kombinerar:
- Full-text search (tsvector)
- Vector search (pgvector)

**Facit:**
```sql
-- Tabell
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    content TEXT,
    content_tsvector tsvector GENERATED ALWAYS AS (to_tsvector('swedish', content)) STORED,
    embedding vector(1536)
);

-- Index
CREATE INDEX ON articles USING GIN (content_tsvector);
CREATE INDEX ON articles USING hnsw (embedding vector_cosine_ops);

-- Hybrid query
WITH keyword_results AS (
    SELECT id, ts_rank(content_tsvector, query) AS keyword_score
    FROM articles, to_tsquery('swedish', 'postgres & vector') query
    WHERE content_tsvector @@ query
),
vector_results AS (
    SELECT id, 1 - (embedding <=> $1::vector) AS vector_score
    FROM articles
)
SELECT
    a.title,
    COALESCE(k.keyword_score, 0) * 0.3 +
    COALESCE(v.vector_score, 0) * 0.7 AS combined_score
FROM articles a
LEFT JOIN keyword_results k ON a.id = k.id
LEFT JOIN vector_results v ON a.id = v.id
WHERE k.id IS NOT NULL OR v.id IS NOT NULL
ORDER BY combined_score DESC
LIMIT 10;
```

### Övning 4: Benchmark pgvector vs. No Index
1. Skapa tabell med 100,000 vectors
2. Mät query-tid utan index
3. Skapa HNSW index
4. Mät query-tid med index
5. Jämför!

**Facit:**
```python
import numpy as np
import psycopg2
import time

conn = psycopg2.connect("dbname=benchmark")
cur = conn.cursor()

# Skapa tabell
cur.execute("CREATE TABLE vectors (id SERIAL PRIMARY KEY, embedding vector(384))")

# Insert 100k random vectors
print("Inserting 100k vectors...")
for i in range(100000):
    vec = np.random.rand(384).tolist()
    cur.execute("INSERT INTO vectors (embedding) VALUES (%s)", (vec,))
    if i % 10000 == 0:
        print(f"  {i}...")
        conn.commit()
conn.commit()

# Test UTAN index
query_vec = np.random.rand(384).tolist()
start = time.time()
cur.execute("SELECT id FROM vectors ORDER BY embedding <=> %s::vector LIMIT 10", (query_vec,))
results = cur.fetchall()
no_index_time = time.time() - start
print(f"Query utan index: {no_index_time:.2f}s")

# Skapa index
print("Creating HNSW index...")
start = time.time()
cur.execute("CREATE INDEX ON vectors USING hnsw (embedding vector_cosine_ops)")
conn.commit()
index_build_time = time.time() - start
print(f"Index build time: {index_build_time:.2f}s")

# Test MED index
start = time.time()
cur.execute("SELECT id FROM vectors ORDER BY embedding <=> %s::vector LIMIT 10", (query_vec,))
results = cur.fetchall()
with_index_time = time.time() - start
print(f"Query med index: {with_index_time:.2f}s")

print(f"\nSpeedup: {no_index_time / with_index_time:.1f}x snabbare!")
```

### Övning 5: Produktions-RAG med Metadata
Bygg ett RAG-system för ett företag med:
- Dokument från olika avdelningar
- Access control (vissa användare ser bara vissa dokument)
- Metadata-filtrering

**Hint:**
```sql
CREATE TABLE corp_knowledge (
    id SERIAL PRIMARY KEY,
    department VARCHAR(50),
    confidentiality VARCHAR(20),  -- public, internal, confidential
    title VARCHAR(200),
    chunk_text TEXT,
    embedding vector(1536),
    metadata JSONB
);

-- RLS
ALTER TABLE corp_knowledge ENABLE ROW LEVEL SECURITY;

CREATE POLICY department_access ON corp_knowledge
    USING (
        department = current_setting('app.user_department')
        OR confidentiality = 'public'
    );
```

---

## 💡 Expert Pro Tips (2024-2025)

1. **Chunking är viktigare än du tror** – Dålig chunking = dålig RAG, även med bästa modellen!
2. **Använd HNSW, inte IVFFlat** – HNSW är standard 2024-2025, bättre prestanda.
3. **Hybrid search slår pure vector** – Kombinera keyword + semantic för bäst resultat.
4. **Re-ranking förbättrar precision** – Initialt top-20, sen re-rank till top-5.
5. **Metadata-filtrering är kritiskt** – Users ska inte se confidentila dokument!
6. **pgvector är undervärderat** – För < 5M vectors, slå Pinecone i kostnad/nytta.
7. **Mät alltid precision** – Använd metrics (MRR, NDCG) för att utvärdera.
8. **Batch embeddings sparar pengar** – 10x billigare att batchprocessa via OpenAI.

---

## Sammanfattning: Vad har du lärt dig?

✅ **RAG-koncept**: Hur retrieval + generation kombineras för smartare AI
✅ **Vector embeddings**: Matematisk representation av semantisk mening
✅ **pgvector**: PostgreSQL som kraftfull vector database
✅ **Indexering**: HNSW och IVFFlat för snabb similarity search
✅ **Komplett implementation**: Från chunking till LLM-generation
✅ **Avancerade tekniker**: Hybrid search, re-ranking, metadata-filtrering
✅ **Jämförelser**: pgvector vs. Pinecone/Weaviate/Qdrant
✅ **Verkliga case studies**: Hur företag använder RAG i produktion
✅ **Prestanda-optimering**: Konfiguration och best practices
✅ **Moderna stacks**: Integration med Next.js, FastAPI

**Nya ord (Ordlista):**
- **RAG**: Retrieval-Augmented Generation – Kombination av databassökning och AI-generering
- **Vector embedding**: Numerisk representation av text/data som en vektor
- **Semantic search**: Sökning baserad på mening, inte bara exakta ord
- **pgvector**: PostgreSQL extension för vector similarity search
- **HNSW**: Hierarchical Navigable Small World – Effektiv index-typ för vectors
- **IVFFlat**: Inverted File with Flat compression – Äldre vector index-typ
- **Cosine similarity**: Mått på likhet mellan vectors (0-1)
- **Chunking**: Dela upp lång text i mindre delar för embeddings
- **Hybrid search**: Kombination av keyword-sökning och vector search
- **Re-ranking**: Omordna resultat med mer avancerad modell
- **Dimension**: Antal tal i en vector (t.ex. 1536 för OpenAI embeddings)

---

## Nästa steg: Bygg din egen RAG-app!

Du har nu all kunskap för att bygga produktionsklara AI-applikationer med PostgreSQL! Prova:

1. **Personlig kunskapsbas** – Importera dina anteckningar/dokument
2. **Company chatbot** – RAG för customer support
3. **Code search** – Sök i din codebase med semantic search
4. **Document QA** – Ställ frågor till PDF:er

**Resurser:**
- [pgvector GitHub](https://github.com/pgvector/pgvector)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [LangChain för RAG](https://python.langchain.com/docs/use_cases/question_answering/)

---

**Du är nu en PostgreSQL + AI-expert! 🤖🚀**

---

**Läsningstid**: ~35 minuter
**Nivå**: Bonus (Expert + AI)
**Kräver**: Nivå 3-5 av huvudguiden
