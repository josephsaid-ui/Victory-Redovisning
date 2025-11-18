# PostgreSQL från Noll till Expert
## Nivå 3: "Gymnasiet" - Kom igång med riktig PostgreSQL 🎓

### Introduktion
Nu är det dags att faktiskt börja använda PostgreSQL! På denna nivå kommer du att lära dig hur du installerar och kör PostgreSQL, hur du skapar din första databas och tabeller, och hur du skriver riktiga SQL-kommandon. Detta är steget där teori blir praktik, och där du börjar bygga verkliga databaser. Efter denna nivå kommer du att kunna skapa enkla men funktionella databassystem!

---

## Komma igång: Installation & Verktyg

### Tre sätt att få PostgreSQL (välj ett!)

#### 1. **Docker** (REKOMMENDERAT för nybörjare 2024-2025)
Snabbast och enklast, kräver att Docker är installerat:

```bash
# Skapa en volym för att spara data permanent
docker volume create postgres-data

# Starta PostgreSQL-container
docker run --name my-postgres \
  -e POSTGRES_PASSWORD=mittlösenord \
  -e POSTGRES_USER=minuser \
  -e POSTGRES_DB=mindb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  -d postgres:17

# Anslut till databasen
docker exec -it my-postgres psql -U minuser -d mindb
```

**Fördelar**: Isolerat, enkelt att ta bort och börja om, fungerar likadant på Windows/Mac/Linux.

#### 2. **Lokal installation**
- **Windows**: Ladda ner från postgresql.org/download
- **Mac**: `brew install postgresql@17`
- **Linux**: `apt install postgresql postgresql-contrib` (Ubuntu/Debian)

#### 3. **Molntjänster** (för produktion senare)
- Neon.tech (gratis tier, perfekt för tester)
- Supabase (PostgreSQL + extras)
- Railway.app, Render.com

---

### Verktyg för att prata med PostgreSQL

#### **psql** - Kommandoradsgränssnittet
Det officiella CLI-verktyget. Snabbt och kraftfullt, men kräver terminalkunskap.

```bash
# Anslut till lokal databas
psql -U postgres

# Visa alla databaser
\l

# Byt till en databas
\c mindb

# Visa alla tabeller
\dt

# Avsluta
\q
```

#### **pgAdmin** - Grafiskt gränssnitt
Perfekt för nybörjare som vill se tabeller visuellt och skriva queries i en editor.

```bash
# Kör pgAdmin i Docker (separat container)
docker run -p 5050:80 \
  -e "PGADMIN_DEFAULT_EMAIL=user@example.com" \
  -e "PGADMIN_DEFAULT_PASSWORD=admin" \
  -d dpage/pgadmin4

# Öppna http://localhost:5050 i webbläsaren
```

**Andra populära GUI-verktyg**: DBeaver, TablePlus, DataGrip

---

## Grundläggande SQL: CRUD-operationer

CRUD står för **Create, Read, Update, Delete** – de fyra grundläggande operationerna.

### 1. CREATE - Skapa databas och tabeller

```sql
-- Skapa en ny databas (kör bara om du inte redan har en)
CREATE DATABASE webshop;

-- Byt till databasen (i psql: \c webshop)

-- Skapa din första tabell
CREATE TABLE kunder (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    ålder INTEGER CHECK (ålder >= 18),
    registrerad_datum DATE DEFAULT CURRENT_DATE
);
```

**Förklaring:**
- `SERIAL`: Auto-inkrementerande ID (1, 2, 3, ...)
- `PRIMARY KEY`: Gör `id` till primärnyckel
- `VARCHAR(100)`: Text upp till 100 tecken
- `NOT NULL`: Får inte vara tom
- `UNIQUE`: Inga dubbletter tillåtna
- `CHECK`: Validering (endast 18+)
- `DEFAULT`: Sätts automatiskt om inget anges

---

### 2. INSERT - Lägg till data

