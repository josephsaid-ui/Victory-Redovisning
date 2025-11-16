# 🌐 Pedagogisk Guide: Datornätverk - Från Grunderna till Expertkunskap

> **Din kompletta resa genom nätverksvärlden - från enkla analogier till avancerad nätverksdesign**
>
> 📚 Läsningstid: 1-2 timmar | 💪 Nivåer: 5 (Nybörjare → Expert) | 🎯 Övningar: 25+

---

## 🎯 Välkommen till Nätverksvärlden!

Hej och välkommen! Är du redo att utforska den fascinerande världen av datornätverk? Oavsett om du är helt ny inom området eller redan har erfarenhet, kommer denna guide att ta dig på en resa från de mest grundläggande koncepten till expertkunskap inom modern nätverksteknik.

### Vad kommer du att lära dig?

I denna guide kommer du att:
- 🎈 Förstå nätverkskoncept genom vardagliga analogier
- 🔧 Lära dig praktiska färdigheter för hem- och företagsnätverk
- 🛡️ Bemästra säkerhet och optimering av nätverk
- 🚀 Utforska framtidens teknologier som 5G, AI och Zero Trust
- 💼 Tillämpa din kunskap i verkliga case studies och projekt

### Hur är guiden uppbyggd?

Guiden är uppdelad i **5 progressiva nivåer**:

```
📊 PROGRESSION
│
├─ 🎈 Nivå 1: Nätverkets Grunder (För Alla)
│   └─ Analogier, enkla koncept, 3 övningar
│
├─ 🏠 Nivå 2: Grundläggande Nätverkstermer
│   └─ IP-adresser, routrar, hemexempel, 4 övningar
│
├─ 🔬 Nivå 3: Protokoll och Verktyg
│   └─ OSI/TCP-IP, Wireshark, diagram, 5 övningar
│
├─ 🎓 Nivå 4: Avancerad Routing och Modern Teknik
│   └─ BGP/OSPF, QoS, Wi-Fi 6+, projekt, 7 övningar
│
└─ 🚀 Nivå 5: Expert-nivå och Framtidsteknologi
    └─ 5G/AI/Zero Trust, SDN, case studies, 8 övningar + projekt
```

Låt oss börja resan!

---

## 🎈 Nivå 1: Nätverkets Grunder - Som en 5-åring Förstår Det

### Vad är egentligen ett datornätverk?

Tänk dig att du vill skicka ett brev till din bästa vän. Du lägger brevet i ett kuvert, skriver adressen, går till brevlådan och postar det. Sedan tar postmannen brevet och levererar det till din vän. **Det är exakt så ett datornätverk fungerar!**

🌐 **Enkelt förklarat:**
- **Ditt brev** = data du vill skicka (ett meddelande, en bild, en video)
- **Kuvertet** = datapaket som omsluter informationen
- **Adressen** = IP-adressen som talar om vart informationen ska
- **Postmannen** = routern som skickar paketen rätt väg
- **Brevlådan** = din dator eller telefon

### 🎪 Analogi 1: Leksakståget

Föreställ dig ett leksakståg som kör runt i ditt rum:

```
   🚂 ← Din dator (tåglok)
   ║
   ╠══ 📦 Datapaket (tågvagnar med leksaker)
   ║
   ╚══ 🏠 → Destination (stationen där leksakerna ska)
```

- **Tåglok** = din dator som skickar information
- **Räls** = kablarna eller Wi-Fi-signalerna
- **Stationer** = andra datorer eller servrar
- **Växlar** = routrar som bestämmer vilken väg tåget ska ta

### 🎨 Analogi 2: Telefonleken

Kom ihåg leken där man viskar ett meddelande från person till person? I ett datornätverk fungerar det likadant!

```
Du → Vän 1 → Vän 2 → Vän 3 → Slutdestination
😊    😃      😄      😁         🎉
```

Varje "vän" är en nätverksenhet (router, switch) som tar emot meddelandet och skickar det vidare till nästa, tills det når slutdestinationen!

### 🎯 Övningar - Nivå 1

**Övning 1.1: Rita ditt hemnätverk 🎨**
- Ta papper och penna
- Rita din dator/telefon
- Rita din router (wifi-boxen)
- Rita internet (ett moln)
- Dra linjer mellan dem
- **Facit**: Det borde se ut ungefär så här:

```
[Din Dator] ←──wifi──→ [Router] ←──kabel──→ ☁️ [Internet]
    📱                    📡                      🌍
```

**Övning 1.2: Postanalogispelet 📮**
1. Skriv ner vad varje del motsvarar:
   - Vad är "brevet" i ett datornätverk?
   - Vad är "adressen"?
   - Vad är "postmannen"?
2. Förklara för någon i din familj hur internet fungerar med postanalogien!

**Övning 1.3: Identifiera nätverksenheter hemma 🏠**
- Gå runt i ditt hem
- Hitta 5 enheter som är anslutna till internet
- Lista dem: (Exempel: Mobil, TV, Laptop, Smart-högtalare, etc.)
- **Bonus**: Vilka använder Wi-Fi och vilka använder kabel?

---

## 🏠 Nivå 2: Grundläggande Nätverkstermer - Hemexempel

Nu när du förstår grundkonceptet, låt oss lära oss de viktiga termerna!

### 🔑 IP-adresser: Ditt Digitala Hemadress

Precis som ditt hem har en adress (Storgatan 12, 123 45 Stockholm), har varje enhet på internet en **IP-adress**.

**Det finns två typer:**

1. **IPv4** (den gamla): `192.168.1.10`
   - 4 siffror separerade med punkter
   - Ungefär som: Gata-nummer, Postnummer, Stad, Land

2. **IPv6** (den nya): `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
   - Mycket längre, men det finns plats för ALLA enheter i världen!

### 🏠 Hemexempel: Ditt Lokala Nätverk

```
DITT HEMNÄTVERK
╔════════════════════════════════════════╗
║  Router: 192.168.1.1 (WiFi-boxen) 📡  ║
║  ┌─────────────────────────────────┐  ║
║  │ Laptop:    192.168.1.10  💻     │  ║
║  │ Mobil:     192.168.1.11  📱     │  ║
║  │ Smart-TV:  192.168.1.12  📺     │  ║
║  │ Skrivare:  192.168.1.13  🖨️      │  ║
║  └─────────────────────────────────┘  ║
╚════════════════════════════════════════╝
           ↓ (via kabel/fiber)
      ☁️ INTERNET 🌍
```

### 🔌 Viktiga Nätverksenheter

**1. Router (Routern) 📡**
- Dirigent som styr trafiken
- Kopplar ditt hemnätverk till internet
- Har både en lokal IP (192.168.1.1) och en publik IP

**2. Switch (Switchen) 🔀**
- Som en förlängningssladd för nätverket
- Kopplar ihop många enheter med kablar
- Intelligent - skickar data bara till rätt enhet

**3. Access Point (AP) 📶**
- WiFi-sändare
- Gör det möjligt för trådlösa enheter att ansluta

**4. Modem 📞**
- Översätter signaler från internet till ditt nätverk
- Oftast inbyggd i routern nuförtiden

### 🌐 Privata vs Publika IP-adresser

**Privata IP-adresser** (endast i ditt hemnätverk):
- `192.168.0.0` - `192.168.255.255` (mest vanliga hemma)
- `10.0.0.0` - `10.255.255.255`
- `172.16.0.0` - `172.31.255.255`

**Publik IP-adress**:
- Den adress som internet ser
- Unik för din internetanslutning
- Exempel: `91.123.45.67`

### 🎯 Övningar - Nivå 2

**Övning 2.1: Hitta din IP-adress 🔍**

**På Windows:**
```bash
# Öppna Kommandotolken och skriv:
ipconfig

# Titta efter "IPv4 Address" - det är din lokala IP!
```

**På Mac/Linux:**
```bash
# Öppna Terminal och skriv:
ifconfig
# eller
ip addr show

# Titta efter "inet" följt av en IP-adress
```

**Facit**: Du borde se något som `192.168.1.X` eller `10.0.0.X`

**Övning 2.2: Hitta din publika IP-adress 🌍**
1. Gå till: https://whatismyipaddress.com/
2. Anteckna din publika IPv4-adress
3. Anteckna din IPv6-adress (om du har en)
4. **Fråga**: Varför är dessa olika från din lokala IP?

**Övning 2.3: Rita ett kontorsnätverk 🏢**

Rita ett litet kontorsnätverk med:
- 1 router ansluten till internet
- 1 switch
- 5 datorer
- 1 skrivare
- Ge alla enheter IP-adresser i intervallet `192.168.10.X`

**Facit**:
```
       Internet ☁️
           ↓
    [Router: 192.168.10.1]
           ↓
    [Switch: 192.168.10.2]
      ↙  ↓  ↓  ↓  ↘
    PC1 PC2 PC3 PC4 PC5 + Skrivare
    .10 .11 .12 .13 .14    .15
