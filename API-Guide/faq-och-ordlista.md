# ❓ FAQ och Ordlista

> **Vanliga frågor och terminologi för API-utveckling**

---

## 📚 Innehåll

1. [FAQ - Vanliga frågor](#faq---vanliga-frågor)
   - [Nybörjarfrågor](#nybörjarfrågor)
   - [Troubleshooting](#troubleshooting)
   - [Konceptuella frågor](#konceptuella-frågor)
   - [Best practices](#best-practices)
   - [Säkerhetsfrågor](#säkerhetsfrågor)
2. [Ordlista](#ordlista)
3. [Akronymer](#akronymer)

---

## ❓ FAQ - Vanliga frågor

### 🌱 Nybörjarfrågor

#### 1. Vad är skillnaden mellan ett API och en webbsida?

**Svar:**
- **Webbsida** = För människor (HTML, CSS, bilder)
- **API** = För program (JSON/XML data, ingen visuell design)

**Exempel:**
```
Webbsida (https://www.weathersite.com):
→ Visar: Vackra ikoner, grafer, färger
→ För: Människor att titta på

API (https://api.weathersite.com):
→ Returnerar: {"temp": 15, "description": "sunny"}
→ För: Program att läsa
```

---

#### 2. Behöver jag kunna programmera för att använda API:er?

**Svar:**
- **För att använda API:er**: Lite programmering krävs (JavaScript, Python, etc.)
- **För att testa API:er**: Nej! Använd verktyg som Postman
- **För att bygga API:er**: Ja, programmering krävs

**Lärväg:**
1. Lär dig grundläggande JavaScript eller Python (2-4 veckor)
2. Börja med enkla API-anrop (1 vecka)
3. Bygg små projekt (4-8 veckor)

---

#### 3. Vilket programmeringsspråk är bäst för API:er?

**Svar:**
Alla moderna språk fungerar! Populärast:

| Språk | Användning | Lärningskurva |
|-------|------------|---------------|
| **JavaScript (Node.js)** | Webbutveckling, fullstack | ⭐⭐⭐ Medel |
| **Python** | Data science, backend | ⭐⭐ Lätt |
| **TypeScript** | Enterprise, stora projekt | ⭐⭐⭐⭐ Medel-svår |
| **Go** | Mikroservices, prestanda | ⭐⭐⭐⭐ Svår |
| **Java** | Enterprise, Android | ⭐⭐⭐⭐ Svår |
| **C#** | .NET, Windows | ⭐⭐⭐ Medel |

**Rekommendation för nybörjare:** Python eller JavaScript (Node.js)

---

#### 4. Kostar det att använda API:er?

**Svar:**
Det varierar:

**Gratis API:er** (med begränsningar):
- OpenWeatherMap: 1000 anrop/dag gratis
- GitHub API: 60 anrop/timme (ej inloggad)
- JSONPlaceholder: Obegränsat (test/mock-data)

**Freemium** (gratis tier + betald):
- Stripe: Gratis + 2,9% per transaktion
- Google Maps: $200 kredit/månad
- OpenAI: $5 i krediter vid registrering

**Enterprise** (endast betald):
- Twilio: Betala per SMS
- AWS: Betala för vad du använder

**Tips:** Börja alltid med gratis tier!

---

#### 5. Hur hittar jag publika API:er att öva på?

**Svar:**
**API-kataloger:**
- https://rapidapi.com/ - 35,000+ API:er
- https://publicapis.dev/ - Kurerad lista
- https://apilist.fun/ - Kategoriserad lista
- https://github.com/public-apis/public-apis - GitHub-lista

**Populära test-API:er:**
- https://jsonplaceholder.typicode.com/ - Fake REST API
- https://reqres.in/ - Test REST API med mock data
- https://randomuser.me/ - Random användardata
- https://dog.ceo/api/ - Hundar! 🐕

---

### 🔧 Troubleshooting

#### 6. Jag får "CORS error" - vad gör jag?

**Svar:**
CORS (Cross-Origin Resource Sharing) är en säkerhetsfunktion i webbläsare.

**Problem:**
```
Access to fetch at 'https://api.example.com' from origin
'http://localhost:3000' has been blocked by CORS policy
```

**Lösningar:**

**A) Backend-lösning** (bäst):
```javascript
// Node.js/Express
const cors = require('cors');
app.use(cors());
```

**B) Använd en proxy** (frontend):
```javascript
// package.json (React)
{
  "proxy": "https://api.example.com"
}

// Ändra request från
fetch('https://api.example.com/users')
// till
fetch('/users')
```

**C) Browser extension** (endast utveckling):
- Installera "CORS Unblock" extension
- ⚠️ Använd ENDAST för lokal utveckling!

---

#### 7. Varför får jag "401 Unauthorized"?

**Svar:**
401 = Autentisering krävs eller är ogiltig

**Vanliga orsaker:**

1. **Saknar API-nyckel:**
```javascript
❌ fetch('https://api.example.com/data')
✅ fetch('https://api.example.com/data?apikey=ABC123')
```

2. **Fel header:**
```javascript
❌ headers: { 'Auth': 'Bearer token' }
✅ headers: { 'Authorization': 'Bearer token' }
```

3. **Utgången token:**
```javascript
// JWT har gått ut, logga in igen
```

4. **Fel format:**
```javascript
❌ 'Authorization': 'token123'
✅ 'Authorization': 'Bearer token123'
```

**Debugging:**
```javascript
// Logga dina headers
console.log(req.headers);

// Kontrollera token
const decoded = jwt.decode(token);
console.log('Token expires:', new Date(decoded.exp * 1000));
```

---

#### 8. Varför är mitt API så långsamt?

**Svar:**
Vanliga orsaker och lösningar:

| Problem | Lösning |
|---------|---------|
| **Många databas-queries** | Använd eager loading, join queries |
| **Ingen caching** | Implementera Redis, HTTP-cache |
| **N+1 problem** | Använd DataLoader (GraphQL) eller JOIN (SQL) |
| **Stora responses** | Paginering, field selection |
| **Långsam extern API** | Cacha resultat, använd async/await |
| **Ingen CDN** | Använd CloudFlare, AWS CloudFront |

**Mät prestanda:**
```javascript
// Express middleware
app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = Date.now() - start;
    console.log(`${req.method} ${req.path}: ${duration}ms`);
  });
  next();
});
```

---

#### 9. Hur debuggar jag API-anrop?

**Svar:**
**Verktyg:**

1. **Browser DevTools:**
```
1. Öppna DevTools (F12)
2. Network-tab
3. Kör API-anrop
4. Klicka på request
5. Se Headers, Preview, Response
```

2. **Postman:**
```
- Testa requests isolerat
- Se console för debug-info
- Spara test-requests
```

3. **cURL med verbose:**
```bash
curl -v https://api.example.com/users
# Visar alla headers och response
```

4. **Logging i backend:**
```javascript
// Logga varje request
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} ${req.method} ${req.path}`);
  console.log('Headers:', req.headers);
  console.log('Body:', req.body);
  next();
});
```

---

### 💡 Konceptuella frågor

#### 10. Vad är skillnaden mellan REST och GraphQL?

**Svar:**

| | REST | GraphQL |
|---|------|---------|
| **Endpoints** | Många (/users, /posts) | Ett (/graphql) |
| **Data fetching** | Fasta responses | Flexibla queries |
| **Over-fetching** | Ja (får extra data) | Nej (bara vad du begär) |
| **Under-fetching** | Ja (N+1 problem) | Nej (en query hämtar allt) |
| **Versionering** | /v1/, /v2/ | Deprecation av fält |
| **Caching** | Enkelt (HTTP-cache) | Svårare |
| **Learning curve** | Lättare | Svårare |
| **Best för** | CRUD, publika API:er | Komplexa relationer, mobil |

**Exempel:**

**REST:**
```javascript
// 3 requests
GET /users/1
GET /users/1/posts
GET /posts/1/comments
```

**GraphQL:**
```graphql
# 1 request
query {
  user(id: 1) {
    name
    posts {
      title
      comments {
        text
      }
    }
  }
}
```

---

#### 11. Ska jag använda REST eller GraphQL?

**Svar:**

**Använd REST när:**
- ✅ Enkla CRUD-operationer
- ✅ Publikt API (lättare att dokumentera)
- ✅ Cachning är kritiskt
- ✅ Teamet är bekvämt med REST
- ✅ Resurser har få relationer

**Använd GraphQL när:**
- ✅ Komplexa data-relationer
- ✅ Mobilappar (minska antal requests)
- ✅ Frontend behöver olika vyer av samma data
- ✅ Real-time behov (subscriptions)
- ✅ Snabb frontend-utveckling

**Hybrid-lösning:**
```
REST för publika API:er
GraphQL för interna/mobilappar
```

---

#### 12. Vad är skillnaden mellan autentisering och auktorisering?

**Svar:**

**Autentisering** (Authentication):
- "Vem är du?"
- Verifiera identitet
- Login med användarnamn + lösenord, JWT, OAuth

**Auktorisering** (Authorization):
- "Vad får du göra?"
- Kontrollera rättigheter
- Roller (admin, user, guest)

**Exempel:**
```javascript
// 1. Autentisering
POST /login
→ Returnerar JWT token

// 2. Auktorisering
GET /admin/users
→ Kontrollerar om användaren har "admin"-roll
```

**Flöde:**
```
1. Användare loggar in (Autentisering)
   ✅ Verifierad som "anna@example.com"

2. Användare försöker ta bort en post (Auktorisering)
   → Är användaren ägare av posten?
   → Har användaren "moderator"-rättigheter?
   ✅/❌ Tillåt eller neka
```

---

#### 13. Hur fungerar API-nycklar och är de säkra?

**Svar:**

**Hur de fungerar:**
```
1. Du registrerar dig på API-plattform
2. Du får en nyckel: "abc123def456"
3. Du inkluderar nyckeln i varje request:
   GET /data?apikey=abc123def456
```

**Säkerhet:**

✅ **Bra:**
- Enklare än OAuth för server-to-server
- Snabbt att implementera
- Bra för rate limiting och analytics

❌ **Problem:**
- Kan läcka (loggar, git commits)
- Svåra att revokera (för vissa användare)
- Ingen användarkontext

**Best practices:**
```bash
# 1. Använd environment variables
# .env
API_KEY=abc123def456

# 2. Lägg .env i .gitignore
echo ".env" >> .gitignore

# 3. Rotera regelbundet
# Byt nyckel varje 90 dagar

# 4. Olika nycklar för olika miljöer
API_KEY_DEV=dev_abc123
API_KEY_PROD=prod_xyz789
```

**När INTE använda API-nycklar:**
- ❌ Känslig användardata
- ❌ Frontend-kod (synlig i browser)
- ❌ Third-party access till användarkonton

**Använd istället:**
- ✅ JWT för autentisering
- ✅ OAuth 2.0 för third-party access

---

### 🏆 Best Practices

#### 14. Hur designar jag ett bra API?

**Svar:**

**1. Använd RESTful konventioner:**
```
✅ GET /users          - Lista användare
✅ GET /users/123      - Hämta användare
✅ POST /users         - Skapa användare
✅ PUT /users/123      - Uppdatera användare
✅ DELETE /users/123   - Ta bort användare

❌ GET /getAllUsers
❌ POST /createUser
❌ GET /user/delete/123
```

**2. Versionering från början:**
```
https://api.example.com/v1/users
```

**3. Använd rätt statuskoder:**
```javascript
200 OK          - Lyckad GET/PUT/PATCH
201 Created     - Lyckad POST
204 No Content  - Lyckad DELETE
400 Bad Request - Felaktig syntax från klient
401 Unauthorized- Autentisering krävs
404 Not Found   - Resursen finns inte
500 Server Error- Något gick fel på servern
```

**4. Konsistenta error-responses:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email format är ogiltigt",
    "field": "email",
    "timestamp": "2024-11-16T10:30:00Z"
  }
}
```

**5. Dokumentation:**
- Använd OpenAPI/Swagger
- Inkludera exempel
- Uppdatera vid ändringar

**6. Pagination:**
```
GET /users?page=2&limit=20
```

**7. Filtering:**
```
GET /products?category=electronics&price_max=500
```

**8. Rate limiting:**
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 73
X-RateLimit-Reset: 1699268400
```

---

#### 15. Hur testar jag mitt API?

**Svar:**

**1. Unit tests:**
```javascript
// Jest + Supertest
test('GET /users returnerar 200', async () => {
  const res = await request(app).get('/users');
  expect(res.statusCode).toBe(200);
  expect(res.body).toBeInstanceOf(Array);
});
```

**2. Integration tests:**
```javascript
test('Hela user creation flow', async () => {
  // Registrera
  const registerRes = await request(app)
    .post('/auth/register')
    .send({ email: 'test@example.com', password: 'password123' });

  const token = registerRes.body.token;

  // Hämta profil med token
  const profileRes = await request(app)
    .get('/profile')
    .set('Authorization', `Bearer ${token}`);

  expect(profileRes.statusCode).toBe(200);
});
```

**3. End-to-end tests:**
```javascript
// Cypress, Playwright
describe('User flow', () => {
  it('Kan registrera och logga in', () => {
    cy.visit('/register');
    cy.get('input[name=email]').type('test@example.com');
    cy.get('input[name=password]').type('password123');
    cy.get('button[type=submit]').click();
    cy.url().should('include', '/dashboard');
  });
});
```

**4. Load testing:**
```bash
# Apache Bench
ab -n 1000 -c 10 http://localhost:3000/api/users

# Autocannon
autocannon -c 10 -d 10 http://localhost:3000/api/users
```

**Test pyramid:**
```
      /\
     /E2E\      10% - Slow, expensive
    /──────\
   /Integr.\   20% - Medium speed
  /──────────\
 / Unit tests \ 70% - Fast, many tests
/──────────────\
```

---

### 🔒 Säkerhetsfrågor

#### 16. Hur skyddar jag mitt API mot attacker?

**Svar:**

**1. HTTPS alltid:**
```
❌ http://api.example.com
✅ https://api.example.com
```

**2. Input validation:**
```javascript
const schema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).required()
});
```

**3. SQL Injection-skydd:**
```javascript
❌ db.query(`SELECT * FROM users WHERE id = ${userId}`)
✅ db.query('SELECT * FROM users WHERE id = ?', [userId])
```

**4. Rate limiting:**
```javascript
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 min
  max: 100  // Max 100 requests
});
app.use(limiter);
```

**5. CORS korrekt konfigurerad:**
```javascript
app.use(cors({
  origin: ['https://myapp.com'],  // Inte '*' i produktion!
  credentials: true
}));
```

**6. Helmet.js (säkerhets-headers):**
```javascript
const helmet = require('helmet');
app.use(helmet());
```

**7. JWT best practices:**
```javascript
- Kort lifetime (15 min - 1h)
- Lagra INTE i localStorage (XSS risk)
- Använd httpOnly cookies eller memory
- Refresh tokens för längre sessions
```

**8. API Gateway:**
```
Klient → API Gateway → Backend
         ↑
    - Autentisering
    - Rate limiting
    - DDoS protection
    - IP whitelist
