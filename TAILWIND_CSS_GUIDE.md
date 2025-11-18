# Tailwind CSS – Den Kompletta Guiden

## 📚 Innehållsförteckning

- [Om Denna Guide](#-om-denna-guide)
- [Nivå 1: Vad är Tailwind egentligen? 👶](#nivå-1-vad-är-tailwind-egentligen-)
- [Nivå 2: Första riktiga kontakten med Tailwind 🧒](#nivå-2-första-riktiga-kontakten-med-tailwind-)
- [Nivå 3: Hur Tailwind faktiskt funkar under huven 🎓](#nivå-3-hur-tailwind-faktiskt-funkar-under-huven-)
- [Nivå 4: Avancerade mönster, best practices & anti-patterns 🏛️](#nivå-4-avancerade-mönster-best-practices--anti-patterns-)
- [Nivå 5: Tailwind på masternivå i moderna projekt 💼](#nivå-5-tailwind-på-masternivå-i-moderna-projekt-)
- [Slutlig Självutvärdering 🎓](#-slutlig-självutvärdering)
- [Ordlista 📖](#-ordlista)
- [Resurser för Fördjupning 🔗](#-resurser-för-fördjupning)
- [Vanliga Frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande svenska guiden om Tailwind CSS! Denna guide tar dig från absolut nybörjare till expert genom en noga genomtänkt progressionsmodell.

### Vem är denna guide för?

**För dig som är nybörjare:**
- Har aldrig använt Tailwind CSS tidigare
- Vill förstå grunderna på ett pedagogiskt sätt
- Behöver konkreta exempel och övningar

**För dig som kan vanlig CSS:**
- Vill förstå *varför* Tailwind är annorlunda och bättre för vissa projekt
- Söker en strukturerad väg in i utility-first-tankesättet
- Vill lära dig moderna best practices från start

**För dig som redan använt Tailwind:**
- Vill fördjupa dig i avancerade mönster
- Söker skalbarhetslösningar för större projekt
- Behöver inspiration för arkitektur och struktur

### Hur ska du använda guiden?

Guiden är uppdelad i **5 nivåer** som var och en tar cirka 10–20 minuter att läsa igenom:

1. **Nivå 1 (👶)**: Förstå grundidén – som att förklara för en 5-åring
2. **Nivå 2 (🧒)**: Börja koda med Tailwind – första praktiska kontakten
3. **Nivå 3 (🎓)**: Djupdykning i hur det fungerar under ytan
4. **Nivå 4 (🏛️)**: Avancerade tekniker och best practices
5. **Nivå 5 (💼)**: Masternivå för produktionskod och stora projekt

**Total lästid:** 1,5–3 timmar (beroende på hur mycket du övar)

### Viktigt att veta

- All text och förklaringar är på **svenska**
- All kod, Tailwind-klasser och tekniska termer är på **engelska** (som i verkligheten)
- Varje nivå avslutas med övningar – gör dem för bästa lärande!
- Hoppa inte över nivåer – progressionen är viktig

**Senast uppdaterad:** November 2025 (baserat på Tailwind CSS v3+ med JIT som standard)

---

## Nivå 1: Vad är Tailwind egentligen? 👶

### Introduktion

På denna nivå ska du förstå *vad* Tailwind CSS är och *varför* det existerar – utan att bli överväldigad av teknik. Vi använder vardagsanalogier och enkla bilder för att förklara grundkonceptet. Efter denna nivå kommer du kunna förklara för vem som helst vad Tailwind handlar om!

Detta är viktigt eftersom Tailwind representerar ett helt annat sätt att tänka kring styling jämfört med traditionell CSS. Att förstå tankesättet först gör allt annat mycket enklare.

### Kärnkoncept

#### 1. **Hemsidor behöver kläder (styling)**

Tänk dig att HTML är som en naken person, och CSS är kläderna. Utan CSS ser en hemsida bara ut som ren text i svart och vitt. CSS ger färger, former, avstånd och gör sidan snygg!

#### 2. **Två sätt att klä sig**

**Traditionell CSS** är som att sy egna kläder från scratch:
- Du bestämmer *allt* själv
- Tar lång tid
- Varje plagg är unikt
- Du måste kunna sy (skriva mycket CSS)

**Tailwind CSS** är som att ha en garderob full av färdiga LEGO-bitar:
- Små byggstenar som du kombinerar
- Snabbt att sätta ihop
- Någon annan har gjort det tunga jobbet
- Du fokuserar på att bygga, inte på detaljerna

#### 3. **Vad är "utility-klasser"?**

En **utility-klass** är som en färdig LEGO-bit eller en färgpenna med ett specifikt syfte:
- `text-red-500` = "gör texten röd"
- `bg-blue-200` = "gör bakgrunden ljusblå"
- `p-4` = "lägg till lite luft runt innehållet"

Istället för att skriva:
```css
.min-fina-rubrik {
  color: red;
  font-size: 24px;
  margin-bottom: 10px;
}
```

...så säger du bara till direkt i HTML:en: "jag vill att DEN HÄR texten ska vara röd och stor!"

#### 4. **Varför skulle man vilja ha detta?**

**Traditionell CSS blir rörigt:**
- Du skapar nya klassnamn hela tiden: `.button`, `.button-blue`, `.button-big-blue`, `.special-button`...
- Du glömmer vilka klasser som gör vad
- Du vågar inte ta bort gammal CSS för du vet inte om något använder den

**Tailwind håller ordning:**
- Samma byggstenar överallt
- Du ser direkt vad som händer
- Inget gammalt skräp som samlas

#### 5. **Analogin: LEGO vs. Lera**

**Traditionell CSS** = Forma med lera
- Oändliga möjligheter
- Men varje gång du vill bygga något måste du forma från början
- Svårt att få det exakt likadant två gånger

**Tailwind** = Bygga med LEGO
- Färdiga bitar i olika färger och storlekar
- Snabbt att sätta ihop
- Lätt att göra något liknande igen
- Någon annan har tillverkat bitarna

#### 6. **Ett första smakprov (bara titta, inte koda än!)**

Så här kan en knapp se ut med Tailwind:

```html
<button class="bg-blue-500 text-white p-4 rounded">
  Klicka här!
</button>
```

Vad säger dessa "etiketter" (klasser)?
- `bg-blue-500` = blå bakgrundsfärg
- `text-white` = vit text
- `p-4` = luft runt texten (padding)
- `rounded` = rundade hörn

En människa kan läsa detta och förstå! 🎉

#### 7. **Sammanfattning av grundidén**

Tailwind CSS är ett **verktyg** som ger dig **färdiga byggstenar** (utility-klasser) för att styla hemsidor snabbt och konsekvent. Istället för att skriva egen CSS för varje element, använder du små, återanvändbara klasser direkt i HTML:en.

### Exempel

#### Exempel 1: Från naken text till stylade rubriker

**Utan styling (naken HTML):**
```html
<h1>Välkommen till min hemsida!</h1>
```
Detta ser bara ut som vanlig svart text.

**Med Tailwind-klasser:**
```html
<h1 class="text-4xl text-blue-600 font-bold">
  Välkommen till min hemsida!
</h1>
```

**Vad händer?**
- `text-4xl` = gör texten stor (som storlek 4XL i kläder!)
- `text-blue-600` = färga texten blå
- `font-bold` = gör texten fet

Nu ser rubriken proffsig ut!

#### Exempel 2: Från grå box till färgglad kort

**Naken HTML:**
```html
<div>
  <h2>Min profil</h2>
  <p>Jag heter Anna och älskar att koda!</p>
</div>
```

**Med Tailwind-magi:**
```html
<div class="bg-purple-100 p-6 rounded-lg border border-purple-300">
  <h2 class="text-2xl font-semibold text-purple-800">Min profil</h2>
  <p class="text-gray-700">Jag heter Anna och älskar att koda!</p>
</div>
```

**Vad gjorde vi?**
- `bg-purple-100` = ljuslila bakgrund
- `p-6` = ganska mycket luft runt innehållet
- `rounded-lg` = stora rundade hörn (large)
- `border border-purple-300` = en ram runt boxen i lila
- Texten fick olika storlekar och färger

#### Exempel 3: Knapp som ändras när du håller musen över

```html
<button class="bg-green-500 hover:bg-green-700 text-white px-6 py-3 rounded-full">
  Skicka meddelande
</button>
```

**Vad är nytt här?**
- `bg-green-500` = grön bakgrund
- `hover:bg-green-700` = när du håller musen över blir den mörkare grön!
- `px-6` = luft på sidorna (padding x-axis)
- `py-3` = luft ovanför och under (padding y-axis)
- `rounded-full` = helt rundad (som en kapsel)

**Det magiska:** `hover:` är ett prefix som betyder "när musen är över denna"!

### Visualisering: Så här tänker Tailwind

```
Traditional CSS Workflow:
┌─────────────┐
│   HTML      │ → Behöver styling!
└─────────────┘
      ↓
┌─────────────┐
│ Skriv CSS   │ → .min-klass { color: red; ... }
└─────────────┘
      ↓
┌─────────────┐
│ Länka till  │ → <div class="min-klass">
│   HTML      │
└─────────────┘

Tailwind Workflow:
┌─────────────┐
│   HTML      │ → Behöver styling!
└─────────────┘
      ↓
┌─────────────────────────────────┐
│ Använd färdiga utility-klasser  │ → <div class="text-red-500 p-4">
└─────────────────────────────────┘
      ↓
┌─────────────┐
│   KLART!    │ ✓
└─────────────┘
```

### 💡 Pro Tips

#### Tip 1: Tänk som LEGO-byggare, inte konstnär
När du använder Tailwind, tänk inte "hur ska jag skapa denna unika stil?" utan "vilka färdiga bitar kan jag kombinera för att få det jag vill?". Detta mindset-skifte är nyckeln!

#### Tip 2: Det är okej att klassen blir lång
I början känns det konstigt att ha många klasser på ett element:
```html
<div class="bg-white p-6 rounded-lg shadow-lg border border-gray-200">
```
Men detta är *helt normalt* i Tailwind! Det är bättre än att ha CSS utspridd på 10 olika ställen.

#### Tip 3: Du behöver inte lära dig allt utantill
Det finns hundratals Tailwind-klasser. Ingen kan alla! Du lär dig de vanligaste med tiden, och för resten tittar du i dokumentationen. Det är som att lära sig ord i ett språk – börja med det viktiga.

### ✏️ Övningar

#### Övning 1: Bildtolkning (konceptuell)
**Uppgift:** Läs dessa klasser och förklara med egna ord vad som händer:
```html
<p class="text-lg text-gray-800 italic">
  En viktig mening.
</p>
```

**Facit:**
- `text-lg` = texten är lite större än vanligt (large)
- `text-gray-800` = texten är mörkgrå
- `italic` = texten är kursiv (lutande)

**Sammanfattning:** En större, mörkgrå, kursiv text!

#### Övning 2: Gissa resultatet
**Uppgift:** Vilken av dessa knappar ser mest inbjudande ut för att klicka på? Varför?

**Knapp A:**
```html
<button class="bg-gray-300 text-gray-600 p-2">
  Klicka
</button>
```

**Knapp B:**
```html
<button class="bg-blue-500 text-white px-6 py-3 rounded-lg shadow-md hover:bg-blue-600">
  Klicka
</button>
```

**Facit:**
Knapp B ser mer inbjudande ut eftersom:
- Blå färg (handlingskraft) istället för grå
- Vit text som syns bättre
- Mer padding (px-6 py-3) = större klickyta
- Rundade hörn (rounded-lg) = mjukare intryck
- Skugga (shadow-md) = ser ut att "sticka fram" från sidan
- Ändrar färg vid hover = interaktiv feedback

#### Övning 3: Bygg i huvudet
**Uppgift:** Om du vill göra en orange varningsruta med vit text och lite luft runt, vilka klasser skulle du gissa att du behöver? (Försök gissa innan du tittar på facit!)

Tänk på:
- Bakgrundsfärg (bg-...)
- Textfärg (text-...)
- Luft runt innehåll (p-...)

**Facit (en möjlig lösning):**
```html
<div class="bg-orange-500 text-white p-4">
  Varning! Något viktigt här.
</div>
```

Det viktiga är inte att du gissade exakt rätt klassnamn, utan att du förstod *konceptet*: "bakgrundsfärg + textfärg + padding"!

### 📝 Sammanfattning

**Key Takeaways:**

✅ Tailwind CSS är ett **verktyg** med färdiga **byggstenar** (utility-klasser) för styling
✅ Istället för att skriva egen CSS använder du **små, beskrivande klasser** direkt i HTML
✅ Tänk **LEGO**, inte lera – kombinera färdiga bitar istället för att forma från scratch
✅ Klasser som `bg-blue-500`, `text-white`, `p-4` beskriver **exakt vad de gör**
✅ Det är **normalt** att ha många klasser på ett element
✅ Du behöver **inte kunna allt utantill** – lär dig de vanligaste, slå upp resten

**Ny ordlista (Nivå 1):**

- **Utility-klass**: En färdig CSS-klass som gör EN sak (t.ex. "gör text röd")
- **Tailwind CSS**: Ett ramverk med hundratals färdiga utility-klasser
- **Utility-first**: Tankesättet att bygga design genom att kombinera små klasser
- **Hover**: När muspekaren är över ett element
- **Padding**: Luften/utrymmet *inuti* ett element runt innehållet

**Nästa steg:**

Nu när du förstår *vad* Tailwind är och *varför* det existerar är du redo för Nivå 2! Där börjar vi faktiskt **koda** med Tailwind och lär oss de viktigaste klasserna ordentligt.

---

## Nivå 2: Första riktiga kontakten med Tailwind 🧒

### Introduktion

Nu är det dags att bli praktisk! På denna nivå kommer du lära dig de mest användbara Tailwind-klasserna och hur du faktiskt använder dem. Vi kommer också introducera responsiv design (så att din hemsida ser bra ut på mobiler och datorer) och interaktivitet (som hover-effekter).

Detta är viktigt eftersom dessa grundläggande klasser utgör 80% av vad du kommer använda i ditt dagliga arbete. När du bemästrar dessa kommer du kunna bygga nästan vad som helst!

### Kärnkoncept

#### 1. **Utility-klasser: De viktigaste kategorierna**

Tailwind har hundratals klasser, men de grupperas i logiska kategorier:

**Layout & Spacing:**
- `p-{number}` = padding (luft inuti)
- `m-{number}` = margin (luft utanför)
- `w-{number}` = width (bredd)
- `h-{number}` = height (höjd)

**Typografi:**
- `text-{size}` = textstorlek (xs, sm, base, lg, xl, 2xl, 3xl, 4xl...)
- `font-{weight}` = tjocklek (thin, normal, medium, semibold, bold, black)
- `text-{color}` = färg (red-500, blue-600, gray-800...)

**Färger:**
- `bg-{color}` = bakgrundsfärg
- `text-{color}` = textfärg
- `border-{color}` = kantfärg

**Visuella effekter:**
- `rounded-{size}` = rundade hörn (sm, md, lg, xl, full)
- `shadow-{size}` = skugga (sm, md, lg, xl)
- `border-{width}` = kantlinje (border, border-2, border-4)

#### 2. **Färgsystemet (viktigaste att förstå!)**

Tailwind använder ett färgsystem med **färgnamn** och **nyanser**:

```
text-{färg}-{nyans}
      ↓       ↓
  blue-500
  ↑       ↑
färg   intensitet
```

**Färger:** red, orange, yellow, green, blue, indigo, purple, pink, gray

**Nyanser:** 50 (ljusast) → 100 → 200 → ... → 900 (mörkast)

**Exempel:**
- `bg-blue-50` = nästan vit med en blå ton
- `bg-blue-500` = mitt i blå-skalan (standardblå)
- `bg-blue-900` = mörk, nästan svart blå

#### 3. **Spacing-skalan (hur mycket luft?)**

Tailwind använder nummer för att beskriva avstånd:

| Klass | Storlek | Exempel användning |
|-------|---------|-------------------|
| `p-0` | 0px | Ingen padding alls |
| `p-1` | 0.25rem (4px) | Minimal luft |
| `p-2` | 0.5rem (8px) | Lite luft |
| `p-4` | 1rem (16px) | **Vanligast!** Normal luft |
| `p-6` | 1.5rem (24px) | Ganska mycket luft |
| `p-8` | 2rem (32px) | Mycket luft |
| `p-12` | 3rem (48px) | Extra mycket luft |

**Pro tip:** Du behöver inte lära dig pixelvärdena! Tänk bara: större nummer = mer luft.

#### 4. **Riktningsspecifika spacing**

Du kan lägga till luft på specifika sidor:

- `pt-4` = padding-top (ovanför)
- `pb-4` = padding-bottom (nedanför)
- `pl-4` = padding-left (vänster)
- `pr-4` = padding-right (höger)
- `px-4` = padding på x-axeln (vänster + höger)
- `py-4` = padding på y-axeln (upp + ner)

Samma logik fungerar för margin: `mt-4`, `mb-4`, `mx-4`, `my-4` osv.

#### 5. **Responsiva breakpoints (Mobile First!)**

Tailwind använder en **mobile-first**-approach. Det betyder:

**Utan prefix** = fungerar på alla skärmstorlekar (börja här!)
```html
<div class="text-sm">Liten text på alla enheter</div>
```

**Med prefix** = fungerar från den storleken och uppåt
```html
<div class="text-sm md:text-lg">
  Liten på mobil, större på surfplattor och datorer
</div>
```

**Breakpoints (viktiga att lära sig!):**

| Prefix | Skärmstorlek | Beskrivning |
|--------|--------------|-------------|
| (inget) | Alla storlekar | Din bas-styling |
| `sm:` | ≥ 640px | Stora mobiler (landscape) |
| `md:` | ≥ 768px | Surfplattor |
| `lg:` | ≥ 1024px | Laptops |
| `xl:` | ≥ 1280px | Större skärmar |
| `2xl:` | ≥ 1536px | Stora desktop-skärmar |

**Tänk så här:** Börja med mobilen, lägg sedan till ändringar för större skärmar!

#### 6. **Interaktiva states (hover, focus, active)**

Gör dina element interaktiva med **state-prefix**:

**Hover** (när musen är över):
```html
<button class="bg-blue-500 hover:bg-blue-700">
  Blir mörkare när du hovrar!
</button>
```

**Focus** (när elementet är valt, t.ex. i ett formulär):
```html
<input class="border-gray-300 focus:border-blue-500" />
```

**Active** (när du klickar):
```html
<button class="bg-blue-500 active:bg-blue-800">
  Blir mörkast när du klickar!
</button>
```

**Kombinera med responsivitet!**
```html
<button class="bg-blue-500 hover:bg-blue-700 md:text-lg">
  Större text på desktop, alltid mörkare vid hover
</button>
```

#### 7. **Flexbox basics (för layout)**

Flexbox är det vanligaste sättet att arrangera element i Tailwind:

```html
<div class="flex">
  <!-- Barnen hamnar bredvid varandra -->
</div>
```

**Vanliga kombinationer:**

```html
<!-- Centrerar allt både horisontellt och vertikalt -->
<div class="flex items-center justify-center">
  Jag är centrerad!
</div>

<!-- Sprider ut element jämnt -->
<div class="flex justify-between">
  <div>Vänster</div>
  <div>Höger</div>
</div>

<!-- Vertikalt staplade element med mellanrum -->
<div class="flex flex-col gap-4">
  <div>Första</div>
  <div>Andra</div>
</div>
```

### Exempel

#### Exempel 1: En professionell knapp (steg för steg)

**Steg 1: Börja enkelt**
```html
<button>Klicka här</button>
```
Detta är bara en tråkig knapp.

**Steg 2: Lägg till färg och padding**
```html
<button class="bg-blue-500 text-white px-6 py-3">
  Klicka här
</button>
```
Nu börjar det likna något!
- `bg-blue-500` = blå bakgrund
- `text-white` = vit text
- `px-6` = luft på sidorna
- `py-3` = luft ovanför/under

**Steg 3: Gör den snyggare med rundade hörn**
```html
<button class="bg-blue-500 text-white px-6 py-3 rounded-lg">
  Klicka här
</button>
```
- `rounded-lg` = stora rundade hörn

**Steg 4: Lägg till hover-effekt**
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white px-6 py-3 rounded-lg">
  Klicka här
</button>
```
- `hover:bg-blue-700` = mörkare när musen är över

**Steg 5: Lägg till skugga och transition**
```html
<button class="bg-blue-500 hover:bg-blue-700 text-white px-6 py-3 rounded-lg shadow-md hover:shadow-lg transition">
  Klicka här
</button>
```
- `shadow-md` = medel skugga
- `hover:shadow-lg` = större skugga vid hover
- `transition` = mjuk övergång mellan states

**Färdigt!** En proffsig knapp på 1 rad HTML! 🎉

#### Exempel 2: Ett responsivt profilkort

```html
<div class="bg-white rounded-xl shadow-lg p-6 max-w-sm mx-auto">
  <!-- Profilbild -->
  <div class="w-24 h-24 bg-gradient-to-r from-blue-400 to-purple-500 rounded-full mx-auto mb-4"></div>

  <!-- Namn -->
  <h2 class="text-2xl font-bold text-center text-gray-800 mb-2">
    Anna Andersson
  </h2>

  <!-- Titel -->
  <p class="text-center text-gray-600 mb-4">
    Frontend-utvecklare
  </p>

  <!-- Beskrivning -->
  <p class="text-gray-700 text-sm leading-relaxed mb-6">
    Passionerad om att skapa vackra användargränssnitt med modern teknik.
    Älskar Tailwind CSS!
  </p>

  <!-- Knapp -->
  <button class="w-full bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-lg transition">
    Kontakta mig
  </button>
</div>
```

**Vad händer här?**

**Yttre container:**
- `bg-white` = vit bakgrund
- `rounded-xl` = extra rundade hörn
- `shadow-lg` = stor skugga (sticker ut från sidan)
- `p-6` = luft inuti
- `max-w-sm` = max-bredd (small)
- `mx-auto` = centrerar kortet horisontellt

**Profilbild:**
- `w-24 h-24` = 24 units bred och hög (kvadrat)
- `bg-gradient-to-r from-blue-400 to-purple-500` = gradient från blå till lila
- `rounded-full` = helt rund
- `mx-auto mb-4` = centrerad med lite luft under

**Textelement:**
- Olika storlekar (`text-2xl`, `text-sm`)
- Olika vikter (`font-bold`, normal)
- Olika färger (`text-gray-800`, `text-gray-600`, `text-gray-700`)
- `text-center` = centrerad text
- `leading-relaxed` = mer radavstånd för lättare läsning

**Knapp:**
- `w-full` = hela bredden av containern
- Färg + hover + transition (som vi lärt oss!)

#### Exempel 3: Responsiv layout (mobil → desktop)

```html
<div class="container mx-auto px-4">
  <!-- Header -->
  <header class="py-6">
    <h1 class="text-2xl md:text-4xl font-bold text-gray-900">
      Min Portfolio
    </h1>
  </header>

  <!-- Grid med projekt -->
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Projekt 1 -->
    <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition">
      <h3 class="text-xl font-semibold mb-2">Projekt 1</h3>
      <p class="text-gray-600">En cool webbapp</p>
    </div>

    <!-- Projekt 2 -->
    <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition">
      <h3 class="text-xl font-semibold mb-2">Projekt 2</h3>
      <p class="text-gray-600">En annan cool app</p>
    </div>

    <!-- Projekt 3 -->
    <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-xl transition">
      <h3 class="text-xl font-semibold mb-2">Projekt 3</h3>
      <p class="text-gray-600">Ännu en app</p>
    </div>
  </div>
</div>
```

**Responsiv magi:**

**Rubriken:**
- `text-2xl` = 2XL på mobil
- `md:text-4xl` = 4XL på surfplattor och uppåt

**Grid-layouten:**
- `grid-cols-1` = 1 kolumn på mobil (allt staplas)
- `md:grid-cols-2` = 2 kolumner på surfplattor
- `lg:grid-cols-3` = 3 kolumner på laptops

**Resultat:**
- 📱 Mobil: Allt staplas vertikalt
- 📱 Surfplatta: 2 kolumner
- 💻 Desktop: 3 kolumner

### Visualisering: Vanligaste klasserna (skriv ut denna!)

```
┌─────────────────────────────────────────────────────────┐
│             TAILWIND CHEAT SHEET (Nivå 2)              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  SPACING (Padding & Margin)                            │
│  ────────────────────────────────                      │
│  p-4    = padding överallt                             │
│  px-4   = padding vänster/höger                        │
│  py-4   = padding upp/ner                              │
│  pt-4   = padding top                                  │
│  m-4    = margin (samma logik som padding)             │
│                                                         │
│  FÄRGER                                                 │
│  ────────                                               │
│  bg-blue-500      = blå bakgrund                       │
│  text-gray-800    = mörkgrå text                       │
│  border-red-300   = ljusröd kant                       │
│                                                         │
│  TYPOGRAFI                                              │
│  ──────────                                             │
│  text-sm / text-lg / text-2xl  = storlekar             │
│  font-bold / font-semibold     = vikter                │
│  text-center / text-left       = justering             │
│                                                         │
│  LAYOUT                                                 │
│  ──────                                                 │
│  flex              = flexbox                            │
│  items-center      = centrerar vertikalt               │
│  justify-center    = centrerar horisontellt            │
│  gap-4             = mellanrum mellan barn             │
│  grid grid-cols-3  = 3 kolumner                        │
│                                                         │
│  VISUELLT                                               │
│  ────────                                               │
│  rounded-lg        = rundade hörn                       │
│  shadow-md         = skugga                             │
│  border border-2   = kantlinje                          │
│                                                         │
│  INTERAKTIVITET                                         │
│  ──────────────                                         │
│  hover:bg-blue-700  = ändra vid hover                  │
│  focus:ring-2       = ring vid focus                   │
│  transition         = mjuka övergångar                 │
│                                                         │
│  RESPONSIVITET                                          │
│  ─────────────                                          │
│  md:text-lg        = större text på surfplattor+       │
│  lg:grid-cols-3    = 3 kolumner på laptop+             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Tip 1: Börja alltid med mobilen (Mobile First!)
Skriv din bas-styling utan prefix först. Lägg sedan till `md:`, `lg:` etc för större skärmar. Detta är mycket lättare än att tänka tvärtom!

**Bra:**
```html
<div class="text-sm md:text-lg">
  Liten på mobil, stor på desktop
</div>
```

**Mindre bra:**
```html
<!-- Försök inte tänka "desktop först" -->
```

#### Tip 2: Använd konsekvent spacing-skala
Håll dig till Tailwinds spacing-skala (4, 6, 8, 12, 16...) istället för att blanda olika värden. Detta ger konsekvent design automatiskt!

**Bra:** `p-4`, `p-6`, `p-8` (multiplar av 4)
**Mindre bra:** Blanda `p-5`, `p-7`, `p-11` (konstigare värden)

#### Tip 3: Gruppera klasser logiskt i huvudet
När du skriver många klasser, gruppera dem mentalt:

```html
<div class="
  bg-white rounded-lg shadow-md     ← Grundläggande utseende
  p-6 max-w-lg mx-auto              ← Layout och spacing
  hover:shadow-xl transition        ← Interaktivitet
  md:p-8 lg:max-w-2xl               ← Responsivitet
">
```

Detta gör koden lättare att läsa och uppdatera!

### ✏️ Övningar

#### Övning 1: Bygg en enkel knapp
**Uppgift:** Skapa en grön knapp med vit text, padding, rundade hörn som blir mörkare vid hover.

**Hjälp:** Du behöver:
- Grön bakgrund: `bg-green-???`
- Vit text: `text-white`
- Padding: `px-?` och `py-?`
- Rundade hörn: `rounded-?`
- Hover: `hover:bg-green-???` (mörkare nyans)

**Facit:**
```html
<button class="bg-green-500 hover:bg-green-700 text-white px-6 py-3 rounded-lg">
  Min gröna knapp
</button>
```

**Alternativa lösningar:**
- `bg-green-600` och `hover:bg-green-800` (mörkare grundfärg)
- `rounded-md` eller `rounded-xl` (olika hörn-rundning)
- `px-8 py-4` (mer padding)

Allt detta fungerar! Experimentera!

#### Övning 2: Centrera en box
**Uppgift:** Skapa en vit box med skugga som är centrerad på sidan, med lite text inuti.

**Hjälp:** Du behöver:
- Vit bakgrund: `bg-white`
- Skugga: `shadow-??`
- Max-bredd: `max-w-??`
- Centrering: `mx-auto`
- Padding inuti: `p-??`

**Facit:**
```html
<div class="bg-white shadow-lg rounded-lg p-8 max-w-md mx-auto">
  <h2 class="text-2xl font-bold mb-4">Min centrerade box</h2>
  <p class="text-gray-700">Detta är innehållet i min box!</p>
</div>
```

#### Övning 3: Responsiv text
**Uppgift:** Skapa en rubrik som är liten på mobil, medelstor på surfplattor och stor på desktop.

**Facit:**
```html
<h1 class="text-xl md:text-3xl lg:text-5xl font-bold">
  Jag växer med skärmen!
</h1>
```

**Förklaring:**
- Mobil: `text-xl` (extra large)
- Surfplatta (md): `text-3xl` (3x extra large)
- Desktop (lg): `text-5xl` (5x extra large)

#### Övning 4: Enkel card-komponent
**Uppgift:** Bygg ett kort (card) med:
- Vit bakgrund
- Rundade hörn
- Skugga
- En rubrik
- En beskrivning
- En knapp längst ner

**Facit:**
```html
<div class="bg-white rounded-xl shadow-md p-6 max-w-sm">
  <!-- Rubrik -->
  <h3 class="text-xl font-bold text-gray-900 mb-2">
    Kortets rubrik
  </h3>

  <!-- Beskrivning -->
  <p class="text-gray-600 mb-4">
    En kort beskrivning av vad detta kort handlar om.
  </p>

  <!-- Knapp -->
  <button class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg w-full transition">
    Läs mer
  </button>
</div>
```

#### Övning 5: Flexbox-layout
**Uppgift:** Skapa en header med:
- En logotyp till vänster
- Navigeringslänkar till höger
- Allt vertikalt centrerat

**Facit:**
```html
<header class="bg-gray-900 text-white">
  <div class="container mx-auto px-4 py-4 flex items-center justify-between">
    <!-- Logo -->
    <div class="text-2xl font-bold">
      MinSite
    </div>

    <!-- Navigation -->
    <nav class="flex gap-6">
      <a href="#" class="hover:text-blue-400 transition">Hem</a>
      <a href="#" class="hover:text-blue-400 transition">Om</a>
      <a href="#" class="hover:text-blue-400 transition">Kontakt</a>
    </nav>
  </div>
</header>
```

**Förklaring:**
- `flex items-center justify-between` = flexbox med innehåll vertikalt centrerat och spritt mellan vänster/höger
- `gap-6` = mellanrum mellan navigeringslänkar
- `container mx-auto px-4` = centrerad container med padding på sidorna

### 📝 Sammanfattning

**Key Takeaways:**

✅ **Färgsystemet** fungerar som `text-{färg}-{nyans}` där nyans går från 50 (ljus) till 900 (mörk)
✅ **Spacing** använder en logisk skala: p-4, p-6, p-8... (större nummer = mer utrymme)
✅ **Mobile First** betyder att du börjar utan prefix, lägger sedan till `md:`, `lg:` för större skärmar
✅ **Interaktivitet** skapas med `hover:`, `focus:`, `active:` prefix
✅ **Flexbox** är ditt bästa verktyg för layout: `flex`, `items-center`, `justify-between`, `gap-4`
✅ **Gruppera klasser** logiskt i huvudet: utseende, layout, interaktivitet, responsivitet

**Ny ordlista (Nivå 2):**

- **Breakpoint**: En skärmstorlek där design ändras (sm, md, lg, xl, 2xl)
- **Mobile First**: Designa för mobil först, lägg till för större skärmar sedan
- **State**: Ett elements tillstånd (hover, focus, active)
- **Flexbox**: Ett layoutsystem för att arrangera element flexibelt
- **Container**: En wrapper som begränsar maxbredd och centrerar innehåll
- **Gradient**: En färgövergång från en färg till en annan
- **Transition**: Mjuk animering mellan två states
- **Gap**: Mellanrum mellan element i flex eller grid

**Nästa steg:**

Nu kan du faktiskt *bygga* med Tailwind! I Nivå 3 går vi djupare och lär oss hur Tailwind fungerar under huven, hur du konfigurerar det för dina projekt, och hur du skapar återanvändbara komponenter. Det är dags att gå från att använda Tailwind till att *bemästra* det!

---

## Nivå 3: Hur Tailwind faktiskt funkar under huven 🎓

### Introduktion

Nu är det dags att lyfta på motorhuven! På denna nivå kommer du förstå hur Tailwind genererar CSS, hur du konfigurerar och anpassar ramverket för ditt projekt, och hur du bygger återanvändbara komponenter på rätt sätt.

Detta är viktigt eftersom förståelsen för hur Tailwind fungerar gör dig till en mycket mer effektiv utvecklare. Du kommer kunna felsöka problem, optimera din kod och anpassa ramverket exakt efter dina behov.

### Kärnkoncept

#### 1. **Hur Tailwind genererar CSS (JIT-läget)**

Sedan Tailwind v3.0 är **JIT (Just-In-Time)** mode standard. Så här fungerar det:

**Klassiska CSS-ramverk:**
```
Alla möjliga klasser → Gigantisk CSS-fil → Ta bort oanvänt (purge)
```

**Tailwind JIT (2025):**
```
Skanna dina filer → Hitta klasser → Generera ENDAST den CSS som används
```

**Processen:**

1. **Konfiguration:** Du anger vilka filer Tailwind ska skanna (i `content`-arrayen)
2. **Scanning:** Tailwind läser dina HTML/JSX/Vue-filer och letar efter klassnamn
3. **Generering:** Skapar CSS *endast* för de klasser du faktiskt använder
4. **Optimering:** Produktionsversionen är minimal (ofta <10kB!)

**Fördelar med JIT:**
- ⚡ Blixtsnabb kompilering (800ms vs 30-45s i gamla läget)
- 🎨 Alla varianter fungerar direkt (hover:, focus:, md: etc)
- 🔢 Arbiträra värden: `w-[347px]`, `text-[#1da1f2]`
- 📦 Minimal bundle-storlek

#### 2. **tailwind.config.js – Din kontrolltorn**

Detta är Tailwinds konfigurationsfil. Här anpassar du allt!

**Grundstruktur:**

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/**/*.{html,js,jsx,ts,tsx}',
    './pages/**/*.{html,js,jsx,ts,tsx}',
  ],
  theme: {
    extend: {
      // Dina anpassningar här
    },
  },
  plugins: [],
}
```

**Viktiga sektioner:**

**a) `content` - Vart ska Tailwind leta?**
```javascript
content: [
  './src/**/*.{html,js,jsx,ts,tsx}',  // Alla filer i src/
  './components/**/*.vue',             // Vue-komponenter
  './app/**/*.{ts,tsx}',              // Next.js app-mapp
]
```

**VARNING:** Om en fil inte finns i `content`-arrayen kommer dess klasser inte genereras!

**b) `theme.extend` - Lägg till utan att ersätta**
```javascript
theme: {
  extend: {
    colors: {
      'brand-blue': '#0066cc',
      'brand-green': '#00cc66',
    },
    spacing: {
      '128': '32rem',
      '144': '36rem',
    },
    fontFamily: {
      'headline': ['Montserrat', 'sans-serif'],
    },
  },
}
```

Nu kan du använda `text-brand-blue`, `p-128`, `font-headline`!

**c) `theme` (utan extend) - Ersätt helt**
```javascript
theme: {
  colors: {
    // VARNING: Detta ersätter ALLA defaultfärger!
    'primary': '#0066cc',
    'secondary': '#00cc66',
  },
}
```

**Tumregel:** Använd nästan alltid `extend` för att behålla Tailwinds default-värden!

#### 3. **@layer - Organisera din egen CSS**

Tailwind har tre **lager** för CSS:

```css
@layer base {
  /* Grundläggande HTML-resets och bas-styling */
}

@layer components {
  /* Återanvändbara komponent-klasser */
}

@layer utilities {
  /* Egna utility-klasser */
}
```

**Varför använda @layer?**
- Kontrollerar i vilken ordning CSS läses in
- Säkerställer korrekt specificity (viktighet)
- Gör koden mer organiserad

**Exempel:**

```css
@layer base {
  h1 {
    @apply text-4xl font-bold;
  }

  h2 {
    @apply text-3xl font-semibold;
  }
}

@layer components {
  .btn-primary {
    @apply bg-blue-500 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition;
  }

  .card {
    @apply bg-white rounded-xl shadow-lg p-6;
  }
}

@layer utilities {
  .text-shadow {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  }
}
```

#### 4. **@apply - Extrahera upprepade mönster**

`@apply` låter dig använda Tailwind-klasser i vanlig CSS:

```css
.btn {
  @apply px-4 py-2 rounded font-semibold transition;
}

.btn-blue {
  @apply btn bg-blue-500 text-white hover:bg-blue-700;
}
```

**När ska du använda @apply?**

✅ **Bra användning:**
- Upprepad komponent med 10+ klasser som används många gånger
- Komponenter som behövs i många projekt
- Bas-element som ska se likadana ut överallt

❌ **Undvik @apply för:**
- Enstaka element (använd klasser direkt i HTML)
- Variationer som bara skiljer sig lite (använd props/conditional classes istället)
- Allt – då förlorar du fördelarna med utility-first!

**Exempel - Bra användning:**

```css
/* components.css */
@layer components {
  .form-input {
    @apply w-full px-4 py-2 border border-gray-300 rounded-lg
           focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
           transition;
  }

  .form-label {
    @apply block text-sm font-medium text-gray-700 mb-2;
  }
}
```

Nu i HTML:
```html
<label class="form-label">Email</label>
<input type="email" class="form-input" />
```

Mycket cleanare än 15+ klasser på varje input-fält!

#### 5. **Flexbox och Grid i Tailwind (djupdykning)**

**Flexbox-mönster:**

```html
<!-- Klassisk navbar -->
<div class="flex items-center justify-between">
  <div>Logo</div>
  <div>Navigation</div>
</div>

<!-- Centrerad hero-sektion -->
<div class="flex items-center justify-center min-h-screen">
  <div>Centrerat innehåll</div>
</div>

<!-- Card-layout med gap -->
<div class="flex flex-wrap gap-4">
  <div class="flex-1">Card 1</div>
  <div class="flex-1">Card 2</div>
  <div class="flex-1">Card 3</div>
</div>
```

**Viktiga flex-klasser:**

| Klass | Vad den gör |
|-------|-------------|
| `flex` | Aktiverar flexbox |
| `flex-col` | Staplar barn vertikalt |
| `flex-row` | Barn horisontellt (default) |
| `flex-wrap` | Tillåter radbrytning |
| `flex-1` | Element tar lika mycket plats |
| `items-start/center/end` | Justering vertikalt |
| `justify-start/center/end/between` | Justering horisontellt |
| `gap-4` | Mellanrum mellan element |

**Grid-mönster:**

```html
<!-- Enkel 3-kolumns grid -->
<div class="grid grid-cols-3 gap-4">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
  <div>6</div>
</div>

<!-- Responsiv grid -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
  <!-- Element här -->
</div>

<!-- Komplex layout -->
<div class="grid grid-cols-12 gap-4">
  <div class="col-span-8">Huvudinnehåll (8/12)</div>
  <div class="col-span-4">Sidebar (4/12)</div>
</div>
```

**Viktiga grid-klasser:**

| Klass | Vad den gör |
|-------|-------------|
| `grid` | Aktiverar grid |
| `grid-cols-3` | 3 kolumner |
| `grid-rows-2` | 2 rader |
| `col-span-2` | Element tar 2 kolumner |
| `row-span-2` | Element tar 2 rader |
| `gap-4` | Mellanrum mellan celler |

#### 6. **Arbiträra värden (super-kraft i JIT!)**

Behöver du ett specifikt värde som inte finns i Tailwinds skala?

```html
<!-- Exakt bredd -->
<div class="w-[347px]">Exakt 347px bred</div>

<!-- Custom färg -->
<div class="bg-[#1da1f2] text-[rgb(123,45,67)]">Twitter-blå bakgrund</div>

<!-- Specifik padding -->
<div class="p-[17px]">17px padding</div>

<!-- Grid med custom kolumner -->
<div class="grid grid-cols-[200px_1fr_1fr]">
  <!-- Första kolumnen 200px, resten flexibelt -->
</div>
```

**Tips:** Använd arbiträra värden sparsamt! Stick till Tailwinds skala när det går – det ger konsekvent design.

#### 7. **Dark mode i Tailwind**

Tailwind har inbyggt stöd för dark mode!

**Metod 1: Media-baserad (automatiskt enligt system)**

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'media',
  // ...
}
```

```html
<div class="bg-white dark:bg-gray-900 text-black dark:text-white">
  Anpassar sig efter systemets dark mode
</div>
```

**Metod 2: Class-baserad (kontrollerad med JavaScript)**

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  // ...
}
```

```html
<!-- Lägg till 'dark' på html eller body -->
<html class="dark">
  <body>
    <div class="bg-white dark:bg-gray-900">
      Dark mode aktivt när 'dark' class finns!
    </div>
  </body>
</html>
```

**Toggle dark mode (React-exempel):**

```javascript
// Toggle dark mode
const toggleDarkMode = () => {
  document.documentElement.classList.toggle('dark');
}
```

### Exempel

#### Exempel 1: Komplett projektsetup (steg för steg)

**1. Installera Tailwind:**

```bash
npm install -D tailwindcss
npx tailwindcss init
```

**2. Konfigurera `tailwind.config.js`:**

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'primary': {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          900: '#1e3a8a',
        },
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
      spacing: {
        '128': '32rem',
      },
    },
  },
  plugins: [],
}
```

**3. Skapa `src/input.css`:**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn {
    @apply px-6 py-3 rounded-lg font-semibold transition;
  }

  .btn-primary {
    @apply btn bg-primary-500 text-white hover:bg-primary-900;
  }
}
```

**4. Bygg CSS:**

```bash
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```

**5. Använd i HTML:**

```html
<!DOCTYPE html>
<html>
<head>
  <link href="/dist/output.css" rel="stylesheet">
</head>
<body class="font-sans">
  <button class="btn-primary">
    Min custom knapp!
  </button>
</body>
</html>
```

#### Exempel 2: Skapa ett återanvändbart komponent-system

**components.css:**

```css
@layer components {
  /* Cards */
  .card {
    @apply bg-white rounded-xl shadow-lg overflow-hidden;
  }

  .card-header {
    @apply px-6 py-4 border-b border-gray-200;
  }

  .card-body {
    @apply p-6;
  }

  .card-footer {
    @apply px-6 py-4 bg-gray-50 border-t border-gray-200;
  }

  /* Buttons */
  .btn {
    @apply px-6 py-3 rounded-lg font-semibold transition cursor-pointer inline-block text-center;
  }

  .btn-primary {
    @apply btn bg-blue-500 text-white hover:bg-blue-700;
  }

  .btn-secondary {
    @apply btn bg-gray-500 text-white hover:bg-gray-700;
  }

  .btn-outline {
    @apply btn border-2 border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white;
  }

  /* Forms */
  .form-group {
    @apply mb-4;
  }

  .form-label {
    @apply block text-sm font-medium text-gray-700 mb-2;
  }

  .form-input {
    @apply w-full px-4 py-2 border border-gray-300 rounded-lg
           focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent;
  }

  .form-error {
    @apply text-red-500 text-sm mt-1;
  }
}
```

**Användning:**

```html
<div class="card">
  <div class="card-header">
    <h3 class="text-xl font-bold">Kontaktformulär</h3>
  </div>
  <div class="card-body">
    <div class="form-group">
      <label class="form-label">Email</label>
      <input type="email" class="form-input" placeholder="din@email.se" />
    </div>

    <div class="form-group">
      <label class="form-label">Meddelande</label>
      <textarea class="form-input" rows="4"></textarea>
    </div>
  </div>
  <div class="card-footer">
    <button class="btn-primary">Skicka</button>
    <button class="btn-outline ml-2">Avbryt</button>
  </div>
</div>
```

#### Exempel 3: Avancerad responsiv dashboard-layout

```html
<div class="min-h-screen bg-gray-100">
  <!-- Topbar -->
  <header class="bg-white border-b border-gray-200 sticky top-0 z-10">
    <div class="flex items-center justify-between px-6 py-4">
      <h1 class="text-2xl font-bold text-gray-900">Dashboard</h1>
      <div class="flex items-center gap-4">
        <button class="text-gray-600 hover:text-gray-900">
          <span class="text-xl">🔔</span>
        </button>
        <div class="w-10 h-10 bg-blue-500 rounded-full"></div>
      </div>
    </div>
  </header>

  <!-- Main layout -->
  <div class="flex">
    <!-- Sidebar (döljs på mobil, syns på desktop) -->
    <aside class="hidden lg:block w-64 bg-white border-r border-gray-200 min-h-screen">
      <nav class="p-4">
        <a href="#" class="block px-4 py-2 rounded-lg bg-blue-50 text-blue-600 font-medium mb-2">
          Översikt
        </a>
        <a href="#" class="block px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-700 mb-2">
          Projekt
        </a>
        <a href="#" class="block px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-700 mb-2">
          Team
        </a>
        <a href="#" class="block px-4 py-2 rounded-lg hover:bg-gray-50 text-gray-700 mb-2">
          Inställningar
        </a>
      </nav>
    </aside>

    <!-- Content area -->
    <main class="flex-1 p-6">
      <!-- Stats grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        <div class="bg-white rounded-lg shadow p-6">
          <div class="text-sm text-gray-600 mb-2">Totala användare</div>
          <div class="text-3xl font-bold text-gray-900">24,532</div>
          <div class="text-sm text-green-600 mt-2">↑ 12% från förra månaden</div>
        </div>

        <div class="bg-white rounded-lg shadow p-6">
          <div class="text-sm text-gray-600 mb-2">Intäkter</div>
          <div class="text-3xl font-bold text-gray-900">$45,234</div>
          <div class="text-sm text-green-600 mt-2">↑ 8% från förra månaden</div>
        </div>

        <div class="bg-white rounded-lg shadow p-6">
          <div class="text-sm text-gray-600 mb-2">Nya kunder</div>
          <div class="text-3xl font-bold text-gray-900">1,234</div>
          <div class="text-sm text-red-600 mt-2">↓ 3% från förra månaden</div>
        </div>

        <div class="bg-white rounded-lg shadow p-6">
          <div class="text-sm text-gray-600 mb-2">Aktiva projekt</div>
          <div class="text-3xl font-bold text-gray-900">42</div>
          <div class="text-sm text-gray-600 mt-2">→ Oförändrat</div>
        </div>
      </div>

      <!-- Table -->
      <div class="bg-white rounded-lg shadow overflow-hidden">
        <div class="px-6 py-4 border-b border-gray-200">
          <h2 class="text-xl font-semibold text-gray-900">Senaste projekt</h2>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Projekt
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Status
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                  Deadline
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr class="hover:bg-gray-50">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm font-medium text-gray-900">Webbapp redesign</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs rounded-full bg-green-100 text-green-800">
                    Aktiv
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  2025-12-15
                </td>
              </tr>
              <!-- Fler rader... -->
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</div>
```

**Viktiga tekniker i detta exempel:**

- `sticky top-0` = Topbar som fastnar överst vid scroll
- `hidden lg:block` = Sidebar dold på mobil, syns på desktop
- `flex-1` = Content tar resterande plats
- `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4` = Responsiv stats-grid
- `overflow-x-auto` = Tabell kan scrolla horisontellt på mobil
- `hover:bg-gray-50` = Hover-effekt på tabellrader

### Visualisering: Tailwind Build Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                TAILWIND BUILD PROCESS (JIT)                 │
└─────────────────────────────────────────────────────────────┘

1. CONFIGURATION
   ┌──────────────────────┐
   │ tailwind.config.js   │
   │ - content: [...]     │
   │ - theme: {...}       │
   │ - plugins: [...]     │
   └───────┬──────────────┘
           │
           ▼
2. SCANNING
   ┌──────────────────────┐
   │ Läs alla filer i     │
   │ content-arrayen      │
   │                      │
   │ index.html ───┐      │
   │ app.js ───────┼──►   │
   │ Button.jsx ───┘      │
   └───────┬──────────────┘
           │
           ▼
3. HITTA KLASSER
   ┌──────────────────────┐
   │ class="bg-blue-500   │
   │         text-white   │
   │         px-6 py-3"   │
   └───────┬──────────────┘
           │
           ▼
4. GENERERA CSS
   ┌──────────────────────┐
   │ .bg-blue-500 {       │
   │   background-color:  │
   │     rgb(59,130,246); │
   │ }                    │
   │ .text-white {        │
   │   color: #fff;       │
   │ }                    │
   │ ... (endast dessa!)  │
   └───────┬──────────────┘
           │
           ▼
5. OUTPUT
   ┌──────────────────────┐
   │ output.css           │
   │ (~8kB gzipped)       │
   └──────────────────────┘
```

### Flödesschema: Ska jag använda @apply?

```
Har du upprepade klasser på många element?
│
├─ Ja (10+ klasser, 5+ ställen)
│  │
│  └─► Är det en återanvändbar komponent?
│     │
│     ├─ Ja → ✅ Använd @apply
│     │         (t.ex. .btn, .card, .form-input)
│     │
│     └─ Nej → 🤔 Överväg komponentisering i ditt ramverk
│               (React-komponent, Vue-komponent etc)
│
└─ Nej (få klasser eller enstaka användning)
   │
   └─► ❌ Använd klasser direkt i HTML
       (behåll utility-first-filosofin!)
```

### 💡 Pro Tips

#### Tip 1: Använd Tailwind CSS IntelliSense
Installera VS Code-extensionen "Tailwind CSS IntelliSense" för autocomplete, syntax highlighting och hover-previews! Detta är nästan ett MÅSTE för produktiv Tailwind-utveckling.

#### Tip 2: Organisera din config smart
Bryt ut stora konfigurationer till separata filer:

```javascript
// tailwind.config.js
const colors = require('./config/colors');
const typography = require('./config/typography');

module.exports = {
  theme: {
    extend: {
      colors,
      ...typography,
    },
  },
}
```

Detta håller main-config clean när projektet växer!

#### Tip 3: Använd @layer för rätt specificity
Om dina komponenter inte får rätt styling, kontrollera att du använder `@layer components`. Detta säkerställer att utilities alltid kan overridea komponenter:

```css
@layer components {
  .btn {
    @apply bg-blue-500; /* Kan overrideas av bg-red-500 i HTML */
  }
}
```

### ✏️ Övningar

#### Övning 1: Konfigurera ett projekt
**Uppgift:** Skapa en `tailwind.config.js` som:
- Skannar alla `.html` och `.js`-filer i `src/`-mappen
- Lägger till en custom färg: `brand-purple: #9333ea`
- Lägger till ett custom spacing-värde: `page: 5rem`

**Facit:**

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-purple': '#9333ea',
      },
      spacing: {
        'page': '5rem',
      },
    },
  },
  plugins: [],
}
```

**Nu kan du använda:**
- `bg-brand-purple`
- `text-brand-purple`
- `p-page` (padding 5rem)
- `m-page` (margin 5rem)

#### Övning 2: Skapa en återanvändbar knapp-komponent
**Uppgift:** Använd `@apply` för att skapa tre knapptyper:
- `.btn` - Bas-styling
- `.btn-success` - Grön knapp
- `.btn-danger` - Röd knapp

**Facit:**

```css
@layer components {
  .btn {
    @apply px-6 py-3 rounded-lg font-semibold transition cursor-pointer;
  }

  .btn-success {
    @apply btn bg-green-500 text-white hover:bg-green-700;
  }

  .btn-danger {
    @apply btn bg-red-500 text-white hover:bg-red-700;
  }
}
```

**Användning:**
```html
<button class="btn-success">Spara</button>
<button class="btn-danger">Ta bort</button>
```

#### Övning 3: Bygg en flexbox-navbar
**Uppgift:** Skapa en navbar med:
- Logo till vänster
- Navigation i mitten
- Profilbild till höger
- Allt vertikalt centrerat
- Responsiv: Navigation döljs på mobil

**Facit:**

```html
<nav class="bg-white shadow-md">
  <div class="container mx-auto px-4">
    <div class="flex items-center justify-between py-4">
      <!-- Logo -->
      <div class="text-2xl font-bold text-blue-600">
        MittVarumärke
      </div>

      <!-- Navigation (döljs på mobil) -->
      <div class="hidden md:flex gap-6">
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Hem</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Produkter</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Om oss</a>
        <a href="#" class="text-gray-700 hover:text-blue-600 transition">Kontakt</a>
      </div>

      <!-- Profil -->
      <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
    </div>
  </div>
</nav>
```

#### Övning 4: Grid-layout med olika kolumnbredder
**Uppgift:** Skapa en layout med:
- 2/3 av bredden för huvudinnehåll
- 1/3 för sidebar
- Staplas vertikalt på mobil

**Facit:**

```html
<div class="container mx-auto px-4 py-8">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
    <!-- Huvudinnehåll (8/12 = 2/3) -->
    <main class="lg:col-span-8">
      <div class="bg-white rounded-lg shadow-md p-6">
        <h1 class="text-3xl font-bold mb-4">Huvudinnehåll</h1>
        <p class="text-gray-700">
          Detta tar upp 2/3 av bredden på desktop, full bredd på mobil.
        </p>
      </div>
    </main>

    <!-- Sidebar (4/12 = 1/3) -->
    <aside class="lg:col-span-4">
      <div class="bg-gray-100 rounded-lg shadow-md p-6">
        <h2 class="text-xl font-bold mb-4">Sidebar</h2>
        <p class="text-gray-700">
          Detta tar upp 1/3 av bredden på desktop.
        </p>
      </div>
    </aside>
  </div>
</div>
```

**Förklaring:**
- `grid-cols-1` på mobil = allt staplas
- `lg:grid-cols-12` på desktop = 12-kolumns grid
- `lg:col-span-8` = huvudinnehåll tar 8 kolumner
- `lg:col-span-4` = sidebar tar 4 kolumner

#### Övning 5: Dark mode-implementation
**Uppgift:** Skapa ett kort som:
- Har vit bakgrund i ljust läge
- Har mörkgrå bakgrund i mörkt läge
- Texten anpassar sig också

**Facit:**

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  // ... resten av config
}
```

```html
<div class="min-h-screen bg-gray-100 dark:bg-gray-900 p-8">
  <div class="max-w-md mx-auto">
    <div class="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
      <h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-4">
        Dark Mode-kort
      </h2>
      <p class="text-gray-700 dark:text-gray-300 mb-4">
        Detta kort anpassar sig efter dark mode!
      </p>
      <button
        onclick="document.documentElement.classList.toggle('dark')"
        class="bg-blue-500 hover:bg-blue-700 dark:bg-blue-600 dark:hover:bg-blue-800
               text-white px-4 py-2 rounded-lg transition"
      >
        Toggle Dark Mode
      </button>
    </div>
  </div>
</div>
```

#### Övning 6: Använd arbiträra värden
**Uppgift:** Skapa en div med:
- Exakt 350px bredd
- Custom färg: #ff6b9d (rosa)
- 23px padding

**Facit:**

```html
<div class="w-[350px] bg-[#ff6b9d] p-[23px] mx-auto">
  <p class="text-white">
    Jag använder arbiträra värden!
  </p>
</div>
```

**OBS:** Använd detta sparsamt - stick till Tailwinds skala när möjligt!

#### Övning 7: Komplex form med komponenter
**Uppgift:** Skapa ett formulär med återanvändbara klasser för:
- Labels
- Input-fält
- Fel-meddelanden
- Submit-knapp

**Facit:**

```css
/* components.css */
@layer components {
  .form-group {
    @apply mb-6;
  }

  .form-label {
    @apply block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2;
  }

  .form-input {
    @apply w-full px-4 py-2 border border-gray-300 dark:border-gray-600
           rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white
           focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent
           transition;
  }

  .form-error {
    @apply text-red-500 text-sm mt-1;
  }

  .form-submit {
    @apply w-full bg-blue-500 hover:bg-blue-700 text-white py-3 rounded-lg
           font-semibold transition cursor-pointer;
  }
}
```

```html
<form class="max-w-md mx-auto bg-white dark:bg-gray-800 p-8 rounded-xl shadow-lg">
  <h2 class="text-2xl font-bold mb-6 text-gray-900 dark:text-white">
    Skapa konto
  </h2>

  <div class="form-group">
    <label class="form-label">Användarnamn</label>
    <input type="text" class="form-input" placeholder="dittnamn" />
    <div class="form-error">Detta fält är obligatoriskt</div>
  </div>

  <div class="form-group">
    <label class="form-label">Email</label>
    <input type="email" class="form-input" placeholder="din@email.se" />
  </div>

  <div class="form-group">
    <label class="form-label">Lösenord</label>
    <input type="password" class="form-input" />
  </div>

  <button type="submit" class="form-submit">
    Skapa konto
  </button>
</form>
```

### 📝 Sammanfattning

**Key Takeaways:**

✅ **JIT-mode** genererar endast CSS för klasser du faktiskt använder – blixtsnabbt och minimal bundle
✅ **content-arrayen** i `tailwind.config.js` är kritisk – glöm inte inkludera alla dina filer!
✅ **theme.extend** låter dig lägga till custom färger, spacing osv. UTAN att ersätta defaults
✅ **@layer** organiserar din CSS i tre lager: base, components, utilities
✅ **@apply** är bra för återanvändbara komponenter, men överdriva inte – behåll utility-first!
✅ **Flexbox och Grid** är dina bästa vänner för layout i Tailwind
✅ **Arbiträra värden** `[350px]` fungerar men använd sparsamt för konsekvent design
✅ **Dark mode** är inbyggt – välj mellan 'media' (auto) eller 'class' (manuell kontroll)

**Ny ordlista (Nivå 3):**

- **JIT (Just-In-Time)**: Kompileringsläge som genererar CSS on-demand
- **content-array**: Lista i config som anger vilka filer Tailwind ska skanna
- **theme.extend**: Konfigurationssektion för att lägga till custom värden
- **@layer**: Direktiv för att organisera CSS i lager (base, components, utilities)
- **@apply**: Direktiv för att använda utility-klasser i egen CSS
- **Arbiträra värden**: Custom värden med bracket-syntax: `w-[347px]`
- **Specificity**: CSS-konceptet om vilken regel som "vinner" när flera appliceras
- **Purging**: Process att ta bort oanvänd CSS (automatiskt i JIT)

**Nästa steg:**

Nu förstår du hur Tailwind fungerar under huven och kan konfigurera det för dina behov! I Nivå 4 går vi in på avancerade mönster, best practices för stora projekt, och hur du undviker vanliga fallgropar. Vi bygger också mer komplexa komponentsystem och lär oss hur man strukturerar Tailwind-kod i produktionsmiljöer!

---

## Nivå 4: Avancerade mönster, best practices & anti-patterns 🏛️

### Introduktion

Välkommen till universitetsnivån! Här lär du dig hur man bygger och underhåller stora Tailwind-projekt på ett professionellt sätt. Vi fokuserar på skalbarhet, teamarbete, och att undvika vanliga fallgropar som kan förvandla ett rent projekt till ett underhållsmardröm.

Detta är viktigt eftersom skillnaden mellan ett "fungerar på min dator"-projekt och ett produktionssystem ofta ligger i disciplin, struktur och förståelse för best practices. Den kunskap du får här kommer göra dig redo för verkliga, stora projekt.

### Kärnkoncept

#### 1. **Projektstruktur för skalbarhet**

När projektet växer blir struktur kritiskt. Här är en beprövad mappstruktur:

```
project/
├── src/
│   ├── styles/
│   │   ├── main.css                 # Entry point
│   │   ├── base/
│   │   │   ├── reset.css            # Custom resets
│   │   │   └── typography.css       # Bas-typografi
│   │   ├── components/
│   │   │   ├── buttons.css          # Alla knapp-varianter
│   │   │   ├── cards.css            # Kort-komponenter
│   │   │   ├── forms.css            # Formulär-element
│   │   │   └── navigation.css       # Navigering
│   │   └── utilities/
│   │       └── custom.css           # Egna utilities
│   ├── components/                   # Ramverks-komponenter (React/Vue)
│   └── config/
│       ├── colors.js                # Färgpalett
│       ├── spacing.js               # Spacing-skala
│       └── typography.js            # Typografi-system
├── tailwind.config.js
└── package.json
```

**main.css:**
```css
@import './base/reset.css';
@import './base/typography.css';

@tailwind base;
@tailwind components;
@tailwind utilities;

@import './components/buttons.css';
@import './components/cards.css';
@import './components/forms.css';
@import './components/navigation.css';

@import './utilities/custom.css';
```

#### 2. **Design Token System (Centraliserad styling)**

Istället för att sprida färger och värden överallt, definiera allt centralt:

**config/colors.js:**
```javascript
module.exports = {
  // Brand colors
  brand: {
    primary: {
      50: '#eff6ff',
      100: '#dbeafe',
      200: '#bfdbfe',
      500: '#3b82f6',  // Main brand color
      900: '#1e3a8a',
    },
    secondary: {
      500: '#10b981',
      700: '#047857',
    },
  },
  // Semantic colors
  success: {
    light: '#d1fae5',
    DEFAULT: '#10b981',
    dark: '#065f46',
  },
  warning: {
    light: '#fef3c7',
    DEFAULT: '#f59e0b',
    dark: '#92400e',
  },
  error: {
    light: '#fee2e2',
    DEFAULT: '#ef4444',
    dark: '#991b1b',
  },
  // UI colors
  background: {
    primary: '#ffffff',
    secondary: '#f9fafb',
    tertiary: '#f3f4f6',
  },
  text: {
    primary: '#111827',
    secondary: '#6b7280',
    tertiary: '#9ca3af',
    inverse: '#ffffff',
  },
};
```

**config/spacing.js:**
```javascript
module.exports = {
  // Layout spacing (för stora områden)
  'layout-xs': '1rem',      // 16px
  'layout-sm': '1.5rem',    // 24px
  'layout-md': '2rem',      // 32px
  'layout-lg': '3rem',      // 48px
  'layout-xl': '4rem',      // 64px

  // Component spacing (för komponenter)
  'component-xs': '0.5rem',  // 8px
  'component-sm': '0.75rem', // 12px
  'component-md': '1rem',    // 16px
  'component-lg': '1.25rem', // 20px
};
```

**tailwind.config.js:**
```javascript
const colors = require('./src/config/colors');
const spacing = require('./src/config/spacing');

module.exports = {
  content: ['./src/**/*.{html,js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors,
      spacing,
    },
  },
};
```

**Fördelar:**
- ✅ En enda källa till sanning
- ✅ Lätt att uppdatera hela temat
- ✅ Tydliga semantiska namn
- ✅ Kan delas mellan flera projekt

#### 3. **Klassordning och läsbarhet**

Håll en konsekvent ordning för klasser. Här är en rekommenderad standard:

```html
<div class="
  /* 1. Layout & Position */
  relative flex items-center justify-between

  /* 2. Box Model (utsida → insida) */
  w-full max-w-7xl mx-auto px-4 py-6

  /* 3. Typografi */
  text-lg font-semibold text-gray-900

  /* 4. Visuella effekter */
  bg-white rounded-lg shadow-md border border-gray-200

  /* 5. Transitions & Animations */
  transition duration-300

  /* 6. Interaktivitet */
  hover:shadow-xl hover:bg-gray-50

  /* 7. Responsivitet (sist!) */
  md:px-6 lg:px-8 xl:text-xl
">
  Innehåll
</div>
```

**Alternativt, använd Prettier plugin:**
```bash
npm install -D prettier prettier-plugin-tailwindcss
```

Detta sorterar automatiskt klasserna enligt Tailwinds rekommenderade ordning!

#### 4. **Komponentabstraktion: När och hur**

**Anti-pattern: HTML-helvetet**
```html
<!-- Undvik detta! -->
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Knapp 1
</button>
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Knapp 2
</button>
<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
  Knapp 3
</button>
<!-- 50 knappar till... 😱 -->
```

**Lösning 1: Ramverks-komponent (bäst!)**

**React:**
```jsx
// Button.jsx
export function Button({ variant = 'primary', size = 'md', children, ...props }) {
  const baseClasses = 'font-semibold rounded-lg transition';

  const variantClasses = {
    primary: 'bg-blue-500 hover:bg-blue-700 text-white',
    secondary: 'bg-gray-500 hover:bg-gray-700 text-white',
    outline: 'border-2 border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white',
  };

  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-6 py-3 text-base',
    lg: 'px-8 py-4 text-lg',
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`}
      {...props}
    >
      {children}
    </button>
  );
}

