# ⚙️ Nivå 2C: Pakethantering & Systemadministration

**⏱️ Beräknad tid:** 30-45 minuter
**📚 Svårighetsgrad:** ⭐⭐ Nybörjare-Intermediate
**🎯 Förutsättningar:** Nivå 2A & 2B genomförda
**🎓 Lärdomsmål:** Installera program, hantera processer och förstå systemadministration

---

## 📋 Innehåll

1. [Pakethantering med APT](#-pakethantering-med-apt)
2. [Process-hantering](#-process-hantering)
3. [System-services](#-system-services)
4. [Användare och grupper](#-användare-och-grupper)
5. [Nätverk-basics](#-nätverk-basics)
6. [System-information](#-system-information)
7. [Praktiska övningar](#-praktiska-övningar)
8. [Självtest & Sammanfattning](#-självtest-nivå-2c)

---

## 📦 Pakethantering med APT

### Vad är APT?

**APT** (Advanced Package Tool) är Debian/Kali's pakethanterare.

```
┌──────────────────────────────────────────────────────────┐
│  APT = App Store för Linux (men via terminal)           │
│                                                          │
│  Istället för att ladda ner .exe från webbplatser:      │
│  → Installera allt säkert via APT                       │
└──────────────────────────────────────────────────────────┘
```

### Repositories (paket-källor)

APT laddar ner paket från **repositories** (servrar med programvara).

```bash
# Kali's repositories finns i:
cat /etc/apt/sources.list

# Typisk output:
# deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware
```

### 1. `apt update` - Uppdatera paketlistor

```bash
# ALLTID kör detta först!
sudo apt update

# Vad händer:
# - Laddar ner senaste paketlistor från repositories
# - Ingen installation sker (bara uppdatering av metadata)
```

**🔴 VIKTIGT:** Kör `apt update` INNAN `apt upgrade` eller `apt install`!

### 2. `apt upgrade` - Uppgradera installerade paket

```bash
# Uppgradera alla paket
sudo apt upgrade

# Frågar om bekräftelse (Y/n)
# Visar hur mycket som laddas ner

# Skip bekräftelse (auto-yes)
sudo apt upgrade -y

# Full-upgrade (kan ta bort paket om nödvändigt)
sudo apt full-upgrade
```

**Skillnad upgrade vs full-upgrade:**

| Kommando | Vad det gör |
|----------|-------------|
| `apt upgrade` | Uppgradera paket, tar INTE bort befintliga |
| `apt full-upgrade` | Uppgradera paket, KAN ta bort/lägga till paket om behövs |

### 3. `apt install` - Installera paket

```bash
# Installera ett paket
sudo apt install nmap

# Installera flera paket
sudo apt install nmap wireshark metasploit-framework

# Auto-yes (skip bekräftelse)
sudo apt install -y nmap

# Simulate (visa vad som skulle hända utan att installera)
sudo apt install --simulate nmap

# Installera från .deb-fil
sudo apt install ./package.deb

# Installera specifik version
sudo apt install package=version
```

**Vanliga paket att installera:**

```bash
# Development tools
sudo apt install build-essential git vim

# Network tools
sudo apt install net-tools dnsutils

# System utilities
sudo apt install htop tree curl wget

# Python tools
sudo apt install python3-pip

# Terminator (bättre terminal)
sudo apt install terminator
```

### 4. `apt remove` - Avinstallera paket

```bash
# Ta bort paket (men behåll config-filer)
sudo apt remove package

# Ta bort paket OCH config-filer (purge)
sudo apt purge package

# Ta bort dependencies som inte längre behövs
sudo apt autoremove

# Kombinera (rekommenderat):
sudo apt purge package && sudo apt autoremove
```

### 5. `apt search` - Sök efter paket

```bash
# Sök efter paket
apt search nmap

# Sök med regex
apt search "^nmap"

# Visa detaljer om paket
apt show nmap
```

### 6. `apt list` - Lista paket

```bash
# Lista alla tillgängliga paket
apt list

# Lista installerade paket
apt list --installed

# Lista paket som kan uppgraderas
apt list --upgradable

# Lista alla nmap-relaterade paket
apt list | grep nmap
```

### 7. `apt-cache` - Cache-operations

```bash
# Detaljerad info om paket
apt-cache show nmap

# Vilka paket beror på detta paket?
apt-cache rdepends nmap

# Dependencies för paket
apt-cache depends nmap
```

### 8. `dpkg` - Low-level package manager

```bash
# Lista installerade paket
dpkg -l

# Kontrollera om specifikt paket är installerat
dpkg -l | grep nmap

# Lista filer installerade av paket
dpkg -L nmap

# Vilken paket installerade denna fil?
dpkg -S /usr/bin/nmap

# Installera .deb-fil
sudo dpkg -i package.deb

# Ta bort paket
sudo dpkg -r package
```

### APT Cheat Sheet

| Kommando | Vad det gör |
|----------|-------------|
| `sudo apt update` | Uppdatera paketlistor |
| `sudo apt upgrade` | Uppgradera paket |
| `sudo apt install package` | Installera paket |
| `sudo apt remove package` | Ta bort paket (behåll config) |
| `sudo apt purge package` | Ta bort paket (inkl. config) |
| `sudo apt autoremove` | Ta bort orphaned dependencies |
| `apt search keyword` | Sök paket |
| `apt show package` | Visa paket-info |
| `apt list --installed` | Lista installerade |

### Best practices för APT

```bash
# 1. ALLTID uppdatera först
sudo apt update

# 2. Uppgradera system regelbundet
sudo apt update && sudo apt upgrade -y

# 3. Rensa efter installation
sudo apt autoremove && sudo apt clean

# 4. Kombinera vanliga operationer
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y && sudo apt clean

# 5. Sök före installation
apt search package-name
apt show package-name  # Läs beskrivningen!
sudo apt install package-name
```

---

## ⚡ Process-hantering

### Vad är en process?

**Process** = Ett pågående program/kommando

```
Varje program du kör = en process
- Terminal = process
- Firefox = process
- nmap = process
```

### 1. `ps` - Process Status

```bash
# Visa dina processer
ps

# Visa alla processer
ps aux

# Visa process-träd
ps auxf

# Hitta specifik process
ps aux | grep firefox
```

**ps aux output-förklaring:**

```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
kali      1234  2.5  1.3 123456 45678 ?        Ssl  10:30   0:42 firefox
│          │    │    │     │     │    │        │    │       │    │
│          │    │    │     │     │    │        │    │       │    └─ Kommando
│          │    │    │     │     │    │        │    │       └────── CPU-tid
│          │    │    │     │     │    │        │    └────────────── Starttid
│          │    │    │     │     │    │        └─────────────────── Status
│          │    │    │     │     │    └──────────────────────────── Terminal
│          │    │    │     │     └───────────────────────────────── Minne (KB)
│          │    │    │     └─────────────────────────────────────── Virtual memory
│          │    │    └───────────────────────────────────────────── % Memory
│          │    └────────────────────────────────────────────────── % CPU
│          └─────────────────────────────────────────────────────── Process ID
└────────────────────────────────────────────────────────────────── Användare
```

### 2. `top` / `htop` - Live process viewer

```bash
# Top (standard, alltid installerat)
top

# Navigering i top:
# q     = quit
# k     = kill process (ange PID)
# M     = sortera efter minne
# P     = sortera efter CPU
# 1     = visa alla CPU-cores

# htop (bättre, mer user-friendly)
sudo apt install htop -y
htop

# htop navigation:
# F9    = kill process (välj från lista)
# F6    = sortera
# /     = sök
# q     = quit
```

### 3. `kill` - Avsluta process

```bash
# Hitta process ID
ps aux | grep firefox
# firefox har PID 1234

# Kill process (normal)
kill 1234

# Force kill (om processen inte svarar)
kill -9 1234

# Kill by name
killall firefox

# Kill alla processer för en användare
pkill -u username
```

**Kill signals:**

| Signal | Nummer | Vad det gör |
|--------|--------|-------------|
| SIGTERM | 15 | Snäll avslutning (default) |
| SIGKILL | 9 | Force kill (kan inte ignoreras) |
| SIGHUP | 1 | Hang up (restarta service ofta) |

```bash
# Snäll kill (processen kan städa upp)
kill -15 1234
kill 1234  # (samma sak)

# Force kill (omedelbar terminering)
kill -9 1234
kill -SIGKILL 1234  # (samma sak)
```

### 4. Background & Foreground jobs

```bash
# Kör kommando i bakgrunden (lägg till & i slutet)
nmap -sS 192.168.1.0/24 &

# Lista bakgrundsjobb
jobs

# Bring job till foreground
fg %1  # (job nummer 1)

# Pausa pågående kommando
Ctrl + Z

# Fortsätt pausat jobb i bakgrunden
bg %1

# Disown job (fortsätt köra även efter logout)
disown %1
```

**Praktiskt exempel:**

```bash
# 1. Starta långsamt kommando
nmap -p- 192.168.1.1
# Tar lång tid...

# 2. Pausa det (Ctrl+Z)
^Z
[1]+  Stopped                 nmap -p- 192.168.1.1

# 3. Lägg i bakgrunden
bg %1

# 4. Fortsätt arbeta medan det kör
ls
pwd

# 5. Kolla status
jobs

# 6. Återgå till det
fg %1
```

---

## 🔧 System-services

### Vad är services?

**Services** (även kallade daemons) = Program som kör i bakgrunden

Exempel:
- SSH server
- Apache webserver
- MySQL database
- Network Manager

### `systemctl` - Service management

```bash
# Starta service
sudo systemctl start servicename

# Stoppa service
sudo systemctl stop servicename

# Starta om service
sudo systemctl restart servicename

# Reload config (utan att starta om)
sudo systemctl reload servicename

# Kolla status
systemctl status servicename

# Enable service (starta vid boot)
sudo systemctl enable servicename

# Disable service (starta INTE vid boot)
sudo systemctl disable servicename

# Lista alla services
systemctl list-units --type=service

# Lista aktiva services
systemctl list-units --type=service --state=running

# Lista failed services
systemctl --failed
```

**Praktiska exempel:**

```bash
# SSH server
sudo systemctl start ssh
systemctl status ssh
sudo systemctl enable ssh  # Starta vid boot

# Apache webserver
sudo systemctl start apache2
systemctl status apache2

# MySQL
sudo systemctl start mysql
systemctl status mysql

# NetworkManager
systemctl status NetworkManager

# Stop och disable Bluetooth (om du inte använder)
sudo systemctl stop bluetooth
sudo systemctl disable bluetooth
```

### Service status-förklaring

```bash
systemctl status ssh

● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2025-11-17 10:30:15 CET; 2h 15min ago
   │       │         │
   │       │         └──── När den startades
   │       └────────────── Status (running/stopped/failed)
   └────────────────────── Loaded och enabled vid boot?

Main PID: 1234 (sshd)
Tasks: 1 (limit: 4915)
Memory: 2.5M
CGroup: /system.slice/ssh.service
        └─1234 /usr/sbin/sshd -D
```

---

## 👥 Användare och grupper

### User management

```bash
# Aktuell användare
whoami

# Alla inloggade användare
who

# Detaljerad user-info
id

# Lista alla användare (läs /etc/passwd)
cat /etc/passwd

# Skapa ny användare
sudo adduser username

# Ta bort användare
sudo deluser username

# Ändra lösenord
passwd  # Eget lösenord
sudo passwd username  # Någon annans

# Byt till annan användare
su username

# Byt till root
sudo su
# ELLER
sudo -i
```

### Group management

```bash
# Lista användarens grupper
groups

# Lista alla grupper
cat /etc/group

# Skapa grupp
sudo groupadd groupname

# Lägg till användare i grupp
sudo usermod -aG groupname username

# Ta bort från grupp
sudo deluser username groupname
```

### sudo - Superuser Do

```bash
# Kör kommando som root
sudo command

# Kör tidigare kommando som root
sudo !!

# Öppna root shell
sudo -i

# Kör kommando som annan användare
sudo -u username command

# Lista sudo-privileges
sudo -l

# Editera /etc/sudoers (ALDRIG direkt editera!)
sudo visudo
```

---

## 🌐 Nätverk-basics

### 1. `ip` - Modern network tool

```bash
# Visa alla nätverksinterfaces
ip addr
ip a  # (short form)

# Visa routing table
ip route

# Visa link status
ip link

# Sätt interface up/down
sudo ip link set eth0 up
sudo ip link set eth0 down
```

### 2. `ifconfig` - Äldre (men ofta använt)

```bash
# Installera om saknas
sudo apt install net-tools

# Visa alla interfaces
ifconfig

# Visa specifikt interface
ifconfig eth0

# Sätt IP-adress (temporärt)
sudo ifconfig eth0 192.168.1.100
```

### 3. `ping` - Test connectivity

```bash
# Ping Google
ping google.com

# Ping specifikt antal gånger
ping -c 4 google.com

# Ping med specifik storlek
ping -s 1000 google.com
```

### 4. Network info kommandon

```bash
# DNS lookup
nslookup google.com
dig google.com

# Trace route
traceroute google.com

# Network statistics
netstat -tulpn  # Listening ports
ss -tulpn       # Modern variant av netstat

# Show connections
netstat -an | grep ESTABLISHED
```

### 5. `curl` och `wget` - Download from web

```bash
# Fetch webpage
curl https://example.com

# Save to file
curl https://example.com -o output.html

# Follow redirects
curl -L https://example.com

# wget - download file
wget https://example.com/file.zip

# wget - recursive download
wget -r https://example.com/directory/
```

---

## 📊 System-information

### Sys info kommandon

```bash
# Hostname
hostname

# OS info
cat /etc/os-release
lsb_release -a

# Kernel version
uname -r
uname -a  # Alla details

# CPU info
lscpu
cat /proc/cpuinfo

# Memory info
free -h

# Disk usage
df -h

# Disk usage för mappar
du -sh *
du -h --max-depth=1

# PCI devices
lspci

# USB devices
lsusb

# Block devices (disks)
lsblk
```

### Resource monitoring

```bash
# RAM usage
free -h

# Disk space
df -h

# Folder sizes
du -sh /home/kali/*

# System uptime
uptime

# CPU/memory top users
top
htop

# IO statistics
iostat
```

---

## 🧪 Praktiska övningar

### Övning 1: APT package management

```bash
# 1. Uppdatera systemet
sudo apt update

# 2. Sök efter ett paket
apt search htop

# 3. Visa info om paketet
apt show htop

# 4. Installera htop
sudo apt install htop -y

# 5. Verifiera installation
which htop
htop --version

# 6. Kör htop
htop
# (Tryck 'q' för att avsluta)

# 7. Simulate avinstallation (utan att faktiskt göra det)
sudo apt remove --simulate htop

# 8. Faktiskt avinstallera
sudo apt purge htop

# 9. Cleanup
sudo apt autoremove
```

### Övning 2: Process management

```bash
# 1. Starta ett långsamt kommando i bakgrunden
sleep 300 &

# 2. Lista bakgrundsjobb
jobs

# 3. Hitta PID med ps
ps aux | grep sleep

# 4. Kolla process med top
top
# (Tryck 'q' för att avsluta)

# 5. Kill processen med kill
kill %1  # (job nummer)
# ELLER
kill PID  # (använd PID från ps)

# 6. Verifiera att den är borta
jobs
ps aux | grep sleep
```

### Övning 3: Services

```bash
# 1. Kolla SSH service status
systemctl status ssh

# 2. Om stopped - starta den
sudo systemctl start ssh

# 3. Kolla igen
systemctl status ssh

# 4. Enable för autostart vid boot
sudo systemctl enable ssh

# 5. Lista alla active services
systemctl list-units --type=service --state=running | head -20
```

### Övning 4: Nätverk

```bash
# 1. Kolla din IP-adress
ip addr show

# 2. Test connectivity
ping -c 4 8.8.8.8

# 3. DNS lookup
nslookup google.com

# 4. Kolla listening ports
sudo netstat -tulpn | grep LISTEN
# ELLER
sudo ss -tulpn | grep LISTEN

# 5. Trace route till google
traceroute google.com
```

### Övning 5: System info

```bash
# 1. Kolla OS version
cat /etc/os-release

# 2. Kernel version
uname -r

# 3. CPU info
lscpu | head -20

# 4. Memory usage
free -h

# 5. Disk usage
df -h

# 6. Folder sizes i hemkatalog
du -sh ~/*

# 7. System uptime
uptime
```

---

## 🧪 Självtest - Nivå 2C

### Kunskapsfrågor

1. **Vilket kommando uppdaterar paketlistor utan att installera?**
   - A) `sudo apt upgrade`
   - B) `sudo apt update`
   - C) `sudo apt install`
   - D) `sudo apt refresh`

2. **Vad är skillnaden mellan `apt remove` och `apt purge`?**
   - A) Ingen skillnad
   - B) purge tar också bort config-filer
   - C) remove är snabbare
   - D) purge är för system-paket

