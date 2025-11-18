# PostgreSQL från Noll till Expert
## Nivå 5: "Expert" - PostgreSQL på masternivå 💼

### Introduktion
Grattis till att ha kommit till sista nivån! Här går vi djupt in i PostgreSQL:s mest avancerade funktioner som används i produktionssystem med miljontals användare. Du kommer att lära dig hantera komplexa data med JSONB, skala databaser med partitionering, automatisera med stored procedures, säkra multi-tenant-applikationer med Row Level Security, och optimera för produktion med replikering och connection pooling. Efter denna nivå är du en fullfjädrad PostgreSQL-expert som kan designa och underhålla enterprise-system!

---

## 1. Avancerad JSONB: NoSQL-kraften i PostgreSQL

### Varför JSONB? (2024-2025 perspektiv)
JSONB kombinerar relationsdatabasers styrka (ACID, constraints) med NoSQL:s flexibilitet. PostgreSQL 17 introducerade `JSON_TABLE()` för ännu kraftfullare queries.

### Grundläggande JSONB-operationer

```sql
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100),
    metadata JSONB
);

INSERT INTO produkter (namn, metadata) VALUES
    ('Laptop', '{"märke": "Dell", "specs": {"cpu": "Intel i7", "ram_gb": 16}}'),
    ('Telefon', '{"märke": "Samsung", "specs": {"kamera_mp": 48, "5g": true}}');

-- Hämta ett specifikt fält
SELECT namn, metadata->>'märke' AS märke FROM produkter;

-- Hämta nested data
SELECT namn, metadata->'specs'->>'cpu' AS cpu FROM produkter;

-- Filtrera på JSONB-innehåll
SELECT * FROM produkter WHERE metadata->>'märke' = 'Dell';

-- Kontrollera om nyckel finns
SELECT * FROM produkter WHERE metadata ? 'märke';

-- Sök i nested objekt
SELECT * FROM produkter WHERE metadata @> '{"specs": {"5g": true}}';
```

### Avancerade queries med JSONB (2024-2025)

```sql
-- Uppdatera del av JSONB
UPDATE produkter
SET metadata = jsonb_set(metadata, '{specs,ram_gb}', '32')
WHERE namn = 'Laptop';

-- Lägg till nytt fält
UPDATE produkter
SET metadata = metadata || '{"garanti_år": 2}'::jsonb
WHERE id = 1;

-- Ta bort fält
UPDATE produkter
SET metadata = metadata - 'garanti_år'
WHERE id = 1;

-- Aggregera JSONB-data
SELECT
    metadata->>'märke' AS märke,
    COUNT(*) AS antal,
    AVG((metadata->'specs'->>'ram_gb')::int) AS genomsnitt_ram
FROM produkter
WHERE metadata->'specs' ? 'ram_gb'
GROUP BY metadata->>'märke';
```

### Index för JSONB (KRITISKT för prestanda!)

```sql
-- GIN index för snabba sökningar
CREATE INDEX idx_metadata_gin ON produkter USING GIN (metadata);

-- Index på specifik nyckel
CREATE INDEX idx_metadata_märke ON produkter ((metadata->>'märke'));

-- Index för containment queries (@>)
CREATE INDEX idx_metadata_specs ON produkter USING GIN ((metadata->'specs'));
```

**2024 Best Practice**: Använd JSONB för flexibel metadata, user preferences, eller audit logs. För kritisk affärsdata, använd vanliga kolumner för bättre type safety.

---

## 2. Partitionering: Skala till miljarder rader

### När behöver du partitionering?
- Tabeller > 100 GB
- Tidsseriedata (logs, metrics, events)
- När äldre data sällan används
- Multi-tenant-applikationer med tydliga tenant-gränser

### Range-partitionering (vanligast för tidsdata)

