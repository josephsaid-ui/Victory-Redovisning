# 🔍 Nivå 3A: Reconnaissance - Network Scanning

**⏱️ Beräknad tid:** 2-3 timmar
**📚 Svårighetsgrad:** ⭐⭐⭐ Intermediate
**🎯 Förutsättningar:** Nivå 2 genomförd, lab-miljö uppsatt
**🎓 Lärdomsmål:** Scanna nätverk, hitta enheter och tjänster, analysera nätverkstrafik

---

## 📋 Innehåll

1. [Vad är Reconnaissance?](#-vad-är-reconnaissance)
2. [Nmap - Network Mapper (DJUPGÅENDE)](#-nmap---network-mapper)
3. [Netdiscover - Network Discovery](#-netdiscover---network-discovery)
4. [Wireshark - Packet Analysis](#-wireshark---packet-analysis)
5. [Praktiska lab-övningar](#-praktiska-lab-övningar)
6. [Självtest](#-självtest-nivå-3a)

---

## 🎯 Vad är Reconnaissance?

### Definition

**Reconnaissance** (även kallat "recon" eller "information gathering") är den första fasen i penetrationstestning där du samlar information om målet.

```
┌──────────────────────────────────────────────────────────┐
│  PENETRATION TESTING LIFECYCLE                           │
├──────────────────────────────────────────────────────────┤
│  1. RECONNAISSANCE ← Vi är här!                          │
│     Samla information om målsystemet                     │
│                                                          │
│  2. SCANNING & ENUMERATION                               │
│     Identifiera sårbarheter                              │
│                                                          │
│  3. GAINING ACCESS                                       │
│     Exploitera sårbarheter                               │
│                                                          │
│  4. MAINTAINING ACCESS                                   │
│     Etablera persistent access                           │
│                                                          │
│  5. COVERING TRACKS                                      │
│     Ta bort spår (etiskt: dokumentera istället)          │
│                                                          │
│  6. REPORTING                                            │
│     Rapportera fynd och rekommendationer                 │
└──────────────────────────────────────────────────────────┘
```

### Typer av Reconnaissance

| Typ | Beskrivning | Exempel | Legalitet |
|-----|-------------|---------|-----------|
| **Passive Recon** | Samla info UTAN att interagera direkt med målet | Google search, WHOIS, Shodan | ✅ Generellt OK (offentlig info) |
| **Active Recon** | Direkt interaktion med målsystemet | Port scanning, ping sweeps | ⚠️ Kräver tillstånd! |

**🔴 VIKTIGT:** Alla verktyg i denna nivå är **Active Reconnaissance** - kräver **EXPLICIT TILLSTÅND**!

### Vad vill vi ta reda på?

```
RECONNAISSANCE MÅL:

🌐 NÄTVERK:
├─ Vilka hosts är aktiva?
├─ Vilket IP-range används?
├─ Vilka subnets finns?
└─ Nätverks-topologi

🖥️ HOSTS:
├─ IP-adresser
├─ Hostnamn
├─ Operativsystem
└─ MAC-adresser

🔌 SERVICES:
├─ Vilka portar är öppna?
├─ Vilka services kör? (HTTP, SSH, FTP, etc.)
├─ Versioner av services
└─ Konfiguration

🔐 POTENTIELLA SÅRBARHETER:
├─ Outdated software
├─ Missconfig
├─ Default credentials
└─ Known vulnerabilities
```

---

## 🗺️ Nmap - Network Mapper

### 📖 Vad är Nmap?

**Nmap** (Network Mapper) är det mest populära och kraftfulla verktyget för nätverksscanning och säkerhetsanalys.

```
┌──────────────────────────────────────────────────────────┐
│  NMAP = Swiss Army Knife för network scanning           │
│                                                          │
│  Skapad av: Gordon Lyon (Fyodor) - 1997                 │
│  Använt i: The Matrix Reloaded, Mr. Robot, etc.         │
│  Status: Industry standard för pentesters                │
└──────────────────────────────────────────────────────────┘
```

**Vad kan Nmap göra?**
- 🔍 Host discovery (vilka enheter är uppe på nätverket?)
- 🔌 Port scanning (vilka portar är öppna?)
- 🖥️ OS detection (vilket operativsystem kör?)
- 🔧 Service/version detection (vilken version av Apache, etc?)
- 🔐 Vulnerability scanning (via NSE scripts)
- 📊 Network mapping (skapa nätverkskartor)

### ⚖️ Laglig användning av Nmap

**✅ OK att använda:**
```
✅ Ditt eget nätverk
✅ Ditt företags nätverk (med IT-avdelningens tillstånd)
✅ Lab-miljöer (Metasploitable, VMs)
✅ Med explicit skriftligt tillstånd
✅ Bug bounty programs (inom scope)
```

**❌ ALDRIG använda på:**
```
❌ Andras nätverk utan tillstånd
❌ ISP:ns infrastruktur
❌ Offentliga WiFi utan ägares tillstånd
❌ Arbetsplatsens nätverk (utan IT-godkännande)
❌ "Bara för att se vad som händer"
```

**🔴 VARNING:** Aggressiv scanning kan:
- Krascha känsliga system
- Tolkas som attack
- Trigga IDS/IPS (Intrusion Detection/Prevention Systems)
- Leda till åtal för dataintrång

### 🔧 Nmap installation och verifiering

```bash
# Nmap är förinstallerat i Kali
nmap --version

# Om det saknas:
sudo apt install nmap -y

# Verifiera version (2025: bör vara 7.94+)
nmap --version
```

### 📋 Grundläggande Nmap-syntax

```bash
nmap [Scan Type] [Options] {target}

# Exempel:
nmap -sV 192.168.1.10
 │    │   │
 │    │   └─ Target (IP eller hostname)
 │    └───── Option (-sV = version detection)
 └────────── Command
```

---

## 🎯 Nmap: Host Discovery

### 1. Ping Sweep - Hitta aktiva hosts

```bash
# Ping sweep på subnet (snabbt hitta live hosts)
nmap -sn 192.168.1.0/24

# -sn = "no port scan" (bara host discovery)
# /24 = subnet mask (255.255.255.0 = 254 hosts)

# Förväntat output:
# Nmap scan report for 192.168.1.1
# Host is up (0.0023s latency).
# MAC Address: AA:BB:CC:DD:EE:FF (Router manufacturer)
#
# Nmap scan report for 192.168.1.10
# Host is up (0.0045s latency).
# MAC Address: 11:22:33:44:55:66 (Computer manufacturer)
# ...
# Nmap done: 254 IP addresses (5 hosts up) scanned in 2.43 seconds
```

**Subnet-notation:**

| CIDR | Subnet Mask | Antal hosts | Exempel användning |
|------|-------------|-------------|-------------------|
| `/24` | 255.255.255.0 | 254 | Hem-nätverk, små kontor |
| `/16` | 255.255.0.0 | 65,534 | Stora företagsnätverk |
| `/8` | 255.0.0.0 | 16,777,214 | Mycket stora nätverk |

**Andra host discovery metoder:**

```bash
# ARP ping (fungerar bara på lokalt nätverk, men väldigt pålitlig)
sudo nmap -PR 192.168.1.0/24

# TCP SYN ping (specifika portar)
sudo nmap -PS22,80,443 192.168.1.0/24

# UDP ping
sudo nmap -PU 192.168.1.0/24

# Assume all hosts are up (skip host discovery)
nmap -Pn 192.168.1.10
```

---

## 🔌 Nmap: Port Scanning

### Förstå portar

**Vad är en port?**
- Portar = "dörrar" in till ett system
- Port nummer: 0-65535
- Vissa portar har standard-services

**Vanliga portar:**

| Port | Service | Beskrivning |
|------|---------|-------------|
| 20/21 | FTP | File Transfer Protocol |
| 22 | SSH | Secure Shell |
| 23 | Telnet | Unencrypted remote login (osäkert!) |
| 25 | SMTP | Email (sending) |
| 53 | DNS | Domain Name System |
| 80 | HTTP | Web traffic |
| 110 | POP3 | Email (receiving) |
| 143 | IMAP | Email (receiving) |
| 443 | HTTPS | Secure web traffic |
| 445 | SMB | Windows file sharing |
| 3306 | MySQL | Database |
| 3389 | RDP | Remote Desktop Protocol |
| 5432 | PostgreSQL | Database |
| 8080 | HTTP-alt | Alternative web port |

### 1. Basic scan (Top 1000 portar)

```bash
# Scanna vanligaste 1000 portar (default)
nmap 192.168.1.10

# Output:
# Starting Nmap 7.94 ( https://nmap.org )
# Nmap scan report for 192.168.1.10
# Host is up (0.00043s latency).
# Not shown: 997 closed ports
# PORT    STATE SERVICE
# 22/tcp  open  ssh
# 80/tcp  open  http
# 443/tcp open  https
#
# Nmap done: 1 IP address (1 host up) scanned in 0.52 seconds
```

### 2. Scanna specifika portar

```bash
# En port
nmap -p 80 192.168.1.10

# Flera portar
nmap -p 22,80,443 192.168.1.10

# Port-range
nmap -p 1-100 192.168.1.10

# Alla portar (långsamt!)
nmap -p- 192.168.1.10
# -p- = samma som -p 1-65535

# Top X portar
nmap --top-ports 20 192.168.1.10
```

### 3. Scan-typer (TCP)

```bash
# TCP SYN Scan (stealth scan - default för root)
sudo nmap -sS 192.168.1.10
# Snabbast, stealthiest
# Kräver root

# TCP Connect Scan (default för non-root)
nmap -sT 192.168.1.10
# Fullständig TCP handshake
# Lämnar mer spår i loggar

# TCP ACK Scan (firewall detection)
sudo nmap -sA 192.168.1.10

# TCP Window Scan
sudo nmap -sW 192.168.1.10

# TCP Null Scan (ingen flaggor)
sudo nmap -sN 192.168.1.10
```

**TCP Three-way Handshake:**

```
Normal TCP connection:
Client → SYN → Server
Client ← SYN-ACK ← Server
Client → ACK → Server
[Connection established]

SYN Scan (stealth):
Nmap → SYN → Target
Nmap ← SYN-ACK ← Target (port open)
Nmap → RST → Target (abort, don't complete)
[Connection NOT established = less logging]
```

### 4. UDP Scan

```bash
# UDP scan (långsamt men viktigt!)
sudo nmap -sU 192.168.1.10

# UDP + TCP
sudo nmap -sU -sT 192.168.1.10

# Top UDP ports
sudo nmap -sU --top-ports 20 192.168.1.10
```

**Varför UDP?**
- Många services använder UDP (DNS, SNMP, DHCP)
- Ofta försummade i säkerhetstester
- Kan innehålla sårbarheter

---

## 🔍 Nmap: Service & OS Detection

### 1. Service Version Detection

```bash
# Detect service versions
nmap -sV 192.168.1.10

# Output exempel:
# PORT    STATE SERVICE VERSION
# 22/tcp  open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
# 80/tcp  open  http    Apache httpd 2.4.38 ((Debian))
# 443/tcp open  ssl/http Apache httpd 2.4.38 ((Debian))

# Intensity (0-9, default 7)
nmap -sV --version-intensity 0 192.168.1.10  # Light (snabbare)
nmap -sV --version-intensity 9 192.168.1.10  # Aggressive (grundligare)
```

**Varför viktigt?**
- Versioner kan ha kända sårbarheter
- Äldre versioner = ofta osäkra
- Exempel: Apache 2.2.0 har många kända exploits

### 2. OS Detection

```bash
# Detect operating system
sudo nmap -O 192.168.1.10

# Output exempel:
# Device type: general purpose
# Running: Linux 4.X|5.X
# OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
# OS details: Linux 4.15 - 5.6
# Network Distance: 1 hop

# Aggressive OS detection
sudo nmap -O --osscan-guess 192.168.1.10
```

---

## ⚡ Nmap: Timing & Performance

### Timing Templates (-T)

```bash
# -T<0-5> kontrollerar scan-hastighet

nmap -T0 192.168.1.10  # Paranoid (extremt långsam, stealth)
nmap -T1 192.168.1.10  # Sneaky (väldigt långsam)
nmap -T2 192.168.1.10  # Polite (långsam, mindre påfrestande)
nmap -T3 192.168.1.10  # Normal (default)
nmap -T4 192.168.1.10  # Aggressive (snabb, för pentesters)
nmap -T5 192.168.1.10  # Insane (mycket snabb, kan missa saker)
```

**Rekommendationer:**

| Scenario | Timing | Varför |
|----------|--------|--------|
| **Produktion** | T2 | Mindre risk att störa services |
| **Pentest (normal)** | T3 eller T4 | Balans mellan hastighet och noggrannhet |
| **Lab-miljö** | T4 eller T5 | Snabbare resultat, ingen risk |
| **IDS evasion** | T0 eller T1 | Mycket långsamt för att undvika detektering |

### Custom Timing

```bash
# Max samtidiga probes
nmap --max-parallelism 10 192.168.1.10

# Timeout för svar
nmap --host-timeout 5m 192.168.1.10

# Scan delay (mellan probes)
nmap --scan-delay 1s 192.168.1.10
```

---

## 🔥 Nmap: Aggressive Scan

### -A (Aggressive)

```bash
# Aggressive scan = -O + -sV + -sC + traceroute
nmap -A 192.168.1.10

# Vad händer:
# -O  = OS detection
# -sV = Version detection
# -sC = Default NSE scripts
# traceroute = Network path

# Med timing:
nmap -A -T4 192.168.1.10
```

**🔴 VARNING:** Aggressive scans:
- Tar längre tid
- Genererar mer nätverkstrafik
- Mer detekterbara
- Kan störa services
- **Använd ENDAST i lab eller med tillstånd!**

---

## 🎨 Nmap Scripting Engine (NSE)

### Vad är NSE?

**NSE** = Nmap Scripting Engine - scripts för advanced scanning

**Script-kategorier:**
- auth - Authentication
- broadcast - Broadcast discovery
- brute - Brute force attacks
- default - Standard scripts (-sC)
- discovery - Service discovery
- dos - Denial of service (🔴 FARLIGT!)
- exploit - Exploitation (🔴 KRÄVER TILLSTÅND!)
- external - External resources
- fuzzer - Fuzzing
- intrusive - Intrusive scans
- malware - Malware detection
- safe - Säkra scripts
- version - Version detection
- vuln - Vulnerability detection

### Använda NSE scripts

```bash
# Default scripts (safe)
nmap -sC 192.168.1.10

# Specifik kategori
nmap --script vuln 192.168.1.10

# Specifikt script
nmap --script http-enum 192.168.1.10

# Flera scripts
nmap --script "http-*" 192.168.1.10

# Lista alla scripts
ls /usr/share/nmap/scripts/

# Sök scripts
nmap --script-help "http-*"

# Update script database
sudo nmap --script-updatedb
```

### Populära NSE scripts

```bash
# Web application enumeration
nmap --script http-enum 192.168.1.10

# SMB vulnerability scanning
nmap --script smb-vuln-* 192.168.1.10

# SSH brute force (🔴 ENDAST I LAB!)
nmap --script ssh-brute 192.168.1.10

# DNS enumeration
nmap --script dns-brute domain.com

# SSL/TLS vulnerabilities
nmap --script ssl-* 192.168.1.10

# Default credentials check
nmap --script auth 192.168.1.10
```

**Exempel: Vulnerability scanning**

```bash
# Scanna för kända sårbarheter
nmap --script vuln 192.168.1.10

# Kan hitta:
# - MS17-010 (EternalBlue)
# - Heartbleed
# - Shellshock
# - SQL injection
# - XSS
# osv.
```

---

## 💾 Nmap: Output & Reporting

### Output-format

```bash
# Normal output (till terminal och fil)
nmap 192.168.1.10 -oN scan.txt

# XML output (för parsing)
nmap 192.168.1.10 -oX scan.xml

# Grepable output (för grep/awk)
nmap 192.168.1.10 -oG scan.gnmap

# Alla format
nmap 192.168.1.10 -oA scan
# Skapar: scan.nmap, scan.xml, scan.gnmap

# Append (inte overwrite)
nmap 192.168.1.10 -oN scan.txt --append-output
```

### Verbose & Debugging

```bash
# Verbose (show more info)
nmap -v 192.168.1.10

# Extra verbose
nmap -vv 192.168.1.10

# Debug (för troubleshooting)
nmap -d 192.168.1.10

# Packet trace
nmap --packet-trace 192.168.1.10
```

---

## 📊 Nmap: Praktiska användningsfall

### Use Case 1: Quick Network Overview

```bash
# Hitta alla live hosts och deras OS
sudo nmap -sn -O 192.168.1.0/24 -oN network_overview.txt

# Analysera:
cat network_overview.txt | grep "Nmap scan report"
```

### Use Case 2: Comprehensive Host Scan

```bash
# Full scan av en specifik host
sudo nmap -A -p- -T4 -oA full_scan_host 192.168.1.10

# -A = OS + Version + Scripts + Traceroute
# -p- = Alla portar
# -T4 = Fast
# -oA = Alla output-format
```

### Use Case 3: Web Server Enumeration

```bash
# Scanna web server för info
nmap -p 80,443 --script http-enum,http-headers,http-methods 192.168.1.10
```

### Use Case 4: Vulnerability Assessment

```bash
# Scanna för vanliga sårbarheter
nmap --script vuln -sV -p- 192.168.1.10 -oN vuln_scan.txt
```

### Use Case 5: Stealth Scan

```bash
# Försök undvika detektering
sudo nmap -sS -T2 -f --data-length 25 -D RND:10 192.168.1.10

# -sS = SYN scan
# -T2 = Polite timing
# -f = Fragment packets
# --data-length = Add random data
# -D RND:10 = Decoy (10 random IPs)
```

---

## 🎓 Nmap Cheat Sheet

### Quick Reference

```bash
# HOST DISCOVERY
nmap -sn 192.168.1.0/24          # Ping sweep
sudo nmap -PR 192.168.1.0/24     # ARP scan

# PORT SCANNING
nmap 192.168.1.10                # Top 1000 ports
nmap -p- 192.168.1.10            # All ports
nmap -p 22,80,443 192.168.1.10   # Specific ports
nmap --top-ports 100 IP          # Top 100 ports

# SCAN TYPES
sudo nmap -sS IP                 # SYN scan (stealth)
nmap -sT IP                      # Connect scan
sudo nmap -sU IP                 # UDP scan

# DETECTION
nmap -sV IP                      # Version detection
sudo nmap -O IP                  # OS detection
nmap -A IP                       # Aggressive (all)

# TIMING
nmap -T0 IP                      # Paranoid
nmap -T3 IP                      # Normal
nmap -T4 IP                      # Aggressive
nmap -T5 IP                      # Insane

# NSE SCRIPTS
nmap -sC IP                      # Default scripts
nmap --script vuln IP            # Vulnerability scan
nmap --script http-enum IP       # HTTP enumeration

# OUTPUT
nmap IP -oN file.txt             # Normal output
nmap IP -oX file.xml             # XML output
nmap IP -oA basename             # All formats

# COMMON COMBOS
sudo nmap -sS -sV -O -p- -T4 -A IP -oA full_scan
nmap -Pn -p 80,443 --script http-* IP
```

---

## 🌐 Netdiscover - Network Discovery

### 📖 Vad är Netdiscover?

**Netdiscover** är ett ARP-baserat verktyg för att hitta live hosts på lokala nätverk.

**Skillnad mot Nmap:**
- Netdiscover = Passiv/Aktiv ARP scanning (mycket snabbt lokalt)
- Nmap = Mer omfattande, fler metoder

**Användningsfall:**
- Snabbt hitta alla enheter på lokalt WiFi
- Hitta rogue devices
- Nätverksöversikt

### Installation & Verifiering

```bash
# Förinstallerat i Kali
which netdiscover

# Om saknas:
sudo apt install netdiscover -y
```

### Grundläggande användning

```bash
# Auto-detect interface och range
sudo netdiscover

# Specifikt interface
sudo netdiscover -i eth0

# Specifikt range
sudo netdiscover -r 192.168.1.0/24

# Passive mode (lyssna bara, skicka inte ARP requests)
sudo netdiscover -p
```

### Output-exempel

```
Currently scanning: 192.168.1.0/24   |   Screen View: Unique Hosts

 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname
 -----------------------------------------------------------------------------
 192.168.1.1     aa:bb:cc:dd:ee:ff      1      60  Router Manufacturer
 192.168.1.10    11:22:33:44:55:66      1      60  Dell Inc.
 192.168.1.25    99:88:77:66:55:44      1      60  Apple, Inc.
```

### Användningsfall: Hitta rogue devices

```bash
# Scanna nätverk och spara output
sudo netdiscover -r 192.168.1.0/24 -P > network_devices.txt

# Analysera:
# - Känner du igen alla MAC-adresser?
# - Finns det okända enheter?
# - Stämmer antalet enheter?
```

---

## 📡 Wireshark - Packet Analysis

### 📖 Vad är Wireshark?

**Wireshark** är världens mest populära network protocol analyzer (packet sniffer).

**Vad kan Wireshark göra?**
- 📡 Fånga nätverkstrafik i realtid
- 🔍 Analysera paket djupgående
- 🕵️ Följa TCP-streams
- 🔐 Hitta okrypterad data (lösenord, etc.)
- 🐛 Troubleshoot nätverksproblem
- 🎓 Lära sig hur protokoll fungerar

**🔴 JURIDISK VARNING:**
```
✅ OK att använda:
   - På ditt eget nätverk
   - På trafik du själv genererar
   - I lab-miljöer
   - Med explicit tillstånd

❌ OLAGLIGT att använda:
   - Sniffa andras trafik utan tillstånd
   - Offentliga WiFi utan tillstånd
   - Arbetsplatsens nätverk (utan IT-OK)
   - "Bara för att lära sig"

Olaglig packet sniffing = "olovlig avlyssning" (BrB 4:9a)
Straff: Böter eller fängelse upp till 2 år
```

### Installation

```bash
# Förinstallerat i Kali
wireshark --version

# Starta Wireshark (GUI)
sudo wireshark

# 🔴 VARNING om att köra som root visas - detta är OK i Kali lab
```

### Interface basics

```
Wireshark Interface:

┌─────────────────────────────────────────────────────────┐
│  Menu Bar: File, Edit, View, Capture, etc.             │
├─────────────────────────────────────────────────────────┤
│  Toolbar: Start/Stop capture, Save, etc.               │
├─────────────────────────────────────────────────────────┤
│  Filter Bar: [Display Filter]                          │
├─────────────────────────────────────────────────────────┤
│  Packet List: Lista av alla fångade paket              │
│  #  Time   Source     Dest       Protocol  Info        │
│  1  0.000  10.0.0.1   10.0.0.2   TCP       [SYN]       │
├─────────────────────────────────────────────────────────┤
│  Packet Details: Detaljerad breakdown av valt paket     │
│  ▼ Frame                                                │
│  ▼ Ethernet II                                          │
│  ▼ Internet Protocol                                    │
│  ▼ Transmission Control Protocol                        │
├─────────────────────────────────────────────────────────┤
│  Packet Bytes: Hexadecimal och ASCII                    │
└─────────────────────────────────────────────────────────┘
```

### Starta capture

```
1. Öppna Wireshark
2. Välj interface (eth0, wlan0, etc.)
3. Klicka blå hajfena (🦈) = Start capture
4. Trafik börjar fångas
5. Röd fyrkant = Stop capture
```

### Display Filters (viktigast!)

**Display filters** filtrerar paket EFTER capture.

```bash
# Visa bara HTTP-trafik
http

# Visa bara specifik IP
ip.addr == 192.168.1.10

# Visa trafik FRÅN specifik IP
ip.src == 192.168.1.10

# Visa trafik TILL specifik IP
ip.dst == 192.168.1.10

# Specifik port
tcp.port == 80

# HTTP GET requests
http.request.method == "GET"

# HTTP POST requests
http.request.method == "POST"

# Visa bara DNS-trafik
dns

# TCP SYN packets
tcp.flags.syn == 1

# Kombinera filters (AND)
ip.addr == 192.168.1.10 && tcp.port == 80

# OR
http || dns

# NOT
!arp
```

### Vanliga filters - Cheat Sheet

| Filter | Vad det visar |
|--------|---------------|
| `http` | All HTTP traffic |
| `https` | All HTTPS traffic |
| `dns` | All DNS queries/responses |
| `tcp` | All TCP traffic |
| `udp` | All UDP traffic |
| `icmp` | Ping requests/replies |
| `arp` | ARP requests/replies |
| `ip.addr == X` | Traffic to/from IP X |
| `tcp.port == 80` | Traffic on port 80 |
| `http.request` | HTTP requests only |
| `http.response` | HTTP responses only |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | SYN packets (start of connection) |

### Follow Stream (viktigt!)

**Follow Stream** = Se hela konversationen mellan två hosts

```
1. Högerklicka på ett paket
2. Follow → TCP Stream (eller HTTP/UDP/TLS)
3. Se hela konversationen i läsbar form

Exempel:
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
...

HTTP/1.1 200 OK
Content-Type: text/html
...
<html>...</html>
```

### Hitta lösenord i klartext

**🎓 Övning: Hitta FTP-lösenord**

```bash
# 1. Starta Wireshark på eth0
# 2. Generera FTP-trafik (i annan terminal):
ftp 192.168.1.10
# Login: testuser
# Password: testpass123

# 3. I Wireshark, använd filter:
ftp

# 4. Se paket med "USER testuser" och "PASS testpass123"
# 5. Follow TCP Stream för att se hela sessionen
```

**Protokoll som ofta skickar lösenord i klartext:**
- FTP (port 21)
- Telnet (port 23)
- HTTP Basic Auth (port 80)
- SMTP (port 25)
- POP3 (port 110)

**Säkra alternativ (encrypted):**
- SFTP/SCP (SSH - port 22)
- HTTPS (port 443)
- SMTPS/IMAPS (encrypted email)

### Export Objects

**Exportera filer från HTTP-trafik:**

```
1. File → Export Objects → HTTP
2. Se lista av alla filer (bilder, HTML, JS, etc.)
3. Välj fil → Save
```

Användningsfall:
- Analysera webbsidor
- Hitta malware
- Forensics

### Wireshark statistics

```
Statistics menu:

├─ Capture File Properties (översikt)
├─ Protocol Hierarchy (vilka protokoll används?)
├─ Conversations (vilka hosts pratar med varandra?)
├─ Endpoints (vilka IPs är aktiva?)
├─ I/O Graph (trafik över tid)
└─ HTTP → Requests (alla HTTP requests)
```

### Wireshark för troubleshooting

**Exempel: Varför är webbplatsen långsam?**

```
1. Capture trafik när du browsar till sidan
2. Statistics → I/O Graph
3. Se:
   - Många retransmissions? = Packet loss
   - Lång tid mellan request och response? = Server slow
   - Många TCP resets? = Connection problems
```

---

## 🧪 Praktiska lab-övningar

### 🎯 Lab Setup

**Du behöver:**
- Kali Linux (din huvudmaskin)
- Metasploitable 2 VM (target)
- Båda på samma nätverk (Host-Only eller NAT)

```bash
# I Kali - hitta din IP
ip addr show

# I Metasploitable - hitta dess IP
ifconfig

# Test connectivity
ping <METASPLOITABLE-IP>
```

### Övning 1: Nmap Basics

```bash
# 1. Hitta Metasploitable på nätverket
nmap -sn 192.168.56.0/24

# 2. Basic scan
nmap <METASPLOITABLE-IP>

# 3. Identifiera öppna portar
# Förväntat: 21 (FTP), 22 (SSH), 23 (Telnet), 80 (HTTP), etc.

# 4. Service version detection
nmap -sV <METASPLOITABLE-IP>

# 5. OS detection
sudo nmap -O <METASPLOITABLE-IP>

# 6. Aggressive scan
nmap -A -T4 <METASPLOITABLE-IP> -oN metasploitable_scan.txt

# 7. Analysera resultaten
cat metasploitable_scan.txt
# Vilka services är outdated?
# Vilka portar är öppna?
```

### Övning 2: NSE Vulnerability Scanning

```bash
# 1. Scanna för sårbarheter
nmap --script vuln <METASPLOITABLE-IP> -oN vuln_scan.txt

# 2. SMB vulnerabilities (Metasploitable har många!)
nmap --script smb-vuln-* <METASPLOITABLE-IP>

# 3. FTP anonymous login
nmap --script ftp-anon <METASPLOITABLE-IP>

# 4. HTTP enumeration
nmap --script http-enum -p 80 <METASPLOITABLE-IP>

# Förväntat: Många sårbarheter hittas!
# (Detta är meningen - Metasploitable är avsiktligt sårbar)
```

### Övning 3: Netdiscover

```bash
# 1. Hitta alla enheter på nätverket
sudo netdiscover -r 192.168.56.0/24

# 2. Identifiera:
# - Kali Linux (din IP)
# - Metasploitable (target IP)
# - Andra VMs?

# 3. Notera MAC-adresser
```

### Övning 4: Wireshark Packet Capture

```bash
# 1. Starta Wireshark
sudo wireshark

# 2. Välj interface (se var Metasploitable är)
# - Om Host-Only: vboxnet0
# - Om NAT: eth0

# 3. Start capture (🦈)

# 4. I annan terminal - generera trafik:
ping <METASPLOITABLE-IP>

# 5. I Wireshark - filter:
icmp

# 6. Se ping requests och replies

# 7. Stop capture
```

### Övning 5: Wireshark - HTTP Traffic Analysis

```bash
# 1. Starta Wireshark capture

# 2. I Kali - browse till Metasploitable's webserver:
firefox http://<METASPLOITABLE-IP>

# 3. I Wireshark - filter:
http

# 4. Hitta HTTP GET request

# 5. Follow TCP Stream

# 6. Se:
GET / HTTP/1.1
Host: <METASPLOITABLE-IP>
User-Agent: Mozilla/5.0...

HTTP/1.1 200 OK
...
<html>...</html>

# 7. Export Objects → HTTP
# Se alla laddade filer (bilder, CSS, JS)
```

### Övning 6: Wireshark - Hitta lösenord (FTP)

```bash
# 1. Starta Wireshark capture

# 2. I Kali terminal - anslut till Metasploitable FTP:
ftp <METASPLOITABLE-IP>
# Username: msfadmin
# Password: msfadmin

# 3. I Wireshark - filter:
ftp

# 4. Hitta paket med:
# USER msfadmin
# PASS msfadmin

# 5. Follow TCP Stream - se hela FTP-sessionen

# 🔴 LÄRDOM: FTP skickar lösenord i KLARTEXT!
# Använd SFTP istället i verkliga scenarion.
```

---

## 🧪 Självtest - Nivå 3A

### Kunskapsfrågor

1. **Vad är reconnaissance?**
   - A) Exploitering av sårbarheter
   - B) Informationsinsamling om målet
   - C) Rapportskrivning
   - D) Removing access

2. **Vilken typ av Nmap-scan är mest "stealth"?**
   - A) `-sT` (TCP Connect)
   - B) `-sS` (SYN Scan)
   - C) `-sU` (UDP Scan)
   - D) `-A` (Aggressive)

