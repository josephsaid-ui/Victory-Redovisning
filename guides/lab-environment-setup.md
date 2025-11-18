# 🔬 Lab Environment Setup Guide

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

## 📚 Innehållsförteckning

1. [Varför Lab Environments?](#varfor-lab)
2. [Lab Network Architecture](#network-architecture)
3. [Metasploitable 2 Setup](#metasploitable-2)
4. [Metasploitable 3 Setup](#metasploitable-3)
5. [DVWA Setup](#dvwa)
6. [Vulnerable WordPress Setup](#wordpress)
7. [Windows Vulnerable VMs](#windows-vms)
8. [HackTheBox och TryHackMe](#online-platforms)
9. [Docker Lab Environments](#docker-labs)
10. [Nätverkskonfiguration](#network-config)
11. [Säkerhet och Isolation](#security-isolation)
12. [Troubleshooting](#troubleshooting)

---

## 🎯 Varför Lab Environments? {#varfor-lab}

### Betydelsen av Säkra Testmiljöer

**Lab environments** är KRITISKA för att lära sig etisk hacking:

```
✅ FÖRDELAR MED LAB ENVIRONMENTS:

1️⃣  LAGLIGT & SÄKERT
    • Inga juridiska risker
    • Inget verkligt system skadas
    • Inga etiska dilemman

2️⃣  OBEGRÄNSAD TESTNING
    • Testa alla tekniker
    • Experimentera fritt
    • Lär av misstag utan konsekvenser

3️⃣  REPRODUCERBART
    • Snapshots → återställ enkelt
    • Upprepa övningar
    • Testa olika approacher

4️⃣  KONTROLLERAD MILJÖ
    • Ingen risk för produktionssystem
    • Isolerat nätverk
    • Fullständig kontroll

5️⃣  CERTIFIERINGSFÖRBEREDELSE
    • OSCP, CEH, GPEN kräver labbar
    • Praktisk erfarenhet
    • Portfolio-byggande
```

### Lab Types

| Lab Type | Komplexitet | Kostnad | Användning |
|----------|-------------|---------|------------|
| **Lokala VMs** | Låg-Medel | Gratis | Daglig träning, grundläggande |
| **Online Platforms** | Medel-Hög | $10-20/mån | Strukturerad learning, certifiering |
| **Custom Labs** | Hög | Varierar | Avancerad träning, specifika scenarios |
| **Red Team Ranges** | Mycket hög | $$$$ | Professionell träning, företag |

---

## 🏗️ Lab Network Architecture {#network-architecture}

### Rekommenderad Setup

```
┌─────────────────────────────────────────────────────────┐
│                  HOST MACHINE (Windows 11)              │
│                                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │            VirtualBox Manager                     │ │
│  │                                                   │ │
│  │  ┌─────────────┐        ┌────────────────────┐  │ │
│  │  │ Kali Linux  │◄──────►│ Metasploitable 2   │  │ │
│  │  │ 192.168.56.2│        │ 192.168.56.101     │  │ │
│  │  └──────┬──────┘        └────────────────────┘  │ │
│  │         │                                        │ │
│  │         │               ┌────────────────────┐  │ │
│  │         └──────────────►│ DVWA               │  │ │
│  │                         │ 192.168.56.102     │  │ │
│  │                         └────────────────────┘  │ │
│  │                                                 │ │
│  │  Network: Host-Only (vboxnet0)                 │ │
│  │  Subnet: 192.168.56.0/24                       │ │
│  └───────────────────────────────────────────────┘ │
│                                                     │
│  Internet ◄──► NAT (för updates)                   │
└─────────────────────────────────────────────────────┘
```

### Network Modes i VirtualBox

| Mode | Beskrivning | Användning |
|------|-------------|------------|
| **NAT** | VM kan accessa internet, isolerad från host | Updates, downloads |
| **Bridged** | VM får IP från fysiskt nätverk | ❌ EJ för vulnerable VMs! |
| **Host-Only** | VM och host kan kommunicera, ej internet | ✅ PERFEKT för labbar |
| **Internal Network** | Endast mellan VMs | Avancerade multi-VM scenarios |

**🔴 VIKTIGT:** Använd **ALDRIG** Bridged mode för vulnerable VMs → kan exponera ditt fysiska nätverk!

---

## 💀 Metasploitable 2 Setup {#metasploitable-2}

### Översikt

**Metasploitable 2** är en avsiktligt sårbar Linux-VM skapad av Rapid7 för penetrationstestning.

| Egenskap | Detalj |
|----------|--------|
| **OS** | Ubuntu 8.04 (uttjänt) |
| **Sårbarheter** | 40+ olika services |
| **Storlek** | ~900 MB |
| **Användning** | Nybörjarvänlig, perfekt första lab |
| **Svårighetsgrad** | Lätt till Medel |

### Installation

#### Steg 1: Ladda Ner

```bash
# Officiell källa (SourceForge)
# https://sourceforge.net/projects/metasploitable/

# Eller via command line (på Kali eller Linux)
wget https://sourceforge.net/projects/metasploitable/files/Metasploitable2/metasploitable-linux-2.0.0.zip
```

#### Steg 2: Extrahera

```bash
# Windows
# Högerklicka → Extract All

# Linux/Kali
unzip metasploitable-linux-2.0.0.zip
```

#### Steg 3: Importera till VirtualBox

**Metod A: Skapa ny VM med befintlig disk**

1. Öppna VirtualBox → **New**
2. **Namn:** Metasploitable 2
3. **Type:** Linux
4. **Version:** Ubuntu (64-bit) eller Other Linux (64-bit)
5. **Memory:** 512 MB (minimum)
6. **Hard Disk:** Use an existing virtual hard disk file
   - Klicka folder-ikon → Browse
   - Välj `Metasploitable.vmdk`
7. **Create**

**Metod B: Importera direkt**

1. VirtualBox → **Machine → Add**
2. Navigate till `Metasploitable.vmdk`
3. Select → Open

#### Steg 4: Konfigurera Network

1. Välj Metasploitable 2 VM → **Settings**
2. **Network → Adapter 1**
   - ☑ Enable Network Adapter
   - **Attached to:** Host-only Adapter
   - **Name:** vboxnet0
3. **OK**

#### Steg 5: Starta och Logga In

```bash
# Starta VM i VirtualBox

# Login credentials
Username: msfadmin
Password: msfadmin

# Efter login, kolla IP
ifconfig
# eth0: 192.168.56.101 (exempel)
```

### Verifiera Installation

**Från Kali Linux:**

```bash
# Ping test
ping 192.168.56.101

# Quick Nmap scan
nmap -sV 192.168.56.101

# Output bör visa många öppna portar:
# 21/tcp   open  ftp         vsftpd 2.3.4
# 22/tcp   open  ssh         OpenSSH 4.7p1
# 23/tcp   open  telnet      Linux telnetd
# 25/tcp   open  smtp        Postfix smtpd
# 80/tcp   open  http        Apache httpd 2.2.8
# ...många fler
```

### Vanliga Sårbarheter i Metasploitable 2

| Service | Port | Vulnerability | Exploit Module |
|---------|------|---------------|----------------|
| **vsftpd** | 21 | Backdoor | `exploit/unix/ftp/vsftpd_234_backdoor` |
| **SSH** | 22 | Weak passwords | Brute-force med Hydra |
| **Telnet** | 23 | Unencrypted | `auxiliary/scanner/telnet/telnet_login` |
| **Samba** | 139/445 | Username map script | `exploit/multi/samba/usermap_script` |
| **Distcc** | 3632 | Remote code execution | `exploit/unix/misc/distcc_exec` |
| **PostgreSQL** | 5432 | Default credentials | `postgres/postgres` |
| **VNC** | 5900 | No password | Direct VNC connection |
| **Tomcat** | 8180 | Default credentials | `tomcat/tomcat` |

### Snapshot Strategy

**🟢 REKOMMENDATION:** Ta snapshot INNAN du börjar attackera!

```
VirtualBox → Metasploitable 2 → Machine → Take Snapshot
Namn: "Fresh Install - Clean State"
```

**Varför?**
- Snabb återställning om något går fel
- Testa olika attack paths
- Jämföra före/efter

---

## 🔥 Metasploitable 3 Setup {#metasploitable-3}

### Översikt

**Metasploitable 3** är efterföljaren till Metasploitable 2, byggd med moderna teknologier.

| Egenskap | Detalj |
|----------|--------|
| **OS** | Windows Server 2008 R2 eller Ubuntu 14.04 |
| **Sårbarheter** | 50+ moderna sårbarheter |
| **Storlek** | ~4-6 GB |
| **Komplexitet** | Medel till Hög |
| **Build Method** | Packer + Vagrant (automatiserad) |

### Installation (Ubuntu Version)

**🟡 NOTERA:** Metasploitable 3 kräver mer avancerad setup än M2.

#### Steg 1: Förutsättningar

```bash
# På Kali (eller Linux host)
sudo apt update
sudo apt install virtualbox vagrant packer

# Verifiera installationer
vagrant --version
packer --version
```

#### Steg 2: Klona Repository

```bash
# Klona Metasploitable 3 repo
git clone https://github.com/rapid7/metasploitable3.git
cd metasploitable3

# Välj Ubuntu variant
cd metasploitable3-ubuntu
```

#### Steg 3: Bygg med Packer

```bash
# Bygg Ubuntu VM (tar 30-60 minuter)
packer build -only=virtualbox-iso metasploitable3-ubuntu.json

# Detta skapar en .box-fil i builds/
```

#### Steg 4: Lägg till Vagrant Box

```bash
# Lägg till byggd box
vagrant box add builds/metasploitable3-ubuntu.box --name metasploitable3-ubuntu

# Verifiera
vagrant box list
# metasploitable3-ubuntu (virtualbox, 0)
```

#### Steg 5: Initiera och Starta

```bash
# Skapa ny directory för VM
mkdir ~/metasploitable3-lab
cd ~/metasploitable3-lab

# Initiera
vagrant init metasploitable3-ubuntu

# Redigera Vagrantfile för Host-Only network
nano Vagrantfile

# Lägg till:
config.vm.network "private_network", ip: "192.168.56.103"

# Spara och starta
vagrant up
```

#### Steg 6: Logga In

```bash
# SSH via Vagrant
vagrant ssh

# Eller direkt via SSH
ssh vagrant@192.168.56.103
# Password: vagrant
```

### Metasploitable 3 Windows Version

**Alternativt:** Bygg Windows Server 2008 R2 version:

```bash
cd metasploitable3/metasploitable3-windows
packer build -only=virtualbox-iso metasploitable3-windows.json
vagrant box add builds/metasploitable3-windows.box --name metasploitable3-windows
```

**Credentials:**
- Username: `vagrant`
- Password: `vagrant`

### Vanliga Sårbarheter i Metasploitable 3

| Vulnerability | Type | Difficulty |
|---------------|------|------------|
| **ProFTPD** | Remote Code Execution | Easy |
| **Apache Tomcat** | Manager default credentials | Easy |
| **ManageEngine** | Multiple vulnerabilities | Medium |
| **Elasticsearch** | CVE-2015-1427 RCE | Medium |
| **IIS WebDAV** | CVE-2017-7269 | Medium-Hard |
| **JMX** | Unauth RMI Registry | Medium |

---

## 🌐 DVWA Setup {#dvwa}

### Översikt

**DVWA (Damn Vulnerable Web Application)** är en PHP/MySQL web application designad för att lära web application security.

| Egenskap | Detalj |
|----------|--------|
| **Typ** | Web Application |
| **Språk** | PHP + MySQL |
| **Fokus** | OWASP Top 10 |
| **Svårighetsgrader** | Low, Medium, High, Impossible |
| **Sårbarheter** | SQLi, XSS, CSRF, File Upload, Command Injection, etc. |

### Installation (Metod 1: Manual på LAMP)

#### Steg 1: Förbered LAMP Server

```bash
# På Ubuntu VM eller ny Ubuntu installation
sudo apt update
sudo apt install apache2 mariadb-server php php-mysqli php-gd libapache2-mod-php -y

# Starta services
sudo systemctl start apache2
sudo systemctl start mariadb
sudo systemctl enable apache2
sudo systemctl enable mariadb
```

#### Steg 2: Ladda Ner DVWA

```bash
# Navigera till web root
cd /var/www/html

# Klona DVWA
sudo git clone https://github.com/digininja/DVWA.git dvwa

# Sätt permissions
sudo chown -R www-data:www-data /var/www/html/dvwa
sudo chmod -R 755 /var/www/html/dvwa
```

#### Steg 3: Konfigurera Database

```bash
# Logga in MySQL
sudo mysql -u root

# Skapa databas och användare
CREATE DATABASE dvwa;
CREATE USER 'dvwauser'@'localhost' IDENTIFIED BY 'dvwapass';
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwauser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

#### Steg 4: Konfigurera DVWA

```bash
# Kopiera config
cd /var/www/html/dvwa/config
sudo cp config.inc.php.dist config.inc.php

# Redigera config
sudo nano config.inc.php

# Ändra database credentials:
$_DVWA[ 'db_user' ] = 'dvwauser';
$_DVWA[ 'db_password' ] = 'dvwapass';
$_DVWA[ 'db_database' ] = 'dvwa';

# Spara (Ctrl+O, Enter, Ctrl+X)
```

#### Steg 5: PHP Configuration

```bash
# Redigera php.ini
sudo nano /etc/php/7.4/apache2/php.ini

# Ändra/kontrollera:
allow_url_include = On
allow_url_fopen = On
display_errors = On

# Spara och restarta Apache
sudo systemctl restart apache2
```

#### Steg 6: Setup Database via Web Interface

```
1. Browse till: http://192.168.56.102/dvwa
2. Klicka "Create / Reset Database"
3. Login:
   Username: admin
   Password: password
4. Klicka "DVWA Security" → Sätt till "Low"
```

### Installation (Metod 2: Docker)

**Enklast och snabbast:**

```bash
# Installera Docker (om ej installerat)
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker

# Kör DVWA container
sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa

# Access via: http://192.168.56.X
# Login: admin / password
```

### DVWA Modules

| Module | Vulnerability Type | Learning Objective |
|--------|-------------------|-------------------|
| **Brute Force** | Authentication bypass | Password strength, rate limiting |
| **Command Injection** | OS command execution | Input validation |
| **CSRF** | Cross-Site Request Forgery | Token validation |
| **File Inclusion** | Local/Remote File Inclusion | Path traversal, input filtering |
| **File Upload** | Unrestricted file upload | File type validation, magic bytes |
| **SQL Injection** | Database manipulation | Parameterized queries |
| **SQL Injection (Blind)** | Boolean/Time-based SQLi | Advanced SQL injection |
| **Weak Session IDs** | Session hijacking | Secure session management |
| **XSS (DOM)** | Client-side XSS | JavaScript security |
| **XSS (Reflected)** | Non-persistent XSS | Output encoding |
| **XSS (Stored)** | Persistent XSS | Data sanitization |
| **CSP Bypass** | Content Security Policy | Header security |
| **JavaScript** | Client-side attacks | JavaScript obfuscation |

### Security Levels

```
LOW:
• Ingen security
• Lätt att exploatera
• Bra för nybörjare

MEDIUM:
• Enkel validering
• Kräver lite mer teknik
• Intermediate level

HIGH:
• Starkare skydd
• Kräver avancerade tekniker
• Bypass-utmaningar

IMPOSSIBLE:
• Säker implementation
• Visa hur det SKA göras
• Lär bästa praxis
```

---

## 📝 WordPress Vulnerable Setup {#wordpress}

### WPScan Test Environment

#### Steg 1: Installera WordPress

```bash
# På LAMP server
cd /var/www/html
sudo wget https://wordpress.org/latest.tar.gz
sudo tar -xzvf latest.tar.gz
sudo chown -R www-data:www-data wordpress

# Skapa databas
sudo mysql -u root
CREATE DATABASE wordpress;
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost' IDENTIFIED BY 'wppass';
FLUSH PRIVILEGES;
EXIT;
```

#### Steg 2: Konfigurera WordPress

```
Browse: http://192.168.56.X/wordpress
Följ setup-wizard:
- Database: wordpress
- Username: wpuser
- Password: wppass
- Table Prefix: wp_
```

#### Steg 3: Installera Sårbara Plugins

**Manuellt (för testing):**

```bash
# Ladda ner gamla/sårbara plugin-versioner från exploit-db
# Exempel: Upload vulnerable plugin via WordPress admin panel

# Eller via WP-CLI
wp plugin install plugin-name --version=1.0 --activate
```

**Vulnerable WordPress VM (Färdig):**

```bash
# Alternativt: Använd färdig vulnerable WordPress VM
# Ladda ner från VulnHub:
# https://www.vulnhub.com/entry/dc-1,292/
```

---

## 🪟 Windows Vulnerable VMs {#windows-vms}

### Recommended Vulnerable Windows VMs

| VM Name | Description | Download |
|---------|-------------|----------|
| **Metasploitable 3 (Windows)** | Windows Server 2008 R2 | GitHub (Packer build) |
| **IEWIN7** | IE Testing VM (ofta sårbara) | Microsoft Developer VMs |
| **SickOS 1.2** | Windows + Linux dual-boot | VulnHub |
| **HackSys Extreme Vulnerable Driver** | Kernel exploitation | GitHub |

### Windows Server 2019 Evaluation

**Legal och gratis för 180 dagar:**

```
1. Ladda ner: https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019
2. Installera i VirtualBox
3. Manuellt introducera sårbarheter för testing:
   - Inaktivera Windows Defender
   - Svaga lösenord
   - Aktivera SMBv1
   - Installera gamla mjukvaror
```

**🔴 VIKTIGT:** Isolera alltid i Host-Only network!

---

## 🌍 HackTheBox och TryHackMe {#online-platforms}

### HackTheBox (HTB)

**Översikt:**
- 300+ vulnerable machines
- Real-world scenarios
- Ranking system
- VPN-baserad access

**Setup:**

```bash
# 1. Registrera på hackthebox.com (gratis tier finns)
# 2. Ladda ner VPN config från Account → VPN Access
# 3. Anslut via OpenVPN på Kali

sudo openvpn lab_username.ovpn

# 4. Verifiera anslutning
ifconfig tun0
# Bör visa 10.10.14.X IP

# 5. Ping HTB machines
ping 10.10.10.X
```

**HTB Tiers:**

| Tier | Kostnad | Machines | Retired Machines | Starting Point |
|------|---------|----------|------------------|----------------|
| **Free** | $0 | 20 active | Nej | Ja |
| **VIP** | $14/mån | 20 active | Alla (400+) | Ja + Walkthrough |
| **VIP+** | $22/mån | 20 active | Alla | Ja + Walkthrough + Dedicated |

### TryHackMe (THM)

**Översikt:**
- Nybörjarvänlig
- Guided learning paths
- Web-baserad VM access (ej VPN krävs)
- 1000+ rooms

**Setup:**

```bash
# 1. Registrera på tryhackme.com
# 2. Starta "AttackBox" (Kali Linux i webbläsaren)
#    ELLER
# 3. Anslut egen Kali via OpenVPN

sudo openvpn username.ovpn

# 4. Machines tillgängliga direkt via THM interface
```

**THM Learning Paths:**

- Complete Beginner
- Offensive Pentesting
- Web Fundamentals
- Cyber Defense
- CompTIA Pentest+
- Red Teaming

### Jämförelse HTB vs THM

| Aspekt | HackTheBox | TryHackMe |
|--------|------------|-----------|
| **Svårighetsgrad** | Medel-Hög | Lätt-Medel |
| **Nybörjare** | Svårt att börja | Mycket nybörjarvänligt |
| **Guidance** | Minimal (VIP: writeups) | Extensive (guided rooms) |
| **Access** | VPN required | Web-based eller VPN |
| **Community** | Stort, kompetitivt | Stort, supportivt |
| **Certifiering** | OSCP-förberedelse | CompTIA, general pentesting |
| **Kostnad** | $0-22/mån | $0-11/mån |

---

## 🐳 Docker Lab Environments {#docker-labs}

### Fördelar med Docker Labs

```
✅ SNABB SETUP (sekunder istället för timmar)
✅ MINIMAL DISKUTRYMME (MB istället för GB)
✅ LÄTT ATT ÅTERSTÄLLA (docker restart)
✅ PORTABILITET (samma på alla plattformar)
```

### DVWA Docker (Redan täckt)

```bash
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

### WebGoat (OWASP)

```bash
# WebGoat - Web application security learning
docker run -p 8080:8080 -p 9090:9090 webgoat/webgoat

# Access:
# http://localhost:8080/WebGoat
```

### Juice Shop (OWASP)

```bash
# Modern vulnerable web app (Node.js)
docker run --rm -p 3000:3000 bkimminich/juice-shop

# Access: http://localhost:3000
```

### Vulnerable WordPress

```bash
# WPScan vulnerable WordPress
docker run --rm -p 8000:80 l4rm4nd/wordpress:5.8.1

# Access: http://localhost:8000
```

### Docker Compose Multi-Container Lab

**Exempel: Fullständig lab med flera services:**

```yaml
# docker-compose.yml
version: '3'
services:
  dvwa:
    image: vulnerables/web-dvwa
    ports:
      - "80:80"

  juice-shop:
    image: bkimminich/juice-shop
    ports:
      - "3000:3000"

  webgoat:
    image: webgoat/webgoat
    ports:
      - "8080:8080"
      - "9090:9090"

  mysql:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: vulnerable
      MYSQL_DATABASE: testdb
    ports:
      - "3306:3306"
```

**Starta alla samtidigt:**

```bash
docker-compose up -d

# Access:
# DVWA: http://localhost:80
# Juice Shop: http://localhost:3000
# WebGoat: http://localhost:8080
# MySQL: localhost:3306
```

---

## 🔧 Nätverkskonfiguration {#network-config}

### VirtualBox Host-Only Network Setup

#### Steg 1: Skapa Host-Only Adapter

```
VirtualBox → File → Host Network Manager

Klicka "Create"
Namn: vboxnet0
IPv4 Address: 192.168.56.1
IPv4 Network Mask: 255.255.255.0
DHCP Server: ☐ Disabled (vi sätter statiska IPs)

Apply → Close
```

#### Steg 2: Konfigurera VM Network

**För Kali Linux:**

```
VM Settings → Network → Adapter 1
☑ Enable Network Adapter
Attached to: Host-only Adapter
Name: vboxnet0
```

**För Metasploitable/DVWA/etc:**

Samma konfiguration, men med olika IP:

```
Metasploitable 2: 192.168.56.101
DVWA:            192.168.56.102
Metasploitable 3: 192.168.56.103
WordPress:       192.168.56.104
```

### Statiska IP-adresser

**På Kali Linux:**

```bash
# Redigera /etc/network/interfaces
sudo nano /etc/network/interfaces

# Lägg till:
auto eth0
iface eth0 inet static
    address 192.168.56.2
    netmask 255.255.255.0
    network 192.168.56.0
    broadcast 192.168.56.255

# Restarta network
sudo systemctl restart networking

# Verifiera
ip a
```

**På Ubuntu targets:**

```bash
# Ubuntu 18.04+ använder Netplan
sudo nano /etc/netplan/01-netcfg.yaml

network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: no
      addresses:
        - 192.168.56.101/24

# Apply
sudo netplan apply
```

### Firewall Configuration

**På Kali (om firewall aktivt):**

```bash
# Tillåt trafik till lab network
sudo ufw allow from 192.168.56.0/24

# Eller stäng av helt för lab (EJ rekommenderat för produktion)
sudo ufw disable
```

---

## 🔒 Säkerhet och Isolation {#security-isolation}

### Kritiska Säkerhetsåtgärder

```
🔴 KRITISKT - FÖLJ DESSA REGLER:

1️⃣  ALDRIG BRIDGED MODE
    ❌ Exponerar vulnerable VMs till fysiskt nätverk
    ❌ Kan kompromettera andra enheter
    ✅ Använd ENDAST Host-Only eller Internal Network

2️⃣  INGEN INTERNET-ACCESS FÖR VULNERABLE VMs
    ❌ Vulnerable VMs kan bli komprometterade av riktiga attackerare
    ✅ Isolera helt från internet

3️⃣  SNAPSHOTS INNAN EXPLOITS
    ✅ Ta snapshot innan varje test
    ✅ Återställ efter varje session
    ✅ Håll "clean state" backup

4️⃣  ALDRIG KÄNSLIG DATA I LAB VMs
    ❌ Inga riktiga lösenord
    ❌ Ingen personlig information
    ❌ Inga företagsdata

5️⃣  DOKUMENTERA OCH LOGA
    ✅ Spara kommandon och resultat
    ✅ Screenshot för portfolio
    ✅ Anteckna lessons learned
```

### Network Isolation Levels

| Level | Configuration | Safety | Use Case |
|-------|---------------|--------|----------|
| **Level 1** | Host-Only + No Internet | ⭐⭐⭐⭐⭐ | Rekommenderat för alla labbar |
| **Level 2** | Internal Network | ⭐⭐⭐⭐ | Multi-VM scenarios utan host access |
| **Level 3** | NAT (outbound only) | ⭐⭐⭐ | Om updates behövs |
| **Level 4** | Bridged | ⭐ | ❌ ALDRIG för vulnerable VMs |

### Snapshot Strategy

```bash
# 1. Clean Install
VirtualBox → VM → Take Snapshot
Namn: "00-Clean-Install"
Beskrivning: "Fresh installation, no changes"

# 2. Configured State
Efter basic configuration:
Namn: "01-Configured"
Beskrivning: "Network configured, ready for testing"

# 3. Before Major Exploit
Innan stor exploit:
Namn: "02-Pre-Metasploit-Test"
Beskrivning: "Before vsftpd backdoor exploit"

# 4. Återställ
VirtualBox → VM → Snapshots → Right-click snapshot → Restore
```

---

## 🔧 Troubleshooting {#troubleshooting}

### Vanliga Problem och Lösningar

#### Problem 1: VM Can't Ping Each Other

```
Symptom: ping 192.168.56.101 → timeout

Lösningar:
1. Kontrollera båda VMs använder samma Host-Only adapter (vboxnet0)
2. Verifiera statiska IPs är korrekt konfigurerade
3. Inaktivera firewall temporärt för test:
   sudo ufw disable  # Kali
   sudo ufw status   # Verifiera

4. Testa från host:
   ping 192.168.56.2  # Kali
   ping 192.168.56.101  # Metasploitable
```

#### Problem 2: DVWA Database Error

```
Symptom: "Could not connect to database"

Lösningar:
1. Verifiera MySQL körs:
   sudo systemctl status mariadb
   sudo systemctl start mariadb

2. Kontrollera credentials i config.inc.php
3. Reset database:
   sudo mysql -u root
   DROP DATABASE dvwa;
   CREATE DATABASE dvwa;
   GRANT ALL ON dvwa.* TO 'dvwauser'@'localhost';
   EXIT;

4. Browse till /dvwa/setup.php → Create Database
```

#### Problem 3: Metasploitable 3 Build Fails

```
Symptom: Packer build error

Lösningar:
1. Kontrollera internet connection
2. Öka timeout i .json:
   "boot_wait": "10s" → "boot_wait": "30s"

3. Försäkra tillräckligt diskutrymme (15GB+)
4. Ladda ner pre-built box istället:
   vagrant box add rapid7/metasploitable3-ub1404
```

#### Problem 4: VirtualBox Guest Additions Not Working

```
Symptom: Ingen delad clipboard, låg upplösning

Lösning:
1. VM → Devices → Insert Guest Additions CD image
2. På VM:
   sudo mkdir /media/cdrom
   sudo mount /dev/cdrom /media/cdrom
   cd /media/cdrom
   sudo ./VBoxLinuxAdditions.run

3. Restart VM
```

#### Problem 5: Out of Memory

```
Symptom: VM kraschar, "Not enough memory"

Lösningar:
1. Minska RAM allocation:
   Kali: 2048 MB (minimum)
   Metasploitable: 512 MB
   DVWA: 512 MB

2. Stäng andra VMs
3. Stäng tunga applikationer på host
4. Öka host RAM om möjligt
```

#### Problem 6: Slow Performance

```
Lösningar:
1. Aktivera VT-x/AMD-V i BIOS
2. Allokera flera CPU cores:
   VM Settings → System → Processor → 2-4 cores

3. Använd SSD för VMs
4. Inaktivera 3D acceleration (kan orsaka problem):
   VM Settings → Display → 3D Acceleration: ☐
```

---

## 📊 Lab Environment Checklist

### Initial Setup

- [ ] VirtualBox installerat
- [ ] Host-Only network (vboxnet0) konfigurerat
- [ ] Kali Linux VM fungerande
- [ ] Kali har statisk IP: 192.168.56.2
- [ ] Snapshots tagna för clean state

### Vulnerable VMs

- [ ] Metasploitable 2 importerad (192.168.56.101)
- [ ] DVWA installerat och fungerande (192.168.56.102)
- [ ] (Optional) Metasploitable 3 (192.168.56.103)
- [ ] (Optional) Vulnerable WordPress (192.168.56.104)
- [ ] Alla VMs använder Host-Only network
- [ ] Ingen VM har internet access via Bridged

### Testing och Verification

- [ ] Ping fungerar mellan Kali och alla targets
- [ ] Nmap scan visar öppna portar på Metasploitable
- [ ] DVWA accessible via webbläsare från Kali
- [ ] Snapshots tagna för alla VMs

### Security

- [ ] Inga vulnerable VMs i Bridged mode
- [ ] Dokumentation påbörjad
- [ ] Backup-strategi etablerad

---

## 🎯 Nästa Steg

**Nu när du har din lab-miljö:**

1. **Börja med Metasploitable 2**
   - Följ Nivå 4B: Exploitation guide
   - Testa vsftpd backdoor exploit
   - Dokumentera alla steg

2. **DVWA Challenges**
   - Börja med "Low" security
   - Testa SQL Injection
   - Prova XSS attacks

3. **Join Online Platforms**
   - TryHackMe: Complete Beginner path
   - HackTheBox: Starting Point boxes

4. **Dokumentera Allt**
   - Håll lab journal
   - Screenshot viktiga fynd
   - Bygg portfolio

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**🔬 "A good lab environment is the foundation of practical cybersecurity learning."**
