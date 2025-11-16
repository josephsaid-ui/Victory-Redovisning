# ⚙️ Nivå 3: Tekniska Detaljer och REST-principer

> **För utvecklare som bygger API:er**
>
> **Tidsåtgång**: 5-6 timmar + Projekt 1
>
> **Förkunskaper**: Nivå 1-2 eller erfarenhet av webbutveckling

---

## 📚 Innehåll

1. [REST-arkitektur i detalj](#rest-arkitektur-i-detalj)
2. [HTTP-statuskoder (komplett guide)](#http-statuskoder-komplett-guide)
3. [Error handling och edge cases](#error-handling-och-edge-cases)
4. [CORS - Cross-Origin Resource Sharing](#cors---cross-origin-resource-sharing)
5. [Säkerhet: HTTPS, rate limiting, input validation](#säkerhet-grundläggande)
6. [Postman avancerat](#postman-avancerat)
7. [API-dokumentation med Swagger/OpenAPI](#api-dokumentation-med-swaggeropenapi)
8. [Testning av API:er](#testning-av-apier)
9. [Projekt 1: Bygg en väderapp](#projekt-1-bygg-en-väderapp)

---

## 🏛️ REST-arkitektur i detalj

### Vad är REST?

**REST** (Representational State Transfer) är en arkitekturstil för att designa API:er, introducerad 2000 av Roy Fielding.

**Inte:**
- ❌ Ett protokoll
- ❌ En standard
- ❌ Ett ramverk

**Utan:**
- ✅ En uppsättning designprinciper
- ✅ Riktlinjer för hur API:er bör fungera
- ✅ Best practices

### De 6 REST-principerna

#### 1. Client-Server-separation

```
┌─────────────┐          ┌─────────────┐
│   CLIENT    │          │   SERVER    │
│  (Frontend) │ ←──────→ │  (Backend)  │
│             │          │             │
│ - UI/UX     │          │ - Business  │
│ - Rendering │          │   logic     │
│ - User      │          │ - Database  │
│   input     │          │ - Security  │
└─────────────┘          └─────────────┘

Fördel: Kan utvecklas oberoende
```

#### 2. Stateless (tillståndslös)

Varje request måste innehålla ALL information som behövs.

```
❌ STATEFUL (dåligt):
Request 1: Login(username, password)
→ Server sparar session
Request 2: GetProfile()
→ Server använder sparad session

✅ STATELESS (bra):
Request 1: GetProfile(authToken)
→ Token innehåller all info
Request 2: UpdateProfile(authToken, newData)
→ Token innehåller all info
```

**Fördelar:**
- ✅ Enklare skalning (vilken server som helst kan hantera requesten)
- ✅ Bättre tillförlitlighet (inga "lost sessions")
- ✅ Enklare cachning

**I praktiken:**
```javascript
// Klienten skickar auth-token i varje request
fetch('https://api.example.com/profile', {
  headers: {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
  }
});
```

#### 3. Cacheable (cachningsbart)

Responses ska ange om de kan cachas.

```http
HTTP/1.1 200 OK
Cache-Control: max-age=3600, public
ETag: "33a64df551425fcc55e4d42a148795d9"
Last-Modified: Mon, 16 Nov 2024 10:00:00 GMT

{
  "temperature": 15
}
```

**Cache-strategier:**

| Header | Beskrivning | Exempel |
|--------|-------------|---------|
| `Cache-Control: max-age=3600` | Cacha i 1 timme | Väderdata |
| `Cache-Control: no-cache` | Validera innan användning | Banksaldo |
| `Cache-Control: no-store` | Cacha ALDRIG | Känslig data |
| `Cache-Control: public` | Kan cachas av alla (CDN) | Bilder |
| `Cache-Control: private` | Endast i webbläsare | Personlig data |

#### 4. Uniform Interface (enhetligt gränssnitt)

**a) Resursbaserad:**
```
✅ /users/123
✅ /products/abc
✅ /orders/456

❌ /getUser?id=123
❌ /fetchProduct?sku=abc
```

**b) Manipulation genom representationer:**
```javascript
// Hämta representation (JSON)
GET /users/123
→ {"id": 123, "name": "Anna"}

// Ändra genom att skicka ny representation
PUT /users/123
Body: {"id": 123, "name": "Anna Svensson"}
```

**c) Självbeskrivande meddelanden:**
```http
Content-Type: application/json
Accept: application/json
```

**d) HATEOAS (Hypermedia):**
```json
{
  "id": 123,
  "name": "Anna",
  "links": [
    {"rel": "self", "href": "/users/123"},
    {"rel": "posts", "href": "/users/123/posts"},
    {"rel": "friends", "href": "/users/123/friends"}
  ]
}
```

#### 5. Layered System (lager-system)

Klienten behöver inte veta om den pratar med slutservern eller en mellanliggande server.

```
CLIENT → LOAD BALANCER → API GATEWAY → CACHE → SERVER → DATABASE
         ↑               ↑              ↑
      Transparent     Transparent   Transparent
```

#### 6. Code on Demand (valfritt)

Servern kan skicka executable code (t.ex. JavaScript).

```json
{
  "data": {...},
  "script": "function validate() { ... }"
}
```

*Används sällan i moderna API:er.*

### RESTful vs REST-like

```
┌────────────────┬──────────────┬─────────────┐
│ Princip        │ RESTful      │ REST-like   │
├────────────────┼──────────────┼─────────────┤
│ HTTP-metoder   │ ✅ Använder  │ ⚠️ Ibland   │
│ Stateless      │ ✅ Alltid    │ ⚠️ Mestadels│
│ Resursbaserad  │ ✅ Alltid    │ ✅ Ja       │
│ HATEOAS        │ ✅ Ja        │ ❌ Sällan   │
│ Cachning       │ ✅ Konfigur. │ ⚠️ Ibland   │
└────────────────┴──────────────┴─────────────┘
```

**Verklighet:** De flesta API:er är "REST-like" (inte fullt RESTful), och det är OK!

---

## 📊 HTTP-statuskoder (komplett guide)

### 2xx - Success

| Kod | Namn | Användning |
|-----|------|------------|
| **200** | OK | Standard success (GET, PUT, PATCH) |
| **201** | Created | Resurs skapad (POST) |
| **202** | Accepted | Request accepterad, men inte färdigbehandlad (async) |
| **204** | No Content | Success, men inget att returnera (DELETE) |

**Exempel:**
```javascript
// 200 OK
GET /users/123
→ {"id": 123, "name": "Anna"}

// 201 Created
POST /users
→ Location: /users/124
  {"id": 124, "name": "Erik"}

// 204 No Content
DELETE /users/123
→ (ingen body)
```

### 3xx - Redirection

| Kod | Namn | Användning |
|-----|------|------------|
| **301** | Moved Permanently | URL har ändrats permanent |
| **302** | Found | Temporär redirect |
| **304** | Not Modified | Använd cachad version |
| **307** | Temporary Redirect | Som 302, men behåll HTTP-metod |
| **308** | Permanent Redirect | Som 301, men behåll HTTP-metod |

### 4xx - Client Errors

| Kod | Namn | När den används | Exempel |
|-----|------|----------------|---------|
| **400** | Bad Request | Felaktig syntax | Saknad required field |
| **401** | Unauthorized | Autentisering krävs | Ingen/ogiltig token |
| **403** | Forbidden | Inte tillåten | Användare saknar rättigheter |
| **404** | Not Found | Resursen finns inte | /users/999999 |
| **405** | Method Not Allowed | Fel HTTP-metod | DELETE på read-only resurs |
| **409** | Conflict | Konflikt (t.ex. duplicate) | Email redan registrerad |
| **422** | Unprocessable Entity | Validering misslyckades | Ogiltigt email-format |
| **429** | Too Many Requests | Rate limit nådd | Max 100 req/min överskridet |

**Error response-format:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Ogiltigt email-format",
    "details": [
      {
        "field": "email",
        "issue": "Måste vara en giltig email-adress"
      }
    ],
    "timestamp": "2024-11-16T10:30:00Z",
    "path": "/api/users"
  }
}
```

### 5xx - Server Errors

| Kod | Namn | När den används |
|-----|------|----------------|
| **500** | Internal Server Error | Okänt fel på servern |
| **502** | Bad Gateway | Gateway fick ogiltigt svar |
| **503** | Service Unavailable | Servern är tillfälligt nere |
| **504** | Gateway Timeout | Gateway timeout |

**Viktigt:** 5xx = Serverns fel, INTE klientens!

---

## 🛡️ Error Handling och Edge Cases

### Best practices för felhantering

#### 1. Konsistent error-format

```json
{
  "error": {
    "code": "UNIQUE_ERROR_CODE",
    "message": "Mänsklig läsbar beskrivning",
    "details": [...],
    "timestamp": "ISO 8601 timestamp",
    "requestId": "för debugging"
  }
}
```

#### 2. Hjälpsamma felmeddelanden

```json
❌ Dåligt:
{
  "error": "Error"
}

✅ Bra:
{
  "error": {
    "code": "INVALID_EMAIL",
    "message": "Email-adressen 'anna@invalid' är ogiltig",
    "hint": "Använd formatet: namn@domän.se"
  }
}
```

#### 3. Validera input

```javascript
// Node.js/Express exempel
app.post('/users', (req, res) => {
  const { email, password } = req.body;

  // Validering
  if (!email || !email.includes('@')) {
    return res.status(422).json({
      error: {
        code: 'INVALID_EMAIL',
        message: 'Ogiltigt email-format',
        field: 'email'
      }
    });
  }

  if (!password || password.length < 8) {
    return res.status(422).json({
      error: {
        code: 'WEAK_PASSWORD',
        message: 'Lösenordet måste vara minst 8 tecken',
        field: 'password'
      }
    });
  }

  // Skapa användare...
});
```

```python
# Python/Flask exempel
from flask import Flask, request, jsonify

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Validering
    if not data.get('email') or '@' not in data['email']:
        return jsonify({
            'error': {
                'code': 'INVALID_EMAIL',
                'message': 'Ogiltigt email-format',
                'field': 'email'
            }
        }), 422

    # Skapa användare...
```

### Edge cases att hantera

#### 1. Tomma listor

```javascript
GET /users?role=admin

// Om inga admins finns:
✅ Bra:
{
  "data": [],
  "total": 0,
  "page": 1
}

❌ Dåligt:
404 Not Found
```

#### 2. Stora dataset (paginering)

```javascript
GET /users?page=1&limit=20

{
  "data": [...],  // Max 20 items
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  },
  "links": {
    "self": "/users?page=1&limit=20",
    "next": "/users?page=2&limit=20",
    "last": "/users?page=8&limit=20"
  }
}
```

#### 3. Långsamma operationer (async)

```javascript
// Initierar långsam operation
POST /reports/generate
→ 202 Accepted
{
  "jobId": "abc123",
  "status": "processing",
  "statusUrl": "/reports/status/abc123"
}

// Kolla status
GET /reports/status/abc123
→ 200 OK
{
  "jobId": "abc123",
  "status": "completed",
  "result": "/reports/download/abc123"
}
```

#### 4. Idempotens (säker att anropa flera gånger)

```javascript
// POST är INTE idempotent
POST /users
→ Skapar ny användare varje gång

// PUT är idempotent
PUT /users/123
{"name": "Anna"}
→ Samma resultat oavsett antal anrop

// DELETE är idempotent
DELETE /users/123
→ Första: 204 No Content
→ Andra: 404 Not Found (OK!)
```

---

## 🌍 CORS - Cross-Origin Resource Sharing

### Problemet: Same-Origin Policy

Webbläsare blockerar requests från en annan origin:

```
Frontend:  https://myapp.com
Backend:   https://api.myapp.com
           ↑
        Olika origins! ❌
```

**Origin = protocol + domain + port**

| URL 1 | URL 2 | Same origin? |
|-------|-------|--------------|
| `https://api.example.com/users` | `https://api.example.com/posts` | ✅ Ja |
| `https://api.example.com` | `http://api.example.com` | ❌ Nej (protokoll) |
| `https://api.example.com` | `https://www.example.com` | ❌ Nej (subdomain) |
| `https://api.example.com:443` | `https://api.example.com:8080` | ❌ Nej (port) |

### CORS Headers

```http
# Preflight request (OPTIONS)
OPTIONS /api/users
Origin: https://myapp.com
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Content-Type, Authorization

# Response från server
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: https://myapp.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
Access-Control-Max-Age: 3600

# Actual request
POST /api/users
Origin: https://myapp.com

# Response
HTTP/1.1 201 Created
Access-Control-Allow-Origin: https://myapp.com
```

### Implementera CORS i backend

**Node.js/Express:**
```javascript
const cors = require('cors');

// Tillåt alla origins (development)
app.use(cors());

// Tillåt specifika origins (production)
app.use(cors({
  origin: ['https://myapp.com', 'https://www.myapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,  // Tillåt cookies
  maxAge: 3600       // Cache preflight i 1h
}));
```

**Python/Flask:**
```python
from flask_cors import CORS

app = Flask(__name__)

# Tillåt alla origins
CORS(app)

# Tillåt specifika origins
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://myapp.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

### CORS-fel (debugging)

**Felmeddelande i webbläsare:**
```
Access to fetch at 'https://api.example.com/users' from origin
'https://myapp.com' has been blocked by CORS policy: No
'Access-Control-Allow-Origin' header is present on the requested resource.
```

**Lösning:**
1. Lägg till CORS headers på backend
2. Kontrollera att origin är tillåten
3. För credentials (cookies), sätt `Access-Control-Allow-Credentials: true`

---

## 🔒 Säkerhet: Grundläggande

### 1. Använd alltid HTTPS

```
❌ http://api.example.com   ← Data i klartext
✅ https://api.example.com  ← Krypterad kommunikation
```

**Varför?**
- Skyddar mot man-in-the-middle-attacker
- Krypterar API-nycklar och tokens
- SEO-fördel
- Krävs för moderna features (geolocation, etc.)

### 2. Rate Limiting

Begränsa antal requests per tidsenhet för att förhindra missbruk.

```
100 requests/minut per IP-adress
1000 requests/timme per API-nyckel
```

**Implementation (Express):**
```javascript
const rateLimit = require('express-rate-limit');

const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minuter
  max: 100,                   // Max 100 requests
  message: {
    error: {
      code: 'RATE_LIMIT_EXCEEDED',
      message: 'För många requests, försök igen om 15 minuter'
    }
  },
  standardHeaders: true,      // Returnera RateLimit headers
  legacyHeaders: false,
});