```sql
-- Huvudtabell (parent table)
CREATE TABLE loggar (
    id BIGSERIAL,
    användare_id INTEGER,
    händelse VARCHAR(100),
    skapad_vid TIMESTAMP NOT NULL,
    metadata JSONB
) PARTITION BY RANGE (skapad_vid);

-- Skapa partitioner för 2025
CREATE TABLE loggar_2025_01 PARTITION OF loggar
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

CREATE TABLE loggar_2025_02 PARTITION OF loggar
    FOR VALUES FROM ('2025-02-01') TO ('2025-03-01');

-- ...fortsätt för varje månad

-- Default-partition för data utanför range
CREATE TABLE loggar_default PARTITION OF loggar DEFAULT;

-- Index på varje partition skapas automatiskt
CREATE INDEX ON loggar (skapad_vid);
CREATE INDEX ON loggar (användare_id);
```

### Partition Pruning (automatisk optimering!)

```sql
-- PostgreSQL hoppar automatiskt över irrelevanta partitioner
EXPLAIN SELECT * FROM loggar
WHERE skapad_vid BETWEEN '2025-02-01' AND '2025-02-07';

-- Resultat visar att endast loggar_2025_02 skannas!
```

**Prestanda**: Queries på partitionerade tabeller kan vara 10-100x snabbare!

### List-partitionering (för kategorier)

```sql
-- Multi-tenant-databas
CREATE TABLE kund_data (
    id BIGSERIAL,
    tenant_id INTEGER,
    data TEXT
) PARTITION BY LIST (tenant_id);

CREATE TABLE kund_data_företag_a PARTITION OF kund_data
    FOR VALUES IN (1, 2, 3);  -- Kund-ID:n för Företag A

CREATE TABLE kund_data_företag_b PARTITION OF kund_data
    FOR VALUES IN (4, 5, 6);  -- Kund-ID:n för Företag B
```

### Hash-partitionering (jämn fördelning)

```sql
CREATE TABLE användare (
    id BIGSERIAL,
    namn VARCHAR(100)
) PARTITION BY HASH (id);

-- Skapa 4 partitioner för jämn fördelning
CREATE TABLE användare_p0 PARTITION OF användare
    FOR VALUES WITH (MODULUS 4, REMAINDER 0);
CREATE TABLE användare_p1 PARTITION OF användare
    FOR VALUES WITH (MODULUS 4, REMAINDER 1);
CREATE TABLE användare_p2 PARTITION OF användare
    FOR VALUES WITH (MODULUS 4, REMAINDER 2);
CREATE TABLE användare_p3 PARTITION OF användare
    FOR VALUES WITH (MODULUS 4, REMAINDER 3);
```

### Automatisk partition-hantering med pg_partman

```sql
-- Installera extension (kräver superuser)
CREATE EXTENSION pg_partman;

-- Konfigurera automatisk skapning av partitioner
SELECT partman.create_parent(
    'public.loggar',
    'skapad_vid',
    'native',
    'monthly',
    p_premake := 3  -- Skapa 3 månaders partitioner i förväg
);

-- Schemalägg automatisk underhåll (via cron)
SELECT partman.run_maintenance();
```

---

## 3. PL/pgSQL: Programmera i databasen

### Stored Functions

```sql
-- Funktion för att beräkna total kundvärde
CREATE OR REPLACE FUNCTION kund_totalt_värde(kund_id_param INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    totalt NUMERIC;
BEGIN
    SELECT COALESCE(SUM(belopp), 0)
    INTO totalt
    FROM beställningar
    WHERE kund_id = kund_id_param;

    RETURN totalt;
END;
$$ LANGUAGE plpgsql;

-- Användning
SELECT namn, kund_totalt_värde(id) AS livstidsvärde
FROM kunder
ORDER BY livstidsvärde DESC
LIMIT 10;
```

### Stored Procedures (PostgreSQL 11+)

