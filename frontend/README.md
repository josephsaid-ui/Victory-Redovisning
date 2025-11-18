# Eye Care Secretary - Frontend

Modern React-baserad frontend för Eye Care Secretary-applikationen.

## ✨ Features

- 🎨 **Modern UI** med Tailwind CSS
- 📱 **Responsiv design** som fungerar på alla enheter
- 🔍 **Sjukdomsdatabas** - Sök och filtrera 200 ögonsjukdomar
- 💊 **Läkemedelsdatabas** - 100 ögonläkemedel med detaljerad information
- 🔎 **Symtomchecker** - AI-driven symptomanalys
- 👥 **Patienthantering** - Demo-funktionalitet för patientöversikt
- ⚡ **Snabb navigation** med React Router
- 🎯 **TypeScript** för typsäkerhet

## 🏗️ Teknologi

- **React 18** - UI-bibliotek
- **TypeScript** - Typsäkert JavaScript
- **Vite** - Snabb byggverktyg och dev-server
- **Tailwind CSS** - Utility-first CSS
- **React Router** - Client-side routing
- **Lucide React** - Ikonbibliotek
- **Axios** - HTTP-klient (för API-integrering)

## 📁 Projektstruktur

```
frontend/
├── src/
│   ├── components/       # Återanvändbara komponenter
│   │   └── Layout.tsx    # Huvudlayout med sidebar
│   ├── pages/            # Sidor/vyer
│   │   ├── Dashboard.tsx
│   │   ├── Diseases.tsx
│   │   ├── Medications.tsx
│   │   ├── SymptomChecker.tsx
│   │   └── Patients.tsx
│   ├── services/         # API-tjänster
│   ├── types/            # TypeScript-typer
│   ├── hooks/            # Custom React hooks
│   ├── utils/            # Hjälpfunktioner
│   ├── App.tsx           # Huvudkomponent
│   ├── main.tsx          # Entry point
│   └── index.css         # Global CSS med Tailwind
├── package.json
├── vite.config.ts
├── tailwind.config.js
└── tsconfig.json
```

## 🚀 Komma igång

### Förutsättningar

- Node.js >= 18.0.0
- npm eller yarn

### Installation

1. **Installera beroenden:**
   ```bash
   npm install
   ```

2. **Starta utvecklingsserver:**
   ```bash
   npm run dev
   ```

   Öppna [http://localhost:5173](http://localhost:5173) i din webbläsare.

3. **Bygg för produktion:**
   ```bash
   npm run build
   ```

4. **Förhandsgranska produktionsbygget:**
   ```bash
   npm run preview
   ```

## 🎨 Sidor och funktioner

### Dashboard
- Översikt med statistik
- Snabblänkar till huvudfunktioner
- Akuta tillstånd-översikt

### Sjukdomsdatabas
- Sök bland 200 ögonsjukdomar
- Filtrera per kategori (Retina, Glaukom, Katarakt, etc.)
- Detaljerad information om symtom och behandling

### Läkemedelsdatabas
- 100 ögonläkemedel
- Filtrera per kategori (Glaukom, Antibiotika, etc.)
- Dosering och indikationer

### Symtomchecker
- AI-driven symptomanalys
- Differentialdiagnostik
- Akutgradsbedömning
- Behandlingsrekommendationer

### Patienthantering (Demo)
- Patientöversikt
- Besökshistorik
- Nästa bokade besök

## 🔌 API-integrering

Frontendar konfigurerad att kommunicera med backend via proxy:

```typescript
// vite.config.ts
server: {
  port: 5173,
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
    },
  },
}
```

API-anrop görs via `/api`-prefix och dirigeras automatiskt till backend.

## 🎨 Styling

Projektet använder Tailwind CSS med custom konfiguration:

- **Färgschema:** Primary blue/indigo
- **Komponenter:** Card, Button, Input definierade i `index.css`
- **Responsive:** Mobile-first approach
- **Dark mode:** Kan implementeras vid behov

## 📝 Scripts

```bash
npm run dev      # Starta utvecklingsserver
npm run build    # Bygg för produktion
npm run preview  # Förhandsgranska produktionsbygge
npm run lint     # Linta kod med ESLint
```

## 🔒 Säkerhet och GDPR

**OBS:** Detta är en demonstrationsapp. För produktionsanvändning krävs:

- ✅ Säker autentisering och auktorisering
- ✅ Kryptering av patientdata
- ✅ GDPR-efterlevnad
- ✅ Loggning och audit trails
- ✅ Säkra API-anrop
- ✅ Integration med journalsystem

## 🚧 Nästa steg

- [ ] Implementera riktig API-integration
- [ ] Lägg till autentisering
- [ ] Implementera detaljvyer för sjukdomar och läkemedel
- [ ] Lägg till export-funktioner
- [ ] Implementera offline-support
- [ ] Lägg till unit tests
- [ ] Implementera E2E-tester

## 📄 Licens

MIT

## 👨‍💻 Utveckling

Utvecklad som del av Victory Redovisning Eye Care Secretary-projektet.
