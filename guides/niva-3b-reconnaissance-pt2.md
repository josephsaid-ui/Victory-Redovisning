# 🕵️ Nivå 3B: OSINT & Advanced Reconnaissance

**⏱️ Beräknad tid:** 1.5-2 timmar
**📚 Svårighetsgrad:** ⭐⭐⭐ Intermediate
**🎯 Förutsättningar:** Nivå 3A genomförd
**🎓 Lärdomsmål:** OSINT-tekniker, email harvesting, data mining, internet-wide scanning

---

## 📋 Innehåll

1. [Vad är OSINT?](#-vad-är-osint)
2. [theHarvester - Email & Data Harvesting](#-theharvester---email--data-harvesting)
3. [Maltego - Data Mining & Link Analysis](#-maltego---data-mining--link-analysis)
4. [Recon-ng - Web Reconnaissance Framework](#-recon-ng---web-reconnaissance-framework)
5. [Shodan - Internet-Wide Scanning](#-shodan---internet-wide-scanning)
6. [Praktiska OSINT-övningar](#-praktiska-osint-övningar)
7. [Självtest](#-självtest-nivå-3b)

---

## 🔍 Vad är OSINT?

### Definition

**OSINT** = **O**pen **S**ource **INT**elligence

Information som samlas från **offentligt tillgängliga källor**.

```
┌──────────────────────────────────────────────────────────┐
│  OSINT = Intelligence från offentlig information         │
│                                                          │
│  Källor:                                                 │
│  ├─ Sökmotorer (Google, Bing, etc.)                     │
│  ├─ Sociala medier (LinkedIn, Twitter, Facebook)        │
│  ├─ Företagsregister (Bolagsverket, etc.)               │
│  ├─ DNS records                                          │
│  ├─ WHOIS databases                                      │
│  ├─ Public data leaks                                    │
│  ├─ Job postings                                         │
│  ├─ News articles                                        │
│  └─ Tech documentation                                   │
└──────────────────────────────────────────────────────────┘
```

### OSINT vs Active Recon

| Aspect | OSINT (Passive) | Active Recon |
|--------|-----------------|--------------|
| **Interaktion** | Ingen direkt kontakt | Direkt interaktion med målet |
| **Detekterbart** | Mycket svårt | Lätt (logs, IDS/IPS) |
| **Legalitet** | ✅ Generellt OK (offentlig data) | ⚠️ Kräver tillstånd |
| **Exempel** | Google search, LinkedIn | Nmap scanning, ping |
| **Risk** | Låg | Kan trigga alarms |

### Vad kan vi hitta med OSINT?

**Information om företag:**
- 📧 Email-adresser (format, employees)
- 👥 Anställda (namn, titlar, kontakt)
- 🌐 Subdomains och IP-ranges
- 💼 Teknisk stack (servrar, software)
- 📱 Phone numbers
- 📍 Physical locations
- 🔐 Data leaks (breach databases)

**Information om individer:**
- 📧 Email addresses
- 👤 Usernames
- 📱 Phone numbers
- 🏠 Addresses (OBS: etik!)
- 💼 Employment history
- 🎓 Education
- 🔗 Social media profiles

**🔴 ETIK & JURIDIK:**

```
✅ OK att göra:
   - Söka offentlig information
   - Analysera company websites
   - Läsa public social media profiles
   - WHOIS lookups
   - DNS enumeration

⚠️ GRÅZON:
   - Data från leaks (redan publikt men känsligt)
   - Extensive scraping (kan bryta ToS)
   - Social engineering baserat på OSINT

❌ FÖRBJUDET:
   - Använda OSINT för stalking/harassment
   - Bryta ToS (Terms of Service)
   - Phishing baserat på OSINT
   - Privacy-intrång
   - Olaglig data aggregation
```

---

## 📧 theHarvester - Email & Data Harvesting

### 📖 Vad är theHarvester?

**theHarvester** är ett OSINT-verktyg för att samla:
- Email-adresser
- Subdomains
- Hostnames
- Employee names
- Open ports
- Banners

**Data sources:**
- Google
- Bing
- LinkedIn
- Twitter
- Shodan
- Hunter.io
- VirusTotal
- Många fler...

### Installation & Verifiering

```bash
# Förinstallerat i Kali
theHarvester --help

# Om saknas:
sudo apt install theharvester -y

# Uppdatera (viktigt för nya data sources)
cd /usr/share/theharvester
sudo pip3 install -r requirements.txt
```

### Grundläggande syntax

```bash
theHarvester -d domain.com -b source

# -d = domain (target)
# -b = source (data source)
# -l = limit (antal resultat)
```

### Data Sources

```bash
# Lista alla tillgängliga sources
theHarvester -h | grep -A 50 "Sources:"

# Populära sources:
# - google (Google search)
# - bing (Bing search)
# - linkedin (LinkedIn - kräver API)
# - twitter (Twitter)
# - shodan (Shodan - kräver API key)
# - all (alla sources - långsamt!)
```

### Exempel: Basic email harvesting

```bash
# Hitta emails för example.com via Google
theHarvester -d example.com -b google

# Output:
# [*] Target: example.com
#
# [*] Searching Google:
#     Emails found:
#     ├─ john.doe@example.com
#     ├─ jane.smith@example.com
#     ├─ contact@example.com
#     └─ support@example.com
#
#     Hosts found:
#     ├─ www.example.com
#     ├─ mail.example.com
#     └─ ftp.example.com

# Med limit (default 500)
theHarvester -d example.com -b google -l 100
```

### Exempel: Multiple sources

```bash
# Använda flera sources
theHarvester -d example.com -b google,bing

# Alla sources (långsamt, men mest comprehensive)
theHarvester -d example.com -b all

# Shodan (kräver API key)
theHarvester -d example.com -b shodan
```

### API Keys (för fler features)

Vissa sources kräver API keys:

```bash
# Konfigurera API keys
nano /etc/theHarvester/api-keys.yaml

# Exempel:
# shodan:
#   key: YOUR_SHODAN_API_KEY
# hunter:
#   key: YOUR_HUNTER_API_KEY
```

**Få API keys:**
- Shodan: https://account.shodan.io/
- Hunter.io: https://hunter.io/api
- VirusTotal: https://virustotal.com/

### Save output

```bash
# Spara till HTML
theHarvester -d example.com -b google -f output

# Skapar:
# - output.html (web-viewable)
# - output.xml (machine-readable)
# - output.json (JSON format)

# Öppna HTML:
firefox output.html
```

### Praktiskt exempel: Employee enumeration

```bash
# Hitta anställda på LinkedIn
theHarvester -d example.com -b linkedin -l 200

# Analysera email-format:
# john.doe@example.com
# jane.smith@example.com
#
# Format: firstname.lastname@example.com

# Nu vet du:
# 1. Email-format
# 2. Anställdas namn
# 3. Kan gissa fler emails (viktigt för spearphishing-defense!)
```

### theHarvester cheat sheet

```bash
# Basic email harvest
theHarvester -d domain.com -b google

# Multiple sources
theHarvester -d domain.com -b google,bing,linkedin

# With limit
theHarvester -d domain.com -b google -l 100

# All sources
theHarvester -d domain.com -b all

# Save output
theHarvester -d domain.com -b google -f filename

# DNS lookup
theHarvester -d domain.com -b google -n

# Shodan
theHarvester -d domain.com -b shodan
```

### ⚖️ Legal & Ethical use

**✅ OK att använda:**
- Din egen organisation (med tillstånd)
- Bug bounty programs (inom scope)
- Pentest med kontrakt
- Lärande på public test domains

**❌ INTE OK:**
- Phishing campaigns baserat på harvested emails
- Spam
- Stalking/harassment
- Bryta mot ToS

---

## 🔗 Maltego - Data Mining & Link Analysis

### 📖 Vad är Maltego?

**Maltego** är ett kraftfullt verktyg för:
- **Data mining** (samla information)
- **Link analysis** (visualisera relationer)
- **OSINT investigations**

**GUI-baserat** (drag-and-drop interface)

```
Maltego visar relationer mellan:
├─ Domains ↔ IP addresses
├─ Email addresses ↔ Persons
├─ Companies ↔ Employees
├─ Social media ↔ Individuals
└─ DNS records ↔ Infrastructure
```

### Maltego versions

| Version | Features | Cost | Rekommendation |
|---------|----------|------|----------------|
| **Community Edition** | Limited transforms, basics | Gratis | ✅ För lärande |
| **Classic** | More transforms | ~$999/år | Professionell |
| **XL** | Unlimited | ~$1,999/år | Enterprise |

**Vi använder Community Edition (gratis)**

### Installation

```bash
# Maltego är förinstallerat i Kali
maltego

# Första gången:
# 1. Registrera gratis account på paterva.com
# 2. Verify email
# 3. Login i Maltego
# 4. Välj "Maltego CE (Free)"
```

### Maltego Interface

```
┌─────────────────────────────────────────────────────────┐
│  Menu Bar: File, Edit, View, etc.                      │
├─────────────────────────────────────────────────────────┤
│  Toolbar: New graph, Run transforms, etc.              │
├─────────────────────────────────────────────────────────┤
│  Entity Palette: Drag entities här                      │
│  ├─ Domain                                              │
│  ├─ Person                                              │
│  ├─ Email Address                                       │
│  ├─ Phone Number                                        │
│  └─ Company                                             │
├─────────────────────────────────────────────────────────┤
│  Graph View: Visualisering av data och relationer       │
│                                                         │
│       [Company] ───── [Person1]                         │
│          │             │                                │
│          │             └─── [Email1]                    │
│          │                                              │
│       [Domain] ───── [IP Address]                       │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  Property View: Detaljer om vald entity                 │
│  Detail View: Transform results                         │
└─────────────────────────────────────────────────────────┘
```

### Grundläggande koncept

**Entities** = Datapunkter (Person, Domain, Email, etc.)

**Transforms** = Operationer som hittar information

```
Exempel Transform:
Domain (example.com)
    ↓ [To DNS Name - NS]
DNS Server (ns1.example.com)
    ↓ [To IP Address]
IP Address (1.2.3.4)
    ↓ [To Netblock]
Netblock (1.2.3.0/24)
```

### Steg-för-steg: First investigation

```
1. Öppna Maltego
2. New Graph
3. Från Entity Palette → Drag "Domain" till grafen
4. Dubbelklicka domain → Skriv: example.com
5. Högerklicka domain → Run Transform → All Transforms
6. Vänta medan Maltego hittar:
   - Subdomains
   - IP addresses
   - MX records
   - NS records
   - Email addresses
7. Visualiseringen uppdateras automatiskt
8. Utforska relationer genom att klicka på entities
```

### Populära transforms

```bash
# Domain transforms:
├─ To DNS Name (hitta subdomains)
├─ To IP Address (hitta IPs)
├─ To MX Record (email servers)
├─ To NS Record (name servers)
└─ To Email Address (hitta emails)

# Email transforms:
├─ To Person (hitta person bakom email)
├─ To Domain (hitta associerad domain)
└─ To Social Media (LinkedIn, Twitter, etc.)

# Person transforms:
├─ To Email Address
├─ To Phone Number
└─ To Social Media Profiles

# IP Address transforms:
├─ To Domain (reverse DNS)
├─ To Location (geolocation)
└─ To Netblock (IP range)
```

### Exempel: Company investigation

```
SCENARIO: Undersök company "ExampleCorp"

1. Drag "Company" entity
2. Name: ExampleCorp
3. Run Transform: "To Website"
   → Hittar: examplecorp.com

4. På domain → Run Transform: "To Email Address"
   → Hittar: contact@examplecorp.com, hr@examplecorp.com

5. På emails → Run Transform: "To Person"
   → Hittar: John Doe, Jane Smith

6. På personer → Run Transform: "To LinkedIn Profile"
   → Hittar LinkedIn-profiler

7. Resultat: Graf som visar
   Company → Domain → Emails → Personer → LinkedIn
```

### Maltego Machines (automated workflows)

**Machine** = Pre-built transform-sekvenser

```bash
# Populära machines:
├─ Company Stalker (undersök företag)
├─ Footprint L1/L2/L3 (olika djup)
├─ Person - Email Address (hitta emails för person)
└─ Find Juicy Info (hitta känslig info)

# Köra Machine:
1. Välj entity
2. Toolbar → Machines
3. Välj machine
4. Run
```

### Export results

```bash
# Exportera graf:
File → Export Graph → PNG/PDF/GraphML

# Copy data:
Högerklicka entities → Copy → Paste i spreadsheet
```

### ⚖️ Legal considerations

**Maltego samlar offentlig data** men:

```
✅ OK:
   - OSINT på public information
   - Pentest med tillstånd
   - Bug bounty research

⚠️ GRÅZON:
   - Extensive scraping (kan bryta ToS)
   - Personal information aggregation

❌ FÖRBJUDET:
   - Stalking
   - Harassment
   - Privacy violations
   - Selling aggregated data utan consent
```

---

## 📚 Recon-ng - Web Reconnaissance Framework

### 📖 Vad är Recon-ng?

**Recon-ng** är ett modulariserat web reconnaissance framework (liknande Metasploit, men för recon).

**Features:**
- Modular architecture (ladda bara de modules du behöver)
- Database storage (spara resultat)
- API integration (Google, Shodan, etc.)
- Automated workflows

```
┌──────────────────────────────────────────────────────────┐
│  Recon-ng = Metasploit för reconnaissance               │
│                                                          │
│  Modules:                                                │
│  ├─ Discovery (hitta hosts, emails, etc.)               │
│  ├─ Import (importera data från andra verktyg)          │
│  ├─ Recon (active reconnaissance)                        │
│  └─ Reporting (generera rapporter)                      │
└──────────────────────────────────────────────────────────┘
```

### Installation & Start

```bash
# Förinstallerat i Kali
recon-ng

# Om saknas:
sudo apt install recon-ng -y

# Starta:
recon-ng

# Prompt:
# [recon-ng][default] >
```

### Grundläggande kommandon

```bash
# Hjälp
help

# Lista workspaces
workspaces list

# Skapa workspace
workspaces create example_investigation

# Byta workspace
workspaces load example_investigation

# Lista modules
modules search

# Lista installerade modules
modules search -i

# Visa marketplace
marketplace search

# Installera module
marketplace install MODULE_NAME
```

### Modules & Marketplace

**Recon-ng v5+** använder marketplace-system:

```bash
# Sök modules
marketplace search

# Sök specifik typ
marketplace search gmail

# Visa module info
marketplace info recon/domains-hosts/google_site_web

# Installera module
marketplace install recon/domains-hosts/google_site_web

# Installera alla modules (tar tid!)
marketplace install all
```

**Module-kategorier:**

```
discovery/    - Upptäck hosts, emails, etc.
exploitation/ - Exploit (varsamt!)
import/       - Importera från andra verktyg
recon/        - Reconnaissance modules
reporting/    - Generera rapporter
```

### Använda modules

```bash
# Ladda module
modules load recon/domains-hosts/google_site_web

# Visa module options
options list

# Sätt SOURCE (domain att undersöka)
options set SOURCE example.com

# Kör module
run

# Resultat sparas i database
```

### Database management

```bash
# Visa domains i database
db query SELECT * FROM domains

# Visa hosts
db query SELECT * FROM hosts

# Visa contacts (personer)
db query SELECT * FROM contacts

# Export till CSV
db export /tmp/results.csv
```

### Praktiskt exempel: Domain reconnaissance

```bash
# 1. Starta recon-ng
recon-ng

# 2. Skapa workspace
workspaces create target_recon

# 3. Installera nödvändiga modules
marketplace install recon/domains-hosts/google_site_web
marketplace install recon/hosts-hosts/resolve
marketplace install recon/domains-contacts/whois_pocs

# 4. Ladda module för subdomain discovery
modules load recon/domains-hosts/google_site_web

# 5. Sätt target
options set SOURCE example.com

# 6. Kör
run

# 7. Se resultat
db query SELECT * FROM hosts

# 8. Resolve hostnames till IPs
modules load recon/hosts-hosts/resolve
run

# 9. Hitta contacts via WHOIS
modules load recon/domains-contacts/whois_pocs
options set SOURCE example.com
run

# 10. Se contacts
db query SELECT * FROM contacts
```

### API Keys

Många modules kräver API keys:

```bash
# Lista alla keys
keys list

# Lägg till key
keys add shodan_api YOUR_API_KEY_HERE
keys add google_api YOUR_GOOGLE_API_KEY

# Ta bort key
keys remove shodan_api
```

**Få API keys:**
- Shodan: https://account.shodan.io/
- Google Custom Search: https://developers.google.com/custom-search/
- VirusTotal: https://virustotal.com/

### Reporting

```bash
# Ladda reporting module
modules load reporting/html

# Sätt output fil
options set FILENAME /tmp/report.html
options set CREATOR "Your Name"
options set CUSTOMER "Client Name"

# Generera rapport
run

# Öppna rapport
firefox /tmp/report.html
```

### Recon-ng cheat sheet

```bash
# Workspace management
workspaces create NAME
workspaces load NAME
workspaces list

# Module management
marketplace search KEYWORD
marketplace install MODULE
modules load MODULE
modules search

# Options
options list
options set NAME VALUE
run

# Database
db query SELECT * FROM TABLE
db export FILE.csv

# API Keys
keys add NAME VALUE
keys list

# Common modules:
# - recon/domains-hosts/google_site_web (subdomains via Google)
# - recon/hosts-hosts/resolve (DNS resolution)
# - recon/domains-contacts/whois_pocs (WHOIS contacts)
# - recon/domains-hosts/hackertarget (subdomain enum)
```

---

## 🌍 Shodan - Internet-Wide Scanning

### 📖 Vad är Shodan?

**Shodan** = "Google för Internet of Things"

```
Google indexerar:      Shodan indexerar:
├─ Websites           ├─ Servers
├─ Images             ├─ IoT devices
├─ Text               ├─ Cameras
                      ├─ Routers
                      ├─ Industrial systems
                      ├─ SCADA
                      └─ Anything connected to internet
```

**Vad Shodan visar:**
- Open ports
- Service versions
- Banners
- Geolocation
- Organization
- Vulnerabilities

**🔴 JURIDISK VARNING:**

```
Shodan = Passiv recon (OK)
- Shodan har redan scannat internet
- Du bara söker i deras databas
- Ingen direkt interaktion med targets

MEN:
❌ Använda informationen för obehörig åtkomst = OLAGLIGT
✅ Använda för att säkra egna system = BRA
✅ Använda med tillstånd för pentest = OK
```

### Shodan Web Interface

**URL:** https://www.shodan.io/

**Konto:**
- Gratis: 1 search credit, begränsad data
- Member ($59/mån): Fler credits, API access
- Corporate: Unlimited

### Grundläggande Shodan searches

```bash
# Söka på web interface (https://shodan.io):

# Hitta Apache servers
apache

# Specifik version
apache 2.2.14

# Specifik port
port:22

# Specifikt land
country:SE

# Kombinera
apache country:SE

# Organisation
org:"Amazon"

# Hostname
hostname:.gov

# OS
os:Windows

# Before/after date
port:22 before:01/01/2020
```

### Shodan Filters

| Filter | Beskrivning | Exempel |
|--------|-------------|---------|
| `city` | City | `city:Stockholm` |
| `country` | Country code | `country:SE` |
| `geo` | Coordinates | `geo:59.3293,18.0686` |
| `hostname` | Hostname | `hostname:example.com` |
| `net` | Network range | `net:192.168.1.0/24` |
| `org` | Organization | `org:"Telia"` |
| `os` | Operating system | `os:Linux` |
| `port` | Port number | `port:80` |
| `before/after` | Time filter | `before:01/01/2020` |

### Shodan CLI

```bash
# Installera Shodan CLI
sudo apt install shodan -y

# ELLER via pip:
pip3 install shodan

# Initiera (kräver API key)
shodan init YOUR_API_KEY

# Få API key:
# 1. Registrera på shodan.io
# 2. Gå till Account → API Key
# 3. Copy key
```

### Shodan CLI kommandon

```bash
# Sök hosts
shodan search apache

# Visa host info
shodan host 1.2.3.4

# Räkna resultat
shodan count apache country:SE

# Download data
shodan download output.json.gz apache

# Parse downloaded data
shodan parse --fields ip_str,port,org output.json.gz

# Stats
shodan stats --facets country apache
```

### Shodan för defensiv säkerhet

**Hitta DIN egen exponering:**

```bash
# Sök din organisations IP-range
net:YOUR_IP_RANGE

# Vad hittar du?
# ├─ Öppna portar som inte borde vara publika?
# ├─ Outdated services?
# ├─ Default credentials?
# ├─ Misconfigured devices?
# └─ IoT-devices som är exponerade?

# Exempel: Hitta exponerade databaser
"port:3306 mysql" org:"Your Company"

# Exponerade kameror
"webcamXP" org:"Your Company"

# Exponerade RDP
"port:3389" org:"Your Company"
```

### Shodan Exploits

Shodan har också exploit-databas:

```bash
# Sök exploits
shodan search exploits:*

# CVE-specifik
cve:CVE-2021-44228 (Log4Shell)

# Visa exploits för host
shodan host 1.2.3.4 --vulnerabilities
```

### Shodan Dorks (search queries)

**Populära Shodan Dorks:**

```bash
# Default passwords
"default password"

# Webcams
"webcamXP"
"IP Webcam Server"

# SCADA systems
"SCADA"
port:502

# Databases
"MongoDB Server Information" port:27017
"MySQL" port:3306

# Printers
"HP LaserJet" port:9100

# Elasticsearch (ofta exposed)
port:9200 "elasticsearch"

# Redis (databas, ofta ingen auth)
port:6379 "Redis"

# Jenkins (CI/CD, ofta ingen auth)
"Dashboard [Jenkins]"
```

### Praktiskt exempel: Company assessment

```bash
# 1. Sök organisationens namn
org:"Example Corp"

# 2. Analysera resultat:
# - Hur många hosts hittades?
# - Vilka services är exponerade?
# - Finns default passwords?
# - Outdated software?

# 3. Specifika services:
org:"Example Corp" port:22  # SSH
org:"Example Corp" port:3389  # RDP
org:"Example Corp" port:80  # HTTP

# 4. Vulnerabilities
org:"Example Corp" vuln:*
```

### Shodan Monitor

**Monitor** = Övervaka din egen infrastruktur kontinuerligt

```
Shodan.io → Monitor (kräver paid account)

1. Lägg till IP-ranges
2. Shodan övervakar för:
   - Nya öppna portar
   - Nya services
   - Nya sårbarheter
3. Email alerts när ändringar upptäcks
```

---

## 🧪 Praktiska OSINT-övningar

### Övning 1: theHarvester - Email Harvesting

```bash
# 🎯 Mål: Hitta emails för en public organization

# 1. Välj target (använd ENDAST publika test-domains eller din egen):
# - example.com (safe test domain)
# - ELLER: Din egen organisations domain (med tillstånd!)

# 2. Basic harvest
theHarvester -d example.com -b google -l 100

# 3. Multiple sources
theHarvester -d example.com -b google,bing

# 4. Spara resultat
theHarvester -d example.com -b google -f example_harvest

# 5. Analysera:
# - Email format? (firstname.lastname@?)
# - Hur många employees hittades?
# - Subdomains?

# 6. Öppna HTML rapport
firefox example_harvest.html
```

### Övning 2: Maltego - Company Investigation

```bash
# 🎯 Mål: Visualisera företags digitala footprint

# 1. Öppna Maltego
maltego

# 2. New Graph

# 3. Drag "Company" entity till grafen

# 4. Dubbelklicka → Name: "Example Corporation" (eller test company)

# 5. Högerklicka → Run Transform → "To Website [using Search Engine]"

# 6. På domain som hittades → Run Transform → "All Transforms"

# 7. Utforska grafen:
# - Vilka relationer hittas?
# - Emails?
# - Personer?
# - Subdomains?

# 8. Export: File → Export Graph → PNG
```

### Övning 3: Recon-ng - Automated reconnaissance

```bash
# 🎯 Mål: Automated domain reconnaissance

# 1. Starta recon-ng
recon-ng

# 2. Skapa workspace
workspaces create test_recon

# 3. Installera modules
marketplace install recon/domains-hosts/google_site_web
marketplace install recon/hosts-hosts/resolve

# 4. Ladda subdomain module
modules load recon/domains-hosts/google_site_web

# 5. Sätt target
options set SOURCE example.com

# 6. Kör
run

# 7. Se resultat
db query SELECT * FROM hosts

# 8. Resolve hosts till IPs
modules load recon/hosts-hosts/resolve
run

# 9. Se IPs
db query SELECT ip_address, host FROM hosts

# 10. Export
db export /tmp/recon_results.csv

# 11. Analysera CSV
cat /tmp/recon_results.csv
```

### Övning 4: Shodan - Internet-wide search

```bash
# 🎯 Mål: Förstå vad som är exponerat på internet

# 🔴 VARNING: Använd ENDAST för defensiv säkerhet eller lärande!

# 1. Gå till https://shodan.io
# 2. Registrera gratis account

# 3. Basic searches (i web interface):

# a) Apache servers i Sverige
apache country:SE

# b) SSH servers
port:22

# c) Webcams (educational only!)
"webcamXP"

# d) Industrial systems (VARNING - titta bara, rör INTE!)
"SCADA"

# 4. Analysera ett resultat:
# - Vilken port?
# - Vilken service?
# - Version?
# - Location?
# - Organization?

# 5. CLI (om du har API key):
shodan search "apache country:SE"

# 6. Host info
shodan host 8.8.8.8

# 🔴 VIKTIGT: Använd ENDAST för att:
# - Förstå vad som exponeras (learning)
# - Checka DIN egen infrastructure
# - Aldrig för obehörig åtkomst!
```

### Övning 5: OSINT på dig själv

```bash
# 🎯 Mål: Se vad som finns om DIG på internet (self-assessment)

# 1. Google yourself
# Sök: "ditt namn" "din stad"

# 2. theHarvester på din email-domain
theHarvester -d yourdomain.com -b google

# 3. Shodan på ditt hem-IP (om du har statiskt)
# shodan.io → Sök din IP

# 4. Social media check:
# - LinkedIn
# - Twitter
# - Facebook
# - Instagram

# 5. Have I Been Pwned?
# https://haveibeenpwned.com/
# Kolla om din email är i data breaches

# 🎓 LÄRDOM:
# - Vad hittar du om dig själv?
# - Vad skulle en attacker kunna hitta?
# - Hur kan du minska din digitala footprint?
```

---

## 🧪 Självtest - Nivå 3B

### Kunskapsfrågor

1. **Vad är OSINT?**
   - A) Open Source Intelligence (offentlig information)
   - B) Operating System Intelligence
   - C) Online Security Intelligence
   - D) Offensive Security Intelligence Tools

2. **Är OSINT generellt lagligt?**
   - A) Nej, alltid olagligt
   - B) Ja, eftersom det är offentlig information (men etik är viktigt!)
   - C) Bara om du har tillstånd
   - D) Bara för law enforcement

