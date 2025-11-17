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

## Nivå 3a: Gymnasiet - Tekniska Detaljer (Del 1) 💻

### Introduktion

Nu blir det seriöst! I denna nivå kommer du att lära dig hur man faktiskt bygger LLM-agenter med kod. Vi går igenom de populäraste frameworks, visar konkreta kodexempel, och lär dig best practices från 2025. Du kommer att skriva din första fungerande agent och förstå hur proffs bygger produktionsklara system. Efter denna nivå kan du börja bygga egna agentprojekt!

**Vad du kommer att lära dig:**
- Praktisk implementation med Python och moderna frameworks
- LangChain, LangGraph, AutoGen, CrewAI
- Verkliga kodexempel du kan köra direkt
- Priser och kostnadsoptimering för olika LLM-providers
- Säkerhet och best practices 2025

### Kärnkoncept

#### 1. 💰 LLM Pricing - Kostnader 2025

Innan du börjar bygga agenter måste du förstå kostnadsstrukturen. Här är de senaste priserna (november 2025):

**Major LLM Providers - Priser per miljon tokens:**

| Provider | Modell | Input ($/1M) | Output ($/1M) | Context Window | Best For |
|----------|--------|--------------|---------------|----------------|----------|
| **OpenAI** | GPT-4o | $2.50 | $10.00 | 128K | Generalist, komplex reasoning |
| OpenAI | GPT-4o-mini | $0.15 | $0.60 | 128K | Snabba, enkla uppgifter |
| **Anthropic** | Claude 4.5 Sonnet | $3.00 | $15.00 | 200K | Längre kontext, coding |
| Anthropic | Claude 4.5 Haiku | $0.25 | $1.25 | 200K | Snabba responses |
| **Google** | Gemini 2.0 Pro | $1.25 | $5.00 | 1M | Massiv context, multimodal |
| Google | Gemini 2.0 Flash | $0.075 | $0.30 | 1M | Billigast, snabbast |
| **DeepSeek** | DeepSeek-R1 | $0.55 | $2.19 | 64K | Cost-effective reasoning |

**Viktig insikt från 2025:**
- **Output tokens kostar 3-5x mer** än input tokens
- **Gemini Flash** är billigast för höga volymer
- **Claude 4.5** har längst context window (200K tokens)
- **Gemini 2.0 Pro** har extremt lång context (1M tokens!) - perfekt för RAG

**Kostnadsexempel:**

En chatbot som hanterar 100,000 konversationer/dag:
- Genomsnitt: 500 input tokens, 200 output tokens per konversation

```python
# Beräkning för GPT-4o
input_cost = (500 * 100000 / 1_000_000) * 2.50   # $125/dag
output_cost = (200 * 100000 / 1_000_000) * 10.00 # $200/dag
total_daily = input_cost + output_cost            # $325/dag
monthly_cost = total_daily * 30                   # $9,750/månad

# Jämför med Gemini Flash
input_cost_gemini = (500 * 100000 / 1_000_000) * 0.075   # $3.75/dag
output_cost_gemini = (200 * 100000 / 1_000_000) * 0.30   # $6/dag
total_daily_gemini = input_cost_gemini + output_cost_gemini # $9.75/dag
monthly_cost_gemini = total_daily_gemini * 30              # $292.50/månad

# Besparing: $9,750 - $292.50 = $9,457.50/månad (97% billigare!)
```

#### 2. 🛠️ Agent Frameworks 2025

**Översikt av populära frameworks:**

**A) LangChain + LangGraph**

LangChain är det mest använda frameworket, med 110K+ GitHub stars (2025). LangGraph 1.0 släpptes i oktober 2024 och är nu standard för stateful agents.

