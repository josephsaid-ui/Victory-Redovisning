# Git & GitHub Manual för Windows 11 med Miniconda
**Skapad: 2025-11-17**
**För: Windows 11 användare med Miniconda**

---

## 📚 Nivå 1: För en 5-åring

### Vad är Git?

Tänk dig att du bygger med LEGO. Du bygger ett slott. Men ibland vill du prova att bygga tornet på ett annat sätt. Vad händer om det nya tornet ser fult ut? Då vill du ju ha tillbaka det gamla tornet!

**Git är som en magisk maskin som tar bilder av ditt LEGO-slott!**

Varje gång du bygger något coolt, trycker du på en knapp och *KLICK!* - maskinen tar en bild. Om du förstör något senare, kan du titta på bilden och bygga tillbaka det precis som det var!

### Vad är GitHub?

GitHub är som ett stort bibliotek på internet där alla barn kan visa sina LEGO-slott. Du kan:
- Visa dina slott för andra barn
- Titta på andras slott
- Hjälpa andra att bygga deras slott
- Låta andra hjälpa dig med ditt slott

### Hur funkar det?

1. **Du bygger** - Du bygger med dina LEGO-klossar (skriver kod på din dator)
2. **Du tar en bild** - Du trycker på knappen och säger "Jag gillar hur det ser ut nu!" (git commit)
3. **Du visar för andra** - Du lägger bilden i biblioteket så andra kan se (git push)
4. **Du hämtar andras idéer** - Du kan kolla på andras bilder och kopiera deras coola idéer (git pull)

---

## 📘 Nivå 2: För en 10-åring

### Vad är Git och varför behöver du det?

Tänk dig att du skriver en saga. Du skriver kapitel 1, sedan kapitel 2, sedan kapitel 3. Men plötsligt kommer du på en bättre idé för kapitel 2!

**Problemet:** Om du ändrar kapitel 2 och det blir sämre, hur får du tillbaka den gamla versionen?

**Lösningen:** Git är ett program som kommer ihåg ALLA versioner av din saga!

Det är som att ha en tidmaskin för dina filer. Du kan:
- Gå tillbaka till hur filen såg ut igår
- Se exakt vad du ändrade mellan olika dagar
- Prova nya idéer utan att förstöra originalet
- Arbeta tillsammans med kompisar på samma projekt

### Vad är GitHub?

GitHub är en hemsida på internet där du kan:
- **Spara dina projekt** - Som ett USB-minne i molnet
- **Samarbeta** - Jobba på samma projekt med dina klasskamrater
- **Dela** - Visa dina projekt för hela världen
- **Lära** - Titta på hur andra löst problem

### Grundläggande ord att känna till:

- **Repository (repo)** = En mapp med alla dina filer OCH hela historiken
- **Commit** = En sparad version av dina filer (som en sparningspunkt i ett spel)
- **Push** = Skicka dina ändringar till GitHub (ladda upp)
- **Pull** = Hämta ändringar från GitHub (ladda ner)
- **Branch** = En kopia där du kan testa saker utan att förstöra originalet

### Hur börjar du?

Tänk dig att du ska skriva en uppsats med din kompis. Här är hur Git hjälper er:

1. **Skapa ett repo** - Ni skapar en gemensam mapp för uppsatsen
2. **Skriv** - Du skriver din del
3. **Commit** - Du sparar din version med ett meddelande "La till introduktion"
4. **Push** - Du lägger upp det på GitHub
5. **Din kompis Pull** - Din kompis hämtar dina ändringar
6. **Repeat** - Ni fortsätter så tills uppsatsen är klar!

---

## 📗 Nivå 3: För en 15-åring

### Djupare förståelse av Git

Git är ett **versionshanteringssystem** (VCS - Version Control System). Det skapades av Linus Torvalds (samma person som skapade Linux) år 2005.

#### Varför Git är viktigt:

1. **Historik** - Se exakt vad som ändrats, när och av vem
2. **Samarbete** - Flera personer kan jobba på samma kod samtidigt
3. **Branching** - Testa nya features utan att påverka huvudkoden
4. **Backup** - Dina projekt är säkrade på flera platser
5. **Professionellt** - Alla utvecklare och företag använder Git