```sql
-- Lägg till en kund
INSERT INTO kunder (namn, email, ålder)
VALUES ('Anna Svensson', 'anna@example.com', 25);

-- Lägg till flera samtidigt
INSERT INTO kunder (namn, email, ålder) VALUES
    ('Erik Johansson', 'erik@example.com', 32),
    ('Lisa Berg', 'lisa@example.com', 28),
    ('Johan Nilsson', 'johan@example.com', 45);

-- Returnera den nya raden (PostgreSQL-specifik feature!)
INSERT INTO kunder (namn, email, ålder)
VALUES ('Sara Lundgren', 'sara@example.com', 22)
RETURNING *;
```

---

### 3. SELECT - Hämta data (READ)

```sql
-- Hämta allt
SELECT * FROM kunder;

-- Hämta specifika kolumner
SELECT namn, email FROM kunder;

-- Filtrera med WHERE
SELECT * FROM kunder WHERE ålder > 30;

-- Flera villkor
SELECT namn FROM kunder
WHERE ålder >= 25 AND email LIKE '%example.com';

-- Sortera
SELECT * FROM kunder ORDER BY ålder DESC;

-- Begränsa antal resultat
SELECT * FROM kunder LIMIT 3;

-- Räkna rader
SELECT COUNT(*) FROM kunder;
SELECT COUNT(*) FROM kunder WHERE ålder >= 30;
```

---

### 4. UPDATE - Uppdatera befintlig data

```sql
-- Uppdatera en kunds email
UPDATE kunder
SET email = 'anna.ny@example.com'
WHERE id = 1;

-- Uppdatera flera kolumner
UPDATE kunder
SET namn = 'Anna Svensson-Berg', ålder = 26
WHERE email = 'anna.ny@example.com';

-- Uppdatera alla som uppfyller ett villkor
UPDATE kunder
SET ålder = ålder + 1
WHERE ålder < 30;
```

**VARNING**: Glöm aldrig `WHERE`! Annars uppdateras ALLA rader!

---

### 5. DELETE - Ta bort data

```sql
-- Ta bort en specifik kund
DELETE FROM kunder WHERE id = 5;

-- Ta bort alla under 20 år (kom ihåg CHECK-constraint!)
DELETE FROM kunder WHERE ålder < 20;

-- TA BORT ALLT (använd med EXTREM försiktighet!)
DELETE FROM kunder;  -- Töm tabellen
```

---

## PostgreSQL Datatyper (de viktigaste)

### **Text**
- `VARCHAR(n)`: Text med maxlängd n
- `TEXT`: Obegränsad text
- `CHAR(n)`: Fast längd (fylls med mellanslag)

### **Nummer**
- `INTEGER` / `INT`: Heltal (-2.1 miljarder till +2.1 miljarder)
- `BIGINT`: Större heltal
- `SERIAL`: Auto-inkrementerande heltal
- `NUMERIC(p, s)`: Exakta decimaltal (t.ex. pengar)
- `REAL` / `DOUBLE PRECISION`: Flyttal

### **Datum & Tid**
- `DATE`: Datum (2025-01-15)
- `TIME`: Tid (14:30:00)
- `TIMESTAMP`: Datum + tid
- `TIMESTAMPTZ`: Med tidszon (REKOMMENDERAT!)

### **Boolean**
- `BOOLEAN`: TRUE, FALSE, eller NULL

### **JSON** (PostgreSQL-specialitet!)
- `JSON`: Lagrar JSON som text
- `JSONB`: Binärt JSON-format (SNABBARE, rekommenderat!)

```sql
-- Exempel med JSONB
CREATE TABLE produkter (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100),
    egenskaper JSONB
);

INSERT INTO produkter (namn, egenskaper) VALUES
    ('Laptop', '{"märke": "Dell", "ram_gb": 16, "färg": "silver"}'),
    ('Telefon', '{"märke": "Samsung", "kamera_mp": 48, "5g": true}');

-- Sök i JSONB
SELECT namn FROM produkter
WHERE egenskaper->>'märke' = 'Dell';
```

---

## Relationer & JOINs: Koppla samman tabeller

### Grundkonceptet
Databaser är som LEGO – du bygger många små tabeller och kopplar ihop dem!

**Exempel scenario**: En webshop med kunder och beställningar.

