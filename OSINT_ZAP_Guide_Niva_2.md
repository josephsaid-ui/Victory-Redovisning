# 🏠 Nivå 2: Grundläggande OSINT och ZAP-verktyg

> **"Give me six hours to chop down a tree and I will spend the first four sharpening the axe." - Abraham Lincoln**
>
> 📚 Läsningstid: 30-40 min | 🎯 Övningar: 4 | 💡 Svårighetsgrad: Nybörjare/Medel

---

## 🗺️ Navigation
**[⬅️ Tillbaka till Nivå 1](OSINT_ZAP_Guide_Niva_1.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 3](OSINT_ZAP_Guide_Niva_3.md)**

---

## 🎯 Vad du lär dig i denna nivå

Efter att ha läst Nivå 2 kommer du att:
- ✅ Bemästra Google Dorking för avancerade sökningar
- ✅ Använda WHOIS för domänundersökningar
- ✅ Utforska Wayback Machine för historisk data
- ✅ Extrahera metadata från filer och bilder
- ✅ Installera och konfigurera OWASP ZAP
- ✅ Genomföra din första automatiserade säkerhetsskanning
- ✅ Förstå och tolka ZAP-alerts
- ✅ Sätta upp testmiljöer (DVWA, WebGoat)

---

## 🔍 Del 1: Avancerad Google Dorking

Du lärde dig grunderna i Nivå 1. Nu går vi MYCKET djupare!

### 🎯 Vad är Google Dorking?

**Google Dorking** (även kallat Google Hacking) är konsten att använda avancerade sökoperatorer för att hitta information som inte är lätt att hitta med vanliga sökningar.

Upptäckt av **Johnny Long** som skapade "Google Hacking Database" (GHDB).

### 📚 Fullständig Lista: Google Search Operators

```
GRUNDLÄGGANDE OPERATORER
═══════════════════════════════════════════════════════════════════
Operator          Beskrivning                    Exempel
───────────────────────────────────────────────────────────────────
"exakt fras"      Söker exakt matchning         "information security"

site:             Begränsa till specifik site   site:github.com OSINT
                  Funkar med TLD också          site:.gov classified

filetype:         Specifik filtyp               filetype:pdf pentest
ext:              Samma som filetype:           ext:pdf pentest

-                 Uteslut ord/site              security -camera
                                                site:reddit.com -site:old.reddit.com

OR                Antingen eller                hacking OR pentesting

AND               Båda orden måste finnas       security AND testing
                  (implicit om inget anges)

*                 Wildcard (ersätter ord)       "best * for pentesting"

..                Nummerintervall               laptop 5000..15000 kr

( )               Gruppera                      (hacking OR pentesting) tutorial

AVANCERADE OPERATORER
═══════════════════════════════════════════════════════════════════
intitle:          Söker i sidtitel              intitle:"index of" password

allintitle:       Alla ord i titel              allintitle:login admin panel

inurl:            Söker i URL                   inurl:admin login

allinurl:         Alla ord i URL                allinurl:admin login php

intext:           Söker i sidtext               intext:"powered by wordpress"

allintext:        Alla ord i text               allintext:username password email

inanchor:         Söker i länktext              inanchor:"click here"

cache:            Googles cachad version        cache:example.com

related:          Liknande webbplatser          related:github.com

info:             Info om URL                   info:google.com

define:           Definition                    define:osint

location:         Geografisk sökning            location:stockholm "cyber security"

source:           Nyhetskälla                   cybersecurity source:bbc

KOMBINATIONER (Kraftfulla!)
═══════════════════════════════════════════════════════════════════
site:linkedin.com intitle:"CISO" location:stockholm
filetype:pdf site:gov.se "sekretess"
inurl:admin intitle:login site:.se
site:pastebin.com "password" filetype:txt
"index of" "parent directory" "password.txt"
```

### 🎯 Praktiska Google Dork Exempel

#### 1. Hitta Exponerade Filer

```bash
# Hitta PDF-dokument med lösenord
filetype:pdf "password" site:edu

# Excel-filer med känslig data
filetype:xlsx "confidential"

# Konfigurationsfiler
filetype:env "DB_PASSWORD"
filetype:config inurl:web.config

# Backup-filer (ofta glömda!)
filetype:bak inurl:backup
filetype:old inurl:backup
ext:sql inurl:backup
```

#### 2. Hitta Sårbara Webbplatser

```bash
# Webbplatser med directory listing aktiverat
intitle:"index of" "parent directory"

# Login-sidor
intitle:"login" inurl:admin
intitle:"admin panel" inurl:login

# phpMyAdmin (databasadmin)
intitle:"phpMyAdmin" "Welcome to phpMyAdmin"

# Öppna kameror
intitle:"webcamXP 5" inurl:8080

# Sårbara servrar
intext:"Apache/2.4" intitle:"Index of /"
```

#### 3. OSINT för Företag