```

---

#### 17. Ska jag använda OAuth 2.0 eller JWT?

**Svar:**

**De är inte motsatser - de används ofta tillsammans!**

**JWT** (JSON Web Token):
- **Vad:** Token-format
- **När:** Stateless autentisering
- **Användning:** Du skapar och validerar tokens själv

**OAuth 2.0:**
- **Vad:** Auktoriserings-ramverk
- **När:** Third-party access ("Logga in med Google")
- **Användning:** Delegerad access till användardata

**Kombinera dem:**
```
1. Användare klickar "Logga in med Google"
2. OAuth 2.0 flow med Google
3. Din server får access token från Google
4. Du skapar en JWT för användaren
5. Användaren använder JWT för dina API:er
```

**Använd JWT när:**
- ✅ Intern autentisering
- ✅ Stateless API
- ✅ Mikroservices
- ✅ Single Sign-On

**Använd OAuth 2.0 när:**
- ✅ "Logga in med Google/Facebook/GitHub"
- ✅ Third-party app behöver access till användardata
- ✅ Begränsad access (scopes)

---

#### 18. Hur hanterar jag känslig data i API:er?

**Svar:**

**1. Kryptera vid transport (HTTPS):**
```
Alla requests måste gå över HTTPS
```

**2. Kryptera vid lagring:**
```javascript
// Lösenord
const bcrypt = require('bcrypt');
const hashedPassword = await bcrypt.hash(password, 10);