3. **Hur startar du en service?**
   - A) `sudo service start name`
   - B) `sudo systemctl start name`
   - C) `sudo start name`
   - D) `sudo run name`

4. **Vad gör `kill -9 PID`?**
   - A) Snäll avslutning
   - B) Force kill (omedelbar)
   - C) Pausa process
   - D) Restarta process

5. **Vilket kommando visar din IP-adress?**
   - A) `ip addr` eller `ifconfig`
   - B) `show ip`
   - C) `getip`
   - D) `myip`

6. **Hur kör du kommando i bakgrunden?**
   - A) `command &`
   - B) `bg command`
   - C) `background command`
   - D) `command -bg`

7. **Vad visar `free -h`?**
   - A) Disk usage
   - B) Memory (RAM) usage
   - C) CPU usage
   - D) Free space

8. **Hur ser du alla pågående processer?**
   - A) `ps`
   - B) `ps aux`
   - C) `top`
   - D) Alla ovanstående

9. **Vilket kommando visar disk usage?**
   - A) `df -h`
   - B) `du -h`
   - C) `free -h`
   - D) Både A och B

10. **Hur enable:ar du en service att starta vid boot?**
    - A) `sudo systemctl start service`
    - B) `sudo systemctl enable service`
    - C) `sudo autostart service`
    - D) `sudo boot enable service`