```

**Övning 2.4: Pinga en enhet! 🏓**

Ping är som att ropa "Hallå!" till en enhet och vänta på svar.

```bash
# Pinga Google (Windows/Mac/Linux)
ping google.com

# Pinga din router (byt ut med din routers IP)
ping 192.168.1.1

# För att stoppa ping: tryck Ctrl+C
```

**Vad ska du se?**
- Tiden det tar för svar (i millisekunder)
- Om paketen kommer fram (0% packet loss = bra!)

**Bonus**: Pinga din egen dator med `ping localhost` eller `ping 127.0.0.1`

---

## 🔬 Nivå 3: Nätverksprotokoll och Verktyg - Teknisk Förståelse

Nu går vi djupare! Här lär du dig hur data faktiskt färdas genom nätverket.

### 📚 OSI-modellen: Nätverkets 7 Lager

OSI-modellen är som ett recept i 7 steg för hur data skickas över nätverk:

```
OSI-MODELLEN (7 lager)
═══════════════════════════════════════
7. APPLIKATION    📱  [HTTP, FTP, Email]
   "Vad användaren ser"
───────────────────────────────────────
6. PRESENTATION   🎨  [Kryptering, Komprimering]
   "Översättning & formatering"
───────────────────────────────────────
5. SESSION        🤝  [Startar/avslutar förbindelser]
   "Håller konversationen igång"
───────────────────────────────────────
4. TRANSPORT      🚚  [TCP, UDP]
   "Säkerställer leverans"
───────────────────────────────────────
3. NÄTVERK        🗺️  [IP, Routing]
   "Hittar vägen"
───────────────────────────────────────
2. DATALÄNK       🔗  [MAC-adresser, Switch]
   "Hoppar mellan närliggande enheter"
───────────────────────────────────────
1. FYSISK         ⚡  [Kablar, WiFi-signaler]
   "Den faktiska signalen"
═══════════════════════════════════════
```

**🎯 Minnesregel (Engelska):**
"**P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way"
(Physical, Data Link, Network, Transport, Session, Presentation, Application)

**🎯 Minnesregel (Svenska):**
"**F**ar **D**u **N**ågon **T**revlig **S**ak **P**å **A**lltid"
(Fysisk, Datalänk, Nätverk, Transport, Session, Presentation, Applikation)

### 🌐 TCP/IP-modellen: Den Praktiska Modellen

I verkligheten använder internet **TCP/IP-modellen** (4 lager):

```
TCP/IP-MODELLEN vs OSI
════════════════════════════════════════════
TCP/IP                    OSI
────────────────────────────────────────────
4. APPLIKATION    ←→  7. Applikation
                  ←→  6. Presentation
                  ←→  5. Session
────────────────────────────────────────────
3. TRANSPORT      ←→  4. Transport
   [TCP/UDP]
────────────────────────────────────────────
2. INTERNET       ←→  3. Nätverk
   [IP]
────────────────────────────────────────────
1. LÄNK           ←→  2. Datalänk
                  ←→  1. Fysisk
════════════════════════════════════════════
```

### 🔄 Dataflöde: Hur ett Webbsidbesök Fungerar

När du besöker `www.google.com`:

```
DIN DATOR                                    GOOGLES SERVER
═════════════════════════════════════════════════════════════
1. Du skriver www.google.com i webbläsaren
   │
2. DNS-förfrågan: "Vad är IP:n för google.com?"
   ├──→ DNS-server → Svar: 142.250.74.78
   │
3. TCP-handskakning (3-stegs):
   ├──→ SYN (Hej, kan vi prata?)         ──────→
   ←──── SYN-ACK (Ja, vi kan!)          ←──────┤
   ├──→ ACK (Perfekt, här kommer data!) ──────→
   │
4. HTTP-förfrågan skickas:
   ├──→ GET / HTTP/1.1                  ──────→
   │    Host: www.google.com
   │
5. Google skickar tillbaka HTML:
   ←──── HTTP/1.1 200 OK                ←──────┤
   ←──── <html>...</html>               ←──────┤
   │
6. Din webbläsare visar sidan! 🎉
```

### 🛠️ Wireshark: Se Nätverkstrafiken

**Wireshark** är som röntgenglasögon för nätverk - du kan se ALLA paket som färdas!

**Installera Wireshark:**
- Windows/Mac/Linux: https://www.wireshark.org/download.html

**Grundläggande användning:**

```
STEG 1: Välj nätverkskort
┌─────────────────────────────────┐
│ ☑ WiFi (wlan0)                  │
│ ☐ Ethernet (eth0)               │
│ ☐ Loopback (lo)                 │
└─────────────────────────────────┘

STEG 2: Klicka "Start" och se paketen flöda!

WIRESHARK-FÖNSTER:
╔════════════════════════════════════════════╗
║ Filter: http or dns                        ║
╠════════════════════════════════════════════╣
║ Nr  | Tid   | Källa        | Dest         ║
║ 1   | 0.000 | 192.168.1.10 | 8.8.8.8      ║ DNS
║ 2   | 0.023 | 8.8.8.8      | 192.168.1.10 ║ DNS Reply
║ 3   | 0.050 | 192.168.1.10 | 142.250.74.78║ TCP SYN
║ 4   | 0.089 | 142.250.74.78| 192.168.1.10 ║ TCP SYN-ACK
╚════════════════════════════════════════════╝
```

**Användbara filter i Wireshark:**
```
http              # Visa endast HTTP-trafik
dns               # Visa endast DNS-förfrågningar
ip.addr == 192.168.1.10  # Trafik till/från specifik IP
tcp.port == 80    # HTTP-trafik (port 80)
tcp.port == 443   # HTTPS-trafik (krypterad)
```

### 🎯 Övningar - Nivå 3

**Övning 3.1: OSI-lagerMatchning 🎮**

Matcha protokollet med rätt OSI-lager:

1. HTTP         → ?
2. Ethernet     → ?
3. IP           → ?
4. TCP          → ?
5. WiFi-signal  → ?

**Facit:**
1. HTTP → Lager 7 (Applikation)
2. Ethernet → Lager 2 (Datalänk)
3. IP → Lager 3 (Nätverk)
4. TCP → Lager 4 (Transport)
5. WiFi-signal → Lager 1 (Fysisk)

**Övning 3.2: Utforska med Wireshark 🔬**

1. Installera Wireshark
2. Starta en capture på ditt WiFi-kort
3. Öppna en webbläsare och gå till http://example.com
4. Stoppa capture
5. Filtrera på `http`
6. **Hitta**: GET-requesten till example.com

**Bonus**: Kan du se HTML-koden som servern skickar tillbaka?

**Övning 3.3: DNS-lookup 🔍**

Använd kommandot `nslookup` för att hitta IP-adresser:

```bash
# Hitta IP:n för google.com
nslookup google.com

# Hitta IP:n för youtube.com
nslookup youtube.com

# Använd en specifik DNS-server (Google DNS)
nslookup google.com 8.8.8.8
```

**Frågor:**
- Vilken IP fick du för google.com?
- Fick du flera IP-adresser? Varför?

**Övning 3.4: Traceroute - Följen Paketets Resa 🗺️**

Se vilka routrar ditt paket hoppar genom:

```bash
# Windows
tracert google.com

# Mac/Linux
traceroute google.com
```

**Du kommer att se:**
```
Traceroute till google.com (142.250.74.78)
 1  192.168.1.1     (Din router)         1 ms
 2  10.0.0.1        (ISP:s router)       5 ms
 3  194.123.45.1    (ISP:s gateway)     12 ms
 4  ...
 ...
15  142.250.74.78   (Google!)           22 ms
```

**Frågor:**
- Hur många "hopp" tog det att nå Google?
- Vilken var den långsammaste hoppet?

**Övning 3.5: Portskanning med nmap 🔐**

⚠️ **OBS**: Skanna endast DINA EGNA enheter! Att skanna andras nätverk utan tillåtelse är olagligt.

```bash
# Installera nmap först (Google för instruktioner)

# Skanna din egen dator
nmap localhost

# Skanna din router
nmap 192.168.1.1

# Detaljerad skanning med OS-detection
nmap -A 192.168.1.1
```

**Du kommer att se:**
```
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https
```

**Frågor:**
- Vilka portar är öppna på din router?
- Vad används port 22 till? (Tips: SSH)

---

## 🎓 Nivå 4: Avancerad Routing och Modern Teknik - Professionell Nivå

Nu blir det riktigt avancerat! Här lär du dig hur stora nätverk och företag bygger sina infrastrukturer.

### 🗺️ Routing-protokoll: Hitta Bästa Vägen

**Statisk vs Dynamisk Routing:**

```
STATISK ROUTING (Manuell)
═══════════════════════════════════
Router A: "För att nå 10.0.2.0/24,
           skicka via 192.168.1.1"

+ Fördelar: Säkrare, förutsägbar
- Nackdelar: Manuellt arbete, skalar inte
═══════════════════════════════════

DYNAMISK ROUTING (Automatisk)
═══════════════════════════════════
Routrar pratar med varandra:
"Jag kan nå nätverk X via väg Y med kostnad Z"

