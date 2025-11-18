# FastAPI – Den Kompletta Guiden

## 📚 Innehållsförteckning

1. [Om Denna Guide](#-om-denna-guide)
2. [Nivå 1: Vad är ett API och vad gör FastAPI? 👶](#nivå-1-vad-är-ett-api-och-vad-gör-fastapi-)
3. [Nivå 2: Webben, HTTP och FastAPI-grunder 🧒](#nivå-2-webben-http-och-fastapi-grunder-)
4. [Nivå 3: Bygga dina första FastAPI-endpoints 🎓](#nivå-3-bygga-dina-första-fastapi-endpoints-)
5. [Nivå 4: Arkitektur, beroenden och best practices 🏛️](#nivå-4-arkitektur-beroenden-och-best-practices-️)
6. [Nivå 5: Produktion, säkerhet och avancerade mönster 💼](#nivå-5-produktion-säkerhet-och-avancerade-mönster-)
7. [Slutlig Självutvärdering 🎓](#-slutlig-självutvärdering)
8. [Ordlista 📖](#-ordlista)
9. [Resurser för Fördjupning 🔗](#-resurser-för-fördjupning)
10. [Vanliga Frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den kompletta guiden om **FastAPI** – ett modernt Python-ramverk för att bygga snabba, skalbara API:er!

Denna guide tar dig från absolut nybörjare till expertnivå genom **fem progressiva nivåer**. Varje nivå är designad för att ge dig praktisk kunskap och konkreta färdigheter:

- **Nivå 1 (👶 5-åringen)**: Förstå grundkoncepten med enkla analogier – ingen kod, bara idéer
- **Nivå 2 (🧒 10-åringen)**: Lär dig webbutvecklingens byggstenar och hur FastAPI passar in
- **Nivå 3 (🎓 Gymnasiet)**: Skriv din första fungerande FastAPI-applikation
- **Nivå 4 (🏛️ Universitet)**: Bygg professionella, välstrukturerade projekt
- **Nivå 5 (💼 Expert)**: Sätt din applikation i produktion med säkerhet och prestanda i fokus

**Total läsningstid**: 1.5–3 timmar
**Förutsättningar**: Ingen tidigare erfarenhet krävs – vi börjar från grunden!

Varje nivå innehåller:
- ✨ Tydliga förklaringar och exempel
- 🎨 Visualiseringar och diagram
- 💡 Pro tips från verkligheten
- ✏️ Praktiska övningar med facit
- 📝 Sammanfattning av viktiga lärdomar

---

## Nivå 1: Vad är ett API och vad gör FastAPI? 👶

### Introduktion

På denna första nivå ska du lära dig vad ett **API** (Application Programming Interface) egentligen är, och varför verktyg som **FastAPI** är så användbara. Vi kommer inte att skriva någon kod här – istället ska vi använda vardagliga analogier och enkla bilder för att förstå koncepten. När du är klar med denna nivå kommer du att kunna förklara för vem som helst vad ett API är och varför det är viktigt i dagens digitala värld!

### Kärnkoncept

#### 1. **Vad är ett program?**

Tänk dig att ett datorprogram är som en hjälpsam robot. Denna robot kan göra vissa saker åt dig – till exempel räkna ut hur mycket pengar du har, visa dig väderprognosen, eller hitta en bild av en katt. Men för att roboten ska förstå vad du vill, måste du prata med den på ett speciellt sätt.

#### 2. **Vad är ett API?**

Ett **API** är som en **meny på en restaurang**.

- På menyn står det vilka rätter du kan beställa (t.ex. hamburgare, pizza, glass)
- När du beställer, säger du till kocken vad du vill ha
- Kocken lagar maten och ger den till dig
- Du behöver inte veta *hur* kocken lagar maten – du behöver bara veta vad du kan beställa!

På samma sätt är ett API en lista över saker du kan "beställa" från ett datorprogram. Du skickar en **förfrågan** (beställning), och programmet skickar tillbaka ett **svar** (maten).

#### 3. **Varför behöver vi API:er?**

Föreställ dig att du har en mobilapp som visar dagens väder. Hur vet appen vad vädret är? Jo, den **frågar** ett annat program (en väderserver) genom ett API:

```
Du → Mobilapp → API → Väderserver → API → Mobilapp → Du
```

Utan API skulle appen inte kunna prata med väderservern!

#### 4. **Vad är FastAPI då?**

FastAPI är som en **verktygslåda** för att bygga API:er snabbt och enkelt. Om du vill skapa ditt eget API (kanske för att dela information om dina leksaker med dina kompisar), så hjälper FastAPI dig att göra det på ett smart sätt.

Tänk på det som:
- **LEGO-byggsatser** → FastAPI ger dig färdiga block att bygga med
- **Kokbok** → FastAPI visar dig exakt hur du ska göra steg för steg
- **Snabb väg** → FastAPI gör att det går mycket fortare att bygga än om du skulle börja från noll

#### 5. **Exempel på API:er i vardagen**

Du använder API:er varje dag utan att tänka på det:

- **När du spelar ett spel på mobilen** → Spelet använder API:er för att spara dina poäng
- **När du kollar YouTube** → Appen använder API:er för att hämta videos
- **När du handlar online** → Webbsidan använder API:er för att visa vilka produkter som finns
- **När du chattar med kompisar** → Chattprogrammet använder API:er för att skicka meddelanden

#### 6. **Hur fungerar "prata med ett program"?**

Tänk dig att du har en önskelista-robot:

1. **Du säger**: "Robot, ge mig en lista på alla leksaker"
2. **Roboten kollar** i sin hjärna (databas) efter leksaker
3. **Roboten svarar**: "Här är listan: bil, docka, bollplank"

Detta är exakt hur ett API fungerar – du ställer en fråga, programmet tänker, och sen får du ett svar!

#### 7. **Varför är FastAPI "snabbt"?**

Namnet "Fast" betyder "snabbt" på engelska. FastAPI är byggt för att:
- Svara på frågor mycket snabbt (som en blixt!)
- Låta programmerare bygga API:er snabbt (mindre tid att vänta)
- Göra många saker samtidigt (som att äta glass OCH lyssna på musik samtidigt)

### Exempel

#### Exempel 1: Brevbäraren-analogin

Föreställ dig att ett API är som en **brevbärare**:

- **Du** skriver ett brev (din förfrågan): "Kära bibliotek, kan jag låna boken om dinosaurier?"
- **Brevbäraren** (API:et) levererar brevet till biblioteket
- **Biblioteket** läser brevet och hittar boken
- **Brevbäraren** (API:et) tar tillbaka boken till dig

Du behöver inte gå till biblioteket själv – brevbäraren gör jobbet åt dig!

#### Exempel 2: Fjärrkontroll till TV:n

En fjärrkontroll är ett slags API:

- Den har **knappar** (olika saker du kan be TV:n göra)
- När du trycker på "volym upp", skickar fjärrkontrollen ett meddelande till TV:n
- TV:n **förstår** meddelandet och höjer volymen
- Du ser resultatet direkt!

Du behöver inte öppna TV:n och ändra elektroniken – du använder bara API:et (fjärrkontrollen).

#### Exempel 3: Beställa mat på restaurang

När du går till en restaurang:

1. Du får en **meny** (lista på vad du kan beställa) → Detta är API:ets dokumentation
2. Du **beställer** en hamburgare → Detta är din förfrågan/request
3. Kocken **lagar** hamburgaren → Detta är vad servern gör
4. Servitören **levererar** hamburgaren → Detta är svaret/response
5. Du **äter** och är nöjd → Du använder informationen du fick

Du bryr dig inte om hur kocken lagar maten eller var hen köper ingredienserna – du bryr dig bara om att få din hamburgare!

### Visualiseringar

#### Diagram 1: API som en bro

```
┌─────────────┐          ┌─────────────┐          ┌─────────────┐
│             │          │             │          │             │
│  DU/APPEN   │ ────────▶│     API     │ ────────▶│   SERVER    │
│  (Frågar)   │          │ (Brevbärare)│          │  (Svarar)   │
│             │ ◀────────│             │ ◀────────│             │
└─────────────┘          └─────────────┘          └─────────────┘

   "Vad är      Förfrågan    "Kan du svara    Hittar svaret
    vädret?"    går fram →    på detta?"       i databasen

    "20°C!"  ← Svar kommer   "Här är svaret"   Skickar tillbaka
               tillbaka                         informationen
```

#### Diagram 2: Vardagsexempel på API-användning

```
┌──────────────────────────────────────────────────────────┐
│                    DU ANVÄNDER API:ER                     │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  📱 Mobil-app  →  [API]  →  🌐 Internet  →  💾 Server   │
│                                                           │
│  Exempel:                                                 │
│  • YouTube-appen frågar: "Ge mig kattvideos"            │
│  • Väder-appen frågar: "Vad är vädret i Stockholm?"     │
│  • Spel-appen säger: "Spara mina 100 poäng"             │
│  • Kart-appen frågar: "Hur tar jag mig till skolan?"    │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

#### Diagram 3: FastAPI som verktygslåda

```
┌────────────────────────────────────────┐
│         FASTAPI VERKTYGSLÅDA           │
├────────────────────────────────────────┤
│                                        │
│  🔧 Verktyg för att ta emot frågor     │
│  🔨 Verktyg för att skicka svar        │
│  📋 Verktyg för att kontrollera data   │
│  ⚡ Verktyg för att göra det snabbt    │
│  📖 Verktyg för att göra dokumentation │
│  🛡️ Verktyg för att göra det säkert    │
│                                        │
│  = ALLT DU BEHÖVER FÖR ATT BYGGA ETT   │
│    FANTASTISKT API! 🚀                 │
│                                        │
└────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Tip 1: API:er är överallt!
Nästan varje app du använder på mobilen eller datorn använder API:er för att hämta information. Nästa gång du öppnar en app, tänk på att den troligen "pratar" med en server någonstans i världen genom ett API!

#### Tip 2: Du behöver inte kunna programmera för att förstå API:er
API:er är bara ett sätt att kommunicera. Precis som du inte behöver kunna bygga en telefon för att ringa ett samtal, behöver du inte kunna programmera för att förstå *konceptet* bakom API:er.

#### Tip 3: FastAPI gör svåra saker enkla
Innan verktyg som FastAPI fanns, tog det mycket längre tid att bygga API:er. FastAPI gör så att även personer som precis har lärt sig programmera kan bygga riktigt bra API:er snabbt!

### ✏️ Övningar

#### Övning 1: Rita ett API-flöde
**Uppgift**: Ta en penna och papper. Rita hur en mobilapp (t.ex. en väderapp) pratar med en server för att få väderprognosdata. Rita tre rutor: "Mobilapp", "API", och "Server". Använd pilar för att visa hur informationen flödar.

**Facit**:
```
Mobilapp → API → Server
         (fråga)
Mobilapp ← API ← Server
         (svar)
```
Din teckning ska visa att mobilappen skickar en fråga genom API:et till servern, och servern skickar tillbaka ett svar samma väg!

#### Övning 2: Leka "API-server"
**Uppgift**: Be en kompis eller familjemedlem att ställa dig frågor som om du vore en "API-server". Till exempel:
- Fråga: "Vad är 5 + 3?"
- Ditt svar: "8"

Innan du svarar, säg högt: "Behandlar förfrågan..." och vänta några sekunder (precis som en riktig server!).

**Facit**: Detta hjälper dig förstå att:
1. API:er tar emot frågor
2. De "tänker" (bearbetar)
3. De ger tillbaka svar

#### Övning 3: Hitta API:er omkring dig
**Uppgift**: Skriv ner fem appar eller webbsidor du använder och gissa vad deras API:er gör. Exempel:
- **Spotify**: API:et hämtar sånger från en databas
- **Instagram**: API:et hämtar bilder från dina kompisar
- **Google Maps**: API:et visar kartor och vägbeskrivningar

**Facit**: Du kan gissa på nästan vilken app som helst! De flesta moderna appar använder API:er för att:
- Hämta data (bilder, texter, videos)
- Spara data (kommentarer, poäng)
- Uppdatera data (redigera din profil)

### 📝 Sammanfattning

**Key Takeaways:**

- 🎯 **API = En meny av saker du kan be ett program göra**
  Precis som en restaurangmeny visar vad du kan beställa, visar ett API vad du kan fråga ett program om.

- 🚀 **FastAPI = En verktygslåda för att bygga API:er snabbt**
  Det hjälper programmerare att skapa API:er mycket snabbare än tidigare.

- 🔄 **API:er låter program prata med varandra**
  Din mobilapp kan prata med en server, servern kan prata med en databas, osv.

- 💬 **Du använder API:er varje dag**
  Varje gång du använder en app, chattar, spelar spel eller kollar vädret – du använder API:er!

- 📱 **API:er är som brevbärare**
  De tar dina frågor, levererar dem till rätt ställe, och tar tillbaka svaren.

**Ordlista (Nivå 1):**

- **API**: Ett sätt för program att prata med varandra
- **FastAPI**: Ett verktyg för att bygga API:er snabbt med Python
- **Förfrågan/Request**: En fråga du ställer till ett program
- **Svar/Response**: Det programmet skickar tillbaka till dig
- **Server**: En dator som väntar på frågor och skickar tillbaka svar
- **App**: Ett program du använder på din mobil eller dator

**Vad kommer härnäst?**

Nu när du förstår *vad* ett API är, är det dags att lära dig *hur* det fungerar tekniskt! I nästa nivå ska vi utforska webben, lära oss om HTTP, och börja förstå hur FastAPI faktiskt kommunicerar över internet. Vi kommer att lära oss ord som "endpoint", "JSON", och "klient/server" – och allt kommer bli glasklart!

---

## Nivå 2: Webben, HTTP och FastAPI-grunder 🧒

### Introduktion

Välkommen till nivå 2! Nu ska vi börja förstå hur webben faktiskt fungerar och hur FastAPI passar in i bilden. Du kommer att lära dig viktiga ord som **HTTP**, **JSON**, **endpoint**, och **klient/server**. Vi använder exempel från skola och fritid för att göra allt begripligt. I slutet av denna nivå kommer du att kunna förklara hur en webbläsare pratar med en server, och varför FastAPI är perfekt för att bygga moderna webb-API:er!

### Kärnkoncept

#### 1. **Klient och Server – Två viktiga roller**

Tänk på det som en konversation mellan två personer med olika roller:

- **Klient** = Den som frågar (t.ex. du, din webbläsare, en mobilapp)
- **Server** = Den som svarar (t.ex. en dator någonstans som har informationen du vill ha)

**Exempel från skolan:**
- Du (klient) frågar läraren (server): "Vad har vi för läxa?"
- Läraren (server) svarar: "Läs kapitel 5 i matteboken"

I datorrvärlden:
- Din webbläsare (klient) frågar Google.com (server): "Vad är vädret idag?"
- Google (server) svarar: "22°C och soligt"

#### 2. **HTTP – Språket för webben**

**HTTP** står för **HyperText Transfer Protocol**. Det är som ett gemensamt språk som klienter och servrar använder för att prata med varandra på internet.

Tänk på HTTP som **regler för en konversation**:
- Hur man ställer en fråga (request)
- Hur man svarar (response)
- Vilka typer av frågor man kan ställa

**Vardagsanalogi:**
När du ringer ett pizzaställe finns det regler:
1. Säg vad du vill beställa (GET = hämta information, POST = skicka ny information)
2. Ange din adress (URL)
3. Vänta på svar (server bearbetar)
4. Få bekräftelse eller pizza (response)

#### 3. **Request (Förfrågan) och Response (Svar)**

Varje gång något händer på webben är det en **request** och en **response**:

```
KLIENT                           SERVER
  │                                 │
  │──── REQUEST (Fråga) ────────▶  │
  │     "Ge mig hemsidan"           │
  │                                 │
  │                                 │ (Server tänker...)
  │                                 │
  │ ◀─── RESPONSE (Svar) ──────────│
  │     "Här är hemsidan!"          │
  │                                 │
```

**Verkligt exempel:**
- Du skriver "youtube.com" i webbläsaren → **REQUEST**
- YouTube skickar tillbaka hemsidan → **RESPONSE**

#### 4. **HTTP-metoder – Olika typer av frågor**

När du pratar med en server kan du göra olika saker. De vanligaste är:

**GET** – "Ge mig information" (hämta)
- Exempel: Visa mig en lista på alla filmer
- Som att fråga: "Vad har ni för glass?"

**POST** – "Ta emot ny information" (skapa)
- Exempel: Spara denna nya kommentar
- Som att säga: "Jag vill beställa en chokladglass"

**PUT** – "Uppdatera befintlig information" (ändra helt)
- Exempel: Ändra mitt lösenord
- Som att säga: "Byt ut min beställning till jordgubbsglass istället"

**DELETE** – "Ta bort information" (radera)
- Exempel: Ta bort mitt konto
- Som att säga: "Ångra min beställning"

**Tabell:**

| Metod    | Vad gör den?        | Exempel från skolan                        |
|----------|---------------------|--------------------------------------------|
| GET      | Hämtar information  | "Kan jag se schemat?"                      |
| POST     | Skapar något nytt   | "Här är min färdiga uppsats"               |
| PUT      | Uppdaterar allt     | "Jag vill ändra hela min uppsats"          |
| DELETE   | Tar bort något      | "Radera min gamla uppsats"                 |

#### 5. **URL och Endpoints**

**URL** (Uniform Resource Locator) är som en **adress** på internet:
- `https://youtube.com/videos` → Adressen till YouTubes videolista

En **endpoint** är en specifik adress där du kan göra något med API:et:
- `/videos` → Endpoint för att hämta videos
- `/users` → Endpoint för att hantera användare
- `/comments` → Endpoint för att hantera kommentarer

**Analogi:**
Tänk på ett stort köpcentrum:
- Köpcentret = API:et
- Varje butik = En endpoint
- "Leksaksaffären" = `/toys`
- "Bokhandeln" = `/books`

Varje butik (endpoint) gör olika saker!

#### 6. **JSON – Dataformat för webben**

**JSON** står för **JavaScript Object Notation**. Det är det vanligaste sättet att skicka data mellan klient och server.

JSON ser ut ungefär så här:

```json
{
  "namn": "Anna",
  "ålder": 10,
  "favoritfärg": "blå",
  "hobbies": ["fotboll", "läsa", "rita"]
}
```

Varför JSON?
- **Lätt att läsa** för människor
- **Lätt att förstå** för datorer
- **Fungerar överallt** (i alla programmeringsspråk)

**Analogi:**
JSON är som ett **ifyllt formulär**:
- "Namn: Anna"
- "Ålder: 10"
- "Favoritfärg: Blå"

Istället för att skriva en hel saga kan du bara ge kortfattad information i ett strukturerat format!

#### 7. **FastAPI och Python**

**Python** är ett programmeringsspråk (som svenska eller engelska, fast för datorer).
**FastAPI** är ett verktyg byggt med Python som gör det superenkelt att skapa API:er.

Varför är FastAPI bra?
- ⚡ **Snabbt** – Svarar på frågor blixtsnabbt
- 🎯 **Enkelt** – Du behöver inte skriva så mycket kod
- 🛡️ **Säkert** – Det hjälper dig undvika misstag
- 📖 **Självdokumenterande** – Det skapar automatiskt en beskrivning av ditt API

**Liknelse:**
Om Python är "språket", är FastAPI som en "mall" för att skriva brev snabbt. Istället för att komma på allt från början, använder du mallen!

#### 8. **Uvicorn – Servern som kör FastAPI**

För att din FastAPI-app ska fungera behöver du något som **startar servern**. Det är vad **uvicorn** gör.

**Analogi:**
- Din FastAPI-app = En bil
- Uvicorn = Motorn som får bilen att köra

Utan uvicorn står din app bara där. Med uvicorn börjar den "lyssna" på frågor från klienter!

### Exempel

#### Exempel 1: Fråga läraren om schema (GET)

**Scenario**: Du vill veta vad ni har för lektion imorgon.

**Verkliga världen:**
- Du (klient) går fram till läraren (server)
- Du frågar: "Vad har vi för lektion imorgon?" (GET request till `/schedule`)
- Läraren kollar i sitt häfte (databas)
- Läraren svarar: "Matematik klockan 9" (JSON response: `{"subject": "Matematik", "time": "09:00"}`)

**I API-termer:**
```
REQUEST:  GET /schedule
RESPONSE: {"subject": "Matematik", "time": "09:00"}
```

#### Exempel 2: Lämna in läxa (POST)

**Scenario**: Du har gjort din läxa och vill lämna in den.

**Verkliga världen:**
- Du (klient) går till läraren (server)
- Du säger: "Här är min läxa!" och ger papper (POST request med data)
- Läraren tar emot och lägger i sin pärm (sparar i databas)
- Läraren säger: "Tack, mottaget!" (response: `{"status": "success"}`)

**I API-termer:**
```
REQUEST:  POST /homework
BODY:     {"student": "Anna", "subject": "Matte", "content": "Uppgift 1-10"}
RESPONSE: {"status": "success", "message": "Läxa mottagen"}
```

#### Exempel 3: En komplett webbsida-förfrågan

Låt säga du vill kolla Instagram:

1. **Du skriver**: `instagram.com` i webbläsaren
2. **Webbläsaren skickar**: HTTP GET request till Instagrams server
3. **Servern tänker**: "Okej, denna användare vill se startsidan"
4. **Servern svarar**: Skickar tillbaka HTML, bilder, och data (som JSON)
5. **Webbläsaren visar**: Allt för dig på skärmen

Bakom kulisserna händer **hundratals** requests – för varje bild, varje kommentar, varje "like"!

### Visualiseringar

#### Diagram 1: Klient-Server-modellen

```
┌──────────────────┐                      ┌──────────────────┐
│                  │                      │                  │
│  KLIENT          │                      │  SERVER          │
│                  │                      │                  │
│  • Webbläsare    │  ──── REQUEST ────▶ │  • FastAPI-app   │
│  • Mobilapp      │                      │  • Databas       │
│  • Annat program │  ◀─── RESPONSE ───  │  • Logik         │
│                  │                      │                  │
└──────────────────┘                      └──────────────────┘

     Frågar om data                         Skickar tillbaka data
```

#### Diagram 2: HTTP Request/Response-cykeln

```
1. ANVÄNDARE                 2. KLIENT                3. SERVER
   │                            │                         │
   │ Klickar på                 │                         │
   │ "Visa profil"              │                         │
   │ ─────────────────────────▶ │                         │
                                │ GET /profile/anna       │
                                │ ──────────────────────▶ │
                                │                         │
                                │                         │ (Hämtar data)
                                │                         │
                                │ {"name": "Anna", ...}   │
                                │ ◀──────────────────────│
   │                            │                         │
   │ Ser sin profil             │                         │
   │ ◀─────────────────────────│                         │
   │                            │                         │
```

#### Diagram 3: HTTP-metoder i praktiken

```
┌─────────────────────────────────────────────────────────────┐
│              FYRA VANLIGASTE HTTP-METODER                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📖 GET /books          →  "Ge mig alla böcker"             │
│     Response: [{"title": "Harry Potter"}, {...}]            │
│                                                              │
│  ➕ POST /books         →  "Lägg till en ny bok"            │
│     Body: {"title": "Nya boken"}                            │
│     Response: {"status": "created", "id": 123}              │
│                                                              │
│  ✏️ PUT /books/123      →  "Uppdatera bok #123"             │
│     Body: {"title": "Uppdaterad titel"}                     │
│     Response: {"status": "updated"}                         │
│                                                              │
│  🗑️ DELETE /books/123   →  "Ta bort bok #123"               │
│     Response: {"status": "deleted"}                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### Diagram 4: JSON-exempel

```
En person beskriven i JSON:

{
  "namn": "Erik",
  "ålder": 12,
  "skola": "Lundaskolan",
  "ämnen": ["Matte", "Engelska", "Idrott"],
  "favoritmat": {
    "huvudrätt": "Pizza",
    "dessert": "Glass"
  }
}

Lägg märke till:
• { } betyder ett objekt (en sak med egenskaper)
• [ ] betyder en lista (flera saker)
• "nyckel": "värde" – varje egenskap har ett namn och ett värde
```

### 💡 Pro Tips

#### Tip 1: GET förändrar ingenting, POST gör det
När du använder **GET**, hämtar du bara information – inget ändras på servern. När du använder **POST**, skapar eller ändrar du något. Därför kan du trycka "uppdatera" i webbläsaren (GET) hur många gånger du vill, men om du "submittar" ett formulär (POST) flera gånger skapar du flera kopior!

#### Tip 2: JSON är som ett recept
Precis som ett recept har en struktur ("Ingredienser", "Steg 1", "Steg 2"), har JSON en struktur med nycklar och värden. Detta gör det enkelt för både människor och datorer att förstå!

#### Tip 3: FastAPI ger dig superkrafter
Innan FastAPI fanns (och liknande verktyg) tog det mycket längre tid att bygga API:er. Du var tvungen att själv kolla att all data var korrekt, skriva dokumentation, och mycket mer. FastAPI gör allt detta automatiskt! Det är som att ha en assistent som hjälper dig med de tråkiga delarna.

### ✏️ Övningar

#### Övning 1: Förklara med egna ord
**Uppgift**: Förklara med egna ord vad ett "endpoint" är. Använd en analogi från ditt eget liv (skola, hem, fritid).

**Facit**:
Ett endpoint är som en **specifik avdelning i en butik**. Om butiken är API:et, så är "leksaksavdelningen" ett endpoint (`/toys`), "bokavdelningen" ett annat endpoint (`/books`), och "kassan" ännu ett (`/checkout`). Varje endpoint har ett specifikt jobb!

Ett annat svar: Ett endpoint är som **olika frågor du kan ställa till en person**. "Vad heter du?" är ett endpoint, "Hur gammal är du?" är ett annat. Varje fråga (endpoint) ger olika svar!

#### Övning 2: Klient vs Server
**Uppgift**: För varje scenario, identifiera vad som är klienten och vad som är servern:

a) Du kollar vädret på din mobil
b) Du spelar ett onlinespel
c) Du laddar upp en bild på Instagram
d) Du googlar "bästa pizzan i Stockholm"

**Facit**:
a) **Klient**: Väder-appen på din mobil | **Server**: Väder-företagets dator som har väderdata
b) **Klient**: Spelappen på din dator/konsol | **Server**: Spelföretagets server som kör spelet
c) **Klient**: Instagram-appen på din mobil | **Server**: Instagrams server som sparar bilden
d) **Klient**: Din webbläsare | **Server**: Googles sökserver

#### Övning 3: JSON-data
**Uppgift**: Skapa JSON-data som beskriver din favoritfilm. Inkludera:
- Titel
- År
- Regissör
- Skådespelare (lista)
- Betyg (1-5)

**Facit**:
```json
{
  "titel": "Harry Potter och De Vises Sten",
  "år": 2001,
  "regissör": "Chris Columbus",
  "skådespelare": [
    "Daniel Radcliffe",
    "Emma Watson",
    "Rupert Grint"
  ],
  "betyg": 5
}
```

Viktiga detaljer:
- Text omges av citattecken: `"text här"`
- Nummer behöver inga citattecken: `2001` eller `5`
- Listor använder hakparenteser: `[item1, item2]`
- Varje rad (utom sista) slutar med komma

#### Övning 4: Rita ett flödesschema
**Uppgift**: Rita ett enkelt flödesschema som visar vad som händer när du klickar på "Gilla" på Instagram. Inkludera: Klient → Request → Server → Databas → Response → Klient.

**Facit**:
```
1. Du klickar "Gilla" ❤️
   │
   ↓
2. Instagram-appen (KLIENT) skickar:
   POST /like
   Body: {"post_id": 12345, "user_id": 67890}
   │
   ↓
3. Instagrams SERVER tar emot requesten
   │
   ↓
4. Servern sparar i DATABASEN:
   "User 67890 gillade post 12345"
   │
   ↓
5. Servern skickar RESPONSE:
   {"status": "success", "likes": 143}
   │
   ↓
6. Appen (KLIENT) visar:
   "143 personer gillar detta" ❤️
```

#### Övning 5: Frågesport
**Uppgift**: Svara på följande frågor:

1. Vilket HTTP-verb använder du för att hämta information?
2. Vad står JSON för?
3. Vad är en URL?
4. Vilken del av en URL är endpointet i: `https://api.example.com/users/123`?
5. Vad är skillnaden mellan en klient och en server?

**Facit**:
1. **GET** – För att hämta/läsa information
2. **JavaScript Object Notation** – Ett format för att strukturera data
3. **Uniform Resource Locator** – En adress på internet (som "husadress för en webbsida")
4. `/users/123` – Detta är endpointet (allt efter domännamnet)
5. **Klient** = Den som frågar (appen, webbläsaren) | **Server** = Den som svarar (datorn som har informationen)

### 📝 Sammanfattning

**Key Takeaways:**

- 🔄 **Klient och Server är två roller i en konversation**
  Klienten frågar, servern svarar. Din webbläsare är klient, webbplatsen ligger på en server.

- 🌐 **HTTP är webben språk**
  Det är reglerna för hur klienter och servrar pratar med varandra. Alla på internet använder HTTP.

- 📨 **Request och Response är grundläggande**
  Varje interaktion på webben är en request (fråga) följd av en response (svar).

- 🔤 **GET, POST, PUT, DELETE är olika typer av frågor**
  GET = hämta, POST = skapa, PUT = uppdatera, DELETE = ta bort.

- 📍 **En URL är en adress, ett endpoint är en specifik plats**
  URL: `https://api.com/users` där `/users` är endpointet.

- 📊 **JSON är det vanligaste dataformatet**
  Det är enkelt, läsbart, och fungerar överallt. Tänk på det som ett ifyllt formulär.

- ⚡ **FastAPI + Python gör det enkelt att bygga API:er**
  Du skriver mindre kod och får mer funktionalitet automatiskt.

- 🚀 **Uvicorn kör din FastAPI-app**
  Det är motorn som startar servern och låter den ta emot requests.

**Ordlista (Nivå 2):**

- **HTTP**: HyperText Transfer Protocol – Språket för kommunikation på webben
- **Request**: En förfrågan från klient till server
- **Response**: Svaret från server tillbaka till klient
- **Klient**: Den som frågar (t.ex. webbläsare, app)
- **Server**: Den som svarar (en dator som kör din FastAPI-app)
- **GET**: HTTP-metod för att hämta information
- **POST**: HTTP-metod för att skicka/skapa ny information
- **PUT**: HTTP-metod för att uppdatera befintlig information
- **DELETE**: HTTP-metod för att ta bort information
- **URL**: Uniform Resource Locator – En adress på internet
- **Endpoint**: En specifik adress i ett API där du kan göra något (t.ex. `/users`)
- **JSON**: JavaScript Object Notation – Ett format för att strukturera data
- **Python**: Ett programmeringsspråk
- **FastAPI**: Ett verktyg för att bygga API:er med Python
- **Uvicorn**: En server som kör FastAPI-applikationer

**Vad kommer härnäst?**

Nu när du förstår grunderna i HTTP, JSON, och hur klient/server fungerar, är det dags att **skriva din första riktiga FastAPI-app**! I nästa nivå kommer du att:
- Installera FastAPI och uvicorn
- Skriva din första endpoint
- Skicka och ta emot JSON-data
- Köra din egen server på din dator
- Testa ditt API i webbläsaren

Det blir praktiskt och kul – du kommer faktiskt **bygga något** som fungerar! 🚀

---

## Nivå 3: Bygga dina första FastAPI-endpoints 🎓

### Introduktion

Välkommen till nivå 3 – nu blir det praktiskt! I denna nivå kommer du att lära dig hur FastAPI faktiskt fungerar genom att skriva riktig kod. Du kommer att installera FastAPI, skapa din första applikation, bygga endpoints för GET och POST, arbeta med Pydantic-modeller för datavalidering, och köra din egen server. I slutet av denna nivå kommer du att ha en fungerande FastAPI-applikation som du kan testa i din webbläsare!

**Vad du behöver**: En dator med Python 3.8+ installerat.

### Kärnkoncept

#### 1. **Installation av FastAPI och Uvicorn**

För att komma igång behöver du installera två paket:
- **FastAPI** – Själva ramverket
- **Uvicorn** – ASGI-servern som kör din app

**Med pip (rekommenderat för nybörjare):**

```bash
# Installera FastAPI med alla standardberoenden (inklusive uvicorn)
pip install "fastapi[standard]"

# Alternativt: minimal installation
pip install fastapi uvicorn
```

**Med Poetry (för mer avancerad projekthantering):**

```bash
# Skapa ett nytt projekt
poetry init

# Lägg till FastAPI och Uvicorn
poetry add "fastapi[standard]"
```

**Verifiera installationen:**
```bash
python -c "import fastapi; print(fastapi.__version__)"
```

#### 2. **Din första FastAPI-applikation**

Skapa en fil som heter `main.py`:

```python
# main.py
from fastapi import FastAPI

# Skapa en FastAPI-applikation
app = FastAPI()

# Definiera din första endpoint
@app.get("/")
def read_root():
    return {"message": "Hej från FastAPI!"}
```

**Förklaring:**
- `from fastapi import FastAPI` → Importerar FastAPI-klassen
- `app = FastAPI()` → Skapar en instans av applikationen
- `@app.get("/")` → En **dekorator** som säger "När någon gör en GET-request till `/`, kör denna funktion"
- `return {"message": "..."}` → Python-dictionary blir automatiskt JSON!

#### 3. **Köra servern med Uvicorn**

```bash
# Starta utvecklingsservern
uvicorn main:app --reload

# Förklaring:
# main      → namnet på filen (main.py)
# app       → namnet på FastAPI-instansen (app = FastAPI())
# --reload  → Servern startar om automatiskt när du ändrar kod
```

**Output du ser:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Öppna din webbläsare** och gå till: `http://127.0.0.1:8000`

Du kommer se:
```json
{"message": "Hej från FastAPI!"}
```

🎉 **Grattis!** Din första API-endpoint fungerar!

#### 4. **Automatisk dokumentation**

FastAPI genererar automatiskt interaktiv API-dokumentation! Gå till:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

Här kan du se alla dina endpoints och **testa dem direkt i webbläsaren**!

#### 5. **GET-endpoints med Path Parameters**

Låt oss lägga till en endpoint som hämtar information om en specifik användare:

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hej från FastAPI!"}

# Ny endpoint med path parameter
@app.get("/users/{user_id}")
def read_user(user_id: int):
    """
    Hämtar information om en användare baserat på ID.

    user_id: Ett heltal som identifierar användaren
    """
    return {
        "user_id": user_id,
        "name": f"Användare #{user_id}",
        "status": "aktiv"
    }
```

**Förklaring:**
- `{user_id}` i path → En **path parameter** (dynamisk del av URL:en)
- `user_id: int` → FastAPI validerar automatiskt att det är ett heltal!
- Om du försöker med `http://127.0.0.1:8000/users/abc` får du ett valideringsfel

**Testa:**
- Gå till `http://127.0.0.1:8000/users/42`
- Resultat: `{"user_id": 42, "name": "Användare #42", "status": "aktiv"}`

#### 6. **GET-endpoints med Query Parameters**

Query parameters är de parametrar som kommer efter `?` i en URL:

```python
# Lägg till i main.py
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    """
    Hämtar en lista av items med paginering.

    skip: Antal items att hoppa över (standard: 0)
    limit: Max antal items att returnera (standard: 10)
    """
    return {
        "skip": skip,
        "limit": limit,
        "items": [f"Item {i}" for i in range(skip, skip + limit)]
    }
```

**Testa:**
- `http://127.0.0.1:8000/items/` → Använder standardvärden (skip=0, limit=10)
- `http://127.0.0.1:8000/items/?skip=5&limit=3` → Hoppar över 5, hämtar 3

#### 7. **Pydantic-modeller för datavalidering**

**Pydantic** är ett kraftfullt bibliotek för datavalidering. När du tar emot data från klienter (t.ex. POST-requests), använder du Pydantic-modeller för att säkerställa att datan är korrekt.

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

# Definiera en Pydantic-modell
class User(BaseModel):
    """
    Modell för en användare.
    """
    name: str = Field(..., min_length=1, max_length=50, description="Användarens namn")
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$", description="Giltig e-postadress")
    age: Optional[int] = Field(None, ge=0, le=150, description="Ålder (0-150)")
    is_active: bool = Field(True, description="Om användaren är aktiv")

    # Exempel på hur modellen ser ut
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Anna Andersson",
                "email": "anna@example.com",
                "age": 25,
                "is_active": True
            }
        }
```

**Förklaring av Field:**
- `...` → Obligatoriskt fält (krävs)
- `min_length`, `max_length` → Validering av stränglängd
- `pattern` → Regex-validering (för email)
- `Optional[int]` → Fältet kan vara `None`
- `ge` (greater or equal), `le` (less or equal) → Numerisk validering
- `description` → Förklaring som visas i dokumentationen

**Viktigt om Pydantic v2:**
- `Optional[str]` betyder att värdet kan vara `None`, men fältet är fortfarande **obligatoriskt**
- För att göra ett fält **frivilligt**, använd: `age: int | None = None` eller `Field(default=None)`

#### 8. **POST-endpoint för att skapa data**

Nu använder vi vår Pydantic-modell i en POST-endpoint:

```python
# Lägg till i main.py
@app.post("/users/")
def create_user(user: User):
    """
    Skapar en ny användare.

    Tar emot JSON-data som valideras mot User-modellen.
    """
    # I verkligheten skulle du spara till databas här
    return {
        "status": "success",
        "message": f"Användare {user.name} skapad!",
        "user": user
    }
```

**Testa med curl:**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Anna Andersson",
    "email": "anna@example.com",
    "age": 25,
    "is_active": true
  }'
```

**Eller använd Swagger UI** (`/docs`) och tryck på "Try it out"!

**Vad händer vid fel data?**
```bash
# Felaktig email
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Anna",
    "email": "inte-en-email",
    "age": 25
  }'
```

FastAPI returnerar automatiskt ett **422 Unprocessable Entity** fel med detaljer:
```json
{
  "detail": [
    {
      "type": "string_pattern_mismatch",
      "loc": ["body", "email"],
      "msg": "String should match pattern '^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$'",
      "input": "inte-en-email"
    }
  ]
}
```

#### 9. **Async vs Sync – Grundläggande förklaring**

FastAPI stödjer både **synkron** (`def`) och **asynkron** (`async def`) kod.

**Synkron (def):**
```python
@app.get("/sync")
def sync_endpoint():
    # Blockerar tråden medan den körs
    return {"type": "sync"}
```

**Asynkron (async def):**
```python
@app.get("/async")
async def async_endpoint():
    # Låter andra requests köras samtidigt
    return {"type": "async"}
```

**När ska du använda async?**
- ✅ **Använd `async def`** när du gör I/O-operationer (databas, API-anrop, filläsning)
- ❌ **Använd inte `async def`** för CPU-tunga operationer (komplexa beräkningar)
- 🆗 **Använd `def`** om du är osäker – FastAPI hanterar det ändå bra!

**Exempel med async:**
```python
import asyncio

@app.get("/slow")
async def slow_endpoint():
    # Simulerar en långsam operation (t.ex. databasanrop)
    await asyncio.sleep(2)  # Vänta 2 sekunder utan att blockera
    return {"message": "Färdig efter 2 sekunder"}
```

**Viktig regel**: Om du använder `async def`, måste du använda `await` för I/O-operationer!

#### 10. **Response models – Styra vad som returneras**

Du kan specificera exakt vilken data som ska returneras:

```python
# Modell för vad vi tar emot
class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # Kommer inte synas i response!

# Modell för vad vi returnerar
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    # Notera: password finns INTE här!

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    # Simulera att skapa användare med ID
    return {
        "id": 123,
        "name": user.name,
        "email": user.email,
        "password": user.password  # Detta filtreras bort!
    }
```

**Resultat**: Även om vi returnerar `password`, kommer FastAPI automatiskt filtrera bort det eftersom `UserResponse` inte innehåller det fältet!

### Exempel

#### Exempel 1: Komplett minimal app

```python
# minimal_app.py
from fastapi import FastAPI

app = FastAPI(
    title="Min första API",
    description="Ett enkelt exempel-API",
    version="1.0.0"
)

@app.get("/")
def root():
    """Välkomstsida"""
    return {"message": "Välkommen till mitt API!"}

@app.get("/hello/{name}")
def hello(name: str):
    """Hälsa på någon"""
    return {"message": f"Hej {name}!"}

# Kör med: uvicorn minimal_app:app --reload
```

#### Exempel 2: TODO-lista API

```python
# todo_app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="TODO API")

# Modeller
class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    completed: bool = False

class Todo(TodoCreate):
    id: int

# "Databas" (bara en lista i minnet)
todos: List[Todo] = []
next_id: int = 1

# Endpoints
@app.get("/todos", response_model=List[Todo])
def get_todos():
    """Hämta alla todos"""
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """Hämta en specifik todo"""
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo hittades inte")

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    """Skapa en ny todo"""
    global next_id
    new_todo = Todo(id=next_id, **todo.model_dump())
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_update: TodoCreate):
    """Uppdatera en todo"""
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            updated = Todo(id=todo_id, **todo_update.model_dump())
            todos[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Todo hittades inte")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Ta bort en todo"""
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[i]
            return {"message": "Todo borttagen"}
    raise HTTPException(status_code=404, detail="Todo hittades inte")

# Kör med: uvicorn todo_app:app --reload
```

#### Exempel 3: Före och efter validering

**Utan FastAPI/Pydantic (manuell validering):**
```python
# Utan FastAPI - mycket kod!
def create_user_manual(data: dict):
    # Manuell validering
    if "name" not in data:
        return {"error": "name saknas"}
    if not isinstance(data["name"], str):
        return {"error": "name måste vara en sträng"}
    if len(data["name"]) < 1:
        return {"error": "name kan inte vara tom"}
    if "email" not in data:
        return {"error": "email saknas"}
    # ... 20 rader till validering ...

    return {"status": "ok", "data": data}
```

**Med FastAPI/Pydantic (automatisk validering):**
```python
# Med FastAPI - allt automatiskt!
class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: str

@app.post("/users")
def create_user(user: User):
    return {"status": "ok", "data": user}
# FastAPI gör ALL validering automatiskt!
```

### Visualiseringar

#### Diagram 1: Request-flöde i FastAPI

```
   KLIENT                  FASTAPI                  DIN KOD
     │                        │                        │
     │  POST /users           │                        │
     │  {"name": "Anna"}      │                        │
     ├───────────────────────→│                        │
     │                        │                        │
     │                        │ 1. Validera med        │
     │                        │    Pydantic-modell     │
     │                        │                        │
     │                        │    ✓ Giltig data!      │
     │                        │                        │
     │                        ├───────────────────────→│
     │                        │   Anropa din funktion  │
     │                        │   create_user(user)    │
     │                        │                        │
     │                        │←───────────────────────│
     │                        │   Return data          │
     │                        │                        │
     │                        │ 2. Serialisera till    │
     │                        │    JSON                │
     │                        │                        │
     │←───────────────────────│                        │
     │  200 OK                │                        │
     │  {"status": "success"} │                        │
     │                        │                        │
```

#### Diagram 2: Projektstruktur för nybörjare

```
my-fastapi-project/
│
├── main.py              # Din FastAPI-applikation
├── requirements.txt     # Lista över dependencies
│   └── fastapi[standard]
│   └── uvicorn
│
└── README.md           # Beskrivning av projektet
```

#### Diagram 3: Pydantic-validering

```
┌──────────────────────────────────────────────────────┐
│           PYDANTIC VALIDERAR AUTOMATISKT              │
├──────────────────────────────────────────────────────┤
│                                                       │
│  Input:  {"name": "Anna", "age": "25"}               │
│           │                                           │
│           ▼                                           │
│  Pydantic BaseModel                                   │
│    ┌─────────────────────────────┐                   │
│    │ name: str                    │ ✓ "Anna" är str  │
│    │ age: int                     │ ✓ "25" → 25 (konv)│
│    │ email: str                   │ ✗ SAKNAS!        │
│    └─────────────────────────────┘                   │
│           │                                           │
│           ▼                                           │
│  Resultat: ValidationError                            │
│  {                                                    │
│    "detail": [                                        │
│      {                                                │
│        "loc": ["body", "email"],                     │
│        "msg": "field required"                       │
│      }                                                │
│    ]                                                  │
│  }                                                    │
└──────────────────────────────────────────────────────┘
```

#### Diagram 4: GET vs POST

```
┌─────────────────────────────────────────────────┐
│                 GET vs POST                     │
├─────────────────────────────────────────────────┤
│                                                  │
│  GET /users/123                                 │
│  ├─ Path parameter: user_id=123                │
│  ├─ Query params: ?limit=10&skip=5             │
│  ├─ Ingen request body                         │
│  └─ Säkert att anropa flera gånger             │
│                                                  │
│  POST /users                                    │
│  ├─ Request body: {"name": "Anna", ...}        │
│  ├─ Skapar nya resurser                        │
│  ├─ Ändrar server-state                        │
│  └─ Inte idempotent (flera anrop = flera objekt)│
│                                                  │
└─────────────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Tip 1: Använd `--reload` bara under utveckling
Flaggan `--reload` gör att servern startar om vid varje koändring. Det är perfekt under utveckling, men använd **ALDRIG** detta i produktion! I produktion kör du utan `--reload`.

#### Tip 2: Testa dina endpoints i Swagger UI
Istället för att skriva curl-kommandon eller använda externa verktyg, använd den inbyggda dokumentationen på `/docs`. Där kan du testa alla endpoints direkt med ett grafiskt gränssnitt!

#### Tip 3: Pydantic gör typkonvertering automatiskt
Om du skickar `{"age": "25"}` (sträng) och din modell säger `age: int`, kommer Pydantic automatiskt konvertera `"25"` → `25`. Men om du skickar `{"age": "tjugofem"}` får du ett valideringsfel!

#### Tip 4: Använd beskrivande endpoint-namn
Istället för `/get_user_by_id`, använd `/users/{user_id}`. RESTful konventioner gör ditt API lättare att förstå!

#### Tip 5: HTTPException för felhantering
Använd `raise HTTPException(status_code=404, detail="Hittades inte")` för att returnera HTTP-fel med rätt statuskod.

### ✏️ Övningar

#### Övning 1: Skapa en "Hej"-endpoint
**Uppgift**: Skapa en ny FastAPI-app med en GET-endpoint `/hej` som returnerar `{"message": "Hej på dig!"}`.

**Facit**:
```python
# hej_app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hej")
def say_hello():
    return {"message": "Hej på dig!"}

# Kör med: uvicorn hej_app:app --reload
# Testa: http://127.0.0.1:8000/hej
```

#### Övning 2: POST-endpoint med Pydantic
**Uppgift**: Skapa en Pydantic-modell `Book` med fälten:
- `title`: str (obligatorisk, minst 1 tecken)
- `author`: str (obligatorisk)
- `year`: int (frivillig, mellan 1000 och 2100)
- `pages`: int (frivillig, minst 1)

Skapa sedan en POST-endpoint `/books` som tar emot en bok och returnerar den med ett meddelande.

**Facit**:
```python
# books_app.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(...)
    year: Optional[int] = Field(None, ge=1000, le=2100)
    pages: Optional[int] = Field(None, ge=1)

@app.post("/books")
def create_book(book: Book):
    return {
        "message": f"Boken '{book.title}' av {book.author} mottagen!",
        "book": book
    }

# Testa med:
# curl -X POST "http://127.0.0.1:8000/books" \
#   -H "Content-Type: application/json" \
#   -d '{"title": "1984", "author": "George Orwell", "year": 1949, "pages": 328}'
```

#### Övning 3: Query-parameter
**Uppgift**: Skapa en GET-endpoint `/greet` som tar en query-parameter `name` (standard: "Vän") och returnerar en hälsning.

**Exempel**:
- `/greet` → `{"message": "Hej Vän!"}`
- `/greet?name=Anna` → `{"message": "Hej Anna!"}`

**Facit**:
```python
@app.get("/greet")
def greet(name: str = "Vän"):
    return {"message": f"Hej {name}!"}
```

#### Övning 4: Path parameter med validering
**Uppgift**: Skapa en GET-endpoint `/square/{number}` som returnerar kvadraten av ett nummer. Numret ska vara mellan 1 och 100.

**Facit**:
```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/square/{number}")
def get_square(number: int = Path(..., ge=1, le=100)):
    return {
        "number": number,
        "square": number ** 2
    }

# Testa:
# http://127.0.0.1:8000/square/5  → {"number": 5, "square": 25}
# http://127.0.0.1:8000/square/101 → Valideringsfel!
```

#### Övning 5: In-memory databas (mini-projekt)
**Uppgift**: Bygg ett enkelt "användare-API" med:
- GET `/users` → Lista alla användare
- GET `/users/{user_id}` → Hämta specifik användare
- POST `/users` → Skapa ny användare (använd Pydantic-modell)
- En lista i minnet som "databas"

**Facit**:
```python
# users_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modell
class User(BaseModel):
    name: str
    email: str
    age: Optional[int] = None

class UserInDB(User):
    id: int

# "Databas"
users_db: List[UserInDB] = []
next_id = 1

# Endpoints
@app.get("/users", response_model=List[UserInDB])
def get_all_users():
    return users_db

@app.get("/users/{user_id}", response_model=UserInDB)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Användare hittades inte")

@app.post("/users", response_model=UserInDB, status_code=201)
def create_user(user: User):
    global next_id
    new_user = UserInDB(id=next_id, **user.model_dump())
    users_db.append(new_user)
    next_id += 1
    return new_user

# Kör med: uvicorn users_api:app --reload
```

#### Övning 6: Testa med webbläsare och curl
**Uppgift**: För appen i Övning 5:
1. Öppna `/docs` och testa att skapa 3 användare
2. Använd curl för att hämta alla användare
3. Använd webbläsaren för att hämta användare #2

**Facit**:
```bash
# Skapa användare
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"name": "Anna", "email": "anna@example.com", "age": 25}'

# Hämta alla användare
curl "http://127.0.0.1:8000/users"

# Webbläsare: http://127.0.0.1:8000/users/2
```

#### Övning 7 (Bonus): Identifiera och rätta fel
**Uppgift**: Denna kod har flera problem. Hitta och rätta dem:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/items")
def create_item(item):  # Problem 1: Ingen type hint
    if item.price < 0:  # Problem 2: Validering i funktion istället för modell
        return {"error": "Pris kan inte vara negativt"}
    return item

@app.get("/items/{item_id}")
def get_item(item_id):  # Problem 3: Ingen type hint
    return {"id": item_id}
```

**Facit**:
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Pris måste vara positivt")  # Fix: Validering i modell
    quantity: int = Field(..., ge=0, description="Antal måste vara 0 eller mer")

@app.post("/items")
def create_item(item: Item):  # Fix: Lägg till type hint
    # Nu behövs ingen manuell validering - Pydantic gör det!
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):  # Fix: Lägg till type hint
    return {"id": item_id}
```

**Förklaring av fixes:**
1. **Type hints**: Lägg till `item: Item` och `item_id: int` så FastAPI vet vad som förväntas
2. **Validering i modell**: Använd `Field(gt=0)` istället för att kolla manuellt i funktionen
3. **Automatisk dokumentation**: Med type hints blir dokumentationen på `/docs` korrekt

### 📝 Sammanfattning

**Key Takeaways:**

- 📦 **Installation**: `pip install "fastapi[standard]"` ger dig allt du behöver

- 🚀 **Kör servern**: `uvicorn main:app --reload` startar utvecklingsservern

- 📖 **Gratis dokumentation**: Gå till `/docs` för interaktiv Swagger UI

- 🎯 **Endpoints är enkla**: `@app.get("/path")` för GET, `@app.post("/path")` för POST

- 🔍 **Path parameters**: `/users/{user_id}` låter dig ha dynamiska URL:er

- ❓ **Query parameters**: `/items?skip=5&limit=10` för filtrera och paginera

- ✅ **Pydantic är magi**: Definiera en `BaseModel` och få automatisk validering, serialisering och dokumentation

- 🛡️ **Validering är automatisk**: FastAPI + Pydantic validerar all in- och utdata åt dig

- ⚡ **Async är valfritt**: Använd `async def` för I/O-operationer, `def` för resten

- 🎁 **Response models**: Kontrollera exakt vad som returneras med `response_model`

**Ordlista (Nivå 3):**

- **ASGI**: Asynchronous Server Gateway Interface – Standard för async Python-webapps
- **Uvicorn**: En snabb ASGI-server som kör FastAPI-appar
- **Path parameter**: Dynamisk del av URL:en, t.ex. `/users/{user_id}`
- **Query parameter**: Parameter efter `?` i URL:en, t.ex. `?limit=10`
- **Pydantic**: Bibliotek för datavalidering och serialisering
- **BaseModel**: Basklass för Pydantic-modeller
- **Field**: Funktion för att lägga till validering och metadata till fält
- **Decorator**: `@app.get(...)` som "dekorerar" en funktion och gör den till en endpoint
- **Response model**: Pydantic-modell som definierar vad en endpoint returnerar
- **Swagger UI**: Interaktivt gränssnitt för att testa API:er (finns på `/docs`)
- **ReDoc**: Alternativ dokumentation (finns på `/redoc`)
- **HTTPException**: Klass för att returnera HTTP-fel med statuskoder

**Vad kommer härnäst?**

Nu när du kan bygga grundläggande endpoints och validera data, är det dags att lära dig hur man bygger **riktigt stora applikationer**! I nästa nivå kommer vi att utforska:

- Hur man strukturerar ett större projekt med flera filer
- APIRouter för att dela upp endpoints i moduler
- Dependency Injection för att återanvända kod
- Databaskopplingar
- Felhantering på global nivå
- Bakgrundsjobb
- Best practices och anti-patterns

Det blir universitetsnivå – men oroa dig inte, vi tar det steg för steg! 🎓

---

## Nivå 4: Arkitektur, beroenden och best practices 🏛️

### Introduktion

Välkommen till nivå 4 – universitetsnivå! Nu ska vi bygga **riktiga, professionella applikationer**. Du kommer att lära dig hur man strukturerar större projekt, använder Dependency Injection för återanvändbar kod, hanterar fel elegant, kör bakgrundsjobb, och mycket mer. I slutet av denna nivå kommer du att kunna bygga produktionsklar kod med best practices från 2025. Det här är steget från "hobbyist" till "professionell utvecklare"!

### Kärnkoncept

#### 1. **Projektstruktur för större applikationer**

När ditt projekt växer blir det snabbt rörigt att ha allt i en fil. Här är en beprövad struktur:

```
my_fastapi_project/
│
├── app/
│   ├── __init__.py
│   ├── main.py                 # Huvudapplikation
│   ├── config.py               # Konfiguration
│   ├── dependencies.py         # Gemensamma dependencies
│   │
│   ├── routers/                # En router per domän
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── items.py
│   │   └── auth.py
│   │
│   ├── schemas/                # Pydantic-modeller (request/response)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── models/                 # Databasmodeller (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── services/               # Affärslogik
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   │
│   ├── db/                     # Databas-relaterat
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   └── core/                   # Kärnfunktionalitet
│       ├── __init__.py
│       ├── security.py
│       └── errors.py
│
├── tests/                      # Tester
│   ├── __init__.py
│   ├── test_users.py
│   └── test_items.py
│
├── alembic/                    # Databasmigrationer (om du använder SQLAlchemy)
│
├── .env                        # Miljövariabler (gitignore detta!)
├── .env.example                # Exempel på miljövariabler
├── requirements.txt            # Dependencies
├── pyproject.toml              # Poetry config (alternativ)
└── README.md
```

**Viktiga principer:**
- **Separation of concerns**: Varje del har ett specifikt ansvar
- **Schemas vs Models**: Schemas = API (Pydantic), Models = Databas (SQLAlchemy)
- **Services**: Affärslogik separerad från endpoints
- **Routers**: Gruppera relaterade endpoints

#### 2. **APIRouter – Modulär struktur**

**APIRouter** låter dig dela upp dina endpoints i separata filer och sedan kombinera dem.

**Exempel: `app/routers/users.py`**
```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.user import User, UserCreate, UserResponse
from ..services.user_service import UserService

# Skapa en router för användare
router = APIRouter(
    prefix="/users",           # Alla endpoints börjar med /users
    tags=["users"],            # Gruppering i dokumentation
    responses={404: {"description": "Inte hittad"}},
)

# Fake databas för demo
fake_users_db = []

@router.get("/", response_model=List[UserResponse])
def get_all_users():
    """Hämta alla användare"""
    return fake_users_db

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Hämta en specifik användare"""
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Användare hittades inte")

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """Skapa en ny användare"""
    new_user = {
        "id": len(fake_users_db) + 1,
        **user.model_dump()
    }
    fake_users_db.append(new_user)
    return new_user
```

**Exempel: `app/routers/items.py`**
```python
from fastapi import APIRouter
from typing import List

router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.get("/")
def get_all_items():
    """Hämta alla items"""
    return [{"id": 1, "name": "Item 1"}]

@router.get("/{item_id}")
def get_item(item_id: int):
    """Hämta specifik item"""
    return {"id": item_id, "name": f"Item {item_id}"}
```

**Huvudfil: `app/main.py`**
```python
from fastapi import FastAPI
from .routers import users, items

# Skapa applikationen
app = FastAPI(
    title="Min Modulära API",
    description="API med flera routers",
    version="2.0.0"
)

# Inkludera routers
app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Välkommen till API:et"}

# Nu finns endpoints:
# /users/         (från users.router)
# /users/{id}     (från users.router)
# /items/         (från items.router)
# /items/{id}     (från items.router)
```

**Kör med:**
```bash
uvicorn app.main:app --reload
```

#### 3. **Dependency Injection – Återanvändbar kod**

Dependency Injection (DI) är ett av FastAPI:s mest kraftfulla features. Det låter dig:
- Återanvända kod
- Testa lättare (mocka dependencies)
- Separera concerns
- Cachea resultat automatiskt

**Grundläggande exempel:**

```python
from fastapi import Depends, FastAPI

app = FastAPI()

# En dependency-funktion
def get_current_time():
    """Returnerar aktuell tid"""
    from datetime import datetime
    return datetime.now()

@app.get("/time")
def show_time(current_time: datetime = Depends(get_current_time)):
    """
    current_time injiceras automatiskt av FastAPI
    """
    return {"time": current_time.isoformat()}

# FastAPI anropar get_current_time() och skickar resultatet till show_time()
```

**Avancerat: Databas-session som dependency**

```python
# app/db/database.py
from typing import Generator

class Database:
    """Fake databas för demo"""
    def __init__(self):
        self.data = []

    def get_all(self):
        return self.data

    def add(self, item):
        self.data.append(item)

# Global databas-instans
db = Database()

def get_db() -> Generator:
    """
    Dependency som ger tillgång till databasen.
    I verkligheten skulle detta vara en SQLAlchemy-session.
    """
    try:
        yield db
    finally:
        # Cleanup om behövs
        pass

# app/routers/items.py
from fastapi import APIRouter, Depends
from ..db.database import Database, get_db

router = APIRouter(prefix="/items", tags=["items"])

@app.get("/items")
def get_items(db: Database = Depends(get_db)):
    """
    db injiceras automatiskt!
    """
    return db.get_all()

@app.post("/items")
def create_item(item: dict, db: Database = Depends(get_db)):
    db.add(item)
    return {"status": "created", "item": item}
```

**Hierarkiska dependencies:**

```python
from fastapi import Depends, HTTPException, Header

# Dependency 1: Validera API-nyckel
def verify_api_key(x_api_key: str = Header(...)):
    """Kontrollera om API-nyckeln är giltig"""
    if x_api_key != "secret-api-key-123":
        raise HTTPException(status_code=403, detail="Ogiltig API-nyckel")
    return x_api_key

# Dependency 2: Hämta användare (beror på verify_api_key)
def get_current_user(api_key: str = Depends(verify_api_key)):
    """
    Denna dependency kräver verify_api_key först!
    """
    # I verkligheten skulle du slå upp användaren i databasen
    return {"user_id": 123, "name": "Anna", "api_key": api_key}

# Endpoint som använder den hierarkiska dependencyn
@app.get("/protected")
def protected_route(user: dict = Depends(get_current_user)):
    """
    FastAPI kör först verify_api_key, sedan get_current_user
    """
    return {"message": f"Hej {user['name']}!", "user": user}

# Testa med:
# curl -H "x-api-key: secret-api-key-123" http://localhost:8000/protected
```

**Caching av dependencies:**

FastAPI cachar dependency-resultat per request automatiskt!

```python
from fastapi import Depends

call_counter = 0

def expensive_operation():
    """Simulerar en dyr operation"""
    global call_counter
    call_counter += 1
    print(f"Anropad {call_counter} gånger")
    return "Dyrt resultat"

@app.get("/cached")
def route1(data1: str = Depends(expensive_operation)):
    return {"data1": data1}

@app.get("/multi")
def route2(
    data1: str = Depends(expensive_operation),
    data2: str = Depends(expensive_operation),  # Samma dependency!
):
    # expensive_operation anropas BARA EN GÅNG per request!
    return {"data1": data1, "data2": data2, "note": "Cachad!"}
```

#### 4. **Pydantic validators – Avancerad validering**

Pydantic v2 har kraftfulla valideringsmöjligheter:

```python
from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: str
    age: Optional[int] = Field(None, ge=13, le=120)
    password: str = Field(..., min_length=8)
    password_confirm: str

    # Field validator (validerar ett fält)
    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        """Användarnamn får bara innehålla bokstäver och siffror"""
        if not v.isalnum():
            raise ValueError('Användarnamn får bara innehålla bokstäver och siffror')
        return v.lower()  # Konvertera till lowercase

    @field_validator('email')
    @classmethod
    def email_must_be_valid(cls, v: str) -> str:
        """Enkel emailvalidering"""
        if '@' not in v or '.' not in v:
            raise ValueError('Ogiltig emailadress')
        return v.lower()

    # Model validator (validerar hela modellen)
    @model_validator(mode='after')
    def passwords_match(self):
        """Kontrollera att lösenorden matchar"""
        if self.password != self.password_confirm:
            raise ValueError('Lösenorden matchar inte')
        return self

# Användning:
@app.post("/register")
def register(user: UserCreate):
    # Om vi kommer hit har all validering passerat!
    return {
        "message": "Användare skapad",
        "username": user.username,  # lowercase
        "email": user.email,        # lowercase
    }

# Testfall som misslyckas:
# {"username": "User@123", ...}         → Fel: endast alfanumeriskt
# {"email": "nogmail", ...}             → Fel: ogiltig email
# {"password": "abc", ...}               → Fel: för kort
# {"password": "abc123", "password_confirm": "abc456"} → Fel: matchar inte
```

**Computed fields (beräknade fält):**

```python
from pydantic import BaseModel, computed_field

class User(BaseModel):
    first_name: str
    last_name: str
    age: int

    @computed_field
    @property
    def full_name(self) -> str:
        """Beräknat fält som inte finns i input"""
        return f"{self.first_name} {self.last_name}"

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

# Användning:
user = User(first_name="Anna", last_name="Andersson", age=25)
print(user.full_name)  # "Anna Andersson"
print(user.is_adult)   # True

# I JSON:
# {
#   "first_name": "Anna",
#   "last_name": "Andersson",
#   "age": 25,
#   "full_name": "Anna Andersson",  ← Beräknat
#   "is_adult": true                ← Beräknat
# }
```

#### 5. **Global felhantering**

Istället för att skriva `try/except` överallt, använd **exception handlers**:

```python
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# Custom exception
class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

# Global handler för custom exception
@app.exception_handler(ItemNotFoundException)
async def item_not_found_exception_handler(
    request: Request,
    exc: ItemNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Item hittades inte",
            "item_id": exc.item_id,
            "path": str(request.url)
        }
    )

# Global handler för valideringsfel
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Anpassad felhantering för valideringsfel.
    Returnerar tydligare felmeddelanden.
    """
    return JSONResponse(
        status_code=422,
        content={
            "error": "Valideringsfel",
            "details": exc.errors(),
            "body": exc.body
        }
    )

# Global handler för alla HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Anpassad hantering för HTTP-exceptions"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code
        }
    )

# Endpoint som använder custom exception
@app.get("/items/{item_id}")
def get_item(item_id: int):
    items = {1: "Item 1", 2: "Item 2"}
    if item_id not in items:
        raise ItemNotFoundException(item_id)  # Hanteras av vår handler
    return {"item": items[item_id]}

# Endpoint som kan kasta HTTPException
@app.get("/restricted")
def restricted():
    raise HTTPException(status_code=403, detail="Åtkomst nekad")
```

#### 6. **BackgroundTasks – Bakgrundsjobb**

För **lätta** bakgrundsjobb (t.ex. skicka email, logga) använd `BackgroundTasks`:

```python
from fastapi import BackgroundTasks, FastAPI
import time

app = FastAPI()

def write_log(message: str):
    """Simulerar att skriva till en loggfil"""
    time.sleep(2)  # Simulerar långsam operation
    with open("log.txt", "a") as f:
        f.write(f"{message}\n")
    print(f"Logg skriven: {message}")

def send_email(email: str, message: str):
    """Simulerar att skicka email"""
    time.sleep(3)
    print(f"Email skickat till {email}: {message}")

@app.post("/signup")
def sign_up(
    email: str,
    username: str,
    background_tasks: BackgroundTasks
):
    """
    Skapar användare och skickar välkomstemail i bakgrunden
    """
    # Snabbt svar till klient
    user = {"email": email, "username": username}

    # Lägg till bakgrundsjobb
    background_tasks.add_task(write_log, f"Ny användare: {username}")
    background_tasks.add_task(send_email, email, "Välkommen!")

    # Returnera direkt (bakgrundsjobb körs efter)
    return {"message": "Användare skapad", "user": user}

# Klienten får svar DIREKT, även om email tar 3 sekunder!
```

**Viktigt om BackgroundTasks:**
- ✅ Bra för: Logga, skicka email, enkel data-processing
- ❌ Dåligt för: Tunga jobb, jobb som kan misslyckas, distribuerade system
- 🔄 För tunga jobb: Använd **Celery** eller **RQ** istället

**Async background tasks:**

```python
import asyncio

async def async_task(name: str):
    """Async bakgrundsjobb"""
    await asyncio.sleep(2)
    print(f"Async task {name} klar")

@app.get("/async-bg")
async def async_background(background_tasks: BackgroundTasks):
    background_tasks.add_task(async_task, "Task 1")
    return {"message": "Async task startat"}
```

**Varning:** Async background tasks kan blockera event loop om de är CPU-tunga!

#### 7. **Enkel autentisering – API-nyckel exempel**

```python
from fastapi import Depends, HTTPException, Security
from fastapi.security import APIKeyHeader

# Definiera var API-nyckeln ska vara (i header)
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Vår "databas" med giltiga nycklar
API_KEYS = {
    "secret-key-123": {"user": "Alice", "role": "admin"},
    "secret-key-456": {"user": "Bob", "role": "user"},
}

async def get_api_key(api_key: str = Security(api_key_header)):
    """
    Dependency som validerar API-nyckel.
    """
    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail="API-nyckel saknas i header 'X-API-Key'"
        )

    if api_key not in API_KEYS:
        raise HTTPException(
            status_code=403,
            detail="Ogiltig API-nyckel"
        )

    return API_KEYS[api_key]

# Skyddad endpoint
@app.get("/protected")
async def protected_route(user_info: dict = Depends(get_api_key)):
    return {
        "message": f"Välkommen {user_info['user']}!",
        "role": user_info['role']
    }

# Skyddad endpoint endast för admin
async def require_admin(user_info: dict = Depends(get_api_key)):
    """Kräver admin-rättigheter"""
    if user_info.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Kräver admin-rättigheter")
    return user_info

@app.delete("/admin/delete-user/{user_id}")
async def delete_user(user_id: int, admin: dict = Depends(require_admin)):
    return {"message": f"Användare {user_id} borttagen av {admin['user']}"}

# Testa:
# curl -H "X-API-Key: secret-key-123" http://localhost:8000/protected
# curl -H "X-API-Key: secret-key-456" http://localhost:8000/admin/delete-user/1  → 403
```

#### 8. **Async vs Sync – Fördjupning**

**När FastAPI får en request:**

```python
# SYNC (def)
@app.get("/sync")
def sync_route():
    # Körs i threadpool
    # Blockerar INTE event loop
    # Bra för: CPU-tunga operationer, synkrona DB-anrop
    time.sleep(1)  # OK att göra!
    return {"type": "sync"}

# ASYNC (async def)
@app.get("/async")
async def async_route():
    # Körs i event loop
    # Får INTE blockera!
    # Bra för: I/O-operationer med async libraries
    await asyncio.sleep(1)  # OK
    # time.sleep(1)  # ❌ ALDRIG! Blockerar event loop!
    return {"type": "async"}
```

**Mixing async and sync:**

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

def blocking_task():
    """En blockande operation"""
    time.sleep(2)
    return "Klar"

@app.get("/mixed")
async def mixed_route():
    # Kör blocking task i threadpool
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(executor, blocking_task)
    return {"result": result}
```

**Best practice guide:**

| Scenario | Använd | Exempel |
|----------|--------|---------|
| Async DB (SQLAlchemy async) | `async def` | `await session.execute(...)` |
| Sync DB (SQLAlchemy sync) | `def` | `session.query(...)` |
| HTTP requests (httpx) | `async def` | `await client.get(...)` |
| HTTP requests (requests) | `def` | `requests.get(...)` |
| Filläsning (aiofiles) | `async def` | `await file.read()` |
| Filläsning (standard) | `def` | `file.read()` |
| CPU-tung operation | `def` | Komplexa beräkningar |
| Osäker? | `def` | FastAPI hanterar det |

### Exempel

#### Exempel 1: Komplett modulär app-struktur

**Fil: `app/schemas/user.py`**
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True  # Pydantic v2
```

**Fil: `app/services/user_service.py`**
```python
from typing import List, Optional
from ..schemas.user import UserCreate, UserResponse

class UserService:
    """Affärslogik för användare"""

    def __init__(self):
        self.users = []  # Fake DB
        self.next_id = 1

    def create_user(self, user: UserCreate) -> UserResponse:
        """Skapa en ny användare"""
        new_user = UserResponse(
            id=self.next_id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            is_active=True
        )
        self.users.append(new_user)
        self.next_id += 1
        return new_user

    def get_all_users(self) -> List[UserResponse]:
        """Hämta alla användare"""
        return self.users

    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        """Hämta användare med ID"""
        for user in self.users:
            if user.id == user_id:
                return user
        return None

# Singleton instance
user_service = UserService()

def get_user_service() -> UserService:
    """Dependency för UserService"""
    return user_service
```

**Fil: `app/routers/users.py`**
```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.user import UserCreate, UserResponse
from ..services.user_service import UserService, get_user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    """Hämta alla användare"""
    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    """Hämta specifik användare"""
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Användare hittades inte")
    return user

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    user: UserCreate,
    service: UserService = Depends(get_user_service)
):
    """Skapa ny användare"""
    return service.create_user(user)
```

**Fil: `app/main.py`**
```python
from fastapi import FastAPI
from .routers import users

app = FastAPI(
    title="Modulär Användar-API",
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "API fungerar"}
```

#### Exempel 2: Dependency Injection-kedja

```python
from fastapi import Depends, HTTPException, Header
from typing import Optional

# Layer 1: Validera API-nyckel
def verify_token(x_token: str = Header(...)):
    if x_token != "fake-token":
        raise HTTPException(status_code=401, detail="Ogiltig token")
    return x_token

# Layer 2: Hämta användare (beror på Layer 1)
def get_current_user(token: str = Depends(verify_token)):
    # I verkligheten: slå upp token i databas
    return {"user_id": 123, "username": "alice"}

# Layer 3: Kontrollera rättigheter (beror på Layer 2)
def get_admin_user(user: dict = Depends(get_current_user)):
    if user.get("username") != "alice":  # Simplified
        raise HTTPException(status_code=403, detail="Inte admin")
    return user

# Endpoint som använder hela kedjan
@app.delete("/admin/data")
def delete_data(admin: dict = Depends(get_admin_user)):
    """
    Kräver:
    1. Giltig token (verify_token)
    2. Inloggad användare (get_current_user)
    3. Admin-rättigheter (get_admin_user)
    """
    return {"message": "Data borttagen", "by": admin["username"]}
```

### Visualiseringar

#### Diagram 1: Request-flöde genom modulär app

```
Request: POST /users
│
├─→ main.py (FastAPI app)
│   │
│   ├─→ include_router(users.router)
│   │
│   └─→ app/routers/users.py
│       │
│       ├─→ Depends(get_user_service)
│       │   └─→ app/services/user_service.py
│       │       └─→ Affärslogik
│       │
│       ├─→ Validera input (Pydantic schema)
│       │   └─→ app/schemas/user.py
│       │
│       └─→ Returnera response
│
└─→ Response: UserResponse (JSON)
```

#### Diagram 2: Dependency Injection-flöde

```
┌─────────────────────────────────────────────────────┐
│         DEPENDENCY INJECTION KEDJA                  │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Request kommer in                                  │
│    │                                                 │
│    ├─→ FastAPI ser: Depends(get_admin_user)        │
│    │                                                 │
│    ├─→ get_admin_user behöver: Depends(get_current_user)
│    │                                                 │
│    ├─→ get_current_user behöver: Depends(verify_token)
│    │                                                 │
│    └─→ FastAPI kör i ordning:                      │
│        1. verify_token(x_token från header)         │
│        2. get_current_user(token från 1)            │
│        3. get_admin_user(user från 2)               │
│        4. Din endpoint-funktion(admin från 3)       │
│                                                      │
│  ✓ Alla dependencies lösta!                        │
│  → Kör endpoint-funktionen                          │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### Diagram 3: Jämförelse - Dålig vs Bra struktur

```
┌────────────────────────────────────────────────────────┐
│              DÅLIG STRUKTUR (Anti-pattern)             │
├────────────────────────────────────────────────────────┤
│                                                         │
│  main.py (1500 rader!)                                 │
│    ├─ Alla endpoints                                   │
│    ├─ Alla Pydantic-modeller                          │
│    ├─ Databaskod                                       │
│    ├─ Affärslogik                                      │
│    └─ Utilities                                        │
│                                                         │
│  Problem:                                              │
│    • Omöjligt att navigera                            │
│    • Svårt att testa                                   │
│    • Merge conflicts                                   │
│    • Ingen separation of concerns                     │
│                                                         │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│              BRA STRUKTUR (Best practice)              │
├────────────────────────────────────────────────────────┤
│                                                         │
│  app/                                                   │
│    ├─ main.py (50 rader - bara setup)                 │
│    ├─ routers/ (endpoints, 100-200 rader vardera)     │
│    │    ├─ users.py                                    │
│    │    └─ items.py                                    │
│    ├─ schemas/ (Pydantic-modeller)                    │
│    │    ├─ user.py                                     │
│    │    └─ item.py                                     │
│    ├─ services/ (Affärslogik)                         │
│    │    ├─ user_service.py                            │
│    │    └─ item_service.py                            │
│    ├─ db/ (Databas)                                   │
│    │    └─ database.py                                 │
│    └─ core/ (Utilities)                               │
│         ├─ config.py                                   │
│         └─ security.py                                 │
│                                                         │
│  Fördelar:                                             │
│    ✓ Lätt att hitta kod                               │
│    ✓ Lätt att testa                                   │
│    ✓ Flera personer kan jobba samtidigt               │
│    ✓ Tydlig separation of concerns                    │
│                                                         │
└────────────────────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Tip 1: Använd services för affärslogik
Lägg **aldrig** affärslogik direkt i endpoints. Endpoints ska bara:
1. Ta emot request
2. Validera (Pydantic gör detta)
3. Anropa service
4. Returnera response

#### Tip 2: Dependency Injection gör testning enkel
```python
# I tester kan du enkelt mocka dependencies:
def fake_db():
    return {"fake": "data"}

app.dependency_overrides[get_db] = fake_db
```

#### Tip 3: Använd BackgroundTasks försiktigt
BackgroundTasks är bra för **lätta** jobb. Om ditt jobb:
- Tar >10 sekunder
- Kan misslyckas och behöver retry
- Behöver köras på schemalagd basis

→ Använd **Celery** istället!

#### Tip 4: Async betyder inte alltid snabbare
Om du inte använder async I/O libraries (async databas, httpx, etc.), ger `async def` ingen fördel. I vissa fall är `def` faktiskt snabbare för enkla operationer!

#### Tip 5: Separera schemas från models
- **Schemas** (Pydantic): API-representation (vad klienter ser)
- **Models** (SQLAlchemy): Databas-representation (hur data lagras)

Dessa är ofta **olika**! Exempel: Databas har `password_hash`, men schema returnerar aldrig detta.

### ✏️ Övningar

#### Övning 1: Dela upp en monolitisk app
**Uppgift**: Du har denna monolitiska `main.py`. Dela upp den i:
- `app/main.py`
- `app/routers/products.py`
- `app/schemas/product.py`

```python
# Monolitisk main.py (dålig stil)
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

products = []

@app.get("/products")
def get_products():
    return products

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product
```

**Facit**:

```python
# app/schemas/product.py
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

class ProductResponse(ProductCreate):
    id: int

# app/routers/products.py
from fastapi import APIRouter
from typing import List
from ..schemas.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])