app.use('/api/', limiter);
```

**Response headers:**
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 73
X-RateLimit-Reset: 1699268400
```

### 3. Input Validation

**Validera ALLT från klienten!**

```javascript
// Använd bibliotek som Joi eller Zod
const Joi = require('joi');

const userSchema = Joi.object({
  email: Joi.string().email().required(),
  password: Joi.string().min(8).required(),
  age: Joi.number().integer().min(18).max(120)
});

app.post('/users', (req, res) => {
  const { error, value } = userSchema.validate(req.body);

  if (error) {
    return res.status(422).json({
      error: {
        code: 'VALIDATION_ERROR',
        details: error.details
      }
    });
  }

  // Fortsätt med validerad data...
});
```

### 4. SQL Injection-skydd

```javascript
❌ FARLIGT:
const query = `SELECT * FROM users WHERE id = ${req.params.id}`;
// Attackerare kan skicka: 1 OR 1=1

✅ SÄKERT (prepared statements):
const query = 'SELECT * FROM users WHERE id = ?';
db.query(query, [req.params.id]);
```

### 5. API-nyckel rotation

```
Best practices:
- Rotera nycklar varje 90 dagar
- Använd olika nycklar för dev/staging/production
- Lagra ALDRIG nycklar i kod (använd .env)
- Revokera nycklar vid misstänkt aktivitet
```