```bash
# Hitta anställda på LinkedIn
site:linkedin.com "CISO" "Stockholm" "Ericsson"

# Emails på specifik domän
site:example.com filetype:pdf intext:"@example.com"

# Presentationer och dokument
site:slideshare.net "company name"
site:scribd.com "company name"

# Job postings (avslöjar teknisk stack!)
site:linkedin.com "company" "job opening" "python"
```

#### 4. Hitta Data Leaks

```bash
# Pastebin leaks
site:pastebin.com "company.com" password

# GitHub leaks (använd försiktigt!)
site:github.com "company.com" password
site:github.com "api_key" "sk-" (Stripe keys)
site:github.com "AWS_ACCESS_KEY_ID"

# Public S3 buckets
site:s3.amazonaws.com "company"
```

⚠️ **VARNING:** Använd ALDRIG dessa dorks för att exploatera! Endast för OSINT och med tillstånd.

### 🛡️ Etiska Riktlinjer för Google Dorking

```
✅ OKEJ ATT GÖRA:
─────────────────────────────────────────────────────────
• Söka efter PUBLIKT tillgänglig information
• Testa EGNA domäner för exponerade filer
• Lära sig vilka misstag man ska undvika
• Rapportera om du hittar känslig data exponerad

❌ INTE OKEJ ATT GÖRA:
─────────────────────────────────────────────────────────
• Ladda ner känsliga dokument för egen vinning
• Sprida funna lösenord eller credentials
• Exploatera sårbarheter du hittar
• Massscanna webbplatser (tung last på servrar)
```

---

## 🌐 Del 2: WHOIS och Domänundersökning

### 🎯 Vad är WHOIS?

WHOIS är en databas som innehåller information om vem som äger en domän.

**Vad kan du hitta?**
- 👤 Registrant (ägare)
- 📧 Kontakt-email
- 📞 Telefonnummer
- 🏢 Organisation
- 📅 Registreringsdatum
- 📅 Utgångsdatum
- 🌐 DNS-servrar (nameservers)
- 🔢 IP-adress

### 🔍 Utföra WHOIS-lookup

#### Metod 1: Online Tools

```
WHOIS LOOKUP WEBBPLATSER:
───────────────────────────────────────────────
• https://who.is/
• https://whois.domaintools.com/
• https://www.whois.com/
• https://lookup.icann.org/
```

#### Metod 2: Kommandorad (Linux/Mac)

```bash
# Grundläggande WHOIS
whois google.com

# WHOIS för IP-adress
whois 8.8.8.8

# Spara resultat till fil
whois example.com > whois_example.txt
```

#### Metod 3: Windows PowerShell

```powershell
# Installera först
Install-Module -Name DomainTools

# Kör WHOIS
nslookup example.com
```

### 📊 Tolka WHOIS-data

**Exempel WHOIS-resultat:**

```
═══════════════════════════════════════════════════════════════
Domain Name: EXAMPLE.COM
Registry Domain ID: 2336799_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.iana.org
Registrar URL: http://res-dom.iana.org
Updated Date: 2023-08-14T07:01:31Z
Creation Date: 1995-08-14T04:00:00Z  ← Hur gammal är domänen?
Registrar Registration Expiration Date: 2024-08-13T04:00:00Z
Registrar: RESERVED-Internet Assigned Numbers Authority

Registrant Organization: Internet Assigned Numbers Authority
Registrant State/Province: CA
Registrant Country: US
Registrant Email: noreply@iana.org  ← Kontakt

Name Server: A.IANA-SERVERS.NET  ← DNS-servrar
Name Server: B.IANA-SERVERS.NET

DNSSEC: signedDelegation  ← Säkerhetsfunktion
═══════════════════════════════════════════════════════════════
```

### 🔐 Privacy Protection (WHOIS Protection)

Många domänägare använder **WHOIS privacy** för att dölja sin identitet:

```
UTAN Privacy Protection:        MED Privacy Protection:
─────────────────────────────────────────────────────────
Name: John Doe                  Name: REDACTED FOR PRIVACY
Email: john@email.com           Email: proxy@whoisguard.com
Phone: +46 70 123 4567          Phone: REDACTED FOR PRIVACY
Address: Storgatan 1            Address: REDACTED FOR PRIVACY
```

**Tips:** Även med privacy protection kan du hitta:
- Registrar (vilket företag sålde domänen)
- Registreringsdatum
- DNS-servrar (kan avslöja hosting)

### 🎯 Reverse WHOIS

Hitta ALLA domäner som ägs av samma person/organisation:

**Tools:**
- https://viewdns.info/reversewhois/
- https://domainbigdata.com/
- https://whoxy.com/ (API tillgängligt)

**Användning:**
```
Sök efter: john.doe@example.com

Resultat:
─────────────────────────────
example.com
example.net
johns-site.com
secret-project.io
```

Detta kan avslöja "dolda" projekt eller företag!

---

## 🕰️ Del 3: Wayback Machine - Historisk Data

### 🎯 Vad är Wayback Machine?

