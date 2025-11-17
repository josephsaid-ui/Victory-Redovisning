# Nivå 2: Introduktion till termer 🎓

[← Tillbaka: Nivå 1](./llm-agenter-niva1.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 3 →](./llm-agenter-niva3.md)

---

## Introduktion

Nu när du vet vad en agent är, ska vi lära oss de riktiga orden som experter använder. Det är som att lära sig fotbollstermer - istället för att bara säga "kicka bollen" kan du säga "passning", "skott" och "hörna".

**Vad ska du lära dig?** Viktiga ord och begrepp som LLM, Prompt, Tool, Memory och Chain. Efter denna nivå kan du prata om agenter som en proffs!

---

## Kärnkoncept

### 1. LLM - Agentens hjärna 🧠

**LLM** står för **Large Language Model** (Stor Språkmodell på svenska).

Tänk dig att en LLM är som:
- **En superstark hjärna** som har läst nästan allt på internet
- **En jättesmart kompis** som kan prata om nästan vad som helst
- **En snabb tänkare** som kan lösa problem på sekunder

**Exempel på LLM:er:**
- ChatGPT (från företaget OpenAI)
- Claude (från företaget Anthropic)
- Gemini (från Google)

**Så används det:**
```
Du: "Vad är huvudstaden i Sverige?"
LLM tänker: "Jag har läst om detta... det är Stockholm!"
LLM svarar: "Stockholm är Sveriges huvudstad."
```

### 2. Prompt - Hur du pratar med agenten 💬

En **prompt** är helt enkelt det du säger till agenten. Men precis som när du pratar med människor, kan du säga samma sak på olika sätt:

**Dålig prompt (otydlig):**
```
"Hjälp mig med grejer"
```
*Agenten vet inte vad du menar!*

**Bra prompt (tydlig):**
```
"Skapa en lista över 5 aktiviteter jag kan göra inomhus en regnig dag.
Jag gillar att måla, läsa och bygga saker."
```
*Agenten vet exakt vad du vill!*

**Pro tip:** Ju mer detaljer du ger, desto bättre svar får du!

### 3. Tools - Agentens verktygslåda 🔧

**Tools** (verktyg) är allt som en agent kan använda för att göra saker:

| Verktyg | Vad det gör | Exempel |
|---------|-------------|---------|
| **Sökning** | Letar upp info på internet | "Hitta recept på kladdkaka" |
| **Kalender** | Bokar tider | "Boka möte tisdag 14:00" |
| **Email** | Skickar/läser mail | "Skicka tack-mail till mormor" |
| **Kalkylator** | Räknar | "Vad är 17% av 289?" |
| **Väder-app** | Kollar väder | "Kommer det regna imorgon?" |
| **Databas** | Sparar/hämtar information | "Vad beställde vi förra gången?" |

**Tänk på det som:**
En snickare har hammare, såg och skruvmejsel. En agent har sökning, kalender och email!

### 4. Memory - Agentens minne 💭

Det finns två typer av minne:

**Korttidsminne (Short-term memory):**
```
Du: "Jag heter Lisa och jag är 10 år"
Agent: "Hej Lisa!"
Du: "Vad heter jag?"
Agent: "Du heter Lisa och är 10 år"
```
*Agenten kommer ihåg det vi just pratade om*

**Långtidsminne (Long-term memory):**
```
Förra veckan:
Du: "Min favoritfärg är lila"

Idag:
Agent: "Ska jag designa inbjudan i lila, din favoritfärg?"
```
*Agenten kommer ihåg från tidigare samtal!*

**Varför är detta viktigt?**
Med bra minne slipper du upprepa dig. Agenten lär känna dig!

### 5. Chain - Flera steg efter varandra 🔗

En **chain** (kedja) är när agenten gör flera saker i ordning:

**Exempel: "Planera min skoldag imorgon"**

