# 💻 Nivå 1: Installation & Setup

**⏱️ Beräknad tid:** 30-90 minuter (beroende på metod)
**📚 Svårighetsgrad:** ⭐⭐ Nybörjare-Intermediate
**🎯 Förutsättningar:** Nivå 0A & 0B genomförda
**💾 Diskutrymme:** Minimum 40GB ledigt

---

## 📋 Innehåll

1. [Systemkrav](#-systemkrav)
2. [Installationsmetoder - jämförelse](#-installationsmetoder---jämförelse)
3. [Metod 1: VirtualBox (Rekommenderad för nybörjare)](#-metod-1-virtualbox-rekommenderad)
4. [Initial konfiguration](#️-initial-konfiguration)
5. [Systemuppdatering](#-systemuppdatering)
6. [Essential post-install konfiguration](#-essential-post-install-konfiguration)
7. [Installera Guest Additions](#-installera-guest-additions-virtualbox)
8. [Snapshot-strategi](#-snapshot-strategi)
9. [Troubleshooting](#-troubleshooting-vanliga-problem)
10. [Självtest](#-självtest-nivå-1)

**📌 För andra installationsmetoder:**
- [WSL2 Installation](./niva-1-wsl2.md)
- [Dual Boot Installation](./niva-1-dual-boot.md)
- [Live USB](./niva-1-live-usb.md)

---

## 🖥️ Systemkrav

### Minimum-krav (för att köra överhuvudtaget)

| Komponent | Minimum | Kommentar |
|-----------|---------|-----------|
| **Processor (CPU)** | Dual-core 2.0 GHz | Intel VT-x eller AMD-V MÅSTE stödjas |
| **RAM** | 4 GB total | 2GB för Windows + 2GB för Kali VM |
| **Lagring** | 40 GB ledigt | 20GB för Kali + utrymme för snapshots |
| **OS** | Windows 11 | Home eller Pro |
| **Grafik** | Integrerad | Vilken som helst |
| **Nätverk** | WiFi eller Ethernet | Internetanslutning för installation |
| **Display** | 1280x720 | Minimum resolution |

**🔴 VARNING:** Med minimum-krav kommer systemet vara MYCKET långsamt.

### Rekommenderade krav (för bra upplevelse)

| Komponent | Rekommenderat | Varför |
|-----------|---------------|--------|
| **Processor (CPU)** | Quad-core 2.5 GHz+ | VMs är CPU-intensiva |
| **RAM** | 8 GB total | 4GB för Windows + 4GB för Kali |
| **Lagring** | 80 GB ledigt SSD | SSD gör ENORM skillnad för VMs |
| **OS** | Windows 11 Pro | Pro har Hyper-V (alternativ till VirtualBox) |
| **Grafik** | Dedikerad GPU | Bättre för GUI-verktyg som Wireshark |
| **Nätverk** | Ethernet + WiFi | Ethernet för stabilitet, WiFi för wireless testing |

### Optimala krav (för professionellt arbete)

| Komponent | Optimalt | Benefit |
|-----------|----------|---------|
| **Processor (CPU)** | 6+ kärnor, 3.0+ GHz | Köra flera VMs samtidigt |
| **RAM** | 16+ GB | 4-6GB för Kali + Windows + andra VMs |
| **Lagring** | 256+ GB NVMe SSD | Blixtrsnabba VMs och snapshots |
| **OS** | Windows 11 Pro | Hyper-V support |
| **Extern WiFi-adapter** | TP-Link TL-WN722N eller Alfa AWUS036NHA | För wireless pentesting (viktigt!) |

### 🔍 Kontrollera dina systemspecifikationer

**Windows 11 - Kolla specs:**

1. **Processor & RAM:**
   ```
   Tryck: Windows + Pause/Break
   ELLER
   Högerklicka "This PC" → Properties
   ```

2. **Diskutrymme:**
   ```
   Öppna File Explorer → This PC
   Kolla ledigt utrymme på C:
   ```

3. **Virtualization Support:**
   ```powershell
   # Öppna PowerShell som Admin
   systeminfo

   # Leta efter:
   # "Virtualization Enabled In Firmware: Yes"
   ```

**🔴 Om Virtualization är disabled:**

```
FIX: Aktivera i BIOS

1. Starta om datorn
2. Tryck F2, F12, Delete, eller ESC vid boot (varierar per tillverkare)
3. Hitta "Virtualization Technology" (Intel VT-x) eller "SVM Mode" (AMD)
4. Sätt till "Enabled"
5. Save & Exit (F10 vanligtvis)
6. Boota Windows och verifiera igen
```

| Tillverkare | BIOS Key | Var hittar du VT-x/AMD-V |
|-------------|----------|--------------------------|
| **Dell** | F2 | Virtualization Support → Enable Intel VT |
| **HP** | F10 eller ESC | System Configuration → Virtualization Technology |
| **Lenovo** | F1 eller F2 | Security → Virtualization → Enable |
| **ASUS** | F2 eller Delete | Advanced → CPU Configuration → SVM Mode |
| **Acer** | F2 | Main → Virtualization Technology |
| **MSI** | Delete | OC → CPU Features → SVM Mode |

---

## 🔀 Installationsmetoder - jämförelse

### 📊 Detaljerad jämförelsetabell

| Faktor | VirtualBox/VMware ⭐ | WSL2 | Dual Boot | Live USB | Cloud (AWS/Azure) |
|--------|---------------------|------|-----------|----------|-------------------|
| **Svårighetsgrad** | ⭐⭐ Lätt | ⭐⭐ Lätt | ⭐⭐⭐⭐ Avancerat | ⭐ Mycket lätt | ⭐⭐⭐ Intermediate |
| **Installation tid** | 30-60 min | 15-30 min | 60-120 min | 10 min | 20-40 min |
| **Prestanda** | 70-80% | 85-95% | 100% | 60-70% | 90-100% |
| **Säkerhet (isolation)** | ⭐⭐⭐⭐⭐ Perfekt | ⭐⭐⭐⭐ Bra | ⭐⭐⭐ OK | ⭐⭐⭐⭐⭐ Perfekt | ⭐⭐⭐⭐ Bra |
| **Snapshots** | ✅ Ja | ❌ Nej | ❌ Nej | ❌ Nej | ✅ Ja (AMI images) |
| **Portabilitet** | ⭐⭐⭐ Medium | ⭐⭐⭐⭐⭐ Excellent | ⭐ Låg | ⭐⭐⭐⭐⭐ Perfekt | ⭐⭐⭐⭐ Bra |
| **GUI-support** | ✅ Full | ⚠️ Via Win-KeX | ✅ Full | ✅ Full | ⚠️ Via X11/VNC |
| **Wireless testing** | ⚠️ Med USB WiFi-adapter | ❌ Begränsad | ✅ Full | ✅ Full | ❌ Nej |
| **Risk för data-loss** | ✅ Ingen (Windows oskadad) | ✅ Ingen | 🔴 Hög (kan radera Windows!) | ✅ Ingen | ✅ Ingen |
| **Kostnad** | 💰 Gratis | 💰 Gratis | 💰 Gratis | 💰 $5-10 för USB | 💰💰 $20-100/mån |
| **Bäst för** | Lärande, övning | CLI-arbete, integration | Daglig användning | Testning, recovery | Team collaboration |
| **Windows-integration** | ⭐⭐⭐ Medium | ⭐⭐⭐⭐⭐ Perfekt | ❌ Ingen | ❌ Ingen | ⭐⭐ Låg |
| **Diskutrymme** | 40-60 GB | 20-30 GB | 40-60 GB | 0 GB (persistent USB) | Beroende på plan |
| **Nybörjarvänligt** | ⭐⭐⭐⭐⭐ Ja | ⭐⭐⭐⭐ Ja | ⭐⭐ Nej | ⭐⭐⭐⭐ Ja | ⭐⭐⭐ OK |

### 🎯 Vilken metod ska DU välja?

```
┌──────────────────────────────────────────────────────────┐
│  BESLUTSSTÖD: Välj installationsmetod                   │
└──────────────────────────────────────────────────────────┘

❓ Är du TOTAL nybörjare till Linux?
   └─ JA → VirtualBox ⭐⭐⭐⭐⭐

❓ Vill du främst använda CLI (command-line)?
   └─ JA → WSL2 ⭐⭐⭐⭐⭐

❓ Vill du testa wireless hacking (WiFi cracking)?
   └─ JA → Dual Boot ELLER VirtualBox med USB WiFi-adapter

❓ Har du bara 1 dator och vill inte riskera data?
   └─ JA → VirtualBox ⭐⭐⭐⭐⭐

❓ Vill du använda Kali som ditt huvudsakliga OS?
   └─ JA → Dual Boot (men INTE rekommenderat för nybörjare)

❓ Vill du testa Kali utan installation?
   └─ JA → Live USB ⭐⭐⭐⭐

❓ Behöver du samarbeta med team remote?
   └─ JA → Cloud (AWS/Azure)

❓ Har du <4GB RAM?
   └─ JA → WSL2 ELLER Live USB (VirtualBox kommer vara för långsam)

❓ Studerar du till OSCP eller liknande?
   └─ JA → VirtualBox ⭐⭐⭐⭐⭐ (samma miljö som OSCP-exam)
```

### 🏆 Rekommendation för denna guide

**För 90% av användare: VirtualBox**

**Varför?**
- ✅ Säkert (Windows påverkas inte)
- ✅ Snapshots (kan ångra misstag)
- ✅ Industry standard (OSCP exam använder VM)
- ✅ Full GUI-support
- ✅ Lätt att ta bort om du ångrar dig
- ✅ Kan köra flera Kali-instanser
- ✅ Nybörjarvänligt

**Näst bäst: WSL2** (för CLI-fokuserade användare)

---

## 🖥️ Metod 1: VirtualBox (Rekommenderad)

### Steg 1: Ladda ner nödvändiga filer

#### 1.1 - Ladda ner VirtualBox

**URL:** https://www.virtualbox.org/wiki/Downloads

```
┌──────────────────────────────────────────────────────────┐
│  LADDA NER VIRTUALBOX 7.0+                               │
└──────────────────────────────────────────────────────────┘

1. Gå till: https://www.virtualbox.org/wiki/Downloads
2. Klicka: "Windows hosts" (den stora blåa länken)
3. Spara filen: VirtualBox-7.0.x-Win.exe
4. Filstorlek: ~100-120 MB
```

**🟢 TIP:** Ladda också ner "Extension Pack" för USB 2.0/3.0-support:
- Samma sida → "VirtualBox 7.0.x Oracle VM VirtualBox Extension Pack"
- Behövs för USB WiFi-adapters!

#### 1.2 - Ladda ner Kali Linux

**URL:** https://www.kali.org/get-kali/

**Två alternativ:**

**ALTERNATIV A: Pre-built VM (Rekommenderad - enklast)**
```
1. Gå till: https://www.kali.org/get-kali/#kali-virtual-machines
2. Välj: "VirtualBox" (64-bit)
3. Ladda ner: kali-linux-2025.x-virtualbox-amd64.7z
4. Filstorlek: ~3-4 GB
5. Verktyg för uppackning: 7-Zip (https://www.7-zip.org/)
```

**ALTERNATIV B: ISO för custom installation**
```
1. Gå till: https://www.kali.org/get-kali/#kali-installer-images
2. Välj: "Installer Images" → 64-bit
3. Ladda ner: kali-linux-2025.x-installer-amd64.iso
4. Filstorlek: ~3-4 GB
5. Längre installation men mer kontroll
```

**🎯 Rekommendation:** Använd **ALTERNATIV A (Pre-built VM)** - mycket enklare för nybörjare!

### Steg 2: Installera VirtualBox

```
┌──────────────────────────────────────────────────────────┐
│  INSTALLATION AV VIRTUALBOX                              │
└──────────────────────────────────────────────────────────┘

1. Kör VirtualBox-7.0.x-Win.exe (högerklicka → Run as Administrator)

2. Installation wizard:
   ├─ Welcome → Next
   ├─ Custom Setup → Lämna allt standard → Next
   ├─ Warning om network interfaces (kommer att disconnecta kort)
   │  → Klicka Yes
   ├─ Ready to Install → Install
   └─ Wait ~2-3 minuter

3. Vid "Missing Dependencies Python Core / win32api":
   → Klicka Yes (installeras automatiskt)

4. Finish → Starta INTE VirtualBox ännu
```

### Steg 3: Installera Extension Pack

```
1. Dubbelklicka på: Oracle_VM_VirtualBox_Extension_Pack-7.0.x.vbox-extpack
2. VirtualBox öppnas automatiskt
3. Install → Scroll ner → I Agree
4. Ange admin-lösenord (om ombedd)
5. OK
```

**🟢 Varför behövs Extension Pack?**
- USB 2.0 och 3.0-support (viktigt för USB WiFi-adapters)
- PXE boot support
- Bättre prestanda för vissa operationer

### Steg 4A: Importera Pre-built VM (Enklast - Rekommenderad)

Om du laddade ner Pre-built VM (ALTERNATIV A):

```
┌──────────────────────────────────────────────────────────┐
│  IMPORTERA KALI LINUX VM                                 │
└──────────────────────────────────────────────────────────┘

1. Packa upp .7z-filen:
   ├─ Högerklicka på kali-linux-2025.x-virtualbox-amd64.7z
   ├─ 7-Zip → Extract Here
   └─ Vänta ~5 minuter (stor fil)

2. Du får en .vbox-fil (Kali-Linux-2025.x-virtualbox-amd64.vbox)

3. Öppna VirtualBox

4. File → Import Appliance (Ctrl+I)

5. Välj den uppackade .vbox-filen

6. Appliance settings:
   ┌─────────────────────────────────────────────────┐
   │ Name: Kali-Linux-2025                           │
   │ Guest OS Type: Debian (64-bit)                  │
   │ CPU: 2 (eller fler om du har)                   │
   │ RAM: 2048 MB (ändra till 4096 om du har 8GB+)  │
   │ Storage: ~80GB (dynamiskt allokerad)            │
   └─────────────────────────────────────────────────┘

7. Import → Vänta 2-5 minuter

8. Kali Linux dyker upp i listan! ✅
```

**Default credentials för Pre-built VM:**
```
Username: kali
Password: kali
```

**🟡 VIKTIGT:** Byt lösenord direkt efter första login! (Instruktioner nedan)

### Steg 4B: Skapa VM från ISO (Alternativ - mer kontroll)

Om du laddade ner ISO (ALTERNATIV B):

```
┌──────────────────────────────────────────────────────────┐
│  SKAPA NY VIRTUELL MASKIN                                │
└──────────────────────────────────────────────────────────┘

1. VirtualBox → New (Ctrl+N)

2. Name and Operating System:
   ├─ Name: Kali-Linux-2025
   ├─ Type: Linux
   ├─ Version: Debian (64-bit)
   └─ Next

3. Memory (RAM):
   ├─ 2048 MB minimum
   ├─ 4096 MB rekommenderat (om du har 8GB+ total RAM)
   └─ Next

4. Hard disk:
   ├─ Create a virtual hard disk now
   └─ Create

5. Hard disk file type:
   ├─ VDI (VirtualBox Disk Image)
   └─ Next

6. Storage on physical hard disk:
   ├─ Dynamically allocated (växer efter behov)
   └─ Next

7. File location and size:
   ├─ Location: Standard (C:\Users\[You]\VirtualBox VMs\Kali-Linux-2025)
   ├─ Size: 80 GB (kommer inte ta 80GB direkt, växer dynamiskt)
   └─ Create

8. VM är skapad! Men behöver konfigureras innan installation.
```

#### 4B.2 - Konfigurera VM settings (före installation)

```
1. Högerklicka Kali-Linux-2025 → Settings

2. System:
   ├─ Motherboard:
   │  ├─ Base Memory: 4096 MB (om möjligt)
   │  └─ Boot Order: Optical, Hard Disk (avmarkera Floppy)
   ├─ Processor:
   │  ├─ Processors: 2 (eller fler om du har 4+ kärnor)
   │  └─ Enable PAE/NX: ✅ Checked
   └─ Acceleration:
      └─ Paravirtualization Interface: Default

3. Display:
   ├─ Screen:
   │  ├─ Video Memory: 128 MB
   │  ├─ Graphics Controller: VMSVGA
   │  └─ Enable 3D Acceleration: ✅ Checked (optional)

4. Storage:
   ├─ Controller: IDE → Empty (CD icon)
   ├─ Attributes → Optical Drive → Click CD icon
   ├─ Choose a disk file...
   └─ Välj kali-linux-2025.x-installer-amd64.iso

5. Network:
   ├─ Adapter 1:
   │  ├─ Enable Network Adapter: ✅ Checked
   │  ├─ Attached to: NAT (default, fungerar bra)
   │  └─ Advanced → Adapter Type: Intel PRO/1000 MT Desktop
   │
   └─ För advanced networking (senare):
      Adapter 2 kan sättas till "Host-only" eller "Bridged"

6. USB:
   ├─ Enable USB Controller: ✅ Checked
   └─ USB 3.0 (xHCI) Controller (kräver Extension Pack)

7. Shared Folders (optional - kan sättas senare):
   └─ Lägg till för att dela filer mellan Windows och Kali

8. OK → Stäng Settings
```

#### 4B.3 - Installera Kali från ISO

```
┌──────────────────────────────────────────────────────────┐
│  KALI LINUX INSTALLATION                                 │
└──────────────────────────────────────────────────────────┘

1. Starta VM:
   ├─ Dubbelklicka Kali-Linux-2025
   └─ Eller: Högerklicka → Start → Normal Start

2. Boot menu dyker upp:
   ├─ Välj: "Graphical install" (använd piltangenter)
   └─ Enter

3. Select a language:
   └─ English (eller Svenska om du föredrar)

4. Select your location:
   └─ Sweden (för timezone)

5. Configure keyboard:
   └─ Swedish (eller din layout)

6. Configure the network:
   ├─ Hostname: kali (eller valfritt namn)
   └─ Domain name: (lämna tomt om du inte vet)

7. Set up users and passwords:
   ├─ Full name: Ditt namn
   ├─ Username: kali (rekommenderat)
   ├─ Password: [Välj starkt lösenord]
   └─ Re-enter password

   🔴 VIKTIGT: Kom ihåg detta lösenord!

8. Configure the clock:
   └─ Stockholm (för Sverige)

9. Partition disks:
   ├─ Välj: "Guided - use entire disk"
   ├─ Select disk: SCSI3 (0,0,0) (sda) - 80.0 GB
   ├─ Partitioning scheme: "All files in one partition"
   └─ Finish partitioning → Yes

10. Configure the package manager:
    ├─ Use a network mirror: Yes
    ├─ HTTP proxy: (lämna tomt)
    └─ Wait for package lists to download

11. Install the GRUB boot loader:
    ├─ Install GRUB: Yes
    └─ Device: /dev/sda

12. Finish the installation:
    └─ Continue → VM startar om

13. Ta bort ISO:
    ├─ Devices → Optical Drives → Remove disk from virtual drive
    └─ Force unmount (om ombedd)

14. VM startar om → Kali boot screen → Login!
```

### Steg 5: Första boot och login

```
┌──────────────────────────────────────────────────────────┐
│  FÖRSTA LOGIN                                            │
└──────────────────────────────────────────────────────────┘

1. Kali boot screen visas
2. Vänta ~30 sekunder
3. Login screen dyker upp

4. Login:
   Username: kali
   Password: [ditt lösenord] (eller "kali" för pre-built VM)

5. Enter → Välkommen till Kali Linux! 🐉

6. Desktop environment (standard: Xfce) laddas
```

**🎉 GRATTIS! Du har nu Kali Linux igång!**

---

## ⚙️ Initial konfiguration

### 1. Byt lösenord (om du använde pre-built VM)

```bash
# Öppna terminal (Applications → Terminal eller Ctrl+Alt+T)
passwd

# Ange nuvarande lösenord: kali
# Ange nytt lösenord: [ditt starka lösenord]
# Bekräfta: [samma lösenord igen]
```

**🟡 Skapa ett STARKT lösenord:**
- Minst 12 tecken
- Blanda stora/små bokstäver, siffror, symboler
- Exempel: `K4li!Secur3_2025`

### 2. Kontrollera nätverksanslutning

```bash
# Testa internet
ping -c 4 google.com

# Förväntat resultat:
# 64 bytes from google.com (142.250.74.46): icmp_seq=1 ttl=115 time=15.2 ms
# ...
# 4 packets transmitted, 4 received, 0% packet loss
```

**❌ Om det inte fungerar:**

```bash
# Kontrollera nätverksinterface
ip a

# Du ska se:
# 1: lo: <LOOPBACK...> (localhost)
# 2: eth0: <BROADCAST...> (ditt nätverkskort)
#    inet 10.0.2.15/24 (eller liknande IP)

# Om eth0 inte har IP:
sudo dhclient eth0

# Testa igen:
ping -c 4 google.com
```

**🟢 Alternativ lösning (om DHCP inte fungerar):**
1. VirtualBox VM → Settings → Network
2. Adapter 1 → Attached to: NAT
3. Advanced → Adapter Type: Intel PRO/1000 MT Desktop
4. OK → Restart VM

### 3. Ändra tangentbordslayout (om behövs)

```bash
# Lista tillgängliga layouts
localectl list-keymaps | grep sv

# Sätt till svensk layout
sudo localectl set-keymap sv

# Verifiera
localectl status
```

**Grafiskt sätt:**
```
Applications → Settings → Keyboard
→ Layout tab → Add → Swedish → OK
```

---

## 🔄 Systemuppdatering

**🔴 VIKTIGT:** Uppdatera ALLTID systemet direkt efter installation!

### Uppdatera paketlistor och installera uppdateringar

```bash
# 1. Uppdatera paketlistor
sudo apt update

# Output kommer visa:
# Hit:1 http://kali.download/kali kali-rolling InRelease
# Reading package lists... Done
# Building dependency tree... Done
# X packages can be upgraded. Run 'apt list --upgradable' to see them.

# 2. Se vad som kan uppdateras (optional)
apt list --upgradable

# 3. Uppgradera alla paket
sudo apt upgrade -y

# Vänta 5-15 minuter beroende på internethastighe

# 4. Full-upgrade (för kernel och major updates)
sudo apt full-upgrade -y

# 5. Ta bort gamla paket
sudo apt autoremove -y

# 6. Rensa cache
sudo apt clean
```

**🟢 TIP:** Kombinera alla kommandon:

```bash
sudo apt update && sudo apt upgrade -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean
```

### Verifiera installerade verktyg

```bash
# Kontrollera Kali-version
cat /etc/os-release

# Du ska se:
# NAME="Kali GNU/Linux"
# VERSION="2025.x"
# ID=kali
# ...

# Kontrollera kernel-version
uname -r

# Exempel output:
# 6.5.0-kali3-amd64

# Lista några viktiga verktyg
which nmap metasploit-framework burpsuite
```

---

## 🔧 Essential post-install konfiguration

### 1. Installera vanliga verktyg (om de saknas)

```bash
# Några verktyg som ofta används
sudo apt install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    net-tools \
    build-essential \
    python3-pip \
    terminator

# Förklaring:
# curl/wget - Ladda ner filer
# git - Version control
# vim/nano - Text editors
# net-tools - Nätverksverktyg (ifconfig, etc.)
# build-essential - Kompileringsverktyg
# python3-pip - Python package manager
# terminator - Bättre terminal emulator
```

### 2. Konfigurera terminalen (optional men rekommenderat)

**Installera Oh-My-Zsh för bättre shell:**

```bash
# Installera Zsh (om inte redan installerat)
sudo apt install -y zsh

# Installera Oh-My-Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Sätt Zsh som default shell
chsh -s $(which zsh)

# Logga ut och in igen för att aktivera
```

**Konfigurera Zsh-tema:**

```bash
# Editera Zsh-config
nano ~/.zshrc

# Hitta raden: ZSH_THEME="robbyrussell"
# Ändra till: ZSH_THEME="agnoster" (eller "powerlevel10k" för advanced)

# Spara (Ctrl+O, Enter, Ctrl+X)

# Ladda om config
source ~/.zshrc
```

### 3. Installera vanliga browser (Chrome eller Firefox ESR)

```bash
# Firefox ESR (rekommenderad för pentesting)
sudo apt install -y firefox-esr

# ELLER Google Chrome:
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
```

### 4. Konfigurera shared clipboard (mellan Windows och Kali)

```bash
# Installera VirtualBox Guest Additions (se nästa sektion)
# Då får du automatiskt shared clipboard

# Alternativt: Installera clipboard-verktyg
sudo apt install -y xclip

# Använd xclip för copy-paste mellan Windows och Kali
```

---

## 📦 Installera Guest Additions (VirtualBox)

**Vad är Guest Additions?**
- Shared clipboard (copy-paste mellan Windows och Kali)
- Shared folders
- Bättre skärmupplösning (auto-resize)
- Bättre muspekare
- Drag-and-drop filer

### Installation

```bash
# 1. I VirtualBox-menyn:
# Devices → Insert Guest Additions CD image...

# 2. I Kali terminal:
sudo apt update
sudo apt install -y build-essential dkms linux-headers-$(uname -r)

# 3. Montera CD:
sudo mkdir -p /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom

# 4. Kör installation:
cd /mnt/cdrom
sudo ./VBoxLinuxAdditions.run

# 5. Vänta på installation (2-5 min)

# 6. Starta om:
sudo reboot

# 7. Efter omstart - verifiera:
lsmod | grep vbox

# Du ska se:
# vboxguest
# vboxsf
# vboxvideo
```

### Aktivera shared clipboard och drag-and-drop

```
1. Stäng av Kali VM

2. VirtualBox → Högerklicka Kali → Settings

3. General → Advanced:
   ├─ Shared Clipboard: Bidirectional
   └─ Drag'n'Drop: Bidirectional

4. OK

5. Starta VM igen

6. Testa: Kopiera text i Windows → Paste i Kali (Ctrl+Shift+V i terminal)
```

### Sätta upp Shared Folder

```
1. VirtualBox → Kali VM Settings → Shared Folders

2. Klicka "+" (Add new shared folder)

3. Folder Path: Browse → Välj Windows-mapp (t.ex. C:\Users\[You]\Documents\KaliShared)

4. Folder Name: shared (eller valfritt)

5. ✅ Auto-mount
   ✅ Make Permanent

6. OK

7. I Kali:
sudo usermod -aG vboxsf $USER

8. Logga ut och in igen

9. Access shared folder:
cd /media/sf_shared
ls

# Nu kan du flytta filer mellan Windows och Kali!
```

---

## 💾 Snapshot-strategi

**Vad är Snapshots?**
- "Sparningspunkter" som du kan återgå till
- Om något går fel → restore snapshot → tillbaka till fungerande state

### Viktiga snapshots att ta

```
┌──────────────────────────────────────────────────────────┐
│  REKOMMENDERAD SNAPSHOT-STRATEGI                         │
└──────────────────────────────────────────────────────────┘

📸 Snapshot 1: "Fresh Install"
   När: Direkt efter installation
   Varför: Om något går helt fel, börja om från grunden

📸 Snapshot 2: "Fully Updated"
   När: Efter apt update && upgrade
   Varför: Efter första uppdateringen - bra startpunkt

📸 Snapshot 3: "Guest Additions Installed"
   När: Efter Guest Additions installation
   Varför: Innan du börjar anpassa systemet

📸 Snapshot 4: "Configured and Ready"
   När: Efter all initial konfiguration (tools, zsh, etc.)
   Varför: Din "arbetsredo" baseline

📸 Snapshot X: "Before Risky Operation"
   När: Innan du gör något potentiellt farligt
   Exempel: Innan du installerar experimental tools
```

### Hur ta snapshot

```
METOD 1: Via VirtualBox GUI (VM måste vara avstängd eller Running)

1. Stäng Kali eller kör den
2. VirtualBox → Välj Kali VM
3. Hamburger menu (☰) eller Machine → Take Snapshot
4. Name: "Fully Updated - 2025-11-17"
5. Description: "After initial apt upgrade, guest additions installed"
6. OK

Snapshot är tagen! (tar ~30 sekunder)

METOD 2: Via kommandorad (Windows)

# Lista VMs:
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" list vms

# Ta snapshot:
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" snapshot "Kali-Linux-2025" take "Snapshot Name" --description "Description"
```

### Återställa från snapshot

```
1. Stäng av Kali VM (om den kör)

2. VirtualBox → Välj Kali VM

3. Hamburger menu (☰) → Snapshots

4. Välj snapshot du vill återställa till

5. Restore

6. ⚠️ Varning: "This will discard current state"
   → Klicka Restore

7. Starta VM → Du är tillbaka vid snapshot-punkten!
```

**🟡 VIKTIGT:**
- Snapshots tar diskutrymme (10-30GB per snapshot)
- Ta inte för många (max 5-10)
- Ta bort gamla snapshots du inte behöver längre

---

## 🆘 Troubleshooting vanliga problem

### Problem 1: "VT-x is not available"

**Error:**
```
VT-x/AMD-V hardware acceleration is not available on your system.
```

**Lösning:**
```
1. Starta om datorn
2. Gå in i BIOS (F2, F12, Delete - varierar)
3. Hitta "Virtualization Technology" (Intel VT-x) eller "SVM Mode" (AMD)
4. Sätt till Enabled
5. Save & Exit
6. Försök igen
```

**Om det fortfarande inte fungerar:**
- Kontrollera att Hyper-V är disabled i Windows:
  ```
  Windows Features → Uncheck "Hyper-V"
  Restart
  ```

### Problem 2: VM är extremt långsam

**Lösningar:**

```
✅ Fix 1: Öka RAM
   VirtualBox → Settings → System → Base Memory → 4096 MB

✅ Fix 2: Öka CPU cores
   Settings → System → Processor → 2 (eller fler)

✅ Fix 3: Enable 3D Acceleration
   Settings → Display → Enable 3D Acceleration

✅ Fix 4: Använd SSD istället för HDD
   Flytta .vdi-filen till SSD

✅ Fix 5: Disable unneeded services i Kali
   sudo systemctl disable bluetooth
   sudo systemctl disable cups (printing)
```

### Problem 3: Inget internet i Kali

**Diagnos:**

```bash
# 1. Kontrollera nätverksinterface
ip a

# 2. Testa ping:
ping -c 4 8.8.8.8  # Google DNS

# 3. Testa DNS:
ping -c 4 google.com
```

**Lösningar:**

```
✅ Fix 1: Restart networking
   sudo systemctl restart NetworkManager

✅ Fix 2: DHCP renewal
   sudo dhclient -r
   sudo dhclient eth0

✅ Fix 3: Ändra network adapter type
   VirtualBox Settings → Network → Advanced
   → Adapter Type: Intel PRO/1000 MT Desktop

✅ Fix 4: Använd Bridged Adapter istället för NAT
   Settings → Network → Attached to: Bridged Adapter
```

### Problem 4: Shared clipboard fungerar inte

```
✅ Fix 1: Installera Guest Additions (se ovan)

✅ Fix 2: Kontrollera Settings
   VM Settings → General → Advanced
   → Shared Clipboard: Bidirectional

✅ Fix 3: Restart VBoxClient
   killall VBoxClient
   VBoxClient --clipboard
   VBoxClient --draganddrop

✅ Fix 4: Använd Ctrl+Shift+V i Kali terminal
   (Inte bara Ctrl+V)
```

### Problem 5: Skärmen är för liten / inte auto-resize

```
✅ Fix 1: Installera Guest Additions

✅ Fix 2: Enable 3D Acceleration
   Settings → Display → Enable 3D Acceleration

✅ Fix 3: Öka Video Memory
   Settings → Display → Video Memory: 128 MB

✅ Fix 4: Manuellt sätta resolution
   Applications → Settings → Display
   → Välj högre resolution
```

### Problem 6: "Not enough space" vid installation

```
✅ Fix 1: Öka disk size INNAN du startar installation
   VirtualBox → Settings → Storage → [Disk]
   → Attributes → Size → Öka till minst 80GB

✅ Fix 2: Rensa Windows disk space
   Windows: Disk Cleanup → Clean system files

✅ Fix 3: Flytta VM till annan disk med mer utrymme
   Settings → General → Advanced → Default Machine Folder
```

---

## 🧪 Självtest - Nivå 1

### Praktiska uppgifter

Verifiera att din installation fungerar:

- [ ] **1. Kan du starta Kali VM utan fel?**

- [ ] **2. Kan du logga in med ditt lösenord?**

- [ ] **3. Har du internet?**
  ```bash
  ping -c 4 google.com
  ```

- [ ] **4. Är systemet uppdaterat?**
  ```bash
  sudo apt update
  sudo apt list --upgradable
  # Ska visa "All packages are up to date" eller liknande
  ```

- [ ] **5. Fungerar shared clipboard?**
  - Kopiera text i Windows
  - Paste i Kali terminal (Ctrl+Shift+V)

- [ ] **6. Har du tagit minst en snapshot?**
  - VirtualBox → Snapshots → Se att minst 1 snapshot finns

- [ ] **7. Kan du öppna terminalen?**
  - Ctrl+Alt+T eller Applications → Terminal

- [ ] **8. Fungerar några grundläggande verktyg?**
  ```bash
  nmap --version
  metasploit-framework --version
  wireshark --version
  ```

### Kunskapsfrågor

1. **Vad är den rekommenderade installationsmetoden för nybörjare?**
   - A) Dual Boot
   - B) VirtualBox
   - C) Live USB
   - D) Cloud

2. **Vad är minimum RAM-krav för att köra Kali i VM?**
   - A) 1 GB
   - B) 2 GB
   - C) 4 GB total (2GB för VM)
   - D) 8 GB

3. **Vad är Guest Additions?**
   - A) Extra säkerhetsverktyg
   - B) VirtualBox-tillägg för shared clipboard, bättre grafik, etc.
   - C) Ett antivirus
   - D) En type av snapshot