**Internet Archive's Wayback Machine** (https://web.archive.org/) är en tjänst som sparar "snapshots" av webbplatser över tid.

**Grundat:** 1996 (arkiverar sedan dess!)
**Antal sidor:** 800+ miljarder webbsidor

### 🔍 Varför är det användbart för OSINT?

```
WAYBACK MACHINE ANVÄNDNINGSFALL:
═══════════════════════════════════════════════════════════════

1. HITTA RADERAD INFORMATION
   Företaget raderade pinsam info från sin site?
   → Kolla Wayback Machine!

2. SE HISTORISK UTVECKLING
   Hur såg webbplatsen ut för 10 år sedan?
   → Spåra företagets historia

3. HITTA GAMLA KONTAKTER
   Gamla email-adresser eller telefonnummer
   → Kan fortfarande vara giltiga!

4. UPPTÄCK FÖRÄNDRINGAR
   Vad ändrades mellan 2022 och 2023?
   → Kan avslöja strategibyten

5. ÅTERSTÄLL FÖRLORAD DATA
   Din egen gamla blogg raderades?
   → Wayback Machine kan ha sparat den!
═══════════════════════════════════════════════════════════════
```

### 🎯 Använda Wayback Machine

**Steg 1:** Gå till https://web.archive.org/

**Steg 2:** Ange URL (t.ex. `example.com`)

**Steg 3:** Se tidslinje:

```
WAYBACK MACHINE TIDSLINJE
════════════════════════════════════════════════════════

1995  1998  2001  2004  2007  2010  2013  2016  2019  2022
──┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──
  │    │    │    │    │    │    │    │    │    │    │
  5   12   45   89  123  234  345  456  567  678  789  ← Snapshots

Klicka på ett datum för att se hur sidan såg ut!
```

**Steg 4:** Jämför versioner!

```bash
# Se specific snapshot
https://web.archive.org/web/20200101000000/example.com
                           └─ År-Mån-Dag-Tid

# Hitta första snapshot
https://web.archive.org/web/1996*/example.com
```

### 🛠️ Wayback Machine Tips & Tricks

#### 1. Spara Sida för Framtiden

Vill du säkerställa att en sida arkiveras?

```
Gå till: https://web.archive.org/save/
Ange URL: https://example.com
→ Arkiveras direkt!
```

#### 2. CDX API (Avancerat)

Hämta metadata programmatiskt:

```bash
# Lista alla snapshots för en URL
curl "http://web.archive.org/cdx/search/cdx?url=example.com&output=json"

# Filter på årtal
curl "http://web.archive.org/cdx/search/cdx?url=example.com&from=2020&to=2023"
```

#### 3. Kolla Subdomains

```bash
# Alla arkiverade subdomains
https://web.archive.org/web/*/subdomain.example.com
```

---

## 📸 Del 4: Metadata och EXIF-data

### 🎯 Vad är Metadata?

**Metadata** = "Data om data"

När du tar ett foto med din telefon sparas MYCKET mer än bara bilden:

```
EXIF-DATA I ETT FOTO
═══════════════════════════════════════════════════════════════
📅 Datum & Tid: 2024-11-17 14:32:15
📷 Kamera: iPhone 15 Pro
🔧 Inställningar: F/1.8, ISO 100, 1/120s
📍 GPS-koordinater: 59.3293° N, 18.0686° E (STOCKHOLM!)
👤 Författare: John Doe
💻 Mjukvara: Adobe Photoshop CC 2024
🏷️ Taggar: vacation, sweden, summer
═══════════════════════════════════════════════════════════════
```

**RISKER:**
- 📍 GPS kan avslöja var du bor/jobbar
- 📅 Timestamps kan avslöja när du är hemma/borta
- 📷 Kameramodell kan kopplas till dig
- 👤 Författarnamn kan avslöja identitet

### 🔍 Extrahera EXIF-data

#### Metod 1: Online Tools

```
EXIF VIEWER WEBBPLATSER:
───────────────────────────────────────────────
• https://exifdata.com/
• https://www.metadata2go.com/
• https://jimpl.com/
• http://exif.regex.info/exif.cgi
```

#### Metod 2: ExifTool (Kommandorad)

**Installation:**

```bash
# Linux (Debian/Ubuntu)
sudo apt install libimage-exiftool-perl

# macOS
brew install exiftool

# Windows
# Ladda ner från: https://exiftool.org/
```

**Användning:**

```bash
# Visa all EXIF-data
exiftool photo.jpg

# Specifik information
exiftool -GPSPosition photo.jpg
exiftool -Make -Model photo.jpg

# Batch-process (flera filer)
exiftool *.jpg

# Spara till CSV
exiftool -csv *.jpg > metadata.csv

# TA BORT all metadata (viktigt för privacy!)
exiftool -all= photo.jpg
# Skapar photo.jpg (utan metadata) och photo.jpg_original
```

**Exempel Output:**