```
Steg 1: Kolla schemat → Du har matte, engelska, idrott
    ↓
Steg 2: Kolla vädret → Soligt och varmt
    ↓
Steg 3: Kolla läxor → Matteläxa sida 45
    ↓
Steg 4: Skapa checklista:
    → Packa: matte-bok, matteläxa, idrottskläder
    → Påminnelse: Gör matteläxa ikväll
    → Tips: Ta med vattenflaska (varmt väder!)
```

Varje steg använder information från förra steget. Därför heter det en **kedja** - allt hänger ihop!

---

## Konkreta Exempel

### Exempel 1: Läxhjälp-agent med alla begrepp 📚

**Du skriver en prompt:**
```
"Jag behöver hjälp med min NO-läxa om vattnets kretslopp.
Förklara enkelt och ge sedan 3 quizfrågor för att testa mig."
```

**Agenten jobbar:**
1. **LLM (hjärnan)** förstår att du vill lära dig om vattnets kretslopp
2. **Tool (Sökning)** letar upp bra bilder om vattnets kretslopp
3. **Chain (steg-för-steg)**:
   - Först: Förklara vad vattnets kretslopp är
   - Sen: Visa bild
   - Sist: Skapa 3 quizfrågor
4. **Memory (minne)** kommer ihåg att du läser NO, så nästa gång kan den fråga "Hur gick NO-läxan?"

### Exempel 2: Födelsedags-agent 🎉

**Prompt:**
```
"Min kompis Felix fyller år 15:e mars.
Hjälp mig komma ihåg och planera."
```

**Agenten använder:**
- **Memory**: Sparar "Felix, 15 mars" i långtidsminne
- **Tool (Kalender)**: Skapar påminnelse 1 vecka innan
- **Tool (Sökning)**: "Presentidéer för 10-åringar"
- **Chain**:
  1. Spara datum
  2. Sätt påminnelse
  3. 1 vecka innan → föreslå present
  4. 1 dag innan → påminn att gratulera

### Exempel 3: Researchassistent för skolprojekt 🔬

**Prompt:**
```
"Jag ska göra en presentation om vikingar.
Hitta 5 intressanta fakta och berätta varifrån du fick info."
```

**Agenten använder:**
```
LLM: Förstår att du vill ha vikinga-fakta + källor
    ↓
Tool (Sökning): Letar på Wikipedia, museer, läroböcker
    ↓
Tool (Sammanfattning): Plockar ut viktigaste informationen
    ↓
Memory: Sparar att du jobbar med vikingar (kan hjälpa mer senare)
    ↓
Chain:
  1. Sök "vikingar fakta"
  2. Läs 10 artiklar
  3. Välj 5 coolaste fakta
  4. Spara länkar till källorna
  5. Presentera resultat med källor
```

---

## 💡 Pro Tips

### Tip 1: De flesta agenter är specialiserade
Precis som läkare kan vara hjärtläkare eller tandläkare, kan agenter vara:
- **Email-agent**: Jättebra på mail, men kan inte boka resor
- **Kalender-agent**: Perfekt för möten, men kan inte skriva texter
- **Forsknings-agent**: Hittar information, men kanske inte kan beställa pizza

**Ta reda på vad din agent är bra på!**

### Tip 2: Bättre prompts = bättre resultat

**Gå från detta:**
```
"Skriv något om djur"
```

**Till detta:**
```
"Skriv 5 meningar om lejon. Inkludera: var de bor, vad de äter,
och en rolig fakta. Gör det lätt att förstå för en 10-åring."
```

**Formel för bra prompts:**
1. Vad du vill ha (5 meningar)
2. Om vad (lejon)
3. Vilka detaljer (var, vad, roligt)
4. I vilken stil (lätt för 10-åring)

### Tip 3: Agenter kan göra misstag - dubbelkolla viktigt!
Även smarta agenter kan:
- Hitta fel information ibland
- Missförstå vad du menade
- Göra mattefel

**Alltid dubbelkolla** om det är något viktigt (som läxor eller fakta)!

