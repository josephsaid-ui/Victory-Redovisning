# 🐧 Nivå 2A: Terminal & Filsystem

**⏱️ Beräknad tid:** 30-45 minuter
**📚 Svårighetsgrad:** ⭐⭐ Nybörjare
**🎯 Förutsättningar:** Nivå 1 genomförd (Kali installerat)
**🎓 Lärdomsmål:** Navigera bekvämt i Linux-terminalen och förstå filsystemet

---

## 📋 Innehåll

1. [Vad är terminalen?](#-vad-är-terminalen)
2. [Öppna terminalen](#-öppna-terminalen)
3. [Bash basics](#-bash-basics)
4. [Linux filsystem-struktur](#-linux-filsystem-struktur)
5. [Navigeringskommandon](#-navigeringskommandon)
6. [Viktiga genvägar](#⌨️-viktiga-genvägar)
7. [Wildcards och pattern matching](#-wildcards-och-pattern-matching)
8. [Praktiska övningar](#-praktiska-övningar)
9. [Självtest](#-självtest-nivå-2a)

---

## 💻 Vad är terminalen?

### Definition

**Terminal** (även kallad "shell", "command-line", "CLI") är ett textbaserat interface för att kommunicera med operativsystemet.

```
┌──────────────────────────────────────────────────────────┐
│  WINDOWS                    vs    LINUX                  │
├──────────────────────────────────────────────────────────┤
│  Grafiskt (GUI)                  Terminal (CLI)          │
│  Klicka med musen               Skriv kommandon          │
│  Explorer-fönster               Textbaserat              │
│  cmd.exe / PowerShell           Bash / Zsh / Fish        │
└──────────────────────────────────────────────────────────┘
```

### Varför använda terminalen?

| Fördel | Förklaring | Exempel |
|--------|------------|---------|
| **⚡ Snabbare** | Kommandon är snabbare än klickande | `cd /var/log` istället för 5 klick |
| **🎯 Precision** | Exakt kontroll över vad som händer | `rm *.txt` tar bort alla .txt-filer |
| **🤖 Automation** | Skriv scripts som gör jobbet åt dig | Scanna 100 IPs med ett kommando |
| **💪 Power** | Vissa saker går BARA via terminal | Många pentest-verktyg är CLI-only |
| **🌍 Universal** | Fungerar på alla Linux-system | Samma kommandon överallt |
| **📝 Repeatable** | Copy-paste kommandon = konsekvent | Dela exakta instruktioner |

### Shell vs Terminal vs Console

**Ofta förvirrat - här är skillnaden:**

```
┌──────────────────────────────────────────────────────────┐
│  TERMINAL EMULATOR                                       │
│  (Programmet du ser - fönstret)                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │ kali@kali:~$                                       │  │
│  │ ↑                                                  │  │
│  │ SHELL (Bash/Zsh)                                   │  │
│  │ (Tolkar dina kommandon)                            │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘

TERMINAL = Fönstret/programmet (Gnome Terminal, Terminator, etc.)
SHELL = Språket/tolken (Bash, Zsh, Fish)
CONSOLE = Fysisk terminal (sällan använt idag)
```

**Populära shells:**

| Shell | Beskrivning | Default i Kali? |
|-------|-------------|-----------------|
| **Bash** | Bourne Again Shell - mest populär | ✅ Ja (tidigare) |
| **Zsh** | Z Shell - modernare, fler features | ✅ Ja (nuvarande default) |
| **Fish** | Friendly Interactive Shell - nybörjarvänlig | ❌ Nej (kan installeras) |
| **Sh** | Original shell - väldigt basic | ❌ Nej |

---

## 🚀 Öppna terminalen

### Metod 1: Genväg (snabbast)

```
Tryck: Ctrl + Alt + T
```

### Metod 2: Application Menu

```
Applications → System Tools → Terminal
```

### Metod 3: Högerklicka på skrivbordet

```
Högerklicka var som helst på desktop → "Open Terminal Here"
```

### Metod 4: Terminator (avancerad terminal)

```bash
# Installera Terminator (om inte redan installerat)
sudo apt install terminator -y

# Starta
terminator
```

**Terminator features:**
- Split screen (flera terminals i samma fönster)
- Tabs
- Drag-and-drop reordering

---

## 🎨 Bash basics

### Anatomy of the prompt

När du öppnar terminalen ser du något liknande:

```bash
┌──(kali㉿kali)-[~]
└─$
```

**Förklaring:**

```
┌──(kali㉿kali)-[~]
└─$
 │   │   │    │  │
 │   │   │    │  └─ Prompt symbol ($ = normal user, # = root)
 │   │   │    └──── Current directory (~ = home)
 │   │   └───────── Hostname (datornamn)
 │   └───────────── Username
 └───────────────── Decorative line (Kali's fancy prompt)
```

**Olika prompt-varianter:**

```bash
$                    # Basic user prompt
#                    # Root prompt (admin)
kali@kali:~$         # User@host:directory$
┌──(kali㉿kali)-[~]  # Kali's fancy Zsh prompt
└─$
```

### Root vs Normal User

| User Type | Prompt | Makt | När använda |
|-----------|--------|------|-------------|
| **Normal user** | `$` | Begränsad | Dagligt arbete |
| **Root (sudo)** | `#` | Full kontroll | Installation, systemändringar |

**🔴 VIKTIGT:** Kör ALLTID som normal user om inte kommandot kräver root!

```bash
# ❌ DÅLIGT - hela tiden som root
sudo su
# Nu är du root för allt (farligt!)

# ✅ BRA - sudo endast när behövs
ls /home/kali           # Normal user räcker
sudo apt install nmap   # Kräver root → använd sudo
```

### Grundläggande kommando-struktur

```
kommando [options] [argument]
   │        │          │
   │        │          └─ Vad ska kommandot arbeta på (filer, etc.)
   │        └──────────── Modifierar beteendet (-a, --help, etc.)
   └───────────────────── Själva programmet/kommandot
```

**Exempel:**

```bash
ls -la /home/kali
│  │   │
│  │   └─ Argument: vilken mapp att lista
│  └───── Options: -l (long format), -a (all files including hidden)
└──────── Command: ls (list)
```

### Hjälp-system

**Tre sätt att få hjälp:**

```bash
# 1. --help flag (snabbast)
ls --help

# 2. man pages (manual - mer detaljerat)
man ls
# Navigera: Piltangenter, Space (nästa sida), q (quit)

# 3. info pages (ännu mer detaljerat)
info ls

# 4. tldr (community examples - om installerat)
tldr ls
```

**🟢 TIP:** Börja alltid med `--help`, gå till `man` om du behöver mer.

---

## 📁 Linux filsystem-struktur

### Linux är INTE som Windows!

**Windows:**
```
C:\
├─ Program Files\
├─ Users\
└─ Windows\

D:\
└─ Data\
```

**Linux:**
```
/  (root - ALLT börjar här)
├─ home/
├─ etc/
├─ var/
└─ usr/
```

**Ingen C:, D:, E: - allt är under ett enda träd med `/` i toppen!**

### The Filesystem Hierarchy Standard (FHS)

```
/  (root - filsystemets topp)
│
├─ bin/          Viktiga kommandon (ls, cp, mv)
├─ boot/         Boot-filer (kernel)
├─ dev/          Devices (hårdvara som filer)
├─ etc/          Konfigurationsfiler (system-wide)
├─ home/         Användares hemkataloger
│  └─ kali/      DIN hemkatalog
│     ├─ Desktop/
│     ├─ Documents/
│     └─ Downloads/
├─ lib/          Bibliotek (som DLL i Windows)
├─ media/        Monterade media (USB, DVD)
├─ mnt/          Manuella mount points
├─ opt/          Tredjepartsprogram
├─ proc/         Process-information (virtuellt)
├─ root/         Root-användarens hemkatalog
├─ run/          Runtime-data
├─ sbin/         System-binärer (admin-kommandon)
├─ srv/          Service data
├─ sys/          System-information (virtuellt)
├─ tmp/          Temporära filer (raderas vid omstart)
├─ usr/          User programs
│  ├─ bin/       Användarprogram
│  ├─ lib/       Bibliotek
│  ├─ local/     Lokalt installerade program
│  └─ share/     Delad data (docs, icons, etc.)
└─ var/          Variabel data
   ├─ log/       Loggfiler
   ├─ mail/      Email
   └─ www/       Webbserver-filer
```

### Viktiga kataloger för penetrationstestning

| Katalog | Innehåll | Varför viktigt |
|---------|----------|----------------|
| `/home/kali/` | Din hemkatalog | Där du jobbar, sparar filer |
| `/etc/` | Konfigurationsfiler | Konfigurera verktyg, se systeminfo |
| `/var/log/` | Loggfiler | Se vad som hänt, troubleshooting |
| `/tmp/` | Temporära filer | Snabb skrivbar plats (men raderas!) |
| `/usr/share/` | Delad data | Wordlists, exploits, scripts |
| `/usr/share/wordlists/` | Password-listor | För password cracking |
| `/usr/share/metasploit-framework/` | Metasploit-filer | Exploits, payloads |
| `/opt/` | Extra verktyg | Manuellt installerade verktyg |

### Absolut vs Relativ path

**Absolut path** - från root (`/`):
```bash
/home/kali/Documents/report.txt
# Fungerar ALLTID, oavsett var du är
```

**Relativ path** - från nuvarande plats:
```bash
Documents/report.txt
# Fungerar bara om du är i /home/kali/
```

**Speciella paths:**

| Symbol | Betydelse | Exempel |
|--------|-----------|---------|
| `/` | Root-katalogen | `/etc/passwd` |
| `~` | Din hemkatalog | `~/Documents` = `/home/kali/Documents` |
| `.` | Nuvarande katalog | `./script.sh` (kör script i current dir) |
| `..` | Förälder-katalog | `cd ..` (gå upp ett steg) |
| `-` | Föregående katalog | `cd -` (gå tillbaka till förra platsen) |

---

## 🧭 Navigeringskommandon

### 1. `pwd` - Print Working Directory

**Vad:** Visar var du är just nu

```bash
pwd

# Output:
# /home/kali
```

**När använda:**
- När du tappat bort dig
- För att bekräfta att du är på rätt plats innan farliga kommandon

### 2. `ls` - List

**Vad:** Lista filer och mappar

**Grundläggande användning:**

```bash
# Lista nuvarande katalog
ls

# Lista specifik katalog
ls /home/kali/Documents

# Lista med detaljer
ls -l

# Lista alla filer (inklusive dolda)
ls -a

# Kombinera options
ls -la

# Human-readable storlekar
ls -lh

# Sortera efter modifieringstid (nyast först)
ls -lt

# Reverse order
ls -lr
```

**Output-förklaring:**

```bash
ls -l
-rw-r--r-- 1 kali kali  1234 Nov 17 10:30 file.txt
│││││││││  │ │    │     │    │           │
│││││││││  │ │    │     │    │           └─ Filnamn
│││││││││  │ │    │     │    └──────────── Modifieringstid
│││││││││  │ │    │     └───────────────── Storlek (bytes)
│││││││││  │ │    └─────────────────────── Grupp
│││││││││  │ └──────────────────────────── Ägare
│││││││││  └─────────────────────────────── Antal hard links
││││││││└─ Andra (world) permissions: r-- (read)
│││││└──── Grupp permissions: r-- (read)
││└────────── Ägare permissions: rw- (read, write)
│└─────────── Special permissions
└──────────── File type: - (regular file)
              d = directory
              l = symbolic link
```

**Vanliga ls-varianter:**

| Kommando | Vad det gör |
|----------|-------------|
| `ls` | Basic lista |
| `ls -l` | Long format (detaljer) |
| `ls -a` | Alla filer (inkl. dolda som börjar med `.`) |
| `ls -la` | Long format + alla filer |
| `ls -lh` | Human-readable storlekar (KB, MB, GB) |
| `ls -lt` | Sorterat efter tid (nyast först) |
| `ls -lS` | Sorterat efter storlek |
| `ls -lR` | Rekursivt (alla undermappar) |
| `ls -ld */` | Lista bara mappar |

### 3. `cd` - Change Directory

**Vad:** Byt katalog (navigera i filsystemet)

```bash
# Gå till din hemkatalog
cd
cd ~

# Gå till specifik katalog (absolut path)
cd /etc

# Gå till katalog (relativ path)
cd Documents

# Gå upp ett steg
cd ..

# Gå upp två steg
cd ../..

# Gå till föregående katalog
cd -

# Gå till root
cd /
```

**Praktiska exempel:**

```bash
# Du är i: /home/kali
cd Documents
# Nu i: /home/kali/Documents

cd ..
# Nu i: /home/kali

cd /var/log
# Nu i: /var/log

cd -
# Tillbaka till: /home/kali

cd ~/Desktop
# Till: /home/kali/Desktop
```

**🟢 TIP:** Tab-completion!
```bash
cd Doc<TAB>
# Auto-kompletterar till: cd Documents/
```

### 4. `tree` - Visa katalogträd

**Vad:** Visuell representation av filstruktur

```bash
# Installera tree (om inte redan installerat)
sudo apt install tree -y

# Visa träd
tree

# Begränsa djup
tree -L 2

# Bara mappar
tree -d

# Visa dolda filer
tree -a
```

**Exempel output:**

```
/home/kali/
├── Desktop/
├── Documents/
│   ├── report.txt
│   └── notes.md
├── Downloads/
│   └── exploit.py
└── scripts/
    ├── scan.sh
    └── utils/
        └── helper.py

5 directories, 4 files
```

---

## ⌨️ Viktiga genvägar

### Terminal-genvägar

| Genväg | Vad det gör |
|--------|-------------|
| `Ctrl + C` | Avbryt pågående kommando |
| `Ctrl + D` | Exit (logga ut / stäng terminal) |
| `Ctrl + L` | Rensa skärmen (samma som `clear`) |
| `Ctrl + A` | Gå till början av raden |
| `Ctrl + E` | Gå till slutet av raden |
| `Ctrl + U` | Radera allt innan cursor |
| `Ctrl + K` | Radera allt efter cursor |
| `Ctrl + W` | Radera föregående ord |
| `Ctrl + R` | Sök i command history (reverse search) |
| `Ctrl + Z` | Pausa kommando (suspend till bakgrund) |
| `↑` / `↓` | Bläddra i command history |
| `Tab` | Auto-complete filnamn/kommandon |
| `Tab Tab` | Visa alla möjligheter |

### Auto-completion (Tab)

```bash
# Skriv början, tryck Tab
cd Doc<Tab>
# → cd Documents/

# Tvetydig completion - tryck Tab två gånger
cd D<Tab><Tab>
# Visar: Desktop/ Documents/ Downloads/

# Completion fungerar för kommandon också
nma<Tab>
# → nmap
```

### Command history

```bash
# Visa historik
history

# Visa senaste 10 kommandon
history 10

# Kör kommando från history (nummer från history-listan)
!123

# Kör senaste kommandot
!!

# Kör senaste kommando som började med "nmap"
!nmap

# Sök i history interaktivt
Ctrl + R
# (reverse-i-search): nm<type more>
# → visar senaste kommando som matchar
```

**🟢 TIP:** Kombinera med sudo:
```bash
# Du glömde sudo:
apt update
# Permission denied!

# Snabb fix:
sudo !!
# → sudo apt update
```

---

## 🎯 Wildcards och pattern matching

### Wildcards (globbing)

| Wildcard | Matchar | Exempel |
|----------|---------|---------|
| `*` | Noll eller fler tecken | `*.txt` = alla .txt-filer |
| `?` | Exakt ett tecken | `file?.txt` = file1.txt, fileA.txt |
| `[abc]` | Ett tecken från listan | `file[123].txt` = file1.txt, file2.txt, file3.txt |
| `[a-z]` | Ett tecken från range | `[a-z]*.txt` = alla .txt som börjar med bokstav |
| `[!abc]` | INTE tecken från listan | `[!0-9]*` = filer som INTE börjar med siffra |

**Praktiska exempel:**

```bash
# Lista alla .txt-filer
ls *.txt

# Lista alla filer som börjar med "report"
ls report*

# Lista file1.txt, file2.txt, ... file9.txt (men INTE file10.txt)
ls file?.txt

# Ta bort alla .log-filer
rm *.log

# Kopiera alla .py-filer till backup-mapp
cp *.py backup/

# Lista alla filer som börjar med stor bokstav
ls [A-Z]*

# Lista alla .jpg och .png-filer
ls *.{jpg,png}
```

**🟡 VIKTIGT med wildcards:**

```bash
# FARLIGT - tar bort ALLA filer i katalogen!
rm *

# Säkrare - bekräfta först vad som skulle matchas
ls *

# Eller använd -i (interactive) för bekräftelse
rm -i *.txt
```

---

## 🧪 Praktiska övningar

### Övning 1: Navigering basics

```bash
# 1. Var är du? Skriv ut working directory
pwd

# 2. Gå till root
cd /

# 3. Lista innehållet
ls

# 4. Gå till /etc
cd etc

# 5. Lista alla filer (inkl. dolda)
ls -la

# 6. Gå tillbaka till din hemkatalog
cd ~

# 7. Bekräfta att du är hemma
pwd
# Ska visa: /home/kali
```

### Övning 2: Skapa katalogstruktur

```bash
# 1. Gå till hemkatalogen
cd ~

# 2. Skapa en övningsmapp
mkdir linux-practice

# 3. Gå in i mappen
cd linux-practice

# 4. Skapa undermappar
mkdir Documents Images Scripts

# 5. Verifiera strukturen
ls -l

# 6. Visa som träd (om tree är installerat)
tree

# Förväntat resultat:
# linux-practice/
# ├── Documents/
# ├── Images/
# └── Scripts/
```

### Övning 3: Utforska filsystemet

```bash
# 1. Kolla vad som finns i /usr/share/
ls /usr/share/

# 2. Hitta wordlists (för password cracking)
ls /usr/share/wordlists/

# 3. Kolla storlek på wordlist
ls -lh /usr/share/wordlists/rockyou.txt.gz

# 4. Se innehåll i /etc/passwd (user-information)
cat /etc/passwd

# 5. Räkna hur många användare som finns
wc -l /etc/passwd
```

### Övning 4: Wildcards

```bash
# Förberedelse: Skapa testfiler
cd ~/linux-practice
touch file1.txt file2.txt file3.txt
touch report.txt notes.txt
touch script.py script.sh
touch image1.jpg image2.png

# 1. Lista alla .txt-filer
ls *.txt

# 2. Lista alla filer som börjar med "file"
ls file*

# 3. Lista file1.txt, file2.txt, file3.txt (men inte andra)
ls file?.txt

# 4. Lista alla script-filer (.py och .sh)
ls script.*

# 5. Lista alla bildfiler
ls *.{jpg,png}
```

### Övning 5: Command history

```bash
# 1. Kör några kommandon
pwd
ls
cd /etc
pwd
cd ~

# 2. Visa history
history

# 3. Använd piltangent-upp för att bläddra genom history

# 4. Sök i history med Ctrl+R
# Tryck Ctrl+R, skriv "pwd"
# Se att tidigare pwd-kommandon visas

# 5. Kör senaste kommandot igen
!!
```

---

## 🧪 Självtest - Nivå 2A

### Kunskapsfrågor

1. **Vad är skillnaden mellan terminal och shell?**
   - A) Det är samma sak
   - B) Terminal är programmet/fönstret, shell är tolkaren (Bash/Zsh)
   - C) Shell är GUI, terminal är CLI
   - D) Terminal är för Windows, shell för Linux

2. **Vad betyder `~` i Linux?**
   - A) Root-katalogen (/)
   - B) Din hemkatalog (/home/kali)
   - C) Föregående katalog
   - D) Nuvarande katalog

3. **Vilket kommando visar din nuvarande plats i filsystemet?**
   - A) `ls`
   - B) `cd`
   - C) `pwd`
   - D) `tree`