```python
# Installation
pip install langchain langchain-openai langgraph

# Enkel agent med LangChain
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate

# 1. Definiera verktyg
@tool
def get_weather(city: str) -> str:
    """Hämtar väder för en stad"""
    # I verkligheten: API-anrop
    return f"Soligt och 22°C i {city}"

@tool
def calculator(expression: str) -> float:
    """Räknar matematiska uttryck"""
    return eval(expression)  # OBS: Använd inte eval() i produktion!

# 2. Sätt upp LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",  # Billigare för enkla agents
    temperature=0         # Deterministisk för agents
)

# 3. Skapa prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "Du är en hjälpsam assistent med tillgång till verktyg."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")  # För agent reasoning
])

# 4. Skapa agent
tools = [get_weather, calculator]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Kör agent
result = agent_executor.invoke({
    "input": "Vad är vädret i Stockholm och hur många grader Fahrenheit är det?"
})
print(result["output"])
```

**Output exempel:**
```
> Entering new AgentExecutor chain...

Thought: Jag behöver först få vädret i Stockholm, sen konvertera till Fahrenheit

Action: get_weather
Action Input: Stockholm
Observation: Soligt och 22°C i Stockholm

Thought: Nu behöver jag konvertera 22°C till Fahrenheit med formeln F = C * 9/5 + 32

Action: calculator
Action Input: 22 * 9/5 + 32
Observation: 71.6

Thought: Nu har jag all information

Final Answer: Det är soligt och 22°C (71.6°F) i Stockholm!
```

**B) LangGraph - Stateful Agent Workflows**

LangGraph 1.0 (2024) introducerade graph-baserade agent flows med persistens och checkpoints.

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator

# 1. Definiera state
class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    next_step: str
    data: dict

# 2. Definiera nodes (steg i agenten)
def research_node(state: AgentState):
    """Researchar information"""
    # Gör research...
    return {
        "messages": [("assistant", "Research done!")],
        "next_step": "analyze",
        "data": {"research": "findings"}
    }

def analyze_node(state: AgentState):
    """Analyserar research"""
    # Analysera...
    return {
        "messages": [("assistant", "Analysis complete!")],
        "next_step": "write",
        "data": {**state["data"], "analysis": "insights"}
    }

def write_node(state: AgentState):
    """Skriver rapport"""
    return {
        "messages": [("assistant", "Report written!")],
        "next_step": END
    }

# 3. Bygg graph
workflow = StateGraph(AgentState)

# Lägg till nodes
workflow.add_node("research", research_node)
workflow.add_node("analyze", analyze_node)
workflow.add_node("write", write_node)

# Lägg till edges (flöde)
workflow.set_entry_point("research")
workflow.add_edge("research", "analyze")
workflow.add_edge("analyze", "write")
workflow.add_edge("write", END)

# 4. Kompilera
app = workflow.compile()

# 5. Kör med state persistence
result = app.invoke({
    "messages": [],
    "next_step": "research",
    "data": {}
})

print(result)
```

**Varför LangGraph?**
- ✅ Stateful - agent kommer ihåg mellan steg
- ✅ Checkpoints - kan återuppta om något går fel
- ✅ Human-in-the-loop - kan pausa och fråga användaren
- ✅ Parallella branches - flera agents samtidigt

**C) AutoGen - Multi-Agent Conversations**

AutoGen (Microsoft) specialiserar sig på multi-agent dialoger.

```python
from autogen import AssistantAgent, UserProxyAgent

# 1. Konfigurera LLM
llm_config = {
    "model": "gpt-4o",
    "api_key": "your-api-key",
    "temperature": 0.7
}

# 2. Skapa agents
# Assistant som skriver kod
coder = AssistantAgent(
    name="Coder",
    system_message="Du är en expert Python-utvecklare. Skriv ren, testbar kod.",
    llm_config=llm_config
)

# Assistant som granskar kod
reviewer = AssistantAgent(
    name="Reviewer",
    system_message="Du granskar kod för bugs och förbättringar.",
    llm_config=llm_config
)

# User proxy som kör kod
user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Kör automatiskt
    code_execution_config={"work_dir": "coding"}
)

# 3. Starta konversation
user_proxy.initiate_chat(
    coder,
    message="Skriv en funktion som beräknar Fibonacci-tal rekursivt och iterativt. Inkludera tester."
)

