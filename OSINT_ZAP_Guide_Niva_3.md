# 🔬 Nivå 3: Tekniska Verktyg och Metoder - Systematisk OSINT och ZAP

> **"In God we trust, all others must bring data." - W. Edwards Deming**
>
> 📚 Läsningstid: 45-60 min | 🎯 Övningar: 5 | 💡 Svårighetsgrad: Medel/Avancerad

---

## 🗺️ Navigation
**[⬅️ Tillbaka till Nivå 2](OSINT_ZAP_Guide_Niva_2.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 4](OSINT_ZAP_Guide_Niva_4.md)**

---

## 🎯 Vad du lär dig i denna nivå

Efter att ha läst Nivå 3 kommer du att:
- ✅ Behärska Maltego för visuell länkanalys och OSINT-kartläggning
- ✅ Använda theHarvester för email och subdomain enumeration
- ✅ Utforska Shodan för IoT och server reconnaissance
- ✅ Bemästra Recon-ng för modulär OSINT
- ✅ Använda ZAP Spider för att kartlägga webbapplikationer
- ✅ Utföra fuzzing och parameter manipulation
- ✅ Testa authentication och session management
- ✅ Hitta och verifiera XSS-sårbarheter praktiskt
- ✅ Följa en systematisk penetrationstestningsmetodik

---

## 🕸️ Del 1: Maltego - Visuell OSINT-kartläggning

### 🎯 Vad är Maltego?

**Maltego** är ett kraftfullt verktyg för visuell länkanalys och OSINT-undersökningar.

**Tänk på det som:**
- 🧩 Ett pusselverktyg som sätter ihop information visuellt
- 🗺️ En karta över hur entiteter (personer, företag, domäner) är sammanlänkade
- 🔍 En automatiserad OSINT-robot som gör många sökningar åt dig

### 📊 Maltego Koncept

```
MALTEGO ENTITIES (Entiteter)
═══════════════════════════════════════════════════════════════

👤 Person
   ├─ Email Address
   ├─ Phone Number
   ├─ Social Media Profile
   └─ Physical Address

🏢 Organization (Företag)
   ├─ Domain
   ├─ Website
   ├─ Employees
   └─ Phone Numbers

🌐 Domain
   ├─ DNS Records
   ├─ IP Address
   ├─ Subdomains
   ├─ Email Addresses
   └─ SSL Certificate

🔢 IP Address
   ├─ Geolocation
   ├─ Netblock (IP-range)
   ├─ AS Number
   └─ Open Ports

TRANSFORMS (Omvandlingar)
═══════════════════════════════════════════════════════════════
Person → Email Addresses (hitta alla emails)
Domain → IP Address (DNS lookup)
Email → Social Media (hitta Twitter/LinkedIn)
Company → Employees (hitta anställda på LinkedIn)
Domain → Subdomains (hitta alla subdomains)
```

### 💾 Installation och Setup

#### Maltego CE (Community Edition - Gratis)

**Steg 1: Ladda ner**
```
https://www.maltego.com/downloads/
→ Välj "Maltego CE (Community Edition)"
→ Gratis för icke-kommersiellt bruk
```

**Steg 2: Skapa konto**
```
1. Registrera på maltego.com
2. Aktivera via email
3. Logga in i Maltego-appen
```

**Steg 3: Första start**
```
┌────────────────────────────────────────────────┐
│  Maltego Setup Wizard                          │
│                                                │
│  Välj: "Maltego CE (Free)"                     │
│  Login med ditt konto                          │
│                                                │
│  Install Transforms:                           │
│  ☑ Paterva CTAS (gratis)                      │
│  ☑ VirusTotal Public API (gratis, kräver key) │
│  ☑ Have I Been Pwned (gratis)                 │
│  ☐ Shodan (kräver API-key, $59/mån)          │
│                                                │
└────────────────────────────────────────────────┘
```

### 🎯 Maltego Interface

```
MALTEGO HUVUDFÖNSTER
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [File] [Machines] [View] [Entities] [Transforms] [Help]    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Palette]         │         [Graph Canvas]                │
│  Entities:         │                                        │
│  📧 Email          │    👤 ──→ 📧 ──→ 🌐                    │
│  🌐 Domain         │     │           │                      │
│  🔢 IP             │     ↓           ↓                      │
│  👤 Person         │    📱          🔢                       │
│  🏢 Company        │                                        │
│  📱 Phone          │    [Visual relationship map]           │
│  🐦 Twitter        │                                        │
│  💼 LinkedIn       │                                        │
│                    │                                        │
├────────────────────┴─────────────────────────────────────────┤
│  [Detail View]  [Property View]  [Transform Output]        │
│  Selected: email@example.com                                │
│  Type: EmailAddress                                         │
│  Weight: 100                                                │
└─────────────────────────────────────────────────────────────┘
```

### 🔍 Grundläggande Maltego-undersökning

**Scenario:** Undersök domänen "example.com"

**Steg 1: Lägg till Entity**
```
1. Från Palette, dra "Domain" till Canvas
2. Dubbelklicka och skriv: example.com
3. Enter
```

