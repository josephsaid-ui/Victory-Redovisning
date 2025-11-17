# 🕵️ BONUS: Darkweb OSINT & Threat Intelligence

> **"On the internet, nobody knows you're a dog. On the darkweb, nobody knows you're investigating." - Adapted**
>
> ⚠️ **VARNING:** Denna guide är för säkerhetsforskare, threat intelligence-analytiker och lag enforcement.
> 📚 Läsningstid: 60-90 min | 🎯 Övningar: 5 | 💡 Svårighetsgrad: Avancerad/Expert

---

## 🗺️ Navigation
**[🏠 Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)** | **[📚 Extra Guide](OSINT_ZAP_Guide_Extra.md)**

---

## ⚠️ Viktig Etisk Disclaimer

**INNAN DU FORTSÄTTER - LÄS DETTA:**

```
TILLÅTNA ANVÄNDNINGSOMRÅDEN:
══════════════════════════════════════════════════════════════
✅ Threat Intelligence (hitta hot mot din organisation)
✅ Security Research (förstå hur attackerare opererar)
✅ OSINT på publika darkweb-källor
✅ Forensisk investigation (med juridiskt mandat)
✅ Penetration Testing (darkweb-tjänster med tillstånd)
✅ Utbildning och träning

FÖRBJUDNA AKTIVITETER:
══════════════════════════════════════════════════════════════
❌ Köpa eller sälja illegala varor/tjänster
❌ Hacka darkweb-sajter utan tillstånd
❌ Distribuera malware
❌ Stjäla eller köpa stulna data
❌ Delta i kriminell verksamhet
❌ Bryta mot svenska/internationella lagar

JURIDISK VARNING:
══════════════════════════════════════════════════════════════
Att BESÖKA darkweb är lagligt i Sverige.
Att DELTA I kriminell verksamhet är INTE lagligt.

Denna guide är för DEFENSIVE säkerhetsändamål endast!
```

---

## 📋 Innehållsförteckning

