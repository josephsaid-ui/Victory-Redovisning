# Ghidra – Den Kompletta Guiden till Reverse Engineering

## 📚 Innehållsförteckning

1. [Om Denna Guide](#-om-denna-guide)
2. [Nivå 1: Ghidra som magiskt förstoringsglas 👶](#nivå-1-ghidra-som-magiskt-förstoringsglas-)
3. [Nivå 2: Förstå grundspråket i Ghidra 🧒](#nivå-2-förstå-grundspråket-i-ghidra-)
4. [Nivå 3: Din första riktiga analys i Ghidra 🎓](#nivå-3-din-första-riktiga-analys-i-ghidra-)
5. [Nivå 4: Avancerade analyser och scripting i Ghidra 🏛️](#nivå-4-avancerade-analyser-och-scripting-i-ghidra-️)
6. [Nivå 5: Professionell reverse engineering med Ghidra 💼](#nivå-5-professionell-reverse-engineering-med-ghidra-)
7. [Slutlig Självutvärdering 🎓](#-slutlig-självutvärdering)
8. [Ordlista 📖](#-ordlista)
9. [Resurser för Fördjupning 🔗](#-resurser-för-fördjupning)
10. [Vanliga Frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

Välkommen till den mest omfattande guiden om **Ghidra** – det kraftfulla verktyget för reverse engineering som utvecklades av NSA och släpptes som open source 2019.

### Vem är denna guide för?

Denna guide är designad för **alla** – från nyfikna nybörjare som aldrig hört talas om reverse engineering, till erfarna utvecklare och säkerhetsanalytiker som vill fördjupa sina kunskaper i Ghidra.

### Progressionen

Guiden är uppbyggd i **5 nivåer** som gradvis ökar i komplexitet:

- **Nivå 1 (👶 5-åringen)**: Enkla analogier och grundkoncept utan teknisk jargong
- **Nivå 2 (🧒 10-åringen)**: Introduktion till viktiga termer och Ghidras gränssnitt
- **Nivå 3 (🎓 Gymnasiet)**: Praktisk användning, installation och första analyser
- **Nivå 4 (🏛️ Universitet)**: Avancerade tekniker, scripting och best practices
- **Nivå 5 (💼 Expert)**: Professionell användning, moderna workflows och verkliga case studies

### Hur du bör läsa denna guide

- **Läs progressivt**: Varje nivå bygger på den föregående. Hoppa inte över nivåer om du är ny.
- **Gör övningarna**: Teoretisk kunskap är värdefull, men praktisk erfarenhet är ovärderlig.
- **Ta din tid**: Varje nivå tar 10-20 minuter att läsa, men övningarna kan ta längre tid.
- **Återkom**: Använd guiden som referens när du arbetar med Ghidra.

### Total tidsåtgång

- **Läsning**: 1.5-3 timmar
- **Övningar**: 5-15 timmar (beroende på förkunskaper och fördjupningsnivå)

### Vad du kommer att lära dig

- Vad Ghidra är och varför det finns
- Grundläggande koncept inom reverse engineering
- Hur man installerar och använder Ghidra
- Analysera program från enkla till komplexa
- Scripting och automation
- Professionella workflows och best practices
- Etiska och juridiska aspekter
- Moderna features och plugins (2023-2025)

Låt oss börja resan från nybörjare till expert!

---

## Nivå 1: Ghidra som magiskt förstoringsglas 👶

### Introduktion

På denna nivå ska vi förstå **vad Ghidra gör** utan att använda komplicerade ord. Tänk dig att du har en leksak som du inte kan öppna – men du vill förstå hur den fungerar inuti. Ghidra är som ett specialverktyg som hjälper oss att titta inuti färdiga saker och förstå hur de är byggda. Detta steg är viktigt eftersom det ger dig den grundläggande förståelsen av *varför* vi behöver verktyg som Ghidra, innan vi lär oss *hur* de fungerar.

### Kärnkoncept

#### 1. Program är som slutna lådor

Tänk dig att program (som spel, appar eller andra saker på datorn) är som **färdigbyggda leksaker i slutna lådor**. När någon ger dig en leksak kan du använda den, men du kan inte se inuti hur alla delar passar ihop.

#### 2. Att titta inuti utan att förstöra

Ghidra är som ett **magiskt förstoringsglas** som låter dig titta inuti lådan utan att krossa den. Du kan se alla delar, hur de är kopplade till varandra, och förstå varför leksaken gör det den gör.

#### 3. Hitta hemligheter och pussel

Ibland har lådor **gömda rum** eller delar som är svåra att se. Ghidra hjälper dig att hitta dessa gömda ställen, precis som när du letar efter dolda skatter i ett mysterium.

#### 4. Förstå hur saker fungerar

När du tittar inuti kan du se:
- Vilka **delar** som finns (som knappar, hjul och lampor)
- Hur delarna är **sammankopplade** (vilken knapp gör vad)
- Vad som händer när du **trycker på en knapp** (ljuset tänds, hjulet snurrar)

### Exempel

#### Exempel 1: Leksaksbilen

Föreställ dig en **leksaksbil** som kan köra framåt och bakåt:

- **Utan Ghidra**: Du ser bilen och kan trycka på knapparna. Den kör framåt eller bakåt, men du vet inte *hur*.
- **Med Ghidra**: Du tittar inuti och ser att när du trycker på "framåt-knappen", går en signal till en motor som får hjulen att snurra åt ett håll. När du trycker på "bakåt-knappen", snurrar motorn åt andra hållet.

Nu förstår du inte bara *vad* bilen gör, utan *hur* den gör det!

#### Exempel 2: Det hemliga meddelandet

Din kompis ger dig en **låda med ett hemligt meddelande** inuti:

- **Utan Ghidra**: Du ser bara en låda. Du kan skaka den och höra något inuti, men du vet inte vad.
- **Med Ghidra**: Med ditt magiska förstoringsglas ser du inuti lådan och upptäcker att det finns en lapp med texten "Skattjakten börjar vid det stora trädet!".

Ghidra hjälper dig att **läsa** vad som är gömt inuti, även om du inte kan öppna lådan på vanligt sätt.

#### Exempel 3: Pusslet med många rum

Tänk dig ett stort **pussel-hus** med många rum:

- **Utan Ghidra**: Du står utanför huset. Du kan gå in genom dörren och se ett rum, men du ser inte alla andra rum eller hur de är kopplade.
- **Med Ghidra**: Ditt förstoringsglas visar dig en **karta över hela huset** uppifrån. Du ser alla rum, alla dörrar mellan rummen, och kan förstå hur du kommer från ingången till skattkammaren längst bak.

### 💡 Pro Tips

#### Tips 1: Nyfikenhet är din superkraft
När du använder verktyg som Ghidra är det viktigaste att vara **nyfiken**. Fråga dig: "Hur fungerar detta?" och "Varför gör det så här?" – precis som när du tar isär ett pussel för att se hur bitarna passar ihop.

#### Tips 2: Det är okej att inte förstå allt direkt
När du tittar inuti något komplicerat (som ett stort program), ser du kanske **tusentals delar**. Bli inte rädd! Du behöver inte förstå allt på en gång. Börja med en liten del, förstå den, och gå sedan vidare till nästa.

#### Tips 3: Dokumentera vad du upptäcker
Precis som en upptäcktsresande ritar en karta, är det bra att **skriva ner** vad du hittar. "Detta är knappen som tänder lampan", "Här är rummet med skatten". Senare kommer du inte ihåg allt, så anteckningar hjälper dig.

### ✏️ Övningar

#### Övning 1: Rita ditt mysterium-hus ⭐
**Instruktioner**:
1. Tänk på ditt hem eller skola som ett "mysterium-hus"
2. Rita en enkel karta över 3-4 rum
3. Rita linjer (dörrar) som visar hur du kan gå mellan rummen
4. Markera med en X var du börjar och med en stjärna var "skatten" finns

**Lösning**:
Det finns inget rätt eller fel svar! Poängen är att du övar på att tänka på hur saker är **kopplade** till varandra. I Ghidra kommer du att se liknande "kartor" över hur ett program hoppar mellan olika delar.

**Förklaring**:
Detta är din första introduktion till **kontrollflöde** – hur man rör sig från punkt A till punkt B genom olika vägar. I riktiga program är "rummen" olika funktioner, och "dörrarna" är när programmet hoppar från en funktion till en annan.

#### Övning 2: Hemligt meddelande ⭐
**Instruktioner**:
1. Skriv en hemlig mening på ett papper
2. Stoppa det i ett kuvert och stäng det
3. Be någon annan att gissa vad som står inuti *utan att öppna kuvertet*
4. Låt dem sedan öppna och läsa

**Lösning**:
När de inte kan se inuti, måste de **gissa** (kanske baserat på hur tjockt kuvertet är, hur det känns). Men när de öppnar det ser de sanningen direkt.

**Förklaring**:
Detta visar skillnaden mellan att **använda** ett program (hålla ett slutet kuvert) och att **analysera** det med Ghidra (öppna och läsa innehållet). Ghidra "öppnar" program så att vi kan läsa vad de innehåller.

#### Övning 3: Leksaksflöde ⭐
**Instruktioner**:
1. Ta en leksak eller apparat (t.ex. en fjärrkontroll eller lampa)
2. Skriv ner steg-för-steg vad som händer när du använder den:
   - "Jag trycker på knappen"
   - "Lampan tänds"
   - "Jag trycker igen"
   - "Lampan släcks"
3. Rita pilar mellan stegen

**Lösning**:
```
Tryck knapp → Kontrollera om lampan är på
                   ↓
          Ja? → Släck lampan
          Nej? → Tänd lampan
```

**Förklaring**:
Du har precis skapat ditt första **flödesdiagram**! I Ghidra kommer du att se liknande diagram som visar hur ett program fattar beslut ("om knappen är nedtryckt, gör detta; annars gör det").

### 📝 Sammanfattning

#### Key Takeaways
- Program är som **slutna lådor** – vi kan använda dem utan att se inuti
- Ghidra är som ett **magiskt förstoringsglas** som låter oss titta inuti och förstå hur saker fungerar
- Att titta inuti hjälper oss att se **delar**, **kopplingar** och **hemligheter**
- Du behöver inte förstå allt på en gång – börja **smått** och bygg upp din förståelse
- **Nyfikenhet** och **dokumentation** är dina bästa verktyg

#### Ordlista (Nivå 1)
- **Program**: Något som körs på en dator (som spel eller appar)
- **Låda/Sluten låda**: En bild för hur program ser ut när vi inte kan se inuti dem
- **Förstoringsglas**: Verktyg för att titta närmare på saker (Ghidra är ett digitalt "förstoringsglas")
- **Delar**: Små bitar som tillsammans bygger något större
- **Kopplingar**: Hur delar är sammankopplade och påverkar varandra
- **Flöde**: Ordningen saker händer i (först detta, sedan det)

#### Nästa steg
Nu när du förstår **grundidén** om att titta inuti slutna lådor är du redo för nästa nivå, där vi börjar lära oss de riktiga orden som används när vi pratar om Ghidra och program. Du kommer att lära dig vad ord som "binär", "funktion" och "dekompilering" betyder – men oroa dig inte, vi förklarar allt steg för steg!

---

## Nivå 2: Förstå grundspråket i Ghidra 🧒

### Introduktion

Nu är det dags att lära dig det riktiga språket som används inom reverse engineering och Ghidra. På denna nivå kommer du att möta nya ord som "binär", "källkod", "funktion" och "dekompilering". Du kommer också att få en första titt på hur Ghidra ser ut på skärmen. Detta steg är viktigt eftersom du inte kan använda Ghidra effektivt om du inte förstår vad olika delar heter och vad de gör. Tänk på det som att lära dig läsa en karta innan du ger dig ut på en riktig skattjakt!

### Kärnkoncept

#### 1. Från recept till kaka: Källkod och Binär

När någon vill skapa ett program, skriver de **källkod** – det är som ett recept. Källkod är skriven på ett programmeringsspråk (som C, C++, Python eller Java) som människor kan läsa och förstå.

Men datorer kan inte läsa recept direkt! Så källkoden måste "bakas" (översättas) till något datorn förstår – en **binär fil** (också kallad "körbar fil" eller "executable"). Detta är som den färdiga kakan. Kakan ser inte ut som receptet – det är bara färdig mat.

**Exempel från verkligheten**:
- **Recept (källkod)**: "Blanda 2 ägg, 1 dl mjöl, stek i pannan"
- **Kaka (binär)**: En färdig pannkaka på tallriken

När du får en färdig pannkaka kan du äta den, men du kan inte direkt se vilket recept som användes. Ghidra försöker "smaka" på kakan och **gissa** receptet!

#### 2. Maskinkod och Assembler

Inuti en binär fil finns **maskinkod** – enstaka instruktioner som datorn förstår direkt. Maskinkod är jättesvårt för människor att läsa (det ser ut som `48 89 E5 B8 00`).

Därför finns **assembler** – ett språk som är lite mer läsbart för människor, men fortfarande mycket nära vad datorn faktiskt gör. Assembler ser ut ungefär så här:
```
MOV eax, 5      ; Flytta talet 5 till en plats som heter "eax"
ADD eax, 3      ; Addera 3 till det
```

Ghidra visar dig assembler så att du inte behöver läsa rå maskinkod.

#### 3. Funktioner – byggstenar i program

Program är inte bara en lång lista med instruktioner. De är uppdelade i **funktioner** – små avsnitt som gör en specifik sak.

**Exempel från vardagen**:
- **Funktion 1**: "Gör frukost" (ta fram bröd, bred smör, lägg på ost)
- **Funktion 2**: "Duka bordet" (lägg fram tallrik, bestick, glas)
- **Funktion 3**: "Äta frukost" (använd resultatet från funktion 1 och 2)

I Ghidra ser du alla funktioner i ett program. Många har namn som `main`, `calculate`, `print_message`, men ibland har de bara nummer som `FUN_00401000` om Ghidra inte vet vad de heter.

#### 4. Variabler och Minne

När program körs behöver de komma ihåg saker – som siffror, text eller resultat från beräkningar. Dessa lagras i **variabler** (namngivna "lådor" för data) eller direkt i datorns **minne**.

**Exempel**: Om ett program ska räkna hur många poäng du har i ett spel, sparar det siffran i en variabel som kanske heter `score` eller `points`.

#### 5. Dekompilering – från kaka tillbaka till (ungefärligt) recept

Ghidras superkraft är **dekompilering**. Det innebär att ta en binär fil (kakan) och försöka skapa källkod (receptet) igen. Men OBS: det blir aldrig exakt samma recept som originalet, bara en gissning som *kan* producera samma kaka.

**Varför är detta svårt?**
Många olika recept kan ge samma kaka! Om du bara smakar på pannkakan kan du gissa att det är ägg och mjöl, men du vet inte om det var 1 eller 2 ägg, eller om det var vetemjöl eller grahamsmjöl.

#### 6. Ghidras gränssnitt – din verktygslåda

När du öppnar Ghidra ser du flera delar på skärmen (fönster):

- **Project Window**: Här ser du alla projekt (samlingar av filer) du arbetar med
- **CodeBrowser**: Huvudfönstret där du analyserar program
  - **Listing**: Visar assembler-koden (maskinnära instruktioner)
  - **Decompiler**: Visar dekompilerad kod (försök att återskapa källkoden)
  - **Symbol Tree**: Lista över alla funktioner och data i programmet
  - **Data Type Manager**: Visar olika datatyper (som "heltal", "text", "lista")
  - **Function Graph**: Ritar diagram över hur funktioner hänger ihop

#### 7. Analys – Ghidras detektivarbete

När du öppnar en binär fil i Ghidra frågar den: "Vill du analysera filen?" Om du säger ja, sätter Ghidra igång sitt **detektivarbete**:
- Hittar alla funktioner
- Försöker förstå vad de gör
- Hittar strängar (texter) i programmet
- Skapar dekompilerad kod

Detta tar några sekunder till minuter beroende på filens storlek.

### Exempel

#### Exempel 1: Från källkod till binär och tillbaka

**Steg 1 – Källkod (receptet)**:
```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 3);
    printf("Result: %d\n", result);
    return 0;
}
```

**Steg 2 – Kompilering (bakning)**:
En programmerare använder en kompilator för att göra om källkoden till en binär fil (`program.exe`). Nu kan datorn köra programmet.

**Steg 3 – Dekompilering med Ghidra (gissa receptet)**:
När du öppnar `program.exe` i Ghidra, ser du kanske något som:
```c
int FUN_00401000(int param_1, int param_2) {
    return param_1 + param_2;
}

void entry() {
    int iVar1;
    iVar1 = FUN_00401000(5, 3);
    printf("Result: %d\n", iVar1);
    return;
}
```

Lägg märke till att Ghidra inte visste att funktionen hette `add`, så den kallade den `FUN_00401000`. Men den förstod vad funktionen *gör* – den adderar två tal!

#### Exempel 2: Hitta en hemlig sträng

Föreställ dig att du har fått ett program, men du vet inte vad det gör. Du öppnar det i Ghidra och:

1. Går till **Symbol Tree** → **Defined Strings**
2. Ser en lista över alla texter i programmet:
   - "Welcome to the secret program!"
   - "Password: dragon123"
   - "Access granted"

Aha! Programmet har en inbyggd lösenordskontroll, och lösenordet är `dragon123`!

**Före analys**: Du vet inte ens att det finns ett lösenord.
**Efter analys**: Du vet exakt vilket lösenord som krävs.

#### Exempel 3: Förstå en funktion med Function Graph

Du hittar en funktion i Ghidra och vill förstå vad den gör. Du klickar på knappen **Function Graph** och ser ett diagram:

```
         [Start: check_password]
                 |
         [Läs input från användare]
                 |
         [Jämför med "dragon123"]
               /   \
             Ja     Nej
            /         \
    [Skriv ut      [Skriv ut
     "Access        "Access
     granted"]      denied"]
         |              |
         └──────┬───────┘
                |
              [Slut]
```

Nu ser du tydligt: funktionen läser användarens input, jämför med "dragon123", och skriver antingen "Access granted" eller "Access denied".

### 💡 Pro Tips

#### Tips 1: Lär dig genvägar (Keyboard Shortcuts)
Ghidra har många snabba knappar som gör arbetet lättare:
- **G**: "Go to" – hoppa till en specifik adress eller funktion
- **L**: Sätt en etikett (label) på en plats
- **;**: Skriv en kommentar
- **Enter**: Följ en referens (om du ser ett funktionsanrop, tryck Enter för att hoppa till den funktionen)

Du behöver inte lära dig alla på en gång – börja med **G** och **;** (kommentarer är ovärderliga!).

#### Tips 2: Namnge saker du förstår
När Ghidra inte vet vad något heter (som `FUN_00401000` eller `DAT_004020A0`), och du räknar ut det, **döp om det direkt**! Högerklicka → Rename.

Om du väntar med namngivning tills senare, kommer du att glömma vad allt betyder. Döp om medan du fortfarande minns!

#### Tips 3: Använd både Listing och Decompiler
Ibland är **assembler-koden** (Listing) lättare att förstå, ibland är **dekompilerad kod** (Decompiler) bättre. Titta på båda! De visar samma sak men på olika sätt. Det är som att ha både en karta och en kompass – båda hjälper dig att navigera.

### ✏️ Övningar

#### Övning 1: Matcha termer med förklaringar ⭐

**Instruktioner**: Para ihop termen med rätt förklaring.

| Term | Förklaring |
|------|------------|
| A. Källkod | 1. Ett litet avsnitt av kod som gör en specifik uppgift |
| B. Binär | 2. Kod som människor skriver (som ett recept) |
| C. Funktion | 3. Ghidras försök att återskapa källkod från binär |
| D. Assembler | 4. Färdig fil som datorn kan köra (som en färdig kaka) |
| E. Dekompilering | 5. Maskinnära kod som är lite mer läsbar än rå maskinkod |

**Lösning**:
- A → 2
- B → 4
- C → 1
- D → 5
- E → 3

**Förklaring**:
Att kunna matcha dessa termer visar att du förstår grunderna. Om något var svårt, läs igenom avsnittet igen – det är viktigt att du har koll på dessa begrepp!

#### Övning 2: Identifiera "funktioner" i vardagen ⭐

**Instruktioner**:
Tänk på processen "Gör frukost". Dela upp den i 3-5 små "funktioner" (delar som var och en gör en sak).

**Exempel på lösning**:
1. **Funktion: get_bread()** – Hämta bröd från skåpet
2. **Funktion: toast_bread()** – Rosta brödet i brödrost
3. **Funktion: spread_butter()** – Bred smör på brödet
4. **Funktion: add_topping()** – Lägg på ost eller marmelad
5. **Funktion: serve_breakfast()** – Lägg på tallrik och servera

**Förklaring**:
I riktiga program är kod uppdelad på samma sätt. Istället för att ha en jättelång lista med steg, har du små funktioner som gör en sak vardera. Detta gör koden lättare att förstå och återanvända.

**Bonus**: Vilken funktion skulle anropa vilken?
- `serve_breakfast()` skulle anropa alla andra funktioner i ordning!

#### Övning 3: Ghidra UI Bingo ⭐⭐

**Instruktioner**:
Nedan är en lista över element i Ghidras gränssnitt. Skriv en kort mening om vad var och en gör.

1. **Listing-fönstret**
2. **Decompiler-fönstret**
3. **Symbol Tree**
4. **Function Graph**

**Lösning**:
1. **Listing-fönstret**: Visar assembler-kod (maskinnära instruktioner) för programmet
2. **Decompiler-fönstret**: Visar dekompilerad kod (försök att återskapa källkod som är lättare att läsa)
3. **Symbol Tree**: En lista över alla funktioner, data och symboler i programmet
4. **Function Graph**: Ritar ett diagram över hur en funktion fattar beslut och hoppar mellan olika delar

**Förklaring**:
När du öppnar Ghidra första gången kan det se förvirrande ut med alla fönster. Men varje fönster har ett specifikt syfte. Med tiden kommer du att lära dig exakt vilket fönster du behöver titta i för att hitta information snabbt.

#### Övning 4: Gissa vad funktioner gör ⭐⭐

**Instruktioner**:
Nedan är namn på funktioner från ett okänt program. Gissa vad varje funktion troligen gör baserat bara på namnet.

1. `print_welcome_message`
2. `validate_user_input`
3. `calculate_total`
4. `save_to_file`

**Lösning**:
1. **print_welcome_message**: Skriver ut ett välkomstmeddelande till användaren (t.ex. "Welcome to the program!")
2. **validate_user_input**: Kontrollerar att användarens input är giltig (t.ex. inte tom, rätt format)
3. **calculate_total**: Räknar ut en summa (t.ex. totalpris, totala poäng)
4. **save_to_file**: Sparar data till en fil på datorn

**Förklaring**:
Bra funktionsnamn är som skyltar – de berättar vad som finns inuti! När du analyserar program i Ghidra och räknar ut vad en funktion gör, ge den ett bra namn. Framtida du (eller någon annan) kommer att vara tacksam!

**Bonus**: Vad händer om alla funktioner hette `FUN_00401000`, `FUN_00401050`, etc.?
- Det blir jättesvårt att komma ihåg vad allt gör! Därför är namngivning så viktigt.

#### Övning 5: Från recept till kaka och tillbaka ⭐⭐⭐

**Instruktioner**:
Föreställ dig att du har denna enkla källkod:

```c
int multiply(int x, int y) {
    return x * y;
}
```

1. Vad skulle en kompilator göra med denna kod? (Beskriv med egna ord)
2. Om Ghidra dekompilerar den färdiga binären, skulle den få tillbaka exakt samma kod? Varför/varför inte?

**Lösning**:

1. **Vad kompilatorn gör**:
   - Läser källkoden (receptet)
   - Översätter den till maskinkod (instruktioner datorn förstår)
   - Skapar en binär fil som innehåller dessa instruktioner
   - Kanske "optimerar" koden (gör den snabbare) genom att ändra vissa saker

2. **Skulle Ghidra få tillbaka exakt samma kod?**
   - **Nej, troligen inte!** Ghidra skulle se assembler-instruktioner som:
     ```
     MOV eax, [första parametern]
     IMUL eax, [andra parametern]
     RET
     ```
   - Och gissa att det är en multiplikation, så dekompilerad kod skulle bli något som:
     ```c
     int FUN_00401000(int param_1, int param_2) {
         return param_1 * param_2;
     }
     ```
   - Samma logik, men funktionsnamnet `multiply`, variabelnamnen `x` och `y` är borta!

**Förklaring**:
När kod kompileras, "glöms" mycket information bort – som funktionsnamn och variabelnamn. Det är som att ta en kaka och försöka gissa receptet: du kan se ingredienserna, men du vet inte vad bagaren kallade dem ("smör" vs "mjölkfett"?). Ghidra gör sitt bästa, men det blir aldrig 100% samma som originalet.

### 📝 Sammanfattning

#### Key Takeaways
- **Källkod** är som ett recept (människor kan läsa det), **binär** är som en färdig kaka (datorn kan köra den)
- **Assembler** är maskinnära kod som är lite mer läsbar än rå maskinkod
- **Funktioner** är små byggstenar som gör specifika uppgifter
- **Dekompilering** är Ghidras försök att återskapa källkod från en binär – det blir en gissning, inte originalet
- Ghidras **gränssnitt** har flera fönster: Listing (assembler), Decompiler (C-liknande kod), Symbol Tree (lista över funktioner), Function Graph (diagram)
- **Analys** är när Ghidra automatiskt hittar funktioner, strängar och strukturer i en binär
- **Namnge** funktioner och variabler när du förstår dem – framtida du kommer att tacka dig!

#### Ordlista (Nivå 2)
- **Källkod**: Kod skriven av programmerare i språk som C, Python, Java (läsbar för människor)
- **Binär/Körbar fil**: Färdig fil (t.ex. `.exe`) som datorn kan köra direkt
- **Maskinkod**: Rå instruktioner i form av siffror som datorn förstår
- **Assembler**: Maskinnära kod som är lite mer läsbar än maskinkod
- **Funktion**: En namngiven del av kod som gör en specifik uppgift
- **Variabel**: En "låda" som håller data (siffror, text, etc.)
- **Minne**: Var datorn sparar data medan ett program körs
- **Dekompilering**: Processen att försöka återskapa källkod från en binär fil
- **Listing**: Fönster i Ghidra som visar assembler-kod
- **Decompiler**: Fönster i Ghidra som visar dekompilerad (C-liknande) kod
- **Symbol Tree**: Lista över funktioner, data och symboler i programmet
- **Function Graph**: Visuellt diagram över hur en funktion fattar beslut
- **Analys**: Ghidras automatiska process för att förstå en binär fil

#### Nästa steg
Nu när du kan grundspråket är du redo att faktiskt **använda** Ghidra! I nästa nivå kommer du att installera Ghidra, öppna din första binär fil, och göra en riktig analys. Du kommer att se Listing, Decompiler och Function Graph i praktiken. Det är dags att gå från teori till praktik!

---

## Nivå 3: Din första riktiga analys i Ghidra 🎓

### Introduktion

Välkommen till praktiken! I denna nivå går vi från teori till verklig användning av Ghidra. Du kommer att lära dig hur man installerar Ghidra på olika plattformar, skapar ditt första projekt, importerar en binär fil, kör analys och navigerar i koden. Du kommer också att förstå grunderna om hur datorer fungerar på låg nivå – vad register och stack är, hur funktioner anropar varandra, och hur du läser både assembler-kod och dekompilerad kod. Detta steg är kritiskt eftersom det ger dig den praktiska erfarenheten du behöver för att bli bekväm med verktyget innan vi går djupare i avancerade tekniker.

### Kärnkoncept

#### 1. Installation av Ghidra (2024-2025)

**Systemkrav**:
- **Java Development Kit (JDK) 21**: Ghidra 11.3 (senaste versionen i februari 2025) kräver JDK 21
- **Operativsystem**: Windows, Linux eller macOS
- **Minne**: Minst 4 GB RAM (8+ GB rekommenderas för större program)
- **Diskutrymme**: ~500 MB för Ghidra + utrymme för projekt

**Steg-för-steg installation**:

**Alla plattformar**:
1. Ladda ner JDK 21 från Oracle eller OpenJDK
2. Installera JDK och kontrollera att `java -version` visar version 21+
3. Ladda ner Ghidra från officiella GitHub releases (NationalSecurityAgency/ghidra)
4. Extrahera ZIP/tar.gz-filen till önskad plats (t.ex. `C:\Tools\ghidra` eller `/opt/ghidra`)

**Windows**:
- Kör `ghidraRun.bat` från `ghidra_11.3\` mappen
- För Python 3-support: kör `pyghidraRun.bat`

**Linux/macOS**:
- Gör scriptet körbart: `chmod +x ghidraRun`
- Kör: `./ghidraRun`
- För Python 3-support: `./pyghidraRun`

**OBS**: Ghidra använder ingen traditionell installer – för att avinstallera, ta bara bort mappen!

#### 2. Grundläggande CPU-arkitektur: x86/x64

För att förstå vad Ghidra visar dig behöver du grundläggande kunskap om hur en CPU fungerar.

**Register** – snabba "lådor" inuti CPU:n:
- **EAX, EBX, ECX, EDX** (x86 32-bit): Generella register för beräkningar och tillfällig data
- **RAX, RBX, RCX, RDX** (x64 64-bit): 64-bitarsversioner av ovan
- **EIP/RIP** (Instruction Pointer): Pekar på nästa instruktion som ska köras
- **ESP/RSP** (Stack Pointer): Pekar på toppen av stacken
- **EBP/RBP** (Base Pointer): Referenspunkt för lokala variabler i en funktion

**Stack** – LIFO (Last In, First Out) datastruktur:
- Används för att lagra:
  - Returadresser (var programmet ska fortsätta efter ett funktionsanrop)
  - Lokala variabler
  - Parametrar till funktioner (i vissa calling conventions)
- Växer "nedåt" i minnet (lägre adresser)
- `PUSH` lägger data på stacken, `POP` tar bort data

**Calling Conventions** – regler för hur funktioner anropas:
- **x86 (32-bit)**: Parametrar läggs ofta på stacken
- **x64 (64-bit) Windows**: Första 4 parametrarna i RCX, RDX, R8, R9; resten på stacken
- **x64 (64-bit) Linux**: Första 6 parametrarna i RDI, RSI, RDX, RCX, R8, R9; resten på stacken

#### 3. Skapa och hantera projekt i Ghidra

**Projekt** i Ghidra är som en mapp som innehåller alla dina analyser:
- Sparar program (binärer du analyserar)
- Sparar din markup (kommentarer, omdöpningar, strukturer)
- Kan delas mellan flera användare (för team-samarbete)

**Två typer av projekt**:
1. **Non-Shared Project**: Lokalt projekt, bara du kan se det
2. **Shared Project**: Kan delas i ett team via en server

För nybörjare: börja med **Non-Shared Project**.

#### 4. Analysprocessen i Ghidra

När du importerar en binär fil sker följande:

1. **Import**: Ghidra läser filen och identifierar format (PE, ELF, Mach-O, etc.)
2. **Analysis** (om du väljer "Yes" vid prompt):
   - **Disassembly**: Konverterar maskinkod till assembler
   - **Function Discovery**: Hittar funktionsgränser
   - **String Discovery**: Hittar textsträngar
   - **Call Graph**: Kartlägger vilka funktioner som anropar vilka
   - **Decompilation**: Skapar C-liknande kod från assembler

Du kan alltid köra om analysen senare via **Analysis → Auto Analyze**.

#### 5. Navigering i CodeBrowser

**Listing-fönstret** (vänster/center):
- Visar assembler-kod rad för rad
- Varje rad har: adress, bytes (maskinkod), instruktion, eventuell kommentar
- Exempel:
  ```
  00401000  55              PUSH    EBP
  00401001  89 e5           MOV     EBP, ESP
  00401003  b8 05 00 00 00  MOV     EAX, 0x5
  ```

**Decompiler-fönstret** (höger):
- Visar pseudo-C-kod
- Lättare att läsa än assembler
- Inte perfekt, men oftast bra nog för att förstå logiken

**Symbol Tree** (vänster panel):
- **Functions**: Lista över alla funktioner
- **Data**: Globala variabler
- **Defined Strings**: Alla textsträngar i programmet
- **Imports/Exports**: Funktioner som importeras från DLL:er eller exporteras

**Function Graph**:
- Visuell representation av en funktions kontrollflöde
- Rutor = kodblock (basic blocks)
- Pilar = hopp/grenar (if/else, loopar)

#### 6. Kontrollflöde – if/else och loopar

Program är inte bara linjära. De fattar beslut!

**If/Else i assembler**:
```
CMP  eax, 0        ; Jämför eax med 0
JE   label_else    ; Om lika (Jump if Equal), hoppa till else
; if-blocket
...
JMP  label_end     ; Hoppa över else
label_else:
; else-blocket
...
label_end:
```

**Loop i assembler**:
```
MOV  ecx, 10       ; Räknare = 10
label_loop:
...                ; Loop-kropp
DEC  ecx           ; Minska räknare
JNZ  label_loop    ; Om inte noll, hoppa tillbaka
```

I **Function Graph** ser du detta som pilar som går tillbaka eller förgrenar sig.

#### 7. Kommentarer och Namngivning

En av de viktigaste sakerna du kan göra:
- **; (semikolon)**: Lägg till kommentar på aktuell rad
- **Högerklick → Rename**: Döp om funktion eller variabel
- **Ctrl+L**: Sätt etikett (label) på en adress

**Före namngivning**:
```c
int FUN_00401000(int param_1, int param_2) {
    return param_1 + param_2;
}
```

**Efter namngivning**:
```c
int add_numbers(int first, int second) {
    return first + second;
}
```

Mycket mer läsbart!

### Exempel

#### Exempel 1: Installera Ghidra och starta första gången (Steg-för-steg)

**Steg 1**: Ladda ner och installera JDK 21
- Gå till Oracle eller Adoptium (OpenJDK)
- Ladda ner JDK 21 för ditt OS
- Installera och verifiera: öppna terminal/kommandotolk, skriv `java -version`
- Du bör se: `java version "21.x.x"`

**Steg 2**: Ladda ner Ghidra
- Gå till GitHub: NationalSecurityAgency/ghidra/releases
- Ladda ner `ghidra_11.3_PUBLIC.zip` (eller senaste versionen)

**Steg 3**: Extrahera
- Windows: Högerklicka → "Extract All" → välj `C:\Tools\`
- Linux: `unzip ghidra_11.3_PUBLIC.zip -d /opt/`
- macOS: Dubbelklicka ZIP-filen, flytta mappen till Applications

**Steg 4**: Kör Ghidra
- Windows: Dubbelklicka `ghidraRun.bat` i `ghidra_11.3\` mappen
- Linux/macOS: I terminal, `cd /opt/ghidra_11.3/` och `./ghidraRun`

**Steg 5**: Första start
- Ghidra öppnar "Project Window"
- Du ser: "No Project Open"
- **Grattis!** Ghidra är installerat!

#### Exempel 2: Skapa projekt och importera "Hello World"

**Steg 1**: Skapa projekt
- I Ghidra Project Window, klicka **File → New Project**
- Välj **Non-Shared Project** → Next
- Välj projektmapp (t.ex. `C:\GhidraProjects\`)
- Namnge projektet: `MyFirstProject` → Finish

**Steg 2**: Förbered en enkel binär (eller använd en befintlig)
Om du inte har en binär fil, skapa en enkel:

```c
// hello.c
#include <stdio.h>

int main() {
    printf("Hello, Ghidra!\n");
    return 0;
}
```

Kompilera:
- **Windows**: `gcc hello.c -o hello.exe`
- **Linux**: `gcc hello.c -o hello`

**Steg 3**: Importera i Ghidra
- Klicka **File → Import File** (eller dra-och-släpp filen i Project Window)
- Välj `hello.exe` eller `hello`
- Ghidra detekterar format automatiskt (PE eller ELF)
- Klicka **OK**

**Steg 4**: Öppna i CodeBrowser
- Dubbelklicka på `hello` i Project Window
- CodeBrowser öppnas
- Popup frågar: **"Would you like to analyze hello now?"**
- Klicka **Yes**

**Steg 5**: Kör analys
- En dialog med analysinställningar visas
- För nybörjare: lämna allt som default
- Klicka **Analyze**
- Vänta några sekunder (en progress bar visas)

**Steg 6**: Utforska resultatet!
- I Symbol Tree (vänster), expandera **Functions**
- Hitta `main` (kanske heter den `entry` eller `FUN_00401000`)
- Dubbelklicka på `main`
- Listing visar assembler
- Decompiler visar pseudo-C-kod

#### Exempel 3: Förstå en enkel funktion i Listing vs Decompiler

Låt oss titta på en `add`-funktion.

**Källkod**:
```c
int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 3);
    return 0;
}
```

**Listing (Assembler)**:
```
---- add ----
00401000  55              PUSH    EBP
00401001  89 e5           MOV     EBP, ESP
00401003  8b 45 08        MOV     EAX, dword ptr [EBP + 0x8]   ; a
00401006  03 45 0c        ADD     EAX, dword ptr [EBP + 0xc]   ; b
00401009  5d              POP     EBP
0040100a  c3              RET
```

**Decompiler (Pseudo-C)**:
```c
int add(int param_1, int param_2) {
    return param_1 + param_2;
}
```

**Vad händer?**
- `PUSH EBP` / `MOV EBP, ESP`: Setup stack frame
- `MOV EAX, [EBP+8]`: Hämta första parametern (`a`) till EAX
- `ADD EAX, [EBP+12]`: Addera andra parametern (`b`) till EAX
- `RET`: Returnera (resultatet är i EAX)

Dekompilerad kod visar samma logik men på högre nivå!

#### Exempel 4: Hitta strängar och spåra var de används

**Uppgift**: Hitta var "Hello, Ghidra!" skrivs ut i programmet.

**Steg 1**: Hitta strängen
- Gå till Symbol Tree → **Defined Strings**
- Leta efter `"Hello, Ghidra!"`
- Dubbelklicka den → du ser var i minnet den lagras

**Steg 2**: Hitta referenser
- Högerklicka på strängen → **References → Show References to**
- Du ser en lista över alla ställen i koden som refererar till denna sträng
- Vanligtvis är det ett anrop till `printf` eller liknande

**Steg 3**: Följ till funktionen
- Dubbelklicka på referensen
- Du hamnar i en funktion (troligen `main`)
- I Decompiler ser du kanske:
  ```c
  printf("Hello, Ghidra!\n");
  ```

**Före analys**: Du vet inte var strängen används.
**Efter analys**: Du vet exakt vilken funktion som skriver ut den!

#### Exempel 5: Använd Function Graph för att förstå if/else

**Kod**:
```c
int check_value(int x) {
    if (x > 10) {
        return 1;
    } else {
        return 0;
    }
}
```

**Steg 1**: Hitta funktionen i Symbol Tree
- Functions → `check_value` (eller `FUN_...`)

**Steg 2**: Visa Function Graph
- Klicka på funktionen
- I toolbar, klicka **Window → Function Graph** (eller tryck **Ctrl+Shift+G** beroende på shortcuts)

**Steg 3**: Tolka grafen
Du ser något som:

```
┌─────────────────┐
│  Entry          │
│  CMP eax, 0xa   │ (jämför x med 10)
│  JLE 0x401010   │
└────┬────────────┘
     │
     ├─────────┐
     │         │
     ▼         ▼
┌─────────┐ ┌─────────┐
│ x > 10  │ │ x <= 10 │
│ MOV eax,│ │ MOV eax,│
│     1   │ │     0   │
│ RET     │ │ RET     │
└─────────┘ └─────────┘
```

**Tolkning**:
- **Entry-block**: Jämför `x` med 10
- **Vänster gren**: Om `x > 10`, sätt EAX=1 och returnera
- **Höger gren**: Om `x <= 10`, sätt EAX=0 och returnera

Function Graph gör if/else-logik **visuell**!

#### Exempel 6: Döp om funktioner för bättre läsbarhet

**Problem**: Ghidra har hittat funktioner men döpt dem `FUN_00401000`, `FUN_00401020`, etc.

**Lösning**: Döp om baserat på vad de gör!

**Steg 1**: Analysera funktionen
- Klicka på `FUN_00401000`
- I Decompiler ser du:
  ```c
  int FUN_00401000(int param_1, int param_2) {
      return param_1 + param_2;
  }
  ```
- Uppenbart: detta är en addition-funktion!

**Steg 2**: Döp om funktionen
- Högerklicka på funktionsnamnet → **Rename Function**
- Ange nytt namn: `add_numbers`
- Klicka OK

**Steg 3**: Döp om parametrar
- Högerklicka på `param_1` → **Rename Variable**
- Döp till `first_number`
- Upprepa för `param_2` → `second_number`

**Resultat**:
```c
int add_numbers(int first_number, int second_number) {
    return first_number + second_number;
}
```

**Mycket** mer läsbart!

### Visualisering: Ghidra Workflow

```
┌─────────────────────────────────────────────────────────┐
│                  GHIDRA WORKFLOW                        │
└─────────────────────────────────────────────────────────┘

1. SKAPA PROJEKT
   ┌──────────────┐
   │ File → New   │
   │   Project    │
   └──────┬───────┘
          │
          ▼
2. IMPORTERA BINÄR
   ┌──────────────┐
   │ File →       │
   │ Import File  │
   └──────┬───────┘
          │
          ▼
3. ANALYSERA
   ┌──────────────┐
   │ Analyze? Yes │
   │ → Analyze    │
   └──────┬───────┘
          │
          ▼
4. UTFORSKA
   ┌──────────────────────────────────┐
   │ - Listing (assembler)            │
   │ - Decompiler (pseudo-C)          │
   │ - Symbol Tree (funktioner, data) │
   │ - Function Graph (visuellt)      │
   └──────┬───────────────────────────┘
          │
          ▼
5. MARKUP
   ┌──────────────────────────────────┐
   │ - Döp om funktioner/variabler    │
   │ - Lägg till kommentarer          │
   │ - Skapa strukturer               │
   └──────┬───────────────────────────┘
          │
          ▼
6. DOKUMENTERA
   ┌──────────────┐
   │ Spara projekt│
   │ Exportera    │
   │ rapport      │
   └──────────────┘
```

### Jämförelsetabell: Listing vs Decompiler

| Aspekt | Listing (Assembler) | Decompiler (Pseudo-C) |
|--------|---------------------|----------------------|
| **Läsbarhet** | Låg (kräver förståelse för assembler) | Hög (liknar C-kod) |
| **Exakthet** | 100% (direkt översättning från maskinkod) | ~90% (gissning, kan ha fel) |
| **Detaljer** | Alla instruktioner synliga | Abstraherar bort vissa detaljer |
| **Bäst för** | Förstå exakt vad som händer, optimeringar, lågnivålogik | Förstå övergripande logik snabbt |
| **Exempel** | `MOV eax, 5` | `result = 5;` |

**Best practice**: Använd **båda**! Börja med Decompiler för att förstå big picture, använd Listing när du behöver exakta detaljer.

### 💡 Pro Tips

#### Tips 1: Använd "Go To" (G) för snabb navigering
Tryck **G** var som helst i CodeBrowser och skriv:
- En adress: `0x401000` → hoppa till den adressen
- En funktionsnamn: `main` → hoppa till main-funktionen
- En symbol: `_start` → hoppa till symbolen

Detta sparar enormt mycket tid jämfört med att scrolla eller klicka!

#### Tips 2: Kommentera medan du lär dig
Varje gång du förstår vad en rad kod gör, tryck **;** (semikolon) och skriv en kommentar. Exempel:
```
00401003  b8 05 00 00 00  MOV  EAX, 0x5   ; Set counter to 5
```

När du kommer tillbaka senare (eller om någon annan tittar), blir det mycket lättare att förstå!

#### Tips 3: Spara ofta!
Ghidra auto-sparar en del, men det är bra vana att manuellt spara:
- **File → Save** (eller **Ctrl+S** i vissa vyer)

Om Ghidra kraschar (sällan, men händer), förlorar du inte allt arbete!

#### Tips 4: Använd Search → For Strings för att hitta intressanta ledtrådar
Om du inte vet var du ska börja:
- **Search → For Strings**
- Titta på strängar som:
  - Felmeddelanden: "Error: Invalid password"
  - Debug-meddelanden: "DEBUG: Entering function X"
  - Användarbara ledtrådar: "Admin mode enabled"

Strängar ger ofta **enorm** insikt i vad ett program gör!

### ✏️ Övningar

#### Övning 1: Installera Ghidra och verifiera installation ⭐

**Instruktioner**:
1. Följ installationsstegen ovan för ditt operativsystem
2. Starta Ghidra
3. Skapa ett nytt Non-Shared Project med namnet `TestProject`
4. Ta en skärmdump av Project Window som visar ditt projekt

**Förväntat resultat**:
- Ghidra startar utan fel
- Du ser Project Window med `TestProject` listat

**Felsökning**:
- **"Java not found"**: Kontrollera att JDK 21 är installerat och i PATH
- **"Unsupported Java version"**: Uppgradera till JDK 21

#### Övning 2: Kompilera och analysera "Hello World" ⭐⭐

**Instruktioner**:
1. Skapa en fil `hello.c`:
   ```c
   #include <stdio.h>
   int main() {
       printf("Hello, World!\n");
       return 0;
   }
   ```
2. Kompilera: `gcc hello.c -o hello` (Linux/macOS) eller `gcc hello.c -o hello.exe` (Windows)
3. Importera `hello` till Ghidra-projektet
4. Analysera filen
5. Hitta `main`-funktionen i Symbol Tree
6. Granska Listing och Decompiler

**Frågor att svara på**:
- Vad heter `main`-funktionen i Ghidra? (Tips: ibland `main`, ibland `entry`, ibland `FUN_...`)
- Hur många funktioner hittade Ghidra totalt?
- Kan du hitta strängen "Hello, World!" i Defined Strings?

**Lösningsförslag**:
- `main` bör vara synlig i Functions eller ha ett liknande namn
- Totala funktioner varierar (inkluderar biblioteksfunktioner från libc)
- "Hello, World!" finns i Defined Strings och används i `main` via `printf`

#### Övning 3: Hitta och spåra en sträng ⭐⭐

**Instruktioner**:
1. Använd samma `hello`-binär från övning 2
2. Gå till Symbol Tree → Defined Strings
3. Hitta "Hello, World!"
4. Högerklicka → "Show References to..."
5. Vilken funktion använder strängen?
6. Gå till den funktionen och läs Decompiler-koden

**Förväntat resultat**:
- Du hittar en referens från `main` (eller liknande)
- I Decompiler ser du ett anrop till `printf` eller `puts` med strängen

**Bonus**:
- Vad händer om du ändrar strängen i Ghidra? (OBS: detta ändrar bara analysen, inte binären själv!)

#### Övning 4: Döp om funktioner och variabler ⭐⭐

**Instruktioner**:
1. Skapa en lite mer komplex fil:
   ```c
   #include <stdio.h>
   int add(int a, int b) { return a + b; }
   int multiply(int a, int b) { return a * b; }
   int main() {
       int x = add(5, 3);
       int y = multiply(x, 2);
       printf("Result: %d\n", y);
       return 0;
   }
   ```
2. Kompilera och importera till Ghidra
3. Analysera
4. Om funktionerna heter `FUN_...`, döp om dem till `add`, `multiply`, och `main`
5. Döp om parametrar till något beskrivande

**Förväntat resultat**:
Före:
```c
int FUN_00401000(int param_1, int param_2) { return param_1 + param_2; }
```

Efter:
```c
int add(int first, int second) { return first + second; }
```

**Reflektion**:
- Hur mycket lättare blev koden att förstå efter namngivning?

#### Övning 5: Förstå kontrollflöde med Function Graph ⭐⭐⭐

**Instruktioner**:
1. Skapa fil `compare.c`:
   ```c
   #include <stdio.h>
   int check_age(int age) {
       if (age >= 18) {
           return 1; // Adult
       } else {
           return 0; // Child
       }
   }
   int main() {
       int result = check_age(20);
       printf("Result: %d\n", result);
       return 0;
   }
   ```
2. Kompilera och analysera i Ghidra
3. Hitta `check_age`-funktionen
4. Öppna Function Graph
5. Rita (på papper eller digitalt) flödesdiagrammet du ser

**Frågor**:
- Hur många block (rutor) ser du i grafen?
- Vilket block innehåller jämförelsen (CMP)?
- Vilka två block representerar if/else-grenarna?

**Förväntat svar**:
- 3 block: Entry (jämför age med 18), True-block (return 1), False-block (return 0)
- Entry-block innehåller `CMP` och `JGE/JL` (eller liknande)
- True/False-block har `MOV eax, 1` respektive `MOV eax, 0`

**Bonus**:
- Ändra koden till en loop och se hur grafen förändras!

#### Övning 6: Jämför Listing och Decompiler ⭐⭐⭐

**Instruktioner**:
1. Använd `check_age`-funktionen från övning 5
2. Titta på Listing (assembler)
3. Titta på Decompiler (pseudo-C)
4. Fyll i tabellen:

| Vad sker | Listing (assembler) | Decompiler (pseudo-C) |
|----------|---------------------|-----------------------|
| Jämförelse | ? | ? |
| Om sant | ? | ? |
| Om falskt | ? | ? |

**Lösningsförslag**:

| Vad sker | Listing (assembler) | Decompiler (pseudo-C) |
|----------|---------------------|-----------------------|
| Jämförelse | `CMP eax, 0x12` <br> `JL label_false` | `if (age >= 18)` |
| Om sant | `MOV eax, 1` <br> `RET` | `return 1;` |
| Om falskt | `MOV eax, 0` <br> `RET` | `return 0;` |

**Reflektion**:
- Vilken version var lättare att förstå snabbt?
- Vilken version visade exakt vad CPU:n gör?

#### Övning 7: Mini-projekt: Dokumentera ett okänt program ⭐⭐⭐⭐

**Instruktioner**:
1. Ladda ner ett enkelt CLI-verktyg eller använd ett befintligt (t.ex. `whoami`, `hostname`, eller skapa ett eget)
2. Importera och analysera i Ghidra
3. Dokumentera programmet:
   - Hur många funktioner finns?
   - Vilken är entry point?
   - Vilka strängar finns (error messages, output, etc.)?
   - Rita ett enkelt call graph (vilka funktioner anropar vilka)?
4. Skriv en kort rapport (1 sida) om vad programmet gör

**Exempel på rapport-struktur**:
```
Program: my_tool.exe
Entry Point: main (0x401000)
Antal funktioner: 8

Huvudfunktioner:
- main: Anropar parse_arguments och execute
- parse_arguments: Läser kommandoradsargument
- execute: Utför huvudlogiken
- print_help: Skriver ut hjälptext

Intressanta strängar:
- "Usage: my_tool [options]"
- "Error: Invalid argument"

Call Graph:
main → parse_arguments
main → execute
   execute → read_file
   execute → process_data
main → print_help (om --help)
```

**Lärdom**:
Detta är **exakt** vad reverse engineers gör professionellt – de dokumenterar okända program för att förstå deras beteende!

### 📝 Sammanfattning

#### Key Takeaways
- **Installation**: Ghidra kräver JDK 21, extraheras till valfri mapp, ingen traditionell installer
- **CPU-arkitektur**: Grundläggande förståelse för register (EAX, ESP, EIP) och stack är kritisk
- **Projekt**: Samlar alla analyser, skapar med File → New Project
- **Import & Analys**: Importera binär → Analyze (auto-hittar funktioner, strängar, etc.)
- **Navigation**: Använd Listing (assembler), Decompiler (pseudo-C), Symbol Tree, Function Graph
- **Kontrollflöde**: If/else och loopar syns som grenar i assembler och Function Graph
- **Markup**: Döp om funktioner/variabler och kommentera för att göra analysen begriplig
- **Best practice**: Använd både Listing och Decompiler, kommentera medan du lär, spara ofta

#### Ordlista (Nivå 3)
- **JDK (Java Development Kit)**: Programvara som krävs för att köra Ghidra
- **Register**: Snabba lagringsplatser inuti CPU:n (EAX, EBX, ESP, etc.)
- **Stack**: LIFO-datastruktur för att lagra returadresser och lokala variabler
- **Stack Pointer (ESP/RSP)**: Register som pekar på toppen av stacken
- **Instruction Pointer (EIP/RIP)**: Register som pekar på nästa instruktion
- **Calling Convention**: Regler för hur funktioner tar emot parametrar och returnerar värden
- **Entry Point**: Första funktionen som körs när ett program startar (ofta `main` eller `_start`)
- **Import**: Processen att läsa en binär fil in i Ghidra
- **Analysis**: Ghidras automatiska process för att hitta funktioner, strängar, etc.
- **Markup**: Manuella ändringar du gör (kommentarer, omdöpningar) för att göra koden begriplig
- **Basic Block**: Ett sammanhängande stycke kod utan grenar (visas som en ruta i Function Graph)
- **Call Graph**: Diagram som visar vilka funktioner som anropar vilka

#### Nästa steg
Nu kan du installera, konfigurera och använda Ghidra för grundläggande analyser! I nästa nivå går vi **djupare**: avancerad analys av komplexa program, scripting (automatisera uppgifter), hantera obfuscation och packers, best practices för större projekt, och mycket mer. Du är redo att gå från grundläggande användare till avancerad praktiker!

---

## Nivå 4: Avancerade analyser och scripting i Ghidra 🏛️

### Introduktion

Nu är det dags att ta steget från grundläggande användning till avancerad reverse engineering. På denna nivå kommer du att lära dig hur man analyserar komplexa program med pekare, strukturer och objektorienterad kod (C++), automatiserar arbetsflöden genom scripting i Python och Java, hanterar obfuscerade binärer och packers, samt förstår best practices för större projekt. Du kommer också att möta verkliga utmaningar som anti-debugging och konstiga calling conventions. Detta steg är kritiskt för att bli en självständig reverse engineer som kan ta sig an riktiga problem utan att behöva hjälp för varje liten detalj.

### Kärnkoncept

#### 1. Komplexa datastrukturer: Pekare, Strukturer och Array

När program blir mer sofistikerade använder de komplexa datastrukturer. Ghidra kan identifiera många av dessa automatiskt, men ofta behöver du hjälpa till manuellt.

**Pekare**:
- En pekare är en variabel som innehåller en minnesadress (pekare till en annan variabel)
- I assembler ser du ofta `MOV eax, [ebx]` – läs från minnet som EBX pekar på
- I Decompiler: `*ptr` eller `ptr->field`

**Strukturer (structs)**:
- Samling av variabler (fields) grupperade tillsammans
- Exempel från C:
  ```c
  struct Person {
      char name[50];
      int age;
      float salary;
  };
  ```
- I Ghidra: Data Type Manager → Create Structure → definiera fields
- Applicera strukturen på en minnesadress → Ghidra visar fields istället för rå bytes

**Array**:
- Flera element av samma typ i följd
- Exempel: `int numbers[10]` – 10 heltal efter varandra
- I Ghidra: märk ett område som array med rätt typ

**Tips**: Om Decompiler visar något som `undefined4 *param_1`, är det troligen en pekare till något Ghidra inte känner igen. Skapa en struktur och applicera den!

#### 2. Objektorienterad kod: C++ och VTables

C++ lägger till komplexitet med klasser, arv och virtuella funktioner.

**VTable (Virtual Table)**:
- En tabell med pekare till virtuella funktioner
- Varje objekt har en gömd pekare (vptr) till sin klass vtable
- I Decompiler ser du ofta: `(**(code **)(*param_1 + 8))(param_1);` – anrop via vtable!

**Hantering i Ghidra**:
1. Identifiera vtable i minnet (array av funktionspekare)
2. Skapa en struktur för klassen med vptr som första field
3. Använd OOAnalyzer-plugin (från SEI/CMU) för automatisk C++-analys

**Utmaning**: Ghidra har inte inbyggt stöd för C++-klasser (ännu), så manuell markup krävs.

#### 3. Ghidra Scripting: Automatisera analys

Ghidra har ett kraftfullt scripting API för både **Python** och **Java**.

**Varför scripta?**
- Automatisera repetitiva uppgifter (t.ex. döp om alla funktioner som matchar ett mönster)
- Batch-analys av många filer
- Extrahera data programmatiskt (alla strängar, alla imports, etc.)
- Implementera custom analysatorer

**Python (Jython 2.7 eller Python 3 med PyGhidra/Ghidrathon)**:

Ghidra 11.3 (2025) har integrerat **PyGhidra** för native Python 3-support!

**Enkelt script-exempel (Python)**:
```python
# Lista alla funktioner
from ghidra.program.model.listing import *

fm = currentProgram.getFunctionManager()
for func in fm.getFunctions(True):  # True = iterate forward
    print("Function: {} at {}".format(func.getName(), func.getEntryPoint()))
```

**Java-exempel**:
```java
// Lista alla strängar
import ghidra.program.model.data.*;

Listing listing = currentProgram.getListing();
DataIterator dataIt = listing.getDefinedData(true);
while (dataIt.hasNext()) {
    Data data = dataIt.next();
    if (data.getDataType().getName().equals("string")) {
        println(data.getAddress() + ": " + data.getValue());
    }
}
```

**Kör script**:
- **Window → Script Manager**
- Skapa nytt script eller importera befintligt
- Dubbelklicka för att köra

**Headless Mode** (batch-analys utan GUI):
```bash
analyzeHeadless /path/to/project ProjectName -import file.exe -postScript MyScript.py
```

#### 4. Obfuscation och Packers

Moderna binärer försöker ofta gömma sig från analys.

**Obfuscation-tekniker**:
- **Control Flow Flattening**: Gör kontrollflödet komplext med switchar
- **Opaque Predicates**: Falska if-satser som alltid är sanna/falska
- **String Encryption**: Strängar dekrypteras vid runtime
- **API Hashing**: API-funktioner anropas via hash istället för namn
- **Junk Code**: Meningslös kod för att distrahera

**Packers**:
- **Vad**: Komprimerar/krypterar en binär, lägger till en "unpacker stub"
- **Varför**: Minska filstorlek, gömma innehåll från antivirusprogram
- **Exempel**: UPX, Themida, VMProtect
- **Identifiering**: Hög entropi i code-sektionen, liten mängd imports, uppenbara dekrypteringsloopar

**Hantering i Ghidra**:
1. **Unpacking**: Kör programmet i debugger, dumpa minnet när det är opackat, analysera den dumpen
2. **Static Deobfuscation**: Använd plugins som **Ghidra Deobfuscator** (abstract interpretation)
3. **Scripting**: Skriv custom scripts för att ta bort junk code eller dekryptera strängar

**Pro Tip**: För packade binärer, analysera först unpacker-stubben för att förstå algoritmen, sedan applicera den manuellt eller i debugger.

#### 5. Best Practices för större projekt

När du analyserar stora binärer (100+ funktioner), organisation är nyckeln.

**Projektstruktur**:
- Skapa **mappar** i Symbol Tree för att gruppera funktioner (t.ex. "Crypto", "Network", "UI")
- Använd **namespaces** för att undvika namnkollisioner

**Namngivningskonventioner**:
- Prefixer för typ: `str_WelcomeMessage`, `func_ParseInput`, `data_ConfigStruct`
- Beskrivande namn: `validateUserPassword` istället för `check1`

**Kommentarer**:
- **Plate Comments** (över funktion): Sammanfattning av vad funktionen gör
- **EOL Comments** (End Of Line): Specifika detaljer per rad
- **Pre/Post Comments**: Före eller efter ett block

**Versionshantering**:
- Ghidra-projekt kan versionshanteras med **Git** (men var försiktig med binära filer)
- Exportera markup som XML för backup: **File → Export → Ghidra Project XML**

**Dokumentation**:
- Skriv en **README** för projektet som förklarar:
  - Vad binären gör
  - Vilka huvudfunktioner som identifierats
  - Eventuella oklarheter eller TODOs

#### 6. Anti-patterns: Vad man INTE ska göra

**Anti-pattern 1: För mycket manuell klickning**
- **Problem**: Du döper om hundratals funktioner genom att klicka varje gång
- **Lösning**: Skriv ett script!

**Anti-pattern 2: Ingen dokumentation**
- **Problem**: Du spenderar veckor på analys, men dokumenterar inget. Sex månader senare minns du ingenting.
- **Lösning**: Kommentera medan du analyserar, skriv sammanfattningar

**Anti-pattern 3: Inte spara regelbundet**
- **Problem**: Ghidra kraschar (sällsynt men händer), du förlorar timmar av arbete
- **Lösning**: Ctrl+S ofta, eller aktivera auto-save

**Anti-pattern 4: Ignorera calling conventions**
- **Problem**: Du tolkar parametrar fel eftersom du inte vet om de är i register eller på stacken
- **Lösning**: Lär dig calling conventions för din målarkitektur (x86 vs x64, Windows vs Linux)

#### 7. Avancerade analyspass: Custom Analyzers

Ghidra låter dig skapa egna **analyzers** som körs automatiskt under analysfasen.

**Use case**: Du vet att ett program använder en custom kryptorutin för strängar. Skriv en analyzer som:
1. Hittar alla krypterade strängar
2. Dekrypterar dem
3. Lägger till dem som kommentarer

**Implementation**: Kräver Java, ärv från `AbstractAnalyzer`

**Exempel-struktur**:
```java
public class MyStringDecryptor extends AbstractAnalyzer {
    @Override
    public boolean added(Program program, AddressSetView set, TaskMonitor monitor, MessageLog log) {
        // Din logik här
        return true;
    }
}
```

Registrera i **analyzeHeadless** eller via GUI.

### Exempel

#### Exempel 1: Skapa en struktur och applicera den

**Scenario**: Du har hittat data i minnet som ser ut så här:
```
0x402000: 48 65 6c 6c 6f 00 00 00  |  "Hello\0\0\0"
0x402008: 19 00 00 00              |  25 (int)
0x40200C: 00 00 48 42              |  50.0 (float)
```

Det ser ut som en `Person`-struktur!

**Steg 1**: Skapa struktur
- Data Type Manager → högerklicka → **New → Structure**
- Namn: `Person`
- Lägg till fields:
  - `char name[8]`
  - `int age`
  - `float salary`

**Steg 2**: Applicera strukturen
- Gå till adress `0x402000` i Listing
- Tryck **Ctrl+L** (Edit Data Type)
- Välj `Person`

**Resultat**:
```
0x402000:  Person {
             name: "Hello"
             age: 25
             salary: 50.0
           }
```

Mycket mer begripligt än rå bytes!

#### Exempel 2: Skriv ett Python-script för att lista alla strängar som innehåller "password"

**Kod** (`find_password_strings.py`):
```python
# Find all strings containing "password"
from ghidra.program.model.data import *

listing = currentProgram.getListing()
memory = currentProgram.getMemory()

print("Searching for strings containing 'password'...\n")

for data in listing.getDefinedData(True):
    if data.getDataType().getName().startswith("string"):
        value = str(data.getValue())
        if "password" in value.lower():
            print("Found at {}: {}".format(data.getAddress(), value))
```

**Kör**:
1. Script Manager → New → Python
2. Klistra in kod, spara som `find_password_strings.py`
3. Dubbelklicka för att köra

**Output**:
```
Searching for strings containing 'password'...

Found at 0x403020: Enter password:
Found at 0x403050: Invalid password
Found at 0x403080: default_password123
```

**Nytta**: Istället för att manuellt söka igenom hundratals strängar, får du resultatet på sekunder!

#### Exempel 3: Identifiera en packad binär

**Indikationer på packing**:
1. **Få imports**: Bara `LoadLibrary`, `GetProcAddress`, `VirtualAlloc`
2. **Stora datasektioner**: `.data` eller `.rsrc` är mycket större än `.text`
3. **Hög entropi**: Datan ser ut som slumpmässighet (krypterad/komprimerad)
4. **Tydlig unpacker-loop**: Assembler-kod som itererar över bytes och XOR:ar/dekrypterar

**Analys i Ghidra**:
- Importera binären
- Granska **Program Trees → Program Tree** för att se sektioner
- Om `.text` är liten (några KB) men filen är stor (MB) → troligen packad
- Leta efter en loop i entry point som skriver till minnet → unpacking-rutin

**Lösning**:
- Använd en debugger (x64dbg, WinDbg) för att köra till OEP (Original Entry Point)
- Dumpa minnet med **Scylla** eller **PE-bear**
- Importera den dumpen i Ghidra för riktig analys

#### Exempel 4: Reverse-engineera en enkel VTable (C++)

**Källkod (okänd för dig)**:
```cpp
class Animal {
public:
    virtual void speak() { printf("..."); }
    virtual void move() { printf("moving..."); }
};

class Dog : public Animal {
public:
    void speak() override { printf("Woof!"); }
};

int main() {
    Animal *a = new Dog();
    a->speak();  // Calls Dog::speak via vtable
    return 0;
}
```

**I Ghidra**:
Du ser i Decompiler:
```c
void entry() {
    undefined4 *obj = (undefined4 *)operator_new(4);
    *obj = &PTR_FUN_00402000;  // vptr set to Dog's vtable
    (**(code **)(*obj))(obj);  // Call first function in vtable
}
```

**Tolkning**:
- `PTR_FUN_00402000` är Dog's vtable
- Gå till `0x402000` i Listing → du ser två pekare till funktioner
- Första pekaren → `Dog::speak`
- Andra pekaren → `Animal::move` (Dog ärvde den)

**Förbättra**:
1. Skapa struktur `Dog_vtable` med två function pointers
2. Applicera på `0x402000`
3. Döp om funktionerna till `Dog_speak` och `Animal_move`

Nu är koden mycket mer begriplig!

#### Exempel 5: Headless batch-analys av flera filer

**Scenario**: Du har 50 DLL-filer att analysera och vill extrahera alla exporterade funktioner.

**Script** (`export_functions.py`):
```python
# Export all exported functions to CSV
import csv

fm = currentProgram.getFunctionManager()
exports = []

for func in fm.getFunctions(True):
    if func.isExternal() == False and func.isThunk() == False:
        exports.append([func.getName(), str(func.getEntryPoint())])

with open('/tmp/exports.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Function', 'Address'])
    writer.writerows(exports)

print("Exported {} functions to /tmp/exports.csv".format(len(exports)))
```

**Headless kommando**:
```bash
for dll in *.dll; do
    analyzeHeadless /tmp/ghidra_project MyProject -import "$dll" \
        -postScript export_functions.py -deleteProject
done
```

**Resultat**: Du får en CSV-fil för varje DLL med alla funktioner – allt utan att öppna GUI!

### Jämförelsetabell: Scripting-språk i Ghidra

| Aspekt | Python (Jython 2.7) | Python 3 (PyGhidra) | Java |
|--------|---------------------|---------------------|------|
| **Tillgänglighet** | Inbyggt sedan början | Ghidra 11.3+ (2025) | Inbyggt sedan början |
| **Prestanda** | Långsam (JVM overhead) | Medel | Snabb |
| **Läsbarhet** | Hög (Python syntax) | Hög (Python syntax) | Medel (mer verbose) |
| **Bibliotek** | Begränsade (Python 2 EOL) | Full Python 3 ekosystem | Java ekosystem |
| **Bäst för** | Snabba prototyper | Modern Python kod | Performance-kritiska scripts |
| **Lärkkurva** | Låg | Låg | Medel (kräver Java-kunskap) |

**Rekommendation**: Använd **PyGhidra (Python 3)** för nya scripts, Java om du behöver maximal prestanda.

### 💡 Pro Tips

#### Tips 1: Använd Bookmarks för att markera viktiga platser
Under analysen hittar du kritiska funktioner (kryptorutiner, nätverkskommunikation, etc.). Markera dem!
- Högerklicka i Listing → **Bookmark**
- Kategori: "Crypto", "Network", "Security", etc.
- Se alla bookmarks: **Window → Bookmarks**

#### Tips 2: Differential Analysis – jämför två versioner av ett program
Om du har två versioner av samma program (t.ex. före och efter en patch):
- Importera båda i samma projekt
- Använd **Tools → Version Tracking** för att jämföra skillnader
- Identifiera exakt vad som ändrats (buggfixar, nya features)

#### Tips 3: Integrera med andra verktyg
Ghidra är kraftfull men inte allomfattande. Kombinera med:
- **x64dbg/WinDbg**: För dynamisk analys
- **Frida**: För runtime instrumentation
- **Binwalk**: För firmware-analys
- **IDA Free**: För vissa arkitekturer som Ghidra inte stödjer väl

Exportera data från Ghidra, analysera i annat verktyg, importera tillbaka!

#### Tips 4: Lär dig "Equates" för att ersätta magiska nummer
Om du ser `CMP eax, 0x10` och 0x10 representerar något specifikt (t.ex. "MAX_USERS"):
- Högerklicka på `0x10` → **Set Equate** → "MAX_USERS"
- Nu visas: `CMP eax, MAX_USERS`

Mycket mer läsbart!

### ✏️ Övningar

#### Övning 1: Skapa och applicera en struktur ⭐⭐

**Instruktioner**:
1. Skapa en C-fil med en struktur:
   ```c
   struct Config {
       int version;
       char name[32];
       int enabled;
   };
   struct Config cfg = {1, "MyApp", 1};
   int main() { return cfg.version; }
   ```
2. Kompilera och analysera i Ghidra
3. Hitta `cfg` i minnet (globalt data)
4. Skapa strukturen `Config` i Data Type Manager
5. Applicera den på `cfg`

**Förväntat resultat**:
Istället för rå bytes ser du:
```
Config cfg = {
    version: 1,
    name: "MyApp",
    enabled: 1
}
```

#### Övning 2: Skriv ett script för att räkna funktioner per kategori ⭐⭐

**Instruktioner**:
Skriv ett Python-script som:
1. Räknar totalt antal funktioner
2. Räknar hur många som är `import`-funktioner
3. Räknar hur många som är `thunk`-funktioner
4. Skriver ut resultatet

**Hints**:
- `func.isExternal()` → true om import
- `func.isThunk()` → true om thunk

**Exempel på output**:
```
Total functions: 245
Imports: 89
Thunks: 12
User-defined: 144
```

#### Övning 3: Identifiera obfuscation i en binär ⭐⭐⭐

**Instruktioner**:
1. Ladda ner ett "crackme" (t.ex. från crackmes.one eller liknande utbildningsresurs)
2. Analysera i Ghidra
3. Leta efter:
   - Funktioner med ovanligt många block i Function Graph
   - Konstiga hopp (jmp till eax, call [eax+4], etc.)
   - Strängar som verkar kodade (inte läsbar text)
4. Dokumentera vilka obfuscation-tekniker som används

**Frågor**:
- Är kontrollflödet "flattat" (alla block går till en central switch)?
- Finns det opaque predicates (if-satser som alltid tar samma gren)?
- Är API-anrop dolda bakom dynamiska hopp?

#### Övning 4: Reverse-engineera en enkel C++-klass ⭐⭐⭐

**Instruktioner**:
1. Kompilera denna C++-kod:
   ```cpp
   #include <iostream>
   class Calculator {
   public:
       virtual int add(int a, int b) { return a + b; }
       virtual int multiply(int a, int b) { return a * b; }
   };
   int main() {
       Calculator calc;
       std::cout << calc.add(5, 3) << std::endl;
       return 0;
   }
   ```
2. Analysera i Ghidra
3. Hitta vtable för `Calculator`
4. Identifiera `add` och `multiply` i vtable
5. Skapa en struktur för `Calculator` med vptr

**Förväntat**:
Du hittar en tabell med två pekare → första pekar på `add`, andra på `multiply`.

#### Övning 5: Headless batch-analys ⭐⭐⭐

**Instruktioner**:
1. Skapa 3-5 enkla C-program (olika funktionalitet)
2. Kompilera alla
3. Skriv ett Python-script som listar alla funktioner i en fil
4. Kör headless-analys på alla filer med scriptet
5. Samla resultaten i en rapport

**Kommando-exempel**:
```bash
analyzeHeadless /tmp/batch_project BatchProject \
    -import program1.exe \
    -postScript list_functions.py \
    -deleteProject
```

**Mål**: Automatisera så att du kan analysera 100 filer med ett kommando!

#### Övning 6: Differential analysis av två versioner ⭐⭐⭐⭐

**Instruktioner**:
1. Skapa ett program, version 1:
   ```c
   int add(int a, int b) { return a + b; }
   int main() { return add(5, 3); }
   ```
2. Modifiera till version 2:
   ```c
   int add(int a, int b) { return a + b + 1; }  // Bug introduced!
   int subtract(int a, int b) { return a - b; }  // New function
   int main() { return add(5, 3); }
   ```
3. Kompilera båda versionerna
4. Importera båda i Ghidra
5. Använd **Version Tracking** för att jämföra
6. Identifiera exakt vad som ändrats

**Förväntat resultat**:
- `add` har modifierats (ny instruktion: ADD eax, 1)
- `subtract` är ny
- `main` är oförändrad

**Nytta**: Detta är hur säkerhetsforskare hittar bugfixar och reverse-engineerar vad patchar gör!

#### Övning 7: Mini-projekt: Dekryptera kodade strängar ⭐⭐⭐⭐

**Instruktioner**:
1. Skapa ett program med enkelt XOR-krypterade strängar:
   ```c
   #include <stdio.h>
   void decrypt(char *str, int key) {
       for (int i = 0; str[i]; i++) str[i] ^= key;
   }
   int main() {
       char msg[] = {0x1B, 0x1A, 0x1F, 0x1F, 0x18, 0x00};  // "Hello" XOR 0x73
       decrypt(msg, 0x73);
       printf("%s\n", msg);
       return 0;
   }
   ```
2. Kompilera och analysera i Ghidra
3. Identifiera `decrypt`-funktionen
4. Skriv ett Ghidra-script som:
   - Hittar alla arrayer som skickas till `decrypt`
   - Dekrypterar dem (XOR med 0x73)
   - Lägger till dekrypterade strängar som kommentarer

**Förväntat**:
Vid arrayen `{0x1B, 0x1A, ...}` finns nu en kommentar: `// Decrypted: "Hello"`

**Detta är riktigt professionell reverse engineering!**

#### Övning 8: Analysera en packad binär (frivillig, avancerad) ⭐⭐⭐⭐⭐

**Instruktioner**:
1. Ladda ner **UPX** (gratis packer)
2. Packa ett enkelt program: `upx -9 program.exe`
3. Analysera den packade versionen i Ghidra
4. Identifiera unpacker-stubben
5. Använd en debugger för att köra till OEP
6. Dumpa det opackade minnet
7. Analysera den dumpen i Ghidra

**Utmaning**: Detta kräver kombination av statisk analys (Ghidra) och dynamisk analys (debugger).

### 📝 Sammanfattning

#### Key Takeaways
- **Komplexa datastrukturer**: Skapa strukturer för pekare, arrays och objekt – Ghidra behöver hjälp!
- **C++ reverse engineering**: VTables är kluriga, använd OOAnalyzer eller manuell markup
- **Scripting är kraftfullt**: Automatisera repetitiva uppgifter med Python (PyGhidra) eller Java
- **Obfuscation & Packers**: Identifiera tekniker, använd deobfuscation-plugins eller unpacking med debugger
- **Best practices**: Organisation, namngivning, kommentarer, versionshantering – kritiskt för stora projekt
- **Anti-patterns**: Undvik för mycket klickning, dålig dokumentation, och ignorera calling conventions
- **Headless mode**: Batch-analysera hundratals filer utan GUI
- **Differential analysis**: Jämför versioner för att hitta patchar och ändringar

#### Ordlista (Nivå 4)
- **Pekare (Pointer)**: Variabel som innehåller en minnesadress
- **Struktur (Struct)**: Gruppering av flera variabler under ett namn
- **VTable (Virtual Table)**: Tabell med pekare till virtuella funktioner i C++
- **vptr**: Gömd pekare i varje C++-objekt som pekar på klassens vtable
- **Obfuscation**: Tekniker för att göra kod svår att förstå (control flow flattening, junk code, etc.)
- **Packer**: Program som komprimerar/krypterar en binär för att gömma innehåll
- **Entropi**: Mått på slumpmässighet (hög entropi = troligen krypterat/komprimerat)
- **OEP (Original Entry Point)**: Riktiga entry point efter att en binär har opackats
- **Opaque Predicate**: Falsk if-sats som alltid tar samma gren, används för obfuscation
- **Headless Mode**: Kör Ghidra utan GUI för batch-analys
- **PyGhidra**: Python 3-integration för Ghidra (införd i Ghidra 11.3)
- **Ghidrathon**: Äldre Python 3-extension (PyGhidra är nu inbyggt)
- **Equate**: Namnger ett magiskt nummer för bättre läsbarhet
- **Plate Comment**: Kommentar över en hel funktion
- **EOL Comment**: End-of-line kommentar för en specifik rad
- **Thunk**: En funktion som bara hoppar till en annan funktion (ofta imports)

#### Nästa steg
Nu behärskar du avancerad analys och automation! I nästa (sista) nivå går vi in på **expertnivå**: professionell användning av Ghidra i verkliga scenarier (malware-analys, sårbarhetsforskning), plugin-utveckling, integration med andra verktyg, team-samarbete, moderna features (2023-2025), och etiska/juridiska aspekter. Du är redo att bli en Ghidra-expert!

---

## Nivå 5: Professionell reverse engineering med Ghidra 💼

### Introduktion

Grattis! Du har nått expertnivå. I denna sista nivå går vi igenom hur Ghidra används professionellt i verkliga scenarier – malware-analys, sårbarhetsforskning, firmware reverse engineering, och forensik. Du kommer att lära dig om plugin-utveckling för att utöka Ghidras funktionalitet, moderna features i Ghidra 11.3 (2025), team-samarbete med shared projects, integration med andra verktyg i en complete analysis pipeline, samt kritiska etiska och juridiska aspekter. Detta är nivån där du går från hobbyist till professionell reverse engineer. Kunskap på denna nivå krävs för att arbeta inom cybersäkerhet, incident response, eller som säkerhetsforskare.

### Kärnkoncept

#### 1. Professionella användningsområden: Verkliga scenarier

Ghidra används i flera olika professionella sammanhang:

**Malware-analys (Threat Intelligence)**:
- **Mål**: Förstå vad malware gör, hitta indicators of compromise (IOCs), identifiera C2-kommunikation
- **Workflow**:
  1. Isolerad miljö (VM utan nätverk)
  2. Statisk analys i Ghidra: strängar, imports, kontrollflöde
  3. Dynamisk analys med debugger för att se runtime-beteende
  4. Dokumentera: capabilities, network indicators, file artifacts
- **Exempel**: Analysera ransomware för att hitta krypteringsalgoritm och möjlig dekrypteringsnyckel
- **Verktyg**: Ghidra + x64dbg/WinDbg + FLOSS (string extraction) + Wireshark

**Sårbarhetsforskning (Vulnerability Research)**:
- **Mål**: Hitta säkerhetshål i programvara (buffer overflows, use-after-free, etc.)
- **Workflow**:
  1. Reverse-engineera programmet för att förstå arkitekturen
  2. Identifiera "attack surface" (funktioner som tar user input)
  3. Fuzzing för att trigga crashes
  4. Analysera crashes i Ghidra för att förstå root cause
  5. Utveckla proof-of-concept exploit
- **Exempel**: Hitta en buffer overflow i ett network service genom att analysera hur det parsar inkommande paket
- **Verktyg**: Ghidra + AFL/libFuzzer + GDB/WinDbg + pwntools

**Firmware Reverse Engineering (IoT/Embedded)**:
- **Mål**: Förstå hur firmware fungerar, hitta hardcoded credentials, backdoors
- **Workflow**:
  1. Extrahera firmware (från device eller download)
  2. Använd Binwalk för att identifiera och extrahera filsystem
  3. Importera binärer till Ghidra (ofta ARM/MIPS architecture)
  4. Analysera för secrets, vulnerabilities
- **Exempel**: Analysera router firmware för att hitta backdoor
- **Verktyg**: Ghidra + Binwalk + QEMU (emulering) + Firmwalker

**Digital Forensik**:
- **Mål**: Förstå vad okänd programvara på ett system gör (under incident response)
- **Workflow**:
  1. Extrahera binär från komprometterat system
  2. Statisk analys i Ghidra
  3. Identifiera persistence mechanisms, lateral movement
  4. Dokumentera för legal rapport
- **Exempel**: Under en incident, hitta okänd .dll → analysera i Ghidra → identifiera som persistence backdoor
- **Verktyg**: Ghidra + Volatility (memory forensics) + YARA (signature scanning)

#### 2. Modern Ghidra (2023-2025): Nya features

Ghidra 11.3 (februari 2025) introducerade flera kraftfulla features:

**PyGhidra – Native Python 3 Integration**:
- Ersätter Jython 2.7 med full Python 3
- Access till hela Ghidra API från CPython
- Möjliggör användning av moderna Python-bibliotek (numpy, pandas, requests, etc.)
- **Use case**: Scripting med machine learning för att klassificera funktioner

**JIT P-Code Emulator**:
- **Vad**: Just-In-Time kompilerad P-Code emulator (Ghidras intermediära språk)
- **Fördel**: Mycket snabbare emulation än tidigare
- **Use case**: Emulera dekrypteringsrutiner utan att köra malware

**VSCode Integration**:
- Utveckla Ghidra scripts och extensions direkt i VSCode
- Syntax highlighting, debugging, autocomplete
- **Workflow**: Skriv script i VSCode → testa i Ghidra → iterera

**Förbättrad Debugger Support (via eXDI)**:
- Windows kernel debugging i VM
- macOS kernel debugging via LLDB
- **Use case**: Analysera driver-kod live

**LibreTranslate Plugin**:
- Översätt strängar offline (kinesiska, ryska malware → engelska)
- Ingen dependency på externa services
- **Use case**: Analysera malware från andra länder

**Search Decompiled Text Globally**:
- Sök genom dekompilerad kod över **alla funktioner**
- Tidigare: bara search i Listing (assembler)
- **Use case**: Hitta alla ställen som använder ett specifikt API (t.ex. `CreateRemoteThread` för process injection)

#### 3. Plugin-utveckling: Utöka Ghidra

Ghidra är modulärt – du kan skriva egna plugins för custom functionality.

**När utveckla en plugin?**
- Du behöver funktionalitet som inte finns
- Du vill integrera med externa verktyg
- Du har en återkommande analys som skulle gynnas av automation

**Språk**: Java (Ghidra's core är Java)
**IDE**: Eclipse eller IntelliJ IDEA med **GhidraDev**-extension

**Typer av extensions**:
1. **Analyzer**: Körs automatiskt under analysfasen (t.ex. decrypt strings)
2. **Plugin**: Lägger till UI-komponenter, nya menyer, fönster
3. **Loader**: Stödjer nya filformat (t.ex. custom firmware format)
4. **Processor Module**: Stödjer nya CPU-arkitekturer

**Exempel: Enkel plugin-struktur**:
```java
public class MyPlugin extends Plugin {
    public MyPlugin(PluginTool tool) {
        super(tool);
        // Setup UI, register actions
    }

    @Override
    public void init() {
        // Initialize plugin
    }
}
```

**Distribution**: Exportera som `.zip` extension → andra kan installera via **File → Install Extensions**

**Community plugins** (2024-2025):
- **Kaiju**: Advanced binary analysis (YARA integration, function hashing)
- **GhiHorn**: Path analysis, symbolic execution
- **ret-sync**: Sync Ghidra med debugger (x64dbg, IDA, etc.)
- **Dragon Dance**: Binary diffing

#### 4. Team-samarbete: Shared Projects

I professionella teams analyserar flera personer samma binär.

**Shared Project Server**:
- En central server där alla ansluter
- Ändringar synkas i realtid (kommentarer, namngivningar, etc.)
- **Setup**: Kräver Ghidra Server (körs separat)

**Workflow**:
1. Admin startar Ghidra Server
2. Analytiker skapar **Shared Project** och pekar på servern
3. Flera användare kan öppna samma binär
4. Ändringar visas för alla (med användarnamn)
5. Check-in/Check-out system för att undvika konflikter

**Best practices**:
- Använd **version control** (Git för projektfiler, inte binärer)
- Definiera **naming conventions** i teamet
- Ha en **lead analyst** som granskar markup innan merge

**Modern alternative**: Exportera markup till text/JSON → versionshantera det → återimportera

#### 5. Integration med andra verktyg: The RE Toolkit

Ghidra är kraftfullt men inte komplett. Professionella användare kombinerar verktyg.

**Typical RE Toolkit**:
- **Ghidra**: Statisk analys, dekompilering
- **x64dbg / GDB / LLDB**: Dynamisk analys, debugging
- **Frida**: Runtime instrumentation (modifiera beteende live)
- **Binary Ninja** eller **IDA Pro**: Alternativa disassemblers (för jämförelse)
- **Radare2/Rizin**: CLI-based RE (scriptable)
- **angr**: Symbolic execution, automated vulnerability discovery
- **YARA**: Pattern matching för att identifiera malware-familjer

**Integration-exempel 1: Ghidra + Frida**
1. Analysera i Ghidra, identifiera en krypteringsfunktion på adress `0x401234`
2. Skriv Frida-script för att hook `0x401234` och logga input/output
3. Kör programmet med Frida → samla kryptokeys
4. Importera keys tillbaka till Ghidra-analys som kommentarer

**Integration-exempel 2: Ghidra + ret-sync + x64dbg**
1. Installera **ret-sync** plugin i både Ghidra och x64dbg
2. Analysera i Ghidra, sätt en bookmark
3. Klicka på bookmark → hoppar automatiskt till samma adress i x64dbg
4. Ändra kommentar i x64dbg → synkas tillbaka till Ghidra

#### 6. Performance-optimering: Analysera stora binärer

Moderna applikationer kan vara 100+ MB (Chrome, Office, etc.). Ghidra kan bli långsamt.

**Optimeringstekniker**:

**1. Begränsa analysen**:
- Analysera inte bibliotek du inte behöver (t.ex. skippa standard C library)
- **Analysis → Auto Analyze** → avmarkera onödiga analyzers

**2. Öka minne till Ghidra**:
- Redigera `ghidraRun.bat` (Windows) eller `ghidraRun` (Linux)
- Ändra `-Xmx` från default (ofta 4GB) till mer (t.ex. 16GB)
- Exempel: `-Xmx16G`

**3. Dela upp analysen**:
- Om binären har tydliga moduler (t.ex. olika DLL:er), analysera separat
- Använd **Program Trees** för att organisera stora binärer i logiska delar

**4. Custom Analysis Pass**:
- Skriv egna analyzers som bara kör på specifika delar (t.ex. bara .text-sektion)

#### 7. Etik och Juridik: Den kritiska aspekten

**Detta är EXTREMT viktigt!** Reverse engineering kan vara olagligt beroende på omständigheterna.

**Juridiska aspekter (huvudsakligen USA, men liknande i EU)**:

**DMCA (Digital Millennium Copyright Act) – 17 U.S.C. § 1201**:
- Förbjuder "circumvention of technological protection measures"
- **Undantag**: Section 103(f) tillåter RE för **interoperability**
- Exempel: Du får reverse-engineera ett filformat för att skriva en kompatibel reader
- **INTE OK**: Cracking av DRM (t.ex. Spotify, Netflix)

**CFAA (Computer Fraud and Abuse Act) – 18 U.S.C. § 1030**:
- Förbjuder "unauthorized access" till datorsystem
- **Risk**: Kan tolkas brett – även RE av en app kan ses som "exceeding authorized access"
- **Säkert**: Analysera programvara du äger eller har tillstånd att analysera

**Contract Law (EULA, Terms of Service)**:
- Många EULAs förbjuder explicit reverse engineering
- **Gråzon**: Är sådana klausuler verkställbara? Varierar per jurisdiktion
- **USA**: Ofta verkställbart
- **EU**: Software Directive 91/250/EEC tillåter RE för interoperability trots EULA

**Copyright och Fair Use**:
- Fair use kan motivera RE för research, criticism, education
- Inte en absolut garanti – rättspraxis är komplex

**Praktiska riktlinjer för att hålla dig på rätt sida**:
1. **Analysera bara programvara du äger eller har explicit tillstånd att analysera**
2. **Research context**: Dokumentera att ditt syfte är säkerhetsforskning, inte piracy
3. **Disclosure**: Om du hittar sårbarhet, rapportera ansvarigt (responsible disclosure)
4. **Undvik att distribuera cracking-verktyg** – även om analysen är legal
5. **Konsultera juridisk expertis** om du är osäker

**Etiska principer**:
- **Responsible Disclosure**: Rapportera sårbar till vendor innan public release (ofta 90 dagar)
- **Do No Harm**: Använd inte RE för att skada individer eller organisationer
- **Transparency**: Var öppen med dina metoder i research papers
- **Respect Privacy**: Om du hittar användardata under analys, hantera det konfidentiellt

### Exempel: Verkliga Case Studies

#### Case Study 1: Malware-analys – Ransomware Dekryptering

**Scenario**: Ett företag har drabbats av ransomware. Filer är krypterade. Kan vi dekryptera utan att betala lösen?

**Steg 1: Triage**
- Extrahera ransomware-binär från infekterat system
- Kör i isolerad VM (ingen nätverksanslutning!)
- Identifiera ransomware-familj med YARA signatures

**Steg 2: Statisk analys i Ghidra**
- Importera binär
- Leta efter krypteringsrelaterade API-anrop:
  - `CryptEncrypt` (Windows Crypto API)
  - `EVP_EncryptInit` (OpenSSL)
  - Eller custom implementation
- Hitta var nyckeln genereras

**Steg 3: Nyckelgenerering**
Antagom vi hittar i Decompiler:
```c
void generate_key() {
    int seed = GetTickCount();  // Weak! Current time as seed
    srand(seed);
    for (int i = 0; i < 16; i++) {
        key[i] = rand() % 256;
    }
}
```

**Analys**: Nyckeln baseras på `GetTickCount()` vid körning! Detta är en svaghet.

**Steg 4: Återskapa nyckeln**
- Från filesystem timestamps, uppskatta när filer krypterades
- Bruteforce alla möjliga `GetTickCount()`-värden i det tidsintervallet
- För varje seed, generera key, försök dekryptera en fil
- När signatur matchar (t.ex. `.docx` börjar med `PK\x03\x04`) → rätt nyckel!

**Resultat**: Filer dekrypterade utan lösen. Firma sparade $500,000.

**Lärdom**: Svaga RNG (Random Number Generator) i malware är vanligt – reverse engineering kan avslöja dem!

#### Case Study 2: Vulnerability Research – Buffer Overflow i Network Daemon

**Scenario**: Du analyserar ett open-source network daemon för att hitta sårbare.

**Steg 1: Reconnaissance**
- Kompilera daemon
- Importera i Ghidra
- Identifiera "attack surface": funktioner som tar nätverksdata

**Steg 2: Identifiera intressanta funktioner**
I Symbol Tree hittar du: `parse_http_request()`

**Steg 3: Analys i Decompiler**
```c
void parse_http_request(char *buf) {
    char path[256];
    sscanf(buf, "GET %s HTTP/1.1", path);  // VULNERABLE!
    // ... process path ...
}
```

**Problem**: `sscanf` med `%s` läser obegränsat → buffer overflow om input är > 256 bytes!

**Steg 4: Proof of Concept**
- Skapa en HTTP request med 300-byte path
- Kör daemon i debugger
- Bekräfta crash (segfault)
- Analysera: EIP (instruction pointer) överskrivet → code execution möjlig!

**Steg 5: Responsible Disclosure**
- Skriv rapport: vulnerability description, impact, PoC, suggested fix
- Skicka till maintainer (privat)
- Vänta 90 dagar eller till patch, sedan public disclosure

**Resultat**: CVE tilldelad, patch released, säkerhetsresearch-credits.

**Lärdom**: Ghidra hjälper identifiera osäkra kod-mönster – kombinerat med fuzzing blir det kraftfullt!

#### Case Study 3: Firmware Reverse Engineering – IoT Router Backdoor

**Scenario**: Analysera firmware från en IoT router för att hitta security issues.

**Steg 1: Firmware Extraction**
- Ladda ner firmware update file från tillverkarens site (t.ex. `router_fw_v2.bin`)
- Använd **Binwalk**: `binwalk -e router_fw_v2.bin`
- Extraherar filesystem (SquashFS)

**Steg 2: Hitta intressant binär**
I extraherade filer: `/usr/sbin/httpd` (web interface daemon)

**Steg 3: Importera till Ghidra**
- Arkitektur: MIPS (ofta i routers)
- Ghidra stödjer MIPS → importera

**Steg 4: Analys**
Sök efter strängar som "password", "telnet", "backdoor"

Hittar:
```
String: "secret_admin_access"
Referenced by: function at 0x401234
```

Gå till funktionen i Decompiler:
```c
int check_auth(char *username, char *password) {
    if (strcmp(username, "admin") == 0 && strcmp(password, "secret_admin_access") == 0) {
        return 1;  // Grant access
    }
    // ... normal auth ...
}
```

**Backdoor hittad!** Hardcoded credentials: `admin / secret_admin_access`

**Steg 5: Verification**
- Emulera firmware i QEMU
- Försök logga in med backdoor-credentials
- Bekräftat: full admin access!

**Steg 6: Disclosure**
- Rapportera till vendor
- Om vendor ignorerar, public disclosure efter 90 dagar
- Varning till användare: uppdatera firmware eller byt router

**Lärdom**: Firmware är ofta dåligt säkrad – Ghidra + Binwalk är standardverktyg för IoT-analys.

### Visualisering: Professional RE Workflow

```
┌───────────────────────────────────────────────────────────┐
│          PROFESSIONAL REVERSE ENGINEERING WORKFLOW         │
└───────────────────────────────────────────────────────────┘

1. RECONNAISSANCE
   ├─ Filtyp, arkitektur, packer?
   ├─ Strings, imports, exports
   └─ Initial triage

2. STATIC ANALYSIS (Ghidra)
   ├─ Importera & analysera
   ├─ Identifiera entry points
   ├─ Markup: rename, comment, structures
   └─ Dokumentera fynd

3. DYNAMIC ANALYSIS (Debugger)
   ├─ Sätt breakpoints baserat på statisk analys
   ├─ Stega genom kod
   ├─ Observera runtime-beteende
   └─ Dumpa minne vid behov

4. SCRIPTING & AUTOMATION
   ├─ Identifiera repetitiva mönster
   ├─ Skriv Ghidra-scripts för automation
   └─ Batch-analys om flera samples

5. INTEGRATION & CORRELATION
   ├─ Kombinera fynd från olika verktyg
   ├─ Cross-reference med threat intel
   └─ Bygg komplett bild

6. REPORTING & DISCLOSURE
   ├─ Dokumentera: vad, hur, varför
   ├─ Responsible disclosure (om särbarheter)
   └─ Share findings med team/community

7. FOLLOW-UP
   ├─ Monitorera patchar
   ├─ Uppdatera signatures/detections
   └─ Lär från erfarenheten
```

### 💡 Pro Tips (Expert-nivå)

#### Tips 1: Använd Ghidra's "Scripting Development Mode"
Aktivera via **Edit → Tool Options → Scripting**:
- Enable "Source Directory" pointing till ditt Git repo med scripts
- Ändra script → Ghidra laddar om automatiskt (ingen manuell refresh)
- Perfekt för snabb iteration under script-utveckling

#### Tips 2: Kör Ghidra i Debug-mode för plugin-utveckling
```bash
ghidraRun -debug 18001
```
Anslut sedan Eclipse/IntelliJ debugger på port 18001 → sätt breakpoints i din plugin-kod!

#### Tips 3: Bygg en personal "RE Playbook"
Dokumentera alla custom scripts, workflows, och knep du lär dig. Över tid blir detta en ovärderlig resurs.

Struktur:
```
RE_Playbook/
├── Scripts/
│   ├── decrypt_strings.py
│   ├── find_crypto.py
│   └── ...
├── Workflows/
│   ├── malware_triage.md
│   ├── vulnerability_research.md
│   └── ...
└── Reference/
    ├── calling_conventions.md
    ├── common_patterns.md
    └── ...
```

#### Tips 4: Delta-analys mellan Ghidra och IDA för maximal täckning
Olika dekompillers producerar olika resultat. För kritisk analys:
- Analysera samma binär i både Ghidra och IDA Pro
- Jämför dekompilering av samma funktion
- Ofta får du olika "perspectives" som kompletterar varandra

#### Tips 5: Bidra till Ghidra-communityn
När du utvecklat något användbart:
- Publicera scripts på GitHub
- Skriv tutorials/blog posts
- Bidra med bugfixar till Ghidra-projektet
- Delta i NSA Ghidra GitHub discussions

Att ge tillbaka stärker hela ekosystemet!

### ✏️ Övningar (Expert-nivå)

#### Övning 1: Full malware-analys (ENDAST utbildningsmalware!) ⭐⭐⭐⭐⭐

**VARNING**: Använd endast malware-samples från **legitima educational sources** (t.ex. malware.re, malware-traffic-analysis.net med tydlig educational licensing).

**Instruktioner**:
1. Skaffa en safe malware sample (ransomware eller banker trojan)
2. Skapa isolerad VM (snapshot före analys!)
3. Statisk analys i Ghidra:
   - Hitta alla nätverksrelaterade funktioner
   - Identifiera C2-kommunikation
   - Hitta persistence mechanisms
4. Dynamisk analys i debugger
5. Skriv en **full rapport** (5-10 sidor) som inkluderar:
   - Executive summary
   - Technical analysis
   - IOCs (IP addresses, domains, file hashes)
   - Mitigation recommendations

**Mål**: Detta är vad professionella malware-analytiker gör dagligen!

#### Övning 2: Utveckla en Ghidra-plugin ⭐⭐⭐⭐⭐

**Instruktioner**:
1. Installera Eclipse och GhidraDev
2. Skapa ett nytt Ghidra Plugin Project
3. Implementera en enkel plugin som:
   - Lägger till en ny meny: "My Tools → Find Crypto Constants"
   - Scannar hela programmet efter kända kryptografiska konstanter (t.ex. AES S-box, SHA round constants)
   - Visar resultat i en dialog
4. Exportera och installera pluginen
5. Testa på ett program som använder OpenSSL eller liknande

**Resources**: Använd Ghidra's JavaDoc och exempel-plugins i `<ghidra>/Extensions/sample/`

#### Övning 3: Setup Shared Project med kollegor ⭐⭐⭐⭐

**Instruktioner**:
1. Installera Ghidra Server på en maskin (kan vara localhost för test)
2. Skapa ett Shared Project
3. Bjud in en kollega (eller använd två Ghidra-instanser själv)
4. Båda analyserar samma binär samtidigt
5. Testa:
   - Döp om en funktion i instans 1 → se att den uppdateras i instans 2
   - Lägg till kommentarer i instans 2 → se i instans 1
6. Dokumentera workflow för team-analys

#### Övning 4: Integrera Ghidra med Frida ⭐⭐⭐⭐

**Instruktioner**:
1. Analysera en enkel app i Ghidra (t.ex. en console app som frågar efter password)
2. Identifiera password-checking-funktionen
3. Skriv ett Frida-script som:
   - Hookar password-check-funktionen
   - Loggar input-password
   - Alterar return-värdet till "always true"
4. Kör appen med Frida → bypass password check
5. Dokumentera processen: Ghidra-analys → Frida-hook → bypass

**Lärdom**: Kombination av statisk (Ghidra) och dynamisk (Frida) analys är extremt kraftfullt!

#### Övning 5: Responsible Disclosure – simulering ⭐⭐⭐⭐

**Instruktioner**:
1. Hitta ett open-source projekt (t.ex. ett litet network daemon på GitHub)
2. Reverse-engineera det i Ghidra
3. Leta efter **potentiella** sårbarheter (buffer overflow, format string, use-after-free)
4. Om du hittar något:
   - Skriv en PoC (Proof of Concept) som demonstrerar sårbarheten
   - Skriv en disclosure-rapport (inkludera: beskrivning, impact, PoC, suggested fix)
   - Skicka till projektet (via GitHub issue eller privat email till maintainer)
   - Följ responsible disclosure guidelines: 90 dagar grace period

**Viktigt**: Välj ett LITET projekt där maintainer troligen uppskattar hjälpen. Stora projekt har ofta bounty programs – följ deras process!

### 📝 Sammanfattning

#### Key Takeaways
- **Professionell användning**: Malware-analys, vulnerability research, firmware RE, forensik – olika workflows för olika mål
- **Ghidra 11.3 (2025)**: PyGhidra (Python 3), JIT emulator, VSCode integration, förbättrad debugger, LibreTranslate, global decompile search
- **Plugin-utveckling**: Utöka Ghidra med Java-plugins – analyzers, UI-extensions, loaders, processor modules
- **Team-samarbete**: Shared Projects med Ghidra Server för real-time collaboration
- **Verktygintegration**: Ghidra + debuggers + Frida + Binwalk + angr = complete RE toolkit
- **Performance**: Optimera för stora binärer – begränsa analys, öka minne, custom analyzers
- **Etik & Juridik**: DMCA (interoperability exception), CFAA (unauthorized access), contract law (EULA), fair use – **KRITISKT att förstå!**
- **Responsible disclosure**: Rapportera sårbarer ansvarigt (90 dagar grace period)
- **Verkliga case studies**: Ransomware dekryptering, buffer overflow discovery, firmware backdoors – praktiska exempel

#### Ordlista (Nivå 5)
- **Threat Intelligence**: Samling och analys av information om cyberhot
- **IOC (Indicator of Compromise)**: Artifact som indikerar säkerhetsincident (IP, hash, domain)
- **C2 (Command & Control)**: Server som malware kommunicerar med för instruktioner
- **Attack Surface**: Alla punkter där en applikation tar input (potentiella sårbararer)
- **Fuzzing**: Automated testing med slumpmässig/muterad input för att hitta crashes
- **Use-After-Free**: Sårbarhet där minne används efter det har frigjorts
- **PoC (Proof of Concept)**: Demonstration av en sårbarhet
- **RNG (Random Number Generator)**: Algoritm för att generera slumptal
- **Responsible Disclosure**: Etisk process för att rapportera sårbarheter
- **CVE (Common Vulnerabilities and Exposures)**: Standardiserad identifierare för sårbarheter
- **DMCA**: Digital Millennium Copyright Act – USA copyright-lag
- **CFAA**: Computer Fraud and Abuse Act – USA cybercrime-lag
- **EULA**: End User License Agreement
- **Fair Use**: Juridisk doktrin som tillåter begränsad användning av copyrighted material
- **Interoperability**: Förmåga för system att samarbeta
- **GhidraDev**: Eclipse/IntelliJ-plugin för Ghidra-utveckling
- **Shared Project**: Ghidra-projekt som delas mellan flera användare via server
- **P-Code**: Ghidras intermediära representation av maskinkod
- **JIT**: Just-In-Time compilation
- **Symbolic Execution**: Analysteknik som utforskar alla möjliga execution paths

#### Du har nu nått Ghidra-masternivå!

Grattis! Du har nu genomgått hela resan från nybörjare till expert. Du förstår:
- Grundläggande koncept och terminologi
- Praktisk användning och navigation
- Avancerad analys och scripting
- Professionella workflows och verkliga användningsområden
- Etiska och juridiska aspekter

**Nästa steg för dig**:
1. **Praktisera**: Analysera verkliga program, lös crackmes, delta i CTF-tävlingar
2. **Specialisera**: Välj ett område (malware, vulnerability research, firmware) och fördjupa dig
3. **Bidra**: Dela dina scripts, tutorials, och plugins med communityn
4. **Håll dig uppdaterad**: Följ Ghidra releases, nya plugins, research papers
5. **Nätverka**: Gå med i RE-communities (Reddit r/ReverseEngineering, Discord-servrar, Twitter)

**Du är nu redo för professionell reverse engineering. Lycka till!**

---

## 🎓 Slutlig Självutvärdering

Använd denna checklista för att bedöma vilken nivå du befinner dig på och vad du behöver träna mer på.

### Nivå 1: Förstår grundkonceptet ✓
- [ ] Jag kan förklara vad reverse engineering är med enkla ord
- [ ] Jag förstår att program är "slutna lådor" som kan analyseras
- [ ] Jag vet att Ghidra är ett verktyg för att titta "inuti" program

### Nivå 2: Känner till terminologin ✓
- [ ] Jag kan förklara skillnaden mellan källkod och binär
- [ ] Jag vet vad assembler och dekompilering är
- [ ] Jag känner till Ghidras huvudfönster (Listing, Decompiler, Symbol Tree)
- [ ] Jag förstår vad en funktion och variabel är

### Nivå 3: Kan använda Ghidra praktiskt ✓
- [ ] Jag har installerat Ghidra framgångsrikt
- [ ] Jag kan skapa projekt och importera binärer
- [ ] Jag kan navigera i CodeBrowser (Listing, Decompiler, Function Graph)
- [ ] Jag kan hitta strängar och spåra var de används
- [ ] Jag kan döpa om funktioner och lägga till kommentarer
- [ ] Jag förstår grundläggande x86/x64 (register, stack, calling conventions)
- [ ] Jag kan analysera en enkel "Hello World"-binär från början till slut

### Nivå 4: Behärskar avancerade tekniker ✓
- [ ] Jag kan skapa och applicera datastrukturer i Ghidra
- [ ] Jag kan analysera C++-kod med vtables
- [ ] Jag har skrivit minst ett fungerande Ghidra-script (Python eller Java)
- [ ] Jag kan identifiera packers och obfuscation
- [ ] Jag följer best practices: namngivning, dokumentation, versionshantering
- [ ] Jag kan köra headless batch-analys
- [ ] Jag kan göra differential analysis mellan två versioner av ett program

### Nivå 5: Professionell användning ✓
- [ ] Jag har genomfört en fullständig malware-analys (på educational sample)
- [ ] Jag har utvecklat en egen Ghidra-plugin eller avancerat script
- [ ] Jag kan integrera Ghidra med andra verktyg (debugger, Frida, etc.)
- [ ] Jag förstår etiska och juridiska aspekter av reverse engineering
- [ ] Jag kan följa responsible disclosure-processen
- [ ] Jag kan optimera Ghidra för stora binärer
- [ ] Jag är bekant med Ghidra 11.3's nya features (PyGhidra, JIT emulator, etc.)

### Färdighetsnivåer

**Beginner (0-25% checkboxar)**: Du har börjat din resa! Fokusera på Nivå 1-2, lär dig terminologin.

**Intermediate (26-50% checkboxar)**: Bra framsteg! Fortsätt med praktiska övningar i Nivå 3-4.

**Advanced (51-75% checkboxar)**: Du är på god väg! Fördjupa dig i scripting och verkliga use cases.

**Expert (76-100% checkboxar)**: Grattis! Du behärskar Ghidra. Överväg att bidra till communityn och specialisera dig.

---

## 📖 Ordlista

En samlad ordlista över alla viktiga termer från guiden, sorterad alfabetiskt.

### A
- **Analysis**: Ghidras automatiska process för att förstå en binär fil (hitta funktioner, strängar, etc.)
- **Analyzer**: Plugin som körs automatiskt under analysfasen
- **Anti-debugging**: Tekniker som malware använder för att upptäcka och motverka debugging
- **Assembler**: Maskinnära kod som är lite mer läsbar än rå maskinkod
- **Attack Surface**: Alla punkter där en applikation tar input (potentiella sårbarheter)

### B
- **Basic Block**: Ett sammanhängande stycke kod utan grenar (visas som en ruta i Function Graph)
- **Binär/Körbar fil**: Färdig fil (t.ex. `.exe`) som datorn kan köra direkt

### C
- **C2 (Command & Control)**: Server som malware kommunicerar med för instruktioner
- **Call Graph**: Diagram som visar vilka funktioner som anropar vilka
- **Calling Convention**: Regler för hur funktioner tar emot parametrar och returnerar värden
- **CFAA**: Computer Fraud and Abuse Act – USA cybercrime-lag
- **CVE**: Common Vulnerabilities and Exposures – standardiserad identifierare för sårbarheter

### D
- **Data Type Manager**: Ghidra-fönster som visar olika datatyper
- **Decompiler**: Fönster i Ghidra som visar dekompilerad (C-liknande) kod
- **Dekompilering**: Processen att försöka återskapa källkod från en binär fil
- **DMCA**: Digital Millennium Copyright Act – USA copyright-lag

### E
- **EIP/RIP (Instruction Pointer)**: Register som pekar på nästa instruktion
- **Entry Point**: Första funktionen som körs när ett program startar
- **Entropi**: Mått på slumpmässighet (hög entropi = troligen krypterat/komprimerat)
- **EOL Comment**: End-of-line kommentar för en specifik rad
- **Equate**: Namnger ett magiskt nummer för bättre läsbarhet
- **ESP/RSP (Stack Pointer)**: Register som pekar på toppen av stacken
- **EULA**: End User License Agreement

### F
- **Fair Use**: Juridisk doktrin som tillåter begränsad användning av copyrighted material
- **Function**: En namngiven del av kod som gör en specifik uppgift
- **Function Graph**: Visuellt diagram över hur en funktion fattar beslut
- **Fuzzing**: Automated testing med slumpmässig/muterad input för att hitta crashes

### G
- **GhidraDev**: Eclipse/IntelliJ-plugin för Ghidra-utveckling
- **Ghidrathon**: Äldre Python 3-extension för Ghidra

### H
- **Headless Mode**: Kör Ghidra utan GUI för batch-analys

### I
- **Import**: Processen att läsa en binär fil in i Ghidra
- **Interoperability**: Förmåga för system att samarbeta
- **IOC (Indicator of Compromise)**: Artifact som indikerar säkerhetsincident

### J
- **JDK (Java Development Kit)**: Programvara som krävs för att köra Ghidra
- **JIT**: Just-In-Time compilation

### L
- **Listing**: Fönster i Ghidra som visar assembler-kod

### M
- **Markup**: Manuella ändringar i Ghidra (kommentarer, omdöpningar)
- **Maskinkod**: Rå instruktioner i form av siffror som datorn förstår
- **Minne**: Var datorn sparar data medan ett program körs

### O
- **Obfuscation**: Tekniker för att göra kod svår att förstå
- **OEP (Original Entry Point)**: Riktiga entry point efter unpacking
- **Opaque Predicate**: Falsk if-sats som alltid tar samma gren

### P
- **Packer**: Program som komprimerar/krypterar en binär
- **P-Code**: Ghidras intermediära representation av maskinkod
- **Pekare (Pointer)**: Variabel som innehåller en minnesadress
- **Plate Comment**: Kommentar över en hel funktion
- **PoC (Proof of Concept)**: Demonstration av en sårbarhet
- **PyGhidra**: Python 3-integration för Ghidra (Ghidra 11.3+)

### R
- **Register**: Snabba lagringsplatser inuti CPU:n
- **Responsible Disclosure**: Etisk process för att rapportera sårbarheter
- **RNG (Random Number Generator)**: Algoritm för att generera slumptal

### S
- **Shared Project**: Ghidra-projekt som delas mellan flera användare via server
- **Stack**: LIFO-datastruktur för att lagra returadresser och lokala variabler
- **Struktur (Struct)**: Gruppering av flera variabler under ett namn
- **Symbol Tree**: Lista över funktioner, data och symboler i programmet
- **Symbolic Execution**: Analysteknik som utforskar alla möjliga execution paths
- **Källkod**: Kod skriven av programmerare i språk som C, Python, Java

### T
- **Threat Intelligence**: Samling och analys av information om cyberhot
- **Thunk**: En funktion som bara hoppar till en annan funktion

### U
- **Use-After-Free**: Sårbarhet där minne används efter det har frigjorts

### V
- **Variabel**: En "låda" som håller data (siffror, text, etc.)
- **vptr**: Gömd pekare i C++-objekt som pekar på klassens vtable
- **VTable (Virtual Table)**: Tabell med pekare till virtuella funktioner i C++

---

## 🔗 Resurser för Fördjupning

### Officiella Ghidra-resurser

**Ghidra Officiell Site**:
- GitHub Repository: NationalSecurityAgency/ghidra (releases, källkod, issue tracker)
- Dokumentation: Finns i Ghidra-installationen under `docs/`
- API JavaDoc: Komplett reference för scripting och plugin-utveckling

**Ghidra Training Materials** (NSA):
- Beginner Class: Introduction to Ghidra
- Advanced Development Class: Plugin och extension-utveckling
- Alla finns i `<ghidra>/docs/GhidraClass/`

### Böcker

**"The Ghidra Book: The Definitive Guide"** (No Starch Press):
- Omfattande guide från grunderna till avancerade tekniker
- Praktiska exempel och case studies
- Författare: Chris Eagle och Kara Nance

**"Practical Reverse Engineering"** (Bruce Dang, Alexandre Gazet, Elias Bachaalany):
- Täcker RE generellt, inte bara Ghidra
- Excellent komplement för att förstå low-level detaljer

**"Ghidra Software Reverse Engineering for Beginners"** (Packt):
- Steg-för-steg tutorials från installation till avancerad analys

### Online-kurser

**TryHackMe**: "Ghidra" room – interaktiv hands-on kurs

**Kaspersky Expert Training**: "Advanced Malware Reverse Engineering with Ghidra"

**Hackaday.io**: "Introduction to Reverse Engineering with Ghidra" – fyra sessioner

### Tutorials och Blogs

**Shogun Lab**: "Here Be Dragons: Reverse Engineering with Ghidra" (serie)

**VoidStar Security**: Ghidra development environment setup och plugin-tutorials

**Medium**: Sök efter "Ghidra" för hundratals tutorials om olika use cases

### Community och Forum

**Reddit**:
- r/ReverseEngineering – allmän RE-community
- r/Ghidra – specifik för Ghidra-diskussioner

**Discord**: Flera RE-servrar med Ghidra-channels

**Twitter/X**: Följ #Ghidra och @NSACyber för updates

**GitHub Discussions**: NationalSecurityAgency/ghidra – officiella diskussioner

### Plugins och Scripts

**GitHub Topics**:
- ghidra-scripts – 40+ repositories med Python-scripts
- ghidra-plugins – 25+ repositories med Java-plugins
- ghidra-extension – extensions och analyzers

**Notabla plugins**:
- **Kaiju** (CERT): Binary analysis, YARA integration
- **GhiHorn** (CERT): Symbolic execution och path analysis
- **ret-sync**: Synkronisera Ghidra med debuggers
- **Dragon Dance**: Binary diffing
- **FindCrypt-Ghidra**: Identifiera kryptografiska konstanter

### Practice och Utmaningar

**Crackmes.one**: Hundratals reverse engineering-utmaningar (olika svårighetsgrader)

**Malware Traffic Analysis**: Educational malware samples med tillhörande PCAP-filer

**PicoCTF, HackTheBox, CTFtime**: CTF-tävlingar med RE-challenges

**FLARE-On**: Årlig RE-CTF från FireEye/Mandiant

### Relaterade Verktyg (för komplett toolkit)

**Disassemblers/Decompilers**:
- Binary Ninja – modern alternativ till Ghidra
- IDA Pro – industry standard (kommersiell)
- Radare2/Rizin – CLI-based RE

**Debuggers**:
- x64dbg – Windows debugger
- GDB – Linux debugger
- LLDB – macOS debugger
- WinDbg – Windows kernel debugger

**Dynamic Analysis**:
- Frida – Runtime instrumentation
- PIN – Intel's dynamic instrumentation
- DynamoRIO – Dynamic instrumentation platform

**Malware Analysis**:
- FLOSS – String extraction från malware
- Volatility – Memory forensics
- YARA – Pattern matching

**Firmware Analysis**:
- Binwalk – Firmware extrahering
- QEMU – Emulation
- Firmwalker – Firmware-analys automation

### Håll dig uppdaterad

**NSA GitHub**: Watch NationalSecurityAgency/ghidra för nya releases

**Ghidra Release Cycle**: Nya versioner släpps cirka 2-3 gånger per år

**Security Conferences**: REcon, Black Hat, DEF CON – ofta Ghidra-talks

**Podcasts**:
- Risky Business – cybersecurity news (täcker RE-verktyg)
- Malicious Life – malware history (RE-context)

---

## ❓ Vanliga Frågor (FAQ)

### Grundläggande frågor

**1. Är Ghidra verkligen gratis?**

Ja! Ghidra är helt gratis och open source (Apache License 2.0). Det finns inga begränsningar, ingen "pro version", inga dolda kostnader. Du kan använda det för både personligt bruk och kommersiellt arbete utan att betala.

**2. Hur jämförs Ghidra med IDA Pro?**

**Ghidra fördelar**: Gratis, open source, kraftfull dekompilare, P-Code (intermediär språk), kollaborativa projekt.

**IDA Pro fördelar**: Större plugin-ekosystem, bättre stöd för vissa exotiska arkitekturer, snabbare för mycket stora binärer, mer mogen (finns sedan 1990-talet).

**Slutsats**: För de flesta användare räcker Ghidra utmärkt. IDA Pro är värt investeringen för professionella som behöver specialiserade features.

**3. Kan jag använda Ghidra på Windows/Linux/macOS?**

Ja! Ghidra är multi-platform eftersom det är skrivet i Java. Fungerar identiskt på Windows, Linux och macOS. Kräver bara JDK 21 (Ghidra 11.3) eller senare.

**4. Hur mycket minne behöver Ghidra?**

**Minimum**: 4 GB RAM
**Rekommenderat**: 8 GB RAM
**För stora binärer (>100 MB)**: 16+ GB RAM

Du kan öka Ghidras minnesallokering genom att redigera `ghidraRun`-scriptet.

**5. Kan Ghidra köra/debugga program?**

Ghidra 11.3 har debugger-support (för vissa plattformar via eXDI), men primärt fokus är **statisk analys**. För full debugging, använd Ghidra tillsammans med x64dbg, GDB, eller LLDB. Plugin **ret-sync** kan synkronisera mellan Ghidra och en debugger.

### Installation och Setup

**6. Varför startar inte Ghidra? (Vanliga problem)**

**Problem 1**: "Java not found"
- **Lösning**: Installera JDK 21, se till att `java` finns i PATH

**Problem 2**: "Unsupported Java version"
- **Lösning**: Uppgradera till JDK 21 (Ghidra 11.3 kräver det)

**Problem 3**: Ghidra startar men är extremt långsamt
- **Lösning**: Öka minne i `ghidraRun` script (`-Xmx8G` istället för `-Xmx4G`)

**7. Var hittar jag Ghidra-installationen?**

Det beror på var du extraherade ZIP-filen:
- **Windows**: Ofta `C:\Tools\ghidra_11.3\`
- **Linux**: Ofta `/opt/ghidra_11.3/` eller `~/ghidra_11.3/`
- **macOS**: Ofta `/Applications/ghidra_11.3/`

**8. Hur uppdaterar jag Ghidra?**

Ghidra uppdateras INTE automatiskt. För att uppdatera:
1. Ladda ner den nya versionen från GitHub
2. Extrahera till ny mapp
3. Dina gamla projekt är kompatibla (öppna dem med nya Ghidra)

### Användning

**9. Vad är skillnaden mellan Listing och Decompiler?**

- **Listing**: Visar **assembler-kod** (maskinnära instruktioner). 100% exakt men svårt att läsa.
- **Decompiler**: Visar **C-liknande pseudo-kod**. Lättare att förstå men inte perfekt (en gissning baserad på assembler).

**Best practice**: Använd BÅDA! Decompiler för snabb förståelse, Listing för exakta detaljer.

**10. Hur analyserar jag en binär första gången?**

**Workflow**:
1. **File → Import File** (eller dra-och-släpp)
2. Ghidra detekterar format automatiskt → klicka OK
3. Dubbelklicka filen i Project Window → CodeBrowser öppnas
4. Klicka "Yes" när fråga kommer: "Analyze now?"
5. Klicka "Analyze" (med default settings)
6. Vänta på analys (kan ta sekunder till minuter)
7. Utforska: Symbol Tree → Functions, hitta `main` eller `entry`, dubbelklicka

**11. Hur hittar jag "main"-funktionen?**

- Sök i **Symbol Tree → Functions** efter "main"
- Om den inte heter "main", leta efter "entry", "_start", eller liknande
- På Windows, ofta "WinMain" eller "wWinMain"
- Om du inte hittar den, gå till **entry point** (visas automatiskt vid analys)

**12. Kan jag ändra/patcha en binär med Ghidra?**

Ja, men med begränsningar:
- Ghidra är primärt för **analys**, inte patching
- Du kan ändra bytes via **Patch Instruction** (Ctrl+Shift+G) men det är klumpigt
- För riktiga patchar, använd verktyg som **x64dbg**, **HxD** (hex editor), eller **Binary Ninja**
- Ghidra kan sedan exportera den modifierade binären

### Scripting och Automation

**13. Ska jag lära mig Python eller Java för Ghidra-scripting?**

**Python (PyGhidra)** – Rekommenderat för de flesta:
- Enklare syntax
- Snabbare att skriva prototyper
- Från Ghidra 11.3: native Python 3-support!

**Java** – Om du behöver:
- Maximal prestanda
- Utveckla plugins (inte bara scripts)

**Slutsats**: Börja med Python. Gå till Java när du behöver skriva plugins.

**14. Var hittar jag exempel-scripts?**

- I Ghidra: **Window → Script Manager** → filter på "Examples"
- Ghidra-installationen: `<ghidra>/Ghidra/Features/Python/ghidra_scripts/`
- GitHub: Sök "ghidra-scripts" → hundratals exempel

**15. Hur kör jag ett script?**

1. **Window → Script Manager**
2. Hitta ditt script (eller skriv nytt: **New → Python**)
3. Dubbelklicka för att köra
4. Output visas i Console-fönstret

**Headless** (utan GUI):
```bash
analyzeHeadless /path/project ProjectName -import file.exe -postScript myscript.py
```

### Avancerad användning

**16. Hur analyserar jag packade/obfuscerade binärer?**

**Steg 1**: Identifiera packer (UPX, Themida, VMProtect):
- Använd **DIE** (Detect It Easy) eller **Exeinfo PE**

**Steg 2**: Försök unpacking:
- **Statiskt**: Vissa packers har automatisk unpackers (t.ex. UPX: `upx -d file.exe`)
- **Dynamiskt**: Kör i debugger, dumpa minnet vid OEP (Original Entry Point)

**Steg 3**: Analysera uppackad version i Ghidra

**För obfuscation**: Använd plugins som **Ghidra Deobfuscator** eller skriv custom scripts.

**17. Hur analyserar jag firmware/IoT-binärer?**

1. Extrahera firmware: **Binwalk** (`binwalk -e firmware.bin`)
2. Hitta intressant binär (ofta MIPS, ARM, PowerPC)
3. Importera till Ghidra, välj rätt arkitektur
4. Analysera normalt

**Tips**: Många IoT-devices har minimalt med symboler → mycket manuell markup krävs.

**18. Kan flera personer analysera samma binär samtidigt?**

Ja! Använd **Shared Project**:
1. Starta Ghidra Server på en central maskin
2. Skapa Shared Project (istället för Non-Shared)
3. Andra användare ansluter till servern
4. Ändringar synkas i realtid

**Alternativ**: Exportera markup till XML/Git → merge manuellt.

### Etik och Legalitet

**19. Är reverse engineering lagligt?**

**Kortsvar**: Det beror på.

**Lagligt**:
- Analysera programvara du äger eller har tillstånd att analysera
- Research för interoperability (DMCA Section 103(f))
- Security research (responsible disclosure)
- Educational purposes

**Olagligt/Riskabelt**:
- Bryta kryptering/DRM (DMCA anti-circumvention)
- Reverse-engineera för att skapa pirat-kopior
- Analysera programvara utan tillstånd (kan bryta EULA)
- "Unauthorized access" enligt CFAA

**Rådvara din rätt**: Konsultera juridisk expertis om du är osäker.

**20. Vad är responsible disclosure?**

När du hittar en sårbarhet:
1. **Rapportera privat** till vendor (email, bug bounty program)
2. **Vänta 90 dagar** (grace period för vendor att patcha)
3. Om vendor patchar: public disclosure med credits
4. Om vendor ignorerar: public disclosure efter 90 dagar med varning

**Publicera INTE sårbarheten direkt** – det kan utnyttjas av angripare innan patch finns.

### Felsökning

**21. Varför dekompilerar inte Ghidra en funktion?**

Möjliga orsaker:
- Funktionen är för komplex (Ghidra ger upp)
- Obfuscerad kod (Ghidra förstår inte kontrollflödet)
- Indirekt hopp/anrop som Ghidra inte kan lösa

**Lösningar**:
- Titta på Listing (assembler) istället
- Använd plugins för deobfuscation
- Manuell markup: Fix kontrollflöde, skapa funktioner manuellt

**22. Ghidra kraschar/fryser när jag analyserar stora filer. Vad gör jag?**

**Lösningar**:
1. **Öka minne**: Redigera `ghidraRun`, ändra `-Xmx4G` till `-Xmx16G`
2. **Begränsa analys**: Analysis → Auto Analyze → avmarkera onödiga analyzers
3. **Dela upp**: Analysera olika delar separat
4. **Starkare dator**: SSD, mer RAM, snabbare CPU hjälper

**23. Hur bidrar jag till Ghidra-projektet?**

1. **Bugfixar/Features**: Fork GitHub-repo, gör ändringar, skicka Pull Request
2. **Rapportera buggar**: GitHub Issues med detaljerad beskrivning och reproduktionssteg
3. **Dokumentation**: Förbättra befintlig dokumentation eller skriv tutorials
4. **Community**: Hjälp andra på forum, Reddit, Discord

**Tack för att du vill bidra till open source!**

---

**🎉 Grattis! Du har nu genomgått hela den kompletta Ghidra-guiden!**

Du har rest från grundläggande koncept (5-åringen) till professionell masternivå (expert). Du är nu rustad med kunskap om:

- Installation och konfiguration
- Grundläggande och avancerad användning
- Scripting och automation
- Professionella workflows
- Etiska och juridiska aspekter
- Moderna features (Ghidra 11.3, 2025)

**Din resa börjar här.** Använd denna guide som referens, praktisera regelbundet, och dela med dig av din kunskap till andra. Reverse engineering är en konst som kräver tålamod, nyfikenhet och kontinuerlig inlärning.

**Lycka till i din reverse engineering-karriär!**