```sql
-- Procedure för att arkivera gamla loggar
CREATE OR REPLACE PROCEDURE arkivera_gamla_loggar(månader_gamla INTEGER)
LANGUAGE plpgsql AS $$
DECLARE
    arkiverade_rader INTEGER;
BEGIN
    -- Flytta data till arkivtabell
    INSERT INTO loggar_arkiv
    SELECT * FROM loggar
    WHERE skapad_vid < NOW() - (månader_gamla || ' months')::INTERVAL;

    GET DIAGNOSTICS arkiverade_rader = ROW_COUNT;

    -- Ta bort från huvudtabell
    DELETE FROM loggar
    WHERE skapad_vid < NOW() - (månader_gamla || ' months')::INTERVAL;

    -- Logga resultatet
    RAISE NOTICE 'Arkiverade % rader', arkiverade_rader;

    COMMIT;  -- Procedures kan ha transaktionskontroll!
END;
$$;

-- Kör proceduren
CALL arkivera_gamla_loggar(12);
```

### Triggers: Automatisk logik

```sql
-- Auto-uppdatera modifieringsdatum
CREATE OR REPLACE FUNCTION uppdatera_ändringstid()
RETURNS TRIGGER AS $$
BEGIN
    NEW.uppdaterad_vid = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_uppdatera_ändringstid
BEFORE UPDATE ON produkter
FOR EACH ROW
EXECUTE FUNCTION uppdatera_ändringstid();

-- Audit trigger (spara alla ändringar)
CREATE OR REPLACE FUNCTION audit_ändringar()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_logg (tabell, operation, gamla_data, nya_data, användare)
    VALUES (
        TG_TABLE_NAME,
        TG_OP,
        row_to_json(OLD),
        row_to_json(NEW),
        current_user
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER produkter_audit
AFTER INSERT OR UPDATE OR DELETE ON produkter
FOR EACH ROW EXECUTE FUNCTION audit_ändringar();
```

---

## 4. Row Level Security (RLS): Multi-Tenant säkerhet

### Vad är RLS?
RLS tillämpar automatiska filter på VARJE query baserat på policies. Perfekt för SaaS-applikationer där flera kunder delar samma tabeller.

### Grundläggande RLS-setup

```sql
-- Skapa tabell
CREATE TABLE dokument (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER NOT NULL,
    titel VARCHAR(200),
    innehåll TEXT,
    skapad_av VARCHAR(100)
);

-- Aktivera RLS
ALTER TABLE dokument ENABLE ROW LEVEL SECURITY;

-- Skapa policy: Användare ser bara sin tenants data
CREATE POLICY tenant_isolation ON dokument
    USING (tenant_id = current_setting('app.current_tenant')::INTEGER);

-- För INSERT-operationer
CREATE POLICY tenant_isolation_insert ON dokument
    FOR INSERT
    WITH CHECK (tenant_id = current_setting('app.current_tenant')::INTEGER);
```

### Användning i applikation

```sql
-- I din applikation (t.ex. Node.js, Python):
-- När en användare från tenant 5 loggar in:

-- Sätt session-variabel
SET app.current_tenant = 5;

-- Nu filtreras alla queries automatiskt!
SELECT * FROM dokument;  -- Visar ENDAST tenant 5:s dokument

-- Även JOINs respekterar RLS
SELECT d.titel, u.namn
FROM dokument d
JOIN användare u ON d.skapad_av = u.id;
-- Automatiskt filtrerat till tenant 5!
```

### Avancerade RLS-policies

```sql
-- Olika policies för olika roller
CREATE POLICY admin_full_access ON dokument
    TO admin_role
    USING (true);  -- Admins ser allt

CREATE POLICY user_own_data ON dokument
    TO user_role
    USING (skapad_av = current_user);  -- Användare ser bara sina egna

-- Policy baserad på JSONB-innehåll
CREATE POLICY public_documents ON dokument
    USING ((metadata->>'public')::boolean = true);
```

**2024 Warningar**:
- RLS gäller INTE för superusers eller table owners!
- Komplexa policies kan påverka prestanda – använd index!
- Testa noga – RLS-buggar kan läcka data mellan tenants!

---

## 5. High Availability & Replikering

### Replikeringstyper i PostgreSQL

