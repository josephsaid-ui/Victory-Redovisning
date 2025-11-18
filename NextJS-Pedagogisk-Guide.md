# Next.js – Den Kompletta Guiden
## Från Nybörjare till Expert

---

## 📚 Innehållsförteckning

1. [Om Denna Guide](#-om-denna-guide)
2. [Nivå 1: Vad är en hemsida & vad gör Next.js? 👶](#nivå-1-vad-är-en-hemsida--vad-gör-nextjs-)
3. [Nivå 2: Grundbegrepp i Next.js 🧒](#nivå-2-grundbegrepp-i-nextjs-)
4. [Nivå 3: Hur Next.js fungerar tekniskt 🎓](#nivå-3-hur-nextjs-fungerar-tekniskt-)
5. [Nivå 4: Avancerade koncept & best practices 🏛️](#nivå-4-avancerade-koncept--best-practices-)
6. [Nivå 5: Masternivå i Next.js 💼](#nivå-5-masternivå-i-nextjs-)
7. [Slutlig Självutvärdering 🎓](#-slutlig-självutvärdering)
8. [Ordlista 📖](#-ordlista)
9. [Resurser för Fördjupning 🔗](#-resurser-för-fördjupning)
10. [Vanliga Frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande svenska guiden om **Next.js**!

### Vem är denna guide för?

Denna guide är designad för **alla** – från den som aldrig sett en rad kod till den erfarna utvecklaren som vill lära sig Next.js på djupet. Du behöver **ingen förkunskap** för att börja, men du kommer att nå expertis när du är klar.

### Hur ska jag använda guiden?

Guiden är uppdelad i **5 progressiva nivåer**:

- **Nivå 1** (👶): För den som är helt ny – ingen kod, bara koncept
- **Nivå 2** (🧒): Grundläggande begrepp med enkla exempel
- **Nivå 3** (🎓): Teknisk förståelse med kodexempel
- **Nivå 4** (🏛️): Avancerade koncept och bästa praxis
- **Nivå 5** (💼): Expertnivå med arkitekturtänk

**Rekommendation**:
- Läs nivåerna i ordning
- Hoppa inte över övningar – de befäster kunskapen
- Återvänd till tidigare nivåer om något känns oklart
- Total läsningstid: 1.5–3 timmar

### Vad kommer du kunna efter guiden?

Efter att ha genomfört hela guiden kommer du att:
- ✅ Förstå exakt vad Next.js är och varför det används
- ✅ Kunna bygga moderna webbapplikationer med Next.js
- ✅ Behärska Server och Client Components
- ✅ Förstå renderingsstrategier (SSR, SSG, ISR)
- ✅ Kunna optimera prestanda och användarupplevelse
- ✅ Kunna deploya produktionsklara applikationer
- ✅ Tänka som en senior Next.js-utvecklare

Låt oss börja resan!

---

## Nivå 1: Vad är en hemsida & vad gör Next.js? 👶

### Introduktion

På denna nivå ska du lära dig vad en hemsida egentligen är och varför Next.js är ett så smart verktyg. Vi kommer inte prata om kod alls – istället ska vi använda bilder och berättelser som du känner igen från vardagen. Efter denna nivå kommer du kunna förklara för vem som helst vad Next.js gör!

### Kärnkoncept

#### 1. Vad är en hemsida?

Tänk dig en **leksaksaffär**. I leksaksaffären finns det:
- En **entré** där du kommer in (startsidan)
- Olika **avdelningar** med leksaker (olika sidor: bilar, dockor, spel)
- **Skyltar** som visar var saker finns (menyer och knappar)
- En **kassa** där du betalar (formulär och knappar)

En **hemsida är precis som en leksaksaffär** – fast på internet! Istället för att gå dit med fötterna, använder du en dator eller telefon. Varje gång du klickar på en knapp är det som att gå till en ny avdelning i affären.

#### 2. Vad är ett "ramverk" eller "verktyg"?

Låt säga att du ska bygga ett hus med LEGO. Du kan:
- **Alternativ A**: Hitta på allt själv – vilka bitar du ska använda, hur taket ska se ut, var dörren ska vara
- **Alternativ B**: Köpa ett LEGO-kit som har instruktioner och alla bitar du behöver

Ett **ramverk** (som Next.js) är som **LEGO-kitet** – det ger dig:
- Färdiga bitar som passar ihop perfekt
- Instruktioner för hur man bygger snabbt och bra
- Hjälp så att huset inte rasar

#### 3. Vad gör Next.js så speciellt?

Tänk dig två kök:

**Kök A – Det vanliga köket (React):**
- Du har ingredienser och verktyg
- Du lagar all mat själv
- Det tar lång tid att duka fram maten
- Du måste tänka på allt själv

**Kök B – Det smarta restaurangköket (Next.js):**
- Du har ingredienser OCH färdiga recept
- En del mat är redan förberedd (så den kommer snabbare)
- Några saker lagas direkt när gästen beställer
- Det finns hjälp som automatiskt vet vad som ska göras först

**Next.js är som det smarta restaurangköket** – det hjälper dig göra hemsidor snabbare och bättre!

#### 4. Varför använder man Next.js?

Tänk dig att du ska berätta en historia för dina kompisar:

**Utan Next.js:** Du måste berätta HELA historien varje gång någon ny kommer. Det tar lång tid!

**Med Next.js:** Du kan:
- Berätta vissa delar av historien en gång och spara dem (så du slipper upprepa dig)
- Vissa kompisar får höra historien direkt (ingen väntan!)
- Du kan berätta olika delar av historien åt olika personer samtidigt

Det betyder att **hemsidan blir snabbare** och folk slipper vänta!

#### 5. Server och Klient – vad är det?

Tänk dig en restaurang:

**Servern (Restaurangens kök):**
- Där all mat lagas
- Du kan inte se vad som händer där
- Det är där alla ingredienser och hemligheter finns
- Maten färdigställs och skickas ut

**Klienten (Ditt bord):**
- Där du sitter och äter
- Du ser tallriken framför dig
- Du kan klicka på knappar (som att beställa mer)
- Det är din telefon eller dator

**Next.js är smart** för det vet vad som ska göras i köket (servern) och vad som ska göras vid ditt bord (klienten)!

### Exempel

#### Exempel 1: Netflix är som en Next.js-hemsida

När du går in på Netflix händer detta:
1. **Startsidan** laddas snabbt (Next.js har förberett den!)
2. Dina **favoriter** visas direkt (Next.js kommer ihåg vad DU gillar)
3. När du klickar på en film – **DEN laddar när du behöver den** (inte allt på en gång)

Utan verktyg som Next.js skulle Netflix ta superlång tid att ladda!

#### Exempel 2: En skolhemsida

Tänk dig din skolas hemsida:
- **Startsida**: Hälsning och nyheter
- **Schema**: Ditt schema för veckan
- **Matsedel**: Vad ni äter i dag
- **Kontakt**: Hur du når skolan

Varje sida är som ett **rum i ett hus**:
```
Huset (Hemsidan)
│
├── Vardagsrum (Startsida)
├── Kök (Matsedel)
├── Studierum (Schema)
└── Hall (Kontakt)
```

Med Next.js kan man göra så att:
- Varje rum vet vad som ska finnas där
- Du kan gå snabbt mellan rummen
- Vissa saker finns i alla rum (som en meny)

#### Exempel 3: Före och efter Next.js

**Före Next.js (vanlig React):**
Du bygger ett pussel:
- Du måste skära ut varje pusselsbit själv
- Du måste rita bilden själv
- Du måste hitta på hur bitarna ska passa ihop

**Efter Next.js:**
Du får ett färdigt pussel-kit:
- Bitarna är redan utskurna
- Bilden finns på lådan
- Det finns instruktioner som visar hur det ska bli

Båda ger ett färdigt pussel, men Next.js gör det **mycket enklare och snabbare**!

### Visualisering: Så fungerar en hemsida

Här är hur det ser ut när du besöker en hemsida:

```
DU (med telefon/dator)
        ↓
   [Jag vill se Netflix!]
        ↓
    INTERNET (vägar och broar)
        ↓
   SERVERN (det stora köket där hemsidan bor)
        ↓
   [Servern lagar ihop hemsidan]
        ↓
    INTERNET (tillbaka samma väg)
        ↓
   DIN SKÄRM (du ser Netflix!)
```

**Med Next.js** är detta extra snabbt för vissa saker är redan förberedda!

### 💡 Pro Tips (för vuxna som läser med barnen)

1. **Next.js är inte magi** – det är som ett smart LEGO-kit för hemsidor
2. **Server vs klient** är som kök vs matbord – vissa saker görs i köket, vissa vid bordet
3. **Snabbhet är viktigt** – Next.js gör hemsidor snabba så folk slipper vänta

### ✏️ Övningar

#### Övning 1: Rita din egen hemsida
Rita en hemsida som en byggnad med olika rum. Varje rum är en sida. Exempel:
- Rum 1: Startsida
- Rum 2: Om mig
- Rum 3: Mina bilder

**Bonus**: Rita pilar mellan rummen som visar hur man går mellan sidorna!

#### Övning 2: Matcha begreppen
Dra streck mellan vänster och höger:

| Begrepp | Förklaring |
|---------|-----------|
| Hemsida | En leksaksaffär på internet |
| Next.js | Ett smart LEGO-kit för att bygga hemsidor |
| Server | Restaurangens kök där maten lagas |
| Klient | Ditt bord där du äter |
| Ramverk | Instruktioner och färdiga bitar |

**Facit**: Alla ord på vänster sida matchar förklaringarna på samma rad!

#### Övning 3: Varför är Next.js bra?
Läs dessa påståenden och säg om de är SANNA eller FALSKA:

1. Next.js gör hemsidor långsammare ❌ FALSKT – det gör dem snabbare!
2. Next.js är som ett smart kök ✅ SANT – det hjälper dig göra saker snabbare!
3. Du måste kunna allt själv med Next.js ❌ FALSKT – Next.js hjälper dig!
4. Next.js kan göra vissa saker färdiga innan du ens frågar ✅ SANT – det kan förberedda sidor!

### 📝 Sammanfattning

**Vad har du lärt dig?**
- ✅ En **hemsida** är som en affär eller ett hus på internet
- ✅ Ett **ramverk** är som ett smart LEGO-kit med instruktioner
- ✅ **Next.js** är ett verktyg som gör hemsidor snabbare och enklare att bygga
- ✅ **Servern** är som ett kök där saker förbereds
- ✅ **Klienten** är din telefon eller dator där du ser resultatet

**Nya ord du har lärt dig:**
- **Hemsida**: En plats på internet man kan besöka
- **Ramverk**: Ett verktyg med färdiga bitar och instruktioner
- **Next.js**: Ett smart ramverk för att bygga hemsidor
- **Server**: Datorn där hemsidan bor (som ett kök)
- **Klient**: Din enhet där du ser hemsidan (som ditt matbord)

**Nästa steg:**
Nu när du förstår vad Next.js är på ett enkelt sätt, är du redo för **Nivå 2** där vi börjar prata om hur saker faktiskt fungerar! Vi kommer prata om sidor, mappar och vad en utvecklare gör när hen bygger en app. Spännande!

---

## Nivå 2: Grundbegrepp i Next.js 🧒

### Introduktion

Nu när du vet vad Next.js är, ska vi lära oss de viktigaste begreppen! På denna nivå kommer vi prata om **komponenter**, **sidor**, **routes** och **mappar**. Vi kommer också förstå skillnaden mellan vad som händer på servern (i köket) och hos klienten (vid ditt bord). Efter denna nivå kommer du förstå hur en Next.js-app är uppbyggd – och du kommer kunna rita upp strukturen själv!

### Kärnkoncept

#### 1. Vad är React?

Innan vi kan förstå Next.js måste vi förstå **React**. Tänk dig att du bygger med LEGO:

**React är LEGO-bitarna:**
- Små bitar som du kan sätta ihop
- Varje bit gör en sak (en knapp, en text, en bild)
- Du kan återanvända samma bitar många gånger
- Du bygger stora saker av små bitar

**Next.js är LEGO-kitet:**
- Instruktioner för hur bitarna ska sättas ihop
- Färdiga kombinationer av bitar
- Verktyg som gör byggandet snabbare

React är grunden – Next.js bygger vidare på React!

#### 2. Vad är en Komponent?

En **komponent** är som en LEGO-bit eller ett byggkloss. Det är en liten del av en hemsida som gör EN sak.

**Exempel på komponenter:**
- En **knapp** som man kan klicka på
- En **meny** högst upp på sidan
- Ett **kort** som visar en produkt
- En **footer** längst ner på sidan

**Analogin – som möbler i ett hus:**
```
Huset (Hemsidan)
│
├── Soffa (Navigation/meny)
├── Tavla (Hero-sektion)
├── Bokhylla (Produktlista)
└── Lampa (Knapp)
```

Varje möbel är en komponent! Du kan flytta möblerna mellan rum (sidor) och använda samma soffa i flera rum.

#### 3. Vad är en Sida (Page)?

En **sida** är en hel vy som användaren ser. Det är som ett helt rum i huset.

**Skillnad mellan komponent och sida:**
- **Komponent**: En möbel (soffa, bord, lampa)
- **Sida**: Ett helt rum med möbler (vardagsrum, kök, sovrum)

**Exempel:**
- **Startsida**: Välkomsttext + bilder + meny
- **Om-sida**: Information om företaget + bild på teamet
- **Kontaktsida**: Formulär + karta + telefonnummer

#### 4. Vad är en Route?

En **route** är vägen till en sida. Det är som adressen till ett rum.

Tänk dig en skola:
- `/` = huvudentrén (startsidan)
- `/klassrum` = korridoren till klassrum
- `/matsalen` = vägen till matsalen
- `/biblioteket` = vägen till biblioteket

På en hemsida fungerar det likadant:
- `mittforetag.se/` → Startsidan
- `mittforetag.se/om` → Om-sidan
- `mittforetag.se/kontakt` → Kontaktsidan
- `mittforetag.se/produkter` → Produktsidan

**Route = Adress till en sida**

#### 5. Filbaserad routing – Mappar = Routes!

Det här är det **smartaste med Next.js**: Dina mappar blir automatiskt routes!

Tänk dig en skolryggsäck med mappar:

```
Min Skolryggsäck (Projektet)
│
└── Pärmen "app" (Här bor alla sidor)
    │
    ├── Pärm "om" (blir /om)
    │   └── Blad: page.tsx (innehållet på /om-sidan)
    │
    ├── Pärm "kontakt" (blir /kontakt)
    │   └── Blad: page.tsx (innehållet på /kontakt-sidan)
    │
    └── Blad: page.tsx (startsidan /)
```

**Magiskt, eller hur?**
- Du skapar en mapp som heter `om` → Du får en sida på `/om`
- Du skapar en mapp som heter `kontakt` → Du får en sida på `/kontakt`
- Filen `page.tsx` i mappen är det som visas på sidan!

#### 6. Server vs Klient – Kök vs Matbord (igen!)

Vi pratade om kök (server) och matbord (klient) i Nivå 1. Nu ska vi förstå det lite djupare:

**Server (Köket):**
- Där Next.js förbereder sidor
- Där data hämtas från databaser
- Du kan inte se vad som händer där (det är privat!)
- Snabbt och kraftfullt
- Exempel: Hämta alla produkter från databasen

**Klient (Matbord/Din dator):**
- Där du SER sidan
- Där du KLICKAR på knappar
- Där animationer och interaktioner sker
- Din webbläsare (Chrome, Safari, Firefox)
- Exempel: En knapp som öppnar en meny när du klickar

**Next.js bestämmer vad som görs var:**
- Tunga saker (databashämtning) → Servern
- Interaktiva saker (klick, animationer) → Klienten

#### 7. Vad gör en utvecklare?

En **utvecklare** (eller **programmerare**) är som en arkitekt och byggare:

**Steg när man bygger en Next.js-app:**
1. **Planera**: Rita upp vilka sidor som behövs
2. **Skapa mappar**: En mapp för varje route/sida
3. **Bygga komponenter**: Knappar, menyer, kort
4. **Sätta ihop**: Placera komponenter på sidor
5. **Testa**: Kolla att allt fungerar
6. **Deploya**: Publicera så andra kan besöka hemsidan

### Exempel

#### Exempel 1: En Klasshemsida

Låt oss bygga en enkel hemsida för din klass!

**Vilka sidor behöver vi?**
- Startsida: Välkomsttext och klassbilder
- Schema: Veckans lektioner
- Klasslista: Alla elever
- Kontakt: Mailadress till läraren

**Hur ser mappstrukturen ut?**
```
app/
├── page.tsx          → Startsida (/)
├── schema/
│   └── page.tsx      → Schema-sida (/schema)
├── klasslista/
│   └── page.tsx      → Klasslista (/klasslista)
└── kontakt/
    └── page.tsx      → Kontakt-sida (/kontakt)
```

**Vad finns i varje `page.tsx`?**
Varje page.tsx innehåller komponenter! Exempel:
- **Startsidan**: En rubrik + ett välkomstmeddelande + en bild
- **Schema**: En tabell med veckans lektioner
- **Klasslista**: En lista med alla elevers namn
- **Kontakt**: En text med mailadress

#### Exempel 2: Komponenter vs Sidor

Låt oss förstå skillnaden tydligt:

**Scenario:** En webbshop för leksaker

**Komponenter (återanvändbara bitar):**
- `Button` – en knapp (används överallt!)
- `ProductCard` – ett kort som visar en leksak
- `Navigation` – menyn högst upp
- `Footer` – informationen längst ner

**Sidor (hela vyer):**
- **Startsida** (`/`): Navigation + välkomsttext + 3 ProductCards + Footer
- **Produktsida** (`/produkter`): Navigation + 12 ProductCards + Footer
- **Om oss** (`/om`): Navigation + text om företaget + Footer
- **Kontakt** (`/kontakt`): Navigation + formulär + Footer

**Ser du mönstret?**
- **Navigation och Footer** används på ALLA sidor (de är komponenter!)
- **ProductCard** används på flera sidor (komponent!)
- Varje sida kombinerar olika komponenter

#### Exempel 3: Från Route till Mapp

Här är hur routes blir mappar i Next.js:

| URL (Route) | Mappstruktur |
|-------------|--------------|
| `hemsida.se/` | `app/page.tsx` |
| `hemsida.se/om` | `app/om/page.tsx` |
| `hemsida.se/produkter` | `app/produkter/page.tsx` |
| `hemsida.se/produkter/leksaker` | `app/produkter/leksaker/page.tsx` |
| `hemsida.se/kontakt` | `app/kontakt/page.tsx` |

**Se hur det fungerar?**
- Varje `/` i URLen = en ny mapp
- Innehållet på sidan = `page.tsx` filen

### Visualisering

#### Diagram 1: Från Mapp till Webbsida

```
MAPPSTRUKTUR                    WEBBLÄSARE
═══════════════                 ═══════════

app/
├── page.tsx          ────────► hemsida.se/
│
├── om/
│   └── page.tsx      ────────► hemsida.se/om
│
└── kontakt/
    └── page.tsx      ────────► hemsida.se/kontakt
```

#### Diagram 2: Hur Komponenter Bygger en Sida

```
        SIDA: Startsidan (/)
        ┌─────────────────────────┐
        │  [Navigation]           │ ← Komponent
        ├─────────────────────────┤
        │  [Rubrik]               │ ← Komponent
        ├─────────────────────────┤
        │  [Välkomsttext]         │ ← Komponent
        ├─────────────────────────┤
        │  [Produktkort 1]        │ ← Komponent
        │  [Produktkort 2]        │ ← Komponent
        │  [Produktkort 3]        │ ← Komponent
        ├─────────────────────────┤
        │  [Footer]               │ ← Komponent
        └─────────────────────────┘
```

Sidan är som ett pussel där varje bit är en komponent!

### 💡 Pro Tips

1. **Tänk i komponenter**: Dela upp saker i små bitar. En knapp = en komponent. En meny = en komponent. Små bitar är lättare att arbeta med!

2. **Mappstrukturen är viktig**: Dina mappar i `app/`-mappen blir dina routes. Tänk noga på hur du namnger mappar!

3. **Återanvänd komponenter**: Om du har en knapp som ser likadan ut överallt – gör DEN komponenten och använd den många gånger!

### ✏️ Övningar

#### Övning 1: Rita Mappstrukturen

Du ska bygga en hemsida för ett bibliotek med dessa sidor:
- Startsida (/)
- Böcker (/bocker)
- Om biblioteket (/om)
- Öppettider (/oppettider)
- Kontakta oss (/kontakt)

**Uppgift**: Rita mappstrukturen i `app/`-mappen!

**Facit**:
```
app/
├── page.tsx           → Startsida
├── bocker/
│   └── page.tsx       → Böcker
├── om/
│   └── page.tsx       → Om biblioteket
├── oppettider/
│   └── page.tsx       → Öppettider
└── kontakt/
    └── page.tsx       → Kontakt
```

#### Övning 2: Matcha Begreppen

Dra streck mellan begrepp och förklaring:

| Begrepp | Förklaring |
|---------|-----------|
| Komponent | Vägen till en sida (t.ex. /om) |
| Sida | Hela vyn användaren ser |
| Route | En återanvändbar del av en sida (t.ex. en knapp) |
| `app/` | Mappen där alla sidor bor |
| `page.tsx` | Filen som innehåller en sida |

**Facit**:
- **Komponent** → En återanvändbar del av en sida (t.ex. en knapp)
- **Sida** → Hela vyn användaren ser
- **Route** → Vägen till en sida (t.ex. /om)
- **`app/`** → Mappen där alla sidor bor
- **`page.tsx`** → Filen som innehåller en sida

#### Övning 3: Identifiera Komponenter och Sidor

Titta på YouTube eller din favoritwebbplats. Identifiera:

**5 Komponenter:**
1. Exempel: Sökfält
2. Exempel: Videokort
3. Exempel: Knapp för "Prenumerera"
4. Exempel: Kommentarsfält
5. Exempel: Navigation/meny

**3 Sidor:**
1. Exempel: Startsida
2. Exempel: Video-sida
3. Exempel: Ditt konto-sida

**Reflektion**: Vilka komponenter används på flera sidor?

#### Övning 4: Bygg en Route

Du vill skapa en sida på `/mina-husdjur/katter`.

**Frågor:**
1. Vilken mappstruktur behöver du?
2. Vad heter filen som innehåller sidan?

**Facit**:
1. Mappstruktur:
```
app/
└── mina-husdjur/
    └── katter/
        └── page.tsx
```
2. Filen heter: `page.tsx`

#### Övning 5: Server eller Klient?

Bestäm om följande ska göras på SERVERN eller KLIENTEN:

1. Hämta alla produkter från databasen → **SERVER** (tungt jobb, privat)
2. Visa en animering när man hovrar över en knapp → **KLIENT** (interaktivt)
3. Kolla om användaren är inloggad → **SERVER** (säkerhet!)
4. Öppna en meny när man klickar → **KLIENT** (interaktivt)
5. Hämta väderdata från en API → **SERVER** (data-hämtning)

### 📝 Sammanfattning

**Vad har du lärt dig?**
- ✅ **React** är grundblocken (LEGO-bitar), **Next.js** är verktygen och instruktionerna
- ✅ En **komponent** är en liten återanvändbar del (knapp, meny, kort)
- ✅ En **sida** är en hel vy (startsida, om-sida, kontakt-sida)
- ✅ En **route** är adressen till en sida (t.ex. `/om`, `/kontakt`)
- ✅ **Filbaserad routing**: Dina mappar blir automatiskt routes i Next.js!
- ✅ **Server** gör tunga jobb (databaser, API), **Klient** gör interaktiva saker (klick, animationer)

**Nya ord du har lärt dig:**
- **React**: JavaScript-bibliotek för att bygga användargränssnitt
- **Komponent**: En återanvändbar bit av en sida (Button, Menu, Card)
- **Sida (Page)**: En hel vy som användaren ser
- **Route**: Vägen/adressen till en sida (URL)
- **Filbaserad routing**: Mappar blir automatiskt routes
- **`app/`**: Mappen där alla sidor och routes bor
- **`page.tsx`**: Filen som definierar vad som visas på en sida
- **Server**: Där tunga beräkningar och datahämtning sker
- **Klient**: Din webbläsare där du ser och interagerar med sidan

**Nästa steg:**
Nu förstår du grundbegreppen! I **Nivå 3** börjar vi med riktig kod. Du kommer lära dig hur man faktiskt skapar sidor, komponenter och hämtar data. Vi går från teori till praktik – det blir spännande!

---

## Nivå 3: Hur Next.js fungerar tekniskt 🎓

### Introduktion

Nu är det dags att få händerna i koden! På denna nivå kommer vi gå igenom hur du faktiskt bygger en Next.js-applikation steg för steg. Du kommer lära dig hur du strukturerar ditt projekt, skapar komponenter och sidor, hämtar data och navigerar mellan sidor. Alla kodexempel använder **TypeScript** och moderna **Next.js 15 App Router**-patterns. Efter denna nivå kommer du kunna bygga en komplett Next.js-app själv!

### Kärnkoncept

#### 1. Next.js Projektstruktur

När du skapar ett Next.js-projekt får du en specifik mappstruktur. Låt oss förstå vad varje del gör:

```
mitt-projekt/
├── app/                    # App Router - alla sidor och routes
│   ├── layout.tsx         # Root layout (används på alla sidor)
│   ├── page.tsx           # Startsidan (/)
│   ├── globals.css        # Globala CSS-stilar
│   ├── om/
│   │   └── page.tsx       # Om-sidan (/om)
│   └── api/
│       └── hello/
│           └── route.ts   # API endpoint (/api/hello)
├── components/             # Återanvändbara komponenter
│   ├── Button.tsx
│   ├── Navigation.tsx
│   └── Footer.tsx
├── public/                 # Statiska filer (bilder, fonts)
│   └── logo.png
├── node_modules/           # Installerade paket (auto-genererad)
├── package.json           # Projektets dependencies och scripts
├── tsconfig.json          # TypeScript-konfiguration
└── next.config.js         # Next.js-konfiguration
```

**Viktiga mappar:**
- **`app/`**: Här bor ALLA dina sidor och routes (App Router)
- **`components/`**: Återanvändbara komponenter som du använder på flera sidor
- **`public/`**: Statiska filer som bilder, ikoner, fonts
- **`app/api/`**: API routes (backend endpoints)

#### 2. Layouts - Delade UI-element

En **layout** är som en "mall" som används på flera sidor. Tänk dig menyn och footern som finns på alla sidor – det är en layout!

**Root Layout** (`app/layout.tsx`):
```typescript
// Detta är root layout - används på ALLA sidor
export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="sv">
      <body>
        <nav>
          <a href="/">Hem</a>
          <a href="/om">Om</a>
          <a href="/kontakt">Kontakt</a>
        </nav>

        {/* children = innehållet från varje sida */}
        <main>{children}</main>

        <footer>
          <p>© 2025 Mitt Företag</p>
        </footer>
      </body>
    </html>
  )
}
```

**Vad händer här?**
- `children` är innehållet från varje specifik sida
- Navigation och footer visas på **alla** sidor automatiskt
- Du behöver bara definiera layouten EN gång!

**Nested Layouts** (nestade layouter):
Du kan ha layouter inuti layouter!

```typescript
// app/dashboard/layout.tsx
export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div>
      <aside>
        {/* Sidebar bara för dashboard-sidor */}
        <a href="/dashboard">Översikt</a>
        <a href="/dashboard/settings">Inställningar</a>
      </aside>
      <div>{children}</div>
    </div>
  )
}
```

Nu har alla sidor under `/dashboard` både root layout OCH dashboard layout!

#### 3. Pages - Sidor

En **page** är vad användaren faktiskt ser. Det är innehållet som ändras mellan olika routes.

**Enkel sida** (`app/page.tsx`):
```typescript
// Detta är startsidan (/)
export default function HomePage() {
  return (
    <div>
      <h1>Välkommen till vår hemsida!</h1>
      <p>Detta är startsidan.</p>
    </div>
  )
}
```

**Sida med route** (`app/om/page.tsx`):
```typescript
// Detta är om-sidan (/om)
export default function AboutPage() {
  return (
    <div>
      <h1>Om oss</h1>
      <p>Vi är ett företag som älskar Next.js!</p>
    </div>
  )
}
```

**Dynamisk route** (`app/blog/[slug]/page.tsx`):
```typescript
// Detta matchar /blog/mitt-inlagg, /blog/annat-inlagg, etc.
export default function BlogPost({
  params,
}: {
  params: { slug: string }
}) {
  return (
    <div>
      <h1>Blogginlägg: {params.slug}</h1>
      <p>Detta är innehållet för {params.slug}</p>
    </div>
  )
}
```

**Hur fungerar `[slug]`?**
- `[slug]` = dynamisk parameter
- `/blog/min-artikel` → `params.slug = "min-artikel"`
- `/blog/ny-artikel` → `params.slug = "ny-artikel"`

#### 4. Server Components vs Client Components

Detta är **SUPER viktigt** att förstå! Next.js 15 använder Server Components som standard.

**Server Components** (standard):
```typescript
// Detta är en Server Component (default)
// Inget 'use client' behövs!
export default async function ProductList() {
  // Du kan hämta data direkt i komponenten!
  const products = await fetch('https://api.example.com/products')
    .then(res => res.json())

  return (
    <div>
      <h2>Produkter</h2>
      {products.map((product: any) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>{product.price} kr</p>
        </div>
      ))}
    </div>
  )
}
```

**Fördelar med Server Components:**
- ✅ Kan vara `async` (vänta på data)
- ✅ Kan hämta data direkt (fetch, databas)
- ✅ Ingen JavaScript skickas till klienten (snabbare!)
- ✅ Kan använda privata API-nycklar (säkert)

**Begränsningar:**
- ❌ Kan INTE använda `useState`, `useEffect`
- ❌ Kan INTE lyssna på klick eller andra events
- ❌ Kan INTE använda browser API:er (localStorage, etc.)

**Client Components:**
```typescript
'use client' // Detta gör komponenten till en Client Component!

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Räknare: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Öka
      </button>
    </div>
  )
}
```

**När använder du Client Components?**
- När du behöver `useState`, `useEffect`
- När du behöver lyssna på klick, hover, input
- När du behöver browser API:er (localStorage, window)
- När du behöver interaktivitet!

**Bästa praxis:**
- Använd Server Components så mycket som möjligt
- Markera bara komponenter som MÅSTE vara interaktiva som `'use client'`
- Håll Client Components små och fokuserade

**Komposition - Kombinera Server och Client:**
```typescript
// app/page.tsx (Server Component)
import Counter from '@/components/Counter' // Client Component

export default async function HomePage() {
  // Hämta data på servern
  const data = await fetch('https://api.example.com/data')
    .then(res => res.json())

  return (
    <div>
      <h1>Startsida</h1>
      <p>Data från servern: {data.message}</p>

      {/* Client Component för interaktivitet */}
      <Counter />
    </div>
  )
}
```

#### 5. Data Fetching - Hämta Data

I Next.js App Router hämtar du data **direkt i komponenten**!

**Grundläggande fetch:**
```typescript
// Server Component (default)
export default async function PostList() {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts')
  const posts = await res.json()

  return (
    <div>
      <h1>Alla Inlägg</h1>
      {posts.map((post: any) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.body}</p>
        </article>
      ))}
    </div>
  )
}
```

**Fetch med caching-kontroll:**
```typescript
// Alltid hämta färsk data (ingen cache)
const res = await fetch('https://api.example.com/data', {
  cache: 'no-store'
})

// Cacha i 60 sekunder (ISR - Incremental Static Regeneration)
const res = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 }
})
```

**Parallell data fetching:**
```typescript
export default async function Dashboard() {
  // Hämta ALLA på samma gång (parallellt)
  const [users, products, stats] = await Promise.all([
    fetch('https://api.example.com/users').then(r => r.json()),
    fetch('https://api.example.com/products').then(r => r.json()),
    fetch('https://api.example.com/stats').then(r => r.json()),
  ])

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Användare: {users.length}</p>
      <p>Produkter: {products.length}</p>
      <p>Besökare: {stats.visitors}</p>
    </div>
  )
}
```

#### 6. Navigation - Link och useRouter

**Link Component** (rekommenderat):
```typescript
import Link from 'next/link'

export default function Navigation() {
  return (
    <nav>
      <Link href="/">Hem</Link>
      <Link href="/om">Om</Link>
      <Link href="/produkter">Produkter</Link>
      <Link href="/kontakt">Kontakt</Link>
    </nav>
  )
}
```

**Dynamiska länkar:**
```typescript
export default function ProductList({ products }) {
  return (
    <div>
      {products.map(product => (
        <Link key={product.id} href={`/produkter/${product.id}`}>
          {product.name}
        </Link>
      ))}
    </div>
  )
}
```

**Programmatisk navigation med useRouter:**
```typescript
'use client' // useRouter kräver Client Component!

import { useRouter } from 'next/navigation'

export default function LoginButton() {
  const router = useRouter()

  const handleLogin = async () => {
    // Logga in användaren...
    const success = await login()

    if (success) {
      // Navigera till dashboard efter login
      router.push('/dashboard')
    }
  }

  return <button onClick={handleLogin}>Logga in</button>
}
```

**Router metoder:**
- `router.push('/path')` - Navigera (lägg till i historik)
- `router.replace('/path')` - Navigera (ersätt i historik)
- `router.refresh()` - Uppdatera data
- `router.back()` - Gå tillbaka
- `router.forward()` - Gå framåt

#### 7. Route Handlers - API Routes

Du kan skapa backend endpoints direkt i Next.js!

**Enkel GET endpoint** (`app/api/hello/route.ts`):
```typescript
export async function GET() {
  return Response.json({ message: 'Hej från API!' })
}
```

**POST endpoint med body:**
```typescript
// app/api/users/route.ts
export async function POST(request: Request) {
  const body = await request.json()

  // Här skulle du spara i databas
  console.log('Ny användare:', body)

  return Response.json({
    success: true,
    user: body
  })
}
```

**Dynamisk route handler:**
```typescript
// app/api/products/[id]/route.ts
export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  const productId = params.id

  // Hämta produkt från databas
  const product = await getProductById(productId)

  return Response.json(product)
}
```

### Exempel

#### Exempel 1: Komplett Page med Data Fetching

```typescript
// app/blog/page.tsx
type Post = {
  id: number
  title: string
  body: string
}

export default async function BlogPage() {
  // Hämta data från API
  const res = await fetch('https://jsonplaceholder.typicode.com/posts')
  const posts: Post[] = await res.json()

  return (
    <div className="container">
      <h1>Blogg</h1>
      <div className="posts">
        {posts.slice(0, 10).map(post => (
          <article key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.body}</p>
            <Link href={`/blog/${post.id}`}>
              Läs mer →
            </Link>
          </article>
        ))}
      </div>
    </div>
  )
}
```

#### Exempel 2: Layout med Navigation

```typescript
// app/layout.tsx
import Link from 'next/link'
import './globals.css'

export const metadata = {
  title: 'Min Next.js App',
  description: 'En fantastisk Next.js-applikation',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="sv">
      <body>
        <header>
          <nav>
            <Link href="/">Hem</Link>
            <Link href="/om">Om</Link>
            <Link href="/blog">Blogg</Link>
            <Link href="/kontakt">Kontakt</Link>
          </nav>
        </header>

        <main>{children}</main>

        <footer>
          <p>© 2025 Min App. Alla rättigheter reserverade.</p>
        </footer>
      </body>
    </html>
  )
}
```

#### Exempel 3: Kombinera Server och Client Components

```typescript
// components/LikeButton.tsx
'use client'

import { useState } from 'react'

export default function LikeButton({ postId }: { postId: number }) {
  const [likes, setLikes] = useState(0)
  const [liked, setLiked] = useState(false)

  const handleLike = () => {
    if (!liked) {
      setLikes(likes + 1)
      setLiked(true)
    }
  }

  return (
    <button onClick={handleLike} disabled={liked}>
      ❤️ {likes} Likes
    </button>
  )
}
```

```typescript
// app/blog/[id]/page.tsx
import LikeButton from '@/components/LikeButton'

type Post = {
  id: number
  title: string
  body: string
}

export default async function BlogPost({
  params,
}: {
  params: { id: string }
}) {
  // Hämta data på servern
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${params.id}`
  )
  const post: Post = await res.json()

  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.body}</p>

      {/* Client Component för interaktivitet */}
      <LikeButton postId={post.id} />
    </article>
  )
}
```

### Visualisering

#### Diagram 1: Request Flow i Next.js

```
ANVÄNDARE                      NEXT.JS SERVER              DATABAS/API
    │                               │                          │
    │ 1. Besöker /blog              │                          │
    ├──────────────────────────────>│                          │
    │                               │                          │
    │                               │ 2. Server Component      │
    │                               │    kör (async)           │
    │                               │                          │
    │                               │ 3. Hämta data            │
    │                               ├─────────────────────────>│
    │                               │                          │
    │                               │ 4. Returnera data        │
    │                               │<─────────────────────────┤
    │                               │                          │
    │                               │ 5. Rendera HTML          │
    │                               │    (med data)            │
    │                               │                          │
    │ 6. Färdig HTML + minimal JS   │                          │
    │<──────────────────────────────┤                          │
    │                               │                          │
    │ 7. Användaren ser sidan       │                          │
    │    (snabbt!)                  │                          │
```

#### Diagram 2: Filstruktur för en Blogg-app

```
app/
├── layout.tsx              # Root layout (nav + footer)
├── page.tsx                # Startsida (/)
├── globals.css             # Globala stilar
│
├── blog/
│   ├── page.tsx            # Blogglista (/blog)
│   └── [id]/
│       └── page.tsx        # Enskilt inlägg (/blog/123)
│
├── om/
│   └── page.tsx            # Om-sida (/om)
│
├── kontakt/
│   └── page.tsx            # Kontakt-sida (/kontakt)
│
└── api/
    ├── hello/
    │   └── route.ts        # GET /api/hello
    └── contact/
        └── route.ts        # POST /api/contact

components/
├── LikeButton.tsx          # Client Component
├── Navigation.tsx          # Server Component
└── Footer.tsx              # Server Component
```

### 💡 Pro Tips

1. **Server Components är default** - Du behöver bara lägga till `'use client'` när du MÅSTE ha interaktivitet. Börja alltid med Server Components!

2. **Fetch caching** - Använd `cache: 'no-store'` för dynamisk data, och `next: { revalidate: 60 }` för data som kan cachas.

3. **Parallell fetching sparar tid** - Använd `Promise.all()` när du hämtar flera datakällor samtidigt.

### ✏️ Övningar

#### Övning 1: Skapa ditt första Next.js-projekt

**Uppgift:**
1. Installera Next.js: `npx create-next-app@latest mitt-projekt`
2. Välj TypeScript, App Router, och Tailwind CSS
3. Kör projektet: `npm run dev`
4. Öppna `http://localhost:3000` i webbläsaren

**Reflektion:** Vad ser du på startsidan?

#### Övning 2: Skapa en ny sida

**Uppgift:**
Skapa en "Om mig"-sida:
1. Skapa mappen `app/om`
2. Skapa filen `app/om/page.tsx`
3. Lägg till följande kod:

```typescript
export default function AboutPage() {
  return (
    <div>
      <h1>Om mig</h1>
      <p>Jag lär mig Next.js!</p>
    </div>
  )
}
```

4. Besök `http://localhost:3000/om`

**Facit:** Du borde se din nya sida!

#### Övning 3: Lägg till Navigation

**Uppgift:**
Uppdatera `app/layout.tsx` för att lägga till en navigation:

```typescript
import Link from 'next/link'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="sv">
      <body>
        <nav style={{ padding: '1rem', background: '#f0f0f0' }}>
          <Link href="/" style={{ marginRight: '1rem' }}>Hem</Link>
          <Link href="/om">Om</Link>
        </nav>
        <main style={{ padding: '2rem' }}>
          {children}
        </main>
      </body>
    </html>
  )
}
```

**Facit:** Nu har du en navigation som visas på alla sidor!

#### Övning 4: Hämta Data från ett API

**Uppgift:**
Skapa en sida som hämtar och visar användare från ett API:

```typescript
// app/users/page.tsx
type User = {
  id: number
  name: string
  email: string
}

export default async function UsersPage() {
  const res = await fetch('https://jsonplaceholder.typicode.com/users')
  const users: User[] = await res.json()

  return (
    <div>
      <h1>Användare</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  )
}
```

**Facit:** Du borde se en lista med 10 användare från API:et!

#### Övning 5: Skapa en Client Component med State

**Uppgift:**
Skapa en räknare-komponent:

```typescript
// components/Counter.tsx
'use client'

import { useState } from 'react'

export default function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Räknare: {count}</p>
      <button onClick={() => setCount(count + 1)}>+</button>
      <button onClick={() => setCount(count - 1)}>-</button>
    </div>
  )
}
```

Använd sedan komponenten på startsidan:

```typescript
// app/page.tsx
import Counter from '@/components/Counter'

export default function HomePage() {
  return (
    <div>
      <h1>Välkommen!</h1>
      <Counter />
    </div>
  )
}
```

**Facit:** Du borde kunna öka och minska räknaren genom att klicka på knapparna!

#### Övning 6: Dynamisk Route

**Uppgift:**
Skapa en dynamisk route för produkter:

1. Skapa `app/produkter/[id]/page.tsx`:

```typescript
export default function ProductPage({
  params,
}: {
  params: { id: string }
}) {
  return (
    <div>
      <h1>Produkt {params.id}</h1>
      <p>Detta är information om produkt {params.id}</p>
    </div>
  )
}
```

2. Besök `http://localhost:3000/produkter/123`
3. Testa även `/produkter/abc` och `/produkter/999`

**Facit:** ID:t i URL:en visas på sidan!

#### Övning 7: Skapa ett enkelt API

**Uppgift:**
Skapa en API route:

```typescript
// app/api/time/route.ts
export async function GET() {
  return Response.json({
    time: new Date().toISOString(),
    message: 'Hej från API!'
  })
}
```

Besök `http://localhost:3000/api/time` i webbläsaren.

**Facit:** Du borde se JSON med aktuell tid!

### 📝 Sammanfattning

**Vad har du lärt dig?**
- ✅ **Projektstruktur**: `app/` för routes, `components/` för komponenter, `public/` för statiska filer
- ✅ **Layouts**: Delade UI-element som visas på flera sidor
- ✅ **Pages**: Innehållet på varje sida (`page.tsx`)
- ✅ **Server Components**: Default, kan hämta data, inget state/events
- ✅ **Client Components**: Behöver `'use client'`, kan ha state och events
- ✅ **Data Fetching**: Använd `async/await` direkt i Server Components
- ✅ **Navigation**: `Link` för länkar, `useRouter` för programmatisk navigation
- ✅ **API Routes**: Skapa backend endpoints i `app/api/`

**Nya ord du har lärt dig:**
- **App Router**: Nya routing-systemet i Next.js (app/-mappen)
- **Layout**: Delad UI-mall för flera sidor
- **Server Component**: Komponent som körs på servern (default)
- **Client Component**: Komponent som körs i webbläsaren (`'use client'`)
- **Async Component**: Server Component som väntar på data
- **Route Handler**: API endpoint (backend)
- **Dynamic Route**: Route med parameter (`[id]`)
- **Metadata**: Information om sidan (titel, beskrivning)
- **ISR**: Incremental Static Regeneration (smart caching)

**Nästa steg:**
Nu kan du bygga grundläggande Next.js-appar! I **Nivå 4** dyker vi djupare in i avancerade koncept som renderingsstrategier (SSR, SSG, ISR), performance-optimeringar, middleware, Server Actions och mycket mer. Vi tar din kunskap till nästa nivå!

---

## Nivå 4: Avancerade koncept & best practices 🏛️

### Introduktion

Välkommen till universitetsnivå! Här går vi på djupet med avancerade Next.js-koncept som separerar juniora från seniora utvecklare. Du kommer lära dig om renderingsstrategier, performance-optimering, middleware, Server Actions, och arkitekturella best practices. Efter denna nivå kan du fatta välgrundade beslut om hur du bygger skalbara och performanta Next.js-applikationer. Detta är kunskapen som används i produktion på stora företag!

### Kärnkoncept

#### 1. Renderingsstrategier - SSR, SSG, ISR, CSR

En av de viktigaste aspekterna av Next.js är att förstå **när och hur** olika renderingsstrategier ska användas.

**Server-Side Rendering (SSR) - Dynamic Rendering:**

Data hämtas och sidan renderas vid **varje request**.

```typescript
// Tvinga SSR genom att markera som dynamic
export const dynamic = 'force-dynamic'

export default async function DashboardPage() {
  // Hämtas varje gång sidan besöks
  const res = await fetch('https://api.example.com/user-data', {
    cache: 'no-store' // Ingen caching
  })
  const data = await res.json()

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Senaste uppdatering: {new Date().toLocaleString()}</p>
      <p>Användare: {data.username}</p>
    </div>
  )
}
```

**När använder du SSR?**
- ✅ Användarpersonlig data (dashboards, profiler)
- ✅ Data som ändras konstant (live-data, real-time)
- ✅ SEO-kritiskt innehåll som måste vara färskt
- ✅ E-handel med lagerdata som ändras ofta

**Trade-offs:**
- ❌ Långsammare (varje request väntar på server)
- ❌ Högre server-load
- ❌ Kostar mer att driva

**Static Site Generation (SSG) - Static Rendering:**

HTML genereras vid **build-time** och återanvänds för alla requests.

```typescript
// Detta blir automatiskt statiskt om du inte använder dynamic eller cache: 'no-store'
export default async function BlogPage() {
  const res = await fetch('https://api.example.com/posts')
  const posts = await res.json()

  return (
    <div>
      <h1>Blogg</h1>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.content}</p>
        </article>
      ))}
    </div>
  )
}
```

**När använder du SSG?**
- ✅ Marknadsföringssidor (landingpages)
- ✅ Bloggar och dokumentation
- ✅ Innehåll som sällan ändras
- ✅ Produktkatalog (om inte lager är kritiskt)

**Fördelar:**
- ✅ Extremt snabbt (servas från CDN)
- ✅ Billigt (ingen server-beräkning per request)
- ✅ Bäst SEO

**Incremental Static Regeneration (ISR):**

Hybrid: Statisk vid build, men **revalideras** efter en viss tid.

```typescript
// Revalidera var 60:e sekund
export default async function ProductsPage() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 60 } // ISR - uppdatera var 60:e sekund
  })
  const products = await res.json()

  return (
    <div>
      <h1>Produkter</h1>
      {products.map(product => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>{product.price} kr</p>
        </div>
      ))}
    </div>
  )
}
```

**När använder du ISR?**
- ✅ E-handel (produktkatalog uppdateras periodiskt)
- ✅ Nyhetsportaler (artiklar uppdateras regelbundet)
- ✅ Stora sajter med tusentals sidor
- ✅ Data som ändras varje timme/dag

**Fördelar:**
- ✅ Snabbt som SSG
- ✅ Innehåll hålls uppdaterat
- ✅ Best of both worlds

**Client-Side Rendering (CSR):**

Data hämtas i webbläsaren efter initial load.

```typescript
'use client'

import { useState, useEffect } from 'react'

export default function RealtimeData() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/realtime')
      .then(res => res.json())
      .then(setData)
  }, [])

  if (!data) return <p>Laddar...</p>

  return <div>{data.message}</div>
}
```

**När använder du CSR?**
- ✅ Data som ändras väldigt ofta (live chat, real-time dashboards)
- ✅ Användarinteraktioner (filter, sökningar)
- ✅ Privat data som inte behöver SEO

**Beslutstabell:**

| Behov | Strategi | Exempel |
|-------|----------|---------|
| SEO + Statiskt innehåll | SSG | Blogg, marknadsföring |
| SEO + Uppdateras regelbundet | ISR | E-handel, nyheter |
| SEO + User-specific | SSR | Dashboard, profil |
| Inget SEO + Real-time | CSR | Live chat, notiser |

#### 2. Performance-optimering

**Bundle Size Optimization:**

Använd `next/dynamic` för att lazy-load tunga komponenter:

```typescript
import dynamic from 'next/dynamic'

// Ladda bara när komponenten behövs
const HeavyChart = dynamic(() => import('@/components/Chart'), {
  loading: () => <p>Laddar diagram...</p>,
  ssr: false // Hoppa över SSR för denna komponent
})

export default function Analytics() {
  return (
    <div>
      <h1>Analytics</h1>
      <HeavyChart />
    </div>
  )
}
```

**Optimera imports:**

```typescript
// ❌ Dåligt - importerar HELA biblioteket
import _ from 'lodash'

// ✅ Bra - importerar bara det du behöver
import debounce from 'lodash/debounce'

// next.config.js - automatisk optimering
module.exports = {
  experimental: {
    optimizePackageImports: ['lodash', 'date-fns', 'react-icons']
  }
}
```

**Image Optimization:**

```typescript
import Image from 'next/image'

export default function ProductCard({ product }) {
  return (
    <div>
      {/* Next.js optimerar automatiskt bilderna */}
      <Image
        src={product.image}
        alt={product.name}
        width={400}
        height={300}
        priority={false} // true för above-fold bilder
        quality={85} // 1-100 (default 75)
        placeholder="blur" // Visar blur medan bilden laddar
      />
      <h3>{product.name}</h3>
    </div>
  )
}
```

**Caching-strategier:**

```typescript
// Ingen cache (alltid färsk data)
fetch(url, { cache: 'no-store' })

// Cache för alltid (build-time data)
fetch(url, { cache: 'force-cache' })

// ISR - revalidera efter 60 sekunder
fetch(url, { next: { revalidate: 60 } })

// Tag-baserad revalidering
fetch(url, { next: { tags: ['products'] } })
```

**Font Optimization:**

```typescript
// app/layout.tsx
import { Inter, Roboto_Mono } from 'next/font/google'

const inter = Inter({
  subsets: ['latin'],
  display: 'swap', // Bättre performance
})

const robotoMono = Roboto_Mono({
  subsets: ['latin'],
  weight: ['400', '700'], // Ladda bara de vikter du behöver
})

export default function RootLayout({ children }) {
  return (
    <html lang="sv" className={inter.className}>
      <body>{children}</body>
    </html>
  )
}
```

#### 3. Avancerad Routing

**Catch-all Routes:**

```typescript
// app/docs/[...slug]/page.tsx
// Matchar /docs/a, /docs/a/b, /docs/a/b/c, etc.

export default function DocsPage({
  params,
}: {
  params: { slug: string[] }
}) {
  return (
    <div>
      <h1>Docs</h1>
      <p>Path: {params.slug.join('/')}</p>
    </div>
  )
}
```

**Optional Catch-all Routes:**

```typescript
// app/shop/[[...categories]]/page.tsx
// Matchar /shop OCH /shop/a, /shop/a/b, etc.

export default function ShopPage({
  params,
}: {
  params: { categories?: string[] }
}) {
  const path = params.categories ? params.categories.join('/') : 'alla'

  return <h1>Kategori: {path}</h1>
}
```

**Route Groups (organisatoriska):**

```typescript
// Mappar inom () påverkar INTE URL:en

app/
├── (marketing)/          # Inte synlig i URL
│   ├── about/
│   │   └── page.tsx      # URL: /about
│   └── contact/
│       └── page.tsx      # URL: /contact
│
└── (shop)/               # Inte synlig i URL
    ├── products/
    │   └── page.tsx      # URL: /products
    └── cart/
        └── page.tsx      # URL: /cart
```

Varje route group kan ha sin egen layout!

```typescript
// app/(marketing)/layout.tsx
export default function MarketingLayout({ children }) {
  return (
    <div>
      <nav>{/* Marketing nav */}</nav>
      {children}
    </div>
  )
}

// app/(shop)/layout.tsx
export default function ShopLayout({ children }) {
  return (
    <div>
      <nav>{/* Shop nav */}</nav>
      {children}
    </div>
  )
}
```

#### 4. Middleware

Middleware körs **innan** en request når din sida. Perfekt för auth, redirects, och rewrites.

```typescript
// middleware.ts (i root)
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  // Kolla auth
  const token = request.cookies.get('token')

  // Redirect om ej inloggad
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  // Lägg till custom header
  const response = NextResponse.next()
  response.headers.set('x-custom-header', 'my-value')

  return response
}

// Kör middleware bara på vissa routes
export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*'],
}
```

**Användningsfall:**
- Authentication/Authorization
- Bot detection
- Redirects och rewrites
- A/B testing
- Geolocation-baserad routing
- Rate limiting

#### 5. Server Actions - Moderna Formulär

Server Actions är asynkrona funktioner som körs på servern och kan kallas från Client Components. Perfekt för formulär!

```typescript
// app/actions.ts
'use server'

import { revalidatePath } from 'next/cache'

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string
  const content = formData.get('content') as string

  // Validering
  if (!title || title.length < 3) {
    return { error: 'Titeln måste vara minst 3 tecken' }
  }

  // Spara i databas
  await db.posts.create({
    title,
    content,
  })

  // Revalidera cache så nya datan visas
  revalidatePath('/blog')

  return { success: true }
}
```

**Användning i formulär:**

```typescript
// app/blog/new/page.tsx
import { createPost } from '@/app/actions'

export default function NewPostPage() {
  return (
    <form action={createPost}>
      <input name="title" type="text" placeholder="Titel" required />
      <textarea name="content" placeholder="Innehåll" required />
      <button type="submit">Skapa inlägg</button>
    </form>
  )
}
```

**Med client-side state (progressiv enhancement):**

```typescript
'use client'

import { useFormStatus } from 'react-dom'
import { createPost } from '@/app/actions'

function SubmitButton() {
  const { pending } = useFormStatus()

  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Skapar...' : 'Skapa inlägg'}
    </button>
  )
}

export default function NewPostForm() {
  return (
    <form action={createPost}>
      <input name="title" type="text" placeholder="Titel" required />
      <textarea name="content" placeholder="Innehåll" required />
      <SubmitButton />
    </form>
  )
}
```

**Validation med Zod:**

```typescript
'use server'

import { z } from 'zod'

const postSchema = z.object({
  title: z.string().min(3, 'Titel måste vara minst 3 tecken'),
  content: z.string().min(10, 'Innehåll måste vara minst 10 tecken'),
  published: z.boolean().optional(),
})

export async function createPost(formData: FormData) {
  const rawData = {
    title: formData.get('title'),
    content: formData.get('content'),
    published: formData.get('published') === 'on',
  }

  // Validera
  const validated = postSchema.safeParse(rawData)

  if (!validated.success) {
    return {
      error: validated.error.errors[0].message
    }
  }

  // Spara validerad data
  await db.posts.create(validated.data)

  revalidatePath('/blog')
  return { success: true }
}
```

#### 6. Best Practices för Filstruktur

För större projekt, organisera kod bättre:

```
app/
├── (auth)/                    # Route group
│   ├── login/
│   └── register/
│
├── (dashboard)/               # Route group
│   ├── layout.tsx            # Dashboard layout
│   ├── page.tsx              # /dashboard
│   ├── settings/
│   └── analytics/
│
├── api/
│   ├── posts/
│   └── users/
│
├── _components/               # Private folder (ej route)
│   ├── DashboardNav.tsx
│   └── Sidebar.tsx
│
└── actions.ts                 # Server Actions

components/                     # Globala komponenter
├── ui/                        # Generiska UI-komponenter
│   ├── Button.tsx
│   ├── Input.tsx
│   └── Card.tsx
│
└── features/                  # Feature-specifika komponenter
    ├── auth/
    ├── posts/
    └── users/

lib/                           # Utilities, helpers
├── db.ts                      # Databas-klient
├── auth.ts                    # Auth-logik
└── utils.ts                   # Helper-funktioner

hooks/                         # Custom React hooks
├── useAuth.ts
└── useLocalStorage.ts

types/                         # TypeScript types
├── user.ts
└── post.ts
```

#### 7. CSS-strategier

**CSS Modules (rekommenderat för komponenter):**

```typescript
// components/Button.module.css
.button {
  background: blue;
  color: white;
  padding: 0.5rem 1rem;
}

.primary {
  background: green;
}

// components/Button.tsx
import styles from './Button.module.css'

export default function Button({ primary, children }) {
  return (
    <button className={`${styles.button} ${primary ? styles.primary : ''}`}>
      {children}
    </button>
  )
}
```

**Tailwind CSS (rekommenderat för utility-first):**

```typescript
export default function Card({ children }) {
  return (
    <div className="rounded-lg border border-gray-200 p-6 shadow-md hover:shadow-lg transition-shadow">
      {children}
    </div>
  )
}
```

**Global CSS:**

```css
/* app/globals.css */
:root {
  --color-primary: #0070f3;
  --color-secondary: #7928ca;
  --spacing-unit: 8px;
}

body {
  font-family: system-ui, -apple-system, sans-serif;
  line-height: 1.6;
}
```

### Exempel

#### Exempel 1: E-handel med Hybrid Rendering

```typescript
// app/products/page.tsx - ISR för produktlista
export default async function ProductsPage() {
  const res = await fetch('https://api.example.com/products', {
    next: { revalidate: 3600 } // Uppdatera varje timme
  })
  const products = await res.json()

  return (
    <div>
      <h1>Produkter</h1>
      {products.map(product => (
        <Link key={product.id} href={`/products/${product.id}`}>
          {product.name}
        </Link>
      ))}
    </div>
  )
}

// app/products/[id]/page.tsx - SSR för individuell produkt (live lager)
export const dynamic = 'force-dynamic'

export default async function ProductPage({ params }) {
  const res = await fetch(`https://api.example.com/products/${params.id}`, {
    cache: 'no-store' // Alltid färsk data (lager)
  })
  const product = await res.json()

  return (
    <div>
      <h1>{product.name}</h1>
      <p>Pris: {product.price} kr</p>
      <p>I lager: {product.stock} st</p>
    </div>
  )
}
```

#### Exempel 2: Auth Middleware

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'
import { verifyToken } from '@/lib/auth'

export async function middleware(request: NextRequest) {
  const token = request.cookies.get('auth-token')?.value

  // Skyddade routes
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url))
    }

    // Verifiera token
    const isValid = await verifyToken(token)
    if (!isValid) {
      return NextResponse.redirect(new URL('/login', request.url))
    }
  }

  // Admin routes - extra check
  if (request.nextUrl.pathname.startsWith('/admin')) {
    const user = await getUserFromToken(token)
    if (!user?.isAdmin) {
      return NextResponse.redirect(new URL('/dashboard', request.url))
    }
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/dashboard/:path*', '/admin/:path*'],
}
```

#### Exempel 3: Performance-optimerad Dashboard

```typescript
// app/dashboard/page.tsx
import dynamic from 'next/dynamic'

// Lazy-load tunga komponenter
const AnalyticsChart = dynamic(() => import('@/components/AnalyticsChart'), {
  loading: () => <ChartSkeleton />,
  ssr: false // Renderas bara på klient
})

const RecentActivity = dynamic(() => import('@/components/RecentActivity'))

export default async function DashboardPage() {
  // Parallell data fetching
  const [user, stats, activity] = await Promise.all([
    fetchUser(),
    fetchStats(),
    fetchActivity()
  ])

  return (
    <div>
      <h1>Dashboard</h1>

      {/* Above-fold - renderas direkt */}
      <UserCard user={user} />
      <StatsOverview stats={stats} />

      {/* Below-fold - lazy-loaded */}
      <AnalyticsChart />
      <RecentActivity data={activity} />
    </div>
  )
}
```

### 💡 Pro Tips

1. **Hybrid är nyckeln** - Använd olika renderingsstrategier för olika sidor. Marketing = SSG, Dashboard = SSR, Produkter = ISR.

2. **Bundle analyzer** - Använd `@next/bundle-analyzer` för att identifiera stora paket som kan lazy-loadas.

3. **Middleware för auth** - Flytta auth-logik till middleware istället för att ha den i varje sida.

4. **Server Actions för formulär** - Enklare än API routes, men lika kraftfullt. Använd för mutations!

5. **Route Groups** - Organisera kod logiskt utan att påverka URL:er.

### ✏️ Övningar

#### Övning 1: Implementera ISR

Skapa en blogg med ISR som uppdateras var 5:e minut:

```typescript
// app/blog/page.tsx
export default async function BlogPage() {
  const res = await fetch('https://jsonplaceholder.typicode.com/posts', {
    next: { revalidate: 300 } // 5 minuter
  })
  const posts = await res.json()

  return (
    <div>
      <h1>Blogg (uppdateras var 5:e minut)</h1>
      <p>Senaste uppdatering: {new Date().toLocaleString()}</p>
      {posts.slice(0, 5).map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
        </article>
      ))}
    </div>
  )
}
```

#### Övning 2: Auth Middleware

Implementera basic auth middleware:

```typescript
// middleware.ts
import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

export function middleware(request: NextRequest) {
  const isAuthenticated = request.cookies.get('auth')?.value === 'true'

  if (!isAuthenticated) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: '/dashboard/:path*',
}
```

#### Övning 3: Server Action Formulär

Skapa ett kontaktformulär med Server Action:

```typescript
// app/actions.ts
'use server'

export async function submitContact(formData: FormData) {
  const name = formData.get('name') as string
  const email = formData.get('email') as string
  const message = formData.get('message') as string

  console.log('Kontakt:', { name, email, message })

  // I verkligheten: spara i databas eller skicka email

  return { success: true, message: 'Tack för ditt meddelande!' }
}
```

```typescript
// app/contact/page.tsx
import { submitContact } from '@/app/actions'

export default function ContactPage() {
  return (
    <form action={submitContact}>
      <input name="name" type="text" placeholder="Ditt namn" required />
      <input name="email" type="email" placeholder="Din email" required />
      <textarea name="message" placeholder="Meddelande" required />
      <button type="submit">Skicka</button>
    </form>
  )
}
```

#### Övning 4: Lazy Load Tung Komponent

```typescript
// components/HeavyChart.tsx
export default function HeavyChart() {
  // Tänk dig att detta är ett stort diagram-bibliotek
  return <div>Tungt diagram här...</div>
}
```

```typescript
// app/analytics/page.tsx
import dynamic from 'next/dynamic'

const HeavyChart = dynamic(() => import('@/components/HeavyChart'), {
  loading: () => <p>Laddar diagram...</p>,
  ssr: false
})

export default function AnalyticsPage() {
  return (
    <div>
      <h1>Analytics</h1>
      <HeavyChart />
    </div>
  )
}
```

#### Övning 5: Optimera Bilder

```typescript
import Image from 'next/image'

export default function Gallery() {
  const images = [
    '/photo1.jpg',
    '/photo2.jpg',
    '/photo3.jpg',
  ]

  return (
    <div>
      {images.map((src, i) => (
        <Image
          key={src}
          src={src}
          alt={`Photo ${i + 1}`}
          width={600}
          height={400}
          priority={i === 0} // Första bilden prioriteras
          quality={85}
        />
      ))}
    </div>
  )
}
```

#### Övning 6: Route Groups

Skapa olika layouter för marketing vs app:

```
app/
├── (marketing)/
│   ├── layout.tsx       # Marketing layout
│   ├── page.tsx         # / (landing)
│   └── about/
│       └── page.tsx     # /about
│
└── (app)/
    ├── layout.tsx       # App layout
    └── dashboard/
        └── page.tsx     # /dashboard
```

#### Övning 7: Parallell Data Fetching

```typescript
export default async function DashboardPage() {
  // Hämta allt parallellt!
  const [users, posts, comments] = await Promise.all([
    fetch('https://jsonplaceholder.typicode.com/users').then(r => r.json()),
    fetch('https://jsonplaceholder.typicode.com/posts').then(r => r.json()),
    fetch('https://jsonplaceholder.typicode.com/comments').then(r => r.json()),
  ])

  return (
    <div>
      <p>Användare: {users.length}</p>
      <p>Inlägg: {posts.length}</p>
      <p>Kommentarer: {comments.length}</p>
    </div>
  )
}
```

#### Övning 8-10: Mini-Projekt - Enkel Blogg

**Uppgift:** Bygg en blogg med:
- Statisk blogglista (ISR, 60 sek)
- Dynamiska blogginlägg (SSR)
- Kommentarsformulär (Server Actions)
- Auth för admin-sidor (Middleware)
- Lazy-loadad komponenteditor

**Filstruktur:**
```
app/
├── blog/
│   ├── page.tsx              # ISR lista
│   ├── [id]/
│   │   └── page.tsx          # SSR inlägg
│   └── new/
│       └── page.tsx          # Admin: skapa inlägg
├── actions.ts                # Server Actions
└── layout.tsx

middleware.ts                 # Auth för /blog/new
```

### 📝 Sammanfattning

**Vad har du lärt dig?**
- ✅ **Renderingsstrategier**: SSR för dynamic, SSG för static, ISR för hybrid, CSR för client-only
- ✅ **Performance**: Lazy loading, bundle optimization, image optimization, caching
- ✅ **Avancerad routing**: Catch-all, optional catch-all, route groups
- ✅ **Middleware**: Auth, redirects, custom headers
- ✅ **Server Actions**: Moderna formulär utan API routes
- ✅ **Filstruktur**: Skalbar organisation för stora projekt
- ✅ **CSS-strategier**: CSS Modules, Tailwind, global CSS

**Nya ord du har lärt dig:**
- **SSR**: Server-Side Rendering - renderas per request
- **SSG**: Static Site Generation - renderas vid build
- **ISR**: Incremental Static Regeneration - hybrid av SSG och SSR
- **CSR**: Client-Side Rendering - renderas i webbläsaren
- **Middleware**: Kod som körs innan request når sidan
- **Server Actions**: Asynkrona server-funktioner för mutations
- **Route Groups**: Organisatoriska mappar som inte påverkar URL
- **Catch-all Routes**: Routes som matchar multipla segment
- **Revalidation**: Uppdatering av cachad data
- **Bundle Size**: Storleken på JavaScript som skickas till klienten

**Vanliga misstag att undvika:**

❌ **Överanvända Client Components** - Använd Server Components som default!
❌ **Ingen caching-strategi** - Välj rätt strategi för varje route
❌ **Tunga bundle sizes** - Lazy-load stora komponenter
❌ **Fel renderingsstrategi** - SSG för user-data är fel, SSR för static content är slöseri
❌ **Ignorera performance metrics** - Mät och optimera!

**Anti-patterns:**

```typescript
// ❌ DÅLIGT - Client Component för data fetching
'use client'
import { useEffect, useState } from 'react'

export default function BadPage() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('/api/data').then(r => r.json()).then(setData)
  }, [])

  return <div>{data?.message}</div>
}

// ✅ BRA - Server Component
export default async function GoodPage() {
  const data = await fetch('https://api.example.com/data').then(r => r.json())
  return <div>{data.message}</div>
}
```

**Nästa steg:**
Du är nu på väg mot expert-nivå! I **Nivå 5** går vi in på production-ready koncept: databas-integration, deployment, miljövariabler, observability, säkerhet och arkitekturella beslut på enterprise-nivå. Vi tar steget från "kan bygga" till "kan driva i produktion"!

---

## Nivå 5: Masternivå i Next.js 💼

### Introduktion

Välkommen till expertnivå! Detta är den kunskap som senior utvecklare använder för att driva Next.js-applikationer i produktion på enterprise-nivå. Vi kommer täcka databas-integration, deployment, säkerhet, performance monitoring, och arkitekturella beslut. Efter denna nivå är du redo att bygga, deploya och underhålla produktionsklara Next.js-applikationer som skalas till miljontals användare. Detta är kunskapen som gör dig värd på arbetsmarknaden!

### Kärnkoncept

#### 1. Databas-integration med Prisma

Prisma är det mest populära ORM:et för Next.js. Här är produktionsklara patterns:

**Installation och setup:**

```bash
npm install prisma @prisma/client
npx prisma init
```

**Databas-schema** (`prisma/schema.prisma`):

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        String   @id @default(cuid())
  email     String   @unique
  name      String?
  posts     Post[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([email])
}

model Post {
  id        String   @id @default(cuid())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User     @relation(fields: [authorId], references: [id])
  authorId  String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([authorId])
  @@index([published])
}
```

**Singleton Pattern för Prisma Client** (kritiskt för development!):

```typescript
// lib/prisma.ts
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma =
  globalForPrisma.prisma ??
  new PrismaClient({
    log: process.env.NODE_ENV === 'development'
      ? ['query', 'error', 'warn']
      : ['error'],
  })

if (process.env.NODE_ENV !== 'production') {
  globalForPrisma.prisma = prisma
}
```

**Varför singleton?** Förhindrar connection pool exhaustion under utveckling när Next.js hot-reloads.

**Användning i Server Components:**

```typescript
// app/posts/page.tsx
import { prisma } from '@/lib/prisma'

export default async function PostsPage() {
  const posts = await prisma.post.findMany({
    where: { published: true },
    include: { author: true },
    orderBy: { createdAt: 'desc' },
    take: 10,
  })

  return (
    <div>
      <h1>Blogginlägg</h1>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>Av: {post.author.name}</p>
          <p>{post.content}</p>
        </article>
      ))}
    </div>
  )
}
```

**Server Actions med Prisma:**

```typescript
// app/actions/posts.ts
'use server'

