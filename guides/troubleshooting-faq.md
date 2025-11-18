# 🔧 Troubleshooting & FAQ

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

## 📚 Innehållsförteckning

1. [Installationsproblem](#installation)
2. [Nätverksproblem](#network)
3. [Verktygs-specifika Problem](#verktyg)
4. [Lab Environment Problem](#lab-environment)
5. [Performance Problem](#performance)
6. [Windows 11 Specifika Problem](#windows-11)
7. [Vanliga FAQ - Learning](#faq-learning)
8. [Vanliga FAQ - Certifieringar](#faq-certifieringar)
9. [Vanliga FAQ - Karriär](#faq-karriar)
10. [Vanliga FAQ - Legal & Etik](#faq-legal)

---

## 💿 Installationsproblem {#installation}

### Problem: VirtualBox Installeras Inte på Windows 11

**Symptom:**
```
Installation failed
Error 1920. Service 'VirtualBox Host-Only Network Provider' failed to start
```

**Lösningar:**

**1. Kör som Administrator:**
```powershell
# Högerklicka VirtualBox installer → Run as Administrator
```

**2. Inaktivera Windows Defender temporärt:**
```
Windows Security → Virus & threat protection → Manage settings →
Real-time protection: OFF (temporarily)

# Install VirtualBox
# Re-enable protection after installation
```

**3. Installera Visual C++ Redistributable:**
```
Ladda ner: https://aka.ms/vs/17/release/vc_redist.x64.exe
Installera → Restart → Försök VirtualBox igen
```

**4. Windows Features:**
```
Control Panel → Programs → Turn Windows features on or off
☐ Hyper-V (uncheck if enabled)
☐ Virtual Machine Platform (uncheck if enabled)
☐ Windows Hypervisor Platform (uncheck if enabled)

Restart → Install VirtualBox
```

---

### Problem: Kali Linux Startar Inte Efter Installation

**Symptom:**
```
Black screen eller "FATAL: No bootable medium found"
```

**Lösningar:**

**1. Kontrollera Boot Order:**
```
VirtualBox → Kali VM → Settings → System → Boot Order
☑ Hard Disk (first)
☑ Optical (second)
☐ Floppy (uncheck)
```

**2. Verifiera VMDK/VDI fil:**
```
VirtualBox → Kali VM → Settings → Storage
Controller: SATA
└─ Hard Disk: Kali-Linux-2024.vdi (should be attached)

If missing: Click + icon → Add → Select .vdi file
```

**3. Enable VT-x/AMD-V i BIOS:**
```
Restart PC → Enter BIOS (F2, Del, F12 - beroende på dator)
Advanced → CPU Configuration → Intel VT-x: Enabled
                              → AMD-V: Enabled
Save & Exit
```

---

### Problem: "VT-x is not available" Error

**Symptom:**
```
Failed to open a session for the virtual machine
VT-x is not available (VERR_VMX_NO_VMX)
```

**Lösningar:**

**1. Enable i BIOS** (se ovan)

**2. Inaktivera Hyper-V (Windows):**
```powershell
# Kör som Administrator i PowerShell
bcdedit /set hypervisorlaunchtype off
Restart-Computer

# After restart, check:
systeminfo | findstr /i "Hyper-V"
# Should show: "A hypervisor has been detected. Features required for Hyper-V will not be displayed."
```

**3. Windows Sandbox/WSL2 Konflikt:**
```
Inaktivera Windows Sandbox och WSL2 temporarily:
dism.exe /online /disable-feature /featurename:Microsoft-Windows-Subsystem-Linux
dism.exe /online /disable-feature /featurename:VirtualMachinePlatform
Restart
```

---

### Problem: Kali Linux Installer Hänger vid "Detecting Network Hardware"

**Lösning:**
```
1. VirtualBox → Kali VM → Settings → Network
2. Adapter 1 → Attached to: NAT (temporarily)
3. Advanced → Adapter Type: Intel PRO/1000 MT Desktop (change från default)
4. OK → Restart installation

Efter installation, ändra tillbaka till Host-Only om önskat
```

---

## 🌐 Nätverksproblem {#network}

### Problem: VM Kan Inte Pinga Varandra

**Symptom:**
```bash
ping 192.168.56.101
# timeout
```

**Diagnostic:**
```bash
# På Kali
ip a
# Kollar om IP är korrekt (192.168.56.X)

# På Metasploitable
ifconfig
# Kollar IP

# Ping gateway
ping 192.168.56.1
# Om detta funkar, men inte ping mellan VMs → firewall issue
```

**Lösningar:**

**1. Verifiera Network Mode:**
```
VirtualBox → Båda VMs → Settings → Network
Adapter 1: Host-only Adapter
Name: vboxnet0 (SAME for both!)
```

**2. Kontrollera Host-Only Network Existerar:**
```
VirtualBox → File → Host Network Manager
Borde se: vboxnet0
IPv4 Address: 192.168.56.1
Subnet Mask: 255.255.255.0

If missing: Create
```

**3. Inaktivera Firewall Temporärt:**

**Kali:**
```bash
sudo ufw status
# If active:
sudo ufw allow from 192.168.56.0/24
# Eller disable helt:
sudo ufw disable
```

**Ubuntu/Metasploitable:**
```bash
sudo iptables -F
sudo iptables -X
```

**4. Restart Networking:**
```bash
# Kali
sudo systemctl restart networking

# Eller restart hela VM
```

---

### Problem: Kali Har Internet, Men VMs Har Inte

**Symptom:**
```bash
# På Kali
ping 8.8.8.8  # Works

# På Metasploitable
ping 8.8.8.8  # Timeout
```

**Förklaring:** Host-Only network har INGEN internet access by design (för säkerhet).

**Lösning (om du behöver internet på target):**

**Option A: Dual Network Adapters**
```
VirtualBox → Metasploitable → Settings → Network

Adapter 1: Host-only Adapter (vboxnet0)
  → För kommunikation med Kali

Adapter 2: NAT
  → För internet access

Enable Network Adapter: ☑ (both)
```

**Option B: NAT Network (alla VMs får internet):**
```
VirtualBox → File → Preferences → Network → NAT Networks
Add new NAT network (name: NATNetwork)

VirtualBox → All VMs → Settings → Network
Adapter 1: NAT Network
Name: NATNetwork
```

**🔴 VARNING:** Ge INTE vulnerable VMs internet access i production! Endast för updates/testing i isolerad miljö.

---

### Problem: "Network Unreachable" Efter Static IP Config

**Symptom:**
```bash
ping 192.168.56.1
# connect: Network is unreachable
```

**Lösning:**
```bash
# Kontrollera /etc/network/interfaces
cat /etc/network/interfaces

# Borde se:
auto eth0
iface eth0 inet static
    address 192.168.56.2
    netmask 255.255.255.0
    network 192.168.56.0
    broadcast 192.168.56.255
    # gateway 192.168.56.1  # NO gateway for host-only!

# Restart network
sudo systemctl restart networking

# OR use ifconfig manually
sudo ifconfig eth0 192.168.56.2 netmask 255.255.255.0 up
```

---

## 🛠️ Verktygs-specifika Problem {#verktyg}

### Nmap Problem

#### Problem: Nmap Scan Tar För Lång Tid

**Symptom:**
```bash
nmap 192.168.56.101
# Hangs for 10+ minutes
```

**Lösningar:**

**1. Specificera Port Range:**
```bash
# Instead of all 65535 ports:
nmap -p 1-1000 192.168.56.101

# Top 100 ports:
nmap --top-ports 100 192.168.56.101
```

**2. Timing Template:**
```bash
# Default är -T3, use -T4 för snabbare:
nmap -T4 192.168.56.101

# Or even -T5 (not recommended for real pentests):
nmap -T5 192.168.56.101
```

**3. Disable Ping:**
```bash
# If host blocking ping:
nmap -Pn 192.168.56.101
```

#### Problem: "You do not have permission to send raw packets"

**Lösning:**
```bash
# Kör med sudo:
sudo nmap -sS 192.168.56.101

# TCP Connect scan (no sudo needed):
nmap -sT 192.168.56.101
```

---

### Metasploit Problem

#### Problem: Metasploit Startar Inte / Database Error

**Symptom:**
```bash
msfconsole
# Error: database.yml connection failed
```

**Lösningar:**

**1. Starta PostgreSQL:**
```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

**2. Initiera MSF Database:**
```bash
sudo msfdb init

# If already exists:
sudo msfdb reinit
```

**3. Verifiera:**
```bash
msfconsole
msf6 > db_status
# [*] Connected to msf (should see this)
```

#### Problem: Exploit Fungerar Inte (No Session Created)

**Diagnostik:**

**1. Kontrollera LHOST är korrekt:**
```bash
msf6 > show options

# LHOST should be YOUR Kali IP, not 0.0.0.0 or 127.0.0.1
set LHOST 192.168.56.2
```

**2. Verifiera Target Är Sårbar:**
```bash
msf6 > check
# [+] Target is vulnerable (good)
# [-] Target is not vulnerable (try different exploit)
```

**3. Network Connectivity:**
```bash
# Ping target först:
ping 192.168.56.101

# Nmap verify port open:
nmap -p 21 192.168.56.101
```

**4. Firewall:**
```bash
# Check Kali firewall not blocking return connection:
sudo ufw status
sudo ufw allow from 192.168.56.0/24
```

---

### Burp Suite Problem

#### Problem: Browser Kan Inte Ansluta Till Burp Proxy

**Symptom:**
```
Firefox: "The proxy server is refusing connections"
```

**Lösningar:**

**1. Verifiera Burp Lyssnar:**
```
Burp Suite → Proxy → Options → Proxy Listeners
127.0.0.1:8080 (should be running, checked)
```

**2. Kontrollera Firefox Proxy Settings:**
```
Firefox → Settings → Network Settings → Manual proxy configuration
HTTP Proxy: 127.0.0.1
Port: 8080
☑ Also use this proxy for HTTPS
```

**3. Test Connection:**
```bash
# I terminal:
curl -x http://127.0.0.1:8080 http://example.com
# Should see request in Burp HTTP history
```

#### Problem: SSL/TLS Errors (Certificate Warnings)

**Lösning:**
```
1. Burp Suite → Proxy → Options → Import / Export CA Certificate
2. Export → Certificate in DER format → Save as burp.cer

3. Firefox → Settings → Privacy & Security → Certificates →
   View Certificates → Authorities → Import → burp.cer

4. ☑ Trust this CA to identify websites
5. OK

Restart Firefox → HTTPS sites should work now
```

---

### John the Ripper / Hashcat Problem

#### Problem: John Inte Installerat / Funkar Inte

**Symptom:**
```bash
john
# command not found
```

**Lösning:**
```bash
# Kali Linux har John pre-installed, men om saknas:
sudo apt update
sudo apt install john

# Verifiera:
john --version
```

#### Problem: Hashcat "No devices found"

**Symptom:**
```bash
hashcat -b
# No devices found/left
```

**Orsak:** VirtualBox har begränsat GPU-access. Hashcat kräver faktisk GPU.

**Lösningar:**

**1. CPU-only Mode (långsam):**
```bash
hashcat -D 1 -m 0 hash.txt wordlist.txt
# -D 1 = CPU only
```

**2. Använd John Istället (fungerar bra i VM):**
```bash
john --wordlist=rockyou.txt hash.txt
```

**3. Host Machine (om tillgänglig):**
```
Installera Hashcat på Windows 11 host (native)
Använd GPU där för max speed
```

---

### Hydra Problem

#### Problem: Hydra "Connection Refused"

**Symptom:**
```bash
hydra -l admin -P passwords.txt ssh://192.168.56.101
# [ERROR] could not connect to ssh://192.168.56.101:22 - connect: Connection refused
```

**Diagnostik:**
```bash
# 1. Verify service running:
nmap -p 22 192.168.56.101
# 22/tcp closed ssh (BAD - service not running)

# 2. Check på target:
sudo systemctl status ssh
# inactive (dead) - service stopped

# Start it:
sudo systemctl start ssh
```

#### Problem: Hydra Account Lockout

**Symptom:**
```bash
hydra -l admin -P rockyou.txt ssh://target
# After ~5 attempts, no more successful connections
```

**Orsak:** Target har account lockout efter X försök.

**Lösning:**
```bash
# Use VERY slow attack:
hydra -l admin -P passwords.txt -t 1 -w 10 ssh://target
# -t 1 = only 1 thread
# -w 10 = 10 seconds between attempts

# Or use password spraying:
hydra -L users.txt -p "Password123" ssh://target
# Many users, one password = less lockout risk
```

---

## 🔬 Lab Environment Problem {#lab-environment}

### Metasploitable Problem

#### Problem: Kan Inte Logga In på Metasploitable

**Credentials:**
```
Username: msfadmin
Password: msfadmin

If inte fungerar:
Username: user
Password: user
```

#### Problem: Metasploitable Ingen IP-adress

**Symptom:**
```bash
ifconfig
# eth0: no IP shown
```

**Lösning:**
```bash
# Manually request IP via DHCP:
sudo dhclient eth0

# Verifiera:
ifconfig eth0
# Should now show 192.168.56.X

# Permanent fix (edit /etc/network/interfaces):
sudo nano /etc/network/interfaces

# Add:
auto eth0
iface eth0 inet dhcp

# Restart networking:
sudo /etc/init.d/networking restart
```

---

### DVWA Problem

#### Problem: DVWA Database Connection Error

**Symptom:**
```
Could not connect to the MySQL database.
```

**Lösningar:**

**1. Verify MySQL Running:**
```bash
sudo systemctl status mysql
# or
sudo systemctl status mariadb

# Start if stopped:
sudo systemctl start mysql
```

**2. Check Credentials i config:**
```bash
cat /var/www/html/dvwa/config/config.inc.php

$_DVWA[ 'db_user' ]     = 'dvwauser';  # Correct?
$_DVWA[ 'db_password' ] = 'dvwapass';  # Correct?
$_DVWA[ 'db_database' ] = 'dvwa';      # Correct?
```

**3. Reset Database:**
```bash
sudo mysql -u root
DROP DATABASE dvwa;
CREATE DATABASE dvwa;
GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwauser'@'localhost' IDENTIFIED BY 'dvwapass';
FLUSH PRIVILEGES;
EXIT;

# Browse to: http://localhost/dvwa/setup.php
# Click "Create / Reset Database"
```

#### Problem: DVWA Security Level Inte Sparas

**Lösning:**
```bash
# Kontrollera PHP sessions directory är writable:
sudo chmod 777 /var/lib/php/sessions

# Restart Apache:
sudo systemctl restart apache2
```

---

## ⚡ Performance Problem {#performance}

### Problem: VM Är Väldigt Långsam

**Lösningar:**

**1. Öka RAM Allocation:**
```
VirtualBox → VM → Settings → System → Base Memory
Kali: 2048 MB minimum (4096 MB recommended)
Metasploitable: 512 MB minimum (1024 MB recommended)

Rule: Not more than 50% of host RAM total
```

**2. Öka CPU Cores:**
```
VirtualBox → VM → Settings → System → Processor
Increase to 2-4 cores (if host har 4+ cores)
```

**3. Enable VT-x/AMD-V och Nested Paging:**
```
VirtualBox → VM → Settings → System → Acceleration
☑ Enable VT-x/AMD-V
☑ Enable Nested Paging
```

**4. SSD vs HDD:**
```
VMs på SSD = MYCKET snabbare än HDD
Move .vdi files till SSD om möjligt
```

**5. Inaktivera 3D Acceleration:**
```
VirtualBox → VM → Settings → Display → 3D Acceleration
☐ Disable (ofta orsakar problem istället för hjälp)
```

**6. Disable Transparency/Effects i Kali:**
```bash
# XFCE (Kali default):
Settings → Window Manager Tweaks → Compositor →
☐ Enable display compositing
```

---

### Problem: VM Fryser / Hänger

**Lösningar:**

**1. Increase Video Memory:**
```
VirtualBox → VM → Settings → Display → Video Memory
Increase to 128 MB
```

**2. Disable Shared Clipboard:**
```
VirtualBox → VM → Settings → General → Advanced
Shared Clipboard: Disabled
Drag'n'Drop: Disabled
```

**3. Check Host Resources:**
```
Windows Task Manager (Ctrl+Shift+Esc)
If CPU/RAM maxed → close other applications
```

---

### Problem: Disk Space Running Out

**Symptom:**
```bash
df -h
# /dev/sda1  20G  19G  0  100% /
```

**Lösningar:**

**1. Clean Package Cache:**
```bash
sudo apt clean
sudo apt autoremove
```

**2. Remove Old Kernels:**
```bash
# List installed kernels:
dpkg --list | grep linux-image

# Remove old (keep current!)
sudo apt remove linux-image-5.10.0-kali1-amd64
# (replace with actual old version)
```

**3. Find Large Files:**
```bash
sudo du -h /home | sort -rh | head -20
# Shows largest 20 dirs/files

# Common culprits:
# ~/.cache (can delete)
# /var/log (old logs)
# /tmp (can clean)
```

**4. Expand Virtual Disk:**
```bash
# Shutdown VM first

# På host (Windows PowerShell):
cd "C:\Program Files\Oracle\VirtualBox"
.\VBoxManage modifyhd "C:\Path\To\Kali.vdi" --resize 40960
# 40960 MB = 40 GB

# Start VM, expand partition inside:
# GParted (GUI) or:
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
```

---

## 🪟 Windows 11 Specifika Problem {#windows-11}

### Problem: VirtualBox och VMware Konflikt

**Symptom:**
```
Cannot start VM
VERR_NEM_VM_CREATE_FAILED
```

**Lösning:**
```powershell
# Disable Hyper-V completely
bcdedit /set hypervisorlaunchtype off

# Disable Memory Integrity:
Windows Security → Device Security → Core isolation → Memory integrity: OFF

# Restart
```

---

### Problem: Windows Defender Blockerar Kali Tools

**Symptom:**
```
Metasploit payloads deleted
Mimikatz.exe removed
```

**Lösning (ENDAST för lab VMs!):**

**1. Exclude VM Folder:**
```
Windows Security → Virus & threat protection →
Manage settings → Exclusions → Add exclusion → Folder →
Select: C:\Users\YourName\VirtualBox VMs\
```

**2. Disable Real-time Protection (temporarily):**
```
Windows Security → Virus & threat protection →
Manage settings → Real-time protection: OFF
```

**🔴 VIKTIGT:** Aktivera igen när du inte använder Kali!

---

### Problem: Windows 11 Home - Hyper-V Conflict

**Symptom:**
```
VT-x is not available even though enabled in BIOS
```

**Orsak:** Windows 11 Home har vissa virtualization features enabled.

**Lösning:**
```powershell
# Disable Device Guard:
bcdedit /set {default} hypervisorlaunchtype off

# Disable all virtualization features:
Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -NoRestart
Disable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart
Disable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -NoRestart

Restart-Computer
```

---

## 📚 Vanliga FAQ - Learning {#faq-learning}

### Q: Hur lång tid tar det att lära sig Kali Linux från nybörjare?

**A:**
- **Grunderna (Nivå 0-2):** 1-2 månader (part-time)
- **Intermediate (Nivå 3-4):** 3-6 månader
- **Advanced (Nivå 5):** 6-12 månader
- **OSCP-ready:** 12-18 månader totalt

**Det beror på:**
- Din befintliga IT-bakgrund
- Tid du kan dedicera (2h/dag vs 8h/dag)
- Hur snabbt du lär dig
- Praktisk övning (viktigt!)

---

### Q: Måste jag kunna programmering?

**A:**
**Nej, inte från början.** Men...

**Grundläggande scripting hjälper enormt:**
- **Bash:** Automation, scripts för pentesting
- **Python:** Custom tools, exploit modification

**Rekommendation:**
1. Börja med denna guide (inga programmeringskrav)
2. Lär basic Bash samtidigt (del av guiden)
3. Lägg till Python efter 3-6 månader
4. Advanced: Go, PowerShell, Ruby

**Resurser:**
- "Automate the Boring Stuff with Python" (gratis online)
- "Black Hat Python"

---

### Q: Vilken ordning ska jag följa guidens nivåer?

**A:**
**ALLTID i ordning:**

```
Nivå 0 → Nivå 1 → Nivå 2 → Nivå 3 → Nivå 4 → Nivå 5

Varje nivå bygger på tidigare kunskaper.
Hoppa INTE över nivåer även om de verkar "basic"!
```

---

### Q: Hur mycket tid ska jag spendera på praktiska övningar vs teori?

**A:**
**Ratio: 70% praktik / 30% teori**

```
Exempel vecka:
├─ 5 timmar: Läsa guider, videor, böcker (30%)
└─ 12 timmar: Hands-on labs, HTB, THM (70%)

"Learning by doing" är KRITISKT för cybersecurity.
```

---

### Q: Behöver jag en stark dator?

**A:**
**Minimum specs:**
- **CPU:** Intel i5 / AMD Ryzen 5 (4 cores)
- **RAM:** 8 GB (16 GB rekommenderat)
- **Storage:** 100 GB free (SSD preferred)
- **GPU:** Inte nödvändigt (men hjälper Hashcat)

**Optimal:**
- CPU: i7 / Ryzen 7 (6-8 cores)
- RAM: 16-32 GB
- Storage: 250 GB+ SSD
- GPU: NVIDIA (för Hashcat)

**Om din dator är svag:**
- Kör endast 1-2 VMs åt gången
- Minska RAM allocation
- Använd cloud VMs (AWS, Azure gratis tiers)

---

### Q: Kan jag lära mig detta själv eller behöver jag kurser?

**A:**
**Du kan absolut lära dig själv!**

**Denna guide + gratis resurser räcker:**
- ✅ Denna guide (komplett)
- ✅ TryHackMe (free tier)
- ✅ HackTheBox (free tier)
- ✅ PortSwigger Academy (helt gratis)
- ✅ YouTube (IppSec, John Hammond)

**Betala för om du vill:**
- OSCP ($1,649) - Worth it!
- TryHackMe Premium ($11/mån) - Nice to have
- HTB VIP ($14/mån) - Good value

**Bootcamps:**
- Dyra ($10k+)
- Inte nödvändigt om du är self-motivated
- Men snabbare om du behöver struktur

---

## 🎓 Vanliga FAQ - Certifieringar {#faq-certifieringar}

### Q: Vilken är den bästa första certifieringen?

**A:**
**För penetration testing:**
1. **eJPT** ($200) - Bästa första praktiska cert
2. **OSCP** ($1,649) - Industry standard, men svår

**För general cybersecurity:**
1. **CompTIA Security+** ($370) - Bred kunskapsbas
2. **eJPT** → **OSCP** path

**Rekommendation:**
```
Start → eJPT (3-6 månader) → OSCP (6-12 månader)
```

---

### Q: Är CEH värt pengarna?

**A:**
**Pros:**
- ✅ HR-vänlig (rekryterare känner till den)
- ✅ DoD 8570 approved (government jobs)
- ✅ International recognition

**Cons:**
- ❌ Dyr ($1,199 exam + $800 kurs)
- ❌ Mest theoretical (multiplechoice)
- ❌ Mindre respekterad av tekniska personer

**Verdict:**
- **Om du vill government/corporate job:** Ja, worth it
- **Om du vill hands-on pentesting role:** Nej, ta OSCP istället
- **Om företaget betalar:** Absolut!

---

### Q: Kan jag klara OSCP utan arbetslivserfarenhet?

**A:**
**Ja!** Många klarar OSCP som första cert.

**Förberedelse:**
1. Slutför denna guide (Nivå 0-5) ✅
2. HackTheBox: 30-50 boxes (TJ Null's list)
3. TryHackMe: Offensive Pentesting path
4. PWK course material (included i OSCP)
5. PWK labs: Root 50+ machines

**Tidslinje:**
- **Med denna guide som grund:** 6-12 månader prep
- **Från noll:** 12-18 månader

**Tips:**
- Bygg stark foundation först (denna guide!)
- Practice enumeration (viktigast!)
- Learn dokumentation (screenshots, commands)

---

### Q: Hur många gånger får jag försöka OSCP exam?

**A:**
**Unlimited försök!**

**Paket:**
- Learn One ($1,649): 90 days lab + 1 exam attempt
- Learn Unlimited ($1,999): 1 år lab + unlimited attempts

**Tips:**
- De flesta klarar på 1-2 försök
- Ge dig själv 90 dagar för första försöket
- Om du failar, lär från misstagen och försök igen

---

## 💼 Vanliga FAQ - Karriär {#faq-karriar}

### Q: Vilken är ingångslönen för junior penetration tester i Sverige?

**A:**
**Stockholm (2024-2025):**
- Junior (0-2 år): **35,000 - 45,000 SEK/mån**
- Mid (2-5 år): **50,000 - 65,000 SEK/mån**

**Övriga Sverige:**
- Junior: **30,000 - 40,000 SEK/mån**
- Mid: **45,000 - 60,000 SEK/mån**

**Faktorer som ökar lön:**
- OSCP certification (+10-15k)
- Programming skills (Python)
- Stockholm location (+10-20%)
- Konsultföretag (ofta högre)

---

### Q: Behöver jag universitetsexamen?

**A:**
**Nej, inte nödvändigt!**

**Cybersecurity är skills-based:**
- ✅ Certifications > Degree
- ✅ Portfolio (GitHub, blog) > Degree
- ✅ Practical experience > Degree

**Men en examen kan:**
- Hjälpa med första jobbet (HR filters)
- Ge bredare kunskapsbas
- Krävas för vissa government jobs

**Alternativ till uni:**
- Yrkeshögskola (cybersecurity programs)
- Self-taught + certifications (denna väg!)
- Bootcamps

**Bottom line:**
OSCP + portfolio > Universitetsexamen utan praktisk erfarenhet

---

### Q: Hur får jag första jobbet utan erfarenhet?

**A:**
**Strategy:**

**1. Bygg Portfolio:**
- ✅ GitHub med tools/scripts
- ✅ Blog med writeups (10+ posts)
- ✅ HackTheBox/THM profile (visa ranking)
- ✅ Bug bounty participation (även duplicates OK)

**2. Certifications:**
- ✅ Minimum: eJPT eller Security+
- ✅ Ideal: OSCP

**3. Networking:**
- ✅ LinkedIn (connect med professionals)
- ✅ Attend meetups (BSides Stockholm)
- ✅ Join Discord communities
- ✅ Twitter (följ och engagera)

**4. Apply Strategic:**
- Konsultföretag (oftare junior roles)
- SOC positions (stepping stone till pentesting)
- Internships
- Freelance (Upwork, Fiverr small gigs)

**5. CV Tips:**
- Lead med certifications
- Showcase portfolio projects
- Quantify achievements ("Rooted 40 HTB machines")

---

### Q: Ska jag börja med SOC analyst eller gå direkt till pentesting?

**A:**
**Depends on din situation:**

**Gå direkt till Pentesting om:**
- ✅ Du har OSCP
- ✅ Strong portfolio
- ✅ Kan bevisa skills
- ✅ OK med längre jobbsök

**Börja med SOC om:**
- ✅ Behöver inkomst snabbt (fler SOC jobs)
- ✅ Vill lära defensive först
- ✅ Osäker på pentesting

**Progression:**
```
SOC L1 (1 år) → SOC L2 (1-2 år) → Pentester
Eller:
SOC L1 (6 mån) → Junior Pentester (med OSCP)
```

**Många pentesters började i SOC!** Det ger väldigt bra foundation.

---

### Q: Kan jag arbeta remote som pentester?

**A:**
**Ja, men...**

**Remote-vänliga roller:**
- ✅ Application security (mest remote-friendly)
- ✅ Bug bounty (fully remote)
- ✅ Konsulter (blandning)
- ✅ Vissa consulting firms (100% remote)

**Mindre remote:**
- ❌ On-site pentests (fysisk access)
- ❌ Red team operations (ofta on-site)

**Tips:**
- Junior roles: Ofta kräver on-site (learning)
- Senior roles: Mer remote flexibility
- Post-COVID: Mer remote än tidigare

**Plattformar:**
- WeWorkRemotely
- Remote.co
- AngelList (startups)

---

## ⚖️ Vanliga FAQ - Legal & Etik {#faq-legal}

### Q: Är det lagligt att lära sig hacking?

**A:**
**JA, helt lagligt!**

**Lagligt:**
- ✅ Lära verktyg och tekniker
- ✅ Testa på EGNA system
- ✅ Lab environments (Metasploitable, DVWA)
- ✅ CTF platforms (HTB, THM)
- ✅ Bug bounty programs (med tillstånd)

**Olagligt:**
- ❌ Testa på system du inte äger
- ❌ Använda tekniker på riktiga targets
- ❌ "Testa säkerheten" utan tillstånd

**Analogi:**
```
Att lära sig låsplockning är lagligt.
Att öppna andras lås utan tillstånd är olagligt.

Samma sak med hacking!
```

---

### Q: Kan jag "testa" min grannes WiFi-säkerhet?

**A:**
**❌ NEJ! ABSOLUT INTE!**

**Detta är BROTT:**
- Dataintrång (BrB 4 kap. 9c §)
- Avlyssning
- Upp till 2 års fängelse

**Även om:**
- "Jag sa ingenting till någon"
- "Jag gjorde ingen skada"
- "Jag ville bara hjälpa"

**Det räknas fortfarande som BROTT.**

**Säkert alternativ:**
- ✅ Testa DITT EGET WiFi
- ✅ Få SKRIFTLIGT tillstånd från granne

---

### Q: Vad är skillnaden mellan White Hat, Grey Hat och Black Hat?

**A:**

| Type | Definition | Legal | Examples |
|------|------------|-------|----------|
| **White Hat** | Etisk hacking med tillstånd | ✅ Legal | Pentesters, security consultants |
| **Grey Hat** | Hacking utan tillstånd, men väl-avsedd | ⚠️ Illegal men "god vilja" | Hittar bug, rapporterar utan tillstånd |
| **Black Hat** | Malicious hacking | ❌ Illegal | Stölder, sabotage, spionage |

**VIKTIGT:**
Även **Grey Hat är olagligt** i Sverige och de flesta länder!

**"God vilja" är INTE ett försvar i domstol.**

---

### Q: Vad händer om jag hittar en sårbarhet när jag "bara kollar"?

**A:**
**Du har redan begått dataintrång om du kollade utan tillstånd.**

**Rätt process:**

**1. Om du OAVSIKTLIGT hittar sårbarhet:**
```
✅ Stoppa omedelbart
✅ Dokumentera (minimal info)
✅ Responsible disclosure till företaget
✅ Ge rimlig tid att fixa (90 dagar standard)
```

**2. Kontakta:**
```
Email: security@company.com
Eller via bug bounty platform
```

**3. ALDRIG:**
```
❌ Fortsätt exploatera
❌ Publicera offentligt direkt
❌ Kräva lösensumma ("bug bounty or I publish")
```

**Exempel:**
```
✅ GOOD: "Hej, jag råkade hitta att er /admin är öppen. Här är detaljer."
❌ BAD: "Jag har hackat er databas och har 1000 kundregister. Betala 10k SEK."
```

---

### Q: Behöver jag VPN när jag använder Kali?

**A:**
**För lab environments: NEJ**

**När du BEHÖVER VPN:**
- Bug bounty hunting (dölj home IP)
- Testing i "gray area"
- Privacy concerns

**När du INTE behöver:**
- ✅ Lokala VMs (helt isolerat)
- ✅ HTB/THM (de förväntar sig pentesting)
- ✅ Authorized pentests

**VPN-providers (ej logging):**
- Mullvad (Swedish, privacy-focused)
- ProtonVPN
- IVPN

**🔴 VIKTIGT:**
VPN gör dig inte "osynlig" eller "över lagen"!
Du kan fortfarande spåras vid seriösa brott.

---

### Q: Kan jag använda Kali Linux på mitt jobb-nätverk?

**A:**
**Fråga ALLTID IT först!**

**Vanliga företagspolicies:**
- ❌ Inga pentesting tools utan Security team approval
- ❌ Inga scanners (kan trigga IDS)
- ❌ Inga packet sniffers

**Även "oskuldsfull" scanning kan:**
- Trigga security alerts
- Orsaka performance issues
- Bryta policy → uppsägning

**Säkert:**
- ✅ Kör Kali hemma
- ✅ Kör på din laptop UTAN företagets nätverk
- ✅ Få explicit tillstånd från IT Security team

---

## 💡 Tips för Bästa Resultat

**Learning:**
1. Följ guiden i ordning
2. Practice > Theory
3. Dokumentera allt
4. Ta breaks (avoid burnout)

**Troubleshooting:**
1. Google error messages
2. Check logs (`/var/log/`)
3. Reddit/Discord communities
4. Stack Overflow

**Karriär:**
1. Build portfolio från dag 1
2. Network aktivt
3. Stay curious
4. Be patient

---

## 🆘 Fortfarande Problem?

**Hjälp-resurser:**

**Discord:**
- TryHackMe Official Discord
- HackTheBox Discord
- InfoSec Prep (OSCP)

**Reddit:**
- r/kalilinux
- r/AskNetsec
- r/HowToHack

**Forums:**
- Kali Linux Forums
- Offensive Security Forums

**YouTube:**
- Sök specifika fel + "fix" eller "solution"
- Många har haft samma problem!

**GitHub:**
- Issues på verktygs repositories
- Security community är helpful!

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**🔧 "Every expert was once a beginner who refused to give up."**