3. **Vad gör `nmap -sn`?**
   - A) Port scan
   - B) Ping sweep (no port scan)
   - C) OS detection
   - D) Version detection

4. **Vilken port är HTTP?**
   - A) 21
   - B) 22
   - C) 80
   - D) 443

5. **Vad är NSE?**
   - A) Network Service Enumeration
   - B) Nmap Scripting Engine
   - C) Network Security Evaluator
   - D) Nmap System Engine

6. **Vad gör Netdiscover?**
   - A) Port scanning
   - B) ARP-based network discovery
   - C) Packet analysis
   - D) Vulnerability scanning

7. **Vad är Wireshark?**
   - A) Port scanner
   - B) Packet sniffer/analyzer
   - C) Exploit framework
   - D) Password cracker

8. **Vilket protokoll skickar lösenord i klartext?**
   - A) HTTPS
   - B) SSH
   - C) FTP
   - D) SFTP

9. **Vad betyder `-A` i Nmap?**
   - A) Anonymous scan
   - B) Aggressive (OS + Version + Scripts + Traceroute)
   - C) All ports
   - D) Auto-detect

10. **Är det lagligt att scanna andras nätverk utan tillstånd?**
    - A) Ja, om du har goda avsikter
    - B) Ja, Nmap är lagligt
    - C) NEJ, det är dataintrång
    - D) Ja, om du bara scannar snabbt