### Git vs GitHub - Vad är skillnaden?

- **Git** = Programmet på din dator som hanterar versioner
- **GitHub** = En webbplats där du lagrar och delar dina Git-projekt

**Analogi:** Git är som Microsoft Word, GitHub är som OneDrive.

### Viktiga Git-koncept:

#### Working Directory, Staging Area, Repository

```
Din dator:
┌─────────────────┐
│ Working Dir     │  <- Här jobbar du med dina filer
│ (dina filer)    │
└────────┬────────┘
         │ git add
┌────────▼────────┐
│ Staging Area    │  <- Filer redo att sparas (commitas)
│ (redo att       │
│  committa)      │
└────────┬────────┘
         │ git commit
┌────────▼────────┐
│ Local Repo      │  <- Alla sparade versioner på din dator
│ (.git mappen)   │
└────────┬────────┘
         │ git push
┌────────▼────────┐
│ GitHub (Remote) │  <- Ditt projekt på internet
└─────────────────┘
```

### Installation för Windows 11 (2025)

#### Steg 1: Installera Git

**Alternativ A: Med Winget (snabbast, rekommenderas)**
1. Öppna PowerShell eller Command Prompt
2. Kör: `winget install --id Git.Git -e --source winget`

**Alternativ B: Med installer**
1. Gå till https://git-scm.com/downloads
2. Ladda ner senaste versionen (2.51.2 eller nyare)
3. Kör installern
4. **VIKTIGA INSTÄLLNINGAR:**
   - Editor: Välj "Visual Studio Code" (om du har det) istället för Vim
   - Default branch: Välj "main" (modernt standard)
   - PATH: Välj "Git from the command line and also from 3rd-party software"
   - Resten: Behåll standardinställningar

#### Steg 2: Konfigurera Git

Öppna Git Bash (eller din Anaconda Prompt) och kör:

```bash
git config --global user.name "Ditt Namn"
git config --global user.email "din.email@example.com"
git config --global init.defaultBranch main
```

#### Steg 3: Installera GitHub Desktop (valfritt men rekommenderat för nybörjare)

1. Gå till https://desktop.github.com/
2. Ladda ner för Windows
3. Installera och logga in med ditt GitHub-konto

### Integration med Miniconda

Eftersom du har Miniconda kan du använda Git på två sätt:

#### Alternativ 1: Anaconda Prompt
1. Öppna "Anaconda Prompt" från Start-menyn
2. Git borde fungera direkt här efter installation

#### Alternativ 2: Git Bash med Conda
För att använda conda i Git Bash:
```bash
# Navigera till din Miniconda installation
cd /c/Users/DittNamn/miniconda3/Scripts
# Initiera conda för bash
./conda init bash
# Starta om Git Bash
```

### Grundläggande Git-kommandon:

```bash
# Skapa ett nytt repo
git init

# Klona (kopiera) ett projekt från GitHub
git clone https://github.com/användarnamn/projekt.git

# Se status på dina filer
git status

# Lägg till filer till staging area
git add filnamn.txt          # En fil
git add .                    # Alla ändrade filer

# Spara en version (commit)
git commit -m "Beskrivning av vad du ändrat"

# Se historik
git log

# Skicka till GitHub
git push

# Hämta från GitHub
git pull
```

### Ditt första projekt:

```bash
# 1. Skapa en mapp
mkdir mitt-första-projekt
cd mitt-första-projekt

# 2. Initiera Git
git init

# 3. Skapa en fil
echo "# Mitt Första Projekt" > README.md

# 4. Lägg till filen
git add README.md

# 5. Committa
git commit -m "Första commit: La till README"

# 6. Koppla till GitHub (skapa först ett repo på github.com)
git remote add origin https://github.com/dittnamn/mitt-första-projekt.git

# 7. Pusha
git push -u origin main
```

---

## 📕 Nivå 4: För en 20-åring (Fullständig teknisk guide)

### Avancerad Git-arkitektur och bästa praxis

#### Git's Distribuerade Natur