**Steg 2: Kör Transforms**
```
Högerklicka på domain → Run Transform

Användbara transforms:
─────────────────────────────────────────────────
📧 To Email Addresses [Find email addresses]
   → Hittar emails som använder denna domän

🔢 To DNS Name - NS (Nameserver)
   → Hittar nameservers (hosting-info)

🔢 To IP Address
   → DNS lookup till IP

🌐 To Domains [DNS]
   → Hittar subdomains

🔐 To SSL Certificate
   → SSL cert-info och andra domäner på samma cert

👤 To Person [From WHOIS Info]
   → Hitta ägare/kontakter

🏢 To Companies [From WHOIS]
   → Företag kopplat till domänen
```

**Steg 3: Analysera Resultatet**

```
EXEMPEL-GRAF EFTER TRANSFORMS:
═══════════════════════════════════════════════════════════════

              example.com (Domain)
                    │
        ┌───────────┼───────────┬─────────────┐
        │           │           │             │
    📧 Emails   🔢 IP      🌐 Subdomains  🔐 SSL Cert
        │       (1.2.3.4)       │             │
    ┌───┼───┐       │      ┌────┼────┐   other-domain.com
    │   │   │       │      │    │    │
  admin contact  🌍 Location  www  api  mail
  sales  info    Stockholm
   │
  👤 John Doe
   │
  💼 LinkedIn
  🐦 Twitter
```

### 🎨 Maltego Machines (Automation)

**Machines** = Fördefinierade arbetsflöden som kör flera transforms automatiskt

**Användbara Machines:**

```
COMPANY STALKER
─────────────────────────────────────────────────
Input: Company name (t.ex. "Spotify")
Output: Alla domäner, emails, personer, social media

Perfekt för: Corporate reconnaissance

FOOTPRINT L1
─────────────────────────────────────────────────
Input: Domain
Output: Basic footprint (IPs, emails, DNS)

Perfekt för: Quick overview

PERSON - EMAIL ADDRESS
─────────────────────────────────────────────────
Input: Email address
Output: Social media profiles, phone, location

Perfekt för: Person OSINT
```

**Köra en Machine:**
```
1. Toolbar → "Machines" → "Company Stalker"
2. Ange företagsnamn
3. [Finish and Run]
4. Vänta 5-15 minuter
5. Analysera grafen!
```

### 🛡️ Maltego Tips & Best Practices

**1. Layouthantering:**
```
Problem: Grafen blir rörig med 100+ noder

Lösningar:
→ Använd layouts: [Block] [Organic] [Hierarchical]
→ Gruppera entities: Högerklicka → Group
→ Ta bort ointressanta: Delete
→ Filtrera på entity-typ
```

**2. Exportera resultat:**
```
File → Export Graph → PNG/PDF/CSV

För rapporter:
→ PNG (visuellt)
→ CSV (alla entities till Excel)
```

**3. API Keys för mer data:**
```
Gratis API keys som förbättrar Maltego:
─────────────────────────────────────────────────
VirusTotal: https://www.virustotal.com/gui/join-us
  → Gratis: 500 requests/dag

Have I Been Pwned: https://haveibeenpwned.com/API/Key
  → Gratis för research

Shodan: https://account.shodan.io/
  → $59 en gång (lifetime för API)
  → 100 query credits/mån på gratis
```

---

## 🌐 Del 2: theHarvester - Email & Subdomain Enumeration

### 🎯 Vad är theHarvester?

**theHarvester** är ett kommandoradsverktyg för att samla:
- 📧 Email-adresser
- 🌐 Subdomains
- 👤 Namn
- 🔢 IP-adresser
- 🔗 URLs

...från publika källor som Google, Bing, LinkedIn, etc.

### 💾 Installation

```bash
# Linux (Kali har det förinstallerat)
sudo apt install theharvester

# Via pip
pip3 install theHarvester

# Från GitHub (senaste version)
git clone https://github.com/laramies/theHarvester
cd theHarvester
pip3 install -r requirements.txt
python3 theHarvester.py
```

### 🔍 Grundläggande Användning

**Syntax:**
```bash
theHarvester -d <domain> -l <antal resultat> -b <källa>
```

**Exempel 1: Hitta emails på en domän**
```bash
# Sök efter emails på example.com via Google
theHarvester -d example.com -l 500 -b google

# Output:
[*] Target: example.com
[*] Searching Google...

[*] Emails found:
──────────────────────────────────────
admin@example.com
contact@example.com
info@example.com
support@example.com
sales@example.com
```

**Exempel 2: Hitta subdomains**
```bash
# Använd flera källor samtidigt
theHarvester -d example.com -l 500 -b google,bing,dnsdumpster

# Output:
[*] Hosts found:
──────────────────────────────────────
www.example.com:93.184.216.34
mail.example.com:93.184.216.35
api.example.com:93.184.216.36
dev.example.com:93.184.216.37
staging.example.com:93.184.216.38
admin.example.com:93.184.216.39
```

### 📚 theHarvester Källor (Engines)