#### **Streaming Replication (built-in)**
```
┌─────────────┐      WAL Stream       ┌─────────────┐
│   Primary   │ ──────────────────────>│  Replica 1  │
│  (Read/Write)│                       │ (Read-only) │
└─────────────┘                       └─────────────┘
                                            │
                                            v
                                      ┌─────────────┐
                                      │  Replica 2  │
                                      │ (Read-only) │
                                      └─────────────┘
```

**Setup (förenklat)**:
```sql
-- På primary:
ALTER SYSTEM SET wal_level = replica;
ALTER SYSTEM SET max_wal_senders = 3;
CREATE USER replicator REPLICATION LOGIN PASSWORD 'secure_password';

-- På replica (via pg_basebackup):
-- pg_basebackup -h primary_host -U replicator -D /var/lib/postgresql/data -P
```

#### **Logical Replication (PostgreSQL 10+)**
Replikera specifika tabeller till andra databaser. Perfekt för:
- Multi-region setups
- Datawarehouse-feeds
- Migration mellan versioner

```sql
-- På source database
CREATE PUBLICATION my_publication FOR TABLE kunder, beställningar;

-- På destination database
CREATE SUBSCRIPTION my_subscription
    CONNECTION 'host=source_host dbname=sourcedb user=replica_user'
    PUBLICATION my_publication;
```

### Connection Pooling med pgBouncer (2024-2025 Standard)

**Varför?** PostgreSQL skapar en process per connection (dyrt). pgBouncer återanvänder connections.

**Docker setup:**
```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:17
    environment:
      POSTGRES_PASSWORD: secret

  pgbouncer:
    image: edoburu/pgbouncer
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_USER: postgres
      DB_PASSWORD: secret
      POOL_MODE: transaction  # Mest effektivt!
      MAX_CLIENT_CONN: 1000
      DEFAULT_POOL_SIZE: 20
    ports:
      - "6432:6432"
```

**Applikationen ansluter till pgBouncer (port 6432) istället för direkt till PostgreSQL!**

**Resultat**: 1000 klienter → 20 faktiska PostgreSQL-connections. Enorm prestandavinst!

---

## 6. Prestandatuning: Produktionsklar PostgreSQL

### Viktiga konfigurationsparametrar (2024-2025)

```sql
-- Visa aktuella inställningar
SHOW shared_buffers;
SHOW work_mem;

-- Rekommenderade inställningar för moderna servrar (32GB RAM):
ALTER SYSTEM SET shared_buffers = '8GB';          -- 25% av RAM
ALTER SYSTEM SET effective_cache_size = '24GB';   -- 75% av RAM
ALTER SYSTEM SET work_mem = '64MB';               -- Per operation
ALTER SYSTEM SET maintenance_work_mem = '2GB';    -- För VACUUM, CREATE INDEX
ALTER SYSTEM SET random_page_cost = 1.1;          -- För SSD (default 4.0 är för HDD!)
ALTER SYSTEM SET max_connections = 200;
ALTER SYSTEM SET max_wal_size = '4GB';

-- Ladda om konfiguration
SELECT pg_reload_conf();
```

### Index-strategier för produktion

```sql
-- Composite index (ordningen är VIKTIG!)
CREATE INDEX idx_beställningar_kund_datum ON beställningar (kund_id, datum DESC);

-- Bra för:
SELECT * FROM beställningar WHERE kund_id = 42 ORDER BY datum DESC;

-- Partial index (mindre, snabbare)
CREATE INDEX idx_aktiva_produkter ON produkter (namn)
WHERE aktiv = true;  -- Index bara aktiva produkter!

-- Expression index
CREATE INDEX idx_email_lower ON kunder (LOWER(email));

-- Användning:
SELECT * FROM kunder WHERE LOWER(email) = 'anna@example.com';

-- Covering index (index-only scan)
CREATE INDEX idx_produkter_covering ON produkter (kategori) INCLUDE (namn, pris);

-- PostgreSQL läser BARA från index, inte från tabell!
SELECT namn, pris FROM produkter WHERE kategori = 'Elektronik';
```

### Query optimization workflow

