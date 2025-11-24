# VirtualBox - Manual för Avancerade Funktioner

## Innehållsförteckning

1. [Introduktion](#introduktion)
2. [Snapshots och VM-kloning](#snapshots-och-vm-kloning)
3. [Avancerad Nätverkskonfiguration](#avancerad-nätverkskonfiguration)
4. [USB och Hårdvaruåtkomst](#usb-och-hårdvaruåtkomst)
5. [VirtualBox CLI - VBoxManage](#virtualbox-cli---vboxmanage)
6. [Automation och Scripting](#automation-och-scripting)
7. [Remote Desktop och Headless Mode](#remote-desktop-och-headless-mode)
8. [Virtuella Diskar - Avancerat](#virtuella-diskar---avancerat)
9. [GPU Passthrough och PCI Passthrough](#gpu-passthrough-och-pci-passthrough)
10. [Säkerhet och Kryptering](#säkerhet-och-kryptering)
11. [Prestanda-optimering Avancerat](#prestanda-optimering-avancerat)
12. [Nätverk mellan VM:ar - Avancerade Scenarier](#nätverk-mellan-vmar---avancerade-scenarier)
13. [Backup och Disaster Recovery](#backup-och-disaster-recovery)
14. [Extension Pack och Tillägg](#extension-pack-och-tillägg)
15. [Troubleshooting Avancerat](#troubleshooting-avancerat)

---

## Introduktion

Denna manual täcker avancerade funktioner i VirtualBox för erfarna användare som vill gå bortom grundläggande virtualisering. Om du inte har läst grundmanualen rekommenderas det starkt att börja där.

**Vad du lär dig:**
- Avancerad VM-hantering med snapshots och kloning
- Komplex nätverkskonfiguration med flera adapters
- Automation via kommandorad
- Remote access och headless körning
- Säkerhet och kryptering
- Prestanda-tuning för produktionsmiljöer

**Förkunskaper:**
- Grundläggande VirtualBox-användning
- Bekväm med kommandorad/terminal
- Förståelse för nätverk (IP, subnät, routing)
- Grundläggande Linux/Windows-administration

---

## Snapshots och VM-kloning

### Snapshots - Tidsmaskinen för VM:ar

Snapshots låter dig spara exakt tillstånd av en VM vid en specifik tidpunkt. Du kan sedan återställa till detta tillstånd när som helst.

#### Skapa Snapshot

**Via GUI:**
1. Välj din VM (kan vara igång eller avstängd)
2. Klicka på **hamburger-menyn** (☰) bredvid VM-namnet
3. Välj **Snapshots**
4. Klicka på **Ta** (Take)
5. Ge snapshot ett beskrivande namn och beskrivning

**Via kommandorad:**
```bash
VBoxManage snapshot "VM-Namn" take "Snapshot-Namn" \
  --description "Beskrivning av tillståndet" \
  --live
```

**`--live` flaggan**: Tar snapshot medan VM körs utan att pausa den.

#### Snapshot-strategier

**1. Pre-installation Snapshot**
```bash
# Innan du installerar något viktigt
VBoxManage snapshot "Kali-Linux" take "Clean-Install" \
  --description "Fresh Kali installation before any modifications"
```

**Användning**: Säkerhetskopiering innan stora ändringar

**2. Snapshot-kedja för utveckling**
```
Clean Install
    ├── Development Environment Setup
    │   ├── Feature-Branch-A
    │   └── Feature-Branch-B
    └── Testing Configuration
        └── Load-Test-Scenario
```

**Skapa kedja:**
```bash
# Bas
VBoxManage snapshot "DevVM" take "Clean-Install"

# Starta VM, installera dev tools, stäng av

# Nästa nivå
VBoxManage snapshot "DevVM" take "Dev-Environment"

# Fortsätt bygga kedjor...
```

**3. Cykliska snapshots (automatiserat)**
```bash
#!/bin/bash
# Daglig snapshot-rotation (behåll 7 dagar)

VM_NAME="Production-Server"
DATE=$(date +%Y-%m-%d)
SNAPSHOT_NAME="Daily-Backup-$DATE"

# Ta ny snapshot
VBoxManage snapshot "$VM_NAME" take "$SNAPSHOT_NAME"

# Lista alla snapshots
SNAPSHOTS=$(VBoxManage snapshot "$VM_NAME" list --machinereadable | grep SnapshotName | cut -d'"' -f2)

# Radera snapshots äldre än 7 dagar
for SNAP in $SNAPSHOTS; do
    if [[ $SNAP =~ Daily-Backup-([0-9]{4}-[0-9]{2}-[0-9]{2}) ]]; then
        SNAP_DATE="${BASH_REMATCH[1]}"
        DAYS_OLD=$(( ( $(date +%s) - $(date -d "$SNAP_DATE" +%s) ) / 86400 ))

        if [ $DAYS_OLD -gt 7 ]; then
            echo "Deleting old snapshot: $SNAP ($DAYS_OLD days old)"
            VBoxManage snapshot "$VM_NAME" delete "$SNAP"
        fi
    fi
done
```

#### Återställa Snapshot

**Via GUI:**
1. Gå till Snapshots-vyn
2. Högerklicka på snapshot du vill återställa till
3. Välj **Restore** (Återställ)
4. Välj om du vill skapa snapshot av nuvarande tillstånd först (rekommenderas)

**Via kommandorad:**
```bash
# Återställ till specifik snapshot
VBoxManage snapshot "VM-Namn" restore "Snapshot-Namn"

# Återställ till senaste snapshot
VBoxManage snapshot "VM-Namn" restorecurrent
```

#### Ta bort Snapshots

**Viktigt**: När du tar bort en snapshot **slås den samman** med parent/child snapshots. Data går inte förlorad.

```bash
# Ta bort specifik snapshot
VBoxManage snapshot "VM-Namn" delete "Snapshot-Namn"

# Ta bort alla snapshots (slå samman till nuvarande state)
VBoxManage snapshot "VM-Namn" deleteall
```

### VM-kloning

Kloning skapar en komplett kopia av en VM.

#### Typer av kloning

**1. Full Clone (Fullständig kopia)**
```bash
VBoxManage clonevm "Original-VM" \
  --name "Klon-VM" \
  --register
```

- Skapar oberoende kopia
- Tar mer diskutrymme
- Kan användas oberoende av original

**2. Linked Clone (Länkad kopia)**
```bash
# Kräver snapshot först
VBoxManage snapshot "Original-VM" take "Clone-Base"

# Skapa länkad klon
VBoxManage clonevm "Original-VM" \
  --snapshot "Clone-Base" \
  --name "Linked-Clone" \
  --options link \
  --register
```

- Delar basdata med original via snapshot
- Sparar mycket diskutrymme
- Snabbare att skapa
- **Kräver att original-VM finns kvar**

#### Praktiska klonscenarier

**Scenario 1: Testa flera konfigurationer parallellt**
```bash
# Bas-VM med färdig installation
BASE_VM="Ubuntu-Base"

# Ta snapshot för kloning
VBoxManage snapshot "$BASE_VM" take "Clone-Point"

# Skapa flera test-VMs
for CONFIG in nginx apache caddy; do
    VBoxManage clonevm "$BASE_VM" \
      --snapshot "Clone-Point" \
      --name "WebServer-$CONFIG" \
      --options link \
      --register
done

# Nu har du 3 VMs att testa olika web servers på
```

**Scenario 2: Distribuera identiska VMs med unika MAC**
```bash
# Klona och ge unika MAC-adresser
VBoxManage clonevm "Template-VM" \
  --name "Node-1" \
  --options link \
  --register

# Generera ny MAC
VBoxManage modifyvm "Node-1" --macaddress1 auto

# Upprepa för Node-2, Node-3, etc.
```

**Scenario 3: Export/Import för distribution**
```bash
# Exportera till OVA (Open Virtualization Archive)
VBoxManage export "Min-VM" \
  --output /path/to/export.ova \
  --manifest \
  --vsys 0 \
  --description "Beskrivning av VM" \
  --version "1.0"

# På annan dator: Importera
VBoxManage import /path/to/export.ova \
  --vsys 0 \
  --vmname "Importerad-VM"
```

---

## Avancerad Nätverkskonfiguration

### Multi-adapter Setup

En VM kan ha upp till **8 nätverksadapters** samtidigt. Detta möjliggör komplexa nätverksscenarier.

#### Scenario 1: Router/Firewall VM

**Setup:**
- Adapter 1: Bridged (WAN - anslutet till internet)
- Adapter 2: Internal Network (LAN - internt nätverk)

```bash
# Konfigurera adapters
VBoxManage modifyvm "Router-VM" --nic1 bridged --bridgeadapter1 eth0
VBoxManage modifyvm "Router-VM" --nic2 intnet --intnet2 "LAN"
VBoxManage modifyvm "Router-VM" --nicpromisc2 allow-all
```

**I Router-VM (Linux):**
```bash
# Aktivera IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf

# Setup interfaces
sudo ip addr add 10.0.10.1/24 dev eth1  # LAN interface

# Firewall (iptables)
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

**Klient-VMs:**
```bash
# Anslut klient till samma Internal Network
VBoxManage modifyvm "Client-VM" --nic1 intnet --intnet1 "LAN"
```

**I klient-VM:**
```bash
# Sätt router som gateway
sudo ip addr add 10.0.10.100/24 dev eth0
sudo ip route add default via 10.0.10.1
```

#### Scenario 2: Dual-Network Penetration Testing

**Setup:**
- Adapter 1: NAT (för uppdateringar och verktyg)
- Adapter 2: Host-only (för kontroll från värd)
- Adapter 3: Internal Network (för attack-lab)

```bash
VBoxManage modifyvm "Kali-Pentest" --nic1 nat
VBoxManage modifyvm "Kali-Pentest" --nic2 hostonly --hostonlyadapter2 vboxnet0
VBoxManage modifyvm "Kali-Pentest" --nic3 intnet --intnet3 "AttackLab"
VBoxManage modifyvm "Kali-Pentest" --nicpromisc3 allow-all

# Target VM
VBoxManage modifyvm "Target-Server" --nic1 intnet --intnet1 "AttackLab"
```

**I Kali:**
```bash
# eth0: NAT (internet)
# eth1: Host-only (192.168.56.x)
# eth2: Internal (för attacks)

# Konfigurera attack-interface
sudo ip addr add 10.0.99.10/24 dev eth2
sudo ip link set eth2 up
```

### Port Forwarding (NAT)

Ge åtkomst till tjänster i NAT-baserade VMs.

#### Via GUI:
```
Inställningar → Nätverk → Adapter 1 → Avancerat → Port Forwarding
```

#### Via CLI:
```bash
# SSH: Vidarebefordra värd-port 2222 till gäst-port 22
VBoxManage modifyvm "VM-Namn" \
  --natpf1 "SSH,tcp,,2222,,22"

# HTTP: Port 8080 → 80
VBoxManage modifyvm "VM-Namn" \
  --natpf1 "HTTP,tcp,,8080,,80"

# HTTPS: Port 8443 → 443
VBoxManage modifyvm "VM-Namn" \
  --natpf1 "HTTPS,tcp,,8443,,443"

# Ta bort regel
VBoxManage modifyvm "VM-Namn" --natpf1 delete "SSH"
```

#### Praktiskt exempel: Web development
```bash
# Web server med databas
VBoxManage modifyvm "DevServer" --natpf1 "Web,tcp,,8080,,80"
VBoxManage modifyvm "DevServer" --natpf1 "MySQL,tcp,,3306,,3306"
VBoxManage modifyvm "DevServer" --natpf1 "SSH,tcp,,2222,,22"

# Anslut från värd:
# Web: http://localhost:8080
# MySQL: mysql -h 127.0.0.1 -P 3306
# SSH: ssh -p 2222 user@localhost
```

### VLAN Tagging

För avancerad nätverkssegmentering.

```bash
# Aktivera VLAN 100 på adapter 1
VBoxManage modifyvm "VM-Namn" --nictrace1 on --nictracefile1 /tmp/trace.pcap
VBoxManage setextradata "VM-Namn" \
  "VBoxInternal/Devices/pcnet/0/LUN#0/Config/Network" "10.0.100.0/24"
```

### Network Bandwidth Throttling

Simulera långsamma nätverksanslutningar.

```bash
# Begränsa adapter 1 till 1 Mbps
VBoxManage bandwidthctl "VM-Namn" add "Limit1Mbps" --type network --limit 1m

# Applicera på adapter
VBoxManage modifyvm "VM-Namn" --nicbandwidthgroup1 "Limit1Mbps"

# Ta bort begränsning
VBoxManage modifyvm "VM-Namn" --nicbandwidthgroup1 none
```

### Promiscuous Mode

Tillåter att fånga all nätverkstrafik (behövs för packet sniffing).

```bash
# Allow All: Fånga all trafik
VBoxManage modifyvm "VM-Namn" --nicpromisc1 allow-all

# Allow VMs: Endast trafik från andra VMs
VBoxManage modifyvm "VM-Namn" --nicpromisc1 allow-vms

# Deny: Standard (ingen promiscuous mode)
VBoxManage modifyvm "VM-Namn" --nicpromisc1 deny
```

---

## USB och Hårdvaruåtkomst

### USB Passthrough

#### Förutsättningar
- **VirtualBox Extension Pack** installerat
- USB 2.0/3.0 stöd aktiverat i VM-inställningar

#### Installation av Extension Pack
```bash
# Ladda ner (matcha VirtualBox-version!)
wget https://download.virtualbox.org/virtualbox/7.0.14/Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack

# Installera
VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-7.0.14.vbox-extpack

# Verifiera
VBoxManage list extpacks
```

#### USB Filter - Automatisk anslutning

**Via GUI:**
```
Inställningar → USB → Klicka på +-ikonen → Välj enhet
```

**Via CLI:**
```bash
# Lista anslutna USB-enheter
VBoxManage list usbhost

# Output exempel:
# UUID: xxx-xxx-xxx
# VendorId: 0x1234 (1234)
# ProductId: 0x5678 (5678)
# Product: My USB Device

# Skapa filter
VBoxManage usbfilter add 0 \
  --target "VM-Namn" \
  --name "My USB Device" \
  --vendorid 1234 \
  --productid 5678
```

#### USB över nätverk (USB/IP)

Dela USB-enheter över nätverket.

**På värd-maskin (Linux):**
```bash
# Installera usbip
sudo apt install linux-tools-generic usbip

# Ladda kernel module
sudo modprobe usbip-core
sudo modprobe usbip-host

# Lista enheter
usbip list -l

# Dela enhet (t.ex. bus 1, device 5)
sudo usbip bind -b 1-5

# Starta server
sudo usbipd -D
```

**I VirtualBox VM:**
```bash
# Installera klient
sudo apt install usbip

# Anslut till värd
sudo usbip attach -r <värd-IP> -b 1-5
```

### Serieport (COM port) Forwarding

Ge VM åtkomst till serieportar.

```bash
# Pipe till fil
VBoxManage modifyvm "VM-Namn" \
  --uart1 0x3F8 4 \
  --uartmode1 file /path/to/output.log

# TCP server (lyssna på port 5555)
VBoxManage modifyvm "VM-Namn" \
  --uart1 0x3F8 4 \
  --uartmode1 tcpserver 5555

# Anslut till värd-serieport
VBoxManage modifyvm "VM-Namn" \
  --uart1 0x3F8 4 \
  --uartmode1 server /dev/ttyS0
```

### Raw Disk Access

Ge VM direkt åtkomst till fysiska diskar (FARLIGT - använd med försiktighet!)

#### Linux värd:
```bash
# Skapa VMDK som pekar på fysisk disk
VBoxManage createmedium disk \
  --filename /path/to/rawdisk.vmdk \
  --format VMDK \
  --variant RawDisk \
  --property RawDrive=/dev/sdb

# Anslut till VM
VBoxManage storageattach "VM-Namn" \
  --storagectl "SATA" \
  --port 1 \
  --device 0 \
  --type hdd \
  --medium /path/to/rawdisk.vmdk
```

**VARNING**: VM har full åtkomst till hela disken. Fel kan förstöra data!

#### Specifika partitioner endast:
```bash
# Skapa VMDK för partition /dev/sdb1
VBoxManage createmedium disk \
  --filename /path/to/partition.vmdk \
  --format VMDK \
  --variant RawDisk \
  --property RawDrive=/dev/sdb \
  --property Partitions=1
```

---

## VirtualBox CLI - VBoxManage

### Komplett VM-hantering via CLI

#### Lista VM:ar och info
```bash
# Lista alla VMs
VBoxManage list vms

# Lista körande VMs
VBoxManage list runningvms

# Detaljerad info
VBoxManage showvminfo "VM-Namn"

# Visa endast specifik info
VBoxManage showvminfo "VM-Namn" --machinereadable | grep memory
```

#### Skapa VM från scratch
```bash
# Skapa VM
VBoxManage createvm \
  --name "MyVM" \
  --ostype "Ubuntu_64" \
  --register

# Sätt minne och CPU
VBoxManage modifyvm "MyVM" --memory 4096 --cpus 2

# Skapa virtuell disk
VBoxManage createmedium disk \
  --filename ~/VirtualBox\ VMs/MyVM/MyVM.vdi \
  --size 50000 \
  --format VDI

# Lägg till storage controller
VBoxManage storagectl "MyVM" \
  --name "SATA Controller" \
  --add sata \
  --bootable on

# Anslut disk
VBoxManage storageattach "MyVM" \
  --storagectl "SATA Controller" \
  --port 0 \
  --device 0 \
  --type hdd \
  --medium ~/VirtualBox\ VMs/MyVM/MyVM.vdi

# Anslut ISO
VBoxManage storageattach "MyVM" \
  --storagectl "SATA Controller" \
  --port 1 \
  --device 0 \
  --type dvddrive \
  --medium /path/to/ubuntu.iso

# Konfigurera nätverk
VBoxManage modifyvm "MyVM" --nic1 nat

# Starta VM
VBoxManage startvm "MyVM" --type headless
```

#### Kontrollera körande VM
```bash
# Pausa
VBoxManage controlvm "VM-Namn" pause

# Resume
VBoxManage controlvm "VM-Namn" resume

# Reset
VBoxManage controlvm "VM-Namn" reset

# Poweroff (hård avstängning)
VBoxManage controlvm "VM-Namn" poweroff

# ACPI shutdown (mjuk avstängning)
VBoxManage controlvm "VM-Namn" acpipowerbutton

# Spara state (suspend)
VBoxManage controlvm "VM-Namn" savestate
```

#### Ändra VM-konfiguration
```bash
# Minne
VBoxManage modifyvm "VM-Namn" --memory 8192

# CPU
VBoxManage modifyvm "VM-Namn" --cpus 4

# Videominne
VBoxManage modifyvm "VM-Namn" --vram 128

# Aktivera 3D
VBoxManage modifyvm "VM-Namn" --accelerate3d on

# Boot order
VBoxManage modifyvm "VM-Namn" --boot1 dvd --boot2 disk --boot3 none --boot4 none

# Clipboard
VBoxManage modifyvm "VM-Namn" --clipboard bidirectional

# Drag and drop
VBoxManage modifyvm "VM-Namn" --draganddrop bidirectional
```

### Bulk Operations

#### Starta alla VMs med tag
```bash
#!/bin/bash
# Starta alla VMs vars namn börjar med "Server"

VBoxManage list vms | grep "Server" | while read -r line; do
    VM_NAME=$(echo "$line" | cut -d'"' -f2)
    echo "Starting $VM_NAME..."
    VBoxManage startvm "$VM_NAME" --type headless
done
```

#### Health check script
```bash
#!/bin/bash
# Kontrollera status för alla VMs

echo "VM Health Check - $(date)"
echo "================================"

VBoxManage list vms | while read -r line; do
    VM_NAME=$(echo "$line" | cut -d'"' -f2)

    # Status
    STATE=$(VBoxManage showvminfo "$VM_NAME" --machinereadable | grep "VMState=" | cut -d'"' -f2)

    # Minne
    MEMORY=$(VBoxManage showvminfo "$VM_NAME" --machinereadable | grep "^memory=" | cut -d'=' -f2)

    echo "$VM_NAME: $STATE (${MEMORY}MB RAM)"

    # Om running, visa CPU användning
    if [ "$STATE" == "running" ]; then
        CPU=$(VBoxManage metrics query "$VM_NAME" Guest/CPU/Load/User:avg | tail -1)
        echo "  CPU: $CPU"
    fi
done
```

---

## Automation och Scripting

### Vagrant Integration

Vagrant är ett verktyg för att automatisera VM-skapande och konfiguration.

#### Installation
```bash
# Ubuntu/Debian
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install vagrant
```

#### Grundläggande Vagrantfile
```ruby
# Vagrantfile
Vagrant.configure("2") do |config|
  # Bas-box
  config.vm.box = "ubuntu/focal64"

  # VM-inställningar
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
    vb.name = "My-Vagrant-VM"
  end

  # Nätverk
  config.vm.network "private_network", ip: "192.168.56.10"

  # Port forwarding
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Synkad mapp
  config.vm.synced_folder "./data", "/vagrant_data"

  # Provisioning
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y nginx
  SHELL
end
```

#### Användning
```bash
# Starta VM (skapar första gången)
vagrant up

# SSH in
vagrant ssh

# Stäng av
vagrant halt

# Förstör VM
vagrant destroy

# Återskapa från början
vagrant destroy -f && vagrant up
```

#### Multi-machine setup
```ruby
Vagrant.configure("2") do |config|
  # Web server
  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/focal64"
    web.vm.hostname = "web"
    web.vm.network "private_network", ip: "192.168.56.10"

    web.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

    web.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y nginx
    SHELL
  end

  # Database server
  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/focal64"
    db.vm.hostname = "db"
    db.vm.network "private_network", ip: "192.168.56.11"

    db.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end

    db.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y mysql-server
    SHELL
  end
end
```

### Packer för Image Building

Automatisera skapande av VM-images.

#### Exempel Packer template (JSON)
```json
{
  "builders": [
    {
      "type": "virtualbox-iso",
      "guest_os_type": "Ubuntu_64",
      "iso_url": "https://releases.ubuntu.com/20.04/ubuntu-20.04.6-live-server-amd64.iso",
      "iso_checksum": "sha256:...",
      "ssh_username": "vagrant",
      "ssh_password": "vagrant",
      "ssh_timeout": "20m",
      "shutdown_command": "echo 'vagrant' | sudo -S shutdown -P now",
      "disk_size": 40000,
      "memory": 2048,
      "cpus": 2,
      "http_directory": "http",
      "boot_wait": "5s",
      "boot_command": [
        "<esc><wait>",
        "install <wait>",
        "preseed/url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/preseed.cfg <wait>",
        "auto <wait>",
        "<enter><wait>"
      ]
    }
  ],
  "provisioners": [
    {
      "type": "shell",
      "inline": [
        "sudo apt-get update",
        "sudo apt-get upgrade -y",
        "sudo apt-get install -y build-essential"
      ]
    }
  ],
  "post-processors": [
    {
      "type": "vagrant",
      "output": "ubuntu-custom.box"
    }
  ]
}
```

### Ansible för VM-konfiguration

Automatisera konfiguration efter VM-skapande.

#### Ansible inventory
```ini
# inventory.ini
[webservers]
web1 ansible_host=192.168.56.10 ansible_user=vagrant

[databases]
db1 ansible_host=192.168.56.11 ansible_user=vagrant

[all:vars]
ansible_ssh_private_key_file=~/.vagrant.d/insecure_private_key
```

#### Playbook
```yaml
# playbook.yml
---
- hosts: webservers
  become: yes
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Copy website
      copy:
        src: files/index.html
        dest: /var/www/html/index.html

- hosts: databases
  become: yes
  tasks:
    - name: Install MySQL
      apt:
        name: mysql-server
        state: present

    - name: Start MySQL
      service:
        name: mysql
        state: started
        enabled: yes
```

#### Körning
```bash
ansible-playbook -i inventory.ini playbook.yml
```

---

## Remote Desktop och Headless Mode

### VRDE (VirtualBox Remote Desktop Extension)

Tillåter fjärråtkomst till VM via RDP.

#### Aktivera VRDE
```bash
# Aktivera
VBoxManage modifyvm "VM-Namn" --vrde on

# Sätt port (default: 3389)
VBoxManage modifyvm "VM-Namn" --vrdeport 5000

# Sätt authentication
VBoxManage modifyvm "VM-Namn" --vrdeauthtype external

# Tillåt flera anslutningar
VBoxManage modifyvm "VM-Namn" --vrdemulticon on
```

#### Anslut från klient
```bash
# Linux: rdesktop
rdesktop localhost:5000

# Windows: mstsc
# Ange: localhost:5000

# Mac: Microsoft Remote Desktop
# Server: localhost:5000
```

### Headless Mode

Kör VM utan GUI - perfekt för servrar.

```bash
# Starta headless
VBoxManage startvm "VM-Namn" --type headless

# Eller utan output alls
VBoxManage startvm "VM-Namn" --type headless > /dev/null 2>&1 &
```

#### SSH Access Setup

**I VM (Linux):**
```bash
# Installera SSH server
sudo apt install openssh-server

# Starta och aktivera
sudo systemctl start ssh
sudo systemctl enable ssh
```

**Port forwarding för SSH:**
```bash
VBoxManage modifyvm "VM-Namn" --natpf1 "ssh,tcp,,2222,,22"
```

**Anslut:**
```bash
ssh -p 2222 user@localhost
```

### VBoxHeadless Daemon

Kör VM som bakgrunds-daemon.

```bash
# Starta som daemon
VBoxHeadless --startvm "VM-Namn" &

# Med VRDE på specifik port
VBoxHeadless --startvm "VM-Namn" --vrde on --vrdeport 5000 &
```

### Systemd Service för auto-start

**Skapa service fil:**
```bash
sudo nano /etc/systemd/system/vbox-vm@.service
```

```ini
[Unit]
Description=VirtualBox VM %i
After=network.target vboxdrv.service
Before=runlevel2.target runlevel3.target runlevel4.target runlevel5.target shutdown.target

[Service]
User=vboxuser
Group=vboxusers
Type=forking
Restart=no
TimeoutSec=5min
IgnoreSIGPIPE=no
KillMode=process
GuessMainPID=no
RemainAfterExit=yes

ExecStart=/usr/bin/VBoxManage startvm %i --type headless
ExecStop=/usr/bin/VBoxManage controlvm %i acpipowerbutton

[Install]
WantedBy=multi-user.target
```

**Aktivera:**
```bash
# Ladda om systemd
sudo systemctl daemon-reload

# Aktivera för specifik VM
sudo systemctl enable vbox-vm@"VM-Namn"

# Starta
sudo systemctl start vbox-vm@"VM-Namn"

# Status
sudo systemctl status vbox-vm@"VM-Namn"
```

---

## Virtuella Diskar - Avancerat

### Disk Typer och Format

**VDI**: VirtualBox native format
**VMDK**: VMware compatible
**VHD**: Microsoft Hyper-V compatible
**VHDX**: Modern Hyper-V format
**HDD**: Parallels Desktop format

### Konvertera mellan format
```bash
# VDI till VMDK
VBoxManage clonemedium disk \
  source.vdi target.vmdk \
  --format VMDK

# VMDK till VDI
VBoxManage clonemedium disk \
  source.vmdk target.vdi \
  --format VDI

# VDI till VHD
VBoxManage clonemedium disk \
  source.vdi target.vhd \
  --format VHD
```

### Resize Disk

```bash
# Öka disk storlek
VBoxManage modifymedium disk /path/to/disk.vdi --resize 100000

# (100000 MB = ~100 GB)
```

**Efter resize - expandera partition i gäst:**
```bash
# Linux
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1

# Eller för LVM
sudo pvresize /dev/sda1
sudo lvextend -l +100%FREE /dev/mapper/vg-root
sudo resize2fs /dev/mapper/vg-root
```

### Komprimera Disk (Reclaim Space)

**Steg 1: I gäst-VM (Linux)**
```bash
# Nollställ oanvänt utrymme
sudo dd if=/dev/zero of=/empty bs=1M
sudo rm -f /empty

# Stäng av VM
sudo poweroff
```

**Steg 2: På värd**
```bash
# Komprimera VDI
VBoxManage modifymedium disk /path/to/disk.vdi --compact
```

### Multi-attach Disks (Delad disk)

Dela en disk mellan flera VMs (READ-ONLY).

```bash
# Skapa delad disk
VBoxManage createmedium disk \
  --filename /path/to/shared.vdi \
  --size 10000 \
  --format VDI \
  --variant Standard

# Gör multi-attach (immutable eller shareable)
VBoxManage modifymedium disk /path/to/shared.vdi \
  --type shareable

# Anslut till flera VMs
VBoxManage storageattach "VM1" \
  --storagectl "SATA" \
  --port 1 \
  --device 0 \
  --type hdd \
  --medium /path/to/shared.vdi \
  --mtype shareable

VBoxManage storageattach "VM2" \
  --storagectl "SATA" \
  --port 1 \
  --device 0 \
  --type hdd \
  --medium /path/to/shared.vdi \
  --mtype shareable
```

**VARNING**: Båda VMs kan skriva - filsystemkorruption kan ske! Använd endast med cluster-aware filsystem (GFS2, OCFS2) eller read-only.

### Differencing Disks

Skapa delta-disk för ändringar (likt snapshots men för diskar).

```bash
# Bas-disk (read-only)
VBoxManage modifymedium disk /path/to/base.vdi --type immutable

# Skapa differencing disk
VBoxManage createmedium disk \
  --filename /path/to/diff.vdi \
  --diffparent /path/to/base.vdi

# Alla ändringar skrivs till diff.vdi
```

### Disk Encryption

Kryptera hela VM-disken.

```bash
# Skapa krypterad disk
VBoxManage encryptmedium /path/to/disk.vdi \
  --newpassword - \
  --cipher "AES-XTS256-PLAIN64" \
  --newpasswordid "MySecureVM"

# Lösenord via stdin
echo "MySecretPassword" | VBoxManage encryptmedium /path/to/disk.vdi \
  --newpassword - \
  --cipher "AES-XTS256-PLAIN64" \
  --newpasswordid "MySecureVM"
```

**Starta krypterad VM:**
```bash
# GUI: Du får prompt för lösenord

# CLI: Ge lösenord
VBoxManage startvm "EncryptedVM" --type gui

# Lösenord via file
echo "MySecretPassword" > /tmp/password
VBoxManage setproperty encryptpasswordfile /tmp/password
VBoxManage startvm "EncryptedVM" --type headless
rm /tmp/password
```

### iSCSI Targets

Använd nätverks-baserad storage.

```bash
# Lägg till iSCSI server
VBoxManage storageattach "VM-Namn" \
  --storagectl "SCSI" \
  --port 2 \
  --device 0 \
  --type hdd \
  --medium iscsi \
  --server 192.168.1.100 \
  --target iqn.2024.com.example:storage.target1 \
  --initiator iqn.2024.com.example:vm1 \
  --lun 0
```

---

## GPU Passthrough och PCI Passthrough

### GPU Acceleration i VirtualBox

VirtualBox har begränsat GPU-stöd. För riktig GPU passthrough behövs KVM/QEMU. Men VirtualBox kan:

#### 1. 3D Acceleration (emulerad)
```bash
VBoxManage modifyvm "VM-Namn" --accelerate3d on
VBoxManage modifyvm "VM-Namn" --vram 256
```

**Begränsningar:**
- Endast för desktop-grafik
- Inget CUDA/OpenCL stöd
- Begränsad prestanda

#### 2. 2D Video Acceleration
```bash
VBoxManage modifyvm "VM-Namn" --accelerate2dvideo on
```

### PCI Passthrough (Experimentellt)

**VARNING**: Detta är experimentellt och fungerar endast på Linux-värdar med specifik hårdvara.

**Förutsättningar:**
- Intel VT-d eller AMD IOMMU aktiverat i BIOS
- Linux värd med IOMMU aktiverat

**Aktivera IOMMU i Linux:**
```bash
# Redigera GRUB
sudo nano /etc/default/grub

# Lägg till:
# För Intel:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash intel_iommu=on iommu=pt"

# För AMD:
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amd_iommu=on iommu=pt"

# Uppdatera GRUB
sudo update-grub
sudo reboot
```

**Hitta PCI device:**
```bash
# Lista PCI devices
lspci -nn

# Exempel output:
# 01:00.0 VGA compatible controller [0300]: NVIDIA Corporation ... [10de:1234]
```

**Lägg till PCI device till VM:**
```bash
VBoxManage modifyvm "VM-Namn" \
  --pciattach 01:00.0
```

**VIKTIGT**:
- Enhet måste vara ledig (inte använd av värd)
- Kan kräva blacklisting av drivers på värd
- Fungerar inte alltid - hårdvara-beroende

---

## Säkerhet och Kryptering

### VM Disk Encryption (Detaljerat)

#### Full Disk Encryption
```bash
# Kryptera befintlig disk
VBoxManage encryptmedium /path/to/disk.vdi \
  --newpassword - \
  --cipher "AES-XTS256-PLAIN64" \
  --newpasswordid "Production-VM-001"
```

**Supported ciphers:**
- `AES-XTS128-PLAIN64` (snabbare, mindre säker)
- `AES-XTS256-PLAIN64` (långsammare, mer säker) **Rekommenderat**

#### Password Management
```bash
# Ändra lösenord
VBoxManage encryptmedium /path/to/disk.vdi \
  --oldpassword - \
  --newpassword - \
  --cipher "AES-XTS256-PLAIN64" \
  --newpasswordid "Production-VM-001"

# Ta bort kryptering (dekryptera)
VBoxManage encryptmedium /path/to/disk.vdi \
  --oldpassword -
```

#### Password Rotation Script
```bash
#!/bin/bash
# Rotera krypteringslösenord för VM

VM_NAME="SecureVM"
DISK_PATH="/path/to/disk.vdi"
OLD_PASS_FILE="/secure/old_password"
NEW_PASS_FILE="/secure/new_password"

# Stoppa VM
VBoxManage controlvm "$VM_NAME" acpipowerbutton
sleep 30

# Vänta tills stoppad
while VBoxManage showvminfo "$VM_NAME" | grep -q "running"; do
    sleep 5
done

# Rotera lösenord
VBoxManage encryptmedium "$DISK_PATH" \
  --oldpassword "$(cat $OLD_PASS_FILE)" \
  --newpassword "$(cat $NEW_PASS_FILE)" \
  --cipher "AES-XTS256-PLAIN64" \
  --newpasswordid "${VM_NAME}-$(date +%Y%m%d)"

# Uppdatera lösenordsfiler
mv "$NEW_PASS_FILE" "$OLD_PASS_FILE"

# Starta VM
VBoxManage setproperty encryptpasswordfile "$OLD_PASS_FILE"
VBoxManage startvm "$VM_NAME" --type headless

echo "Password rotation complete"
```

### Secure Boot

Aktivera UEFI Secure Boot.

```bash
# Aktivera EFI
VBoxManage modifyvm "VM-Namn" --firmware efi

# Aktivera Secure Boot
VBoxManage modifyvm "VM-Namn" --secure-boot on

# TPM (Trusted Platform Module) - VirtualBox 7.0+
VBoxManage modifyvm "VM-Namn" --tpm-type 2.0
```

### Nätverkssäkerhet

#### Isolera VM helt
```bash
# Ingen nätverksåtkomst
VBoxManage modifyvm "VM-Namn" --nic1 none

# Eller Internal network utan router
VBoxManage modifyvm "VM-Namn" --nic1 intnet --intnet1 "Isolated"
```

#### Firewall rules för Host-only
```bash
# På Linux-värd: Blockera host-only trafik med iptables
sudo iptables -A FORWARD -i vboxnet0 -o eth0 -j DROP
sudo iptables -A FORWARD -i eth0 -o vboxnet0 -j DROP

# Tillåt endast specifik VM
sudo iptables -A FORWARD -s 192.168.56.10 -i vboxnet0 -o eth0 -j ACCEPT
```

### Teleporter (VM Migration) över säker kanal

```bash
# Destination VM (lyssnar)
VBoxManage modifyvm "DestVM" --teleporter on --teleporterport 6000

# Source VM (skickar)
VBoxManage controlvm "SourceVM" teleport \
  --host 192.168.1.100 \
  --port 6000 \
  --password "MigrationSecret123"
```

**För säker migration via SSH tunnel:**
```bash
# Setup SSH tunnel
ssh -L 6000:localhost:6000 user@remote-host

# På remote: Starta dest VM i teleporter mode
VBoxManage modifyvm "DestVM" --teleporter on --teleporterport 6000
VBoxManage startvm "DestVM" --type headless

# Lokalt: Teleportera
VBoxManage controlvm "SourceVM" teleport \
  --host localhost \
  --port 6000 \
  --password "MigrationSecret123"
```

---

## Prestanda-optimering Avancerat

### CPU Performance Tuning

#### CPU Execution Cap
```bash
# Begränsa CPU till 80% (för att lämna utrymme åt värd)
VBoxManage modifyvm "VM-Namn" --cpuexecutioncap 80

# Max prestanda
VBoxManage modifyvm "VM-Namn" --cpuexecutioncap 100
```

#### CPU Hot-plugging
```bash
# Aktivera CPU hotplug (lägg till CPU under körning)
VBoxManage modifyvm "VM-Namn" --cpuhotplug on

# Lägg till CPU medan VM körs
VBoxManage modifyvm "VM-Namn" --cpus 4
VBoxManage controlvm "VM-Namn" plugcpu 3  # Lägg till CPU #3
```

#### NUMA (Non-Uniform Memory Access)
```bash
# För stora VMs med många CPUs
VBoxManage modifyvm "VM-Namn" --cpus 16 --numa on
```

### Memory Performance

#### Large Pages
```bash
# Använd large pages för bättre minneshantering
VBoxManage modifyvm "VM-Namn" --largepages on
```

**Linux värd: Aktivera hugepages**
```bash
# Allokera hugepages
sudo sysctl -w vm.nr_hugepages=1024

# Permanent
echo "vm.nr_hugepages=1024" | sudo tee -a /etc/sysctl.conf

# Ge VirtualBox rättigheter
sudo usermod -aG hugetlb $USER
```

#### Page Fusion (KSM - Kernel Samepage Merging)
```bash
# Aktivera Page Fusion (delar identiska minnesidor mellan VMs)
VBoxManage modifyvm "VM-Namn" --pagefusion on
```

### Disk I/O Optimization

#### I/O APIC och HPET
```bash
# Aktivera för bättre I/O prestanda
VBoxManage modifyvm "VM-Namn" --ioapic on
VBoxManage modifyvm "VM-Namn" --hpet on
```

#### Host I/O Cache
```bash
# Aktivera för disk controller
VBoxManage storagectl "VM-Namn" \
  --name "SATA" \
  --hostiocache on
```

#### SSD Flag
```bash
# Markera disk som SSD (för TRIM support)
VBoxManage storageattach "VM-Namn" \
  --storagectl "SATA" \
  --port 0 \
  --device 0 \
  --type hdd \
  --medium /path/to/disk.vdi \
  --nonrotational on \
  --discard on
```

#### I/O Bandwidth Limiting
```bash
# Skapa I/O limit group
VBoxManage bandwidthctl "VM-Namn" add "Disk1Limit" \
  --type disk \
  --limit 50m  # 50 MB/s

# Applicera på disk
VBoxManage storageattach "VM-Namn" \
  --storagectl "SATA" \
  --port 0 \
  --device 0 \
  --type hdd \
  --medium /path/to/disk.vdi \
  --bandwidthgroup "Disk1Limit"
```

### Paravirtualization Providers

Olika providers ger olika prestanda beroende på gäst-OS.

```bash
# Lista providers
VBoxManage modifyvm "VM-Namn" --paravirtprovider

# För Linux-gäster: KVM (bäst)
VBoxManage modifyvm "VM-Namn" --paravirtprovider kvm

# För Windows: Hyper-V eller Default
VBoxManage modifyvm "VM-Namn" --paravirtprovider hyperv

# För äldre system: Legacy
VBoxManage modifyvm "VM-Namn" --paravirtprovider legacy

# Automatiskt val
VBoxManage modifyvm "VM-Namn" --paravirtprovider default
```

### Grafik Performance

```bash
# Maximal grafik-prestanda
VBoxManage modifyvm "VM-Namn" --vram 256
VBoxManage modifyvm "VM-Namn" --accelerate3d on
VBoxManage modifyvm "VM-Namn" --accelerate2dvideo on
VBoxManage modifyvm "VM-Namn" --graphicscontroller vmsvga
```

### Metrics och Monitoring

```bash
# Aktivera metrics
VBoxManage metrics setup --period 1 --samples 60 "VM-Namn"

# Visa CPU usage
VBoxManage metrics query "VM-Namn" Guest/CPU/Load/User

# Visa RAM usage
VBoxManage metrics query "VM-Namn" Guest/RAM/Usage/Used

# Alla metrics
VBoxManage metrics query "VM-Namn"

# Lista available metrics
VBoxManage metrics list "VM-Namn"
```

#### Continuous monitoring script
```bash
#!/bin/bash
VM_NAME="MonitoredVM"

while true; do
    clear
    echo "=== VM Metrics: $VM_NAME ==="
    echo "Time: $(date)"
    echo

    # CPU
    CPU=$(VBoxManage metrics query "$VM_NAME" Guest/CPU/Load/User:avg | tail -1 | awk '{print $2}')
    echo "CPU Usage: ${CPU}%"

    # RAM
    RAM=$(VBoxManage metrics query "$VM_NAME" Guest/RAM/Usage/Used:avg | tail -1 | awk '{print $2}')
    echo "RAM Usage: ${RAM} kB"

    # Disk
    DISK_READ=$(VBoxManage metrics query "$VM_NAME" Disk/Usage/Read:avg | tail -1 | awk '{print $2}')
    DISK_WRITE=$(VBoxManage metrics query "$VM_NAME" Disk/Usage/Write:avg | tail -1 | awk '{print $2}')
    echo "Disk Read: ${DISK_READ} B/s"
    echo "Disk Write: ${DISK_WRITE} B/s"

    sleep 5
done
```

---

## Nätverk mellan VM:ar - Avancerade Scenarier

### Scenario: Kubernetes Cluster i VirtualBox

Bygg ett 3-node Kubernetes cluster.

```bash
#!/bin/bash
# Skapa K8s cluster

# Skapa host-only network
VBoxManage hostonlyif create
VBoxManage hostonlyif ipconfig vboxnet0 --ip 192.168.56.1 --netmask 255.255.255.0

# Skapa master node
VBoxManage createvm --name "k8s-master" --ostype "Ubuntu_64" --register
VBoxManage modifyvm "k8s-master" --memory 4096 --cpus 2
VBoxManage modifyvm "k8s-master" --nic1 nat --nic2 hostonly --hostonlyadapter2 vboxnet0

# Skapa disk för master
VBoxManage createmedium disk --filename ~/VMs/k8s-master.vdi --size 40000
VBoxManage storagectl "k8s-master" --name "SATA" --add sata --bootable on
VBoxManage storageattach "k8s-master" --storagectl "SATA" --port 0 --device 0 --type hdd --medium ~/VMs/k8s-master.vdi

# Skapa 2 worker nodes
for i in 1 2; do
    VBoxManage createvm --name "k8s-worker${i}" --ostype "Ubuntu_64" --register
    VBoxManage modifyvm "k8s-worker${i}" --memory 2048 --cpus 2
    VBoxManage modifyvm "k8s-worker${i}" --nic1 nat --nic2 hostonly --hostonlyadapter2 vboxnet0

    VBoxManage createmedium disk --filename ~/VMs/k8s-worker${i}.vdi --size 40000
    VBoxManage storagectl "k8s-worker${i}" --name "SATA" --add sata --bootable on
    VBoxManage storageattach "k8s-worker${i}" --storagectl "SATA" --port 0 --device 0 --type hdd --medium ~/VMs/k8s-worker${i}.vdi
done

echo "K8s cluster VMs created. Now install Ubuntu and configure K8s."
```

**Network plan:**
- `eth0` (NAT): Internet access för package installation
- `eth1` (Host-only): Cluster communication
  - Master: 192.168.56.10
  - Worker1: 192.168.56.11
  - Worker2: 192.168.56.12

### Scenario: DMZ med Firewall

**Topology:**
```
Internet (Bridged)
    |
[Firewall VM]
    |
    +-- DMZ (Internal Network: dmz)
    |     |
    |     +-- Web Server
    |     +-- Mail Server
    |
    +-- LAN (Internal Network: lan)
          |
          +-- Desktop VMs
```

```bash
# Firewall VM
VBoxManage modifyvm "Firewall" \
  --nic1 bridged --bridgeadapter1 eth0 \
  --nic2 intnet --intnet2 "dmz" \
  --nic3 intnet --intnet3 "lan"

# DMZ Servers
VBoxManage modifyvm "WebServer" --nic1 intnet --intnet1 "dmz"
VBoxManage modifyvm "MailServer" --nic1 intnet --intnet1 "dmz"

# LAN Clients
VBoxManage modifyvm "Desktop1" --nic1 intnet --intnet1 "lan"
VBoxManage modifyvm "Desktop2" --nic1 intnet --intnet1 "lan"
```

**I Firewall VM (Linux):**
```bash
# Interfaces:
# eth0: WAN (Bridged)
# eth1: DMZ (10.0.1.0/24)
# eth2: LAN (10.0.2.0/24)

# Enable forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# NAT for outbound traffic
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# DMZ rules
sudo iptables -A FORWARD -i eth0 -o eth1 -p tcp --dport 80 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o eth1 -p tcp --dport 443 -j ACCEPT
sudo iptables -A FORWARD -i eth1 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT

# LAN rules (full outbound)
sudo iptables -A FORWARD -i eth2 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o eth2 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Block DMZ to LAN
sudo iptables -A FORWARD -i eth1 -o eth2 -j DROP

# Allow LAN to DMZ (specific services)
sudo iptables -A FORWARD -i eth2 -o eth1 -p tcp --dport 80 -j ACCEPT
```

### Scenario: Load Balancer + Backend Pool

```bash
# Load Balancer VM
VBoxManage modifyvm "LoadBalancer" \
  --nic1 bridged --bridgeadapter1 eth0 \
  --nic2 intnet --intnet2 "backend"

# Backend VMs
for i in {1..3}; do
    VBoxManage modifyvm "Backend${i}" \
      --nic1 intnet --intnet1 "backend"
done
```

**Load Balancer (nginx):**
```nginx
upstream backend {
    server 10.0.99.11:8080;
    server 10.0.99.12:8080;
    server 10.0.99.13:8080;
}

server {
    listen 80;

    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Backup och Disaster Recovery

### Export/Import (OVA/OVF)

#### Export VM
```bash
# Basic export
VBoxManage export "VM-Namn" --output /backup/vm-backup.ova

# Med manifest (checksum)
VBoxManage export "VM-Namn" \
  --output /backup/vm-backup.ova \
  --manifest

# Med metadata
VBoxManage export "VM-Namn" \
  --output /backup/vm-backup.ova \
  --manifest \
  --vsys 0 \
  --product "My Application" \
  --producturl "https://example.com" \
  --vendor "My Company" \
  --version "2.0" \
  --description "Production server backup $(date +%Y-%m-%d)"
```

#### Import VM
```bash
# Basic import
VBoxManage import /backup/vm-backup.ova

# Dry-run (visa vad som skulle importeras)
VBoxManage import /backup/vm-backup.ova --dry-run

# Custom options
VBoxManage import /backup/vm-backup.ova \
  --vsys 0 \
  --vmname "Restored-VM" \
  --memory 8192 \
  --cpus 4
```

### Automated Backup Script

```bash
#!/bin/bash
# VirtualBox Backup Script

BACKUP_DIR="/mnt/backups/virtualbox"
VM_LIST=("ProductionVM" "DatabaseVM" "WebServer")
RETENTION_DAYS=30
DATE=$(date +%Y%m%d-%H%M%S)

# Create backup directory
mkdir -p "$BACKUP_DIR"

for VM in "${VM_LIST[@]}"; do
    echo "Backing up $VM..."

    # Get VM state
    STATE=$(VBoxManage showvminfo "$VM" --machinereadable | grep "VMState=" | cut -d'"' -f2)

    # If running, take snapshot
    if [ "$STATE" == "running" ]; then
        echo "  VM is running, taking live snapshot..."
        VBoxManage snapshot "$VM" take "backup-$DATE" --live
        SNAPSHOT="backup-$DATE"
    else
        SNAPSHOT=""
    fi

    # Export
    echo "  Exporting to OVA..."
    VBoxManage export "$VM" \
      --output "$BACKUP_DIR/${VM}-${DATE}.ova" \
      --manifest \
      --vsys 0 \
      --description "Backup created on $(date)"

    # Delete snapshot if created
    if [ -n "$SNAPSHOT" ]; then
        echo "  Removing backup snapshot..."
        VBoxManage snapshot "$VM" delete "$SNAPSHOT"
    fi

    # Compress
    echo "  Compressing..."
    gzip "$BACKUP_DIR/${VM}-${DATE}.ova"

    echo "  $VM backup complete"
done

# Cleanup old backups
echo "Cleaning up backups older than $RETENTION_DAYS days..."
find "$BACKUP_DIR" -name "*.ova.gz" -mtime +$RETENTION_DAYS -delete

echo "Backup complete!"
```

### Incremental Backups med rsync

```bash
#!/bin/bash
# Incremental backup of VM disks

BACKUP_DIR="/mnt/backups/vbox-incremental"
VM_DIR="$HOME/VirtualBox VMs"
DATE=$(date +%Y%m%d)

# Create dated backup directory
BACKUP_TARGET="$BACKUP_DIR/$DATE"
mkdir -p "$BACKUP_TARGET"

# Link to previous backup for incremental
LATEST=$(ls -1d "$BACKUP_DIR"/* | grep -v "$DATE" | sort | tail -1)

if [ -n "$LATEST" ]; then
    echo "Using $LATEST as reference for incremental backup"

    # Rsync with hardlinks for unchanged files
    rsync -av --link-dest="$LATEST" \
      "$VM_DIR/" \
      "$BACKUP_TARGET/"
else
    echo "No previous backup found, performing full backup"
    rsync -av "$VM_DIR/" "$BACKUP_TARGET/"
fi

# Keep only last 7 daily backups
ls -1d "$BACKUP_DIR"/* | sort | head -n -7 | xargs rm -rf

echo "Incremental backup complete: $BACKUP_TARGET"
```

### Disaster Recovery Plan

**1. Regular snapshots:**
```bash
# Daily snapshot cron
# /etc/cron.daily/vbox-snapshot
#!/bin/bash
VBoxManage snapshot "CriticalVM" take "daily-$(date +%Y%m%d)" --description "Automated daily snapshot"

# Keep only 7 days
SNAPSHOTS=$(VBoxManage snapshot "CriticalVM" list --machinereadable | grep SnapshotName | grep "daily-" | cut -d'"' -f2 | head -n -7)
for SNAP in $SNAPSHOTS; do
    VBoxManage snapshot "CriticalVM" delete "$SNAP"
done
```

**2. Offsite backup:**
```bash
#!/bin/bash
# Upload backup to remote server

LOCAL_BACKUP="/mnt/backups/virtualbox"
REMOTE_SERVER="backup-server.example.com"
REMOTE_USER="backup"
REMOTE_PATH="/backups/vbox"

# Sync to remote
rsync -avz --delete \
  -e "ssh -i /root/.ssh/backup_key" \
  "$LOCAL_BACKUP/" \
  "${REMOTE_USER}@${REMOTE_SERVER}:${REMOTE_PATH}/"
```

**3. Recovery procedure:**
```bash
#!/bin/bash
# Recover VM from backup

BACKUP_FILE="/backup/ProductionVM-20240115.ova.gz"

# Decompress
gunzip "$BACKUP_FILE"

# Import
VBoxManage import "${BACKUP_FILE%.gz}" \
  --vsys 0 \
  --vmname "ProductionVM-Recovered"

# Start
VBoxManage startvm "ProductionVM-Recovered" --type headless

echo "VM recovered and started"
```

---

## Extension Pack och Tillägg

### VirtualBox Extension Pack

Tillhandahåller:
- USB 2.0/3.0 support
- VirtualBox Remote Desktop Protocol (VRDP)
- Disk encryption
- NVMe storage
- PXE boot för Intel cards

#### Installation
```bash
# Ladda ner (matcha version!)
VBOX_VERSION=$(vboxmanage --version | cut -d'r' -f1)
wget "https://download.virtualbox.org/virtualbox/${VBOX_VERSION}/Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-extpack"

# Installera
VBoxManage extpack install "Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-extpack" --accept-license=sha256

# Verifiera
VBoxManage list extpacks
```

#### Avinstallera
```bash
VBoxManage extpack uninstall "Oracle VM VirtualBox Extension Pack"
```

### Guest Additions Advanced

#### Installation från kommandorad

**Linux gäst:**
```bash
# Montera Guest Additions ISO
sudo mount /dev/cdrom /mnt

# Installera
cd /mnt
sudo ./VBoxLinuxAdditions.run

# Unmount
cd ~
sudo umount /mnt

# Starta om
sudo reboot
```

**Windows gäst:**
```cmd
# Kör från CD
D:\VBoxWindowsAdditions.exe /S

# /S = silent installation
```

#### Automatisk installation via script

**Vagrantfile exempel:**
```ruby
config.vm.provision "shell", inline: <<-SHELL
  # Installera dependencies
  apt-get update
  apt-get install -y build-essential dkms linux-headers-$(uname -r)

  # Montera och installera Guest Additions
  mkdir -p /mnt/cdrom
  mount /dev/cdrom /mnt/cdrom
  sh /mnt/cdrom/VBoxLinuxAdditions.run --nox11
  umount /mnt/cdrom
SHELL
```

#### Shared Folders Advanced

```bash
# Skapa delad mapp med specifika rättigheter
VBoxManage sharedfolder add "VM-Namn" \
  --name "projects" \
  --hostpath "/home/user/projects" \
  --automount \
  --auto-mount-point "/mnt/projects"

# I gäst: lägg till user i vboxsf-gruppen
sudo usermod -aG vboxsf $USER

# Manuell montering med specifika options
sudo mount -t vboxsf -o uid=1000,gid=1000,dmode=775,fmode=664 projects /mnt/projects
```

---

## Troubleshooting Avancerat

### Kernel Panic / Boot Issues

#### Enable verbose logging
```bash
# Aktivera seriell port för kernel output
VBoxManage modifyvm "VM-Namn" --uart1 0x3F8 4
VBoxManage modifyvm "VM-Namn" --uartmode1 file /tmp/vm-serial.log

# I VM boot parameters (GRUB), lägg till:
# console=ttyS0,115200

# Läs logs
tail -f /tmp/vm-serial.log
```

#### Repair Mode
```bash
# Boot från ISO i rescue mode
VBoxManage storageattach "VM-Namn" \
  --storagectl "IDE" \
  --port 1 \
  --device 0 \
  --type dvddrive \
  --medium /path/to/ubuntu.iso

# Ändra boot order
VBoxManage modifyvm "VM-Namn" --boot1 dvd --boot2 disk
```

### Nätverksproblem - Deep Dive

#### Packet capture
```bash
# Aktivera trace på nätverksadapter
VBoxManage modifyvm "VM-Namn" \
  --nictrace1 on \
  --nictracefile1 /tmp/vm-network.pcap

# Starta VM och reproducera problem

# Analysera med tcpdump eller Wireshark
tcpdump -r /tmp/vm-network.pcap

# Inaktivera trace
VBoxManage modifyvm "VM-Namn" --nictrace1 off
```

#### DNS resolution issues
```bash
# Använd custom DNS i NAT network
VBoxManage modifyvm "VM-Namn" \
  --natdnshostresolver1 on \
  --natdnsproxy1 on

# Eller specifik DNS server
VBoxManage modifyvm "VM-Namn" \
  --natdnshostresolver1 off

# I VM, konfigurera manuellt:
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

### Prestanda-problem - Diagnostik

#### VM CPU hogs
```bash
# Inside VM: Hitta processer med hög CPU
top -b -n 1 | head -20

# På värd: Se vilka VMs använder mest
ps aux | grep VBox | awk '{print $2, $3, $11}' | sort -k2 -rn
```

#### Disk I/O bottlenecks
```bash
# I VM: iostat
sudo apt install sysstat
iostat -x 1

# På värd: iotop
sudo iotop

# Kontrollera om disk är full
df -h
```

#### Memory leaks
```bash
# I VM: Memory usage över tid
free -h

# Hitta minneskrävande processer
ps aux --sort=-%mem | head -10

# På värd: VM memory stats
VBoxManage metrics query "VM-Namn" Guest/RAM/Usage/Used
```

### VM Won't Start

#### Check logs
```bash
# VM log location
LOG_FILE="$HOME/VirtualBox VMs/VM-Namn/Logs/VBox.log"

# Visa senaste error
grep -i error "$LOG_FILE" | tail -20

# Visa warnings
grep -i warning "$LOG_FILE" | tail -20
```

#### Common issues

**1. VT-x not available:**
```bash
# Check if enabled in BIOS
egrep -o '(vmx|svm)' /proc/cpuinfo

# Disable Hyper-V on Windows host
bcdedit /set hypervisorlaunchtype off
```

**2. Kernel driver not loaded:**
```bash
# Linux: reload vboxdrv
sudo /sbin/vboxconfig

# Or manually
sudo modprobe vboxdrv
```

**3. UUID conflicts:**
```bash
# Change UUID of disk
VBoxManage internalcommands sethduuid /path/to/disk.vdi

# Change VM UUID
VBoxManage internalcommands setvmuuid "VM-Namn"
```

### Corrupted VM

#### Repair config
```bash
# Backup original
cp "$HOME/VirtualBox VMs/VM-Namn/VM-Namn.vbox" \
   "$HOME/VirtualBox VMs/VM-Namn/VM-Namn.vbox.backup"

# VM config är XML - editera försiktigt
nano "$HOME/VirtualBox VMs/VM-Namn/VM-Namn.vbox"

# Eller återskapa från disk
VBoxManage createvm --name "VM-Recovered" --ostype "Ubuntu_64" --register
VBoxManage storagectl "VM-Recovered" --name "SATA" --add sata
VBoxManage storageattach "VM-Recovered" --storagectl "SATA" --port 0 --device 0 --type hdd --medium /path/to/existing.vdi
```

#### Repair disk
```bash
# Check disk integrity
VBoxManage showmediuminfo /path/to/disk.vdi

# Compact (might fix minor issues)
VBoxManage modifymedium disk /path/to/disk.vdi --compact

# Clone to new disk (might fix corruption)
VBoxManage clonemedium disk /path/to/corrupt.vdi /path/to/fixed.vdi
```

### Debug Mode

```bash
# Starta med debug logging
VBoxManage setextradata "VM-Namn" "VBoxInternal/Logging/Enabled" "1"

# Starta VM
VBoxManage startvm "VM-Namn"

# Inaktivera debug
VBoxManage setextradata "VM-Namn" "VBoxInternal/Logging/Enabled" "0"
```

---

## Sammanfattning

Denna avancerade manual har täckt:

✅ **Snapshots och Kloning** - Tidsmaskiner och VM-distribution
✅ **Avancerad Nätverk** - Multi-adapter, routing, VLANs
✅ **USB och Hårdvara** - Passthrough, serieportar, raw disk
✅ **VBoxManage CLI** - Fullständig kommandoradshantering
✅ **Automation** - Vagrant, Packer, Ansible integration
✅ **Remote Access** - VRDE, headless mode, SSH
✅ **Virtuella Diskar** - Encryption, resize, multi-attach
✅ **Säkerhet** - Disk encryption, Secure Boot, TPM
✅ **Prestanda** - CPU tuning, memory optimization, I/O
✅ **Komplex Nätverk** - Kubernetes, DMZ, load balancing
✅ **Backup & DR** - Export, incremental backups, recovery
✅ **Troubleshooting** - Deep diagnostics, repair procedures

### Nästa Steg

För att bli expert på VirtualBox:

1. **Praktisera** - Bygg egna lab-miljöer
2. **Automatisera** - Skriv scripts för återkommande uppgifter
3. **Experimentera** - Testa olika nätverkstopologier
4. **Dokumentera** - Skriv egna playbooks och procedurer
5. **Bidra** - Dela kunskap och lösningar med communityn

### Resurser

- **Officiell dokumentation**: https://www.virtualbox.org/manual/
- **Forum**: https://forums.virtualbox.org/
- **Bugtracker**: https://www.virtualbox.org/wiki/Bugtracker
- **Wiki**: https://www.virtualbox.org/wiki/

---

**Lycka till med din VirtualBox-mastery! 🚀**
