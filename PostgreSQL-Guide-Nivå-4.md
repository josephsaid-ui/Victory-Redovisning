# PostgreSQL från Noll till Expert
## Nivå 4: "Universitetsnivå" - Avancerade koncept 🏛️

### Introduktion
Välkommen till den avancerade nivån! Här lämnar vi nybörjarterritoriet och går djupt in i hur PostgreSQL verkligen fungerar under huven. Du kommer att förstå transaktioner och ACID-egenskaper, lära dig hur index accelererar queries, förstå query planner, designa databaser med normalisering, och hantera säkerhet. Efter denna nivå har du teoretisk och praktisk kunskap som gör att du kan arbeta professionellt med PostgreSQL. Detta är nivån där du går från användare till expert!

---

## 1. Transaktioner & ACID-egenskaper

### Vad är en transaktion?
En **transaktion** är en sekvens av operationer som behandlas som EN enda enhet. Antingen lyckas ALLT, eller så MISSLYCKAS allt och ingenting ändras.

**Verkligt scenario**: Överföring av pengar mellan bankkonton
```sql
-- Utan transaktion (FARLIGT!)
UPDATE konton SET saldo = saldo - 1000 WHERE konto_id = 1;
-- Vad händer om systemet kraschar HÄR? ↓
UPDATE konton SET saldo = saldo + 1000 WHERE konto_id = 2;
-- Person 1 förlorade 1000 kr, men person 2 fick dem aldrig!

-- Med transaktion (SÄKERT!)
BEGIN;
UPDATE konton SET saldo = saldo - 1000 WHERE konto_id = 1;
UPDATE konton SET saldo = saldo + 1000 WHERE konto_id = 2;
COMMIT;  -- Båda operationerna lyckas, eller ingen av dem
```

### ACID-egenskaperna (varför PostgreSQL är pålitligt)

#### **A = Atomicity (Atomärhet)**
Transaktionen är "allt eller inget". Inga halva transaktioner.

```sql
BEGIN;
INSERT INTO beställningar (kund_id, produkt) VALUES (1, 'Laptop');
INSERT INTO lager (produkt, antal) VALUES ('Laptop', -1);  -- Fel! Negativt antal
ROLLBACK;  -- Ångrar BÅDA operationerna
```

#### **C = Consistency (Konsekvens)**
Databasen går från ett giltigt tillstånd till ett annat giltigt tillstånd. Alla regler (constraints) respekteras.

```sql
-- Om en regel säger "saldo får inte vara negativt"
UPDATE konton SET saldo = -500 WHERE id = 1;  -- AVVISAS automatiskt
```

#### **I = Isolation (Isolering)**
Transaktioner påverkar inte varandra, även om de körs samtidigt.

**Isolationsnivåer i PostgreSQL:**

| Nivå              | Dirty Read | Non-Repeatable Read | Phantom Read | PostgreSQL Default |
|-------------------|------------|---------------------|--------------|-------------------|
| Read Uncommitted  | ✗          | Möjlig              | Möjlig       | ✗                 |
| Read Committed    | ✗          | Möjlig              | Möjlig       | **✓ (Standard)**  |
| Repeatable Read   | ✗          | ✗                   | Möjlig       | ✓                 |
| Serializable      | ✗          | ✗                   | ✗            | ✓                 |

```sql
-- Sätt isolationsnivå för en transaktion
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT * FROM konton WHERE id = 1;
-- Även om någon annan ändrar detta konto nu, ser vi samma värde
SELECT * FROM konton WHERE id = 1;  -- Samma resultat!
COMMIT;
```

**Viktigt 2024-2025**: PostgreSQL använder **MVCC (Multi-Version Concurrency Control)**, vilket betyder att varje transaktion ser en "ögonblicksbild" av databasen. Detta ger hög prestanda utan att låsa tabeller!

#### **D = Durability (Hållbarhet)**
När en transaktion är committad, är den **permanent**. Även vid strömavbrott.

PostgreSQL använder **WAL (Write-Ahead Logging)**: alla ändringar skrivs först till en logg innan de tillämpas. Vid krasch spelas loggen upp.

---

## 2. Index: Accelerera dina queries

### Varför index?
Utan index måste PostgreSQL läsa VARJE rad (sequential scan). Med index hittar den direkt rätt rader.