import { prisma } from '@/lib/prisma'
import { revalidatePath } from 'next/cache'
import { z } from 'zod'

const createPostSchema = z.object({
  title: z.string().min(3),
  content: z.string().min(10),
  authorId: z.string(),
})

export async function createPost(formData: FormData) {
  const parsed = createPostSchema.safeParse({
    title: formData.get('title'),
    content: formData.get('content'),
    authorId: formData.get('authorId'),
  })

  if (!parsed.success) {
    return { error: parsed.error.errors[0].message }
  }

  try {
    const post = await prisma.post.create({
      data: {
        ...parsed.data,
        published: true,
      },
    })

    revalidatePath('/posts')
    return { success: true, postId: post.id }
  } catch (error) {
    return { error: 'Kunde inte skapa inlägg' }
  }
}
```

**Production best practices för Prisma:**

```json
// package.json
{
  "scripts": {
    "postinstall": "prisma generate",
    "db:migrate": "prisma migrate deploy",
    "db:push": "prisma db push",
    "db:seed": "ts-node prisma/seed.ts"
  }
}
```

**Connection pooling för serverless:**

```env
# .env
DATABASE_URL="postgresql://user:pass@host:5432/db?connection_limit=5&pool_timeout=20"
```

#### 2. Deployment på Vercel

Vercel är Next.js-skaparnas platform och den mest optimerade för Next.js.

**Förberedelser:**

1. **Installera Vercel CLI:**
```bash
npm install -g vercel
```

2. **Login:**
```bash
vercel login
```

3. **Deploydirekt från projektet:**
```bash
vercel
```

**vercel.json** - Konfiguration:

```json
{
  "buildCommand": "prisma generate && next build",
  "devCommand": "next dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["arn1"],
  "env": {
    "DATABASE_URL": "@database-url"
  }
}
```

**Git-baserad deployment:**

1. Pusha till GitHub
2. Koppla repository till Vercel
3. Auto-deploy vid push till main
4. Preview deployments för varje PR

**Edge Functions:**

```typescript
// app/api/edge/route.ts
export const runtime = 'edge' // Kör på Vercel Edge