---

## ✏️ Övningar

### Övning 2.1: Ordlista-matchning 📖

**Svårighetsgrad**: ⭐
**Tid**: ~5 minuter

**Uppgift:**
Matcha rätt ord med rätt förklaring:

**Ord:**
1. LLM
2. Prompt
3. Tool
4. Memory
5. Chain

**Förklaringar:**
A. Det du säger till agenten
B. Flera steg som agenten gör i ordning
C. Hjärnan som tänker
D. Verktyg som agenten använder (t.ex. sökning)
E. Agentens förmåga att komma ihåg saker

<details>
<summary>💡 Lösning</summary>

**Rätt svar:**
1. LLM → **C** (Hjärnan som tänker)
2. Prompt → **A** (Det du säger till agenten)
3. Tool → **D** (Verktyg som agenten använder)
4. Memory → **E** (Agentens förmåga att komma ihåg)
5. Chain → **B** (Flera steg i ordning)

**Minnestrick:**
- **L**LM = **L**arge brain (stor hjärna)
- **P**rompt = **P**rata (vad du säger)
- **T**ool = **T**ools (verktyg, båda börjar på T!)
- **M**emory = **M**inns (kommer ihåg)
- **C**hain = **C**onnected (sammankopplade steg)

</details>

---

### Övning 2.2: Förbättra prompten ✍️

**Svårighetsgrad**: ⭐⭐
**Tid**: ~10 minuter

**Uppgift:**
Dessa prompts är dåliga. Skriv om dem så de blir tydligare!

**Dålig prompt 1:**
```
"Hjälp mig"
```

**Dålig prompt 2:**
```
"Mat"
```

**Dålig prompt 3:**
```
"Gör något roligt"
```

**Tips för att förbättra:**
- Vad vill du ha? (en lista, en förklaring, ett förslag?)
- Om vad exakt?
- Hur många?
- I vilken stil?

<details>
<summary>💡 Lösning</summary>

**Här är bra omskrivningar:**

**Bättre prompt 1:**
```
"Hjälp mig hitta 3 böcker om rymd som är lämpliga för 10-åringar.
Förklara kort vad varje bok handlar om."
```
*Nu vet agenten: vad (böcker), ämne (rymd), hur många (3), för vem (10-åringar),
och vad mer (förklaring).*

**Bättre prompt 2:**
```
"Föreslå 5 enkla recept jag kan laga själv. Jag kan göra mackor,
varma smörgåsar och enkla sallader. Visa ingredienser och steg."
```
*Nu vet agenten: vad du kan laga, hur många recept, och vad du vill se.*

**Bättre prompt 3:**
```
"Föreslå en rolig inomhusaktivitet jag kan göra själv på 30 minuter.
Jag gillar att rita och bygga saker. Ge steg-för-steg instruktioner."
```
*Nu vet agenten: typ av aktivitet, tid, vad du gillar, och hur detaljerat du vill ha det.*

**Varför fungerar detta?**
Ju mer information du ger, desto lättare är det för agenten att hjälpa dig.
Det är som att be någon köpa godis åt dig:
- Otydligt: "Köp godis" → De kanske tar något du inte gillar
- Tydligt: "Köp 3 chokladkarameller och 2 sura skallar" → Du får exakt vad du vill!

</details>

---

### Övning 2.3: Rita en chain 🔗

**Svårighetsgrad**: ⭐⭐
**Tid**: ~10 minuter

**Uppgift:**
Din uppgift till en agent: **"Hjälp mig förbereda för mitt mattetest på fredag"**

Rita eller skriv en **chain** (steg för steg) som visar vad agenten skulle göra.

**Börja här:**
```
Steg 1: ...
Steg 2: ...
Steg 3: ...
```

**Tips:**
- Vad behöver agenten först kolla?
- Vilka verktyg (tools) kan den använda?
- Vad är slutmålet?

<details>
<summary>💡 Lösning</summary>