**Analogi**: Att hitta en bok i biblioteket
- **Utan index**: Gå genom varje hylla och kolla varje bok (långsamt!)
- **Med index**: Slå upp i katalogen, gå direkt till rätt hylla (snabbt!)

### B-tree Index (Standard i PostgreSQL)

B-tree (Balanced Tree) är default-indextypen. Perfekt för:
- Jämförelser: `=`, `<`, `>`, `<=`, `>=`, `BETWEEN`
- Sortering: `ORDER BY`
- Pattern matching: `LIKE 'foo%'` (men inte `LIKE '%foo'`)

```sql
-- Skapa index
CREATE INDEX idx_kunder_email ON kunder(email);

-- Multi-kolumn index
CREATE INDEX idx_beställningar_datum_kund ON beställningar(datum, kund_id);

-- Unique index (automatiskt för PRIMARY KEY och UNIQUE)
CREATE UNIQUE INDEX idx_users_username ON users(username);
```

**Hur B-tree fungerar (förenklat):**
```
         [Erik, Lisa]
        /      |      \
   [Anna]  [Erik,Johan] [Lisa,Sara]
     |        |    |       |     |
   Anna    Erik Johan   Lisa  Sara
```
Istället för att kolla 5 namn, behöver vi bara 2-3 steg!

### Andra indextyper

```sql
-- Hash index (bara för =, snabbare än B-tree för exakta matchningar)
CREATE INDEX idx_hash ON tabell USING HASH (kolumn);

-- GIN (Generalized Inverted Index) - perfekt för JSONB, arrays, full-text
CREATE INDEX idx_jsonb ON produkter USING GIN (egenskaper);

-- GiST (för geografisk data, range-typer)
CREATE INDEX idx_location ON platser USING GIST (koordinater);
```

### När ska man INTE använda index?

❌ Små tabeller (< 1000 rader) – sequential scan är snabbare
❌ Kolumner med få unika värden (t.ex. boolean true/false)
❌ Kolumner som sällan används i WHERE/JOIN
❌ Tabeller med mycket INSERT/UPDATE (index bromsar skrivningar)

**Gyllene regel 2024**: Mät först, optimera sen! Använd EXPLAIN ANALYZE.

---

## 3. Query Planner & EXPLAIN

### Vad är Query Planner?
När du skickar en query, analyserar PostgreSQL den och skapar en **execution plan** (exekveringsplan) – den mest effektiva vägen att hämta data.

### EXPLAIN - Din bästa vän för optimering

```sql
-- Se planen (utan att köra queryn)
EXPLAIN SELECT * FROM kunder WHERE ålder > 30;

-- Kör queryn OCH se faktiska tider
EXPLAIN ANALYZE SELECT * FROM kunder WHERE ålder > 30;
```

**Exempel-output:**
```
Seq Scan on kunder  (cost=0.00..35.50 rows=500 width=100) (actual time=0.012..0.123 rows=487 loops=1)
  Filter: (ålder > 30)
  Rows Removed by Filter: 513
Planning Time: 0.084 ms
Execution Time: 0.145 ms
```

**Viktiga termer:**
- **Seq Scan** (Sequential Scan): Läser hela tabellen (långsamt för stora tabeller)
- **Index Scan**: Använder index (snabbare)
- **Bitmap Index Scan**: Kombinerar flera index
- **cost**: Uppskattad kostnad (planerar-enhet, inte tid)
- **rows**: Uppskattat/faktiskt antal rader
- **actual time**: Faktisk exekveringstid (endast med ANALYZE)

### Före och efter index

```sql
-- FÖRE index
EXPLAIN ANALYZE SELECT * FROM beställningar WHERE kund_id = 42;
-- Resultat: Seq Scan, 245ms

-- Skapa index
CREATE INDEX idx_beställningar_kund ON beställningar(kund_id);

-- EFTER index
EXPLAIN ANALYZE SELECT * FROM beställningar WHERE kund_id = 42;
-- Resultat: Index Scan, 2ms (122x snabbare!)
```

---

## 4. Normalisering: Designa databaser rätt

### Vad är normalisering?
Att organisera data för att **minska redundans** och **öka dataintegritet**.

**Statistik 2024**:
- Organisationer som följer 1NF ser 35% minskning i kostnad för datakorrigering
- 2NF minskar uppdateringsanomalier med 60%
- 3NF minskar dataanomalier med 65%

### De tre viktigaste normalformerna

#### **1NF (First Normal Form)**: Atomära värden