products_db = []
next_id = 1

@router.get("/", response_model=List[ProductResponse])
def get_products():
    return products_db

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    global next_id
    new_product = ProductResponse(id=next_id, **product.model_dump())
    products_db.append(new_product)
    next_id += 1
    return new_product

# app/main.py
from fastapi import FastAPI
from .routers import products

app = FastAPI()
app.include_router(products.router)
```

#### Övning 2: Skapa en dependency-kedja
**Uppgift**: Skapa en dependency-kedja för ett blogg-API:
1. `verify_api_key`: Kontrollera API-nyckel i header
2. `get_current_user`: Hämta användare baserat på API-nyckel
3. `get_post_author`: Kontrollera att användaren är författare till posten
4. Endpoint `/posts/{post_id}/delete` som använder `get_post_author`

**Facit**:

```python
from fastapi import Depends, HTTPException, Header

API_KEYS = {"key123": {"user_id": 1, "username": "alice"}}
POSTS = {1: {"id": 1, "title": "Post 1", "author_id": 1}}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=401, detail="Ogiltig API-nyckel")
    return x_api_key

def get_current_user(api_key: str = Depends(verify_api_key)):
    return API_KEYS[api_key]

def get_post_author(post_id: int, user: dict = Depends(get_current_user)):
    if post_id not in POSTS:
        raise HTTPException(status_code=404, detail="Post hittades inte")
    post = POSTS[post_id]
    if post["author_id"] != user["user_id"]:
        raise HTTPException(status_code=403, detail="Du är inte författare")
    return {"post": post, "user": user}