```
KUNDER-tabell               BESTÄLLNINGAR-tabell
┌────┬──────────┐          ┌────┬───────────┬────────────┐
│ ID │ Namn     │          │ ID │ Kund_ID   │ Produkt    │
├────┼──────────┤          ├────┼───────────┼────────────┤
│ 1  │ Anna     │◄─────────┤ 1  │ 1         │ Laptop     │
│ 2  │ Erik     │          │ 2  │ 1         │ Mus        │
│ 3  │ Lisa     │◄─────────┤ 3  │ 3         │ Tangentbord│
└────┴──────────┘          └────┴───────────┴────────────┘
                                    │
                              FOREIGN KEY
                            (refererar till Kunder.ID)
```

### Skapa tabeller med relationer

```sql
-- Skapa beställningar-tabellen
CREATE TABLE beställningar (
    id SERIAL PRIMARY KEY,
    kund_id INTEGER REFERENCES kunder(id),
    produkt VARCHAR(100),
    pris NUMERIC(10, 2),
    beställd_datum TIMESTAMP DEFAULT NOW()
);

-- Lägg till testdata
INSERT INTO beställningar (kund_id, produkt, pris) VALUES
    (1, 'Laptop Dell XPS', 12999.00),
    (1, 'Trådlös mus', 299.00),
    (3, 'Mekaniskt tangentbord', 899.00),
    (2, 'Skärm 27"', 3499.00);
```

---

### INNER JOIN - Hitta matchningar

```sql
-- Visa alla beställningar med kundnamn
SELECT
    kunder.namn,
    beställningar.produkt,
    beställningar.pris
FROM beställningar
INNER JOIN kunder ON beställningar.kund_id = kunder.id;
```

**Resultat:**
```
┌────────────────┬─────────────────────────┬─────────┐
│ namn           │ produkt                 │ pris    │
├────────────────┼─────────────────────────┼─────────┤
│ Anna Svensson  │ Laptop Dell XPS         │ 12999.00│
│ Anna Svensson  │ Trådlös mus             │ 299.00  │
│ Lisa Berg      │ Mekaniskt tangentbord   │ 899.00  │
│ Erik Johansson │ Skärm 27"               │ 3499.00 │
└────────────────┴─────────────────────────┴─────────┘
```

---

### LEFT JOIN - Inkludera alla från vänster tabell

```sql
-- Visa ALLA kunder, även de utan beställningar
SELECT
    kunder.namn,
    beställningar.produkt
FROM kunder
LEFT JOIN beställningar ON kunder.id = beställningar.kund_id;
```

Om Johan (kund_id = 4) inte har beställt något, visas han ändå med `NULL` i produkt-kolumnen.

---

## Schema & Constraints

### **Schema**
En schema är som en mapp för tabeller. Standard-schemat heter `public`.

```sql
-- Skapa ett eget schema
CREATE SCHEMA admin;

-- Skapa tabell i schema
CREATE TABLE admin.logg (
    id SERIAL PRIMARY KEY,
    meddelande TEXT,
    tidpunkt TIMESTAMP DEFAULT NOW()
);

-- Använd den
INSERT INTO admin.logg (meddelande) VALUES ('System startad');
SELECT * FROM admin.logg;
```

### **Constraints** (villkor)
- `NOT NULL`: Måste ha ett värde
- `UNIQUE`: Inga dubbletter
- `CHECK`: Egen validering
- `FOREIGN KEY`: Refererar till annan tabell
- `DEFAULT`: Standardvärde

---

## 🎯 Övningar

### Övning 1: Skapa din första databas
Skapa en databas för ett bibliotek med:
1. En tabell `böcker` med: id, titel, författare, isbn, utgivningsår
2. En tabell `låntagare` med: id, namn, email, telefon

**Facit:**
```sql
CREATE TABLE böcker (
    id SERIAL PRIMARY KEY,
    titel VARCHAR(200) NOT NULL,
    författare VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    utgivningsår INTEGER CHECK (utgivningsår >= 1000 AND utgivningsår <= 2025)
);

CREATE TABLE låntagare (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefon VARCHAR(15)
);
```

---

### Övning 2: CRUD-operationer
Använd tabellerna från Övning 1 och:
1. Lägg till 3 böcker
2. Lägg till 2 låntagare
3. Uppdatera en boks titel
4. Ta bort en bok