### Praktiska uppgifter (i lab)

- [ ] **1. Ping sweep för att hitta Metasploitable**
  ```bash
  nmap -sn 192.168.56.0/24
  ```

- [ ] **2. Basic scan på Metasploitable**
  ```bash
  nmap <METASPLOITABLE-IP>
  ```

- [ ] **3. Service version detection**
  ```bash
  nmap -sV <METASPLOITABLE-IP>
  ```

- [ ] **4. Vulnerability scan med NSE**
  ```bash
  nmap --script vuln <METASPLOITABLE-IP>
  ```

- [ ] **5. Netdiscover network discovery**
  ```bash
  sudo netdiscover -r 192.168.56.0/24
  ```

- [ ] **6. Wireshark HTTP capture**
  ```bash
  # Start Wireshark, browse to http://<METASPLOITABLE-IP>, filter http
  ```

- [ ] **7. Wireshark FTP password sniffing**
  ```bash
  # Capture FTP login, filter ftp, hitta lösenord
  ```

### Svar

<details>
<summary>Klicka för svar</summary>

**Kunskapsfrågor:**
1. **B** - Informationsinsamling om målet
2. **B** - `-sS` (SYN Scan) - incomplete handshake
3. **B** - Ping sweep (host discovery utan port scan)
4. **C** - 80 (HTTPS är 443)
5. **B** - Nmap Scripting Engine
6. **B** - ARP-based network discovery
7. **B** - Packet sniffer/analyzer
8. **C** - FTP (och Telnet, HTTP Basic Auth, etc.)
9. **B** - Aggressive (combines OS + Version + Scripts + Traceroute)
10. **C** - NEJ, det är dataintrång utan explicit tillstånd