❌ **Fel** (flera värden i en cell):
```
┌────┬────────┬──────────────────┐
│ ID │ Namn   │ Telefonnummer    │
├────┼────────┼──────────────────┤
│ 1  │ Anna   │ 070-111, 070-222 │  ← FEL!
└────┴────────┴──────────────────┘
```

✅ **Rätt** (en cell = ett värde):
```
┌────┬────────┬───────────────┐
│ ID │ Namn   │ Telefonnummer │
├────┼────────┼───────────────┤
│ 1  │ Anna   │ 070-111       │
│ 1  │ Anna   │ 070-222       │
└────┴────────┴───────────────┘
```

#### **2NF**: Inga partiella beroenden

**Problem**: Attribut beror bara på DEL av primärnyckeln.

❌ **Fel**:
```sql
-- Primärnyckel: (kurs_id, student_id)
CREATE TABLE kurs_registreringar (
    kurs_id INT,
    student_id INT,
    kurs_namn VARCHAR(100),  -- Beror bara på kurs_id! (partiellt beroende)
    betyg CHAR(1),
    PRIMARY KEY (kurs_id, student_id)
);
```

✅ **Rätt** (dela upp i två tabeller):
```sql
CREATE TABLE kurser (
    kurs_id INT PRIMARY KEY,
    kurs_namn VARCHAR(100)
);

CREATE TABLE registreringar (
    kurs_id INT REFERENCES kurser(kurs_id),
    student_id INT REFERENCES studenter(student_id),
    betyg CHAR(1),
    PRIMARY KEY (kurs_id, student_id)
);
```

#### **3NF**: Inga transitiva beroenden

**Problem**: Attribut beror på annat icke-nyckel-attribut.

❌ **Fel**:
```sql
CREATE TABLE anställda (
    id INT PRIMARY KEY,
    namn VARCHAR(100),
    avdelning VARCHAR(50),
    avdelningschef VARCHAR(100)  -- Beror på avdelning, inte på id! (transitivt)
);
```

✅ **Rätt**:
```sql
CREATE TABLE avdelningar (
    namn VARCHAR(50) PRIMARY KEY,
    chef VARCHAR(100)
);

CREATE TABLE anställda (
    id INT PRIMARY KEY,
    namn VARCHAR(100),
    avdelning VARCHAR(50) REFERENCES avdelningar(namn)
);
```

### När ska man DENORMALISERA?

I vissa fall är det OK att bryta mot normalisering för **prestanda**:
- Read-heavy applikationer (läser mycket, skriver lite)
- Rapporter och analytics
- Cachat data

**Exempel**: E-handel – lagra `totalt_pris` direkt istället för att räkna ut från order_items varje gång.

---

## 5. Constraints: Affärsregler i databasen

### Alla typer av constraints

```sql
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,

    -- NOT NULL: Måste ha värde
    namn VARCHAR(100) NOT NULL,

    -- UNIQUE: Inga dubbletter
    sku VARCHAR(50) UNIQUE NOT NULL,

    -- CHECK: Egen validering
    pris NUMERIC(10,2) CHECK (pris > 0),
    lager INTEGER CHECK (lager >= 0),

    -- DEFAULT: Standardvärde
    skapad_datum TIMESTAMP DEFAULT NOW(),
    aktiv BOOLEAN DEFAULT true,

    -- FOREIGN KEY: Referens till annan tabell
    kategori_id INTEGER REFERENCES kategorier(id) ON DELETE SET NULL
);

-- CHECK med flera kolumner
ALTER TABLE events ADD CONSTRAINT check_dates
    CHECK (slut_datum >= start_datum);

-- EXCLUDE: Förhindra överlappningar (avancerat!)
CREATE TABLE bokningar (
    rum_id INTEGER,
    under TSRANGE,
    EXCLUDE USING GIST (rum_id WITH =, under WITH &&)
);
-- Förhindrar att samma rum bokas för överlappande tider!
```

---

## 6. Views & Materialiserade Views

### Views (Virtuella tabeller)

```sql
-- Skapa en view
CREATE VIEW aktiva_kunder AS
SELECT id, namn, email
FROM kunder
WHERE aktiv = true AND sista_inloggning > NOW() - INTERVAL '6 months';

-- Använd som vanlig tabell
SELECT * FROM aktiva_kunder;
```

Views beräknas varje gång du frågar efter dem (ingen data lagras).

