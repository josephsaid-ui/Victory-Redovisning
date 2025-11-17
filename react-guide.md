# React - Den Kompletta Guiden: Från Nybörjare till Expert

> En komplett resa genom React-utveckling - från absolut nybörjare till produktionsklar expert

---

## 📚 Innehållsförteckning

- [🎯 Om Denna Guide](#-om-denna-guide)
- [🤔 Vad är React?](#-vad-är-react)
- [Nivå 1: Webb för 5-åringar 👶](#nivå-1-webb-för-5-åringar-)
- [Nivå 2: Grundläggande React 🧒](#nivå-2-grundläggande-react-)
- [Nivå 3: Komponenter & State 🎓](#nivå-3-komponenter--state-)
- [Nivå 4: Avancerade Koncept 🚀](#nivå-4-avancerade-koncept-)
- [Nivå 5: Expert & Produktion 💎](#nivå-5-expert--produktion-)
- [🎓 Slutlig Självutvärdering](#-slutlig-självutvärdering)
- [📖 Ordlista](#-ordlista)
- [🆚 React vs Andra Framework](#-react-vs-andra-framework)
- [🔗 Resurser för Fördjupning](#-resurser-för-fördjupning)
- [❓ Vanliga Frågor (FAQ)](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande React-guiden på svenska! Denna guide är designad för att ta dig från absolut nybörjare till produktionsklar React-utvecklare genom en noggrant strukturerad inlärningsresa.

### Vad gör denna guide unik?

**Progressiv inlärning i 5 nivåer:**
- 🍼 **Nivå 1 (5-åringen)**: Förstå webbsidor och interaktivitet utan kod
- 🧒 **Nivå 2 (10-åringen)**: Dina första React-komponenter
- 🎓 **Nivå 3 (Gymnasiet)**: State, hooks och interaktiva appar
- 🚀 **Nivå 4 (Universitet)**: Avancerade patterns och optimering
- 💎 **Nivå 5 (Expert)**: Produktion, testing och moderna patterns

**Omfattande praktisk träning:**
- 50+ övningar med kompletta lösningar
- 5 fullständiga projekt
- Verkliga kodexempel från produktionsappar
- Best practices från dag 1

**Total läsningstid:** 2-4 timmar (beroende på ditt tempo och förkunskaper)

### Hur du använder denna guide

1. **Börja från början**: Även om du kan programmera, börja på nivå 1-2 för att förstå React-tänket
2. **Gör alla övningar**: Det är skillnad på att läsa och att göra
3. **Bygg projekten**: Praktisk erfarenhet är ovärderlig
4. **Ta pauser**: Varje nivå är 15-25 minuter, perfekt för fokuserade sessioner
5. **Kom tillbaka**: Använd som referens när du kodar

### Förkunskaper

- **Nivå 1-2**: Inga förkunskaper krävs!
- **Nivå 3**: Grundläggande HTML, CSS och JavaScript
- **Nivå 4**: God förståelse för JavaScript (ES6+)
- **Nivå 5**: Erfarenhet av att bygga webbapplikationer

---

## 🤔 Vad är React?

React är ett JavaScript-bibliotek för att bygga användargränssnitt. Men vad betyder det egentligen?

### Enkelt förklarat

**Traditionell webbsida:**
```
Du klickar på en knapp →
Hela sidan laddas om →
Du ser resultatet
```

**Med React:**
```
Du klickar på en knapp →
Bara den delen som ändras uppdateras →
Superbbt snabbt!
```

### Varför React?

**Problemen med vanilla JavaScript:**
- ❌ Mycket kod för att uppdatera UI
- ❌ Svårt att hålla ordning när appen växer
- ❌ Buggar när UI och data är ur synk
- ❌ Repetitiv kod

**Lösningen - React:**
- ✅ **Komponentbaserat**: Bygg UI som LEGO-bitar
- ✅ **Deklarativt**: Beskriv HUR det ska se ut, inte steg-för-steg
- ✅ **Effektivt**: Bara uppdaterar vad som behövs
- ✅ **Återanvändbart**: Skriv en gång, använd överallt
- ✅ **Stort ekosystem**: Tusentals färdiga lösningar

### React i siffror (2024)

- **225,000+** GitHub stars
- **18M+** nedladdningar per vecka
- Används av: Facebook, Instagram, Netflix, Airbnb, Uber, Discord, och tusentals fler
- **Största** UI-biblioteket i världen

### Vem använder React?

- **Stora företag**: Meta (Facebook), Netflix, Tesla, Shopify
- **Startups**: De flesta moderna web-startups
- **Open source**: Nästan alla moderna webb-projekt
- **Du snart!** Efter denna guide

---

Nu när du förstår *vad* React är, låt oss börja lära oss *hur*!

---

## Nivå 1: Webb för 5-åringar 👶

**Läsningstid:** ~10 minuter
**Förkunskaper:** Inga!

### Introduktion

Innan vi dyker in i React, ska vi förstå grunderna: Vad är en webbsida? Hur fungerar knappar? Varför behöver vi React? I denna nivå lär du dig grundkoncepten genom enkla analogier från vardagen.

---

### Kärnkoncept

#### 1. Webbsidan - Ett Magiskt Papper

**Föreställ dig:**
Du har ett stort papper där du kan rita och skriva saker. På detta papper kan du:
- Rita bilder (som en bild på en katt)
- Skriva text (som "Välkommen!")
- Skapa knappar som gör saker när du trycker på dem

**En webbsida är exakt detta:**
- Bilder = `<img>`
- Text = `<p>Hej!</p>`
- Knappar = `<button>Klicka mig!</button>`

Men det magiska är att detta papper kan **ändra sig själv**!

#### 2. Komponenter - LEGO-Bitar för Webbsidor

**Tänk på LEGO:**
- Du har olika bitar: hjul, fönster, dörrar, tak
- Du kombinerar bitarna för att bygga ett hus, en bil, ett torn
- Samma bits kan användas i många byggen

**React-komponenter:**
```
Komponent = En återanvändbar bit av webbsidan

Exempel:
- En knapp
- Ett kort med bild och text
- Ett formulär
- En hel navigation
```

**Verkligt exempel:**
Tänk på YouTube:
- 🎬 **Videospelare** = En komponent
- 💬 **Kommentarssektion** = En komponent
- 👍 **Like-knapp** = En komponent
- 📝 **Kommentarsfält** = En komponent

Alla dessa komponenter byggs ihop till hela YouTube!

#### 3. State - Minneslappar för Komponenter

**Föreställ dig:**
Du spelar ett spel och håller koll på dina poäng på en lapp:
```
Poäng: 10

Du får 5 poäng → Du stryker över "10" och skriver "15"
Poäng: 15
```

Lappen **kommer ihåg** dina poäng.

**I React:**
```
State = Komponentens minne

Exempel:
- En räknare kommer ihåg vilket nummer den är på
- En kundvagn kommer ihåg vilka produkter som finns
- Ett formulär kommer ihåg vad du skrivit
```

**Magiskt:**
När state ändras → webbsidan uppdateras automatiskt! ✨

#### 4. Props - Meddelanden mellan Komponenter

**Tänk på ett brev:**
```
Från: Mamma
Till: Dig
Meddelande: "Handla mjölk"
```

Du får ett meddelande med information.

**Props i React:**
```
Från: Parent Component
Till: Child Component
Meddelande: { name: "Anna", age: 10 }
```

Komponenter skickar information till varandra med props!

**Exempel:**
```
<WelcomeCard
  name="Anna"
  message="Välkommen till vår app!"
/>

WelcomeCard får två props:
- name: "Anna"
- message: "Välkommen till vår app!"
```

#### 5. Events - Att Lyssna på Händelser

**I verkliga livet:**
```
När dörrklockan ringer → Du öppnar dörren
När telefonen ringer → Du svarar
När timern piper → Du tar ut kakan
```

**I React:**
```
När användaren klickar → Något händer
När användaren skriver → Uppdatera state
När sidan laddas → Hämta data
```

**Exempel:**
```
<button onClick={addPoäng}>
  Lägg till poäng
</button>

När knappen klickas → addPoäng-funktionen körs
```

---

### Konkreta Exempel

#### Exempel 1: Instagram-appen (utan kod)

**Hur Instagram är uppbyggd:**

```
📱 Instagram App
│
├── 📸 Header
│   ├── Instagram-logo
│   ├── Sökfält
│   └── Ikoner (hem, meddelanden, profil)
│
├── 📜 Feed
│   ├── Post-kort #1
│   │   ├── Användarinfo (bild + namn)
│   │   ├── Bild
│   │   ├── Like-knapp (minns om du gillat)
│   │   ├── Kommentar-knapp
│   │   └── Antal likes (state: 1,234)
│   │
│   ├── Post-kort #2
│   │   └── (Samma struktur)
│   │
│   └── Post-kort #3
│       └── (Samma struktur)
│
└── 🔽 Bottom Navigation
    ├── Hem-ikon
    ├── Sök-ikon
    ├── Lägg till-ikon
    ├── Reels-ikon
    └── Profil-ikon
```

**Notera:**
- **Post-kort** är en komponent som återanvänds!
- **Like-knapp** har state (gillar jag detta eller inte?)
- **Antal likes** ändras dynamiskt

#### Exempel 2: En Räknare (koncept)

```
┌─────────────────┐
│   RÄKNARE       │
│                 │
│   Count: 5      │  ← State (minnet)
│                 │
│   [+1] [-1]     │  ← Knappar (events)
└─────────────────┘

Vad händer:
1. Du klickar på [+1]
2. State ändras från 5 → 6
3. Webbsidan uppdateras automatiskt
4. Du ser "Count: 6"

Detta är React i ett nötskal!
```

#### Exempel 3: Todo-Lista (koncept)

```
┌────────────────────────┐
│  MINA UPPGIFTER        │
│                        │
│  [Lägg till uppgift]   │  ← Input + Knapp
│                        │
│  ☑️ Handla mjölk       │  ← Todo-items
│  ☑️ Ringa tandläkare   │    (lista i state)
│  ☐ Göra läxan          │
│                        │
│  3 uppgifter totalt    │  ← Beräknas från state
└────────────────────────┘

State håller koll på:
- Listan med todos
- Vilka som är klara
- Vilka som inte är klara
```

---

### 💡 Pro Tips

#### Tip 1: Tänk i "Bitar"
När du ser en webbsida, försök identifiera komponenter:
- Netflix → Filmkort, Header, Sökning, Kategori-rader
- Twitter → Tweet-kort, Sidebar, Trend-lista
- Spotify → Spellista, Låt-rad, Spelarkontroller

#### Tip 2: State är "Minne"
Om något kan ändras (räknare, formulär, kundvagn) → det är state!

#### Tip 3: Props är "Meddelanden"
Om en komponent behöver information utifrån → det är props!

---

### ✏️ Övningar

#### Övning 1.1: Identifiera Komponenter

**Svårighetsgrad:** ⭐
**Tid:** ~5 minuter

**Uppgift:**
Titta på YouTube (eller en annan webbsida du gillar). Rita eller lista 5 komponenter du ser.

**Exempel:**
```
YouTube:
1. Videospelaren (stor komponent)
2. Video-thumbnail (liten bild med titel)
3. Kommentar (användarnamn + text + likes)
4. Sidebar-meny (länkar till olika sidor)
5. Sökfält (input + sök-knapp)
```

<details>
<summary>💡 Exempel-svar</summary>

**Möjliga svar för olika sidor:**

**Netflix:**
1. Film/Serie-kort (poster + titel + info)
2. Header med logo och navigation
3. Kategori-rad ("Populärt nu", "Trender")
4. Hjälte-banner (stor bild högst upp)
5. Profil-dropdown

**Twitter:**
1. Tweet-kort (avatar + namn + text + knappar)
2. Sidebar med navigation
3. "Vad händer"-lista (trends)
4. "Vem att följa"-kort
5. Tweet-komposer (där du skriver nya tweets)

**Varför är detta viktigt?**
När du börjar tänka i komponenter förstår du hur React fungerar. Varje del är en byggbit som kan återanvändas!

</details>

---

#### Övning 1.2: Vad är State?

**Svårighetsgrad:** ⭐
**Tid:** ~5 minuter

**Uppgift:**
Vilka av dessa saker behöver "komma ihåg" något (state)? Markera Ja eller Nej.

1. En knapp som ändrar färg när du klickar på den
2. En logo som alltid ser likadan ut
3. En räknare som visar antal klick
4. En statisk bild
5. En kundvagn med produkter
6. Ett formulär där du skriver ditt namn
7. En titel som aldrig ändras
8. En timer som räknar ned

<details>
<summary>💡 Svar</summary>

1. **Ja** - Behöver komma ihåg: Vilken färg är knappen just nu?
2. **Nej** - Logon ändras aldrig, inget att minnas
3. **Ja** - Behöver komma ihåg: Hur många klick?
4. **Nej** - Bilden är statisk, inget att minnas
5. **Ja** - Behöver komma ihåg: Vilka produkter finns i kundvagnen?
6. **Ja** - Behöver komma ihåg: Vad har användaren skrivit?
7. **Nej** - Titeln ändras aldrig
8. **Ja** - Behöver komma ihåg: Hur många sekunder kvar?

**Tumregel:**
Om det kan ÄNDRAS → Behöver state
Om det är STATISKT → Inget state behövs

</details>

---

#### Övning 1.3: Bygg en App i Huvudet

**Svårighetsgrad:** ⭐⭐
**Tid:** ~8 minuter

**Uppgift:**
Tänk dig att du ska bygga en enkel "Like-knapp" för Instagram.

**Beskriv (utan kod):**
1. Vilka komponenter behövs?
2. Vad är state?
3. Vad händer när användaren klickar?

**Tips:**
Tänk på:
- Knappen själv
- Antal likes
- Har jag gillat detta eller inte?

<details>
<summary>💡 Exempel-svar</summary>

**Like-knapp för Instagram:**

**1. Komponenter:**
```
LikeButton
├── Heart-ikon (❤️ eller 🤍)
├── Antal likes (1,234)
└── Klick-hantering
```

**2. State (minneslappar):**
```
- liked: true/false (Har JAG gillat detta?)
- likeCount: 1234 (Totalt antal likes)
```

**3. Vad händer när du klickar:**

**Om liked = false:**
```
1. Användaren klickar på hjärtat
2. State ändras:
   - liked: false → true
   - likeCount: 1234 → 1235
3. Hjärtat blir rött ❤️
4. Siffran uppdateras till 1,235
```

**Om liked = true (du klickar igen):**
```
1. Användaren klickar igen (unlike)
2. State ändras:
   - liked: true → false
   - likeCount: 1235 → 1234
3. Hjärtat blir vitt 🤍
4. Siffran uppdateras till 1,234
```

**Varför är detta bra?**
Du har nu förstått HELA flödet för en React-komponent:
- State (minne)
- Event (klick)
- Uppdatering (UI ändras)

Detta är exakt hur React fungerar!

</details>

---

### 📝 Sammanfattning

**Du har nu lärt dig:**

✅ **Vad en webbsida är:**
   - Ett magiskt papper som kan ändra sig själv
   - Består av bitar (komponenter)

✅ **Komponenter:**
   - LEGO-bitar för webbsidor
   - Kan återanvändas
   - Byggs ihop till hela appar

✅ **State:**
   - Komponentens minne
   - När state ändras → UI uppdateras automatiskt
   - Exempel: räknare, kundvagn, formulär

✅ **Props:**
   - Meddelanden mellan komponenter
   - Skicka information från parent till child

✅ **Events:**
   - Lyssna på vad användaren gör
   - onClick, onChange, etc.
   - Kör funktioner när saker händer

**Nya ord du lärt dig:**
- **Komponent**: En återanvändbar UI-bit
- **State**: Data som komponenten kommer ihåg
- **Props**: Information som skickas till komponenter
- **Event**: Något som händer (klick, tangentryck, etc.)
- **UI**: User Interface (användar gränssnitt)

---

**Redo för nästa nivå?**

I Nivå 2 börjar vi koda! Vi skapar vår första React-komponent, lär oss JSX, och bygger enkla interaktiva element.

**Om du känner dig osäker:**
Läs igenom denna nivå igen. Grundkonceptet med komponenter, state och props är fundamentalt för React!

---

## Nivå 2: Grundläggande React 🧒

**Läsningstid:** ~18 minuter
**Förkunskaper:** Grundläggande JavaScript

### Introduktion

Nu börjar vi koda! I denna nivå lär du dig:
- Setup av ett React-projekt
- JSX - Reacts syntax
- Din första komponent
- Props och återanvändning
- Grundläggande styling

---

### Setup & Din Första Komponent

**Skapa ett React-projekt:**
```bash
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

**Din första komponent:**
```jsx
// App.jsx
function App() {
  return (
    <div>
      <h1>Hej React!</h1>
      <p>Detta är min första komponent</p>
    </div>
  )
}

export default App
```

**Vad händer här?**
- `function App()` = Komponenten (en JavaScript-funktion!)
- `return (...)` = Vad komponenten visar
- `<h1>`, `<p>` = HTML-liknande syntax (JSX)
- `export default` = Gör komponenten tillgänglig för andra

---

### JSX - JavaScripts och HTML:s Barn

```jsx
// JavaScript i JSX med {}
function Greeting() {
  const name = "Anna"
  const age = 10

  return (
    <div>
      <h1>Hej {name}!</h1>
      <p>Du är {age} år gammal</p>
      <p>Nästa år är du {age + 1}</p>
    </div>
  )
}
```

**Regler för JSX:**
1. Måste ha EN förälder: `<div>...</div>` eller `<>...</>`
2. Alla tags måste stängas: `<img />`, `<br />`
3. `className` istället för `class`: `<div className="box">`
4. camelCase för attribut: `onClick` inte `onclick`

---

### Props - Skicka Data till Komponenter

```jsx
// Återanvändbar komponent
function UserCard(props) {
  return (
    <div className="card">
      <h2>{props.name}</h2>
      <p>Ålder: {props.age}</p>
      <p>Email: {props.email}</p>
    </div>
  )
}

// Använd komponenten
function App() {
  return (
    <div>
      <UserCard name="Anna" age={25} email="anna@example.com" />
      <UserCard name="Erik" age={30} email="erik@example.com" />
      <UserCard name="Sara" age={28} email="sara@example.com" />
    </div>
  )
}
```

**Med destructuring (bättre!):**
```jsx
function UserCard({ name, age, email }) {
  return (
    <div className="card">
      <h2>{name}</h2>
      <p>Ålder: {age}</p>
      <p>Email: {email}</p>
    </div>
  )
}
```

---

### Villkor och Listor

**Villkor:**
```jsx
function Greeting({ isLoggedIn, username }) {
  return (
    <div>
      {isLoggedIn ? (
        <h1>Välkommen tillbaka, {username}!</h1>
      ) : (
        <h1>Vänligen logga in</h1>
      )}
    </div>
  )
}
```

**Listor:**
```jsx
function TodoList() {
  const todos = ['Handla mjölk', 'Ringa tandläkare', 'Göra läxan']

  return (
    <ul>
      {todos.map((todo, index) => (
        <li key={index}>{todo}</li>
      ))}
    </ul>
  )
}
```

---

**📝 Sammanfattning Nivå 2:**

✅ Setup med Vite
✅ JSX-syntax
✅ Komponenter som funktioner
✅ Props för återanvändbarhet
✅ Villkor och listor

---

## Nivå 3: Komponenter & State 🎓

**Läsningstid:** ~20 minuter

### useState - Komponentens Minne

```jsx
import { useState } from 'react'

function Counter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>+1</button>
      <button onClick={() => setCount(count - 1)}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  )
}
```

**Anatomin av useState:**
```jsx
const [state, setState] = useState(initialValue)
      ↑      ↑              ↑         ↑
   värdet  funktion     hooken   startvärde
```

---

### Event Handling

```jsx
function Form() {
  const [name, setName] = useState('')

  const handleSubmit = (e) => {
    e.preventDefault()
    alert(`Hej ${name}!`)
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Ditt namn"
      />
      <button type="submit">Skicka</button>
    </form>
  )
}
```

---

### Objekt och Array State

**Objekt:**
```jsx
const [user, setUser] = useState({ name: '', age: 0 })

// Uppdatera
setUser({ ...user, name: 'Anna' })
```

**Array:**
```jsx
const [todos, setTodos] = useState([])

// Lägg till
setTodos([...todos, newTodo])

// Ta bort
setTodos(todos.filter(todo => todo.id !== id))

// Uppdatera
setTodos(todos.map(todo =>
  todo.id === id ? { ...todo, done: true } : todo
))
```

---

**📝 Sammanfattning Nivå 3:**

✅ useState för state management
✅ Event handlers
✅ Formulär
✅ Objekt och array state

---

## Nivå 4: Avancerade Koncept 🚀

**Läsningstid:** ~22 minuter

### useEffect - Side Effects

```jsx
import { useState, useEffect } from 'react'

function UserProfile({ userId }) {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(data => {
        setUser(data)
        setLoading(false)
      })
  }, [userId]) // Kör när userId ändras

  if (loading) return <p>Laddar...</p>

  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  )
}
```

---

### Custom Hooks

```jsx
// useLocalStorage.js
function useLocalStorage(key, initialValue) {
  const [value, setValue] = useState(() => {
    const saved = localStorage.getItem(key)
    return saved !== null ? JSON.parse(saved) : initialValue
  })

  useEffect(() => {
    localStorage.setItem(key, JSON.stringify(value))
  }, [key, value])

  return [value, setValue]
}

// Användning
function App() {
  const [name, setName] = useLocalStorage('name', '')

  return (
    <input
      value={name}
      onChange={(e) => setName(e.target.value)}
    />
  )
}
```

---

### Context API - Global State

```jsx
import { createContext, useContext, useState } from 'react'

const ThemeContext = createContext()

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

function useTheme() {
  return useContext(ThemeContext)
}

// Användning
function App() {
  return (
    <ThemeProvider>
      <Header />
      <Content />
    </ThemeProvider>
  )
}

function Header() {
  const { theme, setTheme } = useTheme()

  return (
    <header style={{ background: theme === 'dark' ? '#333' : '#fff' }}>
      <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>
        Toggle Theme
      </button>
    </header>
  )
}
```

---

**📝 Sammanfattning Nivå 4:**

✅ useEffect för side effects
✅ Custom hooks
✅ Context API
✅ Datahämtning

---

## Nivå 5: Expert & Produktion 💎

**Läsningstid:** ~20 minuter

### Performance Optimization

**useMemo:**
```jsx
const expensiveValue = useMemo(() => {
  return computeExpensiveValue(a, b)
}, [a, b])
```

**useCallback:**
```jsx
const memoizedCallback = useCallback(() => {
  doSomething(a, b)
}, [a, b])
```

**React.memo:**
```jsx
const MyComponent = React.memo(function MyComponent(props) {
  return <div>{props.value}</div>
})
```

---

### TypeScript med React

```typescript
interface Props {
  name: string
  age: number
  onSave: (data: UserData) => void
}

const UserCard: React.FC<Props> = ({ name, age, onSave }) => {
  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age}</p>
    </div>
  )
}
```

---

### Testing

```jsx
// UserCard.test.jsx
import { render, screen } from '@testing-library/react'
import UserCard from './UserCard'

test('renders user name', () => {
  render(<UserCard name="Anna" age={25} />)
  expect(screen.getByText('Anna')).toBeInTheDocument()
})
```

---

### Best Practices

1. **Komponentstruktur:**
```
src/
├── components/
│   ├── common/
│   ├── features/
│   └── layouts/
├── hooks/
├── utils/
└── App.jsx
```

2. **Namngivning:**
- Komponenter: PascalCase (`UserCard`)
- Hooks: useXxx (`useUser`)
- Konstanter: UPPER_CASE

3. **Keep It Simple:**
- Små komponenter
- En sak per komponent
- Dela upp stora komponenter

---

## 🎓 Slutlig Självutvärdering

### Efter Nivå 1-2
- [ ] Förstå komponenter och props
- [ ] Skapa grundläggande komponenter
- [ ] Använda JSX

### Efter Nivå 3
- [ ] Hantera state med useState
- [ ] Event handling
- [ ] Formulär

### Efter Nivå 4-5
- [ ] useEffect och side effects
- [ ] Custom hooks
- [ ] Context API
- [ ] Performance optimization
- [ ] Testing

---

## 📖 Ordlista

**Component**: Återanvändbar UI-byggsten
**JSX**: JavaScript XML - HTML i JavaScript
**Props**: Argument till komponenter
**State**: Komponentens lokala data
**Hook**: Funktion som börjar med "use"
**Effect**: Bieffekter (API-anrop, etc)
**Context**: Global state
**Rendering**: När React uppdaterar DOM

---

## 🆚 React vs Andra Framework

| Feature | React | Vue | Angular | Svelte |
|---------|-------|-----|---------|--------|
| **Typ** | Library | Framework | Framework | Compiler |
| **Lär kurva** | Medel | Lätt | Svår | Lätt |
| **Bundle** | ~40KB | ~30KB | ~150KB | ~5KB |
| **TypeScript** | ✅ | ✅ | ✅ | ✅ |
| **Community** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🔗 Resurser

### Officiell Dokumentation
- [React.dev](https://react.dev) - Nya officiella docs
- [React GitHub](https://github.com/facebook/react)

### Kurser
- [React Official Tutorial](https://react.dev/learn)
- [FreeCodeCamp React](https://www.freecodecamp.org/news/tag/react/)

### Communities
- [React Subreddit](https://reddit.com/r/reactjs)
- [Reactiflux Discord](https://www.reactiflux.com/)

---

## ❓ Vanliga Frågor (FAQ)

**1. Vad är skillnaden mellan React och React Native?**
React = Webbappar, React Native = Mobila appar

**2. Behöver jag TypeScript?**
Nej, men det rekommenderas för större projekt.

**3. Vilken bundler ska jag använda?**
Vite (modern, snabb) eller Create React App (traditionell)

**4. Hur lär jag mig React snabbast?**
Bygg projekt! Start med todo-app, sedan mer komplexa.

**5. Vad är Virtual DOM?**
Reacts interna representation av UI - gör uppdateringar snabba.

**6. useState vs useReducer?**
useState för enkel state, useReducer för komplex logik.

**7. När ska jag använda useEffect?**
För side effects: API-anrop, subscriptions, timers.

**8. Hur undviker jag re-renders?**
React.memo, useMemo, useCallback

**9. Vad är React 18:s nya features?**
Concurrent rendering, automatic batching, Suspense.

**10. Server Components - vad är det?**
Komponenter som renderas på servern (Next.js).

---

## 🎉 Grattis!

Du har nu genomfört hela React-guiden!

**Vad du kan nu:**
✅ Bygga React-komponenter
✅ Hantera state och props
✅ Hooks (useState, useEffect, custom)
✅ Context API
✅ Performance optimization
✅ Best practices

**Nästa steg:**
1. Bygg en todo-app
2. Lägg till routing (React Router)
3. State management (Zustand, Redux)
4. Bygg ett större projekt!

**Lycka till! 🚀**

---

*Guide skapad 2024-11-17 | Version 1.0*