**Exempel på en bra chain:**

```
Steg 1: Kolla kalender
    → Upptäck: Mattetest fredag kl 10:00 (om 3 dagar)
    Tool: Kalender

Steg 2: Identifiera vad testet handlar om
    → Fråga användaren ELLER kolla tidigare meddelanden
    → Svar: "Multiplikation och division"
    Tool: Memory (minne)

Steg 3: Hitta övningsmaterial
    → Sök efter "multiplikation division övningar årskurs 4"
    → Hitta 3 bra webbsidor med övningar
    Tool: Sökning

Steg 4: Skapa studieplan
    → Måndag: Öva multiplikation 20 min
    → Tisdag: Öva division 20 min
    → Onsdag: Blandade övningar 30 min
    → Torsdag: Gör ett provtest 30 min
    Tool: Kalender + påminnelser

Steg 5: Sätt påminnelser
    → Påminnelse varje dag kl 17:00: "Dags att öva matte!"
    → Påminnelse torsdag: "Glöm inte att repetera inför testet imorgon!"
    Tool: Kalender

Steg 6: Sammanfatta och presentera
    → Visa hela planen för användaren
    → Fråga: "Vill du att jag hittar fler övningar?"
```

**Varför fungerar detta?**
Varje steg bygger på det förra:
- Du kan inte göra en studieplan (steg 4) innan du vet vad testet handlar om (steg 2)
- Du kan inte sätta påminnelser (steg 5) innan du har en plan (steg 4)

Det är som att baka:
1. Först: Hitta recept
2. Sen: Köp ingredienser
3. Sen: Baka
4. Sist: Dekorera

Du kan inte börja med steg 4!

</details>

**Bonus:**
Rita samma chain men för: **"Planera en camping-resa i sommar"**

---

### Övning 2.4: Vilka tools behövs? 🔧

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~10 minuter

**Uppgift:**
För varje uppgift nedan, lista vilka **tools** (verktyg) en agent skulle behöva:

**Uppgift A:** "Boka tandläkartid nästa vecka och lägg till i min kalender"

**Uppgift B:** "Hitta den billigaste flygbiljetten till Paris i juli"

**Uppgift C:** "Sammanfatta de 5 senaste emailen från min lärare"

**Möjliga tools att välja från:**
- Sökning (internet)
- Kalender
- Email
- Databas (sparar info)
- Jämförelse (kollar priser)
- Sammanfattning (läser långa texter och gör dem korta)
- Telefon/SMS

<details>
<summary>💡 Lösning</summary>

**Uppgift A: Boka tandläkartid**

Behöver:
1. **Sökning** → Hitta tandläkarens hemsida eller telefonnummer
2. **Kalender** → Kolla när du är ledig nästa vecka
3. **Telefon/Bokning** → Ringa eller boka online
4. **Kalender** → Lägga in den bokade tiden

**Kedja:**
```
Sökning → Kalender (kolla ledig tid) → Bokning → Kalender (spara tid)
```

---

**Uppgift B: Billigaste flygbiljetten**

Behöver:
1. **Sökning** → Hitta flygbolag som flyger till Paris
2. **Jämförelse** → Kolla priser på olika dagar i juli
3. **Kalender** → Se när du kan åka (kanske jobbar vissa dagar?)
4. **Databas** → Spara resultatet så du kan tänka på det

**Kedja:**
```
Kalender (när kan jag?) → Sökning (hitta flyg) → Jämförelse (billigaste?) → Databas (spara)
```

---

**Uppgift C: Sammanfatta email**

Behöver:
1. **Email** → Logga in och hitta de 5 senaste emailen från läraren
2. **Sammanfattning** → Läsa varje email och plocka ut det viktigaste
3. **Databas** → Kanske spara sammanfattningen

**Kedja:**
```
Email (hämta 5 st) → Sammanfattning (varje email) → Presentera resultat
```

---

