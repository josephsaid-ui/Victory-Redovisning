# LLM-AGENTER - Den Kompletta Guiden
### Från Grundkoncept till Expertnivå

---

## 📚 Innehållsförteckning

- [Om Denna Guide](#-om-denna-guide)
- [Nivå 1: "5-åringen" - Grundkonceptet](#nivå-1-5-åringen---grundkonceptet-)
- [Nivå 2: "10-åringen" - Introduktion till termer](#nivå-2-10-åringen---introduktion-till-termer-)
- [Nivå 3: "Gymnasiet" - Tekniska detaljer](#nivå-3-gymnasiet---tekniska-detaljer-)
- [Nivå 4: "Universitetsnivå" - Avancerade koncept](#nivå-4-universitetsnivå---avancerade-koncept-)
- [Nivå 5: "Expert" - Masternivå](#nivå-5-expert---masternivå-)
- [Slutlig Självutvärdering](#-slutlig-självutvärdering)
- [Ordlista](#-ordlista)
- [Resurser för Fördjupning](#-resurser-för-fördjupning)
- [Vanliga Frågor (FAQ)](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande pedagogiska guiden om LLM-agenter på svenska! Den här guiden är designad för att ta dig från absolut nybörjare till expert genom en strukturerad läranderesa i fem nivåer.

### Vad kommer du att lära dig?

LLM-agenter representerar nästa steg i AI-utvecklingen - från passiva chatbots till autonoma system som kan planera, resonera, använda verktyg och genomföra komplexa uppgifter. I den här guiden kommer du att:

- Förstå vad LLM-agenter är och hur de fungerar
- Lära dig om olika typer av agenter och när du ska använda dem
- Utforska moderna frameworks som LangChain, AutoGen, CrewAI
- Bygga egna agenter från grunden
- Implementera avancerade tekniker som ReAct, Reflexion och multi-agent systems
- Följa bästa praxis för produktion (2025)

### Hur är guiden uppbyggd?

Guiden följer en progressiv inlärningsmodell där varje nivå bygger på den föregående:

**Nivå 1 (10-15 min):** Grundkonceptet förklarat så enkelt att ett barn förstår
**Nivå 2 (15-20 min):** Introduktion till termer och begrepp
**Nivå 3 (20-30 min):** Tekniska detaljer och implementation
**Nivå 4 (30-45 min):** Avancerade koncept och arkitekturer
**Nivå 5 (45-60 min):** Expertnivå med cutting-edge forskning (2025)

**Total läsningstid:** 2-3 timmar
**Totalt antal övningar:** 50+
**Praktiska projekt:** 3 st

### Vem är guiden för?

- **Nybörjare:** Ingen förkunskap krävs - börja på Nivå 1
- **Utvecklare:** Hoppa till Nivå 3 för teknisk implementation
- **AI/ML-ingenjörer:** Börja på Nivå 4 för avancerade koncept
- **Experter:** Nivå 5 täcker senaste forskningen och best practices från 2025

Låt oss börja resan!

---

## Nivå 1: 5-åringen - Grundkonceptet 👶

### Introduktion

Tänk dig om din leksakrobot inte bara kunde följa ett enkelt kommando som "gå framåt", utan kunde förstå "Jag vill ha mitt favoritgosedjur som ligger uppe i hyllan". Roboten skulle då själv lista ut: *jag behöver hitta hyllan, kanske ta en stol, klättra upp, hitta gosedjuret och ge det till barnet*. Det är precis vad en LLM-agent är - en AI som kan tänka själv och lösa problem steg för steg!

### Kärnkoncept

#### 1. 🤖 Vad är en Agent?

En **agent** är som en smart hjälpreda som kan:
- Lyssna på vad du vill ha
- Tänka ut en plan
- Göra saker för att uppnå målet
- Lära sig och anpassa sig

**Exempel från barnens värld:**
Om mamma säger "Kan du duka bordet?", så gör du inte bara EN sak. Du:
1. Tänker: "Jag behöver tallrikar, gafflar, knivar, glas"
2. Går till skåpet och tar fram tallrikar
3. Hämtar bestick från lådan
4. Ställer upp allt på rätt plats
5. Kollar att allt ser bra ut

Du är en "dukning-agent" som själv tänker ut stegen!

#### 2. 🧠 Vad gör LLM-agenter speciella?

LLM står för "Large Language Model" - det är som en jättesmart hjärna som läst massor av böcker och kan prata och förstå språk. När vi kombinerar den med "agent-förmågan" får vi något magiskt:

**Vanlig AI (chatbot):**
Du: "Vad är vädret?"
AI: "Det är soligt idag!"
*(Kan bara svara på frågor)*

**LLM-Agent:**
Du: "Planera en picknick åt mig"
Agent: "Okej! Jag kollar vädret... Det blir soligt! Jag ska hitta en fin park... Jag gör en inköpslista... Jag bokar en plats... Klart!"
*(Kan göra flera saker och använda verktyg)*

#### 3. 🛠️ Agenter kan använda "verktyg"

Precis som du använder olika verktyg för olika saker (penna för att skriva, sax för att klippa), kan LLM-agenter också använda digitala verktyg:

- 🔍 Söka på internet
- 📧 Skicka email
- 📊 Räkna och göra matematik
- 🎨 Rita bilder
- 📅 Kolla kalendern

**Rolig analog:**
En agent är som en kock i köket:
- Kocken (agenten) får uppgiften: "Laga pannkakor"
- Kocken vet vilka verktyg som behövs: vispen, pannan, spateln
- Kocken utför stegen: blanda, hälla, vända, servera
- Om något går fel (pannkakan bränns) kan kocken anpassa sig!

#### 4. 🔄 Agenter kan "tänka" i loopar

När du bygger med LEGO och något inte passar, vad gör du? Du provar något annat! Agenter gör samma sak:

```
1. Försök göra något
2. Kolla om det funkade
3. Om inte - försök på ett annat sätt
4. Upprepa tills det lyckas!
```

**Exempel:**
Agent ska hitta en billig leksak online:
- Steg 1: Sök på "leksaksbilar"
- Steg 2: Oj, för dyrt! Sök istället "leksaksbilar rea"
- Steg 3: Perfekt! Hittade en för 50 kr
- Klart!

#### 5. 👥 Flera agenter kan jobba tillsammans

Ibland är det bättre om flera agenter samarbetar - som när du och dina kompisar bygger ett högt torn av klossar tillsammans:

- Agent 1 (Planner): "Vi behöver 100 klossar och börja med en bred bas"
- Agent 2 (Builder): "Okej, jag börjar bygga!"
- Agent 3 (Checker): "Stanna! Det här håller inte, gör basen bredare"

### Exempel

#### Exempel 1: Agenten som hjälper till med läxan

**Situation:** Lisa behöver hjälp med matteläxan.

**Vanlig chatbot:**
Lisa: "Vad är 15 × 8?"
Chatbot: "120"
*(Ger bara svaret)*

**LLM-Agent:**
Lisa: "Hjälp mig förstå multiplikation"
Agent: "Okej! Jag ska förklara steg-för-steg..."
1. "Tänk på 15 × 8 som 15 grupper med 8 äpplen"
2. "Låt mig rita en bild..." (använder ritverktyg)
3. "Nu provar vi tillsammans! Vad blir 10 × 8?"
4. (Lisa svarar fel) "Inte riktigt, låt mig visa på ett annat sätt..."
5. (Lisa svarar rätt) "Jättebra! Nu förstår du det!"

**Vad gjorde agenten?**
- Förstod att Lisa ville *lära sig*, inte bara få svaret
- Använde olika verktyg (ritning, frågor)
- Anpassade förklaringen när Lisa inte förstod
- Gav uppmuntran

#### Exempel 2: Födelsedagsplanerararen

**Uppgift:** Planera en överraskningsfest för mamma!

**Hur agenten tänker:**

```
📝 PLAN:
1. Kolla mammans kalender - är hon ledig på lördag?
2. Fråga pappa om budget
3. Sök efter tårtkonditorier i närheten
4. Beställ tårta
5. Skicka inbjudningar till familjen
6. Köp present (kolla vad mamma gillar)
7. Boka restaurang

💭 UTFÖRANDE:
Steg 1: [Kollar kalendern] ✓ Ledig på lördag!
Steg 2: [Frågar pappa] Budget: 2000 kr
Steg 3: [Söker konditorier] Hittat 5 st
Steg 4: ❌ Oh nej! Konditoriet var fullbokat!
        → Försöker nästa konditori... ✓ De har tid!
Steg 5: [Skickar email] Inbjudan skickad till 10 personer
Steg 6: [Kollar mammans önskelista] Hittat perfekt bok!
Steg 7: [Bokar bord] Restaurang bokad kl 18:00

🎉 KLART! Fest planerad!
```

#### Exempel 3: Leksakssökar-agenten

**Scenario:** Du vill ha den coolaste leksaken till bästa pris.

**Agentens arbete:**

1. **Förstå:** "Jag ska hitta LEGO Millennium Falcon billigast"
2. **Sök:** Kollar 5 olika butiker online
3. **Jämför:**
   - Lekia: 899 kr
   - Toys R Us: 849 kr
   - Amazon: 795 kr + frakt 50 kr = 845 kr
4. **Tänk:** "Amazon är billigast!"
5. **Kolla extra:** "Finns det rabattkoder?" Ja! -10%
6. **Räkna:** 795 × 0.9 = 715 kr + 50 = 765 kr
7. **Resultat:** "Billigast på Amazon med rabattkod: 765 kr! Köp den?"

### Visualisering

#### Hur en agent fungerar - enkelt schema:

```
┌─────────────────────────────────────────────────────────┐
│                        👤 DU                             │
│              "Jag vill ha glass!" 🍦                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   🤖 AGENTEN                             │
│  ┌─────────────────────────────────────────────────┐   │
│  │  🧠 TÄNK: "Var kan jag köpa glass?"             │   │
│  └──────────────────┬──────────────────────────────┘   │
│                     │                                    │
│  ┌─────────────────▼──────────────────────────────┐   │
│  │  🔍 GÖR: Söker glass-affärer i närheten        │   │
│  └──────────────────┬──────────────────────────────┘   │
│                     │                                    │
│  ┌─────────────────▼──────────────────────────────┐   │
│  │  👀 KOLLA: Hittade 3 affärer, en är öppen!     │   │
│  └──────────────────┬──────────────────────────────┘   │
│                     │                                    │
│  ┌─────────────────▼──────────────────────────────┐   │
│  │  ✅ ANPASSA: "Den affären är närmast!"         │   │
│  └──────────────────┬──────────────────────────────┘   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                   📍 RESULTAT                            │
│    "Gå till Glassbaren på Storgatan 5,                  │
│     de har jordgubbsglass - din favorit!"               │
└─────────────────────────────────────────────────────────┘
```

#### Skillnad mellan Chatbot och Agent:

```
CHATBOT 💬                      AGENT 🤖
═══════════                     ═══════════
Svarar på frågor                Löser problem
      ↓                               ↓
   En gång                        Många steg
      ↓                               ↓
  Inga verktyg                   Använder verktyg
      ↓                               ↓
  Kan inte lära                  Anpassar sig
```

### 💡 Pro Tips

**Tip 1: Agenter är som smarta kompisar**
De kan inte göra *magi*, men de kan:
- Tänka steg-för-steg
- Använda verktyg du ger dem
- Lära sig från misstag
- Fråga om de inte förstår

**Tip 2: Ju tydligare du är, desto bättre hjälper agenten**
❌ Dåligt: "Fixa grejer"
✅ Bra: "Hjälp mig städa rummet - börja med att plocka upp leksaker från golvet"

**Tip 3: Agenter behöver träning**
Som när du lär dig cykla - första gången är svårt, men sen blir det bättre och bättre!

### ✏️ Övningar

#### Övning 1.1: Hitta agenten

**Svårighetsgrad**: ⭐
**Tid**: ~5 minuter

**Uppgift:**
Vilka av dessa är agenter? Sätt ✓ eller ✗

1. En miniräknare som bara räknar 2+2 = 4
2. En robot som städar hela rummet själv och undviker möbler
3. En lampa som tänds när du trycker på knappen
4. Siri som kan söka recept, ställa timer och svara på frågor
5. Ett trafikljus som byter färg

**Tips:**
Tänk på: Kan den göra *flera olika saker* för att uppnå ett mål? Kan den *anpassa* sig?

<details>
<summary>💡 Lösning</summary>

1. ✗ Miniräknare - Gör bara EN sak, tänker inte själv
2. ✓ Städrobot - Planerar väg, undviker hinder, anpassar sig = AGENT!
3. ✗ Lampa - Bara på/av, ingen planering
4. ✓ Siri - Kan göra många saker, använder verktyg, planerar = AGENT!
5. ✗ Trafikljus - Följer bara ett program, anpassar sig inte

**Varför fungerar detta?**
En agent måste kunna:
- Göra flera olika saker
- Bestämma själv HUR den gör det
- Använda verktyg
- Anpassa sig till situationen

Städroboten och Siri kan allt detta, därför är de agenter!

</details>

---

#### Övning 1.2: Bygg din första "agent-plan"

**Svårighetsgrad**: ⭐⭐
**Tid**: ~7 minuter

**Uppgift:**
Du är en "Frukost-agent" som ska hjälpa någon äta frukost. Skriv ner stegen agenten skulle göra.

**Scenario:** "Jag vill ha en god och nyttig frukost!"

Fyll i planen:

```
Steg 1: Förstå vad personen gillar
Fråga: ________________________________________

Steg 2: Kolla vad som finns hemma
Verktyg att använda: __________________________

Steg 3: Föreslå alternativ
Om det finns ägg → _____________________________
Om det finns müsli → ___________________________

Steg 4: Kolla om personen är nöjd
Om JA → _______________________________________
Om NEJ → ______________________________________

Steg 5: ________________________________________
```

**Tips:**
Tänk på vad DU skulle göra om någon bad dig laga frukost!

<details>
<summary>💡 Lösning</summary>

```
Steg 1: Förstå vad personen gillar
Fråga: "Vad gillar du? Söt eller salt frukost? Allergier?"

Steg 2: Kolla vad som finns hemma
Verktyg att använda: Kolla i kylen och skåpet (inventerings-verktyg)

Steg 3: Föreslå alternativ
Om det finns ägg → "Vill du ha stekt ägg eller omelett?"
Om det finns müsli → "Müsli med yoghurt och bär?"

Steg 4: Kolla om personen är nöjd
Om JA → Börja laga maten
Om NEJ → Fråga vad som saknas, föreslå annat

Steg 5: Laga frukost och servera med en glad hälsning!
```

**Varför fungerar detta?**
Agenten gör precis som en smart hjälpreda:
1. **Förstår** behovet (nyttig frukost)
2. **Samlar information** (vad finns hemma?)
3. **Anpassar sig** till svaren (olika förslag)
4. **Validerar** (är du nöjd?)
5. **Agerar** (lagar frukost)

Det här är exakt hur riktiga LLM-agenter fungerar!

</details>

---

#### Övning 1.3: Agent eller inte Agent - Avancerad

**Svårighetsgrad**: ⭐⭐
**Tid**: ~8 minuter

**Uppgift:**
Läs dessa scenarier och förklara VARFÖR det är eller inte är en agent.

**Scenario A:**
En app som varje morgon kl 7 visar vädret på din telefon.

Agent? ☐ JA  ☐ NEJ
Motivering: _______________________________________________

**Scenario B:**
En AI-assistent som:
- Kollar ditt schema
- Ser att du har möte kl 9
- Kollar väder och trafik
- Väcker dig tidigare om det är dåligt väder
- Föreslår vad du ska ta på dig

Agent? ☐ JA  ☐ NEJ
Motivering: _______________________________________________

**Scenario C:**
Netflix som föreslår filmer baserat på vad du tittat på.

Agent? ☐ JA  ☐ NEJ
Motivering: _______________________________________________

**Bonus:**
Rita hur Scenario B:s agent skulle tänka (använd pilar och rutor som i exemplen ovan).

<details>
<summary>💡 Lösning</summary>

**Scenario A: NEJ - Inte en agent**
Motivering: Den gör bara EN förutbestämd sak (visar väder kl 7). Den anpassar sig inte, använder inga verktyg för att uppnå ett mål, och gör inga beslut. Det är bara en timer med en funktion.

**Scenario B: JA - Definitivt en agent!**
Motivering: Den:
- ✓ Samlar information från olika källor (schema, väder, trafik)
- ✓ Använder flera verktyg (kalender, väder-API, trafikdata)
- ✓ Resonerar och anpassar sig ("Om dåligt väder → väck tidigare")
- ✓ Har ett mål (att du kommer i tid till mötet)
- ✓ Tar beslut baserat på kontext

**Scenario C: Delvis - Väldigt enkel agent**
Motivering: Netflix-rekommendationer är *lite* agentiskt eftersom systemet:
- Analyserar ditt beteende
- Anpassar förslag
- HAR ett mål (att du ska titta på något du gillar)

MEN det är en väldigt enkel "agent" eftersom den:
- Bara gör EN typ av uppgift (rekommendera)
- Inte använder många verktyg
- Inte löser komplexa problem med flera steg

**Bonus - Scenario B som diagram:**

```
     Klockan 6:30 ⏰
          ↓
    ┌─────────────┐
    │  🤖 AGENT   │
    └──────┬──────┘
           │
    Steg 1: Kolla schema
           ↓
    📅 Möte kl 9:00
           │
    Steg 2: Kolla väder
           ↓
    🌧️ Regn + trafik
           │
    Steg 3: Tänk
           ↓
    "Behöver 30 min extra"
           │
    Steg 4: Agera
           ↓
    ⏰ Väck kl 6:30 (inte 7:00)
           +
    💬 "Regn idag! Ta paraply
        och kör väg 2 ist för 1"
```

**Varför fungerar detta?**
Skillnaden mellan en agent och vanlig automation är:
- **Automation:** Gör samma sak varje gång (väder kl 7)
- **Agent:** Tänker, anpassar, och beslutar baserat på situation

Ju fler "om-då-annars" beslut systemet kan ta självständigt, desto mer är det en riktig agent!

</details>

---

### 📝 Sammanfattning - Nivå 1

**Key Takeaways:**

✓ **En LLM-agent** är som en smart hjälpreda som kan tänka, planera och göra saker
✓ **Skillnaden från chatbots:** Agenter kan använda verktyg och lösa komplexa problem i flera steg
✓ **Agenter arbetar i loopar:** Tänk → Gör → Kolla → Anpassa → Upprepa
✓ **Verktyg är viktigt:** Som en kock behöver verktyg, behöver agenter tillgång till verktyg (sök, kalender, mm)
✓ **Flera agenter kan samarbeta:** Som ett lag där alla har olika roller

**Nya ord du lärt dig:**

| Ord | Betydelse |
|-----|-----------|
| **Agent** | En AI som kan tänka själv och lösa problem steg-för-steg |
| **LLM** | Large Language Model - en AI-hjärna som förstår språk |
| **Verktyg** | Digitala funktioner agenten kan använda (sök, räkna, etc) |
| **Loop/Slinga** | När agenten upprepar: försök → kolla → försök igen |
| **Multi-agent** | Flera agenter som jobbar tillsammans |

**Redo för nästa nivå?**

Nu när du förstår grunderna, är det dags att lära dig de riktiga termerna och hur agenter fungerar tekniskt! I Nivå 2 kommer du att lära dig om:
- Vad ReAct, Tool Calling och RAG betyder
- Skillnaden mellan olika typer av agenter
- Hur agenter kommunicerar med datorer
- Bygga din första enkla agent-prototyp!

🎉 **Grattis, du har klarat Nivå 1!**

---

## Nivå 2: 10-åringen - Introduktion till termer 📚

### Introduktion

Nu när du förstår grunderna är det dags att lära dig hur man pratar om LLM-agenter på riktigt! Vi kommer att introducera viktiga termer och begrepp som används i AI-världen, och du kommer att lära dig skillnaden mellan olika typer av agenter. I slutet av denna nivå kommer du att kunna förklara för dina kompisar vad "ReAct-agenter", "verktygsanrop" och "promptar" är!

### Kärnkoncept

#### 1. 🗣️ Prompts - Hur vi pratar med agenter

En **prompt** är helt enkelt det meddelande du skickar till en AI. Men för agenter är prompts extra viktiga eftersom de behöver tydliga instruktioner.

**Enkel chatbot-prompt:**
```
"Vad är huvudstaden i Sverige?"
```

**Agent-prompt:**
```
"Du är en researche-assistent. Din uppgift är att hitta information om
Stockholm. Använd verktyget 'websearch' för att söka fakta. Sammanfatta
resultaten i 3 punkter. Om du inte hittar information, förklara varför."
```

**Skillnaden:**
- Chatbot-prompts är korta frågor
- Agent-prompts innehåller:
  - 🎭 **Roll** ("Du är en research-assistent")
  - 🎯 **Mål** ("hitta information om Stockholm")
  - 🛠️ **Verktyg** ("använd websearch")
  - 📋 **Format** ("sammanfatta i 3 punkter")
  - 🚨 **Felhantering** ("om du inte hittar...")

#### 2. 🔧 Tool Calling (Verktygsanrop)

**Tool Calling** eller **Function Calling** är när agenten kan "ringa" till olika verktyg för att göra saker.

**Analogi från skolan:**
Om din mattelärare ger dig en uppgift att rita en graf:
1. Du använder **verktyget** "linjal" för att mäta
2. Du använder **verktyget** "penna" för att rita
3. Du använder **verktyget** "miniräknare" för att räkna

Agenten gör samma sak med digitala verktyg!

**Exempel på vanliga verktyg:**

| Verktyg | Vad det gör | Exempel |
|---------|-------------|---------|
| `web_search()` | Söker på internet | "Sök efter recept på pannkakor" |
| `calculator()` | Räknar matematik | "Räkna ut 15% moms på 200 kr" |
| `get_weather()` | Hämtar väderdata | "Vad blir det för väder imorgon?" |
| `send_email()` | Skickar email | "Skicka resultat till mamma@email.com" |
| `read_file()` | Läser filer | "Läs min inköpslista" |

**Hur verktygsanrop fungerar:**

```
1. Agent får uppgift: "Hur många dagar är det till jul?"
2. Agent tänker: "Jag behöver dagens datum och kunna räkna"
3. Agent anropar: get_current_date()
   → Svar: "2025-11-17"
4. Agent vet: Jul = 25 december
5. Agent anropar: calculator("dagar mellan 2025-11-17 och 2025-12-25")
   → Svar: 38 dagar
6. Agent svarar: "Det är 38 dagar till jul!"
```

#### 3. 🤔 ReAct - Reasoning and Acting

**ReAct** står för **Rea**soning (resonera) och **Act** (agera). Det är en metod där agenten växlar mellan att tänka och att göra.

**ReAct-mönstret:**

```
THOUGHT (Tanke) → ACTION (Handling) → OBSERVATION (Observation) → Upprepa
```

**Konkret exempel:**

**Uppgift:** "Vilken stad är störst i Sverige och hur många invånare har den?"

```
THOUGHT 1: "Jag behöver veta vilken stad som är störst i Sverige"
ACTION 1: web_search("största staden i Sverige")
OBSERVATION 1: "Stockholm är Sveriges största stad"

THOUGHT 2: "Nu vet jag staden, men behöver invånarantalet"
ACTION 2: web_search("Stockholm invånare 2025")
OBSERVATION 2: "Stockholm har cirka 978,000 invånare"

THOUGHT 3: "Perfekt! Nu har jag all information"
FINAL ANSWER: "Stockholm är Sveriges största stad med cirka 978,000 invånare"
```

**Varför är ReAct bra?**
- ✅ Agenten förklarar sitt tänkande (du ser hur den resonerar)
- ✅ Du kan hitta fel i logiken
- ✅ Agenten kan korrigera sig själv om något blir fel

#### 4. 🧠 RAG - Retrieval Augmented Generation

**RAG** står för **Retrieval Augmented Generation**. Det låter komplicerat, men betyder bara:

**Retrieval** = Hämta information
**Augmented** = Förbättra/Utöka
**Generation** = Skapa svar

**Enkelt förklarat:**
Istället för att agenten bara gissar svaret från sitt "minne", hämtar den först relevant information och *sen* svarar.

**Skolanalogi:**

**Utan RAG:**
Lärare: "Vad hände år 1066?"
Du (gissar): "Ehh... något med vikingar?"

**Med RAG:**
Lärare: "Vad hände år 1066?"
Du: *Slår upp i läroboken* (RETRIEVAL)
Du: *Läser om slaget vid Hastings* (AUGMENTED)
Du: "Slaget vid Hastings där William Erövraren besegrade England!" (GENERATION)

**Hur RAG fungerar för en agent:**

```
Fråga: "Vad skrev jag i min dagbok igår?"

1. RETRIEVAL:
   - Sök i dagboksdatabasen efter gårdagens inlägg
   - Hitta: "2025-11-16: Fantastisk dag! Spelade fotboll och fick mvp!"

2. AUGMENTED:
   - Ta den hämtade informationen
   - Lägg till i agentens kontext

3. GENERATION:
   - "Enligt din dagbok spelade du fotboll igår och blev MVP (Most Valuable Player)!"
```

**Varför är RAG viktigt?**
- 📚 Agenten kan använda DIN data (inte bara vad den tränats på)
- 🎯 Mer exakta svar (hämtar fakta istället för att gissa)
- 🔄 Uppdaterad information (kan hämta ny data)

#### 5. 🔁 Agent Loop (Agent-loopen)

**Agent Loop** är den process där agenten jobbar:

```
┌─────────────────────────────────────┐
│  1. Få uppgift                      │
└───────────┬─────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  2. Tänk (vad behöver jag göra?)    │
└───────────┬─────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  3. Välj ett verktyg                │
└───────────┬─────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  4. Använd verktyget                │
└───────────┬─────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  5. Läs resultatet                  │
└───────────┬─────────────────────────┘
            ↓
┌─────────────────────────────────────┐
│  6. Är uppgiften klar?              │
│     JA → Svara användaren           │
│     NEJ → Gå tillbaka till steg 2   │
└─────────────────────────────────────┘
```

**Exempel:**

**Uppgift:** "Beställ pizza till mig"

```
Loop 1:
- Tänk: "Vad för pizza vill användaren ha?"
- Verktyg: Fråga användaren
- Resultat: "Margarita"
- Klar? NEJ → fortsätt

Loop 2:
- Tänk: "Vilka pizzerior finns i närheten?"
- Verktyg: web_search("pizzerior nära [användarens adress]")
- Resultat: Lista med 5 pizzerior
- Klar? NEJ → fortsätt

Loop 3:
- Tänk: "Ring till pizzerian och beställ"
- Verktyg: phone_call() till pizzerian
- Resultat: "Beställning gjord, klar om 30 min"
- Klar? JA → Svara

Slutsvar: "Jag har beställt en Margarita från Pizzahuset, den kommer om 30 minuter!"
```

#### 6. 🎭 Typer av Agenter

Det finns flera olika typer av agenter:

**A) Task-Oriented Agents (Uppgiftsorienterade)**
- Gör EN specifik sak bra
- Exempel: Kundtjänstbot som bara hjälper med beställningar

**B) Conversational Agents (Samtalande)**
- Kan prata om mycket
- Exempel: ChatGPT, Claude

**C) Autonomous Agents (Autonoma)**
- Jobbar helt självständigt
- Exempel: En agent som övervakar ditt hem och anpassar värme/ljus automatiskt

**D) Multi-Agent Systems (Flera agenter tillsammans)**
- Flera specialiserade agenter samarbetar
- Exempel:
  - Agent 1: Researcher (forskar)
  - Agent 2: Writer (skriver)
  - Agent 3: Reviewer (granskar)

#### 7. 🧩 Context och Memory (Kontext och Minne)

**Context** = Allt agenten "vet" just nu
**Memory** = Vad agenten "kommer ihåg" från tidigare

**Short-term Memory (Korttidsminne):**
Som när du har en konversation - du minns vad ni pratade om för 2 minuter sedan.

```
Du: "Jag gillar fotboll"
Agent: "Kul! Vilket lag?"
Du: "Barcelona"
...
Du: "Berätta mer"
Agent: "Om Barcelona? De spelar i La Liga..."
(Agenten kommer ihåg att ni pratade om Barcelona)
```

**Long-term Memory (Långtidsminne):**
Agenten sparar information mellan sessioner.

```
Måndagen:
Du: "Mitt favoritlag är Barcelona"
Agent: "Noterat! ✓"

Fredagen:
Du: "Vad är mitt favoritlag?"
Agent: "Barcelona! Du sa det på måndag."
```

### Exempel

#### Exempel 1: Bygg en ReAct-sekvens för läxhjälp

**Scenario:** Agenten ska hjälpa dig med en uppsats om dinosaurier.

**Användarens fråga:** "Hjälp mig skriva en uppsats om T-Rex"

**ReAct-sekvens:**

```
THOUGHT 1: "Användaren vill ha hjälp med uppsats om T-Rex. Jag behöver
           först samla fakta om T-Rex."

ACTION 1: web_search("Tyrannosaurus Rex fakta för barn")

OBSERVATION 1: "T-Rex levde för 66 miljoner år sedan, var upp till 12
                meter lång, åt kött, hade korta armar..."

THOUGHT 2: "Bra! Nu har jag grundläggande fakta. Jag ska strukturera
           detta som en uppsats med introduktion, kropp och slutsats."

ACTION 2: generate_outline("Uppsats om T-Rex")

OBSERVATION 2:
"1. Introduktion - Vad var T-Rex?
 2. När levde T-Rex?
 3. Hur såg T-Rex ut?
 4. Vad åt T-Rex?
 5. Slutsats - Varför är T-Rex fascinerande?"

THOUGHT 3: "Perfekt! Nu har jag en struktur. Låt mig fylla i varje del
           med fakta jag hittat."

ACTION 3: write_section(section="Introduktion", facts=observation_1)

OBSERVATION 3: "Tyrannosaurus Rex, eller T-Rex, var en av de största
                köttätande dinosaurierna..."

THOUGHT 4: "Bra början! Jag fortsätter med resten av sektionerna..."

[Fortsätter tills uppsatsen är klar]

FINAL ANSWER: "Här är din uppsats om T-Rex! Jag har delat upp den i 5
              delar och använt vetenskapliga fakta. Vill du att jag
              förklarar någon del mer detaljerat?"
```

#### Exempel 2: RAG i praktiken - Fråga om din egen data

**Scenario:** Du har en samling av 100 recept i en fil, och vill att agenten hjälper dig hitta rätt.

**Utan RAG:**
```
Du: "Vilket recept har jag som använder jordgubbar?"
Agent: "Jag vet inte vilka recept DU har, men vanliga jordgubbsrecept
        är smoothies, sylt, tårta..."
(Agenten gissar bara)
```

**Med RAG:**
```
Du: "Vilket recept har jag som använder jordgubbar?"

1. RETRIEVAL:
   Agent: read_file("mina_recept.txt")
   Agent: search_in_file(query="jordgubbar")
   → Hittade 3 recept: "Jordgubbspaj", "Jordgubbssmoothie", "Jordgubbsglass"

2. AUGMENTED:
   Agent tar de hittade recepten och läser detaljerna

3. GENERATION:
   Agent: "Du har 3 recept med jordgubbar:
          1. Jordgubbspaj (sidan 15) - behöver 500g jordgubbar
          2. Jordgubbssmoothie (sidan 34) - behöver 200g jordgubbar
          3. Jordgubbsglass (sidan 67) - behöver 300g jordgubbar

          Vilket vill du testa?"
```

**Skillnaden:**
- Utan RAG: Generella gissningar
- Med RAG: Exakt information från DIN data

#### Exempel 3: Multi-Agent system - Skriva en artikel

**Scenario:** Skapa en professionell bloggpost.

**Agents och deras roller:**

```
┌─────────────────────────────────────────────────────────────┐
│                    📋 COORDINATOR AGENT                      │
│              (Koordinerar hela projektet)                    │
└────────┬────────────────────────────────────────────────────┘
         │
         │ Delegerar uppgifter till:
         │
    ┌────┴───────┬──────────────┬──────────────┐
    │            │              │              │
    ▼            ▼              ▼              ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ RESEARCH│  │ WRITER  │  │ EDITOR  │  │ SEO     │
│ AGENT   │  │ AGENT   │  │ AGENT   │  │ AGENT   │
└─────────┘  └─────────┘  └─────────┘  └─────────┘
```

**Arbetsflöde:**

```
Steg 1 - Research Agent:
- Uppgift: "Hitta information om LLM-agenter"
- Verktyg: web_search(), read_articles()
- Resultat: Lista med 10 källor och sammanfattning

Steg 2 - Writer Agent:
- Uppgift: "Skriv artikel baserat på research"
- Input: Research Agents sammanfattning
- Resultat: Första utkastet av artikeln (800 ord)

Steg 3 - Editor Agent:
- Uppgift: "Granska artikeln och förbättra"
- Input: Writer Agents utkast
- Verktyg: grammar_check(), readability_score()
- Resultat: Korrigerad version med bättre flöde

Steg 4 - SEO Agent:
- Uppgift: "Optimera för sökmotorer"
- Input: Editor Agents version
- Verktyg: keyword_analysis(), meta_description_generator()
- Resultat: Slutversion + meta-taggar + nyckelord

Steg 5 - Coordinator:
- Samlar allt
- Presenterar för användaren
- "Här är din färdiga artikel, optimerad och polerad!"
```

**Varför multi-agent?**
- 🎯 Varje agent gör vad den är bäst på
- ⚡ Kan jobba parallellt (snabbare)
- ✅ Högre kvalitet (specialisering)

### Visualisering

#### Tool Calling - Steg för steg

```
┌──────────────────────────────────────────────────┐
│  👤 ANVÄNDARE                                     │
│  "Hur mycket kostar 5 äpplen om ett kostar 3kr?" │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│  🤖 AGENT                                         │
│  Analyserar frågan...                            │
│  "Jag behöver multiplicera 5 × 3"               │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│  🔧 TOOL CALL                                     │
│  calculator(operation="multiply", a=5, b=3)      │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│  💻 VERKTYGET                                     │
│  Räknar: 5 × 3 = 15                              │
│  Returnerar: 15                                  │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│  🤖 AGENT                                         │
│  Tar emot svar: 15                               │
│  Formulerar svar                                 │
└────────────────┬─────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────┐
│  👤 ANVÄNDARE                                     │
│  "5 äpplen kostar 15 kronor"                     │
└──────────────────────────────────────────────────┘
```

#### RAG vs Vanlig Generation

```
╔═══════════════════════════════════════════════════════════╗
║                  VANLIG GENERATION (Utan RAG)              ║
╚═══════════════════════════════════════════════════════════╝

Fråga: "Vad stod det i min mejl från Maria?"
                    ↓
         ┌─────────────────┐
         │  🤖 LLM Agent   │
         │   (Gissar)      │
         └─────────────────┘
                    ↓
"Jag kan inte komma åt dina mejl, men vanligtvis innehåller
mejl hälsningar och information..."
❌ Inte användbart!


╔═══════════════════════════════════════════════════════════╗
║              RAG (Retrieval Augmented Generation)          ║
╚═══════════════════════════════════════════════════════════╝

Fråga: "Vad stod det i min mejl från Maria?"
                    ↓
         ┌─────────────────┐
         │  📥 RETRIEVAL   │
         │ read_email()    │
         │ search("Maria") │
         └────────┬────────┘
                  │
    ┌─────────────┴─────────────┐
    │ Hämtat mejl:              │
    │ "Från: Maria              │
    │  Hej! Mötet flyttas       │
    │  till fredag kl 14."      │
    └─────────────┬─────────────┘
                  │
         ┌────────▼────────┐
         │  🤖 + 📄        │
         │  LLM + Data     │
         └────────┬────────┘
                  │
                  ▼
"Maria skrev att mötet flyttas till fredag kl 14."
✅ Perfekt svar!
```

#### Jämförelse: Olika agenttyper

```
┌─────────────────────────────────────────────────────────┐
│  TASK-ORIENTED AGENT                                    │
│  ────────────────────────────────────────────────       │
│  Specialiserad på EN uppgift                            │
│                                                          │
│  Exempel: Pizza-beställningsbot                         │
│  ┌──────────────────────────────────────┐              │
│  │ Kan:                                 │              │
│  │ ✓ Ta beställning                     │              │
│  │ ✓ Kolla meny                         │              │
│  │ ✓ Beräkna pris                       │              │
│  │ ✓ Skicka beställning                 │              │
│  │                                      │              │
│  │ Kan INTE:                            │              │
│  │ ✗ Prata om vädret                    │              │
│  │ ✗ Hjälpa med läxor                   │              │
│  └──────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  CONVERSATIONAL AGENT                                   │
│  ────────────────────────────────────────────────       │
│  Generalist - kan prata om mycket                       │
│                                                          │
│  Exempel: ChatGPT, Claude                               │
│  ┌──────────────────────────────────────┐              │
│  │ Kan:                                 │              │
│  │ ✓ Svara på frågor                    │              │
│  │ ✓ Hjälpa med kod                     │              │
│  │ ✓ Skriva texter                      │              │
│  │ ✓ Förklara koncept                   │              │
│  │ ✓ Översätta                          │              │
│  │                                      │              │
│  │ Begränsning:                         │              │
│  │ → Oftast ingen verktygsåtkomst       │              │
│  └──────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  AUTONOMOUS AGENT                                       │
│  ────────────────────────────────────────────────       │
│  Jobbar helt självständigt                              │
│                                                          │
│  Exempel: Smart hem-system                              │
│  ┌──────────────────────────────────────┐              │
│  │ Gör utan att fråga:                  │              │
│  │ ✓ Justerar temperatur                │              │
│  │ ✓ Släcker lampor när du går          │              │
│  │ ✓ Varnar för ovanliga ljud           │              │
│  │ ✓ Beställer mat när kylen är tom     │              │
│  │ ✓ Rapporterar varje vecka            │              │
│  └──────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────┘
```

### 💡 Pro Tips

**Tip 1: Bra prompts = Bra resultat**
Ju mer detaljer du ger agenten, desto bättre svar får du!

❌ Dålig prompt: "Hjälp mig"
✅ Bra prompt: "Hjälp mig skriva en inbjudan till min födelsedag. Jag fyller 10 år och festen är på lördag kl 14."

**Tip 2: Förstå agent-loopen**
Om agenten gör något konstigt, tänk på loopen:
- Förstod den uppgiften rätt? (Tänk-steget)
- Valde den rätt verktyg? (Verktyg-steget)
- Tolkade den resultatet rätt? (Observation-steget)

**Tip 3: RAG gör agenter smartare**
Om du vill att agenten ska veta om DIN specifika data (dina filer, dina anteckningar), använd RAG! Annars gissar den bara.

**Tip 4: Multi-agent för komplexa uppgifter**
Som när du gör grupparbete - dela upp arbetet!
- En agent researchar
- En agent skriver
- En agent kollar kvalitet

### ✏️ Övningar

#### Övning 2.1: Identifiera verktygsanrop

**Svårighetsgrad**: ⭐⭐
**Tid**: ~8 minuter

**Uppgift:**
En agent får uppgiften: "Planera min dag imorgon"

Vilka verktyg skulle agenten behöva använda? Lista minst 5 verktyg och vad de gör.

```
1. Verktyg: _______________  Vad det gör: _______________
2. Verktyg: _______________  Vad det gör: _______________
3. Verktyg: _______________  Vad det gör: _______________
4. Verktyg: _______________  Vad det gör: _______________
5. Verktyg: _______________  Vad det gör: _______________
```

**Tips:**
Tänk på vad agenten behöver veta för att planera dagen: väder, schema, restid, mm.

<details>
<summary>💡 Lösning</summary>

```
1. Verktyg: get_calendar()
   Vad det gör: Hämtar användarens schema/bokningar för imorgon

2. Verktyg: get_weather("tomorrow")
   Vad det gör: Kollar väderprognosen för att planera kläder/aktiviteter

3. Verktyg: get_current_time()
   Vad det gör: Behöver veta nuvarande tid för att planera realistiskt

4. Verktyg: calculate_travel_time(från, till)
   Vad det gör: Räknar ut restid mellan möten/aktiviteter

5. Verktyg: get_todo_list()
   Vad det gör: Kollar vad som behöver göras så det kan planeras in

6. Bonus: get_meal_plan() eller suggest_meals()
   Vad det gör: Föreslår när det är dags att äta baserat på schemat
```

**Varför fungerar detta?**
För att planera en dag behöver agenten:
- Veta vad som redan är planerat (kalender)
- Anpassa för yttre faktorer (väder)
- Vara realistisk med tid (restid, nuvarande tid)
- Inkludera uppgifter som behöver göras (todo)

Det här visar hur agenter kombinerar FLERA verktyg för att lösa EN uppgift!

</details>

---

#### Övning 2.2: Skriv en ReAct-sekvens

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~12 minuter

**Uppgift:**
Skriv en komplett ReAct-sekvens för följande uppgift:

**Scenario:** "Jag behöver köpa en present till mormor som fyller 75 år. Hon gillar trädgårdsarbete. Budget: 300 kr."

Fyll i mallen:

```
THOUGHT 1: _________________________________________________
ACTION 1: __________________________________________________
OBSERVATION 1: _____________________________________________

THOUGHT 2: _________________________________________________
ACTION 2: __________________________________________________
OBSERVATION 2: _____________________________________________

THOUGHT 3: _________________________________________________
ACTION 3: __________________________________________________
OBSERVATION 3: _____________________________________________

FINAL ANSWER: ______________________________________________
```

**Tips:**
- Agenten behöver förstå: vem, intressen, budget
- Använd verktyg för att söka produkter
- Jämför alternativ innan beslut

<details>
<summary>💡 Lösning</summary>

```
THOUGHT 1: "Användaren vill ha present till mormor, 75 år, gillar
           trädgård, budget 300 kr. Jag bör söka efter trädgårds-
           relaterade presenter i den prisklassen."

ACTION 1: web_search("trädgårdspresent present under 300 kr")

OBSERVATION 1: "Hittade flera alternativ: trädgårdshandskar (89 kr),
               fröpaket (120 kr), planteringskärl (250 kr),
               trädgårdsbok (199 kr), knäskydd för trädgård (150 kr)"

THOUGHT 2: "Bra alternativ! Men vilket är bäst för en 75-åring?
           Knäskydd låter praktiskt eftersom det kan vara tungt att
           knäböja vid den åldern. Låt mig kolla recensioner."

ACTION 2: get_product_reviews("trädgårds knäskydd")

OBSERVATION 2: "Genomsnitt 4.5/5 stjärnor. Många äldre användare
               säger det hjälper deras knän. Pris: 149 kr. Finns
               på Plantagen och Bauhaus."

THOUGHT 3: "Utmärkt! Priset är under budget, bra recensioner, och
           praktiskt. Jag kan föreslå detta, och kanske kombinera
           med fröpaketet eftersom jag har 151 kr kvar av budgeten."

ACTION 3: calculator(300 - 149)

OBSERVATION 3: "151 kronor kvar"

FINAL ANSWER: "Jag rekommenderar trädgårds-knäskydd (149 kr) som
              huvudpresent - perfekt för någon som älskar trädgård
              och är 75 år. Du har 151 kr kvar, så du kan lägga till
              ett fint fröpaket (120 kr) med till exempel tomater
              eller blommor. Total: 269 kr, under budgeten! Finns på
              Plantagen och Bauhaus."
```

**Varför fungerar detta?**
ReAct-sekvensen visar att agenten:
1. **Förstår kontexten** (ålder, intresse, budget)
2. **Söker brett först** (flera alternativ)
3. **Resonerar** om vad som passar bäst
4. **Validerar valet** (kollar recensioner)
5. **Optimerar** (använder hela budgeten smart)
6. **Ger konkret svar** med var man köper

Det här är betydligt smartare än att bara säga "Köp en blomma" - agenten resonerar som en människa!

</details>

---

#### Övning 2.3: RAG eller Vanlig Generation?

**Svårighetsgrad**: ⭐⭐
**Tid**: ~8 minuter

**Uppgift:**
För varje scenario, bestäm om du behöver RAG eller om vanlig generation räcker. Förklara varför!

**Scenario A:** "Vad är 15 × 23?"
Behöver RAG? ☐ JA  ☐ NEJ
Varför? ____________________________________________________

**Scenario B:** "Vilka möten har jag nästa vecka?"
Behöver RAG? ☐ JA  ☐ NEJ
Varför? ____________________________________________________

**Scenario C:** "Förklara vad fotosyntesen är"
Behöver RAG? ☐ JA  ☐ NEJ
Varför? ____________________________________________________

**Scenario D:** "Sammanfatta de tre senaste dokumenten jag jobbat på"
Behöver RAG? ☐ JA  ☐ NEJ
Varför? ____________________________________________________

**Scenario E:** "Vem vann fotbolls-VM 1994?"
Behöver RAG? ☐ JA  ☐ NEJ
Varför? ____________________________________________________

<details>
<summary>💡 Lösning</summary>

**Scenario A: NEJ**
Varför? Matematik kan agenten räkna ut själv med sitt inbyggda kunnande eller med calculator-verktyget. Ingen extern data behövs.

**Scenario B: JA - Behöver RAG!**
Varför? Agenten kan inte GISSA dina möten. Den måste HÄMTA (retrieve) från din kalender för att veta exakt vad du har bokat. Detta är klassisk RAG-användning.

**Scenario C: NEJ**
Varför? Fotosyntesen är allmän kunskap som agenten tränats på. Den kan förklara detta utan att hämta extern data. (Obs: Om du ville ha en specifik forskningsartikel om fotosyntesen skulle RAG behövas.)

**Scenario D: JA - Behöver RAG!**
Varför? Agenten måste LÄSA dina dokument för att kunna sammanfatta dem. Den behöver:
1. Hitta de tre senaste dokumenten (retrieval)
2. Läsa innehållet (retrieval)
3. Sammanfatta baserat på faktiskt innehåll (generation med kontext)

**Scenario E: NEJ (mestadels)**
Varför? VM 1994 vann Brasilien - detta är historisk fakta som agenten troligen känner till. DOCK: Om du ville ha detaljerad statistik från matcherna skulle RAG kunna göra svaret bättre genom att hämta exakt data.

**Sammanfattning - När behövs RAG?**

```
Behöver RAG när:
✓ Frågan gäller DIN specifika data (dina filer, din kalender, dina mejl)
✓ Du vill ha exakt information (citat, siffror från dokument)
✓ Informationen ändras ofta (dagens aktiekurs, senaste nytt)
✓ Informationen är för ny för agentens träningsdata

Behöver INTE RAG när:
✗ Allmän kunskap (huvudstäder, historiska händelser)
✗ Enkel matematik eller logik
✗ Generella förklaringar av koncept
✗ Kreativa uppgifter (skriv en dikt)
```

</details>

---

#### Övning 2.4: Designa ett Multi-Agent system

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Du ska designa ett multi-agent system för att planera och genomföra en skoltripp.

**Uppgift:** "Planera en endags skoltripp för 25 elever till ett museum i Stockholm"

Fyll i:

1. Hur många agenter behövs? ______

2. Lista varje agent och dess roll:

```
Agent 1:
Namn: _______________
Roll: _______________
Verktyg den använder: _______________

Agent 2:
Namn: _______________
Roll: _______________
Verktyg den använder: _______________

[Lägg till fler om det behövs]
```

3. Rita arbetsflödet mellan agenterna (använd pilar för att visa vem som pratar med vem)

4. Vilken agent startar processen? _______________

5. Vilken agent avslutar processen? _______________

**Bonus:**
Vad händer om en agent stöter på problem? T.ex. om bussen är fullbokad?

<details>
<summary>💡 Lösning</summary>

**1. Antal agenter:** 5-6 agenter

**2. Agenter och roller:**

```
Agent 1:
Namn: Coordinator (Koordinator)
Roll: Övergripande planering och delegering av uppgifter
Verktyg: task_delegator(), timeline_creator()

Agent 2:
Namn: Museum Scout (Museumssökare)
Roll: Hitta lämpliga museum, kolla öppettider, boka biljetter
Verktyg: web_search(), museum_booking_api(), get_availability()

Agent 3:
Namn: Transport Planner (Transportplanerare)
Roll: Ordna transport (buss eller tåg) för 25 elever
Verktyg: bus_booking_api(), calculate_route(), get_price_quote()

Agent 4:
Namn: Budget Manager (Budgetansvarig)
Roll: Hålla koll på kostnader och se till det håller budget
Verktyg: calculator(), expense_tracker(), budget_checker()

Agent 5:
Namn: Schedule Master (Schemaläggare)
Roll: Skapa en detaljerad tidsplan för dagen
Verktyg: timeline_generator(), time_calculator(), create_itinerary()

Agent 6:
Namn: Risk Assessor (Riskbedömare)
Roll: Kolla säkerhet, väder, backup-planer
Verktyg: weather_api(), safety_checker(), emergency_planner()
```

**3. Arbetsflöde:**

```
                    ┌─────────────────┐
                    │   COORDINATOR   │ ← Startar här
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
          ┌──────────┐ ┌──────────┐ ┌──────────┐
          │ MUSEUM   │ │TRANSPORT │ │ BUDGET   │
          │ SCOUT    │ │ PLANNER  │ │ MANAGER  │
          └────┬─────┘ └────┬─────┘ └────┬─────┘
               │            │            │
               └────────────┼────────────┘
                            │
                            ▼ (Alla rapporterar tillbaka)
                    ┌───────────────┐
                    │  SCHEDULE     │
                    │  MASTER       │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  RISK         │
                    │  ASSESSOR     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  COORDINATOR  │ ← Avslutar här
                    │  (Final plan) │
                    └───────────────┘
```

**4. Startagent:** Coordinator

**5. Avslutningsagent:** Coordinator (samlar all info och presenterar final plan)

**Bonus - Felhantering:**

Om Transport Planner stöter på "Buss fullbokad":

```
Transport Planner:
  ↓
  "Buss fullbokad för önskat datum"
  ↓
  THOUGHT: "Jag behöver alternativ"
  ↓
  ACTION 1: Kolla andra bussbolag
  ACTION 2: Kolla tåg som alternativ
  ↓
  Rapporterar till Coordinator:
  "Buss fullbokad, men tåg finns för +50 kr/person"
  ↓
Coordinator frågar Budget Manager:
  "Har vi råd med +50 kr × 25 elever?"
  ↓
Budget Manager:
  "Ja, vi har marginal"
  ↓
Coordinator till Transport Planner:
  "Boka tåg istället"
  ↓
Schedule Master:
  Justerar tidsplanen för tågtider
  ↓
✅ Problem löst genom agent-samarbete!
```

**Varför fungerar detta?**

Multi-agent systemet är kraftfullt eftersom:
1. **Specialisering:** Varje agent fokuserar på sin expertis
2. **Parallellisering:** Museum Scout och Transport Planner kan jobba samtidigt
3. **Felhantering:** Om en agent stöter på problem kan andra hjälpa till
4. **Koordinering:** Coordinator ser till att allt hänger ihop
5. **Kvalitetskontroll:** Risk Assessor kollar slutresultatet

För en komplex uppgift som att planera en skoltripp är multi-agent betydligt bättre än en ensam agent!

</details>

---

#### Övning 2.5: Prompt Engineering

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~12 minuter

**Uppgift:**
Förbättra dessa prompts för att ge agenten bättre instruktioner.

**Prompt A (dålig):**
```
"Skriv något om katter"
```

Förbättrad version:
```
___________________________________________________________
___________________________________________________________
___________________________________________________________
```

**Prompt B (dålig):**
```
"Hjälp mig"
```

Förbättrad version:
```
___________________________________________________________
___________________________________________________________
___________________________________________________________
```

**Prompt C (okej, men kan bli bättre):**
```
"Hitta en film åt mig"
```

Förbättrad version:
```
___________________________________________________________
___________________________________________________________
___________________________________________________________
```

**Tips:**
En bra prompt innehåller:
- Roll (vem är agenten?)
- Uppgift (vad ska göras?)
- Kontext (varför/för vem?)
- Format (hur ska resultatet se ut?)
- Verktyg (om specifika verktyg behövs)

<details>
<summary>💡 Lösning</summary>

**Prompt A - Förbättrad:**

```
Du är en djurexpert som ska skriva för barn i åldern 8-10 år.

Uppgift: Skriv en kort, rolig text om katter (cirka 150 ord) som
förklarar:
1. Varför katter spinner
2. Varför de har morrhår
3. En rolig kattfakta

Format: Skriv i enkelt språk med 3 korta stycken. Avsluta med en
fråga till läsaren.

Ton: Entusiastisk och pedagogisk.
```

**Varför är detta bättre?**
- ✓ Tydlig roll (djurexpert för barn)
- ✓ Specifik uppgift (3 punkter att täcka)
- ✓ Klart format (150 ord, 3 stycken)
- ✓ Målgrupp definierad (8-10 år)
- ✓ Ton angiven (entusiastisk)

---

**Prompt B - Förbättrad:**

```
Du är en läxhjälp-assistent för gymnasieelever.

Situation: Jag har en matteuppgift jag inte förstår - "Lös ekvationen
2x + 5 = 15"

Uppgift: Hjälp mig förstå PROCESSEN, inte bara ge svaret.
1. Förklara steg-för-steg vad jag ska göra
2. Förklara VARFÖR varje steg fungerar
3. Ge mig en liknande övningsuppgift att prova själv

Verktyg: Du kan använda calculator() om du behöver räkna.

Format: Numrera stegen tydligt.
```

**Varför är detta bättre?**
- ✓ Specifik situation (ekvationen är given)
- ✓ Klart mål (förstå processen)
- ✓ Steg-för-steg bruten ned
- ✓ Inkluderar pedagogik (varför, inte bara vad)
- ✓ Verktyg specificerade

---

**Prompt C - Förbättrad:**

```
Du är en film-rekommendationsagent.

Kontext: Jag vill ha en film att titta på ikväll med min familj
(föräldrar + barn 7 och 10 år).

Preferenser:
- Genre: Äventyr eller komedi
- INTE skräck eller våld
- Helst något från 2020-talet
- Tillgängligt på Netflix eller Disney+

Uppgift:
1. Använd web_search() för att hitta filmer som matchar kriterierna
2. Föreslå TOP 3 filmer
3. För varje film, inkludera: titel, år, kort sammanfattning (2
   meningar), varför den passar familjen, vilken tjänst den finns på

Format:
Film 1: [Titel]
- År: [år]
- Handling: [2 meningar]
- Varför: [1 mening]
- Tjänst: [Netflix/Disney+]

[Samma för Film 2 och 3]
```

**Varför är detta bättre?**
- ✓ Kontext given (familj med barn i specifika åldrar)
- ✓ Preferenser listade (genre, tid, plattform)
- ✓ Begränsningar tydliga (inget våld)
- ✓ Exakt format specificerat
- ✓ Verktyg namngivna (web_search)
- ✓ Antal resultat angivet (TOP 3)

---

**Sammanfattning - Prompt Engineering Principer:**

```
❌ Dålig prompt:
"Gör något"

✅ Bra prompt:
┌─────────────────────────────────────┐
│ 1. ROLL: Du är en [expert/assistent]│
│ 2. KONTEXT: [Varför/För vem]        │
│ 3. UPPGIFT: [Specifikt vad]         │
│ 4. FORMAT: [Hur resultatet ser ut]  │
│ 5. VERKTYG: [Om specifika behövs]   │
│ 6. BEGRÄNSNINGAR: [Vad INTE göra]   │
└─────────────────────────────────────┘
```

Kom ihåg: Ju tydligare du är, desto bättre resultat får du! Agenten gissar inte - den följer instruktioner.

</details>

---

### 📝 Sammanfattning - Nivå 2

**Key Takeaways:**

✓ **Prompts är viktiga:** Tydliga instruktioner = bättre resultat. Inkludera roll, uppgift, format och kontext.

✓ **Tool Calling:** Agenter kan "ringa" verktyg som calculator, web_search, send_email för att göra saker.

✓ **ReAct (Reasoning + Acting):** Agenter växlar mellan att tänka (THOUGHT) och göra (ACTION), kollar resultatet (OBSERVATION), och upprepar.

✓ **RAG (Retrieval Augmented Generation):** Istället för att gissa hämtar agenten först relevant data från dina filer/databaser, sen svarar den med exakt information.

✓ **Agent Loop:** Kontinuerlig process: Få uppgift → Tänk → Välj verktyg → Använd verktyg → Kolla resultat → Upprepa tills klar.

✓ **Olika typer av agenter:**
- Task-oriented: Specialiserade på EN uppgift
- Conversational: Generalist som kan prata om mycket
- Autonomous: Jobbar helt självständigt
- Multi-agent: Flera agenter samarbetar

✓ **Minne:** Kort-tids (pågående konversation) vs Lång-tids (sparas mellan sessioner)

**Nya termer du lärt dig:**

| Term | Engelsk term | Betydelse |
|------|--------------|-----------|
| **Prompt** | Prompt | Instruktion/meddelande till AI |
| **Verktygsanrop** | Tool Calling / Function Calling | När agenten använder verktyg |
| **ReAct** | ReAct | Reasoning + Acting (tänka och agera) |
| **RAG** | Retrieval Augmented Generation | Hämta data först, sen svara |
| **Agent Loop** | Agent Loop | Återkommande process: tänk-gör-kolla-upprepa |
| **Kontext** | Context | Vad agenten "vet" just nu |
| **Minne** | Memory | Vad agenten "kommer ihåg" |
| **Autonomous** | Autonomous | Självständig, jobbar utan ständig input |

**Redo för nästa nivå?**

Nu har du lärt dig grundtermerna och hur agenter fungerar! I Nivå 3 går vi djupare in på det tekniska:
- Hur man faktiskt bygger en agent med kod
- Introducerar LangChain, AutoGen, och andra frameworks
- Skapar din första riktiga agent
- Förstår arkitekturer och design patterns
- Implementerar RAG och ReAct från grunden

🎉 **Grattis, du har klarat Nivå 2!**

---