3. **Vad gör theHarvester?**
   - A) Port scanning
   - B) Email och subdomain harvesting från offentliga källor
   - C) Password cracking
   - D) Exploit development

4. **Vad är Maltego bäst för?**
   - A) Port scanning
   - B) Data mining och visualisering av relationer
   - C) Password attacks
   - D) Web hacking

5. **Vad är Recon-ng liknande?**
   - A) Nmap
   - B) Metasploit (men för reconnaissance)
   - C) Wireshark
   - D) Burp Suite

6. **Vad indexerar Shodan?**
   - A) Websites som Google
   - B) Internet-connected devices (servers, IoT, etc.)
   - C) Emails
   - D) Social media

7. **Är det lagligt att använda Shodan?**
   - A) Nej
   - B) Ja (söka i deras databas är OK, men obehörig åtkomst är ej OK)
   - C) Bara för government
   - D) Bara med VPN

8. **Vilket verktyg använder "transforms"?**
   - A) Nmap
   - B) theHarvester
   - C) Maltego
   - D) Shodan

9. **Vad kan du hitta med theHarvester?**
   - A) Passwords
   - B) Emails, subdomains, employee names
   - C) Exploits
   - D) Encrypted data

10. **Vad är risken med OSINT?**
    - A) Det är alltid olagligt
    - B) Kan användas för stalking/social engineering om det missbrukas
    - C) Inga risker
    - D) Det fungerar inte

