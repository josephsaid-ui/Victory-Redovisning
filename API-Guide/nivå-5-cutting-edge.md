# 🌟 Nivå 5: Cutting-Edge API-tekniker (2023-2025)

> **För experter och arkitekter**
>
> **Tidsåtgång**: 8-10 timmar + Projekt 2
>
> **Förkunskaper**: Nivå 1-4 eller omfattande erfarenhet av API-utveckling

---

## 📚 Innehåll

1. [Serverless API:er](#serverless-apier)
2. [AI-integrerade API:er](#ai-integrerade-apier)
3. [Zero Trust för API:er](#zero-trust-för-apier)
4. [gRPC och Protocol Buffers](#grpc-och-protocol-buffers)
5. [API:er i Web3 och Blockchain](#apier-i-web3-och-blockchain)
6. [Edge Computing och Distributed API:er](#edge-computing-och-distributed-apier)
7. [AsyncAPI och Event-driven Architecture](#asyncapi-och-event-driven-architecture)
8. [API Observability och Monitoring](#api-observability-och-monitoring)
9. [Verkliga case studies](#verkliga-case-studies)

---

## ☁️ Serverless API:er

### Vad är Serverless?

**Serverless** = Du kör kod utan att hantera servrar (molnleverantören gör det)

```
Traditionellt:
- Du provisionar servrar
- Du betalar 24/7
- Du hanterar skalning
- Du uppdaterar OS

Serverless:
- Kod körs på begäran
- Betala per anrop (millisekunder)
- Automatisk skalning (0 → miljoner requests)
- Ingen serverhantering
```

### AWS Lambda + API Gateway

**Arkitektur:**
```
Internet → API Gateway → Lambda Function → DynamoDB/RDS
                ↓
          Autentisering, rate limiting, caching
```

**Exempel: Skapa ett API med AWS Lambda**

```javascript
// lambda-handler.js
exports.handler = async (event) => {
  // Parse request
  const { httpMethod, path, body } = event;

  // GET /users
  if (httpMethod === 'GET' && path === '/users') {
    const users = await getUsers();  // Hämta från DynamoDB

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify(users)
    };
  }

  // POST /users
  if (httpMethod === 'POST' && path === '/users') {
    const user = JSON.parse(body);
    const newUser = await createUser(user);

    return {
      statusCode: 201,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newUser)
    };
  }

  // 404
  return {
    statusCode: 404,
    body: JSON.stringify({ error: 'Not found' })
  };
};

// DynamoDB operations
const AWS = require('aws-sdk');
const dynamoDB = new AWS.DynamoDB.DocumentClient();

async function getUsers() {
  const params = {
    TableName: 'Users'
  };

  const result = await dynamoDB.scan(params).promise();
  return result.Items;
}

async function createUser(user) {
  const params = {
    TableName: 'Users',
    Item: {
      id: AWS.util.uuid.v4(),
      ...user,
      createdAt: new Date().toISOString()
    }
  };

  await dynamoDB.put(params).promise();
  return params.Item;
}
```

**Deployment (Serverless Framework):**

```yaml
# serverless.yml
service: user-api

provider:
  name: aws
  runtime: nodejs18.x
  region: eu-north-1
  environment:
    USERS_TABLE: ${self:service}-users-${opt:stage, 'dev'}

functions:
  api:
    handler: lambda-handler.handler
    events:
      - http:
          path: /{proxy+}
          method: ANY
          cors: true

resources:
  Resources:
    UsersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: ${self:provider.environment.USERS_TABLE}
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
        BillingMode: PAY_PER_REQUEST
```

**Deploy:**
```bash
npm install -g serverless
serverless deploy
```

### Azure Functions

```javascript
// index.js (Azure Function)
module.exports = async function (context, req) {
  context.log('JavaScript HTTP trigger function processed a request.');

  if (req.method === 'GET') {
    const users = await getUsers();
    context.res = {
      status: 200,
      body: users,
      headers: { 'Content-Type': 'application/json' }
    };
  }

  if (req.method === 'POST') {
    const user = req.body;
    const newUser = await createUser(user);
    context.res = {
      status: 201,
      body: newUser
    };
  }
};
```

### Fördelar och nackdelar med Serverless

| Fördelar | Nackdelar |
|----------|-----------|
| ✅ Ingen serverhantering | ❌ Cold starts (latens vid första anrop) |
| ✅ Automatisk skalning | ❌ Vendor lock-in |
| ✅ Betala per användning | ❌ Begränsad execution time (15 min AWS) |
| ✅ Hög tillgänglighet | ❌ Debugging svårare |
| ✅ Snabb utveckling | ❌ Stateless (behöver extern storage) |

**När använda Serverless:**
- ✅ Sporadisk trafik
- ✅ Event-driven workloads
- ✅ Mikrotjänster
- ✅ Prototyper och MVPs

**När INTE använda:**
- ❌ Konstant hög trafik (traditionella servrar billigare)
- ❌ Behöver låg latens (cold starts)
- ❌ Långvariga processer (>15 min)

---

## 🤖 AI-integrerade API:er

### OpenAI API (GPT-4, ChatGPT)

**Bygg AI-funktionalitet i ditt API:**

```javascript
// Node.js exempel
const OpenAI = require('openai');
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// API endpoint för AI-chatbot
app.post('/api/chat', async (req, res) => {
  const { message, conversationHistory } = req.body;

  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "Du är en hjälpsam kundtjänstassistent för ett e-handelsföretag."
        },
        ...conversationHistory,
        {
          role: "user",
          content: message
        }
      ],
      temperature: 0.7,
      max_tokens: 500
    });

    const reply = completion.choices[0].message.content;

    res.json({
      reply,
      model: completion.model,
      usage: completion.usage
    });

  } catch (error) {
    res.status(500).json({
      error: 'AI request failed',
      details: error.message
    });
  }
});
```

**Använd i frontend:**
```javascript
// React exempel
async function sendMessage(message) {
  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message,
      conversationHistory: chatHistory
    })
  });

  const data = await response.json();
  return data.reply;
}
```

### Anthropic Claude API

```python
# Python exempel
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

@app.route('/api/analyze-text', methods=['POST'])
def analyze_text():
    text = request.json['text']

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Analysera följande text och ge en sammanfattning samt sentiment: {text}"
            }
        ]
    )

    return jsonify({
        'analysis': message.content[0].text,
        'model': message.model,
        'tokens': message.usage
    })
```

### Bildgenerering med DALL-E / Stable Diffusion

```javascript
// Generera bild från text
app.post('/api/generate-image', async (req, res) => {
  const { prompt } = req.body;

  const response = await openai.images.generate({
    model: "dall-e-3",
    prompt: prompt,
    n: 1,
    size: "1024x1024",
    quality: "hd"
  });

  res.json({
    imageUrl: response.data[0].url
  });
});
```

### Best Practices för AI API:er

```javascript
// 1. Implementera retry-logik (AI API:er kan vara instabila)
async function callAIWithRetry(prompt, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await openai.chat.completions.create({...});
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await sleep(2 ** i * 1000);  // Exponential backoff
    }
  }
}

// 2. Cachea resultat (AI-anrop är dyra!)
const cache = new Map();

app.post('/api/ai', async (req, res) => {
  const cacheKey = JSON.stringify(req.body);

  if (cache.has(cacheKey)) {
    return res.json({ ...cache.get(cacheKey), cached: true });
  }

  const result = await callAI(req.body);
  cache.set(cacheKey, result);

  res.json(result);
});

// 3. Rate limiting (undvik höga kostnader)
const aiLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 10,  // Max 10 AI-requests per minut
  message: 'För många AI-requests'
});

app.use('/api/ai', aiLimiter);

// 4. Content moderation (filtrera olämpligt innehåll)
async function moderateContent(text) {
  const moderation = await openai.moderations.create({
    input: text
  });

  if (moderation.results[0].flagged) {
    throw new Error('Content flagged as inappropriate');
  }
}
```

---

## 🔐 Zero Trust för API:er

### Vad är Zero Trust?

**Traditionell säkerhet:**
```
Utifrån (internet) → Firewall → Inuti (trusted) ✅
```

**Zero Trust:**
```
"Trust no one, verify everything"
- Verifiera VARJE request
- Minsta privilegium (least privilege)
- Anta att nätverk är fientligt
```

### Implementera Zero Trust

#### 1. mTLS (Mutual TLS)

**Både klient och server verifierar varandra:**

```
Traditionell TLS:
Klient → Verifierar servern ✅
Server → Litar på klient ❌

mTLS:
Klient → Verifierar servern ✅
Server → Verifierar klient ✅ (via klientcertifikat)
```

**Node.js exempel:**
```javascript
const https = require('https');
const fs = require('fs');

const options = {
  key: fs.readFileSync('server-key.pem'),
  cert: fs.readFileSync('server-cert.pem'),
  ca: fs.readFileSync('ca-cert.pem'),
  requestCert: true,         // Begär klientcertifikat
  rejectUnauthorized: true   // Avvisa ogiltiga certifikat
};

https.createServer(options, (req, res) => {
  // Klienten är verifierad via mTLS
  const clientCert = req.socket.getPeerCertificate();
  console.log('Client CN:', clientCert.subject.CN);

  res.writeHead(200);
  res.end('Authenticated via mTLS');
}).listen(443);
```

#### 2. API Gateway med Identity Verification

```
Request → API Gateway
            ├─ Verifiera JWT
            ├─ Kontrollera IP whitelist
            ├─ Rate limiting
            ├─ Validate request schema
            └─ Forward till backend (om OK)
```

#### 3. Service Mesh (Istio, Linkerd)

**Automatisk mTLS mellan alla mikrotjänster:**

```yaml
# Istio policy
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT  # Kräv mTLS för all trafik
```

#### 4. Continuous Verification

```javascript
// Verifiera vid VARJE request, inte bara login
function verifyEveryRequest(req, res, next) {
  // 1. Verifiera JWT
  const token = verifyJWT(req.headers.authorization);

  // 2. Kontrollera att token inte är revokerad
  if (await isTokenRevoked(token.jti)) {
    return res.status(401).json({ error: 'Token revoked' });
  }

  // 3. Kontrollera IP (flagga om IP ändras)
  if (token.ip !== req.ip) {
    await logSuspiciousActivity(token, req);
  }

  // 4. Kontrollera rättigheter för DENNA resurs
  if (!await hasPermission(token.sub, req.method, req.path)) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  next();
}
```

---

## ⚡ gRPC och Protocol Buffers

### Vad är gRPC?

**gRPC** = Google Remote Procedure Call
- Modern RPC-framework (Google, 2015)
- Använder HTTP/2
- Protocol Buffers (istället för JSON)
- 10x snabbare än REST

**Jämförelse:**

| | REST | gRPC |
|---|------|------|
| **Format** | JSON (text) | Protocol Buffers (binärt) |
| **Protokoll** | HTTP/1.1 | HTTP/2 |
| **Streaming** | Svårt | Inbyggt |
| **Hastighet** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Storlek** | Större | Mindre (50-70%) |
| **Browser support** | ✅ Native | ⚠️ Kräver proxy |

### Protocol Buffers

**Definition (`.proto`-fil):**

```protobuf
// user.proto
syntax = "proto3";

package user;

// Service definition
service UserService {
  rpc GetUser (GetUserRequest) returns (User);
  rpc ListUsers (ListUsersRequest) returns (stream User);
  rpc CreateUser (CreateUserRequest) returns (User);
}

// Messages
message User {
  int32 id = 1;
  string name = 2;
  string email = 3;
  int32 age = 4;
  repeated string interests = 5;
}

message GetUserRequest {
  int32 id = 1;
}

message ListUsersRequest {
  int32 page = 1;
  int32 limit = 2;
}

message CreateUserRequest {
  string name = 1;
  string email = 2;
  int32 age = 3;
}
```

### gRPC Server (Node.js)

```javascript
const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Ladda .proto-fil
const packageDefinition = protoLoader.loadSync('user.proto');
const userProto = grpc.loadPackageDefinition(packageDefinition).user;

// Implementera service
const userService = {
  GetUser: (call, callback) => {
    const userId = call.request.id;

    // Hämta från databas
    const user = {
      id: userId,
      name: 'Anna',
      email: 'anna@example.com',
      age: 28,
      interests: ['fotboll', 'matlagning']
    };

    callback(null, user);
  },

  ListUsers: (call) => {
    // Server streaming - skicka flera users
    const users = getUsers();  // Från databas

    users.forEach(user => {
      call.write(user);
    });

    call.end();
  },

  CreateUser: (call, callback) => {
    const newUser = call.request;

    // Spara i databas
    const savedUser = saveUser(newUser);

    callback(null, savedUser);
  }
};

// Starta server
const server = new grpc.Server();
server.addService(userProto.UserService.service, userService);
server.bindAsync(
  '0.0.0.0:50051',
  grpc.ServerCredentials.createInsecure(),
  () => {
    server.start();
    console.log('gRPC server running on port 50051');
  }
);
```

### gRPC Client

```javascript
const client = new userProto.UserService(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

// Unary call
client.GetUser({ id: 123 }, (error, user) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('User:', user);
});

// Server streaming
const call = client.ListUsers({ page: 1, limit: 10 });

call.on('data', (user) => {
  console.log('Received user:', user);
});

call.on('end', () => {
  console.log('Stream ended');
});

call.on('error', (error) => {
  console.error('Stream error:', error);
});
```

### gRPC Streaming-typer

```
1. Unary (som REST)
   Client → Request → Server
   Client ← Response ← Server

2. Server streaming
   Client → Request → Server
   Client ← Response 1 ← Server
   Client ← Response 2 ← Server
   Client ← Response 3 ← Server

3. Client streaming
   Client → Request 1 → Server
   Client → Request 2 → Server
   Client → Request 3 → Server
   Client ← Response ← Server

4. Bidirectional streaming
   Client ↔ Server (realtid, chat)
```

---

## 🔗 API:er i Web3 och Blockchain

### Blockchain API:er

**Interagera med blockchain:**

```javascript
// Ethereum (web3.js)
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_API_KEY');

// API endpoint för att hämta wallet balance
app.get('/api/wallet/:address/balance', async (req, res) => {
  const address = req.params.address;

  // Hämta balance från Ethereum blockchain
  const balanceWei = await web3.eth.getBalance(address);
  const balanceEth = web3.utils.fromWei(balanceWei, 'ether');

  res.json({
    address,
    balance: balanceEth,
    unit: 'ETH'
  });
});

// Hämta transaction history
app.get('/api/wallet/:address/transactions', async (req, res) => {
  const address = req.params.address;

  // Använd Etherscan API
  const etherscanResponse = await fetch(
    `https://api.etherscan.io/api?module=account&action=txlist&address=${address}&apikey=YOUR_API_KEY`
  );

  const data = await etherscanResponse.json();

  res.json({
    address,
    transactions: data.result
  });
});
```

### Smart Contract API:er

```javascript
// Interagera med smart contract
const contractABI = [...];  // Contract ABI
const contractAddress = '0x...';
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Läs från contract (gratis)
app.get('/api/nft/:tokenId', async (req, res) => {
  const tokenId = req.params.tokenId;

  const owner = await contract.methods.ownerOf(tokenId).call();
  const tokenURI = await contract.methods.tokenURI(tokenId).call();

  res.json({
    tokenId,
    owner,
    tokenURI
  });
});

// Skriv till contract (kostar gas)
app.post('/api/nft/mint', async (req, res) => {
  const { to, tokenURI } = req.body;

  const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);

  const tx = contract.methods.mint(to, tokenURI);
  const gas = await tx.estimateGas({ from: account.address });

  const signedTx = await account.signTransaction({
    to: contractAddress,
    data: tx.encodeABI(),
    gas
  });

  const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

  res.json({
    transactionHash: receipt.transactionHash,
    tokenId: receipt.events.Transfer.returnValues.tokenId
  });
});
```

### IPFS API (Decentralized Storage)

```javascript
const { create } = require('ipfs-http-client');
const ipfs = create({ url: 'https://ipfs.infura.io:5001' });

// Upload fil till IPFS
app.post('/api/ipfs/upload', async (req, res) => {
  const file = req.files.file;

  const result = await ipfs.add(file.data);

  res.json({
    cid: result.cid.toString(),
    url: `https://ipfs.io/ipfs/${result.cid}`
  });
});

// Hämta från IPFS
app.get('/api/ipfs/:cid', async (req, res) => {
  const cid = req.params.cid;

  const stream = ipfs.cat(cid);
  const chunks = [];

  for await (const chunk of stream) {
    chunks.push(chunk);
  }

  const data = Buffer.concat(chunks);
  res.send(data);
});
```

---

## 🌐 Edge Computing och Distributed API:er

### Vad är Edge Computing?

**Traditionell Cloud:**
```
Användare (Stockholm) → Server (USA) → 200ms latens
```

**Edge:**
```
Användare (Stockholm) → Edge Server (Stockholm) → 10ms latens
```

### Cloudflare Workers (Edge Functions)

```javascript
// Kör JavaScript på Cloudflare's edge (200+ platser globalt)
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url = new URL(request.url);

  // API på edge
  if (url.pathname === '/api/hello') {
    return new Response(
      JSON.stringify({
        message: 'Hello from the edge!',
        location: request.cf.city,  // Användarens stad
        country: request.cf.country
      }),
      {
        headers: { 'Content-Type': 'application/json' }
      }
    );
  }

  // Cacha på edge
  if (url.pathname.startsWith('/api/data')) {
    const cache = caches.default;
    let response = await cache.match(request);

    if (!response) {
      response = await fetch('https://origin-server.com/api/data');
      // Cacha i 1 timme
      response = new Response(response.body, response);
      response.headers.set('Cache-Control', 'max-age=3600');
      await cache.put(request, response.clone());
    }

    return response;
  }

  return new Response('Not found', { status: 404 });
}
```

### Deno Deploy (Edge Runtime)

```typescript
// API på edge med Deno
import { serve } from "https://deno.land/std@0.200.0/http/server.ts";

serve(async (req) => {
  const url = new URL(req.url);

  if (url.pathname === "/api/users") {
    // Kör på edge, nära användaren
    const users = await fetchUsers();

    return new Response(JSON.stringify(users), {
      headers: { "content-type": "application/json" }
    });
  }

  return new Response("Not found", { status: 404 });
});
```

---

## 📡 AsyncAPI och Event-driven Architecture

### AsyncAPI (som OpenAPI, men för events)

```yaml
# asyncapi.yml
asyncapi: 3.0.0
info:
  title: Order Events API
  version: 1.0.0

channels:
  order.created:
    address: orders/created
    messages:
      OrderCreated:
        payload:
          type: object
          properties:
            orderId:
              type: string
            userId:
              type: string
            items:
              type: array
            total:
              type: number

  order.shipped:
    address: orders/shipped
    messages:
      OrderShipped:
        payload:
          type: object
          properties:
            orderId:
              type: string
            trackingNumber:
              type: string

operations:
  publishOrderCreated:
    action: send
    channel:
      $ref: '#/channels/order.created'

  subscribeOrderShipped:
    action: receive
    channel:
      $ref: '#/channels/order.shipped'
```

### Event-driven med Webhooks

```javascript
// Registrera webhook
app.post('/api/webhooks', async (req, res) => {
  const { url, events } = req.body;

  // Spara webhook
  await db.webhooks.create({
    url,
    events,  // ['order.created', 'order.shipped']
    secret: generateSecret()
  });

  res.json({ message: 'Webhook registered' });
});

// När event inträffar, skicka till alla registrerade webhooks
async function publishEvent(eventType, data) {
  const webhooks = await db.webhooks.findByEvent(eventType);

  for (const webhook of webhooks) {
    // Skicka POST till webhook URL
    const signature = generateSignature(data, webhook.secret);

    await fetch(webhook.url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Webhook-Signature': signature
      },
      body: JSON.stringify({
        event: eventType,
        data,
        timestamp: new Date().toISOString()
      })
    });
  }
}

// Användning
await publishEvent('order.created', {
  orderId: '123',
  userId: '456',
  total: 599
});
```

---

## 📊 API Observability och Monitoring

### OpenTelemetry (Standard för observability)

```javascript
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

const sdk = new NodeSDK({
  tracing: {
    exporter: new ConsoleSpanExporter()
  },
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();

// Dina API:er instrumenteras automatiskt!
app.get('/api/users', async (req, res) => {
  // OpenTelemetry trackar automatiskt:
  // - Request duration
  // - Database queries
  // - External API calls
  const users = await db.users.findAll();
  res.json(users);
});
```

### Custom metrics med Prometheus

```javascript
const client = require('prom-client');

// Skapa metrics
const httpRequestDuration = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code']
});

const apiCallsTotal = new client.Counter({
  name: 'api_calls_total',
  help: 'Total number of API calls',
  labelNames: ['endpoint']
});

// Middleware för att mäta requests
app.use((req, res, next) => {
  const start = Date.now();

  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;

    httpRequestDuration
      .labels(req.method, req.route?.path || req.path, res.statusCode)
      .observe(duration);

    apiCallsTotal.labels(req.path).inc();
  });

  next();
});