# Agenter pratar nu med varandra tills uppgiften är klar!
```

**D) CrewAI - Role-Based Teams**

CrewAI fokuserar på team-baserade agents med tydliga roller.

```python
from crewai import Agent, Task, Crew, Process

# 1. Definiera agents med roller
researcher = Agent(
    role='Researcher',
    goal='Hitta och sammanfatta information om LLM-agenter',
    backstory='Expert på AI-research med fokus på praktiska implementationer',
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='Tech Writer',
    goal='Skriv pedagogiska artiklar om AI',
    backstory='Erfaren teknisk författare som gör komplexa ämnen begripliga',
    verbose=True,
    allow_delegation=False
)

# 2. Definiera tasks
research_task = Task(
    description='Research de 5 viktigaste trenderna inom LLM-agenter 2025',
    agent=researcher,
    expected_output='Bullet-lista med 5 trender och korta beskrivningar'
)

writing_task = Task(
    description='Skriv en bloggpost baserat på researchen',
    agent=writer,
    expected_output='800-ord bloggpost i markdown-format'
)

# 3. Skapa crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential  # Eller Process.hierarchical
)

# 4. Kör
result = crew.kickoff()
print(result)
```

**E) Vercel AI SDK 6.0 (2025)**

Ny på scenen men extremt populär för web-applikationer.

```typescript
// Installation: npm install ai @ai-sdk/openai

import { openai } from '@ai-sdk/openai';
import { generateText, tool } from 'ai';
import { z } from 'zod';

// 1. Definiera verktyg med Zod schema
const weatherTool = tool({
  description: 'Hämta väder för en stad',
  parameters: z.object({
    city: z.string().describe('Stadens namn'),
  }),
  execute: async ({ city }) => {
    // API-anrop här
    return { temp: 22, condition: 'sunny', city };
  },
});

// 2. Kör agent
const { text } = await generateText({
  model: openai('gpt-4o'),
  tools: { weather: weatherTool },
  maxSteps: 5,  // Max antal tool calls
  prompt: 'Vad är vädret i Stockholm och Paris?',
});

console.log(text);
```

**Framework Jämförelse 2025:**

| Framework | Best For | Svårighet | GitHub Stars | Production Ready |
|-----------|----------|-----------|--------------|------------------|
| LangChain | Generalist, RAG | Medel | 110K+ | ✅ Ja |
| LangGraph | Complex workflows | Hög | (del av LangChain) | ✅ Ja |
| AutoGen | Multi-agent dialogs | Medel | 35K+ | ✅ Ja |
| CrewAI | Role-based teams | Låg | 25K+ | ⚠️ Beta |
| Vercel AI SDK | Web apps, TypeScript | Låg | 15K+ | ✅ Ja |

#### 3. 🎯 Best Practices 2025

**A) Prompt Caching - Spara 90% på kostnader**

Ny feature från 2024 som cachar system prompts.

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-key")

# Lång system prompt som sällan ändras
SYSTEM_PROMPT = """
Du är en expert Python-utvecklare...
[2000 ord med exempel, guidelines, etc]
"""

# Första anropet - betalar för hela prompten
response = client.messages.create(
    model="claude-4.5-sonnet-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"}  # Cache i 5 min
        }
    ],
    messages=[{"role": "user", "content": "Skriv en funktion som..."}]
)

# Nästa anrop inom 5 min - betalar bara 10% för cachad prompt!
response2 = client.messages.create(
    model="claude-4.5-sonnet-20250514",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"}
        }
    ],
    messages=[{"role": "user", "content": "En annan fråga..."}]
)

# Kostnadsbesparing:
# Utan caching: $3.00/1M tokens × 2000 tokens = $0.006 per anrop
# Med caching: $0.006 första, $0.0006 nästa = 90% billigare!
```

**B) Structured Outputs - Garanterad JSON**

Alla major providers stödjer nu structured outputs (2024-2025).