export async function GET(request: Request) {
  const geo = request.headers.get('x-vercel-ip-country')

  return Response.json({
    message: 'Hej från edge!',
    country: geo,
    timestamp: new Date().toISOString(),
  })
}
```

#### 3. Miljövariabler - Production-ready

**Struktur för miljövariabler:**

```
.env                 # Committa ALDRIG (läggs i .gitignore)
.env.local          # Lokala override (committa ALDRIG)
.env.development    # Development defaults (OK att committa)
.env.production     # Production defaults (OK att committa)
.env.example        # Template (committa alltid)
```

**`.env.example`:**
```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/mydb"

# Auth
NEXTAUTH_SECRET="your-secret-here"
NEXTAUTH_URL="http://localhost:3000"

# External APIs
OPENAI_API_KEY="sk-..."

# Public (synliga i browser)
NEXT_PUBLIC_APP_URL="http://localhost:3000"
NEXT_PUBLIC_GA_ID="G-XXXXXXXXXX"
```

**Typsäkerhet för env vars:**

```typescript
// lib/env.ts
import { z } from 'zod'

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  NEXTAUTH_SECRET: z.string().min(32),
  NEXTAUTH_URL: z.string().url(),
  OPENAI_API_KEY: z.string().startsWith('sk-'),
  NEXT_PUBLIC_APP_URL: z.string().url(),
})