// Användning
<Button variant="primary" size="md">Klicka här</Button>
<Button variant="outline" size="lg">Större knapp</Button>
```

**Lösning 2: @apply (om inget ramverk)**

```css
@layer components {
  .btn {
    @apply font-semibold rounded-lg transition cursor-pointer;
  }

  .btn-primary {
    @apply btn bg-blue-500 hover:bg-blue-700 text-white;
  }

  .btn-sm { @apply btn px-3 py-1.5 text-sm; }
  .btn-md { @apply btn px-6 py-3 text-base; }
  .btn-lg { @apply btn px-8 py-4 text-lg; }
}
```

**Tumregel för när du ska extrahera:**
- 🔄 Används 5+ gånger → Överväg komponent
- 🔄 10+ klasser per element → Stark kandidat
- 🔄 Komplexa varianter → Definitiv komponent

#### 5. **Dark Mode: Strategier för stora projekt**

**Strategi 1: CSS Variables + Tailwind (mest flexibel)**

```css
/* base.css */
@layer base {
  :root {
    --color-bg-primary: 255 255 255;
    --color-bg-secondary: 249 250 251;
    --color-text-primary: 17 24 39;
    --color-text-secondary: 107 114 128;
  }

  .dark {
    --color-bg-primary: 17 24 39;
    --color-bg-secondary: 31 41 55;
    --color-text-primary: 243 244 246;
    --color-text-secondary: 156 163 175;
  }
}
```

```javascript
// tailwind.config.js
module.exports = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'bg-primary': 'rgb(var(--color-bg-primary) / <alpha-value>)',
        'bg-secondary': 'rgb(var(--color-bg-secondary) / <alpha-value>)',
        'text-primary': 'rgb(var(--color-text-primary) / <alpha-value>)',
        'text-secondary': 'rgb(var(--color-text-secondary) / <alpha-value>)',
      },
    },
  },
};
```

**Användning:**
```html
<div class="bg-bg-primary text-text-primary">
  Anpassar sig automatiskt till dark mode!