Git är ett **Distributed Version Control System (DVCS)**. Till skillnad från centraliserade system (som SVN) har varje utvecklare en komplett kopia av hela projektet inklusive all historik.

**Fördelar:**
- Fungerar offline
- Extremt snabba operationer (commit, branch, merge, log)
- Robust mot serverfel
- Flexibla arbetsflöden

#### Git's Objektmodell

Git lagrar data som en serie snapshots i en DAG (Directed Acyclic Graph). Fyra objekttyper:

1. **Blob** - Innehållet i en fil
2. **Tree** - Kataloger och filnamn
3. **Commit** - Metadata om en snapshot
4. **Tag** - Permanent referens till en commit

Alla objekt identifieras med SHA-1 hash (40 hexadecimala tecken).

### Professionell Installation & Setup (Windows 11 + Miniconda)

#### Del 1: Git Installation (2025 Best Practices)

**Via Winget (Rekommenderat):**
```powershell
# Installera senaste Git (2.51.2+)
winget install --id Git.Git -e --source winget

# Verifiera installation
git --version
```

**Kritiska konfigurationer:**

```bash
# Identitet (obligatoriskt)
git config --global user.name "Ditt Fullständiga Namn"
git config --global user.email "din@email.com"

# Modern default branch
git config --global init.defaultBranch main

# Editor (välj det du föredrar)
git config --global core.editor "code --wait"  # VS Code
# eller
git config --global core.editor "notepad"      # Notepad

# Line ending hantering (viktigt för Windows)
git config --global core.autocrlf true

# Credential caching (undvik att skriva lösenord varje gång)
git config --global credential.helper manager

# Färglagd output
git config --global color.ui auto

# Default pull behavior (rekommenderat sedan Git 2.27+)
git config --global pull.rebase false

# Alias för produktivitet
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --oneline --graph --all --decorate'

# Visa all konfiguration
git config --list --show-origin
```

#### Del 2: GitHub Authentication (2025)

**Token-baserad autentisering (lösenord fungerar INTE längre):**

1. **Skapa Personal Access Token (PAT):**
   - Gå till GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - "Generate new token (classic)"
   - Välj scopes: `repo`, `workflow`, `admin:org` (beroende på behov)
   - Kopiera token (visas bara EN gång!)

2. **Använd token:**
   ```bash
   # När du pushar första gången kommer Git Credential Manager att fråga
   # Använd din token som lösenord
   git push -u origin main
   ```

**SSH Keys (mer säkert och bekvämt):**

```bash
# Generera SSH-nyckel
ssh-keygen -t ed25519 -C "din@email.com"
# Spara i default location: C:\Users\DittNamn\.ssh\id_ed25519

# Starta SSH agent (i Git Bash)
eval "$(ssh-agent -s)"

# Lägg till nyckel
ssh-add ~/.ssh/id_ed25519

# Kopiera public key
cat ~/.ssh/id_ed25519.pub
# Lägg till i GitHub: Settings → SSH and GPG keys → New SSH key

# Testa connection
ssh -T git@github.com

# Använd SSH URLs istället för HTTPS
git clone git@github.com:användarnamn/repo.git
```

#### Del 3: Miniconda Integration

**Problem:** Conda är inte tillgängligt i Git Bash som standard.

**Lösning 1: Använd Anaconda Prompt med Git**

Git är tillgängligt i Anaconda Prompt efter installation. Detta är den enklaste lösningen.

**Lösning 2: Aktivera Conda i Git Bash**

```bash
# I Git Bash, navigera till Miniconda Scripts
cd /c/Users/DittAnvändarnamn/miniconda3/Scripts

# Initiera conda för bash
./conda init bash

# Starta om Git Bash

# Nu fungerar conda kommandon!
conda --version
conda activate your_env
```

**Lösning 3: Windows Terminal (Mest moderna approach)**

```powershell
# Installera Windows Terminal (om inte redan installerat)
winget install Microsoft.WindowsTerminal

# Lägg till Anaconda Prompt profile i Windows Terminal
# Settings → Add new profile → Miniconda3
# Command line: C:\Users\DittNamn\miniconda3\Scripts\activate.bat
```