export const env = envSchema.parse(process.env)

// Använd:
// import { env } from '@/lib/env'
// const dbUrl = env.DATABASE_URL
```

**Vercel Environment Variables:**

- Gå till Project Settings → Environment Variables
- Lägg till för varje miljö: Production, Preview, Development
- Använd encrypted secrets för känslig data

**Lokal development med Vercel:**

```bash
# Dra ner env vars från Vercel
vercel env pull .env.local
```

#### 4. Autentisering & Säkerhet

**NextAuth.js v5 (Auth.js):**

```typescript
// auth.ts
import NextAuth from "next-auth"
import GitHub from "next-auth/providers/github"
import Google from "next-auth/providers/google"
import { PrismaAdapter } from "@auth/prisma-adapter"
import { prisma } from "@/lib/prisma"

export const { handlers, auth, signIn, signOut } = NextAuth({
  adapter: PrismaAdapter(prisma),
  providers: [
    GitHub({
      clientId: process.env.GITHUB_ID!,
      clientSecret: process.env.GITHUB_SECRET!,
    }),
    Google({
      clientId: process.env.GOOGLE_ID!,
      clientSecret: process.env.GOOGLE_SECRET!,
    }),
  ],
  callbacks: {
    async session({ session, user }) {
      session.user.id = user.id
      session.user.role = user.role
      return session
    },
  },
  pages: {
    signIn: '/login',
    signOut: '/logout',
    error: '/error',
  },
})
```

**Skydda routes med middleware:**

```typescript
// middleware.ts
import { auth } from "@/auth"
import { NextResponse } from "next/server"