```
ExifTool Version Number         : 12.40
File Name                       : IMG_1234.jpg
Directory                       : /Users/john/Photos
File Size                       : 3.2 MB
File Modification Date/Time     : 2024:11:17 14:32:15+01:00
File Access Date/Time           : 2024:11:17 15:00:00+01:00
File Permissions                : rw-r--r--
File Type                       : JPEG
MIME Type                       : image/jpeg
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Apple
Camera Model Name               : iPhone 15 Pro
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : 17.0.3
Modify Date                     : 2024:11:17 14:32:15
Y Cb Cr Positioning             : Centered
Exposure Time                   : 1/120
F Number                        : 1.8
Exposure Program                : Program AE
ISO                             : 100
Exif Version                    : 0232
Date/Time Original              : 2024:11:17 14:32:15
Create Date                     : 2024:11:17 14:32:15
Shutter Speed Value             : 1/120
Aperture Value                  : 1.8
Brightness Value                : 8.5
Metering Mode                   : Multi-segment
Flash                           : Off, Did not fire
Focal Length                    : 6.9 mm
Color Space                     : sRGB
Exif Image Width                : 4032
Exif Image Height               : 3024
Sensing Method                  : One-chip color area
Scene Type                      : Directly photographed
GPS Latitude Ref                : North
GPS Longitude Ref               : East
GPS Altitude Ref                : Above Sea Level
GPS Time Stamp                  : 13:32:15
GPS Speed Ref                   : km/h
GPS Speed                       : 0
GPS Img Direction Ref           : True North
GPS Img Direction               : 245.5
GPS Dest Bearing Ref            : True North
GPS Dest Bearing                : 245.5
GPS Date Stamp                  : 2024:11:17
GPS Horizontal Positioning Error: 5 m
GPS Latitude                    : 59 deg 19' 45.48" N  ← PLATS!
GPS Longitude                   : 18 deg 4' 6.96" E    ← PLATS!
GPS Altitude                    : 12.5 m
GPS Position                    : 59 deg 19' 45.48" N, 18 deg 4' 6.96" E
```

### 📍 Konvertera GPS-koordinater

```python
# Python-script för att konvertera GPS till decimal
def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes/60 + seconds/3600
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# Exempel från EXIF ovan:
lat = dms_to_decimal(59, 19, 45.48, 'N')
lon = dms_to_decimal(18, 4, 6.96, 'E')

print(f"Latitude: {lat}")   # 59.329300
print(f"Longitude: {lon}")  # 18.068600

# Google Maps URL:
print(f"https://www.google.com/maps?q={lat},{lon}")
```

### 📄 Metadata i Andra Filtyper

**PDF-dokument:**

```bash
# Visa PDF-metadata
exiftool document.pdf

# Vanliga metadata-fält:
# - Author (Författare)
# - Creator (Program som skapade PDF:en)
# - Producer (PDF-generator)
# - CreationDate
# - ModDate
# - Title
# - Keywords
```

**Office-dokument (Word, Excel, PowerPoint):**

```bash
# DOCX/XLSX/PPTX metadata
exiftool document.docx

# Kan avslöja:
# - Författare och företag
# - Tidigare författare (revision history)
# - Template-info
# - Total editing time
# - Interna sökvägar (C:\Users\john\Documents\...)
```

### 🛡️ Skydda Din Privacy - Ta Bort Metadata

**Innan du delar filer online:**

```bash
# Metod 1: ExifTool (rekommenderat)
exiftool -all= file.jpg

# Metod 2: ImageMagick
convert original.jpg -strip cleaned.jpg

# Metod 3: mat2 (Metadata Anonymisation Toolkit)
sudo apt install mat2
mat2 file.jpg
```

**För PDF:**

```bash
# PDF metadata-removal
exiftool -all= document.pdf

# Eller använd online: https://www.metadata2go.com/
```

---

## 🛡️ Del 5: OWASP ZAP - Installation och Setup

Nu börjar vi med säkerhetstestning! 🚀

### 🎯 Vad är OWASP ZAP igen?

**OWASP ZAP** (Zed Attack Proxy) är:
- 🆓 Gratis och open source
- 🌍 Världens mest populära security testing tool
- 🕷️ Spider + Scanner + Proxy i ett
- 🐛 Hittar sårbarheter som XSS, SQLi, etc.
- 🎓 Perfekt för lärande

**Jämfört med Burp Suite:**
```
ZAP                          Burp Suite
──────────────────────────────────────────────
✅ 100% gratis                ⚠️ Freemium (limited free)
✅ Open source               ❌ Proprietary
✅ Bra för automation        ✅ Excellent för manual testing
✅ Lättare att lära          ⚠️ Brantare learning curve
⚠️ Mindre features i gratis  ✅ Mer features i Pro ($449/år)
```

**Slutsats:** ZAP är PERFEKT för att börja! 🎉

### 💾 Installation

#### Windows

1. Gå till: https://www.zaproxy.org/download/
2. Ladda ner "Windows (64) Installer"
3. Kör `.exe`-filen
4. Följ installationsguiden
5. Klar! 🎉

