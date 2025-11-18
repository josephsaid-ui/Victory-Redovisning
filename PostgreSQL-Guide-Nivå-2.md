# PostgreSQL från Noll till Expert
## Nivå 2: "10-åringen" - Grundläggande databastermer 🧒

### Introduktion
Nu när du förstår att en databas är som smarta lådor för information, är det dags att lära dig de viktiga orden som alla som jobbar med databaser använder. Du kommer att förstå vad "tabeller", "rader" och "kolumner" betyder, och få se ditt första riktiga exempel på hur PostgreSQL används. Detta är grunden för att kunna prata om databaser som ett proffs!

---

### Kärnkoncept: De viktiga orden

#### 1. **Tabell** (Table)
En tabell är som ett kalkylblad eller en klasslista. Den har rader och kolumner och håller information om EN typ av sak.

**Exempel från skolan:**
- En tabell för **elever** (namn, ålder, klass)
- En tabell för **böcker** (titel, författare, antal sidor)
- En tabell för **lärare** (namn, ämne, telefonnummer)

Tänk på det som en sida i en Excel-fil, fast mycket smartare!

---

#### 2. **Rad** (Row / Record)
En rad är EN enskild post i tabellen. Om tabellen handlar om elever, så är varje rad EN elev.

**Exempel:**

```
ELEVER-tabellen:
Rad 1: Lisa Andersson, 10 år, Klass 4A
Rad 2: Erik Svensson, 11 år, Klass 5B
Rad 3: Anna Berg, 10 år, Klass 4A
```

Varje rad = EN elev med all information om just den eleven.

---

#### 3. **Kolumn** (Column / Field)
En kolumn är EN typ av information som finns för alla rader. Alla elever har ett "namn", en "ålder" och en "klass" – dessa är kolumnerna.

**Visualisering:**

```
┌───────────────┬────────┬─────────┐
│ Namn          │ Ålder  │ Klass   │  ← KOLUMNER
├───────────────┼────────┼─────────┤
│ Lisa Andersson│ 10     │ 4A      │  ← RAD 1
│ Erik Svensson │ 11     │ 5B      │  ← RAD 2
│ Anna Berg     │ 10     │ 4A      │  ← RAD 3
└───────────────┴────────┴─────────┘
```

**Kom ihåg:** Kolumner = vad vi vill veta (namn, ålder), Rader = vem det handlar om (Lisa, Erik, Anna).

---

#### 4. **Primärnyckel** (Primary Key)
Detta är det som gör varje rad UNIK. Tänk dig att det finns TVÅ elever som heter Lisa Andersson i skolan – hur vet vi vilken vi menar?

Lösningen: Ge varje elev ett UNIKT nummer som bara DE har!

**Exempel:**

```
┌─────┬───────────────┬────────┬─────────┐
│ ID  │ Namn          │ Ålder  │ Klass   │
├─────┼───────────────┼────────┼─────────┤
│ 1   │ Lisa Andersson│ 10     │ 4A      │
│ 2   │ Erik Svensson │ 11     │ 5B      │
│ 3   │ Anna Berg     │ 10     │ 4A      │
│ 4   │ Lisa Andersson│ 9      │ 3C      │  ← En annan Lisa!
└─────┴───────────────┴────────┴─────────┘
```

**ID-kolumnen** är primärnyckeln. Den är alltid unik och gör att varje rad kan identifieras exakt.

---

#### 5. **Fråga / Query**
En "query" är hur du PRATAR med databasen. Du ställer en fråga, och databasen svarar.

**Exempel på frågor du kan ställa:**
- "Vilka elever är 10 år gamla?"
- "Visa mig alla böcker av Astrid Lindgren"
- "Hur många elever finns i klass 4A?"

---

#### 6. **SQL** (Structured Query Language)
SQL är *språket* du använder för att prata med PostgreSQL. Det är som att lära sig orden och reglerna för att kunna beställa mat på ett utländskt språk.

**Enkelt SQL-exempel:**

```sql
SELECT namn, ålder
FROM elever
WHERE klass = '4A';
```

Detta betyder på svenska: "Visa mig namn och ålder för alla elever i klass 4A".

Du behöver inte kunna skriva SQL än – bara veta att det är språket vi använder!

---

### Vad är speciellt med PostgreSQL?

Det finns många olika databassystem (MySQL, SQLite, Oracle, osv.), men PostgreSQL är speciellt för att:

1. **Det är öppen källkod (gratis!)** – Vem som helst kan använda det utan att betala.