### Praktiska uppgifter

- [ ] **1. theHarvester email harvest på test domain**
  ```bash
  theHarvester -d example.com -b google
  ```

- [ ] **2. Maltego basic investigation**
  ```bash
  # Skapa graf med Domain entity, kör transforms
  ```

- [ ] **3. Recon-ng subdomain discovery**
  ```bash
  # Workspace → Module → Run
  ```

- [ ] **4. Shodan basic search (web)**
  ```bash
  # Sök: apache country:SE
  ```

- [ ] **5. Kombinera verktyg**
  ```bash
  # theHarvester → hitta subdomains
  # Nmap → scanna subdomains
  # Shodan → kolla vad som är publikt exponerat
  ```

### Svar

<details>
<summary>Klicka för svar</summary>

**Kunskapsfrågor:**
1. **A** - Open Source Intelligence (offentlig information)
2. **B** - Ja, eftersom det är offentlig information (men etik är viktigt!)
3. **B** - Email och subdomain harvesting från offentliga källor
4. **B** - Data mining och visualisering av relationer
5. **B** - Metasploit (men för reconnaissance)
6. **B** - Internet-connected devices (servers, IoT, etc.)
7. **B** - Ja (söka är OK, obehörig åtkomst är ej OK)
8. **C** - Maltego
9. **B** - Emails, subdomains, employee names
10. **B** - Kan användas för stalking/social engineering om det missbrukas