#### macOS

```bash
# Metod 1: Homebrew (rekommenderat)
brew install --cask owasp-zap

# Metod 2: Manuell installation
# Ladda ner .dmg från https://www.zaproxy.org/download/
# Dra ZAP.app till Applications
```

#### Linux

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install zaproxy

# Arch Linux
yay -S zaproxy

# Kali Linux (förinstallerad!)
zaproxy

# Eller universal: Flatpak
flatpak install flathub org.zaproxy.ZAP
```

#### Docker (Avancerat - för automation)

```bash
# Kör ZAP i Docker
docker run -u zap -p 8080:8080 -p 8090:8090 \
  -i ghcr.io/zaproxy/zaproxy:stable zap-webswing.sh

# Öppna webbläsare: http://localhost:8080/zap
```

### 🎨 Första Start och Konfiguration

**Steg 1: Starta ZAP**

```
Första gången du startar ZAP ser du:

┌──────────────────────────────────────────────────┐
│  Welcome to OWASP ZAP!                           │
│                                                  │
│  Do you want to persist the ZAP session?         │
│                                                  │
│  ○ Yes, I want to persist this session          │
│      └─→ Sparar allt mellan sessioner           │
│                                                  │
│  ● No, I do not want to persist this session    │
│      └─→ Rekommenderat för början!              │
│                                                  │
│  [ OK ]                                          │
└──────────────────────────────────────────────────┘
```

**Välj:** "No, I do not want to persist" för nu.

**Steg 2: ZAP Interface**

```
ZAP HUVUDFÖNSTER
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [File] [Edit] [View] [Analyse] [Report] [Tools] [Help]     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Quick Start Tab  │  Manual Explore  │  Automated Scan     │
│                                                             │
├───────────────┬─────────────────────────────────────────────┤
│               │                                             │
│   Sites       │         Workspace                           │
│   Tree        │         (Requests/Responses visas här)      │
│               │                                             │
│  ▼ Sites      │                                             │
│    └─ http:// │                                             │
│      example  │                                             │
│        │      │                                             │
│        ├─GET  │                                             │
│        └─POST │                                             │
│               │                                             │
├───────────────┴─────────────────────────────────────────────┤
│  [History] [Search] [Alerts]                                │
│                                                             │
│  Alerts:  🔴 High: 0  🟠 Medium: 0  🟡 Low: 0  ℹ️ Info: 0  │
└─────────────────────────────────────────────────────────────┘
```

**Viktiga paneler:**
- **Sites:** Träd med alla hittade URLs
- **History:** All HTTP-trafik
- **Alerts:** Funna sårbarheter
- **Request/Response:** Se exakt vad som skickas

### 🎯 Konfigurera ZAP som Proxy

För att fånga trafik från din webbläsare måste du konfigurera ZAP som proxy.

**ZAP lyssnar på:** `localhost:8080` (default)

#### Konfigurera Firefox (Rekommenderat!)

**Steg 1: Installera FoxyProxy**
- Gå till Firefox Add-ons
- Sök efter "FoxyProxy Standard"
- Klicka "Add to Firefox"

**Steg 2: Konfigurera FoxyProxy**

```
FoxyProxy Settings:
─────────────────────────────────────────
Title: OWASP ZAP
Proxy Type: HTTP
Proxy IP: 127.0.0.1 (eller localhost)
Port: 8080
```

**Steg 3: Aktivera/Avaktivera**
- Klicka FoxyProxy-ikonen i toolbar
- Välj "OWASP ZAP" för att aktivera
- Välj "Turn Off" när du inte testar

#### Konfigurera Chrome

**Metod 1: Browser Extension**
- Installera "Proxy SwitchyOmega"
- Konfigurera: HTTP Proxy = localhost:8080

**Metod 2: System Proxy (Mac/Windows)**
- Ändra i system settings
- **OBS:** Påverkar ALL trafik!

### 🔐 Installera ZAP Root CA Certificate

För att se HTTPS-trafik (krypterad) måste du lita på ZAPs certifikat.

**Steg 1: Generera Cert**
1. I ZAP: `Tools` → `Options` → `Dynamic SSL Certificates`
2. Klicka `Save`
3. Spara `owasp_zap_root_ca.cer`

**Steg 2: Importera i Firefox**
1. Firefox `Settings` → `Privacy & Security`
2. Scrolla ner till `Certificates` → `View Certificates`
3. `Authorities` tab → `Import`
4. Välj `owasp_zap_root_ca.cer`
5. Kryssa i **"Trust this CA to identify websites"**
6. Klicka `OK`

**Steg 3: Testa**
1. Besök https://example.com med proxy aktiverad
2. Titta i ZAP History - du borde se requesten!

⚠️ **VIKTIGT:** Ta bort ZAP-certifikatet när du inte använder ZAP! Annot kan andra med ZAP-access se din krypterade trafik.

---

## 🎯 Övningar - Nivå 2

### Övning 2.1: Google Dorking - Hitta Publika Dokument 🔎

**Mål:** Öva på avancerade sökoperatorer för att hitta specifik information.

**Uppgifter:**

**1. Hitta PDF-dokument om cybersäkerhet från svenska myndigheter:**
```
Din sökning: _________________________________
Antal resultat: _____
3 intressanta dokument du hittade:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________
```

<details>
<summary>💡 Hint</summary>

```
site:.se filetype:pdf cybersäkerhet
site:gov.se filetype:pdf säkerhet
site:msb.se filetype:pdf it-säkerhet
```
</details>

**2. Hitta exponerade directory listings:**
```
Din sökning: _________________________________
Hittade du några? (Ja/Nej): _____
Om ja, vilken typ av filer? ___________________
```

<details>
<summary>💡 Hint</summary>

```
intitle:"index of" "parent directory"
intitle:"index of" /"backup"
```
</details>

⚠️ **PÅMINNELSE:** LADDA INTE NER känsliga filer! Detta är endast för lärande.

**3. Sök efter LinkedIn-profiler för cybersäkerhetsexperter i Stockholm:**
```
Din sökning: _________________________________
Antal profiler hittade: _____
Vanligaste job titles: ________________________
```

<details>
<summary>💡 Hint</summary>

```
site:linkedin.com "information security" OR "cybersecurity" Stockholm
site:linkedin.com intitle:"CISO" Stockholm
```
</details>

**4. Hitta företags tekniska stack:**
```
Välj ett företag: _____________________________
Din sökning: __________________________________