1. **Identifiera långsamma queries**
```sql
-- pg_stat_statements extension (MÅSTE-ha för produktion!)
CREATE EXTENSION pg_stat_statements;

-- Topp 10 långsammaste queries
SELECT
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    max_exec_time
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

2. **Analysera med EXPLAIN ANALYZE**
```sql
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
```

3. **Lägg till index där Seq Scan sker på stora tabeller**

4. **Re-mät och verifiera**

### VACUUM & AUTOVACUUM (kritiskt!)

```sql
-- PostgreSQL skapar "dead tuples" vid UPDATE/DELETE
-- VACUUM städar upp dessa

-- Manuell vacuum
VACUUM ANALYZE produkter;

-- Full vacuum (låser tabell, används sällan)
VACUUM FULL produkter;

-- Autovacuum (default ON, men kan behöva justeras)
ALTER TABLE stora_tabellen SET (autovacuum_vacuum_scale_factor = 0.05);
-- Vacuum när 5% av tabellen är dead tuples (default 20%)
```

---

## 7. Modern Arkitektur med PostgreSQL (2024-2025)

### Pattern 1: PostgreSQL med Next.js/React (App Router)

```
┌──────────────┐
│   Next.js    │
│  (App Router)│
│              │
│   Prisma ORM │ ──────> ┌──────────────┐
│  or Drizzle  │         │  pgBouncer   │ ──> ┌──────────────┐
└──────────────┘         └──────────────┘     │ PostgreSQL   │
                                               │   (Neon/     │
                                               │  Supabase)   │
                                               └──────────────┘
```

**Best Practices:**
- Använd Server Components för databasqueries
- Connection pooling via pgBouncer/Neon
- RLS för multi-tenant apps

### Pattern 2: Microservices med delad PostgreSQL

```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Service A  │  │  Service B  │  │  Service C  │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       v                v                v
    ┌──────────────────────────────────────┐
    │       PostgreSQL Database            │
    │  schema_a  │  schema_b  │  schema_c  │
    └──────────────────────────────────────┘
```

**Viktigt**: Använd separata schemas för varje service!

### Pattern 3: CQRS (Command Query Responsibility Segregation)

```
Write Path:               Read Path:
┌──────────┐             ┌──────────────┐
│  App     │             │  Read API    │
│  writes  │             └──────┬───────┘
└────┬─────┘                    │
     v                           v
┌──────────────┐         ┌──────────────────┐
│  PostgreSQL  │ ───────>│  Materialized    │
│  (Primary)   │ Logical │  View / Read     │
│              │ Repl.   │  Replica         │
└──────────────┘         └──────────────────┘
```

---

## 🎯 Övningar

### Övning 1: JSONB för flexibel produktkatalog
Skapa en e-handel där varje produktkategori har olika attribut (t.ex. böcker har "författare", kläder har "storlek").

**Facit:**
```sql
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(200),
    kategori VARCHAR(50),
    pris NUMERIC(10,2),
    attribut JSONB
);

CREATE INDEX idx_produkter_attribut ON produkter USING GIN (attribut);

INSERT INTO produkter (namn, kategori, pris, attribut) VALUES
    ('Clean Code', 'Bok', 299, '{"författare": "Robert Martin", "sidor": 464, "isbn": "9780132350884"}'),
    ('T-shirt', 'Kläder', 199, '{"storlek": "M", "färg": "blå", "material": "bomull"}');

-- Sök böcker av specifik författare
SELECT namn, pris FROM produkter
WHERE kategori = 'Bok' AND attribut @> '{"författare": "Robert Martin"}';

-- Hitta alla kläder i storlek M
SELECT namn FROM produkter
WHERE kategori = 'Kläder' AND attribut->>'storlek' = 'M';
```

### Övning 2: Partitionera en logg-tabell
Skapa en partitionerad tabell för systemloggar och visa hur partition pruning fungerar.

**Facit:**
```sql
CREATE TABLE system_loggar (
    id BIGSERIAL,
    nivå VARCHAR(20),
    meddelande TEXT,
    tidpunkt TIMESTAMP NOT NULL
) PARTITION BY RANGE (tidpunkt);