2. **Det är extremt pålitligt** – Stora företag som Instagram, Spotify och Reddit använder PostgreSQL för miljontals användare.

3. **Det följer reglerna** – PostgreSQL följer SQL-standarder mycket noga, vilket betyder att det du lär dig här fungerar överallt.

4. **Det kan hantera mycket** – Från små projekt (din klasshemsida) till gigantiska system (hela sjukhus).

5. **Det är smart med olika typer av data** – PostgreSQL kan hantera inte bara text och nummer, utan också JSON-data, geografiska koordinater, och mycket mer!

**Tänk på PostgreSQL som ett riktigt professionellt verktyg som används i verkligheten, men som du kan börja lära dig redan nu!**

---

### Tre konkreta exempel från verkligheten

#### Exempel 1: Biblioteket i din skola

**Tabell: Böcker**
```
┌────┬──────────────────────┬─────────────────┬────────┐
│ ID │ Titel                │ Författare      │ Utlånad│
├────┼──────────────────────┼─────────────────┼────────┤
│ 1  │ Pippi Långstrump     │ Astrid Lindgren │ Ja     │
│ 2  │ Harry Potter         │ J.K. Rowling    │ Nej    │
│ 3  │ Ronja Rövardotter    │ Astrid Lindgren │ Ja     │
└────┴──────────────────────┴─────────────────┴────────┘
```

**Fråga**: "Vilka böcker är tillgängliga att låna?"
**Svar**: Harry Potter (för Utlånad = Nej)

---

#### Exempel 2: Ditt lags poängställning

**Tabell: Matcher**
```
┌────┬────────┬───────────┬──────────┐
│ ID │ Datum  │ Motståndare│ Våra mål │
├────┼────────┼───────────┼──────────┤
│ 1  │ 2025-01-10│ Blå laget │ 3        │
│ 2  │ 2025-01-17│ Röda laget│ 2        │
│ 3  │ 2025-01-24│ Gula laget│ 5        │
└────┴────────┴───────────┴──────────┘
```

**Fråga**: "Hur många mål har vi gjort totalt?"
**Svar**: 3 + 2 + 5 = 10 mål

PostgreSQL kan räkna ut detta automatiskt!

---

#### Exempel 3: Födelsedagskalendern

**Tabell: Vänner**
```
┌────┬─────────┬──────────────┬───────────┐
│ ID │ Namn    │ Födelsedag   │ Favoritgodis│
├────┼─────────┼──────────────┼───────────┤
│ 1  │ Lisa    │ 15 mars      │ Choklad   │
│ 2  │ Erik    │ 22 juli      │ Lakrits   │
│ 3  │ Anna    │ 8 mars       │ Lösgodis  │
└────┴─────────┴──────────────┴───────────┘
```

**Fråga**: "Vilka fyller år i mars?"
**Svar**: Lisa och Anna

---

### 🎯 Övningar

#### Övning 1: Identifiera tabell-delar
Se på denna tabell över provresultat:

```
┌────┬─────────┬──────┬─────┐
│ ID │ Elev    │ Ämne │ Poäng│
├────┼─────────┼──────┼─────┤
│ 1  │ Sara    │ Matte│ 85   │
│ 2  │ Johan   │ Matte│ 92   │
│ 3  │ Sara    │ Svenska│ 78 │
└────┴─────────┴──────┴─────┘
```

**Frågor:**
a) Vilken är primärnyckeln?
b) Hur många rader finns det?
c) Hur många kolumner finns det?
d) Vilken information ger rad nummer 2?

**Facit:**
a) ID-kolumnen (varje rad har ett unikt nummer)
b) 3 rader (Sara-Matte, Johan-Matte, Sara-Svenska)
c) 4 kolumner (ID, Elev, Ämne, Poäng)
d) Johan fick 92 poäng i Matte

---

#### Övning 2: Lagra vs Hitta
Bestäm om följande är "LAGRA information" eller "HITTA information":

a) Lägga till en ny elev i klassen
b) Se vilka som har födelsedag i juni
c) Uppdatera Lisas telefonnummer
d) Ta reda på högsta poängen på provet
e) Radera en bok som inte finns kvar

**Facit:**
- **LAGRA**: a (lägga till), c (uppdatera), e (radera) – Allt som ÄNDRAR i databasen
- **HITTA**: b (se vilka), d (ta reda på) – Allt som bara LÄSER information