Resultat - teknologier de använder:
- ____________________________________________
- ____________________________________________
- ____________________________________________
```

<details>
<summary>💡 Hint</summary>

```
site:linkedin.com "företagsnamn" "job opening" python
site:stackoverflow.com "företagsnamn"
site:github.com "företagsnamn"
```
</details>

**Facit:**
Du borde ha hittat:
- Hundratals PDF:er från svenska myndigheter (MSB, SÄPO, etc.)
- Några webbplatser med directory listing (vanligt på äldre sites)
- Många cybersäkerhetsexperter på LinkedIn
- Tech stack genom job postings

---

### Övning 2.2: WHOIS-lookup på en Domän 🌐

**Mål:** Lära dig extrahera information från WHOIS-data.

**Uppgift 1: Grundläggande WHOIS**

Välj 3 domäner att analysera:
1. En känd tech-företag (t.ex. spotify.com)
2. En svensk myndighet (t.ex. polisen.se)
3. Din egen domän (om du har en)

**För varje domän, dokumentera:**

```
DOMÄN 1: ______________________________________

WHOIS Information:
─────────────────────────────────────────────
Registrar: ___________________________________
Registreringsdatum: __________________________
Utgångsdatum: ________________________________
Nameservers:
  - _________________________________________
  - _________________________________________

Privacy Protection: Ja / Nej

Om Nej, synlig information:
  Registrant: ________________________________
  Email: _____________________________________
  Organisation: ______________________________

DNS Records (från nslookup):
  A record (IP): _____________________________
  MX record (Email): _________________________
  TXT records: _______________________________
```

**Verktyg att använda:**
```bash
# Online
https://who.is/
https://whois.domaintools.com/

# Kommandorad (Linux/Mac)
whois spotify.com
nslookup spotify.com
dig spotify.com ANY

# Windows PowerShell
nslookup spotify.com
```

**Uppgift 2: Reverse WHOIS**

Använd ViewDNS eller DomainBigData:

```
Sök efter email/organisation från Uppgift 1:
Sökterm: _____________________________________

Antal andra domäner hittade: _________________

3 intressanta domäner:
1. __________________________________________
2. __________________________________________
3. __________________________________________

Slutsats - vad avslöjar detta om företaget?
_____________________________________________
_____________________________________________
```

**Facit:**
- Stora företag använder ofta privacy protection
- Myndigheter har ofta ÖPPEN WHOIS-data
- Reverse WHOIS kan avslöja dotterbolag eller sidoprojekt
- Nameservers avslöjar hosting (AWS, Cloudflare, etc.)

---

### Övning 2.3: Installera och Konfigurera OWASP ZAP 🛠️

**Mål:** Få ZAP installerat och fungerande med din webbläsare.

**Checklista:**

```
INSTALLATION
─────────────────────────────────────────────
[ ] ZAP nedladdat från zaproxy.org
[ ] ZAP installerat på min dator
[ ] ZAP startar utan problem
[ ] Jag valde "No persist session"

WEBBLÄSARE SETUP
─────────────────────────────────────────────
[ ] Firefox installerat (rekommenderat)
[ ] FoxyProxy extension installerat
[ ] FoxyProxy konfigurerat (localhost:8080)
[ ] FoxyProxy kan aktiveras/avaktiveras

CERTIFIKAT
─────────────────────────────────────────────
[ ] ZAP Root CA cert exporterat
[ ] Cert importerat i Firefox
[ ] "Trust för websites" aktiverat