```
POPULÄRA KÄLLOR
═══════════════════════════════════════════════════════════════
Källa           Typ           API Key?   Beskrivning
───────────────────────────────────────────────────────────────
google          Sökmotor      Nej        Emails, subdomains från Google
bing            Sökmotor      Nej        Microsoft Bing
baidu           Sökmotor      Nej        Kinesisk sökmotor
yahoo           Sökmotor      Nej        Yahoo search

dnsdumpster     DNS           Nej        Subdomain enumeration
crtsh           SSL Cert      Nej        Certificate Transparency logs
certspotter     SSL Cert      Nej        Certificate Transparency

shodan          IoT/Server    JA         IoT/server reconnaissance
hunter          Email         JA         Email finder service
virustotal      Threat Intel  JA         Domain/IP intel

linkedin        Social        Nej*       LinkedIn profiles (*rate limited)
twitter         Social        Nej        Twitter mentions

REKOMMENDERADE KOMBINATIONER
═══════════════════════════════════════════════════════════════
För emails:       -b google,bing,hunter,yahoo
För subdomains:   -b google,dnsdumpster,crtsh,certspotter
För allt:         -b all (OBS: Långsamt!)
```

### 🎯 Avancerad Användning

**1. Spara resultat:**
```bash
# HTML-rapport
theHarvester -d example.com -b google -f results_example

# Output: results_example.html, results_example.xml, results_example.json
```

**2. Använd proxies (för anonymitet):**
```bash
# Använd Tor/proxies
theHarvester -d example.com -b google -p
```

**3. DNS-brute force:**
```bash
# Brute force subdomains (aggressivt!)
theHarvester -d example.com -b google -c

# OBS: Skickar många requests! Använd endast på egna domäner.
```

**4. Shodan integration:**
```bash
# Kräver Shodan API key
# Lägg till i ~/.theHarvester/api-keys.yaml:
# shodan_key: YOUR_API_KEY_HERE

theHarvester -d example.com -b shodan

# Output: Alla IPs och öppna portar kopplade till domänen
```

### 🐍 Python Script med theHarvester

```python
#!/usr/bin/env python3
"""
Automatiserad theHarvester-script
"""

import subprocess
import json

def harvest_domain(domain, sources=['google', 'bing', 'dnsdumpster']):
    """Kör theHarvester och returnera resultat"""

    results = {
        'emails': [],
        'hosts': [],
        'ips': []
    }

    for source in sources:
        print(f"[*] Harvesting från {source}...")

        cmd = [
            'theHarvester',
            '-d', domain,
            '-b', source,
            '-f', f'output_{domain}_{source}'
        ]

        try:
            subprocess.run(cmd, check=True, capture_output=True)

            # Läs JSON-resultat
            with open(f'output_{domain}_{source}.json', 'r') as f:
                data = json.load(f)

                results['emails'].extend(data.get('emails', []))
                results['hosts'].extend(data.get('hosts', []))
                results['ips'].extend(data.get('ips', []))

        except Exception as e:
            print(f"[!] Error med {source}: {e}")

    # Ta bort duplicates
    results['emails'] = list(set(results['emails']))
    results['hosts'] = list(set(results['hosts']))
    results['ips'] = list(set(results['ips']))

    return results

# Använd scriptet
if __name__ == "__main__":
    domain = "example.com"

    print(f"[*] Starting reconnaissance på {domain}")
    results = harvest_domain(domain)

    print(f"\n[+] Resultat för {domain}")
    print(f"  Emails: {len(results['emails'])}")
    print(f"  Hosts: {len(results['hosts'])}")
    print(f"  IPs: {len(results['ips'])}")

    print("\n[*] Emails:")
    for email in sorted(results['emails']):
        print(f"  - {email}")

    print("\n[*] Subdomains:")
    for host in sorted(results['hosts']):
        print(f"  - {host}")
```

---

## 🔍 Del 3: Shodan - Internet of Things & Server Reconnaissance

### 🎯 Vad är Shodan?

**Shodan** = "Google för Internet of Things"

Istället för att indexera webbsidor, indexerar Shodan:
- 🌐 Webservrar
- 📹 Webcams
- 🏭 Industrial Control Systems (SCADA)
- 🖨️ Skrivare
- 🔌 Routrar
- ☁️ Cloud-tjänster
- 🗄️ Databaser (exponerade!)

**Varför är det användbart?**
- 🔍 Reconnaissance - Hitta attack surface
- 🛡️ Defensive - Hitta exponerade system i DIN organisation
- 📊 Research - Statistik om internet

### 🌐 Shodan Web Interface

**Steg 1: Skapa konto**
```
https://account.shodan.io/register
→ Gratis tier: 100 query credits
→ Betald: $59 (lifetime API access)
```

**Steg 2: Basic Search**
```
Sök: "apache"
→ Alla Apache-servrar

Sök: "country:SE"
→ Alla enheter i Sverige

Sök: "port:22"
→ Alla enheter med SSH öppet
```

### 🔎 Shodan Search Filters

```
SHODAN FILTERS
═══════════════════════════════════════════════════════════════
Filter          Beskrivning              Exempel
───────────────────────────────────────────────────────────────
country:        Land (ISO kod)           country:SE (Sverige)
city:           Stad                     city:"Stockholm"
geo:            GPS-koordinater          geo:59.3293,18.0686
port:           Portnummer               port:80, port:443
os:             Operativsystem           os:"Windows 10"
product:        Produkt/mjukvara         product:"Apache"
version:        Version                  version:"2.4.41"
hostname:       Hostname                 hostname:"example.com"
net:            IP-range (CIDR)          net:192.168.0.0/16
asn:            AS Number                asn:AS15169 (Google)
org:            Organisation             org:"Google"
isp:            Internet Service Provider isp:"Telia"

AVANCERADE
═══════════════════════════════════════════════════════════════
http.title:     HTTP title-tag           http.title:"Admin Panel"
http.html:      HTML-innehåll            http.html:"password"
ssl:            SSL/TLS-info             ssl:"example.com"
vuln:           Sårbarheter (CVE)        vuln:CVE-2014-0160
has_screenshot: Har screenshot           has_screenshot:true
```