### Praktiska uppgifter

- [ ] **1. Uppdatera systemet**
  ```bash
  sudo apt update && sudo apt upgrade -y
  ```

- [ ] **2. Installera ett paket**
  ```bash
  sudo apt install tree -y
  tree --version
  ```

- [ ] **3. Visa processer och hitta en specifik**
  ```bash
  ps aux | grep bash
  ```

- [ ] **4. Kolla en service status**
  ```bash
  systemctl status ssh
  ```

- [ ] **5. Visa din IP-adress**
  ```bash
  ip addr show
  ```

- [ ] **6. Test network connectivity**
  ```bash
  ping -c 4 google.com
  ```

- [ ] **7. Kolla disk usage**
  ```bash
  df -h
  ```

### Svar

<details>
<summary>Klicka för svar</summary>

**Kunskapsfrågor:**
1. **B** - `sudo apt update`
2. **B** - purge tar också bort config-filer
3. **B** - `sudo systemctl start name`
4. **B** - Force kill (omedelbar terminering)
5. **A** - `ip addr` eller `ifconfig`
6. **A** - `command &`
7. **B** - Memory (RAM) usage
8. **D** - Alla ovanstående (ps, ps aux, top)
9. **D** - Både A (df) och B (du)
10. **B** - `sudo systemctl enable service`