---

## 🧪 Postman Avancerat

### Collections och Environment Variables

**Environment variables:**
```json
{
  "baseUrl": "https://api.example.com",
  "apiKey": "abc123",
  "userId": "{{$randomInt}}"
}
```

**Använd i requests:**
```
GET {{baseUrl}}/users/{{userId}}
Authorization: Bearer {{apiKey}}
```

### Pre-request Scripts

```javascript
// Generera timestamp
pm.environment.set("timestamp", new Date().toISOString());

// Generera random email
const randomEmail = `user${Math.random()}@example.com`;
pm.environment.set("email", randomEmail);
```

### Tests (Automated testing)

```javascript
// Testa statuskod
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// Testa response time
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// Testa JSON-innehåll
pm.test("User has email", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.email).to.exist;
});

// Spara värde från response
var jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);
```

### Collection Runner

Kör alla requests i en collection automatiskt:

```
1. Collection: "User Management"
   ├─ Create User (POST)
   ├─ Get User (GET) ← använder userId från Create
   ├─ Update User (PUT)
   └─ Delete User (DELETE)

2. Run Collection → Se alla tester köras
```

---

## 📖 API-dokumentation med Swagger/OpenAPI

### Vad är OpenAPI?

**OpenAPI** (tidigare Swagger) är en standard för att beskriva RESTful API:er.