</div>
```

**Strategi 2: Tailwind dark: klasser (enklare, mer verbose)**

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  Innehåll
</div>
```

**Best practice: Kombinera!**
- Använd CSS variables för globala färger
- Använd `dark:` för specifika overrides

#### 6. **Performance-optimering**

**Checklist för optimal performance:**

✅ **1. Säkerställ korrekt content-konfiguration:**
```javascript
// Bra
content: [
  './src/**/*.{js,jsx,ts,tsx}',
  './pages/**/*.{js,jsx,ts,tsx}',
]

// Dåligt (för brett, långsam build)
content: ['./**/*.html']

// Dåligt (missar filer)
content: ['./src/index.html']  // Glömmer komponenter!
```

✅ **2. Använd PurgeCSS säkerhetslistor vid behov:**
```javascript
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  safelist: [
    'bg-red-500',    // Dynamiska klasser som inte syns i scanning
    'text-3xl',
    {
      pattern: /bg-(red|green|blue)-(100|500|900)/,  // Pattern för många varianter
    },
  ],
};
```

✅ **3. Dela upp CSS för stora appar:**
```javascript
// Ladda bara kritisk CSS först
<link rel="stylesheet" href="critical.css">

// Lazy-load resten
<link rel="preload" href="main.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

✅ **4. Optimera builds:**
```bash
# Development (snabbt, stort)
npx tailwindcss -i input.css -o output.css --watch