### 🎯 Shodan Search Exempel

**1. Hitta exponerade webcams:**
```
Sök: "Server: webcamXP" port:8080
Resultat: Webcams utan autentisering!

⚠️ ETIK: TITTA INTE på folks privata kameror! Detta är för att förstå risker.
```

**2. Hitta MongoDB-databaser (exponerade):**
```
Sök: "MongoDB Server Information" port:27017 -authentication

Resultat: Databaser öppna utan lösenord!
```

**3. Hitta Raspberry Pi:**
```
Sök: "Raspbian" country:SE

Resultat: Alla Raspberry Pi i Sverige
```

**4. Hitta specifikt företag:**
```
Sök: org:"Spotify" country:SE

Resultat: Alla Spotify's servrar i Sverige
```

**5. Hitta sårbara servrar:**
```
Sök: vuln:CVE-2014-0160 country:SE

Resultat: Servrar i Sverige sårbara för Heartbleed
```

**6. Industrial Control Systems:**
```
Sök: "SCADA" country:SE

⚠️ VARNING: RÖR INTE! Dessa system styr kritisk infrastruktur.
```

### 🐍 Shodan API & Python

**Installation:**
```bash
pip install shodan
```

**Get API Key:**
```
1. Logga in på Shodan
2. Gå till: https://account.shodan.io/
3. Kopiera "API Key"
```

**Python-script:**
```python
#!/usr/bin/env python3
import shodan

# Din API key
SHODAN_API_KEY = "YOUR_API_KEY_HERE"

# Initiera Shodan API
api = shodan.Shodan(SHODAN_API_KEY)

def search_shodan(query):
    """Sök på Shodan"""
    try:
        results = api.search(query)

        print(f"[+] Hittade {results['total']} resultat")
        print(f"[*] Visar första {len(results['matches'])}:\n")

        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Organisation: {result.get('org', 'N/A')}")
            print(f"OS: {result.get('os', 'N/A')}")
            print(f"Port: {result['port']}")
            print(f"Hostname: {result.get('hostnames', ['N/A'])[0]}")
            print(f"Location: {result.get('location', {}).get('city', 'Unknown')}, {result.get('location', {}).get('country_name', 'Unknown')}")
            print(f"Data:\n{result['data'][:200]}...")
            print("-" * 60)

    except shodan.APIError as e:
        print(f"[!] Error: {e}")

def get_host_info(ip):
    """Få detaljerad info om specifik IP"""
    try:
        host = api.host(ip)

        print(f"\n[+] Information för {ip}:")
        print(f"Organisation: {host.get('org', 'N/A')}")
        print(f"OS: {host.get('os', 'N/A')}")
        print(f"Country: {host.get('country_name', 'N/A')}")
        print(f"City: {host.get('city', 'N/A')}")

        print(f"\nÖppna portar:")
        for item in host['data']:
            print(f"  Port {item['port']}: {item.get('product', 'Unknown')}")

        if 'vulns' in host:
            print(f"\nSårbarheter:")
            for vuln in host['vulns']:
                print(f"  - {vuln}")

    except shodan.APIError as e:
        print(f"[!] Error: {e}")

# Exempel
if __name__ == "__main__":
    # Sök
    search_shodan("apache country:SE")

    # Specifik host
    get_host_info("8.8.8.8")  # Google DNS
```

### 🛡️ Defensive Shodan - Hitta DIN Exponering

**Använd Shodan för att hitta VAD attackers kan hitta om DIG:**

```bash
# Hitta alla dina servrar
shodan search "org:DittFöretag"

# Hitta exponerade admin-paneler
shodan search "http.title:admin hostname:ditt-företag.se"

# Hitta öppna databaser
shodan search "MongoDB hostname:ditt-företag.se"

# Hitta gamla sårbara servrar
shodan search "hostname:ditt-företag.se vuln:*"
```

**Åtgärda:**
1. Stäng onödiga portar
2. Kräv autentisering på alla tjänster
3. Uppdatera mjukvara (patcha sårbarheter)
4. Använd brandvägg

---

## 🕷️ Del 4: OWASP ZAP - Spider och Manual Testing

### 🎯 ZAP Spider - Kartlägg Hela Webbplatsen

**Spider** = En robot som "kryper" genom webbplatsen och följer alla länkar.

**Två typer:**
1. **Traditional Spider** - Följer HTML-länkar (<a href="">)
2. **AJAX Spider** - Kör JavaScript och hittar dynamiskt innehåll

#### Traditional Spider

**Steg 1: Konfigurera Spider**
```
ZAP → Tools → Options → Spider

Inställningar:
─────────────────────────────────────────────────
Max Depth: 5 (hur djupt att följa länkar)
Max Children: 0 (unlimited)
Max Duration: 60 min
Number of Threads: 5
```