**Facit:**
```sql
-- 1. Lägg till böcker
INSERT INTO böcker (titel, författare, isbn, utgivningsår) VALUES
    ('Pippi Långstrump', 'Astrid Lindgren', '9789129688313', 1945),
    ('1984', 'George Orwell', '9780451524935', 1949),
    ('Harry Potter', 'J.K. Rowling', '9780747532699', 1997);

-- 2. Lägg till låntagare
INSERT INTO låntagare (namn, email, telefon) VALUES
    ('Anna Andersson', 'anna@example.com', '0701234567'),
    ('Erik Svensson', 'erik@example.com', '0709876543');

-- 3. Uppdatera
UPDATE böcker SET titel = 'Pippi Långstrump går ombord' WHERE id = 1;

-- 4. Ta bort
DELETE FROM böcker WHERE id = 3;
```

---

### Övning 3: SELECT med filter
Från `kunder`-tabellen vi skapade tidigare:
1. Hitta alla kunder över 30 år
2. Hitta kunder vars email slutar på "example.com"
3. Räkna hur många kunder som är mellan 25-35 år
4. Visa de tre äldsta kunderna

**Facit:**
```sql
-- 1.
SELECT * FROM kunder WHERE ålder > 30;

-- 2.
SELECT * FROM kunder WHERE email LIKE '%example.com';

-- 3.
SELECT COUNT(*) FROM kunder WHERE ålder BETWEEN 25 AND 35;

-- 4.
SELECT * FROM kunder ORDER BY ålder DESC LIMIT 3;
```

---

### Övning 4: Lägg till lån-tabell
Utöka biblioteksdatabasen med en `lån`-tabell som kopplar böcker till låntagare:
- id, bok_id (foreign key), låntagare_id (foreign key), lånedatum, återlämningsdatum

**Facit:**
```sql
CREATE TABLE lån (
    id SERIAL PRIMARY KEY,
    bok_id INTEGER REFERENCES böcker(id) ON DELETE CASCADE,
    låntagare_id INTEGER REFERENCES låntagare(id) ON DELETE CASCADE,
    lånedatum DATE DEFAULT CURRENT_DATE,
    återlämningsdatum DATE
);

-- ON DELETE CASCADE betyder att om en bok raderas,
-- raderas också alla lån kopplade till den.
```

---

### Övning 5: Din första JOIN
Använd tabellerna från övning 4 och:
1. Lägg till ett par lån
2. Skriv en query som visar: låntagarens namn, bokens titel, och lånedatum

**Facit:**
```sql
-- 1. Lägg till lån
INSERT INTO lån (bok_id, låntagare_id) VALUES
    (1, 1),  -- Anna lånar Pippi
    (2, 1),  -- Anna lånar 1984
    (1, 2);  -- Erik lånar Pippi (efter Anna)

-- 2. JOIN-query
SELECT
    låntagare.namn AS låntagare,
    böcker.titel AS bok,
    lån.lånedatum
FROM lån
INNER JOIN låntagare ON lån.låntagare_id = låntagare.id
INNER JOIN böcker ON lån.bok_id = böcker.id;
```

---

### Övning 6: JSONB-experiment
Skapa en tabell `användare` där varje användare kan ha flexibla inställningar i JSONB-format:

**Facit:**
```sql
CREATE TABLE användare (
    id SERIAL PRIMARY KEY,
    användarnamn VARCHAR(50) UNIQUE,
    inställningar JSONB
);

INSERT INTO användare (användarnamn, inställningar) VALUES
    ('anna123', '{"tema": "mörkt", "språk": "sv", "notiser": true}'),
    ('erik456', '{"tema": "ljust", "språk": "en", "notiser": false}');

-- Hitta alla med mörkt tema
SELECT användarnamn FROM användare
WHERE inställningar->>'tema' = 'mörkt';
```

---

### Övning 7: Designa en blogg-databas (mini-projekt)
Skapa tabeller för en enkel blogg med:
- Författare (id, namn, email)
- Inlägg (id, författare_id, titel, innehåll, publicerad_datum)
- Kommentarer (id, inlägg_id, författarnamn, kommentar, datum)