// Metrics endpoint
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', client.register.contentType);
  res.end(await client.register.metrics());
});
```

---

## 🏆 Verkliga Case Studies

### Case Study 1: Stripe API

**Vad gör Stripe bra:**

1. **Utmärkt dokumentation** - Interaktiva exempel, code snippets i 7+ språk
2. **Versioner** - Tydlig versionering, inga breaking changes
3. **Webhooks** - Real-time notifikationer för events
4. **Idempotency keys** - Säkra retries
5. **Test mode** - Komplett testmiljö med test-nycklar

**Idempotency-exempel:**
```javascript
// Klient skickar samma idempotency key vid retry
fetch('https://api.stripe.com/v1/charges', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk_test_...',
    'Idempotency-Key': 'unique-key-123'  // Vid retry: samma resultat!
  },
  body: 'amount=2000&currency=sek'
});
```

### Case Study 2: Twitter/X API Evolution

**Problem:** Breaking changes bröt tusentals appar

**Lösning:**
- Tydlig deprecation-tidsplan (6-12 månader)
- Flera API-versioner parallellt (v1.1, v2)
- Developer support och migration guides

### Case Study 3: Netflix API (Stängdes 2014)

**Varför det misslyckades:**
- För komplext (hundratals endpoints)
- Svårt att versionera
- Hög underhållskostnad

**Lärdomar:**
- Håll API:er enkla
- Tänk på långsiktig underhållbarhet
- Lyssna på utvecklare

---

## 🎯 Sammanfattning Nivå 5

### Vad du har lärt dig

✅ **Serverless** - AWS Lambda, Azure Functions, kostnadseffektiva API:er
✅ **AI-integration** - OpenAI, Claude, bildgenerering
✅ **Zero Trust** - mTLS, continuous verification
✅ **gRPC** - Protocol Buffers, streaming, prestanda
✅ **Web3** - Blockchain API:er, smart contracts, IPFS
✅ **Edge Computing** - Cloudflare Workers, Deno Deploy
✅ **AsyncAPI** - Event-driven, webhooks
✅ **Observability** - OpenTelemetry, Prometheus, monitoring
✅ **Case studies** - Lär från Stripe, Twitter, Netflix

### Checklista

- [ ] Jag kan deploya ett serverless API
- [ ] Jag kan integrera AI i mitt API
- [ ] Jag förstår Zero Trust-principer
- [ ] Jag kan bygga ett gRPC API
- [ ] Jag kan interagera med blockchain
- [ ] Jag kan deploya API:er på edge
- [ ] Jag kan designa event-driven arkitektur
- [ ] Jag har implementerat monitoring och observability

---

## 🚀 Projekt 2: Säker GraphQL-API för e-handel

**Se detaljerad projektbeskrivning i:** [projekt.md → Projekt 2](./projekt.md#projekt-2-graphql-ecommerce)

---

## 📚 Fortsatt lärande

Du har nu en solid grund i API:er från grunderna till cutting-edge! Fortsätt lära:

1. **Praktisera** - Bygg egna projekt
2. **Läs dokumentation** - Stripe, AWS, Google Cloud
3. **Följ communities** - Reddit r/webdev, Dev.to, Twitter
4. **Bidra till open source** - GitHub, GitLab
5. **Bygg i produktion** - Ingenting slår verklig erfarenhet!

---

[🏠 Tillbaka till huvudindex](./README.md) | [⬅️ Nivå 4](./nivå-4-avancerat.md) | [📝 Gå till Övningar](./övningar.md)