Detta är viktigt! SQL har olika kommandon för dessa:
- **LAGRA**: INSERT (lägg till), UPDATE (uppdatera), DELETE (ta bort)
- **HITTA**: SELECT (hämta/visa)

---

#### Övning 3: Designa din egen tabell
Rita upp (på papper eller i huvudet) en tabell för dina **favoritspel**. Den ska innehålla:
- En primärnyckel
- Spelets namn
- Plattform (PC, PlayStation, mobil...)
- Betyg (1-10)

Lägg till minst 3 rader (3 olika spel).

**Exempel på facit:**

```
┌────┬──────────────┬───────────┬───────┐
│ ID │ Spelnamn     │ Plattform │ Betyg │
├────┼──────────────┼───────────┼───────┤
│ 1  │ Minecraft    │ PC        │ 10    │
│ 2  │ Among Us     │ Mobil     │ 8     │
│ 3  │ Zelda BOTW   │ Switch    │ 9     │
└────┴──────────────┴───────────┴───────┘
```

---

#### Övning 4: Vad frågar man efter?
Om du har en tabell med alla böcker du läst, formulera i vanlig svenska vad du skulle vilja fråga efter för dessa scenarios:

a) Du vill återläsa en riktigt bra bok (5 stjärnor)
b) Du har glömt namnet på en bok av en viss författare
c) Du vill veta hur många böcker du läst i år

**Facit:**
a) "Visa alla böcker med betyg 5 stjärnor"
b) "Visa alla böcker av [författarens namn]"
c) "Räkna hur många böcker jag läst under 2025"

Senare kommer du lära dig skriva dessa som riktiga SQL-queries!

---

#### Övning 5: PostgreSQL vs anteckningsbok (återbesök)
Nu när du vet vad kolumner och rader är, förklara varför det är svårt att använda en vanlig anteckningsbok istället för PostgreSQL när du har:

- 1000 elevers information
- Vill sortera alla efter efternamn
- Vill hitta alla som bor i en viss stad

**Facit:**
- **Anteckningsbok**: Du måste bläddra genom alla 1000 sidor manuellt, skriva om allt för hand för att sortera, leta med ögonen rad för rad för att hitta staden.
- **PostgreSQL**: Skriver en kort fråga, får svar på en sekund. Datorn gör allt tungt arbete!

---

### 💡 Pro Tips

1. **Primärnyckeln är din bästa vän** – Ge ALLTID varje rad ett unikt ID. Det gör livet mycket enklare!
2. **En tabell = EN typ av sak** – Blanda inte elever och böcker i samma tabell. Håll det organiserat!
3. **SQL är enklare än du tror** – De flesta kommandon är vanliga engelska ord: SELECT (välj), FROM (från), WHERE (där).

---

### Sammanfattning: Vad har du lärt dig?

✅ **Tabell** = En samling data om EN typ av sak (som ett kalkylblad)
✅ **Rad** = EN enskild post (en elev, en bok)
✅ **Kolumn** = EN typ av information (namn, ålder, titel)
✅ **Primärnyckel** = Unikt ID som identifierar varje rad
✅ **Query** = En fråga du ställer till databasen
✅ **SQL** = Språket du använder för att prata med PostgreSQL
✅ **PostgreSQL** = Ett proffsigt, gratis och pålitligt databassystem

**Nya ord (Ordlista):**
- **Tabell (Table)**: Organiserad samling av data i rader och kolumner
- **Rad (Row/Record)**: En enskild post i tabellen
- **Kolumn (Column/Field)**: En typ av information som finns för alla rader
- **Primärnyckel (Primary Key)**: Unikt identifierande värde för varje rad (oftast ett ID)
- **SQL (Structured Query Language)**: Språket för att kommunicera med databasen
- **Query**: En fråga eller kommando till databasen
- **Schema**: Den övergripande strukturen av tabeller och kolumner (kommer i nästa nivå!)

---

### Nästa steg: Nivå 3! 🎓

Nu kan du de viktigaste begreppen! I nästa nivå ska du faktiskt börja ANVÄNDA PostgreSQL på riktigt. Du kommer lära dig installera det, skapa tabeller, lägga in data och ställa dina första riktiga SQL-frågor. Det börjar bli seriöst – och riktigt kul!

Bra jobbat så här långt! 🎉

---

**Läsningstid**: ~15 minuter
**Nivå**: 2/5 (Grundläggande termer)
**Nästa nivå**: Kom igång med riktig PostgreSQL
