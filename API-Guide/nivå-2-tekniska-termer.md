# 🔧 Nivå 2: Tekniska Termer och Grundläggande Verktyg

> **För utvecklare som vill förstå API-grunder**
>
> **Tidsåtgång**: 3-4 timmar
>
> **Förkunskaper**: Nivå 1 eller grundläggande programmeringskunskap

---

## 📚 Innehåll

1. [HTTP - Grundprotokollet](#http---grundprotokollet)
2. [HTTP-metoder (GET, POST, PUT, DELETE, PATCH)](#http-metoder)
3. [URL-struktur och endpoints](#url-struktur-och-endpoints)
4. [Request och Response i detalj](#request-och-response-i-detalj)
5. [JSON och XML - Dataformat](#json-och-xml---dataformat)
6. [API-nycklar och autentisering (grundnivå)](#api-nycklar-och-autentisering)
7. [Ditt första API-anrop (med exempel)](#ditt-första-api-anrop)
8. [Verktyg för API-testning](#verktyg-för-api-testning)

---

## 🌐 HTTP - Grundprotokollet

### Vad är HTTP?

**HTTP** (HyperText Transfer Protocol) är språket som webbläsare och servrar använder för att prata med varandra.

```
Klient (webbläsare/app)  ←──── HTTP ────→  Server
```

**Analogi:**
Om API:et är en restaurangmeny, är HTTP det språk som du och servitören pratar.

### HTTP vs HTTPS

| | HTTP | HTTPS |
|---|------|-------|
| **Säkerhet** | ❌ Okrypterad | ✅ Krypterad |
| **Användning** | Gamla sidor | Moderna sidor |
| **Säkerhet** | Data kan läsas av andra | Data är skyddad |
| **Symbol** | 🔓 | 🔒 |

**Viktigt:** Använd alltid HTTPS för API:er som hanterar känslig data!

```
❌ http://api.example.com/user/password  ← FARLIGT!
✅ https://api.example.com/user/password ← SÄKERT!
```

### HTTP request/response-cykel

```
1. KLIENT SKICKAR REQUEST
┌─────────────────────────────────┐
│ GET /weather?city=Stockholm     │
│ Host: api.weather.com           │
│ Authorization: Bearer abc123    │
└─────────────────────────────────┘
              │
              ↓
   [Internet - HTTPS-tunnel]
              │
              ↓
2. SERVER TAR EMOT OCH PROCESSAR
┌─────────────────────────────────┐
│ Server läser förfrågan          │
│ Validerar authorization         │
│ Hämtar data från databas        │
└─────────────────────────────────┘
              │
              ↓
3. SERVER SKICKAR RESPONSE
┌─────────────────────────────────┐
│ HTTP/1.1 200 OK                 │
│ Content-Type: application/json  │
│                                 │
│ {"temp": 15, "weather": "sunny"}│
└─────────────────────────────────┘
              │
              ↓
4. KLIENT TAR EMOT OCH VISAR
┌─────────────────────────────────┐
│ App visar: "15°C ☀️"            │
└─────────────────────────────────┘
```

---

## 🔨 HTTP-metoder

HTTP-metoder (även kallade **HTTP verbs**) beskriver vilken typ av operation du vill göra.

### De 5 viktigaste metoderna

```
┌─────────┬─────────────┬────────────────────────────┐
│ Metod   │ Betydelse   │ Exempel                    │
├─────────┼─────────────┼────────────────────────────┤
│ GET     │ Hämta data  │ "Visa mina email"          │
│ POST    │ Skapa nytt  │ "Skicka ett nytt email"    │
│ PUT     │ Uppdatera   │ "Byt lösenord"             │
│ PATCH   │ Deluppdatera│ "Ändra endast förnamn"     │
│ DELETE  │ Ta bort     │ "Radera ett email"         │
└─────────┴─────────────┴────────────────────────────┘
```

### CRUD-mappning

**CRUD** = Create, Read, Update, Delete (grundläggande dataoperationer)

| CRUD | HTTP-metod | SQL-motsvarighet | Exempel |
|------|------------|------------------|---------|
| **Create** | POST | INSERT | Skapa ny användare |
| **Read** | GET | SELECT | Läs användarprofil |
| **Update** | PUT/PATCH | UPDATE | Uppdatera profil |
| **Delete** | DELETE | DELETE | Ta bort konto |

### Detaljerade exempel

#### GET - Hämta data

```http
GET /api/users/123
Host: api.example.com
```

**Karaktär:**
- ✅ Säker att anropa flera gånger (idempotent)
- ✅ Kan cachas
- ✅ Synlig i webbläsarhistorik
- ❌ Skickar INGEN data i body (använd query parameters istället)

**Exempel i verkliga livet:**
```javascript
// Hämta väderdata för Stockholm
GET https://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid=abc123
```

#### POST - Skapa ny resurs

```http
POST /api/users
Host: api.example.com
Content-Type: application/json

{
  "name": "Anna Andersson",
  "email": "anna@example.com",
  "age": 28
}
```

**Karaktär:**
- ❌ INTE idempotent (varje anrop skapar en NY resurs)
- ✅ Kan skicka stor data i body
- ✅ Används för att skapa NYA resurser

**Exempel:**
```javascript
// Skapa en ny användare
POST https://api.example.com/users
Body: {"name": "Anna", "email": "anna@example.com"}
```

#### PUT - Ersätt hela resursen

```http
PUT /api/users/123
Host: api.example.com
Content-Type: application/json

{
  "name": "Anna Svensson",
  "email": "anna.svensson@example.com",
  "age": 29
}
```

**Karaktär:**
- ✅ Idempotent (samma request ger samma resultat)
- ⚠️ Ersätter HELA resursen (alla fält måste anges)

#### PATCH - Delvis uppdatering

```http
PATCH /api/users/123
Host: api.example.com
Content-Type: application/json

{
  "email": "anna.new@example.com"
}
```

**Karaktär:**
- ✅ Uppdaterar ENDAST angivna fält
- ✅ Mer effektivt än PUT för små ändringar

**PUT vs PATCH:**
```
Originaldata:
{
  "name": "Anna",
  "email": "anna@example.com",
  "age": 28
}

PUT /users/123
{
  "name": "Anna"
}
→ Resultat: {"name": "Anna"}  ← email och age raderas!

PATCH /users/123
{
  "name": "Anna"
}
→ Resultat: {"name": "Anna", "email": "anna@example.com", "age": 28}
```

#### DELETE - Ta bort resurs

```http
DELETE /api/users/123
Host: api.example.com
```

**Karaktär:**
- ✅ Idempotent
- ⚠️ Ofta behövs auktorisering
- ✅ Kan returnera 204 No Content eller 200 OK

---

## 🔗 URL-struktur och endpoints

### Anatomi av en API-URL

```
https://api.openweathermap.org:443/data/2.5/weather?q=Stockholm&units=metric#results
  │       │                     │   │              │                           │
  │       │                     │   │              │                           │
 [1]     [2]                   [3] [4]            [5]                         [6]

[1] Protokoll (https)
[2] Domän/Host (api.openweathermap.org)
[3] Port (443 är standard för HTTPS)
[4] Path/Endpoint (/data/2.5/weather)
[5] Query Parameters (?q=Stockholm&units=metric)
[6] Fragment (#results) - används sällan i API:er
```

### Path Parameters vs Query Parameters

#### Path Parameters (del av URL-sökvägen)

```
GET /api/users/123/posts/456
              ↑         ↑
          user_id   post_id
```

**Användning:** Identifiera en specifik resurs

**Exempel:**
```
/users/123          ← Användare med ID 123
/posts/456          ← Inlägg med ID 456
/products/abc-123   ← Produkt med SKU abc-123
```

#### Query Parameters (efter ?)

```
GET /api/users?role=admin&active=true&page=2
                ↑          ↑          ↑
            Filtrera   Filtrera   Paginering
```

**Användning:** Filtrera, sortera, paginera

**Exempel:**
```
/users?role=admin               ← Filtrera: endast admins
/products?sort=price&order=asc  ← Sortera: billigast först
/posts?page=2&limit=10          ← Paginering: sida 2, 10 per sida
```

### Best practices för endpoint-design

✅ **BRA:**
```
GET    /users              ← Lista användare
GET    /users/123          ← Hämta specifik användare
POST   /users              ← Skapa ny användare
PUT    /users/123          ← Uppdatera användare
DELETE /users/123          ← Ta bort användare

GET    /users/123/posts    ← Hämta användarens inlägg
```

❌ **DÅLIGT:**
```
GET    /getAllUsers        ← HTTP-metoden säger redan "get"
POST   /createUser         ← POST betyder redan "create"
GET    /user/delete/123    ← Använd DELETE-metoden istället!
GET    /users?id=123       ← Använd path parameter: /users/123
```

### Versionering i URL

```
Version 1:  https://api.example.com/v1/users
Version 2:  https://api.example.com/v2/users
```

**Varför versioner?**
- Bakåtkompatibilitet
- Gradvis migrering
- A/B-testning

---

## 📨 Request och Response i detalj

### HTTP Request-struktur

```http
POST /api/users HTTP/1.1                          ← Request Line
Host: api.example.com                             ┐
Content-Type: application/json                    │
Authorization: Bearer abc123xyz                   │← Headers
Accept: application/json                          │
User-Agent: MyApp/1.0                             ┘
                                                  ← Blank line
{                                                 ┐
  "name": "Anna",                                 │
  "email": "anna@example.com"                     │← Body
}                                                 ┘
```

### Viktiga Headers

| Header | Syfte | Exempel |
|--------|-------|---------|
| **Content-Type** | Format på data som SKICKAS | `application/json` |
| **Accept** | Format på data som ÖNSKAS | `application/json` |
| **Authorization** | Autentisering | `Bearer token123` |
| **User-Agent** | Klientinformation | `Mozilla/5.0` |
| **Accept-Language** | Språkpreferens | `sv-SE, en;q=0.9` |

### HTTP Response-struktur

```http
HTTP/1.1 200 OK                                   ← Status Line
Content-Type: application/json                    ┐
Content-Length: 125                               │
Cache-Control: max-age=3600                       │← Headers
X-RateLimit-Remaining: 99                         │
Date: Mon, 16 Nov 2024 10:30:00 GMT               ┘
                                                  ← Blank line
{                                                 ┐
  "id": 123,                                      │
  "name": "Anna",                                 │← Body
  "email": "anna@example.com"                     │
}                                                 ┘
```

### HTTP-statuskoder (grundläggande)

```
┌──────────┬─────────────────┬───────────────────────────┐
│ Kod      │ Betydelse       │ Förklaring                │
├──────────┼─────────────────┼───────────────────────────┤
│ 2xx      │ Success         │ Allt gick bra             │
│ 200      │ OK              │ Lyckad request            │
│ 201      │ Created         │ Ny resurs skapad          │
│ 204      │ No Content      │ Lyckad, men inget svar    │
│          │                 │                           │
│ 3xx      │ Redirection     │ Resursen har flyttats     │
│ 301      │ Moved Permanent │ Permanent flytt           │
│ 304      │ Not Modified    │ Använd cachad version     │
│          │                 │                           │
│ 4xx      │ Client Error    │ Du gjorde något fel       │
│ 400      │ Bad Request     │ Felaktig syntax           │
│ 401      │ Unauthorized    │ Autentisering krävs       │
│ 403      │ Forbidden       │ Inte tillåten             │
│ 404      │ Not Found       │ Resursen finns inte       │
│ 429      │ Too Many Req    │ Rate limit nådd           │
│          │                 │                           │
│ 5xx      │ Server Error    │ Servern kraschade         │
│ 500      │ Internal Error  │ Något gick fel på server  │
│ 502      │ Bad Gateway     │ Gateway-problem           │
│ 503      │ Unavailable     │ Servern är nere           │
└──────────┴─────────────────┴───────────────────────────┘
```

**Minnesregel:**
- **2xx** = ✅ Grattis!
- **3xx** = ↪️ Kolla här istället
- **4xx** = ❌ DU gjorde fel
- **5xx** = 💥 VI gjorde fel

---

## 📄 JSON och XML - Dataformat

### JSON (JavaScript Object Notation)

**Modern standard för API:er** (95% av alla API:er använder JSON)

```json
{
  "användare": {
    "id": 123,
    "namn": "Anna Andersson",
    "ålder": 28,
    "aktiv": true,
    "intressen": ["fotboll", "matlagning", "resor"],
    "adress": {
      "gata": "Storgatan 1",
      "stad": "Stockholm",
      "postnummer": "11122"
    }
  }
}
```

**Fördelar:**
- ✅ Lätt att läsa för människor
- ✅ Kompakt (mindre data)
- ✅ Native support i JavaScript
- ✅ Stöd i alla moderna språk

**Datatyper i JSON:**
```json
{
  "string": "text",
  "number": 123,
  "float": 12.34,
  "boolean": true,
  "null": null,
  "array": [1, 2, 3],
  "object": {"key": "value"}
}
```

### XML (eXtensible Markup Language)

**Äldre standard**, används fortfarande i vissa branscher (bank, myndigheter, SOAP-API:er)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<användare>
  <id>123</id>
  <namn>Anna Andersson</namn>
  <ålder>28</ålder>
  <aktiv>true</aktiv>
  <intressen>
    <intresse>fotboll</intresse>
    <intresse>matlagning</intresse>
    <intresse>resor</intresse>
  </intressen>
  <adress>
    <gata>Storgatan 1</gata>
    <stad>Stockholm</stad>
    <postnummer>11122</postnummer>
  </adress>
</användare>
```

**Fördelar:**
- ✅ Stöd för attribut
- ✅ Strikta valideringsregler (XSD-schema)
- ✅ Namespaces för att undvika konflikter

**Nackdelar:**
- ❌ Mycket mer verbose (större filer)
- ❌ Svårare att läsa
- ❌ Långsammare parsing

### JSON vs XML - Jämförelse

| | JSON | XML |
|---|------|-----|
| **Läsbarhet** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Storlek** | Kompakt | Större (+50-70%) |
| **Hastighet** | Snabb | Långsammare |
| **Support** | Alla moderna språk | Alla språk |
| **Användning 2024** | 95% av API:er | 5% av API:er |
| **Best för** | Webbutveckling | Enterprise, SOAP |

**Samma data:**
```
JSON:  125 bytes
XML:   310 bytes
```

---

## 🔑 API-nycklar och autentisering (grundnivå)

### Varför autentisering?

1. **Identifiera** vem som anropar API:et
2. **Begränsa** antal anrop (rate limiting)
3. **Skydda** känslig data
4. **Fakturera** användare

### API-nyckel (enklaste metoden)

```
GET /weather?q=Stockholm&appid=abc123def456
                         ↑
                    API-nyckel
```

**Så fungerar det:**

```
1. Registrera dig → Få en API-nyckel
   Din nyckel: abc123def456

2. Inkludera i varje request:
   Option A (Query parameter):
   GET /data?appid=abc123def456

   Option B (Header):
   GET /data
   Authorization: ApiKey abc123def456

3. Servern validerar nyckeln:
   ✅ Giltig → Returnera data
   ❌ Ogiltig → 401 Unauthorized
```

**Exempel (OpenWeatherMap):**

```javascript
// JavaScript (fetch)
fetch('https://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid=DIN_API_NYCKEL')
  .then(response => response.json())
  .then(data => console.log(data));
```

```python
# Python (requests)
import requests

api_key = "DIN_API_NYCKEL"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Stockholm&appid={api_key}"

response = requests.get(url)
data = response.json()
print(data)
```

### ⚠️ Säkerhetsvarningar för API-nycklar

```
❌ GÖR ALDRIG:
- Committa API-nycklar till GitHub
- Dela nycklar i publika forum
- Hårdkoda nycklar i frontend-kod
- Använd samma nyckel överallt

✅ GÖR ISTÄLLET:
- Använd environment variables (.env-fil)
- Rotera nycklar regelbundet
- Använd olika nycklar för dev/prod
- Lägg till .env i .gitignore
```

**Exempel (.env-fil):**
```bash
# .env (lägg i .gitignore!)
OPENWEATHER_API_KEY=abc123def456
DATABASE_URL=postgres://localhost/mydb
```

```javascript
// Läs från .env
require('dotenv').config();
const apiKey = process.env.OPENWEATHER_API_KEY;
```

---

## 🚀 Ditt första API-anrop

### Exempel 1: Hämta väderdata (JavaScript)

```javascript
// Använd fetch API (inbyggt i moderna webbläsare)
const apiKey = 'DIN_API_NYCKEL';  // Få en gratis nyckel på openweathermap.org
const stad = 'Stockholm';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${stad}&appid=${apiKey}&units=metric&lang=sv`;

fetch(url)
  .then(response => {
    // Kontrollera om request lyckades
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();  // Parsea JSON
  })
  .then(data => {
    // Visa resultatet
    console.log(`Väder i ${data.name}:`);
    console.log(`Temperatur: ${data.main.temp}°C`);
    console.log(`Känns som: ${data.main.feels_like}°C`);
    console.log(`Beskrivning: ${data.weather[0].description}`);
  })
  .catch(error => {
    // Hantera fel
    console.error('Fel vid API-anrop:', error);
  });
```

**Svar (JSON):**
```json
{
  "name": "Stockholm",
  "main": {
    "temp": 15.2,
    "feels_like": 14.1,
    "humidity": 72
  },
  "weather": [
    {
      "description": "lätt regn",
      "icon": "10d"
    }
  ]
}
```

### Exempel 2: Hämta väderdata (Python)

```python
import requests  # Installera: pip install requests

# Konfigurera API-anrop
api_key = "DIN_API_NYCKEL"
stad = "Stockholm"
url = f"https://api.openweathermap.org/data/2.5/weather"

# Query parameters
params = {
    "q": stad,
    "appid": api_key,
    "units": "metric",  # Celsius
    "lang": "sv"        # Svenska beskrivningar
}

# Skicka GET request
response = requests.get(url, params=params)

# Kontrollera status
if response.status_code == 200:
    data = response.json()

    print(f"Väder i {data['name']}:")
    print(f"Temperatur: {data['main']['temp']}°C")
    print(f"Känns som: {data['main']['feels_like']}°C")
    print(f"Beskrivning: {data['weather'][0]['description']}")
else:
    print(f"Fel: {response.status_code}")
    print(response.text)
```

### Exempel 3: POST-request (skapa data)

```javascript
// Skapa en ny användare (exempel-API)
const newUser = {
  name: "Anna Andersson",
  email: "anna@example.com",
  age: 28
};

fetch('https://jsonplaceholder.typicode.com/users', {
  method: 'POST',  // Specificera metod
  headers: {
    'Content-Type': 'application/json',  // Viktigt!
  },
  body: JSON.stringify(newUser)  // Konvertera object till JSON-sträng
})
  .then(response => response.json())
  .then(data => {
    console.log('Användare skapad:', data);
    // Får tillbaka: {id: 11, name: "Anna Andersson", ...}
  });
```

```python
# Python-motsvarighet
import requests

new_user = {
    "name": "Anna Andersson",
    "email": "anna@example.com",
    "age": 28
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/users',
    json=new_user  # requests hanterar JSON-konvertering automatiskt
)

if response.status_code == 201:  # 201 = Created
    print("Användare skapad:", response.json())
```

---

## 🛠️ Verktyg för API-testning

### 1. Postman (mest populär)

**Vad det är:** GUI-verktyg för att testa API:er utan att skriva kod

**Installera:** https://www.postman.com/downloads/

**Grundläggande användning:**

```
1. Ny Request
   ┌────────────────────────────────────┐
   │ GET  ▼ │ https://api.example.com/users │ [Send]
   └────────────────────────────────────┘

2. Välj HTTP-metod (GET/POST/etc)

3. Ange URL

4. (Valfritt) Lägg till Headers, Body, Authorization

5. Klicka "Send"

6. Se resultat:
   ┌────────────────────────────────────┐
   │ Status: 200 OK                     │
   │ Time: 245ms                        │
   │ Size: 1.2KB                        │
   │                                    │
   │ Body  │ Headers │ Cookies          │
   │────────────────────────────────────│
   │ {                                  │
   │   "id": 1,                         │
   │   "name": "Anna"                   │
   │ }                                  │
   └────────────────────────────────────┘
```

**Funktioner:**
- ✅ Spara requests i Collections
- ✅ Environment variables
- ✅ Automated testing
- ✅ Mock servers
- ✅ Team collaboration

### 2. cURL (kommandorad)

**Vad det är:** Kommandoradsverktyg för HTTP-requests (redan installerat på Mac/Linux)

```bash
# GET request
curl https://api.github.com/users/github

# GET med headers
curl -H "Authorization: Bearer abc123" \
     https://api.example.com/users

# POST request
curl -X POST https://api.example.com/users \
     -H "Content-Type: application/json" \
     -d '{"name":"Anna","email":"anna@example.com"}'

# Visa headers i response
curl -i https://api.example.com/users

# Följ redirects
curl -L https://bit.ly/short-url

# Spara output till fil
curl https://api.example.com/data > output.json
```

**Fördelar:**
- ✅ Snabbt för enkla tester
- ✅ Scriptbart
- ✅ Fungerar överallt

### 3. Insomnia

**Alternativ till Postman**, mer minimalistiskt gränssnitt

- https://insomnia.rest/

### 4. VS Code REST Client

**Extension för VS Code** - testa API:er direkt i editorn

```http
### Exempel-request (spara som test.http)

GET https://api.github.com/users/github
Accept: application/json

###

POST https://jsonplaceholder.typicode.com/users
Content-Type: application/json

{
  "name": "Anna",
  "email": "anna@example.com"
}
```

Klicka "Send Request" ovanför varje block!

---

## 📝 Övningar för Nivå 2

*(Kompletta övningar finns i [övningar.md](./övningar.md), övning 8-15)*

### Övning 2.1: HTTP-metoder
Matcha rätt metod till scenariot:

1. Hämta en lista av produkter → ?
2. Lägga till en ny produkt → ?
3. Uppdatera produktens pris → ?
4. Ta bort en produkt → ?

### Övning 2.2: Läsa statuskoder
Vad betyder dessa statuskoder?

- 200
- 201
- 404
- 500
- 401

### Övning 2.3: Ditt första API-anrop med Postman

1. Installera Postman
2. Skapa ett nytt GET-request till:
   ```
   https://jsonplaceholder.typicode.com/users/1
   ```
3. Skicka requesten och analysera svaret
4. Ändra URL:en till `/users/999` - vad händer?

### Övning 2.4: JSON-parsing

Skriv kod (JavaScript eller Python) som:
1. Hämtar data från `https://jsonplaceholder.typicode.com/users`
2. Hittar användaren med namnet "Leanne Graham"
3. Skriver ut användarens email

---

## 🎯 Sammanfattning

### Vad du har lärt dig

✅ **HTTP-grunderna** - Protokollet som driver webben
✅ **HTTP-metoder** - GET, POST, PUT, PATCH, DELETE
✅ **URL-struktur** - Endpoints, parameters, versioner
✅ **Request/Response** - Headers, body, statuskoder
✅ **Dataformat** - JSON och XML
✅ **Autentisering** - API-nycklar och säkerhet
✅ **Praktiska verktyg** - Postman, cURL, VS Code

### Checklista

- [ ] Jag kan förklara skillnaden mellan GET och POST
- [ ] Jag förstår HTTP-statuskoder (200, 404, 500)
- [ ] Jag kan läsa JSON-data
- [ ] Jag har gjort mitt första API-anrop med Postman
- [ ] Jag har kodat ett enkelt API-anrop (JavaScript eller Python)
- [ ] Jag förstår varför HTTPS är viktigt
- [ ] Jag vet hur API-nycklar fungerar

---

## ➡️ Nästa steg

**[Nivå 3: Tekniska Detaljer →](./nivå-3-tekniska-detaljer.md)**

I Nivå 3 lär du dig:
- REST-principer i detalj
- Error handling och edge cases
- CORS och säkerhet
- Verktyg som Postman (avancerat)
- Dokumentation med Swagger/OpenAPI

---

[🏠 Tillbaka till huvudindex](./README.md) | [⬅️ Nivå 1](./nivå-1-grunderna.md) | [➡️ Nivå 3](./nivå-3-tekniska-detaljer.md)