#### Del 4: .gitignore för Python/Miniconda projekt

Skapa alltid en `.gitignore`-fil i ditt projekt:

```bash
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Conda
conda-meta/
.conda/

# Jupyter Notebook
.ipynb_checkpoints
*.ipynb_checkpoints/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Data (lägg till dina stora datafiler här)
*.csv
*.xlsx
*.pkl
*.h5
data/raw/*
!data/raw/.gitkeep

# Models
models/*.pkl
models/*.h5
*.model

# Logs
*.log
logs/

# Environment variables
.env
.env.local
```

### Avancerade Git Workflows

#### Feature Branch Workflow (Rekommenderat för team)

```bash
# 1. Börja alltid från uppdaterad main
git checkout main
git pull origin main

# 2. Skapa feature branch
git checkout -b feature/ny-funktionalitet

# 3. Arbeta och committa
git add .
git commit -m "feat: lägg till ny funktionalitet"

# 4. Håll branchen uppdaterad med main
git fetch origin
git rebase origin/main  # eller git merge origin/main

# 5. Push feature branch
git push -u origin feature/ny-funktionalitet

# 6. Skapa Pull Request på GitHub

# 7. Efter merge, städa upp
git checkout main
git pull origin main
git branch -d feature/ny-funktionalitet
git push origin --delete feature/ny-funktionalitet
```

#### Conventional Commits (Industri-standard)

Format: `<type>(<scope>): <subject>`

**Types:**
- `feat`: Ny funktionalitet
- `fix`: Buggfix
- `docs`: Dokumentation
- `style`: Formatering (ingen kod-ändring)
- `refactor`: Kod-omstrukturering
- `test`: Lägg till tester
- `chore`: Underhåll (dependencies, etc.)

**Exempel:**
```bash
git commit -m "feat(auth): lägg till tvåfaktorsautentisering"
git commit -m "fix(api): hantera timeout-fel korrekt"
git commit -m "docs(readme): uppdatera installationsinstruktioner"
```

### Vanliga Git-scenarier och lösningar

#### 1. Ångra senaste commit (inte pushad)

```bash
# Behåll ändringar i working directory
git reset --soft HEAD~1

# Ta bort ändringar helt
git reset --hard HEAD~1
```

#### 2. Ändra commit-meddelande

```bash
# Senaste commit
git commit --amend -m "Nytt meddelande"

# Äldre commit (avancerat)
git rebase -i HEAD~3  # Ändra 3 senaste commits
```

#### 3. Återställ en fil till tidigare version

```bash
# Från senaste commit
git checkout HEAD -- filnamn.txt

# Från specifik commit
git checkout abc1234 -- filnamn.txt
```

#### 4. Stash - Spara temporärt arbete

```bash
# Spara ändringar utan commit
git stash

# Lista stashes
git stash list

# Återställ senaste stash
git stash pop

# Återställ specifik stash
git stash apply stash@{1}
```

#### 5. Merge vs Rebase

**Merge** (skapar merge-commit):
```bash
git checkout main
git merge feature-branch
```

**Rebase** (linjär historik):
```bash
git checkout feature-branch
git rebase main
```

**När använda vad?**
- **Merge**: Public branches, bevarar exakt historik
- **Rebase**: Lokala ändringar, renare historik

#### 6. Cherry-pick - Applicera specifik commit

```bash
git cherry-pick abc1234
```

#### 7. Lösa merge-konflikter

```bash
# Efter git merge eller git pull
# 1. Öppna filer med konflikter
# 2. Sök efter markeringar:
#    <<<<<<< HEAD
#    din kod
#    =======
#    andras kod
#    >>>>>>> branch-name

# 3. Redigera manuellt
# 4. Lägg till resolved filer
git add konfliktfil.txt

# 5. Fortsätt merge
git commit
```

### Avancerade GitHub-funktioner

#### GitHub Actions (CI/CD)