**Steg 2: Kör Spider**
```
1. Högerklicka på target i Sites-tree
2. Attack → Spider
3. Välj Context (om du har)
4. [Start Scan]
```

**Steg 3: Övervaka Progress**
```
ZAP SPIDER PANEL
═══════════════════════════════════════════════════════════════
Status: Running...
Progress: ████████░░░░░░░░ 45%

URLs Found: 387
URLs Processed: 175

Duration: 5m 32s
Requests/sec: 12

[Pause] [Stop] [Clear]
```

#### AJAX Spider (För moderna Single-Page Apps)

```
1. Högerklicka på target
2. Attack → AJAX Spider
3. Browser: Firefox Headless (rekommenderat)
4. Max Duration: 10 min
5. [Start Scan]

AJAX Spider kör faktiskt en webbläsare och klickar runt!
→ Hittar React/Angular/Vue.js-routes
→ Långsammare men mer komplett
```

### 🎯 Manual Explore & Active Scan

**Manual Explore** = Du surfar manuellt medan ZAP lär sig struktur

**Steg 1: Manual Explore**
```
Quick Start → Manual Explore
URL: http://localhost (DVWA eller din test-site)
[Launch Browser]

→ ZAP öppnar webbläsare med HUD (Heads Up Display)
```

**Steg 2: ZAP HUD (Heads Up Display)**
```
ZAP HUD OVERLAY
═══════════════════════════════════════════════════════════════

    [🔍 Spider]  [🎯 Attack]  [🚨 Alerts]  [🔧 Settings]

    Din webbsida visas här...

    Höger sidebar:
    ├─ 🕷️ Spider current site
    ├─ 🎯 Active Scan current site
    ├─ 🔍 Show all alerts
    └─ 🛠️ Enable/Disable HUD

    För varje HTTP request ser du:
    ┌──────────────────────────────────────┐
    │ GET /login.php                       │
    │ Status: 200                          │
    │ [🔍 Inspect] [✏️ Replay] [🎯 Fuzz]  │
    └──────────────────────────────────────┘
```

**Steg 3: Active Scan**
```
När du utforskat tillräckligt:
1. Högerklicka på site i Sites-tree
2. Attack → Active Scan
3. Policy: Default (eller välj Custom)
4. [Start Scan]

Active Scan testar:
─────────────────────────────────────────────────
✓ SQL Injection
✓ XSS (Reflected & Stored)
✓ Path Traversal
✓ Command Injection
✓ CSRF
✓ XXE
✓ Security Headers
✓ Cookie flags
✓ ... och mycket mer!
```

### 🎨 Fuzzing med ZAP

**Fuzzing** = Testa med massa olika inputs för att hitta buggar

**Scenario:** Testa login-formulär för SQL Injection

**Steg 1: Fånga Request**
```
1. I ZAP HUD eller History, hitta login-requesten:

POST /login.php HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded

username=admin&password=test123
```

**Steg 2: Öppna i Fuzzer**
```
Högerklicka på request → Attack → Fuzz
```

**Steg 3: Markera Parameter**
```
Markera värdet som ska fuzzas:

username=admin&password=test123
          ^^^^^

[Add...] → [Payloads]
```

**Steg 4: Välj Payload**
```
ZAP FUZZER - Payload Dialog
═══════════════════════════════════════════════════════════════
Type: File Fuzzers

Välj:
☑ jbrofuzz / SQL Injection
☑ fuzzdb / SQL Injection
☑ Custom wordlist...

[Add] [OK]
```

**Steg 5: Kör Fuzzer**
```
[Start Fuzzer]

FUZZER RESULTAT
═══════════════════════════════════════════════════════════════
Payload                     State    Code   Time    Size
───────────────────────────────────────────────────────────────
admin' OR '1'='1            Success  200    245ms   1234
admin' OR '1'='1'--         Success  200    198ms   1234
admin' OR '1'='1'#          Success  200    203ms   1234
admin'; DROP TABLE users--  Success  500    412ms   567   ⚠️
' OR 1=1--                  Success  200    189ms   1234
' UNION SELECT NULL--       Error    500    298ms   432

Intressant: Payload 4 gav 500 error (kanske sårbar?)
```

**Steg 6: Analysera**
```
Dubbelklicka på intressant payload för att se response:

HTTP/1.1 500 Internal Server Error
...

You have an error in your SQL syntax...
                                    ^^^^^
                            SÅRBAR FÖR SQLi!
```

### 🍪 Session Management Testing

**Testa om sessions är säkra:**

**1. Cookie Flags:**
```
I ZAP Alerts, leta efter:

🟡 Cookie without HttpOnly flag
🟡 Cookie without Secure flag
🟡 Cookie without SameSite attribute

Lösning: Sätt rätt flags i backend:
Set-Cookie: session=abc123; HttpOnly; Secure; SameSite=Strict
```

**2. Session Fixation:**
```
Test:
1. Logga in
2. Kopiera session cookie
3. Logga ut
4. Använd gamla cookien igen
5. Om du fortfarande är inloggad → Sårbart!
```

**3. Session Timeout:**
```
Test:
1. Logga in
2. Vänta 30 min (eller längre)
3. Försök använda applikationen
4. Ska loggas ut automatiskt

Om inte → Sessions timeout för långt (säkerhetsrisk)
```