export default auth((req) => {
  const isLoggedIn = !!req.auth
  const isAuthPage = req.nextUrl.pathname.startsWith('/login')
  const isProtectedPage = req.nextUrl.pathname.startsWith('/dashboard')

  if (isProtectedPage && !isLoggedIn) {
    return NextResponse.redirect(new URL('/login', req.url))
  }

  if (isAuthPage && isLoggedIn) {
    return NextResponse.redirect(new URL('/dashboard', req.url))
  }

  return NextResponse.next()
})

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
```

**Säkerhetsheaders:**

```typescript
// next.config.js
module.exports = {
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          {
            key: 'X-DNS-Prefetch-Control',
            value: 'on'
          },
          {
            key: 'Strict-Transport-Security',
            value: 'max-age=63072000; includeSubDomains; preload'
          },
          {
            key: 'X-Frame-Options',
            value: 'SAMEORIGIN'
          },
          {
            key: 'X-Content-Type-Options',
            value: 'nosniff'
          },
          {
            key: 'Referrer-Policy',
            value: 'origin-when-cross-origin'
          }
        ]
      }
    ]
  }
}
```

**CSRF Protection i Server Actions:**

Server Actions har inbyggt CSRF-skydd! Men för extra säkerhet:

```typescript
'use server'

import { auth } from '@/auth'

