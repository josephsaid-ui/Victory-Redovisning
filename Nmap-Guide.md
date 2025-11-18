# Nmap & Nätverksskanning – Den Kompletta Guiden

## 📚 Innehållsförteckning

- [Om Denna Guide](#-om-denna-guide)
- [Nivå 1: Datorer som Pratar med Varandra 👶](#nivå-1-datorer-som-pratar-med-varandra-)
- [Nivå 2: IP-adresser, Portar & Första Nmap-kommandot 🧒](#nivå-2-ip-adresser-portar--första-nmap-kommandot-)
- [Nivå 3: Så Fungerar Internet på Riktigt 🎓](#nivå-3-så-fungerar-internet-på-riktigt-)
- [Nivå 4: Avancerad Nätverksteori & Komplexa Miljöer 🏛️](#nivå-4-avancerad-nätverksteori--komplexa-miljöer-️)
- [Nivå 5: Expert – Stora Nätverk & Professionell Användning 💼](#nivå-5-expert--stora-nätverk--professionell-användning-)
- [Slutlig Självutvärdering 🎓](#-slutlig-självutvärdering)
- [Ordlista 📖](#-ordlista)
- [Resurser för Fördjupning 🔗](#-resurser-för-fördjupning)
- [Vanliga Frågor (FAQ) ❓](#-vanliga-frågor-faq)

---

## 🎯 Om Denna Guide

### Välkommen!

Denna guide tar dig från absolut nybörjare till expert inom nätverksskanning och Nmap. Du behöver inga förkunskaper – vi börjar med grunderna och bygger kunskapen steg för steg.

### Hur ska du läsa denna guide?

Guiden är uppdelad i **5 nivåer**, var och en tar cirka 10–20 minuter att läsa:

- **Nivå 1** (👶): För dig som aldrig hört talas om nätverk – vi förklarar som för ett barn
- **Nivå 2** (🧒): Grundläggande begrepp och dina första Nmap-kommandon
- **Nivå 3** (🎓): Så fungerar TCP/IP och olika scan-typer på riktigt
- **Nivå 4** (🏛️): Avancerad nätverksteori, brandväggar och komplexa miljöer
- **Nivå 5** (💼): Expert-användning i stora organisationer

**Total tid**: 1.5–3 timmar beroende på ditt tempo.

Du kan läsa nivåerna i följd eller hoppa till den nivå som passar din nuvarande kunskap. Varje nivå avslutas med övningar och en sammanfattning.

### ⚠️ VIKTIG JURIDISK OCH ETISK BRASKLAPP

**LÄS DETTA INNAN DU BÖRJAR:**

- **Scanna ENDAST dina egna nätverk eller nätverk där du har skriftligt tillstånd**
- Att scanna andras nätverk utan tillstånd är **olagligt** i de flesta länder, inklusive Sverige
- Denna guide är avsedd för **utbildning, felsökning och säkerhetsgranskning** av egna system
- Du är **själv ansvarig** för hur du använder denna kunskap
- När du övar: Använd **ditt eget hemnätverk**, virtuella testmiljöer eller officiella övningslabbar

**Etiska principer:**
- Be alltid om tillstånd först
- Dokumentera vad du gör och varför
- Respektera andras integritet och system
- Använd kunskapen för att göra internet säkrare, inte för att skada

---

## Nivå 1: Datorer som Pratar med Varandra 👶

### Introduktion

På denna nivå ska du lära dig vad ett nätverk är och vad det betyder att "scanna" ett nätverk. Vi kommer inte använda några svåra ord – istället tänker vi på datorer som kompisar som pratar med varandra! Detta är grunden för allt som kommer sedan, så ta det lugnt och låt bilderna sjunka in.

### Kärnkoncept

#### 1. Datorer kan prata med varandra

Precis som du kan prata med din kompis genom att ropa, skicka en lapp, eller använda en walkie-talkie, kan datorer prata med varandra! När du kollar på en film på Netflix, "pratar" din dator eller surfplatta med en annan dator långt borta som skickar filmen till dig.

**Tänk så här**: När du säger "Hej!" till din kompis och kompisen svarar "Hej tillbaka!", då har ni pratat med varandra. Datorer gör samma sak, men istället för att säga "Hej" kanske de säger "Kan jag få en bild?" eller "Här kommer en film!".

#### 2. Nätverk är som vägar mellan hus

Ett nätverk är alla vägar som datorer använder för att prata med varandra. Precis som du kan gå på vägar mellan olika hus i ditt kvarter, kan meddelanden från datorer färdas på vägar mellan olika datorer.

**Tänk så här**:
- Ditt hus = din dator
- Grannarnas hus = andra datorer
- Vägarna mellan husen = nätverket
- Brev du skickar = meddelanden datorer skickar

#### 3. Inte alla datorer pratar hela tiden

Precis som din kompis ibland sover och inte kan svara när du ropar, är inte alla datorer vakna och redo att prata hela tiden. Vissa datorer är:
- **Vakna och vill prata** (som när du är på lekplatsen)
- **Sovande** (som när du sover på natten)
- **Inte hemma** (som när du är på semester)

#### 4. Vad betyder det att "scanna"?

Att scanna är som att lysa med en ficklampa på alla hus i ditt kvarter för att se vilka som har lamporna tända! När du ser ett upplyst fönster vet du att någon är hemma och vaken.

**Nmap är den magiska ficklampan!** Det är ett verktyg som lyser på alla datorer i ett nätverk för att se:
- Vilka datorer som är vakna
- Vilka som vill prata
- Vad de vill prata om

#### 5. Meddelanden reser som brev

När en dator ska prata med en annan, packar den sitt meddelande i ett "brev" (vi kallar det ett *paket* senare). Brevet har:
- **Avsändare** (vilken dator som skickar)
- **Mottagare** (vilken dator som ska få det)
- **Meddelande** (vad datorn vill säga)

Sedan reser brevet på vägarna (nätverket) tills det kommer fram!

### Exempel

#### Exempel 1: Netflix och fjärrdatorn

När du vill titta på en film på Netflix:

1. **Din dator säger**: "Hej Netflix-dator! Kan jag få filmen om lejon?"
2. **Netflix-dator svarar**: "Javisst! Här kommer första delen!"
3. **Din dator tar emot**: Filmen börjar spelas
4. **De fortsätter prata**: Netflix skickar mer och mer av filmen medan du tittar

De pratar hela tiden när du kollar på filmen!

#### Exempel 2: Lekplatsen med kompisar

Föreställ dig en lekplats där du har många kompisar. Du vill veta vilka kompisar som är där idag.

**Utan "skanning"**: Du måste gå runt och leta efter varje kompis en och en. Det tar lång tid!

**Med "skanning"**: Du står på en hög klätterställning och ropar "Finns det någon här?" – då svarar alla kompisar som är där! Nu vet du direkt vilka som är på lekplatsen.

Nmap gör samma sak med datorer!

#### Exempel 3: Ett hus med många dörrar

Tänk dig ett stort hus med många, många dörrar – 65535 dörrar för att vara exakt! (Vi kommer lära oss varför senare.)

- Vissa dörrar är **öppna** – någon tittar ut och vill prata
- Vissa dörrar är **stängda** – ingen hemma där
- Vissa dörrar är **låsta** – de vill inte prata med främlingar

När Nmap scannar en dator är det som att gå fram till huset och försiktigt knacka på dörrarna för att se vilka som är öppna. Om någon öppnar och säger "Hej!", då vet Nmap att den dörren är öppen.

### Visualisering: ASCII-diagram

```
DIN DATOR                              ANNAN DATOR
+---------+                            +---------+
|  😊     |                            |  😊     |
|  Du     |                            | Netflix |
+---------+                            +---------+
     |                                      |
     |  "Kan jag få en film?"              |
     |------------------------------------->|
     |                                      |
     |      "Här kommer filmen!"           |
     |<-------------------------------------|
     |                                      |
```

### 💡 Pro Tips

#### Pro Tip 1: Fråga alltid om lov först!

Precis som du inte lyser med en riktig ficklampa in i grannens fönster utan att fråga om lov, ska du **aldrig** använda Nmap för att scanna datorer som inte är dina egna utan att ha frågat först. Det är viktigt att vara snäll och respektfull!

#### Pro Tip 2: Alla meddelanden tar olika lång tid

Ibland svarar en dator direkt (som din kompis som står bredvid dig), och ibland tar det längre tid (som ett brev som ska skickas till ett annat land). Datorer långt borta tar längre tid att svara än datorer som är nära!

#### Pro Tip 3: Ju fler datorer, desto längre tid tar det

Om du ska kolla om 1 kompis är på lekplatsen går det snabbt. Om du ska kolla om 100 kompisar är där tar det längre tid! Samma sak med datorer – att scanna många datorer tar längre tid än att scanna några få.

### ✏️ Övningar

#### Övning 1: Rita ditt eget nätverk (lätt)

**Uppgift**: Ta fram ett papper och rita:
1. Rita ditt hus (din dator) som en fyrkant
2. Rita 3 andra hus runt omkring (andra datorer)
3. Rita vägar mellan husen (nätverket)
4. Markera vilket hus som är "vaken" genom att rita en sol ovanför

**Bonus**: Rita en person med en ficklampa (Nmap) som lyser på alla hus!

#### Övning 2: Tänk som ett meddelande (medel)

**Uppgift**: Föreställ dig att DU är ett meddelande som ska resa från din dator till Netflix-datorn för att hämta en film.

Beskriv din resa:
1. Var börjar du? (vilken dator)
2. Vad har du med dig? (meddelandet: "Jag vill ha film!")
3. Vilken väg tar du? (genom nätverket)
4. Vad händer när du kommer fram?
5. Vad tar du med dig tillbaka? (filmen)

**Diskussion**: Dela gärna din historia med någon vuxen eller kompis!

#### Övning 3: Huset med många dörrar (medel-svår)

**Uppgift**: Du står utanför ett hus med 10 dörrar.

För varje dörr, bestäm:
- Är dörren **öppen** (någon vill prata)?
- Är dörren **stängd** (ingen hemma)?
- Är dörren **låst** (vill inte prata med främlingar)?

Exempel:
- Dörr 1: Öppen – där bor en webbsida
- Dörr 2: Stängd – ingen hemma
- Dörr 3: Låst – hemlig dörr
- osv.

**Reflektion**: Om du var Nmap, hur skulle du veta vilka dörrar som är öppna? (Tips: Du knackar och lyssnar om någon svarar!)

### 📝 Sammanfattning

**Vad du har lärt dig:**

- ✅ Datorer kan prata med varandra precis som människor
- ✅ Ett nätverk är som vägar mellan hus (datorer)
- ✅ Meddelanden reser som brev mellan datorer
- ✅ Nmap är som en magisk ficklampa som visar vilka datorer som är vakna
- ✅ Att scanna betyder att kolla vilka datorer som är uppe och vill prata
- ✅ Man måste alltid fråga om lov innan man scannar någon annans datorer

**Nya ord du lärt dig:**
- **Nätverk**: Vägar mellan datorer så de kan prata med varandra
- **Scanna**: Kolla vilka datorer som är vakna och vill prata
- **Nmap**: Ett verktyg (som en ficklampa) för att scanna nätverk
- **Meddelande**: Vad datorer säger till varandra

**Nästa steg:**

I nästa nivå kommer vi börja använda riktiga ord som "IP-adress" och "port", och du får lära dig dina första Nmap-kommandon! Vi kommer fortsätta bygga på det du lärt dig här – allt handlar fortfarande om datorer som pratar med varandra, men vi kommer gå djupare.

**Bra jobbat! 🌟** Du har nu grunderna på plats. Ta en paus, låt det sjunka in, och fortsätt när du känner dig redo!

---

## Nivå 2: IP-adresser, Portar & Första Nmap-kommandot 🧒

### Introduktion

Nu när du förstår grunderna om att datorer pratar med varandra är det dags att lära dig de riktiga orden som nätverkstekniker använder! På denna nivå kommer du lära dig om IP-adresser (husnummer för datorer), portar (dörrnummer), och du kommer köra dina första riktiga Nmap-kommandon. Detta är spännande – du kommer faktiskt använda verktyget! Men kom ihåg: scanna bara ditt eget nätverk.

### Kärnkoncept

#### 1. IP-adress – Husnummer för datorer

Precis som varje hus på en gata har ett unikt husnummer (Storgatan 5, Lilla vägen 12 osv.), har varje dator på ett nätverk en unik **IP-adress** (IP står för Internet Protocol).

**Så här ser en IP-adress ut:**
- `192.168.0.1`
- `10.0.0.5`
- `172.16.0.100`

En IP-adress består av **fyra siffror** separerade med punkter. Varje siffra kan vara mellan 0 och 255.

**Varför är IP-adresser viktiga?**
För att din dator ska kunna skicka ett meddelande till Netflix-datorn måste den veta Netflix-datorns IP-adress – precis som du måste veta din kompis adress för att skicka ett brev!

**Exempel:**
- Din dator hemma kanske har IP-adressen: `192.168.0.10`
- Din routers IP-adress är ofta: `192.168.0.1`
- Google har IP-adressen: `8.8.8.8` (en av dem)

#### 2. Portar – Dörrnummer på datorer

Kommer du ihåg huset med 65535 dörrar från förra nivån? Varje dörr kallas för en **port**!

En port är som ett dörrnummer. En dator kan göra många olika saker samtidigt (visa webbsidor, ta emot e-post, spela spel), och varje tjänst använder sin egen port.

**Vanliga portar:**
- **Port 80**: Här bor webbsidor (HTTP)
- **Port 443**: Här bor säkra webbsidor (HTTPS)
- **Port 22**: Här bor SSH (för att fjärrstyra datorer)
- **Port 25**: Här bor e-post (SMTP)
- **Port 3389**: Här bor Fjärrskrivbord (Windows)

**Tänk så här:**
- IP-adress = Husnummer: "Storgatan 5"
- Port = Dörrnummer: "Lägenhet 80"
- Tillsammans = Exakt plats: "Storgatan 5, Lägenhet 80"

**I datornätverksspråk:**
- IP-adress = `192.168.0.10`
- Port = `80`
- Tillsammans = `192.168.0.10:80` (webbservern på den datorn)

#### 3. LAN vs WAN – Hemmanätverket vs hela internet

**LAN (Local Area Network)** = Ditt lokala nätverk
- Det är som ditt kvarter – alla datorer hemma hos dig
- Dator, telefon, surfplatta, TV, skrivare – alla i samma "kvarter"
- Använder IP-adresser som börjar med `192.168.x.x` eller `10.x.x.x`

**WAN (Wide Area Network)** = Internet
- Det är som hela världen – alla datorer överallt
- Netflix, Google, Facebook – alla stora tjänster finns här
- Använder alla möjliga IP-adresser

**Router** = Porten ut från ditt kvarter till världen
- Routern är som en vakt som låter meddelanden in och ut
- Den har en IP-adress inåt (mot ditt hem): ofta `192.168.0.1`
- Och en IP-adress utåt (mot internet): din "publika IP"

#### 4. Ping – Är du där?

Innan du scannar med Nmap är det bra att veta om en dator ens är uppe och svarar. Det gör du med **ping**!

Ping är som att ropa "Hallå, är du där?" och vänta på svar.

**Exempel:**
```bash
ping 192.168.0.1
```

Om datorn är uppe får du tillbaka:
```
Reply from 192.168.0.1: time=2ms
```

Om datorn är nere får du ingen respons (eller "Request timed out").

**Vad betyder "time=2ms"?**
Det betyder att det tog 2 millisekunder (0,002 sekunder) för meddelandet att gå fram och tillbaka. Snabbt!

#### 5. Vad är en "tjänst" eller "service"?

När en port är öppen betyder det att en **tjänst** lyssnar där. En tjänst är ett program som väntar på att någon ska prata med det.

**Exempel:**
- En webbserver (Apache, Nginx) lyssnar på port 80
- En SSH-server lyssnar på port 22
- En Minecraft-server lyssnar på port 25565

Nmap's jobb är att kolla vilka portar som är öppna och, om möjligt, gissa vilken tjänst som finns där!

#### 6. Subnät och CIDR-notation

När du ska scanna hela ditt hemnätverk vill du inte skriva alla IP-adresser en efter en. Istället använder du **CIDR-notation**.

**Exempel:**
- `192.168.0.0/24` betyder: Alla IP-adresser från `192.168.0.0` till `192.168.0.255` (256 adresser)
- `10.0.0.0/8` betyder: Alla IP-adresser från `10.0.0.0` till `10.255.255.255` (16 miljoner adresser!)

**/24** är det vanligaste för hemnätverk – det ger dig plats för 254 enheter (0 och 255 är reserverade).

**Varför är detta viktigt?**
När du kör Nmap kan du säga:
```bash
nmap 192.168.0.0/24
```
Då scannar Nmap **alla** datorer i ditt hemnätverk på en gång!

### Exempel

#### Exempel 1: Hitta din egen IP-adress

**På Windows:**
1. Öppna Kommandotolken (CMD)
2. Skriv: `ipconfig`
3. Leta efter "IPv4 Address" – där står din IP!

**På Mac/Linux:**
1. Öppna Terminal
2. Skriv: `ifconfig` eller `ip addr`
3. Leta efter din IP-adress under din nätverksadapter

**Vad du ser:**
```
IPv4 Address: 192.168.0.15
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.0.1
```

- **Din IP**: `192.168.0.15`
- **Din router** (gateway): `192.168.0.1`
- **Ditt nätverk**: `192.168.0.0/24`

#### Exempel 2: Ditt första Nmap-kommando – Scanna en enskild dator

Nu kör vi! Låt oss scanna din router för att se vilka portar som är öppna.

**Kommando:**
```bash
nmap 192.168.0.1
```

**Vad händer:**
1. Nmap skickar meddelanden till alla vanliga portar på 192.168.0.1
2. Den lyssnar på svar
3. Den visar vilka portar som är öppna

**Exempel på resultat:**
```
Starting Nmap scan...
Nmap scan report for 192.168.0.1
Host is up (0.0023s latency).

PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
443/tcp  open     https
8080/tcp filtered http-proxy

Nmap done: 1 IP address (1 host up) scanned in 2.45 seconds
```

**Vad betyder det här?**
- **Host is up**: Datorn (routern) svarar!
- **22/tcp open ssh**: Port 22 är öppen, och det finns SSH där
- **80/tcp open http**: Port 80 är öppen, det finns en webbserver
- **443/tcp open https**: Port 443 är öppen, säker webbserver
- **8080/tcp filtered**: Port 8080 blockeras av en brandvägg

#### Exempel 3: Scanna hela ditt hemnätverk

Nu blir det intressant! Låt oss hitta ALLA datorer i ditt hemnätverk.

**Kommando:**
```bash
nmap 192.168.0.0/24
```

**Vad händer:**
Nmap scannar alla IP-adresser från `192.168.0.1` till `192.168.0.254` (254 möjliga datorer).

**Exempel på resultat:**
```
Nmap scan report for 192.168.0.1
Host is up (0.0023s latency).
PORT   STATE SERVICE
80/tcp open  http

Nmap scan report for 192.168.0.10
Host is up (0.015s latency).
PORT     STATE SERVICE
22/tcp   open  ssh
3389/tcp open  ms-wbt-server

Nmap scan report for 192.168.0.15
Host is up (0.0019s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE
445/tcp open  microsoft-ds

Nmap done: 254 IP addresses (3 hosts up) scanned in 18.42 seconds
```

**Vad ser vi?**
- **3 datorer är uppe** av 254 möjliga
- `192.168.0.1` har en webbserver (routern)
- `192.168.0.10` har SSH och Fjärrskrivbord (kanske en Linux-server?)
- `192.168.0.15` har Windows-fildelning (din dator kanske?)

### Visualisering: ASCII-diagram

#### Diagram 1: Ditt hemnätverk

```
                    INTERNET
                        |
                        |
                   [ROUTER]
                 192.168.0.1
                        |
          +-------------+-------------+
          |             |             |
     [DIN DATOR]   [TELEFON]      [TV]
    192.168.0.10  192.168.0.15  192.168.0.20
```

#### Diagram 2: Datorer med olika portar öppna

```
   DATOR: 192.168.0.10
   +-------------------+
   | Port 22:  SSH     | ← ÖPPEN
   | Port 80:  HTTP    | ← ÖPPEN
   | Port 443: HTTPS   | ← ÖPPEN
   | Port 3389: RDP    | ← STÄNGD
   | Port 8080: Proxy  | ← FILTRERAD (brandvägg)
   | ...               |
   | Port 65535: ?     | ← STÄNGD
   +-------------------+
```

#### Diagram 3: Hur Nmap kommunicerar

```
    NMAP (din dator)              MÅLSERVER
         |                            |
         | "Hallå, är port 80 öppen?" |
         |--------------------------->|
         |                            |
         |    "Ja, jag lyssnar här!"  |
         |<---------------------------|
         |                            |
         | Nmap noterar: Port 80 OPEN |
```

### 💡 Pro Tips

#### Pro Tip 1: Skillnaden mellan "open", "closed" och "filtered"

När Nmap scannar får du tre olika svar:

- **open**: Porten är öppen, en tjänst lyssnar där → "Någon är hemma och dörren är öppen!"
- **closed**: Porten är stängd, ingen tjänst lyssnar → "Ingen hemma, men huset svarar"
- **filtered**: Brandvägg blockerar → "Kan inte nå dörren, det finns ett staket i vägen"

**Varför är detta viktigt?**
- **Open** = intressant! Här kanske det finns något att undersöka eller skydda
- **Closed** = datorn är uppe men tjänsten körs inte
- **Filtered** = någon blockerar aktivt, ofta en brandvägg

#### Pro Tip 2: Använd alltid sudo/administratörsrättigheter för bästa resultat

För att Nmap ska kunna göra alla typer av scanningar behöver det ofta administratörsrättigheter:

**Linux/Mac:**
```bash
sudo nmap 192.168.0.1
```

**Windows:**
Kör Kommandotolken som Administratör

**Varför?**
Vissa scan-tekniker kräver att Nmap kan skicka speciella nätverkspaket, vilket bara administratörer kan göra.

#### Pro Tip 3: Skillnad mellan att scanna ditt LAN och internet

**Aldrig scanna internet utan tillstånd!** Det är skillnad:

✅ **OK att scanna:**
- Din egen dator: `nmap 127.0.0.1` eller `nmap localhost`
- Ditt eget hemnätverk: `nmap 192.168.0.0/24`
- Din egen server (om du har en)

❌ **INTE OK att scanna:**
- Andras webbplatser: `nmap google.com` ← OLAGLIGT utan tillstånd!
- Slumpmässiga IP-adresser på internet
- Ditt företags nätverk (utan IT-avdelningens tillstånd)

#### Pro Tip 4: Vanliga missförstånd

**Missförstånd 1**: "Om alla portar är stängda är jag säker!"
- **Sanning**: Även stängda portar kan ha sårbarheter i operativsystemet. Säkerhet är lager på lager.

**Missförstånd 2**: "Öppna portar = hackad!"
- **Sanning**: Öppna portar är normalt. En webbserver MÅSTE ha port 80/443 öppen för att fungera. Det viktiga är att tjänsterna är säkra och uppdaterade.

**Missförstånd 3**: "Nmap hackar datorer!"
- **Sanning**: Nmap SCANNAR bara. Det är som att kolla vilka fönster som lyser – det gör ingen skada. Men använd det bara på dina egna system!

### ✏️ Övningar

#### Övning 1: Hitta din IP-adress (lätt)

**Uppgift:**
1. Öppna Kommandotolken (Windows) eller Terminal (Mac/Linux)
2. Kör `ipconfig` (Windows) eller `ifconfig` (Mac/Linux)
3. Skriv ner din IP-adress, subnet mask och default gateway

**Förklara:**
- Vad är din IP-adress?
- Vad är din routers IP-adress (gateway)?
- Vilket nätverk tillhör du? (Skriv i CIDR-notation som 192.168.0.0/24)

#### Övning 2: Ping din router (lätt-medel)

**Uppgift:**
1. Hitta din routers IP (oftast 192.168.0.1 eller 192.168.1.1)
2. Kör: `ping 192.168.0.1` (eller din routers IP)
3. Studera resultatet

**Förklara:**
- Hur lång tid tar det för paketen att gå fram och tillbaka? (titta på "time=")
- Är tiden konsekvent eller varierar den?
- Vad betyder "TTL"? (Tips: Time To Live – hur många hopp ett paket kan göra)

#### Övning 3: Installera Nmap (medel)

**Uppgift:**
Installera Nmap på din dator.

**Windows:**
- Ladda ner från nmap.org
- Kör installationsprogrammet
- Välj "Add Nmap to PATH" under installationen

**Mac:**
```bash
brew install nmap
```
(Kräver Homebrew – installera det först om du inte har det)

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install nmap
```

**Testa:**
```bash
nmap --version
```

Du ska se något som: `Nmap version 7.96`

#### Övning 4: Scanna din egen dator (medel)

**Uppgift:**
Scanna din egen dator för att se vilka portar DU har öppna.

**Kommando:**
```bash
nmap 127.0.0.1
```
eller
```bash
nmap localhost
```

**Förklara:**
- Vilka portar är öppna på din dator?
- Vet du vilka tjänster som kör på dessa portar?
- Är det något oväntat?

**Exempel på vad du kan se:**
```
PORT     STATE SERVICE
22/tcp   open  ssh       ← Du kör SSH-server
80/tcp   open  http      ← Du kör en webbserver
3306/tcp open  mysql     ← Du kör MySQL-databas
```

#### Övning 5: Scanna hela ditt hemnätverk (medel-svår)

**VARNING**: Scanna bara ditt EGET hemnätverk! Inte företagets WiFi, inte någon annans nätverk.

**Uppgift:**
1. Bekräfta att du är hemma på ditt eget WiFi
2. Hitta ditt nätverk i CIDR-notation (t.ex. 192.168.0.0/24)
3. Kör: `nmap 192.168.0.0/24`

**Förklara:**
- Hur många enheter hittade Nmap?
- Kan du gissa vilka enheter det är? (router, dator, telefon, TV, etc.)
- Vilka portar är vanligast öppna?

**Bonus:**
Försök matcha IP-adresser med faktiska enheter. Tips: Din router har ofta en webbsida där du kan se anslutna enheter!

#### Övning 6: Förklara för en kompis (medel)

**Uppgift:**
Förklara för en kompis (eller förälder) vad följande betyder:

1. IP-adress
2. Port
3. Vad Nmap gör
4. Varför det är viktigt att bara scanna sina egna system

**Kriterier för lyckat resultat:**
Din kompis ska kunna förklara tillbaka grunderna med egna ord!

**Tips:**
Använd analogierna från guiden:
- IP-adress = husnummer
- Port = dörrnummer
- Nmap = ficklampa som visar vilka som är hemma

#### Övning 7: Bonus-utmaning – Testa olika IP-adresser (svår)

**Uppgift:**
Testa att scanna olika enheter i ditt nätverk en efter en.

**Steg:**
1. Lista alla IP-adresser som är uppe (från övning 5)
2. För varje IP, kör: `nmap [IP-adress]`
3. Dokumentera resultaten i en tabell:

| IP-adress    | Enhet (gissning) | Öppna portar | Tjänster      |
|--------------|------------------|--------------|---------------|
| 192.168.0.1  | Router           | 80, 443      | Webbserver    |
| 192.168.0.10 | Min dator        | 22, 445      | SSH, Fildelning|
| 192.168.0.15 | Telefon          | Inga         | Ingen         |

**Reflektion:**
- Fanns det någon överraskning?
- Har du enheter med portar öppna som du inte visste om?
- Vilken enhet har flest öppna portar?

### 📝 Sammanfattning

**Vad du har lärt dig:**

- ✅ IP-adresser är som husnummer för datorer (t.ex. 192.168.0.10)
- ✅ Portar är som dörrnummer på ett hus (t.ex. port 80 för webbservrar)
- ✅ LAN är ditt lokala nätverk, WAN är hela internet
- ✅ Routern är porten mellan ditt hem och internet
- ✅ Ping kollar om en dator är uppe och svarar
- ✅ Nmap kan scanna en enskild dator eller hela nätverk
- ✅ CIDR-notation (som 192.168.0.0/24) beskriver många IP-adresser på en gång
- ✅ Portar kan vara open, closed eller filtered
- ✅ Du får BARA scanna dina egna system

**Nya ord du lärt dig:**

- **IP-adress**: Unikt nummer som identifierar en dator på ett nätverk
- **Port**: Ett nummer (0-65535) som identifierar en tjänst på en dator
- **LAN (Local Area Network)**: Ditt lokala nätverk (hemma, på kontoret)
- **WAN (Wide Area Network)**: Internet, stora nätverk
- **Router**: Enhet som kopplar ihop LAN med WAN
- **Ping**: Kommando för att kolla om en dator svarar
- **Tjänst/Service**: Program som lyssnar på en port (webbserver, SSH, etc.)
- **CIDR-notation**: Sätt att beskriva många IP-adresser (t.ex. /24)
- **Open port**: En port där en tjänst lyssnar och svarar
- **Closed port**: En port som inte har någon tjänst
- **Filtered port**: En port som blockeras av brandvägg

**Viktiga kommandon du lärt dig:**

```bash
# Hitta din IP
ipconfig              # Windows
ifconfig / ip addr    # Mac/Linux

# Ping en dator
ping 192.168.0.1

# Nmap-kommandon
nmap 127.0.0.1              # Scanna dig själv
nmap 192.168.0.1            # Scanna routern
nmap 192.168.0.0/24         # Scanna hela nätverket
nmap --version              # Kolla Nmap-version
```

**Nästa steg:**

I nästa nivå går vi MYCKET djupare! Du kommer lära dig:
- Hur TCP/IP-protokollet faktiskt fungerar under huven
- Vad TCP, UDP och ICMP är
- Den berömda "3-way handshake"
- Olika typer av Nmap-scanningar (SYN-scan, TCP-scan, UDP-scan)
- Hur Nmap verkligen kommunicerar med datorer

Det blir mer tekniskt, men också mycket mer kraftfullt. Du kommer förstå exakt VAD som händer när du kör Nmap!

**Utmärkt jobbat! 🎉** Du har nu kört dina första Nmap-scanningar och förstår grunderna om IP-adresser och portar. Ta gärna en paus och experimentera lite med övningarna innan du går vidare!

---

## Nivå 3: Så Fungerar Internet på Riktigt 🎓

### Introduktion

Välkommen till den tekniska nivån! Här slutar vi med analogier och börjar prata om hur internet FAKTISKT fungerar under huven. Du kommer lära dig om TCP/IP-stacken, hur datorer etablerar anslutningar, och exakt vad Nmap gör när det scannar. Efter denna nivå kommer du förstå inte bara HUR man kör Nmap, utan VARFÖR olika scan-tekniker fungerar som de gör. Detta är där det blir riktigt spännande!

### Kärnkoncept

#### 1. TCP/IP-stacken – Hur meddelanden paketeras

När du skickar ett meddelande över internet händer mycket bakom kulisserna. Meddelandet delas upp och packas i flera lager, lite som ryska dockor (matrioshka-dockor) där varje lager lägger till sin egen information.

**TCP/IP-modellen har 4 lager:**

```
┌─────────────────────────────────────┐
│  4. Application Layer (Program)     │  ← HTTP, SSH, DNS (vad du vill göra)
├─────────────────────────────────────┤
│  3. Transport Layer (Transport)     │  ← TCP, UDP (hur data ska skickas)
├─────────────────────────────────────┤
│  2. Internet Layer (Nätverk)        │  ← IP (var data ska)
├─────────────────────────────────────┤
│  1. Link Layer (Fysisk/Länk)        │  ← Ethernet, WiFi (kablar och vågor)
└─────────────────────────────────────┘
```

**Enklare förklaring:**
1. **Application Layer**: Du vill besöka en webbsida (HTTP)
2. **Transport Layer**: Data delas upp i bitar och TCP ser till att allt kommer fram
3. **Internet Layer**: IP-adresser bestämmer vart det ska
4. **Link Layer**: Faktiskt sändande över WiFi eller kabel

**Jämför med OSI-modellen:**
OSI-modellen har 7 lager (mer detaljerad), men TCP/IP-modellen med 4 lager är enklare och vad som används i praktiken.

#### 2. IP (Internet Protocol) – Adressering och routing

**IP** (Internet Protocol) ansvarar för att få paket från punkt A till punkt B. Det är som postens adresssystem.

**Ett IP-paket innehåller:**
- **Source IP** (avsändare): Din dators IP
- **Destination IP** (mottagare): Målets IP
- **Data**: Själva innehållet
- **TTL** (Time To Live): Hur många "hopp" paketet får göra innan det kastas bort

**IPv4 vs IPv6:**
- **IPv4**: `192.168.0.1` – 4 siffror, cirka 4 miljarder adresser (nästan slut!)
- **IPv6**: `2001:0db8:85a3::8a2e:0370:7334` – enormt mycket fler adresser

#### 3. TCP (Transmission Control Protocol) – Pålitlig kommunikation

**TCP** är ett protokoll som garanterar att data kommer fram i rätt ordning och utan fel. Det är som ett rekommenderat brev med kvittens.

**TCP-egenskaper:**
- **Connection-oriented**: Först upprättas en anslutning
- **Reliable**: Om något går förlorat skickas det om
- **Ordered**: Data kommer i rätt ordning
- **Error-checked**: Felkontroll inbyggd

**Används för:**
- Webbsidor (HTTP/HTTPS)
- E-post (SMTP, IMAP)
- Filöverföring (FTP, SSH)
- Allt där varje bit är viktig

#### 4. TCP 3-Way Handshake – Hur anslutningar startas

Detta är MYCKET viktigt för att förstå hur Nmap fungerar!

När två datorer ska prata via TCP måste de först "skaka hand" – detta kallas **3-way handshake**.

**Steg 1: SYN (Synchronize)**
- Klient: "Hej, jag vill prata! Här är mitt sekvensnummer."
- Skickar ett SYN-paket

**Steg 2: SYN-ACK (Synchronize-Acknowledge)**
- Server: "OK, jag hörde dig! Här är MITT sekvensnummer, och jag bekräftar ditt."
- Skickar tillbaka SYN-ACK

**Steg 3: ACK (Acknowledge)**
- Klient: "Perfekt, jag bekräftar ditt nummer. Nu kan vi prata!"
- Skickar ACK

**Nu är anslutningen etablerad och data kan skickas!**

```
KLIENT                        SERVER
   |                             |
   | SYN (Seq=100)              |
   |--------------------------->|
   |                             |
   |        SYN-ACK (Seq=200,   |
   |         Ack=101)            |
   |<---------------------------|
   |                             |
   | ACK (Ack=201)              |
   |--------------------------->|
   |                             |
   | ← ANSLUTNING ETABLERAD →  |
   |                             |
```

**Varför är detta viktigt?**
Nmap utnyttjar denna process för att avgöra om portar är öppna!

#### 5. UDP (User Datagram Protocol) – Snabb men opålitlig

**UDP** är som att skicka vykort istället för rekommenderade brev. Snabbt men ingen garanti.

**UDP-egenskaper:**
- **Connectionless**: Ingen handshake, bara skicka!
- **Unreliable**: Om något försvinner, tough luck
- **Fast**: Ingen overhead med kvitteringar
- **No ordering**: Paket kan komma i fel ordning

**Används för:**
- DNS-förfrågningar (snabba uppslag)
- Videostreaming (tappade paket = liten glitch, inte problem)
- Online-spel (snabbhet viktigare än perfekt data)
- VoIP (röstsamtal över internet)

**Skillnad TCP vs UDP:**
```
TCP: "Hej! Fick du mitt meddelande?" "Ja!" "Bra, här kommer nästa!"
UDP: "HEJ!" "HEJ!" "HEJ!" (ingen väntar på svar)
```

#### 6. ICMP (Internet Control Message Protocol) – Felmeddelanden

**ICMP** används för diagnostik och felmeddelanden. Det är inte för att skicka data, utan för att rapportera problem.

**Vanliga ICMP-meddelanden:**
- **Echo Request/Reply**: Det som `ping` använder
- **Destination Unreachable**: "Kan inte nå den datorn"
- **Time Exceeded**: "Paketet hoppade för många gånger (TTL=0)"

**Exempel:**
När du kör `ping 8.8.8.8` skickar du ett **ICMP Echo Request** och får tillbaka ett **ICMP Echo Reply**.

#### 7. Portar och Socket

En **socket** är kombinationen av IP-adress + port + protokoll.

**Exempel:**
- `192.168.0.10:80/TCP` = Socket för webbserver
- `8.8.8.8:53/UDP` = Socket för DNS

**Port-kategorier:**
- **0-1023**: Well-known ports (HTTP=80, HTTPS=443, SSH=22)
- **1024-49151**: Registered ports (MySQL=3306, PostgreSQL=5432)
- **49152-65535**: Dynamic/private ports (tillfälliga anslutningar)

### Nmap Scan-typer – Hur fungerar de?

Nu när du förstår TCP/UDP kan vi förklara hur Nmap faktiskt scannar!

#### Scan-typ 1: TCP Connect Scan (-sT)

**Vad det gör:**
Genomför en FULL 3-way handshake med varje port.

**Hur det fungerar:**
```
NMAP                          MÅLSERVER (port 80)
  |                                |
  | SYN                           |
  |------------------------------>| Port öppen?
  |                                |
  | SYN-ACK                       |
  |<------------------------------| JA! Port är OPEN
  |                                |
  | ACK                           |
  |------------------------------>|
  |                                |
  | RST (Reset - stäng)           |
  |------------------------------>| Nmap avbryter
```

**Om porten är stängd:**
```
NMAP                          MÅLSERVER (port 9999)
  |                                |
  | SYN                           |
  |------------------------------>|
  |                                |
  | RST-ACK                       |
  |<------------------------------| Port är CLOSED
```

**Kommando:**
```bash
nmap -sT 192.168.0.10
```

**För- och nackdelar:**
- ✅ **Fördel**: Fungerar utan root/admin-rättigheter
- ✅ **Fördel**: Fungerar alltid (OS tar hand om anslutningen)
- ❌ **Nackdel**: Lätt att logga (full anslutning upprättas)
- ❌ **Nackdel**: Långsammare än SYN-scan

**Resultat:**
- **open**: Servern svarar med SYN-ACK
- **closed**: Servern svarar med RST-ACK
- **filtered**: Ingen respons (brandvägg)

#### Scan-typ 2: SYN Scan / Stealth Scan (-sS)

**Vad det gör:**
Genomför BARA första steget av handshake (skickar SYN, lyssnar på svar, avbryter).

**Hur det fungerar:**
```
NMAP                          MÅLSERVER (port 80)
  |                                |
  | SYN                           |
  |------------------------------>|
  |                                |
  | SYN-ACK                       |
  |<------------------------------| Port är OPEN!
  |                                |
  | RST (AVBRYT!)                 |
  |------------------------------>| Aldrig fullföljer anslutning
```

**Varför kallas det "stealth"?**
Eftersom anslutningen aldrig fullföljs loggas det inte alltid av enkla system (men moderna IDS/IPS upptäcker det ändå).

**Kommando:**
```bash
sudo nmap -sS 192.168.0.10
```

**Kräver sudo/admin** eftersom Nmap måste skapa råa paket.

**För- och nackdelar:**
- ✅ **Fördel**: Snabbare än TCP Connect
- ✅ **Fördel**: Standard-scan i Nmap (om du kör med sudo)
- ✅ **Fördel**: Mindre påträngande
- ❌ **Nackdel**: Kräver root/admin
- ❌ **Nackdel**: Kan ändå upptäckas av moderna system

**Resultat:**
- **open**: SYN-ACK tas emot
- **closed**: RST tas emot
- **filtered**: Ingen respons eller ICMP unreachable

#### Scan-typ 3: UDP Scan (-sU)

**Vad det gör:**
Skickar UDP-paket till portar för att se om de svarar.

**Hur det fungerar:**
```
NMAP                          MÅLSERVER (port 53)
  |                                |
  | UDP packet                    |
  |------------------------------>|
  |                                |
  | UDP response (eller inget)    |
  |<------------------------------| Port OPEN (kanske)
```

**Om porten är stängd:**
```
NMAP                          MÅLSERVER (port 9999)
  |                                |
  | UDP packet                    |
  |------------------------------>|
  |                                |
  | ICMP Port Unreachable         |
  |<------------------------------| Port är CLOSED
```

**Kommando:**
```bash
sudo nmap -sU 192.168.0.10
```

**Varför är UDP-scanning svår?**
- **Ingen handshake**: Du vet inte om paketet kom fram
- **Ingen respons = öppen eller filtrerad**: Svårt att avgöra
- **LÅNGSAM**: Nmap måste vänta på timeout för varje port som inte svarar

**För- och nackdelar:**
- ✅ **Fördel**: Hittar UDP-tjänster (DNS, SNMP, DHCP)
- ❌ **Nackdel**: MYCKET långsam
- ❌ **Nackdel**: Svår att tolka resultat (open|filtered)

**Resultat:**
- **open**: UDP-svar tas emot
- **closed**: ICMP Port Unreachable
- **open|filtered**: Ingen respons (kan vara brandvägg ELLER öppen port)

#### Scan-typ 4: Version Detection (-sV)

**Vad det gör:**
Efter att ha hittat öppna portar försöker Nmap avgöra VILKEN tjänst och VERSION som körs.

**Hur det fungerar:**
1. Nmap ansluter till porten
2. Skickar olika "probes" (testmeddelanden)
3. Analyserar svaren
4. Jämför med sin databas av tjänster

**Kommando:**
```bash
nmap -sV 192.168.0.10
```

**Exempel på resultat:**
```
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.52 ((Ubuntu))
3306/tcp open mysql   MySQL 8.0.32
```

**För- och nackdelar:**
- ✅ **Fördel**: Ger mycket information
- ✅ **Fördel**: Kan identifiera sårbara versioner
- ❌ **Nackdel**: Långsammare (fler probes)
- ❌ **Nackdel**: Mer "högljudd" (lättare att upptäcka)

#### Scan-typ 5: OS Detection (-O)

**Vad det gör:**
Försöker gissa vilket operativsystem som körs på målet.

**Hur det fungerar:**
Nmap skickar speciella paket och analyserar hur OS:et svarar. Olika OS implementerar TCP/IP lite olika!

**Kommando:**
```bash
sudo nmap -O 192.168.0.10
```

**Exempel på resultat:**
```
Running: Linux 5.X
OS CPE: cpe:/o:linux:linux_kernel:5
OS details: Linux 5.4 - 5.10
```

**Kräver minst 1 öppen och 1 stängd port** för att fungera bra.

#### Scan-typ 6: Nmap Scripting Engine (NSE) (--script)

**Vad det gör:**
Kör automatiserade scripts för att hitta sårbarheter, extrahera information, etc.

**Kategorier av scripts:**
- **default**: Säkra, snabba, informativa scripts
- **discovery**: Hitta mer information om nätverket
- **vuln**: Leta efter sårbarheter
- **auth**: Testa autentisering
- **safe**: Säkra att köra (crashar inte tjänster)
- **intrusive**: Aggressiva (kan påverka tjänster)

**Kommandon:**
```bash
# Kör default scripts
nmap --script default 192.168.0.10

# Kör alla vuln scripts
nmap --script vuln 192.168.0.10

# Kör specifikt script
nmap --script http-title 192.168.0.10
```

**Exempel:**
```bash
nmap --script http-title 192.168.0.10 -p 80
```

**Resultat:**
```
PORT   STATE SERVICE
80/tcp open  http
|_http-title: Welcome to my website!
```

### Visualisering: ASCII-diagram

#### Diagram 1: TCP 3-Way Handshake (öppen port)

```
  CLIENT (Nmap)                    SERVER (port 80)
       |                                 |
       | 1. SYN                         |
       | (Seq=1000, Flags=SYN)          |
       |-------------------------------->|
       |                                 | Port 80 lyssnar?
       |                                 | ✓ JA!
       |                                 |
       | 2. SYN-ACK                     |
       | (Seq=5000, Ack=1001,           |
       |  Flags=SYN+ACK)                |
       |<--------------------------------|
       |                                 |
       | Nmap: "Port är OPEN!"          |
       |                                 |
       | 3. ACK (eller RST)             |
       | (Ack=5001, Flags=ACK)          |
       |-------------------------------->|
       |                                 |
       |   [Anslutning etablerad]       |
       |                                 |
```

#### Diagram 2: SYN Scan vs Full Connect

```
┌─────────────────────────────────────────────────────────┐
│  SYN SCAN (-sS) - "Stealth"                            │
├─────────────────────────────────────────────────────────┤
│  Nmap           Server                                  │
│    |              |                                     │
│    | SYN          |                                     │
│    |------------->|                                     │
│    |              |                                     │
│    | SYN-ACK      |   ← Nmap ser: "OPEN!"             │
│    |<-------------|                                     │
│    |              |                                     │
│    | RST          |   ← Avbryter här!                  │
│    |------------->|                                     │
│    |              |                                     │
│  ALDRIG fullföljer anslutningen                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  FULL CONNECT (-sT)                                     │
├─────────────────────────────────────────────────────────┤
│  Nmap           Server                                  │
│    |              |                                     │
│    | SYN          |                                     │
│    |------------->|                                     │
│    |              |                                     │
│    | SYN-ACK      |                                     │
│    |<-------------|                                     │
│    |              |                                     │
│    | ACK          |   ← Fullföljer anslutning!         │
│    |------------->|                                     │
│    |              |                                     │
│    | FIN          |   ← Stänger anslutning snyggt      │
│    |------------->|                                     │
│    |              |                                     │
│  FULL anslutning (loggas ofta)                          │
└─────────────────────────────────────────────────────────┘
```

#### Diagram 3: TCP vs UDP från Nmaps perspektiv

```
┌─────────────────────────────────────────────────────────┐
│  TCP SCAN                                               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Nmap skickar: SYN                                      │
│                                                          │
│  Möjliga svar:                                          │
│  ┌─────────────────────────────────────────┐           │
│  │ SYN-ACK      → Port OPEN                │           │
│  │ RST          → Port CLOSED              │           │
│  │ Inget svar   → Port FILTERED (brandvägg)│           │
│  │ ICMP error   → Port FILTERED            │           │
│  └─────────────────────────────────────────┘           │
│                                                          │
│  TYDLIGA SVAR! Lätt att tolka.                         │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  UDP SCAN                                               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Nmap skickar: UDP packet                              │
│                                                          │
│  Möjliga svar:                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │ UDP svar    → Port OPEN                        │    │
│  │ ICMP Port   → Port CLOSED                      │    │
│  │  Unreachable                                   │    │
│  │ Inget svar  → Port OPEN|FILTERED (osäkert!)    │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
│  OTYDLIGT! Svårt att veta om port är öppen eller       │
│  om brandvägg blockerar.                                │
└─────────────────────────────────────────────────────────┘
```

### 💡 Pro Tips

#### Pro Tip 1: Förstå "filtered" vs "closed"

Ett av de vanligaste missförstånden:

- **closed**: Datorn är uppe och svarar, men INGEN tjänst lyssnar på porten
  - Exempel: Du har skickat SYN, datorn svarar "RST" (reset) = "Ingen hemma på den dörren"

- **filtered**: Paketet kom aldrig fram eller blockerades av brandvägg
  - Exempel: Du skickar SYN, inget svar alls = "Det finns ett staket, jag når inte dörren"

**Varför är detta viktigt?**
- **Många closed portar** = Normalt! Datorn är säker men svarar ärligt
- **Många filtered portar** = Brandvägg aktiv! Datorn är bakom skydd

#### Pro Tip 2: Kombinera scan-typer för bättre resultat

Du kan kombinera flera tekniker i samma kommando!

**Exempel:**
```bash
# SYN-scan + Version detection + Default scripts
sudo nmap -sS -sV --script default 192.168.0.10

# TCP + UDP scan tillsammans
sudo nmap -sS -sU 192.168.0.10

# Aggressiv scan (allt på en gång: OS, version, scripts, traceroute)
sudo nmap -A 192.168.0.10
```

**Varning:** `-A` (aggressiv scan) är väldigt högljudd och tar tid. Använd bara på egna system!

#### Pro Tip 3: Läs Nmap-output snabbt

När du får Nmap-resultat, fokusera på:

1. **Host is up** – Datorn svarar!
2. **Antal öppna portar** – "Not shown: 995 closed ports" = bara 5 portar är intressanta
3. **PORT/STATE/SERVICE** – Vilka tjänster är öppna
4. **VERSION** (om du kört -sV) – Finns det gamla, sårbara versioner?

**Exempel:**
```
Nmap scan report for 192.168.0.10
Host is up (0.00043s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 7.4 (protocol 2.0)
80/tcp   open  http       Apache httpd 2.4.6
3306/tcp open  mysql      MySQL 5.6.40

Nmap done: 1 IP address (1 host up) scanned in 8.52 seconds
```

**Snabb analys:**
- 3 tjänster öppna
- SSH (säkert fjärrinlogg)
- Webbserver (Apache)
- Databas (MySQL)
- VARNING: MySQL 5.6.40 är gammal! Kanske finns sårbarheter

### ✏️ Övningar

#### Övning 1: Förklara 3-way handshake med egna ord (lätt-medel)

**Uppgift:**
Förklara för en kompis hur TCP 3-way handshake fungerar utan att titta på guiden.

Använd analogier:
- Tänk på det som en konversation
- Vad säger varje sida?
- Varför behövs tre steg?

**Rätt svar:**
1. Klient: "Hej, kan vi prata?" (SYN)
2. Server: "Ja, jag hörde dig! Kan DU höra MIG?" (SYN-ACK)
3. Klient: "Ja, jag hör dig! Låt oss börja!" (ACK)

#### Övning 2: TCP vs UDP – När använder man vad? (medel)

**Uppgift:**
För varje tjänst, bestäm om den använder TCP eller UDP och varför:

1. Webbsida (HTTP)
2. Live-streaming (Twitch, YouTube Live)
3. DNS-uppslag
4. E-post (SMTP)
5. Online-spel (Fortnite, CS:GO)
6. Filnedladdning (BitTorrent)

**Facit:**
1. **TCP** – Varje bit av HTML måste komma fram korrekt
2. **UDP eller TCP** – UDP för live (snabbhet), TCP för inspelat (kvalitet)
3. **UDP** – Snabbhet viktigare, kan fråga igen om det misslyckas
4. **TCP** – E-post måste komma fram helt och korrekt
5. **UDP** – Snabbhet viktigare, tappat paket = liten lagspike
6. **TCP** – Filer måste vara kompletta och korrekta

#### Övning 3: Kör SYN scan på ditt nätverk (medel)

**Uppgift:**
Kör en SYN-scan på din router och jämför med en vanlig scan.

**Kommandon:**
```bash
# Vanlig scan (TCP Connect om inte sudo)
nmap 192.168.0.1

# SYN scan (kräver sudo)
sudo nmap -sS 192.168.0.1
```

**Förklara:**
- Var resultatet samma?
- Vilken var snabbare?
- Märkte du någon skillnad?

#### Övning 4: Version detection (medel)

**Uppgift:**
Kör version detection på en dator i ditt nätverk.

**Kommando:**
```bash
nmap -sV 192.168.0.10
```

**Analysera:**
- Vilka tjänster och versioner hittades?
- Är någon version gammal? (Googla tjänsten + version)
- Finns det sårbarheter i de gamla versionerna?

#### Övning 5: UDP-scanning (medel-svår)

**Uppgift:**
Testa att scanna vanliga UDP-portar.

**Kommando:**
```bash
# Scanna bara top 20 UDP-portar (annars tar det evigheter!)
sudo nmap -sU --top-ports 20 192.168.0.1
```

**Vanliga UDP-portar:**
- 53: DNS
- 67-68: DHCP
- 123: NTP (tidssynk)
- 161: SNMP
- 500: IKE (VPN)

**Förklara:**
- Hur lång tid tog UDP-scan jämfört med TCP?
- Fick du många "open|filtered" resultat?
- Varför är det svårt att veta säkert?

#### Övning 6: Tolka scan-resultat (medel-svår)

**Uppgift:**
Här är output från olika scans. Vad betyder de?

**Scan 1:**
```
PORT    STATE  SERVICE
80/tcp  open   http
443/tcp open   https
```

**Svar:** Webbserver med både HTTP och HTTPS.

**Scan 2:**
```
PORT     STATE    SERVICE
22/tcp   filtered ssh
80/tcp   filtered http
3389/tcp filtered ms-wbt-server
```

**Svar:** Brandvägg blockerar alla portar. Datorn kanske inte ens är uppe, eller så filtreras alla anslutningar.

**Scan 3:**
```
PORT      STATE  SERVICE
135/tcp   open   msrpc
139/tcp   open   netbios-ssn
445/tcp   open   microsoft-ds
3389/tcp  open   ms-wbt-server
```

**Svar:** Windows-dator med Fjärrskrivbord och fildelning öppen. Potentiellt sårbar om inte uppdaterad!

#### Övning 7: Experimentera med NSE scripts (svår)

**Uppgift:**
Testa Nmap Scripting Engine på ditt eget system.

**Kommandon:**
```bash
# Vilka scripts finns?
ls /usr/share/nmap/scripts/ | grep http

# Kör ett specifikt script
nmap --script http-title 192.168.0.1 -p 80

# Kör alla "safe" scripts
nmap --script safe 192.168.0.1
```

**Utforska:**
- Vilka scripts finns tillgängliga?
- Vad gör scriptet "http-headers"?
- Testa på din egen webbserver om du har en!

#### Bonus-utmaning: Bygg en port-scan-strategi (svår)

**Uppgift:**
Du ska scanna en okänd server (din egen testserver). Bygg en strategi:

**Steg-för-steg plan:**
1. Kolla om hosten är uppe: `ping`
2. Snabb scan av vanliga portar: `nmap --top-ports 100`
3. Djupare scan av hittade portar: `nmap -sV -p [portar]`
4. OS-detection: `nmap -O`
5. Kör safe scripts: `nmap --script safe`

**Kör denna strategi på 127.0.0.1 (din egen dator) och dokumentera:**
- Vad hittade du i varje steg?
- Fanns det något oväntat?
- Vilken tjänst exponerar flest öppna portar?

### 📝 Sammanfattning

**Vad du har lärt dig:**

- ✅ TCP/IP-stacken har 4 lager: Application, Transport, Internet, Link
- ✅ TCP är pålitligt och connection-oriented (3-way handshake)
- ✅ UDP är snabbt men opålitligt (connectionless)
- ✅ ICMP används för felmeddelanden och ping
- ✅ TCP 3-way handshake: SYN → SYN-ACK → ACK
- ✅ SYN scan (-sS) är snabbare och stealthier än full connect (-sT)
- ✅ UDP scan (-sU) är långsam och svår att tolka
- ✅ Version detection (-sV) identifierar tjänster och versioner
- ✅ OS detection (-O) gissar operativsystem
- ✅ NSE scripts (--script) utökar Nmaps funktionalitet enormt

**Nya ord du lärt dig:**

- **TCP (Transmission Control Protocol)**: Pålitligt protokoll med anslutning
- **UDP (User Datagram Protocol)**: Snabbt protokoll utan anslutning
- **ICMP (Internet Control Message Protocol)**: Felmeddelanden och diagnostik
- **3-way handshake**: SYN, SYN-ACK, ACK – hur TCP-anslutningar startas
- **SYN**: Synchronize – första steget i TCP-handshake
- **ACK**: Acknowledge – bekräftelse
- **RST**: Reset – avbryt anslutning
- **Socket**: IP + port + protokoll (t.ex. 192.168.0.1:80/TCP)
- **Stealth scan**: SYN scan som inte fullföljer anslutningen
- **NSE (Nmap Scripting Engine)**: Scripts för avancerad scanning
- **Probe**: Testmeddelande Nmap skickar för att identifiera tjänster

**Viktiga kommandon du lärt dig:**

```bash
# Scan-typer
nmap -sT 192.168.0.10          # TCP Connect scan
sudo nmap -sS 192.168.0.10     # SYN scan (stealth)
sudo nmap -sU 192.168.0.10     # UDP scan
nmap -sV 192.168.0.10          # Version detection
sudo nmap -O 192.168.0.10      # OS detection

# NSE Scripts
nmap --script default 192.168.0.10      # Default scripts
nmap --script vuln 192.168.0.10         # Vulnerability scripts
nmap --script http-title -p 80 192.168.0.10  # Specifikt script

# Kombinationer
sudo nmap -sS -sV 192.168.0.10          # SYN + version
sudo nmap -A 192.168.0.10               # Aggressiv (allt!)
sudo nmap -sS -sU 192.168.0.10          # TCP + UDP
```

**Viktiga koncept:**

| Koncept | TCP | UDP |
|---------|-----|-----|
| Anslutning | Ja (3-way handshake) | Nej |
| Pålitlighet | Garanterad | Ingen garanti |
| Ordning | Paket i rätt ordning | Kan komma i fel ordning |
| Hastighet | Långsammare | Snabbare |
| Användning | Webbsidor, e-post, filer | Streaming, DNS, spel |
| Nmap scan | Tydliga resultat | Svårtolkat (open\|filtered) |

**Jämförelse scan-typer:**

| Scan-typ | Kräver sudo? | Hastighet | Stealth | Användning |
|----------|--------------|-----------|---------|------------|
| -sT (TCP Connect) | Nej | Medel | Låg | När du inte har sudo |
| -sS (SYN) | Ja | Snabb | Medel | Default för de flesta |
| -sU (UDP) | Ja | Långsam | Medel | Hitta UDP-tjänster |
| -sV (Version) | Nej | Långsam | Låg | Identifiera tjänster |
| -O (OS detection) | Ja | Medel | Låg | Gissa OS |

**Nästa steg:**

I nästa nivå går vi ännu djupare in på avancerad nätverksteori:
- Hur NAT och brandväggar påverkar scanning
- IDS/IPS och hur de upptäcker Nmap
- VLAN, subnetting och routing
- Avancerade Nmap-tekniker: timing, fragmentering, decoys
- Best practices för professionell användning

Det blir university-nivå, så förbered dig på att verkligen förstå hur komplexa nätverk fungerar!

**Fantastiskt jobbat! 🚀** Du förstår nu hur internet faktiskt fungerar under huven och exakt vad Nmap gör när det scannar. Ta en välförtjänt paus – nästa nivå blir riktigt avancerad!

---

## Nivå 4: Avancerad Nätverksteori & Komplexa Miljöer 🏛️

### Introduktion

Välkommen till universitetsnivån! Här går vi på djupet med hur moderna, komplexa nätverk fungerar. Du kommer lära dig hur NAT, brandväggar, IDS/IPS och andra säkerhetslager påverkar Nmap-scanning. Vi kommer också täcka avancerade Nmap-tekniker som professionella penetrationstestare använder. Efter denna nivå kommer du förstå inte bara hur man scannar nätverk, utan också hur man förstår och navigerar i komplexa nätverksmiljöer med flera säkerhetslager. Detta är kunskapen som skiljer en användare från en expert!

### Kärnkoncept

#### 1. NAT (Network Address Translation) – Hur privata IP:er delas

**Problem**: Vi har slut på IPv4-adresser (bara ~4 miljarder), men behöver ansluta miljarder enheter!

**Lösning**: NAT låter många enheter dela **en** publik IP-adress.

**Hur det fungerar:**

Din router har TWO IP-adresser:
- **Privat IP** (inåt mot ditt hem): `192.168.0.1`
- **Publik IP** (utåt mot internet): `85.123.45.67` (exempel)

När din dator (`192.168.0.10`) vill prata med Google:

```
DIN DATOR          ROUTER (NAT)           GOOGLE
192.168.0.10       Inåt: 192.168.0.1      8.8.8.8
                   Utåt: 85.123.45.67
    |                    |                   |
    | Till: 8.8.8.8     |                   |
    | Från: 192.168.0.10|                   |
    |------------------>|                   |
    |                    | NAT översätter:  |
    |                    | Till: 8.8.8.8    |
    |                    | Från: 85.123.45.67|
    |                    |------------------>|
    |                    |                   |
    |                    | Svar kommer       |
    |                    |<------------------|
    | NAT översätter     |                   |
    | tillbaka           |                   |
    |<-------------------|                   |
```

**NAT-tabell:**
Routern har en tabell som mappar interna adresser till portar:

| Intern IP:Port | Extern Port | Destination |
|----------------|-------------|-------------|
| 192.168.0.10:5000 | 12345 | 8.8.8.8:443 |
| 192.168.0.15:6000 | 12346 | 1.1.1.1:80  |

**Varför är detta viktigt för Nmap?**
- Du kan **inte** scanna interna IP-adresser från internet!
- NAT blockerar oönskad inkommande trafik (som Nmap-scanningar)
- Port forwarding kan öppna specifika portar genom NAT

**Typer av NAT:**
- **SNAT (Source NAT)**: Ändrar källadress (utgående trafik)
- **DNAT (Destination NAT)**: Ändrar destinationsadress (inkommande, port forwarding)
- **Full cone NAT**: Mest öppen (tillåter svar från vilken IP som helst)
- **Symmetric NAT**: Striktast (en unik mapping per destination)

#### 2. Brandväggar (Firewalls) – Stateless vs Stateful

Brandväggar filtrerar trafik baserat på regler. Det finns två huvudtyper:

**Stateless Firewall** (paketfilter):
- Kollar varje paket individuellt
- Baserar beslut på: Source IP, Destination IP, Port, Protocol
- **Minns INTE** tidigare paket

**Exempel:**
```
Regel: Tillåt TCP port 80 från 192.168.0.0/24
Effekt: Varje paket som matchar tillåts, utan kontext
```

**Stateful Firewall** (connection tracking):
- Håller koll på **state** av varje anslutning
- Minns 3-way handshake
- Tillåter bara relaterade paket

**TCP Connection States:**
```
NEW      → Första paketet i en ny anslutning (SYN)
ESTABLISHED → Anslutning etablerad (efter handshake)
RELATED  → Ny anslutning relaterad till existerande (FTP data)
INVALID  → Paketet matchar ingen känd anslutning
```

**Exempel Stateful Regel:**
```
Regel: Tillåt ESTABLISHED, RELATED
Effekt: Om en anslutning startades inifrån, tillåt svaren utifrån
```

**Hur påverkar detta Nmap?**

**Stateless:**
```
Nmap SYN → Brandvägg ser: SYN till port 80 → Blocka allt?
                                           → Tillåt bara port 80?
Result: Simpel logik, lätt att kringgå
```

**Stateful:**
```
Nmap SYN → Brandvägg: "Initierades denna anslutning inifrån?"
                      → NEJ → BLOCK
                      → JA → TILLÅT
Result: Mycket svårare att scanna utifrån!
```

**Nmap mot brandväggar:**
```bash
# Om ICMP blockeras, hoppa över host discovery
nmap -Pn 192.168.0.10

# Testa specifika portar om allt verkar filtrerat
nmap -p 80,443 192.168.0.10
```

#### 3. IDS vs IPS – Intrusion Detection/Prevention Systems

**IDS (Intrusion Detection System)**:
- **Passiv**: Lyssnar på nätverkstrafik
- **Upptäcker**: Konstiga mönster (som Nmap-scans!)
- **Larmar**: Meddelar administratörer
- **Stoppar INTE**: Attacken fortsätter

**IPS (Intrusion Prevention System)**:
- **Aktiv**: Sitter mellan trafiken
- **Upptäcker**: Samma som IDS
- **Blockerar**: Stoppar aktivt misstänkt trafik
- **Stoppar**: Attacken förhindras

**Vanliga Nmap-signaturer som upptäcks:**
1. **SYN scan**: Många SYN-paket utan ACK
2. **Port sweep**: Scanning av många portar snabbt
3. **Host sweep**: Scanning av många IP:er
4. **Version detection**: Kända probe-strängar
5. **NULL/FIN/Xmas scans**: Ovanliga flag-kombinationer

**Hur IDS/IPS upptäcker Nmap:**

```
NMAP                  IDS/IPS                  SERVER
  |                      |                        |
  | SYN port 1          |                        |
  |-------------------->|                        |
  | SYN port 2          | "Hm, många SYN..."   |
  |-------------------->|                        |
  | SYN port 3          |                        |
  |-------------------->| "Detta är en scan!"   |
  |                      | → LARM!               |
  |                      | (eller BLOCK om IPS)  |
```

**Hur man undviker IDS/IPS (ETiskt, på egna system!):**

```bash
# Långsammare scan (svårare att upptäcka)
nmap -T2 192.168.0.10

# Ännu långsammare (paranoid)
nmap -T0 192.168.0.10

# Randomisera ordning
nmap --randomize-hosts 192.168.0.0/24

# Fragmentera paket
nmap -f 192.168.0.10
```

#### 4. VLAN (Virtual LAN) – Segmentering av nätverk

**VLAN** delar upp ett fysiskt nätverk i flera logiska nätverk.

**Exempel:**
```
FYSISK SWITCH (alla anslutna)
   |
   +-- VLAN 10: Management (192.168.10.0/24)
   |
   +-- VLAN 20: Guest WiFi (192.168.20.0/24)
   |
   +-- VLAN 30: Servrar (192.168.30.0/24)
```

**Varför VLAN?**
- **Säkerhet**: Gäster kan inte nå servrar
- **Prestanda**: Mindre broadcast-domän
- **Hantering**: Logisk separation

**För Nmap:**
- Du kan bara scanna din egen VLAN om du inte har routing mellan VLAN:er
- Vissa switches kan detektera VLAN-hopping-attacker

#### 5. Proxy och VPN

**Proxy**:
- Mellanhand mellan klient och server
- Kan anonymisera, cache:a, filtrera

**VPN (Virtual Private Network)**:
- Krypterad tunnel genom internet
- Gör ditt hem till "förlängning" av företagets nätverk

**Hur påverkar detta scanning?**

```
Utan VPN:
NMAP (Ditt hem) → Internet → MålServer
      ↓
  Din publika IP syns

Med VPN:
NMAP → VPN-tunnel → VPN-server → MålServer
                          ↓
                    VPN-serverns IP syns
```

**Etiskt tips:**
- VPN används för att skydda privatliv, INTE för att gömma olaglig scanning
- Många VPN-leverantörer loggar och samarbetar med myndigheter

#### 6. Subnetting & CIDR – Djupdykning

Vi nämnde detta tidigare, men nu går vi djupare.

**CIDR-notation djupdykning:**

`192.168.0.0/24` betyder:
- Nätverksadress: `192.168.0.0`
- Nätmask: `255.255.255.0` (24 ettor, 8 nollor)
- Första adress: `192.168.0.0` (nätverket)
- Sista adress: `192.168.0.255` (broadcast)
- Användbara adresser: `192.168.0.1` - `192.168.0.254` (254 st)

**Vanliga subnät:**

| CIDR | Nätmask | Användbar IP:er | Användning |
|------|---------|-----------------|------------|
| /8   | 255.0.0.0 | 16 777 214 | Stora organisationer |
| /16  | 255.255.0.0 | 65 534 | Medelstora nätverk |
| /24  | 255.255.255.0 | 254 | Hemnätverk, små kontor |
| /30  | 255.255.255.252 | 2 | Point-to-point länkar |
| /32  | 255.255.255.255 | 1 | En enskild IP |

**För Nmap:**
```bash
# Scanna ett /24-nät (254 hostar)
nmap 192.168.0.0/24

# Scanna bara en IP (/32 implicit)
nmap 192.168.0.10

# Scanna ett större /16-nät (65534 hostar!)
nmap 10.0.0.0/16  # TAR LÅNG TID!
```

#### 7. Routing och ARP

**Routing**: Hur paket hittar vägen mellan nätverk.

**Routingtabell** (förenkl

ad):
```
Destination      Gateway         Interface
192.168.0.0/24   0.0.0.0         eth0      (lokalt nätverk)
10.0.0.0/8       192.168.0.1     eth0      (via router)
0.0.0.0/0        192.168.0.1     eth0      (default - allt annat)
```

**ARP (Address Resolution Protocol)**: Mappar IP → MAC-adress i lokalt nätverk

**ARP-process:**
```
Dator A vill prata med 192.168.0.10
   |
   | Vet inte MAC-adressen!
   |
   | Skickar ARP Request: "Vem har 192.168.0.10?"
   | (broadcast till alla)
   |
192.168.0.10 svarar: "Det är jag! Min MAC är AA:BB:CC:DD:EE:FF"
   |
   | Dator A cache:ar detta
   |
   | Nu kan paketen skickas
```

**Nmap och ARP:**
- I lokala nätverk använder Nmap ofta ARP för host discovery
- Snabbare och mer pålitligt än ICMP i LAN
- Kan inte användas över routrar (ARP är bara lokalt)

```bash
# ARP scan (bara lokalt nätverk)
nmap -PR 192.168.0.0/24

# Visa ARP-tabell
arp -a
```

### Avancerade Nmap-tekniker

#### 1. Host Discovery – Hoppa över eller anpassa

**Problem**: Många nätverk blockerar ping (ICMP), så Nmap tror hosten är nere.

**Lösning**: Olika host discovery-metoder.

**Standard host discovery:**
```bash
nmap 192.168.0.10
# Nmap pingar först, om inget svar → "host down" → ingen port-scan
```

**Alternativ:**

```bash
# -Pn: Hoppa över ping, anta att hosten är uppe
nmap -Pn 192.168.0.10

# -PS: TCP SYN ping till specifika portar
nmap -PS22,80,443 192.168.0.10

# -PA: TCP ACK ping
nmap -PA80 192.168.0.10

# -PU: UDP ping
nmap -PU53 192.168.0.10

# -PR: ARP ping (bara LAN)
nmap -PR 192.168.0.0/24

# Kombinera flera
nmap -PS22 -PA80 -PU53 192.168.0.10
```

**När använder man vad?**
- **-Pn**: När du VET hosten är uppe men svarar inte på ping
- **-PS**: Testa vanliga TCP-portar som ofta är öppna
- **-PR**: I lokala nätverk, snabbast och mest pålitlig

#### 2. Port Selection – Anpassa vad du scannar

**Default**: Nmap scannar de 1000 vanligaste portarna.

**Anpassa:**

```bash
# Scanna ALLA portar (1-65535) - TAR LÅNG TID!
nmap -p- 192.168.0.10

# Scanna specifika portar
nmap -p 22,80,443,3306 192.168.0.10

# Port-range
nmap -p 1-1000 192.168.0.10

# Snabb scan - bara top 100
nmap -F 192.168.0.10

# Top 1000 (standard)
nmap --top-ports 1000 192.168.0.10

# Top 10 vanligaste
nmap --top-ports 10 192.168.0.10

# Alla TCP + UDP
nmap -p T:1-65535,U:1-65535 192.168.0.10  # MYCKET LÅNGSAM!
```

**Strategi:**
1. **Först**: Snabb scan (`-F` eller `--top-ports 100`)
2. **Om du hittar något**: Fullständig scan (`-p-`)
3. **För UDP**: Bara top 100 (`-sU --top-ports 100`)

#### 3. Timing Templates (-T0 till -T5)

Nmap har inbyggda timing-profiler:

| Template | Namn | Hastighet | När använda |
|----------|------|-----------|-------------|
| -T0 | Paranoid | Extremt långsam | Undvika IDS (1 port/gång) |
| -T1 | Sneaky | Mycket långsam | Undvika IDS |
| -T2 | Polite | Långsam | Minska belastning |
| -T3 | Normal | **Default** | Balanserad |
| -T4 | Aggressive | Snabb | Snabba nätverk, lokalt |
| -T5 | Insane | Mycket snabb | Riskabelt, kan missa svar |

**Exempel:**
```bash
# Paranoid - 5 minuters väntan mellan paket
nmap -T0 192.168.0.10

# Aggressiv - för snabba skanningar
nmap -T4 192.168.0.0/24

# Custom timing (avancerat)
nmap --max-retries 2 --host-timeout 30m 192.168.0.10
```

**Varning**: T5 kan missa öppna portar pga timeout!

#### 4. Fragmentering och Decoys – Undvika upptäckt

**Fragmentering (-f)**:
Dela upp IP-paket i mindre fragment för att förvirra brandväggar.

```bash
# Fragment paket
nmap -f 192.168.0.10

# Anpassad MTU (Multiple of 8)
nmap --mtu 16 192.168.0.10
```

**Hur det fungerar:**
```
Normalt paket:
[IP Header][TCP Header][Data]

Fragmenterat:
[IP Header][TCP Hea]
[IP Header][der][Data]
```

Vissa brandväggar kan inte inspektera fragmenterade paket korrekt.

**Decoys (-D)**:
Blanda din riktiga IP med fejk-IP:er.

```bash
# Använd decoys
nmap -D RND:10 192.168.0.10
# Skapar 10 fejk-IP:er + din riktiga

# Specifika decoys
nmap -D 192.168.0.5,192.168.0.7,ME 192.168.0.10
# ME = din riktiga IP

# Fullständigt random source IP
nmap -S 10.0.0.5 -e eth0 192.168.0.10
# OBS: Du får INTE svar! Bara för att förvirra loggar
```

**Hur decoys ser ut i loggen:**
```
Målserver ser:
- Scan från 192.168.0.5
- Scan från 192.168.0.7
- Scan från 192.168.0.12 ← din riktiga
- Scan från 192.168.0.18
...

Svårt att veta vilken som är riktig!
```

#### 5. Idle Scan (Zombie Scan) – Extremt stealthy

**Konceptet**: Använd en TREDJE dator (zombie) för att scanna målet.

**Hur det fungerar:**
```
1. NMAP             ZOMBIE           MÅL
      |                |              |
      | Kolla IP ID   |              |
      |-------------->|              |
      | IP ID: 1000   |              |
      |<--------------|              |
      |                |              |

2.    | Skicka SYN från ZOMBIE      |
      | (spoofad source)             |
      |----------------------------->|
      |                |              |
      |                | SYN-ACK      |
      |                |<-------------|
      |                | RST (IP ID+1)|
      |                |------------->|
      |                |              |

3.    | Kolla IP ID igen             |
      |-------------->|              |
      | IP ID: 1002   | ← Ökade med 2!
      |<--------------|              |
      |                |              |
   Port är OPEN! (zombie skickade RST)
```

**Kommando:**
```bash
# Hitta en lämplig zombie (idle host)
nmap --script ipidseq 192.168.0.0/24

# Kör idle scan
nmap -sI zombie_ip target_ip
nmap -sI 192.168.0.50 192.168.0.100
```

**Fördelar:**
- Din IP syns ALDRIG i målets loggar
- Extremt stealth

**Nackdelar:**
- Svårt att hitta lämpliga zombies
- Fungerar bara om zombie har förutsägbar IP ID-sekvens
- Oetiskt att använda någon annans dator som zombie utan tillstånd!

#### 6. Advanced NSE Usage

**NSE Scripts per kategori:**

```bash
# Vulnerability scanning
nmap --script vuln 192.168.0.10

# Brute force (försiktigt!)
nmap --script brute 192.168.0.10

# Discovery
nmap --script discovery 192.168.0.10

# Flera kategorier
nmap --script "default and safe" 192.168.0.10

# Exkludera vissa
nmap --script "default and not intrusive" 192.168.0.10

# Wildcard
nmap --script "http-*" 192.168.0.10 -p 80
```

**Användbara scripts:**

```bash
# SSL/TLS info
nmap --script ssl-cert,ssl-enum-ciphers -p 443 192.168.0.10

# SMB (Windows fildelning)
nmap --script smb-os-discovery,smb-security-mode -p 445 192.168.0.10

# Mysql
nmap --script mysql-info,mysql-databases -p 3306 192.168.0.10

# HTTP
nmap --script http-title,http-headers,http-enum -p 80 192.168.0.10
```

**Script arguments:**
```bash
# Passa argument till scripts
nmap --script http-form-brute --script-args userdb=users.txt,passdb=pass.txt 192.168.0.10

# Flera argument
nmap --script mysql-brute --script-args userdb=users.txt,passdb=pass.txt,brute.timeout=5m 192.168.0.10
```

#### 7. Output Formats – Spara och analysera resultat

**Output-alternativ:**

```bash
# Normal output (läsbar)
nmap -oN scan.txt 192.168.0.10

# XML output (maskinläsbar)
nmap -oX scan.xml 192.168.0.10

# Grepable (för parsing)
nmap -oG scan.gnmap 192.168.0.10

# Alla format samtidigt
nmap -oA scan_results 192.168.0.10
# Skapar: scan_results.nmap, scan_results.xml, scan_results.gnmap

# Append till fil istället för overwrite
nmap --append-output -oN scan.txt 192.168.0.10
```

**Analysera XML med tools:**
```bash
# Konvertera XML till HTML-rapport
xsltproc scan.xml -o scan.html

# Importera i andra tools
# Kan importeras i: Metasploit, Burp Suite, OWASP ZAP, etc.
```

### Best Practices för Professionell Användning

#### 1. Dokumentation och loggning

**Alltid dokumentera:**
```bash
# Mall för dokumentation
#
# Datum: 2025-11-18
# Syfte: Säkerhetsgranskning av webbserver
# Tillstånd: Skriftligt från IT-chef (se mail 2025-11-15)
# Scope: 192.168.10.50 (webbserver-prod)
#
nmap -sS -sV -p- --script vuln -oA webserver_scan_20251118 192.168.10.50
```

**Spara alltid:**
- Kommandot du körde
- När du körde det
- Varför du körde det
- Vem som gav tillstånd
- Resultaten

#### 2. Etisk checklist

Före VARJE scan, fråga dig:

- [ ] Har jag skriftligt tillstånd?
- [ ] Är jag inom scope (rätt IP:er)?
- [ ] Är det rätt tid? (undvik produktionstid)
- [ ] Har jag varnat rätt personer?
- [ ] Kan min scan orsaka skada? (DoS risk?)
- [ ] Loggar jag vad jag gör?

**Om något går fel:**
1. Stoppa omedelbart
2. Informera ansvariga
3. Dokumentera vad som hände
4. Lär dig av misstaget

#### 3. Scan-strategier för olika miljöer

**Hemmanätverk (övning):**
```bash
# Snabb, aggressiv
nmap -T4 -A -v 192.168.0.0/24
```

**Produktionsmiljö:**
```bash
# Försiktig, mindre påträngande
nmap -T2 -sS -sV --top-ports 100 -oA prod_scan target_ip
```

**Stealth reconnaissance:**
```bash
# Långsam, fragmenterad, decoys
nmap -T1 -f -D RND:10 -sS --randomize-hosts target_range
```

**Fullständig säkerhetsgranskning:**
```bash
# Allt! (med tillstånd!)
nmap -T4 -A -sS -sU -p- --script vuln -oA full_audit target
```

#### 4. Tolka resultat i kontext

**Exempel 1: Filtrerade portar**
```
PORT     STATE    SERVICE
80/tcp   filtered http
443/tcp  filtered https
22/tcp   filtered ssh
```

**Analys:**
- Möjligt att brandvägg blockerar alla portar
- Eller: Host är nere
- Eller: Host discovery misslyckades

**Åtgärd:**
```bash
# Testa med -Pn (hoppa över host discovery)
nmap -Pn -p 80,443,22 target
```

**Exempel 2: Bara högre portar öppna**
```
PORT      STATE SERVICE
8080/tcp  open  http-proxy
8443/tcp  open  https-alt
9000/tcp  open  cslistener
```

**Analys:**
- Troligen en utvecklingsmiljö eller container
- Inte standard portar (80, 443)
- Kan vara proxy eller load balancer

**Exempel 3: Många RPC/Microsoft portar**
```
PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
```

**Analys:**
- Definitivt Windows-server
- RDP öppen (3389) - fjärrskrivbord
- SMB öppen (445) - fildelning
- WinRM (5985) - PowerShell remote
- **RISK**: Många attackytor, se till att systemet är uppdaterat!

### Visualisering: ASCII-diagram

#### Diagram 1: NAT-översättning

```
INTERNT NÄTVERK       |    NAT ROUTER    |    INTERNET
                      |                  |
192.168.0.10:5000 ----|--> Översätt  ----|---> 8.8.8.8:443
                      |    Till:         |
                      | 85.1.2.3:12345   |
                      |                  |
                      | NAT-tabell:      |
                      | Int:Ext mapping  |
                      | 192.168.0.10:5000|
                      |   ↔ 12345        |
                      |                  |
192.168.0.15:6000 ----|---> 12346  ------|---> 1.1.1.1:80
                      |                  |
```

#### Diagram 2: Stateful Firewall med Connection Tracking

```
┌────────────────────────────────────────────────────────┐
│         STATEFUL FIREWALL                              │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Connection Table:                                     │
│  ┌──────────────────────────────────────────────┐     │
│  │ Src IP:Port    Dst IP:Port    State          │     │
│  ├──────────────────────────────────────────────┤     │
│  │ 192.168.0.10:5000 → 8.8.8.8:443  ESTABLISHED │     │
│  │ 192.168.0.15:6000 → 1.1.1.1:80   NEW         │     │
│  │ 192.168.0.20:7000 → 10.0.0.1:22  RELATED     │     │
│  └──────────────────────────────────────────────┘     │
│                                                         │
│  Ny trafik:                                            │
│  SYN från 192.168.0.10 → Tillåt (NEW)                 │
│  ACK för etablerad anslutning → Tillåt (ESTABLISHED)  │
│  SYN från internet → Blocka (ingen matchning)         │
│                                                         │
└────────────────────────────────────────────────────────┘
```

#### Diagram 3: IDS/IPS Detection av Nmap Scan

```
TIMELINE: Nmap Port Scan Detected
═══════════════════════════════════════════════════════

T+0s    Nmap skickar SYN → port 1
         ↓
T+0.1s  Nmap skickar SYN → port 2
         ↓
T+0.2s  Nmap skickar SYN → port 3
         ↓                 ┌──────────────────┐
T+0.3s  Nmap skickar SYN →│   IDS UPPTÄCKER  │
                          │  "Port Scan!"    │
                          │   ALARM! 🚨      │
                          └──────────────────┘
                               ↓
                          ADMIN MEDDELAD
                               ↓
                         (om IPS: BLOCK!)

Signaturer som matchar:
- Många SYN till olika portar
- Hög frekvens av connections
- Sekvensiell port-scanning
- Kända Nmap fingerprints
```

#### Tabell: Scan-teknik vs Upptäcktsrisk

| Teknik | IDS Risk | Firewall Bypass | Hastighet | Användning |
|--------|----------|-----------------|-----------|------------|
| -sS (SYN) | Medel | Låg | Snabb | Standard |
| -sT (Connect) | Hög | Låg | Medel | Utan sudo |
| -sN (NULL) | Låg | Medel | Medel | Stealth |
| -sI (Idle) | Mycket låg | Hög | Långsam | Max stealth |
| -f (Fragment) | Låg | Hög | Medel | Bypass filter |
| -D (Decoy) | Låg | Medel | Medel | Förvirra loggar |
| -T0 (Paranoid) | Mycket låg | Medel | Extremt långsam | Undvika IDS |
| -T5 (Insane) | Hög | Låg | Mycket snabb | Riskabelt |

### ✏️ Övningar

#### Övning 1: Förstå NAT i ditt hem (medel)

**Uppgift:**
1. Hitta din **interna IP** (ipconfig/ifconfig)
2. Hitta din **publika IP** (googla "what is my ip")
3. Rita hur NAT fungerar mellan dem

**Förklara:**
- Varför kan andra på internet inte scanna din interna IP direkt?
- Vad behövs för att tillåta inkommande anslutningar? (Port forwarding)

#### Övning 2: Testa -Pn flaggan (medel)

**Uppgift:**
Scanna en host som blockerar ICMP.

**Steg:**
```bash
# Först utan -Pn
nmap 192.168.0.1

# Om "Host seems down", testa med -Pn
nmap -Pn 192.168.0.1
```

**Förklara:**
- Fick du olika resultat?
- Varför är -Pn användbart?

#### Övning 3: Timing templates (medel-svår)

**Uppgift:**
Testa olika timing och mät tid.

**Kommandon:**
```bash
# Snabb
time nmap -T4 --top-ports 100 192.168.0.1

# Normal
time nmap -T3 --top-ports 100 192.168.0.1

# Långsam
time nmap -T2 --top-ports 100 192.168.0.1
```

**Dokumentera:**
- Hur lång tid tog varje scan?
- Var resultaten samma?
- När skulle du välja vilken?

#### Övning 4: NSE Vulnerability Scanning (svår)

**Uppgift:**
Kör sårbarhetsscanning på en testserver.

**Kommando:**
```bash
# ENDAST på egna system!
nmap --script vuln 127.0.0.1
```

**Analysera:**
- Hittades några sårbarheter?
- Vad är severity av dem?
- Hur skulle du åtgärda dem?

#### Övning 5: Output Formats (medel)

**Uppgift:**
Spara en scan i alla format.

**Kommando:**
```bash
nmap -sV -oA my_scan 192.168.0.1
```

**Utforska:**
```bash
# Titta på filerna
cat my_scan.nmap
cat my_scan.xml
cat my_scan.gnmap
```

**Förklara:**
- Vilken fil är lättast att läsa för människor?
- Vilken är bäst för automatisering?
- Hur skulle du söka efter öppna port 80 i gnmap-filen?

#### Övning 6: Case Study - Mystery Server (svår)

**Scenario:**
Du har hittat en server på ditt nätverk: `192.168.0.150`

**Uppgift:**
Bygg en komplett profil av servern.

**Strategi:**
```bash
# 1. Är den uppe?
ping 192.168.0.150

# 2. Snabb scan
nmap -F 192.168.0.150

# 3. Full port scan av öppna portar
nmap -p- 192.168.0.150

# 4. Version detection
nmap -sV -p [discovered_ports] 192.168.0.150

# 5. OS detection
sudo nmap -O 192.168.0.150

# 6. Vulnerability scan
nmap --script vuln -p [discovered_ports] 192.168.0.150
```

**Dokumentera:**
- Vilket OS?
- Vilka tjänster?
- Några sårbarheter?
- Vad är serverns syfte? (web, database, file server?)

#### Övning 7: Bonus - Bygg en Scan Policy (svår)

**Uppgift:**
Skapa en scan-policy för tre scenarier:

**Scenario 1: Snabb inventering**
```bash
# Mål: Hitta alla aktiva hostar snabbt
# Din lösning här:
```

**Scenario 2: Djup säkerhetsgranskning**
```bash
# Mål: Hitta alla sårbarheter
# Din lösning här:
```

**Scenario 3: Stealth reconnaissance**
```bash
# Mål: Undvika upptäckt
# Din lösning här:
```

**Förslag på lösningar:**

**Scenario 1:**
```bash
nmap -sn 192.168.0.0/24  # Bara host discovery
nmap -F -T4 --open 192.168.0.0/24  # Snabb, bara öppna portar
```

**Scenario 2:**
```bash
sudo nmap -sS -sV -sU -p- --script vuln -O -A -T3 -oA deep_scan target
```

**Scenario 3:**
```bash
nmap -sS -T1 -f -D RND:5 --randomize-hosts -oN stealth.log target
```

### 📝 Sammanfattning

**Vad du har lärt dig:**

- ✅ NAT översätter privata IP:er till en publik IP
- ✅ Brandväggar kan vara stateless (enkla regler) eller stateful (connection tracking)
- ✅ IDS upptäcker attacker, IPS blockerar dem aktivt
- ✅ VLAN segmenterar nätverk logiskt
- ✅ VPN och proxy påverkar hur scanning syns
- ✅ Subnetting och CIDR-notation på djupet
- ✅ ARP mappar IP till MAC i lokala nätverk
- ✅ Avancerade Nmap-tekniker: -Pn, timing, fragmentering, decoys, idle scan
- ✅ NSE scripts för vulnerability scanning och automation
- ✅ Output-format för dokumentation och analys
- ✅ Best practices för etisk och professionell användning

**Nya koncept du lärt dig:**

- **NAT (Network Address Translation)**: Delar en publik IP mellan många enheter
- **Stateful Firewall**: Brandvägg som minns anslutningar
- **IDS (Intrusion Detection System)**: Passiv övervakning
- **IPS (Intrusion Prevention System)**: Aktiv blockering
- **VLAN**: Virtuellt LAN, logisk nätverkssegmentering
- **ARP**: Address Resolution Protocol (IP → MAC)
- **MTU**: Maximum Transmission Unit
- **Fragmentering**: Dela upp paket för att kringgå filter
- **Decoy**: Fejk source-IP för att förvirra
- **Idle/Zombie scan**: Använd tredje part för scanning
- **Connection tracking**: Stateful firewalls håller koll på anslutningar

**Kritiska kommandon:**

```bash
# Host Discovery
nmap -Pn target                    # Hoppa över ping
nmap -PS22,80,443 target           # TCP SYN ping
nmap -PR 192.168.0.0/24            # ARP ping (LAN)

# Port Selection
nmap -p- target                    # Alla portar
nmap -F target                     # Fast scan (top 100)
nmap --top-ports 1000 target       # Top 1000

# Timing
nmap -T0 target                    # Paranoid (stealth)
nmap -T4 target                    # Aggressive (snabb)

# Evasion
nmap -f target                     # Fragmentera
nmap -D RND:10 target              # Decoys
nmap -sI zombie target             # Idle scan

# NSE
nmap --script vuln target          # Vulnerability scan
nmap --script "http-*" -p 80 target  # HTTP scripts

# Output
nmap -oA filename target           # Alla format
```

**Anti-patterns (Gör INTE detta!):**

❌ Scanna utan tillstånd
❌ Använd -T5 i produktionsmiljö (kan missa resultat)
❌ Kör `--script vuln` utan att veta vad det gör
❌ Glöm att dokumentera
❌ Använd idle scan med någon annans zombie utan tillstånd
❌ Scanna hela /8-nät utan plan (miljarder paket!)

**Nästa steg:**

I sista nivån (Expert-nivå) kommer vi täcka:
- Performance tuning för stora nätve rk
- Distribuerade scanningar
- Integration med CI/CD och automatisering
- Kombination med andra verktyg
- Enterprise vulnerability management
- Modern cloud och container-scanning
- Avancerad NSE script-utveckling

Det blir professionell användning på högs ta nivå!

**Grattis! 🎓** Du har nu universitets-nivå kunskap om nätverksskanning. Du förstår inte bara hur Nmap fungerar, utan också de komplexa nätverksmiljöer det används i. Ta en paus och låt detta sjunka in – nästa nivå är expert-nivå!

---

## Nivå 5: Expert – Stora Nätverk & Professionell Användning 💼

### Introduktion

Välkommen till expert-nivån! Detta är där teori möter praktisk tillämpning i stora organisationer och moderna infrastrukturer. På denna nivå kommer du lära dig hur Nmap används i enterprise-miljöer, hur man optimerar för stora skanningar, hur man integrerar Nmap i automatiserade workflows, och hur modern infrastruktur (cloud, containers, microservices) påverkar nätverksskanning. Detta är kunskapen som används av säkerhetsteam i Fortune 500-företag, penetrationstestare på professionell nivå, och SOC-analytiker. Efter denna nivå är du redo att använda Nmap på expert-nivå i verkliga, komplexa miljöer.

### Kärnkoncept

#### 1. Performance Tuning – Optimera för stora nätverk

När du ska scanna tusentals eller miljontals IP-adresser måste du tänka på prestanda.

**Problem:**
```bash
# Detta kommer ta VECKOR:
nmap -p- 10.0.0.0/8  # 16 miljoner IP:er × 65535 portar = 🔥
```

**Lösning**: Strategisk optimering.

**Steg 1: Host Discovery först**
```bash
# Bara hitta levande hostar (snabbt!)
nmap -sn -oG live_hosts.gnmap 10.0.0.0/16

# Parsa resultat
grep "Status: Up" live_hosts.gnmap | awk '{print $2}' > live_ips.txt

# Nu har du bara aktiva IP:er att scanna vidare
```

**Steg 2: Parallellisering**
```bash
# Använd GNU Parallel eller xargs
cat live_ips.txt | parallel -j 50 'nmap -sS -p- {} -oA scans/{}'

# Eller med xargs
cat live_ips.txt | xargs -P 50 -I {} nmap -sS -p- {} -oA scans/{}
```

**Steg 3: Timing och aggressiveness**
```bash
# Balansera hastighet vs pålitlighet
nmap -T4 --min-rate 1000 --max-retries 2 target_range

# Custom timing
nmap --min-hostgroup 64 --min-parallelism 100 target_range
```

**Viktiga parametrar:**

| Parameter | Vad den gör | Exempel |
|-----------|-------------|---------|
| --min-rate | Minsta paket/sekund | --min-rate 1000 |
| --max-rate | Max paket/sekund | --max-rate 5000 |
| --min-parallelism | Antal parallella probes | --min-parallelism 100 |
| --min-hostgroup | Scanna flera hostar samtidigt | --min-hostgroup 64 |
| --host-timeout | Max tid per host | --host-timeout 30m |
| --max-retries | Max omförsök | --max-retries 2 |

**Best Practice för stora scanningar:**
```bash
# 1. Host discovery (snabb)
nmap -sn -T4 -oG discovery.gnmap 10.0.0.0/16

# 2. Top ports på levande hostar (medel)
nmap -sS --top-ports 1000 -T4 -iL live_hosts.txt -oA top_ports

# 3. Full scan på intressanta hostar (långsam)
nmap -p- -sV -T3 -iL interesting_hosts.txt -oA full_scan
```

#### 2. Distribuerade scanningar (Konceptuellt)

För MYCKET stora nätverk behöver du distribuera scann ingen över flera maskiner.

**Strategier:**

**Metod 1: IP-range splitting**
```bash
# Dela upp /16 i flera /24
# Maskin 1:
nmap 10.0.0.0/24

# Maskin 2:
nmap 10.0.1.0/24

# ... osv
```

**Metod 2: Port-range splitting**
```bash
# Maskin 1: Portar 1-10000
nmap -p 1-10000 10.0.0.0/16

# Maskin 2: Portar 10001-20000
nmap -p 10001-20000 10.0.0.0/16

# ... osv
```

**Metod 3: Dedikerad orchestration**
```
CONTROLLER
    |
    +--- WORKER 1 (scans 10.0.0.0/20)
    |
    +--- WORKER 2 (scans 10.0.16.0/20)
    |
    +--- WORKER 3 (scans 10.0.32.0/20)
    |
    V
CENTRALISERAD DATABAS
```

**Tools för distribuerad scanning:**
- **dnmap**: Distribuerat Nmap framework
- **Custom Python/Bash scripts med jobb-köer**
- **Kubernetes Jobs** för cloud-miljöer

#### 3. Automatisering & Scripting

**Bash wrapper för regelbundna scanningar:**

```bash
#!/bin/bash
# automated_scan.sh

DATE=$(date +%Y%m%d_%H%M%S)
TARGET_RANGE="192.168.0.0/24"
OUTPUT_DIR="./scans/$DATE"

mkdir -p "$OUTPUT_DIR"

echo "[*] Starting scan at $(date)"

# Host discovery
echo "[+] Phase 1: Host Discovery"
nmap -sn "$TARGET_RANGE" -oG "$OUTPUT_DIR/discovery.gnmap"

# Extract live hosts
grep "Status: Up" "$OUTPUT_DIR/discovery.gnmap" | \
    awk '{print $2}' > "$OUTPUT_DIR/live_hosts.txt"

NUM_HOSTS=$(wc -l < "$OUTPUT_DIR/live_hosts.txt")
echo "[+] Found $NUM_HOSTS live hosts"

# Port scan
echo "[+] Phase 2: Port Scanning"
nmap -sS -sV --top-ports 1000 \
    -iL "$OUTPUT_DIR/live_hosts.txt" \
    -oA "$OUTPUT_DIR/port_scan"

# Vulnerability scan
echo "[+] Phase 3: Vulnerability Scanning"
nmap --script vuln \
    -iL "$OUTPUT_DIR/live_hosts.txt" \
    -oA "$OUTPUT_DIR/vuln_scan"

echo "[*] Scan complete at $(date)"
echo "[*] Results saved to $OUTPUT_DIR"

# Optional: Send notification
# curl -X POST https://slack.com/api/... -d "Scan complete"
```

**Python för avancerad parsing:**

```python
#!/usr/bin/env python3
# parse_nmap.py

import xml.etree.ElementTree as ET
import sys
import json

def parse_nmap_xml(xml_file):
    """Parse Nmap XML and extract key information"""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    results = []

    for host in root.findall('host'):
        if host.find('status').get('state') != 'up':
            continue

        # Get IP
        ip = host.find('address').get('addr')

        # Get hostname if available
        hostname_elem = host.find('hostnames/hostname')
        hostname = hostname_elem.get('name') if hostname_elem is not None else ''

        # Get ports
        ports = []
        for port in host.findall('ports/port'):
            port_id = port.get('portid')
            protocol = port.get('protocol')
            state = port.find('state').get('state')
            service = port.find('service')

            port_info = {
                'port': port_id,
                'protocol': protocol,
                'state': state,
                'service': service.get('name') if service is not None else '',
                'version': service.get('version') if service is not None else ''
            }

            ports.append(port_info)

        results.append({
            'ip': ip,
            'hostname': hostname,
            'ports': ports
        })

    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 parse_nmap.py <nmap_xml_file>")
        sys.exit(1)

    results = parse_nmap_xml(sys.argv[1])
    print(json.dumps(results, indent=2))
```

#### 4. CI/CD Integration – Continuous Security Scanning

Integrera Nmap i din CI/CD-pipeline för automatisk säkerhetsgranskning.

**GitLab CI exempel:**

```yaml
# .gitlab-ci.yml

stages:
  - build
  - test
  - security_scan
  - deploy

security_network_scan:
  stage: security_scan
  image: instrumentisto/nmap:latest
  script:
    - nmap -sV --script vuln $STAGING_SERVER -oX nmap_results.xml
    - python3 parse_and_alert.py nmap_results.xml
  artifacts:
    paths:
      - nmap_results.xml
    expire_in: 30 days
  only:
    - main
    - staging
```

**GitHub Actions exempel:**

```yaml
# .github/workflows/security-scan.yml

name: Security Scan

on:
  schedule:
    - cron: '0 2 * * *'  # Dagligen kl 02:00
  workflow_dispatch:

jobs:
  nmap-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Install Nmap
        run: sudo apt-get install -y nmap

      - name: Run network scan
        run: |
          nmap -sV --top-ports 100 ${{ secrets.STAGING_IP }} -oX scan.xml

      - name: Parse results
        run: python3 scripts/parse_nmap.py scan.xml > findings.json

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: nmap-scan-results
          path: |
            scan.xml
            findings.json

      - name: Check for critical findings
        run: |
          if grep -q "CRITICAL" findings.json; then
            echo "Critical findings detected!"
            exit 1
          fi
```

#### 5. Enterprise Vulnerability Management

Hur Nmap passar in i större sårbarhetshanteringsprogram.

**Workflow:**

```
1. ASSET DISCOVERY (Nmap)
   ↓
2. PORT/SERVICE SCANNING (Nmap -sV)
   ↓
3. VULNERABILITY SCANNING (Nmap --script vuln)
   ↓
4. INTEGRATION (Export till SIEM/Vulnerability Manager)
   ↓
5. PRIORITERING (CVSS scores, business impact)
   ↓
6. REMEDIATION (Patching, config changes)
   ↓
7. RE-SCAN (Verify fix)
```

**Integration med andra verktyg:**

```bash
# Exportera till CSV för analys
nmap -sV --script vuln target -oX scan.xml
xsltproc scan.xml -o scan.html  # För läsbar rapport

# Importera i andra verktyg:
# - Nessus: Kan importera Nmap XML
# - OpenVAS: Kan använda Nmap results
# - Metasploit: db_import scan.xml
# - Splunk: Indexera XML/JSON
```

**Automatisk rapportering:**

```bash
#!/bin/bash
# weekly_report.sh

# Kör scan
nmap -sV --top-ports 1000 -oA weekly_scan $TARGET_RANGE

# Generera rapport
python3 generate_report.py weekly_scan.xml > report_$(date +%Y%m%d).html

# Skicka via email
mail -s "Weekly Network Scan Report" -a report_$(date +%Y%m%d).html \
    security-team@company.com < /dev/null
```

#### 6. Cloud & Container Scanning

Modern infrastruktur kräver moderna tekniker.

**AWS/Azure/GCP Scanning:**

**Utmaningar:**
- Dynamiska IP:er (instanser kommer och går)
- Security Groups / Network ACLs blockerar scanning
- Distributed architecture

**Lösning:**
```bash
# Från INOM cloud (EC2 instance, Azure VM)
# Scanna samma VPC/VNet

# AWS exempel: Hitta alla instanser i VPC
aws ec2 describe-instances \
    --query 'Reservations[*].Instances[*].PrivateIpAddress' \
    --output text > cloud_ips.txt

# Scanna från intern VM
nmap -sS --top-ports 100 -iL cloud_ips.txt -oA cloud_scan
```

**Kubernetes/Docker Scanning:**

**Problem**: Containers har ingen permanent IP, kort livstid

**Lösningar:**

**1. Scanna från host:**
```bash
# Lista alla container IPs
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
    $(docker ps -q) > container_ips.txt

# Scanna
nmap -sS -iL container_ips.txt
```

**2. Scanna service endpoints:**
```bash
# Kubernetes: Scanna service IPs istället för pods
kubectl get services -o wide

# Scanna ClusterIP
nmap -p <service-port> <cluster-ip>
```

**3. Specialiserade verktyg:**
- **Trivy**: Container image scanning
- **Clair**: Vulnerability scanner för containers
- **Anchore**: Container security platform

**Best practice för cloud:**
- Scanna från INOM cloud-miljön (inte från internet)
- Använd cloud-native security tools först
- Nmap som complement, inte huvudverktyg
- Tänk på kostnader (data transfer)

#### 7. NSE Script Development – Skapa egna scripts

Nmap's Scripting Engine låter dig skriva egna scripts i Lua.

**Grundstruktur:**

```lua
-- File: my-script.nse

description = [[
Beskrivning av vad scriptet gör.
]]

author = "Ditt Namn"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

-- Portrule: När ska scriptet köras?
portrule = function(host, port)
    -- Kör bara på port 80 och 443
    return (port.number == 80 or port.number == 443) and port.state == "open"
end

-- Action: Vad ska scriptet göra?
action = function(host, port)
    local result = {}

    -- Din logik här
    local socket = nmap.new_socket()
    local status, err = socket:connect(host, port)

    if not status then
        return "Could not connect"
    end

    socket:send("GET / HTTP/1.0\r\n\r\n")
    local response, err = socket:receive()
    socket:close()

    -- Parsa respons
    if response and response:match("Server: (.*)") then
        table.insert(result, "Server: " .. response:match("Server: (.*)"))
    end

    return result
end
```

**Köra ditt script:**
```bash
# Lägg i ~/.nmap/scripts/ eller /usr/share/nmap/scripts/
cp my-script.nse ~/.nmap/scripts/

# Uppdatera script database
nmap --script-updatedb

# Kör
nmap --script my-script target
```

**Exempel: Custom HTTP header check**

```lua
-- http-custom-header.nse
description = "Checks for custom security headers"

categories = {"safe", "discovery"}

portrule = function(host, port)
    return port.number == 80 or port.number == 443
end

action = function(host, port)
    local http = require "http"
    local shortport = require "shortport"
    local stdnse = require "stdnse"

    local response = http.get(host, port, "/")

    if not response or not response.header then
        return "No response"
    end

    local headers = response.header
    local findings = {}

    -- Check för security headers
    if not headers["x-frame-options"] then
        table.insert(findings, "Missing: X-Frame-Options")
    end

    if not headers["x-content-type-options"] then
        table.insert(findings, "Missing: X-Content-Type-Options")
    end

    if not headers["strict-transport-security"] then
        table.insert(findings, "Missing: Strict-Transport-Security")
    end

    if #findings > 0 then
        return stdnse.format_output(true, findings)
    else
        return "All security headers present"
    end
end
```

#### 8. Kombination med andra verktyg

Nmap är kraftfullt, men i en modern security-stack kombineras det med många verktyg.

**Typical Workflow:**

```
1. RECONNAISSANCE
   - Nmap: Network mapping
   - Masscan: Ultra-fast port scanning
   - Shodan/Censys: Internet-wide scanning data

2. ENUMERATION
   - Nmap -sV: Service detection
   - Nmap NSE: Detailed probing
   - enum4linux, smbclient: Specific protocols

3. VULNERABILITY ASSESSMENT
   - Nmap --script vuln: Basic vulns
   - Nessus/OpenVAS: Deep vulnerability scanning
   - Nikto: Web server scanner

4. EXPLOITATION (ethical/authorized only!)
   - Metasploit: Exploit framework
   - Burp Suite: Web application testing
   - SQLmap: SQL injection

5. POST-EXPLOITATION
   - Privilege escalation
   - Lateral movement
   - Data exfiltration (in authorized tests)

6. REPORTING
   - Aggregera data från alla verktyg
   - Dradis, Faraday: Collaboration platforms
```

**Automation example:**

```bash
#!/bin/bash
# recon_automation.sh

TARGET=$1

echo "[+] Phase 1: Fast port discovery with masscan"
sudo masscan -p1-65535 $TARGET --rate=10000 -oG masscan.gnmap

# Parse masscan results for open ports
PORTS=$(grep "Host:" masscan.gnmap | cut -d' ' -f5 | cut -d'/' -f1 | sort -u | tr '\n' ',' | sed 's/,$//')

echo "[+] Open ports: $PORTS"

echo "[+] Phase 2: Detailed Nmap scan on open ports"
nmap -sV -sC -p$PORTS $TARGET -oA detailed_scan

echo "[+] Phase 3: Vulnerability scanning"
nmap --script vuln -p$PORTS $TARGET -oA vuln_scan

echo "[+] Phase 4: Web enumeration (if port 80/443 open)"
if echo $PORTS | grep -q "80\|443"; then
    nikto -h $TARGET -output nikto_results.txt
fi

echo "[+] Done! Check results:  "
echo "    - detailed_scan.nmap"
echo "    - vuln_scan.nmap"
echo "    - nikto_results.txt (if applicable)"
```

### Visualisering: Flödesscheman & Strategier

#### Flödesschema: Enterprise Scan Strategy

```
┌──────────────────────────────────────────────────────────┐
│              START: Large Network Scan                   │
└───────────────────┬──────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  PHASE 1: Asset Discovery                                │
│  Tool: nmap -sn -T4 [range]                              │
│  Output: List of live IPs                                │
└───────────────────┬───────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  PHASE 2: Quick Port Scan                                │
│  Tool: nmap --top-ports 100 -T4 [live_ips]              │
│  Output: Common services                                 │
└───────────────────┬───────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  Decision: Interesting hosts found?                       │
└───┬─────────────────────────────────────────────┬─────────┘
    │ YES                                         │ NO
    ▼                                             ▼
┌───────────────────────────────────┐    ┌──────────────────┐
│ PHASE 3: Deep Scan                │    │ END: Report      │
│ nmap -p- -sV -sC [interesting]    │    │ No threats found │
└───────────────┬───────────────────┘    └──────────────────┘
                │
                ▼
┌───────────────────────────────────────────────────────────┐
│  PHASE 4: Vulnerability Assessment                        │
│  nmap --script vuln [targets]                            │
└───────────────────┬───────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  PHASE 5: Manual Review & Prioritization                 │
│  - Review findings                                        │
│  - Assign CVSS scores                                     │
│  - Determine business impact                             │
└───────────────────┬───────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  PHASE 6: Remediation & Re-scan                          │
│  - Fix issues                                             │
│  - Verify with targeted re-scan                          │
└───────────────────┬───────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────────────────────┐
│  END: Final Report & Metrics                             │
│  - Before/After comparison                                │
│  - Trend analysis                                         │
│  - Executive summary                                      │
└───────────────────────────────────────────────────────────┘
```

#### Tabell: Scan Strategies by Environment Size

| Miljö | Storlek | Strategi | Exempel Kommando |
|-------|---------|----------|------------------|
| Hem/Litet Kontor | <100 hosts | Enkel, aggressiv | `nmap -A -T4 192.168.0.0/24` |
| SMB | 100-1000 hosts | Fasad, parallell | `nmap -sn → nmap -sS -sV --top-ports 1000` |
| Enterprise | 1000-10000 hosts | Distribuerad, optimerad | Split range, multiple workers |
| Carrier/ISP | 10000+ hosts | Massiv parallellisering | Dedikerade scanning clusters |

### ✏️ Övningar

#### Övning 1: Performance Benchmark (medel-svår)

**Uppgift:**
Jämför olika timing-inställningar och mät prestanda.

**Test:**
```bash
# Test 1: Default
time nmap --top-ports 1000 192.168.0.0/24

# Test 2: Aggressive
time nmap -T4 --min-rate 1000 --top-ports 1000 192.168.0.0/24

# Test 3: Custom optimized
time nmap --min-hostgroup 50 --min-parallelism 100 --top-ports 1000 192.168.0.0/24
```

**Dokumentera:**
- Tid för varje test
- Antal hosts discovered
- Skillnader i resultat (missade något?)
- Din slutsats: Vilken är bäst för ditt nätverk?

#### Övning 2: Bygg ett Automation Script (svår)

**Uppgift:**
Skapa ett Bash-script som:
1. Tar ett IP-range som input
2. Kör host discovery
3. Scannar levande hostar
4. Sparar resultat med tidsstämpel
5. Skickar en sammanfattning

**Mall:**
```bash
#!/bin/bash

# Ditt script här
```

**Bonus:**
- Lägg till error handling
- Logga alla steg till fil
- Email-notifiering vid completion

#### Övning 3: Parse Nmap XML (svår)

**Uppgift:**
Skriv ett Python-script som:
1. Läser Nmap XML-output
2. Extraherar alla hostar med port 22 öppen
3. Skapar en lista: IP, hostname, SSH version

**Template:**
```python
import xml.etree.ElementTree as ET

def parse_ssh_hosts(xml_file):
    # Din kod här
    pass

if __name__ == '__main__':
    parse_ssh_hosts('scan.xml')
```

#### Övning 4: Cloud Scanning Strategy (svår)

**Uppgift:**
Du är ansvarig för att scanna en AWS VPC med:
- 500 EC2 instanser
- Autoscaling groups (instanser kommer och går)
- Security groups blockerar externt scanning

**Designa en strategi:**
1. Hur får du lista alla instanser?
2. Varifrån scannar du?
3. Vilket schema (dagligen, veckovis)?
4. Hur hanterar du dynamiska IP:er?
5. Hur rapporterar du resultat?

**Skriv en 1-sida plan.**

#### Övning 5: Vulnerability Management Workflow (expert)

**Scenario:**
Du har kört `nmap --script vuln` och hittat 50 sårbarheter över 200 hostar.

**Uppgift:**
1. Kategorisera sårbarheterna (Critical, High, Medium, Low)
2. Prioritera baserat på:
   - CVSS score
   - Exponering (internet-facing?)
   - Business impact (produktionsserver?)
3. Skapa en remediation-plan
4. Bestäm re-scan schedule

**Leverera:**
- Spreadsheet med sårbarheter
- Prioriterad lista
- Timeline för fixes

#### Övning 6: NSE Script Development (expert)

**Uppgift:**
Skriv ett NSE script som:
- Kör på port 80/443
- Hämtar HTTP response headers
- Kontrollerar om "Server" header exponerar version
- Rapporterar om det är en säkerhetsrisk

**Steg:**
1. Skapa `.nse` fil
2. Implementera portrule
3. Implementera action
4. Testa
5. Dokumentera

#### Övning 7: Bonus - Enterprise Mock Project (expert)

**Stort projekt:**

**Scenario:**
Du är säkerhetschef på ett företag med:
- 5000 endpoints
- 50 servrar
- 3 datacenters
- Cloud (AWS + Azure)
- Mix av Windows, Linux, IoT

**Uppgift:**
Designa en komplett scanning-strategi:

1. **Asset Inventory:**
   - Hur kartlägger du alla assets?
   - Verktyg?
   - Frekvens?

2. **Scanning Schedule:**
   - Daglig/Veckovis/Månadsvis?
   - Vad scannrar när?

3. **Tooling:**
   - Vilka verktyg utöver Nmap?
   - Integration mellan verktyg?

4. **Automation:**
   - CI/CD integration?
   - Automated remediation?

5. **Reporting:**
   - Till vem?
   - Vilket format?
   - Metriker och KPIer?

6. **Compliance:**
   - PCI DSS, GDPR, ISO 27001?
   - Hur säkerställer du compliance?

**Leverera:**
- 3-5 sidor strategidokument
- Nätverksdiagram
- Exempelscripts
- Budget-uppskattning

### 📝 Sammanfattning

**Vad du har lärt dig på expert-nivå:**

- ✅ Performance tuning för scanningar av tusentals hostar
- ✅ Distribuerad scanning över flera maskiner
- ✅ Automation med Bash och Python
- ✅ CI/CD integration för continuous security
- ✅ Enterprise vulnerability management workflows
- ✅ Cloud och container-scanning strategier
- ✅ NSE script development i Lua
- ✅ Integration med andra säkerhetsverktyg
- ✅ Professio nell rapportering och metrics

**Expert-level koncept:**

- **Horizontal Scaling**: Distribuera scanning över flera workers
- **Rate Limiting**: Balansera hastighet vs nätverksbelastning
- **Continuous Scanning**: Automatiserade, regelbundna scanningar
- **Asset Lifecycle Management**: Hålla koll på assets som kommer och går
- **Vulnerability Lifecycle**: Från discovery → prioritering → remediation → verification
- **Defense in Depth**: Nmap som ett lager i en multi-tool security stack
- **DevSecOps**: Security scanning i varje steg av utvecklingscykeln

**Kritiska Best Practices:**

```bash
# 1. Alltid dokumentera
echo "# Scan: $(date), Target: $TARGET, Purpose: $PURPOSE" >> scan.log

# 2. Använd consistent naming
nmap target -oA scan_$(date +%Y%m%d)_$TARGET_NAME

# 3. Version control dina scripts
git add automated_scan.sh
git commit -m "Add: automated weekly scan"

# 4. Testa i staging först
nmap -T2 staging_server  # Försiktig i prod!

# 5. Monitera din egen scanning
# Så att du vet om något går fel
tail -f /var/log/nmap_scans.log

# 6. Rate limit för att inte överbelasta
nmap --max-rate 500 large_network

# 7. Alltid ha en rollback-plan
# Om något går fel, hur stoppar du snabbt?

# 8. Kommunicera med stakeholders
# Meddela före stora scanningar
```

**Command Cheat Sheet - Expert Edition:**

```bash
# Performance Optimized Scan
nmap -sS -T4 --min-rate 1000 --max-retries 2 \
     --min-hostgroup 64 --min-parallelism 100 \
     --top-ports 1000 -oA optimized_scan $RANGE

# Distributed Scan (split by worker)
# Worker 1:
nmap -sS $RANGE --exclude-file workers_2-5.txt -oA worker1

# Full Enterprise Audit
nmap -sS -sV -sU -p- --script "default and safe" \
     -O -A -T3 --max-retries 3 \
     -oA enterprise_audit_$(date +%Y%m%d) $TARGET

# Cloud-optimized (from within VPC)
nmap -sS -Pn --top-ports 100 -T4 \
     --script cloud-security \
     -iL cloud_instances.txt -oA cloud_scan

# CI/CD Integration Scan
nmap -sV --script vuln \
     --script-args vulns.showall \
     $STAGING_SERVER \
     -oX ci_scan.xml || exit 1

# Kubernetes Service Scan
nmap -sS -p $SERVICE_PORT $CLUSTER_IP -oA k8s_scan
```

**Metrics & KPIs för Enterprise:**

| Metric | Vad det mäter | Mål |
|--------|---------------|-----|
| Coverage | % av assets scannade | >95% |
| Frequency | Dagar sedan senaste scan | <7 dagar |
| Mean Time to Detect (MTTD) | Tid från vuln introduceras till upptäckt | <24h |
| Mean Time to Remediate (MTTR) | Tid från upptäckt till fix | <30 dagar (beroende på severity) |
| False Positive Rate | % felaktiga findings | <5% |
| Critical Vulns Open | Antal kritiska öppna sårbarheter | 0 |

**Nästa steg efter denna guide:**

1. **Certifieringar:**
   - CEH (Certified Ethical Hacker)
   - OSCP (Offensive Security Certified Professional)
   - GPEN (GIAC Penetration Tester)

2. **Praktisk erfarenhet:**
   - HackTheBox / TryHackMe labs
   - Bug bounty programs (HackerOne, Bugcrowd)
   - CTF competitions

3. **Fördjupning:**
   - Läs Nmap's officiella bok
   - Studera NSE script source code
   - Bidra till open source security tools

4. **Specialisering:**
   - Web application security
   - Network penetration testing
   - Cloud security
   - ICS/SCADA security
   - Mobile security

**Grattis! 🏆** Du har nu genomfört hela guiden från 5-årings nivå till expert-nivå! Du förstår inte bara hur Nmap fungerar, utan också hur det används i verkliga, komplexa miljöer av professionella säkerhetsteam. Du har kunskapen som krävs för att:

- Scanna nätverk av alla storlekar
- Integrera security scanning i moderna DevOps-workflows
- Bygga och underhålla enterprise vulnerability management-program
- Automatisera och optimera scanningar
- Använda Nmap tillsammans med andra verktyg i en modern security-stack

**Du är nu en Nmap-expert!** 💪

Använd denna kunskap etiskt, ansvarsfullt och för att göra internet säkrare. Lycka till på din resa inom cybersäkerhet!

---

## 🎓 Slutlig Självutvärdering

Testa din kunskap efter att ha läst guiden! Svara ärligt och se vilken nivå du behärskar.

### Nivå 1-2: Grundläggande förståelse

**1. Vad är en IP-adress?**
- [ ] A) Ett husnummer för datorer på nätverk
- [ ] B) Ett lösenord
- [ ] C) Ett virus
- [ ] D) En webbläsare

**Rätt svar**: A

**2. Vad gör Nmap?**
- [ ] A) Skapar virus
- [ ] B) Scannar nätverk för att hitta datorer och öppna portar
- [ ] C) Skickar spam
- [ ] D) Redigerar bilder

**Rätt svar**: B

**3. Vilket kommando scannar hela ditt hemnätverk (192.168.0.x)?**
- [ ] A) `nmap google.com`
- [ ] B) `nmap 192.168.0.0/24`
- [ ] C) `nmap --hack-everything`
- [ ] D) `nmap -delete-all`

**Rätt svar**: B

**4. Vad betyder "open" när Nmap rapporterar en port?**
- [ ] A) Porten är stängd
- [ ] B) En tjänst lyssnar på porten och svarar
- [ ] C) Datorn är avstängd
- [ ] D) Det finns ett virus

**Rätt svar**: B

### Nivå 3: Teknisk förståelse

**5. Vad är TCP 3-way handshake?**
- [ ] A) SYN → SYN-ACK → ACK
- [ ] B) HELLO → GOODBYE → OK
- [ ] C) PING → PONG → DONE
- [ ] D) START → MIDDLE → END

**Rätt svar**: A

**6. Vad är skillnaden mellan TCP och UDP?**
- [ ] A) TCP är pålitligt med anslutning, UDP är snabbt utan garanti
- [ ] B) Ingen skillnad
- [ ] C) UDP är alltid säkrare
- [ ] D) TCP använder bara port 80

**Rätt svar**: A

**7. Vilket kommando gör en SYN scan?**
- [ ] A) `nmap -sT target`
- [ ] B) `nmap -sS target`
- [ ] C) `nmap -sU target`
- [ ] D) `nmap -sP target`

**Rätt svar**: B

**8. Varför är SYN scan "stealthier" än TCP Connect scan?**
- [ ] A) Den fullföljer inte 3-way handshake
- [ ] B) Den är osynlig
- [ ] C) Den använder kryptering
- [ ] D) Den är alltid olaglig

**Rätt svar**: A

### Nivå 4: Avancerad kunskap

**9. Vad är NAT?**
- [ ] A) Network Address Translation - översätter privata IP:er till publika
- [ ] B) Ett operativsystem
- [ ] C) En webbläsare
- [ ] D) Ett programmeringsspråk

**Rätt svar**: A

**10. Vad är skillnaden mellan IDS och IPS?**
- [ ] A) IDS upptäcker, IPS upptäcker OCH blockerar
- [ ] B) Ingen skillnad
- [ ] C) IPS är långsammare
- [ ] D) IDS används bara i Windows

**Rätt svar**: A

**11. Vilket flag hoppar över host discovery?**
- [ ] A) `-Pn`
- [ ] B) `-sS`
- [ ] C) `-A`
- [ ] D) `-O`

**Rätt svar**: A

**12. Vad gör `-f` flaggan?**
- [ ] A) Fragmenterar paket
- [ ] B) Snabb scan
- [ ] C) Full scan
- [ ] D) Finger scan

**Rätt svar**: A

### Nivå 5: Expert-kunskap

**13. Hur optimerar du Nmap för att scanna tusentals hostar?**
- [ ] A) Host discovery först, sedan parallellisera, använd --min-rate
- [ ] B) Kör `nmap -p- target` på alla direkt
- [ ] C) Använd `-T5` alltid
- [ ] D) Scanna en IP åt gången

**Rätt svar**: A

**14. I vilken ordning bör en enterprise scan-strategi köras?**
- [ ] A) Asset Discovery → Port Scan → Service Detection → Vuln Assessment
- [ ] B) Vuln Assessment → Port Scan → Discovery
- [ ] C) Bara kör --script vuln direkt
- [ ] D) Ingen ordning spelar roll

**Rätt svar**: A

**15. Hur scannar du bäst Kubernetes pods?**
- [ ] A) Scanna service ClusterIPs istället för pod IPs
- [ ] B) Scanna från internet
- [ ] C) Pods kan inte scannas
- [ ] D) Använd bara nmap -A

**Rätt svar**: A

**16. Vad är ett NSE script skrivet i?**
- [ ] A) Lua
- [ ] B) Python
- [ ] C) Java
- [ ] D) C++

**Rätt svar**: A

### Resultat:

**0-4 rätt**: Gå tillbaka och läs Nivå 1-2 igen
**5-8 rätt**: Bra grundkunskap! Fördjupa dig i Nivå 3
**9-12 rätt**: Avancerad användare! Studera Nivå 4 noggrannare
**13-16 rätt**: Expert-nivå! 🏆 Du behärskar Nmap!

### Praktiska färdighetstest:

**Kan du:**

- [ ] Hitta din egen IP-adress och routers IP?
- [ ] Kör en grundläggande Nmap-scan på ditt hemnätverk?
- [ ] Förklara skillnaden mellan open, closed och filtered portar?
- [ ] Köra SYN scan, UDP scan och version detection?
- [ ] Tolka Nmap XML-output?
- [ ] Skriva ett enkelt Bash-script som automatiserar scanningar?
- [ ] Använda NSE scripts för vulnerability scanning?
- [ ] Designa en scan-strategi för ett enterprise-nätverk?
- [ ] Integrera Nmap i en CI/CD-pipeline?
- [ ] Skriva egna NSE scripts i Lua?

**Om du kan 0-3**: Fortsätt öva på grunderna
**Om du kan 4-6**: Du är på god väg!
**Om du kan 7-9**: Avancerad användare
**Om du kan alla 10**: Expert! 🎯

---

## 📖 Ordlista

### A

**ACK (Acknowledge)**
TCP-flagga som bekräftar mottagande av data.

**ARP (Address Resolution Protocol)**
Protokoll som mappar IP-adresser till MAC-adresser i lokala nätverk.

**Asset Discovery**
Process att identifiera alla enheter i ett nätverk.

### B

**Brandvägg (Firewall)**
System som filtrerar nätverkstrafik baserat på säkerhetsregler.

**Broadcast**
Meddelande skickat till alla enheter i ett nätverk.

### C

**CIDR (Classless Inter-Domain Routing)**
Notation för IP-adress-ranges, t.ex. 192.168.0.0/24.

**Closed Port**
Port där ingen tjänst lyssnar, men datorn svarar med RST.

**Connection Tracking**
Stateful firewalls förmåga att minnas aktiva anslutningar.

### D

**Decoy**
Fejk source-IP:er som används för att förvirra loggar och IDS.

**DNS (Domain Name System)**
System som översätter domännamn till IP-adresser.

**DNAT (Destination NAT)**
NAT-typ som ändrar destinationsadress (port forwarding).

### E

**Enumeration**
Process att samla detaljerad information om upptäckta tjänster.

### F

**Filtered Port**
Port där Nmap inte får svar, troligen blockerad av brandvägg.

**Fragmentering**
Att dela upp IP-paket i mindre bitar för att kringgå filter.

### G

**Gateway**
Router som kopplar ihop nätverk, ofta default gateway.

### H

**Host Discovery**
Process att avgöra vilka IP-adresser som är aktiva.

**Handshake (3-way)**
TCP:s SYN → SYN-ACK → ACK process för att etablera anslutning.

### I

**ICMP (Internet Control Message Protocol)**
Protokoll för felmeddelanden och diagnostik (ping).

**IDS (Intrusion Detection System)**
Passivt system som upptäcker men inte blockerar intrång.

**IPS (Intrusion Prevention System)**
Aktivt system som upptäcker OCH blockerar intrång.

**IP-adress**
Unikt nummer som identifierar en enhet på nätverk.

**IPv4**
IP version 4, format: 192.168.0.1 (4 siffror, 0-255).

**IPv6**
IP version 6, format: 2001:0db8::1 (hexadecimalt, mycket fler adresser).

### L

**LAN (Local Area Network)**
Lokalt nätverk, t.ex. ditt hemnätverk.

**Latency**
Tid det tar för ett paket att gå fram och tillbaka.

### M

**MAC-adress**
Hardware-adress för nätverkskort (Media Access Control).

**MTU (Maximum Transmission Unit)**
Största tillåtna paketstorlek.

### N

**NAT (Network Address Translation)**
Teknik som översätter privata IP:er till publika.

**Nmap**
Network Mapper - verktyg för nätverksskanning och säkerhetsgranskning.

**NSE (Nmap Scripting Engine)**
Nmaps script-motor för avancerad funktionalitet (skrivs i Lua).

### O

**Open Port**
Port där en tjänst lyssnar och svarar.

**OS Detection**
Nmaps förmåga att gissa vilket operativsystem som körs (-O).

### P

**Paket**
Enhet av data som skickas över nätverk.

**Ping**
ICMP Echo Request/Reply för att testa om host är uppe.

**Port**
Nummer (0-65535) som identifierar en tjänst på en dator.

**Probe**
Testmeddelande som Nmap skickar för att identifiera tjänster.

**Protokoll**
Regler för hur data ska skickas (t.ex. TCP, UDP, ICMP).

### R

**Reconnaissance**
Insamling av information om mål (första fasen i penetrationstestning).

**Router**
Enhet som dirigerar trafik mellan nätverk.

**RST (Reset)**
TCP-flagga som abrubt avslutar anslutning.

**Routing**
Process att dirigera paket mellan nätverk.

### S

**Service Detection**
Identifiering av vilken tjänst och version som körs på en port (-sV).

**Socket**
Kombination av IP-adress + port + protokoll.

**SNAT (Source NAT)**
NAT-typ som ändrar source-adress (utgående trafik).

**Stealth Scan**
SYN scan (-sS) som inte fullföljer handshake.

**Stateful Firewall**
Brandvägg som minns anslutningar och deras state.

**Stateless Firewall**
Brandvägg som bedömer varje paket individuellt.

**Subnät**
Del av ett större nätverk (t.ex. /24 är ett subnät).

**SYN**
TCP-flagga för att initiera ny anslutning (Synchronize).

### T

**TCP (Transmission Control Protocol)**
Pålitligt, connection-oriented protokoll.

**TTL (Time To Live)**
Antal hopp ett paket får göra innan det kastas.

### U

**UDP (User Datagram Protocol)**
Snabbt, connectionless protokoll utan garanti.

### V

**Version Detection**
Nmap-funktion som identifierar tjänsteversioner (-sV).

**VLAN (Virtual LAN)**
Logisk segmentering av fysiskt nätverk.

**VPN (Virtual Private Network)**
Krypterad tunnel genom internet.

**Vulnerability**
Sårbarhet i system som kan utnyttjas.

### W

**WAN (Wide Area Network)**
Stort nätverk, t.ex. internet.

**Well-known Ports**
Portar 0-1023, reserverade för vanliga tjänster.

### X

**XML**
Format som Nmap kan exportera resultat i (-oX).

### Z

**Zombie Scan**
Idle scan (-sI) som använder tredje part för scanning.

---

## 🔗 Resurser för Fördjupning

### Officiell Nmap-dokumentation

**Nmap Reference Guide**
Den officiella referensen för alla Nmap-kommandon och options.

**Nmap Network Scanning (The Book)**
Skriven av Gordon "Fyodor" Lyon (Nmaps skapare).
Djupdykning i alla aspekter av nätverksskanning.

**NSE Documentation**
Guide till Nmap Scripting Engine och hur man skriver egna scripts.

### Böcker om nätverkssäkerhet

**"The Practice of Network Security Monitoring" av Richard Bejtlich**
Omfattande guide om nätverksövervakning och säkerhet.

**"Network Security Assessment" av Chris McNab**
Praktisk guide till penetrationstestning och sårbarhetshantering.

**"TCP/IP Illustrated, Volume 1" av W. Richard Stevens**
Den definitiva guiden till TCP/IP-protokollet.

**"Metasploit: The Penetration Tester's Guide"**
Hur man kombinerar Nmap med Metasploit för penetrationstestning.

### Online-resurser & Communities

**Nmap.org**
Officiell webbplats med dokumentation, downloads och community.

**Nmap Mailing Lists**
Aktiv community där användare diskuterar tekniker och problem.

**SecLists GitHub**
Listor för security testing (wordlists, scripts, etc.).

**Exploit Database**
Sök sårbarheter och relatera till Nmap-scanningar.

### Övningslabbar & Hands-on

**HackTheBox (HTB)**
Plattform med virtuella maskiner att öva penetrationstestning på.
Börja med "Starting Point" boxar.

**TryHackMe**
Beginner-friendly platform med guidade labs.
Rekommenderade rooms: "Nmap", "Network Security", "Intro to Networking".

**PentesterLab**
Fokuserade övningar på web och network penetration testing.

**OverTheWire: Bandit & Natas**
Wargames för att lära sig Linux och networking basics.

**VulnHub**
Gratis vulnerable VMs att ladda ner och öva på.

### Certifieringar

**eJPT (eLearnSecurity Junior Penetration Tester)**
Beginner-vänlig cert med fokus på praktisk testing.

**CEH (Certified Ethical Hacker)**
Omfattande cert som täcker många verktyg inkl. Nmap.

**OSCP (Offensive Security Certified Professional)**
Praktisk, hands-on cert, krävande men mycket respekterad.

**GPEN (GIAC Penetration Tester)**
Fokus på penetration testing-metodik och verktyg.

**CompTIA Security+**
Bred säkerhetscert, täcker grunderna.

### Video-tutorials & Kurser

**IPPSec (YouTube)**
HackTheBox walkthroughs med detaljerad Nmap-användning.

**The Cyber Mentor (YouTube)**
"Practical Ethical Hacking" kurs täcker Nmap grundligt.

**NetworkChuck (YouTube)**
Beginner-friendly networking tutorials.

**Udemy / Coursera / Pluralsight**
Sök efter "Nmap", "Network Security", "Ethical Hacking".

### Tools att kombinera med Nmap

**Masscan**
Extremt snabb port scanner för stora ranges.

**Metasploit Framework**
Exploit framework som kan importera Nmap-resultat.

**Burp Suite / OWASP ZAP**
Web application security testing.

**Wireshark**
Paketanalys - se exakt vad Nmap skickar.

**Netcat**
Verktyg för att testa portar manuellt.

**Nikto**
Web server vulnerability scanner.

**OpenVAS / Nessus**
Dedikerade vulnerability scanners.

### Skripting och automatisering

**Bash Scripting Guide**
Lär dig automatisera Nmap-scanningar.

**Python `python-nmap` library**
Använd Nmap från Python-scripts.

**Ansible / Terraform**
Infrastructure as Code - automatisera deployment och scanning.

### Fördjupning i specifika områden

**Cloud Security:**
- AWS Security Best Practices
- Azure Security Center
- Google Cloud Security Command Center

**Container Security:**
- Docker Security
- Kubernetes Security
- Trivy / Clair scanner documentation

**IDS/IPS:**
- Snort documentation
- Suricata documentation
- Zeek (formerly Bro) IDS

### Podcasts om säkerhet

**Darknet Diaries**
Berättelser om hacking, cyber security och tech.

**Security Now**
Veckovis diskussion om säkerhetsnyheter.

**Smashing Security**
Lätt, rolig podcast om security.

**Risky Business**
Fokus på enterprise security.

### Hålla sig uppdaterad

**Twitter/X**
Följ: @nmap, @pentestmag, @cybersecboardrm, @USCERT_gov

**Reddit**
r/netsec, r/AskNetsec, r/cybersecurity, r/nmap

**Hacker News**
news.ycombinator.com

**Security Week / Krebs on Security**
Nyheter och analys om cyber security.

---

## ❓ Vanliga Frågor (FAQ)

### Grundläggande frågor

**1. Är det lagligt att använda Nmap?**

Ja, Nmap i sig är ett lagligt verktyg. MEN:
- ✅ Lagligt: Scanna dina egna nätverk och system
- ✅ Lagligt: Scanna med skriftligt tillstånd
- ❌ Olagligt: Scanna andras nätverk utan tillstånd
- ❌ Olagligt: Använda resultaten för skadlig verksamhet

I Sverige och de flesta länder kan obehörig nätverksscanning klassas som dataintrång enligt brottsbalk kapitlet 4 § 9c.

**2. Måste jag ha sudo/root-rättigheter för att köra Nmap?**

Inte alltid, men ofta:
- **BEHÖVS EJ** för: TCP Connect scan (-sT), basic scans
- **BEHÖVS** för: SYN scan (-sS), OS detection (-O), många avancerade funktioner

Utan root får du TCP Connect scan som default. Med root får du SYN scan (snabbare och stealthier).

**3. Varför får jag olika resultat vid olika körningar?**

Flera anledningar:
- **Nätverk förändras**: Hostar kan gå upp/ner mellan scans
- **Timeout**: Om nätverket är långsamt kan Nmap missta inga svar för "port closed"
- **Brandväggar**: Kan blockera inkonsistent eller ha rate limiting
- **Timing**: `-T5` kan missa portar pga korta timeouts

**Lösning**: Kör med `-T3` (default) eller `-T2` för mer pålitliga resultat.

**4. Hur lång tid tar en Nmap-scan?**

Beror på:
- **Antal IP:er**: 1 IP tar sekunder, /16 kan ta timmar-dagar
- **Antal portar**: `--top-ports 100` tar sekunder, `-p-` tar minuter-timmar
- **Timing**: `-T4` snabbare än `-T2`
- **Nätverk**: LAN snabbare än WAN

**Exempel:**
- `nmap 192.168.0.1`: ~5-30 sekunder
- `nmap 192.168.0.0/24`: ~2-10 minuter
- `nmap -p- 192.168.0.1`: ~5-30 minuter
- `nmap -p- 192.168.0.0/24`: Timmar till dagar

**5. Vad betyder "filtered" egentligen?**

**Filtered** betyder att Nmap inte kan avgöra om porten är öppen eller stängd:
- Brandvägg blockerar paket (vanligast)
- Paketet tappas bort i nätverket
- Ingen respons (kan vara många orsaker)

**Filtered ≠ Closed**
- **Closed**: Datorn svarar "ingen lyssnar här" (RST)
- **Filtered**: Ingen respons alls (timeout)

**6. Kan Nmap hacka datorer?**

**NEJ!** Nmap SCANNAR bara, det exploaterar inte sårbarheter.

Nmap kan:
- ✅ Hitta öppna portar
- ✅ Identifiera tjänster och versioner
- ✅ Upptäcka KÄNDA sårbarheter (via NSE scripts)

Nmap kan INTE:
- ❌ Hacka lösenord (det finns andra verktyg för detta)
- ❌ Exploatera sårbarheter (använd Metasploit för detta)
- ❌ Installera backdoors

**Nmap är ett reconnaissance-verktyg, inte ett exploit-verktyg.**

### Tekniska frågor

**7. Vad är skillnaden mellan -sS och -sT?**

| Aspekt | -sS (SYN scan) | -sT (TCP Connect) |
|--------|----------------|-------------------|
| **Kräver root** | Ja | Nej |
| **Hastighet** | Snabbare | Långsammare |
| **Stealth** | Högre | Lägre (loggas lättare) |
| **Handshake** | Aldrig fullföljs (SYN→SYN-ACK→RST) | Fullföljs (SYN→SYN-ACK→ACK) |
| **När använda** | Default med root | När du inte har root |

**8. Hur tolkar jag Nmap-output för "not shown: 998 closed ports"?**

Detta betyder:
- Nmap scannade 1000 portar (default)
- 998 av dem var **closed**
- De stängda portarna visas INTE (för att spara plats)
- Bara **öppna** och **filtered** portar visas

**Exempel:**
```
Not shown: 997 closed ports
PORT    STATE  SERVICE
22/tcp  open   ssh
80/tcp  open   http
443/tcp open   https
```
Tolkning: Av 1000 portar är 997 closed, 3 open.

**9. Varför hittar inte Nmap min Raspberry Pi / IoT-enhet?**

Vanliga orsaker:
1. **Enhet är faktiskt nere** - kontrollera fysiskt
2. **Blockerar ICMP** - använd `-Pn`
3. **Olika subnät** - kolla att du scannar rätt range
4. **WiFi isolation** - vissa routers isolerar trådlösa enheter från varandra
5. **Nätverkssegmentering** - kan vara i en VLAN

**Lösning:**
```bash
# Skippa ping, scanna direkt
nmap -Pn 192.168.0.0/24

# ARP scan (bara LAN)
nmap -PR 192.168.0.0/24

# Kolla routing
ip route
```

**10. Hur scannar jag IPv6-adresser?**

Använd `-6` flaggan:
```bash
# Scanna IPv6
nmap -6 fe80::1

# Scanna IPv6 range
nmap -6 2001:db8::/64

# Både IPv4 och IPv6
nmap -4 -6 hostname
```

**11. Vad gör --script vuln egentligen?**

`--script vuln` kör alla NSE scripts i kategorin "vuln", som testar för:
- Kända CVEs (Common Vulnerabilities and Exposures)
- Common misconfigurations
- Default credentials
- Information disclosure
- Vissa exploiterbara sårbarheter

**OBS:** Det är inte 100% komplett - använd dedikerade vulnerability scanners (Nessus, OpenVAS) för djup scanning.

**12. Kan jag scanna genom en VPN?**

Ja, men med förbehåll:
- ✅ **Kan scanna**: Samma nätverk som VPN ansluter till
- ✅ **Kan scanna**: Med routing genom VPN
- ❌ **Kan ej scanna**: Lokala nätverk på andra sidan om VPN blockerar

**Tips:** Din source-IP blir VPN-serverns IP, inte din riktiga IP.

### Avancerade frågor

**13. Hur undviker jag att bli upptäckt av IDS/IPS?**

Strategier:
1. **Långsammare timing**: `-T0` eller `-T1`
2. **Fragmentering**: `-f`
3. **Decoys**: `-D RND:10`
4. **Randomisera ordning**: `--randomize-hosts`
5. **Sprid ut över tid**: Kör separata scans med timmar emellan
6. **Idle scan**: `-sI` (om du hittar lämplig zombie)

**OBS**: Moderna IDS/IPS upptäcker ändå ofta Nmap. Detta är för LEGITIM testing av dina egna system!

**14. Hur integrerar jag Nmap i en CI/CD pipeline?**

Exempel med GitLab CI:
```yaml
security_scan:
  stage: test
  script:
    - nmap -sV --script vuln $STAGING_IP -oX results.xml
    - python parse_results.py results.xml
  artifacts:
    paths:
      - results.xml
```

Exempel med GitHub Actions:
```yaml
- name: Nmap Scan
  run: nmap -sV ${{ secrets.SERVER_IP }} -oX scan.xml
```

**15. Vad är bästa sättet att scanna ett /8-nätverk (16 miljoner IP:er)?**

**Svårt!** Strategier:
1. **Host discovery först**:
   ```bash
   nmap -sn 10.0.0.0/8 -oG discovery.gnmap
   ```
2. **Parallellisera**: Dela upp i flera /16 och kör samtidigt
3. **Använd masscan**: Mycket snabbare än Nmap för stora ranges
4. **Distributed scanning**: Flera maskiner parallellt
5. **Fokusera**: Scanna bara relevanta subnät

**Tidsestimat:** Med optimering och distribution: veckor. Utan: månader.

**16. Hur skriver jag mitt egna NSE script?**

Grundmall i Lua:
```lua
description = [[Your script description]]
categories = {"safe", "discovery"}

portrule = function(host, port)
    -- When to run
    return port.number == 80
end

action = function(host, port)
    -- What to do
    return "Result"
end
```

Lägg i `~/.nmap/scripts/`, kör `nmap --script-updatedb`, använd med `nmap --script yourscript target`.

### Felsökning

**17. "You requested a scan type which requires root privileges." - Vad gör jag?**

Kör med sudo:
```bash
sudo nmap -sS target
```

Eller använd -sT som inte kräver root:
```bash
nmap -sT target
```

**18. Nmap säger alla portar är "filtered" - vad är problemet?**

Troliga orsaker:
1. **Brandvägg blockerar allt** - försök `-Pn -PS22,80,443`
2. **Fel IP-adress** - dubbelkolla target
3. **Host är verkligen nere** - verifiera med ping
4. **Du är blockerad** - IP:n kan vara banned av target

**19. "WARNING: No route to host" - vad betyder det?**

Betyder att din dator inte vet hur den ska nå målet:
- Kolla routing: `ip route` / `route -n`
- Är target i samma nätverk?
- Har du internetanslutning?
- Försök pinga default gateway först

**20. Hur får jag Nmap att vara "tystare" (mindre output)?**

Använd olika verbosity-nivåer:
```bash
# Normal
nmap target

# Tyst (bara resultat)
nmap -q target

# Mycket tyst (bara errors)
nmap -q -q target

# Ingen output till skärm (bara till fil)
nmap target -oN scan.txt > /dev/null
```

---

## 🎉 Slutord

Grattis! Du har nu gått igenom **Nmap & Nätverksskanning – Den Kompletta Guiden**. Du har rest från att inte veta vad ett nätverk är, till att förstå avancerad nätverksteori, komplexa scan-strategier och enterprise-användning av Nmap.

### Vad du har åstadkommit:

✅ Förstår grundläggande nätverksbegrepp (IP, portar, protokoll)
✅ Kan köra Nmap-scanningar på olika nivåer
✅ Förstår TCP/IP-stacken och hur internet fungerar
✅ Känner till olika scan-tekniker och när de används
✅ Vet hur NAT, brandväggar, IDS/IPS påverkar scanning
✅ Kan optimera scans för stora nätverk
✅ Kan automatisera och integrera Nmap i workflows
✅ Förstår etiska och juridiska aspekter

### Din resa fortsätter:

Detta är **slutet på guiden** men **början på din resa** inom cybersäkerhet.

**Nästa steg:**
1. **Öva, öva, öva** - sätt upp ett eget labb hemma
2. **Gå hands-on** - HackTheBox, TryHackMe, CTFs
3. **Läs vidare** - böcker, dokumentation, artiklar
4. **Bidra** - dela med dig av kunskap, skriv egna NSE scripts
5. **Certifiera dig** - om du vill jobba professionellt

### Viktigaste lärdomen:

**Med stor kraft kommer stort ansvar.** Använd Nmap och din kunskap:
- ✅ För att förbättra säkerhet
- ✅ För att lära dig och andra
- ✅ För att skydda system och användare
- ❌ ALDRIG för att skada eller utan tillstånd

### Tack för att du läste!

Om du har kommit hit har du läst **över 25 000 ord** om Nmap och nätverksskanning. Det är imponerande!

**Lycka till med din fortsatta resa inom cybersäkerhet! 🚀🔒**

*"The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards."* - Gene Spafford

Men eftersom vi inte kan göra så, använder vi Nmap för att förstå och skydda våra system. 😊

---

**Version**: 1.0
**Senast uppdaterad**: November 2025
**Författad för**: Pedagogiskt syfte och cybersäkerhetsutbildning
**Licens**: Educational use

**Feedback?** Hoppas guiden var hjälpsam!