+ Fördelar: Automatisk, skalar bra
- Nackdelar: Mer komplex, overhead
═══════════════════════════════════
```

### 🔄 OSPF (Open Shortest Path First)

OSPF använder **Dijkstra's algoritm** för att hitta kortaste vägen:

```
OSPF-EXEMPEL: Hitta vägen från A till E
════════════════════════════════════════

        (2)
    B ─────── C
   /│         │╲
(1)/ │(3)     │ ╲(2)
  /  │        │  ╲
 A   │    (4) │   E
  ╲  │        │  ╱
(5)╲ │(1)     │ ╱(6)
    ╲│        │╱
     D ─────── F
        (1)

Kostnader i parentes = "metric" (oftast baserat på bandbredd)

OSPF beräknar:
Väg 1: A→B→C→E = 1+2+2 = 5  ✓ BÄST!
Väg 2: A→D→F→E = 5+1+6 = 12
Väg 3: A→B→D→F→E = 1+3+1+6 = 11

OSPF väljer: A→B→C→E
```

**OSPF-konfiguration (Cisco IOS):**

```ios
! Aktivera OSPF process 1
router ospf 1
  ! Sätt router-ID
  router-id 1.1.1.1

  ! Annonsera nätverk 192.168.1.0/24 i area 0 (backbone)
  network 192.168.1.0 0.0.0.255 area 0

  ! Annonsera nätverk 10.0.0.0/8 i area 0
  network 10.0.0.0 0.255.255.255 area 0

! Aktivera OSPF på interface
interface GigabitEthernet0/0
  ip ospf 1 area 0
  ! Sätt kostnad manuellt (valfritt)
  ip ospf cost 10
```

### 🌍 BGP (Border Gateway Protocol) - Internets Backbone

BGP är protokollet som håller ihop internet! Det används mellan olika autonoma system (AS).

```
INTERNET-STRUKTUR MED BGP
═════════════════════════════════════════

    AS 100          AS 200          AS 300
   (Telia)         (Tele2)        (Google)
      │               │               │
      │  BGP-peer    │   BGP-peer    │
      ├──────────────┼───────────────┤
      │              │               │
   ┌──┴──┐        ┌──┴──┐        ┌──┴──┐
   │ BGP │←──────→│ BGP │←──────→│ BGP │
   │ RTR │        │ RTR │        │ RTR │
   └──┬──┘        └──┬──┘        └──┬──┘
      │              │               │
   Kunder         Kunder          Servrar
```

**BGP-konfiguration (Förenklad):**

```ios
! Konfigurera BGP med AS-nummer 65001
router bgp 65001
  ! Sätt router-ID
  bgp router-id 1.1.1.1

  ! Definiera granne (peer) i AS 65002
  neighbor 203.0.113.1 remote-as 65002
  neighbor 203.0.113.1 description "Peer till ISP"

  ! Annonsera våra nätverk
  network 192.168.0.0 mask 255.255.0.0

  ! Aktivera address-family för IPv6
  address-family ipv6
    neighbor 2001:db8::1 remote-as 65002
    network 2001:db8::/32
  exit-address-family
```

### 📶 Wi-Fi 6 (802.11ax) och Wi-Fi 7 (802.11be)

**Wi-Fi Evolution:**

```
WIFI-GENERATIONER
═══════════════════════════════════════════════════════
Generation | Standard  | Max Hastighet | Frekvens
───────────┼───────────┼───────────────┼──────────────
Wi-Fi 4    | 802.11n   | 600 Mbps      | 2.4/5 GHz
Wi-Fi 5    | 802.11ac  | 3.5 Gbps      | 5 GHz
Wi-Fi 6    | 802.11ax  | 9.6 Gbps      | 2.4/5 GHz
Wi-Fi 6E   | 802.11ax  | 9.6 Gbps      | 2.4/5/6 GHz ⭐
Wi-Fi 7    | 802.11be  | 46 Gbps       | 2.4/5/6 GHz 🚀
═══════════════════════════════════════════════════════
```

**Wi-Fi 6/7 Nyckelfunktioner:**

🔹 **OFDMA** (Orthogonal Frequency Division Multiple Access)
```
GAMMALT (Wi-Fi 5):
En användare åt gången per kanal
[User 1] [User 2] [User 3] → Väntar i kö

NYTT (Wi-Fi 6+):
Flera användare samtidigt!
[U1|U2|U3|U4] → Alla samtidigt!
```

🔹 **MU-MIMO** (Multi-User Multiple Input Multiple Output)
- Wi-Fi 5: 4 samtidiga strömmar (downlink)
- Wi-Fi 6: 8 samtidiga strömmar (up/downlink)
- Wi-Fi 7: 16 samtidiga strömmar!

🔹 **Target Wake Time (TWT)**
- IoT-enheter kan "sova" och vakna vid bestämda tider
- Sparar batteri på mobiler och smarta enheter

### 🎚️ QoS (Quality of Service) - Prioritera Trafik

QoS låter dig prioritera viktig trafik (ex. videomöten) över mindre viktig (ex. nedladdningar).

```
QOS-MODELL
═══════════════════════════════════════════════════════

PRIORITET    TYP              EXEMPEL           DSCP
─────────────────────────────────────────────────────
🔴 HÖGST     Voice            VoIP, Teams       EF (46)
🟠 HÖG       Video            Zoom, Streaming   AF41 (34)
🟡 MEDEL     Kritisk Data     ERP, Databaser    AF31 (26)
🟢 NORMAL    Standard         Webb, Email       AF21 (18)
🔵 LÅG       Bulk             Backups, FTP      AF11 (10)
⚫ LÄGST     Scavenger        Torrents          CS1 (8)
═══════════════════════════════════════════════════════
```

**QoS-konfiguration (Cisco):**

```ios
! Skapa class-map för att identifiera trafik
class-map match-any VOICE
  match ip dscp ef
  match protocol rtp

class-map match-any VIDEO
  match ip dscp af41
  match protocol zoom

! Skapa policy-map för att sätta åtgärder
policy-map WAN-QOS
  class VOICE
    priority percent 30        ! Ge 30% bandbredd till röst
  class VIDEO
    bandwidth percent 40       ! Ge 40% till video
  class class-default
    bandwidth percent 30       ! Resten får 30%
    random-detect             ! Aktivera WRED

! Applicera på interface
interface GigabitEthernet0/1
  service-policy output WAN-QOS
```

### 🏠 PROJEKT: Designa ett Optimalt Hemnätverk

**Scenario:** Du ska designa ett modernt hemnätverk för en familj på 4 personer med följande krav:

**Krav:**
- 2 våningar + källare
- 4 sovrum (alla vill ha bra WiFi)
- Hemmakontor (kräver stabil anslutning)
- Smart-hem enheter: 15 st
- Gaming-rum (låg latens viktigt!)
- 4K streaming i vardagsrummet

**Din Lösning Ska Innehålla:**

```
DESIGNMALL
═══════════════════════════════════════════════

1. TOPOLOGI-DIAGRAM
   ┌─────────────────────────────────────────┐
   │  Internet (1 Gbps fiber)                │
   │            ↓                            │
   │      [Huvudrouter]                      │
   │       /    |    ╲                       │
   │   [AP1]  [AP2]  [Switch]               │
   │                    ↓                    │
   │            [Gaming PC, TV, etc.]       │
   └─────────────────────────────────────────┘

2. IP-PLAN
   VLAN 10: Familj        192.168.10.0/24
   VLAN 20: Gäster        192.168.20.0/24
   VLAN 30: IoT (Smart)   192.168.30.0/24
   VLAN 40: Management    192.168.40.0/24

3. UTRUSTNING
   - Router: _______
   - Access Points: _______
   - Switch: _______
   - Kablar: _______

4. QOS-KONFIGURATION
   - Gaming: Högsta prioritet
   - Streaming: Hög prioritet
   - Smart-hem: Normal prioritet

5. SÄKERHET
   - WiFi-kryptering: WPA3
   - Gästnätverk: Isolerat från huvud
   - IoT-nätverk: Begränsad åtkomst
   - Brandvägg: _______

6. BUDGET
   Total kostnad: _______ kr
═══════════════════════════════════════════════
```

**Rekommenderad Utrustning (2024-2025):**
- **Router:** UniFi Dream Machine Pro (ca 5000 kr)
- **Access Points:** 2x UniFi U6 Pro (ca 3500 kr st)
- **Switch:** UniFi Switch 8 PoE (ca 2500 kr)
- **Kablar:** Cat 6A (ca 15 kr/meter)

### 🎯 Övningar - Nivå 4

**Övning 4.1: OSPF-beräkning 🧮**

Givet följande nätverk, beräkna kortaste vägen från Router A till Router F:

```
     (10)      (5)
  B ───── C ───── D
 /│       │       │╲
/ │       │       │ ╲
A  │(20)  │(15)   │  F
╲  │      │       │ /
 ╲│       │       │/
  E ───── G ───── H
    (5)     (10)   (5)

