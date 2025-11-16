# 🚀 Nivå 4: Avancerade Koncept och Arkitektur

> **För erfarna utvecklare**
>
> **Tidsåtgång**: 6-8 timmar
>
> **Förkunskaper**: Nivå 1-3 eller erfarenhet av att bygga API:er

---

## 📚 Innehåll

1. [GraphQL vs REST](#graphql-vs-rest)
2. [API-versionering](#api-versionering)
3. [Autentisering och auktorisering](#autentisering-och-auktorisering)
4. [OAuth 2.0 och JWT](#oauth-20-och-jwt)
5. [Caching-strategier](#caching-strategier)
6. [API Design Patterns](#api-design-patterns)
7. [Mikroservices och API Gateway](#mikroservices-och-api-gateway)
8. [WebSockets och realtidskommunikation](#websockets-och-realtidskommunikation)

---

## ⚡ GraphQL vs REST

### Vad är GraphQL?

**GraphQL** är ett query-språk för API:er, utvecklat av Facebook 2012 (open source 2015).

**Fundamental skillnad:**
```
REST:  Flera endpoints, fasta responses
GraphQL:  Ett endpoint, flexibla queries
```

### REST vs GraphQL - Exempel

#### Scenario: Hämta användare med inlägg och kommentarer

**REST:**
```javascript
// 3 separata requests
GET /users/123
→ {id: 123, name: "Anna", ...}

GET /users/123/posts
→ [{id: 1, title: "..."}, {id: 2, ...}]

GET /posts/1/comments
→ [{id: 1, text: "..."}, ...]
GET /posts/2/comments
→ [...]

Total: 4+ requests
```

**GraphQL:**
```graphql
# 1 request
query {
  user(id: 123) {
    name
    email
    posts {
      title
      comments {
        text
        author {
          name
        }
      }
    }
  }
}

Total: 1 request
```

### GraphQL Schema

```graphql
# Schema Definition Language (SDL)
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Post {
  id: ID!
  title: String!
  content: String!
  author: User!
  comments: [Comment!]!
}

type Comment {
  id: ID!
  text: String!
  author: User!
}

type Query {
  user(id: ID!): User
  users: [User!]!
  post(id: ID!): Post
}

type Mutation {
  createUser(name: String!, email: String!): User!
  updateUser(id: ID!, name: String): User!
  deleteUser(id: ID!): Boolean!
}
```

### GraphQL Queries

```graphql
# Hämta specifika fält
query {
  user(id: 123) {
    name
    email
  }
}

# Med variabler
query GetUser($userId: ID!) {
  user(id: $userId) {
    name
    posts {
      title
    }
  }
}

# Flera queries i en request
query {
  user1: user(id: 123) {
    name
  }
  user2: user(id: 456) {
    name
  }
}
```

### GraphQL Mutations

```graphql
# Skapa användare
mutation {
  createUser(name: "Anna", email: "anna@example.com") {
    id
    name
    email
  }
}

# Uppdatera användare
mutation {
  updateUser(id: 123, name: "Anna Svensson") {
    id
    name
  }
}
```

### För- och nackdelar

| | REST | GraphQL |
|---|------|---------|
| **Flexibilitet** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Caching** | ⭐⭐⭐⭐⭐ (HTTP-cache) | ⭐⭐⭐ (mer komplext) |
| **Lära sig** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Over-fetching** | ❌ Problem | ✅ Ingen |
| **Under-fetching** | ❌ Problem (N+1) | ✅ Ingen |
| **Verktyg** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Real-time** | ⭐⭐ (WebSocket) | ⭐⭐⭐⭐⭐ (Subscriptions) |

**Over-fetching:**
```
REST: GET /users/123
→ Returnerar 50 fält, du behöver bara 3

GraphQL: query { user(id: 123) { name email } }
→ Returnerar exakt vad du behöver
```

**Under-fetching (N+1-problem):**
```
REST:
GET /users → Lista med 10 användare
GET /users/1/posts
GET /users/2/posts
...
Total: 11 requests!

GraphQL:
query { users { name posts { title } } }
Total: 1 request!
```

### När använda vad?

**Använd REST när:**
- ✅ Enkla CRUD-operationer
- ✅ Cachning är kritiskt
- ✅ Publika API:er (enklare att dokumentera)
- ✅ Teamet är bekvämt med REST

**Använd GraphQL när:**
- ✅ Komplexa data-relationer
- ✅ Mobilappar (minska requests)
- ✅ Behöver flexibilitet i queries
- ✅ Real-time med subscriptions

---

## 🔢 API-versionering

### Varför versionera?

```
Problem: Du vill ändra API:et, men gamla klienter använder fortfarande den.

Lösning: Versionering!
```

### Metod 1: URL-versioning (vanligast)

```
https://api.example.com/v1/users
https://api.example.com/v2/users
https://api.example.com/v3/users
```

**Fördelar:**
- ✅ Tydligt och synligt
- ✅ Enkelt att implementera
- ✅ Enkelt att cacha

**Nackdelar:**
- ❌ URL:er ändras
- ❌ Kan bli många versioner

**Implementation:**
```javascript
// Express
app.use('/v1', require('./routes/v1'));
app.use('/v2', require('./routes/v2'));

// Eller med parametrar
app.get('/api/:version/users', (req, res) => {
  const version = req.params.version;
  if (version === 'v1') {
    // v1-logik
  } else if (version === 'v2') {
    // v2-logik
  }
});
```

### Metod 2: Header-versioning

```http
GET /users
Accept: application/vnd.example.v2+json
```

**Fördelar:**
- ✅ URL:er är stabila
- ✅ Följer REST-principer

**Nackdelar:**
- ❌ Mindre synligt
- ❌ Svårare att testa i webbläsare

**Implementation:**
```javascript
app.get('/users', (req, res) => {
  const accept = req.headers['accept'];

  if (accept.includes('v2')) {
    // v2-logik
  } else {
    // v1-logik (default)
  }
});
```

### Metod 3: Query parameter

```
GET /users?version=2
```

**Fördelar:**
- ✅ Enkelt att testa

**Nackdelar:**
- ❌ Inte RESTful
- ❌ Cachnings-problem

### Breaking changes vs non-breaking changes

**Breaking changes (kräver ny version):**
```
❌ Ta bort ett fält
❌ Ändra datatyp (string → int)
❌ Ändra endpoint-namn
❌ Ändra error-format
```

**Non-breaking changes (kan göras i samma version):**
```
✅ Lägga till nytt fält
✅ Lägga till nytt endpoint
✅ Göra required field optional
✅ Lägga till ny HTTP-metod
```

### Deprecation-strategi

```
1. Annonsera deprecation (6 månader i förväg)
   GET /v1/users
   Response headers:
   X-API-Deprecated: true
   X-API-Sunset: 2025-06-01
   Link: <https://api.example.com/v2/users>; rel="successor-version"

2. Logga användning
   - Vilka klienter använder v1?
   - Hur många requests?

3. Kontakta användare
   - Email till API-nyckelhållare

4. Stäng av gamla versionen
   GET /v1/users
   → 410 Gone
   {
     "error": "API v1 är avaktiverad. Använd v2: https://api.example.com/v2/"
   }
```

---

## 🔐 Autentisering och Auktorisering

### Skillnad: Autentisering vs Auktorisering

```
AUTENTISERING (Authentication):
"Vem är du?"
→ Verifiera identitet (användarnamn + lösenord, JWT, etc.)

AUKTORISERING (Authorization):
"Vad får du göra?"
→ Kontrollera rättigheter (admin, user, guest)
```

### Autentiseringsmetoder

#### 1. API-nycklar (enklast, minst säkert)

```http
GET /users
Authorization: ApiKey abc123def456
```

**Användning:**
- Publika API:er
- Server-to-server
- Read-only data

**⚠️ Begränsningar:**
- Ingen användarkontext
- Svårt att revokera
- Kan läcka (loggar, etc.)

#### 2. Basic Authentication

```http
GET /users
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
                     ↑
                Base64(username:password)
```

**⚠️ ANVÄND ALDRIG ÖVER HTTP!**

```
❌ http://api.example.com  + Basic Auth = Lösenord i klartext!
✅ https://api.example.com + Basic Auth = OK (men JWT är bättre)
```

#### 3. Bearer Token (JWT - rekommenderat)

```http
GET /users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

Se detaljer i nästa sektion.

#### 4. OAuth 2.0 (för third-party access)

Se detaljer i nästa sektion.

### Auktorisering med roller (RBAC)

**RBAC** = Role-Based Access Control

```javascript
// Definiera roller
const roles = {
  ADMIN: ['users:read', 'users:write', 'users:delete'],
  EDITOR: ['users:read', 'users:write'],
  VIEWER: ['users:read']
};

// Middleware för auktorisering
function authorize(permission) {
  return (req, res, next) => {
    const userRole = req.user.role;  // Från JWT
    const permissions = roles[userRole];

    if (!permissions.includes(permission)) {
      return res.status(403).json({
        error: 'Forbidden: Saknar rättigheter'
      });
    }

    next();
  };
}

// Använd i routes
app.get('/users', authorize('users:read'), (req, res) => {
  // Endast om användaren har users:read
});

app.delete('/users/:id', authorize('users:delete'), (req, res) => {
  // Endast admins
});
```

---

## 🎫 OAuth 2.0 och JWT

### OAuth 2.0 - "Logga in med Google/Facebook"

**Scenario:** Du bygger en app och vill att användare ska logga in med Google.

#### OAuth 2.0 Flow (Authorization Code)

```
1. ANVÄNDAREN klickar "Logga in med Google"

2. DIN APP redirectar till Google:
   https://accounts.google.com/o/oauth2/v2/auth?
     client_id=DIN_CLIENT_ID&
     redirect_uri=https://dinapp.com/callback&
     response_type=code&
     scope=email profile

3. ANVÄNDAREN loggar in på Google och godkänner

4. GOOGLE redirectar tillbaka med authorization code:
   https://dinapp.com/callback?code=ABC123

5. DIN APP byter code mot access token (server-side):
   POST https://oauth2.googleapis.com/token
   Body:
     code=ABC123
     client_id=DIN_CLIENT_ID
     client_secret=DIN_SECRET
     redirect_uri=https://dinapp.com/callback
     grant_type=authorization_code

6. GOOGLE svarar med access token:
   {
     "access_token": "ya29.a0AfH6SMC...",
     "expires_in": 3600,
     "token_type": "Bearer",
     "refresh_token": "1//0gH..."
   }

7. DIN APP använder access token för att hämta profil:
   GET https://www.googleapis.com/oauth2/v1/userinfo
   Authorization: Bearer ya29.a0AfH6SMC...

8. GOOGLE returnerar användarinfo:
   {
     "id": "123456789",
     "email": "anna@gmail.com",
     "name": "Anna Andersson"
   }
```

**Visualisering:**
```
┌──────────┐                               ┌──────────┐
│ Användare│                               │  Google  │
└────┬─────┘                               └────┬─────┘
     │                                          │
     │  1. Klickar "Logga in med Google"       │
     │◄─────────────────────────────────────┐  │
     │                                      │  │
     │  2. Redirect till Google             │  │
     ├──────────────────────────────────────┼─►│
     │                                      │  │
     │  3. Loggar in + godkänner            │  │
     │◄─────────────────────────────────────┼──┤
     │                                      │  │
     │  4. Redirect med code                │  │
     ├──────────────────────────────────────┘  │
     │                                          │
┌────▼─────┐                                   │
│  Din app │                                   │
└────┬─────┘                                   │
     │  5. Byter code mot token                │
     ├─────────────────────────────────────────►│
     │                                          │
     │  6. Får access token                    │
     │◄─────────────────────────────────────────┤
     │                                          │
     │  7. Hämtar användarinfo med token       │
     ├─────────────────────────────────────────►│
     │                                          │
     │  8. Får användardata                    │
     │◄─────────────────────────────────────────┤
     │                                          │
```

### JWT (JSON Web Tokens)

**JWT** = Self-contained tokens (innehåller all info i sig själva)

#### JWT-struktur

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFubmEiLCJpYXQiOjE1MTYyMzkwMjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
        │                                │                                                                              │
     HEADER                           PAYLOAD                                                                     SIGNATURE
```

**Dekodat:**

```json
// HEADER
{
  "alg": "HS256",
  "typ": "JWT"
}

// PAYLOAD
{
  "sub": "1234567890",  // Subject (user ID)
  "name": "Anna",
  "email": "anna@example.com",
  "role": "admin",
  "iat": 1516239022,    // Issued at
  "exp": 1516242622     // Expires at
}

// SIGNATURE
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret
)
```

#### Skapa JWT (Node.js)

```javascript
const jwt = require('jsonwebtoken');

const SECRET = process.env.JWT_SECRET;  // Lägg i .env!

// Skapa token (efter lyckad login)
function createToken(user) {
  const payload = {
    sub: user.id,
    email: user.email,
    role: user.role
  };

  const options = {
    expiresIn: '1h'  // Token giltig i 1 timme
  };

  return jwt.sign(payload, SECRET, options);
}

// Login endpoint
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  // Validera credentials
  const user = await User.findByEmail(email);
  if (!user || !await user.verifyPassword(password)) {
    return res.status(401).json({ error: 'Ogiltiga credentials' });
  }

  // Skapa JWT
  const token = createToken(user);

  res.json({
    token,
    user: {
      id: user.id,
      email: user.email,
      name: user.name
    }
  });
});
```

#### Verifiera JWT (middleware)

```javascript
function authenticateToken(req, res, next) {
  // Hämta token från header
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];  // Bearer TOKEN

  if (!token) {
    return res.status(401).json({ error: 'Token saknas' });
  }

  // Verifiera token
  jwt.verify(token, SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Ogiltig token' });
    }

    // Lägg till user i request
    req.user = user;
    next();
  });
}

// Skyddad route
app.get('/profile', authenticateToken, (req, res) => {
  res.json({
    message: 'Detta är din profil',
    user: req.user  // Från JWT
  });
});
```

#### Refresh Tokens

**Problem:** Access tokens är korta (1h), användaren vill inte logga in varje timme.

**Lösning:** Refresh tokens!

```javascript
// Login returnerar både access och refresh token
app.post('/login', async (req, res) => {
  const user = await authenticateUser(req.body);

  const accessToken = createAccessToken(user);   // 15 min
  const refreshToken = createRefreshToken(user); // 7 dagar

  // Spara refresh token i databas
  await saveRefreshToken(user.id, refreshToken);

  res.json({
    accessToken,
    refreshToken
  });
});

// Refresh endpoint
app.post('/refresh', async (req, res) => {
  const { refreshToken } = req.body;

  // Verifiera refresh token
  const payload = jwt.verify(refreshToken, REFRESH_SECRET);

  // Kontrollera om token finns i databas (inte revokerats)
  const isValid = await checkRefreshToken(payload.sub, refreshToken);
  if (!isValid) {
    return res.status(403).json({ error: 'Ogiltig refresh token' });
  }

  // Skapa ny access token
  const newAccessToken = createAccessToken({ id: payload.sub });

  res.json({ accessToken: newAccessToken });
});
```

**Best practices:**
```
Access Token:
- Kort lifetime (15 min - 1 timme)
- Lagras i memory (inte localStorage!)
- Skickas i varje request

Refresh Token:
- Lång lifetime (7-30 dagar)
- Lagras säkert (httpOnly cookie)
- Används endast för att få ny access token
- Kan revokeras
```

---

## 💾 Caching-strategier

### Varför caching?

```
Utan cache:  1000 requests → 1000 database queries (långsamt!)
Med cache:   1000 requests → 10 database queries  (snabbt!)
```

### HTTP Cache Headers

#### Cache-Control

```http
# Cacha i 1 timme (3600 sekunder)
Cache-Control: max-age=3600

# Cacha publikt (kan cachas av CDN)
Cache-Control: public, max-age=3600

# Cacha privat (endast webbläsare)
Cache-Control: private, max-age=3600

# Validera innan användning
Cache-Control: no-cache

# Cacha ALDRIG
Cache-Control: no-store

# Cacha, men måste revalidera efter att det gått ut
Cache-Control: must-revalidate, max-age=3600
```

**Exempel:**
```javascript
// Express
app.get('/products', (req, res) => {
  res.set('Cache-Control', 'public, max-age=3600');
  res.json(products);
});

app.get('/profile', authenticateToken, (req, res) => {
  res.set('Cache-Control', 'private, max-age=300');
  res.json(req.user.profile);
});
```

#### ETag (Entity Tag)

**Conditional requests:**

```
1. Första requesten:
   GET /users/123
   →
   HTTP/1.1 200 OK
   ETag: "33a64df551425fcc55e4d42a148795d9"
   {"id": 123, "name": "Anna"}

2. Nästa request (med If-None-Match):
   GET /users/123
   If-None-Match: "33a64df551425fcc55e4d42a148795d9"
   →
   HTTP/1.1 304 Not Modified
   (ingen body, använd cachad version!)

3. Om data har ändrats:
   GET /users/123
   If-None-Match: "33a64df551425fcc55e4d42a148795d9"
   →
   HTTP/1.1 200 OK
   ETag: "NEW_ETAG_HERE"
   {"id": 123, "name": "Anna Svensson"}
```

**Implementation:**
```javascript
const crypto = require('crypto');

app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);

  // Generera ETag från data
  const etag = crypto.createHash('md5').update(JSON.stringify(user)).digest('hex');

  // Kontrollera If-None-Match header
  if (req.headers['if-none-match'] === etag) {
    return res.status(304).end();  // Not Modified
  }

  res.set('ETag', etag);
  res.json(user);
});
```

### Application-level caching (Redis)

**Redis** = In-memory data store (extremt snabb cache)

```javascript
const redis = require('redis');
const client = redis.createClient();

// Middleware för caching
async function cacheMiddleware(req, res, next) {
  const key = `cache:${req.originalUrl}`;

  // Kolla om data finns i cache
  const cached = await client.get(key);
  if (cached) {
    return res.json(JSON.parse(cached));
  }

  // Om inte, fortsätt till route handler
  // Men override res.json för att cacha resultatet
  const originalJson = res.json.bind(res);
  res.json = (data) => {
    client.setEx(key, 3600, JSON.stringify(data));  // Cache i 1h
    originalJson(data);
  };

  next();
}

// Använd caching
app.get('/users', cacheMiddleware, async (req, res) => {
  const users = await User.findAll();  // Databas-query
  res.json(users);
});
```

### CDN (Content Delivery Network)

```
Användare i Stockholm → Stockholm CDN → Instant!
Användare i Tokyo     → Tokyo CDN     → Instant!

Istället för:
Användare i Tokyo → Stockholm Server → Långsamt!
```

**Setup:**
```javascript
// Använd CloudFlare, Cloudinary, AWS CloudFront

// Lägg till Cache-Control headers
app.use('/static', express.static('public', {
  maxAge: '1y',  // Cacha statiska filer i 1 år
  immutable: true
}));
```

---

## 🎨 API Design Patterns

### 1. HATEOAS (Hypermedia)

**"API:et guidar klienten genom länkar"**

```json
{
  "id": 123,
  "name": "Anna",
  "email": "anna@example.com",
  "_links": {
    "self": {"href": "/users/123"},
    "posts": {"href": "/users/123/posts"},
    "friends": {"href": "/users/123/friends"},
    "edit": {"href": "/users/123", "method": "PUT"},
    "delete": {"href": "/users/123", "method": "DELETE"}
  }
}
```

**Fördelar:**
- Klienten behöver inte hårdkoda URL:er
- API:et kan ändras utan att bryta klienter

### 2. Pagination

```javascript
// Cursor-based (rekommenderat för stora dataset)
GET /posts?cursor=abc123&limit=20

{
  "data": [...],
  "pagination": {
    "cursor": "abc123",
    "nextCursor": "def456",
    "hasMore": true
  }
}

// Page-based (enklare, men problem vid samtidiga ändringar)
GET /posts?page=2&limit=20

{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "totalPages": 8
  }
}
```

### 3. Filtering, Sorting, Searching

```
# Filtrering
GET /products?category=electronics&price_min=100&price_max=500

# Sortering
GET /products?sort=price:asc,name:desc

# Sökning
GET /products?q=laptop

# Kombinera
GET /products?category=electronics&sort=price:asc&limit=20
```

### 4. Partial responses (Field selection)

```
# Hämta endast specifika fält
GET /users?fields=id,name,email

{
  "id": 123,
  "name": "Anna",
  "email": "anna@example.com"
}
```

---

## 🏗️ Mikroservices och API Gateway

### Monolith vs Mikroservices

**Monolith:**
```
┌─────────────────────────────────┐
│       EN STOR APPLIKATION       │
│                                 │
│  Users │ Products │ Orders      │
│  Auth  │ Payment  │ Shipping    │
│                                 │
│       EN DATABAS                │
└─────────────────────────────────┘
```

**Mikroservices:**
```
┌──────────┐  ┌──────────┐  ┌──────────┐
│  Users   │  │ Products │  │  Orders  │
│  Service │  │ Service  │  │ Service  │
│   ↕      │  │    ↕     │  │    ↕     │
│   DB     │  │   DB     │  │   DB     │
└──────────┘  └──────────┘  └──────────┘
      ↑              ↑             ↑
      └──────────────┼─────────────┘
                     │
              ┌─────────────┐
              │ API Gateway │
              └─────────────┘
                     ↑
                  Klient
```

### API Gateway

**Vad är en API Gateway?**
- En "front door" för alla mikroservices
- Routing
- Authentication
- Rate limiting
- Caching
- Request/response transformation

**Exempel (AWS API Gateway, Kong, KrakenD):**

```
Klient → API Gateway → Rätt microservice

GET /users/123
→ API Gateway
  ├─ Autentisering
  ├─ Rate limiting
  ├─ Routing: Skicka till User Service
  └─ Returnera svar
```

**Implementation (Node.js):**
```javascript
// API Gateway (Express)
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Routing till olika services
app.use('/users', createProxyMiddleware({
  target: 'http://user-service:3001',
  changeOrigin: true
}));

app.use('/products', createProxyMiddleware({
  target: 'http://product-service:3002',
  changeOrigin: true
}));

app.use('/orders', createProxyMiddleware({
  target: 'http://order-service:3003',
  changeOrigin: true
}));

app.listen(3000);
```

---

## ⚡ WebSockets och Realtidskommunikation

### HTTP vs WebSocket

**HTTP (request-response):**
```
Klient → Request → Server
Klient ← Response ← Server
(Kopplingen stängs)

För realtidsdata: Måste polla varje sekund (ineffektivt!)
```

**WebSocket (persistent connection):**
```
Klient ←────────→ Server
   (Kopplingen stannar öppen)

Server kan pusha data när som helst!
```

### WebSocket-exempel (Socket.io)

**Server (Node.js):**
```javascript
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// När en klient ansluter
io.on('connection', (socket) => {
  console.log('Klient ansluten:', socket.id);

  // Lyssna på meddelanden från klient
  socket.on('message', (data) => {
    console.log('Mottaget:', data);

    // Skicka till alla klienter (broadcast)
    io.emit('message', data);
  });

  // När klient kopplar från
  socket.on('disconnect', () => {
    console.log('Klient frånkopplad:', socket.id);
  });
});

server.listen(3000);
```

**Klient (JavaScript):**
```javascript
const socket = io('http://localhost:3000');

// Lyssna på meddelanden från server
socket.on('message', (data) => {
  console.log('Nytt meddelande:', data);
  displayMessage(data);
});

// Skicka meddelande till server
function sendMessage(text) {
  socket.emit('message', {
    user: 'Anna',
    text: text,
    timestamp: new Date()
  });
}
```

### Server-Sent Events (SSE)

**Enklare alternativ till WebSocket** (endast server → klient)

```javascript
// Server
app.get('/events', (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');
  res.setHeader('Cache-Control', 'no-cache');
  res.setHeader('Connection', 'keep-alive');

  // Skicka event varje sekund
  const interval = setInterval(() => {
    res.write(`data: ${JSON.stringify({ time: new Date() })}\n\n`);
  }, 1000);

  // När klient kopplar från
  req.on('close', () => {
    clearInterval(interval);
  });
});

// Klient
const eventSource = new EventSource('/events');
eventSource.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Ny data:', data);
};
```

---

## 🎯 Sammanfattning Nivå 4

### Vad du har lärt dig

✅ **GraphQL vs REST** - Förstå skillnaderna och när man använder vad
✅ **API-versionering** - URL, header, deprecation-strategier
✅ **Autentisering/Auktorisering** - JWT, OAuth 2.0, RBAC
✅ **Caching** - HTTP cache, Redis, CDN
✅ **Design patterns** - HATEOAS, pagination, filtering
✅ **Mikroservices** - API Gateway, service architecture
✅ **WebSockets** - Real-time kommunikation

### Checklista

- [ ] Jag kan implementera ett GraphQL API
- [ ] Jag förstår olika versionerings-strategier
- [ ] Jag kan implementera JWT-autentisering
- [ ] Jag kan sätta upp OAuth 2.0
- [ ] Jag förstår caching-strategier (HTTP, Redis)
- [ ] Jag kan designa ett API med best practices
- [ ] Jag förstår mikroservices-arkitektur
- [ ] Jag kan implementera WebSocket-kommunikation

---

## ➡️ Nästa steg

**[Nivå 5: Cutting-Edge (2023-2025) →](./nivå-5-cutting-edge.md)**

I Nivå 5 lär du dig:
- Serverless API:er (AWS Lambda, Azure Functions)
- AI-integrerade API:er (OpenAI, Claude)
- Zero Trust för API:er
- gRPC och Protocol Buffers
- API:er i Web3 och edge computing

---

[🏠 Tillbaka till huvudindex](./README.md) | [⬅️ Nivå 3](./nivå-3-tekniska-detaljer.md) | [➡️ Nivå 5](./nivå-5-cutting-edge.md)