```yaml
openapi: 3.1.0
info:
  title: User Management API
  version: 1.0.0
  description: API för att hantera användare

servers:
  - url: https://api.example.com/v1

paths:
  /users:
    get:
      summary: Hämta alla användare
      responses:
        '200':
          description: Lista av användare
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'

    post:
      summary: Skapa ny användare
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/NewUser'
      responses:
        '201':
          description: Användare skapad

  /users/{userId}:
    get:
      summary: Hämta specifik användare
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Användare hittad
        '404':
          description: Användare inte hittad

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
          format: email

    NewUser:
      type: object
      required:
        - name
        - email
      properties:
        name:
          type: string
        email:
          type: string
          format: email
```

### Generera dokumentation

**Swagger UI:**
```javascript
// Node.js/Express
const swaggerUi = require('swagger-ui-express');
const swaggerDocument = require('./swagger.json');

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));
```

Besök `https://api.example.com/api-docs` för interaktiv dokumentation!

---

## 🧪 Testning av API:er

### Unit tests (JavaScript med Jest)

```javascript
// api.test.js
const request = require('supertest');
const app = require('./app');

describe('User API', () => {
  test('GET /users returnerar 200', async () => {
    const response = await request(app).get('/users');
    expect(response.statusCode).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);
  });

  test('POST /users skapar ny användare', async () => {
    const newUser = {
      name: 'Anna',
      email: 'anna@example.com'
    };

    const response = await request(app)
      .post('/users')
      .send(newUser);

    expect(response.statusCode).toBe(201);
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe(newUser.email);
  });

  test('POST /users validerar email', async () => {
    const invalidUser = {
      name: 'Anna',
      email: 'invalid-email'
    };

    const response = await request(app)
      .post('/users')
      .send(invalidUser);

    expect(response.statusCode).toBe(422);
  });
});
```