# Production (långsamt, minimalt)
NODE_ENV=production npx tailwindcss -i input.css -o output.css --minify
```

#### 7. **Anti-patterns att undvika**

❌ **Anti-pattern 1: @apply-överbelastning**

**Dåligt:**
```css
/* Allt via @apply = du skrev bara CSS med extra steg */
.header { @apply flex items-center; }
.nav { @apply flex gap-4; }
.link { @apply text-blue-500 hover:text-blue-700; }
.footer { @apply bg-gray-900 text-white; }
/* ...100 fler... */
```

**Bättre:**
```css
/* Endast för genuint återanvända komponenter */
@layer components {
  .btn-primary {
    @apply px-6 py-3 bg-blue-500 hover:bg-blue-700 text-white rounded-lg;
  }
}
```

❌ **Anti-pattern 2: Magiska siffror överallt**

**Dåligt:**
```html
<div class="w-[347px] h-[219px] p-[13px]">
  <!-- Varför just dessa värden? Ingen vet. -->
</div>
```

**Bättre:**
```javascript
// tailwind.config.js - ge dem namn!
theme: {
  extend: {
    spacing: {
      'sidebar': '347px',
      'card': '219px',
    },
  },
}
```

```html
<div class="w-sidebar h-card p-4">
  <!-- Tydligt och konsekvent! -->