A-B: 10, A-E: 30
```

**Hitta:**
1. Kortaste vägen från A till F
2. Vad händer om länken C-D går ner?
3. Vilken alternativ väg väljer OSPF?

**Facit:**
1. A→B→C→D→F = 10+10+5+5 = 30
2. Om C-D är ner, omdirigeras trafik
3. Alternativ: A→B→C→G→H→F = 10+10+15+10+5 = 50

**Övning 4.2: Konfigurera VLAN 🏢**

Skapa 3 VLAN på en Cisco-switch:
- VLAN 10: Personal (192.168.10.0/24)
- VLAN 20: Gäster (192.168.20.0/24)
- VLAN 30: Servrar (192.168.30.0/24)

```ios
! Din konfiguration här:
! Skapa VLANs
vlan 10
  name Personal
vlan 20
  name Gaster
vlan 30
  name Servrar

! Konfigurera access-port (för en dator i Personal)
interface FastEthernet0/1
  switchport mode access
  switchport access vlan 10
  spanning-tree portfast

! Konfigurera trunk-port (till router)
interface GigabitEthernet0/1
  switchport mode trunk
  switchport trunk allowed vlan 10,20,30
```

**Övning 4.3: WiFi-analys med inSSIDer eller WiFi Analyzer 📶**

1. Ladda ner WiFi Analyzer (Android) eller inSSIDer (Windows)
2. Skanna ditt område
3. **Identifiera:**
   - Vilken kanal använder ditt WiFi?
   - Hur många andra nätverk ser du?
   - Vilken kanal har minst interferens?
   - Vilken signalstyrka har du i olika rum? (dBm)

**Optimal kanal-planering:**
```
2.4 GHz: Använd kanal 1, 6, eller 11 (överlappar inte!)
5 GHz: Många fler kanaler tillgängliga (36, 40, 44, etc.)
```

**Övning 4.4: Packet Tracer Lab - Bygg ett Företagsnätverk 🏗️**

**Verktyg:** Cisco Packet Tracer (gratis från Cisco NetAcad)

**Uppgift:**
1. Skapa ett nätverk med:
   - 1 router
   - 2 switches
   - 6 datorer (3 per switch)
   - 1 server

2. Konfigurera:
   - IP-adresser: 192.168.1.0/24
   - Gateway: 192.168.1.1

3. Testa:
   - Pinga mellan alla datorer
   - Pinga servern från alla datorer
   - Verifiera med `show ip interface brief`

**Övning 4.5: Felsökning - Nätverket Fungerar Inte! 🔧**

**Scenario:** En användare klagar på att de inte kan nå internet. Gå igenom felsökningen steg-för-steg:

```
FELSÖKNINGSFLÖDE
═════════════════════════════════════════════

1. ✓ Fysiskt lager
   └─→ Är kabeln inkopplad?
   └─→ Lyser länklampan?
   └─→ ipconfig / ifconfig visar IP?

2. ✓ Datalänk-lager
   └─→ Rätt VLAN?
   └─→ Switch-port aktiverad?

3. ✓ Nätverkslager
   └─→ Har enheten IP-adress?
   └─→ Rätt subnät?
   └─→ Kan pinga gateway? (ping 192.168.1.1)

4. ✓ DNS
   └─→ Kan pinga IP men inte namn?
   └─→ nslookup google.com fungerar?
   └─→ DNS-server konfigurerad? (8.8.8.8)

5. ✓ Internet
   └─→ Kan pinga extern IP? (ping 8.8.8.8)
   └─→ Routern har anslutning?

VANLIGA LÖSNINGAR:
- Ingen IP → DHCP-server nere? Sätt statisk IP
- Kan pinga IP men inte namn → DNS-problem
- Kan pinga gateway men inte internet → Router-problem
═════════════════════════════════════════════
```

**Övning 4.6: QoS-simulering 📊**

Använd GNS3 eller Packet Tracer:
1. Skapa nätverk med begränsad bandbredd (10 Mbps)
2. Kör samtidig trafik:
   - VoIP-samtal
   - Video-streaming
   - Stor filöverföring
3. Mät latens och jitter utan QoS
4. Implementera QoS (prioritera VoIP)
5. Mät igen - se förbättringen!

**Förväntat resultat:**
```
UTAN QoS:
VoIP: 150ms latens, 50ms jitter ❌ (dåligt)
Video: Buffrar ofta ❌

MED QoS:
VoIP: 20ms latens, 5ms jitter ✅ (bra!)
Video: Smidig uppspelning ✅
```

**Övning 4.7: IPv6-konfiguration 🌐**

Konfigurera IPv6 på en Cisco-router:

```ios
! Aktivera IPv6 globalt
ipv6 unicast-routing

! Konfigurera interface med IPv6
interface GigabitEthernet0/0
  ! Statisk IPv6-adress
  ipv6 address 2001:db8:acad:1::1/64

  ! Aktivera IPv6 automatisk konfiguration
  ipv6 address autoconfig

  ! Aktivera IPv6 SLAAC för klienter
  ipv6 nd prefix 2001:db8:acad:1::/64

  no shutdown

! Verifiera
show ipv6 interface brief
show ipv6 route
```

**Testa:**
```bash
# Pinga IPv6 (Windows/Linux)
ping6 2001:db8:acad:1::1

# Visa din IPv6-adress
ipconfig (Windows)
ip -6 addr (Linux)
```

---

## 🚀 Nivå 5: Expert-nivå och Framtidsteknologi - Cutting Edge

Välkommen till expertvärlden! Här utforskar vi de senaste teknologierna och hur företag i världsklass bygger sina nätverk.

### 🔐 Zero Trust Network Architecture (2023-2025)

**Traditionell säkerhet:** "Trust but verify" (Lita men verifiera)
**Zero Trust:** "Never trust, always verify" (Lita aldrig, verifiera alltid)

```
ZERO TRUST-MODELLEN
═══════════════════════════════════════════════════════════

GAMMALT (Perimeter Security)
┌───────────────────────────────────┐
│  🏢 Företagsnätverk (Trusted)    │
│  ┌─────┐  ┌─────┐  ┌─────┐      │
│  │ PC  │  │ PC  │  │ PC  │      │ ✅ Alla betrodda
│  └─────┘  └─────┘  └─────┘      │
│                                   │
└───────────────────────────────────┘
        │🔥 Brandvägg
        ↓
   ☁️ Internet (Untrusted) ❌

PROBLEM: Om en enhet komprometteras, fritt tillträde inuti!

─────────────────────────────────────────────────────────

NYTT (Zero Trust)
      ☁️ Internet
        ↓
   🔐 Identity Provider (IdP)
        ↓
┌──────┴──────────────────────────────┐
│  ALLA enheter måste autentisera     │
│  ┌─────┐  ┌─────┐  ┌─────┐         │
│  │ PC  │  │ PC  │  │ PC  │         │
│  └──┬──┘  └──┬──┘  └──┬──┘         │
│     │🔐    │🔐    │🔐              │
│  Verify  Verify  Verify             │
└─────────────────────────────────────┘

VARJE åtkomst verifieras:
✓ Vem är du? (MFA)
✓ Vilken enhet? (Device posture)
✓ Varifrån? (Geo-location)
✓ Vad vill du göra? (Least privilege)
═══════════════════════════════════════════════════════════
```

**Implementera Zero Trust med Cisco:**

```ios
! ISE (Identity Services Engine) Integration
aaa new-model
aaa authentication login default group radius
aaa authorization network default group radius

radius server ISE
  address ipv4 10.1.1.10 auth-port 1812 acct-port 1813
  key SuperSecretKey123