### Integration tests (Python med pytest)

```python
# test_api.py
import pytest
import requests

BASE_URL = "https://api.example.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    new_user = {
        "name": "Anna",
        "email": "anna@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.status_code == 201
    assert "id" in response.json()

def test_email_validation():
    invalid_user = {
        "name": "Anna",
        "email": "invalid"
    }
    response = requests.post(f"{BASE_URL}/users", json=invalid_user)
    assert response.status_code == 422
```

---

## 🎯 Sammanfattning Nivå 3

### Vad du har lärt dig

✅ **REST-principer** - De 6 grundläggande principerna
✅ **HTTP-statuskoder** - Komplett guide (2xx, 3xx, 4xx, 5xx)
✅ **Error handling** - Best practices och edge cases
✅ **CORS** - Cross-origin requests och säkerhet
✅ **Säkerhet** - HTTPS, rate limiting, validation
✅ **Postman** - Avancerad testning och automation
✅ **Dokumentation** - Swagger/OpenAPI
✅ **Testning** - Unit och integration tests

### Checklista

- [ ] Jag kan förklara de 6 REST-principerna
- [ ] Jag förstår skillnaden mellan 4xx och 5xx-fel
- [ ] Jag kan implementera error handling
- [ ] Jag vet vad CORS är och hur man fixar det
- [ ] Jag har implementerat rate limiting
- [ ] Jag kan skriva API-tester
- [ ] Jag har dokumenterat ett API med OpenAPI

---

## 🚀 Projekt 1: Bygg en väderapp med API-integration

**Se detaljerad projektbeskrivning i:** [projekt.md → Projekt 1](./projekt.md#projekt-1-väderapp)

---

## ➡️ Nästa steg

**[Nivå 4: Avancerade Koncept →](./nivå-4-avancerat.md)**

I Nivå 4 lär du dig:
- GraphQL vs REST
- API-versionering strategier
- OAuth 2.0 och JWT i detalj
- Caching-strategier
- Mikroservices och API Gateways

---

[🏠 Tillbaka till huvudindex](./README.md) | [⬅️ Nivå 2](./nivå-2-tekniska-termer.md) | [➡️ Nivå 4](./nivå-4-avancerat.md)
