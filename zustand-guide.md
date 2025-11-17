# Zustand - Den Kompletta Guiden: Från Nybörjare till Expert

> En komplett resa genom React state management med Zustand - från absolut nybörjare till produktionsklar expert

---

## 📚 Innehållsförteckning

- [🎯 Om Denna Guide](#-om-denna-guide)
- [🤔 Varför Zustand?](#-varför-zustand)
- [Nivå 1: State Management för 5-åringar 👶](#nivå-1-state-management-för-5-åringar-)
- [Nivå 2: Grundläggande Zustand 🧒](#nivå-2-grundläggande-zustand-)
- [Nivå 3: Praktisk Användning 🎓](#nivå-3-praktisk-användning-)
- [Nivå 4: Avancerade Koncept 🚀](#nivå-4-avancerade-koncept-)
- [Nivå 5: Expert & Produktion 💎](#nivå-5-expert--produktion-)
- [🎓 Slutlig Självutvärdering](#-slutlig-självutvärdering)
- [📖 Ordlista](#-ordlista)
- [🆚 Zustand vs Andra Lösningar](#-zustand-vs-andra-lösningar)
- [🔄 Migreringsguider](#-migreringsguider)
- [🔗 Resurser för Fördjupning](#-resurser-för-fördjupning)
- [❓ Vanliga Frågor (FAQ)](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande Zustand-guiden på svenska! Denna guide är designad för att ta dig från absolut nybörjare till produktionsklar expert genom en noggrant strukturerad inlärningsresa.

### Vad gör denna guide unik?

**Progressiv inlärning i 5 nivåer:**
- 🍼 **Nivå 1 (5-åringen)**: Förstå grundkonceptet bakom state management utan kod
- 🧒 **Nivå 2 (10-åringen)**: Lär dig grunderna i Zustand med enkla exempel
- 🎓 **Nivå 3 (Gymnasiet)**: Bygg riktiga applikationer med best practices
- 🚀 **Nivå 4 (Universitet)**: Bemästra avancerade patterns och optimeringar
- 💎 **Nivå 5 (Expert)**: Producera skalbar kod för verkliga produktionsmiljöer

**Omfattande praktisk träning:**
- 45+ övningar med kompletta lösningar
- 3 fullständiga projekt
- Verkliga kodexempel från produktionsappar
- Testing och debugging-strategier

**Total läsningstid:** 1.5-3 timmar (beroende på ditt tempo och förkunskaper)

### Hur du använder denna guide

1. **Läs sekventiellt**: Varje nivå bygger på tidigare kunskaper
2. **Gör övningarna**: Teori + praktik = verklig förståelse
3. **Ta pauser**: Varje nivå är ca 10-20 minuter, perfekt för fokuserade sessioner
4. **Bygg projekten**: Praktisk erfarenhet är ovärderlig
5. **Kom tillbaka**: Använd denna guide som referens när du kodar

### Förkunskaper

- **Nivå 1-2**: Inga förkunskaper krävs!
- **Nivå 3**: Grundläggande JavaScript och React (hooks)
- **Nivå 4**: God förståelse för React och hooks
- **Nivå 5**: Erfarenhet av att bygga React-applikationer

---

## 🤔 Varför Zustand?

Innan vi dyker in, låt oss förstå varför Zustand har blivit så populärt:

### Problemen med traditionella lösningar

**Context API** (Reacts inbyggda lösning):
- ✅ Inbyggt, ingen extra installation
- ❌ Kan orsaka onödiga re-renders
- ❌ Blir rörigt med nested providers
- ❌ Svårt att optimera performance

**Redux** (Den traditionella standarden):
- ✅ Kraftfull och beprövad
- ✅ Utmärkt DevTools
- ❌ Mycket boilerplate-kod
- ❌ Brant inlärningskurva
- ❌ Komplex setup

### Zustand: Det bästa av båda världarna

**Fördelarna:**
- ✅ **Minimal boilerplate**: Skriv mindre kod, gör mer
- ✅ **Enkel att lära**: Upp och igång på 5 minuter
- ✅ **Otrolig performance**: Inga onödiga re-renders
- ✅ **Liten bundle size**: ~1KB (gzipped)
- ✅ **Flexibel**: Använd med eller utan React
- ✅ **TypeScript-first**: Fantastiskt type-stöd
- ✅ **Middleware-ekosystem**: Persist, DevTools, Immer, och mer
- ✅ **Ingen provider-wrapper**: Använd överallt direkt

### När ska du använda Zustand?

**Perfekt för:**
- Global state som delas mellan många komponenter
- Shopping carts, user settings, theme toggles
- Data som behöver persisteras (localStorage)
- Medium till stora applikationer
- När Context API blir för komplext

**Kanske inte nödvändigt för:**
- Mycket enkel local component state (använd `useState`)
- State som bara delas mellan parent-child (använd props)
- Extremt små applikationer med minimal state

### Jämförelse i siffror

| Lösning | Bundle Size | Setup Tid | Boilerplate | Performance |
|---------|-------------|-----------|-------------|-------------|
| **Zustand** | ~1KB | 5 min | Minimal | ⭐⭐⭐⭐⭐ |
| Redux Toolkit | ~12KB | 20 min | Medel | ⭐⭐⭐⭐ |
| Context API | 0KB (inbyggt) | 10 min | Medel | ⭐⭐⭐ |
| Recoil | ~21KB | 15 min | Medel | ⭐⭐⭐⭐ |
| Jotai | ~3KB | 10 min | Låg | ⭐⭐⭐⭐⭐ |

### Vem använder Zustand?

Zustand används av tusentals företag och projekt världen över:
- Stora e-handelsplattformar
- SaaS-applikationer
- Dashboards och admin-paneler
- Mobile apps (React Native)
- Open source-projekt

**Statistik (2024):**
- 40,000+ GitHub stars
- 1,5M+ nedladdningar/vecka på npm
- Aktivt underhållen av Poimandres-kollektivet

---

Nu när du förstår *varför* Zustand, låt oss börja lära oss *hur*!

---

## Nivå 1: State Management för 5-åringar 👶

**Läsningstid:** ~8 minuter
**Förkunskaper:** Inga!

### Introduktion

Tänk dig att du har en magisk whiteboard i ditt rum som alla i familjen kan se och skriva på. När någon ändrar något på denna whiteboard, kan alla andra se förändringen direkt! Det är exakt vad state management gör i en app - det skapar en gemensam plats där information finns som alla delar kan se och uppdatera.

I denna nivå ska du förstå grundkonceptet bakom varför vi behöver dela information i appar, helt utan kod.

---

### Kärnkoncept

#### 1. Den Gemensamma Whiteboarden (Shared State)

**Föreställ dig:**
Du och dina kompisar bygger med LEGO. Ni har en gemensam låda med LEGO-bitar.

- **Utan gemensam låda:** Varje kompis har sin egen låda. Om du behöver en röd bit måste du fråga alla: "Har du en röd bit?" "Har DU en röd bit?"
- **Med gemensam låda:** Alla tittar i samma låda! När någon tar en bit, ser alla andra att den är borta.

**I en app:**
- **Utan state management:** Varje del av appen måste fråga andra delar: "Vad är användarens namn?" "Är användaren inloggad?"
- **Med state management:** Alla delar tittar på samma ställe! När namnet ändras, ser alla det direkt.

#### 2. Magiska Anteckningstavlan (The Store)

**Föreställ dig:**
På kylskåpet hemma har ni en magnetisk anteckningslista.

- Mamma skriver: "Mjölk: 2 liter kvar"
- Du dricker mjölk och ändrar till: "Mjölk: 1 liter kvar"
- Pappa ser att mjölken håller på att ta slut och köper mer
- Alla i familjen ser alltid rätt information!

**I en app:**
- Appen har en "anteckningstavla" (store) där viktig information finns
- När du klickar på "Lägg till i kundvagn", uppdateras tavlan
- Alla delar av appen (kundvagnsikon, totalpris, produktsida) ser förändringen direkt!

#### 3. Knappen som Ändrar Saker (Actions)

**Föreställ dig:**
Du har en fjärrkontroll till TV:n. Varje knapp gör något specifikt:

- Röd knapp = Volym upp
- Blå knapp = Byt kanal
- Grön knapp = Stäng av

Du kan inte bara säga "TV:n, gör något!" Du måste trycka på en SPECIFIK knapp.

**I en app:**
- Du kan inte bara säga "Appen, ändra dig!"
- Du har specifika knappar/kommandon som "addToCart", "removeFromCart", "login"
- Varje knapp vet exakt vad den ska göra

---

### Konkreta Exempel

#### Exempel 1: Lagerkontroll på Leksakerna

**Scenariot:**
Du, din bror och din syster delar på leksakerna. Ni har:
- 5 bilar
- 3 dockor
- 10 byggklossar

**Utan gemensam lista:**
```
Du: "Hur många bilar finns det?"
Bror: "Jag har 2!"
Syster: "Jag har 1!"
Du: "Då finns det... öh... 2 kvar i lådan?"
*Fel! Svårt att hålla koll!*
```

**Med gemensam lista (på whiteboarden):**
```
🚗 Bilar: 5 totalt
👧 Dockor: 3 totalt
🧱 Byggklossar: 10 totalt

När bror tar en bil:
Bror stryker över "5" och skriver "4"
→ Alla ser direkt att det finns 4 bilar kvar!
```

**I en app-värld:**
Detta är som en webshop som visar "3 st kvar i lager" - alla som tittar på produkten ser samma siffra!

#### Exempel 2: Familjekalendern

**Före (kaos!):**
- Mamma har en kalender på telefonen
- Pappa har en kalender på sin telefon
- Du har din skolkalender
- Ingen vet vad de andra gör!

**Efter (Gemensam kalender = State Management!):**
```
📅 FAMILJEKALENDERN (alla ser denna)

Måndag:
- 15:00 - Mamma jobbar
- 16:00 - Du har fotboll

Tisdag:
- 18:00 - Familj middag

När mamma bokar tandläkare:
→ Hon skriver på kalendern
→ ALLA ser direkt den nya bokningen!
```

**Varför detta är bra:**
- Ingen blir överraskad
- Ingen dubbelbokningar
- Alla har samma information

#### Exempel 3: Poängtavlan i Ett Spel

Tänk dig att ni spelar ett spel med poäng:

**Gammal lösning (sämre):**
```
Du ropas: "Jag har 10 poäng!"
Bror ropas: "Jag har 15 poäng!"

Problem:
- Vad händer om någon glömmer ropa?
- Vad händer om två ropar samtidigt?
- Hur vet vi vem som vinner?
```

**Ny lösning (bättre - med State Management):**
```
📊 POÄNGTAVLAN (synlig för alla)

Spelare 1: 10 poäng  [+5] knapp
Spelare 2: 15 poäng  [+5] knapp

När du trycker [+5]:
→ Tavlan uppdateras automatiskt
→ Alla ser den nya poängen
→ Ingen kan fuska!
→ Vinnaren syns tydligt!
```

**I en app:**
Detta är som när du samlar stjärnor i ett spel - poängen visas överallt (i hörnet, på resultatskärmen, i menyn).

---

### 💡 Pro Tips

#### Tip 1: En Sanning, Många Tittare
Tänk dig en klocka i klassrummet. Det finns EN klocka, men 25 elever kan titta på den. Alla ser samma tid!

I state management: Det finns EN plats för information, men många delar av appen kan "titta" på den.

#### Tip 2: Magiska Uppdateringar
När någon ändrar något på den gemensamma whiteboarden, behöver de inte springa runt och berätta för alla. Alla som TITTAR på whiteboarden ser förändringen automatiskt!

I en app: När någon lägger till något i kundvagnen, uppdateras kundvagnsikonen automatiskt utan att du behöver göra något extra.

#### Tip 3: Regler för Vem Som Får Ändra
På familjens whiteboard kanske bara föräldrar får skriva på kalender-delen, men du får rita i din egen hörna.

I en app: Vissa delar får bara LÄSA information (visa poäng), andra får ÄNDRA information (lägga till poäng).

---

### ✏️ Övningar

#### Övning 1.1: Hitta State i Ditt Liv

**Svårighetsgrad:** ⭐
**Tid:** ~5 minuter

**Uppgift:**
Titta dig omkring hemma och hitta 3 saker som fungerar som "delad information" (state) som flera i familjen använder.

**Exempel att tänka på:**
- Något på kylskåpet?
- Något i vardagsrummet?
- Något digitalt?

**Tips:**
Tänk på saker där FLERA personer behöver veta SAMMA information.

<details>
<summary>💡 Exempel-svar</summary>

**Möjliga svar:**

1. **Kylskåpslistan**:
   - Vem använder: Hela familjen
   - Vad den visar: Vad som behöver köpas
   - Varför det är state: Alla ser samma lista, alla kan uppdatera den

2. **TV-guiden/Netflix**:
   - Vem använder: Familjen
   - Vad den visar: Vilka program som finns
   - Varför det är state: Alla ser samma utbud

3. **WiFi-lösenordet på väggen**:
   - Vem använder: Familj och gäster
   - Vad det visar: Hur man kopplar upp sig
   - Varför det är state: EN sanning som alla kan läsa

4. **Familjens delade fotoalbum (Google Photos, iCloud)**:
   - Vem använder: Hela familjen
   - Vad det visar: Gemensamma foton
   - Varför det är state: När någon lägger till foto ser alla det

**Varför är detta viktigt?**
State management i appar är samma koncept - en gemensam plats där information finns som alla kan se och uppdatera!

</details>

---

#### Övning 1.2: Vad Händer När?

**Svårighetsgrad:** ⭐⭐
**Tid:** ~5 minuter

**Uppgift:**
Läs dessa scenarier och beskriv vad som skulle hända MED och UTAN gemensam information (state).

**Scenario 1: Mjölken i kylskåpet**
- Familjen har en lista på kylskåpet med vad som finns hemma
- Mamma dricker den sista mjölken

Vad händer MED listan?
Vad händer UTAN listan?

**Scenario 2: Netflix "Fortsätt titta"**
- Du tittar på halva filmen på TV:n
- Senare vill du fortsätta på din iPad

Vad händer om Netflix KOMMER IHÅG var du var?
Vad händer om Netflix INTE kommer ihåg?

**Tips:**
Tänk på vad som är bekvämt vs. frustrerande!

<details>
<summary>💡 Svar</summary>

**Scenario 1: Mjölken**

**Med listan (State Management):**
1. Mamma dricker sista mjölken
2. Mamma stryker "Mjölk ✓" från listan
3. Pappa ser att mjölk saknas
4. Pappa köper mjölk på väg hem
5. ✅ Alla är glada!

**Utan listan:**
1. Mamma dricker sista mjölken
2. Mamma kanske glömmer säga till
3. Pappa vet inte att mjölken är slut
4. Nästa morgon: Ingen mjölk till frukost!
5. ❌ Alla är sura!

**Scenario 2: Netflix**

**Med "fortsätt titta" (State Management):**
1. Du tittar på filmen till 45:30 på TV:n
2. Netflix sparar: "Användare123 är vid 45:30 i Film-ABC"
3. Du öppnar Netflix på iPad
4. Netflix visar: "Fortsätt titta från 45:30"
5. ✅ Du fortsätter direkt där du var!

**Utan state:**
1. Du tittar till 45:30 på TV:n
2. Inget sparas
3. Du öppnar Netflix på iPad
4. Filmen börjar från början
5. ❌ Du måste scrubba och gissa var du var!

**Varför detta är viktigt:**
Det här är exakt vad Zustand gör i dina appar - det kommer ihåg och delar information mellan olika delar!

</details>

---

#### Övning 1.3: Designa Din Egen "State"

**Svårighetsgrad:** ⭐⭐
**Tid:** ~8 minuter

**Uppgift:**
Du och dina kompisar ska bygga en lemonadstånd. Rita eller beskriv vilken information ni behöver ha på en gemensam tavla så att alla vet vad som händer.

**Tänk på:**
- Vad behöver ni hålla koll på?
- Vem behöver veta vad?
- Vad händer när något ändras?

**Tips:**
Tänk på: pengar, citroner, glas, kunder, pris...

<details>
<summary>💡 Exempel-svar</summary>

**Lemonadståndets State-Tavla:**

```
🍋 LEMONADSTÅNDET - INFO-TAVLAN
================================

📦 LAGER:
- Citroner: 15 st
- Socker: 500g
- Glas: 20 st
- Is: 2 påsar

💰 EKONOMI:
- Totalt sålt: 320 kr
- Utgifter: 150 kr
- Vinst: 170 kr

👥 IDAG:
- Antal kunder: 16 st
- Glas sålda: 16 st

⚙️ INSTÄLLNINGAR:
- Pris per glas: 20 kr
- Öppettider: 10:00 - 16:00
- Status: ÖPPET ✅
```

**Vad händer när någon köper ett glas?**

1. Kund betalar 20 kr
2. Uppdatera tavlan:
   - Glas: 20 → 19
   - Totalt sålt: 320 → 340 kr
   - Antal kunder: 16 → 17
   - Glas sålda: 16 → 17

3. Alla som tittar på tavlan ser:
   - Kassören ser nya totalen
   - Den som blandar ser att 19 glas finns kvar
   - Chefen ser att vinsten ökar!

**Varför är detta bra?**
- Alla vet alltid vad som finns
- Inga missförstånd
- Lätt att se när något börjar ta slut
- Tydlig ekonomiöversikt

**I en riktig app:**
Detta är exakt som en webshop:
- Lager = Product inventory
- Ekonomi = Sales stats
- Kunder = User activity
- Inställningar = App config

Zustand hjälper dig skapa just denna typ av "info-tavla" för din app!

</details>

---

### 📝 Sammanfattning

**Du har nu lärt dig:**

✅ **State management är som en gemensam whiteboard**
   - En plats där information finns
   - Alla kan se den
   - När någon ändrar ser alla förändringen

✅ **Varför vi behöver det:**
   - Undvika förvirring
   - Alla har samma information
   - Automatiska uppdateringar överallt

✅ **Verkliga exempel:**
   - Familjekalender = alla ser samma schema
   - Kylskåpslista = alla vet vad som behövs
   - Poängtavla = alla ser aktuell ställning
   - Netflix "fortsätt titta" = kommer ihåg var du var

✅ **Tre viktiga delar:**
   - **Store** (lager/tavla): Där information finns
   - **State** (tillstånd): Informationen själv
   - **Actions** (åtgärder): Knappar som ändrar informationen

**Nya ord du lärt dig:**
- **State**: Information/tillstånd som kan ändras
- **Store**: Platsen där state finns
- **Shared State**: Information som delas mellan flera

---

**Redo för nästa nivå?**

I Nivå 2 ska vi börja kika på riktig kod och se hur Zustand skapar denna "magiska whiteboard" i dina React-appar! Men oroa dig inte - vi bygger på det du just lärt dig, steg för steg.

**Om du känner dig osäker:**
Läs igenom denna nivå en gång till. Grundkonceptet med "delad information" är det viktigaste att förstå!

---

## Nivå 2: Grundläggande Zustand 🧒

**Läsningstid:** ~15 minuter
**Förkunskaper:** Grundläggande förståelse för variabler och funktioner

### Introduktion

Nu när du förstår konceptet med delad information, ska vi se hur Zustand faktiskt skapar denna "magiska whiteboard" i kod! I denna nivå kommer du att:
- Installera Zustand i ett projekt
- Skapa din första store
- Läsa och uppdatera state
- Förstå grundläggande begrepp och termer

Oroa dig inte om du inte är kodexpert - vi tar det steg för steg med massor av förklaringar!

---

### Kärnkoncept

#### 1. Vad är Zustand? (The Library)

**Enkel förklaring:**
Zustand är som en verktygslåda som ger dig allt du behöver för att skapa din "gemensamma whiteboard".

**Teknisk förklaring:**
Zustand är ett JavaScript-bibliotek (library) som hjälper dig hantera state i React-applikationer på ett enkelt sätt.

**Namnet:**
"Zustand" är tyska för "state" (tillstånd) - passande namn! 🇩🇪

**Storlek:**
- Hela biblioteket är bara ~1KB (mycket litet!)
- Till jämförelse: Ett foto på telefonen är ofta 2000KB+

#### 2. Store - Din Gemensamma Whiteboard

**Från Nivå 1:**
Kommer du ihåg familjekalendern eller poängtavlan? Det var din "store"!

**I kod:**
```javascript
// Detta skapar en "store" - din gemensamma whiteboard
const useStore = create((set) => ({
  // Här är informationen som finns på whiteboarden
  points: 0
}))
```

**Tänk på det som:**
- En låda som håller information
- En anteckningstavla som alla kan titta på
- En databas (men lokal i din app)

#### 3. State - Informationen Själv

**State** är den faktiska informationen som finns i din store.

**Exempel på state:**
```javascript
{
  name: "Anna",           // State: Användarens namn
  age: 10,                // State: Ålder
  isLoggedIn: true,       // State: Är inloggad
  points: 42              // State: Poäng
}
```

**Jämfört med verkliga saker:**
- Temperatur på termometern = state (ändras)
- Vattennivå i en flaska = state (ändras)
- Din position i ett spel = state (ändras)

#### 4. Actions - Funktioner som Ändrar State

**Actions** är som knappar som ändrar informationen.

**Exempel:**
```javascript
const useStore = create((set) => ({
  points: 0,

  // Action: Lägg till poäng
  addPoints: (amount) => set((state) => ({
    points: state.points + amount
  })),

  // Action: Nollställ poäng
  resetPoints: () => set({ points: 0 })
}))
```

**Varje action:**
- Har ett tydligt namn (addPoints, resetPoints)
- Vet exakt vad den ska göra
- Uppdaterar state på ett säkert sätt

#### 5. Selectors - Titta på Specifika Delar

**Selector** = att välja ut exakt vad du vill titta på från whiteboa rden.

**Exempel:**
```javascript
// Titta på ALLT
const state = useStore()

// Titta bara på points (mer effektivt!)
const points = useStore((state) => state.points)
```

**Analogien:**
På familjens whiteboard kanske du bara bryr dig om "Vad ska vi äta ikväll?" - du behöver inte läsa hela kalendern!

---

### Konkreta Exempel

#### Exempel 1: Din Första Store (Counter)

Låt oss skapa den enklaste möjliga store - en räknare!

**1. Installation:**
```bash
npm install zustand
# eller
yarn add zustand
```

**2. Skapa store (i en fil: `store.js`):**
```javascript
import { create } from 'zustand'

// Skapa en store för att räkna saker
const useCounterStore = create((set) => ({
  // State: Värdet vi håller koll på
  count: 0,

  // Action: Öka med 1
  increment: () => set((state) => ({ count: state.count + 1 })),

  // Action: Minska med 1
  decrement: () => set((state) => ({ count: state.count - 1 })),

  // Action: Nollställ
  reset: () => set({ count: 0 })
}))

export default useCounterStore
```

**3. Använd i en React-komponent:**
```javascript
import useCounterStore from './store'

function Counter() {
  // Hämta state och actions från store
  const count = useCounterStore((state) => state.count)
  const increment = useCounterStore((state) => state.increment)
  const decrement = useCounterStore((state) => state.decrement)
  const reset = useCounterStore((state) => state.reset)

  return (
    <div>
      <h1>Räknare: {count}</h1>
      <button onClick={increment}>+1</button>
      <button onClick={decrement}>-1</button>
      <button onClick={reset}>Nollställ</button>
    </div>
  )
}
```

**Vad händer när du klickar?**
1. Du klickar på "+1"-knappen
2. `increment`-funktionen körs
3. Store uppdateras: `count` blir +1
4. React ser att state ändrats
5. Komponenten renderas om med nya värdet
6. Du ser den nya siffran på skärmen!

**Fördelar:**
- ✅ Mycket enkel kod
- ✅ Tydligt vad varje knapp gör
- ✅ Lätt att förstå och felsöka

#### Exempel 2: Flera Komponenter Delar State

Det magiska med Zustand är att flera komponenter kan använda SAMMA store!

**Store (användarprofil):**
```javascript
import { create } from 'zustand'

const useUserStore = create((set) => ({
  name: 'Gäst',
  points: 0,

  setName: (newName) => set({ name: newName }),
  addPoints: (amount) => set((state) => ({
    points: state.points + amount
  }))
}))

export default useUserStore
```

**Komponent 1: Header (visar namn):**
```javascript
import useUserStore from './userStore'

function Header() {
  const name = useUserStore((state) => state.name)

  return <header>Välkommen, {name}!</header>
}
```

**Komponent 2: Sidebar (visar poäng):**
```javascript
import useUserStore from './userStore'

function Sidebar() {
  const points = useUserStore((state) => state.points)

  return (
    <aside>
      <p>Dina poäng: {points}</p>
    </aside>
  )
}
```

**Komponent 3: GameButton (lägger till poäng):**
```javascript
import useUserStore from './userStore'

function GameButton() {
  const addPoints = useUserStore((state) => state.addPoints)

  return (
    <button onClick={() => addPoints(10)}>
      Klicka mig! (+10 poäng)
    </button>
  )
}
```

**Magin:**
```
När du klickar på GameButton:
1. addPoints(10) körs
2. Store uppdateras: points = 10
3. Sidebar ser ändringen automatiskt → visar "Dina poäng: 10"
4. Header påverkas INTE (den tittar bara på name)
```

**Detta är kraften i Zustand:**
- Flera komponenter delar samma information
- När en ändrar, ser alla andra det direkt
- Varje komponent väljer exakt vad den vill titta på

#### Exempel 3: Todo-lista (Flera State-värden)

Låt oss bygga något lite mer avancerat - en enkel att göra-lista!

**Store:**
```javascript
import { create } from 'zustand'

const useTodoStore = create((set) => ({
  // State: Lista med todos
  todos: [],

  // Action: Lägg till en todo
  addTodo: (text) => set((state) => ({
    todos: [...state.todos, {
      id: Date.now(),
      text: text,
      done: false
    }]
  })),

  // Action: Markera som klar
  toggleTodo: (id) => set((state) => ({
    todos: state.todos.map(todo =>
      todo.id === id
        ? { ...todo, done: !todo.done }
        : todo
    )
  })),

  // Action: Ta bort en todo
  removeTodo: (id) => set((state) => ({
    todos: state.todos.filter(todo => todo.id !== id)
  }))
}))

export default useTodoStore
```

**Komponenten:**
```javascript
import { useState } from 'react'
import useTodoStore from './todoStore'

function TodoList() {
  const [input, setInput] = useState('')

  // Hämta från store
  const todos = useTodoStore((state) => state.todos)
  const addTodo = useTodoStore((state) => state.addTodo)
  const toggleTodo = useTodoStore((state) => state.toggleTodo)
  const removeTodo = useTodoStore((state) => state.removeTodo)

  const handleAdd = () => {
    if (input.trim()) {
      addTodo(input)
      setInput('')
    }
  }

  return (
    <div>
      <h1>Min Todo-lista</h1>

      {/* Input för ny todo */}
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Vad ska du göra?"
      />
      <button onClick={handleAdd}>Lägg till</button>

      {/* Lista över todos */}
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => toggleTodo(todo.id)}
            />
            <span style={{
              textDecoration: todo.done ? 'line-through' : 'none'
            }}>
              {todo.text}
            </span>
            <button onClick={() => removeTodo(todo.id)}>❌</button>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

**Vad händer här?**
- `todos` är en array (lista) med todo-objekt
- `addTodo` lägger till ett nytt objekt i listan
- `toggleTodo` ändrar `done` från false → true eller true → false
- `removeTodo` tar bort en todo från listan

**Notera:**
- Vi använder `useState` för input-fältet (lokal state)
- Vi använder Zustand för todos (delad state)
- Detta är vanligt: lokal state för enkla saker, Zustand för delad information!

---

### 💡 Pro Tips

#### Tip 1: Namngivning av Stores
```javascript
// Bra namngivning
const useUserStore = create(...)      // För användare
const useCartStore = create(...)      // För kundvagn
const useGameStore = create(...)      // För spel

// Börja alltid med "use" (React-konvention för hooks)
// Sluta med "Store" så man vet vad det är
```

#### Tip 2: Organisera State Logiskt
```javascript
// Mindre bra: Allt i en stor store
const useStore = create((set) => ({
  userName: 'Anna',
  userAge: 10,
  cartItems: [],
  cartTotal: 0,
  gamePoints: 0,
  gameLevel: 1
  // ... detta blir rörigt!
}))

// Bättre: Dela upp i flera stores
const useUserStore = create((set) => ({
  name: 'Anna',
  age: 10
}))

const useCartStore = create((set) => ({
  items: [],
  total: 0
}))

const useGameStore = create((set) => ({
  points: 0,
  level: 1
}))
```

#### Tip 3: Använd Selectors för Performance
```javascript
// Mindre effektivt: Hela state
const state = useStore()
console.log(state.count) // Komponenten uppdateras även om annat ändras!

// Mer effektivt: Välj bara vad du behöver
const count = useStore((state) => state.count)
// Komponenten uppdateras BARA när count ändras!
```

---

### ✏️ Övningar

#### Övning 2.1: Din Första Counter

**Svårighetsgrad:** ⭐
**Tid:** ~10 minuter

**Uppgift:**
Skapa en enkel räknare med Zustand.

**Krav:**
1. En store med ett nummer (count)
2. En knapp som ökar numret
3. Visa numret på skärmen

**Startkod:**
```javascript
import { create } from 'zustand'

// TODO: Skapa din store här
const useCounterStore = create((set) => ({
  // Din kod här...
}))

function App() {
  // TODO: Använd store här

  return (
    <div>
      {/* Din UI här */}
    </div>
  )
}
```

**Tips:**
- Börja med `count: 0` i din store
- Skapa en `increment`-funktion
- Använd `useCounterStore` i komponenten

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

// Store
const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}))

// Komponent
function App() {
  const count = useCounterStore((state) => state.count)
  const increment = useCounterStore((state) => state.increment)

  return (
    <div>
      <h1>Räknare: {count}</h1>
      <button onClick={increment}>Öka</button>
    </div>
  )
}

export default App
```

**Varför fungerar detta?**
1. `create((set) => ({...}))` skapar en store
2. `count: 0` är initial state
3. `increment` är en funktion som uppdaterar state
4. `set((state) => ({...}))` är hur vi ändrar state
5. `useCounterStore((state) => state.count)` hämtar count från store
6. När `increment` körs → state ändras → React renderar om

**Vanliga fel:**
- ❌ `set({ count: count + 1 })` - fungerar inte, `count` är inte definierat här!
- ✅ `set((state) => ({ count: state.count + 1 }))` - korrekt!

</details>

---

#### Övning 2.2: Lägg till Decrement och Reset

**Svårighetsgrad:** ⭐⭐
**Tid:** ~10 minuter

**Uppgift:**
Utöka din räknare från 2.1 med:
1. En knapp som minskar värdet (-1)
2. En knapp som nollställer till 0

**Tips:**
- `decrement` är nästan som `increment` fast minus
- `reset` är enklast - sätt bara till 0 direkt

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const useCounterStore = create((set) => ({
  count: 0,

  increment: () => set((state) => ({ count: state.count + 1 })),

  decrement: () => set((state) => ({ count: state.count - 1 })),

  reset: () => set({ count: 0 })
  // Notera: reset behöver inte state-funktionen,
  // vi vet exakt vad vi vill sätta det till!
}))

function App() {
  const count = useCounterStore((state) => state.count)
  const increment = useCounterStore((state) => state.increment)
  const decrement = useCounterStore((state) => state.decrement)
  const reset = useCounterStore((state) => state.reset)

  return (
    <div>
      <h1>Räknare: {count}</h1>
      <button onClick={increment}>+1</button>
      <button onClick={decrement}>-1</button>
      <button onClick={reset}>Nollställ</button>
    </div>
  )
}
```

**Notera skillnaden:**
```javascript
// När du behöver tidigare värde:
increment: () => set((state) => ({ count: state.count + 1 }))

// När du vet exakt vad det ska vara:
reset: () => set({ count: 0 })
```

**Bonus:**
Lägg till en "lägg till 10"-knapp:
```javascript
addTen: () => set((state) => ({ count: state.count + 10 }))
```

</details>

---

#### Övning 2.3: Flera State-värden

**Svårighetsgrad:** ⭐⭐
**Tid:** ~12 minuter

**Uppgift:**
Skapa en store för en användarprofil med:
- `name` (string): Användarens namn
- `age` (number): Ålder
- `isLoggedIn` (boolean): Om användaren är inloggad

Och actions för att:
- Ändra namn
- Öka ålder (födelsedag!)
- Logga in/ut (toggle)

**Startkod:**
```javascript
const useUserStore = create((set) => ({
  // Din state här

  // Dina actions här
}))
```

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const useUserStore = create((set) => ({
  // State
  name: 'Gäst',
  age: 0,
  isLoggedIn: false,

  // Actions
  setName: (newName) => set({ name: newName }),

  increaseAge: () => set((state) => ({ age: state.age + 1 })),

  toggleLogin: () => set((state) => ({ isLoggedIn: !state.isLoggedIn }))
}))

// Exempel på användning
function UserProfile() {
  const name = useUserStore((state) => state.name)
  const age = useUserStore((state) => state.age)
  const isLoggedIn = useUserStore((state) => state.isLoggedIn)
  const setName = useUserStore((state) => state.setName)
  const increaseAge = useUserStore((state) => state.increaseAge)
  const toggleLogin = useUserStore((state) => state.toggleLogin)

  return (
    <div>
      <h2>Profil</h2>
      <p>Namn: {name}</p>
      <p>Ålder: {age}</p>
      <p>Status: {isLoggedIn ? 'Inloggad ✅' : 'Utloggad ❌'}</p>

      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Ditt namn"
      />
      <button onClick={increaseAge}>Grattis på födelsedagen! 🎂</button>
      <button onClick={toggleLogin}>
        {isLoggedIn ? 'Logga ut' : 'Logga in'}
      </button>
    </div>
  )
}
```

**Notera:**
- Vi kan uppdatera flera state-värden oberoende av varandra
- `!state.isLoggedIn` togglar mellan true/false
- Varje action uppdaterar bara det den behöver - resten förblir oförändrat

**Bonus-utmaning:**
Lägg till en action `setBirthday(year)` som räknar ut åldern baserat på året:
```javascript
setBirthday: (birthYear) => set({
  age: new Date().getFullYear() - birthYear
})
```

</details>

---

#### Övning 2.4: Shopping Cart Basics

**Svårighetsgrad:** ⭐⭐⭐
**Tid:** ~15 minuter

**Uppgift:**
Skapa en enkel kundvagn (shopping cart) store.

**Krav:**
- State: `items` (array av produkter)
- Action: `addItem(product)` - lägg till produkt
- Action: `removeItem(productId)` - ta bort produkt
- Action: `clearCart()` - töm kundvagnen

**Varje produkt är ett objekt:**
```javascript
{
  id: 1,
  name: "T-shirt",
  price: 199
}
```

**Tips:**
- Använd array-metoder som `filter`, spread operator `[...]`
- `filter` tar bort element från en array

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const useCartStore = create((set) => ({
  items: [],

  // Lägg till produkt i kundvagnen
  addItem: (product) => set((state) => ({
    items: [...state.items, product]
  })),

  // Ta bort produkt baserat på ID
  removeItem: (productId) => set((state) => ({
    items: state.items.filter(item => item.id !== productId)
  })),

  // Töm hela kundvagnen
  clearCart: () => set({ items: [] })
}))

// Exempel på användning
function ShoppingCart() {
  const items = useCartStore((state) => state.items)
  const addItem = useCartStore((state) => state.addItem)
  const removeItem = useCartStore((state) => state.removeItem)
  const clearCart = useCartStore((state) => state.clearCart)

  // Räkna totalt pris
  const total = items.reduce((sum, item) => sum + item.price, 0)

  return (
    <div>
      <h2>Kundvagn ({items.length} produkter)</h2>

      {/* Lista produkter */}
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.name} - {item.price} kr
            <button onClick={() => removeItem(item.id)}>Ta bort</button>
          </li>
        ))}
      </ul>

      <p><strong>Totalt: {total} kr</strong></p>

      {items.length > 0 && (
        <button onClick={clearCart}>Töm kundvagn</button>
      )}

      {/* Exempel: Lägg till produkter */}
      <h3>Produkter</h3>
      <button onClick={() => addItem({ id: 1, name: 'T-shirt', price: 199 })}>
        Köp T-shirt (199 kr)
      </button>
      <button onClick={() => addItem({ id: 2, name: 'Jeans', price: 599 })}>
        Köp Jeans (599 kr)
      </button>
    </div>
  )
}
```

**Förklaring:**

1. **addItem med spread operator:**
   ```javascript
   [...state.items, product]
   ```
   - `...state.items` = alla befintliga produkter
   - `, product` = plus den nya produkten
   - Skapar en NY array (viktigt i React!)

2. **removeItem med filter:**
   ```javascript
   state.items.filter(item => item.id !== productId)
   ```
   - Behåll alla produkter där ID INTE matchar
   - Returnerar en ny array utan den borttagna produkten

3. **Total-beräkning:**
   ```javascript
   items.reduce((sum, item) => sum + item.price, 0)
   ```
   - `reduce` går igenom alla items
   - Summerar alla prices
   - Startvärde är 0

**Varför fungerar detta?**
- Zustand ser när `items` ändras
- React renderar om komponenten
- Vi ser uppdaterad lista och totalt pris!

**Bonus:**
Lägg till en `getItemCount()` funktion som returnerar antal produkter:
```javascript
const useCartStore = create((set, get) => ({
  items: [],

  // ...actions här...

  // Getter-funktion
  getItemCount: () => get().items.length
}))

// Användning:
const itemCount = useCartStore((state) => state.getItemCount())
```

</details>

---

#### Övning 2.5: Två Komponenter Delar State

**Svårighetsgrad:** ⭐⭐⭐
**Tid:** ~12 minuter

**Uppgift:**
Skapa två separata komponenter som delar samma store:
1. **Counter Display** - visar bara värdet
2. **Counter Controls** - har bara knappar

När du klickar på knappar i Controls, ska Display uppdateras automatiskt!

**Utmaning:**
Gör detta utan att använda props mellan komponenterna - allt via Zustand!

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

// Store (delad mellan komponenter)
const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 })
}))

// Komponent 1: Visar bara värdet
function CounterDisplay() {
  const count = useCounterStore((state) => state.count)

  return (
    <div style={{
      fontSize: '48px',
      fontWeight: 'bold',
      textAlign: 'center',
      padding: '20px',
      background: '#f0f0f0',
      borderRadius: '8px'
    }}>
      {count}
    </div>
  )
}

// Komponent 2: Har bara knappar
function CounterControls() {
  const increment = useCounterStore((state) => state.increment)
  const decrement = useCounterStore((state) => state.decrement)
  const reset = useCounterStore((state) => state.reset)

  return (
    <div style={{
      display: 'flex',
      gap: '10px',
      justifyContent: 'center',
      marginTop: '20px'
    }}>
      <button onClick={decrement}>-</button>
      <button onClick={reset}>Reset</button>
      <button onClick={increment}>+</button>
    </div>
  )
}

// Main App
function App() {
  return (
    <div style={{ padding: '40px' }}>
      <h1>Delad State Demo</h1>
      <CounterDisplay />
      <CounterControls />

      <p style={{ marginTop: '20px', color: '#666' }}>
        💡 Notera: Dessa två komponenter delar ingen kod direkt!
        De kommunicerar via Zustand store.
      </p>
    </div>
  )
}

export default App
```

**Vad är magiskt här?**

1. **Ingen props-passing:**
   ```javascript
   // INTE så här:
   <CounterDisplay count={count} />
   <CounterControls onIncrement={...} onDecrement={...} />

   // Utan så här:
   <CounterDisplay />
   <CounterControls />
   ```

2. **Komponenter vet ingenting om varandra:**
   - `CounterDisplay` vet inte att `CounterControls` finns
   - `CounterControls` vet inte att `CounterDisplay` finns
   - Men de delar samma information via store!

3. **Automatisk synkronisering:**
   - Klicka i Controls → Display uppdateras direkt
   - Ingen manuell kommunikation behövs

**Detta är kraften i Zustand:**
Komponenter kan vara helt oberoende men ändå dela state!

**Real-world exempel:**
- Kundvagnsikon i header + kundvagn i sidebar
- Användarnamn i header + profil i settings
- Notifications-badge + notifications-lista

**Bonus-utmaning:**
Lägg till en tredje komponent `CounterHistory` som visar de senaste 5 ändringarna:
```javascript
// Store med history
const useCounterStore = create((set) => ({
  count: 0,
  history: [],

  increment: () => set((state) => ({
    count: state.count + 1,
    history: [...state.history, `+1 (nu: ${state.count + 1})`].slice(-5)
  }))
  // ...
}))
```

</details>

---

### 📝 Sammanfattning

**Du har nu lärt dig:**

✅ **Vad Zustand är:**
   - Ett litet (1KB) JavaScript-bibliotek
   - Hjälper dig hantera state i React
   - Mycket enklare än Redux, kraftfullare än Context API

✅ **Grundläggande begrepp:**
   - **Store**: Platsen där all state finns (`create(...)`)
   - **State**: Den faktiska informationen (`count: 0`)
   - **Actions**: Funktioner som ändrar state (`increment: () => set(...)`)
   - **Selectors**: Välja specifika delar (`state => state.count`)

✅ **Hur man skapar en store:**
   ```javascript
   const useStore = create((set) => ({
     // State här
     value: 0,

     // Actions här
     setValue: (newValue) => set({ value: newValue })
   }))
   ```

✅ **Hur man använder en store:**
   ```javascript
   const value = useStore((state) => state.value)
   const setValue = useStore((state) => state.setValue)
   ```

✅ **Två sätt att uppdatera state:**
   ```javascript
   // 1. När du behöver tidigare värde
   set((state) => ({ count: state.count + 1 }))

   // 2. När du vet exakt vad det ska vara
   set({ count: 0 })
   ```

**Nya ord du lärt dig:**
- **Library (bibliotek)**: Färdig kod du kan använda
- **Hook**: En React-funktion som börjar med "use"
- **Selector**: Funktion för att välja ut specifik data
- **Immutable**: Skapa ny data istället för att ändra befintlig
- **Array methods**: filter, map, spread operator (...)

**Common patterns du lärt dig:**
- Counter (räknare)
- Toggle (växla mellan true/false)
- List management (lägg till, ta bort från listor)
- Flera komponenter delar state

---

**Redo för nästa nivå?**

I Nivå 3 dyker vi djupare in i:
- Optimering med selectors
- Async actions (hämta data från API)
- DevTools för debugging
- Persist middleware (spara state i localStorage)
- Best practices och patterns

Du har nu grunderna - nästa nivå bygger vidare med mer avancerade koncept!

**Fortsätt öva:**
Försök bygga:
- En färgväljare (color picker state)
- En enkel quiz-app (frågor, poäng, rätt/fel)
- En favoriter-lista (lägg till/ta bort favoriter)

---

## Nivå 3: Praktisk Användning 🎓

**Läsningstid:** ~20 minuter
**Förkunskaper:** JavaScript, React hooks, grundläggande Zustand (Nivå 2)

### Introduktion

Nu när du kan grunderna i Zustand, är det dags att lära dig hur man använder det i verkliga applikationer! I denna nivå kommer du att lära dig:
- Optimera performance med smarta selectors
- Hämta data från API:er (async actions)
- Använda DevTools för debugging
- Spara state mellan sessioner (persist middleware)
- Best practices för strukturering av stores
- Hantera listor och komplexa objekt

Detta är nivån där du blir redo att bygga riktiga applikationer med Zustand!

---

### Kärnkoncept

#### 1. Optimerade Selectors & Shallow Equality

**Problemet:**
```javascript
// ❌ Dåligt: Komponenten renderas om varje gång NÅGOT i store ändras
const state = useStore()
console.log(state.user.name)
```

Även om bara `count` ändras, renderas komponenten om eftersom hela `state`-objektet är nytt.

**Lösningen - Använd Selectors:**
```javascript
// ✅ Bra: Komponenten renderas bara när name ändras
const name = useStore((state) => state.user.name)
```

**Djupdykning:**

Zustand använder `Object.is()` för att jämföra värden. Detta kallas "strict equality":

```javascript
Object.is(5, 5)        // true
Object.is("hej", "hej") // true
Object.is({}, {})      // false (olika objekt!)
Object.is([], [])      // false (olika arrayer!)
```

**Shallow Comparison:**
För objekt och arrayer kan du använda `shallow`:

```javascript
import { create } from 'zustand'
import { shallow } from 'zustand/shallow'

const useUserStore = create((set) => ({
  user: {
    name: 'Anna',
    age: 25,
    email: 'anna@example.com'
  },
  updateUser: (updates) => set((state) => ({
    user: { ...state.user, ...updates }
  }))
}))

// Användning med shallow
function UserCard() {
  // Jämför objektets properties, inte objektet självt
  const user = useUserStore(
    (state) => ({ name: state.user.name, age: state.user.age }),
    shallow
  )

  // Renderas BARA om name eller age ändras, inte om email ändras!
  return <div>{user.name} ({user.age} år)</div>
}
```

**Praktiska riktlinjer:**
```javascript
// ✅ Primitiva värden - bara använd selector
const count = useStore((state) => state.count)

// ✅ Enstaka property från objekt
const name = useStore((state) => state.user.name)

// ✅ Flera properties - använd shallow
const { name, age } = useStore(
  (state) => ({ name: state.user.name, age: state.user.age }),
  shallow
)

// ✅ Array - om du bara läser
const todos = useStore((state) => state.todos)

// ❌ Undvik: Hela state
const state = useStore()
```

#### 2. Async Actions & API Calls

I verkliga appar behöver du ofta hämta data från servrar. Zustand gör detta enkelt!

**Grundläggande async pattern:**
```javascript
const useDataStore = create((set) => ({
  data: null,
  loading: false,
  error: null,

  fetchData: async (url) => {
    // Sätt loading till true
    set({ loading: true, error: null })

    try {
      const response = await fetch(url)
      const data = await response.json()

      // Lyckades - uppdatera data
      set({ data, loading: false })
    } catch (error) {
      // Misslyckades - spara error
      set({ error: error.message, loading: false })
    }
  }
}))
```

**Användning i komponent:**
```javascript
function DataDisplay() {
  const { data, loading, error, fetchData } = useDataStore()

  useEffect(() => {
    fetchData('https://api.example.com/data')
  }, [])

  if (loading) return <div>Laddar...</div>
  if (error) return <div>Error: {error}</div>
  if (!data) return <div>Ingen data</div>

  return <div>{JSON.stringify(data)}</div>
}
```

**Avancerad pattern med abort:**
```javascript
const useDataStore = create((set, get) => ({
  data: null,
  loading: false,
  error: null,
  abortController: null,

  fetchData: async (url) => {
    // Avbryt tidigare request om den fortfarande körs
    get().abortController?.abort()

    const controller = new AbortController()
    set({ loading: true, error: null, abortController: controller })

    try {
      const response = await fetch(url, { signal: controller.signal })
      const data = await response.json()
      set({ data, loading: false })
    } catch (error) {
      if (error.name !== 'AbortError') {
        set({ error: error.message, loading: false })
      }
    }
  },

  cancelFetch: () => {
    get().abortController?.abort()
    set({ loading: false })
  }
}))
```

#### 3. Derived State (Computed Values)

Ibland vill du ha värden som beräknas från befintlig state:

**Metod 1: Selectors (recommended):**
```javascript
const useTodoStore = create((set) => ({
  todos: []
  // ... actions
}))

// Använd selector för derived state
function TodoStats() {
  const totalTodos = useTodoStore((state) => state.todos.length)
  const completedTodos = useTodoStore((state) =>
    state.todos.filter(t => t.done).length
  )
  const activeTodos = useTodoStore((state) =>
    state.todos.filter(t => !t.done).length
  )

  return (
    <div>
      <p>Totalt: {totalTodos}</p>
      <p>Klara: {completedTodos}</p>
      <p>Aktiva: {activeTodos}</p>
    </div>
  )
}
```

**Metod 2: Getters i store:**
```javascript
const useTodoStore = create((set, get) => ({
  todos: [],

  // Getter functions
  getTotalCount: () => get().todos.length,
  getCompletedCount: () => get().todos.filter(t => t.done).length,
  getActiveCount: () => get().todos.filter(t => !t.done).length,

  // Actions
  addTodo: (text) => set((state) => ({
    todos: [...state.todos, { id: Date.now(), text, done: false }]
  }))
}))

// Användning
function TodoStats() {
  const getTotalCount = useTodoStore((state) => state.getTotalCount)
  const getCompletedCount = useTodoStore((state) => state.getCompletedCount)

  return (
    <div>
      <p>Totalt: {getTotalCount()}</p>
      <p>Klara: {getCompletedCount()}</p>
    </div>
  )
}
```

#### 4. Middleware: Persist

Spara state till localStorage automatiskt!

**Installation:**
```bash
npm install zustand
```

**Grundläggande användning:**
```javascript
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

const useSettingsStore = create(
  persist(
    (set) => ({
      theme: 'light',
      language: 'sv',
      fontSize: 16,

      setTheme: (theme) => set({ theme }),
      setLanguage: (language) => set({ language }),
      setFontSize: (fontSize) => set({ fontSize })
    }),
    {
      name: 'app-settings' // Nyckeln i localStorage
    }
  )
)
```

**Vad händer?**
- När state ändras → sparas automatiskt i localStorage
- När sidan laddas → återställs state från localStorage
- Fungerar över flera flikar (samma state!)

**Avancerad konfiguration:**
```javascript
const useUserStore = create(
  persist(
    (set) => ({
      user: null,
      token: null,
      preferences: {},

      login: (user, token) => set({ user, token }),
      logout: () => set({ user: null, token: null })
    }),
    {
      name: 'user-storage',

      // Välj vilka delar som ska sparas
      partialize: (state) => ({
        user: state.user,
        preferences: state.preferences
        // token sparas INTE (för säkerhet)
      }),

      // Använd sessionStorage istället
      storage: sessionStorage,

      // Migrera mellan versioner
      version: 1,
      migrate: (persistedState, version) => {
        if (version === 0) {
          // Uppdatera från gammal struktur
          return {
            ...persistedState,
            preferences: persistedState.settings || {}
          }
        }
        return persistedState
      }
    }
  )
)
```

#### 5. Middleware: DevTools

Debug din store med Redux DevTools!

**Installation:**
```bash
npm install zustand
```

**Användning:**
```javascript
import { create } from 'zustand'
import { devtools } from 'zustand/middleware'

const useCounterStore = create(
  devtools(
    (set) => ({
      count: 0,
      increment: () => set((state) => ({ count: state.count + 1 }), false, 'increment'),
      decrement: () => set((state) => ({ count: state.count - 1 }), false, 'decrement')
    }),
    { name: 'CounterStore' } // Namn i DevTools
  )
)
```

**Funktioner i DevTools:**
- Se alla state-ändringar
- Time-travel debugging (gå tillbaka i tiden!)
- Inspektera actions
- Exportera/importera state

**Kombinera med persist:**
```javascript
const useStore = create(
  devtools(
    persist(
      (set) => ({
        // din store här
      }),
      { name: 'my-storage' }
    ),
    { name: 'MyStore' }
  )
)
```

**Notera ordningen:**
- Innerst: Din store-logik
- Mellerst: persist (om du vill)
- Ytterst: devtools

---

### Konkreta Exempel

#### Exempel 1: Todo-app med Persist och DevTools

En komplett todo-app med alla features:

```javascript
import { create } from 'zustand'
import { persist, devtools } from 'zustand/middleware'

const useTodoStore = create(
  devtools(
    persist(
      (set, get) => ({
        todos: [],
        filter: 'all', // 'all', 'active', 'completed'

        // Actions
        addTodo: (text) => set((state) => ({
          todos: [...state.todos, {
            id: Date.now(),
            text,
            done: false,
            createdAt: new Date().toISOString()
          }]
        }), false, 'addTodo'),

        toggleTodo: (id) => set((state) => ({
          todos: state.todos.map(todo =>
            todo.id === id ? { ...todo, done: !todo.done } : todo
          )
        }), false, 'toggleTodo'),

        deleteTodo: (id) => set((state) => ({
          todos: state.todos.filter(todo => todo.id !== id)
        }), false, 'deleteTodo'),

        editTodo: (id, newText) => set((state) => ({
          todos: state.todos.map(todo =>
            todo.id === id ? { ...todo, text: newText } : todo
          )
        }), false, 'editTodo'),

        setFilter: (filter) => set({ filter }, false, 'setFilter'),

        clearCompleted: () => set((state) => ({
          todos: state.todos.filter(todo => !todo.done)
        }), false, 'clearCompleted'),

        // Getters
        getFilteredTodos: () => {
          const { todos, filter } = get()
          switch (filter) {
            case 'active':
              return todos.filter(t => !t.done)
            case 'completed':
              return todos.filter(t => t.done)
            default:
              return todos
          }
        },

        getStats: () => {
          const todos = get().todos
          return {
            total: todos.length,
            active: todos.filter(t => !t.done).length,
            completed: todos.filter(t => t.done).length
          }
        }
      }),
      { name: 'todo-storage' }
    ),
    { name: 'TodoStore' }
  )
)

export default useTodoStore
```

**Komponent:**
```javascript
import { useState } from 'react'
import useTodoStore from './todoStore'

function TodoApp() {
  const [input, setInput] = useState('')

  const todos = useTodoStore((state) => state.getFilteredTodos())
  const filter = useTodoStore((state) => state.filter)
  const addTodo = useTodoStore((state) => state.addTodo)
  const toggleTodo = useTodoStore((state) => state.toggleTodo)
  const deleteTodo = useTodoStore((state) => state.deleteTodo)
  const setFilter = useTodoStore((state) => state.setFilter)
  const clearCompleted = useTodoStore((state) => state.clearCompleted)
  const stats = useTodoStore((state) => state.getStats())

  const handleSubmit = (e) => {
    e.preventDefault()
    if (input.trim()) {
      addTodo(input)
      setInput('')
    }
  }

  return (
    <div className="todo-app">
      <h1>Mina Uppgifter</h1>

      {/* Add form */}
      <form onSubmit={handleSubmit}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Vad behöver göras?"
        />
        <button type="submit">Lägg till</button>
      </form>

      {/* Filter buttons */}
      <div className="filters">
        <button
          onClick={() => setFilter('all')}
          className={filter === 'all' ? 'active' : ''}
        >
          Alla ({stats.total})
        </button>
        <button
          onClick={() => setFilter('active')}
          className={filter === 'active' ? 'active' : ''}
        >
          Aktiva ({stats.active})
        </button>
        <button
          onClick={() => setFilter('completed')}
          className={filter === 'completed' ? 'active' : ''}
        >
          Klara ({stats.completed})
        </button>
      </div>

      {/* Todo list */}
      <ul className="todo-list">
        {todos.map(todo => (
          <li key={todo.id} className={todo.done ? 'done' : ''}>
            <input
              type="checkbox"
              checked={todo.done}
              onChange={() => toggleTodo(todo.id)}
            />
            <span>{todo.text}</span>
            <button onClick={() => deleteTodo(todo.id)}>×</button>
          </li>
        ))}
      </ul>

      {/* Footer */}
      {stats.completed > 0 && (
        <button onClick={clearCompleted}>
          Rensa klara ({stats.completed})
        </button>
      )}
    </div>
  )
}

export default TodoApp
```

**Features:**
- ✅ Persist - todos sparas automatiskt
- ✅ DevTools - debug enkelt
- ✅ Filter - visa olika vyer
- ✅ Stats - räkna totalt, aktiva, klara
- ✅ Clean code - välstrukturerad

#### Exempel 2: Data Fetching från API

Hämta användare från ett API:

```javascript
import { create } from 'zustand'

const useUserStore = create((set, get) => ({
  users: [],
  loading: false,
  error: null,
  selectedUser: null,

  // Fetch all users
  fetchUsers: async () => {
    set({ loading: true, error: null })

    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/users')

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const users = await response.json()
      set({ users, loading: false })
    } catch (error) {
      set({ error: error.message, loading: false })
    }
  },

  // Fetch single user
  fetchUser: async (id) => {
    set({ loading: true, error: null })

    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
      const user = await response.json()
      set({ selectedUser: user, loading: false })
    } catch (error) {
      set({ error: error.message, loading: false })
    }
  },

  // Search users
  searchUsers: (query) => {
    const allUsers = get().users
    const filtered = allUsers.filter(user =>
      user.name.toLowerCase().includes(query.toLowerCase())
    )
    return filtered
  }
}))

export default useUserStore
```

**Komponent:**
```javascript
import { useEffect } from 'react'
import useUserStore from './userStore'

function UserList() {
  const { users, loading, error, fetchUsers } = useUserStore()

  useEffect(() => {
    fetchUsers()
  }, [fetchUsers])

  if (loading) return <div>Laddar användare...</div>
  if (error) return <div>Error: {error}</div>

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          <strong>{user.name}</strong>
          <br />
          <small>{user.email}</small>
        </li>
      ))}
    </ul>
  )
}
```

---

### 💡 Pro Tips

#### Tip 1: Structuring Large Stores

För stora appar, dela upp i "slices":

```javascript
// userSlice.js
export const createUserSlice = (set) => ({
  user: null,
  login: (user) => set({ user }),
  logout: () => set({ user: null })
})

// cartSlice.js
export const createCartSlice = (set) => ({
  items: [],
  addItem: (item) => set((state) => ({
    items: [...state.items, item]
  }))
})

// store.js
import { create } from 'zustand'
import { createUserSlice } from './userSlice'
import { createCartSlice } from './cartSlice'

const useStore = create((...a) => ({
  ...createUserSlice(...a),
  ...createCartSlice(...a)
}))
```

#### Tip 2: Reset Store Pattern

Lägg till en reset-funktion:

```javascript
const initialState = {
  count: 0,
  name: '',
  items: []
}

const useStore = create((set) => ({
  ...initialState,

  // Actions
  increment: () => set((state) => ({ count: state.count + 1 })),

  // Reset all state
  reset: () => set(initialState)
}))
```

#### Tip 3: Subscribe Outside React

Du kan använda Zustand utanför React-komponenter!

```javascript
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}))

// Lyssna på förändringar
const unsubscribe = useStore.subscribe(
  (state) => console.log('State changed:', state)
)

// Hämta state direkt
const currentState = useStore.getState()
console.log(currentState.count) // 0

// Uppdatera direkt
useStore.getState().increment()
console.log(useStore.getState().count) // 1

// Avsluta lyssnande
unsubscribe()
```

---

### ✏️ Övningar

#### Övning 3.1: Optimera med Selectors

**Svårighetsgrad:** ⭐⭐⭐
**Tid:** ~15 minuter

**Uppgift:**
Du har en store med användardata. Optimera komponenten så den bara renderas när relevant data ändras.

**Startkod:**
```javascript
const useUserStore = create((set) => ({
  user: {
    name: 'Anna',
    email: 'anna@example.com',
    age: 25,
    preferences: {
      theme: 'dark',
      language: 'sv'
    }
  },
  updateUser: (updates) => set((state) => ({
    user: { ...state.user, ...updates }
  }))
}))

// ❌ Detta renderas om även när preferences ändras!
function UserGreeting() {
  const user = useUserStore((state) => state.user)
  return <h1>Hej, {user.name}!</h1>
}
```

**Uppgift:**
Fixa `UserGreeting` så den bara renderas när `name` ändras.

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const useUserStore = create((set) => ({
  user: {
    name: 'Anna',
    email: 'anna@example.com',
    age: 25,
    preferences: {
      theme: 'dark',
      language: 'sv'
    }
  },
  updateUser: (updates) => set((state) => ({
    user: { ...state.user, ...updates }
  }))
}))

// ✅ Renderas BARA när name ändras
function UserGreeting() {
  const name = useUserStore((state) => state.user.name)
  return <h1>Hej, {name}!</h1>
}

// ✅ Med flera värden - använd shallow
import { shallow } from 'zustand/shallow'

function UserCard() {
  const { name, email } = useUserStore(
    (state) => ({
      name: state.user.name,
      email: state.user.email
    }),
    shallow
  )

  return (
    <div>
      <h2>{name}</h2>
      <p>{email}</p>
    </div>
  )
}
```

**Bonus:** Lägg till console.log för att se när komponenten renderas:
```javascript
function UserGreeting() {
  const name = useUserStore((state) => state.user.name)
  console.log('UserGreeting rendered!')
  return <h1>Hej, {name}!</h1>
}
```

Testa att ändra `preferences.theme` - UserGreeting ska INTE rendera om!

</details>

---

#### Övning 3.2: Async Data Fetching

**Svårighetsgrad:** ⭐⭐⭐
**Tid:** ~20 minuter

**Uppgift:**
Skapa en store som hämtar posts från JSONPlaceholder API.

**Krav:**
- State: `posts`, `loading`, `error`
- Action: `fetchPosts()` - hämtar alla posts
- Action: `fetchPostById(id)` - hämtar en specifik post
- Hantera loading och error states korrekt

**API:**
```
GET https://jsonplaceholder.typicode.com/posts
GET https://jsonplaceholder.typicode.com/posts/1
```

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const usePostStore = create((set) => ({
  posts: [],
  selectedPost: null,
  loading: false,
  error: null,

  fetchPosts: async () => {
    set({ loading: true, error: null })

    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/posts')

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const posts = await response.json()
      set({ posts, loading: false })
    } catch (error) {
      set({ error: error.message, loading: false })
    }
  },

  fetchPostById: async (id) => {
    set({ loading: true, error: null })

    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`)

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const post = await response.json()
      set({ selectedPost: post, loading: false })
    } catch (error) {
      set({ error: error.message, loading: false })
    }
  },

  reset: () => set({ posts: [], selectedPost: null, loading: false, error: null })
}))

// Komponent
function PostList() {
  const { posts, loading, error, fetchPosts } = usePostStore()

  useEffect(() => {
    fetchPosts()
  }, [fetchPosts])

  if (loading) return <div>Laddar posts...</div>
  if (error) return <div>Error: {error}</div>

  return (
    <ul>
      {posts.slice(0, 10).map(post => (
        <li key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.body}</p>
        </li>
      ))}
    </ul>
  )
}
```

**Bonus:** Lägg till caching så att posts inte hämtas om de redan finns:
```javascript
fetchPosts: async () => {
  const state = get()

  // Om vi redan har posts, skippa fetch
  if (state.posts.length > 0) {
    return
  }

  set({ loading: true, error: null })
  // ... resten av koden
}
```

</details>

---

#### Övning 3.3: Persist Middleware

**Svårighetsgrad:** ⭐⭐⭐
**Tid:** ~15 minuter

**Uppgift:**
Skapa en inställningar-store som sparar till localStorage.

**Krav:**
- State: `theme` ('light'/'dark'), `fontSize` (12-24), `notifications` (boolean)
- Actions för att ändra varje setting
- Använd persist middleware
- Spara i localStorage med key 'app-settings'

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

const useSettingsStore = create(
  persist(
    (set) => ({
      theme: 'light',
      fontSize: 16,
      notifications: true,

      setTheme: (theme) => set({ theme }),

      setFontSize: (fontSize) => {
        // Validera att fontSize är mellan 12-24
        if (fontSize >= 12 && fontSize <= 24) {
          set({ fontSize })
        }
      },

      toggleNotifications: () => set((state) => ({
        notifications: !state.notifications
      })),

      resetSettings: () => set({
        theme: 'light',
        fontSize: 16,
        notifications: true
      })
    }),
    {
      name: 'app-settings'
    }
  )
)

// Komponent
function SettingsPanel() {
  const {
    theme,
    fontSize,
    notifications,
    setTheme,
    setFontSize,
    toggleNotifications,
    resetSettings
  } = useSettingsStore()

  return (
    <div>
      <h2>Inställningar</h2>

      <div>
        <label>Tema:</label>
        <select value={theme} onChange={(e) => setTheme(e.target.value)}>
          <option value="light">Ljust</option>
          <option value="dark">Mörkt</option>
        </select>
      </div>

      <div>
        <label>Textstorlek: {fontSize}px</label>
        <input
          type="range"
          min="12"
          max="24"
          value={fontSize}
          onChange={(e) => setFontSize(Number(e.target.value))}
        />
      </div>

      <div>
        <label>
          <input
            type="checkbox"
            checked={notifications}
            onChange={toggleNotifications}
          />
          Aktivera notifikationer
        </label>
      </div>

      <button onClick={resetSettings}>Återställ till standard</button>
    </div>
  )
}

export default SettingsPanel
```

**Testa:**
1. Ändra inställningar
2. Ladda om sidan
3. Inställningarna ska vara kvar!
4. Öppna DevTools > Application > Local Storage
5. Se att 'app-settings' finns där

**Bonus:** Använd `partialize` för att bara spara vissa värden:
```javascript
persist(
  (set) => ({ /* ... */ }),
  {
    name: 'app-settings',
    partialize: (state) => ({
      theme: state.theme,
      fontSize: state.fontSize
      // notifications sparas INTE
    })
  }
)
```

</details>

---

#### Övning 3.4: Derived State

**Svårighetsgrad:** ⭐⭐⭐⭐
**Tid:** ~20 minuter

**Uppgift:**
Skapa en shopping cart med derived state för totalpris, rabatter, etc.

**Krav:**
- State: `items` (array av produkter)
- Varje item: `{ id, name, price, quantity }`
- Actions: `addItem`, `removeItem`, `updateQuantity`
- Derived state (getters):
  - `getSubtotal()` - summa innan rabatt
  - `getDiscount()` - 10% rabatt om subtotal > 500kr
  - `getTotal()` - efter rabatt
  - `getItemCount()` - totalt antal produkter

<details>
<summary>💡 Lösning</summary>

```javascript
import { create } from 'zustand'

const useCartStore = create((set, get) => ({
  items: [],

  // Actions
  addItem: (product) => set((state) => {
    const existing = state.items.find(item => item.id === product.id)

    if (existing) {
      // Öka quantity om produkten redan finns
      return {
        items: state.items.map(item =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        )
      }
    } else {
      // Lägg till ny produkt
      return {
        items: [...state.items, { ...product, quantity: 1 }]
      }
    }
  }),

  removeItem: (productId) => set((state) => ({
    items: state.items.filter(item => item.id !== productId)
  })),

  updateQuantity: (productId, quantity) => set((state) => {
    if (quantity <= 0) {
      // Ta bort om quantity är 0
      return {
        items: state.items.filter(item => item.id !== productId)
      }
    }

    return {
      items: state.items.map(item =>
        item.id === productId
          ? { ...item, quantity }
          : item
      )
    }
  }),

  clearCart: () => set({ items: [] }),

  // Derived state (getters)
  getSubtotal: () => {
    const items = get().items
    return items.reduce((sum, item) => sum + (item.price * item.quantity), 0)
  },

  getDiscount: () => {
    const subtotal = get().getSubtotal()
    // 10% rabatt om subtotal > 500kr
    return subtotal > 500 ? subtotal * 0.1 : 0
  },

  getTotal: () => {
    const subtotal = get().getSubtotal()
    const discount = get().getDiscount()
    return subtotal - discount
  },

  getItemCount: () => {
    const items = get().items
    return items.reduce((sum, item) => sum + item.quantity, 0)
  }
}))

// Komponent
function ShoppingCart() {
  const items = useCartStore((state) => state.items)
  const removeItem = useCartStore((state) => state.removeItem)
  const updateQuantity = useCartStore((state) => state.updateQuantity)
  const clearCart = useCartStore((state) => state.clearCart)

  const getSubtotal = useCartStore((state) => state.getSubtotal)
  const getDiscount = useCartStore((state) => state.getDiscount)
  const getTotal = useCartStore((state) => state.getTotal)
  const getItemCount = useCartStore((state) => state.getItemCount)

  const subtotal = getSubtotal()
  const discount = getDiscount()
  const total = getTotal()
  const itemCount = getItemCount()

  return (
    <div className="cart">
      <h2>Kundvagn ({itemCount} produkter)</h2>

      <ul>
        {items.map(item => (
          <li key={item.id}>
            <span>{item.name}</span>
            <span>{item.price} kr</span>
            <input
              type="number"
              min="0"
              value={item.quantity}
              onChange={(e) => updateQuantity(item.id, Number(e.target.value))}
            />
            <span>{item.price * item.quantity} kr</span>
            <button onClick={() => removeItem(item.id)}>Ta bort</button>
          </li>
        ))}
      </ul>

      <div className="summary">
        <p>Delsumma: {subtotal.toFixed(2)} kr</p>
        {discount > 0 && <p>Rabatt (10%): -{discount.toFixed(2)} kr</p>}
        <h3>Totalt: {total.toFixed(2)} kr</h3>
      </div>

      {items.length > 0 && (
        <button onClick={clearCart}>Töm kundvagn</button>
      )}
    </div>
  )
}

// Exempel på användning
function ProductList() {
  const addItem = useCartStore((state) => state.addItem)

  const products = [
    { id: 1, name: 'T-shirt', price: 199 },
    { id: 2, name: 'Jeans', price: 599 },
    { id: 3, name: 'Skor', price: 899 }
  ]

  return (
    <div>
      <h2>Produkter</h2>
      {products.map(product => (
        <div key={product.id}>
          <span>{product.name} - {product.price} kr</span>
          <button onClick={() => addItem(product)}>Lägg till</button>
        </div>
      ))}
    </div>
  )
}
```

**Vad händer:**
1. Lägg till produkter → subtotal uppdateras
2. När subtotal > 500 kr → 10% rabatt automatiskt!
3. Total räknas alltid korrekt
4. ItemCount visar totalt antal produkter

**Bonus:** Lägg till fraktkostnad (fri frakt över 500kr):
```javascript
getShipping: () => {
  const subtotal = get().getSubtotal()
  return subtotal > 500 ? 0 : 49
},

getFinalTotal: () => {
  return get().getTotal() + get().getShipping()
}
```

</details>

---

### 📝 Sammanfattning

**Du har nu lärt dig:**

✅ **Performance-optimering:**
   - Använd selectors för att undvika onödiga re-renders
   - `shallow` för att jämföra objekt och arrayer
   - Välj bara exakt vad komponenten behöver

✅ **Async operations:**
   - Hantera loading, error och success states
   - Fetch data från API:er
   - AbortController för att avbryta requests

✅ **Derived state:**
   - Beräkna värden från befintlig state
   - Getters i store vs selectors i komponenter
   - Håll store enkel, beräkna i komponenter

✅ **Persist middleware:**
   - Spara state till localStorage automatiskt
   - Partialize för att välja vad som sparas
   - Version och migration för updates

✅ **DevTools middleware:**
   - Debug state-ändringar
   - Time-travel debugging
   - Kombinera med persist

✅ **Best practices:**
   - Dela upp stora stores i slices
   - Reset-pattern för att nollställa state
   - Använd Zustand utanför React med `subscribe` och `getState()`

**Viktiga patterns:**
```javascript
// 1. Optimerad selector
const name = useStore((state) => state.user.name)

// 2. Async action
fetchData: async () => {
  set({ loading: true })
  try {
    const data = await fetch(url)
    set({ data, loading: false })
  } catch (error) {
    set({ error, loading: false })
  }
}

// 3. Persist
create(persist((set) => ({...}), { name: 'storage-key' }))

// 4. Derived state
getTotal: () => get().items.reduce((sum, item) => sum + item.price, 0)
```

---

**Redo för nästa nivå?**

I Nivå 4 lär du dig:
- TypeScript integration
- Custom middleware
- Immer middleware för enklare updates
- Advanced patterns (slice pattern)
- Testing Zustand stores
- React Native användning

Du är nu redo att bygga riktiga produktionsappar med Zustand!

**Projekt att bygga:**
1. **E-commerce cart** med persist, async API-fetch, och derived state
2. **Social media feed** med pagination och caching
3. **Dashboard** med real-time data och filters

---

## Nivå 4: Avancerade Koncept 🚀

**Läsningstid:** ~25 minuter
**Förkunskaper:** Nivå 1-3, TypeScript grundkunskaper (rekommenderat)

### Introduktion

Välkommen till avancerad Zustand! Här lär du dig professionella patterns för produktion:
- TypeScript integration för type-safe stores
- Immer middleware för enklare immutable updates
- Custom middleware
- Slice pattern för stora applikationer
- Testing av Zustand stores
- React Native kompatibilitet

---

### Kärnkoncept

#### 1. TypeScript Integration

**Grundläggande typed store:**
```typescript
import { create } from 'zustand'

interface CounterState {
  count: number
  increment: () => void
  decrement: () => void
  reset: () => void
}

const useCounterStore = create<CounterState>()((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  reset: () => set({ count: 0 })
}))
```

**Med komplexa typer:**
```typescript
interface User {
  id: string
  name: string
  email: string
}

interface Product {
  id: string
  name: string
  price: number
}

interface StoreState {
  user: User | null
  cart: Product[]
  loading: boolean

  setUser: (user: User | null) => void
  addToCart: (product: Product) => void
  removeFromCart: (productId: string) => void
}

const useStore = create<StoreState>()((set) => ({
  user: null,
  cart: [],
  loading: false,

  setUser: (user) => set({ user }),
  addToCart: (product) => set((state) => ({
    cart: [...state.cart, product]
  })),
  removeFromCart: (productId) => set((state) => ({
    cart: state.cart.filter(p => p.id !== productId)
  }))
}))
```

**Med middleware:**
```typescript
import { create } from 'zustand'
import { persist, devtools } from 'zustand/middleware'

interface SettingsState {
  theme: 'light' | 'dark'
  language: 'sv' | 'en'
  setTheme: (theme: 'light' | 'dark') => void
  setLanguage: (language: 'sv' | 'en') => void
}

const useSettingsStore = create<SettingsState>()(
  devtools(
    persist(
      (set) => ({
        theme: 'light',
        language: 'sv',
        setTheme: (theme) => set({ theme }),
        setLanguage: (language) => set({ language })
      }),
      { name: 'settings' }
    )
  )
)
```

#### 2. Immer Middleware

Immer låter dig skriva "mutating" kod som blir immutable:

**Utan Immer (manuell immutability):**
```javascript
addTodo: (text) => set((state) => ({
  todos: [...state.todos, { id: Date.now(), text, done: false }]
}))

toggleTodo: (id) => set((state) => ({
  todos: state.todos.map(todo =>
    todo.id === id ? { ...todo, done: !todo.done } : todo
  )
}))
```

**Med Immer (enklare!):**
```javascript
import { create } from 'zustand'
import { immer } from 'zustand/middleware/immer'

const useTodoStore = create(
  immer((set) => ({
    todos: [],

    addTodo: (text) => set((state) => {
      state.todos.push({ id: Date.now(), text, done: false })
    }),

    toggleTodo: (id) => set((state) => {
      const todo = state.todos.find(t => t.id === id)
      if (todo) {
        todo.done = !todo.done
      }
    })
  }))
)
```

**Fördel:** Kod som ser ut som mutations men är faktiskt immutable!

#### 3. Slice Pattern

För stora appar, dela upp i slices:

```typescript
// slices/userSlice.ts
export interface UserSlice {
  user: User | null
  login: (user: User) => void
  logout: () => void
}

export const createUserSlice: StateCreator<StoreState, [], [], UserSlice> = (set) => ({
  user: null,
  login: (user) => set({ user }),
  logout: () => set({ user: null })
})

// slices/cartSlice.ts
export interface CartSlice {
  items: Product[]
  addItem: (product: Product) => void
  removeItem: (id: string) => void
}

export const createCartSlice: StateCreator<StoreState, [], [], CartSlice> = (set) => ({
  items: [],
  addItem: (product) => set((state) => ({
    items: [...state.items, product]
  })),
  removeItem: (id) => set((state) => ({
    items: state.items.filter(item => item.id !== id)
  }))
})

// store.ts
import { create } from 'zustand'
import { createUserSlice, UserSlice } from './slices/userSlice'
import { createCartSlice, CartSlice } from './slices/cartSlice'

type StoreState = UserSlice & CartSlice

const useStore = create<StoreState>()((...a) => ({
  ...createUserSlice(...a),
  ...createCartSlice(...a)
}))
```

#### 4. Testing Zustand Stores

**Med Vitest/Jest:**
```typescript
import { describe, it, expect, beforeEach } from 'vitest'
import { useCounterStore } from './counterStore'

describe('Counter Store', () => {
  beforeEach(() => {
    // Reset state innan varje test
    useCounterStore.setState({ count: 0 })
  })

  it('should increment count', () => {
    const { increment } = useCounterStore.getState()
    increment()
    expect(useCounterStore.getState().count).toBe(1)
  })

  it('should decrement count', () => {
    useCounterStore.setState({ count: 5 })
    const { decrement } = useCounterStore.getState()
    decrement()
    expect(useCounterStore.getState().count).toBe(4)
  })

  it('should reset count', () => {
    useCounterStore.setState({ count: 10 })
    const { reset } = useCounterStore.getState()
    reset()
    expect(useCounterStore.getState().count).toBe(0)
  })
})
```

**Med React Testing Library:**
```typescript
import { renderHook, act } from '@testing-library/react'
import { useCounterStore } from './counterStore'

it('increments counter', () => {
  const { result } = renderHook(() => useCounterStore())

  act(() => {
    result.current.increment()
  })

  expect(result.current.count).toBe(1)
})
```

#### 5. Custom Middleware

Skapa egna middlewares:

```typescript
import { StateCreator, StoreMutatorIdentifier } from 'zustand'

// Logger middleware
type Logger = <
  T,
  Mps extends [StoreMutatorIdentifier, unknown][] = [],
  Mcs extends [StoreMutatorIdentifier, unknown][] = []
>(
  f: StateCreator<T, Mps, Mcs>,
  name?: string
) => StateCreator<T, Mps, Mcs>

type LoggerImpl = <T>(
  f: StateCreator<T, [], []>,
  name?: string
) => StateCreator<T, [], []>

const loggerImpl: LoggerImpl = (f, name) => (set, get, store) => {
  const loggedSet: typeof set = (...a) => {
    console.log(`[${name || 'Store'}] Previous:`, get())
    set(...a)
    console.log(`[${name || 'Store'}] Next:`, get())
  }
  return f(loggedSet, get, store)
}

export const logger = loggerImpl as Logger

// Användning
const useStore = create(
  logger(
    (set) => ({
      count: 0,
      increment: () => set((state) => ({ count: state.count + 1 }))
    }),
    'CounterStore'
  )
)
```

---

### 📝 Sammanfattning Nivå 4

✅ **TypeScript:** Type-safe stores med interfaces
✅ **Immer:** Enklare immutable updates
✅ **Slice Pattern:** Organisera stora stores
✅ **Testing:** Unit tests och integration tests
✅ **Custom Middleware:** Skapa egna middlewares för cross-cutting concerns

---

## Nivå 5: Expert & Produktion 💎

**Läsningstid:** ~20 minuter
**Förkunskaper:** Alla tidigare nivåer

### Expert Topics

#### 1. Performance Optimization

**Selectors with Memoization:**
```typescript
import { create } from 'zustand'
import { createSelector } from 'reselect'

const useTodoStore = create((set, get) => ({
  todos: [],
  // ...actions
}))

// Memoized selector
const selectCompletedTodos = createSelector(
  (state: TodoState) => state.todos,
  (todos) => todos.filter(todo => todo.done)
)

// I komponent
const completedTodos = useTodoStore(selectCompletedTodos)
```

**Transient Updates (skip re-renders):**
```typescript
const useStore = create((set) => ({
  mouseX: 0,
  mouseY: 0,
  updateMousePosition: (x: number, y: number) =>
    set({ mouseX: x, mouseY: y }, true) // true = skip re-render
}))
```

#### 2. SSR (Next.js Integration)

```typescript
// store.ts
import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export const useStore = create(
  persist(
    (set) => ({
      count: 0,
      increment: () => set((state) => ({ count: state.count + 1 }))
    }),
    {
      name: 'my-store',
      // Skip hydration på server
      skipHydration: true
    }
  )
)

// _app.tsx (Next.js)
import { useStore } from '../store'
import { useEffect } from 'react'

export default function App({ Component, pageProps }) {
  useEffect(() => {
    useStore.persist.rehydrate()
  }, [])

  return <Component {...pageProps} />
}
```

#### 3. React Native

Zustand fungerar perfekt med React Native:

```typescript
import { create } from 'zustand'
import { persist, createJSONStorage } from 'zustand/middleware'
import AsyncStorage from '@react-native-async-storage/async-storage'

const useStore = create(
  persist(
    (set) => ({
      user: null,
      login: (user) => set({ user })
    }),
    {
      name: 'app-storage',
      storage: createJSONStorage(() => AsyncStorage)
    }
  )
)
```

#### 4. Migration från Redux

**Redux:**
```javascript
// Redux approach
const reducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 }
    default:
      return state
  }
}

dispatch({ type: 'INCREMENT' })
```

**Zustand:**
```javascript
// Zustand - mycket enklare!
const useStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}))

increment()
```

**Migration Strategy:**
1. Identifiera Redux slices
2. Konvertera varje slice till Zustand store
3. Ersätt `useSelector` med Zustand hooks
4. Ta bort Redux boilerplate steg för steg

---

### 📝 Sammanfattning Nivå 5

✅ **Performance:** Memoization, transient updates
✅ **SSR:** Next.js integration med hydration
✅ **React Native:** AsyncStorage integration
✅ **Migration:** Från Redux till Zustand

---

## 🎓 Slutlig Självutvärdering

### Efter Nivå 1
- [ ] Förklara state management med egna ord
- [ ] Ge exempel på delad information i verkliga livet

### Efter Nivå 2
- [ ] Skapa en enkel Zustand store
- [ ] Använda state i React-komponenter
- [ ] Uppdatera state med actions

### Efter Nivå 3
- [ ] Optimera med selectors
- [ ] Hämta data från API:er (async)
- [ ] Använda persist middleware
- [ ] Debugga med DevTools

### Efter Nivå 4
- [ ] Skapa type-safe stores med TypeScript
- [ ] Använda Immer för enklare updates
- [ ] Implementera slice pattern
- [ ] Testa stores med Vitest/Jest

### Efter Nivå 5
- [ ] Optimera performance
- [ ] Integrera med Next.js (SSR)
- [ ] Använda i React Native
- [ ] Migrera från Redux

---

## 📖 Ordlista

**Action:** Funktion som ändrar state
**Derived State:** Beräknade värden från state
**DevTools:** Debug-verktyg för att inspektera state
**Hook:** React-funktion som börjar med "use"
**Immer:** Library för enklare immutable updates
**Immutable:** Data som inte kan ändras direkt
**Middleware:** Funktion som wrapprar store-logik
**Persist:** Spara state till localStorage/AsyncStorage
**Selector:** Funktion för att välja ut specifik data
**Shallow:** Jämföra objekts properties istället för referens
**Slice:** Del av en större store
**State:** Information/tillstånd som kan ändras
**Store:** Platsen där all state finns
**Subscription:** Lyssna på state-ändringar
**Transient Update:** Uppdatering utan re-render

---

## 🆚 Zustand vs Andra Lösningar

| Feature | Zustand | Redux Toolkit | Context API | Recoil | Jotai |
|---------|---------|---------------|-------------|--------|-------|
| **Bundle Size** | ~1KB | ~12KB | 0KB | ~21KB | ~3KB |
| **Boilerplate** | Minimal | Medel | Låg | Medel | Minimal |
| **Learning Curve** | ⭐ Lätt | ⭐⭐⭐ Medel | ⭐⭐ Lätt | ⭐⭐⭐ Medel | ⭐⭐ Lätt |
| **TypeScript** | ✅ Excellent | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent |
| **DevTools** | ✅ Via middleware | ✅ Built-in | ❌ Nej | ✅ Separat | ✅ Via plugin |
| **Persistence** | ✅ Via middleware | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual | ✅ Via plugin |
| **Async Actions** | ✅ Native | ✅ Thunks | ⚠️ Manual | ✅ Native | ✅ Native |
| **Performance** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Provider Needed** | ❌ Nej | ✅ Ja | ✅ Ja | ✅ Ja | ❌ Nej |
| **Atomicity** | ❌ Store-based | ❌ Store-based | ❌ Context-based | ✅ Atom-based | ✅ Atom-based |
| **Community** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

**När använda vad:**
- **Zustand:** De flesta moderna React-appar, snabb setup, bra performance
- **Redux Toolkit:** Mycket stora appar, behöver Redux DevTools ekosystem
- **Context API:** Mycket små appar, bara props-drilling problem
- **Recoil:** Experimentella features, behöver atomicity
- **Jotai:** Atomic state management, minimalistisk approach

---

## 🔄 Migreringsguider

### Från Context API till Zustand

**Innan (Context API):**
```javascript
const UserContext = createContext()

function UserProvider({ children }) {
  const [user, setUser] = useState(null)

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  )
}

// I App.js
<UserProvider>
  <App />
</UserProvider>

// I komponenter
const { user, setUser } = useContext(UserContext)
```

**Efter (Zustand):**
```javascript
const useUserStore = create((set) => ({
  user: null,
  setUser: (user) => set({ user })
}))

// Ingen provider behövs!

// I komponenter
const { user, setUser } = useUserStore()
```

### Från Redux till Zustand

**Innan (Redux):**
```javascript
// actions.js
export const increment = () => ({ type: 'INCREMENT' })

// reducer.js
export default function counterReducer(state = { count: 0 }, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { ...state, count: state.count + 1 }
    default:
      return state
  }
}

// store.js
const store = createStore(counterReducer)

// Komponenter
const count = useSelector((state) => state.count)
const dispatch = useDispatch()
dispatch(increment())
```

**Efter (Zustand):**
```javascript
// store.js
const useCounterStore = create((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 }))
}))

// Komponenter
const { count, increment } = useCounterStore()
increment()
```

---

## 🔗 Resurser för Fördjupning

### Officiell Dokumentation
- [Zustand GitHub](https://github.com/pmndrs/zustand)
- [Zustand Docs](https://docs.pmnd.rs/zustand/getting-started/introduction)

### Kurser & Tutorials
- [React State Management with Zustand](https://egghead.io/courses/zustand)
- [Zustand Crash Course - YouTube](https://www.youtube.com/results?search_query=zustand+crash+course)

### Artiklar
- [Why Zustand is Better Than Context](https://tkdodo.eu/blog/zustand-and-react-context)
- [Zustand Best Practices](https://tkdodo.eu/blog/working-with-zustand)

### Communities
- [Poimandres Discord](https://discord.gg/poimandres)
- [React Subreddit](https://reddit.com/r/reactjs)

---

## ❓ Vanliga Frågor (FAQ)

**1. Behöver jag en Provider?**
Nej! Till skillnad från Context API och Redux behöver Zustand ingen provider.

**2. Kan jag använda flera stores?**
Ja! Det är ofta bättre att ha flera små stores än en gigantisk.

**3. Fungerar Zustand med React Native?**
Ja, perfekt! Använd AsyncStorage istället för localStorage.

**4. Hur debuggar jag min store?**
Använd devtools middleware och Redux DevTools extension.

**5. Kan jag använda Zustand utanför React?**
Ja! `useStore.getState()` och `useStore.subscribe()` fungerar överallt.

**6. Ska jag använda Immer?**
Om du har komplexa nested updates - ja! Annars är vanilla Zustand bra.

**7. Hur testar jag Zustand stores?**
Använd `getState()` och `setState()` direkt i tests.

**8. Vad är skillnaden mellan Zustand och Jotai?**
Zustand = store-based, Jotai = atom-based. Zustand enklare för de flesta.

**9. Kan jag migrera gradvis från Redux?**
Ja! Båda kan köras samtidigt under migration.

**10. Hur optimerar jag performance?**
Använd selectors, shallow comparison, och transient updates vid behov.

**11. Fungerar det med Next.js?**
Ja, men använd `skipHydration: true` för SSR.

**12. Kan jag kombinera flera middlewares?**
Ja! Wrappa i rätt ordning: devtools(persist(immer(store))).

**13. Hur stor kan min store vara?**
Så stor som behövs! Men överväg att dela upp i slices för bättre organization.

**14. Behöver jag TypeScript?**
Nej, men det ger utmärkt type-safety och autocomplete.

**15. Vad är "shallow" comparison?**
Jämför objekts properties istället för object reference.

**16. Hur persist:ar jag bara vissa värden?**
Använd `partialize` option i persist middleware.

**17. Kan jag använda class components?**
Ja, men hooks är rekommenderat. Använd subscribe för class components.

**18. Hur hanterar jag errors i async actions?**
Använd try-catch och spara error i state.

**19. Vad är transient updates?**
Updates som inte triggar re-renders: `set(state, true)`.

**20. Hur återställer jag hela storen?**
Skapa en reset-funktion som sätter tillbaka till initialState.

---

## 🎉 Grattis!

Du har nu genomfört hela Zustand-guiden från nybörjare till expert!

**Vad du kan nu:**
✅ Förstå state management koncept
✅ Skapa och använda Zustand stores
✅ Optimera performance
✅ Hantera async data
✅ Integrera med TypeScript
✅ Testa dina stores
✅ Bygga produktionsklara applikationer

**Nästa steg:**
1. Bygg ett riktigt projekt med Zustand
2. Experimentera med middleware
3. Bidra till open source-projekt som använder Zustand
4. Dela dina lärdomar med andra!

**Lycka till med din Zustand-resa! 🚀**

---

*Guide skapad 2024-11-17 | Version 1.0*