! TrustSec (Cisco's Zero Trust-lösning)
cts credentials id MyDevice password Cisco123
cts authorization list ISE

! MACsec-kryptering mellan switches (802.1AE)
interface GigabitEthernet1/0/1
  macsec network-link
  mka pre-shared-key key-chain MKA-KEY

! Device posture - Kontrollera om enheten är säker
ip access-list extended POSTURE-CHECK
  permit ip any any

! Micro-segmentation med SDA (Software-Defined Access)
vlan 100
  name Trusted-Devices
vlan 101
  name Quarantine
```

### 🤖 AI och Machine Learning i Nätverk

AI revolutionerar nätverkshantering:

**1. Predictive Analytics (Förutsägande Analys)**
```
AI-DRIVEN NÄTVERKSHANTERING
═══════════════════════════════════════════

TRADITIONELLT:
Problem → Larm → Tekniker fixar → Upprepas
         ⏰ Reaktivt

AI-DRIVEN:
Data → ML-modell → Förutsäger problem → Auto-fix
      🤖 Proaktivt

EXEMPEL:
┌──────────────────────────────────────────┐
│ Mönster upptäckt:                        │
│ "Varje fredag kl 14:00 ökar trafik 300%" │
│                                           │
│ AI-åtgärd:                               │
│ → Öka bandbredd automatiskt kl 13:55    │
│ → Skala upp servrar i molnet            │
│ → Optimera routing för bästa prestanda  │
└──────────────────────────────────────────┘
```

**2. Anomaly Detection (Avvikelsedetektering)**

```python
# Exempel: Enkel anomaly detection med Python
import numpy as np
from sklearn.ensemble import IsolationForest

# Nätverkstrafik-data (bytes per sekund)
normal_trafik = [1000, 1200, 1100, 1050, 1300, 1150]
dagens_trafik = [1100, 1250, 15000, 1200, 1100]  # 15000 = anomali!

# Träna modell
model = IsolationForest(contamination=0.1)
model.fit(np.array(normal_trafik).reshape(-1, 1))

# Detektera avvikelser
for trafik in dagens_trafik:
    prediction = model.predict([[trafik]])
    if prediction == -1:
        print(f"🚨 ANOMALI UPPTÄCKT: {trafik} bytes/s")
        print("Möjlig DDoS-attack eller trafikspike!")
```

**AI-driven verktyg:**
- **Cisco DNA Center:** AI-driven nätverksautomation
- **Juniper Mist AI:** WiFi-optimering med ML
- **Aruba NetInsight:** Prediktiv analys

### 📡 5G och Edge Computing

5G och edge computing förändrar nätverksarkitekturen:

```
5G NETWORK ARCHITECTURE
═══════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────┐
│              5G CORE (Cloud)                        │
│  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐           │
│  │ AMF  │  │ SMF  │  │ UPF  │  │ AUSF │           │
│  └──────┘  └──────┘  └──────┘  └──────┘           │
└────────────────────┬────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
   ┌────▼───┐   ┌───▼────┐   ┌──▼─────┐
   │  Edge  │   │  Edge  │   │  Edge  │
   │  DC 1  │   │  DC 2  │   │  DC 3  │
   └────┬───┘   └───┬────┘   └──┬─────┘
        │           │            │
     ┌──▼──┐     ┌─▼──┐      ┌─▼──┐
     │ 5G  │     │ 5G │      │ 5G │
     │ gNB │     │ gNB│      │ gNB│
     └──┬──┘     └─┬──┘      └─┬──┘
        📱         📱          📱
     Enheter    Enheter    Enheter

5G NYCKELFUNKTIONER:
─────────────────────────────────────────────────────
• eMBB (Enhanced Mobile Broadband): 10+ Gbps
• URLLC (Ultra-Reliable Low Latency): <1ms latens
• mMTC (Massive IoT): 1 miljon enheter/km²
═══════════════════════════════════════════════════════
```

**Network Slicing** - Virtuella nätverk i 5G:

```
NETWORK SLICING
═══════════════════════════════════════════════════

         5G RAN (Radio Access Network)
              │
    ┌─────────┼─────────┐
    │         │         │
┌───▼───┐ ┌──▼────┐ ┌──▼─────┐
│ Slice │ │ Slice │ │ Slice  │
│   1   │ │   2   │ │   3    │
└───┬───┘ └──┬────┘ └──┬─────┘
    │        │         │
  📱 IoT   📹Video   🚗Auto

  Low       High      Ultra
  power     speed     reliable
  Long      4K        <1ms
  battery   stream    latency
```

### ☁️ Software-Defined Networking (SDN) & Cloud

SDN separerar kontroll-planet från data-planet:

```
TRADITIONELLT NÄTVERK vs SDN
═══════════════════════════════════════════════════════

TRADITIONELLT:
┌─────────────────────────────────────────┐
│  Router 1: Kontroll + Data              │
│  [Beslutar OCH Vidarebefordrar]         │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│  Router 2: Kontroll + Data              │
└─────────────────────────────────────────┘
   ❌ Svårt att hantera många routrar individuellt

SDN:
┌──────────────────────────────────────────┐
│  SDN CONTROLLER (Kontroll-plan)         │ 🧠 Centraliserad
│  [OpenDaylight, ONOS, Cisco ACI]        │    intelligens
└─────────────────┬────────────────────────┘
                  │ Southbound API
        ┌─────────┼─────────┐
        │         │         │
   ┌────▼───┐ ┌──▼────┐ ┌──▼─────┐
   │Switch 1│ │Switch2│ │Switch 3│  Data-plan
   │(Dumma) │ │(Dumma)│ │(Dumma) │ (Vidarebefordrar
   └────────┘ └───────┘ └────────┘  bara)

   ✅ Enkel central hantering!
═══════════════════════════════════════════════════════
```

**OpenFlow** - Protokollet som driver SDN:

```
OPENFLOW FLOW TABLE
═══════════════════════════════════════════════════════
Match Fields         | Priority | Actions
─────────────────────┼──────────┼─────────────────────
src_IP=192.168.1.0/24| 100      | Output: Port 1
dst_IP=10.0.0.1      | 200      | Output: Port 2
TCP port=80          | 150      | Drop (blockera HTTP)
IPv6 enabled         | 50       | Output: Port 3
═══════════════════════════════════════════════════════
```

**Python med Ryu SDN Controller:**

```python
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls

class SimpleSwitch(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(SimpleSwitch, self).__init__(*args, **kwargs)
        self.mac_to_port = {}  # MAC-adress → Port mapping

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        """Hanterar inkommande paket"""
        msg = ev.msg
        datapath = msg.datapath
        parser = datapath.ofproto_parser

        # Extrahera MAC-adresser
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        dst = eth.dst
        src = eth.src

        # Lär dig MAC-adress → Port
        self.mac_to_port[src] = msg.in_port

        # Bestäm output port
        if dst in self.mac_to_port:
            out_port = self.mac_to_port[dst]
        else:
            out_port = ofproto.OFPP_FLOOD  # Broadcast om okänd

        # Installera flow i switchen
        match = parser.OFPMatch(in_port=msg.in_port, eth_dst=dst)
        actions = [parser.OFPActionOutput(out_port)]
        self.add_flow(datapath, 1, match, actions)
```

### 🏢 CASE STUDY 1: Google's Global Network

**Googles B4 SDN-nätverk:**

```
GOOGLE B4 - VÄRLDENS STÖRSTA SDN
═══════════════════════════════════════════════════════

Problem: Traditionella routrar för dyra för Googles
         enorma datautbyte mellan datacenter

Lösning: Bygg eget SDN med billig hårdvara!

ARKITEKTUR:
┌──────────────────────────────────────────────────┐
│  Global TE (Traffic Engineering) Server          │ 🧠
│  [Centraliserad kontroll av ALL trafik]          │
└───────────────────┬──────────────────────────────┘
                    │
     ┌──────────────┼──────────────┐
     │              │              │
┌────▼────┐    ┌───▼─────┐   ┌───▼─────┐
│ DC USA  │    │ DC Eur  │   │ DC Asia │
│ (1 Tbps)│────│(1 Tbps) │───│(1 Tbps) │
└─────────┘    └─────────┘   └─────────┘

RESULTAT:
• 70% bättre länk-utnyttjande
• Nästan 100% tillgänglighet
• Kostnadsbesparing: Miljarder USD
═══════════════════════════════════════════════════════
```

**Lärdomar:**
✅ SDN möjliggör centraliserad optimering
✅ Billig hårdvara + smart mjukvara = Kostnadseffektivt
✅ Automation är nyckeln till stor skala

### 🏢 CASE STUDY 2: Cisco's DNA Architecture

**Cisco DNA Center** - Intent-Based Networking:

```
CISCO DNA CENTER
═══════════════════════════════════════════════════════

1. INTENT (Avsikt):
   "Jag vill att VIP-gäster får högsta prioritet på WiFi"

2. DNA CENTER ÖVERSÄTTER:
   ┌────────────────────────────────────┐
   │ • Skapa SSID "VIP-Guest"           │
   │ • Tilldela QoS-profil "Platinum"   │
   │ • Konfigurera alla AP:er           │
   │ • Aktivera FastLane                │
   │ • Sätt upp analytics               │
   └────────────────────────────────────┘

3. AUTOMATION:
   DNA Center konfigurerar automatiskt:
   ✓ 150 Access Points
   ✓ 25 Switches
   ✓ 5 WLC (Wireless Controllers)

   Tid: 5 minuter (vs. 2 dagar manuellt!)

4. ASSURANCE:
   DNA Center övervakar kontinuerligt:
   📊 Vilka klienter har problem?
   🔍 AI-driven felsökning
   🤖 Auto-remediation
═══════════════════════════════════════════════════════
```

### 🌩️ Multi-Cloud Networking (AWS, Azure, GCP)

**Anslut flera moln-providers:**

```
MULTI-CLOUD ARKITEKTUR
═══════════════════════════════════════════════════════

     🏢 On-Premise Datacenter
            │
    ┌───────┼───────┐
    │   SD-WAN      │ (Cisco Viptela, VMware VeloCloud)
    └───────┬───────┘
            │
    ┌───────┼──────────────┐
    │       │              │
┌───▼───┐ ┌─▼────┐   ┌────▼────┐
│  AWS  │ │Azure │   │  GCP    │
│  VPC  │ │ VNet │   │  VPC    │
└───┬───┘ └─┬────┘   └────┬────┘
    │       │             │
  Apps    Apps          Apps

INTERCONNECT-METODER:
─────────────────────────────────────────────────────
1. AWS Direct Connect    → Dedikerad 10Gbps länk
2. Azure ExpressRoute   → Privat anslutning
3. GCP Cloud Interconnect → Låg latens
4. Transit Gateway       → Hub för alla VPC:er
═══════════════════════════════════════════════════════
```

**Exempel: AWS VPC med Terraform:**

```hcl
# Skapa AWS VPC med Terraform
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "Production-VPC"
    Environment = "Prod"
  }
}