Exempel `.github/workflows/python-tests.yml`:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v3

    - name: Setup Miniconda
      uses: conda-incubator/setup-miniconda@v2
      with:
        auto-update-conda: true
        python-version: 3.11

    - name: Install dependencies
      run: |
        conda install pytest
        conda install --file requirements.txt

    - name: Run tests
      run: pytest
```

#### Pull Request Best Practices

1. **Tydlig titel och beskrivning**
2. **Små, fokuserade PRs** (< 400 rader om möjligt)
3. **Länka till issues:** "Fixes #123"
4. **Request reviews** från teammedlemmar
5. **CI måste passa** innan merge

### Säkerhet och Best Practices (2025)

#### ⚠️ COMMITTA ALDRIG:

- **Secrets**: API-nycklar, lösenord, tokens
- **Credentials**: Database connection strings
- **Private keys**: SSH keys, certificates
- **Large files**: > 100MB (använd Git LFS)
- **Compiled code**: .pyc, .exe, .dll
- **Dependencies**: node_modules/, venv/

#### Skydda dig:

```bash
# Scanna för secrets innan commit
pip install detect-secrets
detect-secrets scan

# Git hooks för att förhindra secrets
# Installera pre-commit
pip install pre-commit

# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: detect-private-key
```

#### Om du råkat committa secrets:

```bash
# 1. Rotera secret OMEDELBART (generera nytt)
# 2. Ta bort från historik (BFG Repo-Cleaner)
java -jar bfg.jar --delete-files secrets.txt

# 3. Force push (FAR!)
git push --force
```

### Verktyg för produktivitet

#### GUI-klienter:

1. **GitHub Desktop** - Bäst för nybörjare
2. **GitKraken** - Visuellt imponerande
3. **SourceTree** - Kraftfullt för avancerade
4. **VS Code** - Inbyggt Git-stöd

#### CLI-verktyg:

```bash
# tig - Terminal Git browser
winget install tig

# lazygit - Terminal UI för git
winget install jesseduffield.lazygit

# gh - GitHub CLI
winget install GitHub.cli

# Exempel med gh:
gh repo create mitt-projekt --public
gh pr create --title "Fix bug" --body "Description"
gh pr list
gh pr checkout 123
```

### Komplett projekt-setup checklista:

```bash
# 1. Skapa projekt lokalt
mkdir mitt-projekt && cd mitt-projekt

# 2. Initiera Git
git init

# 3. Skapa .gitignore
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

# 4. Skapa README
echo "# Mitt Projekt" > README.md

# 5. Skapa conda environment
conda create -n mitt-projekt python=3.11
conda activate mitt-projekt

# 6. Exportera dependencies
conda list --export > requirements.txt

# 7. Initial commit
git add .
git commit -m "chore: initial commit"

# 8. Skapa GitHub repo (via gh CLI)
gh repo create mitt-projekt --public --source=. --remote=origin

# 9. Push
git push -u origin main

# 10. Setup GitHub Actions (valfritt)
mkdir -p .github/workflows
# Lägg till workflow-filer

# 11. Skapa branch för utveckling
git checkout -b develop
git push -u origin develop

# Klart! Börja koda!
```

### Felsökning vanliga problem:

#### Problem: "permission denied (publickey)"
```bash
# Lösning: Kontrollera SSH-setup
ssh -T git@github.com
# Om fel: Generera och lägg till ny SSH-key (se tidigare)
```

#### Problem: "fatal: not a git repository"
```bash
# Lösning: Inte i ett git-repo
git init  # eller
cd rätt-mapp
```

#### Problem: "Your branch is ahead of 'origin/main' by N commits"
```bash
# Lösning: Push dina commits
git push origin main
```

#### Problem: "CONFLICT (content): Merge conflict"
```bash
# Lösning: Lös konflikter manuellt
git status  # Se vilka filer som har konflikter
# Redigera filer och ta bort conflict markers
git add .
git commit
```

#### Problem: "Large files detected"
```bash
# Lösning: Använd Git LFS för stora filer
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

### Resurser för fortsatt lärande:

**Dokumentation:**
- https://git-scm.com/doc - Officiell Git-dokumentation
- https://docs.github.com - GitHub Docs
- https://learngitbranching.js.org - Interaktiv Git-tutorial