export async function sensitiveAction() {
  const session = await auth()

  if (!session?.user) {
    throw new Error('Unauthorized')
  }

  // Dubbelkolla permissions
  if (session.user.role !== 'admin') {
    throw new Error('Forbidden')
  }

  // Utför action...
}
```

#### 5. Observability & Monitoring

**Strukturerad loggning med Pino:**

```typescript
// lib/logger.ts
import pino from 'pino'

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: process.env.NODE_ENV === 'development'
    ? { target: 'pino-pretty' }
    : undefined,
})

// Användning:
logger.info({ userId: '123' }, 'User logged in')
logger.error({ error: err, userId: '123' }, 'Login failed')
```

**Error Boundary:**

```typescript
// app/error.tsx
'use client'

import { useEffect } from 'react'
import { logger } from '@/lib/logger'

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  useEffect(() => {
    logger.error({ error, digest: error.digest }, 'Application error')
  }, [error])

  return (
    <div>
      <h2>Något gick fel!</h2>
      <button onClick={() => reset()}>Försök igen</button>
    </div>
  )
}
```

**Performance monitoring med Vercel Analytics:**

```typescript
// app/layout.tsx
import { Analytics } from '@vercel/analytics/react'
import { SpeedInsights } from '@vercel/speed-insights/next'

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
        <SpeedInsights />
      </body>
    </html>
  )
}
```

**Custom metrics:**

```typescript
// lib/metrics.ts
export function trackEvent(event: string, properties?: Record<string, any>) {
  if (typeof window !== 'undefined' && window.analytics) {
    window.analytics.track(event, properties)
  }
}