# Skapa subnät
resource "aws_subnet" "public" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "eu-north-1a"

  tags = {
    Name = "Public-Subnet-1"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "eu-north-1a"

  tags = {
    Name = "Private-Subnet-1"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
}

# Route Table för publik trafik
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

# VPN-anslutning till on-premise
resource "aws_vpn_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "OnPrem-VPN-Gateway"
  }
}
```

### 🎯 PROJEKT: Designa ett Säkert SDN-nätverk

**Scenario:** Du är nätverksarkitekt på ett medelstort företag (500 anställda) som ska migrera till SDN med Zero Trust-säkerhet.

**Krav:**
- 3 kontor (Stockholm, Göteborg, Malmö)
- 50% av anställda jobbar remote
- Kritiska applikationer i AWS
- Backup-system i Azure
- GDPR-compliance
- 99.99% uptime

**Din Design Ska Inkludera:**

```
PROJEKTMALL
═══════════════════════════════════════════════════════

1. ARKITEKTUR-DIAGRAM
   ┌─────────────────────────────────────────────────┐
   │                                                 │
   │  [Rita din SDN-arkitektur här]                  │
   │   - SD-WAN mellan kontor                       │
   │   - SDN Controller (OpenDaylight/Cisco)        │
   │   - Zero Trust-komponenter                     │
   │   - Multi-cloud kopplingar                     │
   │                                                 │
   └─────────────────────────────────────────────────┘

2. IP-ADRESSPLAN
   Stockholm:     10.1.0.0/16
   Göteborg:      10.2.0.0/16
   Malmö:         10.3.0.0/16
   Remote Users:  10.100.0.0/16
   AWS VPC:       172.16.0.0/16
   Azure VNet:    172.17.0.0/16

3. ZERO TRUST IMPLEMENTATION
   • Identity Provider: Okta/Azure AD
   • MFA: Mandatory för alla
   • Device Posture: Cisco ISE
   • Micro-segmentation: Varje app isolerad
   • Least Privilege: Rollbaserad åtkomst

4. SDN CONTROLLER-KONFIGURATION
   Controller: Cisco DNA Center / OpenDaylight

   Policies:
   - Prioritet 1: VoIP-trafik
   - Prioritet 2: Kritiska applikationer
   - Prioritet 3: Standard

   Automation:
   - Auto-provisioning av nya enheter
   - Self-healing vid fel
   - Dynamisk routing

5. SÄKERHETSLAGER
   ┌──────────────────────────────────┐
   │ 1. Perimeter: Next-Gen Firewall  │
   │ 2. Network: Micro-segmentation   │
   │ 3. Endpoint: EDR (CrowdStrike)   │
   │ 4. Application: WAF              │
   │ 5. Data: Encryption (TLS 1.3)    │
   └──────────────────────────────────┘

6. DISASTER RECOVERY
   • Redundanta internetlänkar (2x per kontor)
   • Automatisk failover (<30 sek)
   • Backup till Azure (daglig)
   • RTO: 4 timmar
   • RPO: 1 timme

7. MONITORING & ANALYTICS
   • Centraliserad logging (Splunk/ELK)
   • AI-driven anomaly detection
   • 24/7 SOC (Security Operations Center)
   • SLA-övervakning

8. BUDGET & TIMELINE
   Hårdvara:     X,XXX,XXX kr
   Mjukvara:     XXX,XXX kr
   Konsulter:    XXX,XXX kr
   Licenser/år:  XXX,XXX kr

   Timeline: 6 månader
   - Månad 1-2: Design & planering
   - Månad 3-4: Stockholm-implementation
   - Månad 5: Göteborg & Malmö
   - Månad 6: Testning & optimering
═══════════════════════════════════════════════════════
```

### 🎯 Övningar - Nivå 5

**Övning 5.1: Zero Trust Policy Design 🔐**

Designa Zero Trust-policies för följande användare:
1. CEO (VD) - Tillgång till allt, högrisk
2. Developer - Tillgång till Git, AWS, test-miljö
3. HR - Tillgång till lönesystem, känslig data
4. Guest/Consultant - Begränsad tillfällig åtkomst

**Skapa policy för varje:**
```
POLICY-MALL
──────────────────────────────────────
User: Developer
MFA: Required (Yubikey)
Device: Company laptop only
Location: Allow from: Office, Home VPN
Time: 08:00-18:00 (varning utanför)
Resources: Git, AWS Dev, Jira, Slack
Network Segment: VLAN 20 (Dev)
Logging: All access logged
──────────────────────────────────────
```

**Övning 5.2: SDN Lab med Mininet 🧪**

Installera och experimentera med SDN:

```bash
# Installera Mininet (Linux)
sudo apt-get install mininet

# Skapa enkelt nätverk med 4 hosts, 1 switch
sudo mn --topo single,4 --controller=remote

# I Mininet-CLI:
mininet> h1 ping h2
mininet> pingall
mininet> iperf h1 h2

# Koppla till Ryu Controller (separat terminal)
ryu-manager simple_switch.py
```

**Uppgift:**
1. Skapa topologi med 3 switches och 6 hosts
2. Implementera flow-regel som blockerar ping mellan h1 och h4
3. Mät bandbredd med iperf

**Övning 5.3: AWS VPC Design och Implementation ☁️**

Designa och implementera en produktionsklar AWS VPC:

```
ARKITEKTUR:
┌──────────────────────────────────────┐
│          AWS VPC 10.0.0.0/16         │
│  ┌────────────┐    ┌─────────────┐  │
│  │  Public    │    │  Private    │  │
│  │  Subnet    │    │  Subnet     │  │
│  │ (Web)      │    │ (App+DB)    │  │
│  └─────┬──────┘    └──────┬──────┘  │
│        │                   │         │
│   [Internet GW]      [NAT GW]       │
└────────┼─────────────────────────────┘
         │
     Internet ☁️
```

**Implementera med AWS CLI:**

```bash
# Skapa VPC
aws ec2 create-vpc --cidr-block 10.0.0.0/16

# Skapa subnät
aws ec2 create-subnet --vpc-id vpc-xxx \
  --cidr-block 10.0.1.0/24 --availability-zone eu-north-1a

# Skapa Internet Gateway
aws ec2 create-internet-gateway
aws ec2 attach-internet-gateway --vpc-id vpc-xxx --igw-id igw-xxx

# Skapa Security Group (brandvägg)
aws ec2 create-security-group --group-name web-sg \
  --description "Web servers" --vpc-id vpc-xxx

# Tillåt HTTP och HTTPS
aws ec2 authorize-security-group-ingress --group-id sg-xxx \
  --protocol tcp --port 80 --cidr 0.0.0.0/0
```

**Övning 5.4: Network Automation med Ansible 🤖**

Automatisera konfiguration av 10 Cisco-routrar:

```yaml
# playbook.yml
---
- name: Konfigurera Cisco-routrar
  hosts: routers
  gather_facts: no

  tasks:
    - name: Sätt hostname
      ios_config:
        lines:
          - hostname {{ inventory_hostname }}

    - name: Konfigurera NTP
      ios_config:
        lines:
          - ntp server 10.1.1.1
          - ntp server 10.1.1.2

    - name: Aktivera SSH
      ios_config:
        lines:
          - ip domain-name example.com
          - crypto key generate rsa modulus 2048
          - ip ssh version 2

    - name: Skapa VLAN
      ios_vlan:
        vlan_id: "{{ item.id }}"
        name: "{{ item.name }}"
      loop:
        - { id: 10, name: 'Data' }
        - { id: 20, name: 'Voice' }
        - { id: 30, name: 'Guest' }

    - name: Spara konfiguration
      ios_command:
        commands:
          - write memory
```

**Kör playbook:**
```bash
ansible-playbook -i inventory playbook.yml
```

**Övning 5.5: 5G Network Slicing Simulering 📡**

Simulera network slicing med OpenAirInterface:

**Scenario:** Skapa 3 slices:
1. **eMBB**: Bredband för konsumenter (High speed)
2. **URLLC**: Självkörande bilar (Ultra-low latency)
3. **mMTC**: IoT-sensorer (Massiv anslutning)

**Konfiguration (förenklad):**

```yaml
# network_slices.yaml
slices:
  - name: eMBB
    sst: 1  # Slice Service Type
    sd: 1   # Slice Differentiator
    qos:
      bandwidth: 100 Mbps
      latency: 20 ms
      reliability: 99.9%

  - name: URLLC
    sst: 2
    sd: 2
    qos:
      bandwidth: 10 Mbps
      latency: 1 ms      # Ultra-låg!
      reliability: 99.999%

  - name: mMTC
    sst: 3
    sd: 3
    qos:
      bandwidth: 1 Mbps
      latency: 100 ms
      reliability: 99%
      connection_density: 1000000/km²