</div>
```

❌ **Anti-pattern 3: Ignorera semantiska färgnamn**

**Dåligt:**
```html
<button class="bg-blue-500">Spara</button>
<button class="bg-red-500">Ta bort</button>
<div class="bg-blue-500">Success!</div>
<div class="bg-red-500">Error!</div>
```

*Problem: Om du vill ändra varumärkesfärg måste du hitta alla "blue-500" och avgöra vilka som är knappar vs. status!*

**Bättre:**
```javascript
// tailwind.config.js
colors: {
  primary: colors.blue[500],
  danger: colors.red[500],
  success: colors.green[500],
}
```

```html
<button class="bg-primary">Spara</button>
<button class="bg-danger">Ta bort</button>
<div class="bg-success">Success!</div>
<div class="bg-danger">Error!</div>
```

❌ **Anti-pattern 4: Ingen komponent-hierarki**

**Dåligt:**
```html
<!-- Varje card kopierad med copy-paste -->
<div class="bg-white rounded-xl shadow-lg p-6 mb-4">...</div>
<div class="bg-white rounded-xl shadow-lg p-6 mb-4">...</div>
<div class="bg-white rounded-xl shadow-lg p-6 mb-4">...</div>
```

*Problem: Vill ändra alla cards? 50 ställen att uppdatera!*

**Bättre (React):**
```jsx
function Card({ children, className = '' }) {
  return (
    <div className={`bg-white rounded-xl shadow-lg p-6 ${className}`}>
      {children}
    </div>
  );
}
```

❌ **Anti-pattern 5: !important-syndromet**

**Dåligt:**
```css
.my-class {
  @apply !bg-red-500 !text-white !p-4;
}
```

*Problem: Du slåss mot Tailwinds specificity istället för att använda den!*

**Bättre:**
Använd rätt lager och låt Tailwinds specificity fungera för dig. `!important` ska nästan aldrig behövas.

### Exempel

#### Exempel 1: Komplett Design System

**1. Definiera tokens:**

**tokens/colors.js:**
```javascript
module.exports = {
  // Primitiva färger (designsystemets bas)
  primitive: {
    blue: {
      50: '#eff6ff',
      500: '#3b82f6',
      900: '#1e3a8a',
    },
    gray: {
      50: '#f9fafb',
      100: '#f3f4f6',
      500: '#6b7280',
      900: '#111827',
    },
  },

  // Semantiska färger (vad de betyder i appen)
  semantic: {
    primary: {
      DEFAULT: '#3b82f6',
      hover: '#1e40af',
      active: '#1e3a8a',
    },
    surface: {
      base: '#ffffff',
      raised: '#f9fafb',
      overlay: '#ffffff',
    },
    text: {
      primary: '#111827',
      secondary: '#6b7280',
      tertiary: '#9ca3af',
      inverse: '#ffffff',
    },
    border: {
      DEFAULT: '#e5e7eb',
      strong: '#d1d5db',
    },
    status: {
      success: '#10b981',
      warning: '#f59e0b',
      error: '#ef4444',
      info: '#3b82f6',
    },
  },
};
```

**2. Konfigurera Tailwind:**

```javascript
const { semantic } = require('./tokens/colors');

module.exports = {
  theme: {
    extend: {
      colors: semantic,
    },
  },
};
```

**3. Använd semantiska namn:**

```jsx
function Alert({ type = 'info', children }) {
  const styles = {
    success: 'bg-green-50 border-status-success text-green-900',
    error: 'bg-red-50 border-status-error text-red-900',
    warning: 'bg-yellow-50 border-status-warning text-yellow-900',
    info: 'bg-blue-50 border-status-info text-blue-900',
  };

  return (
    <div className={`border-l-4 p-4 ${styles[type]}`}>
      {children}
    </div>
  );
}
```

#### Exempel 2: Skalbar komponentbibliotek-struktur

```
src/
├── components/
│   ├── ui/                    # Låg-nivå UI-komponenter
│   │   ├── Button/
│   │   │   ├── Button.jsx
│   │   │   ├── Button.stories.jsx
│   │   │   └── button.css     # Eventuell @apply
│   │   ├── Input/
│   │   ├── Card/
│   │   └── index.js           # Barrel export
│   │
│   ├── layout/                # Layout-komponenter
│   │   ├── Header/
│   │   ├── Footer/
│   │   ├── Sidebar/
│   │   └── Container/
│   │
│   ├── features/              # Business-komponenter
│   │   ├── UserProfile/
│   │   ├── ProductCard/
│   │   └── CheckoutForm/
│   │
│   └── pages/                 # Sidor som kombinerar allt
│       ├── HomePage/
│       ├── ProductPage/
│       └── CheckoutPage/
```

**ui/Button/Button.jsx:**
```jsx
import { cva } from 'class-variance-authority';  // CVA för variants

const button = cva(
  // Base styles
  'font-semibold rounded-lg transition-colors focus:outline-none focus:ring-2',
  {
    variants: {
      intent: {
        primary: 'bg-primary text-white hover:bg-primary-hover',
        secondary: 'bg-surface-raised text-text-primary hover:bg-gray-200',
        danger: 'bg-status-error text-white hover:bg-red-700',
      },
      size: {
        small: 'text-sm px-3 py-1.5',
        medium: 'text-base px-6 py-3',
        large: 'text-lg px-8 py-4',
      },
      fullWidth: {
        true: 'w-full',
      },
    },
    defaultVariants: {
      intent: 'primary',
      size: 'medium',
    },
  }
);

export function Button({
  intent,
  size,
  fullWidth,
  children,
  className,
  ...props
}) {
  return (
    <button
      className={button({ intent, size, fullWidth, className })}
      {...props}
    >
      {children}
    </button>
  );
}
```

**Användning:**
```jsx
<Button intent="primary" size="large">Spara</Button>
<Button intent="danger" size="small">Ta bort</Button>
<Button intent="secondary" fullWidth>Full bredd</Button>
```

#### Exempel 3: Responsiv + Dark Mode Dashboard (avancerad)

```jsx
// Layout.jsx
export function DashboardLayout({ children }) {
  const [darkMode, setDarkMode] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className={darkMode ? 'dark' : ''}>
      <div class="min-h-screen bg-surface-base dark:bg-gray-900 text-text-primary dark:text-gray-100">
        {/* Mobile menu button */}
        <button
          onClick={() => setSidebarOpen(!sidebarOpen)}
          className="lg:hidden fixed top-4 left-4 z-50 p-2 rounded-lg bg-surface-raised dark:bg-gray-800"
        >
          ☰
        </button>

        {/* Sidebar */}
        <aside className={`
          fixed inset-y-0 left-0 z-40 w-64
          bg-white dark:bg-gray-800 border-r border-border dark:border-gray-700
          transform transition-transform duration-200 ease-in-out
          ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'}
          lg:translate-x-0
        `}>
          <nav className="p-4 space-y-2">
            <NavLink href="/dashboard">Dashboard</NavLink>
            <NavLink href="/analytics">Analytics</NavLink>
            <NavLink href="/settings">Settings</NavLink>
          </nav>

          {/* Dark mode toggle */}
          <div className="p-4 border-t border-border dark:border-gray-700">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="w-full px-4 py-2 rounded-lg bg-surface-raised dark:bg-gray-700
                         hover:bg-gray-200 dark:hover:bg-gray-600 transition"
            >
              {darkMode ? '☀️ Light' : '🌙 Dark'}
            </button>
          </div>
        </aside>

        {/* Main content */}
        <main className="lg:ml-64 p-4 lg:p-8">
          <div className="max-w-7xl mx-auto">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}

// NavLink component
function NavLink({ href, children }) {
  const isActive = window.location.pathname === href;

  return (
    <a
      href={href}
      className={`
        block px-4 py-2 rounded-lg transition
        ${isActive
          ? 'bg-primary text-white'
          : 'text-text-secondary hover:bg-surface-raised dark:hover:bg-gray-700'
        }
      `}
    >
      {children}
    </a>
  );
}
```

### Visualisering: Komponent-hierarki för stora projekt

```
┌─────────────────────────────────────────────────────────┐
│           COMPONENT ABSTRACTION PYRAMID                 │
└─────────────────────────────────────────────────────────┘

                    ▲ Abstraktion
                    │
┌───────────────────────────────────────────────┐
│  PAGES (Högst nivå)                          │
│  ▸ HomePage, ProductPage, CheckoutPage       │
│  └─ Kombinerar features + layout             │
└───────────────────┬───────────────────────────┘
                    │
┌───────────────────────────────────────────────┐
│  FEATURES (Business Logic)                   │
│  ▸ UserProfile, ProductCard, ShoppingCart    │
│  └─ Använder UI-komponenter                  │
└───────────────────┬───────────────────────────┘
                    │
┌───────────────────────────────────────────────┐
│  LAYOUT (Struktur)                           │
│  ▸ Header, Footer, Sidebar, Container        │
│  └─ Ren layoutlogik                          │
└───────────────────┬───────────────────────────┘
                    │
┌───────────────────────────────────────────────┐
│  UI COMPONENTS (Återanvändbara)              │
│  ▸ Button, Input, Card, Badge, Avatar        │
│  └─ Tailwind utilities + variants            │
└───────────────────┬───────────────────────────┘
                    │
┌───────────────────────────────────────────────┐
│  TAILWIND UTILITIES (Lägst nivå)             │
│  ▸ bg-blue-500, px-4, rounded-lg...          │
│  └─ Grundläggande byggstenar                 │
└───────────────────────────────────────────────┘
```

**Regel:** Ju högre upp i pyramiden, desto mindre Tailwind-klasser direkt i koden!

### 💡 Pro Tips

#### Tip 1: Använd "class-variance-authority" för komplexa komponenter
```bash
npm install class-variance-authority
```

Detta bibliotek gör det superenkelt att hantera varianter:

```jsx
import { cva } from 'class-variance-authority';

const alert = cva('border-l-4 p-4', {
  variants: {
    intent: {
      success: 'bg-green-50 border-green-500 text-green-900',
      error: 'bg-red-50 border-red-500 text-red-900',
    },
    size: {
      small: 'text-sm p-2',
      large: 'text-lg p-6',
    },
  },
  compoundVariants: [
    {
      intent: 'error',
      size: 'large',
      class: 'font-bold',  // Extra styling för stora error-alerts
    },
  ],
  defaultVariants: {
    intent: 'success',
    size: 'small',
  },
});
```

#### Tip 2: Dokumentera ditt design system
Skapa en `DESIGN_SYSTEM.md` i projektet:

```markdown
# Design System