**Scoring:**
- 9-10 rätt: 🏆 Excellent OSINT-förståelse!
- 7-8 rätt: ✅ Bra kunskaper
- 5-6 rätt: 📚 OK - repetera vissa verktyg
- <5 rätt: 🔄 Läs igenom nivån igen

</details>

---

## ✅ Sammanfattning - Nivå 3 (A + B)

### Du har nu lärt dig:

**Active Reconnaissance (Nivå 3A):**
- ✅ Nmap - Network scanning (host discovery, port scanning, service detection)
- ✅ Netdiscover - Network discovery
- ✅ Wireshark - Packet analysis

**Passive Reconnaissance (Nivå 3B):**
- ✅ OSINT fundamentals
- ✅ theHarvester - Email harvesting
- ✅ Maltego - Data mining & visualization
- ✅ Recon-ng - Modular recon framework
- ✅ Shodan - Internet-wide device search

### Reconnaissance Workflow

```
RECONNAISSANCE PROCESS:

1. PASSIVE OSINT
   ├─ Google dorking
   ├─ theHarvester (emails, subdomains)
   ├─ Maltego (relationer)
   ├─ Shodan (public exposure)
   └─ Social media intel

2. ACTIVE RECON (med tillstånd!)
   ├─ Nmap ping sweep (hitta hosts)
   ├─ Nmap port scan (hitta services)
   ├─ Nmap version detection
   ├─ NSE vulnerability scan
   └─ Wireshark (network analysis)

3. ANALYSIS
   ├─ Sammanställ data
   ├─ Identifiera attack surface
   ├─ Hitta potentiella sårbarheter
   └─ Planera nästa steg

4. NEXT PHASE
   └─ Nivå 4: Vulnerability Assessment & Exploitation
```