CREATE TABLE loggar_2025_q1 PARTITION OF system_loggar
    FOR VALUES FROM ('2025-01-01') TO ('2025-04-01');
CREATE TABLE loggar_2025_q2 PARTITION OF system_loggar
    FOR VALUES FROM ('2025-04-01') TO ('2025-07-01');

CREATE INDEX ON system_loggar (tidpunkt);
CREATE INDEX ON system_loggar (nivå);

-- Testa partition pruning
EXPLAIN SELECT * FROM system_loggar
WHERE tidpunkt BETWEEN '2025-02-01' AND '2025-02-28';
-- Visar att BARA loggar_2025_q1 skannas!
```

### Övning 3: Bygg en auto-archiving procedure
Flytta automatiskt gamla rader till arkivtabell.

**Facit:**
```sql
CREATE TABLE orders_active (
    id SERIAL PRIMARY KEY,
    kund_id INTEGER,
    totalt NUMERIC(10,2),
    skapad_datum DATE DEFAULT CURRENT_DATE
);

CREATE TABLE orders_arkiv (LIKE orders_active INCLUDING ALL);

CREATE OR REPLACE PROCEDURE arkivera_gamla_orders(dagar_gamla INTEGER)
LANGUAGE plpgsql AS $$
BEGIN
    WITH flyttade AS (
        DELETE FROM orders_active
        WHERE skapad_datum < CURRENT_DATE - dagar_gamla
        RETURNING *
    )
    INSERT INTO orders_arkiv SELECT * FROM flyttade;

    RAISE NOTICE 'Arkiverade % orders', (SELECT COUNT(*) FROM orders_arkiv);
END;
$$;

-- Schemalägg med pg_cron (extension)
SELECT cron.schedule('0 2 * * *', $$CALL arkivera_gamla_orders(365)$$);
```

### Övning 4: RLS för multi-tenant blogg
Implementera säker tenant-isolation.

**Facit:**
```sql
CREATE TABLE tenants (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100)
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    tenant_id INTEGER REFERENCES tenants(id),
    titel VARCHAR(200),
    innehåll TEXT,
    författare_id INTEGER
);

ALTER TABLE posts ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON posts
    USING (tenant_id = current_setting('app.tenant_id')::INTEGER)
    WITH CHECK (tenant_id = current_setting('app.tenant_id')::INTEGER);

-- Test:
SET app.tenant_id = 1;
SELECT * FROM posts;  -- Visar bara tenant 1:s posts

SET app.tenant_id = 2;
SELECT * FROM posts;  -- Visar bara tenant 2:s posts
```

### Övning 5-8: Case Study - SaaS Analyticsplattform

**Scenario**: Bygg en analysdatabas för en SaaS-app som trackear events från tusentals kunder.

**Krav:**
- Miljontals events per dag
- Queries måste vara snabba (<100ms)
- Varje tenant isolerad
- Auto-arkivering av gammal data

**Facit:**
```sql
-- 1. Partitionerad event-tabell
CREATE TABLE events (
    id BIGSERIAL NOT NULL,
    tenant_id INTEGER NOT NULL,
    event_typ VARCHAR(50),
    user_id INTEGER,
    properties JSONB,
    tidpunkt TIMESTAMP NOT NULL
) PARTITION BY RANGE (tidpunkt);

-- Skapa månatliga partitioner (automatisera med pg_partman!)
CREATE TABLE events_2025_01 PARTITION OF events
    FOR VALUES FROM ('2025-01-01') TO ('2025-02-01');

-- 2. Index för prestanda
CREATE INDEX ON events (tenant_id, tidpunkt DESC);
CREATE INDEX ON events USING GIN (properties);  -- För JSONB-queries

-- 3. RLS för tenant-isolation
ALTER TABLE events ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON events
    USING (tenant_id = current_setting('app.tenant_id')::INTEGER);