1. [Del 1: Tor - The Onion Router](#del-1-tor)
2. [Del 2: ZAP med Tor/Darkweb](#del-2-zap-med-tor)
3. [Del 3: I2P & Alternative Networks](#del-3-i2p)
4. [Del 4: Darkweb OSINT](#del-4-darkweb-osint)
5. [Del 5: Threat Intelligence från Darkweb](#del-5-threat-intelligence)
6. [Del 6: Operational Security (OpSec)](#del-6-opsec)
7. [Del 7: Praktiska Övningar](#del-7-övningar)

---

## 🧅 Del 1: Tor - The Onion Router

### 🎯 Vad är Tor?

**Tor (The Onion Router)** är ett nätverk som möjliggör anonym kommunikation.

```
VARFÖR TOR EXISTERAR:
══════════════════════════════════════════════════════════════
✅ Anonymitet för journalister i förtryckande regimer
✅ Whistleblowers (SecureDrop använder Tor)
✅ Aktivister under hot
✅ Privacy-medvetna användare
✅ Security researchers

Tyvärr OCKSÅ använt för:
❌ Kriminell verksamhet
❌ Illegala marknadsplatser
❌ Extremism

Som säkerhetsforskare måste vi förstå båda sidorna.
```

### 🔧 Hur Tor Fungerar

```
NORMAL INTERNET CONNECTION:
════════════════════════════════════════════════════════════
Du → ISP → Webbplats
     ↑
    Kan se ALLT du besöker

TOR CONNECTION (3 HOP MINIMUM):
════════════════════════════════════════════════════════════
Du → Entry Node → Middle Node → Exit Node → Webbplats
     (Tor Guard)   (Relay)       (kan se destination men inte dig)

Varje node känner bara till föregående och nästa node.
Ingen enskild node känner till hela vägen!

ONION LAYERED ENCRYPTION:
════════════════════════════════════════════════════════════
                    ┌─────────────────┐
                    │ Layer 3: Exit   │
                ┌───┤ Layer 2: Middle ├───┐
            ┌───┤   │ Layer 1: Entry  │   ├───┐
            │   └───┴─────────────────┴───┘   │
         Encrypt                            Decrypt
        (Din sida)                        (Layer by layer)

Som en lök - varje lager avslöjas bara av rätt node!
```

### 💾 Installation av Tor Browser

#### Windows/Mac/Linux

**Steg 1: Ladda ner Tor Browser**
```
Officiell källa: https://www.torproject.org/download/

⚠️ VIKTIGT: Ladda ENDAST från torproject.org!
Falska Tor-browsers kan innehålla malware.

Windows: tor-browser-windows-x86_64-XX.X.X.exe
Mac:     tor-browser-macos-XX.X.X.dmg
Linux:   tor-browser-linux-x86_64-XX.X.X.tar.xz
```

**Steg 2: Installera och Verifiera**
```bash
# Linux installation:
cd ~/Downloads
tar -xf tor-browser-linux-x86_64-*.tar.xz
cd tor-browser
./start-tor-browser.desktop

# Första start:
1. Välj "Connect" (eller "Configure" om du är i censurerat land)
2. Vänta tills Tor-nätverket ansluter
3. Tor Browser öppnas
```

**Steg 3: Verifiera Anslutning**
```
Besök: https://check.torproject.org/

Du ska se:
"Congratulations. This browser is configured to use Tor."

Din IP-adress: [Tor Exit Node IP]
                (INTE din riktiga IP!)
```

### 🔐 Tor Browser Security Settings

**Security Level: Standard vs Safer vs Safest**

```
┌────────────────────────────────────────────────────────┐
│ Tor Browser Security Levels                           │
├────────────────────────────────────────────────────────┤
│                                                        │
│ STANDARD (Default)                                     │
│ ✅ All website features enabled                       │
│ ✅ JavaScript enabled                                 │
│ ❌ Minst säkert                                       │
│                                                        │
│ SAFER (Rekommenderat för de flesta)                   │
│ ⚠️  JavaScript disabled on non-HTTPS sites           │
│ ⚠️  Some fonts and math symbols disabled             │
│ ✅ Bättre säkerhet                                    │
│                                                        │
│ SAFEST (För maximal säkerhet)                         │
│ 🔒 JavaScript disabled på ALLA sites                 │
│ 🔒 Endast static sites och basic services            │
│ ✅ Maximal säkerhet (men många sidor fungerar ej)    │
│                                                        │
└────────────────────────────────────────────────────────┘

Ändra: Klicka på Shield-ikonen längst upp till höger
```

**För OSINT/Research:**
```
Rekommenderad Setting: SAFER

Varför?
✅ JavaScript enabled på HTTPS (behövs för många darkweb-sajter)
✅ Skyddar mot många attacker
✅ Bra balans mellan säkerhet och funktionalitet
```

### 🌐 .onion Adresser

**.onion domäner** är unika för Tor-nätverket.

**Format:**
```
http://[16 eller 56 slumpmässiga tecken].onion

Exempel (v2 - deprecated):
http://3g2upl4pq6kufc4m.onion  (DuckDuckGo)
       ^^^^^^^^^^^^^^^^
       16 tecken (80 bits)

Exempel (v3 - modern):
http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
       56 tecken (336 bits) - Mycket säkrare!
```

**Vanity .onion Addresses:**
```
Kan generera custom början:
http://facebook...ww23y.onion  (Facebooks officiella Tor-sida)
       ^^^^^^^^
     Vanity prefix

Verktyg: mkp224o, Eschalot
⚠️ Tar MYCKET lång tid för långa prefix (exponentiell svårighet)
```

### 🔍 Hitta Darkweb-sajter

**Viktiga startpunkter (alla legala):**

```
SÖKMOTORER:
══════════════════════════════════════════════════════════════
Ahmia
http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion
- Indexerar legala .onion sajter
- Filtrerar bort illegalt innehåll
- Bra för nybörjare

DuckDuckGo
http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion
- Privacy-fokuserad sökmotor
- Finns både på clearweb och darkweb

Torch
http://torchdeedp3i2jigzjdmfpn5ttjhthh5wbmda2rr3jvqjg5p77c54dqd.onion
- Äldsta Tor-sökmotorn
- Stor databas

KATALOGER/WIKIS:
══════════════════════════════════════════════════════════════
The Hidden Wiki
http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion
- Katalog över .onion sajter
- Kategoriserad lista
- ⚠️ Uppdateras ofta, länkar kan vara döda

Dark.fail
https://dark.fail (clearweb mirror)
- Listar status för populära darknet markets
- Verifierar .onion länkar
```

### 📡 Tor Bridges (För censurerade nätverk)

Om Tor blockeras i ditt nätverk:

```bash
# Konfigurera Tor med Bridges
1. Öppna Tor Browser
2. Settings → Connection
3. "Tor is censored in my country" → ON
4. Select bridge type:

BRIDGE TYPES:
─────────────────────────────────────────────────────────
obfs4     - Mest populär, döljer Tor-trafik som random data
meek      - Går via CDN (ser ut som normal HTTPS)
snowflake - P2P-baserad, använder frivilligas browsers

Få bridges:
https://bridges.torproject.org/
eller
Email: bridges@torproject.org (från Gmail/Riseup)
```

### 🛡️ Säkerhetsråd för Tor-användning

```
DO'S ✅
══════════════════════════════════════════════════════════════
✅ Använd endast Tor Browser (inte Chrome/Firefox över Tor)
✅ Håll Tor Browser uppdaterad
✅ Använd HTTPS Everywhere (inbyggt)
✅ Verifiera .onion adresser från pålitliga källor
✅ Använd VM för extra isolering (Whonix, Tails)
✅ Disable JavaScript när möjligt
✅ Använd VPN + Tor för extra anonymitet (kontroversiellt)

DON'TS ❌
══════════════════════════════════════════════════════════════
❌ Logga INTE in på dina vanliga konton över Tor
❌ Använd INTE torrents över Tor (avslöjar din IP!)
❌ Ladda INTE ner filer och öppna utanför Tor Browser
❌ Installera INTE plugins eller tillägg
❌ Maximera INTE fönstret (fingerprinting)
❌ Lita INTE på alla .onion sajter
❌ Klicka INTE på random länkar
```

### 🐧 Whonix - Ultimate Tor Security

**Whonix** = OS designat för maximal anonymitet via Tor

```
WHONIX ARCHITECTURE:
══════════════════════════════════════════════════════════════
┌─────────────────────────────────────────────────────────┐
│                    Host System                          │
│  ┌──────────────────┐      ┌──────────────────┐        │
│  │  Whonix Gateway  │      │ Whonix Workstation│       │
│  │                  │      │                   │       │
│  │  - Tor routing   │ ←→   │ - Your apps       │       │
│  │  - Firewall      │      │ - Isolated        │       │
│  │  - No apps       │      │ - Can't leak IP   │       │
│  └──────────────────┘      └──────────────────┘        │
│         ↓                                               │
│    [Tor Network]                                        │
└─────────────────────────────────────────────────────────┘

ALLA connections från Workstation MÅSTE gå via Gateway (Tor)
Omöjligt att läcka din riktiga IP!
```

**Installation:**
```bash
# Ladda ner Whonix
https://www.whonix.org/wiki/Download

# Import till VirtualBox/KVM
1. Importera Whonix-Gateway OVA
2. Importera Whonix-Workstation OVA
3. Starta Gateway först
4. Starta Workstation
5. All trafik går nu automatiskt via Tor!
```

### 📊 Tor vs VPN vs Tor+VPN

```
COMPARISON:
══════════════════════════════════════════════════════════════
Feature           | Tor      | VPN      | Tor+VPN
──────────────────┼──────────┼──────────┼─────────────────────
Anonymitet        | Hög      | Medel    | Mycket hög
Hastighet         | Långsam  | Snabb    | Mycket långsam
Kryptering        | Ja (3x)  | Ja       | Ja (4x)
Blockera ISP      | Nej*     | Ja       | Ja
Access .onion     | Ja       | Nej      | Ja
Kostar pengar     | Gratis   | $$$      | $$$
Trust model       | Decentralized | Trust VPN provider | Both

*ISP ser att du använder Tor, men inte VAD du gör

TOR + VPN CONFIGURATIONS:
══════════════════════════════════════════════════════════════
1. VPN → Tor (Rekommenderat för darkweb research)
   Du → VPN → Tor → Internet
   + ISP ser inte Tor-användning
   + VPN ser inte vad du gör (Tor krypterar)
   - VPN känner till din identitet

2. Tor → VPN
   Du → Tor → VPN → Internet
   + Exit node ser inte din trafik
   - Svårare att konfigurera
   - Färre use cases
```

---

## 🔧 Del 2: ZAP med Tor/Darkweb

### 🎯 Varför använda ZAP på Darkweb?

```
ANVÄNDNINGSOMRÅDEN:
══════════════════════════════════════════════════════════════
✅ Testa säkerheten på din egen .onion tjänst
✅ Security research på publika darkweb-applikationer
✅ Threat intelligence (identifiera sårbarheter attackers kan utnyttja)
✅ Forensisk analys (med juridiskt mandat)
✅ Penetration testing av darkweb-tjänster (med tillstånd!)

⚠️ ALDRIG: Attackera sajter utan tillstånd!
```

### 🔌 Konfigurera ZAP att använda Tor

#### Metod 1: ZAP → Tor Browser (Enklast)

**Steg 1: Starta Tor Browser**
```bash
# Tor Browser startar automatiskt Tor SOCKS proxy på:
127.0.0.1:9150
```

**Steg 2: Konfigurera ZAP**
```
ZAP → Tools → Options → Connection

┌────────────────────────────────────────────────────────┐
│ Connection Settings                                    │
├────────────────────────────────────────────────────────┤
│                                                        │
│ ☑ Use outgoing proxy server                          │
│                                                        │
│ Address: 127.0.0.1                                     │
│ Port:    9150                                          │
│                                                        │
│ Proxy Type: SOCKS                                      │
│                                                        │
│ ☑ Use proxy for DNS                                  │
│                                                        │
└────────────────────────────────────────────────────────┘

[Save]
```

**Steg 3: Testa**
```
1. I ZAP, gå till Manual Request Editor
2. Request URL: http://check.torproject.org
3. [Send]

Response ska innehålla:
"Congratulations. This browser is configured to use Tor."
```

#### Metod 2: ZAP → Tor Service (Mer stabilt)

**Steg 1: Installera Tor Service**
```bash
# Debian/Ubuntu
sudo apt install tor

# Start Tor
sudo systemctl start tor
sudo systemctl enable tor

# Tor SOCKS proxy startar på:
# 127.0.0.1:9050 (default)
```

**Steg 2: Konfigurera ZAP**
```
ZAP → Tools → Options → Connection

Address: 127.0.0.1
Port:    9050  (OBS: 9050, inte 9150!)
Type:    SOCKS
```

**Steg 3: Konfigurera Tor för Stream Isolation (Optional men rekommenderat)**
```bash
# Redigera /etc/tor/torrc
sudo nano /etc/tor/torrc

# Lägg till:
SocksPort 9050 IsolateDestAddr IsolateDestPort
SocksPort 9051 # För ZAP

# Restart Tor
sudo systemctl restart tor
```

### 🕷️ Spider .onion Websites med ZAP

**.onion sajter kan vara långsamma och instabila.**

**Konfigurera ZAP för Tor-nätverk:**

```
ZAP → Tools → Options → Spider

┌────────────────────────────────────────────────────────┐
│ Spider Settings för Darkweb                           │
├────────────────────────────────────────────────────────┤
│                                                        │
│ Max Depth: 3  (darkweb är långsamt, begränsa djup)   │
│                                                        │
│ Thread Count: 2  (inte för många, max ut nätverket)  │
│                                                        │
│ Max Duration: 30 min  (ge tid för långsamma sidor)   │
│                                                        │
│ Request Delay: 5000 ms  (5 sek mellan requests)      │
│                                                        │
│ ☑ Process forms  (om du vill)                        │
│ ☐ POST forms  (var försiktig!)                       │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Exempel: Spider en test .onion**
```
Target: http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion

1. Högerklicka på URL i Sites-träd
2. Attack → Spider
3. [Start Scan]

Förvänta dig:
- Långsam progress (Tor är långsamt)
- Timeouts (normalt på darkweb)
- Färre URLs än clearweb (mindre sidor)
```

### 🎯 Active Scan på .onion med ZAP

**⚠️ VIKTIGT: Endast på sajter du har tillstånd att testa!**

**Anpassade inställningar för Darkweb:**

```
ZAP → Tools → Options → Active Scan

┌────────────────────────────────────────────────────────┐
│ Active Scan Settings för Darkweb                      │
├────────────────────────────────────────────────────────┤
│                                                        │
│ Thread Count: 1-2  (inte överbelasta Tor-nätverk)    │
│                                                        │
│ Delay when scanning (ms): 3000  (3 sek)              │
│                                                        │
│ ☐ Inject plugin ID in header  (mindre fingerprinting)│
│                                                        │
│ Strength: LOW-MEDIUM  (färre requests)                │
│                                                        │
│ Threshold: MEDIUM  (reducera false positives)         │
│                                                        │
└────────────────────────────────────────────────────────┘
```

**Kör Active Scan:**
```
1. Spider först (för att hitta alla endpoints)
2. Högerklicka på .onion site
3. Attack → Active Scan
4. Välj Policy: "Light" eller custom
5. [Start Scan]

Förvänta dig:
⏱️  Mycket långsam (kan ta timmar!)
⚠️  Många timeouts
📊 Färre alerts än clearweb
```

### 🔍 Manual Testing på Darkweb med ZAP

**Använd ZAP som Intercepting Proxy för Tor Browser:**

**Problem:** Tor Browser använder redan en proxy (Tor SOCKS). Hur får vi ZAP däremellan?

**Lösning: Chain proxies**

```
PROXY CHAIN:
══════════════════════════════════════════════════════════════
Tor Browser → ZAP (8080) → Tor SOCKS (9150) → Tor Network
```

**Konfigurera:**

**Steg 1: Konfigurera ZAP** (redan gjort ovan - ZAP → Tor)

**Steg 2: Konfigurera Tor Browser att använda ZAP**
```
Tor Browser → Settings → Network Settings

☑ Manual proxy configuration

HTTP Proxy:  127.0.0.1    Port: 8080
SSL Proxy:   127.0.0.1    Port: 8080
SOCKS Proxy: [lämna tom]

☑ Use this proxy server for all protocols

[OK]
```

**Steg 3: Testa**
```
1. I Tor Browser, besök: http://check.torproject.org
2. I ZAP History, se requesten
3. Du ser nu .onion trafik i ZAP!
```

**Nu kan du:**
```
✅ Intercept requests (Ctrl+B i ZAP)
✅ Modifiera headers
✅ Testa för XSS, SQLi, etc manuellt
✅ Repeater för att replay requests
✅ Fuzzer för att testa inputs
```

### 📝 ZAP Scripts för Darkweb

**Custom ZAP script för att hantera Tor timeouts:**

```python
# zap_tor_timeout_handler.py
# Script Type: Standalone

from org.zaproxy.zap.extension.script import ScriptVars
import time

def scan_with_retry(target_url, max_retries=3):
    """
    Scanner med retry logic för Tor timeouts
    """

    for attempt in range(max_retries):
        try:
            print(f"[*] Attempt {attempt + 1} for {target_url}")

            # Kör spider
            spider_id = ScriptVars.getGlobalVar("zap").spider.scan(target_url)

            # Vänta tills klar (med timeout)
            timeout = 1800  # 30 min
            start_time = time.time()

            while int(ScriptVars.getGlobalVar("zap").spider.status(spider_id)) < 100:
                if time.time() - start_time > timeout:
                    print("[!] Spider timeout, retrying...")
                    ScriptVars.getGlobalVar("zap").spider.stop(spider_id)
                    break

                time.sleep(5)

            print(f"[+] Spider complete: {spider_id}")
            return True

        except Exception as e:
            print(f"[!] Error on attempt {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                print("[*] Waiting 30s before retry...")
                time.sleep(30)

    return False

# Använd
scan_with_retry("http://your-onion-site.onion")
```

### 🛠️ Troubleshooting ZAP + Tor

**Problem 1: Connection refused**
```
Error: "Connection refused when attempting to connect to target"

Lösning:
1. Verifiera att Tor körs:
   curl --socks5 127.0.0.1:9150 http://check.torproject.org

2. Verifiera ZAP proxy settings:
   Tools → Options → Connection

3. Testa manuellt:
   Manual Request Editor → http://check.torproject.org
```

**Problem 2: Mycket långsam scanning**
```
Detta är normalt! Tor är långsamt.

Optimeringar:
- Reducera threads till 1-2
- Öka request delay
- Använd "Light" scan policy
- Spider först, scan sedan på specific endpoints
```

**Problem 3: Många timeout errors**
```
.onion sajter är ofta instabila.

Lösningar:
- Öka connection timeout i ZAP
- Använd retry logic i custom scripts
- Acceptera att vissa sajter är nere
- Testa vid olika tider på dygnet
```

---

## 🌐 Del 3: I2P & Alternative Anonymous Networks

### 🎯 Vad är I2P?

**I2P (Invisible Internet Project)** = Ett annat anonymt nätverk, annorlunda än Tor.

```
TOR vs I2P:
══════════════════════════════════════════════════════════════
Feature              | Tor              | I2P
─────────────────────┼──────────────────┼────────────────────
Fokus                | Outproxy         | Internal network
Design               | Circuit-based    | Packet-switched
Hastighet            | Långsam          | Snabbare
Anonymitet           | Hög              | Mycket hög
.onion equiv.        | .onion           | .i2p
Användning           | Browse clearweb  | Internal services
Exit nodes           | Ja               | Nej (default)
Latency              | Högre            | Lägre
P2P                  | Nej (discouraged)| Ja (optimerat)

NÄR ANVÄNDA I2P:
✅ Interna tjänster (.i2p sites)
✅ P2P file sharing
✅ Anonymous messaging
✅ När du inte behöver clearweb access

NÄR ANVÄNDA TOR:
✅ Browse clearweb anonymt
✅ Access .onion sites
✅ Simplare för nybörjare
```

### 💾 Installera I2P

**Java I2P (Rekommenderat):**

```bash
# Kräver Java
sudo apt install default-jre

# Ladda ner I2P
wget https://geti2p.net/en/download/debian
# Eller från https://geti2p.net/

# Installera (Debian/Ubuntu)
sudo dpkg -i i2pinstall_*.deb

# Starta I2P
i2prouter start

# I2P Router Console öppnas automatiskt:
http://127.0.0.1:7657
```

**I2P Configuration:**
```
1. Besök Router Console: http://127.0.0.1:7657
2. Bandwidth settings: Sätt enligt din anslutning
3. Vänta ~5-10 min för nätverket att "bootstrap"
4. När "Network Status: OK" visas är du redo!
```

### 🌐 Browse .i2p Sites

**Konfigurera Browser för I2P:**

**Firefox:**
```
Settings → Network Settings

☑ Manual proxy configuration

HTTP Proxy:  127.0.0.1    Port: 4444
SSL Proxy:   127.0.0.1    Port: 4445
SOCKS:       127.0.0.1    Port: 4447

☑ Proxy DNS when using SOCKS v5

[OK]
```

**Besök .i2p sajter:**
```
http://stats.i2p  (I2P network stats)
http://i2p-projekt.i2p  (I2P project homepage)
http://planet.i2p  (I2P blog aggregator)
```

### 🔧 ZAP med I2P

**Konfigurera ZAP för I2P:**

```
ZAP → Tools → Options → Connection

HTTP Proxy:  127.0.0.1    Port: 4444
HTTPS Proxy: 127.0.0.1    Port: 4445

☑ Use proxy for DNS
```

**Test:**
```
Manual Request → http://stats.i2p
→ Du ska se I2P network statistics
```

---

## 🕵️ Del 4: Darkweb OSINT

### 🎯 Darkweb OSINT Framework

```
DARKWEB OSINT METHODOLOGY:
══════════════════════════════════════════════════════════════

1. RECONNAISSANCE
   ├─ Identify .onion targets
   ├─ Verify legitimacy (många phishing!)
   └─ Document infrastructure

2. COLLECTION
   ├─ Manual browsing med screenshots
   ├─ Automated scraping (försiktigt!)
   ├─ Archive pages (Wayback Machine för darkweb)
   └─ Download relevant data

3. PROCESSING
   ├─ Extract entities (names, addresses, crypto wallets)
   ├─ Link analysis
   ├─ Cryptocurrency tracking
   └─ PGP key correlation

4. ANALYSIS
   ├─ Identify threats
   ├─ Track malicious actors
   ├─ Correlate with clearweb intel
   └─ Risk assessment

5. DISSEMINATION
   ├─ Threat intelligence reports
   ├─ Law enforcement reporting
   ├─ Internal security alerts
   └─ Defensive measures
```

### 🔍 Darkweb Search Techniques

**Sökmotorer för Darkweb OSINT:**

```python
#!/usr/bin/env python3
"""
Automated Darkweb Search
Uses Ahmia API for searching .onion sites
"""

import requests
import json

AHMIA_API = "https://ahmia.fi/search/?q="

def search_darkweb(query):
    """Search Ahmia for .onion sites"""

    try:
        # Ahmia API search
        response = requests.get(f"{AHMIA_API}{query}")

        # Parse results
        # Note: You'll need to parse HTML or use proper API
        print(f"[*] Searching for: {query}")
        print(f"[*] Results found on Ahmia")

        # Better: Use Tor SOCKS proxy
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

        response = requests.get(
            f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={query}",
            proxies=proxies,
            timeout=30
        )

        return response.text

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# Usage
results = search_darkweb("threat intelligence")
```

### 📸 Screenshot & Archive Darkweb Sites

**Viktigt för forensics och threat intelligence!**

```python
#!/usr/bin/env python3
"""
Darkweb Screenshot Tool
Takes screenshots of .onion sites for documentation
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from datetime import datetime

def screenshot_onion(url, output_path="screenshots"):
    """
    Screenshot .onion site using Tor
    """

    # Configure Firefox to use Tor
    options = Options()
    options.headless = True  # Run in background

    profile = FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9150)
    profile.set_preference("network.proxy.socks_remote_dns", True)

    options.profile = profile

    # Start browser
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(60)

    try:
        print(f"[*] Loading {url}")
        driver.get(url)

        # Wait for page load
        time.sleep(10)

        # Generate filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_path}/{url.replace('http://', '').replace('.onion', '')}_{timestamp}.png"

        # Screenshot
        driver.save_screenshot(filename)
        print(f"[+] Screenshot saved: {filename}")

        # Also save HTML
        html_filename = filename.replace('.png', '.html')
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        print(f"[+] HTML saved: {html_filename}")

    except Exception as e:
        print(f"[!] Error: {e}")
    finally:
        driver.quit()

# Usage
screenshot_onion("http://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion")
```

### 🔗 Link Analysis på Darkweb

**Track relationships mellan .onion sites:**

```python
#!/usr/bin/env python3
"""
Darkweb Link Crawler
Maps relationships between .onion sites
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import networkx as nx
import matplotlib.pyplot as plt

class OnionCrawler:
    def __init__(self):
        self.session = requests.Session()
        self.session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        self.visited = set()
        self.graph = nx.DiGraph()

    def crawl(self, url, max_depth=2):
        """Crawl .onion site and extract links"""

        if url in self.visited or max_depth == 0:
            return

        self.visited.add(url)
        print(f"[*] Crawling: {url}")

        try:
            response = self.session.get(url, timeout=60)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all links
            for link in soup.find_all('a', href=True):
                href = link['href']

                # Only .onion links
                if '.onion' in href:
                    full_url = urljoin(url, href)

                    # Add edge to graph
                    self.graph.add_edge(url, full_url)

                    # Recursive crawl
                    self.crawl(full_url, max_depth - 1)

        except Exception as e:
            print(f"[!] Error crawling {url}: {e}")

    def visualize(self, output='darkweb_graph.png'):
        """Visualize the link graph"""

        plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(self.graph, k=0.5, iterations=50)

        nx.draw(self.graph, pos,
                with_labels=True,
                node_size=500,
                node_color='lightblue',
                font_size=8,
                arrows=True)

        plt.savefig(output, dpi=300, bbox_inches='tight')
        print(f"[+] Graph saved to {output}")

# Usage
crawler = OnionCrawler()
crawler.crawl("http://your-starting-onion.onion", max_depth=2)
crawler.visualize()
```

### 💰 Cryptocurrency Tracking

**Många darkweb-transaktioner använder Bitcoin/Monero:**

```python
#!/usr/bin/env python3
"""
Bitcoin Address Tracker
Tracks Bitcoin addresses found on darkweb
"""

import requests
import re

def extract_bitcoin_addresses(html):
    """Extract Bitcoin addresses from HTML"""

    # Bitcoin address regex (simplified)
    btc_pattern = r'\b[13][a-km-zA-HJ-NP-Z1-9]{25,34}\b'

    addresses = re.findall(btc_pattern, html)
    return list(set(addresses))

def check_bitcoin_balance(address):
    """Check Bitcoin address balance using blockchain API"""

    try:
        api_url = f"https://blockchain.info/q/addressbalance/{address}"
        response = requests.get(api_url, timeout=10)

        satoshis = int(response.text)
        btc = satoshis / 100000000

        return btc

    except Exception as e:
        print(f"[!] Error checking {address}: {e}")
        return None

def get_bitcoin_transactions(address):
    """Get transaction history for Bitcoin address"""

    try:
        api_url = f"https://blockchain.info/rawaddr/{address}"
        response = requests.get(api_url, timeout=10)
        data = response.json()

        return {
            'address': address,
            'balance': data['final_balance'] / 100000000,
            'total_received': data['total_received'] / 100000000,
            'n_tx': data['n_tx'],
            'transactions': data['txs'][:5]  # First 5
        }

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# Usage for OSINT
html = """<html>Send payment to: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa</html>"""
addresses = extract_bitcoin_addresses(html)

for addr in addresses:
    print(f"\n[*] Analyzing: {addr}")
    balance = check_bitcoin_balance(addr)
    print(f"  Balance: {balance} BTC")

    tx_data = get_bitcoin_transactions(addr)
    if tx_data:
        print(f"  Total received: {tx_data['total_received']} BTC")
        print(f"  Number of transactions: {tx_data['n_tx']}")
```

---

## 🚨 Del 5: Threat Intelligence från Darkweb

### 🎯 Vad är Darkweb Threat Intelligence?

**Darkweb Threat Intelligence** = Samla information från darkweb för att identifiera hot mot din organisation.

```
ANVÄNDN

INGSOMRÅDEN:
══════════════════════════════════════════════════════════════
✅ Data Leak Detection
   - Hitta stulna credentials
   - Company databases på darkweb
   - Customer information leaks

✅ Threat Actor Monitoring
   - Spåra kända hackers
   - Forum discussions om din organisation
   - Planerade attacker

✅ Malware & Exploit Tracking
   - Nya exploits till salu
   - Ransomware-as-a-Service
   - Zero-day discoveries

✅ Brand Protection
   - Phishing sites
   - Counterfeit goods
   - Corporate fraud

✅ Insider Threat Detection
   - Employees selling data
   - Credentials for sale
   - Corporate espionage
```

### 🔍 Monitoring Darkweb Forums

**Populära (och ökända) darkweb forums:**

```
⚠️ DISCLAIMER: Dessa forums används för illegal verksamhet.
Ange endast för research/threat intelligence!

FORUMS (exempel, många är scams):
══════════════════════════════════════════════════════════════
• Dread (Reddit-klon för darkweb)
• RaidForums (data breaches) - STÄNGD av FBI
• BreachForums (efterföljare)
• XSS Forum (rysk hacking-forum)
• Exploit.in (exploit marketplace)

OBS: Många forums kräver:
- Invitation
- Reputation
- Bitcoin deposit
- PGP verification
```

**Automated Forum Monitoring:**

```python
#!/usr/bin/env python3
"""
Darkweb Forum Monitor
Monitors forums for mentions of your company/keywords
"""

import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

class DarkwebMonitor:
    def __init__(self, proxies=None):
        self.session = requests.Session()
        if proxies:
            self.session.proxies = proxies
        else:
            # Default Tor proxy
            self.session.proxies = {
                'http': 'socks5h://127.0.0.1:9050',
                'https': 'socks5h://127.0.0.1:9050'
            }

    def search_forum(self, forum_url, keywords):
        """Search forum for keywords"""

        alerts = []

        try:
            response = self.session.get(forum_url, timeout=60)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all text
            text = soup.get_text().lower()

            # Check for keywords
            for keyword in keywords:
                if keyword.lower() in text:
                    alerts.append({
                        'keyword': keyword,
                        'forum': forum_url,
                        'timestamp': datetime.now().isoformat(),
                        'snippet': self._extract_context(text, keyword)
                    })

            return alerts

        except Exception as e:
            print(f"[!] Error monitoring {forum_url}: {e}")
            return []

    def _extract_context(self, text, keyword, context_length=200):
        """Extract text around keyword"""

        index = text.lower().find(keyword.lower())
        if index == -1:
            return ""

        start = max(0, index - context_length)
        end = min(len(text), index + len(keyword) + context_length)

        return text[start:end]

    def continuous_monitor(self, forums, keywords, interval=3600):
        """Continuously monitor forums"""

        print(f"[*] Starting continuous monitoring...")
        print(f"[*] Forums: {len(forums)}")
        print(f"[*] Keywords: {keywords}")
        print(f"[*] Check interval: {interval}s")

        while True:
            print(f"\n[*] Scan started: {datetime.now()}")

            for forum in forums:
                print(f"  [*] Checking {forum}")
                alerts = self.search_forum(forum, keywords)

                for alert in alerts:
                    print(f"  [!] ALERT: {alert['keyword']} found!")
                    print(f"      Forum: {alert['forum']}")
                    print(f"      Context: {alert['snippet'][:100]}...")

                    # Log to file
                    with open('darkweb_alerts.log', 'a') as f:
                        f.write(f"{alert}\n")

                # Be nice, don't hammer
                time.sleep(30)

            print(f"[*] Scan complete. Sleeping {interval}s...")
            time.sleep(interval)

# Usage
monitor = DarkwebMonitor()

forums = [
    "http://forum-example.onion",
    # Add your target forums
]

keywords = [
    "your-company-name",
    "your-company.com",
    "database leak",
    "credentials"
]

# Run continuous monitoring
# monitor.continuous_monitor(forums, keywords, interval=3600)  # Every hour
```

### 📊 Leaked Credentials Detection

**Check om dina företags credentials är läckta:**

```python
#!/usr/bin/env python3
"""
Credential Leak Detector
Checks darkweb dumps for your organization's emails
"""

import requests
import hashlib

def check_haveibeenpwned(email):
    """
    Check if email is in Have I Been Pwned database
    (Uses their API - clearweb, not darkweb, but good start)
    """

    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"

    headers = {
        'User-Agent': 'Threat-Intelligence-Tool',
        'hibp-api-key': 'YOUR_API_KEY'  # Get from haveibeenpwned.com
    }

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            breaches = response.json()
            return {
                'email': email,
                'breached': True,
                'breach_count': len(breaches),
                'breaches': [b['Name'] for b in breaches]
            }
        elif response.status_code == 404:
            return {
                'email': email,
                'breached': False
            }
        else:
            print(f"[!] Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

def scan_company_emails(domain):
    """
    Generate common email patterns and check
    """

    # Common patterns
    common_names = ['admin', 'info', 'support', 'contact', 'sales', 'hr', 'it']

    emails_to_check = [f"{name}@{domain}" for name in common_names]

    results = []

    for email in emails_to_check:
        print(f"[*] Checking {email}")
        result = check_haveibeenpwned(email)

        if result and result['breached']:
            print(f"  [!] BREACH FOUND!")
            print(f"      Breaches: {', '.join(result['breaches'])}")
            results.append(result)

        # Rate limiting
        import time
        time.sleep(2)

    return results

# Usage
breaches = scan_company_emails("your-company.com")

if breaches:
    print(f"\n[!] ALERT: {len(breaches)} breached emails found!")
    for breach in breaches:
        print(f"  - {breach['email']}: {breach['breach_count']} breaches")
```

### 🎣 Phishing Site Detection

**Monitor darkweb för phishing sites som imiterar ditt varumärke:**

```python
#!/usr/bin/env python3
"""
Phishing Site Detector
Finds darkweb sites imitating your brand
"""

from difflib import SequenceMatcher
import requests
from bs4 import BeautifulSoup

def calculate_similarity(str1, str2):
    """Calculate similarity between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()

def detect_phishing(target_domain, suspect_url, threshold=0.7):
    """
    Detect if suspect_url is phishing target_domain
    """

    try:
        # Setup Tor proxy
        proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }

        response = requests.get(suspect_url, proxies=proxies, timeout=60)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get page title
        title = soup.title.string if soup.title else ""

        # Get text content
        text = soup.get_text()

        # Check similarity
        title_similarity = calculate_similarity(target_domain, title)
        content_similarity = calculate_similarity(target_domain, text)

        is_phishing = title_similarity > threshold or content_similarity > threshold

        return {
            'url': suspect_url,
            'is_phishing': is_phishing,
            'title': title,
            'title_similarity': title_similarity,
            'content_similarity': content_similarity
        }

    except Exception as e:
        print(f"[!] Error: {e}")
        return None

# Usage
result = detect_phishing(
    "YourBank",
    "http://suspected-phishing-site.onion"
)

if result and result['is_phishing']:
    print("[!] PHISHING DETECTED!")
    print(f"    URL: {result['url']}")
    print(f"    Title: {result['title']}")
    print(f"    Similarity: {result['title_similarity']:.2%}")
```

### 📈 Threat Intelligence Feeds

**Integrera darkweb threat intelligence med dina system:**

```python
#!/usr/bin/env python3
"""
Darkweb Threat Intel Feed Generator
Generates structured threat intelligence from darkweb
"""

import json
from datetime import datetime

class ThreatIntelFeed:
    def __init__(self):
        self.indicators = []

    def add_ioc(self, ioc_type, value, source, confidence="medium", context=""):
        """Add Indicator of Compromise"""

        ioc = {
            'type': ioc_type,  # 'domain', 'ip', 'email', 'bitcoin', 'hash'
            'value': value,
            'source': source,
            'confidence': confidence,  # 'low', 'medium', 'high'
            'context': context,
            'first_seen': datetime.now().isoformat(),
            'last_seen': datetime.now().isoformat(),
            'tags': []
        }

        self.indicators.append(ioc)

    def export_stix(self, output_file):
        """Export as STIX format (Structured Threat Information)"""

        # Simplified STIX export
        stix_bundle = {
            'type': 'bundle',
            'id': f'bundle--{datetime.now().timestamp()}',
            'objects': []
        }

        for ioc in self.indicators:
            stix_object = {
                'type': 'indicator',
                'pattern': f"[{ioc['type']}:value = '{ioc['value']}']",
                'labels': ioc['tags'],
                'confidence': ioc['confidence'],
                'created': ioc['first_seen'],
                'modified': ioc['last_seen']
            }
            stix_bundle['objects'].append(stix_object)

        with open(output_file, 'w') as f:
            json.dump(stix_bundle, f, indent=2)

        print(f"[+] STIX feed exported: {output_file}")

    def export_misp(self, output_file):
        """Export for MISP platform"""

        misp_event = {
            'Event': {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'threat_level_id': '2',  # Medium
                'info': 'Darkweb Threat Intelligence',
                'Attribute': []
            }
        }

        for ioc in self.indicators:
            attribute = {
                'type': ioc['type'],
                'value': ioc['value'],
                'comment': ioc['context'],
                'category': 'Network activity'
            }
            misp_event['Event']['Attribute'].append(attribute)

        with open(output_file, 'w') as f:
            json.dump(misp_event, f, indent=2)

        print(f"[+] MISP event exported: {output_file}")

# Usage
feed = ThreatIntelFeed()

# Add IOCs discovered from darkweb
feed.add_ioc(
    'domain',
    'malicious-site.onion',
    'darkweb-forum',
    confidence='high',
    context='Phishing site targeting Bank customers'
)

feed.add_ioc(
    'bitcoin',
    '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
    'ransomware-payment',
    confidence='high',
    context='Ransomware payment address'
)

# Export
feed.export_stix('darkweb_intel.stix')
feed.export_misp('darkweb_intel.misp')
```

---

## 🔐 Del 6: Operational Security (OpSec)

### 🎯 OpSec för Darkweb Research

**KRITISKT:** När du gör darkweb research, skydda dig själv!

```
OPSEC LAYERS:
══════════════════════════════════════════════════════════════

LAYER 1: ANONYMITET
✅ Använd Tor för all darkweb access
✅ Använd VPN + Tor för extra skydd
✅ Använd Whonix eller Tails för maximal isolation

LAYER 2: IDENTITET
✅ Skapa separata pseudonymer för research
✅ Använd ALDRIG din riktiga identitet
✅ Olika pseudonymer för olika communities
✅ Använd PGP för krypterad kommunikation

LAYER 3: DEVICE SECURITY
✅ Dedikerad dator/VM för darkweb research
✅ Full disk encryption
✅ Ingen personal information på enheten
✅ Regelbunden malware-scanning

LAYER 4: NETWORK SECURITY
✅ Aldrig använd work/home network direkt
✅ Offentligt WiFi (med VPN)
✅ Dedicated research network
✅ Firewall rules

LAYER 5: FINANCIAL
✅ Använd aldrig personliga kreditkort
✅ Bitcoin via mixer (för legitima ändamål)
✅ Prepaid cards
✅ Separate bank accounts för research

LAYER 6: LEGAL
✅ Dokumentera alla aktiviteter
✅ Håll dig inom lagen
✅ Konsultera legal innan greyzone research
✅ Ha försäkring (cyber liability)
```

### 🖥️ Tails OS - Ultimate OpSec

**Tails (The Amnesic Incognito Live System)** = Amnestisk OS för maximal anonymitet.

```
TAILS FEATURES:
══════════════════════════════════════════════════════════════
✅ Bootar från USB (leaves no trace on computer)
✅ All trafik via Tor automatiskt
✅ Amnesic - glömmer allt när du stänger av
✅ State-of-the-art crypto tools
✅ Edward Snowden använde Tails

INSTALLERA TAILS:
══════════════════════════════════════════════════════════════
1. Ladda ner från: https://tails.boum.org/
2. Verifiera nedladdningen (viktigt!)
3. Skapa bootable USB med Etcher
4. Boota från USB
5. All trafik går nu via Tor!

ANVÄND TAILS FÖR:
✅ Högkänslig darkweb research
✅ När maximal anonymitet krävs
✅ Whistleblowing
✅ Journalist/activist work
```

### 🔑 PGP för Darkweb

**PGP (Pretty Good Privacy)** = Standard för kryptering på darkweb.

**Generera PGP-nycklar:**
```bash
# Installera GPG
sudo apt install gnupg

# Generera nyckel
gpg --full-generate-key

# Välj:
# - RSA and RSA
# - 4096 bits (stark)
# - Expiration: 1 year (bra practice)
# - Namn: Pseudonym (INTE riktigt namn!)
# - Email: pseudonym@protonmail.com

# Export public key
gpg --armor --export your-email@example.com > public_key.asc

# Export private key (ALDRIG dela!)
gpg --armor --export-secret-keys your-email@example.com > private_key.asc
```

**Kryptera meddelande:**
```bash
# Importera mottagarens public key
gpg --import recipient_public_key.asc

# Kryptera meddelande
echo "Secret message" | gpg --encrypt --armor --recipient recipient@email.com > encrypted.asc

# Dekryptera (med din private key)
gpg --decrypt encrypted.asc
```

**Signera meddelande (bevisa att DU skrev det):**
```bash
gpg --clear-sign message.txt
```

### 🚫 Vad du ALDRIG ska göra

```
KRITISKA MISSTAG - UNDVIK:
══════════════════════════════════════════════════════════════

❌ ALDRIG logga in på personliga konton över Tor
   (Facebook, Gmail, etc. - kopplar dig till darkweb-aktivitet)

❌ ALDRIG ladda ner och öppna filer direkt
   (kan innehålla malware, exploits)

❌ ALDRIG använd samma pseudonym överallt
   (gör det lätt att korrelera aktiviteter)

❌ ALDRIG lita på darkweb-sajter med känslig info
   (många är honeypots från law enforcement)

❌ ALDRIG köp illegala varor/tjänster
   (även för "research" - det är BROTT)

❌ ALDRIG klicka på random länkar
   (många leder till exploits eller CP)

❌ ALDRIG kommunicera om illegal verksamhet
   (du kan bli åtalad för conspiracy)

❌ ALDRIG använd Tor för stora file downloads
   (belastar nätverket, läcker metadata)

❌ ALDRIG anta att du är 100% anonym
   (OpSec failures, timing attacks, etc.)

❌ ALDRIG glöm: LAW ENFORCEMENT FINNS PÅ DARKWEB
   (FBI, Europol, lokala polisen - alla är där)
```

---

## 🎯 Del 7: Praktiska Övningar

### Övning 7.1: Säker Tor Setup 🧅

**Mål:** Installera och konfigurera Tor säkert

```
UPPGIFTER:
□ Installera Tor Browser
□ Verifiera Tor-anslutning (check.torproject.org)
□ Sätt Security Level till "Safer"
□ Besök DuckDuckGo .onion
□ Ta screenshot (för dokumentation)

SÄKERHETSCHECK:
□ Har du verifierat digital signatur på nedladdningen?
□ Använder du latest version?
□ Är JavaScript disabled på non-HTTPS?
□ Har du testat att din IP är dold?

BONUS:
□ Installera Tor som service (port 9050)
□ Konfigurera stream isolation
□ Installera Whonix VMs
```

### Övning 7.2: ZAP med Tor Integration 🔧

**Mål:** Konfigurera ZAP att scanna via Tor

```
UPPGIFTER:
□ Starta Tor Browser (proxy på 9150)
□ Konfigurera ZAP → Tools → Options → Connection
   - Address: 127.0.0.1
   - Port: 9150
   - Type: SOCKS
□ Verifiera med Manual Request till check.torproject.org
□ Spider DuckDuckGo .onion
□ Dokumentera resultat

RESULTAT ATT DOKUMENTERA:
- Spider duration: _____
- URLs found: _____
- Alerts: _____
- Difficulties encountered: _____

REFLEKTION:
- Hur var hastigheten jämfört med clearweb?
- Hittade ZAP några säkerhetsproblem?
- Vilka utmaningar mötte du?
```

### Övning 7.3: Darkweb OSINT Reconnaissance 🕵️

**Mål:** Praktisk OSINT på darkweb

```
TARGET: Ahmia .onion search engine
URL: http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion

UPPGIFTER:
□ Besök Ahmia via Tor Browser
□ Sök efter "security research"
□ Dokumentera 5 legala .onion sajter du hittar
□ Ta screenshots
□ Analysera:
  - Vilken typ av innehåll?
  - Legitim eller misstänkt?
  - Potentiella use cases för threat intelligence?

DOKUMENTATION:
═══════════════════════════════════════════════════════════
Site 1:
URL: _____________________
Type: _____________________
Description: _____________________
Legitimacy: _____________________

Site 2:
URL: _____________________
Type: _____________________
Description: _____________________
Legitimacy: _____________________

[... etc för 5 sites ...]
```

### Övning 7.4: PGP Encryption Practice 🔐

**Mål:** Lär dig PGP för säker kommunikation

```
UPPGIFTER:
□ Installera GPG
□ Generera PGP-nyckelpar
  - Använd pseudonym (inte riktigt namn!)
  - 4096-bit RSA
  - 1-års expiration
□ Export public key
□ Kryptera ett meddelande till dig själv
□ Dekryptera meddelandet
□ Signera ett meddelande

DOKUMENTERA:
Public Key Fingerprint: _____________________
Key ID: _____________________

Encrypted Message (paste här):
_____________________

Decrypted Successfully? Yes / No

BONUS:
□ Upload public key till keyserver
□ Hitta någon annans public key
□ Kryptera meddelande till dem
```

### Övning 7.5: Threat Intelligence Report 📊

**Mål:** Skapa en darkweb threat intelligence rapport

```
SCENARIO:
Du är threat intelligence analyst på ett företag.
Din uppgift: Undersök om företagets data har läckt på darkweb.

UPPGIFTER:
1. RECONNAISSANCE (30 min)
   □ Sök på Ahmia efter företagsnamn
   □ Sök efter domän (company.com)
   □ Sök efter CEO namn
   □ Dokumentera alla fynd

2. ANALYSIS (30 min)
   □ Bedöm trovärdighet på fynd
   □ Klassificera severity (Low/Med/High/Critical)
   □ Identifiera IOCs (email addresses, IPs, etc.)

3. REPORTING (30 min)
   Skriv rapport enligt denna mall:

═══════════════════════════════════════════════════════════
DARKWEB THREAT INTELLIGENCE REPORT
═══════════════════════════════════════════════════════════

EXECUTIVE SUMMARY:
_____________________________________________________
_____________________________________________________

FINDINGS:
┌─────────────────────────────────────────────────┐
│ Severity: [HIGH/MEDIUM/LOW]                     │
│ Confidence: [HIGH/MEDIUM/LOW]                   │
│ Source: [URL/Forum]                             │
│ Description:                                    │
│ _____________________________________________   │
│ _____________________________________________   │
└─────────────────────────────────────────────────┘

INDICATORS OF COMPROMISE (IOCs):
- Email addresses: _____________________________
- IP addresses: _________________________________
- Domains: _____________________________________
- Bitcoin addresses: ___________________________

RECOMMENDATIONS:
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

MITIGATION ACTIONS:
□ Reset compromised credentials
□ Monitor for suspicious activity
□ Inform affected users
□ Enhanced monitoring
□ Legal/Law Enforcement notification

TIMELINE:
- Discovery: ___________________________________
- Analysis complete: ___________________________
- Report delivered: ____________________________
═══════════════════════════════════════════════════════════
```

---

## 🎓 Sammanfattning

### Vad du har lärt dig:

✅ **Tor Fundamentals** - Hur Tor fungerar, installation, säkerhet
✅ **ZAP + Tor Integration** - Scanna darkweb-sajter säkert
✅ **I2P Networks** - Alternativa anonyma nätverk
✅ **Darkweb OSINT** - Sökning, scraping, link analysis
✅ **Threat Intelligence** - Monitoring, IOC collection, reporting
✅ **OpSec** - Håll dig säker under research
✅ **PGP Encryption** - Kryptera kommunikation

### Verktyg du nu behärskar:

🔧 Tor Browser & Tor Service
🔧 OWASP ZAP över Tor
🔧 I2P Router
🔧 Python för darkweb automation
🔧 PGP/GPG för kryptering
🔧 Whonix/Tails för maximal anonymitet

### Din Darkweb Research Toolkit:

```
DARKWEB WORKFLOW:
═══════════════════════════════════════════════════════════
1. Setup: Tor/VPN, Whonix/Tails, PGP keys
2. Reconnaissance: Ahmia, Hidden Wiki, forum search
3. Collection: Screenshots, HTML archives, IOCs
4. Analysis: Link analysis, cryptocurrency tracking
5. Reporting: STIX/MISP feeds, management reports
6. Defense: Implement countermeasures, monitoring
```

---

## ⚠️ Slutlig Påminnelse

**ANVÄND DENNA KUNSKAP ETISKT:**

```
✅ GODKÄND ANVÄNDNING:
- Defensive security research
- Threat intelligence för din organisation
- Penetration testing (med tillstånd)
- Academic research
- Law enforcement (med mandat)

❌ FÖRBJUDEN ANVÄNDNING:
- Illegal handel
- Hacking utan tillstånd
- Distribution av malware
- Brott av något slag
- Kränkning av privacy

DU ÄR ANSVARIG FÖR DINA HANDLINGAR.
Darkweb-kunskap är kraftfullt - använd det klokt!
```

---

**🔒 "With great power comes great responsibility." - Uncle Ben**

**Lycka till med din darkweb threat intelligence-resa! Stay safe, stay legal, stay ethical.** 🕵️🔐

---

**[🏠 Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)** | **[📚 Extra Guide](OSINT_ZAP_Guide_Extra.md)**

---

**© 2024 | För utbildnings- och defensive security-ändamål endast | Använd alltid lagligt och etiskt**