// Känslig data (kreditkort, personnummer)
const crypto = require('crypto');
const algorithm = 'aes-256-gcm';
const key = process.env.ENCRYPTION_KEY;

function encrypt(text) {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv(algorithm, key, iv);
  // ... encryption logic
}
```

**3. Aldrig logga känslig data:**
```javascript
❌ console.log('Password:', password);
❌ console.log('Credit card:', creditCard);
✅ console.log('User logged in:', userId);
```

**4. Filtrera responses:**
```javascript
// Använd serializers för att ta bort känsliga fält
class UserSerializer {
  static serialize(user) {
    return {
      id: user.id,
      name: user.name,
      email: user.email,
      // Exkludera: password, ssn, creditCard
    };
  }
}
```

**5. Använd tokens istället för känslig data:**
```javascript
// Stripe example
const paymentIntent = await stripe.paymentIntents.create({
  amount: 1000,
  currency: 'sek',
  payment_method: 'pm_card_visa',  // Token, inte riktigt kortnummer
});
```

**6. PCI DSS compliance** (för betalningar):
- Lagra ALDRIG hela kortnummer
- Använd tokenization (Stripe, Klarna)
- Följ PCI DSS-regler

---

## 📖 Ordlista

> **Format:** Svensk term / Engelsk term - Förklaring

---

### A

**API** (Application Programming Interface)
- Ett sätt för program att kommunicera med varandra
- Exempel: Väderapp hämtar data från väder-API

**API Gateway**
- En "front door" för mikroservices
- Hanterar routing, autentisering, rate limiting
- Exempel: AWS API Gateway, Kong

**API-nyckel** / API Key
- En unik sträng för att identifiera och autentisera API-anrop
- Exempel: `apikey=abc123def456`

**AsyncAPI**
- Specifikation för event-driven API:er
- Som OpenAPI men för async kommunikation

**Autentisering** / Authentication
- Verifiera vem användaren är
- Exempel: Login med användarnamn + lösenord

**Auktorisering** / Authorization
- Kontrollera vad användaren får göra
- Exempel: Är användaren admin?

---

### B

**Backend**
- Serverdelen av en applikation
- Hanterar logik, databas, API:er

**Bearer Token**
- En typ av access token
- Format: `Authorization: Bearer <token>`

**Body** / Request Body
- Data som skickas med POST/PUT-requests
- Exempel: `{"name": "Anna", "email": "anna@example.com"}`

---

### C

**Cache** / Caching
- Lagra data temporärt för snabbare access
- Exempel: Redis, CDN, browser cache

**CDN** (Content Delivery Network)
- Nätverk av servrar som cachar content globalt
- Exempel: CloudFlare, AWS CloudFront

**CORS** (Cross-Origin Resource Sharing)
- Säkerhetsmekanism för cross-origin requests
- Tillåter/blockerar requests från andra domäner

**CRUD**
- Create, Read, Update, Delete
- Grundläggande dataoperationer
- Mappar till: POST, GET, PUT/PATCH, DELETE

**cURL**
- Kommandoradsverktyg för HTTP-requests
- Exempel: `curl https://api.example.com/users`