@app.delete("/posts/{post_id}")
def delete_post(auth: dict = Depends(get_post_author)):
    """Endast författaren kan radera sin post"""
    post_id = auth["post"][ "id"]
    del POSTS[post_id]
    return {"message": f"Post {post_id} raderad"}
```

#### Övning 3: Implementera global felhantering
**Uppgift**: Skapa en custom exception `InsufficientFundsException` och en global handler för den. Använd den i en endpoint `/withdraw`.

**Facit**:

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class InsufficientFundsException(Exception):
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount

app = FastAPI()

@app.exception_handler(InsufficientFundsException)
async def insufficient_funds_handler(request: Request, exc: InsufficientFundsException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Otillräckligt saldo",
            "balance": exc.balance,
            "requested": exc.amount,
            "missing": exc.amount - exc.balance
        }
    )

# Fake bankkonto
account = {"balance": 100.0}

@app.post("/withdraw")
def withdraw(amount: float):
    if amount > account["balance"]:
        raise InsufficientFundsException(account["balance"], amount)
    account["balance"] -= amount
    return {"balance": account["balance"], "withdrawn": amount}
```

#### Övning 4: BackgroundTasks-exempel
**Uppgift**: Skapa en endpoint `/process-data` som:
1. Returnerar direkt till klienten
2. Kör en background task som "bearbetar data" i 5 sekunder
3. Loggar när bearbetningen är klar