4. **Varför ska du ta snapshots?**
   - A) För att spara diskutrymme
   - B) För att kunna återställa VM till tidigare state
   - C) För att göra VM snabbare
   - D) För att dela VM med andra

5. **Vad är första kommandot du ska köra efter installation?**
   - A) `sudo apt install nmap`
   - B) `sudo apt update`
   - C) `sudo reboot`
   - D) `passwd`

### Svar

<details>
<summary>Klicka för svar</summary>

**Praktiska uppgifter:** Alla ska vara ✅ checked!

**Kunskapsfrågor:**
1. **B** - VirtualBox (säkert, snapshots, nybörjarvänligt)
2. **C** - 4 GB total (2GB för Windows + 2GB för Kali VM minimum)
3. **B** - VirtualBox-tillägg för shared clipboard, bättre grafik, shared folders
4. **B** - För att kunna återställa VM till tidigare state om något går fel
5. **B** - `sudo apt update` (uppdatera paketlistor först!)

**Scoring:**
- Alla praktiska + 5/5 teoretiska: 🏆 Perfekt - du är redo!
- Alla praktiska + 3-4/5: ✅ Bra - fortsätt
- <3 teoretiska ELLER praktiska problem: 🔄 Gå igenom installation igen

</details>

---

## ✅ Checklista - Redo för Nivå 2?