---

### D

**DataLoader**
- Batch och cache laddning av data
- Löser N+1-problemet i GraphQL

**Deprecated** / Föråldrad
- Funktion som inte längre rekommenderas
- Kommer att tas bort i framtida version

**Dokumentation** / Documentation
- Beskrivning av hur API:et fungerar
- Bästa praxis: OpenAPI/Swagger

---

### E

**Edge Computing**
- Kör kod nära användaren (geografiskt)
- Exempel: Cloudflare Workers, Deno Deploy

**Endpoint**
- En specifik URL där man kan hämta/skicka data
- Exempel: `https://api.example.com/users`

**Error Handling** / Felhantering
- Hur API:et hanterar och kommunicerar fel
- Exempel: Statuskoder, felmeddelanden

**ETag** (Entity Tag)
- Hash för caching och conditional requests
- Exempel: `ETag: "33a64df551425fcc55e4"`

---

### F

**Frontend**
- Klientdelen av en applikation
- Exempel: React-app, mobilapp

**Fetch API**
- JavaScript-funktion för HTTP-requests
- Exempel: `fetch('https://api.example.com/users')`

---

### G

**GraphQL**
- Query-språk för API:er
- Alternativ till REST, mer flexibelt

**gRPC**
- Remote Procedure Call-framework av Google
- Använder HTTP/2 och Protocol Buffers