// Användning:
trackEvent('post_created', { postId: '123', userId: 'abc' })
```

#### 6. Arkitekturella Beslut

**Monorepo med Turborepo (översikt):**

```
my-monorepo/
├── apps/
│   ├── web/              # Next.js app
│   ├── admin/            # Admin dashboard
│   └── docs/             # Documentation site
│
├── packages/
│   ├── ui/               # Shared components
│   ├── config/           # Shared configs
│   ├── tsconfig/         # Shared TS configs
│   └── database/         # Prisma schema
│
├── turbo.json           # Turborepo config
└── package.json
```

**När välja Next.js:**

✅ **Bra val:**
- SEO är kritiskt (e-handel, marknadsföring, bloggar)
- Full-stack app med både frontend och backend
- Behöver server-rendering för prestanda
- Team som redan kan React
- Vill ha TypeScript-first experience
- Snabb time-to-market

❌ **Dåligt val:**
- Enbart SPA utan SEO-behov (använd Vite + React)
- Realtids-applikation (WebSockets) som huvudfokus
- Mycket stor, komplex state (överväg Remix eller annat)
- Team utan React-erfarenhet (lär React först)
- Legacy backend som inte kan ersättas (använd React som SPA istället)

**Arkitektur-patterns för stora appar:**

**1. Feature-baserad struktur:**

```
app/
├── (auth)/
│   └── login/
├── (dashboard)/
│   └── [subdomain]/
└── (public)/
    └── blog/

features/
├── auth/
│   ├── components/
│   ├── actions/
│   └── hooks/
├── posts/
│   ├── components/
│   ├── actions/
│   └── types/
└── users/
    └── ...
```

**2. Data Access Layer (DAL):**

```typescript
// lib/dal/posts.ts
import { prisma } from '@/lib/prisma'
import { auth } from '@/auth'
import { cache } from 'react'

// Cache per request
export const getPublishedPosts = cache(async () => {
  return prisma.post.findMany({
    where: { published: true },
    include: { author: true },
    orderBy: { createdAt: 'desc' },
  })
})

// Auth-protected
export async function getMyPosts() {
  const session = await auth()
  if (!session?.user) throw new Error('Unauthorized')

  return prisma.post.findMany({
    where: { authorId: session.user.id },
  })
}

// Använd i Server Components:
// const posts = await getPublishedPosts()
```

**3. DTO Pattern (Data Transfer Objects):**

```typescript
// lib/dto/user.ts
import type { User } from '@prisma/client'

export type PublicUser = Pick<User, 'id' | 'name' | 'image'>

export function toPublicUser(user: User): PublicUser {
  return {
    id: user.id,
    name: user.name,
    image: user.image,
  }
}

// Använd:
const user = await prisma.user.findUnique({ where: { id } })
return toPublicUser(user) // Exponera aldrig email, password etc!
```

### Exempel

#### Case Study 1: E-handel - Migrering från SPA till Next.js

**Före (React SPA med separate backend):**
- Initial load: 3.2s
- Time to Interactive: 4.8s
- SEO: Dålig (JavaScript-beroende)
- Lighthouse score: 62

**Efter (Next.js App Router):**
- Initial load: 0.8s (75% snabbare)
- Time to Interactive: 1.2s (75% snabbare)
- SEO: Excellent (SSR)
- Lighthouse score: 98

**Vad ändrades:**
- Produktlistor: SSG → ISR (revalidate 3600s)
- Enskilda produkter: CSR → SSR (live lager)
- Statiska sidor: CSR → SSG
- API routes integrerade i Next.js
- Image optimization med `next/image`
- Bundle size: -65% med lazy loading

#### Case Study 2: SaaS Dashboard - Från Pages Router till App Router

**Utmaningar:**
- 200+ pages i pages router
- Komplex auth-logik duplicerad överallt
- Ingen TypeScript-säkerhet för routes
- Svår att organisera stora features

**Lösning:**
- Migrerade inkrementellt (App Router stödjer båda)
- Flyttade auth till middleware
- Route groups för feature-organisering
- Server Components för datahämtning
- Server Actions för formulär (ersatte 50+ API routes)

**Resultat:**
- Code reduction: -30%
- Bundle size: -40%
- Developer velocity: +50%
- Type safety: 100%

### 💡 Pro Tips (Expert-level)

1. **React.cache()** - Deduplicate requests per React render:
```typescript
import { cache } from 'react'
export const getUser = cache(async (id: string) => {
  return prisma.user.findUnique({ where: { id } })
})
// Kan kallas många gånger i samma render - körs bara EN gång!
```

2. **Parallel Routes för dashboards:**
```
app/dashboard/@analytics/page.tsx
app/dashboard/@activity/page.tsx
app/dashboard/layout.tsx  # Renders both slots simultaneously
```

3. **Streaming med Suspense:**
```typescript
import { Suspense } from 'react'