## Färger
- `bg-primary`: Primär varumärkesfärg (#3b82f6)
- `bg-surface-base`: Huvudbakgrund (vit i ljust läge)

## Spacing
- Använd `layout-*` för stora områden
- Använd `component-*` för komponenter

## Typografi
- Rubriker: `font-headline` (Montserrat)
- Body: `font-sans` (Inter)
```

#### Tip 3: Sätt upp ESLint-regler för Tailwind
```bash
npm install -D eslint-plugin-tailwindcss
```

**.eslintrc.js:**
```javascript
module.exports = {
  extends: ['plugin:tailwindcss/recommended'],
  rules: {
    'tailwindcss/no-custom-classname': 'warn',
    'tailwindcss/classnames-order': 'warn',
  },
};
```

Detta varnar för:
- Felstavade klasser
- Inkonsekvent klassordning
- Custom klasser som inte finns i config

### ✏️ Övningar

#### Övning 1: Skapa ett design token-system
**Uppgift:** Definiera ett komplett färgsystem med:
- Primitiva färger (blue, gray, green, red)
- Semantiska mappningar (primary, surface, text, status)
- Dark mode-varianter

**Facit: Se Exempel 1 ovan**

#### Övning 2: Refaktorera från anti-pattern till best practice
**Uppgift:** Givet denna kod, refaktorera till en komponent:

```html
<!-- Dålig kod med upprepning -->
<div class="bg-white rounded-lg shadow-md p-6 mb-4 hover:shadow-xl transition">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Produkt 1</h3>
  <p class="text-gray-600">Beskrivning...</p>
</div>
<div class="bg-white rounded-lg shadow-md p-6 mb-4 hover:shadow-xl transition">
  <h3 class="text-xl font-bold text-gray-900 mb-2">Produkt 2</h3>
  <p class="text-gray-600">Beskrivning...</p>
</div>
```

**Facit:**

```jsx
// ProductCard.jsx
export function ProductCard({ title, description }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-4 hover:shadow-xl transition">
      <h3 className="text-xl font-bold text-gray-900 mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
}

// Användning
<ProductCard title="Produkt 1" description="Beskrivning..." />
<ProductCard title="Produkt 2" description="Beskrivning..." />
```

#### Övning 3: Implementera dark mode med CSS variables
**Uppgift:** Skapa ett system där färger definieras med CSS variables och anpassar sig automatiskt till dark mode.

**Facit: Se strategi 1 under "Dark Mode" i Kärnkoncept**

#### Övning 4: Strukturera ett stort projekt
**Uppgift:** Planera mappstrukturen för en e-handelsapp med:
- Produktlistning
- Produktdetaljer
- Kundvagn
- Checkout

**Facit:**

```
src/
├── styles/
│   ├── main.css
│   ├── components/
│   │   ├── buttons.css
│   │   ├── cards.css
│   │   └── forms.css
│   └── base/
│       └── typography.css
├── components/
│   ├── ui/
│   │   ├── Button/
│   │   ├── Card/
│   │   ├── Input/
│   │   └── Badge/
│   ├── layout/
│   │   ├── Header/
│   │   ├── Footer/
│   │   └── Container/
│   └── features/
│       ├── ProductCard/
│       ├── ProductList/
│       ├── CartItem/
│       ├── CartSummary/
│       └── CheckoutForm/
├── pages/
│   ├── HomePage/
│   ├── ProductListPage/
│   ├── ProductDetailPage/
│   ├── CartPage/
│   └── CheckoutPage/
├── config/
│   ├── colors.js
│   ├── spacing.js
│   └── typography.js
└── tailwind.config.js
```

#### Övning 5: Skapa variants med CVA
**Uppgift:** Skapa en Badge-komponent med variants:
- Type: success, warning, error, info
- Size: small, medium, large

**Facit:**

```jsx
import { cva } from 'class-variance-authority';

const badge = cva('inline-flex items-center font-semibold rounded-full', {
  variants: {
    type: {
      success: 'bg-green-100 text-green-800',
      warning: 'bg-yellow-100 text-yellow-800',
      error: 'bg-red-100 text-red-800',
      info: 'bg-blue-100 text-blue-800',
    },
    size: {
      small: 'text-xs px-2 py-0.5',
      medium: 'text-sm px-3 py-1',
      large: 'text-base px-4 py-1.5',
    },
  },
  defaultVariants: {
    type: 'info',
    size: 'medium',
  },
});

export function Badge({ type, size, children, className }) {
  return (
    <span className={badge({ type, size, className })}>
      {children}
    </span>
  );
}

// Användning
<Badge type="success" size="small">Aktiv</Badge>
<Badge type="error" size="large">Fel!</Badge>
```

#### Övning 6: Identifiera anti-patterns
**Uppgift:** För varje kodexempel nedan, identifiera problemet och föreslå lösning.

**a) Problem:**
```css
.everything {
  @apply flex items-center justify-between px-4 py-2;
}
.card {
  @apply bg-white rounded-lg shadow-md p-6;
}
.text {
  @apply text-gray-700;
}
/* 100 fler klasser... */
```

**Facit:** Överanvändning av @apply. Använd istället ramverks-komponenter där möjligt, och reservera @apply endast för genuint återanvända komponenter.

**b) Problem:**
```html
<div class="w-[347px] mt-[23px] bg-[#1da1f2]">
```

**Facit:** Magiska siffror utan kontext. Lägg till i theme.extend med semantiska namn:
```javascript
spacing: {
  'sidebar-width': '347px',
  'section-gap': '23px',
},
colors: {
  'twitter-blue': '#1da1f2',
}
```

**c) Problem:**
```jsx
<button className="bg-blue-500 hover:bg-blue-700 !text-white !px-6">
```

**Facit:** Användning av `!important` (!-prefix). Detta indikerar ett specificity-problem. Lös istället genom rätt lagerordning eller genom att inte kämpa mot Tailwinds system.

#### Övning 7: Dark mode med semantic tokens
**Uppgift:** Konvertera dessa hårdkodade dark mode-klasser till ett semantic token-system:

```html
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
  <h1 class="text-gray-900 dark:text-white">Rubrik</h1>
  <p class="text-gray-600 dark:text-gray-400">Text</p>
</div>
```

**Facit:**

**1. Definiera tokens:**
```css
:root {
  --color-surface-primary: 255 255 255;
  --color-text-primary: 17 24 39;
  --color-text-secondary: 75 85 99;
}

.dark {
  --color-surface-primary: 17 24 39;
  --color-text-primary: 255 255 255;
  --color-text-secondary: 156 163 175;
}
```

**2. Konfigurera Tailwind:**
```javascript
colors: {
  'surface-primary': 'rgb(var(--color-surface-primary) / <alpha-value>)',
  'text-primary': 'rgb(var(--color-text-primary) / <alpha-value>)',
  'text-secondary': 'rgb(var(--color-text-secondary) / <alpha-value>)',
}
```

**3. Använd:**
```html
<div class="bg-surface-primary text-text-primary">
  <h1 class="text-text-primary">Rubrik</h1>
  <p class="text-text-secondary">Text</p>
</div>
```

### 📝 Sammanfattning

**Key Takeaways:**

✅ **Projektstruktur** är kritisk för skalbarhet – separera base, components och utilities
✅ **Design tokens** ger en centraliserad källa till sanning för färger, spacing och typografi
✅ **Komponentabstraktion** bör följa pyramid-modellen: utilities → UI → features → pages
✅ **Klassordning** gör koden läsbar – använd Prettier plugin för automatisk sortering
✅ **@apply** ska användas sparsamt – föredra ramverks-komponenter när möjligt
✅ **Semantiska färgnamn** (`primary`, `surface`, `text-primary`) är bättre än primitiva (`blue-500`)
✅ **Dark mode** hanteras bäst med CSS variables för flexibilitet
✅ **Performance** optimeras genom korrekt content-konfiguration och produktionsbuilds
✅ **Anti-patterns** som !important, magiska värden och @apply-överanvändning måste undvikas

**Ny ordlista (Nivå 4):**

- **Design tokens**: Centraliserade variabler för färger, spacing, typografi etc
- **Semantic naming**: Namngivning baserad på syfte (primary) istället för utseende (blue)
- **Component hierarchy**: Pyramid-struktur från utilities till pages
- **CVA (Class Variance Authority)**: Bibliotek för att hantera komponentvarianter
- **Compound variants**: Kombinationer av varianter med speciell styling
- **Barrel export**: index.js som exporterar alla komponenter från en mapp
- **Safelist**: Lista över klasser som alltid ska inkluderas trots att de inte hittas i scanning
- **Critical CSS**: Minimal CSS som laddas först för snabb rendering

**Nästa steg:**

Nu har du verktyg och kunskap för att bygga stora, skalbara Tailwind-projekt! I Nivå 5 tar vi steget till masternivå och tittar på hur Tailwind används i produktionsmiljöer, modern tooling (2025), integration med stora ramverk, och verkliga case studies från industrin!

---

## Nivå 5: Tailwind på masternivå i moderna projekt 💼

### Introduktion

Välkommen till masternivå! Här fokuserar vi på hur Tailwind används i riktiga produktionsmiljöer 2025, moderna verktyg, skalning i monorepos, och strategier för enterprise-applikationer. Detta är kunskapen som skiljer juniorutvecklare från seniors.

Detta är viktigt eftersom verkliga projekt har komplexa krav: prestanda, skalbarhet, teamsamarbete, CI/CD-pipelines, och underhållbarhet över år. Här lär du dig de strategier och mönster som faktiskt används av stora företag.

### Kärnkoncept

#### 1. **Tailwind CSS v4 (2025): Vad är nytt?**

Tailwind v4 är en helt ny arkitektur med revolutionerande förändringar:

**Stora förändringar:**

**a) CSS-first konfiguration:**
```css
/* Innan (v3): JavaScript-konfiguration */
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
      },
    },
  },
}

/* Nu (v4): CSS-baserad med @theme */
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --font-display: "Montserrat", sans-serif;
  --breakpoint-tablet: 768px;
}
```

**b) Automatisk content-detektion:**
```css
/* Inget behov av content-array längre! */
@import "tailwindcss";

/* v4 hittar automatiskt alla template-filer */
```

**c) Native CSS variables:**
```css
@theme {
  --color-brand-primary: #3b82f6;
}

/* Tillgänglig överallt som CSS-variabel */
.my-component {
  background: var(--color-brand-primary);
}
```

**d) Vite-plugin för blixtsnabb utveckling:**
```javascript
// vite.config.js
import tailwindcss from '@tailwindcss/vite'

export default {
  plugins: [tailwindcss()],
}
```

**Performance:**
- Full rebuild: **3.5x snabbare** än v3
- Incremental rebuilds: **8x snabbare**
- Mindre konfiguration
- Bättre dev-experience

**Migration från v3 → v4:**
```bash
npx @tailwindcss/upgrade@next
```

#### 2. **Monorepo-arkitektur (Turborepo / Nx)**

För stora företag med flera appar som delar kod:

**Typisk struktur:**

```
monorepo/
├── apps/
│   ├── marketing-site/        # Next.js
│   ├── web-app/              # React (Vite)
│   └── admin-panel/          # Next.js
├── packages/
│   ├── ui/                   # Delad komponentbibliotek
│   │   ├── src/
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   └── input.tsx
│   │   ├── tailwind.config.ts
│   │   └── package.json
│   ├── tailwind-config/      # Delad Tailwind-config
│   │   ├── base.ts
│   │   ├── tokens.ts
│   │   └── package.json
│   └── utils/
├── turbo.json
└── package.json
```

**Delad Tailwind-konfiguration:**

**packages/tailwind-config/base.ts:**
```typescript
import type { Config } from 'tailwindcss'
import { tokens } from './tokens'

export const baseConfig: Partial<Config> = {
  theme: {
    extend: {
      colors: tokens.colors,
      spacing: tokens.spacing,
      fontFamily: tokens.fonts,
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

**packages/tailwind-config/tokens.ts:**
```typescript
export const tokens = {
  colors: {
    brand: {
      primary: '#3b82f6',
      secondary: '#10b981',
    },
    surface: {
      base: '#ffffff',
      raised: '#f9fafb',
    },
    text: {
      primary: '#111827',
      secondary: '#6b7280',
    },
  },
  spacing: {
    'layout-sm': '1.5rem',
    'layout-md': '2rem',
    'layout-lg': '3rem',
  },
  fonts: {
    sans: ['Inter', 'system-ui', 'sans-serif'],
    display: ['Montserrat', 'system-ui', 'sans-serif'],
  },
}
```

**apps/web-app/tailwind.config.ts:**
```typescript
import type { Config } from 'tailwindcss'
import { baseConfig } from '@repo/tailwind-config/base'

export default {
  content: [
    './src/**/*.{js,ts,jsx,tsx}',
    // Inkludera delat UI-bibliotek
    '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
  ],
  presets: [baseConfig], // Använd delad config som preset
  theme: {
    extend: {
      // App-specifika overrides
    },
  },
} satisfies Config
```

**Fördelar:**
- ✅ En källa till sanning för design tokens
- ✅ Delat UI-bibliotek mellan appar
- ✅ Konsekvent styling överallt
- ✅ Ändringar på ett ställe påverkar alla appar

#### 3. **Production Optimization (Enterprise-nivå)**

**Checklist för optimal production:**

**1. CSS Bundle-storlek:**
```bash
# Analysera bundle
npx tailwindcss -i input.css -o output.css --minify

# Kontrollera storlek
ls -lh output.css
gzip -c output.css | wc -c  # Gzipped storlek
```

**Mål:** <10kB gzipped

**2. Safelist för dynamiska klasser:**
```typescript
// tailwind.config.ts
export default {
  safelist: [
    // Dynamiska färger från CMS/API
    {
      pattern: /bg-(red|green|blue|yellow)-(50|100|500|600)/,
      variants: ['hover', 'focus'],
    },
    // Status badges
    {
      pattern: /^badge-(success|warning|error|info)$/,
    },
  ],
}
```

**3. Critical CSS-extraktion:**
```javascript
// För Next.js
// pages/_document.tsx
import { extractCritical } from '@emotion/server'

export default function Document() {
  return (
    <Html>
      <Head>
        {/* Inline critical CSS */}
        <style dangerouslySetInnerHTML={{ __html: criticalCss }} />
      </Head>
      <Body>
        {/* Lazy-load resterande CSS */}
        <link rel="preload" href="/styles.css" as="style" />
      </Body>
    </Html>
  )
}
```

**4. CDN & Caching:**
```nginx
# nginx.conf
location ~* \.css$ {
  expires 1y;
  add_header Cache-Control "public, immutable";
}
```

**5. Build-pipeline integration:**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3

      - name: Install dependencies
        run: npm ci

      - name: Build Tailwind CSS
        run: NODE_ENV=production npm run build:css

      - name: Check CSS bundle size
        run: |
          SIZE=$(gzip -c dist/output.css | wc -c)
          if [ $SIZE -gt 15000 ]; then
            echo "CSS bundle too large: ${SIZE} bytes"
            exit 1
          fi

      - name: Verify no purged classes
        run: npm run test:css
```

#### 4. **Modern Stack Integration (2025)**

**Next.js 15 + Tailwind v4:**

```typescript
// next.config.ts
import type { NextConfig } from 'next'

const config: NextConfig = {
  // Tailwind v4 fungerar automatiskt med Next.js
  experimental: {
    optimizeCss: true, // Optimera CSS automatiskt
  },
}

export default config
```

**app/globals.css:**
```css
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --font-sans: "Inter", system-ui, sans-serif;
}

@layer base {
  body {
    @apply bg-surface-base text-text-primary;
  }
}
```

**Vite + React + Tailwind v4:**

```typescript
// vite.config.ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
  build: {
    cssCodeSplit: true, // Dela upp CSS per route
    cssMinify: 'lightningcss', // Snabbare minifiering
  },
})
```

**Astro + Tailwind (för content-tunga sidor):**

```javascript
// astro.config.mjs
import { defineConfig } from 'astro/config'
import tailwind from '@astrojs/tailwind'

export default defineConfig({
  integrations: [tailwind()],
})
```

#### 5. **Team Workflows & Standards**

**Kodgranskningschecklist:**

```markdown
## Tailwind Code Review Checklist

### Styling
- [ ] Används semantiska färgnamn (primary, success) istället för primitiva (blue-500)?
- [ ] Följer spacing Tailwinds skala (4, 6, 8...) utan arbiträra värden?
- [ ] Är klassordningen konsekvent (layout → spacing → färg → effekter → responsivitet)?

### Komponenter
- [ ] Extraherade komponenter för upprepad markup (5+ användningar)?
- [ ] Används ramverks-komponenter istället för @apply där möjligt?
- [ ] Tydliga variant-props för olika stilar?

### Performance
- [ ] Inga oanvända klasser i production build?
- [ ] Dynamiska klasser i safelist?
- [ ] CSS bundle <15kB gzipped?

### Responsivitet
- [ ] Mobile-first approach (bas utan prefix)?
- [ ] Testad på mobil, tablet och desktop?
- [ ] Använder breakpoints konsekvent?

### Tillgänglighet
- [ ] Fokus-states synliga?
- [ ] Färgkontrast uppfyller WCAG AA (minst 4.5:1)?
- [ ] Touch-targets minst 44x44px på mobil?
```

**Prettier-konfiguration (auto-formattering):**

```javascript
// .prettierrc.js
module.exports = {
  plugins: ['prettier-plugin-tailwindcss'],
  tailwindConfig: './tailwind.config.ts',
  tailwindFunctions: ['cn', 'clsx', 'cva'], // Custom merge-funktioner
}
```

**ESLint-regler:**

```javascript
// .eslintrc.js
module.exports = {
  extends: ['plugin:tailwindcss/recommended'],
  rules: {
    'tailwindcss/classnames-order': 'error',
    'tailwindcss/no-custom-classname': ['error', {
      whitelist: ['custom-scrollbar'], // Tillåt specifika
    }],
    'tailwindcss/no-contradicting-classname': 'error',
  },
}
```

#### 6. **Testing & Visual Regression**

**Unit-testa komponenter med Tailwind:**

```typescript
// Button.test.tsx
import { render } from '@testing-library/react'
import { Button } from './Button'

describe('Button', () => {
  it('renders with primary styles', () => {
    const { container } = render(<Button variant="primary">Click</Button>)
    const button = container.firstChild

    expect(button).toHaveClass('bg-primary')
    expect(button).toHaveClass('text-white')
  })
})
```

**Visual regression testing (Chromatic/Percy):**

```typescript
// Button.stories.tsx (Storybook)
import type { Meta, StoryObj } from '@storybook/react'
import { Button } from './Button'

const meta: Meta<typeof Button> = {
  component: Button,
  parameters: {
    chromatic: { viewports: [375, 768, 1200] }, // Test alla breakpoints
  },
}

export default meta

export const AllVariants: StoryObj = {
  render: () => (
    <div className="space-y-4">
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="danger">Danger</Button>
    </div>
  ),
}
```

#### 7. **Accessibility med Tailwind**

**WCAG-kompatibla färger:**

```typescript
// tokens/colors.ts
import { contrast } from 'polished'

export const colors = {
  primary: {
    DEFAULT: '#3b82f6', // 4.58:1 kontrast mot vit (AA-godkänd)
    dark: '#1e40af',    // 8.23:1 kontrast (AAA)
  },
}