### Materialiserade Views (Cachade resultat)

```sql
-- Skapa materialiserad view
CREATE MATERIALIZED VIEW månatlig_försäljning AS
SELECT
    DATE_TRUNC('month', datum) AS månad,
    SUM(belopp) AS total_försäljning,
    COUNT(*) AS antal_orders
FROM beställningar
GROUP BY månad;

-- Använd den
SELECT * FROM månatlig_försäljning;

-- Uppdatera när data ändrats
REFRESH MATERIALIZED VIEW månatlig_försäljning;

-- Uppdatera utan att blockera läsningar (PostgreSQL 9.4+)
REFRESH MATERIALIZED VIEW CONCURRENTLY månatlig_försäljning;
```

**När använda materialiserade views?**
- Komplexa aggregationer som tar lång tid
- Rapporter som inte behöver realtidsdata
- Dashboard-statistik

---

## 7. Säkerhet: Roller & Rättigheter

### Roller (Users & Groups)

```sql
-- Skapa roller
CREATE ROLE app_read_only;
CREATE ROLE app_full_access;
CREATE ROLE john LOGIN PASSWORD 'säkert_lösenord';

-- Ge rättigheter
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_read_only;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_full_access;

-- Tilldela roll till användare
GRANT app_read_only TO john;

-- Återkalla rättigheter
REVOKE SELECT ON kunder FROM john;
```

### Principle of Least Privilege (2024 Best Practice)

```sql
-- App-användare ska INTE ha superuser-rättigheter!
CREATE ROLE webapp_user LOGIN PASSWORD 'strong_password';

-- Ge endast nödvändiga rättigheter
GRANT CONNECT ON DATABASE webshop TO webapp_user;
GRANT SELECT, INSERT, UPDATE ON kunder TO webapp_user;
GRANT SELECT, INSERT ON beställningar TO webapp_user;
-- DELETE är INTE tillåtet!

-- För känslig data, använd column-level permissions
GRANT SELECT (id, namn, email) ON kunder TO webapp_user;
-- Personnummer-kolumnen är INTE tillgänglig
```

---

## 🎯 Övningar

### Övning 1: Transaktion med rollback
Skapa en transaktion som:
1. Lägger till en ny kund
2. Lägger till en beställning för den kunden
3. ROLLBACK om beställningens pris är negativt

**Facit:**
```sql
BEGIN;

INSERT INTO kunder (namn, email) VALUES ('Test Kund', 'test@example.com')
RETURNING id AS kund_id;  -- Antag vi får id = 99

INSERT INTO beställningar (kund_id, produkt, pris) VALUES
(99, 'Testprodukt', -100);  -- NEGATIVT PRIS!

-- Upptäck felet (i verkligheten skulle CHECK constraint stoppa detta)
ROLLBACK;

-- Verifiera att kunden INTE finns
SELECT * FROM kunder WHERE id = 99;  -- Tomt resultat
```

### Övning 2: Skapa och testa index
1. Skapa en tabell med 10,000 rader
2. Mät querytid med EXPLAIN ANALYZE
3. Lägg till index
4. Mät igen och jämför

**Facit:**
```sql
-- 1. Skapa testdata
CREATE TABLE test_produkter (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100),
    kategori VARCHAR(50),
    pris NUMERIC(10,2)
);

INSERT INTO test_produkter (namn, kategori, pris)
SELECT
    'Produkt ' || i,
    CASE WHEN i % 3 = 0 THEN 'Elektronik'
         WHEN i % 3 = 1 THEN 'Kläder'
         ELSE 'Böcker' END,
    (RANDOM() * 1000)::NUMERIC(10,2)
FROM generate_series(1, 10000) AS i;

-- 2. FÖRE index
EXPLAIN ANALYZE SELECT * FROM test_produkter WHERE kategori = 'Elektronik';
-- Execution Time: ~5ms (Seq Scan)

-- 3. Skapa index
CREATE INDEX idx_kategori ON test_produkter(kategori);

-- 4. EFTER index
EXPLAIN ANALYZE SELECT * FROM test_produkter WHERE kategori = 'Elektronik';
-- Execution Time: ~0.5ms (Index Scan) – 10x snabbare!
```

### Övning 3: Normalisera en dålig design
Omvandla denna icke-normaliserade tabell till 3NF:

```sql
-- FÖRE (alla normaliseringsfel!)
CREATE TABLE orders_denormalized (
    order_id INT,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    customer_city VARCHAR(50),
    products TEXT,  -- "Laptop, Mus, Tangentbord"
    order_date DATE
);
```

**Facit:**
```sql
-- 3NF-design
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    order_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE order_items (
    order_id INTEGER REFERENCES orders(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (order_id, product_id)
);
```

### Övning 4: Isolationsnivåer
Testa skillnaden mellan Read Committed och Repeatable Read.

**Facit:**
```sql
-- Terminal 1: Read Committed (default)
BEGIN;
SELECT saldo FROM konton WHERE id = 1;  -- Resultat: 1000

-- Terminal 2: Uppdatera samtidigt
UPDATE konton SET saldo = 2000 WHERE id = 1;
COMMIT;

-- Terminal 1: Läs igen
SELECT saldo FROM konton WHERE id = 1;  -- Resultat: 2000 (ändringen syns!)
COMMIT;

---

-- Terminal 1: Repeatable Read
BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT saldo FROM konton WHERE id = 1;  -- Resultat: 1000

-- Terminal 2: Uppdatera
UPDATE konton SET saldo = 2000 WHERE id = 1;
COMMIT;

-- Terminal 1: Läs igen
SELECT saldo FROM konton WHERE id = 1;  -- Resultat: 1000 (oförändrat!)
COMMIT;
```

### Övning 5: Materialiserad view för rapporter
Skapa en rapportvy för totala försäljningar per kategori.

**Facit:**
```sql
CREATE MATERIALIZED VIEW kategori_rapport AS
SELECT
    p.kategori,
    COUNT(*) AS antal_ordrar,
    SUM(oi.quantity * p.pris) AS total_försäljning
FROM order_items oi
JOIN products p ON oi.product_id = p.id
GROUP BY p.kategori
ORDER BY total_försäljning DESC;

-- Använd den
SELECT * FROM kategori_rapport;

-- Schemalägg refresh (kör från cron eller pg_cron)
REFRESH MATERIALIZED VIEW CONCURRENTLY kategori_rapport;
```

### Övning 6-10: Mini-projekt – Klinikbokningssystem

**Scenario**: Designa en databas för en klinik där:
- Patienter kan boka tider hos läkare
- Läkare har specifika arbetstider
- Inga dubbelbokningar tillåts
- Logg alla ändringar

**Facit:**

```sql
-- 1. Skapa tabeller (3NF)
CREATE TABLE läkare (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100) NOT NULL,
    specialisering VARCHAR(50)
);

CREATE TABLE patienter (
    id SERIAL PRIMARY KEY,
    personnummer CHAR(11) UNIQUE NOT NULL,
    namn VARCHAR(100) NOT NULL,
    telefon VARCHAR(15)
);

CREATE TABLE bokningar (
    id SERIAL PRIMARY KEY,
    läkare_id INTEGER REFERENCES läkare(id),
    patient_id INTEGER REFERENCES patienter(id),
    starttid TIMESTAMP NOT NULL,
    sluttid TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'bokad',
    CONSTRAINT check_tider CHECK (sluttid > starttid),
    CONSTRAINT no_overlap EXCLUDE USING GIST (
        läkare_id WITH =,
        tsrange(starttid, sluttid) WITH &&
    )
);

-- 2. Skapa audit-logg
CREATE TABLE bokningar_audit (
    id SERIAL PRIMARY KEY,
    bokning_id INTEGER,
    operation VARCHAR(10),
    ändrad_av VARCHAR(50),
    tidpunkt TIMESTAMP DEFAULT NOW(),
    gamla_data JSONB,
    nya_data JSONB
);

-- 3. Trigger för automatisk loggning
CREATE OR REPLACE FUNCTION log_booking_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO bokningar_audit (bokning_id, operation, gamla_data)
        VALUES (OLD.id, 'DELETE', row_to_json(OLD)::jsonb);
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO bokningar_audit (bokning_id, operation, gamla_data, nya_data)
        VALUES (NEW.id, 'UPDATE', row_to_json(OLD)::jsonb, row_to_json(NEW)::jsonb);
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO bokningar_audit (bokning_id, operation, nya_data)
        VALUES (NEW.id, 'INSERT', row_to_json(NEW)::jsonb);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER booking_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON bokningar
FOR EACH ROW EXECUTE FUNCTION log_booking_changes();

-- 4. Index för prestanda
CREATE INDEX idx_bokningar_läkare ON bokningar(läkare_id);
CREATE INDEX idx_bokningar_patient ON bokningar(patient_id);
CREATE INDEX idx_bokningar_datum ON bokningar(starttid);

-- 5. View för kommande bokningar
CREATE VIEW kommande_bokningar AS
SELECT
    p.namn AS patient,
    l.namn AS läkare,
    l.specialisering,
    b.starttid,
    b.sluttid,
    b.status
FROM bokningar b
JOIN patienter p ON b.patient_id = p.id
JOIN läkare l ON b.läkare_id = l.id
WHERE b.starttid > NOW() AND b.status != 'avbokad'
ORDER BY b.starttid;

-- 6. Roller för säkerhet
CREATE ROLE reception_staff;
GRANT SELECT, INSERT, UPDATE ON bokningar TO reception_staff;
GRANT SELECT ON läkare, patienter TO reception_staff;

CREATE ROLE läkare_role;
GRANT SELECT ON bokningar, patienter TO läkare_role;
-- Läkare kan INTE ändra bokningar själva
```