export default function Page() {
  return (
    <>
      <Suspense fallback={<Skeleton />}>
        <SlowComponent />
      </Suspense>
    </>
  )
}
```

4. **Partial Prerendering (Next.js 15+):**
```typescript
// next.config.js
module.exports = {
  experimental: {
    ppr: true // Hybrid static + dynamic
  }
}
```

5. **Incremental migration:** Kör Pages Router och App Router samtidigt!

### ✏️ Övningar

#### Övning 1: Sätt upp Prisma

1. Installera Prisma
2. Skapa schema med User och Post
3. Generera migration
4. Skapa seed-data
5. Hämta data i Server Component

#### Övning 2: Deploy till Vercel

1. Pusha projekt till GitHub
2. Koppla till Vercel
3. Sätt environment variables
4. Verifiera deployment

#### Övning 3: Implementera Auth

1. Installera NextAuth
2. Konfigurera GitHub provider
3. Skydda /dashboard med middleware
4. Visa user i UI

#### Övning 4: Structured Logging

1. Installera Pino
2. Skapa logger utility
3. Logga användarhändelser
4. Implementera error boundary

#### Övning 5: Performance Optimization

1. Analysera bundle size
2. Lazy-load tunga komponenter
3. Optimera bilder
4. Implementera Suspense för slow data

#### Övning 6-10: Fullstack Projekt - Bloggplattform

**Krav:**
- Prisma + PostgreSQL
- NextAuth med GitHub
- CRUD för posts (Server Actions)
- ISR för blogglista
- SSR för enskilda posts
- Markdown-stöd
- Image uploads
- Comments system
- Admin dashboard
- Deployed på Vercel

**Bonus:**
- Full-text search med Postgres
- Real-time comments med Pusher
- Email notifications
- Analytics dashboard
- SEO optimization

### 📝 Sammanfattning

**Vad har du lärt dig?**
- ✅ **Prisma**: ORM för type-safe databas-access
- ✅ **Deployment**: Vercel, edge functions, preview deployments
- ✅ **Miljövariabler**: Säker hantering för olika miljöer
- ✅ **Auth**: NextAuth med middleware-skydd
- ✅ **Säkerhet**: Headers, CSRF, sanitering
- ✅ **Observability**: Logging, error tracking, analytics
- ✅ **Arkitektur**: DAL, DTO, feature-baserad struktur
- ✅ **Beslut**: När Next.js är rätt val

**Production Checklist:**

Innan production-deploy, säkerställ att:
- [ ] Environment variables är säkra och korrekt satta
- [ ] Database migrations körs korrekt
- [ ] Error boundaries finns på alla nivåer
- [ ] Logging är strukturerad och informativ
- [ ] Auth är testad och säker
- [ ] Security headers är konfigurerade
- [ ] Performance metrics övervakas
- [ ] SEO metadata är korrekt
- [ ] Images är optimerade
- [ ] Bundle size är analyserad och optimerad
- [ ] E2E tests fungerar
- [ ] Dokumentation är uppdaterad

**Enterprise Best Practices:**

1. **Monorepo**: Turborepo för multi-app projects
2. **CI/CD**: GitHub Actions för automated testing och deployment
3. **Database**: Connection pooling, migrations, backups
4. **Caching**: Multi-layer (CDN, ISR, React cache, database)
5. **Monitoring**: Error tracking (Sentry), Analytics (Vercel), Logs (Datadog)
6. **Security**: Regular audits, dependency updates, penetration testing

**Vanliga produktionsproblem och lösningar:**

| Problem | Symptom | Lösning |
|---------|---------|---------|
| Connection pool exhaustion | Timeout errors | Prisma singleton pattern |
| Slow page loads | High TTFB | Implement ISR/SSG |
| Large bundle size | Slow FCP | Lazy loading, code splitting |
| Memory leaks | Crashing pods | Fix event listeners, clean useEffect |
| Auth issues | Users logged out | Secure cookies, session management |
| Build failures | CI/CD errors | Lock dependencies, test locally |

**Nästa steg efter denna guide:**

Grattis! Du har nu gått från nybörjare till expert i Next.js. Här är vad du kan göra nu:

1. **Bygg verkliga projekt**: Det bästa sättet att lära sig är genom praktik
2. **Bidra till open source**: Next.js, React, och relaterade projekt
3. **Läs officiell dokumentation**: Håll dig uppdaterad med senaste features
4. **Följ community**: Twitter, Discord, Reddit för latest best practices
5. **Lär andra**: Den bästa valideringen av din kunskap är att kunna lära ut

**Resurser för fortsatt lärande:**
- Next.js Documentation
- React Documentation
- Prisma Documentation
- Vercel Blog
- Lee Robinson's YouTube (VP of DX på Vercel)
- Theo's t3.gg (T3 Stack creator)

---

## 🎓 Slutlig Självutvärdering

Testa din kunskap! Bedöm dig själv på följande områden (1-5, där 5 är expert):

### Grundläggande Koncept (Nivå 1-2)

- [ ] Jag kan förklara vad Next.js är med enkla ord
- [ ] Jag förstår skillnaden mellan Server och Client
- [ ] Jag kan förklara filbaserad routing
- [ ] Jag vet vad en komponent och en sida är

**Om du gav dig själv 4-5 på alla punkter:** Du har solid grundförståelse! ✅

### Teknisk Implementation (Nivå 3)

- [ ] Jag kan skapa ett Next.js-projekt från scratch
- [ ] Jag kan skapa sidor och layouter
- [ ] Jag förstår Server Components vs Client Components
- [ ] Jag kan hämta data i en Server Component
- [ ] Jag kan navigera mellan sidor med Link
- [ ] Jag kan skapa API routes

**Om du gav dig själv 4-5 på alla punkter:** Du kan bygga funktionella Next.js-appar! ✅

### Avancerat (Nivå 4)

- [ ] Jag förstår när man ska använda SSR, SSG, ISR eller CSR
- [ ] Jag kan optimera bundle size och prestanda
- [ ] Jag kan implementera middleware för auth
- [ ] Jag kan använda Server Actions för formulär
- [ ] Jag vet hur man strukturerar stora projekt
- [ ] Jag kan lazy-loada komponenter

**Om du gav dig själv 4-5 på alla punkter:** Du är redo för produktionsarbete! ✅

### Expert (Nivå 5)

- [ ] Jag kan integrera databas med Prisma
- [ ] Jag kan deploya till Vercel med miljövariabler
- [ ] Jag kan implementera säker autentisering
- [ ] Jag vet hur man monitorerarproduktionsappar
- [ ] Jag kan fatta arkitekturella beslut
- [ ] Jag vet när Next.js INTE är rätt val

**Om du gav dig själv 4-5 på alla punkter:** Du är Next.js-expert! 🏆

### Praktisk Checklista

Kan du bygga följande **utan att kolla i guiden**?

- [ ] En blogg med statiska sidor (SSG)
- [ ] Ett dashboard med user-specific data (SSR)
- [ ] Ett formulär med Server Actions
- [ ] En produktkatalog med ISR
- [ ] Auth med middleware-skydd
- [ ] En app deployed på Vercel

**Om ja på alla:** Du är produktionsklar! 🚀

---

## 📖 Ordlista

### Grundläggande Termer

**App Router** - Det nya routing-systemet i Next.js som använder `app/`-mappen (Next.js 13+)

**Client Component** - Komponent som körs i webbläsaren. Kräver `'use client'` direktiv. Kan använda hooks och browser APIs.

**Komponent** - En återanvändbar del av UI (t.ex. Button, Card, Navigation)

**Layout** - En UI-mall som delas mellan flera sidor

**Next.js** - Ett React-ramverk för produktionsklara webbapplikationer

**Pages Router** - Det äldre routing-systemet som använder `pages/`-mappen

**React** - JavaScript-bibliotek för att bygga användargränssnitt

**Route** - En URL-path som mappar till en sida (t.ex. `/about`, `/blog/post-1`)

**Server Component** - Komponent som körs på servern (default i App Router). Kan vara async och hämta data direkt.

### Routing & Navigation

**Catch-all Route** - Route som matchar flera segment: `[...slug]`

**Dynamic Route** - Route med parameter: `[id]`

**File-based Routing** - Systemet där mappar blir routes automatiskt

**Link** - Next.js-komponent för navigation mellan sidor

**Middleware** - Kod som körs innan en request når sidan

**Nested Routes** - Routes inom routes (t.ex. `/blog/2024/post-1`)

**Optional Catch-all** - Route som matchar 0 eller fler segment: `[[...slug]]`

**Route Groups** - Organisatoriska mappar som inte påverkar URL: `(marketing)`

**useRouter** - Hook för programmatisk navigation

### Data & Rendering

**CSR (Client-Side Rendering)** - Data hämtas och renderas i webbläsaren

**Data Fetching** - Process att hämta data från API eller databas

**ISR (Incremental Static Regeneration)** - Hybrid: Statisk vid build + revalidering över tid

**Revalidation** - Process att uppdatera cachad data

**Server Actions** - Asynkrona funktioner som körs på servern (för mutations)

**SSG (Static Site Generation)** - HTML genereras vid build-time

**SSR (Server-Side Rendering)** - HTML genereras per request

**Streaming** - Teknik att skicka delar av sidan när de blir klara

### Performance & Optimization

**Bundle Size** - Storleken på JavaScript som skickas till klienten

**Code Splitting** - Dela upp kod i mindre chunks

**Lazy Loading** - Ladda komponenter bara när de behövs

**Metadata** - Information om sidan (title, description) för SEO

**next/dynamic** - Funktion för att lazy-loada komponenter

**next/image** - Optimerad bildkomponent

**Tree Shaking** - Ta bort oanvänd kod från bundle

### Backend & Database

**API Route** - Backend endpoint i Next.js

**DAL (Data Access Layer)** - Abstraktion för databas-access

**DTO (Data Transfer Object)** - Objekt för att kontrollera vilken data som exponeras

**ORM (Object-Relational Mapping)** - Verktyg för att arbeta med databaser (t.ex. Prisma)

**Prisma** - Type-safe ORM för Node.js och TypeScript

**Route Handler** - Ny term för API routes i App Router

### Deployment & Production

**Edge Function** - Funktion som körs på Vercel Edge Network (närmare användaren)

**Environment Variables** - Konfiguration som ändras per miljö

**Vercel** - Deployment-plattform optimerad för Next.js

### Säkerhet

**CSRF (Cross-Site Request Forgery)** - Säkerhetsattack (Next.js har inbyggt skydd)

**NextAuth** - Autentiseringsbibliotek för Next.js

**Security Headers** - HTTP-headers som förbättrar säkerhet

### Avancerat

**Monorepo** - Ett repository med flera projekt/packages

**Parallel Routes** - Flera routes renderas samtidigt (advanced pattern)

**Partial Prerendering (PPR)** - Hybrid av static och dynamic rendering (Next.js 15+)

**Suspense** - React-funktion för att hantera async UI

**Turbopack** - Ny snabb bundler (default i Next.js 15)

**Turborepo** - Verktyg för att hantera monorepos

**TypeScript** - Typad superset av JavaScript

---

## 🔗 Resurser för Fördjupning

### Officiell Dokumentation

**Next.js Docs** - Den officiella dokumentationen för Next.js
- Omfattande guides och API-referens
- Alltid uppdaterad med senaste features
- Interaktiva exempel och tutorials

**React Docs** - Officiell React-dokumentation
- Nödvändig för att förstå Next.js på djupet
- Moderna hooks och patterns
- Bästa praxis från React-teamet

**Prisma Docs** - Dokumentation för Prisma ORM
- Guider för databas-integration
- Best practices för production
- Migration guides

**TypeScript Handbook** - Officiell TypeScript-dokumentation
- Lär dig TypeScript från grunden
- Avancerade typer och patterns

### Lärresurser

**Next.js Learn** - Interaktiv tutorial från Next.js-teamet
- Hands-on projekt från grunden
- Dashboard-app med autentisering
- Gratis och välgjord

**Vercel YouTube** - Officiell kanal med tutorials
- Lee Robinson's videos (VP of DX)
- Product updates och demos
- Best practices

**Theo - t3.gg** - Modern Next.js patterns
- T3 Stack (Next.js + tRPC + Prisma + Tailwind)
- Opinionated men välgrundade råd
- Real-world project breakdowns

**Web Dev Simplified** - Förenklade tutorials
- Next.js basics till advanced
- Jämförelser med andra frameworks
- Praktiska projekt

### Community

**Next.js Discord** - Officiell community
- Hjälp från andra utvecklare
- Diskussioner om best practices
- Direkt tillgång till Next.js-teamet

**r/nextjs (Reddit)** - Diskussioner och frågor
- Visa upp projekt
- Få feedback
- Lär av andras problem

**Stack Overflow** - Frågor och svar
- Sök på `[next.js]` tag
- Konkreta lösningar på problem
- Community-driven hjälp

### Blogs & Newsletters

**Vercel Blog** - Officiell blogg
- Product updates
- Case studies
- Performance guides

**Lee Robinson's Blog** - Personal blog från Vercel's VP of DX
- Modern web development
- Next.js tips och tricks

**Josh W. Comeau** - Interactive teaching
- CSS och React concepts
- Djupgående tutorials
- Visuella förklaringar

### Tools & Libraries

**shadcn/ui** - Component library
- Beautiful components för Next.js
- Copy-paste komponenter
- Tailwind-baserad

**Tailwind CSS** - Utility-first CSS
- Perfekt med Next.js
- Snabb utveckling
- Customizable

**next-auth** - Autentisering
- OAuth providers
- Session management
- Best practices

**Zod** - Schema validation
- Type-safe validation
- Works great med Server Actions
- Runtime + compile-time safety

### Inspiration

**Next.js Showcase** - Appar byggda med Next.js
- Real-world examples
- Se vad som är möjligt
- Source code för många projekt

**Vercel Templates** - Starter templates
- E-commerce
- Blog
- SaaS starters
- Ready to deploy

---

## ❓ Vanliga Frågor (FAQ)

### Allmänt om Next.js

**Q: Måste jag kunna React först?**
A: Ja, definitivt! Next.js bygger på React. Du behöver förstå:
- Components
- Props och state
- Hooks (useState, useEffect)
- JSX

Börja med React basics innan du dyker in i Next.js.

**Q: Vad är skillnaden mellan Next.js och React?**
A: React är ett bibliotek för att bygga UI. Next.js är ett ramverk som:
- Lägger till routing
- Hanterar server-rendering
- Optimerar prestanda automatiskt
- Ger struktur åt applikationen
- Inkluderar backend-funktionalitet (API routes)

**Q: När ska jag välja Next.js?**
A: Välj Next.js när:
- SEO är viktigt
- Du behöver snabb initial load
- Du vill bygga full-stack med React
- TypeScript-first är viktigt
- Du värdesätter developer experience

Välj INTE Next.js om:
- Du bygger enbart en SPA utan SEO-krav
- Din backend är låst och kan inte bytas ut
- Teamet inte kan React

**Q: Är Next.js svårt att lära sig?**
A: Det beror på din bakgrund:
- **Med React-kunskap**: Medel (1-2 veckor för basics)
- **Utan React-kunskap**: Svårt (lär React först, sedan Next.js)
- **Fullständig nybörjare**: Mycket svårt (börja med HTML/CSS/JavaScript)

**Q: Kostar Next.js något?**
A: Next.js är **gratis** och open source! Men:
- Hosting (Vercel, etc.) kan kosta
- Databas kan kosta
- Externa tjänster (Auth, Analytics) kan kosta

Vercel har en generös gratis tier som räcker för de flesta hobby-projekt.

### App Router vs Pages Router

**Q: Ska jag använda App Router eller Pages Router?**
A: **App Router** för nya projekt! Det är framtiden av Next.js.

Pages Router är:
- Äldre systemet
- Fortfarande supportat
- Bra för legacy-appar

App Router är:
- Modernare
- Server Components som default
- Bättre performance
- Framtidssäkert

**Q: Kan jag migrera från Pages till App Router?**
A: Ja! Du kan köra båda samtidigt och migrera gradvis:
1. Nya features i `app/`
2. Befintliga i `pages/`
3. Migrera bit för bit

**Q: Är App Router stabilt?**
A: Ja! Sedan Next.js 13.4 är App Router production-ready.

### Deployment & Hosting

**Q: Var ska jag deploya min Next.js-app?**
A: Bästa alternativen:
1. **Vercel** - Enklast, gjord av Next.js-skaparna
2. **Netlify** - Bra alternativ
3. **AWS/GCP/Azure** - För enterprise
4. **Self-hosted** - Docker + Node.js

**Q: Kan jag köra Next.js på shared hosting?**
A: Nej, du behöver Node.js-stöd. Shared hosting räcker inte.

**Q: Hur dyrt är det att köra en Next.js-app?**
A: Exempel för små appar:
- Vercel Hobby: Gratis (för personliga projekt)
- Vercel Pro: $20/månad
- Database (Neon/PlanetScale): Gratis tier finns
- Total för hobby-projekt: $0-20/månad

För större appar beror det på trafik.

### Performance & SEO

**Q: Är Next.js snabbt?**
A: Mycket snabbt när det används rätt:
- SSG = Extremt snabbt
- ISR = Mycket snabbt
- SSR = Snabbt (beror på servern)

Men fel användning kan göra det långsamt!

**Q: Hur påverkar Next.js SEO?**
A: Positivt! Server-rendering betyder:
- Crawlers ser innehållet direkt
- Snabbare initial load
- Better Core Web Vitals
- Meta tags som fungerar

**Q: Behöver jag göra något speciellt för SEO?**
A: Next.js hjälper, men du måste:
- Sätta rätt metadata
- Optimera bilder
- Använda semantisk HTML
- Skapa sitemap
- Implementera structured data

### Development

**Q: Vilka verktyg behöver jag?**
A: Minimum:
- Node.js (v18+)
- Code editor (VS Code rekommenderas)
- Git

Rekommenderat:
- TypeScript
- ESLint
- Prettier

**Q: Kan jag använda JavaScript istället för TypeScript?**
A: Ja, men TypeScript rekommenderas starkt:
- Catch bugs earlier
- Better autocomplete
- Refactoring blir enklare
- Industry standard

**Q: Hur debuggar jag Next.js?**
A: Flera sätt:
- `console.log()` (server logs i terminal)
- VS Code debugger
- React DevTools
- Next.js DevTools (inbyggd)

### Databas & Backend

**Q: Vilken databas ska jag använda?**
A: Populära val:
- **PostgreSQL** - Robust, feature-rich (rekommenderas)
- **MySQL** - Klassiker
- **MongoDB** - NoSQL alternativ
- **SQLite** - För små appar
- **PlanetScale** - Serverless MySQL
- **Neon** - Serverless Postgres

**Q: Måste jag använda Prisma?**
A: Nej! Alternativ:
- Drizzle ORM
- Raw SQL
- Firebase
- Supabase
- MongoDB Atlas

Men Prisma är mycket populärt och bra!

**Q: Kan Next.js ersätta min backend?**
A: Delvis! Next.js kan:
- Hantera API routes
- Köra server-logic
- Ansluta till databaser

Men för stora appar kan du behöva en separat backend.

### Auth & Security

**Q: Hur implementerar jag autentisering?**
A: Populära lösningar:
- **NextAuth.js** - Mest populär
- **Clerk** - Modern, user-friendly
- **Auth0** - Enterprise-grade
- **Supabase Auth** - Med databas inkluderat

**Q: Är Next.js säkert?**
A: Next.js ger dig verktyg för säkerhet:
- CSRF protection i Server Actions
- Environment variables-hantering
- Security headers-stöd

Men DU måste:
- Validera input
- Sanitera data
- Hantera secrets säkert
- Implementera auth korrekt

**Q: Var ska jag lagra API-nycklar?**
A: **ALLTID** i environment variables:
- Lokalt: `.env.local`
- Production: Vercel/hosting platform
- ALDRIG: I koden eller i git

---

**🎉 Slutord**

Grattis till att du har tagit dig igenom hela guiden! Du har nu gått från att inte veta vad Next.js är till att kunna bygga produktionsklara applikationer.

**Kom ihåg:**
- Lärande är en resa, inte ett mål
- Bygg verkliga projekt för att befästa kunskapen
- Community är din bästa resurs
- Next.js utvecklas konstant - håll dig uppdaterad!

**Nu är det din tur att bygga något fantastiskt! 🚀**