**Varför fungerar detta?**
Olika uppgifter behöver olika verktyg, precis som:
- Måla ett rum: Pensel, målarfärg, tejp
- Baka kaka: Skål, mixer, ugn
- Spela fotboll: Boll, mål, kompisar

En agent behöver rätt verktyg för jobbet!

</details>

---

### Övning 2.5: Designa en agent med allt du lärt 🎨

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Designa en komplett agent! Använd alla begrepp du lärt dig.

**Din agent:**
```
Namn: [Hitta på ett coolt namn]

Vad den gör: [Beskriv huvuduppgiften]

LLM: [Vilken "hjärna"? ChatGPT, Claude, Gemini?]

Tools (minst 3):
- [Verktyg 1]
- [Verktyg 2]
- [Verktyg 3]

Memory:
- Korttidsminne: [Vad kommer den ihåg under ett samtal?]
- Långtidsminne: [Vad sparar den mellan olika dagar?]

Exempel på en Chain (minst 4 steg):
Steg 1: ...
Steg 2: ...
...

Exempel prompt från användaren:
"..."

Agentens svar:
"..."
```

**Tips:**
Tänk på något DU skulle vilja ha hjälp med!

<details>
<summary>💡 Lösningsexempel</summary>

**Exempel 1: KreativKompisen**

```
Namn: KreativKompisen

Vad den gör:
Hjälper mig med kreativa projekt (rita, skriva, bygga)
genom att ge idéer, instruktioner och inspiration.

LLM: ChatGPT (bra på kreativa idéer)

Tools:
- Sökning (hitta tutorials på YouTube)
- Bilddatabas (hitta inspirationsbilder)
- Ritverktyg (kan skissa enkla exempel)
- Timer (för att tajma projekt)

Memory:
- Korttidsminne: Vad jag jobbar på just nu (t.ex. "ritar en drake")
- Långtidsminne: Vad jag brukar gilla (t.ex. "gillar drakar, slott, fantasy")

Exempel chain:
Steg 1: Användaren säger "Jag vill rita något coolt"
Steg 2: Kolla långtidsminne → "Du gillar drakar och fantasy"
Steg 3: Sök inspiration → Hitta 3 bilder på fantasy-drakar
Steg 4: Ge steg-för-steg guide: "Börja med en cirkel för huvudet..."
Steg 5: Sätt timer på 30 min → "Påminnelse: Bra jobbat, ta en paus!"

Exempel prompt:
"Jag är uttråkad och vill göra något kreativt. Jag har papper och
pennor hemma. Vad kan jag göra?"

Agentens svar:
"Härligt! Baserat på att du gillar drakar och fantasy, här är 3 idéer:
1. Rita en drake som vaktar en skattkista (jag kan visa steg-för-steg!)
2. Designa ditt eget fantasyvapen och skriv dess magiska förmågor
3. Skapa en karta över en påhittad fantasy-värld

Vilken vill du prova? Jag har tutorials redo!"
```

---

**Exempel 2: StudieStjärnan**