### 🔐 Authentication Testing

**ZAP Form-Based Auth:**

**Steg 1: Definiera Context**
```
Right-click on site → Include in Context → New Context

Context Name: "DVWA"
```

**Steg 2: Konfigurera Authentication**
```
ZAP → Tools → Options → Authentication

Context: DVWA
Authentication Method: Form-based Authentication

Login Form Target URL: http://localhost/login.php
Login Request POST Data: username={%username%}&password={%password%}

Logged In Indicator (regex): \QLogout\E
Logged Out Indicator (regex): \QLogin\E
```

**Steg 3: Lägg till User**
```
Context: DVWA → Users → Add

Username: admin
Password: password

[Enabled]
```

**Steg 4: Test**
```
Nu när du kör Active Scan:
→ ZAP loggar in automatiskt
→ Testar authenticated areas
→ Re-authenticates om session timeout
```

---

## 🎯 Övningar - Nivå 3

### Övning 3.1: Maltego-undersökning av en Organisation 🕸️

**Mål:** Använd Maltego för att kartlägga ett företag.

**Välj ett företag:** (Välj ett STORT publikt företag, t.ex. Spotify, Ericsson, H&M)

```
Företag att undersöka: _______________________________
```

**Uppgift 1: Domain Investigation**
```
1. Öppna Maltego
2. Lägg till "Company" entity
3. Skriv företagsnamnet
4. Run Transform: "To Domains [DNS]"

Antal domäner hittade: _____
3 intressanta domäner:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________
```

**Uppgift 2: Email Harvesting**
```
5. Välj huvuddomänen
6. Run Transform: "To Email Addresses"

Antal emails hittade: _____
Pattern (t.ex. firstname.lastname@): ___________

Exempel-emails:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________
```

**Uppgift 3: Person Discovery**
```
7. Välj en email
8. Run Transform: "To Person [From Email]"
9. Från Person: "To Social Media Profiles"

Hittade du LinkedIn/Twitter? Ja / Nej
Titel/Position: _________________________________
```

**Uppgift 4: Infrastructure**
```
10. Välj huvuddomänen
11. Run Transform: "To IP Address [DNS]"
12. Från IP: "To Location [From IP Address]"

IP-adress: _____________________________________
Hosting location: _______________________________
ASN/Organisation: ________________________________
```

**Uppgift 5: Company Stalker Machine**
```
13. Machines → "Company Stalker"
14. Input: Företagsnamnet
15. Vänta 10-15 min

RESULTAT (total):
───────────────────────────────────────────────
Domains: _____
Emails: _____
People: _____
Social Profiles: _____
IP Addresses: _____
```

**Dokumentera:**
```
MALTEGO-GRAF BESKRIVNING:
Beskriv de viktigaste sambanden du hittade:
_________________________________________________
_________________________________________________
_________________________________________________

Exportera graf: File → Export → PNG
Bifoga: maltego_[företag].png
```

**Facit/Förväntningar:**
- Stora företag har 10+ domäner
- 50-200+ emails för stora företag
- Många anställda på LinkedIn
- Hosting ofta via cloud (AWS, Azure, Google Cloud)

---

### Övning 3.2: theHarvester - Samla Email-adresser 📧

**Mål:** Använd theHarvester för att samla emails och subdomains.

**Target:** Välj en domän (egen eller test-domän från bug bounty)

```
Target domain: _____________________________________
```

**Uppgift 1: Google Harvest**
```bash
# Kommando
theHarvester -d [domain] -l 500 -b google

Antal emails hittade: _____
Antal hosts hittade: _____

Exempel emails:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________
```

**Uppgift 2: Multi-Source Harvest**
```bash
# Använd flera källor
theHarvester -d [domain] -l 500 -b google,bing,dnsdumpster,crtsh

Källor testade: _____
Total emails: _____
Total hosts: _____

Vilken källa gav mest resultat?
_________________________________________________
```

**Uppgift 3: Subdomain Enumeration**
```bash
# Fokusera på subdomains
theHarvester -d [domain] -b dnsdumpster,crtsh -f output_subdomains

Lista alla subdomains hittade:
_________________________________________________
_________________________________________________
_________________________________________________

Intressanta subdomains (admin, dev, staging, api):
_________________________________________________
```

**Uppgift 4: Spara och Analysera**
```
Öppna: output_subdomains.html

Analysera:
1. Vilka subdomains kan vara känsliga?
   _____________________________________________

2. Vilka subdomains borde vara privata?
   _____________________________________________

3. Finns det testmiljöer exponerade (dev, staging)?
   Ja / Nej: ___________________________________
```

**Bonus: Python Automation**
```python
# Använd Python-scriptet från Del 2
python3 harvest_script.py

Jämför resultaten med manuella kommandot:
Var automatiseringen snabbare? Ja / Nej
Mer komplett? Ja / Nej
```

---

### Övning 3.3: Shodan - IoT Reconnaissance 🔍

**Mål:** Utforska Shodan och förstå exponerade enheter.

⚠️ **ETIK-PÅMINNELSE:** Interagera INTE med enheter du hittar! Endast reconnaissance.

**Uppgift 1: Grundläggande Sökningar**