**Facit**:

```python
from fastapi import BackgroundTasks
import time

def process_data(data_id: int):
    """Simulerar långsam databearbetning"""
    print(f"Börjar bearbeta data {data_id}...")
    time.sleep(5)
    print(f"Data {data_id} klar!")

@app.post("/process-data")
def submit_data(data_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_data, data_id)
    return {
        "message": "Data mottagen, bearbetning pågår i bakgrunden",
        "data_id": data_id
    }

# Klienten får svar DIREKT, bearbetning fortsätter i bakgrunden
```

#### Övning 5: Bygg ett mini-projekt (Bokbibliotek-API)
**Uppgift**: Bygg ett komplett litet API med:
- Routers för `books` och `authors`
- Pydantic schemas
- Enkel service-layer
- Dependency för fake-databas
- Global exception handler för "NotFound"

**Facit** (förenkl version):

```python
# app/schemas/book.py
from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author_id: int

class BookResponse(BookCreate):
    id: int

# app/routers/books.py
from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..schemas.book import BookCreate, BookResponse

router = APIRouter(prefix="/books", tags=["books"])

books_db = []
next_id = 1

@router.get("/", response_model=List[BookResponse])
def get_books():
    return books_db

@router.post("/", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate):
    global next_id
    new_book = BookResponse(id=next_id, **book.model_dump())
    books_db.append(new_book)
    next_id += 1
    return new_book

# app/main.py
from fastapi import FastAPI
from .routers import books

app = FastAPI(title="Bokbibliotek API")
app.include_router(books.router)
```