-- 4. Materialiserad view för dashboard
CREATE MATERIALIZED VIEW daily_stats AS
SELECT
    tenant_id,
    DATE(tidpunkt) AS datum,
    event_typ,
    COUNT(*) AS antal_events,
    COUNT(DISTINCT user_id) AS unika_användare
FROM events
WHERE tidpunkt > NOW() - INTERVAL '30 days'
GROUP BY tenant_id, DATE(tidpunkt), event_typ;

CREATE INDEX ON daily_stats (tenant_id, datum DESC);

-- Refresh varje natt
SELECT cron.schedule('0 3 * * *', 'REFRESH MATERIALIZED VIEW CONCURRENTLY daily_stats');

-- 5. Auto-arkivering
CREATE TABLE events_arkiv (LIKE events INCLUDING ALL);

CREATE OR REPLACE PROCEDURE arkivera_gamla_events()
LANGUAGE plpgsql AS $$
DECLARE
    cutoff_date DATE := CURRENT_DATE - INTERVAL '90 days';
BEGIN
    -- Drop gamla partitioner (snabbt!)
    EXECUTE format('DROP TABLE IF EXISTS events_%s', to_char(cutoff_date, 'YYYY_MM'));

    RAISE NOTICE 'Arkiverade events före %', cutoff_date;
END;
$$;

-- 6. Query-exempel för applikationen
-- (Partition pruning + RLS + index = supersnabbt!)
SET app.tenant_id = 42;

SELECT
    event_typ,
    COUNT(*) AS antal,
    COUNT(DISTINCT user_id) AS unika_användare
FROM events
WHERE tidpunkt >= NOW() - INTERVAL '7 days'
GROUP BY event_typ
ORDER BY antal DESC;
-- Execution time: <50ms (även med miljoner rader!)
```

---

## 💡 Expert Pro Tips (2024-2025)

1. **pgBouncer är obligatoriskt för serverless** – Annars överbelastar du connection limits.
2. **Använd JSONB för flexibilitet, inte för laziness** – Validera datan i applikationen!
3. **Partition Pruning = gratis prestanda** – Men undvik tusentals små partitioner.
4. **RLS är säkerhet-i-depth** – Komplettera med app-level kontroller.
5. **Monitera pg_stat_statements** – Det är guld för optimering.
6. **VACUUM ANALYZE efter bulk-inserts** – Annars får query planner fel statistik.
7. **Använd connection poolers** – Även om du "bara har 100 användare" (de skapar 1000+ connections).
8. **Test RLS-policies noga** – En bugg kan läcka data mellan tenants!

---

## 🌟 Case Studies (Verkliga Scenarion)

### Case 1: E-handelsplattform (10M produkter, 1M+ users)

**Problem**: Produktsök tog 5+ sekunder.

**Lösning:**
```sql
-- FÖRE: Sequential scan på 10M rader
SELECT * FROM produkter WHERE namn ILIKE '%laptop%';

-- EFTER: Full-text search med GIN index
ALTER TABLE produkter ADD COLUMN searchable tsvector
    GENERATED ALWAYS AS (to_tsvector('swedish', namn || ' ' || beskrivning)) STORED;

CREATE INDEX idx_produkter_fts ON produkter USING GIN (searchable);

SELECT * FROM produkter
WHERE searchable @@ to_tsquery('swedish', 'laptop')
ORDER BY ts_rank(searchable, to_tsquery('swedish', 'laptop')) DESC;
```

**Resultat**: 5000ms → 50ms (100x snabbare!)

---

### Case 2: SaaS-plattform (5000 tenants, SQL injection via AI-genererad SQL)

**Problem**: AI-agent genererade SQL som läckte data mellan tenants.

**Lösning:**
```sql
-- Implementera RLS på ALLA tabeller
ALTER TABLE dokument ENABLE ROW LEVEL SECURITY;
ALTER TABLE filer ENABLE ROW LEVEL SECURITY;
ALTER TABLE användare ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON dokument
    USING (tenant_id = current_setting('app.tenant_id')::INTEGER);

