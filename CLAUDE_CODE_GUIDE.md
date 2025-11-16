# Den Ultimata Claude Code Guiden - Från Nybörjare till Proffs

## Innehållsförteckning
1. [Introduktion - Vad är Claude Code?](#introduktion)
2. [Installation och Initial Uppsättning](#installation)
3. [Grundläggande Koncept och Terminologi](#grundläggande-koncept)
4. [Din Första Webb-App med Claude Code](#första-appen)
5. [CLAUDE.md - Hjärtat i Ditt Projekt](#claude-md)
6. [Kontexthantering - Den Viktigaste Färdigheten](#kontexthantering)
7. [Arbetsflöden för Professionell Utveckling](#arbetsflöden)
8. [Avancerade Tekniker](#avancerade-tekniker)
9. [Best Practices för Långsiktig Framgång](#best-practices)
10. [Felsökning och Vanliga Problem](#felsökning)

---

## 1. Introduktion - Vad är Claude Code? {#introduktion}

### Vad är det?
Claude Code är ett kommandoradsverktyg (CLI) för AI-assisterad kodning. Det är som att ha en expert-programmerare som kollega som kan:
- Skriva och redigera kod
- Söka igenom din kodbas
- Köra kommandon och tester
- Skapa och hantera Git-commits
- Förklara kod och arkitektur
- Debugga problem

### Varför använda Claude Code?
- **Produktivitetsökning**: 10-30% snabbare utveckling med rätt arbetssätt
- **Lärverktyg**: Lär dig best practices genom att observera Claude
- **Kodkvalitet**: Konsekvent stil och vältestad kod
- **Dokumentation**: Automatisk generering och uppdatering

### Vad du behöver veta innan du börjar
- **Grundläggande terminologi**:
  - **CLI (Command Line Interface)**: Textbaserat gränssnitt för att köra kommandon
  - **Kontext**: Information som Claude har tillgång till när den svarar
  - **Repository/Repo**: En mapp med kod hanterad av Git
  - **Kodbas**: All kod i ditt projekt

---

## 2. Installation och Initial Uppsättning {#installation}

### Steg 1: Installera Claude Code

**På macOS/Linux:**
```bash
# Installera via npm (kräver Node.js)
npm install -g @anthropic-ai/claude-code

# Eller via Homebrew (macOS)
brew install anthropic/tap/claude-code
```

**På Windows:**
```bash
# Via npm
npm install -g @anthropic-ai/claude-code
```

### Steg 2: Autentisering

```bash
# Starta Claude och följ autentiseringsinstruktionerna
claude

# Du kommer att få en länk - öppna den i webbläsaren och logga in
```

### Steg 3: Verifiera Installation

```bash
# Kör detta för att se version och bekräfta installation
claude --version

# Öppna hjälpdokumentationen
claude --help
```

### Steg 4: Grundläggande Konfiguration

```bash
# Skapa global konfigurationsfil
mkdir -p ~/.claude
touch ~/.claude/CLAUDE.md

# Detta är din globala konfiguration som gäller för alla projekt
```

**Lägg till i ~/.claude/CLAUDE.md:**
```markdown
# Mina Globala Preferenser

## Kodstil
- Använd alltid 2 mellanslag för indrag
- Föredra funktionella komponenter i React
- Skriv beskrivande variabelnamn på engelska

## Arbetsflöde
- Kör alltid tester innan commit
- Skriv tydliga commit-meddelanden
- Använd TypeScript när det är möjligt
```

---

## 3. Grundläggande Koncept och Terminologi {#grundläggande-koncept}

### Kontextfönster
**Vad är det?**
Kontextfönstret är som Claudes arbetsminne. Det innehåller:
- Din konversationshistorik
- Filer som Claude har läst
- Kommandon som körts
- CLAUDE.md innehåll

**Varför är det viktigt?**
- Begränsad storlek (som RAM i en dator)
- Ju mer i kontexten, desto dyrare och långsammare
- För mycket kontext = Claude glömmer viktiga detaljer

**Praktiskt exempel:**
```
Tänk dig kontexten som en whiteboard:
- I början: Tom och snabb
- Efter 10 minuter: Några anteckningar, lätt att överblicka
- Efter 1 timme: Full av information, svårt att hitta det viktiga
- Lösning: Torka tavlan (/clear) och börja om med fokuserad information
```

### Agentiskt Arbete
**Vad innebär "agentisk"?**
Claude arbetar inte bara reaktivt (svarar på frågor), utan kan:
1. Planera flera steg framåt
2. Söka efter information själv
3. Köra kommandon och verktyg
4. Iterera baserat på resultat

**Exempel på agentiskt arbete:**
```
Du: "Implementera användarautentisering"

Claude gör automatiskt:
1. Söker igenom projektet efter befintlig auth-kod
2. Läser relevanta filer
3. Skapar en implementationsplan
4. Skriver kod steg för steg
5. Skriver tester
6. Verifierar att allt fungerar
```

### Verktyg och Permissions
Claude kan använda olika verktyg:
- **Read**: Läsa filer
- **Write**: Skriva nya filer
- **Edit**: Redigera befintliga filer
- **Bash**: Köra terminalkommandon
- **Grep/Glob**: Söka i kod

**Hantera permissions:**
```bash
# Se nuvarande permissions
/permissions

# Under sessionen: Välj "Always allow" för verktyg du litar på
```

---

## 4. Din Första Webb-App med Claude Code {#första-appen}

Låt oss bygga en enkel TODO-app från grunden för att lära oss arbetsflödet.

### Steg 1: Projektinitiering

```bash
# Skapa projektmapp
mkdir min-todo-app
cd min-todo-app

# Starta Claude i projektmappen
claude
```

### Steg 2: Din Första Prompt

**Vad du ska säga till Claude:**
```
Jag vill skapa en TODO-app med följande specifikation:

TEKNISK STACK:
- React med TypeScript
- Vite som build-verktyg
- Tailwind CSS för styling
- LocalStorage för data-persistens

FUNKTIONALITET:
- Lägga till nya todos
- Markera som klara
- Ta bort todos
- Filter: Alla, Aktiva, Klara

Innan du börjar koda:
1. Skapa en projektplan
2. Visa mig mappstrukturen du rekommenderar
3. Vänta på mitt godkännande innan implementation
```

**Varför denna prompt är bra:**
- ✅ Specifik om teknisk stack
- ✅ Tydlig funktionalitet
- ✅ Ber om plan först (inte direkt implementation)
- ✅ Väntar på godkännande

### Steg 3: Granska Planen

Claude kommer presentera en plan. **VIKTIGT: Läs igenom den!**

**Exempel på vad Claude kan föreslå:**
```
📁 min-todo-app/
├── 📁 src/
│   ├── 📁 components/
│   │   ├── TodoItem.tsx
│   │   ├── TodoList.tsx
│   │   ├── TodoInput.tsx
│   │   └── FilterButtons.tsx
│   ├── 📁 hooks/
│   │   └── useTodos.ts
│   ├── 📁 types/
│   │   └── todo.ts
│   ├── App.tsx
│   └── main.tsx
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

**Din respons:**
```
Planen ser bra ut! Några ändringar:
- Lägg till en utils/ mapp för localStorage-funktioner
- Jag vill också ha en types/ för TypeScript-typer

Fortsätt med implementationen.
```

### Steg 4: Implementation

Claude börjar nu skapa filer. **Observera arbetsflödet:**

```
Claude kommer att:
1. Skriva package.json
2. Skapa tsconfig.json
3. Sätta upp Vite
4. Installera dependencies
5. Skapa komponenterna en i taget
6. Skriva tester (om du ber om det)
```

**Under implementationen - Bra vanor:**
```bash
# Var inte rädd för att avbryta och ställa frågor:
"Kan du förklara varför du använder useCallback här?"

# Be om ändringar:
"Kan du refaktorera TodoItem till en mindre komponent?"

# Tryck ESC för att avbryta om Claude gör något fel
```

### Steg 5: Testa Appen

```
Du: "Starta utvecklingsservern och visa mig hur jag testar appen"

Claude kommer:
1. Köra: npm install
2. Köra: npm run dev
3. Ge dig URL (vanligtvis http://localhost:5173)
4. Instruktioner för att testa funktionalitet
```

### Steg 6: Din Första Context Clear

**VIKTIGT ÖGONBLICK:**
Efter att appen fungerar, gör detta:

```bash
/clear
```

**Varför?**
- Du har nu massa kontext från hela implementationen
- Nästa steg (t.ex. lägga till features) behöver inte all denna historik
- Spara pengar och förbättra prestanda

**Efter /clear, dokumentera:**
```
Du: "Läs igenom projektet och skapa en CLAUDE.md fil som dokumenterar:
- Projektets syfte
- Hur man kör appen
- Mappstruktur
- Vanliga kommandon"
```

### Steg 7: Lägg till en Feature (Learning by Doing)

**Nu testar vi Test-Driven Development (TDD):**

```
Du: "Jag vill lägga till en funktion för att redigera befintliga todos.

Använd TDD-approach:
1. Skriv tester först
2. Kör testerna (de ska faila)
3. Implementera funktionalitet
4. Verifiera att testerna passar

Vänta på mitt godkännande mellan varje steg."
```

**Vad du lär dig:**
- TDD workflow
- Hur man läser och förstår tester
- Iterativ utveckling
- Separation of concerns

---

## 5. CLAUDE.md - Hjärtat i Ditt Projekt {#claude-md}

### Vad är CLAUDE.md?

**Enkel förklaring:**
CLAUDE.md är som en "instruktionsmanual" som Claude automatiskt läser varje gång ni interagerar. Det är som att ge Claude ett cheat sheet för ditt projekt.

### Varför är det viktigt?

**Utan CLAUDE.md:**
```
Du: "Lägg till en ny API-endpoint för användare"
Claude: *Gissar arkitektur, kan använda fel mönster*
```

**Med CLAUDE.md:**
```
Du: "Lägg till en ny API-endpoint för användare"
Claude: *Läser CLAUDE.md, ser att du använder Express + TypeScript
        med en specifik mappstruktur, följer dina conventions*
```

### Var ska CLAUDE.md filer placeras?

**1. Projektroot (viktigast):**
```
📁 min-todo-app/
├── CLAUDE.md          # ← Projektspecifik konfiguration
├── src/
└── package.json
```

**2. Hemkatalog (global):**
```
~/.claude/CLAUDE.md    # ← Dina personliga preferenser för alla projekt
```

**3. Per-mapp (för stora projekt):**
```
📁 min-todo-app/
├── CLAUDE.md          # Övergripande projektinfo
├── 📁 src/
│   └── CLAUDE.md      # Specifikt för source code
└── 📁 tests/
    └── CLAUDE.md      # Test-specifika instruktioner
```

### Struktur av en Bra CLAUDE.md

**Mall för en ny webb-app:**

```markdown
# [Projektnamn]

## Översikt
[1-2 meningar om vad projektet gör]

## Teknisk Stack
- Frontend: React 18 + TypeScript
- Styling: Tailwind CSS
- State Management: Zustand
- Build Tool: Vite
- Testing: Vitest + React Testing Library

## Mappstruktur
```
src/
├── components/     # React komponenter
├── hooks/          # Custom React hooks
├── stores/         # Zustand stores
├── utils/          # Hjälpfunktioner
├── types/          # TypeScript types
└── api/            # API client kod
```

## Kodstil och Konventioner

### Namngivning
- Komponenter: PascalCase (TodoItem.tsx)
- Hooks: camelCase med 'use' prefix (useTodos.ts)
- Utilities: camelCase (formatDate.ts)
- Types: PascalCase (User, TodoItem)

### React Best Practices
- ANVÄND funktionella komponenter, INTE class components
- Föredra hooks framför HOCs
- Håll komponenter små (under 200 rader)
- Separera logik i custom hooks

### TypeScript
- Undvik 'any' - använd 'unknown' om typ är osäker
- Definiera interfaces för alla objekt
- Exportera types från types/ mappen

## Testning

### Kör Tester
```bash
npm run test          # Kör alla tester
npm run test:watch    # Watch mode
npm run test:coverage # Med coverage report
```

### Test Konventioner
- En testfil per komponent: Component.test.tsx
- Använd describe/it struktur
- Testa användarbeteende, inte implementation

## Vanliga Kommandon

```bash
npm run dev          # Starta dev server
npm run build        # Bygg för production
npm run preview      # Preview production build
npm run lint         # Kör ESLint
npm run type-check   # TypeScript type checking
```

## Git Workflow
- Använd conventional commits: feat:, fix:, docs:, etc.
- Skapa feature branches: feature/user-authentication
- Kör tester innan commit

## VIKTIGA REGLER
- KÖR ALLTID tester innan du committar
- ANVÄND ALDRIG 'any' i TypeScript utan stark motivering
- DOKUMENTERA alla publika API:er med JSDoc
- FÖLJ befintlig kod-stil - konsistens är viktigt
```

### Exempel: CLAUDE.md för Olika Projekttyper

**Backend API (Node.js + Express):**
```markdown
# API Server - User Management

## Stack
- Node.js 20 + TypeScript
- Express.js
- PostgreSQL med Prisma ORM
- JWT för authentication
- Jest för testing

## Mappstruktur
```
src/
├── routes/         # Express routes
├── controllers/    # Request handlers
├── services/       # Business logic
├── models/         # Prisma models
├── middleware/     # Express middleware
└── utils/          # Hjälpfunktioner
```

## Database
```bash
npx prisma migrate dev    # Skapa ny migration
npx prisma studio         # Öppna DB GUI
```

## API Konventioner
- REST endpoints: /api/v1/resource
- Plurala substantiv: /users, /posts
- HTTP metoder: GET, POST, PUT, DELETE
- Response format: JSON med { data, error, message }

## Error Handling
- Använd custom Error klasser från utils/errors.ts
- Alltid catch async errors med asyncHandler
- Returnera rätt HTTP status codes

## VIKTIGT
- VALIDERA all input med Zod schemas
- ANVÄND prepared statements (Prisma gör detta automatiskt)
- LOGGA alla errors med logger.error()
```

**Full-Stack Next.js App:**
```markdown
# E-commerce Platform

## Stack
- Next.js 14 (App Router)
- TypeScript
- Prisma + PostgreSQL
- NextAuth.js
- Stripe för betalningar
- Tailwind CSS

## Mappstruktur (App Router)
```
app/
├── (auth)/         # Auth related pages
├── (shop)/         # Shopping pages
├── api/            # API routes
└── components/     # Shared components
```

## Routing Konventioner
- Server Components by default
- 'use client' endast när nödvändigt
- Server Actions för mutations

## Data Fetching
- Server Components: Direct Prisma calls
- Client Components: API routes eller React Query

## Authentication
```bash
# Env vars krävs:
NEXTAUTH_SECRET=
NEXTAUTH_URL=
DATABASE_URL=
```

## KRITISKA SÄKERHETSREGLER
- EXPONERA ALDRIG API keys till klienten
- VALIDERA användare server-side för alla mutations
- SANITERA all user input
- ANVÄND CSRF protection (NextAuth gör detta)
```

### Hur Man Förbättrar sin CLAUDE.md

**Iterativ Process:**

1. **Börja enkelt:**
```markdown
# Min App
- React + TypeScript
- Kör: npm run dev
```

2. **Lägg till efter behov:**
Efter första veckan, när Claude gör fel:
```markdown
# Min App
- React + TypeScript
- Kör: npm run dev

## VIKTIGT
- Använd funktionella komponenter (Claude skapade en class component)
```

3. **Använd #-tangenten:**
```
Du: # (tryck på tangenten i Claude)

Claude: "Jag noterade att du föredrar:
- Funktionella komponenter
- 2 spaces indentation
- Named exports

Ska jag lägga till detta i CLAUDE.md?"
```

4. **Förfina med betoning:**
```markdown
## KRITISKA REGLER
- **DU MÅSTE** köra tester innan commit
- **ANVÄND ALLTID** TypeScript strict mode
- **UNDVIK** any type
```

### Common Pitfalls (Vanliga Misstag)

**❌ För lång CLAUDE.md (över 300 rader):**
```
Problem: Claude kan missa viktiga detaljer
Lösning: Dela upp i flera filer per mapp
```

**❌ För vag information:**
```markdown
❌ "Skriv bra kod"
✅ "Använd funktionella komponenter med TypeScript interfaces"

❌ "Testa din kod"
✅ "Kör 'npm test' innan varje commit. Alla tester måste passa."
```

**❌ Glömmer uppdatera:**
```
Problem: CLAUDE.md säger "använd Jest" men projektet bytte till Vitest
Lösning: Uppdatera CLAUDE.md när du ändrar dependencies eller conventions
```

### Tips för Optimering

**Använd Emojis för Visuell Hierarki:**
```markdown
## 🚀 Snabbstart
## ⚙️ Konfiguration
## 🧪 Testning
## 🔒 Säkerhet
## ⚠️ VIKTIGA REGLER
```

**Inkludera Exempel:**
```markdown
## Skapa en Ny Component

```typescript
// ✅ Bra
export const UserCard: React.FC<UserCardProps> = ({ user }) => {
  return <div>{user.name}</div>
}

// ❌ Undvik
export default function(props) {
  return <div>{props.user.name}</div>
}
```
```

**Länka till Externa Resurser:**
```markdown
## Coding Standards
Följ [Airbnb React Style Guide](https://airbnb.io/javascript/react/)

## API Design
Följ [RESTful API Guidelines](./docs/api-guidelines.md)
```

---

## 6. Kontexthantering - Den Viktigaste Färdigheten {#kontexthantering}

### Varför är Kontexthantering Så Viktig?

**The Reality Check (från Shuttle.dev):**
> "The real test isn't whether Claude Code works well on day one with a small codebase - it will. The test is whether it still delivers accurate, useful results six months later when your project has grown ten times larger."

**Problemet:**
- Långa konversationer = Claude glömmer projektregler
- Massa "noise" i kontexten
- Dyrare att köra
- Snabbare förbrukad användargräns

### The Golden Rule: Clear Early, Clear Often

**Muscle Memory Regel:**
```
Efter 1-3 meddelanden om en specifik uppgift → /clear
```

**Praktiskt Exempel:**

```
# Session Start
Du: "Fixa buggen i LoginForm där validation inte fungerar"
Claude: [läser filer, fixar, testar]
Du: "Perfekt!"

/clear   ← GÖR DETTA NU!

Du: "Nu vill jag lägga till lösenordsåterställning"
Claude: [börjar med färsk kontext]
```

### När Ska Man Använda /clear?

**✅ Clearar Kontext Efter:**
1. Slutförd feature implementation
2. Buggfix som är löst och testad
3. Dokumentation skriven
4. Innan du byter fokus (från frontend till backend)
5. När Claude börjar ge irrelevanta svar

**❌ Cleara INTE när:**
1. Mitt i en debug-session
2. När du behöver kontexten från tidigare svar
3. När du ber Claude iterera på nyskriven kod

### Kontexthantering Strategier

#### Strategi 1: Task-Based Clearing

**Koncept:** Clear efter varje avslutad task

```
Task 1: Implementera User Authentication
- Skapa auth komponenter
- Testa
- Commit
/clear ← CLEAR HÄR

Task 2: Add Product Catalog
- Skapa product komponenter
- Testa
- Commit
/clear ← CLEAR HÄR
```

#### Strategi 2: File-Based Context

**Koncept:** Be Claude bara läsa det som behövs

**❌ Dåligt:**
```
Du: "Fixa LoginForm"
Claude: *Läser alla komponenter i projektet*
```

**✅ Bra:**
```
Du: "Läs endast src/components/LoginForm.tsx och
     src/hooks/useAuth.ts. Fixa validation-buggen."

Claude: *Läser bara dessa 2 filer*
```

#### Strategi 3: "Exploration → Plan → Clear → Code"

**Bästa Practice för Nya Features:**

```
# Steg 1: Exploration (inga ändringar)
Du: "Jag vill lägga till dark mode. Utforska projektet och
     berätta hur styling är uppbyggd idag. GÖR INGA ÄNDRINGAR."

Claude: [läser theme-filer, styling approach, etc.]
Claude: "Ni använder Tailwind med CSS variables..."

# Steg 2: Plan
Du: "Baserat på detta, skapa en plan för dark mode implementation"
Claude: [presenterar plan med steg]

# Steg 3: CLEAR!
/clear

# Steg 4: Code (med plan i minnet)
Du: "Implementera dark mode enligt planen vi diskuterade.
     Planen finns i project-docs/dark-mode-plan.md"

Claude: [läser planen, implementerar]
```

**Varför detta fungerar:**
- Exploration-fasen genererar mycket kontext
- Planen dokumenteras (persistence utanför kontext)
- Implementation börjar med färsk, fokuserad kontext

### Avancerad Kontexthantering

#### Multiple Claude Instances

**När att använda:**
- Stora refactorings
- Parallel development
- Code review samtidigt som utveckling

**Setup:**
```bash
# Terminal 1: Feature Development
cd ~/project
claude
> Implementera user dashboard

# Terminal 2: Testing/Review
cd ~/project
claude
> Granska koden i src/dashboard och skriv tester
```

**Best Practices:**
- Namnge terminal-fönster tydligt
- En instance per isolerad task
- Använd olika git worktrees om möjligt

#### Context Dokumentation Pattern

**Koncept:** Dokumentera beslut innan clear

```
# Efter en längre diskussion om arkitektur
Du: "Innan vi clearer kontext, skapa en fil
     docs/decisions/001-state-management.md
     som sammanfattar varför vi valde Zustand över Redux"

Claude: [skapar dokumentation]

/clear

# Nu kan du referera till dokumentet senare
Du: "Läs docs/decisions/001-state-management.md och
     implementera första storen"
```

### Context-Saving Tekniker

#### Teknik 1: Progressive File Reading

**❌ Waste Context:**
```
Du: "Läs alla filer i src/ och fixa type errors"
Claude: *Läser 50 filer, hittar errors i 3*
```

**✅ Save Context:**
```
Du: "Kör TypeScript type check och visa mig resultaten"
Claude: *Kör tsc, visar errors*

Du: "Läs endast de filer som har errors och fixa dem"
Claude: *Läser bara 3 filer*
```

#### Teknik 2: Incremental Exploration

**För stora kodбaser:**

```
# Istället för: "Förklara hela projektet"

# Gör:
Du: "Beskriv mappstrukturen på top-level"
Claude: [listar mappar med kort beskrivning]

Du: "Nu, beskriv vad som finns i src/features/"
Claude: [djupare i features]

# Clear och fortsätt vid behov
```

#### Teknik 3: Summary Extraction

**Efter en lång session:**

```
Du: "Sammanfatta allt vi implementerat denna session i en
     bullet-point lista och spara i CHANGELOG.md"

Claude: [skapar sammanfattning]

/clear

# Nu har du dokumentation istället för lång context history
```

### Mäta och Optimera Kontext-användning

**Tecken på att du behöver cleara:**
1. Claude börjar repetera sig
2. Svarstider blir längre
3. Claude ignorerar instruktioner i CLAUDE.md
4. Kostnaderna ökar märkbart
5. Claude nämner irrelevant information från tidigare

**Experimentera:**
```
Vecka 1: Clear efter varje task → Mät produktivitet
Vecka 2: Clear var 3:e task → Jämför
Vecka 3: Sällan clear → Jämför

Hitta din sweet spot!
```

---

## 7. Arbetsflöden för Professionell Utveckling {#arbetsflöden}

### Workflow 1: Test-Driven Development (TDD)

**Varför TDD med Claude?**
- Förhindrar "mock implementations" (fake kod som bara får tester att passa)
- Garanterar faktisk funktionalitet
- Bättre kodkvalitet
- Dokumentation via tester

**Steg-för-Steg TDD Workflow:**

```
# Steg 1: Definiera Feature med Exempel
Du: "Jag vill skapa en funktion som validerar email-adresser.

Förväntade input/output:
- validateEmail('test@example.com') → true
- validateEmail('invalid.email') → false
- validateEmail('missing@domain') → false
- validateEmail('') → false

Använd TDD: Skriv tester först baserat på dessa exempel.
VÄNTA på mitt godkännande innan implementation."
```

```
# Steg 2: Claude Skriver Tester
Claude: [skapar test fil]

// validateEmail.test.ts
describe('validateEmail', () => {
  it('should return true for valid email', () => {
    expect(validateEmail('test@example.com')).toBe(true)
  })

  it('should return false for missing @', () => {
    expect(validateEmail('invalid.email')).toBe(false)
  })

  // ... fler tester
})
```

```
# Steg 3: Verifiera Att Tester Failar
Du: "Kör testerna och visa att de failar"

Claude:
$ npm test
❌ validateEmail is not defined
```

```
# Steg 4: Commit Testerna
Du: "Commita testerna"

Claude:
$ git add validateEmail.test.ts
$ git commit -m "test: add email validation tests"
```

```
# Steg 5: Implementation
Du: "Implementera validateEmail för att få testerna att passa"

Claude: [skriver implementation]

// validateEmail.ts
export function validateEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}
```

```
# Steg 6: Verifiera
Du: "Kör testerna igen"

Claude:
$ npm test
✅ All tests passed
```

```
# Steg 7: Review med Sub-agent
Du: "Använd en subagent för att granska implementationen och
     verifiera att koden inte är overfit till testerna"

Claude: [startar review-agent]
Agent: "Implementation ser bra ut. Regex täcker edge cases
        och är inte hårdkodad för specifika test cases."
```

```
# Steg 8: Commit Implementation
Du: "Commita implementation"

Claude:
$ git commit -m "feat: implement email validation"
```

**TDD Best Practices:**
- ✅ Skriv minst 3-5 test cases
- ✅ Inkludera edge cases
- ✅ Testa både valid och invalid input
- ✅ Commit tester separat från implementation
- ❌ Låt inte Claude skriva tester och implementation samtidigt

### Workflow 2: Visual Iteration (UI Development)

**För Frontend-utveckling:**

**Setup (En gång per projekt):**

```bash
# Installera Puppeteer MCP för screenshots
npm install -g @anthropic-ai/mcp-puppeteer

# Eller använd mobil-simulator
# Eller ta manuella screenshots
```

**Steg-för-Steg Visual Workflow:**

```
# Steg 1: Ge Visual Reference
Du: "Jag har en design för en landing page. Här är mockupen:
     [bifoga bild eller drag-drop]

     Implementera denna sida med React + Tailwind.
     VÄNTA med att börja tills du bekräftat att du ser bilden."

Claude: "Jag ser designen. Det är en hero-section med CTA-knapp,
         följt av en 3-kolumns feature-grid..."
```

```
# Steg 2: Implementation
Claude: [skapar komponenter]
```

```
# Steg 3: Visual Comparison
Du: "Starta dev servern och ta en screenshot av resultatet"

Claude:
$ npm run dev
[tar screenshot via Puppeteer]
[visar dig screenshot]
```

```
# Steg 4: Iterera
Du: "Bra start! Justeringar:
     - Hero heading ska vara större (text-6xl)
     - CTA-knappen ska ha mer padding
     - Feature cards ska ha subtle shadow"

Claude: [gör ändringar, tar ny screenshot]
```

```
# Steg 5: Final Check
Du: "Ta en sida-vid-sida jämförelse: designen vs. implementation"

Claude: [visar comparison]
Du: "Ser bra ut! Commit"
```

**Tips för Visual Workflow:**
- Använd tydliga screenshots
- Markera specifika detaljer i designen
- Be om responsive views (mobile, tablet, desktop)
- Iterera i små steg

### Workflow 3: Explore → Plan → Code → Commit

**Den Mest Robusta Workflowen för Nya Features:**

**Steg 1: EXPLORE (Ingen kod ännu)**

```
Du: "Jag vill lägga till en checkout-flow för e-commerce siten.

     UTFORSKA först:
     1. Hur hanteras payments idag?
     2. Finns det befintlig cart-logik?
     3. Vilken state management används?

     SKRIV INGEN KOD - bara utforska och rapportera."

Claude: [läser genom projektet]
Claude: "Här är vad jag hittat:
         - Ingen payment integration än
         - Cart logic i src/stores/cartStore.ts (Zustand)
         - Använder Stripe för other payments på siten
         - Server API finns på /api/orders"
```

**Steg 2: PLAN**

```
Du: "Baserat på det, skapa en detaljerad plan för checkout-flow.
     Inkludera:
     - Vilka nya komponenter behövs
     - API endpoints
     - State updates
     - Testing approach"

Claude: [skapar plan]

## Checkout Flow Implementation Plan

### Components Needed
1. CheckoutForm.tsx - Main form container
2. PaymentStep.tsx - Stripe payment integration
3. ShippingStep.tsx - Address form
4. OrderSummary.tsx - Review before payment

### State Management
- Extend cartStore with checkout state
- Add checkoutStore for multi-step form state

### API Changes
- POST /api/checkout/create-session
- POST /api/checkout/confirm

### Testing
- Unit tests for form validation
- Integration test for full checkout flow
- Stripe test mode webhooks

### Implementation Order
1. Create checkout store
2. Build form components
3. Stripe integration
4. API endpoints
5. Tests
```

**Steg 3: CLEAR CONTEXT**

```
Du: "Spara denna plan i docs/plans/checkout-implementation.md"

Claude: [sparar plan]

/clear  ← KRITISKT STEG!
```

**Varför Clear?**
Exploration-fasen läste massa filer och skapade mycket kontext. Nu har vi en dokumenterad plan, så vi kan börja fresh!

**Steg 4: CODE (Med Plan som Guide)**

```
Du: "Läs docs/plans/checkout-implementation.md och implementera
     steg 1: Skapa checkout store.

     Använd TDD - skriv tester först."

Claude: [implementerar första steget]
```

```
Du: "Bra! Commit detta."

Claude:
$ git add src/stores/checkoutStore.ts src/stores/checkoutStore.test.ts
$ git commit -m "feat: add checkout store with multi-step state"
```

```
/clear  ← Clear mellan varje major steg
```

```
Du: "Fortsätt med steg 2: Bygg form-komponenter"
Claude: [implementerar]
```

**Repeat för varje steg i planen**

**Steg 5: INTEGRATION & TESTING**

```
Du: "Nu när alla delar är klara, kör full integration test av
     checkout flödet. Använd Stripe test mode."

Claude: [kör tester, verifierar]
```

**Steg 6: DOCUMENTATION UPDATE**

```
Du: "Uppdatera CLAUDE.md med:
     - Hur checkout-systemet fungerar
     - Stripe test credentials
     - Hur man testar checkout lokalt"

Claude: [uppdaterar dokumentation]
```

**Benefits av denna Workflow:**
- ✅ Systematisk approach
- ✅ Undviker stora refactorings senare
- ✅ Dokumenterad plan som referens
- ✅ Optimal context-användning
- ✅ Incremental commits
- ✅ Lättare att code review

### Workflow 4: Safe Autonomous Mode

**För Repetitiva Uppgifter:**

**När att använda:**
- Linting fixes
- Code formatting
- Import sorting
- Boilerplate generation
- Bulk refactoring

**Setup:**

```bash
# Kör Claude i autonomous mode (skippar permissions)
claude --dangerously-skip-permissions

# ⚠️ SÄKERHET: Gör detta ENDAST i:
# - Docker container
# - Isolerad VM
# - Projekt utan känslig data
# - ALDRIG med internet access i produktionsmiljö
```

**Exempel - Auto-fix Linting:**

```
# I autonomous mode:
Du: "Kör ESLint på hela projektet och fixa alla auto-fixable issues"

Claude:
$ npm run lint:fix
[fixar 47 issues automatiskt]

$ git add .
$ git commit -m "style: fix linting issues"

Done! Fixed 47 linting issues.
```

**Säkerhets-Checklist för Autonomous Mode:**
- [ ] Projektet är i Git (kan revertera)
- [ ] Ingen access till produktionsdata
- [ ] Körts i isolerad miljö
- [ ] Ingen internet access för servern
- [ ] Backup finns

### Workflow 5: Code Review Med Claude

**Två Approacher:**

**Approach A: Claude Reviews Din Kod**

```
Du: "Granska min PR för user-authentication feature.
     Leta efter:
     - Säkerhetsbrister
     - Performance issues
     - Code style violations
     - Missing tests
     - Edge cases som inte hanteras"

Claude: [läser PR changes]
Claude: "Review hittat 3 issues:

1. 🔒 SÄKERHET: Lösenord loggas i error handler (auth.ts:45)
   Rekommendation: Använd generic error message

2. 🐛 BUG: Missing validation för email format (register.ts:12)
   Rekommendation: Lägg till email regex validation

3. 🧪 TEST: Ingen test för 'user already exists' case
   Rekommendation: Lägg till test case"
```

**Approach B: Multiple Claude Instances**

```bash
# Terminal 1: Development
claude
> Implementera user-authentication

# Terminal 2: Review
claude
> Granska ändringar i src/auth/ när de är klara
```

**Benefits:**
- Real-time review
- Separation of concerns
- Fresh perspective (olika kontext)

### Workflow 6: Codebase Exploration (Lära Känna Nytt Projekt)

**När du börjar på befintligt projekt:**

```
# Session 1: High-Level Overview
Du: "Jag är ny i detta projekt. Ge mig en översikt:
     1. Vad gör applikationen?
     2. Teknisk stack
     3. Mappstruktur och dess syfte
     4. Huvudsakliga dependencies"

Claude: [agentiskt söker igenom projektet]
```

```
/clear
```

```
# Session 2: Djupdyk i Ett Område
Du: "Förklara hur autentisering är implementerat.
     Visa mig flödet från login till session management."

Claude: [läser auth-relaterade filer]
Claude: "Auth flow:
         1. LoginForm (src/components/auth/LoginForm.tsx)
         2. authService.login() (src/services/authService.ts:23)
         3. JWT token from API
         4. Stored in authStore (Zustand)
         5. Protected routes check store (src/routes/ProtectedRoute.tsx)"
```

```
/clear
```

```
# Session 3: Hitta Patterns
Du: "Visa mig 3 exempel på hur nya API calls implementeras
     i detta projekt, så jag kan följa samma pattern."

Claude: [söker, visar examples]
```

**Skapa Onboarding Dokument:**

```
Du: "Baserat på vad du lärt dig om projektet, skapa en
     ONBOARDING.md för nya utvecklare."

Claude: [skapar comprehensive guide]
```

---

## 8. Avancerade Tekniker {#avancerade-tekniker}

### Custom Slash Commands

**Vad är Slash Commands?**
Återanvändbara prompt-templates som sparar tid.

**Skapa Din Första Command:**

```bash
# Skapa commands mapp
mkdir -p .claude/commands

# Skapa en command
touch .claude/commands/review-pr.md
```

**Innehåll i review-pr.md:**
```markdown
Granska följande pull request noggrant:

$ARGUMENTS

Leta specifikt efter:
- 🔒 Säkerhetsbrister (SQL injection, XSS, CSRF)
- 🐛 Potentiella bugs och edge cases
- 🎨 Code style violations enligt CLAUDE.md
- 🧪 Saknade tester
- 📚 Saknad eller felaktig dokumentation
- ⚡ Performance issues

Ge konkreta recommendations med filnamn och radnummer.
```

**Använda Command:**
```bash
# I Claude
/review-pr https://github.com/user/repo/pull/123

# Eller
/review-pr src/features/checkout/
```

**Fler Användbara Commands:**

**1. /test-component.md**
```markdown
Skapa omfattande tester för komponenten: $ARGUMENTS

Tester ska inkludera:
- ✅ Rendering tests
- ✅ User interaction tests
- ✅ Edge cases
- ✅ Accessibility tests
- ✅ Error states

Använd React Testing Library och Jest.
Följ AAA pattern: Arrange, Act, Assert.
```

**2. /refactor.md**
```markdown
Refaktorera följande kod: $ARGUMENTS

Fokusera på:
1. Läsbarhet
2. Underhållbarhet
3. Performance
4. Following SOLID principles

Förklara varje ändring och varför den förbättrar koden.
```

**3. /add-feature.md**
```markdown
Implementera ny feature: $ARGUMENTS

Följ denna workflow:
1. EXPLORE - Förstå befintlig arkitektur
2. PLAN - Skapa detaljerad implementation plan
3. Vänta på godkännande
4. CODE - Implementera med TDD
5. TEST - Skriv integration tester
6. DOCS - Uppdatera dokumentation

Använd /clear mellan varje major steg.
```

**4. /debug.md**
```markdown
Debugga följande issue: $ARGUMENTS

Systematic approach:
1. Reproducera buggen
2. Läs relevant kod
3. Identifiera root cause
4. Föreslå fix
5. Skriv regression test
6. Implementera fix
7. Verifiera att test passar
```

**Dela Commands med Teamet:**

```bash
# Commita commands till Git
git add .claude/commands/
git commit -m "docs: add team slash commands"
git push

# Nu kan hela teamet använda samma commands!
```

### Model Context Protocol (MCP)

**Vad är MCP?**
Ett sätt att ge Claude tillgång till externa verktyg och data sources.

**Vanliga MCP Servers:**

**1. Puppeteer (Screenshots & Browser)**
```bash
# Installera
npm install -g @anthropic-ai/mcp-puppeteer

# Konfigurera i .mcp.json
{
  "puppeteer": {
    "command": "npx",
    "args": ["-y", "@anthropic-ai/mcp-puppeteer"]
  }
}
```

**Användning:**
```
Du: "Ta en screenshot av localhost:3000 och analysera layouten"
Claude: [använder Puppeteer MCP för att ta screenshot]
```

**2. Database MCP (PostgreSQL, MySQL)**
```json
{
  "postgres": {
    "command": "npx",
    "args": ["-y", "@anthropic-ai/mcp-postgres"],
    "env": {
      "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
    }
  }
}
```

**Användning:**
```
Du: "Visa mig schema för users-tabellen"
Claude: [queries database via MCP]
```

**3. Custom MCP Server**

**Skapa en MCP server för ditt Internal API:**

```typescript
// mcp-server.ts
import { MCPServer } from '@anthropic-ai/mcp-sdk'

const server = new MCPServer({
  name: 'internal-api',
  version: '1.0.0',
})

server.tool('get-user-stats', async ({ userId }) => {
  const response = await fetch(`https://internal-api.com/users/${userId}/stats`)
  return response.json()
})

server.listen()
```

**Konfigurera:**
```json
{
  "internal-api": {
    "command": "node",
    "args": ["./mcp-server.js"]
  }
}
```

**Använd:**
```
Du: "Hämta user stats för user ID 123 och visualisera data"
Claude: [använder din custom MCP tool]
```

**MCP Best Practices:**
- Projekt-specifika MCP i `.mcp.json` (committas till Git)
- Globala MCP i `~/.claude/mcp.json`
- Använd `--mcp-debug` för troubleshooting
- Dokumentera MCP tools i CLAUDE.md

### Headless Mode & Automation

**Använda Claude i Scripts:**

**Enkel Usage:**
```bash
# Skicka prompt via flag
claude -p "Kör alla tester och rapportera resultat"
```

**I CI/CD Pipeline:**

```yaml
# .github/workflows/ai-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  claude-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Run Claude Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p "Granska alla ändringar i denna PR.
                     Outputta JSON med findings." \
                     --output-format stream-json > review.json

      - name: Post Review Comments
        run: node scripts/post-review-comments.js review.json
```

**Pre-commit Hook:**

```bash
# .git/hooks/pre-commit
#!/bin/bash

# Använd Claude för att validera commits
claude -p "Analysera staged changes.
           Finns det några säkerhetsproblem eller code quality issues?
           Returnera exit code 1 om issues hittas."

if [ $? -ne 0 ]; then
  echo "❌ Claude hittade issues. Fix dem innan commit."
  exit 1
fi
```

**Bulk Processing:**

```bash
# process-components.sh
#!/bin/bash

# Hitta alla komponenter utan tester
components=$(find src/components -name "*.tsx" \
             -not -name "*.test.tsx")

# För varje komponent, generera tester
for component in $components; do
  echo "Processing $component..."

  claude -p "Skapa tester för $component.
             Spara som ${component%.tsx}.test.tsx" \
         --output-format stream-json

  # Small delay för att inte överbelasta
  sleep 2
done
```

**Strukturerad Output:**

```bash
# Få JSON output för parsing
claude -p "Analysera projektet och returnera metrics som JSON:
           - Total LOC
           - Test coverage estimate
           - Number of components
           - Number of API endpoints" \
       --output-format stream-json | jq '.metrics'
```

### Git & GitHub Integration

**Avancerad Git Användning:**

**1. Search Git History**
```
Du: "Varför implementerades user caching?
     Sök i git history efter relevanta commits."

Claude:
$ git log --all --grep="cache" --grep="user" -i
$ git show abc123

"User caching lades till i commit abc123 för att minska
database queries. Original motivation:
'Users were hitting DB on every page load'"
```

**2. Complex Git Operations**
```
Du: "Vi behöver revertera feature/dark-mode mergen men
     behålla en specifik fil (theme.css). Hur gör vi?"

Claude:
$ git revert -m 1 <merge-commit>
$ git checkout <merge-commit> -- src/theme.css
$ git commit --amend
```

**3. Interactive Rebase Assistance**
```
Du: "Jag vill squasha de senaste 5 commits till 2 logiska commits.
     Hjälp mig planera rebasing."

Claude: "Här är de senaste 5 commits:
         1. Add login form
         2. Fix login validation
         3. Add tests
         4. Add logout button
         5. Fix logout bug

         Rekommenderad squash:
         - Commit 1+2+3 → 'feat: add user authentication'
         - Commit 4+5 → 'feat: add logout functionality'

         Köra: git rebase -i HEAD~5"
```

**GitHub via gh CLI:**

**1. Auto-create Issues från TODOs**
```
Du: "Sök igenom koden efter TODO comments och skapa
     GitHub issues för dem"

Claude:
$ grep -r "// TODO" src/

Found 5 TODOs:
1. src/api/users.ts:12 - TODO: Add pagination
2. src/components/Dashboard.tsx:45 - TODO: Add loading state

$ gh issue create --title "Add pagination to users API" \
                  --body "Found in src/api/users.ts:12"
[skapar issues för alla]
```

**2. PR Management**
```
Du: "Skapa en PR för nuvarande branch med sammanfattning
     av alla commits"

Claude:
$ git log main..HEAD --oneline
$ gh pr create --title "Feature: User Dashboard" \
               --body "$(cat <<EOF
## Summary
- Add dashboard component
- Integrate user stats API
- Add responsive layout

## Testing
- [x] Unit tests added
- [x] Manual testing completed
- [ ] E2E tests pending

## Screenshots
![Dashboard](./screenshots/dashboard.png)
EOF
)"
```

**3. Address PR Comments**
```
Du: "Hämta kommentarer från PR #42 och fixa dem"

Claude:
$ gh pr view 42 --json comments -q '.comments'

Comments found:
1. @reviewer: "Missing error handling in fetchUser"
2. @reviewer: "Add prop types to UserCard"

[Fixar varje issue]
$ git commit -m "fix: address PR review comments"
$ git push
```

### Multiple Claude Sessions Pattern

**Scenario: Stor Feature Implementation**

**Terminal 1: Development (Main)**
```bash
claude
> Implementera checkout-flow
```

**Terminal 2: Testing**
```bash
claude
> Skriv och kör tester för ny kod i src/checkout/
> Watch for file changes
```

**Terminal 3: Documentation**
```bash
claude
> Uppdatera dokumentation när nya features läggs till
> Håll docs/ synkad med implementation
```

**Terminal 4: Review**
```bash
claude
> Granska ändringar i checkout/ från säkerhetsperspektiv
```

**Benefits:**
- Parallell arbetsgång
- Separerade kontexter (mer fokuserade)
- En instance per concern
- Snabbare iteration

**Best Practices för Multiple Sessions:**
- Namnge terminal tabs tydligt
- En tydlig "main" session
- Andra sessions är support/monitoring
- Synka med Git commits mellan sessions

---

## 9. Best Practices för Långsiktig Framgång {#best-practices}

### Principle 1: Specificity Över Allt

**❌ Vag Prompt:**
```
"Fixa autentiseringen"
```

**✅ Specifik Prompt:**
```
"I src/services/authService.ts:45, login-funktionen
returnerar fel statuscode (200 istället för 201) vid
successful registration.

Fixa detta och uppdatera motsvarande test i
authService.test.ts för att verifiera korrekt statuscode."
```

**Why Specificity Matters:**
- Mindre context behövs läsas
- Snabbare implementation
- Färre iterationer
- Bättre resultat

**How to Be Specific:**

**1. Använd File Paths:**
```
❌ "Fixa buggen i login"
✅ "Fixa buggen i src/components/auth/LoginForm.tsx:67"
```

**2. Ge Exempel:**
```
❌ "Lägg till validation"
✅ "Lägg till validation:
    - Email: måste innehålla @ och domain
    - Password: minst 8 tecken, en siffra, en special char
    Exempel: validateForm({ email: 'test@example.com', password: 'Pass123!' })"
```

**3. Specificera Teknisk Stack:**
```
❌ "Skapa en API"
✅ "Skapa en REST API med:
    - Express.js + TypeScript
    - Prisma ORM för PostgreSQL
    - JWT authentication
    - Zod för validation
    - Jest för testing"
```

**4. Define Success Criteria:**
```
❌ "Optimera prestandan"
✅ "Optimera dashboard load time:
    - Current: 3.2s
    - Target: <1s
    - Metrics: Lighthouse Performance score >90
    - Fokus: Reducera antal API calls och optimera re-renders"
```

### Principle 2: Visual Context är Guld

**När att Använda Screenshots/Bilder:**

**1. UI Implementation:**
```
Du: [bifoga design mockup]
    "Implementera denna landing page.
     Matcha spacing och colors exakt."
```

**2. Bug Reports:**
```
Du: [screenshot av error]
    "Denna error visas när jag klickar 'Submit'.
     Console visar: [screenshot av console]
     Fixa buggen."
```

**3. Data Visualization:**
```
Du: [diagram av nuvarande arkitektur]
    "Vi vill migrera från denna arkitektur till microservices.
     Skapa en migration plan."
```

**4. Responsive Design:**
```
Du: [screenshots från mobile, tablet, desktop]
    "Sidan ser bra ut på desktop men går sönder på mobile.
     Fixa responsive issues."
```

**Best Practices:**
- Använd höga upplösning bilder
- Markera viktiga detaljer (arrows, highlights)
- Inkludera multiple views om relevant
- Kombiner image + text beskrivning

### Principle 3: Iterative Course Correction

**Power Move: Double-Tap ESC**

```
Du: "Implementera user dashboard"
Claude: [börjar skriva kod]

[Du inser att approach är fel]
ESC ESC (double tap)

[Prompt öppnas för edit]
Du: "Implementera user dashboard

     ANVÄND INTE class components - använd funktionella
     Använd TailwindCSS istället för styled-components"

Claude: [börjar om med rätt approach]
```

**Single ESC: Pausa och Behåll Context**

```
Claude: [mitt i en lång implementation]

ESC (single tap)

Du: "Innan du fortsätter, lägg till TypeScript interfaces först"
Claude: [pivoterar, continues med context intact]
```

**Ask for Alternatives:**

```
Du: "Visa mig 3 olika approacher för state management:
     1. Context API
     2. Zustand
     3. Redux Toolkit

     Förklara pros/cons för vårt use-case."

Claude: [presenterar alternatives]

Du: "Vi kör med Zustand. Implementera det."
```

### Principle 4: Dokumentation är Din Framtida Självs Bästa Vän

**Living Documentation Pattern:**

**Steg 1: Decision Records**
```
# docs/decisions/001-choosing-database.md

## Context
Vi behöver välja database för user data och content.

## Options Considered
1. PostgreSQL - Traditional relational
2. MongoDB - Document database
3. Supabase - Hosted PostgreSQL with extras

## Decision
Supabase

## Rationale
- Built-in authentication
- Real-time subscriptions
- PostgreSQL reliability
- Generous free tier
- Good TypeScript support

## Consequences
- Vendor lock-in risk
- Learning curve för real-time features
- Migration path if needed: Standard PostgreSQL
```

**Steg 2: Håll CLAUDE.md Updated**

```
# Efter varje major feature
Du: "Uppdatera CLAUDE.md med checkout-flow:
     - Hur det fungerar
     - Dependencies
     - Testing approach
     - Common issues och solutions"
```

**Steg 3: Auto-generated Docs**

```
Du: "Generera API dokumentation från våra Express routes.
     Inkludera: endpoints, parameters, responses, examples.
     Spara i docs/api/README.md"

Claude: [analyserar routes, genererar docs]
```

**Steg 4: Inline Documentation**

```
Du: "Lägg till JSDoc comments till alla exported functions
     i src/utils/.

     Inkludera:
     - Description
     - @param med types
     - @returns
     - @example"

Claude: [lägger till comprehensive comments]
```

**Benefits:**
- Lättare onboarding
- Claude kan referera till docs i framtida sessions
- Knowledge preservation
- Team alignment

### Principle 5: Testing är Inte Optional

**Test Pyramid för Claude Code:**

```
        /\
       /  \      E2E Tests (Få)
      /____\     - Critical user journeys
     /      \    - Smoke tests
    /        \
   /          \  Integration Tests (Mer)
  /____________\ - API endpoints
 /              \- Component interaction
/                \
/__________________\ Unit Tests (Flest)
                    - Utilities
                    - Hooks
                    - Business logic
```

**Testing Workflow:**

**1. Unit Tests (Dagligen)**
```
Du: "Skriv unit tests för alla functions i src/utils/dateHelpers.ts"

Claude: [TDD approach - tests först]
```

**2. Integration Tests (Per Feature)**
```
Du: "Nu när checkout-flow är klar, skriv integration test:
     1. Add item to cart
     2. Go to checkout
     3. Fill shipping info
     4. Complete payment (Stripe test mode)
     5. Verify order created"

Claude: [E2E test med Playwright/Cypress]
```

**3. Continuous Testing**
```
Du: "Setup test watching:
     - Kör affected tests när filer ändras
     - Visa coverage report
     - Fail om coverage < 80%"

Claude: [konfigurerar test runner]
```

**Test Best Practices:**
- ✅ Skriv tests innan eller samtidigt med kod (TDD)
- ✅ Test real user behavior, inte implementation
- ✅ Mock external dependencies (APIs, databases)
- ✅ Keep tests fast (< 1s per test suite)
- ❌ Testa inte library/framework kod
- ❌ Skriv inte flaky tests

### Principle 6: Git Hygiene

**Commit Message Standards:**

```bash
# Använd Conventional Commits
feat: add user authentication
fix: resolve login validation bug
docs: update API documentation
style: format code with prettier
refactor: extract auth logic to service
test: add unit tests for authService
chore: update dependencies
```

**Working with Claude:**

```
Du: "Stage alla auth-relaterade ändringar och skapa en commit.
     Följ conventional commits standard.
     Skriv detaljerad commit body om det behövs."

Claude:
$ git add src/auth/ src/components/LoginForm.tsx
$ git commit -m "$(cat <<'EOF'
feat: implement user authentication system

Added:
- JWT-based authentication
- Login/logout functionality
- Protected route wrapper
- Auth context provider

Tests:
- Unit tests for auth service
- Integration test for login flow

Breaking changes: None
EOF
)"
```

**Branch Strategy:**

```
Du: "Skapa en feature branch för dark-mode implementation"

Claude:
$ git checkout -b feature/dark-mode-implementation
```

**PR Best Practices:**

```
Du: "Skapa PR med:
     - Sammanfattning av changes
     - Screenshots (before/after)
     - Testing checklist
     - Breaking changes section"

Claude: [skapar comprehensive PR]
```

### Principle 7: Security First

**Security Checklist för Claude:**

**1. Input Validation**
```
Du: "Granska alla API endpoints i src/api/.
     Verifiera att all user input valideras.
     Lista endpoints som saknar validation."

Claude: [auditerar endpoints]
Claude: "3 endpoints saknar validation:
         - POST /api/comments (body inte validerad)
         - PUT /api/users/:id (params inte sanitized)
         - GET /api/search (query params inte escaped)"
```

**2. Secrets Management**
```
Du: "Sök i hela projektet efter hardcoded secrets, API keys,
     eller credentials. Inkludera git history."

Claude:
$ git log -p | grep -i "api_key\|password\|secret"

"⚠️ Hittat i .env.example:
 STRIPE_SECRET_KEY=sk_test_...

 Detta är OK (example file).

 ❌ KRITISKT: Hittat i commit abc123:
 const API_KEY = 'sk_live_...'

 REKOMMENDATION: Rotate denna key omedelbart!"
```

**3. Dependency Security**
```
Du: "Kör security audit på dependencies och fixa vulnerabilities"

Claude:
$ npm audit
$ npm audit fix

"Fixed 12 vulnerabilities.
 3 require manual review (breaking changes):
 - lodash (prototype pollution)
 - ...

 Vill du att jag undersöker alternativ?"
```

**Security Patterns i CLAUDE.md:**

```markdown
## SÄKERHETSREGLER

### Input Validation
- **ANVÄND ALLTID** Zod schemas för API input
- **SANITERA** all user-generated content
- **ESCAPE** output för att förhindra XSS

### Authentication
- **LAGRA ALDRIG** plaintext passwords
- **ANVÄND** bcrypt med cost factor ≥ 10
- **IMPLEMENTERA** rate limiting på auth endpoints

### API Keys
- **EXPONERA ALDRIG** secrets till frontend
- **ANVÄND** environment variables
- **LÄGG TILL** .env i .gitignore

### Database
- **ANVÄND** prepared statements (Prisma gör detta)
- **VALIDERA** user permissions på varje query
- **KRYPTERA** känslig data at rest
```

### Principle 8: Performance Awareness

**Performance Budgets:**

```
Du: "Sätt upp performance monitoring:
     - Lighthouse CI
     - Budgets: FCP < 1.5s, LCP < 2.5s, TTI < 3.5s
     - Fail build om budgets överskrids"

Claude: [konfigurerar Lighthouse CI]
```

**Optimization Workflow:**

```
Du: "Dashboard-sidan laddar långsamt.
     1. Profila prestandan
     2. Identifiera bottlenecks
     3. Föreslå optimizations
     4. Implementera top 3 fixes"

Claude:
"Profiling results:
 - 45 unnecessary re-renders (React DevTools)
 - 12 API calls på mount (should be 3)
 - Large bundle size (UserList component: 150KB)

 Recommendations:
 1. Memoize UserList med React.memo
 2. Batch API calls med Promise.all
 3. Code-split UserList med lazy loading

 Estimated improvement: 2.3s → 0.8s load time"
```

**Monitoring:**

```markdown
# CLAUDE.md

## Performance Standards

### Metrics
- Lighthouse Performance Score: >90
- First Contentful Paint: <1.5s
- Time to Interactive: <3.5s
- Bundle Size: <200KB (gzipped)

### Monitoring
```bash
npm run lighthouse  # Run Lighthouse audit
npm run analyze     # Bundle size analysis
```

### Optimizations
- Code splitting på route level
- Image optimization (WebP + lazy loading)
- API response caching (React Query)
```

---

## 10. Felsökning och Vanliga Problem {#felsökning}

### Problem 1: Claude Glömmer Kontext/Regler

**Symptom:**
```
Du: "Lägg till en ny component"
Claude: [skapar class component trots att projektet använder funktionella]
```

**Root Cause:**
- För lång conversation utan /clear
- CLAUDE.md för vag eller saknas
- För mycket irrelevant kontext

**Lösning:**

```bash
# 1. Clear context
/clear

# 2. Förbättra CLAUDE.md
Du: "Läs igenom projektet och identifiera code patterns.
     Uppdatera CLAUDE.md med:
     - Component patterns vi använder
     - Naming conventions
     - Prohibited practices"

# 3. Be om bekräftelse
Du: "Innan du skriver kod, bekräfta:
     1. Ska detta vara en funktionell komponent?
     2. Vilken styling approach använder vi?
     3. Var ska filen placeras?"
```

**Prevention:**
```markdown
# I CLAUDE.md - Lägg till betoning

## KRITISKA REGLER

### React Components
- **DU MÅSTE** använda funktionella komponenter
- **ALDRIG** skapa class components
- **EXEMPEL:**
  ```tsx
  // ✅ Gör detta
  export const MyComponent: React.FC = () => {
    return <div>Content</div>
  }

  // ❌ ALDRIG detta
  export class MyComponent extends React.Component {
    render() { return <div>Content</div> }
  }
  ```
```

### Problem 2: Claude Gör För Stora Ändringar På En Gång

**Symptom:**
```
Du: "Lägg till dark mode"
Claude: [refaktorerar hela styling systemet, ändrar 30 filer]
```

**Root Cause:**
- Prompt var för öppen för interpretation
- Ingen steg-för-steg plan requested

**Lösning:**

```
Du: "STOPP. Ångra de senaste ändringarna.

     Låt oss göra om detta metodiskt:

     1. FÖRST: Analysera hur styling funkar idag (GÖR INGA ÄNDRINGAR)
     2. Skapa en minimal plan för dark mode
     3. Implementera i små, incrementala steg
     4. Jag vill godkänna varje steg innan nästa"

Claude: [börjar om med strukturerad approach]
```

**Prevention:**
```
# Alltid för stora features:
Du: "Implementera X med följande approach:

     1. Exploration phase (no code)
     2. Plan creation
     3. Wait for my approval
     4. Implement step by step
     5. I'll say 'continue' between steps"
```

### Problem 3: Tester Failar Efter Claudes Ändringar

**Symptom:**
```
Du: "Fixa login buggen"
Claude: [fixar bug men 5 tester failar nu]
```

**Lösning:**

```
Du: "Kör test suiten och visa mig vilka tester som failar"

Claude:
$ npm test

"5 tests failing:
 1. LoginForm - should show error on invalid email
 2. authService - should return 401 on bad credentials
 ..."

Du: "För varje failing test:
     1. Förklara varför det failar
     2. Är det testet som behöver uppdateras eller koden?
     3. Fixa"

Claude: [går genom varje test systematiskt]
```

**Prevention:**
```
Du: "Efter varje kod-ändring:
     1. Kör affected tests
     2. Om några failar, visa mig och vänta på instruktioner
     3. Committa ALDRIG med failing tests"
```

### Problem 4: Claude Installerar Fel Dependencies

**Symptom:**
```
Claude:
$ npm install moment

Du: "Vi använder date-fns, inte moment!"
```

**Lösning:**

```
Du: "Avinstallera moment och använd date-fns istället"

Claude:
$ npm uninstall moment
$ npm install date-fns
[uppdaterar kod för att använda date-fns]
```

**Prevention:**
```markdown
# CLAUDE.md

## Dependencies

### Approved Libraries
- Date handling: date-fns (NOT moment)
- HTTP client: axios
- State management: Zustand
- Forms: React Hook Form + Zod

### Before Adding New Dependency
1. Check if we already have similar functionality
2. Verify it's actively maintained
3. Check bundle size impact
4. Ask before installing
```

### Problem 5: Git Conflicts Efter Claude Commits

**Symptom:**
```
$ git push
! [rejected] main -> main (non-fast-forward)
```

**Lösning:**

```
Du: "Vi har merge conflicts. Hjälp mig resolve dem."

Claude:
$ git pull --rebase origin main

"Conflicts in:
 - src/components/Header.tsx

 Visar conflict:
 <<<<<<< HEAD
 const Header = () => { ... }
 =======
 export const Header: React.FC = () => { ... }
 >>>>>>> origin/main

 Vår version använder TypeScript typing (bättre).
 Ska jag använda vår version?"

Du: "Ja"

Claude:
$ git add src/components/Header.tsx
$ git rebase --continue
```

**Prevention:**
```
Du: "Innan du börjar arbeta, alltid:
     1. git fetch origin
     2. git rebase origin/main (om vi är på feature branch)
     3. Resolve conflicts om några
     4. SEDAN börja arbeta"
```

### Problem 6: Claude Skapar För Många Filer

**Symptom:**
```
Claude skapar:
- UserCard.tsx
- UserCard.styles.tsx
- UserCard.types.tsx
- UserCard.utils.tsx
- UserCard.test.tsx
- UserCard.stories.tsx

För en 20-radig komponent
```

**Lösning:**

```
Du: "Detta är överkomplicerat. Consolidera till:
     - UserCard.tsx (component + types)
     - UserCard.test.tsx (tests)

     Ta bort de andra filerna."
```

**Prevention:**
```markdown
# CLAUDE.md

## File Organization

### Components
- Under 100 rader: Single file med inline types
- 100-300 rader: Separate test file
- Over 300 rader: Consider splitting component

### Avoid Over-Engineering
- **INTE** separate files för allt
- **PRAGMATISK** organization
- **FOKUS** på läsbarhet, inte "perfect structure"
```

### Problem 7: Performance Issues i Dev Mode

**Symptom:**
```
Claude kör kommandon väldigt långsamt
Responses tar lång tid
```

**Möjliga Orsaker & Lösningar:**

**1. För mycket kontext**
```bash
/clear
```

**2. Stora filer i conversation**
```
Du: "Läs endast funktionen 'processUsers' från utils/data.ts,
     inte hela filen"
```

**3. Många concurrent operations**
```
# Istället för att köra 10 kommandon parallellt
Du: "Kör dessa kommandon sekventiellt:
     1. npm install
     2. npm run build
     3. npm test"
```

### Problem 8: Claude Kan Inte Hitta Fil

**Symptom:**
```
Claude: "Jag kan inte hitta src/components/UserCard.tsx"
```

**Troubleshooting:**

```
Du: "Lista alla filer i src/components/"

Claude:
$ ls -la src/components/

"usercard.tsx  (lowercase!)
 LoginForm.tsx
 ..."

Du: "Filen heter usercard.tsx (lowercase). Använd det namnet."
```

**Prevention:**
```
# Använd tab-completion i prompts
Du: "Läs sr[TAB]
     Läs src/co[TAB]
     Läs src/components/use[TAB]
     Läs src/components/usercard.tsx"
```

### Debug Mode & Diagnostics

**Enable Verbose Logging:**
```bash
# Kör Claude med debug output
claude --verbose

# För MCP issues
claude --mcp-debug
```

**Check Configuration:**
```bash
# Visa nuvarande settings
cat ~/.claude.json

# Visa projekt settings
cat .claude/settings.json

# Lista permissions
/permissions
```

**Common Config Issues:**

**Problem: Claude skippar alltid permissions**
```json
// ~/.claude.json
{
  "permissions": {
    "allowedTools": ["*"]  // ← TOO PERMISSIVE
  }
}
```

**Fix:**
```json
{
  "permissions": {
    "allowedTools": ["Read", "Edit", "Bash", "Grep", "Glob"]
  }
}
```

---

## Checklista: Börja Ett Nytt Projekt Med Claude

```markdown
## Projekt Setup Checklist

### Initial Setup
- [ ] Skapa projekt directory
- [ ] Initiera Git (`git init`)
- [ ] Skapa .gitignore
- [ ] Starta Claude i projekt directory

### Projekt Configuration
- [ ] Skapa CLAUDE.md i project root
  - [ ] Tech stack definierad
  - [ ] Coding conventions
  - [ ] Testing approach
  - [ ] Common commands
- [ ] Setup .claude/commands/ (om custom commands behövs)
- [ ] Konfigurera permissions (/permissions)

### Development Setup
- [ ] Initiera package manager (npm/yarn/pnpm)
- [ ] Setup TypeScript/ESLint/Prettier
- [ ] Configure test framework
- [ ] Setup pre-commit hooks

### Documentation
- [ ] README.md med project overview
- [ ] docs/ directory för decisions
- [ ] CONTRIBUTING.md (för teams)

### Git Workflow
- [ ] Setup branch protection (om team)
- [ ] Define commit message convention
- [ ] Configure .gitignore properly

### First Feature med Claude
- [ ] Use Explore → Plan → Code workflow
- [ ] Skriv tests först (TDD)
- [ ] Clear context regularly
- [ ] Document decisions
- [ ] Review before commit

### Ongoing Maintenance
- [ ] Uppdatera CLAUDE.md när conventions ändras
- [ ] Keep documentation synced med kod
- [ ] Regular dependency updates
- [ ] Security audits
```

---

## Sammanfattning: Nycklar till Framgång

### De 10 Viktigaste Principerna

1. **Context Management är King**
   - Clear early, clear often
   - 1-3 messages per task → /clear

2. **CLAUDE.md är Ditt Viktigaste Verktyg**
   - 100-200 rader sweet spot
   - Specific över generisk
   - Uppdatera kontinuerligt

3. **Var Specifik i Prompts**
   - File paths
   - Exempel
   - Success criteria
   - Tech stack

4. **Test-Driven Development**
   - Tests först
   - Verifiera fail
   - Implementera
   - Commit separat

5. **Visual Context När Möjligt**
   - Screenshots för UI
   - Diagrams för arkitektur
   - Error messages

6. **Structured Workflows**
   - Explore → Plan → Clear → Code
   - Break down stora tasks
   - Incremental commits

7. **Documentation är Investering**
   - Decision records
   - Inline comments
   - Updated CLAUDE.md
   - API docs

8. **Security First**
   - Validate all input
   - Audit dependencies
   - No secrets in code
   - Regular security reviews

9. **Git Hygiene**
   - Conventional commits
   - Atomic commits
   - Descriptive PR descriptions
   - Review before merge

10. **Iterative Mindset**
    - Start small
    - Get feedback
    - Refine approach
    - Scale up

---

## Nästa Steg: Din Learning Path

### Vecka 1: Grunderna
- [ ] Installera och konfigurera Claude
- [ ] Bygg din första app (TODO app tutorial)
- [ ] Skapa din första CLAUDE.md
- [ ] Öva på /clear workflow

### Vecka 2: Workflows
- [ ] Implementera feature med TDD
- [ ] Prova Explore → Plan → Code
- [ ] Skapa custom slash commands
- [ ] Practice context management

### Vecka 3: Avancerat
- [ ] Multiple Claude instances
- [ ] MCP integration
- [ ] Git automation
- [ ] CI/CD integration

### Vecka 4: Optimization
- [ ] Review ditt CLAUDE.md
- [ ] Optimera workflows
- [ ] Document lessons learned
- [ ] Share med team

---

## Resurser

### Officiella Docs
- https://claude.ai/code
- https://docs.anthropic.com/claude-code

### Community
- GitHub Discussions
- Discord communities
- Twitter #ClaudeCode

### Keep Learning
- Experimentera dagligen
- Dokumentera vad som fungerar
- Dela med community
- Iterera på ditt workflow

---

**Remember: Claude Code är ett verktyg. Ditt judgement, kreativitet, och problemlösning är vad som gör skillnad. Använd denna guide som foundation, men anpassa till ditt workflow och projekt.**

**Lycka till med din Claude Code journey! 🚀**