```
Shodan Search 1: "apache country:SE"
Antal resultat: _____
Vanligaste versioner: ___________________________

Shodan Search 2: "MongoDB" -authentication
Antal öppna databaser: _____
Länder med flest: _______________________________
```

**Uppgift 2: Hitta Webcams**
```
Shodan Search: "Server: webcamXP" has_screenshot:true

Antal hittade: _____

REFLEKTION:
Varför är detta ett säkerhetsproblem?
_________________________________________________
_________________________________________________

Hur kan ägare skydda sig?
_________________________________________________
```

**Uppgift 3: Sårbarhetsökning**
```
Shodan Search: vuln:CVE-2014-0160 country:SE

CVE-2014-0160 = Heartbleed (kritisk sårbarhet)

Antal sårbara servrar i Sverige: _____

Är detta förvånande? Varför/varför inte?
_________________________________________________
```

**Uppgift 4: Organisationssökning**
```
Välj ett företag att analysera: _________________

Shodan Search: org:"[företagsnamn]"

Antal exponerade IPs: _____

Öppna portar (top 3):
1. Port _____ (___________ service)
2. Port _____ (___________ service)
3. Port _____ (___________ service)

Upptäckta sårbarheter (om några):
_________________________________________________
```

**Uppgift 5: Shodan API med Python**
```python
# Använd Python-scriptet från Del 3

Target: 8.8.8.8 (Google DNS)

Output förväntad:
Organisation: Google LLC
OS: N/A (DNS-server)
Country: United States

Portar öppna på 8.8.8.8:
_________________________________________________
```

**Defensive Exercise:**
```
Om du har en egen domän:

Shodan Search: hostname:[din-domän]

VAD kan attackers hitta om dig?
_________________________________________________
_________________________________________________

Åtgärder att vidta:
_________________________________________________
```

---

### Övning 3.4: ZAP Spider - Kartlägg Webbplats 🕷️

**Mål:** Använd ZAP Spider för att kartlägga en webbapplikation.

