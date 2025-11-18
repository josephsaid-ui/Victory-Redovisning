# 🔐 Nivå 4C Del 1: Password Attacks - Offline Cracking

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [⬅️ Nivå 4B: Exploitation](niva-4b-exploitation.md)

---

## 🔴 KRITISK JURIDISK VARNING

```
⚖️  OBEHÖRIGT LÖSENORDSKNÄCKANDE ÄR OLAGLIGT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ FÖRBJUDET:
   • Knäcka lösenord till system du INTE äger
   • Testa lösenord mot tjänster utan SKRIFTLIGT tillstånd
   • Använda stolna/läckta hashar från verkliga system
   • Distribuera knäckta lösenord
   • Brute-force attacker mot produktionssystem

✅ TILLÅTET (med explicit tillstånd):
   • Egna system och konton du äger
   • Penetrationstestning med SKRIFTLIGT kontrakt
   • CTF-tävlingar och säkerhetslabbar
   • Educational labs (DVWA, Metasploitable, HackTheBox)
   • Forensisk analys med legal auktorisation

🇸🇪 SVENSK LAG:
   Brottsbalken 4 kap. 9c § - Dataintrång
   → Upp till 2 års fängelse
   → Dokumenterad intention räcker för åtal

🌍 INTERNATIONELLT:
   • USA: CFAA - upp till 10 år
   • EU: GDPR-böter + straffrättsliga påföljder
   • UK: Computer Misuse Act - upp till 10 år
```

**🛑 ANSVARSFRISKRIVNING:**
Författaren tar INGET ansvar för missbruk av denna information. DU är PERSONLIGT ansvarig för dina handlingar.

---

## 📚 Innehållsförteckning