---

### H

**HATEOAS**
- Hypermedia As The Engine Of Application State
- REST-princip: API svarar med länkar till relaterade resurser

**Header** / HTTP Header
- Metadata i HTTP-requests/responses
- Exempel: `Content-Type: application/json`

**HTTP** (HyperText Transfer Protocol)
- Protokoll för kommunikation på webben

**HTTPS**
- HTTP med kryptering (SSL/TLS)
- Säker version av HTTP

---

### I

**Idempotent** / Idempotens
- Operation som ger samma resultat vid upprepade anrop
- Exempel: PUT, DELETE är idempotenta; POST är inte

**Integration Test**
- Test av flera komponenter tillsammans
- Testar hela flöden

---

### J

**JSON** (JavaScript Object Notation)
- Dataformat för API:er
- Exempel: `{"name": "Anna", "age": 28}`

**JWT** (JSON Web Token)
- Token-format för autentisering
- Self-contained (innehåller all info)

---

### K

**Klient** / Client
- Den som begär data från API:et
- Exempel: Webbläsare, mobilapp

---

### L

**Latens** / Latency
- Tid från request till response
- Mål: <200ms för bra UX

**Load Balancer**
- Distribuerar trafik mellan flera servrar
- Förbättrar prestanda och tillförlitlighet