FUNKTIONSTEST
─────────────────────────────────────────────
[ ] FoxyProxy aktiverad
[ ] Besökt http://example.com
[ ] Request syns i ZAP History
[ ] Besökt https://example.com (HTTPS!)
[ ] HTTPS request syns också i ZAP History
[ ] Response-data visbar i ZAP
```

**Test:**

1. Aktivera FoxyProxy → OWASP ZAP
2. Gå till http://example.com
3. I ZAP, titta i "History"-tab
4. Högerklicka på requesten → "Open/Resend with Request Editor"

```
Du borde se något som:

GET http://example.com/ HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0...
Accept: text/html,application/xhtml+xml...
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: keep-alive
```

**Felsökning:**

```
PROBLEM: Kan inte nå webbplatser med proxy aktiverad
LÖSNING: Kontrollera att ZAP är igång och lyssnar på 8080
         Tools → Options → Local Proxies (kontrollera port)

PROBLEM: Kan inte se HTTPS-trafik
LÖSNING: Installera ZAP Root CA cert igen
         Kontrollera att "Trust for websites" är kryssad

PROBLEM: FoxyProxy fungerar inte
LÖSNING: Kontrollera proxy settings:
         IP: 127.0.0.1 (INTE localhost ibland)
         Port: 8080
```

---

### Övning 2.4: Skanna en Test-webbplats (DVWA) 🎯

**Mål:** Genomföra din första automatiserade säkerhetsskanning med ZAP!

**Steg 1: Sätt upp test-miljö**

Vi använder **DVWA** (Damn Vulnerable Web Application) - en AVSIKTLIGT osäker webbapp för träning.

**Option A: Docker (Snabbast)**
```bash
# Kör DVWA i Docker
docker run --rm -it -p 80:80 vulnerables/web-dvwa

# Öppna webbläsare: http://localhost
# Login: admin / password
# Klicka "Create / Reset Database"
# Sätt Security Level: Low
```

**Option B: OWASP WebGoat**
```bash
# Om DVWA inte funkar, använd WebGoat:
docker run -p 8080:8080 -p 9090:9090 \
  -e TZ=Europe/Stockholm webgoat/webgoat

# Öppna: http://localhost:8080/WebGoat
```

**Option C: Online (Hackthebox/TryHackMe)**
- Skapa gratis konto på https://tryhackme.com/
- Starta "OWASP Top 10" room
- Använd deras vulnerable webapp

**Steg 2: Manual Explore med ZAP**

1. **Starta ZAP**
2. **Gå till "Quick Start" tab**
3. **Klicka "Manual Explore"**
4. **Ange URL:** `http://localhost` (eller din test-URL)
5. **Klicka "Launch Browser"**
   - ZAP öppnar en egen webbläsare med proxy förkonfigurerad!

6. **Utforska DVWA:**
   - Logga in (admin/password)
   - Klicka runt på olika sidor
   - Testa SQL Injection-page
   - Testa XSS-page
   - Testa File Upload

7. **I ZAP, se Sites-trädet fyllas:**
```
Sites
└─ http://localhost
   ├─ login.php
   ├─ index.php
   ├─ vulnerabilities
   │  ├─ sqli
   │  ├─ xss_r
   │  ├─ upload
   │  └─ ...
   └─ ...
```

**Steg 3: Automated Scan**

1. **I ZAP, högerklicka** på `http://localhost` i Sites-trädet
2. **Välj:** "Attack" → "Active Scan"
3. **Konfigurera:**
   ```
   Starting Point: http://localhost
   Recurse: ✓ (aktiverad)
   Scope: (lämna tomt för nu)

   [Start Scan]
   ```

4. **Vänta medan ZAP scannar** (kan ta 5-15 min)
   - Se progress i nedersta fönstret
   - Alerts börjar dyka upp!

**Steg 4: Analysera Resultat**

```
ALERTS TAB (Efter skanning)
═══════════════════════════════════════════════════════════

🔴 High Risk: 15
   ├─ SQL Injection
   ├─ Cross-Site Scripting (Reflected)
   ├─ Remote File Inclusion
   └─ ...

🟠 Medium Risk: 8
   ├─ Cross-Site Scripting (Stored)
   ├─ CSRF
   └─ ...

🟡 Low Risk: 12
   ├─ Cookie without HttpOnly flag
   ├─ X-Frame-Options header missing
   └─ ...

ℹ️ Informational: 5
   ├─ Information Disclosure
   └─ ...
```

**Klicka på en alert** (t.ex. SQL Injection):

