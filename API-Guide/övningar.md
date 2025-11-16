# 📝 Övningar: API-utveckling (35+ Praktiska Övningar)

> **Progressiva övningar från grundnivå till expert**
>
> **Tips:** Gör övningarna i ordning. Varje övning bygger på tidigare kunskaper.

---

## 📚 Innehåll

- [Nivå 1: Grundläggande (Övning 1-7)](#nivå-1-grundläggande-övning-1-7)
- [Nivå 2: Tekniska termer (Övning 8-15)](#nivå-2-tekniska-termer-övning-8-15)
- [Nivå 3: Tekniska detaljer (Övning 16-25)](#nivå-3-tekniska-detaljer-övning-16-25)
- [Nivå 4: Avancerade koncept (Övning 26-32)](#nivå-4-avancerade-koncept-övning-26-32)
- [Nivå 5: Cutting-edge (Övning 33-38)](#nivå-5-cutting-edge-övning-33-38)

---

## 🌱 Nivå 1: Grundläggande (Övning 1-7)

### Övning 1: Identifiera API:er i vardagen

**Svårighetsgrad:** ⭐☆☆☆☆

**Mål:** Förstå var API:er används i vardagen

**Uppgift:**
1. Öppna 5 appar på din telefon (t.ex. Instagram, Spotify, Google Maps, väder, bank)
2. För varje app, lista minst 2 API:er som appen troligen använder
3. Förklara VARFÖR appen behöver dessa API:er

**Exempel:**
```
Instagram:
- Google Maps API → För att tagga platser
- Facebook Graph API → För att dela till Facebook
- Payment API (Stripe/PayPal) → För att köpa annonser
```

**Lösning:** [Expandera]
<details>
<summary>Klicka för att visa exempel-lösning</summary>

```
1. Spotify:
   - Music Recognition API (Shazam) → Identifiera låtar
   - Payment API → Premium-prenumerationer
   - Social Media API → Dela låtar

2. Uber:
   - Google Maps API → Kartor och navigation
   - Payment API → Kortbetalningar
   - SMS API (Twilio) → Skicka bekräftelser

3. Väderapp:
   - OpenWeatherMap API → Väderdata
   - Geolocation API → Hitta din position
   - Notification API → Vädervarningar

4. Matbank-app (foodora):
   - Google Maps API → Visa restauranger
   - Payment API → Betalningar
   - Push Notification API → Orderstatus

5. Swedbank-app:
   - BankID API → Identifiering
   - Swish API → Swish-betalningar
   - SMS API → Engångskoder
```
</details>

---

### Övning 2: Läsa JSON

**Svårighetsgrad:** ⭐☆☆☆☆

**Mål:** Förstå JSON-format

**Uppgift:**
Studera följande JSON och svara på frågorna:

```json
{
  "användare": {
    "id": 12345,
    "namn": "Anna Andersson",
    "email": "anna@example.com",
    "ålder": 28,
    "aktiv": true,
    "adress": {
      "gata": "Storgatan 10",
      "stad": "Stockholm",
      "postnummer": "11122"
    },
    "intressen": ["fotboll", "matlagning", "resor"],
    "vänner": 42
  }
}
```

**Frågor:**
1. Vad är användarens email?
2. Hur gammal är användaren?
3. Vilken datatyp är "aktiv"?
4. Hur många intressen har användaren?
5. Vad är användarens postnummer?

<details>
<summary>Lösning</summary>

```
1. anna@example.com
2. 28 år
3. Boolean (true/false)
4. 3 intressen
5. "11122"
```
</details>

---

### Övning 3: Utforska ett publikt API

**Svårighetsgrad:** ⭐⭐☆☆☆

**Mål:** Se ett riktigt API-svar

**Uppgift:**
1. Öppna din webbläsare
2. Gå till: `https://api.github.com/users/github`
3. Studera JSON-svaret

**Frågor:**
- Vad är "login"-värdet?
- Hur många "public_repos" har kontot?
- Vad är "created_at"-datumet?

<details>
<summary>Lösning</summary>

```json
{
  "login": "github",
  "id": 9919,
  "public_repos": 332,
  "created_at": "2008-05-11T04:37:31Z",
  ...
}
```

Du kan också prova:
- `https://api.github.com/users/DIN_GITHUB_USERNAME`
- `https://jsonplaceholder.typicode.com/users/1`
</details>

---

### Övning 4: Matcha analogier

**Svårighetsgrad:** ⭐☆☆☆☆

**Mål:** Koppla API-koncept till verkliga analogier

**Uppgift:**
Matcha rätt analogi till rätt API-koncept:

**Koncept:**
1. API
2. Request
3. Response
4. Endpoint
5. Server

**Analogier:**
A. Köket där maten lagas
B. Serveraren som levererar maten
C. Menyn på restaurangen
D. Din beställning
E. Specifik rätt på menyn

<details>
<summary>Lösning</summary>

```
1. API → C (Menyn)
2. Request → D (Din beställning)
3. Response → B (Serveraren levererar)
4. Endpoint → E (Specifik rätt)
5. Server → A (Köket)
```
</details>

---

### Övning 5: Rita ett API-flöde

**Svårighetsgrad:** ⭐⭐☆☆☆

**Mål:** Visualisera API-kommunikation

**Uppgift:**
Rita ett diagram (på papper eller digitalt) som visar flödet när du:
1. Öppnar en väderapp
2. Appen visar "15°C Soligt i Stockholm"

Inkludera: Klient, API, Server, Databas

<details>
<summary>Exempel-lösning</summary>

```
┌──────────────┐
│ Väderapp     │ 1. Användaren öppnar appen
│ (Klient)     │
└──────┬───────┘
       │
       │ 2. Request: "Ge mig vädret för Stockholm"
       │
       ↓
┌──────────────┐
│ Väder-API    │ 3. API tar emot request
│              │
└──────┬───────┘
       │
       │ 4. API frågar databasen
       │
       ↓
┌──────────────┐
│ Väder-       │ 5. Databas returnerar: 15°C, Soligt
│ databas      │
└──────┬───────┘
       │
       │ 6. API skapar JSON-response
       │
       ↓
┌──────────────┐
│ Väderapp     │ 7. Appen visar: "15°C ☀️ Soligt"
└──────────────┘
```
</details>

---

### Övning 6: API vs ingen API

**Svårighetsgrad:** ⭐⭐☆☆☆

**Mål:** Förstå värdet av API:er

**Uppgift:**
Förklara skillnaden mellan dessa scenarion:

**Scenario A (utan API):**
Du bygger en resebokningsapp. Du måste:
- Bygga egen databas med alla hotell i världen
- Uppdatera priser manuellt varje dag
- Hantera bokningar själv
- Bygga eget betalningssystem

**Scenario B (med API):**
Du bygger en resebokningsapp. Du använder:
- Booking.com API för hotell
- Stripe API för betalningar
- SendGrid API för email-bekräftelser

**Frågor:**
1. Vilket scenario är billigare?
2. Vilket scenario är snabbare att bygga?
3. Vilka risker finns i Scenario A?

<details>
<summary>Lösning</summary>

```
1. Scenario B är MYCKET billigare
   - Ingen egen infrastruktur
   - Betala per användning
   - Delade kostnader

2. Scenario B är snabbare
   - Veckor istället för år
   - Fokusera på din app, inte infrastruktur

3. Risker i Scenario A:
   - Säkerhet (PCI-compliance för betalningar)
   - Datakvalitet (föråldrade priser)
   - Skalbarhet (hantera miljontals hotell)
   - Underhållskostnad
```
</details>

---

### Övning 7: API-terminologi Quiz

**Svårighetsgrad:** ⭐⭐☆☆☆

**Fyll i rätt term:**

1. En ____ är den som begär data (t.ex. en webbläsare)
2. En ____ är den som svarar med data
3. ____ är formatet som används för att skicka data (t.ex. JSON)
4. En ____ är en specifik URL där du kan hämta data
5. ____ betyder att du ber om data
6. ____ betyder att du får data tillbaka

<details>
<summary>Lösning</summary>

```
1. Klient
2. Server
3. JSON (eller XML, men JSON är vanligast)
4. Endpoint
5. Request
6. Response
```
</details>

---

## 🔧 Nivå 2: Tekniska termer (Övning 8-15)

### Övning 8: HTTP-metoder

**Svårighetsgrad:** ⭐⭐☆☆☆

**Mål:** Förstå HTTP-metoder

**Uppgift:**
Matcha rätt HTTP-metod till scenariot:

**Scenarion:**
1. Hämta en lista av produkter
2. Skapa en ny användare
3. Uppdatera en användares email
4. Ta bort ett inlägg
5. Uppdatera endast en användares namn (inte hela objektet)

**Metoder:** GET, POST, PUT, PATCH, DELETE

<details>
<summary>Lösning</summary>

```
1. GET /products
2. POST /users
3. PUT /users/123 (eller PATCH)
4. DELETE /posts/456
5. PATCH /users/123
```
</details>

---

### Övning 9: Statuskoder

**Svårighetsgrad:** ⭐⭐☆☆☆

**Uppgift:**
Vad betyder dessa statuskoder? Fyll i:

| Kod | Betydelse | Vems fel? |
|-----|-----------|-----------|
| 200 | ? | ? |
| 201 | ? | ? |
| 400 | ? | ? |
| 401 | ? | ? |
| 404 | ? | ? |
| 500 | ? | ? |

<details>
<summary>Lösning</summary>

```
200 - OK (allt gick bra) - Ingens fel
201 - Created (resurs skapad) - Ingens fel
400 - Bad Request (felaktig syntax) - Klientens fel
401 - Unauthorized (autentisering krävs) - Klientens fel
404 - Not Found (resursen finns inte) - Klientens fel (fel URL)
500 - Internal Server Error - Serverns fel
```
</details>

---

### Övning 10: Ditt första API-anrop (Postman)

**Svårighetsgrad:** ⭐⭐☆☆☆

**Mål:** Använda Postman för att testa API:er

**Uppgift:**
1. Installera Postman (https://www.postman.com/downloads/)
2. Skapa ett nytt GET-request till: `https://jsonplaceholder.typicode.com/users`
3. Skicka requesten
4. Analysera svaret

**Frågor:**
- Hur många användare returnerades?
- Vad är status-koden?
- Hur lång tid tog requesten?

**Extra:**
- Testa `https://jsonplaceholder.typicode.com/users/1` (en specifik användare)
- Vad händer om du testar `/users/999`?

<details>
<summary>Lösning</summary>

```
/users returnerar:
- 10 användare
- Status: 200 OK
- Tid: ~200-500ms (beroende på nätv erk)

/users/1 returnerar:
- En användare (Leanne Graham)
- Status: 200 OK

/users/999 returnerar:
- Tom object {}
- Status: 200 OK (borde vara 404, men detta är ett mock-API)
```
</details>

---

### Övning 11: Koda ditt första API-anrop (JavaScript)

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Skriva kod för att anropa ett API

**Uppgift:**
Skriv JavaScript-kod som:
1. Hämtar användare från `https://jsonplaceholder.typicode.com/users`
2. Loggar användarnas namn
3. Hittar användaren med emailen som slutar på "@hildegard.org"

```javascript
// Din kod här
async function fetchUsers() {
  // TODO: Hämta användare med fetch()
  // TODO: Logga alla namn
  // TODO: Hitta användare med email som slutar på @hildegard.org
}

fetchUsers();
```

<details>
<summary>Lösning</summary>

```javascript
async function fetchUsers() {
  try {
    // 1. Hämta data
    const response = await fetch('https://jsonplaceholder.typicode.com/users');

    // 2. Kontrollera status
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // 3. Parsea JSON
    const users = await response.json();

    // 4. Logga alla namn
    console.log('Alla användare:');
    users.forEach(user => {
      console.log(user.name);
    });

    // 5. Hitta specifik email
    const hildegardUser = users.find(user =>
      user.email.endsWith('@hildegard.org')
    );

    console.log('\nAnvändare med @hildegard.org:', hildegardUser);

  } catch (error) {
    console.error('Fel vid API-anrop:', error);
  }
}

fetchUsers();
```
</details>

---

### Övning 12: Koda API-anrop (Python)

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Använda Python för API-anrop

**Uppgift:**
Skriv Python-kod som:
1. Hämtar todos från `https://jsonplaceholder.typicode.com/todos`
2. Räknar hur många som är completed
3. Hittar den todo med längst title

```python
import requests

# Din kod här
def fetch_todos():
    # TODO: Implementera
    pass

fetch_todos()
```

<details>
<summary>Lösning</summary>

```python
import requests

def fetch_todos():
    try:
        # 1. Hämta data
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        response.raise_for_status()  # Raise error för bad status

        # 2. Parsea JSON
        todos = response.json()

        # 3. Räkna completed
        completed_count = sum(1 for todo in todos if todo['completed'])
        print(f'Antal completed todos: {completed_count}')

        # 4. Hitta längsta title
        longest_todo = max(todos, key=lambda t: len(t['title']))
        print(f'\nLängsta title ({len(longest_todo["title"])} tecken):')
        print(longest_todo['title'])

        # Extra: Procentandel completed
        total = len(todos)
        percentage = (completed_count / total) * 100
        print(f'\n{percentage:.1f}% av todos är completed')

    except requests.exceptions.RequestException as error:
        print(f'Fel vid API-anrop: {error}')

fetch_todos()
```
</details>

---

### Övning 13: POST-request (Skapa data)

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Skicka data till ett API

**Uppgift (JavaScript):**
Använd `https://jsonplaceholder.typicode.com/posts` för att skapa ett nytt inlägg.

```javascript
async function createPost() {
  const newPost = {
    title: 'Min första post via API',
    body: 'Detta är innehållet',
    userId: 1
  };

  // TODO: Skicka POST-request
  // TODO: Logga svaret
}

createPost();
```

<details>
<summary>Lösning</summary>

```javascript
async function createPost() {
  const newPost = {
    title: 'Min första post via API',
    body: 'Detta är innehållet',
    userId: 1
  };

  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(newPost)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const createdPost = await response.json();
    console.log('Post skapad:', createdPost);
    console.log('Nytt ID:', createdPost.id);

  } catch (error) {
    console.error('Fel:', error);
  }
}

createPost();
```
</details>

---

### Övning 14: Error handling

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Uppgift:**
Förbättra denna kod med korrekt error handling:

```javascript
async function getUser(userId) {
  const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const user = await response.json();
  console.log(user.name);
}

getUser(999);  // Finns inte!
```

**Krav:**
- Kontrollera HTTP-status
- Hantera nätverksfel
- Ge tydliga felmeddelanden

<details>
<summary>Lösning</summary>

```javascript
async function getUser(userId) {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/users/${userId}`
    );

    // Kontrollera HTTP-status
    if (!response.ok) {
      if (response.status === 404) {
        throw new Error(`Användare med ID ${userId} hittades inte`);
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const user = await response.json();

    // Kontrollera att user existerar och har data
    if (!user || !user.name) {
      throw new Error('Ogiltig användardata');
    }

    console.log('Användare hittad:', user.name);
    return user;

  } catch (error) {
    // Hantera olika typer av fel
    if (error instanceof TypeError) {
      console.error('Nätverksfel: Kontrollera din internetanslutning');
    } else {
      console.error('Fel vid hämtning av användare:', error.message);
    }

    return null;
  }
}

// Testa
getUser(1);    // Ska fungera
getUser(999);  // Ska ge felmeddelande
getUser('invalid');  // Ska ge felmeddelande
```
</details>

---

### Övning 15: API-nycklar (OpenWeatherMap)

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Använda ett riktigt API med autentisering

**Uppgift:**
1. Registrera dig på OpenWeatherMap (gratis): https://openweathermap.org/api
2. Få din API-nyckel
3. Hämta vädret för din stad

```javascript
const API_KEY = 'DIN_API_NYCKEL_HÄR';
const STAD = 'Stockholm';

async function getWeather() {
  // TODO: Hämta väderdata
  // URL: https://api.openweathermap.org/data/2.5/weather
  // Parameters: q=STAD, appid=API_KEY, units=metric, lang=sv
}

getWeather();
```

<details>
<summary>Lösning</summary>

```javascript
const API_KEY = 'DIN_API_NYCKEL_HÄR';  // Byt ut!
const STAD = 'Stockholm';

async function getWeather(stad = STAD) {
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${stad}&appid=${API_KEY}&units=metric&lang=sv`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      if (response.status === 401) {
        throw new Error('Ogiltig API-nyckel');
      }
      if (response.status === 404) {
        throw new Error(`Staden "${stad}" hittades inte`);
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Visa väderdata
    console.log(`\n🌍 Väder i ${data.name}, ${data.sys.country}`);
    console.log(`🌡️  Temperatur: ${data.main.temp}°C`);
    console.log(`🤔 Känns som: ${data.main.feels_like}°C`);
    console.log(`☁️  Beskrivning: ${data.weather[0].description}`);
    console.log(`💨 Vind: ${data.wind.speed} m/s`);
    console.log(`💧 Luftfuktighet: ${data.main.humidity}%`);

    return data;

  } catch (error) {
    console.error('Fel:', error.message);
  }
}

// Testa
getWeather('Stockholm');
getWeather('London');
getWeather('Tokyo');
```

**Tips för säkerhet:**
```javascript
// Använd environment variables istället!
// Skapa .env-fil:
// OPENWEATHER_API_KEY=din_nyckel_här

// Läs i Node.js:
require('dotenv').config();
const API_KEY = process.env.OPENWEATHER_API_KEY;
```
</details>

---

## ⚙️ Nivå 3: Tekniska detaljer (Övning 16-25)

### Övning 16: REST-design

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Designa RESTful endpoints

**Uppgift:**
Designa endpoints för en blogg-applikation med:
- Inlägg (posts)
- Kommentarer (comments)
- Användare (users)

Inkludera:
- HTTP-metod
- URL
- Vad det gör

**Exempel:**
```
GET /posts - Hämta alla inlägg
```

Designa minst 10 endpoints.

<details>
<summary>Lösning</summary>

```
POSTS:
GET    /posts              - Lista alla inlägg
GET    /posts/:id          - Hämta specifikt inlägg
POST   /posts              - Skapa nytt inlägg
PUT    /posts/:id          - Uppdatera helt inlägg
PATCH  /posts/:id          - Uppdatera delar av inlägg
DELETE /posts/:id          - Ta bort inlägg

COMMENTS:
GET    /posts/:id/comments     - Hämta kommentarer för ett inlägg
POST   /posts/:id/comments     - Skapa kommentar på inlägg
DELETE /comments/:id            - Ta bort kommentar

USERS:
GET    /users                  - Lista användare
GET    /users/:id              - Hämta användare
POST   /users                  - Skapa användare
GET    /users/:id/posts        - Hämta användarens inlägg

SEARCH/FILTER:
GET    /posts?author=:userId   - Filtrera inlägg per författare
GET    /posts?sort=date&order=desc  - Sortera inlägg
GET    /posts?search=keyword   - Sök inlägg
```

**Bra praxis:**
- Använd plural form (/posts, inte /post)
- Använd substantiv, inte verb (/posts, inte /getPosts)
- Nästlade resurser för relationer (/posts/:id/comments)
</details>

---

### Övning 17: Implementera ett enkelt API (Node.js/Express)

**Svårighetsgrad:** ⭐⭐⭐⭐☆

**Mål:** Bygga ditt första API

**Uppgift:**
Skapa ett enkelt API med Express som hanterar användare.

```bash
npm init -y
npm install express
```

```javascript
const express = require('express');
const app = express();

app.use(express.json());

// In-memory "databas"
let users = [
  { id: 1, name: 'Anna', email: 'anna@example.com' },
  { id: 2, name: 'Erik', email: 'erik@example.com' }
];

// TODO: Implementera endpoints
// GET /users - Lista alla
// GET /users/:id - Hämta en
// POST /users - Skapa ny
// PUT /users/:id - Uppdatera
// DELETE /users/:id - Ta bort

app.listen(3000, () => {
  console.log('API kör på http://localhost:3000');
});
```

<details>
<summary>Lösning</summary>

```javascript
const express = require('express');
const app = express();

app.use(express.json());

let users = [
  { id: 1, name: 'Anna', email: 'anna@example.com' },
  { id: 2, name: 'Erik', email: 'erik@example.com' }
];
let nextId = 3;

// GET /users - Lista alla användare
app.get('/users', (req, res) => {
  res.json(users);
});

// GET /users/:id - Hämta specifik användare
app.get('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const user = users.find(u => u.id === id);

  if (!user) {
    return res.status(404).json({ error: 'Användare inte hittad' });
  }

  res.json(user);
});

// POST /users - Skapa ny användare
app.post('/users', (req, res) => {
  const { name, email } = req.body;

  // Validering
  if (!name || !email) {
    return res.status(400).json({
      error: 'Namn och email krävs'
    });
  }

  if (!email.includes('@')) {
    return res.status(422).json({
      error: 'Ogiltigt email-format'
    });
  }

  const newUser = {
    id: nextId++,
    name,
    email
  };

  users.push(newUser);

  res.status(201).json(newUser);
});

// PUT /users/:id - Uppdatera användare
app.put('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const { name, email } = req.body;

  const index = users.findIndex(u => u.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Användare inte hittad' });
  }

  users[index] = { id, name, email };

  res.json(users[index]);
});

// DELETE /users/:id - Ta bort användare
app.delete('/users/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const index = users.findIndex(u => u.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Användare inte hittad' });
  }

  users.splice(index, 1);

  res.status(204).end();
});

app.listen(3000, () => {
  console.log('API kör på http://localhost:3000');
});
```

**Testa med cURL:**
```bash
# Lista alla
curl http://localhost:3000/users

# Hämta en
curl http://localhost:3000/users/1

# Skapa ny
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Lisa","email":"lisa@example.com"}'

# Uppdatera
curl -X PUT http://localhost:3000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Anna Svensson","email":"anna.svensson@example.com"}'

# Ta bort
curl -X DELETE http://localhost:3000/users/1
```
</details>

---

### Övning 18: CORS

**Svårighetsgrad:** ⭐⭐⭐☆☆

**Mål:** Förstå och fixa CORS-problem

**Uppgift:**
1. Skapa en enkel HTML-sida som anropar ditt API från övning 17
2. Observera CORS-felet i console
3. Fixa det med CORS middleware

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
  <h1>Test API</h1>
  <button onclick="fetchUsers()">Hämta användare</button>
  <div id="result"></div>

  <script>
    async function fetchUsers() {
      const response = await fetch('http://localhost:3000/users');
      const users = await response.json();
      document.getElementById('result').innerHTML = JSON.stringify(users, null, 2);
    }
  </script>
</body>
</html>
```

<details>
<summary>Lösning</summary>

```javascript
// Installera CORS
// npm install cors

const express = require('express');
const cors = require('cors');
const app = express();

// Aktivera CORS för alla origins (development)
app.use(cors());

// Eller specifika origins (production)
app.use(cors({
  origin: ['http://localhost:8080', 'https://minapp.com'],
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

app.use(express.json());

// ... resten av koden
```

**Manuell CORS (utan middleware):**
```javascript
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');

  // Hantera preflight requests
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }

  next();
});
```
</details>

---

### Övning 19: Rate limiting

**Svårighetsgrad:** ⭐⭐⭐⭐☆

**Mål:** Implementera rate limiting

**Uppgift:**
Lägg till rate limiting på ditt API:
- Max 10 requests per minut
- Returnera 429-status när gränsen nås

```bash
npm install express-rate-limit
```

<details>
<summary>Lösning</summary>

```javascript
const rateLimit = require('express-rate-limit');

// Konfigurera rate limiter
const limiter = rateLimit({
  windowMs: 60 * 1000,  // 1 minut
  max: 10,              // Max 10 requests
  message: {
    error: 'För många requests, försök igen om 1 minut'
  },
  standardHeaders: true,  // Returnera RateLimit headers
  legacyHeaders: false,
  handler: (req, res) => {
    res.status(429).json({
      error: 'Rate limit exceeded',
      message: 'Du har gjort för många requests. Försök igen om 1 minut.',
      retryAfter: 60
    });
  }
});

// Applicera på alla routes
app.use(limiter);

// Eller specifika routes
app.use('/api/', limiter);

// Eller olika limits för olika endpoints
const createLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 3  // Max 3 create-requests per minut
});

app.post('/users', createLimiter, (req, res) => {
  // Skapa användare
});
```

**Testa:**
```bash
# Kör detta 15 gånger snabbt
for i in {1..15}; do curl http://localhost:3000/users; echo ""; done
```
</details>

---

### Övning 20: Input validation

**Svårighetsgrad:** ⭐⭐⭐⭐☆

**Mål:** Validera all input från användare

**Uppgift:**
Lägg till robust validering med Joi:

```bash
npm install joi
```

<details>
<summary>Lösning</summary>

```javascript
const Joi = require('joi');

// Definiera schema
const userSchema = Joi.object({
  name: Joi.string()
    .min(2)
    .max(50)
    .required()
    .messages({
      'string.min': 'Namnet måste vara minst 2 tecken',
      'string.max': 'Namnet får max vara 50 tecken',
      'any.required': 'Namn är obligatoriskt'
    }),

  email: Joi.string()
    .email()
    .required()
    .messages({
      'string.email': 'Ogiltigt email-format',
      'any.required': 'Email är obligatoriskt'
    }),

  age: Joi.number()
    .integer()
    .min(18)
    .max(120)
    .optional()
    .messages({
      'number.min': 'Du måste vara minst 18 år',
      'number.max': 'Ogiltigt ålder'
    })
});

// Validation middleware
function validateUser(req, res, next) {
  const { error, value } = userSchema.validate(req.body, {
    abortEarly: false  // Returnera alla fel, inte bara första
  });

  if (error) {
    return res.status(422).json({
      error: 'Validation failed',
      details: error.details.map(err => ({
        field: err.path[0],
        message: err.message
      }))
    });
  }

  // Ersätt req.body med validerad data
  req.body = value;
  next();
}

// Använd i routes
app.post('/users', validateUser, (req, res) => {
  const newUser = {
    id: nextId++,
    ...req.body
  };

  users.push(newUser);
  res.status(201).json(newUser);
});

app.put('/users/:id', validateUser, (req, res) => {
  // Uppdatera användare
});
```

**Testa felfall:**
```bash
# För kort namn
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"A","email":"test@example.com"}'

# Ogiltigt email
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Anna","email":"invalid"}'

# För ung
curl -X POST http://localhost:3000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Anna","email":"anna@example.com","age":15}'
```
</details>

---

### Övning 21-25: Fortsättning

*Av utrymmesskäl, fortsätter övningarna i liknande format med fokus på:*

- **Övning 21:** Testning med Jest/Supertest
- **Övning 22:** Dokumentation med Swagger
- **Övning 23:** Implementera paginering
- **Övning 24:** Filtering och sorting
- **Övning 25:** HTTPS och säkerhet

*(Se fullständiga övningar i online-versionen eller kontakta för komplett PDF)*

---

## 🚀 Nivå 4: Avancerade koncept (Övning 26-32)

### Övning 26: JWT-autentisering

**Svårighetsgrad:** ⭐⭐⭐⭐⭐

**Uppgift:**
Implementera JWT-baserad autentisering:
1. Login endpoint som returnerar JWT
2. Middleware som verifierar JWT
3. Skyddade endpoints

```bash
npm install jsonwebtoken bcrypt
```

<details>
<summary>Lösning finns i fullständig guide</summary>

*Se Nivå 4 i huvudguiden för komplett implementation*
</details>

---

### Övning 27-32: GraphQL, OAuth, Caching, WebSockets, Mikroservices, gRPC

*Dessa avancerade övningar täcks i de fullständiga projekten. Se projekt.md för hands-on implementation.*

---

## 🌟 Nivå 5: Cutting-edge (Övning 33-38)

### Övning 33: Deploy Serverless API (AWS Lambda)

**Svårighetsgrad:** ⭐⭐⭐⭐⭐

**Uppgift:**
Deploya ditt API till AWS Lambda med Serverless Framework

*(Se detaljerad guide i Nivå 5)*

---

### Övning 34-38: AI-integration, Zero Trust, Edge deployment, etc.

*Dessa övningar är integrerade i Projekt 2. Se projekt.md*

---

## ✅ Slutsats

Du har nu 38 progressiva övningar som täcker:
- ✅ Grundläggande API-koncept
- ✅ HTTP, JSON, REST
- ✅ Praktisk kodning (JavaScript, Python)
- ✅ Säkerhet och best practices
- ✅ Avancerade tekniker
- ✅ Modern cloud & AI

**Nästa steg:** [Gör projekten →](./projekt.md)

---

[🏠 Tillbaka till huvudindex](./README.md) | [🚀 Gå till Projekt](./projekt.md)