```python
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

# 1. Definiera struktur med Pydantic
class CalendarEvent(BaseModel):
    title: str
    date: str
    time: str
    attendees: list[str]
    location: str

# 2. Få garanterad strukturerad output
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Extrahera kalenderhändelser från text"},
        {"role": "user", "content": "Möte med Lisa och John imorgon kl 14 på kontoret"}
    ],
    response_format=CalendarEvent
)

event = completion.choices[0].message.parsed
print(event.title)      # "Möte med Lisa och John"
print(event.attendees)  # ["Lisa", "John"]

# Ingen parsing errors - garanterat rätt format! ✅
```

**C) Model Routing - Använd rätt modell för rätt uppgift**

```python
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableBranch

# Definiera olika modeller
fast_cheap_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
smart_expensive_model = ChatOpenAI(model="gpt-4o", temperature=0)

# Klassificera uppgift
def classify_complexity(query: str) -> str:
    """Enkel klassificerare"""
    complex_keywords = ["analysera", "förklara varför", "jämför", "utvärdera"]
    if any(keyword in query.lower() for keyword in complex_keywords):
        return "complex"
    return "simple"

# Router
def route_query(query: str):
    if classify_complexity(query) == "complex":
        return smart_expensive_model
    return fast_cheap_model

# Användning
query1 = "Vad är 5 + 3?"  # → gpt-4o-mini ($0.15/1M)
query2 = "Analysera skillnaderna mellan ReAct och Reflexion"  # → gpt-4o ($2.50/1M)

# Besparing: 90% av queries är enkla → 85% kostnadsbesparing totalt!
```

### Exempel

#### Exempel 1: Din första ReAct Agent från scratch

```python
from openai import OpenAI
import json

client = OpenAI(api_key="your-key")

# 1. Definiera verktyg
tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Söker information på internet",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Sökfråga"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Utför matematiska beräkningar",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Matematiskt uttryck"}
                },
                "required": ["expression"]
            }
        }
    }
]

# 2. Implementera verktyg
def web_search(query: str) -> str:
    # I produktion: använd Google Search API, Tavily, etc.
    mock_results = {
        "befolkning stockholm": "Stockholm har cirka 978,000 invånare (2025)",
        "befolkning göteborg": "Göteborg har cirka 590,000 invånare (2025)"
    }
    return mock_results.get(query.lower(), "Ingen data hittad")

def calculator(expression: str) -> str:
    try:
        # Säkrare än eval: använd ast.literal_eval eller ett math library
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Agent loop
def run_agent(user_query: str, max_iterations: int = 5):
    messages = [
        {"role": "system", "content": "Du är en hjälpsam assistent. Använd verktyg för att svara."},
        {"role": "user", "content": user_query}
    ]

    for iteration in range(max_iterations):
        print(f"\n--- Iteration {iteration + 1} ---")

        # Anropa LLM
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        # Check om LLM vill använda verktyg
        if assistant_message.tool_calls:
            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                print(f"🔧 Calling: {function_name}({arguments})")

                # Kör verktyg
                if function_name == "web_search":
                    result = web_search(arguments["query"])
                elif function_name == "calculator":
                    result = calculator(arguments["expression"])
                else:
                    result = "Unknown tool"

                print(f"📊 Result: {result}")

                # Lägg till resultat i messages
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
        else:
            # Inget tool call - agenten är klar
            print(f"\n✅ Final Answer: {assistant_message.content}")
            return assistant_message.content

    return "Max iterations reached"

# 4. Testa agenten
result = run_agent(
    "Hur många fler invånare har Stockholm än Göteborg i procent?"
)
```

**Output:**
```
--- Iteration 1 ---
🔧 Calling: web_search({'query': 'befolkning stockholm'})
📊 Result: Stockholm har cirka 978,000 invånare (2025)

--- Iteration 2 ---
🔧 Calling: web_search({'query': 'befolkning göteborg'})
📊 Result: Göteborg har cirka 590,000 invånare (2025)

--- Iteration 3 ---
🔧 Calling: calculator({'expression': '((978000 - 590000) / 590000) * 100'})
📊 Result: 65.76271186440678

✅ Final Answer: Stockholm har cirka 65.8% fler invånare än Göteborg.
```