4. **Vad gör `cd ..`?**
   - A) Gå till hemkatalogen
   - B) Gå upp ett steg i katalogträdet
   - C) Gå till root
   - D) Gå till föregående katalog

5. **Vilken katalog innehåller konfigurationsfiler i Linux?**
   - A) `/config/`
   - B) `/settings/`
   - C) `/etc/`
   - D) `/conf/`

6. **Vad matchar wildcarden `*.txt`?**
   - A) Bara filer som heter "txt"
   - B) Alla filer som slutar med .txt
   - C) Alla filer som innehåller "txt"
   - D) Ingenting

7. **Vad betyder `$` i prompten?**
   - A) Du är root
   - B) Du är normal användare
   - C) Kommandot kostar pengar
   - D) Dollar-variabel

8. **Hur avbryter du ett pågående kommando?**
   - A) Alt + F4
   - B) Ctrl + C
   - C) Ctrl + Z
   - D) Delete

9. **Vad visar `ls -la`?**
   - A) Bara mappar
   - B) Long format + alla filer (inkl. dolda)
   - C) Bara dolda filer
   - D) Senast ändrade filer

10. **Hur går du tillbaka till föregående katalog?**
    - A) `cd ..`
    - B) `cd -`
    - C) `cd back`
    - D) `cd prev`