---

### M

**Middleware**
- Kod som körs mellan request och response
- Exempel: Autentisering, logging, CORS

**Mikroservices** / Microservices
- Arkitektur med många små, oberoende tjänster
- Motsats: Monolith

**mTLS** (Mutual TLS)
- Både klient och server verifierar varandra
- Högre säkerhet än vanlig TLS

---

### N

**N+1 Problem**
- Prestanda-problem med många databas-queries
- Exempel: 1 query för lista + N queries för detaljer

---

### O

**OAuth 2.0**
- Auktoriserings-ramverk
- Används för "Logga in med Google/Facebook"

**OpenAPI** (tidigare Swagger)
- Specifikation för att beskriva REST API:er
- Standard för API-dokumentation

---

### P

**Paginering** / Pagination
- Dela upp stora dataset i sidor
- Exempel: `?page=2&limit=20`

**Payload**
- Data som skickas i request/response
- Synonym med "body" i många sammanhang

**Protocol Buffers** (Protobuf)
- Binärt dataformat (Google)
- Används med gRPC

---

### Q

**Query Parameters**
- Data i URL efter `?`
- Exempel: `/users?role=admin&active=true`

---

### R

**Rate Limiting**
- Begränsa antal requests per tidsenhet
- Förhindrar missbruk och DDoS

**RBAC** (Role-Based Access Control)
- Behörighetssystem baserat på roller
- Exempel: admin, user, guest

**Redis**
- In-memory databas för caching
- Extremt snabb

**Request**
- Förfrågan från klient till server
- Innehåller: metod, URL, headers, body

**Response**
- Svar från server till klient
- Innehåller: statuskod, headers, body

**REST** (Representational State Transfer)
- Arkitekturstil för API-design
- Principer: stateless, cacheable, etc.

**RESTful**
- API som följer REST-principer

---

### S

**SDK** (Software Development Kit)
- Bibliotek för att använda ett API
- Exempel: AWS SDK, Stripe SDK

**Serialisering** / Serialization
- Konvertera objekt till sträng (JSON, XML)
- Motsats: Deserialisering

**Server**
- Dator/program som svarar på requests
- Där API:et körs