**Scoring:**
- 9-10 rätt: 🏆 Perfekt!
- 7-8 rätt: ✅ Mycket bra!
- 5-6 rätt: 📚 OK förståelse
- <5 rätt: 🔄 Repetera nivån

</details>

---

## 🎓 Sammanfattning Nivå 2 (A+B+C)

### Du har nu lärt dig:

**Nivå 2A - Terminal & Filsystem:**
- ✅ Öppna och använda terminalen
- ✅ Navigera med cd, pwd, ls
- ✅ Förstå Linux filsystem-struktur
- ✅ Använda wildcards
- ✅ Terminal-genvägar (Ctrl+C, Ctrl+R, Tab, etc.)

**Nivå 2B - Kommandon & Texteditors:**
- ✅ Skapa, kopiera, flytta, ta bort filer (touch, cp, mv, rm)
- ✅ Söka filer och innehåll (find, grep)
- ✅ Permissions (chmod, chown)
- ✅ Editera text (Nano och Vim basics)
- ✅ Pipes och redirection (|, >, >>)

**Nivå 2C - Pakethantering & System:**
- ✅ Installera/avinstallera program (APT)
- ✅ Hantera processer (ps, top, kill)
- ✅ Services (systemctl)
- ✅ Nätverk-basics (ip, ping, netstat)
- ✅ System-information (free, df, uname)