### 📝 Sammanfattning

**Key Takeaways:**

- 📁 **Projektstruktur**: Dela upp i routers, schemas, services, models - separera concerns!

- 🔌 **APIRouter**: Gruppera relaterade endpoints i separata filer med `prefix` och `tags`

- 💉 **Dependency Injection**: Återanvänd kod, förenkla testning, bygg hierarkier av dependencies

- ✅ **Pydantic validators**: `@field_validator` för fältvalidering, `@model_validator` för hela modellen

- 🚨 **Global felhantering**: Använd `@app.exception_handler` för konsekvent felhantering

- ⏱️ **BackgroundTasks**: För lätta jobb som inte blockerar response (email, logging)

- 🔐 **Enkel auth**: API-nyckel i header med `Security(APIKeyHeader(...))`

- ⚡ **Async best practices**: Använd `async def` för I/O, `def` för CPU-jobb

- 🏛️ **Services-layer**: Separera affärslogik från endpoints

- 📦 **Schemas vs Models**: API-representation vs databas-representation

**Ordlista (Nivå 4):**

- **APIRouter**: Klass för att gruppera endpoints i moduler
- **Dependency Injection**: Mönster för att injicera dependencies i funktioner
- **Service layer**: Lager där affärslogik finns (separerat från endpoints)
- **Schema**: Pydantic-modell för API-representation
- **Model**: Databas-modell (t.ex. SQLAlchemy)
- **Field validator**: Pydantic-decorator för att validera enskilda fält
- **Model validator**: Pydantic-decorator för att validera hela modellen
- **Exception handler**: Global hanterare för specifika exceptions
- **BackgroundTasks**: FastAPI-klass för att köra jobb i bakgrunden
- **Security**: FastAPI-modul för autentisering och auktorisering
- **Computed field**: Pydantic-fält som beräknas från andra fält

**Vad kommer härnäst?**

Nu är du redo för **produktionssättning**! I nästa och sista nivå (Expert-nivå) kommer vi att täcka:

- Hur man sätter FastAPI i produktion (uvicorn/gunicorn + nginx)
- Prestanda och skalning (connection pooling, caching med Redis)
- Säkerhet (OAuth2/JWT, CORS, secrets management)
- Databaser (SQLAlchemy + Alembic migrationer)
- Observability (logging, metrics, tracing)
- Schemalagda jobb och workers (Celery/APScheduler)
- Verkliga case studies och arkitekturmönster

Det blir expert-nivå – förberedd dig på att lära dig hur riktiga företag bygger produktions-API:er! 💼🚀