#### Exempel 2: Multi-Agent System med CrewAI

```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Konfigurera LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# 1. Market Research Agent
market_researcher = Agent(
    role='Market Research Analyst',
    goal='Analysera marknaden för LLM-agents verktyg',
    backstory="""Du är en erfaren marknadsanalytiker med expertis inom AI-verktyg.
    Du är bra på att identifiera trender och konkurrensfördel.""",
    llm=llm,
    verbose=True
)

# 2. Product Manager Agent
product_manager = Agent(
    role='Product Manager',
    goal='Definiera features för en ny LLM-agent produkt',
    backstory="""Du är en produktchef med 10 års erfarenhet.
    Du förstår användarbehov och kan prioritera features.""",
    llm=llm,
    verbose=True
)

# 3. Developer Agent
developer = Agent(
    role='Senior Python Developer',
    goal='Skapa teknisk implementation plan',
    backstory="""Du är en senior utvecklare med expertis i Python, LangChain och FastAPI.
    Du skriver ren, skalbar kod.""",
    llm=llm,
    verbose=True
)

# Definiera tasks
research_task = Task(
    description="""Analysera marknaden för LLM-agent verktyg.
    Identifiera top 5 konkurrenter och deras styrkor/svagheter.
    Rekommendera ett gap i marknaden vi kan fylla.""",
    agent=market_researcher,
    expected_output='Markdown rapport med konkurrentanalys och rekommendation'
)

product_task = Task(
    description="""Baserat på market research, definiera:
    1. Target användare (persona)
    2. Core features (top 5)
    3. Unique value proposition
    4. MVP scope""",
    agent=product_manager,
    expected_output='Product Requirements Document (PRD) i markdown'
)

development_task = Task(
    description="""Skapa teknisk implementation plan:
    1. Tech stack (frameworks, databaser, etc)
    2. System arkitektur (diagram)
    3. API design
    4. Development timeline (milestones)""",
    agent=developer,
    expected_output='Technical Design Document i markdown med kod-exempel'
)

# Skapa crew
startup_crew = Crew(
    agents=[market_researcher, product_manager, developer],
    tasks=[research_task, product_task, development_task],
    process=Process.sequential,  # Kör i ordning
    verbose=True
)

# Kör!
result = startup_crew.kickoff()

print("\n" + "="*50)
print("FINAL RESULT")
print("="*50)
print(result)
```

### Visualisering

#### Agent Framework Decision Tree

```
Vad ska du bygga?
       │
       ├─ Enkel chatbot med verktyg?
       │  └─→ LangChain (basic)
       │
       ├─ Komplex workflow med state?
       │  └─→ LangGraph
       │
       ├─ Flera agents som pratar med varandra?
       │  └─→ AutoGen
       │
       ├─ Team med tydliga roller?
       │  └─→ CrewAI
       │
       ├─ Web app med TypeScript?
       │  └─→ Vercel AI SDK
       │
       └─ Custom solution från scratch?
          └─→ OpenAI/Anthropic API direkt
```

#### Cost Optimization Strategy

```
┌─────────────────────────────────────────────────┐
│          COST OPTIMIZATION PYRAMID               │
└─────────────────────────────────────────────────┘

    ▲
   /1\ Använd smartaste modellen (GPT-4o, Claude 4.5)
  /   \ För: Complex reasoning, kritiska beslut
 /  5% \ Kostnad: Hög
/───────\
/       \
/    2   \ Använd mellanmodellen (GPT-4o-mini, Haiku)
/         \ För: Normal processing, de flesta queries
/   20%    \ Kostnad: Medel
/───────────\
/           \
/      3     \ Använd billigaste modellen (Gemini Flash)
/             \ För: Simple tasks, klassificering
/     75%      \ Kostnad: Mycket låg
/───────────────\

Strategi:
1. Klassificera query-komplexitet först (billig modell)
2. Route till rätt modell
3. Cache system prompts (90% besparing)
4. Batchning för icke-realtid uppgifter

Resultat: 80-90% total kostnadsbesparing! 🎉
```