### Praktiska uppgifter

Genomför dessa i terminalen:

- [ ] **1. Navigera till root och tillbaka**
  ```bash
  cd /
  pwd  # Ska visa: /
  cd ~
  pwd  # Ska visa: /home/kali
  ```

- [ ] **2. Lista filer i /etc med detaljer**
  ```bash
  ls -l /etc | head -20
  ```

- [ ] **3. Hitta din hemkatalog storlek**
  ```bash
  du -sh ~
  ```

- [ ] **4. Använd Tab-completion**
  ```bash
  cd /usr/sh<Tab>
  # Ska auto-kompletteras till: cd /usr/share/
  ```

- [ ] **5. Sök i command history**
  ```bash
  # Tryck Ctrl+R
  # Sök efter "ls"
  # Kör ett av de hittade kommandona
  ```

### Svar

<details>
<summary>Klicka för svar</summary>

**Kunskapsfrågor:**

1. **B** - Terminal är programmet/fönstret, shell är tolkaren
2. **B** - Din hemkatalog (/home/kali)
3. **C** - `pwd` (Print Working Directory)
4. **B** - Gå upp ett steg i katalogträdet
5. **C** - `/etc/` innehåller konfigurationsfiler
6. **B** - Alla filer som slutar med .txt
7. **B** - Du är normal användare (# = root)
8. **B** - Ctrl + C
9. **B** - Long format + alla filer (inklusive dolda)
10. **B** - `cd -` (cd .. går upp ett steg, cd - går till förra platsen)

**Scoring:**
- 9-10 rätt: 🏆 Excellent! Du behärskar basics
- 7-8 rätt: ✅ Bra! Några små luckor
- 5-6 rätt: 📚 OK - öva mer
- <5 rätt: 🔄 Läs igenom nivån igen

**Praktiska uppgifter:** Alla ska fungera utan fel!

</details>

---

## ✅ Checklista - Redo för Nivå 2B?

Säkerställ att du:

- [ ] Kan öppna terminalen (Ctrl+Alt+T)
- [ ] Förstår skillnaden mellan terminal och shell
- [ ] Kan navigera med `cd`, `pwd`, `ls`
- [ ] Förstår absolut vs relativ path
- [ ] Vet vad `~`, `.`, `..`, `-` betyder
- [ ] Kan använda Tab-completion
- [ ] Kan använda wildcards (`*`, `?`)
- [ ] Kan använda Ctrl+C för att avbryta
- [ ] Kan söka i command history (Ctrl+R)
- [ ] Förstår grundläggande filsystem-struktur (`/home`, `/etc`, `/var`)

**🎯 Nästa steg:**

👉 **[Nivå 2B - Kommandon & Texteditors](./niva-2b-kommandon.md)**

Nu ska vi lära oss manipulera filer och använda texteditors!

---

**[⬅️ Föregående: Nivå 1](./niva-1-installation.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 2B](./niva-2b-kommandon.md)**