```

**Övning 5.6: AI-baserad Nätverksanomali-detektion 🤖**

Bygg en ML-modell för att detektera DDoS-attacker:

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Ladda nätverks-trafik data (exempel)
data = pd.read_csv('network_traffic.csv')

# Features: packets/sec, bytes/sec, unique_IPs, etc.
X = data[['packets_per_sec', 'bytes_per_sec', 'unique_ips',
          'tcp_flags', 'avg_packet_size']]
y = data['is_attack']  # 0 = Normal, 1 = Attack

# Dela data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Träna Random Forest
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluera
accuracy = model.score(X_test, y_test)
print(f"Noggrannhet: {accuracy * 100:.2f}%")

# Real-time detektion
def detect_attack(live_traffic):
    """Detektera DDoS i realtid"""
    features = [[
        live_traffic['packets_per_sec'],
        live_traffic['bytes_per_sec'],
        live_traffic['unique_ips'],
        live_traffic['tcp_flags'],
        live_traffic['avg_packet_size']
    ]]

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        print(f"🚨 ATTACK DETECTED! Sannolikhet: {probability*100:.1f}%")
        # Trigga automatisk mitigation
        block_malicious_ips(live_traffic)
    else:
        print("✅ Trafik ser normal ut")

# Exempel-användning
live_data = {
    'packets_per_sec': 50000,  # Ovanligt högt!
    'bytes_per_sec': 5000000,
    'unique_ips': 1000,        # Många IPs = DDoS?
    'tcp_flags': 2,            # SYN flood?
    'avg_packet_size': 64
}

detect_attack(live_data)
```

**Övning 5.7: Kubernetes Network Policies 🐳**

Implementera micro-segmentation i Kubernetes:

```yaml
# network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  - Egress

  ingress:
  # Tillåt endast från frontend
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080

  egress:
  # Tillåt endast till databas
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432

  # Tillåt DNS
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: UDP
      port: 53
```

**Applicera:**
```bash
kubectl apply -f network-policy.yaml

# Verifiera
kubectl get networkpolicies -n production
kubectl describe networkpolicy backend-policy -n production
```

**Övning 5.8: Intent-Based Networking (IBN) 🎯**

Skapa intent-baserade policies:

```yaml
# intent.yaml - Cisco DNA Center
intents:
  - name: "Guest WiFi Isolation"
    description: "Gäster ska inte kunna nå interna resurser"

    conditions:
      - user_group: "Guests"
      - ssid: "Guest-WiFi"

    actions:
      - isolate_from: ["Corporate-VLAN", "Server-VLAN"]
      - allow_to: ["Internet"]
      - qos_profile: "Bronze"
      - bandwidth_limit: "10 Mbps"
      - session_timeout: "4 hours"

  - name: "Executive Priority"
    description: "VIPs får alltid bästa service"

    conditions:
      - user_group: "Executives"

    actions:
      - qos_profile: "Platinum"
      - guarantee_bandwidth: "100 Mbps"
      - priority: "Highest"
      - path: "Fastest route"
```

**DNA Center översätter automatiskt till:**
- ACLs (Access Control Lists)
- QoS policies
- VLAN-konfigurationer
- Routing-ändringar

---

## 📊 Självutvärdering

Testa dina kunskaper! Besvara ärligt vilken nivå du är på:

### Nivå 1 - Grundläggande Förståelse ✅
- [ ] Jag förstår vad ett nätverk är med hjälp av analogier
- [ ] Jag kan identifiera nätverksenheter hemma (router, laptop, etc.)
- [ ] Jag förstår grundkonceptet med att skicka data

### Nivå 2 - Hemmanätverk 🏠
- [ ] Jag kan hitta min IP-adress
- [ ] Jag förstår skillnaden mellan lokal och publik IP
- [ ] Jag kan pinga andra enheter
- [ ] Jag kan rita mitt hemnätverk

### Nivå 3 - Teknisk Kompetens 🔬
- [ ] Jag förstår OSI-modellens 7 lager
- [ ] Jag kan använda Wireshark för att analysera trafik
- [ ] Jag förstår TCP/IP-protokollet
- [ ] Jag kan utföra traceroute och förstå resultatet
- [ ] Jag kan använda nmap för portskanning

### Nivå 4 - Professionell 🎓
- [ ] Jag förstår routing-protokoll (OSPF, BGP)
- [ ] Jag kan konfigurera VLANs
- [ ] Jag förstår QoS och kan prioritera trafik
- [ ] Jag kan designa ett företagsnätverk
- [ ] Jag förstår WiFi 6/7-teknologier
- [ ] Jag kan felsöka komplexa nätverksproblem

### Nivå 5 - Expert 🚀
- [ ] Jag förstår Zero Trust-arkitektur
- [ ] Jag kan designa SDN-lösningar
- [ ] Jag kan implementera multi-cloud networking
- [ ] Jag förstår 5G network slicing
- [ ] Jag kan använda AI/ML för nätverksoptimering
- [ ] Jag kan automatisera med Ansible/Terraform
- [ ] Jag förstår Kubernetes networking

**Din Poäng:**
- 0-5 ✅: Nivå 1 - Fortsätt lära!
- 6-10 🏠: Nivå 2 - Bra grundkunskaper!
- 11-15 🔬: Nivå 3 - Tekniskt kompetent!
- 16-22 🎓: Nivå 4 - Professionell nivå!
- 23+ 🚀: Nivå 5 - Du är en expert!

---

## ❓ FAQ - Vanliga Frågor

**1. Vad är skillnaden mellan en router och en switch?**
- **Router**: Kopplar samman olika nätverk (t.ex. ditt hemnätverk till internet). Arbetar på Lager 3 (Nätverk).
- **Switch**: Kopplar samman enheter inom samma nätverk. Arbetar på Lager 2 (Datalänk).

**2. Vilken IP-adress ska jag använda för mitt hemnätverk?**
Använd privata IP-intervall:
- `192.168.0.0/16` (mest vanligt för hem)
- `10.0.0.0/8` (för större nätverk)
- `172.16.0.0/12`

**3. Vad är bättre: WiFi eller kabel?**
- **Kabel (Ethernet)**: Snabbare, mer stabilt, säkrare. Bäst för gaming, streaming, servrar.
- **WiFi**: Bekvämt, flexibelt. Bra för mobila enheter.

**4. Hur säkrar jag mitt WiFi?**
1. Använd **WPA3** (eller minst WPA2)
2. Starkt lösenord (16+ tecken)
3. Dölj SSID (valfritt)
4. Separera gästnätverk
5. Uppdatera routerns firmware

**5. Vad är en god ping-tid?**
- **<20ms**: Utmärkt (gaming, real-time apps)
- **20-50ms**: Bra
- **50-100ms**: Acceptabelt
- **>100ms**: Långsamt (problem för gaming/VoIP)

**6. IPv4 vs IPv6 - behöver jag bry mig?**
Ja! IPv4-adresser tar slut. IPv6 är framtiden:
- **IPv4**: ~4 miljarder adresser (nästan slut)
- **IPv6**: 340 undeciljoner adresser (aldrig slut!)

**7. Vad är DNS och varför är det viktigt?**
DNS = "Internets telefonbok"
- Översätter `google.com` → `142.250.74.78`
- Utan DNS måste du komma ihåg IP-adresser!

**Snabba DNS-servrar:**
- Google: `8.8.8.8`, `8.8.4.4`
- Cloudflare: `1.1.1.1`, `1.0.0.1`
- Quad9: `9.9.9.9`

**8. Hur snabb internetuppkoppling behöver jag?**
- **Ensam, basic**: 10-25 Mbps
- **Familj, streaming**: 50-100 Mbps
- **Gaming, 4K**: 100-250 Mbps
- **Work from home, flera**: 250+ Mbps
- **Entusiast, 8K, server**: 1 Gbps+

**9. Vad är ett VPN och behöver jag ett?**
**VPN** (Virtual Private Network) krypterar din trafik.

**Använd VPN för:**
- ✅ Offentliga WiFi-nätverk
- ✅ Integritet från ISP
- ✅ Åtkomst till företagsnätverk remote

**Skippa VPN:**
- ❌ Om du litar på ditt nätverk
- ❌ Kan göra internet långsammare

**10. Hur felsöker jag "inget internet"?**

```
FELSÖKNINGSGUIDE
═══════════════════════════════════════
1. ✓ Fysiskt
   → Är kabeln inkopplad?
   → Lyser lamporna på routern?

2. ✓ Starta om
   → Stäng av router i 30 sek
   → Starta om din dator

3. ✓ Ping gateway
   → `ping 192.168.1.1`
   → Om det funkar: problemet är routern/ISP

4. ✓ Ping extern IP
   → `ping 8.8.8.8`
   → Om det funkar: DNS-problem

5. ✓ Ping domännamn
   → `ping google.com`
   → Om det funkar: allt ok!

6. ☎️ Kontakta ISP om inget funkar
═══════════════════════════════════════
```

