# VirtualBox Manual - Svenska

## Innehållsförteckning
1. [Introduktion](#introduktion)
2. [Installation och Grundinställningar](#installation-och-grundinställningar)
3. [Skapa en Virtuell Maskin](#skapa-en-virtuell-maskin)
4. [Vanligaste Inställningar](#vanligaste-inställningar)
5. [Optimala Inställningar för Kali Linux på Kraftfull Hårdvara](#optimala-inställningar-för-kali-linux-på-kraftfull-hårdvara)
6. [Nätverksinställningar - Detaljerad Guide](#nätverksinställningar---detaljerad-guide)
7. [Anonym Användning med Nätverksåtkomst](#anonym-användning-med-nätverksåtkomst)
8. [Tips och Troubleshooting](#tips-och-troubleshooting)

---

## Introduktion

VirtualBox är ett kostnadsfritt virtualiseringsprogram som låter dig köra flera operativsystem samtidigt på din dator. Du kan till exempel köra Linux på en Windows-dator, eller testa nya system utan att påverka din huvuddator.

**Viktigaste fördelarna:**
- Gratis och open source
- Fungerar på Windows, Mac, Linux och Solaris
- Enkelt att använda
- Perfekt för att testa nya system säkert
- Bra för att köra system anonymt

---

## Installation och Grundinställningar

### Ladda ner VirtualBox
1. Gå till [virtualbox.org](https://www.virtualbox.org/)
2. Ladda ner versionen för ditt operativsystem
3. Installera programmet (följ installationsguiden)

### Första start
När du startar VirtualBox första gången ser du huvudfönstret där du kan:
- Skapa nya virtuella maskiner
- Hantera befintliga maskiner
- Konfigurera inställningar

---

## Skapa en Virtuell Maskin

### Steg-för-steg guide

#### 1. Klicka på "Ny" (New)
I huvudfönstret, klicka på den blå knappen "Ny".

#### 2. Namnge din maskin
- **Namn**: Välj ett beskrivande namn (t.ex. "Ubuntu 22.04" eller "Windows 10 Test")
- **Typ**: Välj operativsystemtyp (Linux, Windows, BSD, etc.)
- **Version**: Välj specifik version (t.ex. Ubuntu 64-bit)

#### 3. Minnesinställningar (RAM)
**Rekommenderade värden:**
- Windows 10/11: 4-8 GB (4096-8192 MB)
- Linux (Ubuntu/Debian): 2-4 GB (2048-4096 MB)
- Äldre system: 1-2 GB (1024-2048 MB)

**Tumregel**: Ge inte mer än hälften av datorns totala RAM-minne till den virtuella maskinen.

#### 4. Hårddisk
- **Skapa virtuell hårddisk nu**: Standard och rekommenderat
- **VDI (VirtualBox Disk Image)**: Standard format
- **Dynamiskt allokerad**: Växer efter behov (rekommenderat för att spara plats)
- **Fast storlek**: Snabbare men tar upp full plats direkt

**Rekommenderade storlekar:**
- Windows 10/11: 50-100 GB
- Linux: 20-50 GB
- Minimal installation: 10-20 GB

---

## Vanligaste Inställningar

### System

#### Moderkort (Motherboard)
- **Basminne**: RAM-mängd (se rekommendationer ovan)
- **Startsekvent**: CD/DVD först för installation, sedan hårddisk
- **Chipset**: PIIX3 (standard) eller ICH9 (nyare system)
- **Aktivera I/O APIC**: Aktivera för flerkärniga processorer

#### Processor
- **Processorer**: 2-4 CPU-kärnor rekommenderas
  - 1 CPU: Fungerar men långsamt
  - 2 CPU: Bra för de flesta ändamål
  - 4 CPU: Bra för krävande system
- **Execution Cap**: 100% (standard)
- **Aktivera PAE/NX**: Aktivera för 64-bitars system

#### Acceleration
- **VT-x/AMD-V**: Aktivera (kräver aktivering i BIOS)
- **Nested Paging**: Aktivera för bättre prestanda

### Skärm (Display)

- **Videominne**: 64-128 MB (mer för bättre grafik)
- **Skärm Scale Factor**: 100% (standard)
- **Grafikkontroller**: VMSVGA (standard för de flesta)
- **Aktivera 3D-acceleration**: För grafiskt krävande program
- **Antal skärmar**: 1 (standard)

### Lagring (Storage)

#### Hårddisk
- Dina virtuella hårddiskar visas här
- Du kan lägga till fler diskar efter behov

#### CD/DVD
- Montera ISO-filer för installation
- **Högerklicka på CD-ikonen** → Välj ISO-fil
- Koppla loss efter installation för snabbare start

### Nätverk
**Se detaljerad sektion nedan för fullständig information**

### Delad mapp (Shared Folders)

Dela filer mellan värd och gäst:
1. Gå till **Inställningar** → **Delade mappar**
2. Klicka på mappen med + (lägg till)
3. Välj mapp på värddatorn
4. Välj mapp-namn som gästen ser
5. **Auto-montera**: Aktivera för automatisk montering
6. **Gör permanent**: Aktivera

**I gästsystemet:**
- Linux: Mappen visas i `/media/sf_mappnamn`
- Windows: Visas som nätverksenhet

### USB

- **USB 1.1**: Grundläggande stöd
- **USB 2.0**: Rekommenderat för de flesta enheter
- **USB 3.0**: För snabba enheter (kräver Extension Pack)

**Lägg till USB-filter:**
1. Klicka på USB-ikonen med +
2. Välj enhet från listan
3. Enheten kopplas automatiskt till gästen när den ansluts

---

## Optimala Inställningar för Kali Linux på Kraftfull Hårdvara

### Specifikt för Lenovo Legion Pro (i9-275HX, RTX 5070 Ti Mobile, 32GB RAM)

Om du ska köra Kali Linux på en kraftfull gaming-laptop som Lenovo Legion Pro kan du utnyttja hårdvaran maximalt för bästa prestanda. Här är de optimala inställningarna baserat på 2025 års bästa praxis.

#### System Specifikationer (Din Hårdvara)
- **CPU**: Intel Core i9-275HX (24 kärnor: 8 P-cores + 16 E-cores)
- **GPU**: NVIDIA RTX 5070 Ti Mobile (8GB VRAM)
- **RAM**: 32GB DDR5

### Optimal VirtualBox-konfiguration för Kali Linux

#### 1. System → Moderkort

```
Inställningar → System → Moderkort
```

**Basminne (RAM):**
- **Rekommenderat**: 12288 MB (12 GB)
- **Alternativ**: 16384 MB (16 GB) om du planerar tung användning
- **Minimum**: 8192 MB (8 GB)

**Motivering**: Med 32GB totalt kan du säkert ge 12-16GB till VM:en utan att påverka värdsystemet. Kali Linux drar nytta av mer RAM för:
- Stora wordlists och rainbow tables
- Minneskrävande verktyg (Burp Suite, Metasploit)
- Flera verktyg samtidigt
- Browser med många tabs (för web pentesting)

**Övriga inställningar:**
- **Startsekvent**: Hard Disk (ingen installation behövs för färdigt paket)
- **Chipset**: ICH9 (nyare och bättre stöd)
- **Pekdon**: PS/2 Mouse (eller USB om du vill)
- **Aktivera I/O APIC**: ✓ (Viktigt för flerkärniga system)
- **Hardware Clock in UTC Time**: ✓ (Standard för Linux)
- **Enable EFI**: Avaktiverad (om inte Kali kräver det)

#### 2. System → Processor

```
Inställningar → System → Processor
```

**Processorer (CPU-kärnor):**
- **Rekommenderat**: 8 CPU-kärnor
- **Alternativ**: 6 kärnor (bra balans)
- **Maximum**: 12 kärnor (om du kör mycket tunga operationer)

**Motivering**: Din i9-275HX har 24 kärnor totalt (8 P-cores + 16 E-cores). Ge VM:en 6-8 kärnor för:
- Parallell cracking (hashcat, John the Ripper)
- Nmap-skanningar med många trådar
- Burp Suite Intruder attacks
- WiFi-cracking med aircrack-ng
- Flera verktyg parallellt

**OBS**: VirtualBox ser inte skillnad på P-cores och E-cores, så du får en mix. 8 kärnor är sweet spot för prestanda.

**Övriga processorinställningar:**
- **Execution Cap**: 100%
- **Aktivera PAE/NX**: ✓ (Säkerhetsfunktion)
- **Aktivera Nested VT-x/AMD-V**: ❌ (Behövs inte för Kali)

#### 3. System → Acceleration

```
Inställningar → System → Acceleration
```

**Paravirtualisering:**
- **Inställning**: KVM (bäst för Linux gäster)
- **Alternativ**: Default (låter VirtualBox välja)

**Motivering**: KVM (Kernel-based Virtual Machine) ger bästa prestanda för Linux-gäster på moderna Intel-processorer.

**Hårdvaruaccelleration:**
- **Aktivera VT-x/AMD-V**: ✓ (MÅSTE vara aktiverad!)
- **Aktivera Nested Paging**: ✓ (Stor prestandaförbättring)

**VIKTIGT**: Kontrollera att virtualiseringsteknologi är aktiverad i BIOS:
1. Starta om och tryck F2/F1/Delete för BIOS
2. Leta efter: "Intel Virtualization Technology" eller "VT-x"
3. Sätt till: Enabled
4. Leta efter: "VT-d" (optional men bra)
5. Spara och starta om

#### 4. Display (Skärm)

```
Inställningar → Skärm → Screen
```

**Videominne:**
- **Rekommenderat**: 128 MB
- **Minimum**: 64 MB

**Motivering**: Kali Linux GUI (XFCE/KDE) kräver inte mycket videominne. 128MB räcker gott för:
- Full HD upplösning (1920x1080)
- Flera skärmar
- Smooth desktop-upplevelse

**Skala Factor:**
- **Inställning**: 100%
- **Alternativ**: 200% om du har 4K-skärm och vill större text

**Grafikkontroller:**
- **Rekommenderat**: VMSVGA
- **Alternativ**: VBoxVGA eller VBoxSVGA

**Motivering**: VMSVGA har bäst Linux-stöd och fungerar utmärkt med Kali.

**Acceleration:**
- **Aktivera 3D-acceleration**: ✓ (Kan aktiveras för smidigare desktop)
- **Antal skärmar**: 1 (eller fler om du har flera monitorer)

**OBS**: Din RTX 5070 Ti används INTE direkt av VM:en (VirtualBox kan inte GPU passthrough lätt). Men 3D-acceleration via VirtualBox hjälper ändå.

#### 5. Storage (Lagring)

```
Inställningar → Lagring
```

**Virtuell hårddisk:**
- **Storlek**: 80 GB (dynamiskt allokerad)
- **Typ**: VDI (VirtualBox Disk Image)
- **Alternativ**: 100-120 GB om du lagrar stora dataset

**Motivering**: Kali Linux färdigt paket är ca 20-30GB, men du vill ha utrymme för:
- Wordlists (rockyou.txt och större)
- Captured network traffic (pcap-filer)
- Exploit databases
- Custom scripts och verktyg
- Log-filer från pentests

**Storage Controller:**
- **SATA Controller**: AHCI (standard, bra prestanda)
- **Enable Host I/O Cache**: ✓ (Snabbare disk-operationer)
- **Solid-state Drive**: ✓ (Om din VDI ligger på SSD - vilket den borde!)

**TIPS**: Placera VirtualBox VMs på din snabbaste disk (NVMe SSD om möjligt).

#### 6. Nätverk

```
Inställningar → Nätverk → Adapter 1
```

**För Penetration Testing och Säkerhetsarbete:**

**Setup 1: NAT (Säker och isolerad)**
```
Adapter 1:
- Aktivera nätverksadapter: ✓
- Ansluten till: NAT
- Adapter Type: Intel PRO/1000 MT Desktop (82540EM)
- Promiscuous Mode: Allow All (viktigt för nätverkssniffning!)
- Cable Connected: ✓
```

**Motivering**: NAT är bra för grundläggande testning och skyddar ditt huvudnätverk.

**Setup 2: Bridged (För verklig nätverkstestning)**
```
Adapter 1:
- Aktivera nätverksadapter: ✓
- Ansluten till: Bridged Adapter
- Namn: Välj ditt WiFi/Ethernet-kort
- Adapter Type: Intel PRO/1000 MT Desktop
- Promiscuous Mode: Allow All
- Cable Connected: ✓
```

**Motivering**: Bridged låter Kali se hela nätverket som om det vore en fysisk maskin - perfekt för:
- Nätverks-scanning (Nmap)
- Man-in-the-middle-attacker
- WiFi-pentesting
- Sårbarhetsskanning med Nessus/OpenVAS

**OBS**: Använd Bridged ENDAST i testmiljöer eller nätverk du har tillstånd att testa!

**Setup 3: Dual Adapter (Bästa av båda)**
```
Adapter 1: NAT (för internet)
Adapter 2: Host-only (för kommunikation med värd)
```

**Promiscuous Mode**: Detta är VIKTIGT för Kali! Sätts till "Allow All" för att:
- Använda Wireshark för packet capture
- Sniffa nätverkstrafik
- MITM-attacker
- ARP-spoofing

#### 7. USB-inställningar

```
Inställningar → USB
```

**För WiFi-adapters och hårdvara:**
- **USB-kontroller**: USB 3.0 (xHCI) Controller
- **Aktivera USB-kontroller**: ✓

**USB-filter (Lägg till specifika enheter):**

**För externa WiFi-adapters (viktigt för Kali!):**
1. Klicka på USB+ ikonen
2. Välj din WiFi-adapter (ex: Alfa AWUS036ACH, TP-Link TL-WN722N)
3. Adaptern kopplas automatiskt till Kali när den pluggas in

**Motivering**: Inbyggt WiFi i laptops fungerar ofta dåligt för packet injection. Externa USB WiFi-adapters med monitor mode är standard för:
- WiFi-cracking
- Evil Twin-attacker
- Deauthentication-attacker
- WPA/WPA2 handshake capture

**Rekommenderade WiFi-adapters för Kali:**
- Alfa AWUS036ACH (mycket populär)
- Alfa AWUS036NH
- TP-Link TL-WN722N v1 (OBS: v1 endast!)
- Panda PAU09

#### 8. Shared Folders (Delade mappar)

```
Inställningar → Delade mappar
```

**Rekommendation för Kali:**

**Setup för arbetsflöde:**
```
Mappnamn: kali-shared
Mappsökväg: C:\Users\DinAnvändare\KaliShare (Windows)
           eller /home/användare/KaliShare (Linux värd)
Auto-mount: ✓
Monterings-punkt: /mnt/shared
Gör permanent: ✓
```

**Användning**:
- Överför wordlists från värd till Kali
- Exportera rapporter från Kali till värd
- Dela exploit-scripts
- Backup av viktiga filer

**I Kali**, montera med:
```bash
# Skapa mount-punkt
sudo mkdir -p /mnt/shared

# Montera (om inte auto-mount fungerar)
sudo mount -t vboxsf kali-shared /mnt/shared

# Lägg till din användare i vboxsf-gruppen
sudo usermod -aG vboxsf $(whoami)

# Logga ut och in igen
```

#### 9. Guest Additions

**Ska jag installera Guest Additions i Kali?**

**JA - för bättre användarupplevelse:**
- Smidigare mushantering
- Bättre skärmupplösning (automatisk resize)
- Delad mapp fungerar direkt
- Copy/paste mellan värd och gäst
- Drag and drop-filer

**Installation i Kali:**
```bash
# Uppdatera systemet först
sudo apt update && sudo apt upgrade -y

# Installera dependencies
sudo apt install -y build-essential dkms linux-headers-$(uname -r)

# I VirtualBox: Devices → Insert Guest Additions CD image
# Kör installationen
cd /media/cdrom
sudo sh ./VBoxLinuxAdditions.run

# Starta om
sudo reboot
```

**NEJ - för maximal säkerhet och isolation:**
- Om du kör Kali för high-risk pentesting
- Om du vill minimera attack surface
- För forensik-arbete där integritet är kritisk

### Sammanfattning: Optimala inställningar för Kali på Legion Pro

#### Snabbkonfiguration

```
SYSTEM:
├─ Moderkort
│  ├─ RAM: 12288 MB (12 GB)
│  ├─ Chipset: ICH9
│  └─ I/O APIC: Aktiverad
│
├─ Processor
│  ├─ CPU-kärnor: 8
│  └─ PAE/NX: Aktiverad
│
└─ Acceleration
   ├─ Paravirtualisering: KVM
   ├─ VT-x: Aktiverad (kontrollera BIOS!)
   └─ Nested Paging: Aktiverad

DISPLAY:
├─ Videominne: 128 MB
├─ Grafikkontroller: VMSVGA
└─ 3D-acceleration: Aktiverad

STORAGE:
├─ Typ: VDI (dynamisk)
├─ Storlek: 80 GB
├─ Controller: SATA/AHCI
└─ Host I/O Cache: Aktiverad

NÄTVERK:
├─ Adapter 1: NAT eller Bridged
├─ Adapter Type: Intel PRO/1000 MT
└─ Promiscuous Mode: Allow All

USB:
├─ Controller: USB 3.0 (xHCI)
└─ Filter: Lägg till WiFi-adapters

SHARED FOLDERS:
└─ Setup: En delad mapp för överföringar
```

### Prestanda-optimeringar för Kali Linux

#### 1. I Värdsystemet (Windows/Linux)

**Stäng onödiga program:**
- Kali + 8GB värd = 20GB använt av 32GB
- 12GB fritt för värdsystem är gott om

**Prioritering av VirtualBox:**
```batch
REM Windows: Kör som Administratör
start /high "VirtualBox" "C:\Program Files\Oracle\VirtualBox\VirtualBox.exe"
```

**Antivirus-undantag:**
- Lägg till VirtualBox-mappen i undantag
- Lägg till .vdi-filen i undantag
- Förhindrar scanning som saktar ner VM

#### 2. I Kali Linux (Gästsystem)

**Inaktivera onödiga tjänster:**
```bash
# Se vilka tjänster som körs
systemctl list-unit-files --state=enabled

# Inaktivera tjänster du inte behöver (exempel)
sudo systemctl disable bluetooth.service
sudo systemctl disable cups.service  # Om du inte skriver ut
```

**Använd lightweight desktop:**
- Kali default: XFCE (redan lätt)
- Alternativ: i3 window manager (ännu lättare)

**Optimera swap:**
```bash
# Kolla nuvarande swappiness
cat /proc/sys/vm/swappiness

# Minska swappiness (mer RAM, mindre disk)
sudo sysctl vm.swappiness=10

# Gör permanent
echo "vm.swappiness=10" | sudo tee -a /etc/sysctl.conf
```

#### 3. Disk-optimering

**Komprimera VDI när den växer:**
```bash
# Från värdsystemet, när VM är avstängd
cd "C:\Program Files\Oracle\VirtualBox"

# Komprimera (återvinn utrymme)
VBoxManage modifymedium disk "C:\Sökväg\Till\Kali.vdi" --compact
```

**Periodic TRIM (om på SSD):**
```bash
# I Kali
sudo fstrim -av
```

### Verktyg som drar nytta av denna konfigurationen

Med 12GB RAM och 8 CPU-kärnor kan du köra:

**Parallell processing:**
- **Hashcat**: Använder alla 8 CPU-kärnor för cracking
- **John the Ripper**: Multi-threaded password cracking
- **Hydra**: Parallella brute-force-attacker
- **Nmap**: Snabba skanningar med `-T4` eller `-T5`

**Minneskrävande verktyg:**
- **Burp Suite Professional**: Körs smidigt med 12GB
- **Metasploit Framework**: Många moduler samtidigt
- **Wireshark**: Stora packet captures
- **Maltego**: Grafdataanalys

**Samtidig användning:**
- Firefox med många tabs (för web pentesting)
- Burp Suite i bakgrunden
- Terminal med flera verktyg
- Wireshark packet capture
- Metasploit listener

### Troubleshooting för Kali på Legion Pro

#### Problem: VM är långsam trots kraftfull hårdvara

**Lösningar:**
1. **Kontrollera VT-x i BIOS**: Måste vara aktiverad!
2. **Öka RAM**: Från 8GB till 12GB eller 16GB
3. **Kontrollera Hyper-V**: På Windows, inaktivera Hyper-V om aktiverat
   ```batch
   bcdedit /set hypervisorlaunchtype off
   ```
4. **Kolla CPU-användning**: På värd, se om något annat tar resurser

#### Problem: Ingen internet i Kali

**Lösningar:**
1. **Kontrollera nätverksadapter**: Ska vara aktiverad i VirtualBox
2. **Testa i Kali:**
   ```bash
   # Kolla interface
   ip addr show

   # Kolla routing
   ip route show

   # Testa DNS
   ping 8.8.8.8
   ping google.com

   # Starta om nätverket
   sudo systemctl restart NetworkManager
   ```

#### Problem: USB WiFi-adapter syns inte i Kali

**Lösningar:**
1. **Installera Extension Pack**:
   - Ladda ner från virtualbox.org (samma version som VirtualBox)
   - Fil → Inställningar → Extensions → Lägg till
2. **Skapa USB-filter**: I VM-inställningar
3. **Koppla från värd**:
   - Windows: Device Manager → Inaktivera adaptern
   - Sedan anslut till VM via VirtualBox-menyn
4. **Kontrollera i Kali:**
   ```bash
   # Lista USB-enheter
   lsusb

   # Se om WiFi-adapter finns
   iwconfig
   airmon-ng
   ```

#### Problem: Dålig grafisk prestanda

**Lösningar:**
1. **Installera Guest Additions** (se ovan)
2. **Öka videominne**: Till 128 MB
3. **Aktivera 3D-acceleration**
4. **Byt grafikkontroller**: Testa VMSVGA, VBoxVGA, VBoxSVGA

### Specifika tips för Legion Pro-användare

#### 1. Batteritid vs Prestanda

**På batteri**: VirtualBox drar mycket ström. Förväntad batteritid:
- Normal användning: 2-3 timmar
- Tung pentesting: 1-2 timmar

**Tips**: Kör på ström vid tunga operationer (hashcracking, scanning).

#### 2. Kylning och Termalbegränsning

Legion Pro har bra kylning men VM:er genererar värme:
- **Använd Lenovo Vantage**: Sätt profil till "Performance Mode"
- **Elevera laptop**: Bättre luftflöde = mindre thermal throttling
- **Övervaka temperaturer**: Med HWiNFO64 (Windows) eller lm-sensors (Linux)

#### 3. GPU-användning

Din RTX 5070 Ti används **inte direkt** av VM:en. Men:
- **GPU-baserad cracking**: Kör hashcat på värdsystemet istället
- **Eller**: Använd GPU-passthrough (avancerat, kräver KVM inte VirtualBox)

**Alternativ för GPU-cracking:**
```bash
# I värdsystemet (Windows med hashcat installerat)
hashcat -m 1000 -a 0 hashes.txt wordlist.txt

# Överför result till Kali via delad mapp
```

---

## Nätverksinställningar - Detaljerad Guide

Nätverket är en av de viktigaste inställningarna i VirtualBox, särskilt för anonymitet och säkerhet.

### Översikt av nätverkslägen

#### 1. NAT (Network Address Translation) - **Standard**

**Vad det är:**
- Den virtuella maskinen delar värdens internet-anslutning
- Maskinen får ett privat IP-adress (10.0.2.15)
- Kan komma ut till internet
- **Inifrån nätverket kan ingen se den virtuella maskinen**

**Användning:**
- Grundläggande internet-åtkomst
- Bra för isolerade tester
- **Bäst för säkerhet och anonymitet**

**För- och nackdelar:**
- ✅ Säkert - ingen direkt åtkomst utifrån
- ✅ Fungerar direkt utan konfiguration
- ✅ Delar värdens internetanslutning
- ❌ Ingen kommunikation med andra VM:ar
- ❌ Ingen åtkomst från värddatorn till VM

**Konfigurera NAT:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: NAT
```

#### 2. NAT Network - **Rekommenderat för flera VM:ar**

**Vad det är:**
- Flera VM:ar delar samma NAT-nätverk
- VM:ar kan kommunicera med varandra
- Alla har internet-åtkomst
- Isolerat från värdens nätverk

**Användning:**
- När du vill att flera VM:ar ska kunna prata med varandra
- Testa nätverkskommunikation
- Säkert nätverk för flera maskiner

**Skapa NAT Network:**
1. **Arkiv** → **Inställningar** → **Nätverk**
2. Klicka på **NAT Networks** fliken
3. Klicka på **+** för att lägga till
4. Namnge nätverket (t.ex. "NatNetwork")
5. Konfigurera IP-range (standard: 10.0.2.0/24)

**Konfigurera VM för NAT Network:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: NAT Network
- Namn: NatNetwork
```

**För- och nackdelar:**
- ✅ VM:ar kan kommunicera med varandra
- ✅ Alla har internet-åtkomst
- ✅ Säkert och isolerat
- ❌ Kräver initial konfiguration

#### 3. Bridged Adapter (Nätverksbro)

**Vad det är:**
- Den virtuella maskinen kopplas direkt till ditt fysiska nätverk
- Får ett IP från din router (via DHCP)
- Syns som en vanlig dator på nätverket
- Full nätverksåtkomst i båda riktningar

**Användning:**
- När VM behöver vara tillgänglig från andra datorer
- Server-installation
- Nätverkstestning

**Konfigurera Bridged:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: Bridged Adapter
- Namn: Välj ditt nätverkskort (t.ex. eth0, wlan0)
```

**För- och nackdelar:**
- ✅ Full nätverksåtkomst
- ✅ Syns på nätverket som egen enhet
- ✅ Bra för server-användning
- ❌ **INTE anonymt** - syns på nätverket
- ❌ Exponerad för nätverket
- ❌ Använder ett extra IP-nummer

#### 4. Internal Network (Internt nätverk)

**Vad det är:**
- VM:ar kan endast kommunicera med andra VM:ar på samma interna nätverk
- **Ingen internet-åtkomst**
- **Ingen åtkomst till värddatorn**
- Helt isolerat

**Användning:**
- Säkerhetstestning
- Isolerade nätverk
- Labb-miljöer

**Konfigurera Internal Network:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: Internal Network
- Namn: intnet (eller välj eget namn)
```

**För- och nackdelar:**
- ✅ Helt isolerat
- ✅ Perfekt för säkerhetstester
- ✅ Flera VM:ar kan kommunicera
- ❌ Ingen internet-åtkomst

#### 5. Host-only Adapter

**Vad det är:**
- VM kan kommunicera med värddatorn
- VM:ar på samma host-only nätverk kan kommunicera med varandra
- **Ingen direkt internet-åtkomst** (kan delas via värden)

**Användning:**
- Utveckling och testning
- När du behöver åtkomst från värddatorn
- Fil-delning och tjänster

**Skapa Host-only Network:**
1. **Arkiv** → **Inställningar** → **Nätverk**
2. Klicka på **Host-only Networks** fliken
3. Klicka på **+** för att lägga till
4. Konfigurera IP-range (t.ex. 192.168.56.0/24)

**Konfigurera VM för Host-only:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: Host-only Adapter
- Namn: vboxnet0
```

**För- och nackdelar:**
- ✅ Åtkomst från värddatorn
- ✅ VM:ar kan kommunicera
- ✅ Kontrollerat nätverk
- ❌ Ingen direkt internet (kräver NAT-routing)

#### 6. Generic Driver / Not Attached

**Not Attached**: Inget nätverkskort - helt offline
**Generic Driver**: Avancerad konfiguration för speciella behov

---

## Anonym Användning med Nätverksåtkomst

För att köra ett operativsystem anonymt med internet-åtkomst behöver du kombinera rätt nätverksinställningar med säkerhetsverktyg.

### Grundläggande Anonym Konfiguration

#### Steg 1: Välj rätt operativsystem
**Rekommenderade system:**
- **Tails OS**: Speciellt designat för anonymitet
- **Whonix**: Tvåsystems-lösning med Tor
- **Linux (Ubuntu/Debian)**: Med manuell Tor-konfiguration

#### Steg 2: Nätverkskonfiguration för anonymitet

**Rekommenderad setup:**
```
Inställningar → Nätverk → Adapter 1
- Aktivera nätverksadapter: ✓
- Ansluten till: NAT
- Avancerat → Adapter Type: PCnet-PCI II
- Avancerat → Promiscuous Mode: Deny
```

**Varför NAT?**
- Din VM får inte ett synligt IP på nätverket
- All trafik går genom värddatorns IP
- Ingen direkt routing från internet till VM
- Svårt att skilja VM-trafik från värd-trafik

#### Steg 3: MAC-adress anonymitet

VirtualBox genererar unika MAC-adresser som kan spåras. Ändra detta:

```
Inställningar → Nätverk → Adapter 1 → Avancerat
- Klicka på "refresh" ikonen bredvid MAC-address
- Eller ange egen MAC: 080027XXXXXX
```

**För maximal anonymitet:**
```bash
# Slumpa MAC-adress vid varje start (Linux värd):
VBoxManage modifyvm "VM-Namn" --macaddress1 auto
```

### Använda Tor för Anonymitet

#### Metod 1: Tails OS (Enklast)

**Tails** är byggt för anonymitet och använder Tor automatiskt.

1. Ladda ner Tails ISO från [tails.boum.org](https://tails.boum.org/)
2. Skapa VM med:
   - RAM: 2048 MB minimum
   - Nätverk: NAT
3. Starta från ISO
4. All trafik går automatiskt genom Tor

**VirtualBox-inställningar för Tails:**
```
System → Moderkort:
- Basminne: 2048 MB
- Startsekvent: Optical först

Nätverk → Adapter 1:
- Ansluten till: NAT
- Adapter Type: Intel PRO/1000 MT Desktop

Skärm:
- Videominne: 128 MB
- Grafikkontroller: VMSVGA
```

#### Metod 2: Whonix (Mest säkert)

**Whonix** använder två VM:ar:
- **Gateway**: Kör Tor (all trafik går genom denna)
- **Workstation**: Din arbets-VM (vet inte sitt riktiga IP)

**Installation:**
1. Ladda ner Whonix från [whonix.org](https://www.whonix.org/)
2. Importera båda VM:arna (.ova filer)
3. Starta Gateway först, sedan Workstation

**Nätverkskonfiguration:**
- **Gateway**: NAT (ansluten till internet)
- **Workstation**: Internal Network (endast via Gateway)

```
Whonix-Gateway:
Adapter 1: NAT (för internet)
Adapter 2: Internal Network (namn: Whonix)

Whonix-Workstation:
Adapter 1: Internal Network (namn: Whonix)
```

**Fördelar med Whonix:**
- Även om Workstation komprometteras, läcker inte ditt riktiga IP
- Stream isolation
- Professionellt konfigurerad för anonymitet

#### Metod 3: Vanlig Linux + Tor (Manuell)

För Ubuntu/Debian:

**Installation av Tor:**
```bash
# Installera Tor
sudo apt update
sudo apt install tor tor-arm

# Starta Tor
sudo systemctl start tor
sudo systemctl enable tor
```

**Konfigurera all trafik genom Tor:**
```bash
# Installera proxychains för att tvinga all trafik genom Tor
sudo apt install proxychains4

# Redigera konfiguration
sudo nano /etc/proxychains4.conf

# Lägg till i slutet:
socks5 127.0.0.1 9050
```

**Använd program genom Tor:**
```bash
# Kör Firefox genom Tor
proxychains4 firefox

# Test din IP
proxychains4 curl ifconfig.me
```

**Browser-konfiguration:**
- Använd **Tor Browser** (säkrast)
- Eller konfigurera Firefox att använda SOCKS5 proxy: 127.0.0.1:9050

### Ytterligare Säkerhetsåtgärder

#### 1. Inaktivera delad mapp
```
Inställningar → Delade mappar
- Ta bort alla delade mappar
```

#### 2. Inaktivera delat urklipp
```
Inställningar → Allmänt → Avancerat
- Delat urklipp: Inaktiverad
- Drag and drop: Inaktiverad
```

#### 3. Inaktivera USB
```
Inställningar → USB
- Avmarkera "Aktivera USB-kontroller"
```

#### 4. Inaktivera gästtillägg (för maximal isolation)
- **Installera INTE** VirtualBox Guest Additions
- Detta förhindrar viss integration mellan värd och gäst

#### 5. Använd snapshots
Skapa en ren snapshot innan du börjar:
```
Maskinen → Ta snapshot
Namn: "Clean Boot"
```

Återställ till ren state efter varje session.

### DNS-läckor och skydd

**Problem**: DNS-förfrågningar kan läcka din riktiga IP.

**Lösning i Tor/Tails/Whonix**: Hanteras automatiskt

**Manuell lösning:**
```bash
# Redigera resolv.conf för att använda Tor DNS
sudo nano /etc/resolv.conf

# Byt till:
nameserver 127.0.0.1
```

**Eller använd OpenDNS över Tor:**
```bash
# I proxychains konfiguration
dns_over_socks4
```

**Testa för DNS-läckor:**
- Besök [dnsleaktest.com](https://dnsleaktest.com/)
- Kolla att din riktiga ISP inte visas

### WebRTC-läckor (i webbläsare)

**Problem**: WebRTC kan läcka ditt lokala IP.

**Lösning i Firefox:**
1. Gå till `about:config`
2. Sök efter `media.peerconnection.enabled`
3. Sätt till `false`

**Eller använd extension:**
- **uBlock Origin** med WebRTC-blockering
- **Disable WebRTC**

**Testa WebRTC-läckor:**
- Besök [browserleaks.com/webrtc](https://browserleaks.com/webrtc)

### Fullständig anonym setup - Checklista

- [ ] VirtualBox VM med NAT-nätverk
- [ ] Slumpad MAC-adress
- [ ] Tails OS / Whonix / Tor-konfigurerad Linux
- [ ] Delade mappar inaktiverade
- [ ] Delat urklipp inaktiverat
- [ ] USB inaktiverat
- [ ] Guest Additions INTE installerat
- [ ] DNS går genom Tor
- [ ] WebRTC inaktiverat i webbläsare
- [ ] Testat för DNS-läckor
- [ ] Testat för WebRTC-läckor
- [ ] Tor Browser eller Tor-konfigurerad browser
- [ ] Snapshot för ren återställning

### Användningstips för anonymitet

1. **Starta alltid från snapshot**: Återställ till ren state varje session
2. **Blanda inte identiteter**: Logga inte in på personliga konton
3. **Använd olika VM:ar**: En VM per användningsområde
4. **Stäng av innan disconnect**: Stäng alltid VM korrekt
5. **Uppdatera regelbundet**: Håll system och Tor uppdaterade
6. **Testa läckor regelbundet**: Kontrollera IP, DNS, WebRTC

---

## Tips och Troubleshooting

### Prestanda-tips

#### VM är långsam
1. **Öka RAM**: Ge mer minne till VM
2. **Öka CPU-kärnor**: Ge 2-4 kärnor
3. **Aktivera VT-x/AMD-V**: I BIOS/UEFI
4. **Använd SSD**: För virtuella hårddiskar
5. **Installera Guest Additions**: För bättre grafik och integration

#### Grafiken är seg
1. **Öka videominne**: Till 128 MB
2. **Aktivera 3D-acceleration**
3. **Installera Guest Additions**

### Nätverksproblem

#### Ingen internet-anslutning
1. **Kontrollera nätverksläge**: NAT eller Bridged
2. **Aktivera nätverksadapter**: I VM-inställningar
3. **Kolla värd-internet**: Har värddatorn internet?
4. **Starta om nätverksadapter**: I gästsystemet

#### Kan inte nå VM från värddatorn
1. **Använd Host-only eller Bridged**: NAT tillåter inte inkommande
2. **Konfigurera port forwarding**: För NAT (se nedan)
3. **Kontrollera brandvägg**: I gäst-systemet

#### Port Forwarding för NAT
För att komma åt tjänster i VM via NAT:

```
Inställningar → Nätverk → Adapter 1 → Avancerat → Port Forwarding

Klicka på + och lägg till:
Namn: SSH
Protokoll: TCP
Värd-IP: 127.0.0.1
Värd-Port: 2222
Gäst-IP: (lämna tomt)
Gäst-Port: 22
```

Nu kan du SSH:a med: `ssh -p 2222 user@127.0.0.1`

### Installation problem

#### 64-bit option saknas
- **Orsak**: VT-x/AMD-V är inte aktiverat
- **Lösning**: Aktivera i BIOS/UEFI

#### Kan inte installera från ISO
1. **Kontrollera ISO**: Är filen korrupt?
2. **Montera korrekt**: Högerklicka CD i Storage
3. **Ändra boot order**: CD först i boot sequence

### Guest Additions

**Vad är det?**
- Drivrutiner och verktyg för bättre integration
- Bättre grafik och musintegration
- Delad mapp-funktionalitet
- Delat urklipp

**Installation:**
1. Starta VM
2. **Enheter** → **Installera Guest Additions CD-avbildning**
3. Kör installationen i gäst-systemet
4. Starta om

**OBS**: Installera INTE Guest Additions för maximal anonymitet/isolation.

### Backup och snapshots

#### Ta snapshot
```
Maskinen → Ta snapshot
```
Snabbt sätt att spara tillstånd och återställa senare.

#### Exportera VM
```
Fil → Exportera Appliance
```
Skapar en .ova fil du kan dela eller flytta.

#### Backup av virtuell disk
Kopiera .vdi filen från VM-mappen (när VM är avstängd).

### Tangentbords-shortcuts

- **Höger Ctrl** (Host-tangent): Släpp mus/tangentbord från VM
- **Host + F**: Fullskärm
- **Host + L**: Sparad state
- **Host + H**: Pause
- **Host + R**: Reset
- **Host + P**: Screenshot

---

## Sammanfattning - Snabbguide

### Snabbstart ny VM
1. **Ny** → Namnge → Välj OS-typ
2. RAM: 2-4 GB för Linux, 4-8 GB för Windows
3. Skapa disk: 20-50 GB dynamisk
4. Montera ISO: Storage → CD → Välj ISO
5. Starta och installera

### Bästa nätverksinställningar

| Användning | Nätverksläge | Beskrivning |
|-----------|-------------|-------------|
| Grundläggande internet | NAT | Enklast, säkrast |
| Flera VM:ar som pratar | NAT Network | Isolerat nätverk |
| Server/åtkomst utifrån | Bridged | Som egen dator på nätverket |
| Utveckling/värd-åtkomst | Host-only + NAT | Två adaptrar |
| Anonymitet | NAT + Tor | Bästa för anonymitet |
| Total isolation | Internal Network | Ingen internet |

### Anonymitetsinställning (sammanfattning)
1. Nätverk: NAT
2. Slumpad MAC-adress
3. Använd Tails/Whonix
4. Inaktivera: Delad mapp, USB, urklipp
5. Testa DNS/WebRTC-läckor
6. Använd snapshots

### Kali Linux på Legion Pro (Snabbreferens)

**Optimala inställningar för i9-275HX, RTX 5070 Ti Mobile, 32GB RAM:**

| Komponent | Inställning | Värde |
|-----------|-------------|-------|
| RAM | Basminne | 12288 MB (12 GB) |
| CPU | Processorer | 8 kärnor |
| CPU | Paravirtualisering | KVM |
| Display | Videominne | 128 MB |
| Display | Grafikkontroller | VMSVGA |
| Display | 3D-acceleration | Aktiverad |
| Storage | Diskstorlek | 80 GB (dynamisk) |
| Storage | Controller | SATA/AHCI |
| Nätverk | Adapter Type | Intel PRO/1000 MT |
| Nätverk | Promiscuous Mode | Allow All |
| USB | Controller | USB 3.0 (xHCI) |
| System | VT-x/AMD-V | Aktiverad (kontrollera BIOS!) |
| System | Nested Paging | Aktiverad |
| System | I/O APIC | Aktiverad |
| System | Chipset | ICH9 |

**Nätverksval för Kali:**
- **NAT**: Grundläggande säker testning
- **Bridged**: Fullständig nätverksaccess (pentesting i testmiljö)
- **NAT + Host-only**: Bästa av båda (dual adapter)

**Viktiga tillägg:**
- **VirtualBox Extension Pack**: För USB 3.0-stöd (WiFi-adapters)
- **Guest Additions**: För bättre prestanda och delad mapp
- **External WiFi Adapter**: Alfa AWUS036ACH eller liknande

**Prestanda-tips:**
1. Placera VDI på NVMe SSD
2. Lägg till VirtualBox i antivirus-undantag
3. Aktivera "Performance Mode" i Lenovo Vantage
4. Kör på ström vid tunga operationer

**Se fullständig guide i kapitel 5** för detaljerad konfiguration.

---

## Resurser och länkar

**VirtualBox:**
- **VirtualBox**: https://www.virtualbox.org/
- **VirtualBox Extension Pack**: https://www.virtualbox.org/wiki/Downloads
- **VirtualBox Manual**: https://www.virtualbox.org/manual/

**Operativsystem:**
- **Kali Linux**: https://www.kali.org/
- **Tails OS**: https://tails.boum.org/
- **Whonix**: https://www.whonix.org/

**Säkerhet och anonymitet:**
- **Tor Project**: https://www.torproject.org/
- **DNS Leak Test**: https://dnsleaktest.com/
- **Browser Leaks**: https://browserleaks.com/
- **IP Check**: https://check.torproject.org/

**Kali Linux-verktyg:**
- **Metasploit**: https://www.metasploit.com/
- **Burp Suite**: https://portswigger.net/burp
- **Wireshark**: https://www.wireshark.org/
- **Nmap**: https://nmap.org/

---

**Lycka till med VirtualBox!** 🚀

_Denna manual täcker de vanligaste användningsområdena. För avancerade funktioner, se den officiella VirtualBox-dokumentationen._