1. [Introduktion till Password Cracking](#introduktion)
2. [Hash-typer och Kryptografi](#hash-typer)
3. [John the Ripper](#john-the-ripper)
4. [Hashcat](#hashcat)
5. [Wordlists och Regelbaserade Attacker](#wordlists)
6. [Praktiska Övningar](#praktiska-övningar)
7. [Självtest](#självtest)
8. [Sammanfattning och Checklista](#sammanfattning)

---

## 🎯 Introduktion till Password Cracking {#introduktion}

### Vad är Password Cracking?

**Password cracking** är processen att återställa lösenord från krypterade eller hashade format. Detta är en kritisk färdighet inom:

- 🔍 **Penetrationstestning** - Testa lösenordsstyrka
- 🕵️ **Digital forensik** - Återställa data från krypterade volymer
- 🔐 **Security auditing** - Hitta svaga lösenord i organisationer
- 🎓 **Utbildning** - Förstå hur attackerare arbetar

### Offline vs Online Password Attacks

| Aspekt | Offline Cracking | Online Attacks |
|--------|------------------|----------------|
| **Måltyp** | Hash-filer, databaser, krypterade arkiv | Levande tjänster (SSH, FTP, HTTP) |
| **Hastighet** | Miljontals försök/sekund | Hundratals försök/sekund |
| **Detekterbarhet** | Ingen risk (lokalt) | Hög risk (loggas av servern) |
| **Begränsningar** | Behöver hash-fil först | Rate limiting, account lockouts |
| **Verktyg** | John, Hashcat | Hydra, Medusa, Ncrack |
| **GPU-acceleration** | Ja (Hashcat) | Nej (nätverksbegränsad) |

**🔴 DENNA GUIDE:** Fokuserar på **offline cracking** (John the Ripper, Hashcat)
**🟡 NÄSTA GUIDE:** Täcker **online attacks** (Hydra, Medusa, CeWL)

### Attack-typer

```
┌─────────────────────────────────────────────────────┐
│  PASSWORD CRACKING ATTACK-TYPER                     │
└─────────────────────────────────────────────────────┘

1️⃣  DICTIONARY ATTACK (Ordlisteattack)
    ├─ Testar ord från fördefinierad lista
    ├─ Snabbt men begränsat till listans innehåll
    └─ Exempel: rockyou.txt (14M lösenord)

2️⃣  BRUTE FORCE (Rå kraft)
    ├─ Testar ALLA möjliga kombinationer
    ├─ Garanterat lyckas (givet tillräcklig tid)
    └─ Extremt långsamt för långa lösenord

3️⃣  HYBRID ATTACK
    ├─ Kombinerar ordlista + brute force
    ├─ Exempel: password → password123, p@ssw0rd
    └─ Regler för substitution och tillägg

4️⃣  RAINBOW TABLE
    ├─ Förberäknade hash-tabeller
    ├─ Extremt snabbt men kräver mycket lagring
    └─ Ineffektivt mot saltade hashar

5️⃣  RULE-BASED ATTACK
    ├─ Applicerar transformationsregler på ordlistor
    ├─ Kapitalisering, läggning, substitution
    └─ Balans mellan hastighet och täckning
```

### Tid och Komplexitet

**Hur lång tid tar det att knäcka ett lösenord?**

| Lösenord | Komplexitet | MD5 (GPU) | bcrypt |
|----------|-------------|-----------|--------|
| `password` | Lowercase 8 char | < 1 sekund | < 1 sekund |
| `Password1` | Mixed + siffra | < 1 minut | ~ 5 minuter |
| `P@ssw0rd!` | Mixed + special | ~ 1 timme | ~ 2 dagar |
| `Tr0ub4dor&3` | 11 char mixed | ~ 2 dagar | ~ 50 år |
| `correct horse battery staple` | 4 ord (28 char) | ~ 100 år | Praktiskt omöjligt |

**🟢 NOTERA:** Moderna hash-algoritmer som **bcrypt**, **scrypt** och **Argon2** är designade för att vara LÅNGSAMMA, vilket gör brute force extremt tidskrävande.

---

## 🔐 Hash-typer och Kryptografi {#hash-typer}

### Vad är en Hash?

En **hash** är en envägsfunktion som konverterar indata (lösenord) till en fix-längd sträng:

```bash
# Exempel: MD5 hash
echo -n "password" | md5sum
# Output: 5f4dcc3b5aa765d61d8327deb882cf99

# Samma input → Samma output (deterministiskt)
echo -n "password" | md5sum
# Output: 5f4dcc3b5aa765d61d8327deb882cf99

# Liten ändring → Helt annorlunda hash
echo -n "Password" | md5sum
# Output: dc647eb65e6711e155375218212b3964
```

**Egenskaper hos kryptografiska hashar:**
- ✅ Envägsfunktion (kan ej reverseras)
- ✅ Deterministisk (samma input → samma output)
- ✅ Snabb att beräkna
- ✅ Avalanche effect (liten ändring → stor skillnad)
- ✅ Kollisionsresistent (svårt hitta två inputs med samma hash)

### Vanliga Hash-algoritmer

| Algoritm | Hash-längd | Hastighet | Säkerhet | Användning |
|----------|------------|-----------|----------|------------|
| **MD5** | 128 bit (32 hex) | ⚡ Mycket snabb | ❌ OSÄKER | Legacy-system |
| **SHA-1** | 160 bit (40 hex) | ⚡ Snabb | ⚠️ Deprecierad | Git commits |
| **SHA-256** | 256 bit (64 hex) | ⚡ Snabb | ✅ Säker | Blockchain, SSL |
| **NTLM** | 128 bit (32 hex) | ⚡ Mycket snabb | ❌ OSÄKER | Windows (legacy) |
| **bcrypt** | 184 bit | 🐌 Långsam (design) | ✅ Mycket säker | Web apps |
| **scrypt** | Variabel | 🐌 Långsam + RAM-krävande | ✅ Mycket säker | Kryptowallets |
| **Argon2** | Variabel | 🐌 Långsam + RAM-krävande | ✅ Bäst-i-klassen | Moderna system |

### Salting

**Salt** är slumpmässig data som läggs till lösenordet före hashning:

```
Utan salt:
password → MD5 → 5f4dcc3b5aa765d61d8327deb882cf99

Med salt:
password + aB3xZ → MD5 → f7c3bc1d808e04732adf679965ccc34ca014c657
password + kL9mN → MD5 → 8b6d8c9a4d5e3f2a1b0c9d8e7f6a5b4c (olika!)
```

**🔴 VIKTIGT:** Salt förhindrar **rainbow table-attacker** eftersom varje lösenord får en unik hash även om lösenorden är identiska.

### Identifiera Hash-typer

Kali Linux inkluderar verktyg för att identifiera hash-typer:

```bash
# hash-identifier (interaktiv)
hash-identifier

# hashid (kommandorad)
hashid '5f4dcc3b5aa765d61d8327deb882cf99'
# Output: Possible algorithms: MD5, NTLM

# hashid med John/Hashcat mode-nummer
hashid -m '5f4dcc3b5aa765d61d8327deb882cf99'
# Output:
# [+] MD5 [Hashcat Mode: 0]
# [+] NTLM [Hashcat Mode: 1000]
```

---

## 🔨 John the Ripper {#john-the-ripper}

### Översikt

**John the Ripper** (ofta kallad "John") är ett av de mest populära och kraftfulla password cracking-verktygen.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | Openwall Project (Solar Designer) |
| **Licens** | Open source (GPL) |
| **Plattformar** | Linux, Windows, macOS |
| **Hash-stöd** | 100+ format (Unix, Windows, databaser, arkiv) |
| **Attack-lägen** | Single, Wordlist, Incremental (brute force) |
| **GPU-stöd** | Begränsat (bättre i "John Jumbo") |

### Installation

John är förinstallerat i Kali Linux:

```bash
# Verifiera installation
john --version
# Output: John the Ripper 1.9.0-jumbo-1 OMP

# Lista alla hash-format som stöds
john --list=formats
# Output: descrypt, bsdicrypt, md5crypt, bcrypt, LM, AFS, ...

# Lista specifika subformats
john --list=format-details | grep -i ntlm
```

**🟢 TIP:** Kali inkluderar **John Jumbo**, en community-förbättrad version med stöd för fler hash-typer och GPU-acceleration.

### Grundläggande Användning

#### Steg 1: Förbered Hash-filen

John kräver hashar i textformat, vanligtvis en per rad:

```bash
# Exempel: hash.txt
cat hash.txt
5f4dcc3b5aa765d61d8327deb882cf99
```

#### Steg 2: Enklaste Attack (Auto-läge)

```bash
# John detekterar automatiskt hash-typ och använder standardordlista
john hash.txt

# Output exempel:
# Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
# Press 'q' or Ctrl-C to abort, almost any other key for status
# password         (?)
# 1g 0:00:00:00 DONE (2025-01-15 10:42) 100.0g/s 819200p/s
```

**Förklaring:**
- `1g` = 1 hash knäckt
- `100.0g/s` = 100 hashar per sekund
- `819200p/s` = 819,200 lösenordsförsök per sekund

#### Steg 3: Visa Resultat

```bash
# Visa alla knäckta lösenord
john --show hash.txt
# Output: ?:password

# Visa i specifikt format
john --show --format=Raw-MD5 hash.txt
```

### Attack-lägen

#### 1️⃣ Single Crack Mode

**Syftar till att snabbt knäcka lösenord baserat på användarnamn:**

```bash
# Format: username:hash
cat user_hash.txt
admin:5f4dcc3b5aa765d61d8327deb882cf99
john:e10adc3949ba59abbe56e057f20f883e

# Single crack (testar variationer av användarnamnet)
john --single user_hash.txt

# John testar: admin, Admin, ADMIN, admin123, adm1n, etc.
```

**🟢 TIP:** Single mode är mycket snabb och bör ALLTID köras först.

#### 2️⃣ Wordlist Mode

**Testar lösenord från en ordlista:**

```bash
# Använd standardordlista (password.lst)
john --wordlist=/usr/share/john/password.lst hash.txt

# Använd rockyou (14M lösenord)
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Custom wordlist
john --wordlist=/path/to/custom.txt hash.txt
```

**Populära ordlistor i Kali:**

| Ordlista | Storlek | Beskrivning |
|----------|---------|-------------|
| `/usr/share/john/password.lst` | ~4,000 | Johns standard (snabb) |
| `/usr/share/wordlists/rockyou.txt` | ~14M | Läckta lösenord från 2009 |
| `/usr/share/wordlists/fasttrack.txt` | ~222 | Vanliga default-lösenord |
| `/usr/share/seclists/Passwords/` | Varierar | Stora samlingar (måste installeras) |

#### 3️⃣ Incremental Mode (Brute Force)

**Testar alla möjliga kombinationer:**

```bash
# Brute force med standard charset (ASCII)
john --incremental hash.txt

# Brute force endast lowercase (snabbare)
john --incremental:Lower hash.txt

# Brute force siffror (t.ex. PIN-koder)
john --incremental:Digits hash.txt

# Custom charset i john.conf
john --incremental:Custom hash.txt
```

**⚠️ VARNING:** Incremental mode är EXTREMT långsamt för långa lösenord:

```
4 tecken (lowercase) → ~10 sekunder
6 tecken (lowercase) → ~2 timmar
8 tecken (mixed)     → ~flera år
```

#### 4️⃣ Rule-based Attack

**Applicerar transformationsregler på ordlistor:**

```bash
# Använd standardregler
john --wordlist=rockyou.txt --rules hash.txt

# Använd specifik regelset
john --wordlist=rockyou.txt --rules=Jumbo hash.txt

# Lista tillgängliga regelsets
john --list=rules
```

**Exempel på regler (från john.conf):**

| Regel | Beskrivning | Exempel |
|-------|-------------|---------|
| `c` | Kapitalisera första bokstaven | password → Password |
| `u` | Alla versaler | password → PASSWORD |
| `l` | Alla gemener | PASSWORD → password |
| `$1 $2 $3` | Lägg till siffror i slutet | password → password123 |
| `^! ^@` | Lägg till special i början | password → @!password |
| `so0 si1 sa@` | Substitution (leet speak) | password → p@ssw0rd |

**Custom regelset (john.conf):**

```ini
[List.Rules:MyRules]
# Kapitalisera + lägg till siffror
c $1 $2 $3
c $! $@

# Leet speak substitutions
so0 si1 se3 sa@
```

Använd:

```bash
john --wordlist=rockyou.txt --rules=MyRules hash.txt
```

### Hash-format

#### Unix/Linux Lösenord (/etc/shadow)

```bash
# Extrahera hashar från /etc/shadow (kräver root)
sudo unshadow /etc/passwd /etc/shadow > unix_hashes.txt

# Knäck Unix-lösenord
john unix_hashes.txt
```

**Exempel /etc/shadow-rad:**

```
user:$6$salt$hash:18993:0:99999:7:::
      │  │    │
      │  │    └─ SHA-512 hash
      │  └────── Salt
      └───────── Hash-algoritm (6 = SHA-512)
```

**Unix crypt-format:**

| ID | Algoritm | Format |
|----|----------|--------|
| `$1$` | MD5 | `$1$salt$hash` |
| `$2a$` / `$2y$` | bcrypt | `$2a$cost$salthash` |
| `$5$` | SHA-256 | `$5$rounds$salt$hash` |
| `$6$` | SHA-512 | `$6$rounds$salt$hash` |

#### Windows NTLM

```bash
# Format: username:RID:LM:NTLM:::
cat windows_hashes.txt
Administrator:500:aad3b435b51404eeaad3b435b51404ee:8846f7eaee8fb117ad06bdd830b7586c:::

# Specificera format
john --format=NT windows_hashes.txt
```

#### Zip/RAR Arkiv

```bash
# Extrahera hash från ZIP
zip2john encrypted.zip > zip_hash.txt

# Knäck ZIP-lösenord
john zip_hash.txt

# Extrahera hash från RAR
rar2john encrypted.rar > rar_hash.txt
john rar_hash.txt
```

**Andra *2john verktyg:**

```bash
# Lista alla tillgängliga
ls /usr/share/john/*2john*

# Vanliga:
pdf2john encrypted.pdf > pdf_hash.txt
ssh2john id_rsa > ssh_hash.txt
keepass2john database.kdbx > keepass_hash.txt
office2john document.docx > office_hash.txt
```

### Avancerade Tekniker

#### Session Management

```bash
# Starta session med namn
john --session=mycrack hash.txt

# Återuppta session (vid Ctrl+C eller krasch)
john --restore=mycrack

# Lista aktiva sessioner
john --list=sessions
```

#### Status och Statistik

```bash
# Visa status under körning (tryck valfri tangent)
# Output:
# 0g 0:00:03:45 3/3 0g/s 1234Kp/s 1234Kc/s 1234KC/s
# guesses: 0 time: 0:00:03:45 (3) c/s: 1234K

# Förklaring:
# 0g        = 0 hashar knäckta
# 0:00:03:45 = Körtid
# 3/3       = Progress (3 av 3 salts)
# 1234Kp/s  = Kandidater per sekund (passwords tested)
```

#### Fork Mode (Parallell Körning)

```bash
# Använd flera CPU-kärnor
john --fork=4 hash.txt

# Optimal fork för ditt system (antal kärnor)
john --fork=$(nproc) hash.txt
```

#### Mask Attack

```bash
# Format: ?a (alla), ?l (lowercase), ?u (uppercase), ?d (digit), ?s (special)

# 8 tecken, lowercase följt av 2 siffror
john --mask='?l?l?l?l?l?l?d?d' hash.txt
# Testar: aaaaaaaa00, aaaaaaaa01, ..., zzzzzzzz99

# Password följt av år
john --mask='password?d?d?d?d' hash.txt
# Testar: password2020, password2021, ..., password2025
```

### John Configuration (john.conf)

John's beteende styrs av `/etc/john/john.conf` eller `~/.john/john.conf`:

```bash
# Visa aktuell konfiguration
cat /etc/john/john.conf

# Custom konfiguration (exempel)
cat ~/.john/john.conf
```

**Viktiga sektioner:**

```ini
[Options]
# Wordlist om ingen anges
Wordlist = /usr/share/wordlists/rockyou.txt
# Idle = Y (kör med låg prioritet)

[List.Rules:CustomRules]
# Dina egna regler här
c $1 $2 $3
so0 si1

[Incremental:LowerNum]
# Custom charset för brute force
File = $JOHN/lower.chr
MinLen = 4
MaxLen = 8
CharCount = 36
```

### Exempel: Komplett Workflow

```bash
# 1. Identifiera hash-typ
hashid -m hashes.txt

# 2. Single crack mode (snabbast)
john --single hashes.txt

# 3. Wordlist med regler
john --wordlist=/usr/share/wordlists/rockyou.txt --rules=Jumbo hashes.txt

# 4. Brute force (om tid finns)
john --incremental:Lower hashes.txt

# 5. Visa alla knäckta lösenord
john --show hashes.txt

# 6. Exportera resultat
john --show --format=Raw-MD5 hashes.txt > cracked_passwords.txt
```

---

## ⚡ Hashcat {#hashcat}

### Översikt

**Hashcat** är världens snabbaste password cracker med GPU-acceleration.

| Egenskap | Detalj |
|----------|--------|
| **Utvecklare** | Jens Steube (@hashcat) |
| **Licens** | MIT (open source) |
| **Plattformar** | Linux, Windows, macOS |
| **GPU-stöd** | NVIDIA, AMD, Apple Metal |
| **Hash-stöd** | 300+ algoritmer |
| **Hastighet** | 100-1000x snabbare än CPU (beroende på GPU) |

**🔥 FÖRDEL:** Hashcat kan knäcka MD5 med hastigheter över **100 miljarder försök/sekund** på high-end GPU:er.

### Installation

```bash
# Hashcat är förinstallerat i Kali Linux
hashcat --version
# Output: v6.2.6

# Installera senaste versionen (om ej uppdaterat)
sudo apt update
sudo apt install hashcat

# Verifiera GPU-stöd (NVIDIA exempel)
hashcat -I
# Output visar tillgängliga OpenCL/CUDA-enheter
```

### Grundläggande Användning

#### Syntax

```bash
hashcat [options] hashfile [wordlist|mask]
```

**Viktiga parametrar:**

| Parameter | Beskrivning |
|-----------|-------------|
| `-m <num>` | Hash-typ (mode) |
| `-a <num>` | Attack-mode (0=straight, 3=brute force, 6=hybrid) |
| `-o <file>` | Output-fil för knäckta lösenord |
| `--show` | Visa tidigare knäckta hashar |
| `-w <1-4>` | Workload profil (1=låg, 4=nightmare) |
| `--force` | Tvinga körning (ej rekommenderat i produktion) |

#### Hash-modes (Vanliga)

| Mode | Algoritm | Exempel |
|------|----------|---------|
| `0` | MD5 | `5f4dcc3b5aa765d61d8327deb882cf99` |
| `100` | SHA-1 | `5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8` |
| `1000` | NTLM | `8846f7eaee8fb117ad06bdd830b7586c` |
| `1400` | SHA-256 | `5e884898da28047151d0e56f8dc6292773603d0d...` |
| `1800` | SHA-512 (Unix) | `$6$rounds=5000$salt$hash...` |
| `3200` | bcrypt | `$2a$10$salt$hash...` |
| `22000` | WPA/WPA2 | PMKID/EAPOL |

**🔍 Hitta din hash-mode:**

```bash
# Sök efter hash-typ
hashcat --help | grep -i "ntlm"
# Output: 1000 | NTLM

# Använd hashid (visar Hashcat mode)
hashid -m '5f4dcc3b5aa765d61d8327deb882cf99'
# Output: [+] MD5 [Hashcat Mode: 0]
```

### Attack-modes

#### Attack Mode 0: Straight (Wordlist)

```bash
# Enklaste attack - rak ordlista
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt

# Med output-fil
hashcat -m 0 -a 0 hashes.txt rockyou.txt -o cracked.txt

# Med regler (best64.rule ingår i Hashcat)
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

#### Attack Mode 1: Combinator

**Kombinerar två ordlistor:**

```bash
# Kombinera list1 + list2
# Exempel: "pass" + "word" = "password"
hashcat -m 0 -a 1 hashes.txt wordlist1.txt wordlist2.txt
```

#### Attack Mode 3: Brute Force (Mask)

**Testar alla kombinationer enligt mask:**

```bash
# Mask-tecken:
# ?l = lowercase (abcdefghijklmnopqrstuvwxyz)
# ?u = uppercase (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
# ?d = digits (0123456789)
# ?h = hex (0123456789abcdef)
# ?H = HEX (0123456789ABCDEF)
# ?s = special (!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)
# ?a = all (?l?u?d?s)
# ?b = binary (0x00 - 0xFF)

# 8 lowercase tecken
hashcat -m 0 -a 3 hashes.txt ?l?l?l?l?l?l?l?l

# 6 tecken mixed case + siffror
hashcat -m 0 -a 3 hashes.txt ?1?1?1?1?1?1 -1 ?l?u?d

# "Password" + 2 siffror
hashcat -m 0 -a 3 hashes.txt Password?d?d

# Custom charset
hashcat -m 0 -a 3 hashes.txt ?1?1?1?1 -1 abc123
# Testar: aaaa, aaab, aaac, aaa1, ...
```

#### Attack Mode 6: Hybrid Wordlist + Mask

**Ordlista följt av brute force:**

```bash
# Wordlist + 2 siffror
hashcat -m 0 -a 6 hashes.txt rockyou.txt ?d?d
# password → password01, password02, ..., password99

# Wordlist + år
hashcat -m 0 -a 6 hashes.txt rockyou.txt ?d?d?d?d
# password → password2020, password2021, ..., password2025
```

#### Attack Mode 7: Hybrid Mask + Wordlist

**Brute force följt av ordlista:**

```bash
# 2 siffror + wordlist
hashcat -m 0 -a 7 hashes.txt ?d?d rockyou.txt
# password → 01password, 02password, ..., 99password
```

### Regelbaserade Attacker

Hashcat inkluderar kraftfulla regelsets:

```bash
# Lista alla regler
ls /usr/share/hashcat/rules/
# Output: best64.rule, leetspeak.rule, toggles1.rule, ...

# Använd best64 (64 vanliga transformationer)
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule

# Kombinera flera regelsets
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r best64.rule -r toggles1.rule

# OneRuleToRuleThemAll (community-favorit)
# Ladda ner från: https://github.com/NotSoSecure/password_cracking_rules
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r OneRuleToRuleThemAll.rule
```

**Populära regelsets:**

| Regelset | Antal regler | Beskrivning |
|----------|--------------|-------------|
| `best64.rule` | 64 | Bästa balansen snabbhet/täckning |
| `leetspeak.rule` | ~1,000 | Leet speak (a→@, e→3, o→0) |
| `rockyou-30000.rule` | 30,000 | Stora transformationer |
| `OneRuleToRuleThemAll.rule` | ~52,000 | Community-kuraterad (bäst) |

### Workload Profiles

```bash
# -w <1-4> bestämmer GPU-belastning

# -w 1: Låg (dator fortfarande användbar)
hashcat -m 0 -a 0 -w 1 hashes.txt rockyou.txt

# -w 2: Default (balans)
hashcat -m 0 -a 0 -w 2 hashes.txt rockyou.txt

# -w 3: Hög (desktop långsam)
hashcat -m 0 -a 0 -w 3 hashes.txt rockyou.txt

# -w 4: Nightmare (endast för dedikerade servrar)
hashcat -m 0 -a 0 -w 4 hashes.txt rockyou.txt
```

**🟡 REKOMMENDATION:** Använd `-w 3` för offline cracking på dedikerad maskin.

### Session Management

```bash
# Starta namngiven session
hashcat -m 0 -a 0 --session=mycrack hashes.txt rockyou.txt

# Pausa session (Ctrl+C eller 'p' under körning)
# Återuppta session
hashcat --session=mycrack --restore

# Visa status under körning
# Tryck 's' = Status
# Tryck 'p' = Pausa
# Tryck 'r' = Återuppta
# Tryck 'q' = Avsluta
```

### Benchmark

```bash
# Testa din GPU-prestanda
hashcat -b

# Output exempel (NVIDIA RTX 3080):
# * Hash-Mode 0 (MD5)                    → 58000.0 MH/s
# * Hash-Mode 1000 (NTLM)                → 95000.0 MH/s
# * Hash-Mode 1400 (SHA-256)             → 28000.0 MH/s
# * Hash-Mode 3200 (bcrypt)              → 98000 H/s

# Benchmark specifik hash-mode
hashcat -b -m 0
```

**Tolkningar:**
- `MH/s` = Mega Hashes per sekund (miljoner)
- `GH/s` = Giga Hashes per sekund (miljarder)
- `H/s` = Hashes per sekund (för långsamma algoritmer som bcrypt)

### Optimering

#### GPU-optimering

```bash
# Använd alla GPU:er
hashcat -m 0 -a 0 -d 1,2,3 hashes.txt rockyou.txt

# Använd endast GPU 1
hashcat -m 0 -a 0 -d 1 hashes.txt rockyou.txt

# Optimerad kernel
hashcat -m 0 -a 0 -O hashes.txt rockyou.txt
# ⚠️ Begränsar max lösenordslängd men ökar hastighet
```

#### Status och Debug

```bash
# Visa detaljerad status varje 10 sekunder
hashcat -m 0 -a 0 --status --status-timer=10 hashes.txt rockyou.txt

# Debug-läge (visa kandidater)
hashcat -m 0 -a 0 --debug-mode=1 --debug-file=debug.txt hashes.txt rockyou.txt
```

### Exempel: Praktiska Scenarion

#### Scenario 1: Knäcka MD5 Hash

```bash
# Hash-fil
echo '5f4dcc3b5aa765d61d8327deb882cf99' > md5_hash.txt

# Attack med rockyou
hashcat -m 0 -a 0 md5_hash.txt /usr/share/wordlists/rockyou.txt -o cracked.txt

# Visa resultat
cat cracked.txt
# Output: 5f4dcc3b5aa765d61d8327deb882cf99:password
```

#### Scenario 2: Knäcka Windows NTLM

```bash
# NTLM hash (från Windows SAM)
echo '8846f7eaee8fb117ad06bdd830b7586c' > ntlm_hash.txt

# Attack med hybrid (wordlist + siffror)
hashcat -m 1000 -a 6 ntlm_hash.txt rockyou.txt ?d?d?d

# Visa resultat
hashcat -m 1000 ntlm_hash.txt --show
# Output: 8846f7eaee8fb117ad06bdd830b7586c:Password123
```

#### Scenario 3: Knäcka bcrypt (Långsam)

```bash
# bcrypt hash
echo '$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy' > bcrypt_hash.txt

# Attack (bcrypt är MYCKET långsam)
hashcat -m 3200 -a 0 -w 3 bcrypt_hash.txt rockyou.txt

# Förväntad hastighet: ~50,000 H/s (vs MD5: 50 GH/s)
# Tid för rockyou (14M): ~3 dagar
```

#### Scenario 4: Mask Attack för PIN-kod

```bash
# Testa alla 4-siffriga PIN-koder (0000-9999)
hashcat -m 0 -a 3 pin_hash.txt ?d?d?d?d

# Tid: < 1 sekund (10,000 kombinationer)
```

---

## 📚 Wordlists och Regelbaserade Attacker {#wordlists}

### Populära Wordlists

#### Kali Linux Standard

```bash
# Rockyou (MÅSTE dekomprimera först)
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Storlek
wc -l /usr/share/wordlists/rockyou.txt
# Output: 14,344,392 rockyou.txt

# Fasttrack (vanliga default-lösenord)
cat /usr/share/wordlists/fasttrack.txt
# admin, password, root, cisco, ...
```

#### SecLists (Installera separat)

```bash
# Installera SecLists
sudo apt install seclists

# Plats
ls /usr/share/seclists/Passwords/

# Populära listor:
# - Common-Credentials/10-million-password-list-top-1000000.txt
# - Leaked-Databases/rockyou-75.txt
# - Common-Credentials/best1050.txt
```

#### CrackStation (Extern)

```bash
# Ladda ner från: https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm
# Storlek: 15 GB (1.5 miljarder ord)
wget https://crackstation.net/files/crackstation.txt.gz
gunzip crackstation.txt.gz

# Använd med John/Hashcat
john --wordlist=crackstation.txt hashes.txt
```

### Skapa Custom Wordlists

#### CeWL (Custom Wordlist Generator)

**CeWL** skapar wordlists från webbplatser (behandlas i nästa del: 4C Del 2).

#### Crunch (Pattern-baserad Generator)

```bash
# Installera crunch
sudo apt install crunch

# Generera 4-6 tecken (lowercase)
crunch 4 6 -o wordlist.txt
# ⚠️ VARNING: Genererar MILJONTALS ord

# Generera med specifika tecken
crunch 4 4 abc123
# Output: aaaa, aaab, aaac, aaa1, aaa2, ...

# Pattern (@=lowercase, ,=uppercase, %=digit, ^=special)
crunch 8 8 -t pass%%%% -o passwords.txt
# Output: pass0000, pass0001, ..., pass9999

# Pipe direkt till Hashcat (spara diskutrymme)
crunch 4 4 abc123 | hashcat -m 0 -a 0 hashes.txt
```

#### CUPP (Common User Passwords Profiler)

```bash
# Installera CUPP
git clone https://github.com/Mebus/cupp.git
cd cupp

# Interaktiv profil-baserad wordlist
python3 cupp.py -i

# Svarar på frågor om målperson:
# Namn: John Smith
# Födelsedatum: 1990-05-15
# Partner: Jane
# Husdjur: Fluffy
# Hobby: Football

# CUPP genererar: john1990, smith15, fluffy!, jane2015, football, ...
```

### John the Ripper Regler

#### Fördefinierade Regelsets

```bash
# Lista alla regelsets
john --list=rules

# Använd specifikt regelset
john --wordlist=rockyou.txt --rules=Single hashes.txt
john --wordlist=rockyou.txt --rules=Jumbo hashes.txt
```

#### Custom Regelset

**Skapa ~/.john/john.conf:**

```ini
[List.Rules:MyCustom]
# Kapitalisera första bokstaven
c
# Alla versaler
u
# Lägg till vanliga siffror
$1 $2 $3
$1 $9 $9 $0
$2 $0 $2 $5
# Leet speak
so0 si1 se3 sa@
# Kombinera: kapitalisering + leet + siffror
cso0si1 $!
```

**Använd:**

```bash
john --wordlist=custom.txt --rules=MyCustom hashes.txt
```

**Vanliga regel-kommandon:**

| Kommando | Beskrivning | Exempel |
|----------|-------------|---------|
| `c` | Capitalize (första bokstav versal) | password → Password |
| `u` | Uppercase (alla versaler) | password → PASSWORD |
| `l` | Lowercase (alla gemener) | PASSWORD → password |
| `t` | Toggle case (växla) | Password → pASSWORD |
| `$X` | Append (lägg till X i slutet) | password → password1 |
| `^X` | Prepend (lägg till X i början) | password → 1password |
| `sXY` | Substitute (ersätt X med Y) | password → p@ssword |
| `d` | Duplicate (dubblera) | password → passwordpassword |
| `r` | Reverse (vänd) | password → drowssap |

### Hashcat Regler

#### Best64.rule (Rekommenderad)

```bash
# Använd best64 för bästa balans
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**Exempel transformationer:**

```
password → Password
password → PASSWORD
password → password1
password → password123
password → p@ssw0rd
password → Password1!
```

#### Custom Hashcat Regler

**Skapa `my.rule`:**

```
# Kapitalisering
c
u

# Lägg till siffror
$1 $2 $3
$2 $0 $2 $5

# Leet speak
so0 si1 se3 sa@

# Kombinationer
cso0si1se3
```

**Använd:**

```bash
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r my.rule
```

---

## 🧪 Praktiska Övningar {#praktiska-övningar}

### 🔬 Övning 1: Knäcka MD5 Hash med John

**Scenario:** Du har hittat en MD5 hash i en databas-dump.

```bash
# 1. Skapa test-hash
echo -n "summer2024" | md5sum
# Output: a1b2c3d4e5f6... (exempelhash)

# 2. Spara hash i fil
echo 'a1b2c3d4e5f6...' > exercise1.txt

# 3. Identifiera hash-typ
hashid -m exercise1.txt

# 4. Försök single crack
john --single exercise1.txt

# 5. Wordlist attack
john --wordlist=/usr/share/wordlists/rockyou.txt exercise1.txt

# 6. Visa resultat
john --show exercise1.txt
```

**✅ Förväntat resultat:** Lösenordet "summer2024" knäckt.

---

### 🔬 Övning 2: Regelbaserad Attack med Hashcat

**Scenario:** Du vet att målföretaget använder "Password" + årtalet som policy.

```bash
# 1. Skapa test-hash (Password2025)
echo -n "Password2025" | md5sum > exercise2.txt

# 2. Skapa minimal wordlist
echo "password" > mini_wordlist.txt

# 3. Skapa regelset (my_rule.rule)
cat > my_rule.rule << EOF
c $2 $0 $2 $5
c $2 $0 $2 $4
c $2 $0 $2 $3
EOF

# 4. Attack med regel
hashcat -m 0 -a 0 exercise2.txt mini_wordlist.txt -r my_rule.rule

# 5. Visa resultat
hashcat -m 0 exercise2.txt --show
```

**✅ Förväntat resultat:** "Password2025" knäckt.

---

### 🔬 Övning 3: Brute Force PIN-kod

**Scenario:** Du har en 4-siffrig PIN-kod hash.

```bash
# 1. Skapa PIN hash (1234)
echo -n "1234" | md5sum > pin_hash.txt

# 2. Hashcat mask attack
hashcat -m 0 -a 3 pin_hash.txt ?d?d?d?d

# Tid: < 1 sekund (endast 10,000 kombinationer)

# 3. Visa resultat
hashcat -m 0 pin_hash.txt --show
```

**✅ Förväntat resultat:** "1234" knäckt nästan omedelbart.

---

### 🔬 Övning 4: Knäcka Unix /etc/shadow

**Scenario:** Du har root-åtkomst och vill testa lösenordsstyrka.

```bash
# 1. Extrahera hashar (ENDAST PÅ DIN EGEN MASKIN!)
sudo unshadow /etc/passwd /etc/shadow > unix_hashes.txt

# 2. Använd John
john --wordlist=/usr/share/wordlists/rockyou.txt unix_hashes.txt

# 3. Visa knäckta
john --show unix_hashes.txt
```

**🔴 VARNING:** Gör ENDAST på din egen Kali-installation, aldrig på produktionssystem!

---

### 🔬 Övning 5: Hybrid Attack (Wordlist + Mask)

**Scenario:** Användare lägger ofta till siffror efter vanliga ord.

```bash
# 1. Skapa test-hash (dragon99)
echo -n "dragon99" | md5sum > exercise5.txt

# 2. Hybrid attack (wordlist + 2 siffror)
hashcat -m 0 -a 6 exercise5.txt /usr/share/wordlists/rockyou.txt ?d?d

# 3. Visa resultat
hashcat -m 0 exercise5.txt --show
```

**✅ Förväntat resultat:** "dragon99" knäckt.

---

### 🔬 Övning 6: Benchmark Din GPU

```bash
# Testa alla hash-typer
hashcat -b

# Testa endast MD5
hashcat -b -m 0

# Testa bcrypt (långsam)
hashcat -b -m 3200

# Jämför resultat:
# MD5:    ~50 GH/s (miljarder per sekund)
# bcrypt: ~50 KH/s (tusentals per sekund)
# Skillnad: ~1,000,000x långsammare!
```

---

### 🔬 Övning 7: Session Management

```bash
# 1. Starta lång attack
hashcat -m 0 -a 0 --session=longcrack hashes.txt rockyou.txt -r best64.rule

# 2. Pausa med Ctrl+C eller 'p'

# 3. Återuppta
hashcat --session=longcrack --restore

# 4. Kontrollera status (tryck 's' under körning)
```

---

## ✅ Självtest {#självtest}

### Frågor

1. **Vad är skillnaden mellan offline och online password cracking?**

2. **Varför är bcrypt säkrare än MD5 för lösenordslagring?**

3. **Vad gör "salt" i en hash-funktion?**

4. **Vilken Hashcat attack-mode används för brute force?**

5. **Hur identifierar du hash-typ innan cracking?**

6. **Vad är fördelen med GPU-acceleration i Hashcat?**

7. **Förklara skillnaden mellan dictionary attack och hybrid attack.**

8. **Vilken John the Ripper mode bör köras FÖRST?**

9. **Hur lång tid tar det ungefär att brute force ett 8-tecken mixed case lösenord med MD5?**

10. **Varför är rainbow tables ineffektiva mot saltade hashar?**

---

### Svar

<details>
<summary>Klicka för att visa svar</summary>

1. **Offline:** Arbetar med hash-filer lokalt, miljontals försök/sekund, ingen risk för upptäckt.
   **Online:** Attackerar levande tjänster, begränsas av nätverk/rate limits, risk för loggning.

2. **bcrypt** är designat för att vara långsamt (tusentals iterationer), vilket gör brute force extremt tidskrävande. MD5 är snabb (~50 GH/s), bcrypt är ~1 miljoner gånger långsammare.

3. **Salt** är slumpmässig data som läggs till lösenordet före hashning. Samma lösenord får olika hashar, vilket förhindrar rainbow table-attacker och gör pre-computation värdelös.

4. **Attack-mode 3** (`-a 3`) används för brute force (mask attack).

5. Använd verktyg som `hashid`, `hash-identifier`, eller John's `--list=formats`. Hash-längd och format ger också ledtrådar (MD5 = 32 hex, SHA-256 = 64 hex).

6. **GPU** kan parallellisera miljontals beräkningar samtidigt. En modern GPU (RTX 3080) är ~100-1000x snabbare än CPU för hash-knäckning.

7. **Dictionary:** Testar ord från lista.
   **Hybrid:** Kombinerar ordlista med brute force (t.ex. wordlist + 2 siffror).

8. **Single crack mode** (`--single`) bör köras först. Den är snabb och testar variationer baserat på användarnamn/metadata.

9. **Flera år** med CPU, **månader till år** med GPU (beroende på hårdvara). 8 tecken mixed case = 52^8 = ~53 biljoner kombinationer.

10. Rainbow tables är förberäknade hash-tabeller. När salt läggs till får varje lösenord unik hash, vilket gör förberäknade tabeller värdelösa (måste räkna om för varje salt).

</details>

---

## 📝 Sammanfattning och Checklista {#sammanfattning}

### Vad Du Lärt Dig

✅ Skillnaden mellan offline och online password attacks
✅ Hash-typer (MD5, SHA, bcrypt) och salting
✅ John the Ripper attack-modes (single, wordlist, incremental, rules)
✅ Hashcat GPU-acceleration och mask attacks
✅ Wordlists (rockyou, fasttrack, custom)
✅ Regelbaserade attacker för effektiv cracking
✅ Praktiska scenarier (Unix shadow, NTLM, ZIP-arkiv)

### Verktygsöversikt

| Verktyg | Primär Användning | Styrka |
|---------|-------------------|--------|
| **John the Ripper** | Allmän password cracking | Mångsidighet, brett hash-stöd |
| **Hashcat** | GPU-accelererad cracking | Extremt snabb, 300+ hash-typer |
| **hashid** | Identifiera hash-typ | Snabb identifiering |
| **crunch** | Generera custom wordlists | Pattern-baserade listor |

### Bästa Praxis

🟢 **Kör alltid John single mode först** (snabbast)
🟢 **Använd Hashcat för stora jobb** (GPU-acceleration)
🟢 **Testa rockyou.txt med best64.rule först** (bästa ROI)
🟢 **Spara sessions** (vid långa attackers)
🟢 **Benchmarka din hårdvara** (förstå hastighet)

### 🔴 Etiska Påminnelser

- ❌ Knäck ALDRIG lösenord utan explicit tillstånd
- ❌ Använd ALDRIG läckta hashar från verkliga system
- ✅ Testa endast i legala lab-miljöer
- ✅ Dokumentera alla aktiviteter vid penetrationstester

### Nästa Steg

➡️ **[Nivå 4C Del 2: Online Password Attacks](niva-4c-password-attacks-pt2.md)**
   - Hydra (network brute forcing)
   - Medusa (parallel login cracker)
   - CeWL (wordlist från webbplatser)

---

## 🎓 Redo för Nästa Nivå?

### Checklista innan Du Fortsätter

- [ ] Jag förstår skillnaden mellan offline och online attacks
- [ ] Jag kan identifiera hash-typer med `hashid`
- [ ] Jag har framgångsrikt knäckt MD5 med John
- [ ] Jag har testat Hashcat med GPU-acceleration
- [ ] Jag förstår hur regelbaserade attacker fungerar
- [ ] Jag kan skapa custom wordlists med crunch
- [ ] Jag har benchmarket min hårdvara
- [ ] Jag förstår de legala och etiska begränsningarna

**✅ Alla checkboxar markerade?** Du är redo för **Nivå 4C Del 2: Online Password Attacks**!

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md) | [➡️ Nivå 4C Del 2: Online Password Attacks](niva-4c-password-attacks-pt2.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**🔐 "The strength of a password is only as good as its weakest character."**