**Scoring:**
- 9-10 rätt: 🏆 Excellent! Du förstår reconnaissance
- 7-8 rätt: ✅ Bra kunskaper
- 5-6 rätt: 📚 OK - repetera vissa delar
- <5 rätt: 🔄 Läs igenom nivån igen

**Praktiska uppgifter:** Alla ska fungera i din lab-miljö!

</details>

---

## ✅ Checklista - Redo för Nivå 3B?

- [ ] Förstår vad reconnaissance är och varför det är viktigt
- [ ] Kan använda Nmap för host discovery och port scanning
- [ ] Känner till olika Nmap scan-typer (-sS, -sT, -sU, -A)
- [ ] Kan använda NSE scripts för vulnerability scanning
- [ ] Förstår Nmap timing (-T0 till -T5)
- [ ] Kan använda Netdiscover för network discovery
- [ ] Kan använda Wireshark för packet capture
- [ ] Kan använda display filters i Wireshark
- [ ] Kan följa TCP streams i Wireshark
- [ ] Förstår skillnaden mellan encrypted och unencrypted protocols
- [ ] Har genomfört alla lab-övningar på Metasploitable

**🎯 Nästa steg:**

👉 **[Nivå 3B - OSINT & Advanced Reconnaissance](./niva-3b-reconnaissance-pt2.md)**

Nu ska vi lära oss OSINT-verktyg: theHarvester, Maltego, Recon-ng och Shodan!

---

**[⬅️ Föregående: Nivå 2C](./niva-2c-system.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 3B](./niva-3b-reconnaissance-pt2.md)**

---

**📌 Kom ihåg:**

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  "Information is power in pentesting"                    │
│                                                          │
│  "Information är makt inom penetrationstestning"         │
│                                                          │
│  Ju mer du vet om målet, desto effektivare kan du       │
│  hitta och exploatera sårbarheter - lagligt och etiskt! │
│                                                          │
└──────────────────────────────────────────────────────────┘
```