**Target:** DVWA (http://localhost) eller OWASP Juice Shop

**Uppgift 1: Traditional Spider**
```
1. Starta DVWA
2. Logga in (admin/password)
3. Set Security Level: Low
4. I ZAP: Högerklicka http://localhost
5. Attack → Spider

KONFIG:
Max Depth: 5
Max Duration: 10 min
Threads: 5

[Start Spider]

RESULTAT efter spider:
───────────────────────────────────────────────
URLs Found: _____
URLs Processed: _____
Duration: _____ min

Antal endpoints per kategori:
/vulnerabilities/sqli/: _____
/vulnerabilities/xss_r/: _____
/vulnerabilities/upload/: _____
```

**Uppgift 2: AJAX Spider**
```
6. Högerklicka http://localhost
7. Attack → AJAX Spider
8. Browser: Firefox Headless
9. Max Duration: 5 min
10. [Start]

AJAX Spider Results:
───────────────────────────────────────────────
In Scope URLs Added: _____

Hittade AJAX Spider något som Traditional Spider missade?
Ja / Nej: _________________________________________
```

**Uppgift 3: Analysera Sites-träd**
```
Efter spider, dokumentera strukturen:

Sites
└─ http://localhost
   ├─ login.php
   ├─ index.php
   ├─ vulnerabilities/
   │  ├─ sqli/
   │  ├─ xss_r/
   │  ├─ xss_s/
   │  ├─ csrf/
   │  ├─ upload/
   │  ├─ exec/
   │  ├─ fi/
   │  └─ ...
   ├─ security.php
   └─ ...

Rita eller beskriv trädet:
_________________________________________________
_________________________________________________
```

**Uppgift 4: Exclude från Spider**
```
Vissa endpoints vill du INTE spida (t.ex. logout)

11. Right-click på /logout.php
12. Exclude from → Spider

Varför är detta viktigt?
_________________________________________________
```

---

### Övning 3.5: Hitta och Exploatera XSS med ZAP 🎯

**Mål:** Hitta en Cross-Site Scripting (XSS) sårbarhet praktiskt.

**Target:** DVWA → XSS (Reflected) (Security: Low)

**Uppgift 1: Manual Testing**
```
1. Gå till DVWA → XSS (Reflected)
2. Input field: "What's your name?"
3. Testa: <script>alert('XSS')</script>
4. Submit

Resultat:
□ Alert box visas (SÅRBAR!)
□ Input sanitized (SÄKER)

Om sårbar - vad händer?
_________________________________________________
```

**Uppgift 2: ZAP Active Scan**
```
5. I ZAP: Högerklicka på XSS-sidan
6. Attack → Active Scan
7. Policy: Default
8. [Start Scan]

RESULTAT:
───────────────────────────────────────────────
Scan Duration: _____ min

Alerts:
🔴 High: _____
  - XSS (Reflected): Ja / Nej

ZAP payload som funkade:
_________________________________________________
```

**Uppgift 3: Manual Fuzzing**
```
9. I History, hitta XSS-requesten:
   GET /vulnerabilities/xss_r/?name=test

10. Right-click → Attack → Fuzz
11. Markera "test"
12. Add Payload: jbrofuzz → XSS

13. [Start Fuzzer]

FUZZER RESULTAT:
───────────────────────────────────────────────
Totala payloads testade: _____

Payloads som funkade (gav alert):
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

Vilken payload var mest effektiv?
_________________________________________________
```

**Uppgift 4: Stored XSS**
```
14. Gå till DVWA → XSS (Stored)
15. Testa i "Message" field:
    <script>alert('Stored XSS')</script>

16. Submit och refresh page

Resultat:
□ Alert visas varje gång (STORED XSS!)
□ Sanitized

Varför är Stored XSS farligare än Reflected?
_________________________________________________
_________________________________________________
```

**Uppgift 5: Bypass Filters (Security: Medium)**
```
17. Sätt DVWA Security: Medium
18. Testa samma payload → Blockerad!

19. Försök bypass med:
    <ScRiPt>alert('XSS')</ScRiPt>
    <img src=x onerror=alert('XSS')>
    <svg/onload=alert('XSS')>
    <iframe src="javascript:alert('XSS')">

Vilken bypass funkade?
_________________________________________________

Dokumentera requesten som funkade:
_________________________________________________
```

**Bonus: Real-world Impact**
```
Skriv en kort rapport om XSS-sårbarheten:

═══════════════════════════════════════════════
SÅRBARHET: Cross-Site Scripting (XSS)
───────────────────────────────────────────────
Typ: Reflected / Stored
Severity: High

URL: _________________________________________
Parameter: ___________________________________
Payload: _____________________________________

PoC (Proof of Concept):
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________

IMPACT:
- Session hijacking (stjäla cookies)
- Phishing attacks
- Keylogging
- Defacement

REKOMMENDERAD FIX:
- Input validation
- Output encoding
- Content Security Policy (CSP)
═══════════════════════════════════════════════
```

---

## 🎓 Sammanfattning Nivå 3

### Vad du har lärt dig:

✅ **Maltego** - Visuell OSINT-kartläggning och länkanalys
✅ **theHarvester** - Email och subdomain enumeration
✅ **Shodan** - IoT och server reconnaissance
✅ **ZAP Spider** - Kartlägga webbapplikationer systematiskt
✅ **ZAP Fuzzing** - Testa inputs för sårbarheter
✅ **Session Management** - Testa cookies och sessions
✅ **Authentication** - Form-based auth testing med ZAP
✅ **XSS Discovery** - Hitta och exploatera Cross-Site Scripting
✅ **Metodologi** - Systematisk approach till penetrationstesting

### Verktyg du nu behärskar:

🔧 Maltego (visuell OSINT)
🔧 theHarvester (email/subdomain enum)
🔧 Shodan (IoT/server recon)
🔧 OWASP ZAP Spider (traditional + AJAX)
🔧 ZAP Fuzzer
🔧 ZAP HUD (Heads Up Display)

### Din OSINT & Pentesting Toolkit:

```
OSINT WORKFLOW
═══════════════════════════════════════════════════════════
1. theHarvester → Emails & Subdomains
2. Shodan → Exposed services & vulnerabilities
3. Maltego → Visualize connections
4. WHOIS/DNS → Infrastructure mapping

PENTESTING WORKFLOW
═══════════════════════════════════════════════════════════
1. ZAP Spider → Map application
2. Manual Explore → Understand functionality
3. Active Scan → Automated vulnerability detection
4. Manual Testing → Deep-dive specific vulns
5. Fuzzing → Test edge cases
6. Report → Document findings
```

### Nästa Steg:

🎯 **Om du känner dig bekväm:**
→ Gå vidare till **[Nivå 4: Avancerade Tekniker](OSINT_ZAP_Guide_Niva_4.md)**

Där lär du dig:
- Corporate OSINT och DNS enumeration
- ZAP API och Python automation
- Testa för OWASP Top 10 sårbarheter
- SQL Injection praktiskt
- Bygg fullständig säkerhetsaudit (projekt!)

🔄 **Om du vill öva mer:**
→ Repetera övningarna med andra targets
→ Testa på HackTheBox eller TryHackMe
→ Utforska fler Maltego transforms
→ Experimentera med Shodan filters

---

## 🔐 Säkerhetspåminnelse

**Innan du går vidare:**

✅ **Du har lärt dig kraftfulla verktyg** - använd dem ansvarsfullt!

⚠️ **Shodan-etik:**
- Scanna INTE andras nätverk
- Interagera INTE med enheter du hittar
- Använd för DEFENSIVE ändamål (hitta DIN exponering)

⚠️ **OSINT-etik:**
- Respektera privacy även om data är publik
- Använd INTE för stalking eller trakasserier
- Rapportera data leaks ansvarsfull

⚠️ **ZAP-etik:**
- Testa ENDAST med tillstånd
- Testa INTE produktionssystem
- Använd testmiljöer (DVWA, Juice Shop)

---

**Redo för nästa nivå?**

👉 **[Fortsätt till Nivå 4: Avancerade Tekniker →](OSINT_ZAP_Guide_Niva_4.md)**

---

**[⬅️ Tillbaka till Nivå 2](OSINT_ZAP_Guide_Niva_2.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 4](OSINT_ZAP_Guide_Niva_4.md)**

---

**Nivå 3 Komplett! ✅**
*Du har nu teknisk kompetens i OSINT och pentesting! Fortsätt till Nivå 4 för avancerade tekniker.*