Innan du går vidare, säkerställ att:

- [ ] Kali Linux är installerad och startar utan problem
- [ ] Du kan logga in
- [ ] Internet fungerar
- [ ] Systemet är fullt uppdaterat (`sudo apt update && sudo apt upgrade`)
- [ ] Guest Additions är installerat (för VirtualBox-användare)
- [ ] Du har tagit minst en snapshot ("Fully Updated" eller liknande)
- [ ] Shared clipboard fungerar (om du vill ha det)
- [ ] Du känner dig bekväm med att starta/stoppa VM
- [ ] Du vet hur du återställer från snapshot vid behov

**🎯 Nästa steg:**

👉 **[Nivå 2 - Linux-grunderna via Kali](./niva-2-linux-grunder.md)**

Nu ska vi lära oss Linux-basics: terminal, kommandon, filsystem!

---

## 📚 Ytterligare resurser

**För andra installationsmetoder:**
- [WSL2 Installation Guide](./niva-1-wsl2.md)
- [Dual Boot Installation Guide](./niva-1-dual-boot.md)
- [Live USB Creation Guide](./niva-1-live-usb.md)

**Officiell dokumentation:**
- Kali Docs: https://www.kali.org/docs/
- VirtualBox Manual: https://www.virtualbox.org/manual/

**Video tutorials (komplement):**
- NetworkChuck - "you need to learn Kali Linux RIGHT NOW!!"
- HackerSploit - "Kali Linux Installation Guide"

---

**[⬅️ Föregående: Nivå 0B](./niva-0b-legalitet.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 2](./niva-2-linux-grunder.md)**