---

## ✅ Checklista - Redo för Nivå 4?

- [ ] Förstår skillnaden mellan passive och active reconnaissance
- [ ] Kan använda Nmap för comprehensive scanning
- [ ] Kan använda theHarvester för email harvesting
- [ ] Har testat Maltego för data visualization
- [ ] Kan använda Recon-ng för automated recon
- [ ] Förstår vad Shodan är och hur det används
- [ ] Känner till etiska och juridiska gränser för reconnaissance
- [ ] Har genomfört alla praktiska övningar
- [ ] Förstår importance av OSINT i penetrationstestning

**🎯 Nästa steg:**

👉 **[Nivå 4A - Vulnerability Assessment](./niva-4a-vulnerability.md)**

Nu ska vi lära oss hitta sårbarheter med OpenVAS, Nikto, WPScan och SQLmap!

---

**[⬅️ Föregående: Nivå 3A](./niva-3a-reconnaissance-pt1.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 4A](./niva-4a-vulnerability.md)**

---

**📌 Kom ihåg:**

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  "The more you know about your target,                  │
│   the more effective your assessment will be"           │
│                                                          │
│  "Ju mer du vet om målet,                               │
│   desto effektivare blir din bedömning"                 │
│                                                          │
│  Reconnaissance är grunden - skippa aldrig denna fas!    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```