### 💡 Pro Tips

**Tip 1: Börja med GPT-4o-mini för development**
Under utveckling, använd alltid `-mini` versioner. De är 90% billigare och oftast lika bra för testning.

```python
# Development
llm = ChatOpenAI(model="gpt-4o-mini")

# Production (efter testing)
llm = ChatOpenAI(model="gpt-4o")
```

**Tip 2: Sätt alltid temperature=0 för agents**
Agents behöver vara deterministiska för tool calling.

```python
# ❌ Dåligt - random outputs
llm = ChatOpenAI(temperature=0.7)

# ✅ Bra - consistent tool calls
llm = ChatOpenAI(temperature=0)
```

**Tip 3: Använd verbose=True under utveckling**
Se vad agenten tänker!

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True  # Visar hela reasoning chain
)
```

**Tip 4: Prompt Caching = Gratis pengar**
Om din system prompt är >1000 tokens, använd caching.

```python
# Spara 90% på upprepade anrop
system=[{
    "type": "text",
    "text": LONG_SYSTEM_PROMPT,
    "cache_control": {"type": "ephemeral"}  # ← Lägg till denna rad!
}]
```

### ✏️ Övningar

#### Övning 3.1: Bygg din första Tool-Calling Agent

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~20 minuter

**Uppgift:**
Skapa en agent som kan hjälpa användare att:
1. Konvertera valutor (SEK ↔ USD ↔ EUR)
2. Beräkna moms (25%)
3. Ge dagens växelkurs (hårdkodat: 1 USD = 10.50 SEK, 1 EUR = 11.20 SEK)

**Krav:**
- Använd OpenAI function calling
- Implementera minst 3 verktyg
- Agenten ska kunna kombinera verktyg (ex: "Vad kostar $100 inklusive moms i SEK?")

**Startkod:**

```python
from openai import OpenAI
import json

client = OpenAI(api_key="your-key")