**Böcker:**
- "Pro Git" av Scott Chacon (gratis online)
- "Git Pocket Guide" av Richard E. Silverman

**Kurser:**
- GitHub Learning Lab
- Codecademy - Learn Git
- Udacity - Version Control with Git

**Cheat Sheets:**
- https://education.github.com/git-cheat-sheet-education.pdf
- https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet

### Snabbreferens - Viktigaste kommandona:

```bash
# SETUP
git config --global user.name "Namn"
git config --global user.email "email"
git init
git clone <url>

# BASIC WORKFLOW
git status
git add <fil>
git add .
git commit -m "meddelande"
git push
git pull

# BRANCHING
git branch                    # Lista branches
git branch <namn>            # Skapa branch
git checkout <namn>          # Byt branch
git checkout -b <namn>       # Skapa och byt
git merge <branch>           # Merga branch
git branch -d <namn>         # Ta bort branch

# HISTORY
git log
git log --oneline
git log --graph --all
git diff
git show <commit>

# UNDO
git reset --soft HEAD~1      # Ångra commit, behåll ändringar
git reset --hard HEAD~1      # Ångra commit, ta bort ändringar
git revert <commit>          # Skapa ny commit som ångrar
git checkout -- <fil>        # Återställ fil

# REMOTE
git remote add origin <url>
git remote -v
git fetch
git pull origin main
git push -u origin main

# STASH
git stash
git stash pop
git stash list
git stash apply

# HELP
git help <kommando>
git <kommando> --help
```

---

## 🎯 Sammanfattning och nästa steg

### Du har nu lärt dig:

1. **Vad Git och GitHub är** och varför de är viktiga
2. **Hur man installerar** Git på Windows 11 (2025-standard)
3. **Hur man konfigurerar** Git för första gången
4. **Hur man integrerar** Git med Miniconda
5. **Grundläggande kommandon** för dagligt arbete
6. **Avancerade tekniker** för professionell utveckling
7. **Säkerhet och best practices**

### Rekommenderad inlärningsväg:

**Vecka 1: Grunderna**
- Installera Git och GitHub Desktop
- Skapa ditt första repository
- Öva på: add, commit, push, pull
- Skapa .gitignore för dina Python-projekt

**Vecka 2: Branching**
- Skapa och byt mellan branches
- Merga branches
- Hantera enkla konflikter

**Vecka 3: Samarbete**
- Forka ett projekt på GitHub
- Skapa din första Pull Request
- Review någon annans kod

**Vecka 4: Avancerat**
- Prova rebase
- Använd git stash
- Sätt upp GitHub Actions
- Använd git hooks

### Praktisk övning att börja med:

```bash
# 1. Skapa ett övningsprojekt
mkdir git-ovning && cd git-ovning
git init

# 2. Skapa några filer
echo "print('Hello Git!')" > hello.py
echo "# Git Övning" > README.md

# 3. Committa
git add .
git commit -m "Initial commit"

# 4. Skapa en branch
git checkout -b test-branch

# 5. Gör ändringar
echo "print('Från test branch!')" > test.py
git add test.py
git commit -m "Add test file"

# 6. Byt tillbaka till main
git checkout main

# 7. Merga test-branch
git merge test-branch

# 8. Se historiken
git log --oneline --graph

# Grattis! Du har nu använt Git!
```

### Tips för framgång:

1. **Committa ofta** - Små, frekventa commits är bättre än stora
2. **Skriv bra commit-meddelanden** - Framtida du kommer tacka dig
3. **Använd branches** - Testa nya idéer utan risk
4. **Läs error messages** - Git ger ofta hjälpsamma förslag
5. **Gör fel i ett test-repo** - Bästa sättet att lära sig
6. **Använd GitHub Desktop** till en början om CLI känns svårt
7. **Backup viktiga projekt** på GitHub
8. **Lär dig lite varje dag** - Git är enormt, ingen kan allt

---

**Lycka till med din Git-resa! 🚀**

*Om du har frågor, googla alltid frågan + "git" eller fråga på Stack Overflow.*
*Git community är enormt hjälpsam!*