-- Även om AI:n genererar:
-- SELECT * FROM dokument WHERE 1=1;
-- Ser användaren BARA sin tenants data!
```

**Resultat**: 0 data leaks efter implementering (2024 statistik).

---

### Case 3: Analytics-startup (skalningsproblem)

**Problem**: 10M events/dag, queries blev långsammare varje vecka.

**Lösning:**
1. **Partitionering per vecka**
2. **Auto-drop gamla partitioner**
3. **Materialiserade views för aggregerade data**
4. **pgBouncer transaction pooling**

**Resultat**:
- Query-tid stabil (50-100ms) oavsett datamängd
- Infrastrukturkostnad -60% (mindre storage, mindre compute)

---

## Sammanfattning: Du är nu PostgreSQL-expert! 🎓

✅ **JSONB**: NoSQL-flexibilitet i relationsdatabasen
✅ **Partitionering**: Skala till miljarder rader med maintained prestanda
✅ **PL/pgSQL**: Automatisera med functions, procedures och triggers
✅ **RLS**: Säker multi-tenant-isolation på databasnivå
✅ **Replikering**: High availability med streaming/logical replication
✅ **Connection Pooling**: pgBouncer för effektiv resurshantering
✅ **Prestandatuning**: Index-strategier, EXPLAIN, VACUUM, konfiguration
✅ **Modern Arkitektur**: PostgreSQL i moderna stacks (Next.js, microservices)

**Nya ord (Ordlista):**
- **JSONB**: Binärt JSON-format för semi-strukturerad data
- **Partitionering**: Dela upp stora tabeller i mindre hanterbara delar
- **Partition Pruning**: Automatisk optimering där irrelevanta partitioner skippas
- **PL/pgSQL**: PostgreSQL:s procedurspråk för stored logic
- **RLS (Row Level Security)**: Automatiska säkerhetsfilter på rad-nivå
- **Tenant**: Kund i en multi-tenant-applikation
- **Streaming Replication**: Kontinuerlig kopiering av WAL till replicas
- **Logical Replication**: Replikering på tabell-nivå (mer flexibel)
- **pgBouncer**: Lightweight connection pooler
- **Connection Pooling**: Återanvändning av databasconnections
- **pg_stat_statements**: Extension för query-statistik
- **VACUUM**: Process som städar upp dead tuples
- **Full-Text Search**: Sök i text med relevansrankning
- **GIN Index**: Generalized Inverted Index (för JSONB, arrays, full-text)
- **Materialized View**: Fysiskt lagrad vy för komplexa aggregeringar
- **pg_partman**: Extension för automatisk partition-hantering
- **pg_cron**: Extension för schemalagda jobb i PostgreSQL

---

## Vart går du härifrån?

Du har nu gått från nybörjare till expert på ~3 timmar! Här är nästa steg:

### Fortsätt lära
- **PostgreSQL Officiell Dokumentation**: https://www.postgresql.org/docs/
- **PostgREST**: Bygg RESTful APIs direkt från PostgreSQL
- **Supabase**: PostgreSQL som BaaS (Backend-as-a-Service)
- **Citus**: Distribuerad PostgreSQL för massiv skalning

### Bygg projekt
- Multi-tenant SaaS-app med RLS
- Real-time analytics-plattform med partitionering
- E-handel med full-text search och JSONB
- Microservices med delad PostgreSQL

### Certifiering
- PostgreSQL Professional Certification (2024+)
- EDB (EnterpriseDB) Certified Professional

---

**GRATTIS! Du är nu en fullfjädrad PostgreSQL-expert! 🚀🎉**

Du har lärt dig allt från de allra enklaste grunderna till avancerade produktionstekniker. PostgreSQL är ett av de mest kraftfulla verktygen i en utvecklares arsenal – använd din nya kunskap väl!

---

**Läsningstid**: ~30 minuter
**Nivå**: 5/5 (Expert/Masternivå)
**Totalt**: ~1.5-3 timmar för hela guiden (Nivå 1-5)

**Din PostgreSQL-resa är komplett! 🏆**