# TODO: Implementera dessa funktioner
def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Konverterar mellan valutor"""
    # Din kod här
    pass

def calculate_vat(amount: float, include: bool = True) -> float:
    """Beräknar moms (25%)"""
    # Din kod här
    pass

# TODO: Definiera tools JSON för function calling
tools = [
    # Din tool definition här
]

# TODO: Implementera agent loop
def run_currency_agent(query: str):
    # Din agent implementation här
    pass

# Testa
run_currency_agent("Hur mycket är $100 med moms i svenska kronor?")
```

**Tips:**
- Växelkurser: USD=10.50 SEK, EUR=11.20 SEK
- Moms 25% means: `price * 1.25` (inkludera) eller `price / 1.25` (exkludera)
- Agenten behöver kanske göra flera tool calls i sekvens

<details>
<summary>💡 Lösning</summary>

```python
from openai import OpenAI
import json

client = OpenAI(api_key="your-key")

# Växelkurser (hårdkodade)
RATES = {
    "USD_TO_SEK": 10.50,
    "EUR_TO_SEK": 11.20,
    "SEK_TO_USD": 1/10.50,
    "SEK_TO_EUR": 1/11.20,
    "USD_TO_EUR": 10.50/11.20,
    "EUR_TO_USD": 11.20/10.50
}

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """Konverterar mellan valutor"""
    if from_currency == to_currency:
        return amount

    key = f"{from_currency}_TO_{to_currency}"
    if key in RATES:
        return round(amount * RATES[key], 2)
    else:
        return f"Valutapar {key} stöds inte"

def calculate_vat(amount: float, include: bool = True) -> float:
    """Beräknar moms (25%)"""
    VAT_RATE = 0.25
    if include:
        # Lägg till moms
        return round(amount * (1 + VAT_RATE), 2)
    else:
        # Ta bort moms
        return round(amount / (1 + VAT_RATE), 2)

def get_exchange_rate(from_currency: str, to_currency: str) -> str:
    """Hämtar aktuell växelkurs"""
    if from_currency == to_currency:
        return "1.00"

    key = f"{from_currency}_TO_{to_currency}"
    if key in RATES:
        return str(RATES[key])
    return "Växelkurs ej tillgänglig"

# Definiera tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "convert_currency",
            "description": "Konverterar ett belopp mellan olika valutor (SEK, USD, EUR)",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Beloppet som ska konverteras"
                    },
                    "from_currency": {
                        "type": "string",
                        "enum": ["SEK", "USD", "EUR"],
                        "description": "Från valuta"
                    },
                    "to_currency": {
                        "type": "string",
                        "enum": ["SEK", "USD", "EUR"],
                        "description": "Till valuta"
                    }
                },
                "required": ["amount", "from_currency", "to_currency"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_vat",
            "description": "Beräknar belopp inklusive eller exklusive moms (25%)",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "Grundbeloppet"
                    },
                    "include": {
                        "type": "boolean",
                        "description": "True för att lägga till moms, False för att ta bort moms"
                    }
                },
                "required": ["amount", "include"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Hämtar aktuell växelkurs mellan två valutor",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_currency": {
                        "type": "string",
                        "enum": ["SEK", "USD", "EUR"]
                    },
                    "to_currency": {
                        "type": "string",
                        "enum": ["SEK", "USD", "EUR"]
                    }
                },
                "required": ["from_currency", "to_currency"]
            }
        }
    }
]

def run_currency_agent(query: str, max_iterations: int = 10):
    """Kör valuta-agenten"""
    messages = [
        {
            "role": "system",
            "content": "Du är en valutaassistent. Hjälp användare med valutakonvertering och momsberäkningar."
        },
        {"role": "user", "content": query}
    ]

    for iteration in range(max_iterations):
        print(f"\n--- Iteration {iteration + 1} ---")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if assistant_message.tool_calls:
            for tool_call in assistant_message.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                print(f"🔧 {function_name}({arguments})")

                # Kör rätt funktion
                if function_name == "convert_currency":
                    result = convert_currency(**arguments)
                elif function_name == "calculate_vat":
                    result = calculate_vat(**arguments)
                elif function_name == "get_exchange_rate":
                    result = get_exchange_rate(**arguments)
                else:
                    result = "Unknown function"

                print(f"📊 {result}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })
        else:
            print(f"\n✅ {assistant_message.content}")
            return assistant_message.content

    return "Max iterations"

# Testa
print("="*60)
print("TEST 1: Enkel konvertering")
print("="*60)
run_currency_agent("Hur mycket är $100 i svenska kronor?")

print("\n" + "="*60)
print("TEST 2: Konvertering med moms")
print("="*60)
run_currency_agent("Vad kostar $100 inklusive moms i SEK?")

print("\n" + "="*60)
print("TEST 3: Komplex fråga")
print("="*60)
run_currency_agent("Jag har 5000 SEK. Hur mycket blir det i dollar, och vad är det med 25% moms?")
```

**Output exempel:**

```
============================================================
TEST 2: Konvertering med moms
============================================================

--- Iteration 1 ---
🔧 convert_currency({'amount': 100, 'from_currency': 'USD', 'to_currency': 'SEK'})
📊 1050.0

--- Iteration 2 ---
🔧 calculate_vat({'amount': 1050.0, 'include': True})
📊 1312.5

✅ $100 kostar 1312.50 SEK inklusive moms (25%).
```

**Varför fungerar detta?**
1. Agenten får frågan och förstår att den behöver två steg
2. Först konverterar den USD→SEK (tool call 1)
3. Sen lägger den till moms (tool call 2)
4. Agenten kombinerar resultaten i ett begripligt svar

Detta visar hur agents kan **kedja verktyg** för att lösa komplexa uppgifter!

</details>

---

#### Övning 3.2: Framework Comparison

**Svårighetsgrad**: ⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Implementera **samma** agent i två olika frameworks och jämför:

**Agent spec:** En agent som tar en text och:
1. Räknar antal ord
2. Räknar antal meningar
3. Beräknar genomsnittlig meningslängd

Implementera med:
- A) LangChain
- B) Direkt med OpenAI API

**Jämför:**
- Hur många rader kod?
- Hur lätt är det att förstå?
- Vilka fördelar/nackdelar?

<details>
<summary>💡 Lösning</summary>

**A) LangChain Implementation:**

```python
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate

@tool
def count_words(text: str) -> int:
    """Räknar antal ord i texten"""
    return len(text.split())

@tool
def count_sentences(text: str) -> int:
    """Räknar antal meningar"""
    # Enkel: räkna . ! ?
    return text.count('.') + text.count('!') + text.count('?')

@tool
def average_sentence_length(text: str) -> float:
    """Beräknar genomsnittlig meningslängd"""
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    return round(words / sentences if sentences > 0 else 0, 2)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Du analyserar text. Använd verktygen för att ge statistik."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

tools = [count_words, count_sentences, average_sentence_length]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Testa
text = "Detta är en text. Den har tre meningar. Ganska kort!"
result = agent_executor.invoke({"input": f"Analysera denna text: {text}"})
print(result)

# Rader kod: ~30 (exkl imports)
# Fördelar: Färdigt, många features, bra för komplex logic
# Nackdelar: Abstraktion kan göra debugging svårt
```

**B) Direkt OpenAI API:**

```python
from openai import OpenAI
import json

client = OpenAI()

def count_words(text: str) -> int:
    return len(text.split())

def count_sentences(text: str) -> int:
    return text.count('.') + text.count('!') + text.count('?')

def average_sentence_length(text: str) -> float:
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    return round(words / sentences if sentences > 0 else 0, 2)

tools = [{
    "type": "function",
    "function": {
        "name": "count_words",
        "description": "Räknar ord",
        "parameters": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "count_sentences",
        "description": "Räknar meningar",
        "parameters": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "average_sentence_length",
        "description": "Genomsnittlig meningslängd",
        "parameters": {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"]
        }
    }
}]

def analyze_text(text: str):
    messages = [
        {"role": "system", "content": "Du analyserar text statistik."},
        {"role": "user", "content": f"Analysera: {text}"}
    ]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=tools
        )

        msg = response.choices[0].message
        messages.append(msg)

        if not msg.tool_calls:
            return msg.content

        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)

            if tc.function.name == "count_words":
                result = count_words(args["text"])
            elif tc.function.name == "count_sentences":
                result = count_sentences(args["text"])
            elif tc.function.name == "average_sentence_length":
                result = average_sentence_length(args["text"])

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": str(result)
            })

text = "Detta är en text. Den har tre meningar. Ganska kort!"
result = analyze_text(text)
print(result)

# Rader kod: ~70 (exkl imports)
# Fördelar: Full kontroll, lätt att debugga, inga dependencies
# Nackdelar: Mer boilerplate, måste hantera allt själv
```

**Jämförelse:**

| Aspekt | LangChain | Direkt API |
|--------|-----------|------------|
| **Rader kod** | ~30 | ~70 |
| **Läsbarhet** | Hög (om du kan LangChain) | Medel |
| **Kontroll** | Låg (abstraktion) | Hög |
| **Debugging** | Svårare | Lättare |
| **Dependencies** | Många | Inga (bara openai) |
| **Production** | Bra för scaling | Bra för custom needs |

**Slutsats:**
- **Använd LangChain** om: Du bygger snabbt, vill ha batteries-included features
- **Använd Direct API** om: Du behöver full kontroll, minimala dependencies, eller lär dig grunderna

</details>

---

**[Fortsättning följer i Nivå 3b...]**

---