```
Namn: StudieStjärnan

Vad den gör:
Hjälper elever planera läxor, förbereda inför prov,
och förstå svåra ämnen.

LLM: Claude (bra på att förklara svåra saker enkelt)

Tools:
- Kalender (se schema och deadlines)
- Sökning (hitta förklaringar och videor)
- Sammanfattning (göra långa texter kortare)
- Quiz-skapare (testa kunskap)
- Påminnelser

Memory:
- Korttidsminne: Vad vi studerar just nu (t.ex. "fotosyntesen")
- Långtidsminne:
  * Vilka ämnen jag har svårt för (t.ex. "matte")
  * Hur jag lär mig bäst (t.ex. "med bilder och quiz")
  * Kommande prov

Exempel chain:
Steg 1: Måndag morgon → Kolla kalendern
Steg 2: Upptäck: "SO-prov om vikingar på fredag"
Steg 3: Kolla långtidsminne → "Användaren gillar att lära med quiz"
Steg 4: Skapa studieplan:
  - Måndag: Läs kapitel om vikingar (20 min)
  - Tisdag: Titta på video om vikingaskepp
  - Onsdag: Gör 10 quiz-frågor
  - Torsdag: Repetera svåra delar
Steg 5: Sätt påminnelser varje dag kl 17:00
Steg 6: Skicka uppmuntran: "Bra jobbat! Du är redo för provet!"

Exempel prompt:
"Jag har SO-prov om vikingar på fredag men jag vet ingenting. Hjälp!"

Agentens svar:
"Lugn! Vi har 4 dagar, det räcker. Här är din plan:

📅 MÅNDAG (idag):
- Läs sida 34-45 i SO-boken (20 min)
- Jag sätter påminnelse kl 17:00

📅 TISDAG:
- Titta på denna video om vikingaskepp (15 min): [länk]
- Gör 5 quiz-frågor jag skapat

📅 ONSDAG:
- Repetera: Vad handlade boken om? (10 min)
- 10 nya quiz-frågor

📅 TORSDAG:
- Gör ett prövtest (20 min)
- Gå igenom fel svar tillsammans

Du fixar detta! Vill du att jag skapar quiz-frågorna nu?"
```

---

**Varför fungerar dessa exempel?**
Båda agenterna har:
- **Tydligt syfte** (kreativitet vs. studier)
- **Rätt verktyg** för jobbet
- **Smart minne** (lär känna användaren)
- **Bra chains** (logiska steg)
- **Hjälpsamma svar** (konkreta förslag)

**Din tur nu!** Vad skulle DIN drömAgent göra?

</details>

---

## 📝 Sammanfattning

### Du har nu lärt dig:

✅ **LLM** = Agentens hjärna som tänker (t.ex. ChatGPT, Claude, Gemini)
✅ **Prompt** = Det du säger till agenten (ju tydligare, desto bättre!)
✅ **Tools** = Verktyg agenten använder (sökning, kalender, email, etc.)
✅ **Memory** = Kort- och långtidsminne (kommer ihåg konversationer)
✅ **Chain** = Flera steg i ordning (varje steg bygger på förra)

### Nya viktiga ord:

| Ord | Betydelse | Exempel |
|-----|-----------|---------|
| **LLM** | Large Language Model - AI-hjärnan | ChatGPT, Claude |
| **Prompt** | Det du säger till agenten | "Hjälp mig hitta recept" |
| **Tool** | Verktyg agenten använder | Sökning, Kalender |
| **Memory** | Minne (kort eller lång) | Kommer ihåg ditt namn |
| **Chain** | Kedja av steg | Steg 1→2→3→4 |
| **Short-term memory** | Korttidsminne | Detta samtalet |
| **Long-term memory** | Långtidsminne | Mellan olika dagar |

### Nästa steg:

I **Nivå 3** kommer du:
- Lära dig om agent-arkitektur (hur delarna passar ihop)
- Se riktiga kodexempel
- Bygga din första agent själv!
- Förstå olika typer av agenter (ReAct, Plan-and-Execute, etc.)

**Är du redo att ta nästa steg?** 🚀

---

## 🎮 Självtest

Innan du går vidare, testa dig själv:

**Kan du:**
- [ ] Förklara vad en LLM är för någon som aldrig hört talas om det?
- [ ] Ge exempel på vad en "tool" kan vara?
- [ ] Skriva en bra prompt (tydlig och detaljerad)?
- [ ] Förklara skillnaden mellan kort- och långtidsminne?
- [ ] Rita en enkel chain (steg-för-steg)?

**Fick du alla bockar?** Grattis, du är redo för Nivå 3! 🎉

**Fick du inte alla?** Inga problem! Gå tillbaka och läs om de delarna du är osäker på. Ta din tid!

---

[← Tillbaka: Nivå 1](./llm-agenter-niva1.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 3 - Tekniska detaljer 🔧 →](./llm-agenter-niva3.md)