```
═══════════════════════════════════════════════════════════
Alert: SQL Injection
Risk: High
Confidence: Medium
───────────────────────────────────────────────────────────
Description:
SQL injection may be possible in this parameter.

URL:
http://localhost/vulnerabilities/sqli/?id=1&Submit=Submit

Parameter: id

Attack:
id=1' OR '1'='1

Evidence:
You have an error in your SQL syntax...

Solution:
Use prepared statements with parameterized queries.

References:
https://owasp.org/www-community/attacks/SQL_Injection
CWE-89
───────────────────────────────────────────────────────────
Request:
GET /vulnerabilities/sqli/?id=1'%20OR%20'1'='1&Submit=Submit
Host: localhost
Cookie: security=low; PHPSESSID=...

Response:
HTTP/1.1 200 OK
...
You have an error in your SQL syntax...
═══════════════════════════════════════════════════════════
```

**Steg 5: Generera Rapport**

1. **Klicka:** `Report` → `Generate HTML Report`
2. **Spara:** `dvwa_scan_report.html`
3. **Öppna i webbläsare** - se professional rapport!

**Dokumentera dina fynd:**

```
MIN FÖRSTA ZAP-SKANNING
═══════════════════════════════════════════════════════════
Target: http://localhost (DVWA)
Datum: ____________________
Scantid: __________ minuter

RESULTAT:
─────────────────────────────────────────────────────────
🔴 High: _____
🟠 Medium: _____
🟡 Low: _____
ℹ️ Info: _____

TOP 3 KRITISKA SÅRBARHETER:
1. ________________________________________________
   URL: ____________________________________________
   Parameter: ______________________________________

2. ________________________________________________
   URL: ____________________________________________
   Parameter: ______________________________________

3. ________________________________________________
   URL: ____________________________________________
   Parameter: ______________________________________

VAD LÄRDE JAG MIG:
__________________________________________________
__________________________________________________
__________________________________________________

NÄSTA STEG:
__________________________________________________
__________________________________________________
═══════════════════════════════════════════════════════════
```

**Facit:**
På DVWA (Security: Low) borde du hitta:
- 🔴 SQL Injection (flera ställen)
- 🔴 Reflected XSS
- 🔴 Stored XSS
- 🔴 Command Injection
- 🔴 File Inclusion
- 🟠 CSRF
- 🟡 Många cookie/header-issues

**Grattis!** Du har genomfört din första professionella säkerhetsskanning! 🎉

---

## 🎓 Sammanfattning Nivå 2

### Vad du har lärt dig:

✅ **Google Dorking** - Avancerade sökoperatorer för att hitta dold information
✅ **WHOIS** - Undersöka domäner och hitta ägare
✅ **Wayback Machine** - Hitta historisk data och raderad information
✅ **Metadata/EXIF** - Extrahera dold data från filer och bilder
✅ **OWASP ZAP** - Installation och konfiguration
✅ **Proxy Setup** - Fånga HTTP/HTTPS-trafik
✅ **Automated Scanning** - Din första säkerhetsskanning!
✅ **Vulnerability Analysis** - Förstå och tolka ZAP-alerts

### Verktyg du nu behärskar:

🔧 Google (avancerade operators)
🔧 WHOIS (who.is, kommandorad)
🔧 Wayback Machine
🔧 ExifTool
🔧 OWASP ZAP
🔧 FoxyProxy
🔧 DVWA/WebGoat (test-miljöer)

### Nästa Steg:

🎯 **Om du känner dig bekväm:**
→ Gå vidare till **[Nivå 3: Tekniska Verktyg och Metoder](OSINT_ZAP_Guide_Niva_3.md)**

Där lär du dig:
- Maltego för visuell länkanalys
- theHarvester för email-harvesting
- Shodan för IoT och server-reconnaissance
- ZAP Spider och manual fuzzing
- Hitta och exploatera XSS praktiskt

🔄 **Om du vill öva mer:**
→ Repetera övningarna
→ Skanna fler test-miljöer (WebGoat, Juice Shop)
→ Experimentera med Google Dorks
→ Analysera metadata från dina egna filer

---

## 🔐 Säkerhetspåminnelse

**Innan du går vidare, kom ihåg:**

⚠️ **Testa ENDAST:**
- Dina egna system
- Test-miljöer (DVWA, WebGoat, Juice Shop)
- Bug bounty-program (inom scope!)
- System där du har SKRIFTLIGT tillstånd

🚫 **Testa ALDRIG:**
- Andras webbplatser utan tillstånd
- Produktionssystem (även dina egna utan backup!)
- Kritisk infrastruktur
- Skolor/universitet utan explicit OK från IT-avdelning

📝 **Dokumentera:**
- All testning du gör
- Timestamps och scope
- Fynd och rapportering

---

**Redo för nästa nivå?**

👉 **[Fortsätt till Nivå 3: Tekniska Verktyg och Metoder →](OSINT_ZAP_Guide_Niva_3.md)**

---

**[⬅️ Tillbaka till Nivå 1](OSINT_ZAP_Guide_Niva_1.md)** | **[🏠 Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 3](OSINT_ZAP_Guide_Niva_3.md)**

---

**Nivå 2 Komplett! ✅**
*Du har nu grundläggande OSINT och ZAP-kunskaper! Fortsätt till Nivå 3 när du känner dig redo.*