---

## 📖 Ordlista - Svenska/Engelska

| 🇸🇪 Svenska | 🇬🇧 Engelska | 📝 Förklaring |
|-------------|--------------|---------------|
| Brandvägg | Firewall | Skyddar nätverk från oönskad trafik |
| Datacenter | Data Center | Stor anläggning med servrar |
| Datornätverk | Computer Network | System av sammanlänkade datorer |
| Datalänk | Data Link | OSI Lager 2 - länk mellan enheter |
| Datapaket | Data Packet | Enhet av data som skickas över nätverk |
| Flöde | Flow | Ström av datapaket mellan två punkter |
| Gateway | Gateway | Enhet som kopplar ihop olika nätverk |
| IP-adress | IP Address | Unik identifierare för nätverksenheter |
| Kryptering | Encryption | Skydda data med kodning |
| Latens | Latency | Fördröjning i nätverkskommunikation (ms) |
| Länk | Link | Förbindelse mellan två nätverkspunkter |
| Moln | Cloud | Internet-baserade datacenters |
| Nätverk | Network | Sammanlänkade datorer och enheter |
| Omdirigering | Routing | Välja väg för datapaket |
| Prioritering | Quality of Service (QoS) | Ge viktig trafik förtur |
| Router | Router | Dirigerar trafik mellan nätverk |
| Server | Server | Dator som tillhandahåller tjänster |
| Skalning | Scaling | Öka kapacitet när belastning ökar |
| Slicing | Network Slicing | Virtuella nätverk i 5G |
| Stigväxel | Switch | Kopplar samman enheter i samma nätverk |
| Styrplan | Control Plane | Beslutsfattande del av nätverk (SDN) |
| Subnät | Subnet | Delnätverk inom ett större nätverk |
| Tillgängspunkt | Access Point (AP) | WiFi-sändare |
| Trådlöst | Wireless (WiFi) | Nätverk utan kablar |
| Övervakning | Monitoring | Kontinuerlig kontroll av nätverksstatus |
| Zero Trust | Zero Trust | Säkerhetsmodell: "lita aldrig, verifiera alltid" |

---

## 📚 Rekommenderade Resurser

### Böcker 📖

1. **"Computer Networking: A Top-Down Approach"** av Kurose & Ross
   - Nivå: Nybörjare → Medel
   - Perfekt för att förstå grunderna
   - ISBN: 978-0135929360

2. **"TCP/IP Illustrated, Volume 1"** av W. Richard Stevens
   - Nivå: Medel → Avancerad
   - Djupdykning i TCP/IP-protokollen
   - ISBN: 978-0201633467

3. **"Routing TCP/IP, Volume 1"** av Jeff Doyle
   - Nivå: Avancerad
   - Fokus på OSPF, EIGRP
   - ISBN: 978-1587052026

4. **"Zero Trust Networks"** av Gilman & Barth
   - Nivå: Avancerad
   - Modern säkerhetsarkitektur
   - ISBN: 978-1491962190

5. **"Software Defined Networks: A Comprehensive Approach"** av Paul Goransson
   - Nivå: Avancerad → Expert
   - SDN och OpenFlow
   - ISBN: 978-0128045558

### Online-kurser 🎓

1. **Cisco NetAcad - CCNA**
   - URL: https://www.netacad.com/
   - Kostnad: Gratis
   - Nivå: Nybörjare → Medel

2. **Udemy - "The Complete Networking Fundamentals Course"**
   - Instruktör: David Bombal
   - Nivå: Nybörjare
   - Praktiska labs med Packet Tracer

3. **Coursera - "Google IT Support Professional Certificate"**
   - Inkluderar nätverksmodul
   - Nivå: Nybörjare
   - Gratis att granska, certifikat kostar

4. **Pluralsight - Network Engineering Path**
   - Nivå: Medel → Avancerad
   - Subscription-baserad

5. **LinkedIn Learning - Networking Foundations**
   - Nivå: Nybörjare
   - Bra för yrkesverksamma

### YouTube-kanaler 🎥

1. **NetworkChuck**
   - URL: https://www.youtube.com/c/NetworkChuck
   - Nivå: Alla nivåer
   - Roliga, pedagogiska videos om nätverk, säkerhet, Linux
   - ⭐ Rekommenderad för nybörjare!

2. **David Bombal**
   - Fokus: Cisco, automation, labs
   - Nivå: Medel → Avancerad

3. **Professor Messer**
   - Fokus: CompTIA Network+, certifieringar
   - Nivå: Nybörjare → Medel

4. **Eli the Computer Guy**
   - Fokus: Praktiska nätverksguider
   - Nivå: Nybörjare

5. **Keith Barker (CBT Nuggets)**
   - Fokus: Cisco CCNA/CCNP
   - Nivå: Medel → Avancerad

### Verktyg & Simulatorer 🛠️

1. **Cisco Packet Tracer**
   - Gratis nätverkssimulator
   - Perfekt för labb-övningar
   - https://www.netacad.com/courses/packet-tracer

2. **GNS3**
   - Avancerad nätverkssimulator
   - Stöd för riktiga router-images
   - https://www.gns3.com/

3. **Wireshark**
   - Paketanalys-verktyg
   - Gratis och open-source
   - https://www.wireshark.org/

4. **EVE-NG**
   - Enterprise network simulator
   - Nivå: Avancerad
   - https://www.eve-ng.net/

5. **Mininet**
   - SDN-simulering
   - Open-source
   - http://mininet.org/

### Communities & Forum 💬

1. **Reddit: r/networking**
   - Professionella nätverksingenjörer
   - Bra för frågor och diskussioner

2. **Cisco Learning Network**
   - Forum för Cisco-certifieringar
   - https://learningnetwork.cisco.com/

3. **NetworkEngineering Discord**
   - Real-time chat med nätverksproffs

4. **Stack Exchange - Network Engineering**
   - Frågor & svar
   - https://networkengineering.stackexchange.com/

---

## 🎉 Avslutning - Din Resa Börjar Nu!

Grattis! Du har nu gått igenom en omfattande guide om datornätverk, från de mest grundläggande koncepten till cutting-edge teknologier som 5G, AI och Zero Trust.

### 🗺️ Vart går du härifrån?

**Om du är nybörjare:**
1. ✅ Öva på övningarna i Nivå 1-2
2. 📦 Installera Packet Tracer och bygg enkla nätverk
3. 📺 Titta på NetworkChuck på YouTube
4. 📚 Läs "Computer Networking: A Top-Down Approach"

**Om du siktar på CCNA:**
1. 📖 Gå Cisco NetAcad CCNA-kursen (gratis!)
2. 🔬 Labba dagligen i Packet Tracer
3. 📝 Testa din kunskap med practice exams
4. 🎯 Boka CCNA-examen när du är redo (200-301)

**Om du vill bli nätverksingenjör:**
1. 💼 Skaffa praktisk erfarenhet (praktik, junior-roll)
2. 🏆 Certifiera dig (CCNA → CCNP)
3. 🔧 Bygg hemprojekt (homelab med fysisk eller virtuell utrustning)
4. 🌐 Bidra till open-source networking-projekt
5. 📰 Håll dig uppdaterad (följ Cisco, Juniper, Arista blogs)

**Om du vill specialisera dig:**
- 🔐 **Säkerhet**: Studera Zero Trust, gå CCNP Security
- ☁️ **Cloud**: Lär dig AWS/Azure networking, AWS Certified Advanced Networking
- 🤖 **Automation**: Python, Ansible, Terraform, Nornir
- 📡 **Wireless**: CWNA, CCNP Wireless
- 🎯 **SDN**: OpenDaylight, ONOS, Cisco ACI

### 💡 Avslutande Tips

🌟 **Övning ger färdighet**: Teoretisk kunskap räcker inte - labba, labba, labba!

🌟 **Bygg ett homelab**: Köp begagnad Cisco/HP-utrustning eller använd virtualisering (GNS3, EVE-NG)

🌟 **Nätverka** (pun intended): Gå med i communities, delta i forum, gå på meetups

🌟 **Håll dig uppdaterad**: Nätverksteknologi utvecklas snabbt - följ med i svängarna!

🌟 **Lär genom att undervisa**: Förklara koncept för andra - det befäster din egen kunskap

### 🙏 Tack för att du läste!

Jag hoppas denna guide har gett dig en solid grund i datornätverk och inspiration att fortsätta lära. Nätverk är ryggraden i vår digitala värld, och dina kunskaper är värdefulla!

**Lycka till på din resa! 🚀**

*Om du har frågor, kommentarer eller feedback, tveka inte att höra av dig. Fortsätt lära, fortsätt utforska, och framför allt - ha kul!*

---

**Version:** 1.0
**Senast uppdaterad:** November 2024
**Författare:** Pedagogisk Guide-serien
**Licens:** Creative Commons BY-SA 4.0

🌐 **Möjliga nätverk kräver kontinuerligt lärande!**
