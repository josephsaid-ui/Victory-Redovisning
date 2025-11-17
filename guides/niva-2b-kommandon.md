# 📝 Nivå 2B: Kommandon & Texteditors

**⏱️ Beräknad tid:** 45-60 minuter
**📚 Svårighetsgrad:** ⭐⭐ Nybörjare-Intermediate
**🎯 Förutsättningar:** Nivå 2A genomförd
**🎓 Lärdomsmål:** Manipulera filer och editera text i terminalen

---

## 📋 Innehåll

1. [Filmanipulering - basics](#-filmanipulering---basics)
2. [Sökning och filtrering](#-sökning-och-filtrering)
3. [Permissions och ownership](#-permissions-och-ownership)
4. [Texteditors: Nano](#-texteditor-nano-nybörjarvänlig)
5. [Texteditors: Vim](#-texteditor-vim-avancerad)
6. [Pipes och redirection](#-pipes-och-redirection)
7. [Praktiska övningar](#-praktiska-övningar)
8. [Självtest](#-självtest-nivå-2b)

---

## 📄 Filmanipulering - basics

### 1. `touch` - Skapa tom fil eller uppdatera timestamp

```bash
# Skapa tom fil
touch newfile.txt

# Skapa flera filer
touch file1.txt file2.txt file3.txt

# Skapa fil med mellanslag i namnet (använd quotes)
touch "my notes.txt"

# Uppdatera timestamp på befintlig fil
touch existing.txt
```

### 2. `mkdir` - Make Directory

```bash
# Skapa mapp
mkdir myfolder

# Skapa flera mappar
mkdir folder1 folder2 folder3

# Skapa nested directories (parent directories också)
mkdir -p projects/2025/pentest/reports

# Skapa med specifika permissions
mkdir -m 755 public_folder
```

**🟢 TIP:** `-p` är super användbart för att skapa hela katalogträd!

```bash
# Istället för:
mkdir projects
cd projects
mkdir 2025
cd 2025
mkdir pentest

# Gör:
mkdir -p projects/2025/pentest
```

### 3. `cp` - Copy

```bash
# Kopiera fil
cp source.txt destination.txt

# Kopiera fil till annan mapp
cp file.txt /home/kali/backup/

# Kopiera med nytt namn till annan mapp
cp file.txt /home/kali/backup/file_backup.txt

# Kopiera mapp (rekursivt)
cp -r folder/ backup_folder/

# Kopiera med verbose (visa vad som händer)
cp -v file.txt backup/

# Kopiera och bevara attribut (timestamps, permissions)
cp -p file.txt backup/

# Interactive (fråga innan overwrite)
cp -i file.txt existing.txt

# Kopiera flera filer till samma destination
cp file1.txt file2.txt file3.txt destination_folder/
```

**Vanliga cp-options:**

| Option | Vad det gör |
|--------|-------------|
| `-r` eller `-R` | Rekursivt (för mappar) |
| `-v` | Verbose (visa progress) |
| `-i` | Interactive (fråga innan overwrite) |
| `-p` | Preserve (behåll permissions, timestamps) |
| `-u` | Update (kopiera bara om source är nyare) |
| `-a` | Archive (samma som -r -p) |

### 4. `mv` - Move (och rename)

```bash
# Flytta fil
mv file.txt /home/kali/Documents/

# Rename fil (flytta till samma plats med nytt namn)
mv oldname.txt newname.txt

# Flytta mapp
mv folder/ /home/kali/backup/

# Flytta flera filer
mv file1.txt file2.txt file3.txt destination/

# Interactive (fråga innan overwrite)
mv -i file.txt existing.txt

# Verbose
mv -v file.txt destination/
```

**Skillnad mellan cp och mv:**

```bash
# cp = kopiera (originalet finns kvar)
cp file.txt backup.txt
# Nu finns både file.txt OCH backup.txt

# mv = flytta (originalet försvinner)
mv file.txt backup.txt
# Nu finns bara backup.txt
```

### 5. `rm` - Remove

**🔴 VARNING:** `rm` har INGEN papperskorg - filerna är BORTA!

```bash
# Ta bort fil
rm file.txt

# Ta bort flera filer
rm file1.txt file2.txt file3.txt

# Ta bort alla .txt-filer
rm *.txt

# Interactive (fråga för varje fil)
rm -i file.txt

# Force (ingen fråga, ingen varning)
rm -f file.txt

# Ta bort mapp (rekursivt)
rm -r folder/

# Force och rekursivt (FARLIGT!)
rm -rf folder/

# Verbose (visa vad som tas bort)
rm -v file.txt
```

**🔴 ALDRIG GÖR DETTA:**

```bash
# FÖRSTÖR HELA SYSTEMET!
sudo rm -rf /

# FÖRSTÖR HELA DIN HEMKATALOG!
rm -rf ~

# Ta bort nuvarande katalog och allt under (också farligt!)
rm -rf .

# Wildcard mistake - tar bort ALLT
rm -rf *
```

**🟢 SÄKRARE APPROACH:**

```bash
# Använd alltid -i först
rm -i file.txt

# Eller bekräfta vad som skulle tas bort
ls *.txt
# Se att det är rätt filer
rm *.txt

# Eller flytta till "trash" istället (säkrare)
mkdir ~/trash
mv unwanted_file.txt ~/trash/
```

### 6. `rmdir` - Remove Directory

```bash
# Ta bort tom mapp
rmdir empty_folder/

# Ta bort flera tomma mappar
rmdir folder1/ folder2/ folder3/

# Ta bort nested tomma mappar
rmdir -p parent/child/grandchild/
```

**🟡 Skillnad mellan rmdir och rm -r:**

```bash
# rmdir - bara för TOMMA mappar (säkert)
rmdir folder/  # Misslyckas om folder innehåller filer

# rm -r - tar bort mapp OCH innehåll (farligt)
rm -r folder/  # Tar bort allt
```

### 7. `cat` - Concatenate and display

```bash
# Visa fil-innehåll
cat file.txt

# Visa flera filer
cat file1.txt file2.txt

# Numrera rader
cat -n file.txt

# Skapa fil genom att skriva innehåll (Ctrl+D för att avsluta)
cat > newfile.txt
This is some text
More text
^D  # (Ctrl+D)

# Append (lägg till) i fil
cat >> existing.txt
Additional content
^D

# Konkatenera (sammanfoga) filer till en ny
cat file1.txt file2.txt > combined.txt
```

### 8. `less` och `more` - View file content paged

```bash
# View fil med scrolling (bättre än cat för stora filer)
less largefile.txt

# Navigering i less:
# Space      = nästa sida
# b          = föregående sida
# /pattern   = sök efter pattern
# n          = nästa match
# N          = föregående match
# q          = quit
# G          = gå till slutet
# g          = gå till början

# more (äldre, mindre funktioner)
more file.txt
```

### 9. `head` och `tail` - View beginning/end of file

```bash
# Visa första 10 raderna (default)
head file.txt

# Visa första 20 raderna
head -n 20 file.txt

# Visa sista 10 raderna
tail file.txt

# Visa sista 50 raderna
tail -n 50 file.txt

# Follow (följ filen i realtid - SUPER användbart för logs!)
tail -f /var/log/syslog

# Kombinera: visa rad 50-60
head -n 60 file.txt | tail -n 10
```

---

## 🔍 Sökning och filtrering

### 1. `find` - Hitta filer

```bash
# Hitta alla filer i current directory
find .

# Hitta alla .txt-filer
find . -name "*.txt"

# Hitta filer case-insensitive
find . -iname "*.TXT"

# Hitta bara mappar
find . -type d

# Hitta bara filer
find . -type f

# Hitta filer större än 10MB
find . -size +10M

# Hitta filer mindre än 1KB
find . -size -1k

# Hitta filer modifierade senaste 7 dagarna
find . -mtime -7

# Hitta och ta bort alla .tmp-filer
find . -name "*.tmp" -delete

# Hitta och kör kommando på varje fil
find . -name "*.txt" -exec cat {} \;
```

**Find size units:**

| Unit | Betydelse |
|------|-----------|
| `c` | Bytes |
| `k` | Kilobytes |
| `M` | Megabytes |
| `G` | Gigabytes |

### 2. `grep` - Search inside files

```bash
# Sök efter pattern i fil
grep "error" logfile.txt

# Case-insensitive
grep -i "error" logfile.txt

# Visa radnummer
grep -n "error" logfile.txt

# Inverse (visa rader som INTE matchar)
grep -v "info" logfile.txt

# Rekursiv sökning i alla filer
grep -r "password" /etc/

# Räkna antal matches
grep -c "error" logfile.txt

# Visa bara filnamn som innehåller match
grep -l "TODO" *.py

# Visa några rader före/efter match (context)
grep -A 3 "error" logfile.txt  # 3 rader After
grep -B 3 "error" logfile.txt  # 3 rader Before
grep -C 3 "error" logfile.txt  # 3 rader Context (både före och efter)

# Regex patterns
grep "^error" file.txt    # Rader som BÖRJAR med "error"
grep "error$" file.txt    # Rader som SLUTAR med "error"
grep "[0-9]" file.txt     # Rader med siffror
```

### 3. `locate` - Fast file search

```bash
# Snabb sökning (använder databas)
locate filename.txt

# Case-insensitive
locate -i FiLeNaMe.txt

# Räkna antal matches
locate -c "*.txt"

# Uppdatera locate-databasen (kör som root)
sudo updatedb

# Visa bara filer som fortfarande existerar
locate -e filename.txt
```

**locate vs find:**

```
locate:
✅ Mycket snabbare
✅ Söker hela systemet
❌ Kräver updatedb först
❌ Hitta inte nyss skapade filer (tills updatedb körs)

find:
✅ Realtid-sökning
✅ Många filter-options
✅ Kan köra commands på results
❌ Långsammare
```

### 4. `which` och `whereis` - Find command location

```bash
# Var är nmap installerat?
which nmap
# Output: /usr/bin/nmap

# Hitta alla relaterade filer (binary, source, man page)
whereis nmap
# Output: nmap: /usr/bin/nmap /usr/share/man/man1/nmap.1.gz

# Hitta alla Python-instanser
which -a python
```

### 5. `wc` - Word Count

```bash
# Räkna rader, ord, bytes
wc file.txt

# Bara rader
wc -l file.txt

# Bara ord
wc -w file.txt

# Bara characters
wc -m file.txt

# Användbart: Räkna antal filer i mapp
ls | wc -l
```

---

## 🔐 Permissions och ownership

### Förstå Linux permissions

**Varje fil har:**
- **Owner** (användare som äger filen)
- **Group** (grupp som har access)
- **Permissions** (vad owner, group, others får göra)

### Läsa permissions

```bash
ls -l file.txt
-rw-r--r-- 1 kali kali 1234 Nov 17 10:30 file.txt
│││││││││
││││││││└─ Other (alla andra)
│││││└──── Group
││└────────── Owner
│└─────────── Special permissions
└──────────── File type (- = file, d = directory)

r = read (4)
w = write (2)
x = execute (1)
- = no permission (0)
```

**Exempel:**

```
-rwxr-xr--
 │││││││││
 │││││││└─ Other: r-- (read only) = 4
 ││││└──── Group: r-x (read + execute) = 5
 │└────────── Owner: rwx (read + write + execute) = 7
 └─────────── Regular file

Siffror: 754
```

### `chmod` - Change permissions

```bash
# Numeric mode (enklast)
chmod 755 script.sh
# Owner: rwx (7)
# Group: r-x (5)
# Other: r-x (5)

# Vanliga permission-kombinationer:
chmod 777 file.txt  # Alla får göra allt (OSÄKERT!)
chmod 755 script.sh # Owner: full, others: read+execute
chmod 644 file.txt  # Owner: read+write, others: read-only
chmod 600 file.txt  # Owner: read+write, others: ingen access
chmod 700 script.sh # Owner: full, others: ingen access

# Symbolic mode
chmod u+x script.sh    # Add execute för owner
chmod g-w file.txt     # Remove write från group
chmod o+r file.txt     # Add read för others
chmod a+x script.sh    # Add execute för all

# Rekursivt (för mappar och allt under)
chmod -R 755 folder/
```

**Permission guide:**

| Siffra | Binary | Permissions | Användning |
|--------|--------|-------------|------------|
| 0 | 000 | `---` | Ingen access |
| 1 | 001 | `--x` | Execute only |
| 2 | 010 | `-w-` | Write only (ovanligt) |
| 3 | 011 | `-wx` | Write + execute |
| 4 | 100 | `r--` | Read only |
| 5 | 101 | `r-x` | Read + execute |
| 6 | 110 | `rw-` | Read + write |
| 7 | 111 | `rwx` | Full control |

**Vanliga permission patterns:**

```bash
# Scripts som ska köras
chmod 755 script.sh
chmod +x script.sh  # (shortcut)

# Privata filer
chmod 600 private.txt

# Public readable files
chmod 644 document.txt

# Shared folder där alla kan skriva
chmod 777 /tmp/shared/  # (osäkert, men OK för temp)
```

### `chown` - Change ownership

```bash
# Ändra owner
sudo chown newuser file.txt

# Ändra owner och group
sudo chown newuser:newgroup file.txt

# Bara ändra group
sudo chown :newgroup file.txt

# Rekursivt
sudo chown -R user:group folder/
```

### `chgrp` - Change group

```bash
# Ändra group
chgrp newgroup file.txt

# Rekursivt
chgrp -R newgroup folder/
```

---

## ✏️ Texteditor: Nano (nybörjarvänlig)

### Öppna/skapa fil

```bash
# Öppna befintlig eller skapa ny
nano filename.txt

# Öppna med root permissions
sudo nano /etc/hosts
```

### Nano interface

```
  GNU nano 6.0           filename.txt

[Här skriver du text]





^G Help     ^O Write Out ^W Where Is  ^K Cut
^X Exit     ^R Read File ^\ Replace   ^U Paste
```

### Viktiga genvägar

| Genväg | Vad det gör |
|--------|-------------|
| `Ctrl + O` | Save (Write Out) → Enter för att bekräfta |
| `Ctrl + X` | Exit → frågar om save om ändringar finns |
| `Ctrl + K` | Cut current line |
| `Ctrl + U` | Paste (Uncut) |
| `Ctrl + W` | Search (Where Is) |
| `Ctrl + \` | Search and Replace |
| `Ctrl + G` | Help |
| `Ctrl + C` | Show cursor position |
| `Alt + U` | Undo |
| `Alt + E` | Redo |
| `Ctrl + A` | Go to beginning of line |
| `Ctrl + E` | Go to end of line |

### Vanligt workflow

```bash
# 1. Öppna/skapa fil
nano myfile.txt

# 2. Skriv innehåll
# (skriv text...)

# 3. Spara
Ctrl + O
Enter

# 4. Stäng
Ctrl + X
```

**🟢 TIP för nybörjare:** Använd Nano för all text-editering i början!

---

## 🎯 Texteditor: Vim (avancerad)

**🔴 VARNING:** Vim har brant inlärningskurva men är extremt kraftfull!

### Varför lära sig Vim?

- ⚡ Otroligt snabbt när du kan det
- 🌍 Finns på ALLA Linux-system
- 💪 Mäktig för stora filer och kodning
- 🎯 Krävs ofta i professionella miljöer
- 🔧 Används i många andra verktyg (less, man pages)

### Vim modes

Vim har olika "modes" - detta är vad som förvirrar nybörjare!

```
┌────────────────────────────────────────────────────┐
│  NORMAL MODE (default)                             │
│  - Navigera med h,j,k,l                            │
│  - Ta bort med d, kopiera med y                    │
│  - Kommandon                                       │
│                                                    │
│  Tryck: i eller a → INSERT MODE                    │
│  Tryck: : → COMMAND MODE                          │
│  Tryck: v → VISUAL MODE                           │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│  INSERT MODE (skriva text)                         │
│  - Skriv text som vanligt                          │
│  - ESC → tillbaka till NORMAL MODE                │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│  COMMAND MODE (kommandon)                          │
│  - :w = save                                       │
│  - :q = quit                                       │
│  - :wq = save and quit                            │
│  - ESC → tillbaka till NORMAL MODE                │
└────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────┐
│  VISUAL MODE (markera text)                        │
│  - Markera text för copy/cut                       │
│  - ESC → tillbaka till NORMAL MODE                │
└────────────────────────────────────────────────────┘
```

### Öppna Vim

```bash
# Öppna fil
vim filename.txt

# Öppna med root
sudo vim /etc/hosts

# Öppna på specifik rad
vim +42 filename.txt
```

### Basic Vim survival guide

**Öppna fil → Editera → Spara → Stäng:**

```
1. vim file.txt        (öppna)
2. i                   (tryck 'i' för INSERT MODE)
3. [skriv text]        (skriv vad du vill)
4. ESC                 (tillbaka till NORMAL MODE)
5. :wq                 (skriv ':wq' och Enter - save and quit)
```

**Stäng utan att spara:**

```
ESC
:q!
Enter
```

### Viktiga Vim-kommandon (NORMAL MODE)

**Navigation:**

| Tangent | Vad det gör |
|---------|-------------|
| `h` | Vänster |
| `j` | Ner |
| `k` | Upp |
| `l` | Höger |
| `w` | Nästa ord |
| `b` | Föregående ord |
| `0` | Början av rad |
| `$` | Slut av rad |
| `gg` | Början av fil |
| `G` | Slut av fil |
| `:42` | Gå till rad 42 |

**Editing (NORMAL MODE):**

| Kommando | Vad det gör |
|----------|-------------|
| `i` | Insert mode (före cursor) |
| `a` | Insert mode (efter cursor) |
| `A` | Insert mode (slutet av rad) |
| `o` | Insert ny rad UNDER |
| `O` | Insert ny rad ÖVER |
| `x` | Ta bort tecken under cursor |
| `dd` | Ta bort hela raden |
| `dw` | Ta bort ord |
| `d$` | Ta bort till slutet av rad |
| `yy` | Kopiera rad |
| `p` | Paste efter cursor |
| `P` | Paste före cursor |
| `u` | Undo |
| `Ctrl + r` | Redo |

**Search (NORMAL MODE):**

```
/pattern     Sök framåt efter pattern
?pattern     Sök bakåt
n            Nästa match
N            Föregående match
```

**Command mode (:):**

| Kommando | Vad det gör |
|----------|-------------|
| `:w` | Save |
| `:q` | Quit |
| `:wq` | Save and quit |
| `:q!` | Quit utan save (force) |
| `:x` | Save and quit (shortcut) |
| `:w filename` | Save as |
| `:set number` | Visa radnummer |
| `:set nonumber` | Dölj radnummer |
| `:%s/old/new/g` | Replace all "old" med "new" |
| `:help` | Visa hjälp |

### Vim cheat sheet för nybörjare

```
SURVIVAL:
  i       → start skriva
  ESC     → stop skriva
  :wq     → spara och stäng
  :q!     → stäng utan spara

BASICS:
  h,j,k,l → navigera (←↓↑→)
  dd      → ta bort rad
  yy      → kopiera rad
  p       → paste
  u       → undo

SEARCH:
  /text   → sök efter "text"
  n       → nästa match

POWER USER (senare):
  gg      → gå till början
  G       → gå till slutet
  :42     → gå till rad 42
  dw      → delete word
  ciw     → change inner word
```

**🟢 TIP:** Öva med `vimtutor`:

```bash
# Interaktiv Vim-tutorial
vimtutor
```

---

## 🔀 Pipes och redirection

### Output redirection (`>` och `>>`)

```bash
# Skriv output till fil (overwrite)
echo "Hello" > file.txt

# Append output till fil
echo "World" >> file.txt

# Redirect command output
ls -l > filelist.txt

# Redirect errors (stderr) till fil
command 2> error.log

# Redirect både stdout och stderr
command > output.log 2>&1

# Discard output (send to /dev/null)
command > /dev/null
```

### Input redirection (`<`)

```bash
# Läs input från fil
wc -l < file.txt

# Sort innehåll från fil
sort < unsorted.txt > sorted.txt
```

### Pipes (`|`)

**Vad:** Skicka output från ett kommando till ett annat

```bash
# Räkna antal filer
ls | wc -l

# Hitta process och visa sorterat
ps aux | grep firefox | sort

# Visa stora filer
du -sh * | sort -h

# Topp 10 största filer
du -h | sort -h | tail -10

# Real-time log monitoring
tail -f /var/log/syslog | grep error

# Lista bara mappar
ls -l | grep ^d
```

**Power combinations:**

```bash
# Hitta alla .txt-filer och räkna dem
find . -name "*.txt" | wc -l

# Hitta största filer i hemkatalog
du -ah ~ | sort -rh | head -20

# Se aktiva nätverksanslutningar sorterat
netstat -tulpn | grep LISTEN | sort

# Process-sökning
ps aux | grep python | grep -v grep

# Unikt IP-adresser i log
cat access.log | awk '{print $1}' | sort | uniq
```

---

## 🧪 Praktiska övningar

### Övning 1: Filmanipulering

```bash
# 1. Skapa övningsmapp
mkdir ~/command-practice
cd ~/command-practice

# 2. Skapa testfiler
touch file1.txt file2.txt file3.txt
echo "This is file 1" > file1.txt
echo "This is file 2" > file2.txt
echo "This is file 3" > file3.txt

# 3. Kopiera fil1 till backup
cp file1.txt file1_backup.txt

# 4. Rename file2
mv file2.txt renamed_file2.txt

# 5. Visa alla filer
ls -l

# 6. Konkatenera alla filer till en
cat file1.txt renamed_file2.txt file3.txt > combined.txt

# 7. Visa combined.txt
cat combined.txt

# 8. Cleanup - ta bort backupen
rm file1_backup.txt
```

### Övning 2: Sökning

```bash
# 1. Skapa testfiler med innehåll
cd ~/command-practice
echo "Error: Something went wrong" > log1.txt
echo "INFO: Process started" > log2.txt
echo "Error: Database connection failed" > log3.txt
echo "WARNING: Low memory" > log4.txt

# 2. Sök efter "Error" i alla filer
grep "Error" *.txt

# 3. Sök case-insensitive efter "error"
grep -i "error" *.txt

# 4. Visa vilka filer som innehåller "Error"
grep -l "Error" *.txt

# 5. Hitta alla .txt-filer i din hemkatalog
find ~ -name "*.txt" | head -20

# 6. Räkna hur många .txt-filer du har
find ~ -name "*.txt" | wc -l
```

### Övning 3: Permissions

```bash
# 1. Skapa ett script
cd ~/command-practice
echo '#!/bin/bash' > myscript.sh
echo 'echo "Hello from script!"' >> myscript.sh

# 2. Försök köra det
./myscript.sh
# Får error: Permission denied

# 3. Kontrollera permissions
ls -l myscript.sh
# -rw-r--r-- (ingen execute)

# 4. Ge execute-permission
chmod +x myscript.sh

# 5. Kontrollera igen
ls -l myscript.sh
# -rwxr-xr-x (execute för alla)

# 6. Kör scriptet
./myscript.sh
# Output: Hello from script!

# 7. Experimentera med olika permissions
chmod 644 myscript.sh   # Reset to no execute
chmod 700 myscript.sh   # Owner only, full access
chmod 755 myscript.sh   # Standard for scripts
```

### Övning 4: Nano editing

```bash
# 1. Skapa ny fil med Nano
nano mynotes.txt

# 2. Skriv lite text:
# "This is my first Nano edit
# Line 2
# Line 3"

# 3. Spara: Ctrl+O, Enter
# 4. Stäng: Ctrl+X

# 5. Öppna igen och lägg till mer
nano mynotes.txt

# 6. Lägg till en rad längst ner

# 7. Sök efter "first": Ctrl+W, skriv "first", Enter

# 8. Spara och stäng: Ctrl+X, Yes, Enter
```

### Övning 5: Pipes och redirection

```bash
cd ~/command-practice

# 1. Lista filer och spara till fil
ls -l > filelist.txt
cat filelist.txt

# 2. Lägg till mer information
date >> filelist.txt
cat filelist.txt

# 3. Använd pipe för att räkna filer
ls | wc -l

# 4. Sortera och visa top 5 största filer
ls -lh | sort -k5 -h | tail -5

# 5. Hitta alla "txt"-filer och räkna
find . -name "*.txt" | wc -l

# 6. Process-filtrering
ps aux | grep bash
```

---

## 🧪 Självtest - Nivå 2B

### Kunskapsfrågor

1. **Vad är skillnaden mellan `cp` och `mv`?**
   - A) Det är samma sak
   - B) cp kopierar (original finns kvar), mv flyttar (original borta)
   - C) cp är för filer, mv för mappar
   - D) mv är snabbare

2. **Vilket kommando tar bort en MAPP rekursivt?**
   - A) `rm folder`
   - B) `rmdir -r folder`
   - C) `rm -r folder`
   - D) `delete folder`

3. **Vad betyder `chmod 755 script.sh`?**
   - A) Owner: rwx, Group: r-x, Other: r-x
   - B) Alla får full access
   - C) Ingen får access
   - D) Owner: r--, Group: r--, Other: r--

4. **Hur sparar och stänger du i Nano?**
   - A) Ctrl+X
   - B) Ctrl+S, Ctrl+Q
   - C) Ctrl+O (save), Ctrl+X (exit)
   - D) :wq

5. **Vad gör `>`?**
   - A) Redirect output till fil (overwrite)
   - B) Append till fil
   - C) Pipe till annat kommando
   - D) Input från fil

6. **Hur söker du efter "error" i alla .log-filer?**
   - A) `find "error" *.log`
   - B) `grep "error" *.log`
   - C) `search error *.log`
   - D) `cat *.log | find error`

7. **Vad gör `|` (pipe)?**
   - A) Redirect till fil
   - B) Skicka output från kommando till nästa kommando
   - C) Ta bort fil
   - D) OR-operator

8. **Hur ger du execute-permission till ett script?**
   - A) `chmod +x script.sh`
   - B) `chown +x script.sh`
   - C) `execute script.sh`
   - D) `chmod 644 script.sh`

9. **Hur söker du i Vim (NORMAL MODE)?**
   - A) Ctrl+F
   - B) /pattern
   - C) :search pattern
   - D) grep pattern

10. **Vad gör `>>` (append)?**
    - A) Overwrite fil
    - B) Lägg till i slutet av fil
    - C) Ta bort fil
    - D) Kopiera fil

### Praktiska uppgifter

- [ ] **1. Skapa och manipulera filer**
  ```bash
  touch test.txt
  echo "Hello" > test.txt
  cat test.txt
  cp test.txt test_backup.txt
  ls
  ```

- [ ] **2. Ändra permissions på fil**
  ```bash
  chmod 644 test.txt
  ls -l test.txt
  chmod +x test.txt
  ls -l test.txt
  ```

- [ ] **3. Sök efter text i filer**
  ```bash
  grep "bash" /etc/passwd
  ```

- [ ] **4. Använd Nano för att skapa fil**
  ```bash
  nano mytest.txt
  # Skriv något, spara (Ctrl+O), stäng (Ctrl+X)
  cat mytest.txt
  ```

- [ ] **5. Använd pipes**
  ```bash
  ls -l | grep "txt"
  ps aux | grep bash | wc -l
  ```

### Svar

<details>
<summary>Klicka för svar</summary>

**Kunskapsfrågor:**
1. **B** - cp kopierar (original finns kvar), mv flyttar
2. **C** - `rm -r folder`
3. **A** - Owner: rwx (7), Group: r-x (5), Other: r-x (5)
4. **C** - Ctrl+O (save), Ctrl+X (exit)
5. **A** - Redirect output till fil (overwrite)
6. **B** - `grep "error" *.log`
7. **B** - Skicka output från kommando till nästa
8. **A** - `chmod +x script.sh`
9. **B** - `/pattern` (sök framåt)
10. **B** - Lägg till i slutet av fil

**Scoring:**
- 9-10 rätt: 🏆 Excellent!
- 7-8 rätt: ✅ Bra!
- 5-6 rätt: 📚 OK - öva mer
- <5 rätt: 🔄 Läs igen

</details>

---

## ✅ Checklista - Redo för Nivå 2C?

- [ ] Kan skapa, kopiera, flytta, ta bort filer och mappar
- [ ] Förstår skillnaden mellan cp, mv, rm
- [ ] Kan använda wildcards (`*`, `?`)
- [ ] Kan söka filer med `find` och `grep`
- [ ] Förstår permissions (r, w, x) och kan ändra med `chmod`
- [ ] Kan editera filer med Nano (och grundläggande Vim)
- [ ] Förstår redirection (`>`, `>>`, `<`)
- [ ] Kan använda pipes (`|`)
- [ ] Kan kombinera kommandon effektivt

**🎯 Nästa steg:**

👉 **[Nivå 2C - Pakethantering & Systemadministration](./niva-2c-system.md)**

---

**[⬅️ Föregående: Nivå 2A](./niva-2a-terminal.md)** | **[🏠 Huvudguide](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 2C](./niva-2c-system.md)**