Skriv sedan queries för att:
1. Visa alla inlägg med författarens namn
2. Räkna antal kommentarer per inlägg
3. Hitta de 5 senaste inläggen

**Facit:**
```sql
-- Tabeller
CREATE TABLE författare (
    id SERIAL PRIMARY KEY,
    namn VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE
);

CREATE TABLE inlägg (
    id SERIAL PRIMARY KEY,
    författare_id INTEGER REFERENCES författare(id),
    titel VARCHAR(200) NOT NULL,
    innehåll TEXT,
    publicerad_datum TIMESTAMP DEFAULT NOW()
);

CREATE TABLE kommentarer (
    id SERIAL PRIMARY KEY,
    inlägg_id INTEGER REFERENCES inlägg(id) ON DELETE CASCADE,
    författarnamn VARCHAR(100),
    kommentar TEXT,
    datum TIMESTAMP DEFAULT NOW()
);

-- Queries
-- 1. Inlägg med författarnamn
SELECT inlägg.titel, författare.namn, inlägg.publicerad_datum
FROM inlägg
INNER JOIN författare ON inlägg.författare_id = författare.id;

-- 2. Antal kommentarer per inlägg
SELECT inlägg.titel, COUNT(kommentarer.id) AS antal_kommentarer
FROM inlägg
LEFT JOIN kommentarer ON inlägg.id = kommentarer.inlägg_id
GROUP BY inlägg.id, inlägg.titel;

-- 3. Senaste 5 inläggen
SELECT titel, publicerad_datum FROM inlägg
ORDER BY publicerad_datum DESC LIMIT 5;
```

---

## 💡 Pro Tips

1. **Använd alltid SERIAL för ID-kolumner** – PostgreSQL sköter numreringen automatiskt.
2. **TIMESTAMPTZ > TIMESTAMP** – Spara alltid tid med tidszon för att undvika problem senare!
3. **RETURNING-klausulen är guld** – Använd `RETURNING *` efter INSERT/UPDATE för att se vad som hände.
4. **Transaktioner för flera operationer:**
   ```sql
   BEGIN;
   INSERT INTO kunder ...;
   INSERT INTO beställningar ...;
   COMMIT;  -- Eller ROLLBACK; om något gick fel
   ```

---

## Sammanfattning: Vad har du lärt dig?

✅ Installera PostgreSQL med Docker eller lokalt
✅ Använda `psql` och grafiska verktyg som pgAdmin
✅ Skapa databaser och tabeller (`CREATE TABLE`)
✅ CRUD: INSERT, SELECT, UPDATE, DELETE
✅ Viktiga datatyper: VARCHAR, INTEGER, DATE, TIMESTAMP, JSONB
✅ Constraints: NOT NULL, UNIQUE, CHECK, FOREIGN KEY
✅ JOIN-koncept: INNER JOIN och LEFT JOIN
✅ Bygga relationer mellan tabeller

**Nya ord (Ordlista):**
- **Schema**: En namnrymd/mapp för tabeller (default: `public`)
- **Constraint**: Regler för vad en kolumn får innehålla
- **Foreign Key**: Referens till en annan tabells primärnyckel
- **SERIAL**: Auto-inkrementerande heltal (perfekt för ID)
- **CRUD**: Create, Read, Update, Delete (grundoperationerna)
- **JOIN**: Slår ihop data från flera tabeller
- **INNER JOIN**: Visar bara rader med matchningar i båda tabellerna
- **LEFT JOIN**: Visar alla från vänster tabell + matchningar från höger
- **JSONB**: Binärt JSON-format (snabbare än vanlig JSON)

---

### Nästa steg: Nivå 4! 🏛️

Nu har du praktisk erfarenhet med PostgreSQL! I nästa nivå går vi djupare in på teori och avancerade koncept: transaktioner, ACID-egenskaper, index, query-optimering, normalisering, och mycket mer. Det blir seriöst – men otroligt användbart!

Du är nu officiellt en PostgreSQL-användare! 🚀

---

**Läsningstid**: ~20 minuter
**Nivå**: 3/5 (Praktisk grundnivå)
**Nästa nivå**: Avancerade koncept (Universitetsnivå)
