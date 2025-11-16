# 🌱 Nivå 1: Grunderna - Vad är ett API?

> **För nybörjare utan teknisk bakgrund**
>
> **Tidsåtgång**: 2-3 timmar
>
> **Förkunskaper**: Inga

---

## 📚 Innehåll

1. [Vad är ett API? Enkla analogier](#vad-är-ett-api-enkla-analogier)
2. [Varför behöver vi API:er?](#varför-behöver-vi-apier)
3. [API:er du använder varje dag](#apier-du-använder-varje-dag)
4. [Grundläggande begrepp (utan jargong)](#grundläggande-begrepp)
5. [Din första titt på ett API](#din-första-titt-på-ett-api)
6. [Sammanfattning och nästa steg](#sammanfattning)

---

## 🍽️ Vad är ett API? Enkla analogier

### Analogi 1: Restaurangmenyn

Tänk dig att du är på en restaurang:

```
DU (Kund)  →  MENY (API)  →  KÖK (Server/Backend)
    ↓                              ↓
"Jag vill ha                   Kocken lagar
 pasta carbonara"              din beställning
    ↑                              ↓
    ←─────────  SERVITÖREN  ←──────┘
              (levererar din mat)
```

**I denna analogi:**

- **DU** = En app på din telefon (t.ex. en väderapp)
- **MENYN** = API:et (en lista över vad du kan beställa/begära)
- **KÖKET** = Servern där data lagras (t.ex. väderdatabasen)
- **SERVITÖREN** = API:et som tar emot din förfrågan och levererar svaret

**Nyckelpoäng**:
- Du behöver inte veta hur köket fungerar
- Du kan bara beställa det som finns på menyn
- Menyn har ett standardformat som alla förstår

### Analogi 2: Brevlådan

```
┌─────────────────┐
│   DIN BREVLÅDA  │  ← Du kan ta emot meddelanden (läsa)
│   (API)         │  ← Du kan skicka meddelanden (skriva)
└─────────────────┘
       ↕
┌─────────────────┐
│   POSTVERKET    │  ← Hanterar distributionen
└─────────────────┘
       ↕
┌─────────────────┐
│ AVSÄNDARENS BOX │  ← Någon annan som skickar/tar emot
└─────────────────┘
```

**API som brevlåda:**
- Du kan **skicka** meddelanden (requests)
- Du kan **ta emot** meddelanden (responses)
- Du behöver inte veta hur postverket fungerar
- Alla följer samma regler (format, adress, porto)

### Analogi 3: Telefonens kontaktlista

När du trycker på "Ring mamma" i din telefon:

1. Din telefon **använder API:et** för att hitta mammas nummer
2. API:et **begär** informationen från kontaktdatabasen
3. Databasen **returnerar** numret
4. Din telefon **ringer upp** numret

**Du ser aldrig:**
- Var numret är lagrat
- Hur databasen organiserar kontakter
- Den tekniska processen

**Du ser bara:**
- En knapp att trycka på
- Resultatet (samtalet kopplas)

---

## 🤔 Varför behöver vi API:er?

### Problem utan API:er

Föreställ dig att varje app måste ha ALL data själv:

```
❌ UTAN API:er

Väderappen måste:
- Ha egna väderstationer
- Lagra all väderdata
- Uppdatera data varje minut
- Kosta miljoner att driva

Din GPS-app måste:
- Ha hela världskartan lagrad på din telefon (100+ GB)
- Uppdatera vägar manuellt
- Aldrig få realtidstrafik
```

### Lösning med API:er

```
✅ MED API:er

Väderappen:
- Frågar en vädertjänst (API) "Hur är vädret i Stockholm?"
- Får svar på 0.5 sekunder
- Betalar bara för de förfrågningar som görs

GPS-appen:
- Frågar Google Maps API "Visa vägen till Malmö"
- Får uppdaterad kardata
- Inkluderar realtidstrafik
```

### Fördelar

| Fördel | Förklaring | Exempel |
|--------|------------|---------|
| **Återanvändning** | En tjänst kan användas av tusentals appar | Googles Maps API används av Uber, foodora, booking.com |
| **Specialisering** | Experter gör vad de är bäst på | Stripe gör betalningar, du bygger din app |
| **Säkerhet** | Data stannar säkert på servern | Din bank visar saldo via API, inte hela databasen |
| **Uppdateringar** | En uppdatering → alla får nytta | När Google uppdaterar kartor, fungerar alla appar |
| **Kostnadseffektivitet** | Dela infrastruktur | Betala per användning istället för att bygga allt själv |

---

## 📱 API:er du använder varje dag

Du använder sannolikt hundratals API:er dagligen utan att veta det!

### Exempel 1: Morgonrutinen

```
07:00  📱 Väckarklockan ringer
       └→ Använder TimeZone API för korrekt tid

07:15  ☀️  Kollar vädret
       └→ Väderappen använder OpenWeatherMap API

07:30  🚗 Kollar trafiken
       └→ Google Maps använder Traffic API

08:00  💳 Köper kaffe med kort
       └→ Butiken använder Stripe/Klarna Payment API
```

### Exempel 2: Social media-inloggning

När du klickar på "Logga in med Google":

```
1. Din app säger till Google API:
   "Denna person vill logga in"

2. Google API frågar dig:
   "Är det okej att dela ditt namn och email med denna app?"

3. Du säger ja

4. Google API säger till appen:
   "Okej, här är användarens information"

5. Du är inloggad!
```

**Fördelar:**
- Du slipper skapa nytt konto
- Appen får inte ditt Google-lösenord
- Google hanterar säkerheten

### Exempel 3: Streamingtjänster

När du tittar på Netflix:

```
Du trycker "Play"
    ↓
Netflix-appen → API: "Ge mig videoströmmen för 'Stranger Things'"
    ↓
API → CDN (Content Delivery Network): "Skicka videon från närmaste server"
    ↓
CDN → Din app: Streamar videon
```

### Verkliga API-exempel

| Tjänst | API-typ | Vad det gör |
|--------|---------|-------------|
| **OpenWeatherMap** | Väder-API | Ger väderdata för vilken plats som helst |
| **Stripe** | Betalnings-API | Hanterar kortbetalningar säkert |
| **Google Maps** | Kart-API | Visar kartor och vägbeskrivningar |
| **Spotify** | Musik-API | Låter andra appar spela Spotify-musik |
| **Twitter/X** | Social media-API | Låter appar posta och läsa tweets |
| **SendGrid** | Email-API | Skickar email från appar |
| **Twilio** | SMS-API | Skickar SMS från appar |
| **OpenAI** | AI-API | Ger tillgång till ChatGPT och bildgenerering |

---

## 🧩 Grundläggande begrepp (utan jargong)

### Klient och Server

```
KLIENT (Frontend)              SERVER (Backend)
┌──────────────┐              ┌──────────────┐
│              │              │              │
│  Väderappen  │──── API ────→│  Vädertjänst │
│  på din      │              │  med data    │
│  telefon     │←─── API ─────│              │
│              │              │              │
└──────────────┘              └──────────────┘
   (Begär data)                (Skickar data)
```

**Enkelt uttryckt:**
- **Klient** = Den som frågar (din app, webbläsare)
- **Server** = Den som svarar (där data finns)
- **API** = Språket de pratar (hur de kommunicerar)

### Request och Response

En **Request** (förfrågan) är när du ber om något:
```
"Ge mig vädret för Stockholm"
```

En **Response** (svar) är vad du får tillbaka:
```
"Det är 15°C och soligt i Stockholm"
```

**Exempel i verkliga livet:**

| Situation | Request | Response |
|-----------|---------|----------|
| Googlar något | "Recept på pannkakor" | Lista med recept |
| Swish-betalning | "Skicka 100kr till 0701234567" | "Betalning genomförd" |
| Spotify | "Spela denna låt" | Musik börjar spela |

### Endpoints (slutpunkter)

Ett **endpoint** är en specifik adress där du kan begära något:

```
Tänk på det som olika fönster på ett postkontor:

Fönster 1 (endpoint): /weather
→ Här hämtar du väderinfo

Fönster 2 (endpoint): /temperature
→ Här hämtar du bara temperatur

Fönster 3 (endpoint): /forecast
→ Här hämtar du prognos för 5 dagar
```

**I API-termer:**
```
https://api.openweathermap.org/data/2.5/weather
                                      ↑
                                  Endpoint
```

---

## 🔍 Din första titt på ett API

Låt oss titta på ett riktigt API-exempel (förenkla version):

### Scenario: Hämta väderdata

**Vad du vill veta:** "Hur är vädret i Stockholm?"

**Vad du skickar (Request):**
```
GE MIG: väderdata
PLATS: Stockholm
LAND: Sverige
```

**Vad du får tillbaka (Response):**
```json
{
  "stad": "Stockholm",
  "temperatur": 15,
  "väder": "soligt",
  "vind": "5 m/s"
}
```

### Låt oss bryta ner detta

**Del 1: Formatet**
- Data skickas i **JSON** (JavaScript Object Notation)
- Det är som en strukturerad lista, lätt för datorer att förstå
- Människor kan också läsa det!

**Del 2: Strukturen**
```json
{
  "nyckel": "värde",
  "nyckel2": "värde2"
}
```

- **Nyckel** = Namnet på informationen (t.ex. "temperatur")
- **Värde** = Själva informationen (t.ex. 15)

**Del 3: Exempel i vardagen**

Om du skulle beställa pizza via API:

**Request:**
```json
{
  "pizza": "Margherita",
  "storlek": "stor",
  "tillbehör": ["extra ost", "oliver"],
  "adress": "Storgatan 1"
}
```

**Response:**
```json
{
  "ordernummer": 12345,
  "uppskattad_tid": "30 minuter",
  "pris": 125,
  "status": "bekräftad"
}
```

---

## 🎯 Visualisering: Hur ett API-anrop fungerar

### Komplett flöde

```
┌─────────────────────────────────────────────────────────────┐
│                     API-KOMMUNIKATION                       │
└─────────────────────────────────────────────────────────────┘

Steg 1: KLIENTEN FÖRBEREDER FÖRFRÅGAN
┌──────────────┐
│ Väderappen   │  "Jag behöver väderdata för Stockholm"
└──────┬───────┘
       │
       │ Skapar Request:
       │ GET https://api.weather.com/stockholm
       │
       ↓

Steg 2: SKICKA ÖVER INTERNET
       ┊
       ┊ ⚡ Request reser över internet
       ┊
       ↓

Steg 3: SERVERN TAR EMOT
┌──────────────┐
│ API-Server   │  "Jag fick en förfrågan om Stockholm"
└──────┬───────┘
       │
       │ Letar upp data i databasen
       │
       ↓
┌──────────────┐
│  Databas     │  Temperatur: 15°C, Väder: Soligt
└──────┬───────┘
       │
       │

Steg 4: SERVERN SVARAR
       │
       │ Skapar Response (JSON-format)
       │
       ↓
       ┊
       ┊ ⚡ Response reser tillbaka över internet
       ┊
       ↓

Steg 5: KLIENTEN VISAR DATA
┌──────────────┐
│ Väderappen   │  Visar: "15°C ☀️ Soligt i Stockholm"
└──────────────┘
```

### Tidslinje

```
Tid:     0ms    50ms   100ms  150ms  200ms  250ms
         │      │      │      │      │      │
Klient:  ├──────┤                    ├──────┤
         │ Skapa│                    │ Visa │
         │Request│                   │Result│
         │      │      │      │      │      │
Internet:        ├─────┤      ├──────┤
                 │Skicka│     │Svar  │
                 │      │     │      │
Server:                 ├─────┤
                        │Hämta│
                        │Data │

Total tid: ~250ms (0.25 sekunder)
```

---

## 💡 Viktiga insikter för nybörjare

### ✅ Vad du nu förstår

1. **API är som en meny** - Den visar vad du kan begära
2. **API är en mellanhand** - Den kopplar ihop appar och data
3. **API gömmer komplexitet** - Du behöver inte veta hur allting fungerar
4. **API används överallt** - I så gott som alla moderna appar

### 🎓 Minnesregler

| Begrepp | Enkel förklaring |
|---------|------------------|
| **API** | Ett sätt för program att prata med varandra |
| **Request** | "Kan jag få...?" |
| **Response** | "Här är vad du bad om!" |
| **Endpoint** | En specifik adress där du kan hämta/skicka data |
| **Klient** | Den som frågar (din app) |
| **Server** | Den som svarar (där data finns) |

---

## 🚀 Praktiska exempel att utforska

### Prova själv (ingen kod krävs!)

**Exempel 1: Se ett API-svar i webbläsaren**

Öppna din webbläsare och gå till:
```
https://api.github.com/users/github
```

Du kommer att se JSON-data om GitHub-kontot "github"!

**Exempel 2: Väder-API**

Besök (kräver gratis registrering på OpenWeatherMap):
```
https://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid=DIN_API_NYCKEL&units=metric
```

### Reflektionsfrågor

1. Vilka 5 API:er använde du idag utan att tänka på det?
2. Om du skulle bygga en app, vilka API:er skulle du vilja använda?
3. Kan du förklara för någon (utan teknisk bakgrund) vad ett API är?

---

## 📝 Övningar för Nivå 1

*(Kompletta övningar finns i [övningar.md](./övningar.md), övning 1-7)*

### Övning 1.1: Identifiera API:er
Lista 10 appar du använder och gissa vilka API:er de kan använda.

**Exempel:**
- Instagram → Google Maps API (för platstaggar)
- Uber → Google Maps API + Payment API
- Spotify → Music Recognition API + Payment API

### Övning 1.2: Läsa JSON
Studera detta JSON-svar från ett API och förklara vad varje del betyder:

```json
{
  "namn": "Anna Andersson",
  "ålder": 28,
  "stad": "Stockholm",
  "intressen": ["fotboll", "matlagning", "resor"]
}
```

### Övning 1.3: Utforska ett publikt API
Besök https://api.github.com/users/DIN_GITHUB_USERNAME i webbläsaren och se dina GitHub-data.

---

## 🎯 Sammanfattning

### Vad du har lärt dig

✅ **Vad ett API är** - En mellanhand som låter program kommunicera
✅ **Varför API:er är viktiga** - De gör appar smartare och billigare att bygga
✅ **Hur de används dagligen** - I väder, kartor, betalningar, social media
✅ **Grundläggande begrepp** - Request, Response, Klient, Server, Endpoint

### Checklista innan du går vidare

- [ ] Jag kan förklara vad ett API är med en analogi
- [ ] Jag kan nämna 5 API:er jag använder dagligen
- [ ] Jag förstår skillnaden mellan klient och server
- [ ] Jag har tittat på ett riktigt API-svar i JSON-format
- [ ] Jag är redo att lära mig tekniska termer

---

## ➡️ Nästa steg

Nu när du förstår grunderna, är du redo för:

**[Nivå 2: Tekniska Termer →](./nivå-2-tekniska-termer.md)**

I Nivå 2 lär du dig:
- HTTP-metoder (GET, POST, PUT, DELETE)
- Vad är JSON och XML?
- Hur man använder API-nycklar
- Första enkla API-anrop med verktyg

**Uppskattat tid för Nivå 2:** 3-4 timmar

---

## 📚 Extra resurser för nybörjare

### Videos (svenska)
- "Vad är ett API? Förklarat för Nybörjare" - YouTube
- "API för Dummies" - Kodsnack Podcast

### Interaktiva tutorials
- https://restfulapi.net/ (enkel introduktion)
- https://www.postman.com/api-learning-center/ (gratis kurser)

### Böcker för nybörjare
- "APIs for Dummies" - John Paul Mueller
- "Understanding APIs and RESTful APIs" - Laurence Gellert

---

**Nivå 1 slutförd! 🎉**

[🏠 Tillbaka till huvudindex](./README.md) | [➡️ Gå till Nivå 2](./nivå-2-tekniska-termer.md)