**Serverless**
- Kör kod utan att hantera servrar
- Exempel: AWS Lambda, Vercel Functions

**Session**
- Tillstånd mellan klient och server
- REST är stateless (inga sessions)

**SOAP** (Simple Object Access Protocol)
- Äldre protokoll för API:er
- Använder XML, mer komplext än REST

**SSE** (Server-Sent Events)
- Server pushar data till klient (envägs)
- Enklare än WebSockets

**SSL/TLS**
- Krypteringsprotokoll för HTTPS

**Stateless** / Tillståndslös
- Ingen session-info sparas på servern
- Varje request innehåller all info

**Statuskod** / Status Code
- Numerisk kod för result av request
- Exempel: 200 OK, 404 Not Found, 500 Error

**Swagger**
- Verktyg för OpenAPI
- UI för att testa API:er

---

### T

**Throttling**
- Begränsa hastighet på requests
- Synonym med rate limiting

**Token**
- Sträng för autentisering
- Exempel: JWT, OAuth access token

**TLS** (Transport Layer Security)
- Krypteringsprotokoll (SSL:s efterföljare)

---

### U

**Unit Test**
- Test av enskild funktion/komponent
- Isolerad från resten av systemet

**URL** (Uniform Resource Locator)
- Adress till en resurs
- Exempel: `https://api.example.com/users/123`

---

### V

**Validering** / Validation
- Kontrollera att data är korrekt
- Exempel: Email-format, required fields

**Versionering** / Versioning
- Hantera olika versioner av API
- Exempel: `/v1/users`, `/v2/users`

---

### W

**Webhook**
- HTTP callback när en event inträffar
- Server pushar data till klient

**WebSocket**
- Persistent, tvåvägs-kommunikation
- Används för real-time (chat, gaming)

---

### X

**XML** (eXtensible Markup Language)
- Dataformat (äldre än JSON)
- Används fortfarande i SOAP, enterprise

**XSS** (Cross-Site Scripting)
- Säkerhets-sårbarhet
- Attackerare injicerar skadlig kod

---

### Z

**Zero Trust**
- Säkerhetsmodell: "lita på ingenting"
- Verifiera varje request, varje gång

---

## 🔤 Akronymer

| Akronym | Utskrivet | Betydelse |
|---------|-----------|-----------|
| **API** | Application Programming Interface | Gränssnitt för programkommunikation |
| **CDN** | Content Delivery Network | Globalt nätverk för content |
| **CORS** | Cross-Origin Resource Sharing | Säkerhet för cross-domain requests |
| **CRUD** | Create, Read, Update, Delete | Grundläggande dataoperationer |
| **DNS** | Domain Name System | Översätter domännamn till IP |
| **HTTP** | HyperText Transfer Protocol | Protokoll för webben |
| **HTTPS** | HTTP Secure | Krypterad HTTP |
| **JWT** | JSON Web Token | Token-format |
| **REST** | Representational State Transfer | API-arkitekturstil |
| **SDK** | Software Development Kit | Utvecklingsbibliotek |
| **SQL** | Structured Query Language | Databasspråk |
| **SSL** | Secure Sockets Layer | Krypteringsprotokoll |
| **TLS** | Transport Layer Security | SSL:s efterföljare |
| **URI** | Uniform Resource Identifier | Identifierare för resurs |
| **URL** | Uniform Resource Locator | Adress till resurs |
| **UUID** | Universally Unique Identifier | Unik identifierare |
| **XML** | eXtensible Markup Language | Markup-språk |

---

## 📚 Relaterade resurser

- [Huvudindex](./README.md) - Tillbaka till guidens start
- [Nivå 1-5](./README.md#-navigera-efter-din-kunskapsnivå) - Lärvägar
- [Övningar](./övningar.md) - 38 praktiska övningar
- [Projekt](./projekt.md) - 2 stora projekt
- [Resurser](./resurser.md) - Böcker, kurser, verktyg

---

**Hittade du inte svaret?**
- Sök i guiden (Ctrl/Cmd + F)
- Kolla [resurser.md](./resurser.md) för communities
- Öppna en GitHub issue

---

[🏠 Tillbaka till huvudindex](./README.md)