### Essential Linux Kommando-lista

**Must-know kommandon:**

```bash
# Navigation
pwd, cd, ls, tree

# Filhantering
touch, mkdir, cp, mv, rm, cat, less, head, tail

# Sökning
find, grep, locate, which

# Permissions
chmod, chown, ls -l

# Editors
nano, vim

# Pakethantering
sudo apt update, sudo apt install, sudo apt remove

# Processer
ps aux, top, htop, kill, killall

# Services
systemctl status/start/stop/enable

# Nätverk
ip addr, ping, curl, wget

# System
free -h, df -h, du -sh, uname -r
```

---

## ✅ Checklista - Redo för Nivå 3?

Innan du går vidare, säkerställ att du:

- [ ] Kan navigera bekvämt i terminalen
- [ ] Förstår Linux filsystem-strukturen
- [ ] Kan manipulera filer och mappar
- [ ] Kan använda Nano för att editera filer
- [ ] Förstår permissions och kan ändra dem
- [ ] Kan installera/avinstallera program med APT
- [ ] Kan se och hantera processer
- [ ] Kan starta/stoppa services
- [ ] Kan kolla nätverks-information
- [ ] Känner dig bekväm med terminal-basics

**🎯 Nästa steg:**

👉 **[Nivå 3 - Reconnaissance Tools](./niva-3-reconnaissance.md)**

Nu börjar det roliga! Vi ska lära oss använda Kali's säkerhetsverktyg, börjande med Nmap!

---

## 📚 Ytterligare resurser

**Linux learning:**
- Linux Journey: https://linuxjourney.com/
- OverTheWire Bandit: https://overthewire.org/wargames/bandit/
- Explainshell: https://explainshell.com/ (förklara kommandon)

**Cheat sheets:**
- Linux Command Cheat Sheet (vi skapar en i resources-sektionen)
- APT Cheat Sheet
- Vim Cheat Sheet

**Practice:**
- Använd Kali dagligen för att bli bekväm
- Gör vanliga uppgifter i terminalen istället för GUI
- Öva tills kommandona känns naturliga

---

**[⬅️ Föregående: Nivå 2B](./niva-2b-kommandon.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 3](./niva-3-reconnaissance.md)**

---

**🎉 GRATTIS! Du har nu klarat Nivå 2!**

Du har solida Linux-grunder och är redo att börja använda penetrationstestning-verktyg!

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│  "The journey of a thousand hacks begins with           │
│   a single command"                                      │
│                                                          │
│  "Resan mot tusen hacks börjar med ett enda kommando"   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```
