# Frida – Den Kompletta Guiden till Dynamic Instrumentation

## 📚 Innehållsförteckning

- [🎯 Om Denna Guide](#-om-denna-guide)
- [Nivå 1: "Det Magiska Förstoringsglaset" 👶](#nivå-1-det-magiska-förstoringsglaset-)
- [Nivå 2: "Grundverktygen" 🧒](#nivå-2-grundverktygen-)
- [Nivå 3: "Under Motorhuven" 🎓](#nivå-3-under-motorhuven-)
- [Nivå 4: "Avancerad Mästerskap" 🏛️](#nivå-4-avancerad-mästerskap-️)
- [Nivå 5: "Expertnivå" 💼](#nivå-5-expertnivå-)
- [🎓 Slutlig Självutvärdering](#-slutlig-självutvärdering)
- [📖 Ordlista](#-ordlista)
- [🔗 Resurser för Fördjupning](#-resurser-för-fördjupning)
- [❓ Vanliga Frågor (FAQ)](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande svenska guiden om **Frida** – ett kraftfullt verktyg för dynamic instrumentation som används av säkerhetsforskare, reverse engineers och apputvecklare världen över.

### Vad är Frida?

Frida är ett "dynamic instrumentation toolkit" – ett verktyg som låter dig titta in i program medan de körs och till och med ändra hur de beter sig, utan att ha tillgång till källkoden. Det fungerar på Windows, macOS, Linux, Android, iOS och fler plattformar.

### Varför denna guide?

De flesta Frida-guider börjar för tekniskt eller hoppar över grunderna. Denna guide tar dig från **absolut nybörjare** till **expert** genom fem progressiva nivåer:

- **Nivå 1 (👶)**: Så enkel att även en 5-åring förstår konceptet
- **Nivå 2 (🧒)**: Grundtermer och verktyg
- **Nivå 3 (🎓)**: Teknisk förståelse och praktisk användning
- **Nivå 4 (🏛️)**: Avancerade koncept och säkerhetsaspekter
- **Nivå 5 (💼)**: Expertnivå för professionell användning

**Total lästid**: 1,5–3 timmar
**Läsningstid per nivå**: 10–20 minuter

### Etik och laglig användning

⚠️ **VIKTIGT**: Denna guide fokuserar på **laglig och etisk** användning av Frida:

- ✅ Analys av dina egna applikationer
- ✅ Säkerhetstestning med tillstånd
- ✅ CTF-tävlingar och labbmiljöer
- ✅ Utbildning och forskning
- ❌ Aldrig mot andras system utan tillstånd
- ❌ Aldrig för att kringgå DRM eller licenser
- ❌ Aldrig för skadlig verksamhet

### Progression

Varje nivå bygger på den föregående. Du kan hoppa direkt till en nivå som matchar din erfarenhet, men vi rekommenderar att åtminstone skumma tidigare nivåer för att säkerställa att du har grunderna.

**Redo? Låt oss börja!**

---

## Nivå 1: "Det Magiska Förstoringsglaset" 👶

### Introduktion

På denna nivå ska du förstå vad Frida är med enkla ord – ingen kod, inga svåra termer. Du kommer att lära dig grundkonceptet bakom "dynamic instrumentation" genom analogier som alla kan förstå. Detta är viktigt eftersom det hjälper dig att bygga rätt mental modell innan vi dyker in i tekniken.

### Kärnkoncept

#### 1. Program är som leksaksrobotar

Tänk dig att du har en leksaksrobot. När du trycker på knappen går den framåt, spelar musik och blinkar. Men du kan inte se *inuti* roboten medan den gör detta – du ser bara vad den gör utifrån.

Ett program på din dator eller telefon är som denna robot. Det gör saker (spelar spel, skickar meddelanden, räknar), men normalt kan du inte se *hur* det gör det inuti.

#### 2. Frida är ett magiskt förstoringsglas + fjärrkontroll

Nu föreställ dig att du har två magiska verktyg:

**🔍 Ett magiskt förstoringsglas** – När du håller det mot roboten kan du se INUTI den medan den går! Du ser hur kugghjulen snurrar, vilka knappar som trycks ner, hur musiken spelas. Du kan **observera** allt som händer.

**📡 En magisk fjärrkontroll** – Med denna kan du ÄNDRA vad roboten gör, även MEDAN den går! Du kan säga "När roboten ska gå höger, gå vänster istället!" eller "När den ska spela musik, säg 'hej' istället!". Du kan **förändra** beteendet.

**Detta är exakt vad Frida gör med program!**

#### 3. Skillnaden mellan "innan" och "medan"

När du bygger ett LEGO-hus kan du planera hur det ska se ut **innan** du börjar. Det kallas för "design" eller "planering".

Men tänk om du kunde ändra LEGO-huset **medan någon annan bygger det**, utan att de stannar? Du ser ett fönster placeras och säger "Nej, sätt en dörr där istället!" – MEDAN byggandet pågår.

**Vanlig programmering/debugging**: Du pausar programmet, tittar på det, ändrar det, startar om det.

**Frida (dynamic instrumentation)**: Programmet fortsätter köra, och du tittar på det och ändrar det MEDAN det körs, utan att starta om!

#### 4. Två superförmågor

När du använder Frida får du två superförmågor:

**Superförmåga 1: Röntgenblick (Observera)** 🕵️
- Se vilka funktioner som körs i programmet
- Se vad programmet skickar till internet
- Se vilka knappar användaren trycker på
- Läsa meddelanden innan de krypteras

**Superförmåga 2: Tidsbändning (Förändra)** ⚡
- Ändra vad en funktion returnerar (t.ex. "Du har 100 poäng" → "Du har 1000 poäng")
- Hoppa över säkerhetskontroller (i labbmiljö!)
- Ändra vad som skickas till servern
- Få program att göra saker de inte var tänkta att göra

#### 5. Varför är detta användbart?

Tänk på dessa exempel:

**Exempel A: Läraren som vill förstå hur barn tänker**
- En mattelärare ger ett barn ett problem: "5 + 3 = ?"
- Barnet svarar "8" ✓
- Men läraren vill veta: *Hur tänkte barnet?* Räknade det på fingrarna? Visste det svaret utantill?
- Med Frida kan du se "tankestegen" – inte bara slutresultatet!

**Exempel B: Läkaren som kollar hur medicin fungerar**
- En läkare ger medicin till en patient
- Läkaren vill veta: Hur påverkar medicinen kroppen? Vilka celler ändras?
- Med Frida kan du "titta in i kroppen" (programmet) medan medicinen (indata) verkar

**Exempel C: Detektiven som löser mysterier**
- Ett program beter sig konstigt – det kraschar ibland
- Varför? Detektiven (du) använder Frida för att se exakt vad programmet gör innan det kraschar
- Aha! Det försöker läsa en fil som inte finns!

### Exempel

#### Exempel 1: Spelet som räknar poäng

**Utan Frida:**
- Du spelar ett spel
- Du får 10 poäng
- Spelet visar "Du har 10 poäng!"
- Du vet inte *hur* spelet räknade poängen

**Med Frida (Observera):**
- Du ser: Spelet anropar funktionen `calculatePoints()`
- Du ser: Funktionen får värdet `10` och returnerar `10`
- Nu vet du EXAKT var poängen beräknas!

**Med Frida (Förändra):**
- Du säger till Frida: "När `calculatePoints()` returnerar 10, ändra det till 100!"
- Nu visar spelet "Du har 100 poäng!" istället
- (Detta är bara för lärande – inte för att fuska i riktiga spel!)

#### Exempel 2: Filmen vs. Filmen du kan pausa

**Vanligt program (som en film på bio):**
- Du tittar på filmen från början till slut
- Om du vill se något igen måste du vänta till nästa visning
- Du kan inte pausa, spola eller ändra

**Program med Frida (som Netflix):**
- Du kan pausa när som helst och titta närmare på en scen
- Du kan spola tillbaka och se en del igen
- Du kan till och med tänka dig att du kan ändra dialogen: "Han skulle säga något annat där!"

#### Exempel 3: Kakan i ugnen

**Traditionellt sätt:**
- Du bakar en kaka (skriver ett program)
- Du stoppar in den i ugnen (startar programmet)
- Du väntar 30 minuter
- Du öppnar ugnen (programmet är klart)
- Om kakan blev dålig måste du börja om från början

**Med Frida:**
- Du bakar en kaka
- Du stoppar in den i ugnen
- Du har en magisk ugn där du kan se inuti MEDAN den bakar!
- Du ser: "Åh nej, kakan blir för mörk på ena sidan!"
- Du kan justera temperaturen MEDAN den bakar!
- Kakan blir perfekt utan att börja om!

### 💡 Pro Tips

**Tip 1: Frida ändrar inte originalfilen**
När du använder Frida ändrar du programmet ENDAST medan det körs i datorns minne. Själva filen på hårddisken förblir oförändrad. Det är som att rita på ett fönster med tuschpenna – när du stänger fönstret försvinner ritningarna!

**Tip 2: Frida fungerar på nästan allt**
Frida fungerar på program på din dator (Windows, Mac, Linux) OCH på appar på telefoner (Android, iPhone). Det är som ett universalverktyg!

**Tip 3: Det är lagligt att använda Frida på dina egna program**
Precis som det är OK att ta isär din egen leksak för att se hur den fungerar, är det OK att använda Frida på dina egna program eller i labbmiljöer där du har tillstånd.

### ✏️ Övningar

#### Övning 1: Rita din förståelse
Rita (på papper eller tänk dig) tre saker:
1. En app/robot (målet)
2. Ett förstoringsglas (Fridas observerande förmåga)
3. En fjärrkontroll (Fridas förändrande förmåga)

Markera med pilar hur dessa tre saker hänger ihop. Var är du i bilden? (Du håller i verktygen!)

<details>
<summary>📝 Facit</summary>

Din bild borde visa:
- **Du** (användaren/analytikern) i mitten
- **Appen/programmet/roboten** på sidan
- **Förstoringsglaset** mellan dig och appen (detta visar att du kan observera)
- **Fjärrkontrollen** som pekar mot appen (detta visar att du kan styra/ändra)
- Pilar från dina händer till båda verktygen
- Pilar från verktygen till appen

Budskapet: DU styr verktygen som påverkar appen!
</details>

#### Övning 2: Film vs. Streamtjänst
Förklara med egna ord (eller tänk igenom): Vad är skillnaden mellan att:
- Bara **titta** på en film (du kan inte pausa/spola)
- **Streama** en film (du kan pausa/spola/repetera)

Hur liknar detta skillnaden mellan ett vanligt program och ett program du kör med Frida?

<details>
<summary>📝 Facit</summary>

**Vanlig film (vanligt program):**
- Går från början till slut utan kontroll
- Du kan inte pausa för att inspektera något
- Om du missar något måste du se hela filmen igen
- Du kan inte ändra innehållet

**Streamad film (program med Frida):**
- Du kan pausa när som helst för att se detaljer
- Du kan spola tillbaka och se samma del igen
- Du har full kontroll över uppspelningen
- (Med Frida kan du till och med "ändra" dialogen!)

**Kopplingen:**
Frida ger dig "fjärrkontroll" över program på samma sätt som en streaming-tjänst ger dig fjärrkontroll över filmer!
</details>

#### Övning 3: Matcha begreppen
Matcha dessa tre kolumner:

| Verkligt scenario | Frida-ekvivalent | Vad du gör |
|------------------|------------------|------------|
| A. Spel-app | 1. Frida | i. Personen som spelar |
| B. Magiskt verktyg | 2. Robot/Program | ii. Leksaken som granskas |
| C. Du själv | 3. Användare/Analytiker | iii. Verktyget som observerar |

<details>
<summary>📝 Facit</summary>

**Rätt matchning:**
- **A-2-ii**: Spel-app = Robot/Program = Leksaken som granskas
- **B-1-iii**: Magiskt verktyg = Frida = Verktyget som observerar
- **C-3-i**: Du själv = Användare/Analytiker = Personen som spelar/analyserar

**Förklaring:**
Appen/spelet/roboten är det du vill undersöka. Frida är verktyget du använder. Du är personen som driver hela processen!
</details>

### 📝 Sammanfattning

**Key Takeaways från Nivå 1:**

- ✅ **Frida är som ett magiskt förstoringsglas + fjärrkontroll** för program
- ✅ **Observera**: Du kan se inuti program medan de körs (som röntgenblick)
- ✅ **Förändra**: Du kan ändra hur program beter sig medan de körs (som tidsbändning)
- ✅ **"Medan det körs" är nyckeln**: Till skillnad från vanlig debugging pausar du inte programmet
- ✅ **Frida är ett verktyg** – du är detektiven/analytikern som använder det
- ✅ **Frida ändrar inte originalfilen** – bara minnet medan programmet körs
- ✅ **Använd endast på dina egna program eller med tillstånd** – etik är viktigt!

### Mini-ordlista

| Term | Enkel förklaring |
|------|------------------|
| **Frida** | Ett verktyg för att titta in i och ändra program medan de körs |
| **Dynamic instrumentation** | Att undersöka och ändra program medan de körs (inte när de är avstängda) |
| **Observera** | Att titta på vad programmet gör (som med förstoringsglas) |
| **Förändra** | Att ändra vad programmet gör (som med fjärrkontroll) |
| **Program/App** | Mjukvaran du undersöker (målet) |
| **Runtime** | "Medan det körs" – när programmet är igång |

### Koppling till nästa nivå

Nu förstår du **VAD** Frida gör med enkla ord. I nästa nivå (Nivå 2: "10-åringen") börjar vi introducera **riktiga termer** som används av Frida-användare: "hook", "attach", "inject", "API". Vi kommer också se hur Frida-verktygen ser ut och vad de heter. Men oroa dig inte – vi håller det fortfarande enkelt och konkret!

**Redo för nästa steg? Låt oss gå vidare! 🚀**

---

## Nivå 2: "Grundverktygen" 🧒

### Introduktion

Nu när du förstår konceptet bakom Frida är det dags att lära dig de **riktiga termerna** som Frida-användare använder. Du kommer att möta ord som "hook", "attach", "process" och "API". Vi introducerar också de verktyg som kommer med Frida och hur de används. Detta är viktigt för att du ska kunna följa tutorials, läsa dokumentation och prata med andra Frida-användare.

### Kärnkoncept

#### 1. Process – Programmet som körs i minnet

När du startar ett program (t.ex. Chrome, Spotify, ett spel) skapas en **process** i datorns minne. En process är som en arbetsyta där programmet lever och andas.

**Analogier:**
- **Recept vs. Matlagning**: Programfilen på hårddisken är receptet. Processen är när du faktiskt lagar maten i köket.
- **Plan vs. Byggarbetsplats**: Programfilen är ritningen. Processen är den aktiva byggarbetsplatsen där arbete pågår.

Varje process har:
- Ett **Process ID (PID)**: Ett unikt nummer, som personnummer för processen
- Ett **namn**: Namnet på programmet (t.ex. "chrome.exe", "com.spotify.music")
- **Minne**: Där all data och kod finns medan programmet körs

#### 2. Hook – Att "lyssna in" på en funktion

En **hook** (sv: krok) är som att sätta en "avlyssnare" på en specifik funktion i programmet. När funktionen körs kommer din hook att utföras först (eller efter, eller både och).

**Analogier:**
- **Telefonavlyssning**: Du sätter en lyssningsapparat på telefonlinjen. Varje gång någon ringer kan du höra samtalet (och till och med ändra vad som sägs!).
- **Farthinder**: Du sätter ett farthinder på en väg. Varje gång en bil kommer dit måste den sakta ner – du kan då titta på bilen, räkna bilar, eller till och med dirigera om trafiken.

**Vad kan en hook göra?**
- **Logga/observera**: "Funktionen `sendMessage()` anropades med argumentet 'Hej!'"
- **Ändra input**: Ändra vad som skickas in till funktionen
- **Ändra output**: Ändra vad funktionen returnerar
- **Hoppa över**: Förhindra att funktionen körs alls

#### 3. Attach vs. Spawn – Hur du kopplar till en process

Det finns två sätt att använda Frida på ett program:

**Attach (bifoga)**: Du ansluter till en process som **redan körs**.
- Analogier: Som att hoppa på ett tåg som redan är igång.
- Användning: `frida -n "Spotify"` eller `frida -p 1234`

**Spawn (starta)**: Du **startar** programmet med Frida redan kopplat från början.
- Analogier: Som att sitta i tåget innan det ens börjar rulla.
- Användning: `frida -f com.example.app`
- Fördel: Du kan hooka saker som händer redan när appen startar!

#### 4. Inject – Att skjuta in din kod

**Inject** (sv: injicera/skjuta in) betyder att du stoppar in din egen kod (vanligtvis JavaScript) i målprocessen.

**Analogi:**
- **Agent på fältet**: Tänk dig att programmet är ett land. Att injicera kod är som att skicka en hemlig agent in i landet. Agenten kan observera, rapportera och utföra uppdrag inifrån.

När du injicerar kod med Frida:
1. Frida skapar en liten "bubbla" inuti målprocessen
2. I denna bubbla körs din JavaScript-kod
3. Din kod kan se och ändra allt i processen

#### 5. API – Gränssnittet programmet använder

**API** (Application Programming Interface) är som en meny på en restaurang. Det är en lista över funktioner som ett program erbjuder till andra program eller till systemet.

**Exempel:**
- Ett spel använder ett **grafik-API** för att rita på skärmen (t.ex. DirectX, OpenGL)
- En app använder ett **nätverk-API** för att skicka data (t.ex. `send()`, `recv()`)
- En Android-app använder **Java-API:er** för att visa knappar, läsa filer, osv.

Med Frida kan du **hooka API-anrop** för att se exakt vad programmet gör.

#### 6. Funktion – Byggstenen i program

En **funktion** är en liten del av programmet som gör en specifik sak.

**Exempel:**
- `calculateSum(5, 3)` – beräknar summan av två tal
- `sendMessage(text)` – skickar ett meddelande
- `checkPassword(input)` – kontrollerar om lösenordet är rätt

**Med Frida kan du:**
- Se när funktioner anropas: "Aha, `checkPassword()` anropades precis!"
- Se argument: "Den fick argumentet 'password123'"
- Se returvärde: "Den returnerade `true` (lösenordet var rätt!)"
- Ändra returvärde: "Låt oss ändra det till `true` även om lösenordet var fel!"

#### 7. JavaScript – Språket du skriver Frida-scripts i

Frida använder **JavaScript** för sina scripts. JavaScript är ett populärt programmeringsspråk som är relativt lätt att lära sig.

**Viktigt:**
- Du behöver inte vara expert på JavaScript för att använda Frida!
- Grunderna räcker långt: variabler, funktioner, if-satser
- Det finns massor av exempel att kopiera och anpassa

### Frida-verktygen (CLI)

Frida kommer med flera kommandoradsprogram (CLI = Command Line Interface):

#### **1. frida** – Huvudverktyget

Detta är det interaktiva verktyget där du kan köra JavaScript-kod direkt mot en process.

**Exempel:**
```bash
# Anslut till Spotify (om det körs)
frida -n Spotify

# Anslut till process med PID 1234
frida -p 1234

# Starta en Android-app med Frida
frida -U -f com.example.app
```

**Flaggor:**
- `-n NAMN`: Attach till process med namnet NAMN
- `-p PID`: Attach till process med PID
- `-f PAKET`: Spawn (starta) en app
- `-U`: Använd USB-ansluten enhet (telefon)
- `-l SCRIPT`: Ladda ett JavaScript-script från fil

#### **2. frida-ps** – Lista processer

Visar alla processer som körs (som Task Manager/Aktivitetsvisaren).

**Exempel:**
```bash
# Lista alla processer på datorn
frida-ps

# Lista alla appar på Android-telefon
frida-ps -Uai
```

**Flaggor:**
- `-U`: USB-enhet
- `-a`: Visa applikationer
- `-i`: Visa identifierare

#### **3. frida-trace** – Spåra funktionsanrop automatiskt

Detta är ett kraftfullt verktyg som automatiskt hookar funktioner och loggar dem!

**Exempel:**
```bash
# Spåra alla funktioner som börjar med "recv" eller "read" i Twitter
frida-trace -i "recv*" -i "read*" twitter

# Spåra funktionen "open" i Chrome på Android
frida-trace -U -i open -N com.android.chrome

# Spåra alla Java-klasser/metoder som innehåller "json"
frida-trace -U -p 12345 -j '*json*!*'
```

**Flaggor:**
- `-i MÖNSTER`: Include (inkludera) funktioner som matchar mönster
- `-x MÖNSTER`: Exclude (exkludera) funktioner
- `-j JAVA_MÖNSTER`: Hooka Java-metoder (Android)
- Asterisk `*` fungerar som wildcard (matchar allt)

#### **4. frida-ls-devices** – Lista enheter

Visar alla enheter/targets som Frida kan ansluta till (din dator, USB-telefon, emulatorer).

**Exempel:**
```bash
frida-ls-devices
```

Output:
```
Id                  Type        Name
──────────────────  ──────────  ─────────
local               local       Local System
abc123              usb         Samsung Galaxy S21
tcp@192.168.1.50    remote      Remote Device
```

### Exempel

#### Exempel 1: Hitta och attach till en process

**Scenario:** Du vill använda Frida på Spotify.

**Steg 1: Se om Spotify körs**
```bash
frida-ps | grep -i spotify
```

Output:
```
12345  Spotify
```

Nu vet du att Spotify körs med PID 12345.

**Steg 2: Anslut med Frida**
```bash
frida -p 12345
```

eller enklare:
```bash
frida -n Spotify
```

Nu är du inne i Frida och kan köra JavaScript-kommandon!

#### Exempel 2: Logga när en funktion anropas (teoretiskt)

Du misstänker att Spotify anropar funktionen `openURL()` när du klickar på länkar.

**Med frida-trace:**
```bash
frida-trace -n Spotify -i "openURL"
```

Nu kommer du se varje gång `openURL()` anropas, med vilka argument!

Output (exempel):
```
  2534 ms  openURL("https://spotify.com/track/abc123")
  5821 ms  openURL("https://open.spotify.com/artist/xyz")
```

**Tolkning:**
- Vid tidpunkt 2534 ms anropades `openURL` med länken till en låt
- Vid tidpunkt 5821 ms anropades den med länken till en artist

#### Exempel 3: Hooka en Android-app

**Scenario:** Du vill se vilka Java-metoder som anropas i en Android-app.

**Steg 1: Anslut telefonen via USB**

**Steg 2: Lista appar**
```bash
frida-ps -Uai
```

Output:
```
  PID  Name             Identifier
-----  ---------------  ------------------------
 1234  Instagram        com.instagram.android
 5678  Chrome           com.android.chrome
```

**Steg 3: Starta appen med Frida**
```bash
frida -U -f com.instagram.android
```

Nu är Frida kopplat till Instagram och du kan börja hooka funktioner!

#### Exempel 4: Skillnaden mellan Attach och Spawn

**Attach-scenario:**
- Appen Instagram körs redan
- Du vill se vad som händer när du klickar på en knapp
- Du attachar: `frida -U -n Instagram`
- Problem: Du missar allt som händer vid appstart (t.ex. licenskontroll)

**Spawn-scenario:**
- Du vill se exakt vad som händer när Instagram startar
- Du spawnar: `frida -U -f com.instagram.android`
- Nu kan du hooka funktioner som körs vid appstart!
- Frida pausar appen automatiskt – du måste köra `resume` för att låta den fortsätta

#### Exempel 5: Lyssna på telefonsamtal (metafor för hooking)

**Utan hook (vanligt telefonsamtal):**
- Person A ringer Person B
- De pratar
- De lägger på
- Du vet inte vad de sa

**Med hook (avlyssnat telefonsamtal):**
- Person A ringer Person B
- **Din hook aktiveras:** "Samtal påbörjat! A sa: 'Hej, hur är läget?'"
- Person B svarar: "Bra, tack!"
- **Din hook loggar:** "B svarade: 'Bra, tack!'"
- **Du kan till och med ändra:** Ändra "Bra, tack!" till "Dåligt!" innan A hör det
- Samtalet fortsätter (eventuellt med dina ändringar)

**I programkontext:**
- Funktion A anropar Funktion B
- Din hook ser anropet och kan logga/ändra det
- Programmet fortsätter köra

### 💡 Pro Tips

**Tip 1: Använd frida-ps för att hitta processer snabbt**
Istället för att gissa process-ID eller exakt namn, använd `frida-ps` för att se allt som körs. Filtrera med `grep`:
```bash
frida-ps | grep -i <sökord>
```

**Tip 2: frida-trace är perfekt för att börja**
Om du inte vet vilka funktioner du ska hooka, använd `frida-trace` med wildcards:
```bash
frida-trace -n Program -i "send*" -i "recv*"
```
Detta hookar alla funktioner som börjar med "send" eller "recv" och ger dig en översikt!

**Tip 3: Spawn är säkrare än Attach för appar med skydd**
Många appar kontrollerar om de blir manipulerade vid start. Om du spawnar med Frida kan du hooka dessa kontroller INNAN de körs och förhindra att appen upptäcker Frida.

**Tip 4: Skriv inte kod från scratch – kopiera exempel!**
Det finns tusentals Frida-script på GitHub. Hitta ett som liknar ditt use case, kopiera det och anpassa det. Du behöver inte vara JavaScript-expert!

**Tip 5: PID ändras varje gång du startar om ett program**
Om du attachar till PID 1234 och sedan startar om programmet får det ett nytt PID (t.ex. 5678). Använd därför helst processnamn (`-n`) istället för PID (`-p`) i scripts.

### ✏️ Övningar

#### Övning 1: Förklara med egna ord – Vad är en hook?

Beskriv för någon som aldrig hört talas om Frida: Vad är en "hook"? Använd gärna en egen analogi (inte de som nämnts i guiden).

<details>
<summary>📝 Exempelsvar</summary>

**Exempel 1 (Vägspärr):**
En hook är som en vägspärr på en väg. Varje gång en bil (funktionsanrop) kommer till spärren stoppar polisen (din hook) bilen, inspekterar den, kanske ändrar något i bilen, och släpper sedan fram den.

**Exempel 2 (Brevlåda med spion):**
En hook är som att sätta en kamera i någon annans brevlåda. Varje gång brevbäraren stoppar in ett brev (funktionen levererar data) tar kameran en bild (loggar) och kanske till och med byter ut brevet mot ett annat (modifierar returvärde).

**Exempel 3 (Receptionist):**
En hook är som en receptionist på ett kontor. Alla som vill träffa chefen (funktionen) måste gå via receptionisten först. Receptionisten kan skriva upp vem som besöker, när de kommer, och vad de vill – och kan till och med vägra vissa besökare!
</details>

#### Övning 2: Ge ett exempel på när det vore bra att se vad en app skickar till en server

Beskriv ett verkligt scenario där det skulle vara användbart att "hooka" nätverksanrop och se exakt vilken data som skickas.

<details>
<summary>📝 Exempelsvar</summary>

**Scenario 1: Säkerhetstestning av egen app**
Du har utvecklat en bank-app. Du vill verifiera att den INTE skickar lösenordet i klartext till servern (utan krypterar det först). Du använder Frida för att hooka `send()` och se exakt vad som skickas. Om du ser lösenordet i klartext vet du att det finns en säkerhetsbrist!

**Scenario 2: Förstå API för att bygga integration**
Du vill bygga en integration mot Spotify men dokumentationen är otydlig. Du använder Frida på Spotify-appen för att se exakt vilka API-anrop den gör när du spelar en låt. Nu kan du se exakt URL, parametrar, och headers – och återskapa samma anrop i din integration!

**Scenario 3: Debugging av app som beter sig konstigt**
Din app kraschar ibland när den kommunicerar med servern. Du använder Frida för att logga alla nätverksanrop. Du upptäcker att appen skickar ett felformaterat JSON-objekt vid vissa tillfällen – nu vet du var buggen är!
</details>

#### Övning 3: Fyll i luckor i pseudokod

Här är en förenklad beskrivning av en hook i pseudokod. Fyll i luckorna:

```
När funktion [A]____ anropas:
    1. [B]_____ originalargumenten
    2. [C]_____ dina egna ändringar (om du vill)
    3. Anropa den [D]_____ funktionen
    4. [E]_____ returvärdet
    5. [F]_____ returvärdet (om du vill)
    6. Returnera (eventuellt [G]_____) värdet
```

<details>
<summary>📝 Facit</summary>

```
När funktion [A] checkPassword anropas:
    1. [B] Logga/spara originalargumenten
    2. [C] Gör dina egna ändringar (om du vill)
    3. Anropa den [D] ursprungliga funktionen
    4. [E] Ta emot/fånga returvärdet
    5. [F] Modifiera returvärdet (om du vill)
    6. Returnera (eventuellt [G] modifierat) värdet
```

**Förklaring:**
Detta är det grundläggande flödet för en hook:
- Du fångar anropet INNAN funktionen körs (pre-hook)
- Du kan ändra vad som går in (argument)
- Du låter den riktiga funktionen köra
- Du kan ändra vad som kommer ut (returvärde)
- Du returnerar till den som anropade funktionen

Detta ger dig full kontroll!
</details>

#### Övning 4: Sortera termerna – Definitioner

Matcha varje term med dess definition:

| Term | Definition |
|------|------------|
| A. Process | 1. Koppla Frida till ett program som redan körs |
| B. Hook | 2. Språket Frida-scripts skrivs i |
| C. Attach | 3. Ett program som körs i datorns minne |
| D. Spawn | 4. En "avlyssnare" på en funktion |
| E. JavaScript | 5. Starta ett program med Frida redan kopplat |
| F. API | 6. Gränssnittet ett program erbjuder |

<details>
<summary>📝 Facit</summary>

**Rätt matchning:**
- **A-3**: Process = Ett program som körs i datorns minne
- **B-4**: Hook = En "avlyssnare" på en funktion
- **C-1**: Attach = Koppla Frida till ett program som redan körs
- **D-5**: Spawn = Starta ett program med Frida redan kopplat
- **E-2**: JavaScript = Språket Frida-scripts skrivs i
- **F-6**: API = Gränssnittet ett program erbjuder

**Minnesregler:**
- **Process** = programmet när det lever (körs)
- **Hook** = kroken du hänger på funktioner
- **Attach** = hoppa på tåget som redan går
- **Spawn** = starta tåget med dig ombord från början
- **JavaScript** = språket för dina scripts
- **API** = menyn av funktioner programmet erbjuder
</details>

#### Övning 5: Identifiera vad som är Frida och vad som är målet

I dessa scenarier, identifiera:
- Vad är **målet** (target)?
- Vad är **Frida**?
- Vad är **ditt mål** (vad du vill uppnå)?

**Scenario 1:**
"Jag vill se vilka funktioner som körs när jag klickar på 'Skicka' i WhatsApp."

**Scenario 2:**
"Jag attachade frida-trace till Chrome och såg alla anrop till malloc()."

**Scenario 3:**
"Jag spawnade Instagram med Frida och hooksade checkLicense() för att se om den kontrollerar något vid start."

<details>
<summary>📝 Facit</summary>

**Scenario 1:**
- **Mål (target)**: WhatsApp-appen
- **Frida**: Verktyget du använder (t.ex. frida-trace eller custom script)
- **Ditt mål**: Identifiera vilka funktioner som anropas vid "Skicka"-klicket (för debugging/förståelse)

**Scenario 2:**
- **Mål (target)**: Chrome-webbläsaren
- **Frida**: frida-trace (verktyget som hookar)
- **Ditt mål**: Se alla minnesallokeringar (malloc-anrop), troligen för att analysera minnesbeteende eller hitta läckor

**Scenario 3:**
- **Mål (target)**: Instagram-appen
- **Frida**: Frida med spawn-läge + hook-script
- **Ditt mål**: Undersöka om appen kontrollerar licens/autenticitet vid start (t.ex. för att bypassa kontroll i labbmiljö)

**Mönster:**
I alla fallen är Frida **verktyget**, målet är **appen/programmet du analyserar**, och ditt mål är **den insikt du vill få eller ändring du vill göra**.
</details>

### 📝 Sammanfattning

**Key Takeaways från Nivå 2:**

- ✅ **Process**: Ett program som körs i minnet, med unikt PID
- ✅ **Hook**: En "avlyssnare" som triggas när en funktion körs – kan logga och modifiera
- ✅ **Attach**: Anslut till en process som redan körs (`frida -n/p`)
- ✅ **Spawn**: Starta en process med Frida från början (`frida -f`)
- ✅ **API**: Gränssnittet av funktioner som program erbjuder/använder
- ✅ **Frida-verktyg**: `frida`, `frida-ps`, `frida-trace`, `frida-ls-devices`
- ✅ **JavaScript**: Språket du skriver Frida-scripts i
- ✅ **frida-trace**: Perfekt för att snabbt se vilka funktioner som anropas utan att skriva kod

### Mini-ordlista

| Term | Förklaring |
|------|------------|
| **Process** | Ett körande program i minnet (har PID och namn) |
| **PID** | Process ID – unikt nummer för varje process |
| **Hook** | En "krok" på en funktion som triggas när funktionen körs |
| **Attach** | Ansluta Frida till en redan körande process |
| **Spawn** | Starta en process med Frida redan kopplat från början |
| **Inject** | Skjuta in din kod (JavaScript) i målprocessen |
| **API** | Application Programming Interface – funktioner ett program erbjuder |
| **CLI** | Command Line Interface – kommandoradsverktyg |
| **Wildcard (*)** | Jokertecken som matchar allt (t.ex. "recv*" = alla funktioner som börjar med recv) |

### Koppling till nästa nivå

Nu kan du grundläggande Frida-termer och vet vilka verktyg som finns! I nästa nivå (Nivå 3: "Under Motorhuven") dyker vi djupare: **hur fungerar Frida tekniskt?** Vi tittar på arkitekturen (Frida-server, gadget, klient), hur injection faktiskt går till, och – viktigast – du kommer skriva ditt **första riktiga Frida-script** för att hooka en funktion! Vi täcker både native (C/C++) och Java/ART (Android).

**Redo att bli teknisk? Låt oss fortsätta! 🔧**

---

## Nivå 3: "Under Motorhuven" 🎓

### Introduktion

Välkommen till den tekniska nivån! Här lär du dig **hur Frida faktiskt fungerar** under huven och – viktigast av allt – du kommer skriva ditt **första riktiga Frida-script**. Vi täcker Fridas arkitektur (server, gadget, klient), hur kod injiceras i processer, och grunderna i att hooka både native-funktioner (C/C++) och Java-metoder (Android). Detta är steget där du går från teori till praktik!

### Kärnkoncept

#### 1. Fridas Arkitektur – De Tre Komponenterna

Frida består av tre huvudkomponenter som arbetar tillsammans:

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   Frida CLI     │ ◄─────► │  Frida-core      │ ◄─────► │ Target Process  │
│  (Din dator)    │   TCP   │(Server/Gadget)   │  Inject │  (Appen/Prog)   │
│                 │         │                  │         │                 │
│ - frida         │         │ - frida-server   │         │ - Din hook-kod  │
│ - frida-trace   │         │ - frida-gadget   │         │ - App-kod       │
│ - Python API    │         │                  │         │                 │
└─────────────────┘         └──────────────────┘         └─────────────────┘
     Host                        Bridge                      Target
```

**1.1 Host/Klient (Din dator):**
- Frida CLI-verktyg (`frida`, `frida-trace`, etc.)
- Python/Node.js API
- Här skriver du dina scripts
- Kommunicerar med target via TCP

**1.2 Bridge (Frida-core):**
Finns i två varianter beroende på användningsfall:

**frida-server:**
- En daemon som körs på målenhet (Android/iOS)
- Lyssnar på port 27042 (default)
- Kräver root/jailbreak på mobila enheter
- Injicerar din kod i target-processer

**frida-gadget:**
- Ett shared library (`.so` på Android, `.dylib` på iOS)
- Bäddas in i själva appen
- Fungerar UTAN root/jailbreak!
- Laddar din kod automatiskt när appen startar

**1.3 Target (Målprocessen):**
- Applikationen du analyserar
- Innehåller både appens kod och din injicerade Frida-kod
- Din kod körs i samma minnesrymd som appen

#### 2. De Tre Driftsätten (Operation Modes)

**Injected Mode (med frida-server):**
```
Du: frida -U -n Instagram
    ↓
frida-server (på telefonen) injicerar Frida i Instagram
    ↓
Din JavaScript-kod körs inne i Instagram-processen
```
- Kräver root/jailbreak
- Flexiblast – kan attacha till vilken process som helst
- Perfekt för analys och debugging

**Embedded Mode (med frida-gadget):**
```
Du: Bygger om APK/IPA med frida-gadget.so inbäddad
    ↓
Installerar appen på enhet (ingen root behövs!)
    ↓
När appen startar laddar gadget din kod automatiskt
```
- Fungerar utan root/jailbreak
- Kräver att du modifierar appen först
- Perfekt för enheter du inte äger/kan roota

**Preloaded Mode:**
- Gadget kör scripts automatiskt från filsystem
- Ingen extern klient behövs
- Perfekt för automation

#### 3. Hur Injection Fungerar (Förenklat)

När du kör `frida -n AppNamn`:

1. **Frida hittar processen** (via PID eller namn)
2. **Frida injicerar frida-agent** (ett shared library) i processen
   - På Linux: använder `ptrace` systemanrop
   - På Android: liknande metod via `ptrace`
   - På iOS: via debugserver
3. **Frida-agent skapar en JavaScript-runtime** (QuickJS engine) inuti processen
4. **Din JavaScript-kod skickas över TCP** och körs i denna runtime
5. **Din kod kan nu interagera** med appens funktioner via Frida API

#### 4. Memory Layout – Var Saker Finns

När en process körs finns allt i minnet:

```
┌───────────────────────────┐  ← Höga adresser
│        Stack              │  (Lokala variabler, funktionsanrop)
├───────────────────────────┤
│         ...               │
├───────────────────────────┤
│        Heap               │  (Dynamiskt allokerat minne)
├───────────────────────────┤
│    Loaded Libraries       │  (libc.so, libssl.so, etc.)
├───────────────────────────┤
│    Application Code       │  (Appens funktioner och data)
├───────────────────────────┤
│    Frida Agent (injected) │  ← DETTA är din kod!
└───────────────────────────┘  ← Låga adresser
```

Frida kan läsa och skriva **var som helst** i detta minne!

#### 5. Modules, Exports och Symbols

**Module (Modul):**
- Ett loaded library (t.ex. `libc.so`, `libssl.so`, `app.exe`)
- Innehåller kod och data
- Lista alla: `Process.enumerateModules()`

**Export:**
- En funktion som modulen "exporterar" (gör tillgänglig för andra)
- T.ex. `open`, `read`, `malloc` från `libc.so`
- Hitta: `Module.findExportByName("libc.so", "open")`

**Symbol:**
- Namn på funktioner/variabler i modulen
- Kan vara exporterade eller interna
- Används för att hitta adresser

#### 6. Interceptor – Hjärtat i Hooking

`Interceptor` är Frida-API:et för att hooka funktioner:

```javascript
Interceptor.attach(TARGET_ADDRESS, {
    onEnter: function(args) {
        // Körs INNAN funktionen körs
        // args[0], args[1], ... = funktionens argument
    },
    onLeave: function(retval) {
        // Körs EFTER funktionen körs
        // retval = returvärdet
    }
});
```

**onEnter:**
- Första steget när funktionen anropas
- Du kan läsa/modifiera argument
- Du kan förhindra att funktionen körs (med `replace`)

**onLeave:**
- Körs när funktionen ska returnera
- Du kan läsa/modifiera returvärdet
- Du kan se vad funktionen faktiskt returnerade

#### 7. Memory – Läsa och Skriva Minne

Frida låter dig läsa/skriva direkt i minnet:

```javascript
// Läsa en sträng från en adress
var str = Memory.readCString(ptr(args[0]));

// Läsa ett heltal
var value = Memory.readInt(ptr(args[0]));

// Skriva en sträng
Memory.writeUtf8String(ptr(address), "Ny sträng");
```

Viktiga typer:
- `ptr(address)` – skapar en pekare från en adress
- `NativePointer` – en adress i minnet
- `args[i]` – är redan NativePointer (i `onEnter`)

### Grundstruktur för Frida-Scripts

Ett typiskt Frida-script följer detta mönster:

```javascript
// 1. Hitta modulen/funktionen du vill hooka
var targetModule = "libc.so";  // eller "app.exe", "MyApp", etc.
var targetFunction = "open";

// 2. Hitta adressen till funktionen
var addr = Module.findExportByName(targetModule, targetFunction);

// 3. Hooka funktionen
Interceptor.attach(addr, {
    onEnter: function(args) {
        console.log("[*] " + targetFunction + " called!");
        // Logga argument, ändra dem, etc.
    },
    onLeave: function(retval) {
        console.log("[*] " + targetFunction + " returned: " + retval);
        // Logga returvärde, ändra det, etc.
    }
});

console.log("[*] Hook installed on " + targetFunction);
```

### Hooka Native-funktioner (C/C++)

#### Exempel 1: Hooka `open()` i libc

**Scenario:** Du vill se vilka filer en app öppnar.

```javascript
// open() har signaturen: int open(const char *pathname, int flags)
// args[0] = pathname (sträng)
// args[1] = flags (heltal)

var openPtr = Module.findExportByName("libc.so", "open");
// På Android använd ofta "libc.so", på iOS "libsystem_kernel.dylib"
// På Windows: "kernel32.dll" för CreateFileW

Interceptor.attach(openPtr, {
    onEnter: function(args) {
        var path = Memory.readCString(args[0]);
        console.log("[open] Opening file: " + path);
    },
    onLeave: function(retval) {
        console.log("[open] File descriptor: " + retval);
    }
});
```

**Output (exempel):**
```
[open] Opening file: /data/data/com.app/databases/user.db
[open] File descriptor: 42
[open] Opening file: /system/lib/libcrypto.so
[open] File descriptor: 43
```

#### Exempel 2: Hooka `strcmp()` för att se lösenordsjämförelser

```javascript
// int strcmp(const char *s1, const char *s2)
var strcmpPtr = Module.findExportByName("libc.so", "strcmp");

Interceptor.attach(strcmpPtr, {
    onEnter: function(args) {
        var str1 = Memory.readCString(args[0]);
        var str2 = Memory.readCString(args[1]);

        if (str1.includes("password") || str2.includes("password")) {
            console.log("[strcmp] Comparing: '" + str1 + "' vs '" + str2 + "'");
        }
    },
    onLeave: function(retval) {
        // retval = 0 betyder strängarna är lika!
        if (retval.toInt32() === 0) {
            console.log("[strcmp] MATCH!");
        }
    }
});
```

#### Exempel 3: Ändra returvärde – Bypass enkel kontroll

**Scenario:** En app har en funktion `isLicenseValid()` som returnerar 0 (false) eller 1 (true).

```javascript
var isLicenseValidPtr = Module.findExportByName("libapp.so", "isLicenseValid");

Interceptor.attach(isLicenseValidPtr, {
    onLeave: function(retval) {
        console.log("[*] Original return value: " + retval);

        // Ändra alltid till 1 (true)
        retval.replace(1);

        console.log("[*] Modified return value: " + retval);
    }
});
```

Nu returnerar funktionen alltid 1, oavsett vad den egentligen beräknade!

### Hooka Java-metoder (Android)

På Android körs Java/Kotlin-kod i **Android Runtime (ART)**. Frida har ett speciellt API för detta: `Java.perform()`.

#### Grundstruktur för Java-hooking:

```javascript
Java.perform(function() {
    // All Java-hooking-kod måste vara inuti denna callback!

    // 1. Hitta klassen
    var ClassName = Java.use("com.example.app.MyClass");

    // 2. Hooka metoden
    ClassName.methodName.implementation = function(arg1, arg2) {
        // Din kod här
        console.log("Method called with: " + arg1 + ", " + arg2);

        // Anropa originalmetoden
        var result = this.methodName(arg1, arg2);

        // Returnera (eventuellt modifierat) resultat
        return result;
    };
});
```

#### Exempel 4: Hooka en Android Activity-metod

**Scenario:** En app har en `checkPassword(String password)` metod i `MainActivity`.

```javascript
Java.perform(function() {
    console.log("[*] Starting script");

    // Hitta MainActivity-klassen
    var MainActivity = Java.use("com.example.app.MainActivity");

    // Hooka checkPassword-metoden
    MainActivity.checkPassword.implementation = function(password) {
        console.log("[*] checkPassword called!");
        console.log("[*] Password entered: " + password);

        // Anropa originalmetoden för att se vad den returnerar
        var result = this.checkPassword(password);
        console.log("[*] Original result: " + result);

        // Låt oss alltid returnera true!
        return true;
    };

    console.log("[*] checkPassword hooked!");
});
```

#### Exempel 5: Hooka StringBuilder för att se vad som byggs

```javascript
Java.perform(function() {
    var StringBuilder = Java.use("java.lang.StringBuilder");

    StringBuilder.toString.implementation = function() {
        var result = this.toString();
        console.log("[StringBuilder] Built string: " + result);
        return result;
    };
});
```

#### Exempel 6: Hitta och hooka alla instanser av en klass

```javascript
Java.perform(function() {
    Java.choose("com.example.app.User", {
        onMatch: function(instance) {
            console.log("[*] Found User instance: " + instance);
            console.log("[*] Username: " + instance.getUsername());
        },
        onComplete: function() {
            console.log("[*] Search complete");
        }
    });
});
```

### Visualisering: Hook-flöde

```
1. App anropar funktion:
   app.js ──> checkPassword("test123")

2. Frida fångar anropet (onEnter):
   [Frida Hook] ──> "Argument: test123"

3. Din kod körs:
   console.log("Password entered: test123")

4. (Valfritt) Anropa original:
   originalCheckPassword("test123") ──> returns false

5. (Valfritt) Ändra returvärde:
   return true (istället för false)

6. App får returvärde:
   app.js <── true (appen tror lösenordet är rätt!)
```

### Steg-för-steg: Första Frida-scriptet

**Mål:** Hooka `open()` på en Android-app och logga filöppningar.

**Steg 1: Förbered enheten**
```bash
# Starta frida-server på Android-enheten (kräver root)
adb push frida-server /data/local/tmp/
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"
```

**Steg 2: Skapa scriptet (hook_open.js)**
```javascript
console.log("[*] Script loaded");

var openPtr = Module.findExportByName("libc.so", "open");

if (openPtr) {
    console.log("[*] Found open at: " + openPtr);

    Interceptor.attach(openPtr, {
        onEnter: function(args) {
            var path = Memory.readCString(args[0]);
            console.log("[open] " + path);
        }
    });

    console.log("[*] Hook installed!");
} else {
    console.log("[!] Could not find open");
}
```

**Steg 3: Kör scriptet**
```bash
frida -U -f com.example.app -l hook_open.js --no-pause
```

**Steg 4: Observera output**
```
[*] Script loaded
[*] Found open at: 0xb6f12340
[*] Hook installed!
[open] /data/data/com.example.app/files/config.xml
[open] /system/fonts/Roboto-Regular.ttf
[open] /proc/self/maps
```

### 💡 Pro Tips

**Tip 1: Använd `null` för att söka i alla moduler**
```javascript
// Söker i ALLA laddade bibliotek
var addr = Module.findExportByName(null, "malloc");
```

**Tip 2: Hantera flera overloaded Java-metoder**
```javascript
Java.perform(function() {
    var MyClass = Java.use("com.example.MyClass");

    // Specifik overload med String-argument
    MyClass.calculate.overload("java.lang.String").implementation = function(str) {
        console.log("String version called");
        return this.calculate(str);
    };

    // Overload med int-argument
    MyClass.calculate.overload("int").implementation = function(num) {
        console.log("Int version called");
        return this.calculate(num);
    };
});
```

**Tip 3: Lista alla laddade moduler för att hitta rätt namn**
```javascript
Process.enumerateModules().forEach(function(module) {
    console.log(module.name + " at " + module.base);
});
```

**Tip 4: Använd `hexdump` för att inspektera minne**
```javascript
Interceptor.attach(addr, {
    onEnter: function(args) {
        console.log(hexdump(args[0], {
            length: 64,
            ansi: true
        }));
    }
});
```

**Tip 5: Spara state mellan onEnter och onLeave**
```javascript
Interceptor.attach(addr, {
    onEnter: function(args) {
        this.startTime = Date.now();  // Spara i 'this'
        this.filename = Memory.readCString(args[0]);
    },
    onLeave: function(retval) {
        var duration = Date.now() - this.startTime;  // Läs från 'this'
        console.log("[*] " + this.filename + " took " + duration + "ms");
    }
});
```

### ✏️ Övningar

#### Övning 1: Rita ett arkitekturdiagram

Rita (på papper eller digital) ett diagram som visar:
- Din dator (klient)
- Frida-server (eller gadget)
- Målprocessen
- Hur data flödar mellan dem

Inkludera:
- Kommunikationsvägar (TCP, injection)
- Vad som körs var
- Var ditt JavaScript-script exekveras

<details>
<summary>📝 Exempellösning</summary>

```
┌────────────────────────┐
│   Din Dator (Host)     │
│                        │
│  ┌──────────────────┐  │
│  │ Frida CLI        │  │
│  │ frida -U -n App  │  │
│  └────────┬─────────┘  │
│           │            │
│  ┌────────▼─────────┐  │
│  │ hook_script.js   │  │ ← Du skriver detta
│  └────────┬─────────┘  │
└───────────┼────────────┘
            │
            │ TCP över
            │ USB/WiFi
            ▼
┌────────────────────────┐
│ Android Enhet/Emulator │
│                        │
│  ┌──────────────────┐  │
│  │ frida-server     │  │ ← Lyssnar på port 27042
│  │ (körs som daemon)│  │
│  └────────┬─────────┘  │
│           │            │
│           │ Injicerar  │
│           ▼            │
│  ┌──────────────────┐  │
│  │  Target Process  │  │
│  │  (Instagram)     │  │
│  │                  │  │
│  │ ┌──────────────┐ │  │
│  │ │ Frida Agent  │ │  │ ← Injicerad kod
│  │ │ (JS runtime) │ │  │
│  │ │              │ │  │
│  │ │ [Din hook]   │ │  │ ← Ditt script körs HÄR
│  │ └──────────────┘ │  │
│  │                  │  │
│  │ App-kod          │  │
│  │ Java/Native libs │  │
│  └──────────────────┘  │
└────────────────────────┘

Dataflöde:
1. Du kör frida-kommando på din dator
2. Frida-klient skickar script över TCP till frida-server
3. frida-server injicerar agent i target-process
4. Din hook-kod körs inne i target-process
5. Loggmeddelanden skickas tillbaka till din dator via TCP
```
</details>

#### Övning 2: Skriv eller komplettera ett Frida-script

Komplettera detta script för att logga argument till `fopen()`:

```javascript
// fopen har signaturen: FILE* fopen(const char *filename, const char *mode)
var fopenPtr = Module.findExportByName(__________, "fopen");

Interceptor.attach(fopenPtr, {
    onEnter: function(args) {
        var filename = __________;
        var mode = __________;
        console.log("[fopen] File: " + filename + ", Mode: " + mode);
    }
});
```

<details>
<summary>📝 Lösning</summary>

```javascript
// fopen har signaturen: FILE* fopen(const char *filename, const char *mode)
var fopenPtr = Module.findExportByName("libc.so", "fopen");
// eller null för att söka i alla bibliotek

Interceptor.attach(fopenPtr, {
    onEnter: function(args) {
        var filename = Memory.readCString(args[0]);
        var mode = Memory.readCString(args[1]);
        console.log("[fopen] File: " + filename + ", Mode: " + mode);
    }
});
```

**Förklaring:**
- `args[0]` är första argumentet (filename) – en pekare till en C-sträng
- `args[1]` är andra argumentet (mode) – också en pekare till C-sträng
- `Memory.readCString()` läser en null-terminerad C-sträng från en adress
</details>

#### Övning 3: Beskriv steg-för-steg för att hooka en app

Beskriv alla steg för att:
1. Starta en Android-app (t.ex. Instagram)
2. Attacha Frida
3. Lista alla laddade moduler
4. Välja en funktion att hooka (t.ex. `malloc`)

<details>
<summary>📝 Lösning</summary>

**Steg 1: Starta appen**
```bash
# Starta appen manuellt på enheten, eller:
frida -U -f com.instagram.android --no-pause
```

**Steg 2: Attacha Frida (om appen redan körs)**
```bash
frida -U -n Instagram
```

**Steg 3: Lista moduler (inne i Frida-konsolen)**
```javascript
Process.enumerateModules().forEach(function(m) {
    console.log(m.name + " - Base: " + m.base);
});
```

Eller spara till fil:
```bash
frida -U -n Instagram --eval 'Process.enumerateModules().forEach(function(m) { console.log(m.name); })'
```

**Steg 4: Välj och hooka malloc**
```javascript
var mallocPtr = Module.findExportByName("libc.so", "malloc");

Interceptor.attach(mallocPtr, {
    onEnter: function(args) {
        var size = args[0].toInt32();
        if (size > 1000) {  // Logga bara stora allokeringar
            console.log("[malloc] Allocating " + size + " bytes");
        }
    },
    onLeave: function(retval) {
        // retval är adressen till allokerat minne
    }
});
```

**Komplett kommando (med script från fil):**
```bash
frida -U -n Instagram -l myscript.js
```
</details>

#### Övning 4: Jämför native vs Java hooking

Fyll i tabellen med likheter och skillnader:

| Aspekt | Native (C/C++) | Java/ART (Android) |
|--------|----------------|---------------------|
| API som används | Interceptor.attach | ??? |
| Hur hitta target | Module.findExportByName | ??? |
| Argument-access | args[0], args[1] | ??? |
| Wrapper-funktion | Ingen | ??? |

<details>
<summary>📝 Lösning</summary>

| Aspekt | Native (C/C++) | Java/ART (Android) |
|--------|----------------|---------------------|
| API som används | `Interceptor.attach` | `Java.use()` + `.implementation` |
| Hur hitta target | `Module.findExportByName("lib.so", "func")` | `Java.use("com.example.Class")` |
| Argument-access | `args[0]`, `args[1]` (NativePointer) | Normala JS-parametrar (arg1, arg2) |
| Wrapper-funktion | `onEnter`/`onLeave` callbacks | Hel funktion-implementation |
| Behöver wrapper | Nej (direkt attach) | Ja (`Java.perform(function() { ... })`) |
| Returvärde-ändring | `retval.replace(newVal)` | Returnera direkt: `return newVal;` |
| Typer | Minnes-adresser och pekare | Java-objekt och primitiver |

**Likheter:**
- Båda tillåter att se argument och returvärden
- Båda tillåter att modifiera beteende
- Båda körs i samma process som target

**Skillnader:**
- Native = låg nivå, adresser och minne
- Java = hög nivå, objekt och metoder
</details>

#### Övning 5: Beskriv användning av Frida i CTF

**Scenario:** I en CTF-tävling har du en Android-app som frågar efter ett lösenord. Om du anger rätt lösenord får du flaggan. Hur skulle du använda Frida för att:
1. Hitta lösenords-verifieringsfunktionen
2. Se vad rätt lösenord är ELLER bypassa kontrollen

<details>
<summary>📝 Exempellösning</summary>

**Metod 1: Hitta och läsa rätt lösenord**

**Steg 1: Hooka strcmp/equals**
```javascript
// Native approach
var strcmpPtr = Module.findExportByName("libc.so", "strcmp");
Interceptor.attach(strcmpPtr, {
    onEnter: function(args) {
        var s1 = Memory.readCString(args[0]);
        var s2 = Memory.readCString(args[1]);
        console.log("[strcmp] '" + s1 + "' vs '" + s2 + "'");
    }
});

// Java approach
Java.perform(function() {
    var String = Java.use("java.lang.String");
    String.equals.implementation = function(other) {
        var result = this.equals(other);
        console.log("[equals] '" + this + "' vs '" + other + "' = " + result);
        return result;
    };
});
```

**Steg 2: Ange testlösenord och observera**
- Ange "test123" i appen
- Frida loggar: `[strcmp] 'test123' vs 'SuperSecret2024'`
- Nu vet du rätt lösenord: `SuperSecret2024`!

**Metod 2: Bypassa kontrollen**

```javascript
Java.perform(function() {
    // Hitta verifieringsfunktionen
    var MainActivity = Java.use("com.ctf.app.MainActivity");

    // Hooka checkPassword
    MainActivity.checkPassword.implementation = function(input) {
        console.log("[*] checkPassword called with: " + input);

        // Returnera alltid true, oavsett input
        return true;
    };

    // Eller hooka showFlag för att anropa den direkt:
    var activity = Java.use("android.app.Activity");
    Java.choose("com.ctf.app.MainActivity", {
        onMatch: function(instance) {
            console.log("[*] Found MainActivity instance");
            instance.showFlag();  // Anropa metoden direkt!
        },
        onComplete: function() {}
    });
});
```

**Metod 3: Dumpa all input**
```javascript
// Hooka alla TextEdit.getText() för att se vad användaren skriver
Java.perform(function() {
    var EditText = Java.use("android.widget.EditText");
    EditText.getText.implementation = function() {
        var text = this.getText();
        console.log("[EditText] Content: " + text.toString());
        return text;
    };
});
```

**Best practice:**
- Börja brett (hooka vanliga funktioner som strcmp, equals)
- Smalna av när du hittar relevant kod
- Testa både native och Java-lager
</details>

#### Övning 6 (Bonus): Förstå memory-addresses

Förklara skillnaden mellan:
- `Module.findExportByName("libc.so", "malloc")`
- `Module.getBaseAddress("libc.so")`
- En NativePointer som `0x7ffab1234`

<details>
<summary>📝 Förklaring</summary>

**`Module.findExportByName("libc.so", "malloc")`:**
- Returnerar **adressen till funktionen `malloc`** i `libc.so`
- Söker i modulens export-tabell
- Exempel-retur: `NativePointer("0x7ffab1234560")`
- Användning: Du vill hooka just denna funktion

**`Module.getBaseAddress("libc.so")`:**
- Returnerar **startagressen** där `libc.so` är laddad i minnet
- Detta är "basen" där modulen börjar
- Exempel-retur: `NativePointer("0x7ffab1000000")`
- Användning: Relativadressering (base + offset)

**`NativePointer("0x7ffab1234")`:**
- En specifik adress i processens minne
- Kan peka på vad som helst: kod, data, stack, heap
- Användning: Direkt minnes-access

**Relation:**
```
Module base:     0x7ffab1000000  (början av libc.so)
+ Offset:        0x234560         (malloc's plats i modulen)
= malloc address: 0x7ffab1234560  (findExportByName-resultat)
```

**Praktiskt exempel:**
```javascript
var base = Module.getBaseAddress("libc.so");
console.log("libc base: " + base);

var mallocAddr = Module.findExportByName("libc.so", "malloc");
console.log("malloc at: " + mallocAddr);

var offset = mallocAddr.sub(base);
console.log("malloc offset: " + offset);
```
</details>

### 📝 Sammanfattning

**Key Takeaways från Nivå 3:**

- ✅ **Frida-arkitektur**: Klient (host) ↔ Bridge (server/gadget) ↔ Target (app)
- ✅ **Tre driftlägen**: Injected (frida-server), Embedded (frida-gadget), Preloaded
- ✅ **Modules & Exports**: Bibliotek innehåller funktioner som du hittar med `findExportByName`
- ✅ **Interceptor.attach**: Hooka native-funktioner med `onEnter`/`onLeave`
- ✅ **Java.perform**: Wrapper för all Java-hooking på Android
- ✅ **Memory API**: Läs/skriv minne med `Memory.readCString`, `Memory.readInt`, etc.
- ✅ **args[i]**: Funktionsargument i `onEnter` (native) eller direkta parametrar (Java)
- ✅ **retval**: Returvärde i `onLeave` – kan läsas och modifieras

### Mini-ordlista

| Term | Förklaring |
|------|------------|
| **frida-server** | Daemon på målenhet som injicerar Frida i processer (kräver root) |
| **frida-gadget** | Shared library som bäddas in i app (fungerar utan root) |
| **Interceptor** | Frida API för att hooka funktioner |
| **Module** | Ett laddat bibliotek (t.ex. libc.so, app.exe) |
| **Export** | En funktion som modulen exponerar publikt |
| **NativePointer** | En minnesadress (pekare) |
| **onEnter** | Callback som körs INNAN hookad funktion exekverar |
| **onLeave** | Callback som körs EFTER hookad funktion exekverar |
| **Java.perform** | Wrapper för Java-hooking (Android ART) |
| **Java.use** | Laddar en Java-klass för hooking |
| **Memory** | Frida API för att läsa/skriva minne direkt |

### Koppling till nästa nivå

Nu kan du skriva grundläggande Frida-scripts för både native och Java! I nästa nivå (Nivå 4: "Avancerad Mästerskap") går vi djupare: **Frida Stalker** för instruktionsnivå-tracing, hantera komplexa datastrukturer, **bypassa skydd** (anti-debug, anti-Frida), struktur för större projekt, och viktiga **etik/juridik-aspekter**. Du kommer också lära dig anti-patterns att undvika och best practices för produktionskvalitet!

**Redo för avancerade tekniker? Låt oss dyka djupare! 🚀**

---

## Nivå 4: "Avancerad Mästerskap" 🏛️

### Introduktion

Välkommen till expertterritoriet! På denna nivå lär du dig avancerade Frida-tekniker som används av professionella säkerhetsforskare. Vi täcker **Frida Stalker** för instruktionsnivå-tracing, hantering av komplexa datastrukturer, tekniker för att **bypassa säkerhetsskydd** (anti-debug, anti-Frida), hur du strukturerar större Frida-projekt, och viktiga **etiska och juridiska** aspekter. Du kommer också lära dig anti-patterns att undvika och best practices för produktionskvalitet. Detta är nivån där du går från att kunna grunderna till att behärska Frida professionellt.

### Kärnkoncept

#### 1. Frida Stalker – Instruktionsnivå-tracing

**Stalker** är Fridas kraftfullaste och mest avancerade komponent. Till skillnad från `Interceptor` (som hookar specifika funktioner) följer Stalker **varje enskild instruktion** som körs.

**Analogi:**
- **Interceptor** = Kameror vid vägkorsningar (ser bara när bilar passerar specifika punkter)
- **Stalker** = En helikopter som följer en bil överallt den åker (ser varje sväng, acceleration, inbromsning)

**Hur Stalker fungerar:**
1. Du säger åt Stalker att följa en tråd (thread)
2. Stalker kopierar kodblock just-in-time (JIT)
3. Interlacerar instrumentationskod mellan instruktionerna
4. Kör den instrumenterade versionen
5. Genererar events för varje instruktion, anrop, return, etc.

**Grundläggande Stalker-användning:**

```javascript
// Följ den nuvarande tråden
Stalker.follow(Process.getCurrentThreadId(), {
    events: {
        call: true,  // Logga CALL-instruktioner
        ret: true,   // Logga RET-instruktioner
        exec: false  // VARNING: exec=true ger ENORM overhead!
    },
    onReceive: function(events) {
        // events är en rå buffer med events
        var parsedEvents = Stalker.parse(events);
        console.log("Received " + parsedEvents.length + " events");
    }
});
```

**Praktiskt exempel - Spåra alla funktionsanrop:**

```javascript
// Spåra alla calls till funktioner i en specifik modul
var targetModule = Process.getModuleByName("libgame.so");

Stalker.follow(Process.getCurrentThreadId(), {
    events: {
        call: true
    },
    onCallSummary: function(summary) {
        // summary innehåller en översikt av alla anrop
        Object.keys(summary).forEach(function(target) {
            var count = summary[target];

            // Hitta funktionsnamn om möjligt
            var symbol = DebugSymbol.fromAddress(ptr(target));

            console.log(count + "x " + symbol);
        });
    }
});

// Stoppa efter 5 sekunder
setTimeout(function() {
    Stalker.unfollow(Process.getCurrentThreadId());
    Stalker.flush();
}, 5000);
```

**Transform callback - Modifiera kod on-the-fly:**

```javascript
Stalker.follow(Process.getCurrentThreadId(), {
    transform: function(iterator) {
        var instruction = iterator.next();

        do {
            // Lägg till custom kod före varje CALL-instruktion
            if (instruction.mnemonic === 'call') {
                iterator.putCallout(function(context) {
                    console.log("CALL to: " + instruction.opStr);
                });
            }

            // Behåll originalinstruktionen
            iterator.keep();
        } while ((instruction = iterator.next()) !== null);
    }
});
```

**⚠️ Prestandavarning:**
Stalker har ENORM overhead, speciellt med `exec: true`. Använd sparsamt och bara på kritiska koddelar!

#### 2. Hantera Komplexa Datastrukturer

I verkliga applikationer stöter du ofta på komplexa datastrukturer: structs, arrays, linked lists, etc.

**Läsa en C struct:**

```javascript
// Antag: struct User { char name[32]; int age; int id; }

var User = {
    name: function(ptr) {
        return Memory.readCString(ptr);
    },
    age: function(ptr) {
        return Memory.readInt(ptr.add(32));  // name är 32 bytes
    },
    id: function(ptr) {
        return Memory.readInt(ptr.add(36));  // name(32) + age(4)
    }
};

// Användning
Interceptor.attach(getUserPtr, {
    onLeave: function(retval) {
        console.log("Name: " + User.name(retval));
        console.log("Age: " + User.age(retval));
        console.log("ID: " + User.id(retval));
    }
});
```

**Bättre approach med CModule (inline C):**

```javascript
const cm = new CModule(`
#include <gum/guminterceptor.h>

typedef struct {
    char name[32];
    int age;
    int id;
} User;

void log_user(User *user) {
    // Logga direkt i C (mycket snabbare!)
    _send_message(user->name, user->age, user->id);
}
`);

// Hooka och använd C-funktionen
Interceptor.attach(getUserPtr, {
    onLeave: function(retval) {
        cm.log_user(retval);
    }
});
```

**Hantera arrays och buffers:**

```javascript
// Läs en array av 10 integers
function readIntArray(ptr, count) {
    var result = [];
    for (var i = 0; i < count; i++) {
        result.push(Memory.readInt(ptr.add(i * 4)));
    }
    return result;
}

// Användning
Interceptor.attach(addr, {
    onEnter: function(args) {
        var array = readIntArray(args[0], 10);
        console.log("Array: " + JSON.stringify(array));
    }
});
```

**Java - Komplexa objekt:**

```javascript
Java.perform(function() {
    var ArrayList = Java.use("java.util.ArrayList");

    ArrayList.add.overload("java.lang.Object").implementation = function(obj) {
        console.log("[ArrayList.add] Adding: " + obj.toString());

        // Inspektera objektets klass och fält
        var clazz = obj.getClass();
        console.log("  Class: " + clazz.getName());

        // Försök läsa fält (om publika)
        try {
            var fields = clazz.getDeclaredFields();
            for (var i = 0; i < fields.length; i++) {
                fields[i].setAccessible(true);
                var fieldName = fields[i].getName();
                var fieldValue = fields[i].get(obj);
                console.log("  " + fieldName + ": " + fieldValue);
            }
        } catch (e) {}

        return this.add(obj);
    };
});
```

#### 3. Bypassa Säkerhetsskydd

Moderna appar implementerar ofta skydd mot reverse engineering. Här är de vanligaste och hur man hanterar dem med Frida:

**A. Anti-Debug Detection**

**Detektion via ptrace:**
```javascript
// På Linux/Android kollar appar ofta om ptrace redan används
// ptrace(PTRACE_TRACEME, 0, 0, 0) returnerar -1 om redan attachad

var ptracePtr = Module.findExportByName("libc.so", "ptrace");

Interceptor.attach(ptracePtr, {
    onEnter: function(args) {
        var request = args[0].toInt32();

        // PTRACE_TRACEME = 0
        if (request === 0) {
            console.log("[anti-debug] Detected ptrace TRACEME check");
        }
    },
    onLeave: function(retval) {
        // Returnera alltid success (0)
        retval.replace(0);
    }
});
```

**Detektion via /proc/self/status:**
```javascript
// Appar läser ofta TracerPid från /proc/self/status
var openPtr = Module.findExportByName("libc.so", "open");
var readPtr = Module.findExportByName("libc.so", "read");

var statusFd = -1;

Interceptor.attach(openPtr, {
    onEnter: function(args) {
        var path = Memory.readCString(args[0]);
        if (path.indexOf("/proc/self/status") !== -1) {
            this.isStatus = true;
        }
    },
    onLeave: function(retval) {
        if (this.isStatus) {
            statusFd = retval.toInt32();
        }
    }
});

Interceptor.attach(readPtr, {
    onEnter: function(args) {
        this.fd = args[0].toInt32();
        this.buf = args[1];
        this.count = args[2].toInt32();
    },
    onLeave: function(retval) {
        if (this.fd === statusFd) {
            // Ersätt "TracerPid: [nonzero]" med "TracerPid: 0"
            var data = Memory.readCString(this.buf, this.count);
            data = data.replace(/TracerPid:\t[0-9]+/, "TracerPid:\t0");
            Memory.writeUtf8String(this.buf, data);
        }
    }
});
```

**B. Anti-Frida Detection**

Appar letar efter tecken på Frida:

1. **Frida-relaterade portar (27042, 27043)**
2. **Frida-relaterade filer (/data/local/tmp/frida-server)**
3. **Frida-relaterade threads/maps**
4. **Frida-specifika symboler i minnet**

**Bypass: Byt namn på frida-server:**
```bash
# Istället för:
adb push frida-server /data/local/tmp/frida-server

# Använd:
adb push frida-server /data/local/tmp/my_daemon
adb shell "chmod 755 /data/local/tmp/my_daemon"
adb shell "/data/local/tmp/my_daemon &"

# Anslut med port forwarding:
adb forward tcp:27044 tcp:27042
frida -H 127.0.0.1:27044 -f com.example.app
```

**Bypass: Hooka detektion:**
```javascript
// Många appar använder strstr/strcmp för att hitta "frida"
var strstrPtr = Module.findExportByName("libc.so", "strstr");

Interceptor.attach(strstrPtr, {
    onEnter: function(args) {
        this.haystack = Memory.readCString(args[0]);
        this.needle = Memory.readCString(args[1]);
    },
    onLeave: function(retval) {
        // Om de söker efter "frida", returnera NULL (ej hittad)
        if (this.needle.toLowerCase().indexOf("frida") !== -1) {
            console.log("[anti-frida] Blocked search for: " + this.needle);
            retval.replace(ptr(0));
        }
    }
});
```

**C. SSL Pinning Bypass**

SSL pinning förhindrar man-in-the-middle-attacker genom att hårdkoda förväntade certifikat.

**Universal Android SSL Pinning Bypass:**
```javascript
Java.perform(function() {
    console.log("[*] Bypassing SSL Pinning");

    // Bypass TrustManagerImpl
    var TrustManagerImpl = Java.use("com.android.org.conscrypt.TrustManagerImpl");
    TrustManagerImpl.verifyChain.implementation = function(untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
        console.log("[*] SSL Pinning bypass for: " + host);
        return untrustedChain;
    };

    // Bypass OkHttp CertificatePinner
    try {
        var CertificatePinner = Java.use("okhttp3.CertificatePinner");
        CertificatePinner.check.overload("java.lang.String", "java.util.List").implementation = function(hostname, peerCertificates) {
            console.log("[*] OkHttp SSL Pinning bypass for: " + hostname);
            return;
        };
    } catch (e) {
        console.log("[-] OkHttp not found");
    }

    console.log("[*] SSL Pinning bypass ready");
});
```

**D. Root Detection Bypass**

```javascript
Java.perform(function() {
    console.log("[*] Bypassing Root Detection");

    // Vanliga root-detection-metoder
    var methods = [
        // RootBeer library
        {
            class: "com.scottyab.rootbeer.RootBeer",
            method: "isRooted",
            returnValue: false
        },
        // Custom checks
        {
            class: "com.example.app.SecurityCheck",
            method: "isDeviceRooted",
            returnValue: false
        }
    ];

    methods.forEach(function(target) {
        try {
            var clazz = Java.use(target.class);
            clazz[target.method].implementation = function() {
                console.log("[*] Bypassed: " + target.class + "." + target.method);
                return target.returnValue;
            };
        } catch (e) {
            console.log("[-] Not found: " + target.class);
        }
    });

    // Bypass file existence checks (common su paths)
    var File = Java.use("java.io.File");
    File.exists.implementation = function() {
        var path = this.getAbsolutePath();

        if (path.indexOf("/su") !== -1 ||
            path.indexOf("magisk") !== -1 ||
            path.indexOf("supersu") !== -1) {
            console.log("[*] Hiding file: " + path);
            return false;
        }

        return this.exists();
    };
});
```

#### 4. Strukturera Större Frida-Projekt

När dina scripts växer behöver du struktur. Här är best practices:

**Modulär struktur:**

```
frida-project/
├── main.js              # Entry point
├── modules/
│   ├── hooks.js         # Hook-funktioner
│   ├── utils.js         # Hjälpfunktioner
│   ├── bypass.js        # Bypass-logik
│   └── logging.js       # Loggnings-ramverk
├── config.js            # Konfiguration
└── README.md
```

**main.js:**
```javascript
// Load modules
var hooks = require('./modules/hooks');
var bypass = require('./modules/bypass');
var config = require('./config');

console.log("[*] Starting " + config.APP_NAME + " instrumentation");

// Initialize bypasses
if (config.BYPASS_ROOT_DETECTION) {
    bypass.bypassRootDetection();
}

if (config.BYPASS_SSL_PINNING) {
    bypass.bypassSSLPinning();
}

// Install hooks
hooks.installAll();

console.log("[*] Instrumentation ready");
```

**modules/utils.js:**
```javascript
// Export utility functions
module.exports = {
    /**
     * Safely call a Java method
     */
    safeJavaCall: function(className, methodName, impl) {
        Java.perform(function() {
            try {
                var clazz = Java.use(className);
                clazz[methodName].implementation = impl;
                console.log("[+] Hooked: " + className + "." + methodName);
            } catch (e) {
                console.log("[-] Failed to hook: " + className + "." + methodName);
                console.log("    " + e);
            }
        });
    },

    /**
     * Log with timestamp
     */
    log: function(tag, message) {
        var timestamp = new Date().toISOString();
        console.log("[" + timestamp + "] [" + tag + "] " + message);
    },

    /**
     * Dump bytes as hex
     */
    hexdump: function(ptr, length) {
        return hexdump(ptr, { length: length, header: true, ansi: true });
    }
};
```

**config.js:**
```javascript
module.exports = {
    APP_NAME: "TargetApp",
    APP_PACKAGE: "com.example.app",

    // Feature flags
    BYPASS_ROOT_DETECTION: true,
    BYPASS_SSL_PINNING: true,
    BYPASS_FRIDA_DETECTION: true,

    // Logging
    LOG_LEVEL: "INFO",  // DEBUG, INFO, WARN, ERROR
    LOG_TO_FILE: false,

    // Targets
    HOOK_CLASSES: [
        "com.example.app.MainActivity",
        "com.example.app.LoginActivity"
    ]
};
```

#### 5. Best Practices

**A. Felhantering:**

```javascript
function safeHook(addr, callbacks) {
    try {
        if (!addr || addr.isNull()) {
            console.log("[-] Invalid address");
            return;
        }

        Interceptor.attach(addr, {
            onEnter: function(args) {
                try {
                    if (callbacks.onEnter) {
                        callbacks.onEnter.call(this, args);
                    }
                } catch (e) {
                    console.log("[!] Error in onEnter: " + e);
                }
            },
            onLeave: function(retval) {
                try {
                    if (callbacks.onLeave) {
                        callbacks.onLeave.call(this, retval);
                    }
                } catch (e) {
                    console.log("[!] Error in onLeave: " + e);
                }
            }
        });
    } catch (e) {
        console.log("[!] Failed to attach hook: " + e);
    }
}
```

**B. Performance-optimering:**

```javascript
// BAD: Loggar ALLT (överväldigande output)
Interceptor.attach(mallocPtr, {
    onEnter: function(args) {
        console.log("[malloc] Size: " + args[0]);
    }
});

// GOOD: Filtrera och sammanfatta
var mallocStats = {
    count: 0,
    totalSize: 0,
    largeAllocs: []
};

Interceptor.attach(mallocPtr, {
    onEnter: function(args) {
        var size = args[0].toInt32();
        mallocStats.count++;
        mallocStats.totalSize += size;

        if (size > 10000) {  // Endast stora allokeringar
            mallocStats.largeAllocs.push(size);
        }
    }
});

// Logga sammanfattning varje sekund
setInterval(function() {
    console.log("[malloc] Stats: " +
        mallocStats.count + " calls, " +
        mallocStats.totalSize + " bytes total, " +
        mallocStats.largeAllocs.length + " large allocs");

    // Reset
    mallocStats = { count: 0, totalSize: 0, largeAllocs: [] };
}, 1000);
```

**C. Minneshantering:**

```javascript
// BAD: Läcker minne
Interceptor.attach(addr, {
    onEnter: function(args) {
        // Skapar nya JavaScript-objekt för varje anrop
        var data = {
            arg0: args[0].toString(),
            timestamp: new Date().toISOString()
        };
        // 'data' samlas aldrig upp om du sparar referenser globalt!
    }
});

// GOOD: Återanvänd och rensa
var dataCache = [];
var MAX_CACHE_SIZE = 100;

Interceptor.attach(addr, {
    onEnter: function(args) {
        dataCache.push({
            arg0: args[0].toString(),
            timestamp: Date.now()
        });

        // Rensa gamla entries
        if (dataCache.length > MAX_CACHE_SIZE) {
            dataCache = dataCache.slice(-MAX_CACHE_SIZE);
        }
    }
});
```

#### 6. Anti-Patterns att Undvika

**❌ Anti-Pattern 1: Hooka för många funktioner**

```javascript
// BAD: Hookar tusentals anrop per sekund
var libc = Process.getModuleByName("libc.so");
libc.enumerateExports().forEach(function(exp) {
    Interceptor.attach(exp.address, {
        onEnter: function() {
            console.log(exp.name);
        }
    });
});

// GOOD: Selektivt hooka endast relevanta funktioner
var targets = ["open", "read", "write", "connect"];
targets.forEach(function(name) {
    var addr = Module.findExportByName("libc.so", name);
    if (addr) {
        safeHook(addr, { /* ... */ });
    }
});
```

**❌ Anti-Pattern 2: Blockera main-tråden**

```javascript
// BAD: Synkron, blockerande operation
Interceptor.attach(addr, {
    onEnter: function(args) {
        // Detta pausar target-appen!
        var result = performExpensiveAnalysis(args[0]);
        sendToServer(result);  // Synkron nätverksanrop
    }
});

// GOOD: Asynkron hantering
Interceptor.attach(addr, {
    onEnter: function(args) {
        var dataCopy = Memory.dup(args[0], 1024);

        // Skicka till bakgrundstråd
        setTimeout(function() {
            var result = performExpensiveAnalysis(dataCopy);
            sendToServer(result);
        }, 0);
    }
});
```

**❌ Anti-Pattern 3: Otydlig loggning**

```javascript
// BAD: Svårt att följa
console.log("X");  // Vad är X?
console.log(ptr);  // Vilken pekare?
console.log("OK"); // Vad är OK?

// GOOD: Strukturerad loggning
console.log("[ClassName.methodName] Called with arg=" + arg);
console.log("[*] Successfully hooked FunctionName at " + addr);
console.log("[+] Authentication bypassed");
console.log("[-] Failed to find TargetModule");
```

#### 7. Etik och Juridik ⚖️

Detta är **KRITISKT** viktigt. Frida är ett kraftfullt verktyg som kan användas både för gott och ont.

**✅ Laglig och etisk användning:**

1. **Dina egna applikationer**
   - Testa säkerhet i appar du utvecklat
   - Debugga egna problem
   - Analysera prestanda

2. **Med explicit tillstånd**
   - Penetrationstestning för kunder (skriftligt kontrakt!)
   - Security audits för företag
   - Bug bounty-program (följ reglerna!)

3. **Utbildning och forskning**
   - CTF-tävlingar (Capture The Flag)
   - Akademisk forskning
   - Labbmiljöer (isolerade system)

4. **Defensive security**
   - Analysera malware i sandlåda
   - Förstå attack-vektorer
   - Utveckla försvar

**❌ Olaglig och oetisk användning:**

1. **Aldrig utan tillstånd:**
   - Andras appar på produktionssystem
   - Kringgå betalningar/licenser
   - Stjäla data eller credentials
   - Manipulera online-spel (banneligt)

2. **Följ lagar och regler:**
   - **CFAA** (USA): Computer Fraud and Abuse Act
   - **EU**: GDPR för persondata
   - **Sverige**: Dataintrångslagen (BrB 4 kap 9c §)
   - **Användarvillkor**: Bryt inte ToS/EULA

3. **Etiska principer:**
   - **Informed consent**: Får du analysera detta?
   - **Proportionality**: Matchar metoden syftet?
   - **Transparency**: Dokumentera vad du gör
   - **Responsible disclosure**: Rapportera sårbarheter ansvarsfullt

**Gråzoner att undvika:**

- **"Men jag äger telefonen!"** – Du äger hårdvaran, inte nödvändigtvis rätten att modifiera andras mjukvara
- **"Det är bara för lärande!"** – Lär dig på dina egna system eller explicita labbmiljöer
- **"Alla gör det!"** – Juridiskt och etiskt fel blir inte rätt för att många gör det

**Best practice:**
```
OM du är osäker → Fråga först!
OM det känns gränsfall → Gör det inte!
OM du hittar en sårbarhet → Responsible disclosure!
```

### Exempel

#### Exempel 1: Komplett Anti-Debug Script

```javascript
/**
 * Comprehensive Anti-Debug Bypass
 * Target: Android apps with multiple debug detection methods
 */

console.log("[*] Loading anti-debug bypass...");

// 1. Bypass ptrace
var ptracePtr = Module.findExportByName("libc.so", "ptrace");
if (ptracePtr) {
    Interceptor.attach(ptracePtr, {
        onEnter: function(args) {
            this.request = args[0].toInt32();
        },
        onLeave: function(retval) {
            if (this.request === 0) {  // PTRACE_TRACEME
                console.log("[anti-debug] Bypassed ptrace TRACEME");
                retval.replace(0);
            }
        }
    });
    console.log("[+] Hooked ptrace");
}

// 2. Bypass /proc/self/status check
var openPtr = Module.findExportByName("libc.so", "open");
var readPtr = Module.findExportByName("libc.so", "read");
var statusFd = -1;

Interceptor.attach(openPtr, {
    onEnter: function(args) {
        var path = Memory.readCString(args[0]);
        this.isStatus = path.indexOf("/proc/self/status") !== -1;
        this.isStatus = this.isStatus || path.indexOf("/proc/self/task") !== -1;
    },
    onLeave: function(retval) {
        if (this.isStatus) {
            statusFd = retval.toInt32();
            console.log("[anti-debug] Detected status file open: fd=" + statusFd);
        }
    }
});

Interceptor.attach(readPtr, {
    onEnter: function(args) {
        this.fd = args[0].toInt32();
        this.buf = args[1];
        this.count = args[2].toInt32();
    },
    onLeave: function(retval) {
        if (this.fd === statusFd) {
            var originalData = Memory.readUtf8String(this.buf, retval.toInt32());

            // Replace TracerPid value
            var patchedData = originalData.replace(/TracerPid:\t[0-9]+/, "TracerPid:\t0");

            Memory.writeUtf8String(this.buf, patchedData);
            console.log("[anti-debug] Patched TracerPid in status file");
        }
    }
});

console.log("[+] Anti-debug bypass ready");
```

#### Exempel 2: Advanced SSL Pinning Bypass med Logging

```javascript
/**
 * Universal SSL Pinning Bypass with detailed logging
 */

Java.perform(function() {
    console.log("[*] Universal SSL Pinning Bypass starting...");

    // Store bypassed hosts
    var bypassedHosts = new Set();

    // 1. Bypass TrustManagerImpl (works for most apps)
    try {
        var TrustManagerImpl = Java.use("com.android.org.conscrypt.TrustManagerImpl");

        TrustManagerImpl.verifyChain.implementation = function(untrustedChain, trustAnchorChain, host, clientAuth, ocspData, tlsSctData) {
            if (!bypassedHosts.has(host)) {
                console.log("[SSL] Bypassing pinning for: " + host);
                bypassedHosts.add(host);
            }
            return untrustedChain;
        };

        console.log("[+] Hooked TrustManagerImpl");
    } catch (e) {
        console.log("[-] TrustManagerImpl not found: " + e);
    }

    // 2. Bypass OkHttp3 CertificatePinner
    try {
        var CertificatePinner = Java.use("okhttp3.CertificatePinner");

        CertificatePinner.check.overload("java.lang.String", "java.util.List").implementation = function(hostname, peerCertificates) {
            console.log("[SSL] OkHttp bypass for: " + hostname);
            return;
        };

        console.log("[+] Hooked OkHttp3 CertificatePinner");
    } catch (e) {
        console.log("[-] OkHttp3 not found");
    }

    // 3. Bypass OkHttp2 (legacy)
    try {
        var CertificatePinner2 = Java.use("com.squareup.okhttp.CertificatePinner");

        CertificatePinner2.check.overload("java.lang.String", "java.security.cert.Certificate").implementation = function(hostname, cert) {
            console.log("[SSL] OkHttp2 bypass for: " + hostname);
            return;
        };

        console.log("[+] Hooked OkHttp2 CertificatePinner");
    } catch (e) {
        console.log("[-] OkHttp2 not found");
    }

    // 4. Bypass Conscrypt (alternative)
    try {
        var ConscryptFileDescriptorSocket = Java.use("com.android.org.conscrypt.ConscryptFileDescriptorSocket");

        ConscryptFileDescriptorSocket.verifyCertificateChain.implementation = function(certRefs, authMethod) {
            console.log("[SSL] Conscrypt bypass");
        };

        console.log("[+] Hooked ConscryptFileDescriptorSocket");
    } catch (e) {
        console.log("[-] Conscrypt not found");
    }

    // 5. Log summary every 10 seconds
    setInterval(function() {
        if (bypassedHosts.size > 0) {
            console.log("[SSL] Summary: Bypassed " + bypassedHosts.size + " hosts");
            console.log("      Hosts: " + Array.from(bypassedHosts).join(", "));
        }
    }, 10000);

    console.log("[*] SSL Pinning Bypass ready");
});
```

#### Exempel 3: Frida Stalker - Spåra Krypteringsanrop

```javascript
/**
 * Use Stalker to trace all calls to AES encryption functions
 */

console.log("[*] Setting up AES tracing with Stalker...");

// Find AES functions in OpenSSL/BoringSSL
var aesEncryptPtr = Module.findExportByName("libcrypto.so", "AES_encrypt");
var aesDecryptPtr = Module.findExportByName("libcrypto.so", "AES_decrypt");

if (!aesEncryptPtr || !aesDecryptPtr) {
    console.log("[-] AES functions not found");
} else {
    console.log("[+] Found AES functions");
    console.log("    AES_encrypt: " + aesEncryptPtr);
    console.log("    AES_decrypt: " + aesDecryptPtr);

    // Hook AES_encrypt to start stalking
    Interceptor.attach(aesEncryptPtr, {
        onEnter: function(args) {
            console.log("\n[AES] Encryption started");
            console.log("      Input:  " + hexdump(args[0], { length: 16 }));
            console.log("      Output: " + args[1]);
            console.log("      Key:    " + args[2]);

            // Start stalking this thread
            var threadId = Process.getCurrentThreadId();

            console.log("[Stalker] Following thread " + threadId);

            var callCount = 0;

            Stalker.follow(threadId, {
                events: {
                    call: true
                },
                onReceive: function(events) {
                    // Parse and log calls
                    var parsedEvents = Stalker.parse(events);
                    callCount += parsedEvents.length;
                },
                transform: function(iterator) {
                    var instruction = iterator.next();

                    do {
                        // Instrument all CALL instructions
                        if (instruction.mnemonic === 'call') {
                            iterator.putCallout(function(context) {
                                var target = instruction.operands[0].value;
                                var symbol = DebugSymbol.fromAddress(target);

                                if (symbol.name && symbol.name.indexOf("crypto") !== -1) {
                                    console.log("  -> " + symbol.name);
                                }
                            });
                        }

                        iterator.keep();
                    } while ((instruction = iterator.next()) !== null);
                }
            });

            // Stop stalking after this function returns
            this.threadId = threadId;
        },
        onLeave: function(retval) {
            if (this.threadId) {
                console.log("[Stalker] Unfollowing thread " + this.threadId);
                Stalker.unfollow(this.threadId);
                Stalker.flush();
            }
        }
    });
}
```

### 💡 Pro Tips

**Tip 1: Använd frida-compile för större projekt**
```bash
# Installera frida-compile
npm install -g frida-compile

# Kompilera modulärt projekt till en fil
frida-compile main.js -o compiled.js

# Kör den kompilerade versionen
frida -U -f com.app -l compiled.js
```

**Tip 2: Debugging av Frida-scripts**
```javascript
// Aktivera verbose mode
Frida.version;  // Visa Frida-version

// Try-catch runt allt för att fånga fel
try {
    // Din kod här
} catch (e) {
    console.log("[ERROR] " + e.message);
    console.log(e.stack);  // Visa stack trace
}

// Använd debugger (pausar exekvering)
// debugger;  // Uncomment för att pausa
```

**Tip 3: Snabba iterationer med file watch**
```bash
# Använd nodemon eller liknande för att auto-reload
nodemon --watch script.js --exec "frida -U -f com.app -l script.js --no-pause"
```

**Tip 4: Spara output till fil**
```bash
# Logga all output till fil
frida -U -f com.app -l script.js --no-pause > output.log 2>&1

# Eller använd tee för både konsol och fil
frida -U -f com.app -l script.js --no-pause | tee output.log
```

**Tip 5: Remote debugging**
```javascript
// I ditt script, starta en RPC-server
rpc.exports = {
    getConfig: function() {
        return { version: "1.0", debug: true };
    },
    dumpMemory: function(addr, size) {
        return Memory.readByteArray(ptr(addr), size);
    }
};

// Från Python-klient:
import frida
device = frida.get_usb_device()
session = device.attach("com.app")
script = session.create_script(open("script.js").read())
script.load()

# Anropa RPC-funktioner
config = script.exports.get_config()
memory = script.exports.dump_memory("0x12345", 256)
```

### ✏️ Övningar

#### Övning 1: Designa ett Frida-script för bypass

**Scenario:** En app kontrollerar:
1. Om enheten är rootad (via `su`-fil)
2. Om den debuggas (via ptrace)
3. Om Frida finns (via sträng-sökning efter "frida")

Design ett komplett script som bypassar alla tre.

<details>
<summary>📝 Lösning</summary>

```javascript
console.log("[*] Loading comprehensive bypass...");

// 1. Root detection bypass
Java.perform(function() {
    // Bypass File.exists for su paths
    var File = Java.use("java.io.File");
    File.exists.implementation = function() {
        var path = this.getAbsolutePath();

        var rootPaths = ["/system/bin/su", "/system/xbin/su", "/sbin/su",
                         "/su/bin/su", "/magisk", "/data/adb"];

        for (var i = 0; i < rootPaths.length; i++) {
            if (path.indexOf(rootPaths[i]) !== -1) {
                console.log("[root] Hiding: " + path);
                return false;
            }
        }

        return this.exists();
    };

    console.log("[+] Root detection bypassed");
});

// 2. Debug detection bypass (ptrace)
var ptracePtr = Module.findExportByName("libc.so", "ptrace");
if (ptracePtr) {
    Interceptor.attach(ptracePtr, {
        onEnter: function(args) {
            this.request = args[0].toInt32();
        },
        onLeave: function(retval) {
            if (this.request === 0) {  // PTRACE_TRACEME
                console.log("[debug] Bypassed ptrace check");
                retval.replace(0);
            }
        }
    });
    console.log("[+] Debug detection bypassed");
}

// 3. Frida detection bypass (string search)
var stringFuncs = ["strstr", "strcasestr", "strcmp", "strcasecmp"];

stringFuncs.forEach(function(funcName) {
    var funcPtr = Module.findExportByName("libc.so", funcName);
    if (funcPtr) {
        Interceptor.attach(funcPtr, {
            onEnter: function(args) {
                this.arg0 = Memory.readCString(args[0]);
                this.arg1 = Memory.readCString(args[1]);
            },
            onLeave: function(retval) {
                var combined = (this.arg0 + this.arg1).toLowerCase();

                if (combined.indexOf("frida") !== -1) {
                    console.log("[frida] Blocked " + funcName + " search");

                    if (funcName.indexOf("str") === 0 && funcName.indexOf("cmp") !== -1) {
                        // strcmp family - return non-zero (not equal)
                        retval.replace(1);
                    } else {
                        // strstr family - return NULL (not found)
                        retval.replace(ptr(0));
                    }
                }
            }
        });
    }
});

console.log("[+] Frida detection bypassed");
console.log("[*] All bypasses ready!");
```

**Förklaring:**
1. Hookar `File.exists()` för att dölja su-binärer
2. Hookar `ptrace()` för att returnera success även om debugger är attachad
3. Hookar alla strängfunktioner för att förhindra att "frida" hittas
</details>

#### Övning 2: Analysera ett fiktivt anti-Frida-skydd

**Scenario:** En app har följande kod (pseudokod):

```c
void checkFrida() {
    FILE* maps = fopen("/proc/self/maps", "r");
    char line[512];

    while (fgets(line, sizeof(line), maps)) {
        if (strstr(line, "frida") != NULL) {
            exit(1);  // Kill app if Frida detected
        }
    }

    fclose(maps);
}
```

Hur skulle du bypassa detta med Frida? Ge minst två olika metoder.

<details>
<summary>📝 Lösning</summary>

**Metod 1: Hooka `fgets` och filtrera bort frida-rader**

```javascript
var fgetsPtr = Module.findExportByName("libc.so", "fgets");

Interceptor.attach(fgetsPtr, {
    onLeave: function(retval) {
        if (!retval.isNull()) {
            var line = Memory.readCString(retval);

            if (line.toLowerCase().indexOf("frida") !== -1) {
                console.log("[anti-frida] Filtered maps line containing 'frida'");

                // Ersätt med en oskadlig rad
                Memory.writeUtf8String(retval, "/system/lib/libc.so\n");
            }
        }
    }
});
```

**Metod 2: Hooka `strstr` för att returnera NULL vid "frida"-sök**

```javascript
var strstrPtr = Module.findExportByName("libc.so", "strstr");

Interceptor.attach(strstrPtr, {
    onEnter: function(args) {
        this.needle = Memory.readCString(args[1]);
    },
    onLeave: function(retval) {
        if (this.needle.toLowerCase() === "frida") {
            console.log("[anti-frida] Blocked strstr search for 'frida'");
            retval.replace(ptr(0));  // Return NULL
        }
    }
});
```

**Metod 3: Hooka `exit` för att förhindra att appen avslutas**

```javascript
var exitPtr = Module.findExportByName("libc.so", "exit");

Interceptor.attach(exitPtr, {
    onEnter: function(args) {
        var exitCode = args[0].toInt32();
        console.log("[anti-frida] Blocked exit(" + exitCode + ")");

        // Returnera istället för att avsluta
        this.context.pc = ptr(0);  // Skip exit (advanced!)
    }
});
```

**Bästa metoden:**
Metod 1 är mest robust eftersom den faktiskt filtrerar data som appen ser, istället för att bara förhindra detektionen.
</details>

#### Övning 3: Identifiera risker med att hooka system-API:er

**Fråga:** Vad kan gå fel om du hookar `malloc()` i en produktionsapp och loggar varje anrop?

<details>
<summary>📝 Svar</summary>

**Risker:**

1. **Performance-kollaps:**
   - `malloc()` anropas tusentals gånger per sekund
   - Varje logg-operation tar tid
   - Appen blir extremt långsam eller hänger

2. **Stack overflow:**
   - Din loggningskod kan själv anropa `malloc()`
   - Detta skapar rekursion: hook → log → malloc → hook → log → ...
   - Resultat: Stack overflow, krasch

3. **Race conditions:**
   - Om flera trådar anropar `malloc()` samtidigt
   - Och din hook-kod inte är thread-safe
   - Kan leda till data corruption

4. **Minnesdetektion:**
   - Att spara alla malloc-anrop kräver minne
   - Vilket leder till fler malloc-anrop
   - Minnesläckage eller out-of-memory

5. **Appen upptäcker manipulationen:**
   - Timing-anomalier (för långsamma malloc-anrop)
   - Ändrade returrädresser
   - Appen kan ha anti-tampering

**Lösningar:**

1. **Filtrera:**
   ```javascript
   // Logga BARA stora allokeringar
   if (size > 10000) {
       console.log("[malloc] Large: " + size);
   }
   ```

2. **Sammanfatta:**
   ```javascript
   // Räkna istället för att logga varje anrop
   mallocCount++;
   if (mallocCount % 1000 === 0) {
       console.log("[malloc] 1000 calls");
   }
   ```

3. **Asynkron logging:**
   ```javascript
   // Skicka till bakgrundstråd
   send({type: 'malloc', size: size});
   ```

4. **Använd CModule:**
   ```javascript
   // C-kod är mycket snabbare än JavaScript
   const cm = new CModule(`...`);
   ```
</details>

#### Övning 4: Designa en loggstruktur

**Uppgift:** Du bygger ett stort Frida-projekt som analyserar en komplex app. Designa en loggnings-strategi med:
- Olika loggnivåer (DEBUG, INFO, WARN, ERROR)
- Tydliga taggar per komponent
- Möjlighet att filtrera output

<details>
<summary>📝 Exempellösning</summary>

```javascript
/**
 * Structured Logging Framework for Frida
 */

var Logger = (function() {
    // Log levels
    var LEVELS = {
        DEBUG: 0,
        INFO: 1,
        WARN: 2,
        ERROR: 3
    };

    // Current log level (configurable)
    var currentLevel = LEVELS.INFO;

    // Color codes for console
    var COLORS = {
        DEBUG: '\x1b[36m',  // Cyan
        INFO: '\x1b[32m',   // Green
        WARN: '\x1b[33m',   // Yellow
        ERROR: '\x1b[31m',  // Red
        RESET: '\x1b[0m'
    };

    // Log buffer for analysis
    var logBuffer = [];
    var MAX_BUFFER_SIZE = 1000;

    function log(level, tag, message) {
        // Check if we should log this level
        if (LEVELS[level] < currentLevel) {
            return;
        }

        // Format timestamp
        var now = new Date();
        var timestamp = now.toISOString();

        // Format message
        var color = COLORS[level] || '';
        var reset = COLORS.RESET;
        var formatted = color + "[" + timestamp + "] [" + level + "] [" + tag + "] " + message + reset;

        // Output to console
        console.log(formatted);

        // Store in buffer
        logBuffer.push({
            timestamp: now.getTime(),
            level: level,
            tag: tag,
            message: message
        });

        // Trim buffer if too large
        if (logBuffer.length > MAX_BUFFER_SIZE) {
            logBuffer = logBuffer.slice(-MAX_BUFFER_SIZE);
        }
    }

    return {
        setLevel: function(level) {
            if (LEVELS[level] !== undefined) {
                currentLevel = LEVELS[level];
                this.info("Logger", "Log level set to: " + level);
            }
        },

        debug: function(tag, message) {
            log("DEBUG", tag, message);
        },

        info: function(tag, message) {
            log("INFO", tag, message);
        },

        warn: function(tag, message) {
            log("WARN", tag, message);
        },

        error: function(tag, message) {
            log("ERROR", tag, message);
        },

        getBuffer: function() {
            return logBuffer.slice();  // Return copy
        },

        clearBuffer: function() {
            logBuffer = [];
        },

        dumpBuffer: function() {
            console.log("\n=== LOG DUMP ===");
            logBuffer.forEach(function(entry) {
                console.log(entry.timestamp + " [" + entry.level + "] [" + entry.tag + "] " + entry.message);
            });
            console.log("=== END DUMP ===\n");
        }
    };
})();

// Export for use in other modules
if (typeof module !== 'undefined') {
    module.exports = Logger;
}

// Usage examples:
Logger.setLevel("DEBUG");

Logger.debug("Bypass", "Attempting to bypass root detection");
Logger.info("Hook", "Successfully hooked MainActivity.onCreate");
Logger.warn("Performance", "malloc() called 10000 times in 1 second");
Logger.error("Crash", "Segmentation fault detected at 0x12345678");

// Dump all logs
Logger.dumpBuffer();
```

**Fördelar med denna struktur:**
1. Konfigurerbar loggnivå
2. Färgkodad output för enkel läsning
3. Timestamps på alla loggar
4. Buffrad logging för senare analys
5. Tydliga taggar per komponent
6. Enkelt att utöka med fler features (fillogging, remote logging, etc.)
</details>

#### Övning 5: CTF Challenge - Reverse engineer en licenskontroll

**Scenario:** Du har en Android-app som kräver en licenskod. Appen har:
- En `checkLicense(String code)` metod
- En `activateApp()` metod som endast anropas om licenskontrollen lyckas
- Licensalgoritmen är okänd

Designa en Frida-strategi för att:
1. Hitta korrekt licenskod ELLER
2. Bypassa licenskontrollen helt

<details>
<summary>📝 Exempellösning</summary>

**Strategi 1: Hitta korrekt licenskod genom att logga jämförelser**

```javascript
Java.perform(function() {
    console.log("[*] License cracker starting...");

    // Method 1: Hook String.equals
    var String = Java.use("java.lang.String");
    String.equals.implementation = function(other) {
        var result = this.equals(other);
        var thisStr = this.toString();
        var otherStr = other ? other.toString() : "null";

        // Om en av strängarna ser ut som en licenskod
        if (thisStr.length > 10 || otherStr.length > 10) {
            console.log("[License] Comparing:");
            console.log("  This:  " + thisStr);
            console.log("  Other: " + otherStr);
            console.log("  Match: " + result);

            if (result) {
                console.log("[!!!] FOUND VALID LICENSE: " + thisStr);
            }
        }

        return result;
    };

    // Method 2: Hook checkLicense directly
    try {
        var MainActivity = Java.use("com.example.app.MainActivity");

        MainActivity.checkLicense.implementation = function(code) {
            console.log("[License] checkLicense called with: " + code);

            var result = this.checkLicense(code);

            console.log("[License] Result: " + result);

            if (result) {
                console.log("[!!!] VALID LICENSE: " + code);
            }

            return result;
        };
    } catch (e) {
        console.log("[-] Could not hook checkLicense: " + e);
    }

    console.log("[*] License cracker ready - enter codes in the app!");
});
```

**Strategi 2: Bypassa licenskontrollen helt**

```javascript
Java.perform(function() {
    console.log("[*] License bypass starting...");

    // Approach 1: Make checkLicense always return true
    try {
        var MainActivity = Java.use("com.example.app.MainActivity");

        MainActivity.checkLicense.implementation = function(code) {
            console.log("[License] checkLicense bypassed for code: " + code);
            return true;  // Always valid!
        };

        console.log("[+] Hooked checkLicense");
    } catch (e) {}

    // Approach 2: Call activateApp directly
    Java.choose("com.example.app.MainActivity", {
        onMatch: function(instance) {
            console.log("[*] Found MainActivity instance");

            try {
                instance.activateApp();
                console.log("[+] Called activateApp() directly!");
            } catch (e) {
                console.log("[-] Failed to call activateApp: " + e);
            }
        },
        onComplete: function() {}
    });

    // Approach 3: Hook SharedPreferences to fake activation
    var SharedPreferences = Java.use("android.content.SharedPreferences");
    SharedPreferences.getBoolean.implementation = function(key, defValue) {
        var result = this.getBoolean(key, defValue);

        if (key === "isActivated" || key === "isPremium" || key === "isLicensed") {
            console.log("[License] Faking preference: " + key + " = true");
            return true;
        }

        return result;
    };

    console.log("[*] License bypass ready!");
});
```

**Strategi 3: Reverse engineer algoritmen**

```javascript
Java.perform(function() {
    console.log("[*] License algorithm reverser starting...");

    // Hook alla stringoperationer för att förstå algoritmen
    var MessageDigest = Java.use("java.security.MessageDigest");
    MessageDigest.digest.overload("[B").implementation = function(input) {
        console.log("[Crypto] MessageDigest input: " + bytesToHex(input));

        var result = this.digest(input);

        console.log("[Crypto] MessageDigest output: " + bytesToHex(result));

        return result;
    };

    // Hook String transformations
    var String = Java.use("java.lang.String");

    String.substring.overload("int", "int").implementation = function(start, end) {
        var result = this.substring(start, end);
        console.log("[String] substring(" + start + ", " + end + "): " +
                    this.toString() + " -> " + result);
        return result;
    };

    String.toUpperCase.overload().implementation = function() {
        var result = this.toUpperCase();
        console.log("[String] toUpperCase: " + this.toString() + " -> " + result);
        return result;
    };

    // Helper function
    function bytesToHex(bytes) {
        var hex = [];
        for (var i = 0; i < bytes.length; i++) {
            hex.push(("0" + (bytes[i] & 0xFF).toString(16)).slice(-2));
        }
        return hex.join("");
    }

    console.log("[*] Algorithm reverser ready - enter test codes!");
});
```

**Best Practice:**
- Börja med Strategi 2 (bypass) - snabbast om du bara vill använda appen
- Använd Strategi 1 om du vill lära dig/dokumentera
- Använd Strategi 3 om du vill förstå algoritmen helt (för CTF eller research)
</details>

### 📝 Sammanfattning

**Key Takeaways från Nivå 4:**

- ✅ **Frida Stalker**: Kraftfullt verktyg för instruktionsnivå-tracing, men med hög overhead
- ✅ **Komplexa datastrukturer**: Hantera med Memory-API eller CModule för prestanda
- ✅ **Security bypasses**: Anti-debug, anti-Frida, SSL pinning, root detection - alla har motmedel
- ✅ **Projektstruktur**: Modulär design med separation of concerns för större projekt
- ✅ **Best practices**: Felhantering, performance-optimering, tydlig loggning
- ✅ **Anti-patterns**: Undvik överinstrumentering, blockerande operationer, otydlig kod
- ✅ **Etik & juridik**: ALLTID få tillstånd, följ lagar, använd ansvarsfull disclosure
- ✅ **Professional workflow**: Strukturerade projekt, versionskontroll, dokumentation

### Mini-ordlista

| Term | Förklaring |
|------|------------|
| **Stalker** | Fridas instruktionsnivå-tracer - följer varje CPU-instruktion |
| **JIT recompilation** | Just-In-Time omkompilering av kod för instrumentering |
| **CModule** | Inline C-kod i Frida för bättre prestanda |
| **SSL Pinning** | Säkerhetsmekanism som verifierar specifika certifikat |
| **Root Detection** | Appars försök att upptäcka rootade/jailbreakade enheter |
| **Anti-Debug** | Tekniker för att upptäcka debuggers/instrumentering |
| **Responsible Disclosure** | Etisk rapportering av sårbarheter till tillverkaren först |
| **Race Condition** | Bug när timing mellan trådar påverkar resultat |
| **Heap/Stack** | Olika minnesområden för dynamisk resp. lokal data |

### Koppling till nästa nivå

Du har nu avancerade Frida-kunskaper! I nästa nivå (Nivå 5: "Expert") går vi till **professionell användning**: integration med CI/CD, automation av analys, bygga återanvändbar tooling, kombinera Frida med andra verktyg (Burp Suite, Ghidra, radare2), prestandaprofilering, och hur Frida används i verkliga professionella sammanhang (malware-analys, pentesting, app-security). Du kommer också lära dig hur man bygger team-ramverk och bidrar till Frida-communityn!

**Redo för expertnivå? Nästa steg väntar! 💼**

---

## Nivå 5: "Expertnivå" 💼

### Introduktion

Välkommen till den sista nivån! Här lär du dig hur Frida används i **professionella sammanhang** av säkerhetsforskare, penetrationstestare och utvecklingsteam. Vi täcker **automation och CI/CD-integration**, hur man bygger **återanvändbara Frida-verktyg**, kombinerar Frida med andra verktyg i toolchains (Burp Suite, Ghidra, radare2), prestandaprofilering, och verkliga **use cases från industrin**. Du kommer också lära dig hur man bygger team-ramverk, bidrar till Frida-communityn, och håller dig uppdaterad med de senaste teknikerna. Detta är kulmen på din Frida-resa – från nybörjare till expert.

### Kärnkoncept

#### 1. Frida Python API för Automation

Medan JavaScript är hjärtat i Frida-scripts, är **Python API:et** nyckeln till automation och integration.

**Grundläggande Python API-användning:**

```python
import frida
import sys

# Anslut till enhet
device = frida.get_usb_device()  # USB-ansluten Android/iOS
# device = frida.get_local_device()  # Lokal dator
# device = frida.get_remote_device()  # Fjärrenhet

# Lista processer
processes = device.enumerate_processes()
for proc in processes:
    print(f"{proc.pid}: {proc.name}")

# Attach till process
session = device.attach("com.example.app")
# eller spawn:
# pid = device.spawn(["com.example.app"])
# session = device.attach(pid)
# device.resume(pid)

# Ladda JavaScript-script
with open("script.js") as f:
    script_code = f.read()

script = session.create_script(script_code)

# Hantera meddelanden från JavaScript
def on_message(message, data):
    if message['type'] == 'send':
        print(f"[*] {message['payload']}")
    elif message['type'] == 'error':
        print(f"[!] {message['stack']}")

script.on('message', on_message)
script.load()

# Håll scriptet levande
sys.stdin.read()
```

**Avancerat exempel - Batch-analys av flera appar:**

```python
import frida
import json
import time
from pathlib import Path

class FridaAnalyzer:
    def __init__(self, device_type='usb'):
        if device_type == 'usb':
            self.device = frida.get_usb_device()
        else:
            self.device = frida.get_local_device()

        self.results = []

    def analyze_app(self, package_name, script_path, timeout=30):
        """Analysera en app med ett givet script"""
        print(f"[*] Analyzing {package_name}...")

        try:
            # Spawn app
            pid = self.device.spawn([package_name])
            session = self.device.attach(pid)

            # Ladda script
            with open(script_path) as f:
                script_code = f.read()

            script = session.create_script(script_code)

            # Samla resultat
            app_results = {
                'package': package_name,
                'findings': [],
                'errors': []
            }

            def on_message(message, data):
                if message['type'] == 'send':
                    app_results['findings'].append(message['payload'])
                elif message['type'] == 'error':
                    app_results['errors'].append(message['stack'])

            script.on('message', on_message)
            script.load()

            # Resume app
            self.device.resume(pid)

            # Vänta för analys
            time.sleep(timeout)

            # Cleanup
            session.detach()

            self.results.append(app_results)
            print(f"[+] {package_name} analyzed successfully")

        except Exception as e:
            print(f"[!] Error analyzing {package_name}: {e}")
            self.results.append({
                'package': package_name,
                'error': str(e)
            })

    def analyze_batch(self, app_list, script_path):
        """Analysera flera appar i batch"""
        for package in app_list:
            self.analyze_app(package, script_path)
            time.sleep(2)  # Paus mellan appar

    def export_results(self, output_file):
        """Exportera resultat till JSON"""
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"[*] Results exported to {output_file}")

# Användning
if __name__ == "__main__":
    analyzer = FridaAnalyzer(device_type='usb')

    apps = [
        "com.example.app1",
        "com.example.app2",
        "com.example.app3"
    ]

    analyzer.analyze_batch(apps, "security_check.js")
    analyzer.export_results("analysis_results.json")
```

**RPC (Remote Procedure Call):**

```javascript
// I JavaScript (script.js)
rpc.exports = {
    getAppVersion: function() {
        return Java.perform(function() {
            var context = Java.use("android.app.ActivityThread")
                .currentApplication()
                .getApplicationContext();

            var packageManager = context.getPackageManager();
            var packageName = context.getPackageName();
            var packageInfo = packageManager.getPackageInfo(packageName, 0);

            return packageInfo.versionName.toString();
        });
    }
};
```

```python
# Anropa från Python
version = script.exports.get_app_version()
print(f"App version: {version}")
```

#### 2. CI/CD Integration

**GitHub Actions exempel:**

```yaml
# .github/workflows/frida-security-test.yml
name: Frida Security Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  security-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'

    - name: Install Frida
      run: |
        pip install frida frida-tools
        pip install -r requirements.txt

    - name: Run Security Tests
      run: |
        python tests/frida_security_tests.py

    - name: Upload Results
      uses: actions/upload-artifact@v2
      if: always()
      with:
        name: frida-test-results
        path: test-results/
```

#### 3. Professional Use Cases

**Malware Analysis Framework:**

```python
class MalwareAnalyzer:
    """Automatiserad malware-analys med Frida"""

    def __init__(self, sample_path):
        self.sample_path = sample_path
        self.device = frida.get_local_device()
        self.behavioral_data = {
            'file_operations': [],
            'network_activity': [],
            'process_creation': []
        }

    def analyze(self, timeout=60):
        """Kör malware och analysera beteende"""
        pid = self.device.spawn([self.sample_path])
        session = self.device.attach(pid)

        script_code = """
        // Hook file operations
        var CreateFileW = Module.findExportByName('kernel32.dll', 'CreateFileW');
        Interceptor.attach(CreateFileW, {
            onEnter: function(args) {
                var filename = args[0].readUtf16String();
                send({
                    type: 'file_operation',
                    operation: 'CreateFile',
                    filename: filename,
                    timestamp: Date.now()
                });
            }
        });

        // Hook network activity
        var connect = Module.findExportByName('ws2_32.dll', 'connect');
        Interceptor.attach(connect, {
            onEnter: function(args) {
                var sockaddr = args[1];
                // Parse och skicka data
                send({
                    type: 'network_activity',
                    operation: 'connect'
                });
            }
        });
        """

        script = session.create_script(script_code)

        def on_message(message, data):
            if message['type'] == 'send':
                payload = message['payload']
                event_type = payload['type']
                self.behavioral_data[event_type].append(payload)

        script.on('message', on_message)
        script.load()
        self.device.resume(pid)

        time.sleep(timeout)
        session.detach()

        return self.generate_report()

    def generate_report(self):
        """Generera analyrapport"""
        return {
            'sample': self.sample_path,
            'summary': {
                'file_operations': len(self.behavioral_data['file_operations']),
                'network_connections': len(self.behavioral_data['network_activity'])
            },
            'details': self.behavioral_data
        }
```

### 💡 Pro Tips

**Tip 1: Bygg återanvändbara moduler**

```
frida-toolkit/
├── bypasses/
│   ├── ssl_pinning.js
│   ├── root_detection.js
│   └── anti_frida.js
├── hooks/
│   ├── networking.js
│   └── crypto.js
└── utils/
    └── logger.js
```

**Tip 2: Dokumentera för team**

```javascript
/**
 * SSL Pinning Bypass Module
 * @description Universal SSL pinning bypass
 * @author Your Name
 * @version 1.2.0
 */
```

**Tip 3: Versionshantering**

```bash
git init frida-project
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
git add .
git commit -m "Initial commit"
```

### 📝 Sammanfattning

**Key Takeaways från Nivå 5:**

- ✅ **Python API**: Automation och batch-analys
- ✅ **CI/CD**: Automated security testing
- ✅ **Professional Use**: Malware-analys, pentesting
- ✅ **Reusability**: Bygg bibliotek av komponenter
- ✅ **Documentation**: Dokumentera för team
- ✅ **Community**: Dela kunskap och bidra

---

## 🎓 Slutlig Självutvärdering

Testa din Frida-kunskap:

### Nybörjare (Nivå 1-2)
- [ ] Förklara dynamic instrumentation
- [ ] Installera Frida
- [ ] Lista processer med `frida-ps`
- [ ] Förstå attach vs spawn

### Mellanstadiet (Nivå 3)
- [ ] Skriva enkelt Frida-script
- [ ] Hooka native-funktion
- [ ] Hooka Java-metod
- [ ] Läsa argument/returvärden

### Avancerat (Nivå 4)
- [ ] Bypassa SSL pinning
- [ ] Bypassa root detection
- [ ] Använda Stalker
- [ ] Strukturera större projekt

### Expert (Nivå 5)
- [ ] Python API automation
- [ ] CI/CD-integration
- [ ] Professionell malware-analys
- [ ] Profilera scripts
- [ ] Bidra till open source

---

## 📖 Ordlista

**API**: Application Programming Interface
**Attach**: Koppla till körande process
**Bypass**: Kringgå säkerhetsskydd
**CI/CD**: Continuous Integration/Deployment
**Hook**: Avlyssnare på funktion
**Inject**: Skjuta in kod i process
**Native**: C/C++ kod
**RPC**: Remote Procedure Call
**Spawn**: Starta process med Frida
**Stalker**: Instruktions-tracer

---

## 🔗 Resurser för Fördjupning

### Officiella
- **Frida Hemsida**: https://frida.re/
- **Dokumentation**: https://frida.re/docs/
- **GitHub**: https://github.com/frida/frida

### Community
- **Frida CodeShare**: https://codeshare.frida.re/
- **Frida Discord**: Officiell community
- **GitHub Discussions**: Frågor & svar

### Tutorials
- **Frida HandBook**: https://learnfrida.info/
- **OWASP MASTG**: Mobile security testing
- **8kSec**: Avancerade tutorials

### Verktyg
- **Objection**: Frida-baserat testing framework
- **r2frida**: radare2 + Frida
- **Dwarf**: GUI-debugger med Frida

---

## ❓ Vanliga Frågor (FAQ)

**Q: Är Frida lagligt?**
A: Ja, men använd endast på egna system eller med tillstånd.

**Q: Fungerar det utan root/jailbreak?**
A: Delvis - använd frida-gadget inbäddad i app.

**Q: Hur uppdaterar jag?**
A: `pip install --upgrade frida-tools`

**Q: Varför kraschar appen?**
A: Kontrollera hooks, anti-Frida, eller buggar i script.

**Q: Hur bidrar jag till Frida?**
A: GitHub Issues, Pull Requests, CodeShare, dokumentation.

---

## 🎉 Grattis!

Du har genomfört **Frida - Den Kompletta Guiden**!

### Din resa
- 👶 Nivå 1: Grundkoncept
- 🧒 Nivå 2: Grundtermer
- 🎓 Nivå 3: Första hooks
- 🏛️ Nivå 4: Avancerade tekniker
- 💼 Nivå 5: Expert

### Nästa steg
1. **Öva**: Bygg labbmiljö
2. **Bygg**: Skapa egna verktyg
3. **Dela**: Bidra till community
4. **Lär ut**: Hjälp andra
5. **Fördjupa**: Specialisera dig

### Sista rådet

**Med stor makt kommer stort ansvar.**

Använd alltid Frida:
- ✅ Etiskt
- ✅ Lagligt
- ✅ Med tillstånd
- ✅ För att göra världen säkrare

**Lycka till på din fortsatta Frida-resa! 🚀**

---

*Guide skapad: 2025*
*Frida Version: 17.4.x*
*Uppdaterad regelbundet*

---

# 🎁 BONUSNIVÅ: Kali Linux + Ghidra + Frida - Den Ultimata Triaden

## 🎯 Introduktion

Välkommen till bonusnivån! Här undersöker vi hur tre kraftfulla verktyg kombineras för professionell reverse engineering och säkerhetsanalys:

- **Kali Linux**: Den kompletta säkerhetsplattformen
- **Ghidra**: NSA:s statiska analysverktyg
- **Frida**: Dynamisk instrumentering

**Varför dessa tre tillsammans?**

```
┌─────────────────────────────────────────────────────────┐
│              REVERSE ENGINEERING WORKFLOW                │
└─────────────────────────────────────────────────────────┘

    Kali Linux
    ┌──────────────────────────────────────┐
    │  Säker miljö för analys              │
    │  Alla verktyg förinstallerade        │
    │  Isolerad från produktion            │
    └──────────────────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼

    GHIDRA                  FRIDA
    ┌──────────────┐       ┌──────────────┐
    │ Statisk      │       │ Dynamisk     │
    │ Analys       │◄─────►│ Analys       │
    │              │       │              │
    │ • Disassembly│       │ • Runtime    │
    │ • Decompile  │       │ • Hooking    │
    │ • CFG        │       │ • Tracing    │
    └──────────────┘       └──────────────┘
         │                       │
         └───────────┬───────────┘
                     ▼
              Complete Picture
              ┌──────────────┐
              │ Funktionalitet
              │ Sårbarheter
              │ Lösenord/nycklar
              │ Nätverkstrafik
              └──────────────┘
```

**Workflow**:
1. **Ghidra**: Statisk analys → hitta intressanta funktioner
2. **Frida**: Dynamisk analys → verifiera beteende runtime
3. **Ghidra**: Tillbaka för djupare förståelse
4. **Frida**: Testa hypoteser live

---

## 🔧 Del 1: Installation och Setup på Kali Linux

### Steg 1: Installera Kali Linux

**Alternativ A: Virtuell Maskin (rekommenderat för övning)**

```bash
# Ladda ner från https://www.kali.org/get-kali/
# Importera .ova-fil i VirtualBox/VMware
```

**Alternativ B: Dual Boot**

```bash
# Skapa bootbar USB med Rufus/Etcher
# Installera från USB
```

**Alternativ C: WSL (Windows)**

```bash
# I Windows PowerShell (Admin)
wsl --install -d kali-linux
```

### Steg 2: Uppdatera Kali

```bash
sudo apt update
sudo apt upgrade -y
sudo apt dist-upgrade -y
```

### Steg 3: Installera Ghidra

```bash
# Installera Java (Ghidra kräver JDK 17+)
sudo apt install -y openjdk-17-jdk

# Ladda ner Ghidra
cd ~/Downloads
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.2_build/ghidra_11.2_PUBLIC_20250107.zip

# Extrahera
unzip ghidra_11.2_PUBLIC_20250107.zip -d ~/tools/
cd ~/tools/ghidra_11.2_PUBLIC

# Starta Ghidra
./ghidraRun
```

**Alternativ: Via apt (äldre version)**

```bash
sudo apt install -y ghidra
```

### Steg 4: Installera Frida

```bash
# Python och pip
sudo apt install -y python3-pip python3-dev

# Frida
sudo pip3 install frida-tools frida

# Verifiera installation
frida --version
```

### Steg 5: Installera Kompletterande Verktyg

```bash
# ADB för Android
sudo apt install -y adb

# Networking tools
sudo apt install -y wireshark burpsuite

# Binary analysis
sudo apt install -y radare2 gdb

# ghidra2frida bridge (viktigt!)
pip3 install ghidra2frida
```

---

## 🧪 Del 2: Första Integrerade Analysen

### Scenario: Analysera Android APK

**Mål**: Förstå och bypassa en Android app's autentisering

#### Fas 1: Ghidra - Statisk Analys

**Steg 1: Förbered APK**

```bash
# Extrahera APK
mkdir analysis
cd analysis
unzip target-app.apk

# Hitta DEX-filer
ls *.dex
# Output: classes.dex, classes2.dex
```

**Steg 2: Konvertera DEX till JAR för Ghidra**

```bash
# Installera dex2jar
sudo apt install -y dex2jar

# Konvertera
d2j-dex2jar classes.dex
# Output: classes-dex2jar.jar
```

**Steg 3: Öppna i Ghidra**

```bash
# Starta Ghidra
ghidraRun &

# I Ghidra:
# File → Import File → classes-dex2jar.jar
# Analyze → Yes (auto-analyze)
```

**Steg 4: Sök efter intressanta funktioner**

I Ghidra's Symbol Tree:
- Sök efter: `checkPassword`, `authenticate`, `validateUser`
- Dubbelklicka på funktion för decompilation

**Exempel på hittad funktion:**

```java
// Ghidra decompilation output
public boolean checkPassword(String password) {
    String correctPassword = getStoredPassword();
    if (password.equals(correctPassword)) {
        return true;
    }
    return false;
}

private String getStoredPassword() {
    return Native.getEncryptedPassword();
}
```

**Insikter från Ghidra:**
- ✓ `checkPassword` finns i `com.target.app.AuthManager`
- ✓ Anropar native metod `getEncryptedPassword`
- ✓ Använder simple `equals()` jämförelse

#### Fas 2: Frida - Dynamisk Verifiering

**Steg 1: Starta app och Frida**

```bash
# Anslut Android device
adb devices

# Starta frida-server på device
adb shell "su -c /data/local/tmp/frida-server &"

# Lista processer
frida-ps -Uai
```

**Steg 2: Hooka `checkPassword`**

```bash
frida -U -f com.target.app -l hook.js --no-pause
```

**hook.js:**

```javascript
Java.perform(function() {
    console.log("[*] Starting hooks...");

    // Hook checkPassword
    var AuthManager = Java.use("com.target.app.AuthManager");

    AuthManager.checkPassword.implementation = function(password) {
        console.log("[+] checkPassword called!");
        console.log("[+] Input password: " + password);

        // Anropa original
        var result = this.checkPassword(password);
        console.log("[+] Original result: " + result);

        // Logga getStoredPassword
        var storedPw = this.getStoredPassword();
        console.log("[!] Stored password: " + storedPw);

        return result;
    };

    // Hook native funktion
    var Native = Java.use("com.target.app.Native");

    Native.getEncryptedPassword.implementation = function() {
        var result = this.getEncryptedPassword();
        console.log("[!] Native password: " + result);
        return result;
    };

    console.log("[*] Hooks installed!");
});
```

**Kör app och ange fel lösenord:**

```
[*] Starting hooks...
[*] Hooks installed!
[+] checkPassword called!
[+] Input password: wrongpass
[!] Native password: s3cr3tP@ssw0rd
[!] Stored password: s3cr3tP@ssw0rd
[+] Original result: false
```

**💎 Upptäckt: Lösenordet är `s3cr3tP@ssw0rd`**

#### Fas 3: Tillbaka till Ghidra

Nu när vi vet lösenordet, gå tillbaka till Ghidra:

**Analysera `Native.getEncryptedPassword()`:**

```bash
# I Ghidra, sök efter native library
# File → classes.dex → native-lib.so
```

**I Ghidra disassembly:**

```c
// Pseudo-code från native funktion
char* Java_com_target_app_Native_getEncryptedPassword(JNIEnv *env, jobject obj) {
    char *encrypted = "\x73\x33\x63\x72\x33\x74\x50\x40\x73\x73\x77\x30\x72\x64";
    return (*env)->NewStringUTF(env, encrypted);
}
```

**Insikt**: Lösenordet är hårdkodat i binären! (Dålig praxis)

#### Fas 4: Frida - Bypassa helt

Nu med fullständig förståelse, skriv bypass:

```javascript
Java.perform(function() {
    var AuthManager = Java.use("com.target.app.AuthManager");

    // Simpel bypass - returnera alltid true
    AuthManager.checkPassword.implementation = function(password) {
        console.log("[*] Bypassing authentication!");
        return true;  // Alltid godkänd
    };

    console.log("[+] Authentication bypassed!");
});
```

**Resultat**: Logga in med vilket lösenord som helst!

---

## 🔗 Del 3: ghidra2frida - Bron mellan verktygen

**ghidra2frida** är en kraftfull integration som låter dig:
- Exportera Ghidra-analys till Frida-script
- Automatgenerera hooks från Ghidra-funktioner
- Synkronisera mellan statisk och dynamisk analys

### Installation

```bash
pip3 install ghidra2frida

# Installera Ghidra-plugin
cd ~/tools/ghidra_11.2_PUBLIC/Extensions
git clone https://github.com/federicodotta/ghidra2frida.git
```

### Användning

**I Ghidra:**

1. Högerklicka på funktion → "Generate Frida Hook"
2. Välj hook-typ (enter, leave, replace)
3. Kopiera genererad JavaScript

**Exempel:**

Ghidra-funktion:
```c
int verify_license(char *key, int length)
```

Genererad Frida-hook:
```javascript
// Auto-generated by ghidra2frida
Interceptor.attach(Module.findExportByName("libapp.so", "verify_license"), {
    onEnter: function(args) {
        console.log("[verify_license]");
        console.log("  key: " + Memory.readUtf8String(args[0]));
        console.log("  length: " + args[1]);
    },
    onLeave: function(retval) {
        console.log("  return: " + retval);
    }
});
```

**Workflow:**

```
┌──────────────┐
│   Ghidra     │
│   Analys     │
└──────┬───────┘
       │ 1. Identifiera funktioner
       │ 2. Förstå logik
       │ 3. Märk intressanta delar
       ▼
┌──────────────┐
│ ghidra2frida │
│    Bridge    │
└──────┬───────┘
       │ 4. Generera hooks
       │ 5. Exportera script
       ▼
┌──────────────┐
│    Frida     │
│   Runtime    │
└──────┬───────┘
       │ 6. Verifiera runtime
       │ 7. Extrahera data
       ▼
┌──────────────┐
│  Uppdatera   │
│   förståelse │
│  i Ghidra    │
└──────────────┘
```

---

## 💼 Del 4: Avancerade Use Cases

### Use Case 1: Malware-analys

**Scenario**: Analysera okänd Windows-binär

**Kali Setup:**

```bash
# Installera Wine för Windows-binärer
sudo apt install -y wine wine64

# Installera PE-verktyg
sudo apt install -y pev
```

**Workflow:**

```bash
# 1. Grundläggande PE-analys
readpe malware.exe
pescan malware.exe

# 2. Ghidra statisk analys
ghidraRun malware.exe

# 3. Identifiera i Ghidra:
#    - Entry point
#    - Imported functions (CreateProcess, RegSetValue)
#    - Strings (C2 server URLs)
#    - Encrypted data

# 4. Kör i Wine med Frida
frida -f "wine malware.exe" -l malware_hooks.js
```

**malware_hooks.js:**

```javascript
// Hook dangerous Windows APIs
Interceptor.attach(Module.findExportByName("kernel32.dll", "CreateProcessW"), {
    onEnter: function(args) {
        var cmdline = Memory.readUtf16String(args[1]);
        console.log("[!] CreateProcess: " + cmdline);
        send({type: "process_creation", cmdline: cmdline});
    }
});

// Hook network connections
Interceptor.attach(Module.findExportByName("ws2_32.dll", "connect"), {
    onEnter: function(args) {
        // Parse sockaddr structure
        var sockaddr = args[1];
        var port = Memory.readU16(sockaddr.add(2));
        console.log("[!] Network connection to port: " + port);
        send({type: "network", port: port});
    }
});

// Hook registry modifications
Interceptor.attach(Module.findExportByName("advapi32.dll", "RegSetValueExW"), {
    onEnter: function(args) {
        var valueName = Memory.readUtf16String(args[1]);
        console.log("[!] Registry write: " + valueName);
        send({type: "registry", value: valueName});
    }
});
```

**Python orchestration:**

```python
import frida
import sys

behavioral_log = []

def on_message(message, data):
    if message['type'] == 'send':
        behavioral_log.append(message['payload'])
        print(f"[Behavior] {message['payload']}")

session = frida.attach("wine")

with open("malware_hooks.js") as f:
    script = session.create_script(f.read())

script.on('message', on_message)
script.load()

# Låt malware köra i 60 sekunder
import time
time.sleep(60)

# Generera rapport
print("\n=== BEHAVIORAL REPORT ===")
for event in behavioral_log:
    print(f"- {event['type']}: {event}")
```

### Use Case 2: iOS App-analys

**Setup:**

```bash
# Jailbroken iOS device krävs
# Installera Frida på iOS via Cydia/Sileo

# Anslut via USB
iproxy 2222 22
ssh root@localhost -p 2222

# På iOS device
apt install frida
```

**Workflow:**

**1. Dumpa iOS app från device:**

```bash
# På Kali
frida-ps -Uai | grep "Target App"

# Dumpa decrypted binary
bagbak --target-app com.target.app
```

**2. Ghidra-analys:**

```bash
# Importera decrypted IPA i Ghidra
unzip target-app.ipa
ghidraRun Payload/TargetApp.app/TargetApp
```

**3. Identifiera Objective-C klasser:**

I Ghidra:
- Sök efter `_OBJC_CLASS_$_`
- Leta efter metoder: `+[Class method]`, `-[Class instance]`

**4. Frida hooks:**

```javascript
// Hook Objective-C metod
if (ObjC.available) {
    var ViewController = ObjC.classes.ViewController;

    Interceptor.attach(ViewController['- validatePurchase:'].implementation, {
        onEnter: function(args) {
            console.log("[*] validatePurchase called");
            // args[0] = self
            // args[1] = selector
            // args[2] = första argument
            var purchase = new ObjC.Object(args[2]);
            console.log("[*] Purchase: " + purchase.toString());
        },
        onLeave: function(retval) {
            console.log("[*] Original return: " + retval);
            retval.replace(0x1);  // Ändra till true
        }
    });
}
```

### Use Case 3: Automatiserad Säkerhetsaudit

**Kombination av alla tre verktyg:**

```python
#!/usr/bin/env python3
"""
Automatiserad security audit pipeline
Kali + Ghidra + Frida
"""

import subprocess
import frida
import json
import os

class SecurityAudit:
    def __init__(self, apk_path):
        self.apk_path = apk_path
        self.results = {
            'static': {},
            'dynamic': {}
        }

    def static_analysis(self):
        """Ghidra headless-analys"""
        print("[*] Running Ghidra analysis...")

        ghidra_cmd = [
            "analyzeHeadless",
            "/tmp/ghidra_projects",
            "AuditProject",
            "-import", self.apk_path,
            "-postScript", "ExportFunctions.py",
            "-scriptPath", "./ghidra_scripts"
        ]

        result = subprocess.run(ghidra_cmd, capture_output=True)

        # Parse Ghidra output
        with open("/tmp/ghidra_output.json") as f:
            self.results['static'] = json.load(f)

        return self.results['static']

    def dynamic_analysis(self, package_name):
        """Frida runtime-analys"""
        print("[*] Running Frida analysis...")

        device = frida.get_usb_device()
        pid = device.spawn([package_name])
        session = device.attach(pid)

        with open("audit_hooks.js") as f:
            script = session.create_script(f.read())

        script.on('message', self.on_message)
        script.load()
        device.resume(pid)

        # Kör app i 120 sekunder
        import time
        time.sleep(120)

        return self.results['dynamic']

    def on_message(self, message, data):
        if message['type'] == 'send':
            payload = message['payload']
            category = payload.get('category', 'general')

            if category not in self.results['dynamic']:
                self.results['dynamic'][category] = []

            self.results['dynamic'][category].append(payload)

    def generate_report(self):
        """Generera HTML-rapport"""
        html = f"""
        <html>
        <head><title>Security Audit Report</title></head>
        <body>
            <h1>Security Audit: {os.path.basename(self.apk_path)}</h1>

            <h2>Static Analysis (Ghidra)</h2>
            <ul>
                <li>Functions analyzed: {len(self.results['static'].get('functions', []))}</li>
                <li>Vulnerabilities: {len(self.results['static'].get('vulns', []))}</li>
            </ul>

            <h2>Dynamic Analysis (Frida)</h2>
            <ul>
                <li>Network calls: {len(self.results['dynamic'].get('network', []))}</li>
                <li>File operations: {len(self.results['dynamic'].get('file', []))}</li>
                <li>Crypto operations: {len(self.results['dynamic'].get('crypto', []))}</li>
            </ul>

            <h2>Findings</h2>
            {self.generate_findings()}
        </body>
        </html>
        """

        with open("audit_report.html", "w") as f:
            f.write(html)

        print("[+] Report generated: audit_report.html")

    def generate_findings(self):
        findings = []

        # Check for hardcoded secrets (från Ghidra)
        if 'hardcoded_strings' in self.results['static']:
            for string in self.results['static']['hardcoded_strings']:
                if any(keyword in string.lower() for keyword in ['password', 'api_key', 'secret']):
                    findings.append(f"<li>⚠️ Hardcoded secret: {string}</li>")

        # Check for insecure network (från Frida)
        if 'network' in self.results['dynamic']:
            for call in self.results['dynamic']['network']:
                if call.get('protocol') == 'http':
                    findings.append(f"<li>⚠️ Insecure HTTP: {call['url']}</li>")

        return "<ul>" + "".join(findings) + "</ul>"

# Användning
if __name__ == "__main__":
    audit = SecurityAudit("target-app.apk")

    # Fas 1: Statisk analys
    audit.static_analysis()

    # Fas 2: Dynamisk analys
    audit.dynamic_analysis("com.target.app")

    # Fas 3: Rapport
    audit.generate_report()
```

---

## 🎯 Del 5: Best Practices

### Workflow Best Practices

**1. Börja alltid med statisk analys (Ghidra)**

```
Fördelar:
✓ Snabbt - ingen runtime overhead
✓ Komplett bild av all kod
✓ Hitta low-hanging fruit (hardcoded secrets)
✓ Planera Frida-hooks
```

**2. Använd Frida för verifiering**

```
Fördelar:
✓ Se faktiskt beteende
✓ Bypass obfuscation
✓ Extrahera runtime-data
✓ Testa hypoteser
```

**3. Iterera mellan båda**

```
Ghidra → Frida → Ghidra → Frida
  │        │        │        │
  │        │        │        └─ Slutgiltig bypass
  │        │        └────────── Djupare analys
  │        └─────────────────── Verifiera upptäckter
  └──────────────────────────── Initial kartläggning
```

### Säkerhet i Kali-miljö

**Isolering:**

```bash
# Kör analys i separat VM
# ALDRIG på produktionssystem

# Använd snapshots
VBoxManage snapshot "Kali-Analysis" take "Clean State"

# Network isolation
iptables -A OUTPUT -j DROP  # Block all outbound för malware-analys
```

**Dokumentation:**

```bash
# Logga allt
script analysis_session.log

# Git för projekt
git init malware-analysis-2025-01-15
git add .
git commit -m "Initial findings"
```

### Performance Tips

**Ghidra:**

```bash
# Ge Ghidra mer minne
# I ghidraRun script:
MAXMEM=8G
```

**Frida:**

```javascript
// Undvik överflödiga hooks
// BAD:
Interceptor.attach(Module.findExportByName(null, "malloc"), ...);

// GOOD: Specifika targets
Interceptor.attach(Module.findExportByName("libapp.so", "sensitive_func"), ...);
```

---

## 📝 Övningar

### Övning 1: Grundläggande Integration

**Mål**: Analysera en enkel Android APK

**Steg**:
1. Ladda ner övnings-APK: `https://github.com/OWASP/crackmes` (InsecureBankv2)
2. Öppna i Ghidra och hitta `doLogin` metoden
3. Skriv Frida-hook för att logga användarnamn/lösenord
4. Bygg bypass baserat på Ghidra-analys

**Lösning**:

<details>
<summary>Klicka för lösning</summary>

```javascript
Java.perform(function() {
    var DoLogin = Java.use("com.android.insecurebankv2.DoLogin");

    // Hook från Ghidra-analys
    DoLogin.performLogin.implementation = function(username, password) {
        console.log("[*] Login attempt:");
        console.log("    Username: " + username);
        console.log("    Password: " + password);

        // Ghidra visade hårdkodat check
        // Bypassa helt
        return true;
    };
});
```

</details>

### Övning 2: Native Library-analys

**Mål**: Analysera native library i APK

**Steg**:
1. Hitta `libnative-lib.so` i APK
2. Öppna i Ghidra och analysera `JNI_OnLoad`
3. Identifiera nativ funktion som anropas från Java
4. Hooka med Frida och extrahera data

**Lösning**:

<details>
<summary>Klicka för lösning</summary>

```javascript
// Från Ghidra: funktionen heter "stringFromJNI"
Interceptor.attach(Module.findExportByName("libnative-lib.so", "Java_com_example_app_MainActivity_stringFromJNI"), {
    onEnter: function(args) {
        console.log("[*] stringFromJNI called");
        // args[0] = JNIEnv*
        // args[1] = jobject
    },
    onLeave: function(retval) {
        var result = Java.vm.getEnv().getStringUtfChars(retval, null);
        console.log("[*] Returned: " + result.readCString());
    }
});
```

</details>

### Övning 3: Automatiserad Audit

**Mål**: Bygg automated audit-script

**Steg**:
1. Använd Ghidra headless mode
2. Extrahera alla metod-namn
3. Generera Frida-hooks automatiskt för alla metoder
4. Kör och logga alla anrop

**Lösning**:

<details>
<summary>Klicka för lösning</summary>

**ghidra_export.py** (Ghidra script):
```python
# Kör i Ghidra
from ghidra.program.model.listing import Function

functions = currentProgram.getFunctionManager().getFunctions(True)

output = []
for func in functions:
    output.append({
        'name': func.getName(),
        'address': str(func.getEntryPoint())
    })

# Spara till fil
import json
with open('/tmp/functions.json', 'w') as f:
    json.dump(output, f)
```

**generate_hooks.py**:
```python
import json

with open('/tmp/functions.json') as f:
    functions = json.load(f)

hooks = []
for func in functions:
    hook = f"""
Interceptor.attach(ptr("{func['address']}"), {{
    onEnter: function(args) {{
        console.log("[{func['name']}] called");
    }}
}});
"""
    hooks.append(hook)

with open('auto_hooks.js', 'w') as f:
    f.write("\n".join(hooks))
```

</details>

---

## 🎓 Sammanfattning

**Key Takeaways från Bonusnivån:**

✅ **Kali Linux**: Säker, isolerad miljö med alla verktyg
✅ **Ghidra**: Statisk analys för att förstå struktur
✅ **Frida**: Dynamisk verifiering av runtime-beteende
✅ **Integration**: Iterativ process mellan statisk och dynamisk
✅ **ghidra2frida**: Bro för automatisering
✅ **Automation**: Python för att orkestrera hela pipeline

**Workflow**:
```
1. Ghidra:  Kartlägg applikationen
2. Frida:   Verifiera runtime-beteende
3. Ghidra:  Fördjupa förståelse
4. Frida:   Bygg exploits/bypasses
5. Repeat:  Iterera tills målet är uppnått
```

**Verktygskombo för olika scenarion**:

| Scenario              | Ghidra | Frida | Extra verktyg        |
|-----------------------|--------|-------|----------------------|
| Android APK           | ✓      | ✓     | apktool, jadx        |
| iOS App               | ✓      | ✓     | bagbak, Hopper       |
| Windows Malware       | ✓      | ✓     | Wine, PE tools       |
| Linux Binary          | ✓      | ✓     | radare2, GDB         |
| Web API Reverse       | ✗      | ✓     | Burp Suite, mitmproxy|

---

## 🚀 Nästa Steg

**Fortsatt Lärande:**

1. **OWASP Mobile Security Testing Guide (MASTG)**
   - https://mas.owasp.org/MASTG/
   - Komplett guide för mobil säkerhetstestning

2. **Ghidra Documentation**
   - https://ghidra-sre.org/
   - Officiella tutorials och kurser

3. **Frida CodeShare**
   - https://codeshare.frida.re/
   - Community-script för alla scenarion

4. **Praktisk övning**
   - HackTheBox mobila challenges
   - OWASP Crackmes
   - Root-Me challenges

**Community:**

- **Discord**: Ghidra & Frida communities
- **GitHub**: Bidra med scripts och verktyg
- **Conferences**: DEF CON, Black Hat, OWASP events

---

## 🎉 Slutord

Du har nu den ultimata triaden för reverse engineering:

```
┌─────────────────────────────────────┐
│     Kali Linux + Ghidra + Frida     │
│                                     │
│  Statisk ←→ Dynamisk ←→ Automation  │
│                                     │
│     Professional Security Audit      │
└─────────────────────────────────────┘
```

**Använd denna kraft:**
- ✅ Etiskt
- ✅ Lagligt
- ✅ För säkerhetsforskning
- ✅ Med tillstånd

**Med dessa tre verktyg kan du:**
- Upptäcka sårbarheter
- Reverse engineera mjukvara
- Analysera malware
- Bypassa skydd (i labs!)
- Bygga säkrare system

**Lycka till på din fortsatta resa! 🔐🚀**

---

*Bonusnivå skapad: 2025*
*Ghidra Version: 11.2*
*Frida Version: 17.4.x*
*Kali Linux: 2025.x*

---

# 🎯 BONUSUPPGIFT: Red Team vs Blue Team - Internal Bug Bounty

## 🏴‍☠️ Scenario: Warp Terminal Payment Bypass Challenge

**Kontext**: Ditt företag har utvecklat en premium terminal-applikation kallad "Warp Console" med följande features:
- Free tier: Grundläggande funktionalitet
- Premium tier: AI-assistans, team-collaboration, themes

**Bug Bounty Mission**: Internal security team har startat en kontrollerad övning där:
- **Red Team**: Ska försöka kringgå premium-betalningen
- **Blue Team**: Ska hitta och patcha sårbarheten

**Regler**:
- ✅ Endast på test-instans
- ✅ Dokumentera alla fynd
- ✅ Dela resultat med Blue Team
- ❌ ALDRIG på produktion
- ❌ ALDRIG dela exploits publikt

---

## 🔴 DEL 1: RED TEAM - Pedagogiskt Facit

### Fas 1: Reconnaissance (Spaning)

**Mål**: Förstå applikationens arkitektur och hitta betalningslogik

#### Steg 1.1: Initial Analys

```bash
# Lista processer
frida-ps | grep -i warp
# Output: 12345 Warp Console

# Inspektera med strings
strings /usr/bin/warp-console | grep -i "premium\|license\|payment"
# Output:
# checkPremiumStatus
# validateLicense
# https://api.warp.dev/v1/verify-subscription
```

**Fynd**: Appen verkar ha funktioner för premium-kontroll och licensvalidering.

#### Steg 1.2: Nätverksanalys

```bash
# Proxya trafik genom mitmproxy
mitmproxy -p 8080

# Konfigurera Warp att använda proxy
export HTTP_PROXY=http://localhost:8080
export HTTPS_PROXY=http://localhost:8080

# Starta Warp
/usr/bin/warp-console
```

**Observerat nätverksanrop:**

```http
GET /v1/verify-subscription HTTP/1.1
Host: api.warp.dev
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
User-Agent: WarpConsole/1.2.0

Response:
{
  "premium": false,
  "features": ["basic_terminal"],
  "expires_at": null
}
```

**Fynd**: Premium-status kontrolleras via API-anrop.

#### Steg 1.3: Statisk Analys med Ghidra

```bash
# Öppna binary i Ghidra
ghidraRun /usr/bin/warp-console
```

**I Ghidra Symbol Tree, hitta:**

```c
// Pseudo-code från Ghidra
bool checkPremiumAccess() {
    json response = httpGet("https://api.warp.dev/v1/verify-subscription");

    if (response["premium"] == true) {
        enablePremiumFeatures();
        return true;
    }

    return false;
}

void enableAIAssistant() {
    if (isPremiumUser) {  // ← Kolla denna variabel
        initAIFeatures();
    } else {
        showUpgradeDialog();
    }
}
```

**Kritiskt fynd**:
- Global variabel `isPremiumUser` styr features
- Enkel boolean-check utan kryptografisk verifiering

### Fas 2: Identifiera Sårbarhet

**Sårbarhet #1: Client-side Premium Check**

```
┌────────────────────────────────────────┐
│         FLAWED ARCHITECTURE            │
└────────────────────────────────────────┘

    Client (Warp Console)
    ┌─────────────────────────────┐
    │ 1. API: isPremium?          │
    │    Response: false          │
    │                             │
    │ 2. if (isPremiumUser)       │ ← SÅRBAR!
    │       enableFeatures()      │
    │                             │
    └─────────────────────────────┘

PROBLEM: Klienten fattar beslut om premium-features
ATTACK: Modifiera isPremiumUser till true
```

**Sårbarhet #2: Ingen Runtime Integrity Check**

- Ingen anti-tampering
- Ingen code signing verification
- Ingen Frida-detection

### Fas 3: Exploit Development

#### Exploit 1: Frida Hook - Boolean Manipulation

**warp_bypass_v1.js:**

```javascript
console.log("[*] Warp Console Premium Bypass - v1");
console.log("[*] Target: Boolean manipulation");

// Hitta checkPremiumAccess funktion
var baseAddr = Module.findBaseAddress("warp-console");
console.log("[*] Base address: " + baseAddr);

// Hook checkPremiumAccess
var checkPremiumPtr = Module.findExportByName("warp-console", "_Z18checkPremiumAccessv");

if (checkPremiumPtr) {
    Interceptor.attach(checkPremiumPtr, {
        onLeave: function(retval) {
            console.log("[*] Original premium status: " + retval);
            retval.replace(1);  // Ändra till true
            console.log("[+] Modified to: true");
        }
    });
    console.log("[+] Successfully hooked checkPremiumAccess!");
}

// Hook isPremiumUser variabel
var isPremiumUserAddr = baseAddr.add(0x12A4E0);  // Från Ghidra
Memory.writeU8(isPremiumUserAddr, 1);
console.log("[+] Set isPremiumUser = true");
```

**Kör exploiten:**

```bash
frida -l warp_bypass_v1.js warp-console
```

**Resultat:**

```
[*] Warp Console Premium Bypass - v1
[*] Target: Boolean manipulation
[*] Base address: 0x555555554000
[+] Successfully hooked checkPremiumAccess!
[+] Set isPremiumUser = true

[Warp Console]
✅ Premium Features Unlocked
   - AI Assistant: Enabled
   - Team Collaboration: Enabled
   - Premium Themes: Enabled
```

#### Exploit 2: API Response Manipulation

**warp_bypass_v2.js:**

```javascript
console.log("[*] Warp Console Premium Bypass - v2");
console.log("[*] Target: API Response manipulation");

// Hook HTTPS response parsing
Interceptor.attach(Module.findExportByName("libcurl.so", "curl_easy_perform"), {
    onEnter: function(args) {
        this.curl_handle = args[0];
    },
    onLeave: function(retval) {
        // Efter HTTP-anrop, modifiera response
        if (retval == 0) {  // CURLE_OK
            console.log("[*] curl_easy_perform succeeded");
        }
    }
});

// Hook JSON parsing
var jsonParsePtr = Module.findExportByName("warp-console", "_Z9parseJsonPKc");

Interceptor.attach(jsonParsePtr, {
    onEnter: function(args) {
        var jsonStr = Memory.readUtf8String(args[0]);
        console.log("[*] Original JSON: " + jsonStr);

        if (jsonStr.includes('"premium":false')) {
            // Modifiera JSON innan parsing
            var modifiedJson = jsonStr.replace('"premium":false', '"premium":true');
            Memory.writeUtf8String(args[0], modifiedJson);
            console.log("[+] Modified JSON: " + modifiedJson);
        }
    }
});
```

#### Exploit 3: Persistent Patch (Advanced)

**warp_persistent_patch.py:**

```python
#!/usr/bin/env python3
"""
Persistent binary patch för Warp Console
VARNING: Endast för educational purposes i kontrollerad miljö!
"""

import sys

def patch_binary(binary_path):
    """
    Patchar binären för att alltid returnera premium=true
    """
    with open(binary_path, 'rb') as f:
        data = bytearray(f.read())

    # Hitta checkPremiumAccess funktion
    # Offset 0x3A42: Returnerar premium status
    # Original: 48 8B 45 F8    mov rax, [rbp-8]    ; Load premium status
    #          84 C0          test al, al          ; Test if true
    #          74 0E          je short NO_PREMIUM  ; Jump if false
    #
    # Patch:   B0 01          mov al, 1            ; Sätt alltid till true
    #          90             nop
    #          90             nop
    #          90             nop

    offset = 0x3A42
    original = bytes([0x48, 0x8B, 0x45, 0xF8, 0x84, 0xC0])
    patch = bytes([0xB0, 0x01, 0x90, 0x90, 0x90, 0x90])

    if data[offset:offset+len(original)] == original:
        data[offset:offset+len(patch)] = patch
        print(f"[+] Patched at offset 0x{offset:X}")

        # Skriv patchad binary
        with open(binary_path + '.patched', 'wb') as f:
            f.write(data)
        print(f"[+] Saved to {binary_path}.patched")
        return True
    else:
        print("[-] Binary does not match expected pattern")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <warp-console-binary>")
        sys.exit(1)

    patch_binary(sys.argv[1])
```

### Fas 4: Documentation & Reporting

**Bug Bounty Report:**

```markdown
# Vulnerability Report: Warp Console Premium Bypass

## Summary
Client-side premium verification allows attackers to unlock premium features
without payment through runtime manipulation.

## Severity: HIGH
- **CVSS Score**: 7.5
- **Impact**: Revenue loss, unauthorized feature access
- **Likelihood**: High (trivial to exploit with Frida)

## Vulnerability Details

### Root Cause
Premium feature access is controlled by client-side boolean checks without
server-side enforcement.

### Attack Vectors
1. **Frida Runtime Manipulation**: Hook checkPremiumAccess() → return true
2. **API Response Tampering**: Modify JSON response before parsing
3. **Binary Patching**: Permanent modification of executable

### Proof of Concept
See attached: warp_bypass_v1.js

## Reproduction Steps
1. Install Frida: `pip install frida-tools`
2. Run: `frida -l warp_bypass_v1.js warp-console`
3. Observe: All premium features unlocked

## Recommendations
See Blue Team section for remediation.

## Timeline
- 2025-01-15: Vulnerability discovered
- 2025-01-15: Reported to Blue Team
- 2025-01-16: Fix implemented
- 2025-01-20: Patch deployed

## Bounty Claim
$5,000 (High severity, clear PoC, actionable recommendations)
```

---

## 🔵 DEL 2: BLUE TEAM - Pedagogiskt Facit

### Fas 1: Vulnerability Assessment

**Mottagande av Red Team Report:**

```bash
# Verifiera exploit
frida -l warp_bypass_v1.js warp-console

# Resultat: ✅ Confirmed - Exploitable
```

**Severity Analysis:**

| Faktor              | Bedömning | Poäng |
|---------------------|-----------|-------|
| Exploitability      | Trivial   | 10/10 |
| Impact              | Revenue loss | 8/10 |
| Affected Users      | All free users | 10/10 |
| Detection Difficulty| Hard      | 9/10  |

**Slutsats**: Kritisk sårbarhet - omedelbar åtgärd krävs

### Fas 2: Root Cause Analysis

**Arkitektur-diagram (Nuvarande - Sårbar):**

```
┌─────────────────────────────────────────────────────┐
│                 VULNERABLE FLOW                      │
└─────────────────────────────────────────────────────┘

Client                          Server
┌──────────────┐               ┌──────────────┐
│ Warp Console │               │  API Server  │
└──────┬───────┘               └──────┬───────┘
       │                              │
       │ 1. GET /verify-subscription  │
       │─────────────────────────────>│
       │                              │
       │ 2. {premium: false}          │
       │<─────────────────────────────│
       │                              │
       │ 3. if (premium) { ✗ }        │  ← PROBLEM!
       │    enableFeatures()          │
       │                              │
       │ 4. Use premium features      │
       │    (No server check!)        │  ← PROBLEM!
       │                              │
```

**Problem Identifierade:**

1. **Client-Side Trust**: Klienten bestämmer åtkomst
2. **No Continuous Verification**: Ingen runtime server-check
3. **No Anti-Tampering**: Ingen skydd mot Frida
4. **No Feature Gating**: Server validerar inte feature-requests

### Fas 3: Remediation Strategy

**Multi-Layer Defense Approach:**

```
┌────────────────────────────────────────────────┐
│         DEFENSE IN DEPTH STRATEGY              │
└────────────────────────────────────────────────┘

Layer 1: Server-Side Feature Gating
Layer 2: Continuous Token Verification
Layer 3: Anti-Tampering Protection
Layer 4: Runtime Integrity Monitoring
Layer 5: Rate Limiting & Anomaly Detection
```

### Fas 4: Implementation - Lösningar

#### Lösning 1: Server-Side Feature Gating

**INNAN (Sårbar):**

```javascript
// client/features.js
function enableAIAssistant() {
    if (isPremiumUser) {  // ← Client-side check
        initAIFeatures();
    }
}

function processAIRequest(prompt) {
    // Direkt processing utan server-check
    return generateResponse(prompt);
}
```

**EFTER (Säker):**

```javascript
// client/features.js
async function processAIRequest(prompt) {
    // Skicka till server för validering OCH processing
    const response = await fetch('https://api.warp.dev/v1/ai/process', {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${getAuthToken()}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    });

    if (response.status === 403) {
        throw new Error('Premium feature - upgrade required');
    }

    return await response.json();
}
```

```python
# server/api/ai.py
from flask import request, jsonify
from auth import verify_premium_token

@app.route('/v1/ai/process', methods=['POST'])
def process_ai_request():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')

    # SERVER-SIDE premium verification
    user = verify_premium_token(token)

    if not user or not user.is_premium:
        return jsonify({'error': 'Premium subscription required'}), 403

    # Check not expired
    if user.premium_expires < datetime.now():
        return jsonify({'error': 'Subscription expired'}), 403

    # Log usage for rate limiting
    log_feature_usage(user.id, 'ai_request')

    # Process request
    prompt = request.json.get('prompt')
    result = ai_service.generate(prompt, user_id=user.id)

    return jsonify({'result': result})
```

#### Lösning 2: Continuous Token Verification

**token_manager.js:**

```javascript
class SecureTokenManager {
    constructor() {
        this.token = null;
        this.premiumStatus = null;
        this.lastVerified = null;
        this.VERIFICATION_INTERVAL = 5 * 60 * 1000; // 5 minuter
    }

    async initialize() {
        await this.verifyToken();

        // Kontinuerlig verifiering i bakgrunden
        setInterval(() => this.verifyToken(), this.VERIFICATION_INTERVAL);
    }

    async verifyToken() {
        try {
            const response = await fetch('https://api.warp.dev/v1/verify-subscription', {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    // Anti-replay: Nonce
                    'X-Nonce': this.generateNonce(),
                    // Integrity check
                    'X-Integrity': this.calculateIntegrity()
                }
            });

            const data = await response.json();

            // Verifiera signatur från server
            if (!this.verifyServerSignature(data)) {
                throw new Error('Invalid server signature');
            }

            this.premiumStatus = data.premium;
            this.lastVerified = Date.now();

            // Emit event för feature managers
            this.emit('premium-status-updated', this.premiumStatus);

        } catch (error) {
            console.error('Token verification failed:', error);
            // Fail secure: Disable premium features
            this.premiumStatus = false;
            this.emit('premium-status-updated', false);
        }
    }

    isPremium() {
        // Kontrollera att verifiering är färsk
        const timeSinceVerification = Date.now() - this.lastVerified;

        if (timeSinceVerification > this.VERIFICATION_INTERVAL * 2) {
            // För gammal verifiering - fail secure
            return false;
        }

        return this.premiumStatus === true;
    }

    generateNonce() {
        return crypto.randomBytes(16).toString('hex');
    }

    calculateIntegrity() {
        // Hash av kritiska komponenter för att detektera tampering
        const components = [
            this.getAppVersion(),
            this.getBinaryHash(),
            this.getConfigHash()
        ].join('|');

        return crypto.createHash('sha256').update(components).digest('hex');
    }

    verifyServerSignature(data) {
        // Verifiera JWT signatur eller HMAC
        const signature = data.signature;
        const payload = JSON.stringify({
            premium: data.premium,
            expires_at: data.expires_at
        });

        const expectedSignature = crypto
            .createHmac('sha256', SERVER_PUBLIC_KEY)
            .update(payload)
            .digest('hex');

        return signature === expectedSignature;
    }
}
```

#### Lösning 3: Anti-Tampering Protection

**integrity_monitor.cpp:**

```cpp
#include <frida-gum.h>
#include <openssl/sha.h>

class IntegrityMonitor {
private:
    bool frida_detected = false;
    bool debugger_detected = false;
    std::string original_binary_hash;

public:
    IntegrityMonitor() {
        // Beräkna hash av egen binary vid start
        original_binary_hash = calculateSelfHash();
    }

    // Detektera Frida
    bool detectFrida() {
        // Metod 1: Kolla efter Frida libraries
        void* handle = dlopen("libfrida-agent.so", RTLD_NOW);
        if (handle != nullptr) {
            dlclose(handle);
            return true;
        }

        // Metod 2: Kolla efter Frida threads
        DIR* dir = opendir("/proc/self/task");
        if (dir) {
            struct dirent* entry;
            while ((entry = readdir(dir)) != nullptr) {
                if (entry->d_type == DT_DIR) {
                    std::string comm_path = "/proc/self/task/" +
                                           std::string(entry->d_name) + "/comm";
                    std::ifstream comm_file(comm_path);
                    std::string comm;
                    std::getline(comm_file, comm);

                    if (comm.find("frida") != std::string::npos ||
                        comm.find("gmain") != std::string::npos) {
                        closedir(dir);
                        return true;
                    }
                }
            }
            closedir(dir);
        }

        // Metod 3: Kolla efter named pipes som Frida använder
        for (const auto& pipe : {"/frida-agent", "/linjector"}) {
            if (access(pipe, F_OK) == 0) {
                return true;
            }
        }

        return false;
    }

    // Detektera debugger
    bool detectDebugger() {
        // Metod 1: ptrace anti-debug
        if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
            return true;  // Redan debuggad
        }
        ptrace(PTRACE_DETACH, 0, 1, 0);

        // Metod 2: Kolla /proc/self/status
        std::ifstream status("/proc/self/status");
        std::string line;
        while (std::getline(status, line)) {
            if (line.find("TracerPid:") == 0) {
                int tracer_pid = std::stoi(line.substr(11));
                if (tracer_pid != 0) {
                    return true;
                }
            }
        }

        return false;
    }

    // Verifiera binary integrity
    bool verifyBinaryIntegrity() {
        std::string current_hash = calculateSelfHash();
        return current_hash == original_binary_hash;
    }

    std::string calculateSelfHash() {
        std::ifstream binary("/proc/self/exe", std::ios::binary);
        SHA256_CTX sha256;
        SHA256_Init(&sha256);

        char buffer[4096];
        while (binary.read(buffer, sizeof(buffer))) {
            SHA256_Update(&sha256, buffer, binary.gcount());
        }

        unsigned char hash[SHA256_DIGEST_LENGTH];
        SHA256_Final(hash, &sha256);

        std::stringstream ss;
        for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
            ss << std::hex << std::setw(2) << std::setfill('0')
               << static_cast<int>(hash[i]);
        }

        return ss.str();
    }

    // Main monitoring loop
    void startMonitoring() {
        std::thread monitor_thread([this]() {
            while (true) {
                if (detectFrida()) {
                    handleTamperingDetected("Frida detected");
                }

                if (detectDebugger()) {
                    handleTamperingDetected("Debugger detected");
                }

                if (!verifyBinaryIntegrity()) {
                    handleTamperingDetected("Binary integrity violation");
                }

                std::this_thread::sleep_for(std::chrono::seconds(5));
            }
        });

        monitor_thread.detach();
    }

    void handleTamperingDetected(const std::string& reason) {
        // Logga till server
        logSecurityEvent(reason);

        // Disable premium features
        disableAllPremiumFeatures();

        // Optional: Exit application
        std::cerr << "Security violation detected: " << reason << std::endl;
        std::cerr << "Application will now exit." << std::endl;
        exit(1);
    }

    void logSecurityEvent(const std::string& reason) {
        // Skicka till server för analys
        httpPost("https://api.warp.dev/v1/security/events", {
            {"event_type", "tampering_detected"},
            {"reason", reason},
            {"timestamp", getCurrentTimestamp()},
            {"user_id", getUserId()},
            {"device_id", getDeviceId()}
        });
    }
};
```

#### Lösning 4: Runtime Integrity Monitoring

**server/monitoring.py:**

```python
from flask import Flask, request
from datetime import datetime, timedelta
import redis
from collections import defaultdict

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

class AnomalyDetector:
    """Detektera onormalt beteende som kan indikera bypass"""

    def __init__(self):
        self.redis = redis_client

    def check_rate_limit(self, user_id, feature):
        """Rate limiting per feature"""
        key = f"rate_limit:{user_id}:{feature}"

        # Premium users: 100 AI requests/hour
        # Free users: 0 AI requests
        current_count = self.redis.incr(key)

        if current_count == 1:
            # Första requesten - sätt TTL
            self.redis.expire(key, 3600)  # 1 timme

        user = get_user(user_id)

        if not user.is_premium and feature == 'ai_request':
            # Free user försöker använda premium feature
            self.log_security_event(user_id, 'unauthorized_feature_access', {
                'feature': feature,
                'premium_status': False
            })
            return False

        if user.is_premium and current_count > 100:
            # För många requests - möjlig automation
            self.log_security_event(user_id, 'rate_limit_exceeded', {
                'feature': feature,
                'count': current_count,
                'limit': 100
            })
            return False

        return True

    def detect_impossible_travel(self, user_id, ip_address):
        """Detektera om samma user loggar in från två platser samtidigt"""
        key = f"user_location:{user_id}"

        last_location = self.redis.get(key)

        if last_location:
            last_ip, last_time = last_location.decode().split('|')
            last_time = datetime.fromisoformat(last_time)

            # Kolla geografisk distans
            distance = calculate_distance(last_ip, ip_address)
            time_diff = (datetime.now() - last_time).total_seconds()

            # Mänskligt omöjlig resa? (>1000 km på <1 timme)
            if distance > 1000 and time_diff < 3600:
                self.log_security_event(user_id, 'impossible_travel', {
                    'last_ip': last_ip,
                    'current_ip': ip_address,
                    'distance_km': distance,
                    'time_seconds': time_diff
                })
                return False

        # Uppdatera location
        self.redis.setex(
            key,
            3600,  # 1 timme
            f"{ip_address}|{datetime.now().isoformat()}"
        )

        return True

    def detect_version_anomaly(self, user_id, client_version, integrity_hash):
        """Detektera modifierad client"""
        expected_hashes = {
            '1.2.0': 'a3f5d8c9e2b1...',
            '1.2.1': 'b4e6f9d0c3a2...',
        }

        expected_hash = expected_hashes.get(client_version)

        if not expected_hash:
            self.log_security_event(user_id, 'unknown_version', {
                'version': client_version
            })
            return False

        if integrity_hash != expected_hash:
            self.log_security_event(user_id, 'integrity_violation', {
                'version': client_version,
                'expected_hash': expected_hash,
                'actual_hash': integrity_hash
            })
            return False

        return True

    def log_security_event(self, user_id, event_type, metadata):
        """Logga security event för analys"""
        event = {
            'user_id': user_id,
            'event_type': event_type,
            'metadata': metadata,
            'timestamp': datetime.now().isoformat(),
            'ip': request.remote_addr
        }

        # Spara till database
        db.security_events.insert_one(event)

        # Real-time alert för kritiska events
        if event_type in ['unauthorized_feature_access', 'integrity_violation']:
            send_alert_to_security_team(event)

        # Auto-ban efter för många violations
        violation_count = db.security_events.count_documents({
            'user_id': user_id,
            'timestamp': {'$gte': datetime.now() - timedelta(hours=1)}
        })

        if violation_count > 5:
            ban_user(user_id, reason=f"Multiple security violations: {event_type}")

# Integration i API
@app.route('/v1/ai/process', methods=['POST'])
def process_ai_request():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user = verify_token(token)

    if not user:
        return jsonify({'error': 'Invalid token'}), 401

    # Anomaly detection
    detector = AnomalyDetector()

    # Check 1: Rate limiting
    if not detector.check_rate_limit(user.id, 'ai_request'):
        return jsonify({'error': 'Rate limit exceeded'}), 429

    # Check 2: Impossible travel
    if not detector.detect_impossible_travel(user.id, request.remote_addr):
        return jsonify({'error': 'Suspicious activity detected'}), 403

    # Check 3: Client integrity
    client_version = request.headers.get('X-Client-Version')
    integrity_hash = request.headers.get('X-Integrity')

    if not detector.detect_version_anomaly(user.id, client_version, integrity_hash):
        return jsonify({'error': 'Client integrity check failed'}), 403

    # Alla checks passerade - process request
    # ...
```

#### Lösning 5: Code Obfuscation (Defense in Depth)

**build_config.js:**

```javascript
// webpack.config.js med obfuscation
const JavaScriptObfuscator = require('webpack-obfuscator');

module.exports = {
    // ... standard config

    plugins: [
        new JavaScriptObfuscator({
            // Gör reverse engineering svårare
            rotateStringArray: true,
            stringArray: true,
            stringArrayThreshold: 0.75,

            // Anti-debug
            debugProtection: true,
            debugProtectionInterval: 4000,

            // Anti-tampering
            selfDefending: true,

            // Deadcode injection
            deadCodeInjection: true,
            deadCodeInjectionThreshold: 0.4,

            // Control flow flattening
            controlFlowFlattening: true,
            controlFlowFlatteningThreshold: 0.75
        }, [])
    ]
};
```

### Fas 5: Testing & Validation

**Säkerhetstest:**

```bash
# Test 1: Försök använda gamla exploiten
frida -l warp_bypass_v1.js warp-console

# Förväntat resultat:
# [!] Tampering detected: Frida detected
# Application will now exit.
# ✅ PASS

# Test 2: Försök patcha binary
python warp_persistent_patch.py /usr/bin/warp-console

# Förväntat resultat:
# [+] Patched binary created
# [Run patched binary]
# [!] Binary integrity violation
# Application will now exit.
# ✅ PASS

# Test 3: Försök API response manipulation
mitmproxy --modify-body '{"premium":false}' '{"premium":true}'

# Förväntat resultat:
# Server returnerar signerad response
# Client verifierar signatur
# Invalid signature → Fail secure
# ✅ PASS

# Test 4: Premium user - normal usage
# Förväntat resultat:
# ✅ AI features work
# ✅ Rate limiting fungerar
# ✅ PASS
```

### Fas 6: Deployment & Monitoring

**Deployment Plan:**

```yaml
# deployment.yml
version: 2.0.0
release_date: 2025-01-20

phases:
  # Fas 1: Canary deployment (5% users)
  - name: canary
    duration: 24h
    percentage: 5%
    rollback_on:
      - error_rate > 1%
      - crash_rate > 0.1%

  # Fas 2: Gradual rollout
  - name: rollout
    duration: 72h
    percentage: 100%
    stages:
      - 25%: 24h
      - 50%: 24h
      - 100%: 24h

monitoring:
  metrics:
    - security_events_count
    - tampering_detection_rate
    - false_positive_rate
    - premium_feature_usage
    - api_response_time

  alerts:
    - condition: security_events_count > 100/hour
      severity: high
      notify: security-team

    - condition: tampering_detection_rate > 10%
      severity: medium
      notify: dev-team

rollback_plan:
  triggers:
    - manual
    - automated (if critical metrics breached)

  steps:
    1. Stop deployment
    2. Revert to previous version
    3. Notify stakeholders
    4. Post-mortem analysis
```

---

## 📊 DEL 3: Analys & Lärdomar

### Red Team Insikter

**Vad fungerade:**

✅ **Reconnaissance**: Kombination av statisk (Ghidra) och dynamisk (Frida) analys
✅ **Methodology**: Systematisk approach från spaning → exploit → dokumentation
✅ **Tools**: Frida väldigt kraftfullt för runtime manipulation
✅ **Communication**: Tydlig dokumentation hjälpte Blue Team

**Challenges:**

⚠️ **False sense of security**: Client-side checks är alltid sårbar
⚠️ **Complexity**: Vissa exploits krävde djup förståelse av binary
⚠️ **Detection**: Bra anti-tampering kan göra exploits svårare

### Blue Team Insikter

**Vad fungerade:**

✅ **Defense in Depth**: Flera lager av skydd
✅ **Server-Side Enforcement**: Flyttade kritiska decisions till server
✅ **Monitoring**: Real-time detection av anomalier
✅ **Quick Response**: Snabb deployment av fix

**Challenges:**

⚠️ **False Positives**: Anti-tampering kan trigga på legitima debuggers
⚠️ **Performance**: Continuous verification har overhead
⚠️ **User Experience**: Balance mellan säkerhet och UX

### Viktiga Säkerhetsprinciper

#### 1. Never Trust the Client

```
❌ BAD:  if (clientSays.isPremium) { grantAccess(); }
✅ GOOD: if (serverVerifies.isPremium) { grantAccess(); }
```

#### 2. Defense in Depth

```
Lager 1: Client-side checks (UX, ej säkerhet)
Lager 2: Server-side enforcement (primär säkerhet)
Lager 3: Anti-tampering (fördröj attacker)
Lager 4: Monitoring (detektera attacker)
Lager 5: Rate limiting (begränsa skada)
```

#### 3. Fail Secure

```javascript
// När något går fel - fail till säkert state
function isPremium() {
    try {
        return verifyPremiumStatus();
    } catch (error) {
        console.error('Premium verification failed');
        return false;  // ← Fail secure
    }
}
```

#### 4. Continuous Verification

```
Inte bara vid login - verify kontinuerligt:
- Vid varje premium feature request
- Regelbundet i bakgrunden (var 5:e minut)
- Vid misstänkt beteende
```

#### 5. Monitor & Respond

```
Detection → Alert → Response → Learn
    ↑                              ↓
    └──────────── Improve ─────────┘
```

### Metrics & Success Criteria

**Red Team Success:**

| Metric                    | Mål    | Resultat |
|---------------------------|--------|----------|
| Time to exploit           | <8h    | 4h ✅    |
| Exploit reliability       | >90%   | 100% ✅  |
| Documentation quality     | High   | High ✅  |
| Responsible disclosure    | Yes    | Yes ✅   |

**Blue Team Success:**

| Metric                    | Mål    | Resultat |
|---------------------------|--------|----------|
| Time to patch             | <7d    | 5d ✅    |
| Exploit mitigation        | 100%   | 100% ✅  |
| False positive rate       | <1%    | 0.3% ✅  |
| Performance impact        | <5%    | 2% ✅    |
| Zero-day window           | <48h   | 36h ✅   |

---

## 🎓 Övning för Läsaren

### Del A: Red Team Challenge

**Din uppgift**: Företaget har uppdaterat till v2.0 med följande nya "säkerhet":

```javascript
// warp-console v2.0
function checkPremium() {
    const response = api.verify();
    const decrypted = decrypt(response.encryptedStatus, SECRET_KEY);
    return decrypted.premium === true;
}
```

**Frågor:**
1. Vilka potentiella sårbarheter finns fortfarande?
2. Hur skulle du exploitera detta med Frida?
3. Varför är detta fortfarande osäkert?

<details>
<summary>Facit</summary>

**Svar:**

1. **Sårbarheter:**
   - Klienten har fortfarande `SECRET_KEY` (kan extraheras med Frida)
   - Decryption sker client-side (kan bypasses)
   - Ingen continuous verification
   - `premium === true` check kan hookbas

2. **Exploit:**
```javascript
// Hook decrypt function
var decryptPtr = Module.findExportByName("warp-console", "_Z7decryptPKcS0_");
Interceptor.attach(decryptPtr, {
    onLeave: function(retval) {
        // Modifiera decrypterat result
        var result = JSON.parse(Memory.readUtf8String(retval));
        result.premium = true;
        Memory.writeUtf8String(retval, JSON.stringify(result));
    }
});
```

3. **Varför osäkert:**
   - Anything client-side kan manipuleras
   - Kryptografiska nycklar på klient = ej säkert
   - Lösning: Server måste fatta decision OCH utföra action

</details>

### Del B: Blue Team Challenge

**Din uppgift**: Designa säkerhet för ny feature: "Team Collaboration"

**Krav:**
- Multiple users kan dela terminal sessions
- Endast premium teams
- Real-time collaboration

**Frågor:**
1. Var ska premium-verification ske?
2. Hur förhindrar du att free users "joins" en premium session?
3. Vilken monitoring behövs?

<details>
<summary>Facit</summary>

**Säker Design:**

```python
# server/collaboration.py
@app.route('/v1/session/create', methods=['POST'])
def create_session():
    user = verify_token(request.headers['Authorization'])

    # 1. Server-side verification
    if not user.is_premium or not user.team.is_premium:
        return jsonify({'error': 'Premium team required'}), 403

    # 2. Create session på SERVER
    session = CollaborationSession.create(
        owner_id=user.id,
        team_id=user.team.id
    )

    return jsonify({'session_id': session.id})

@app.route('/v1/session/<session_id>/join', methods=['POST'])
def join_session(session_id):
    user = verify_token(request.headers['Authorization'])
    session = CollaborationSession.get(session_id)

    # 1. Verify user is premium
    if not user.is_premium:
        return jsonify({'error': 'Premium required'}), 403

    # 2. Verify user is in same team
    if user.team.id != session.team_id:
        return jsonify({'error': 'Not in session team'}), 403

    # 3. Verify session still valid
    if not session.team.is_premium:
        return jsonify({'error': 'Team subscription expired'}), 403

    # 4. Add user to session (server-side)
    session.add_participant(user.id)

    # 5. Monitor
    log_event('collaboration_join', {
        'user_id': user.id,
        'session_id': session_id
    })

    return jsonify({'websocket_url': f'wss://collab.warp.dev/{session_id}'})

# WebSocket handler
@socketio.on('terminal_input')
def handle_input(data):
    session_id = request.args.get('session')
    user = get_current_user()

    # VERIFY VARJE INPUT
    if not verify_session_access(user.id, session_id):
        disconnect()
        return

    # Broadcast till andra premium users
    emit('terminal_output', data, room=session_id)
```

**Monitoring:**
- Track session creation rate per team
- Alert on abnormal join patterns
- Monitor for session hijacking attempts
- Log all collaboration events

</details>

---

## 🏆 Bug Bounty Resultat

### Utbetalningar

| Team      | Sårbarhet                    | Severity | Bounty  |
|-----------|------------------------------|----------|---------|
| Red Team  | Client-side premium bypass   | High     | $5,000  |
| Red Team  | API response manipulation    | Medium   | $2,500  |
| Red Team  | Persistent binary patch      | Medium   | $2,000  |
| Blue Team | Defense implementation       | -        | $3,000  |
| Blue Team | Monitoring system            | -        | $1,500  |

**Total utbetalt:** $14,000

### Lessons Learned

**För Organisationen:**

✅ Internal bug bounties fungerar för att hitta sårbarheter
✅ Red Team + Blue Team samarbete förbättrar säkerhet
✅ Investering i säkerhet sparar pengar långsiktigt
✅ Documentation är kritisk för både teams

**För Utvecklare:**

✅ Never trust client-side för säkerhetsbeslut
✅ Server-side enforcement är enda sättet
✅ Defense in depth - flera lager
✅ Monitor och respond kontinuerligt

**För Security Team:**

✅ Frida är kraftfullt verktyg för både attack och defense
✅ Kombinera Ghidra + Frida för bästa resultat
✅ Automated testing är kritiskt
✅ Real-world scenarios tränar teams bättre

---

## 🎯 Sammanfattning

**Red Team Workflow:**
```
Recon → Analyze → Exploit → Document → Report
  ↓        ↓         ↓          ↓         ↓
Ghidra   Frida    PoC Code   Write-up  Bounty
```

**Blue Team Workflow:**
```
Receive → Verify → Analyze → Fix → Test → Deploy → Monitor
   ↓        ↓         ↓       ↓      ↓       ↓        ↓
Report   Repro    Root     Patch  QA    Rollout  Alerts
               Cause
```

**Viktigaste Lärdomar:**

1. **Client är ej pålitlig** - All enforcement ska ske server-side
2. **Defense in Depth** - Ett lager räcker ej
3. **Continuous Verification** - Inte bara vid login
4. **Monitor Everything** - Detektera anomalier
5. **Fail Secure** - När något går fel, fail till säker state

**Etik:**
- ✅ Endast på auktoriserade system
- ✅ Dokumentera och rapportera
- ✅ Hjälp till att fixa
- ❌ Exploatera ej i produktion
- ❌ Dela ej exploits publikt

---

**Lycka till med era egna bug bounties! 🔐**

*Red Team vs Blue Team Exercise - Internal Training*
*Skapad: 2025*
*Disclaimer: Endast för educational purposes i kontrollerade miljöer*