// Validering i byggprocess
Object.entries(colors).forEach(([name, shades]) => {
  Object.entries(shades).forEach(([shade, color]) => {
    const contrastRatio = contrast(color, '#ffffff')
    if (contrastRatio < 4.5) {
      console.warn(`${name}-${shade} har dålig kontrast: ${contrastRatio}`)
    }
  })
})
```

**Fokus-states:**

```css
@layer base {
  /* Standardisera fokus-rings */
  *:focus-visible {
    @apply outline-none ring-2 ring-primary ring-offset-2;
  }
}
```

**Screen reader-only utilities:**

```css
@layer utilities {
  .sr-only {
    @apply absolute w-px h-px p-0 -m-px overflow-hidden whitespace-nowrap border-0;
    clip: rect(0, 0, 0, 0);
  }
}
```

### Exempel

#### Exempel 1: Enterprise Monorepo Setup (Komplett)

**Projektstruktur:**

```
enterprise-app/
├── apps/
│   ├── customer-portal/     # Next.js 15
│   ├── admin-dashboard/     # Next.js 15
│   └── marketing-site/      # Astro
├── packages/
│   ├── ui/                  # Komponentbibliotek
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Card.tsx
│   │   │   │   └── Input.tsx
│   │   │   ├── styles/
│   │   │   │   └── globals.css
│   │   │   └── index.ts
│   │   ├── tailwind.config.ts
│   │   └── package.json
│   ├── design-tokens/       # Delat design system
│   │   ├── colors.ts
│   │   ├── spacing.ts
│   │   ├── typography.ts
│   │   └── index.ts
│   └── tailwind-preset/     # Delad config
│       ├── index.ts
│       └── package.json
├── turbo.json
├── package.json
└── .github/
    └── workflows/
        └── ci.yml
```

**packages/design-tokens/colors.ts:**

```typescript
export const colors = {
  // Semantic tokens
  primary: {
    50: '#eff6ff',
    100: '#dbeafe',
    500: '#3b82f6', // Main
    600: '#2563eb',
    900: '#1e3a8a',
  },
  surface: {
    base: '#ffffff',
    raised: '#f9fafb',
    overlay: '#ffffff',
  },
  text: {
    primary: '#111827',
    secondary: '#6b7280',
    tertiary: '#9ca3af',
    inverse: '#ffffff',
  },
  status: {
    success: '#10b981',
    warning: '#f59e0b',
    error: '#ef4444',
    info: '#3b82f6',
  },
  border: {
    DEFAULT: '#e5e7eb',
    strong: '#d1d5db',
  },
} as const
```

**packages/tailwind-preset/index.ts:**

```typescript
import type { Config } from 'tailwindcss'
import { colors, spacing, typography } from '@repo/design-tokens'

export default {
  theme: {
    extend: {
      colors,
      spacing,
      fontFamily: typography.fonts,
      fontSize: typography.sizes,
    },
  },
  plugins: [
    require('@tailwindcss/forms')({
      strategy: 'class',
    }),
    require('@tailwindcss/typography'),
  ],
} satisfies Partial<Config>
```

**packages/ui/tailwind.config.ts:**

```typescript
import type { Config } from 'tailwindcss'
import basePreset from '@repo/tailwind-preset'

export default {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  presets: [basePreset],
} satisfies Config
```

**packages/ui/src/components/Button.tsx:**

```typescript
import { cva, type VariantProps } from 'class-variance-authority'
import { forwardRef } from 'react'

const button = cva(
  'inline-flex items-center justify-center font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed',
  {
    variants: {
      variant: {
        primary: 'bg-primary-500 text-white hover:bg-primary-600 focus:ring-primary-500',
        secondary: 'bg-surface-raised text-text-primary hover:bg-gray-200 focus:ring-gray-400',
        outline: 'border-2 border-primary-500 text-primary-500 hover:bg-primary-50 focus:ring-primary-500',
        ghost: 'text-primary-500 hover:bg-primary-50 focus:ring-primary-500',
        danger: 'bg-status-error text-white hover:bg-red-700 focus:ring-status-error',
      },
      size: {
        sm: 'text-sm px-3 py-1.5 rounded-md',
        md: 'text-base px-6 py-3 rounded-lg',
        lg: 'text-lg px-8 py-4 rounded-xl',
      },
      fullWidth: {
        true: 'w-full',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof button> {
  loading?: boolean
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, fullWidth, loading, children, disabled, ...props }, ref) => {
    return (
      <button
        ref={ref}
        className={button({ variant, size, fullWidth, className })}
        disabled={disabled || loading}
        {...props}
      >
        {loading && <Spinner className="mr-2" />}
        {children}
      </button>
    )
  }
)
Button.displayName = 'Button'
```

**apps/customer-portal/tailwind.config.ts:**

```typescript
import type { Config } from 'tailwindcss'
import basePreset from '@repo/tailwind-preset'

export default {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    // Inkludera UI-biblioteket
    '../../packages/ui/src/**/*.{js,ts,jsx,tsx}',
  ],
  presets: [basePreset],
  theme: {
    extend: {
      // App-specifika overrides om nödvändigt
    },
  },
} satisfies Config
```

**turbo.json (Turborepo-konfiguration):**

```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**", "build/**"]
    },
    "build:css": {
      "cache": true,
      "outputs": ["dist/styles.css"]
    },
    "lint": {
      "dependsOn": ["^lint"]
    },
    "test": {
      "dependsOn": ["^build"],
      "cache": true
    }
  }
}
```

#### Exempel 2: CI/CD Pipeline med CSS-validering

**.github/workflows/ci.yml:**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint Tailwind classes
        run: npm run lint:tailwind

      - name: Build CSS
        run: NODE_ENV=production npm run build:css

      - name: Check CSS bundle size
        run: |
          MAX_SIZE=15000  # 15kB gzipped
          ACTUAL_SIZE=$(gzip -c apps/web-app/dist/output.css | wc -c)

          echo "CSS bundle size: ${ACTUAL_SIZE} bytes (gzipped)"

          if [ $ACTUAL_SIZE -gt $MAX_SIZE ]; then
            echo "❌ CSS bundle too large!"
            echo "Max allowed: ${MAX_SIZE} bytes"
            echo "Actual: ${ACTUAL_SIZE} bytes"
            exit 1
          fi

          echo "✅ CSS bundle size OK"

      - name: Visual regression tests
        run: npm run test:visual
        env:
          CHROMATIC_PROJECT_TOKEN: ${{ secrets.CHROMATIC_TOKEN }}

      - name: Upload CSS artifacts
        uses: actions/upload-artifact@v4
        with:
          name: css-bundle
          path: apps/*/dist/*.css

  deploy:
    needs: lint-and-test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to production
        run: npm run deploy
```

#### Exempel 3: Verklig Case Study - E-handelsplattform

**Scenario:**
Ett företag bygger en e-handelsplattform med:
- Kundsida (Next.js)
- Admin-panel (React + Vite)
- Mobil-app (React Native med Tailwind via Nativewind)
- Delad komponentbibliotek

**Utmaningar:**
- Konsekvent design över 3 plattformar
- 50+ utvecklare i teamet
- Performance-krav: <2s laddningstid
- Tillgänglighet: WCAG AAA

**Lösning:**

**1. Design Token System:**
```typescript
// packages/tokens/src/index.ts
export const tokens = {
  colors: {
    brand: {
      primary: '#FF6B00',  // Företagsfärg
      secondary: '#00A3FF',
    },
    // ... 50+ fler färger
  },
  spacing: {
    // Fibonacci-baserad skala för harmoniska avstånd
    0: '0',
    1: '0.25rem',  // 4px
    2: '0.5rem',   // 8px
    3: '0.75rem',  // 12px
    5: '1.25rem',  // 20px
    8: '2rem',     // 32px
    13: '3.25rem', // 52px
    21: '5.25rem', // 84px
  },
}
```

**2. Komponentbibliotek med Storybook:**
```bash
packages/ui/
├── src/
│   ├── components/
│   │   ├── Product/
│   │   │   ├── ProductCard.tsx
│   │   │   ├── ProductCard.stories.tsx
│   │   │   ├── ProductCard.test.tsx
│   │   │   └── index.ts
│   │   ├── Cart/
│   │   └── Checkout/
│   ├── hooks/
│   └── utils/
└── .storybook/
```

**3. Performance-resultat:**
- Initial CSS bundle: **8.2kB** gzipped
- Lighthouse score: **98/100**
- Laddningstid: **1.4s** (3G)

**4. Team Workflow:**
- Automatisk CSS-bundle check i PR
- Visual regression för alla komponenter
- Tillgänglighetstest i CI
- Storybook deployed för varje PR

### Visualisering: Enterprise Tailwind Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         ENTERPRISE TAILWIND ARCHITECTURE (2025)             │
└─────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│  LAYER 1: Design Tokens (Source of Truth)                   │
│  ▸ colors.ts, spacing.ts, typography.ts                      │
│  ▸ Versionshanterad i @company/design-tokens                 │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  LAYER 2: Tailwind Preset                                   │
│  ▸ Konverterar tokens → Tailwind theme                      │
│  ▸ Inkluderar plugins, safelist                             │
│  ▸ @company/tailwind-preset                                 │
└────────────────────┬─────────────────────────────────────────┘
                     │
                     ├──────────────┬───────────────┐
                     ▼              ▼               ▼
┌─────────────┐ ┌──────────┐ ┌────────────────┐
│  LAYER 3:   │ │  LAYER 3:│ │   LAYER 3:     │
│  UI Package │ │  Web App │ │   Admin Panel  │
│  (Library)  │ │  (Next)  │ │   (Vite)       │
└─────────────┘ └──────────┘ └────────────────┘
     │                │              │
     │                │              │
     └────────────────┴──────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────────┐
│  LAYER 4: Build & Deploy                                    │
│  ▸ Turborepo för builds                                     │
│  ▸ CSS-bundle optimization                                  │
│  ▸ CDN distribution                                          │
└──────────────────────────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Tip 1: Använd Tailwind Play för prototyping
[Tailwind Play](https://play.tailwindcss.com/) är perfekt för att snabbt testa idéer och dela kod med teamet. Kopiera din config och börja experimentera direkt!

#### Tip 2: Dokumentera i koden med JSDoc
```typescript
/**
 * Primary action button
 *
 * @example
 * ```tsx
 * <Button variant="primary" size="lg">
 *   Click me
 * </Button>
 * ```
 */
export const Button = () => { ... }
```

#### Tip 3: Automatisera design token-uppdateringar
```typescript
// scripts/sync-figma-tokens.ts
// Synka Figma design tokens → code automatiskt
import { FigmaClient } from '@figma/api'
import { writeFileSync } from 'fs'

const client = new FigmaClient(process.env.FIGMA_TOKEN!)
const tokens = await client.getVariables('file-key')

writeFileSync(
  'packages/tokens/src/colors.ts',
  generateTokenFile(tokens)
)
```

### ✏️ Övningar

#### Övning 1: Sätt upp ett Monorepo
**Uppgift:** Skapa ett Turborepo med:
- 2 appar (Next.js + Vite)
- 1 delat UI-paket
- Delad Tailwind-preset

**Facit: Se Exempel 1 ovan**

#### Övning 2: Migrera från v3 till v4
**Uppgift:** Konvertera en befintlig Tailwind v3-konfiguration till v4 CSS-first format.

**Innan (v3):**
```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#3b82f6',
      },
    },
  },
}
```

**Efter (v4):**
```css
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
}
```

#### Övning 3: Performance Audit
**Uppgift:** Analysera och optimera ett projekts CSS-bundle.

**Steg:**
1. Bygg production-versionen
2. Mät bundle-storlek (gzipped)
3. Identifiera oanvända klasser
4. Optimera till <10kB

**Verktyg:**
```bash
# 1. Bygg
npm run build

# 2. Analysera
ls -lh dist/output.css
gzip -c dist/output.css | wc -c

# 3. Hitta oanvända (PurgeCSS)
npx purgecss --css dist/output.css --content 'src/**/*.html'

# 4. Validera i CI (se Exempel 2)
```

#### Övning 4: Accessibility Audit
**Uppgift:** Validera att alla färger uppfyller WCAG AA-kontrast.

```typescript
import { contrast } from 'polished'