---

## 💡 Pro Tips

1. **Transaktioner är gratis prestanda-mässigt** – Använd dem generöst för dataintegritet!
2. **Index är inte gratis** – Varje index bromsar INSERT/UPDATE. Ha max 5-7 index per tabell.
3. **EXPLAIN ANALYZE är din bästa vän** – Gissa aldrig, mät alltid!
4. **Normalisera först, denormalisera medvetet** – Starta med 3NF, bryt reglerna endast när prestandamätningar kräver det.
5. **MVCC = bra** – PostgreSQL låser sällan, vilket ger excellent prestanda för läsningar.
6. **Använd TIMESTAMPTZ, inte TIMESTAMP** – Spara alltid med tidszon!

---

## Sammanfattning: Vad har du lärt dig?

✅ **ACID**: Atomicity, Consistency, Isolation, Durability – grunden för pålitliga transaktioner
✅ **Transaktioner**: BEGIN, COMMIT, ROLLBACK för att gruppera operationer
✅ **Isolationsnivåer**: Read Committed, Repeatable Read, Serializable
✅ **Index**: B-tree (standard), Hash, GIN, GiST för snabbare queries
✅ **EXPLAIN**: Verktyg för att förstå och optimera query-prestanda
✅ **Normalisering**: 1NF (atomära värden), 2NF (inga partiella beroenden), 3NF (inga transitiva beroenden)
✅ **Constraints**: NOT NULL, UNIQUE, CHECK, FOREIGN KEY, EXCLUDE
✅ **Views**: Virtuella tabeller för kodåteranvändning
✅ **Materialiserade Views**: Cachade resultat för komplexa queries
✅ **Säkerhet**: Roller, rättigheter, principle of least privilege

**Nya ord (Ordlista):**
- **ACID**: Atomicity, Consistency, Isolation, Durability
- **Transaktion**: Grupperad sekvens av operationer (allt eller inget)
- **MVCC**: Multi-Version Concurrency Control (PostgreSQL's concurrency-system)
- **WAL**: Write-Ahead Logging (säkerställer durability)
- **Index**: Datastruktur för snabbare sökningar
- **B-tree**: Balanced tree, standard indextyp
- **Sequential Scan**: Läsning av hela tabellen rad för rad
- **Query Planner**: PostgreSQL-komponent som optimerar queries
- **Normalisering**: Process för att minska redundans
- **1NF/2NF/3NF**: Normalformer för databasdesign
- **Denormalisering**: Medvetet bryta normaliseringsregler för prestanda
- **View**: Virtuell tabell (sparar inte data)
- **Materialized View**: Fysiskt sparad vy (cache)
- **Constraint**: Regel för datavalidering
- **Role**: Användare eller grupp med specifika rättigheter

---

### Nästa steg: Nivå 5! 💼

Du har nu teoretisk grund och avancerad förståelse! I sista nivån går vi in på expert-territorium: avancerad JSONB, partitionering, stored procedures, row-level security, replikering, och produktionsklara optimeringar. Detta är nivån där du blir PostgreSQL-expert!

Fantastiskt jobbat att komma så här långt! 🎉

---

**Läsningstid**: ~25 minuter
**Nivå**: 4/5 (Avancerad/Universitetsnivå)
**Nästa nivå**: Expert (Masternivå)