const validateColors = (colors: Record<string, string>) => {
  const failures: string[] = []

  Object.entries(colors).forEach(([name, hex]) => {
    const ratio = contrast(hex, '#ffffff')

    if (ratio < 4.5) {
      failures.push(`${name}: ${ratio.toFixed(2)} (behöver ≥4.5)`)
    }
  })

  if (failures.length > 0) {
    console.error('❌ Kontrast-fel:', failures)
    process.exit(1)
  }

  console.log('✅ Alla färger är tillgängliga!')
}
```

#### Övning 5: Skapa ett Design System Playground
**Uppgift:** Bygg en intern webbplats som visar alla komponenter, färger och spacing.

**Struktur:**
```tsx
// app/design-system/page.tsx
export default function DesignSystemPage() {
  return (
    <div className="p-8 max-w-7xl mx-auto">
      <h1>Design System</h1>

      <section>
        <h2>Colors</h2>
        <ColorPalette />
      </section>

      <section>
        <h2>Typography</h2>
        <TypographyScale />
      </section>

      <section>
        <h2>Components</h2>
        <ComponentShowcase />
      </section>
    </div>
  )
}
```

### 📝 Sammanfattning

**Key Takeaways:**

✅ **Tailwind v4** introducerar CSS-first configuration, automatisk content-detektion och native CSS variables
✅ **Monorepos** kräver delad preset-konfiguration och design tokens för konsistens
✅ **Production optimization** fokuserar på CSS bundle-storlek, caching och critical CSS
✅ **Modern tooling** (Vite, Next.js 15) har första-klass Tailwind-integration
✅ **Team workflows** kräver linting, formattering och code review-standarder
✅ **CI/CD** bör inkludera CSS bundle size checks och visual regression testing
✅ **Accessibility** är inte optional – validera kontrast, fokus-states och touch-targets
✅ **Enterprise** kräver skalbar arkitektur, dokumentation och governance

**Ny ordlista (Nivå 5):**

- **Monorepo**: Ett repository med flera projekt/paket
- **Preset**: Återanvändbar Tailwind-konfiguration
- **Turborepo**: Build-system optimerat för monorepos
- **Critical CSS**: Minimal CSS för initial rendering
- **Visual regression**: Automatisk testning av UI-förändringar
- **Design tokens**: Abstrakta designvärden (färger, spacing) oberoende av implementation
- **Safelist**: Klasser som aldrig ska purgeas
- **Bundle size**: Total storlek av CSS-filer
- **WCAG**: Web Content Accessibility Guidelines
- **Chromatic**: Visual testing-plattform

**Grattis!** 🎉

Du har nu genomfört hela guiden från nybörjare till expert! Du behärskar:
- Utility-first-filosofin
- Responsiv design och dark mode
- Konfiguration och optimering
- Best practices och anti-patterns
- Enterprise-arkitektur och produktionsmiljöer

**Nästa steg:**

- Bygg ett verkligt projekt med Tailwind
- Bidra till open source Tailwind-projekt
- Dela din kunskap med teamet
- Håll dig uppdaterad med Tailwind v4+ features

Lycka till på din resa som Tailwind-expert! 🚀

---

## 🎓 Slutlig Självutvärdering

Använd denna checklista för att bedöma din Tailwind-kunskap:

### Nivå 1: Grundläggande förståelse (👶)
- [ ] Jag kan förklara vad Tailwind CSS är med egna ord
- [ ] Jag förstår skillnaden mellan utility-first och traditionell CSS
- [ ] Jag känner igen grundläggande Tailwind-klasser (bg-, text-, p-, m-)
- [ ] Jag förstår konceptet med "byggstenar" vs "skriva från scratch"

### Nivå 2: Praktisk användning (🧒)
- [ ] Jag kan använda Tailwind för att styla enkla komponenter
- [ ] Jag förstår färgsystemet (färg-nyans: blue-500)
- [ ] Jag kan skapa responsiva layouter med breakpoints (sm:, md:, lg:)
- [ ] Jag kan använda hover:, focus: och andra states
- [ ] Jag förstår flexbox och grid i Tailwind
- [ ] Jag kan bygga en enkel webbsida från scratch med Tailwind

### Nivå 3: Konfiguration & Djupare förståelse (🎓)
- [ ] Jag förstår hur JIT-mode fungerar
- [ ] Jag kan konfigurera tailwind.config.js
- [ ] Jag förstår skillnaden mellan theme och theme.extend
- [ ] Jag kan använda @layer och @apply korrekt
- [ ] Jag förstår när jag bör använda @apply (och när inte)
- [ ] Jag kan implementera dark mode
- [ ] Jag kan använda arbiträra värden när nödvändigt

### Nivå 4: Best Practices & Skalbarhet (🏛️)
- [ ] Jag kan strukturera ett större Tailwind-projekt
- [ ] Jag förstår design tokens och semantisk namngivning
- [ ] Jag kan identifiera och undvika anti-patterns
- [ ] Jag kan extrahera återanvändbara komponenter effektivt
- [ ] Jag förstår komponent-hierarkin (utilities → UI → features → pages)
- [ ] Jag kan implementera ett dark mode-system med CSS variables
- [ ] Jag kan optimera CSS bundle-storlek för production
- [ ] Jag känner till class-variance-authority (CVA)

### Nivå 5: Enterprise & Masternivå (💼)
- [ ] Jag kan sätta upp en monorepo med delad Tailwind-konfiguration
- [ ] Jag förstår Tailwind v4:s nya features (@theme, CSS-first)
- [ ] Jag kan integrera Tailwind med moderna ramverk (Next.js, Vite, Astro)
- [ ] Jag kan implementera CI/CD-pipelines med CSS-validering
- [ ] Jag förstår accessibility-krav (WCAG) och kan validera dem
- [ ] Jag kan skriva visual regression tests för Tailwind-komponenter
- [ ] Jag kan designa en skalbar enterprise-arkitektur för Tailwind
- [ ] Jag kan leda ett team i Tailwind best practices

### Resultat:

- **0-8 checkboxar**: Börja med Nivå 1 och jobba dig uppåt
- **9-16 checkboxar**: Du är på rätt väg! Fokusera på Nivå 2-3
- **17-24 checkboxar**: Bra jobbat! Nivå 4 kommer göra dig mycket starkare
- **25-30 checkboxar**: Du är nästan expert! Nivå 5 ger dig sista pushen
- **31+ checkboxar**: Du är en Tailwind-expert! Överväg att dela din kunskap

---

## 📖 Ordlista

Här hittar du alla viktiga termer från guiden, alfabetiskt sorterade:

### A
**@apply** - Direktiv för att använda Tailwind utility-klasser i egen CSS
**@layer** - Direktiv för att organisera CSS i lager (base, components, utilities)
**@theme** - (v4) Direktiv för att definiera design tokens direkt i CSS
**Anti-pattern** - Ett dåligt eller olämpligt designmönster att undvika
**Arbiträra värden** - Custom värden med bracket-syntax, t.ex. `w-[347px]`

### B
**Barrel export** - En index.js som exporterar alla komponenter från en mapp
**Best practice** - Rekommenderat arbetssätt som är beprövat och effektivt
**Border** - Kant eller ram runt ett element
**Breakpoint** - En skärmstorlek där designen ändras (sm, md, lg, xl, 2xl)
**Bundle size** - Total storlek av CSS-filer efter kompilering

### C
**CDN** - Content Delivery Network, för snabb distribution av filer
**Class** - En CSS-klass; i Tailwind oftast en utility-klass
**Component** - En återanvändbar byggsten i UI
**Component hierarchy** - Pyramid-struktur från utilities till pages
**Compound variants** - Kombinationer av varianter med speciell styling (CVA)
**Container** - En wrapper som begränsar maxbredd och centrerar innehåll
**content-array** - Lista i config som anger vilka filer Tailwind ska skanna
**Critical CSS** - Minimal CSS som laddas först för snabb rendering
**CSS variables** - Dynamiska variabler i CSS, t.ex. `--color-primary`
**CVA (Class Variance Authority)** - Bibliotek för att hantera komponentvarianter

### D
**Dark mode** - Mörkt färgtema för UI
**Design system** - Samling av regler och komponenter för konsekvent design
**Design tokens** - Abstrakta designvärden (färger, spacing) oberoende av implementation

### F
**Flexbox** - Ett layoutsystem för att arrangera element flexibelt
**Focus** - När ett element är valt/aktivt (t.ex. input-fält)

### G
**Gap** - Mellanrum mellan element i flex eller grid
**Gradient** - En färgövergång från en färg till en annan
**Grid** - Ett 2D-layoutsystem med rader och kolumner

### H
**Hover** - När muspekaren är över ett element

### J
**JIT (Just-In-Time)** - Kompileringsläge som genererar CSS on-demand (standard i v3+)

### L
**Layout** - Hur element är arrangerade på sidan

### M
**Margin** - Utrymme utanför ett element
**Mobile First** - Designa för mobil först, lägg till för större skärmar sedan
**Monorepo** - Ett repository med flera projekt/paket

### P
**Padding** - Luften/utrymmet inuti ett element runt innehållet
**Plugin** - Tillägg som utökar Tailwinds funktionalitet
**Preset** - Återanvändbar Tailwind-konfiguration
**Purging** - Process att ta bort oanvänd CSS (automatiskt i JIT)

### R
**Responsive design** - Design som anpassar sig till olika skärmstorlekar

### S
**Safelist** - Lista över klasser som aldrig ska purgeas
**Semantic naming** - Namngivning baserad på syfte (primary) istället för utseende (blue)
**Specificity** - CSS-konceptet om vilken regel som "vinner" när flera appliceras
**State** - Ett elements tillstånd (hover, focus, active)

### T
**theme.extend** - Konfigurationssektion för att lägga till custom värden
**Transition** - Mjuk animering mellan två states
**Turborepo** - Build-system optimerat för monorepos

### U
**Utility-first** - Tankesättet att bygga design genom att kombinera små klasser
**Utility-klass** - En färdig CSS-klass som gör EN sak (t.ex. "gör text röd")

### V
**Variant** - En variation av en komponent (t.ex. primary, secondary button)
**Visual regression** - Automatisk testning av UI-förändringar

### W
**WCAG** - Web Content Accessibility Guidelines (tillgänglighetsstandarder)

---

## 🔗 Resurser för Fördjupning

### Officiell Dokumentation

**Tailwind CSS Docs**
- https://tailwindcss.com/docs
- Den ultimata referensen för alla Tailwind-klasser och features
- Uppdateras kontinuerligt med nya versioner

**Tailwind CSS v4 Announcement**
- https://tailwindcss.com/blog/tailwindcss-v4
- Komplett genomgång av v4-features och migration

**Tailwind Play**
- https://play.tailwindcss.com/
- Interaktiv playground för att testa Tailwind direkt i browsern

### Video-kurser & Tutorials

**Tailwind Labs YouTube**
- https://www.youtube.com/@TailwindLabs
- Officiella videos, tips och livestreams från Tailwind-teamet

**Scrimba: Learn Tailwind CSS**
- https://scrimba.com/learn/tailwind
- Interaktiv gratis kurs för nybörjare

**Frontend Masters: Tailwind CSS**
- https://frontendmasters.com/
- Djupgående betalkurser för alla nivåer

### Verktyg & Plugins

**Tailwind CSS IntelliSense**
- VS Code extension för autocomplete och preview
- https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss

**Prettier Plugin for Tailwind CSS**
- Automatisk sortering av klasser
- https://github.com/tailwindlabs/prettier-plugin-tailwindcss

**Headless UI**
- Oanvända, fullt tillgängliga UI-komponenter för Tailwind
- https://headlessui.com/

**Class Variance Authority (CVA)**
- Hantera komponentvarianter elegant
- https://cva.style/

**clsx / classnames**
- Hjälpbibliotek för att kombinera klassnamn
- https://github.com/lukeed/clsx

### Community & Inspiration

**Tailwind UI**
- Officiella premium-komponenter och templates
- https://tailwindui.com/

**Tailwind Components**
- Gratis community-komponenter
- https://tailwindcomponents.com/

**Tailwind Toolbox**
- Templates, komponenter och resurser
- https://www.tailwindtoolbox.com/

**Flowbite**
- Open-source komponentbibliotek
- https://flowbite.com/

**DaisyUI**
- Komponentbibliotek byggt på Tailwind
- https://daisyui.com/

### Böcker

**"Refactoring UI" av Adam Wathan & Steve Schoger**
- Design-principer från Tailwinds skapare
- https://www.refactoringui.com/

### Bloggar & Artiklar

**Tailwind CSS Blog**
- https://tailwindcss.com/blog
- Officiella uppdateringar och djupdykningar

**Adam Wathan (Twitter/X)**
- https://twitter.com/adamwathan
- Tailwinds skapare delar tips och insikter

**CSS-Tricks: Tailwind CSS**
- https://css-tricks.com/tag/tailwind/
- Artiklar och guider om Tailwind

### Podcasts

**Full Stack Radio**
- Podcast av Adam Wathan
- https://fullstackradio.com/

### GitHub

**Tailwind CSS Repository**
- https://github.com/tailwindlabs/tailwindcss
- Källkod, issues och diskussioner

**Awesome Tailwind CSS**
- Kurerad lista med Tailwind-resurser
- https://github.com/aniftyco/awesome-tailwindcss

---

## ❓ Vanliga Frågor (FAQ)

### Allmänna Frågor

**F: Är Tailwind verkligen bättre än vanlig CSS?**
S: Det beror på! Tailwind är fantastiskt för:
- Snabb prototyping
- Konsekvent design utan att skriva mycket CSS
- Projekt med komponent-baserade ramverk (React, Vue)

Vanlig CSS kan vara bättre för:
- Mycket unika, konstnärliga designs
- Enkla statiska webbplatser
- Om du älskar att skriva CSS från scratch

Det är inte antingen-eller – många använder båda!

**F: Blir inte HTML:en ful med alla klasser?**
S: I början känns det konstigt, men:
- Du vänjer dig snabbt
- Med komponenter (React/Vue) skriver du varje klasslista bara en gång
- Fördelarna (snabbhet, konsistens) överväger
- Använd Prettier plugin för automatisk formattering

**F: Hur stor blir CSS-filen?**
S: Tack vare JIT-mode och purging:
- Typiskt 8-15kB gzipped i production
- Endast klasser du faktiskt använder inkluderas
- Detta är mindre än många traditionella CSS-ramverk

**F: Kan jag använda Tailwind med [mitt ramverk]?**
S: Ja! Tailwind fungerar med:
- React, Next.js, Remix
- Vue, Nuxt
- Svelte, SvelteKit
- Angular
- Astro
- Vanilla HTML/JavaScript
- ...och praktiskt taget alla moderna ramverk!

### Tekniska Frågor

**F: Vad är skillnaden mellan v3 och v4?**
S: V4 introducerar:
- CSS-first konfiguration (@theme)
- Automatisk content-detektion
- 3.5x snabbare full rebuilds
- 8x snabbare incremental rebuilds
- Native CSS variables för alla tokens
- Vite plugin för optimal performance

**F: Hur migrerar jag från v3 till v4?**
S: Kör migrations-verktyget:
```bash
npx @tailwindcss/upgrade@next
```
Detta konverterar din config automatiskt!

**F: När ska jag använda @apply?**
S: Använd @apply endast för:
- Genuint återanvända komponenter (knappar, inputs)
- Element med 10+ klasser som används 5+ gånger
- När ramverks-komponenter inte är ett alternativ

Undvik @apply för:
- Allt du kan göra med React/Vue-komponenter
- Enstaka användningar
- Som ersättning för vanlig CSS (då förlorar du fördelarna!)

**F: Hur hanterar jag dynamiska klasser?**
S: Tre sätt:
1. **Safelist** (i config) - för klasser från CMS/API
2. **Fullständiga klassnamn** - undvik string concatenation:
   ```javascript
   // ❌ Fungerar INTE
   <div className={`text-${color}-500`}>

   // ✅ Fungerar
   const classes = {
     red: 'text-red-500',
     blue: 'text-blue-500',
   }
   <div className={classes[color]}>
   ```
3. **Inline styles** - för helt dynamiska värden

**F: Hur testar jag Tailwind-komponenter?**
S: Flera strategier:
- **Unit-tester**: Testa att rätt klasser appliceras
- **Visual regression**: Chromatic, Percy för UI-snapshots
- **E2E-tester**: Cypress, Playwright för funktionalitet
- **Accessibility**: axe-core för WCAG-compliance

### Best Practices

**F: Hur organiserar jag Tailwind i ett stort projekt?**
S: Rekommenderad struktur:
```
src/
├── styles/
│   ├── base/       # Resets, global styling
│   ├── components/ # @apply komponenter om nödvändiga
│   └── utilities/  # Custom utilities
├── components/
│   ├── ui/         # Bas UI-komponenter
│   ├── layout/     # Layout-komponenter
│   └── features/   # Business-komponenter
└── config/
    ├── colors.js   # Design tokens
    └── spacing.js
```

**F: Hur håller jag klassordningen konsekvent?**
S: Installera Prettier plugin:
```bash
npm install -D prettier prettier-plugin-tailwindcss
```
Detta sorterar automatiskt klasserna!

**F: Borde jag använda Tailwind i alla projekt?**
S: Nej, inte nödvändigtvis! Använd Tailwind när:
- ✅ Du bygger en modern webb-app med React/Vue/Svelte
- ✅ Du vill snabb utveckling med konsekvent design
- ✅ Du har eller planerar ett komponentbibliotek
- ✅ Teamet är villigt att lära sig

Överväg alternativ när:
- ❌ Mycket unik, konstnärlig design som kräver custom CSS
- ❌ Extremt enkelt projekt (enkel statisk sida)
- ❌ Teamet motsätter sig utility-first-filosofin

### Performance & Optimization

**F: Hur optimerar jag för production?**
S: Checklist:
1. Säkerställ korrekt `content`-konfiguration
2. Kör production build: `NODE_ENV=production`
3. Aktivera minifiering
4. Använd CDN med caching
5. Överväg critical CSS-extraktion
6. Validera bundle size i CI/CD

**F: Varför fungerar inte mina klasser i production?**
S: Vanliga orsaker:
- **Content-konfiguration missar filer**: Lägg till alla template-filer
- **Dynamiska klassnamn**: Använd safelist eller fullständiga klassnamn
- **Fel build-kommando**: Kör med `NODE_ENV=production`
- **Cache-problem**: Rensa browser-cache och rebuilda

### Dark Mode

**F: Vilken dark mode-strategi bör jag välja?**
S:
- **`class`**: Bäst för manuell kontroll, användarinställningar
- **`media`**: Bäst för automatisk system-baserad dark mode
- **CSS variables**: Mest flexibelt för komplexa teman

Rekommendation: Börja med `class` för maximal kontroll.

**F: Hur kombinerar jag Tailwind dark mode med CSS variables?**
S:
```css
:root {
  --color-bg: 255 255 255;
}

.dark {
  --color-bg: 17 24 39;
}
```

```javascript
// tailwind.config.js
colors: {
  'bg-primary': 'rgb(var(--color-bg) / <alpha-value>)',
}
```

### Accessibility

**F: Är Tailwind tillgängligt (accessible)?**
S: Tailwind själv är neutral, men du kan bygga både tillgänglig och otillgänglig UI. Tips:
- Validera färgkontrast (minst 4.5:1 för WCAG AA)
- Använd semantisk HTML
- Lägg till fokus-states (`focus:ring-2 focus:ring-primary`)
- Testa med screen readers
- Använd `sr-only` för screen reader-only content

**F: Hur validerar jag färgkontrast?**
S: Använd verktyg som:
- Polished-biblioteket: `contrast(color1, color2)`
- Online: WebAIM Contrast Checker
- Browser DevTools: Lighthouse accessibility audit

### Monorepos & Enterprise

**F: Hur delar jag Tailwind-konfiguration i en monorepo?**
S: Skapa ett `tailwind-preset`-paket:
```typescript
// packages/tailwind-preset/index.ts
export default {
  theme: {
    extend: {
      colors: { /* dina färger */ },
    },
  },
} satisfies Partial<Config>

// apps/web/tailwind.config.ts
import preset from '@repo/tailwind-preset'

export default {
  presets: [preset],
  content: ['./src/**/*.tsx'],
}
```

**F: Hur hanterar jag Tailwind i en CI/CD-pipeline?**
S: Best practices:
- Validera CSS bundle size
- Kör linting (eslint-plugin-tailwindcss)
- Visual regression tests (Chromatic)
- Accessibility tests (axe-core)
- Cache node_modules för snabbare builds

---

**Har du fler frågor?**

- 📖 Kolla dokumentationen: https://tailwindcss.com/docs
- 💬 Ställ frågor i Tailwind Discord: https://tailwindcss.com/discord
- 🐛 Rapportera bugs: https://github.com/tailwindlabs/tailwindcss/issues

---

## 🎉 Avslutning

Grattis till att ha kommit igenom hela denna guide! Du har nu en solid grund i Tailwind CSS, från grunderna till enterprise-nivå.

### Din resa fortsätter

**Nästa steg:**
1. **Bygg något**: Det bästa sättet att lära är genom att göra
2. **Dela kunskap**: Lär andra – det stärker din egen förståelse
3. **Håll dig uppdaterad**: Följ Tailwind-bloggen och release notes
4. **Experimentera**: Testa nya patterns och verktyg
5. **Bidra**: Open source-bidrag till Tailwind eller plugins

### Kom ihåg

- ✨ Utility-first är ett tankesätt, inte bara ett ramverk
- 🚀 Snabbhet kommer med övning – ge det tid
- 🎨 Design-system ger konsistens och skalbarhet
- 🔧 Rätt verktyg gör stor skillnad (IntelliSense, Prettier)
- 🤝 Community är din vän – tveka inte att fråga

### Tack!

Tack för att du läste denna guide. Jag hoppas den har gett dig värdefulla insikter och kunskap som du kan använda i dina projekt.

**Lycka till med din Tailwind-resa!** 🎨✨

---

*Guiden uppdaterad: November 2025*
*Baserad på Tailwind CSS v3+ och v4*

