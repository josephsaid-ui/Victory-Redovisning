# ⚖️ Nivå 0B: Legalitet, Etik & Säkerhet

**⏱️ Beräknad tid:** 15-20 minuter
**📚 Svårighetsgrad:** ⭐ Nybörjare
**🎯 Förutsättningar:** Nivå 0A genomförd
**🔴 VIKTIGHET:** KRITISKT - Hoppa INTE över denna sektion!

---

## 📋 Innehåll

1. [Juridisk grund - Sveriges lagar](#️-juridisk-grund---sveriges-lagar)
2. [Internationella lagar](#-internationella-lagar)
3. [Vad som är lagligt vs olagligt](#-vad-som-är-lagligt-vs-olagligt)
4. [När får du använda Kali-verktygen?](#-när-får-du-använda-kali-verktygen)
5. [Konsekvenser av olaglig aktivitet](#-konsekvenser-av-olaglig-aktivitet)
6. [Etiska principer för penetrationstestning](#-etiska-principer-för-penetrationstestning)
7. [Responsible Disclosure](#-responsible-disclosure)
8. [Säkra övningsmiljöer](#-säkra-övningsmiljöer)
9. [Real-world case studies (varningar)](#️-real-world-case-studies-varningar)
10. [Självtest](#-självtest-nivå-0b)

---

## ⚖️ Juridisk grund - Sveriges lagar

### 🇸🇪 Dataintrång (Brottsbalken 4 kap. 9c §)

**Den fullständiga lagtexten:**

> **4 kap. 9 c §**
>
> Den som olovligen genom användning av en teknisk anordning eller på något annat sätt skaffar sig tillgång till en upptagning för automatisk databehandling eller annan sådan överföring eller genom olovlig befattning med en sådan upptagning, ändrar, utplånar, blockerar eller i registret för in en uppgift eller vidtar någon annan sådan åtgärd, döms för dataintrång till böter eller fängelse i högst två år.
>
> Är brottet grovt, döms till fängelse i lägst sex månader och högst sex år. Vid bedömningen av om brottet är grovt ska särskilt beaktas om gärningen har medfört särskilt allvarlig skada eller avsett ett stort antal upptagningar för automatisk databehandling.

### 🔍 Vad betyder detta i praktiken?

| Element | Förklaring | Exempel |
|---------|------------|---------|
| **"olovligen"** | Utan tillstånd från ägaren | Hacka någon annans WiFi utan deras ok |
| **"teknisk anordning"** | Verktyg som datorer, Kali Linux, scripts | Nmap, Metasploit, Aircrack-ng |
| **"skaffar sig tillgång"** | Kommer åt system/data du inte får | Bryta sig in i databas, läsa emails |
| **"ändrar, utplånar, blockerar"** | Modifierar eller förstör data | Radera filer, ändra lösenord, DDoS |
| **"grovt"** | Allvarliga konsekvenser | Stänga ner sjukhussystem, stjäla miljoner poster |

### ⚠️ Viktiga juridiska punkter

```
┌──────────────────────────────────────────────────────────┐
│  🔴 DET SPELAR INGEN ROLL OM DU:                        │
│                                                          │
│  ❌ "Bara testade"                                      │
│  ❌ "Hade goda avsikter"                                │
│  ❌ "Ville hjälpa företaget"                            │
│  ❌ "Inte skadade något"                                │
│  ❌ "Bara kollade"                                      │
│  ❌ "Skulle rapportera sårbarheten"                     │
│                                                          │
│  UTAN TILLSTÅND = DATAINTRÅNG = BROTT                   │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 📊 Straffskala

| Brottstyp | Straff | Typiska fall |
|-----------|--------|--------------|
| **Ringa dataintrång** | Böter | Försök utan skada, första gången, liten omfattning |
| **Dataintrång (standard)** | Böter eller fängelse upp till 2 år | Framgångsrikt intrång, vissa skador |
| **Grovt dataintrång** | Fängelse 6 månader - 6 år | Stor skada, många system, kritisk infrastruktur |

**Tillägg:**
- 💸 **Skadestånd** till offret
- 📝 **Permanent criminal record** (brottsregister)
- 🚫 **Svårt att få jobb inom IT/säkerhet**
- 🌍 **Internationella konsekvenser** om utländska system påverkas

### 🔗 Relaterade brott i svensk lag

| Brott | Lagrum | Relevant när |
|-------|--------|--------------|
| **Bedrägeri** | BrB 9:1 | Stjäla pengar genom hacking |
| **Grov stöld** | BrB 8:1 | Stjäla data av värde |
| **Grovt förtal** | BrB 5:1 | Doxxing, sprida privat info |
| **Olaga hot** | BrB 4:5 | Utpressa med ransomware |
| **Dataintrångssabotage** | BrB 13:4 | DDoS, förstöra system |
| **Olovlig avlyssning** | BrB 4:9a | Packet sniffing på andras trafik |

---

## 🌍 Internationella lagar

Även om du är i Sverige kan du bryta mot internationella lagar!

### 🇺🇸 USA - Computer Fraud and Abuse Act (CFAA)

**Viktigaste lagen för cybersäkerhet globalt**

```
🔴 CFAA gör följande OLAGLIGT:

1. Obehörig åtkomst till datorer
2. Överskrida tillåten åtkomst
3. Datorfusk och bedrägeri
4. Skada på skyddade datorer
5. Trafficking av lösenord
6. Hota med att skada datorer

⚠️ Straffskala: Böter upp till $250,000 + fängelse upp till 20 år
```

**Kända fall:**
- **Aaron Swartz** (2011) - JSTOR-nedladdningar - 35 års fängelse hotades (begick självmord)
- **Marcus Hutchins** (WannaCry-stoppare) - Anklagad för malware-utveckling
- **Lauri Love** - Facing 99 års fängelse för USA-hacking (utlämning nekad)

**🌍 Varför detta påverkar dig i Sverige:**
```
Om du hackar amerikanska system från Sverige:
1. USA kan begära utlämning
2. Svenska myndigheter samarbetar med FBI
3. Du kan dömas i BÅDA länderna
4. Straff kan vara hårdare än i Sverige
```

### 🇪🇺 EU - NIS Directive & GDPR

**NIS (Network and Information Security Directive):**
- Skyddar kritisk infrastruktur
- Energi, transport, hälsa, finans, etc.
- Hårdare straff för angrepp på dessa sektorer

**GDPR (General Data Protection Regulation):**
- Skyddar personuppgifter
- Om du hackar och får tillgång till persondata: **GDPR-överträdelse**
- Böter upp till **20 miljoner EUR eller 4% av global omsättning**

### 🇬🇧 UK - Computer Misuse Act 1990

| Sektion | Brott | Straff |
|---------|-------|--------|
| **Section 1** | Obehörig åtkomst | 2 års fängelse |
| **Section 2** | Obehörig åtkomst med intent | 5 års fängelse |
| **Section 3** | Obehörig modifiering | 10 års fängelse |
| **Section 3A** | Göra/leverera malware | 10 års fängelse |

### 🌏 Andra länder

| Land | Lag | Kommentar |
|------|-----|-----------|
| 🇨🇦 Canada | Criminal Code Section 342.1 | Liknande USA |
| 🇦🇺 Australia | Cybercrime Act 2001 | Upp till 10 års fängelse |
| 🇩🇪 Tyskland | StGB § 202a-c | Data Espionage & Interception |
| 🇫🇷 Frankrike | Article 323-1 Code Pénal | Upp till 7 års fängelse |
| 🇯🇵 Japan | Unauthorized Computer Access Law | 3 års fängelse eller ¥1M böter |

**🔴 VIKTIGT:** Cybercrime är ett GLOBALT brott - du kan åtalas i flera länder samtidigt!

---

## ✅❌ Vad som är lagligt vs olagligt

### Scenario-baserad guide

| Scenario | Lagligt? | Förklaring |
|----------|----------|------------|
| 🏠 **Testa ditt eget hem-WiFi med Aircrack-ng** | ✅ JA | Det är ditt nätverk, du äger det |
| 🏢 **Testa arbetsplatsens WiFi utan att fråga IT** | ❌ NEJ | Du äger inte nätverket - dataintrång |
| 🧪 **Scanna din egen VM (Metasploitable) med Nmap** | ✅ JA | Din egen virtuella maskin i lab |
| 🌐 **Scanna en offentlig webbplats med Nmap** | ⚠️ GRÅ ZON | Tekniskt intrång utan tillstånd - undvik! |
| 📝 **Pentest med skriftligt kontrakt** | ✅ JA | Explicit tillstånd = lagligt |
| 🐛 **Bug bounty inom definierat scope** | ✅ JA | Programmet ger tillstånd |
| 🐛 **Bug bounty UTANFÖR definierat scope** | ❌ NEJ | Även inom bug bounty - håll dig till scope! |
| 👨‍💻 **Hacka din vän's dator "för skojs skull"** | ❌ NEJ | Även med "tillåtelse" - få det SKRIFTLIGT |
| 🏆 **CTF-tävling (Hack The Box, TryHackMe)** | ✅ JA | Plattformarna ger explicit tillstånd |
| 🏫 **Testa skolans nätverk för att "hjälpa dem"** | ❌ NEJ | Ingen asked you - dataintrång |
| 📱 **Testa din partners telefon för att "se om de fuskar"** | ❌ NEJ | Olaglig avlyssning + dataintrång |
| ☕ **Packet sniff på Starbucks WiFi** | ❌ NEJ | Olaglig avlyssning (även om det är öppet WiFi) |
| 🔍 **OSINT på offentlig info (LinkedIn, Google)** | ✅ JA | Offentlig information - inget intrång |
| 🕵️ **Social engineering mot företag utan tillstånd** | ❌ NEJ | Kan vara bedrägeri och intrång |
| 🔧 **Installera Kali Linux** | ✅ JA | Installera verktyg är helt lagligt |
| 💾 **Ladda ner exploits från ExploitDB** | ✅ JA | Ladda ner är OK - användningen avgör |
| 🎓 **Studera malware i isolerad VM** | ✅ JA | För lärande i säker miljö |
| 💻 **Sprida malware** | ❌ NEJ | Grovt brott |
| 🏴‍☠️ **Hacka för att "avslöja korruption"** | ❌ NEJ | Även med "goda avsikter" - olagligt (whistleblowing har andra kanaler) |
| 🎯 **Port scan på 192.168.1.0/24 (ditt hem-nätverk)** | ✅ JA | Ditt eget nätverk |
| 🌍 **Port scan på internet-IP utan tillstånd** | ❌ NEJ | Dataintrång |

### 🔴 "Gråzoner" som du MÅSTE undvika

```
Även om något VERKAR OK, om det är olagligt - GÖR DET INTE!

❌ "Min kompis sa att det var OK att testa hans server"
   → Få det SKRIFTLIGT med hans juridiska namn och datum

❌ "Jag bara scannade, jag gick inte in"
   → Själva scanningen kan vara dataintrång

❌ "Jag tänkte rapportera sårbarheten sen"
   → Du har redan brutit mot lagen VID SJÄLVA INTRÅNGET

❌ "Jag använde VPN så de kan inte spåra mig"
   → VPN skyddar inte från juridiska konsekvenser när du blir fast

❌ "Det var öppet, så jag antog att det var OK"
   → Olåst dörr = inte invitation att gå in
```

---

## 🎯 När får du använda Kali-verktygen?

### ✅ Lagliga användningsområden

#### 1. 🏠 Din egen utrustning

```
✅ DU FÅR TESTA:
├─ Din egen dator
├─ Dina egna virtuella maskiner
├─ Ditt eget hem-nätverk
├─ Din egen router
├─ Dina egna servrar (om du äger/hyr dem)
└─ Enheter du ÄGER

🔴 DU FÅR INTE TESTA:
├─ Arbetsgivarens utrustning (utan deras IT-avd godkännande)
├─ Hyrt utrustning utan hyresvärdens OK
├─ Familjemedlemmars enheter utan skriftligt OK
└─ "Delade" system utan ALLA ägares tillstånd
```

#### 2. 📝 Med explicit skriftligt tillstånd

**Vad ska kontraktet innehålla?**

```
MINIMUM-KRAV FÖR PENTEST-KONTRAKT:

📄 Skriftligt avtal med:
├─ 🏢 Företagsnamn och organisationsnummer
├─ 👤 Kontaktperson med behörighet att ge tillstånd
├─ 📅 Datum för testperiod (start och slut)
├─ 🎯 Scope: Vad FÅR testas
│   ├─ Specifika IP-adresser
│   ├─ Domännamn
│   ├─ Applikationer
│   └─ Nätverkssegment
├─ 🚫 Out of scope: Vad som INTE får testas
│   ├─ Produktion under arbetstid?
│   ├─ Vissa kritiska system?
│   └─ Social engineering?
├─ 🔧 Tillåtna metoder
│   ├─ Vilka verktyg?
│   ├─ DDoS tillåtet? (oftast NEJ)
│   └─ Physical access?
├─ 📞 Emergency contact om något går fel
├─ 📊 Rapporteringskrav
├─ 🤐 NDA (Non-Disclosure Agreement)
└─ ✍️ Signaturer från BÅDA parter

⚠️ SPARA DETTA I MINST 10 ÅR!
```

**Exempel på pentest-kontrakt (förenklad mall):**

```markdown
PENETRATIONSTESTNING - TILLSTÅNDSAVTAL

Mellan:
UPPDRAGSGIVARE: [Företag AB], org.nr [XXXXXX-XXXX]
Representerad av: [Namn, Titel]

Och:
PENTESTER: [Ditt namn/företag]

SCOPE:
✅ Tillåtet:
- IP-range: 192.168.10.0/24
- Domän: testapp.example.com
- Tidsperiod: 2025-12-01 till 2025-12-07
- Verktyg: Nmap, Metasploit, Burp Suite
- Metoder: Network scanning, web app testing

🚫 FÖRBJUDET:
- Produktionsdatabas (192.168.10.50)
- Social engineering mot anställda
- DDoS/stress testing
- Physical intrusion

ANSVAR:
Pentester ansvarar EJ för driftstörningar inom scope.
Uppdragsgivare har informerat IT-avdelningen.

RAPPORTERING:
Leverans senast 2025-12-14

EMERGENCY CONTACT:
[Namn], [Telefon], [Email] (tillgänglig 24/7 under test)

Datum: _____________

Uppdragsgivare: ________________  Pentester: ________________
```

#### 3. 🐛 Bug Bounty Programs

**Vad är bug bounty?**
Företag betalar dig för att hitta sårbarheter i deras system.

**Populära plattformar:**

| Plattform | Företag | Typiska payouts | URL |
|-----------|---------|----------------|-----|
| **HackerOne** | 3000+ företag | $100 - $100,000+ | hackerone.com |
| **Bugcrowd** | 1000+ företag | $50 - $50,000+ | bugcrowd.com |
| **Intigriti** | EU-fokus | €100 - €50,000+ | intigriti.com |
| **YesWeHack** | Europeiska företag | €50 - €25,000+ | yeswehack.com |
| **Synack** | Private programs | $200 - $200,000+ | synack.com (invite-only) |

**🔴 KRITISKA REGLER för Bug Bounty:**

```
📋 BUG BOUNTY ETIQUETTE:

✅ GÖR:
├─ LÄS programreglerna NOGGRANT
├─ Håll dig INOM scope
├─ Rapportera sårbarheter OMEDELBART
├─ Följ disclosure timeline
├─ Kommunicera professionellt
└─ Respektera user privacy

❌ GÖR INTE:
├─ Testa UTANFÖR scope (kan leda till ban + åtal)
├─ Social engineering utan explicit tillåtelse
├─ Läs andras privata data
├─ DDoS eller stress testing
├─ Skapa accounts med fake IDs
├─ Publicera sårbarheten offentligt innan fix
└─ Kräva mer betalt genom hot

⚠️ Varje program har UNIKA regler - läs dem!
```

**Exempel scope från ett bug bounty program:**

```
EXAMPLE BUG BOUNTY SCOPE:

✅ IN SCOPE:
- *.example.com
- api.example.com
- mobile.example.com

🚫 OUT OF SCOPE:
- blog.example.com (Third-party hosted)
- status.example.com (Status page)
- *.test.example.com (Internal testing)

✅ ELIGIBLE VULNERABILITIES:
- SQL Injection
- XSS (Stored/Reflected)
- RCE (Remote Code Execution)
- Authentication bypass
- IDOR (Insecure Direct Object Reference)

🚫 NOT ELIGIBLE:
- Self-XSS
- SPF/DKIM/DMARC issues
- Clickjacking on non-sensitive pages
- CSV injection
- Missing security headers (without PoC)

⚠️ TESTING RULES:
- Do NOT test in production during business hours
- Maximum 10 requests/second
- Do NOT create more than 5 test accounts
- Do NOT download >1MB of data
- STOP if you find user data - report immediately
```

#### 4. 🏆 CTF Platforms & Training Labs

**100% lagliga övningsplatser:**

| Platform | Typ | Kostnad | Rekommendation |
|----------|-----|---------|----------------|
| **Hack The Box** | Realistic labs | Free + VIP ($14/mån) | ⭐⭐⭐⭐⭐ OSCP prep |
| **TryHackMe** | Guided learning paths | Free + Premium ($11/mån) | ⭐⭐⭐⭐⭐ Nybörjarvänlig |
| **PentesterLab** | Web app focus | $20/mån | ⭐⭐⭐⭐ Web pentesting |
| **VulnHub** | Downloadable VMs | Gratis | ⭐⭐⭐⭐ Lokala labs |
| **OverTheWire** | Linux/programming | Gratis | ⭐⭐⭐⭐ Basics |
| **PicoCTF** | CTF challenges | Gratis | ⭐⭐⭐ Bra för nybörjare |
| **Root-Me** | Challenges & CTF | Gratis | ⭐⭐⭐ Fransk plattform |
| **HackThisSite** | Beginner friendly | Gratis | ⭐⭐⭐ Mycket basic |

---

## ⚠️ Konsekvenser av olaglig aktivitet

### 📊 Real-world straffskala (baserat på riktiga fall)

| Brott | Ålder | Straff | Land | År |
|-------|-------|--------|------|-----|
| Hacka skolans system för att ändra betyg | 16 | Böter + ungdomsvård | Sverige | 2019 |
| DDoS mot företag för pengar | 19 | 14 månaders fängelse | Sverige | 2020 |
| Stöld av kreditkortsinformation (50,000 kort) | 24 | 3 års fängelse + €400k böter | Tyskland | 2021 |
| Hack av ex-partners email | 28 | 6 månaders fängelse + kontaktförbud | Sverige | 2022 |
| Sälj av exploits till kriminella | 22 | 4 års fängelse | USA | 2020 |
| Ransomware attack mot sjukhus | 32 | 12 års fängelse | USA | 2021 |
| Hacking av celebriteters iCloud | 35 | 9 månaders fängelse | USA | 2016 |
| Sony PlayStation Network breach | 23 | 3 års fängelse | UK | 2013 |

### 💸 Ekonomiska konsekvenser

```
TOTAL KOSTNAD AV ETT DATAINTRÅNG:

⚖️ Juridiska kostnader:
├─ Advokat: 50,000 - 500,000 kr
├─ Rättegångskostnader: 100,000 - 1,000,000 kr
└─ Böter: 10,000 - 1,000,000+ kr

💰 Skadestånd till offer:
├─ Företag: 500,000 - 50,000,000+ kr
├─ Privatpersoner: 50,000 - 500,000 kr per person
└─ Punitive damages (USA): 10x+ faktiska skador

🚫 Framtida inkomstbortfall:
├─ Svårt få IT-jobb: -30,000 kr/mån livstid
├─ Förstörd karriär: -15,000,000 kr över 40 år
└─ Kan inte starta företag: Omöjligt få investerare

📉 Andra kostnader:
├─ Cannot travel to certain countries
├─ Cannot get security clearance
├─ Stressed relationships
└─ Mental health impact

💥 TOTAL: Potentiellt 15-50+ miljoner kr + fängelse
```

### 👨‍👩‍👧‍👦 Personliga konsekvenser

```
BEYOND PENGAR OCH FÄNGELSE:

❌ Criminal Record (brottsregister):
├─ Stannar på record i 10+ år (Sverige)
├─ Permanent i vissa länder (USA)
├─ Syns vid jobbansökningar
├─ Påverkar resande (USA-visum förnekas ofta)
└─ Kan påverka vårdnad av barn

❌ Karriär:
├─ Svårt få jobb inom IT/säkerhet
├─ Cannot get security clearance
├─ Förstört professionellt rykte
└─ Kollegor och nätverk vänder ryggen

❌ Personligt:
├─ Familj och vänner påverkas
├─ Stress och mental hälsa
├─ Relationships förstörs (trust issues)
└─ Social stigma

❌ Utbildning:
├─ Kan bli avskedad från universitet
├─ Svårt få studieplatser
└─ Certifieringar kan återkallas
```

---

## 🧭 Etiska principer för penetrationstestning

### The Hacker's Code of Ethics (ACM Code)

```
🎯 ETHICAL HACKER'S PLEDGE:

1. 🔐 RESPEKT FÖR PRIVACY
   "Jag respekterar individers och organisationers privacy"

2. 📝 AUTHORIZATION FIRST
   "Jag testar ENDAST system där jag har explicit tillstånd"

3. 💎 INTEGRITY
   "Jag rapporterar sanningsenligt och ändrar inte data onödigt"

4. 🤝 RESPONSIBLE DISCLOSURE
   "Jag rapporterar sårbarheter ansvarsfullt, inte offentligt"

5. 🎓 CONTINUOUS LEARNING
   "Jag håller min kunskap uppdaterad för bättre säkerhet"

6. 🛡️ DO NO HARM
   "Jag minimerar skada och störningar under tester"

7. ⚖️ LEGAL COMPLIANCE
   "Jag följer alla tillämpliga lagar och regler"

8. 🤫 CONFIDENTIALITY
   "Jag håller klientdata konfidentiell"

9. 👥 RESPECT THE COMMUNITY
   "Jag bidrar positivt till säkerhetscommunityn"

10. 🎯 DEFENSE MINDSET
    "Mitt mål är att STÄRKA säkerhet, inte bryta den"
```

### Pentest Methodology - Etiska steg

```
ETHICAL PENTEST WORKFLOW:

📋 1. PRE-ENGAGEMENT
├─ Signera kontrakt med tydligt scope
├─ NDA (Non-Disclosure Agreement)
├─ Rules of Engagement (ROE)
├─ Emergency contacts
└─ Backup plan om något går fel

🎯 2. INFORMATION GATHERING
├─ Håll dig inom scope
├─ Dokumentera allt du gör
├─ Respektera user privacy
└─ OSINT endast på offentlig info

🔍 3. VULNERABILITY ASSESSMENT
├─ Använd non-destructive methods först
├─ Få godkännande innan du kör exploits
├─ Testa inte under peak business hours (om inte tillåtet)
└─ Stop immediately if you find production user data

💥 4. EXPLOITATION
├─ Minimal impact - testa bara tillräckligt för PoC
├─ BACKUP data innan destructive tests
├─ Dokumentera varje steg
└─ Informera client omedelbart vid kritiska fynd

🎣 5. POST-EXPLOITATION
├─ Gå INTE längre än nödvändigt för att bevisa sårbarhet
├─ Ta INTE med dig data (förutom minimal PoC)
├─ Städa upp efter dig (ta bort shells, accounts, etc.)
└─ Dokumentera allt för rapporten

📊 6. REPORTING
├─ Professional, detaljerad rapport
├─ Ärlig bedömning av risk
├─ Konkreta, actionable rekommendationer
├─ Executive summary + tekniska detaljer
└─ Håll rapporten konfidentiell

🔄 7. POST-ENGAGEMENT
├─ Hjälp med remediation om requested
├─ Re-test efter fixes
├─ Arkivera allt säkert
└─ Ta bort ALL data från dina system efter projekt
```

---

## 🚨 Responsible Disclosure

### Vad är Responsible Disclosure?

**Definition:** Processen att rapportera sårbarheter till organisationer på ett ansvarsfullt sätt som ger dem tid att fixa problemet innan det blir offentligt.

### 🔁 Responsible Disclosure Timeline

```
STANDARD 90-DAGARS DISCLOSURE:

Dag 0️⃣: Hitta sårbarhet
├─ Dokumentera noggrant
├─ Skapa Proof of Concept (PoC)
└─ Anonymisera känslig data

Dag 1️⃣: Initial contact
├─ Hitta rätt kontaktpunkt (security@företag.com)
├─ Skicka initial rapport (utan full PoC först)
├─ Ge dina kontaktuppgifter
└─ Sätt deadline (90 dagar standard)

Dag 7️⃣: Follow-up (om inget svar)
├─ Skicka påminnelse
├─ Försök alternativa kanaler
└─ Dokumentera alla försök

Dag 14: Eskalera (om fortfarande inget svar)
├─ Kontakta senior management
├─ LinkedIn/Twitter till CISO
└─ Överväg offentlig disclosure om kritiskt

Dag 30: Företaget bekräftar & arbetar på fix

Dag 60: Företaget begär extension (OK att ge +30 dagar)

Dag 90: Deadline - publikation
├─ Företaget har fixat: Publish full disclosure med credit
├─ Företaget har INTE fixat: Din rätt att publicera (varna först)
└─ Kritisk sårbarhet inte fixad: Överväg noga - user safety först

EFTER DISCLOSURE:
├─ Ge företaget credit för samarbete (om de gjorde)
├─ Dela learnings med community
└─ Uppdatera CVE om applicable
```

### 📧 Email-template för disclosure

```
Subject: Security Vulnerability Report - [Kort beskrivning]

Hej [Security Team / Företag],

Jag har identifierat en säkerhetssårbarhet i [system/applikation]
som jag vill rapportera ansvarsfullt.

SAMMANFATTNING:
- Sårbarhet: [t.ex. SQL Injection]
- Severity: [Critical/High/Medium/Low]
- Påverkan: [t.ex. möjligt att läsa databas]
- Upptäckt: [Datum]

Jag har INTE:
- Exploaterat sårbarheten mer än nödvändigt för att verifiera den
- Åtkomst någon user data
- Delat informationen med andra
- Offentliggjort sårbarheten

Jag är villig att:
- Ge er full teknisk disclosure
- Svara på frågor
- Ge er rimlig tid att fixa (90 dagar standard)

Jag förväntar:
- Bekräftelse inom 7 dagar
- Regelbundna updates
- Koordinerad disclosure efter fix
- [Bounty om applicable]

Vänligen bekräfta mottagande så skickar jag tekniska detaljer.

Kontaktuppgifter:
[Namn]
[Email]
[PGP key om möjligt]

Bästa hälsningar,
[Namn]
```

### ⚖️ Full Disclosure vs Responsible Disclosure

| Aspect | Responsible Disclosure | Full Disclosure | Ditt val |
|--------|----------------------|----------------|----------|
| **Metod** | Rapportera privat först | Publicera omedelbart | ✅ Responsible |
| **Benefit** | Ger tid att fixa | Tvingar snabb fix | ✅ Responsible |
| **Risk** | Kan take longer | Users i fara | ✅ Responsible |
| **Etik** | Ansvarsfull | Kontroversiell | ✅ Responsible |
| **Karriär** | Professionell | Kan skada rykte | ✅ Responsible |
| **Lagligt** | Säkrare juridiskt | Risk för åtal | ✅ Responsible |

---

## 🧪 Säkra övningsmiljöer

### 🏠 Lokala Lab-miljöer (100% säkra)

#### Vulnerable VMs

| VM | Svårighetsgrad | Vad du lär dig | Download |
|----|----------------|----------------|----------|
| **Metasploitable 2** | ⭐ Nybörjare | Grunder i exploitation | sourceforge.net/projects/metasploitable |
| **Metasploitable 3** | ⭐⭐ Intermediate | Modernare sårbarheter | github.com/rapid7/metasploitable3 |
| **DVWA** | ⭐ Nybörjare | Web app hacking | github.com/digininja/DVWA |
| **bWAPP** | ⭐⭐ Intermediate | 100+ web vulns | sourceforge.net/projects/bwapp |
| **WebGoat** | ⭐ Nybörjare | OWASP Top 10 | github.com/WebGoat/WebGoat |
| **Mutillidae** | ⭐⭐ Intermediate | OWASP web app | github.com/webpwnized/mutillidae |
| **Damn Vulnerable Web Services** | ⭐⭐⭐ Advanced | API security | github.com/snoopysecurity/dvws |
| **HackSys Extreme Vulnerable Driver** | ⭐⭐⭐⭐ Expert | Windows kernel exploits | github.com/hacksysteam/HackSysExtremeVulnerableDriver |

#### 🔧 Setup Guide för Metasploitable 2 (quick start)

```bash
# 1. Ladda ner Metasploitable 2
wget https://sourceforge.net/projects/metasploitable/files/Metasploitable2/metasploitable-linux-2.0.0.zip

# 2. Unzip
unzip metasploitable-linux-2.0.0.zip

# 3. Öppna i VirtualBox
# - Skapa ny VM
# - Typ: Linux, Ubuntu (32-bit)
# - Använd befintlig disk: Metasploitable.vmdk
# - Starta VM

# 4. Login credentials:
# Username: msfadmin
# Password: msfadmin

# 5. Hitta IP-adressen
ifconfig

# 6. Från Kali - scanna Metasploitable
nmap -sV [METASPLOITABLE-IP]

# 🎉 Nu kan du börja öva etiskt!
```

### 🌐 Online Lab Platforms

#### Hack The Box (HTB)

```
🎯 HACK THE BOX

Typ: Realistic pentesting labs
Kostnad: Free tier + VIP ($14/mån)
Machines: 100+ aktiva + 300+ retired
Difficulty: Easy → Insane

✅ PRO:
├─ Extremely realistic
├─ Industry recognized
├─ Great community (forum, Discord)
├─ Machines retire → writeups available
└─ Excellent OSCP preparation

⚠️ CON:
├─ Steep learning curve för nybörjare
├─ Free tier: Endast aktiva machines (kan vara hackade redan)
└─ Sometimes competitive (machines get "pwned" fast)

🎓 Rekommendation:
Börja med "Starting Point" free machines, sedan VIP när du vill retired machines
```

#### TryHackMe (THM)

```
🎮 TRYHACKME

Typ: Guided learning paths + challenges
Kostnad: Free + Premium ($11/mån)
Rooms: 600+ guided labs
Difficulty: Very Beginner → Expert

✅ PRO:
├─ Mycket nybörjarvänlig
├─ Guided learning paths (clear progression)
├─ Browser-based Kali (ingen egen VM behövs)
├─ Hints och write-ups built in
└─ King of the Hill (competitive)

⚠️ CON:
├─ Mindre "realistic" än HTB (mer guided)
└─ Premium för fullständiga paths

🎓 Rekommendation:
🌟 PERFEKT för nybörjare! Börja här innan HTB.
```

#### 📊 Jämförelse HTB vs THM

| Aspekt | Hack The Box | TryHackMe |
|--------|-------------|-----------|
| **Nybörjarvänlighet** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Realism** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **OSCP prep** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Community** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Kostnad (value)** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Content mängd** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**🎯 Optimal strategi:**
```
ÅR 1: TryHackMe (lär dig basics)
ÅR 2: Hack The Box (realistic practice)
ÅR 3: Bug Bounty + advanced HTB
```

---

## 🚨 Real-world Case Studies (varningar)

### Case 1: The Good Intentions Gone Wrong

**📖 Story: Swedish Student vs School Network (2019)**

```
Situation:
17-årig IT-intresserad elev på gymnasiet ville "hjälpa"
skolan förbättra sin säkerhet.

Vad han gjorde:
✓ Port-scannade skolans nätverk
✓ Hittade sårbarhet i WiFi
✓ Loggade in på lärares konton
✓ Visade sårbarhet för IT-ansvarig

Avsikt:
"Jag ville bara hjälpa skolan!"

Resultat:
❌ Polisanmälan för dataintrång
❌ Avstängd från skolan
❌ Böter 15,000 kr
❌ Upptagning i brottsregister
❌ Svårt få IT-praktikplats

🔴 VAD GICK FEL?
Han fick ALDRIG tillstånd - även "goda avsikter" är olagligt!

✅ VAD BORDE HAN HA GJORT?
1. Kontaktat IT-ansvarig FÖRST
2. Begärt skriftligt tillstånd
3. Testat under övervakning
4. Dokumenterat enligt professionell standard
```

### Case 2: The Ex-Boyfriend Stalker

**📖 Story: Email Hacking for "Proof" (2022)**

```
Situation:
28-årig man misstänkte att ex-flickvännen fuskat.
Ville "bara veta sanningen".

Vad han gjorde:
✓ Brute-force attack på hennes Gmail
✓ Läste privata emails
✓ Loggade hennes Facebook-meddelanden
✓ Installerade keylogger på hennes laptop (fysisk access)

Avsikt:
"Jag hade rätt att veta!"

Resultat:
❌ 6 månaders fängelse
❌ Kontaktförbud
❌ Skadestånd 150,000 kr
❌ Förstörd IT-karriär (arbetade som systemadministratör)
❌ Lost custody rights (de hade barn)

🔴 LÄRDOMAR:
├─ "Personliga motiv" är INTE juridiskt försvar
├─ Även om du känner personen = fortfarande olagligt
├─ Keyloggers/spyware = grovt brott
└─ Privacy violations har STORA konsekvenser
```

### Case 3: The Bug Bounty Overstepper

**📖 Story: Out of Scope Testing (2021)**

```
Situation:
24-årig bug bounty hunter testade företags web app.

Vad han gjorde:
✓ Hittade SQL injection inom scope ✅
✓ Exploaterade sårbarhet ✅
✓ Testade också företagets EMAIL server (OUT OF SCOPE) ❌
✓ Läste CEO's emails för att "bevisa impact" ❌
✓ Downloadade databas backup (2GB user data) ❌

Avsikt:
"Jag ville visa hur allvarligt det var"

Resultat:
❌ Kickad från bug bounty platform (banned for life)
❌ Åtalad för dataintrång
❌ Böter €50,000
❌ Blacklisted från industry

🔴 LÄRDOMAR:
├─ Även inom bug bounty: HÅLL DIG TILL SCOPE!
├─ "För att bevisa impact" är INTE försvar för out-of-scope
├─ Ladda ALDRIG ner verklig user data
├─ Email servers är nästan alltid out of scope
└─ En incident kan förstöra hela din karriär
```

### Case 4: The VPN False Security

**📖 Story: "De kan inte spåra mig" (2020)**

```
Situation:
22-årig "gray hat" tänkte VPN gjorde honom osynlig.

Vad han gjorde:
✓ Använde VPN för att "skydda sig"
✓ Hackade e-handelsidor för kreditkortsuppgifter
✓ Sålde data på dark web
✓ Trodde VPN gjorde honom ospårbar

Vad som hände:
├─ VPN-provider samarbetade med polis (logs överlämnades)
├─ Bitcoin-transaktioner spårades
├─ Cross-referenced med forum posts (metadata)
└─ Gripen inom 6 månader

Resultat:
❌ 4 års fängelse
❌ €400,000 i böter och skadestånd
❌ All utrustning beslagtagen
❌ Permanent criminal record

🔴 LÄRDOMAR:
├─ VPN är INTE anonymitet-garanti
├─ Metadata läcker: timezone, writing style, bitcoin, etc.
├─ Många VPNs loggar och samarbetar med law enforcement
├─ Även Tor kan komprometteras med tillräckligt resurser
└─ Bästa skyddet: GÖR INGENTING OLAGLIGT!
```

### Case 5: The Accidental DDoS

**📖 Story: Port Scan Gone Wrong (2023)**

```
Situation:
19-årig student övade Nmap-scanning.

Vad han gjorde:
✓ Körde aggressiv Nmap scan (-T5 --max-rate 10000)
✓ Mot ett litet företags web server
✓ Tänkte "det är bara scanning, inte intrång"

Vad som hände:
├─ Hans scanning överbelastade servern
├─ Företagets webb gick ner i 3 timmar
├─ Lost sales: ~500,000 kr
├─ Företaget spårade hans IP (han använde ingen VPN)
└─ Polisanmälan

Resultat:
❌ Åtalad för sabotage + dataintrång
❌ Skadestånd 500,000 kr (livets skuld)
❌ Böter 25,000 kr
❌ Kunde inte betala → betalningsanmärkning

🔴 LÄRDOMAR:
├─ "Bara scanning" kan också vara olagligt
├─ Aggressiv scanning kan ta ner system (oavsiktligt DDoS)
├─ Använd ALLTID slower scans (-T2 eller -T3) om du MÅSTE scanna
├─ Scanna ENDAST system du äger eller har tillstånd för
└─ Småföretags servers kan vara känsliga för aggressive scans
```

---

## 🧪 Självtest - Nivå 0B

### Scenario-baserade frågor

Markera om varje scenario är **LAGLIGT** (✅) eller **OLAGLIGT** (❌):

1. **Du installerar Kali Linux på din laptop**
   - [ ] Lagligt
   - [ ] Olagligt

2. **Du scannar ditt eget hem-WiFi med Aircrack-ng**
   - [ ] Lagligt
   - [ ] Olagligt

3. **Du scannar grannens WiFi för att "se om den är säker"**
   - [ ] Lagligt
   - [ ] Olagligt

4. **Ett företag anlitar dig med kontrakt för pentest. Du testar inom scope.**
   - [ ] Lagligt
   - [ ] Olagligt

5. **Under samma pentest upptäcker du en sårbarhet i system X som är OUT OF SCOPE. Du testar den ändå "för att hjälpa"**
   - [ ] Lagligt
   - [ ] Olagligt

6. **Du hittar en SQL injection på ett företag. Du rapporterar det via deras security@email.**
   - [ ] Lagligt (om du bara testade minimalt för PoC)
   - [ ] Olagligt

7. **Du hittar samma SQL injection och laddar ner deras hela databas för att "bevisa allvarlighetsgraden"**
   - [ ] Lagligt
   - [ ] Olagligt

8. **Du testar på Metasploitable VM på din egen dator**
   - [ ] Lagligt
   - [ ] Olagligt

9. **Du hackar din kompis dator för "skojs skull" och han säger "det är OK"**
   - [ ] Lagligt (muntligt OK räcker)
   - [ ] Olagligt (behöver skriftligt)

10. **Du deltar i Hack The Box CTF**
    - [ ] Lagligt
    - [ ] Olagligt

### Kunskapsfrågor

11. **Vad är straffet för standard dataintrång i Sverige?**
    - A) Varning
    - B) Böter eller fängelse upp till 6 månader
    - C) Böter eller fängelse upp till 2 år
    - D) Alltid fängelse 5 år

12. **Vad står CIA för i säkerhetssammanhang?**
    - A) Criminal Intelligence Agency
    - B) Confidentiality, Integrity, Availability
    - C) Computer Internet Access
    - D) Cyber Investigation Authority

13. **Hur lång är standard "Responsible Disclosure" timeline?**
    - A) 30 dagar
    - B) 60 dagar
    - C) 90 dagar
    - D) 180 dagar

14. **Vad är det FÖRSTA du måste göra om du hittar en sårbarhet under ett bug bounty program?**
    - A) Publicera på Twitter
    - B) Exploatera den maximalt för att förstå impact
    - C) Rapportera till företaget enligt deras process
    - D) Berätta för alla dina vänner

15. **Vilket är det STÖRSTA misstaget i "The Good Intentions Gone Wrong" case study?**
    - A) Använde fel verktyg
    - B) Testade UTAN tillstånd trots goda avsikter
    - C) Rapporterade sårbarheten
    - D) Var för ung

### Svar

<details>
<summary>Klicka för att visa svar (försök själv först!)</summary>

**Scenario-frågor:**

1. ✅ **Lagligt** - Installera Kali är helt OK
2. ✅ **Lagligt** - Ditt eget nätverk, din utrustning
3. ❌ **OLAGLIGT** - Inte ditt nätverk = dataintrång
4. ✅ **Lagligt** - Med kontrakt och inom scope = OK
5. ❌ **OLAGLIGT** - Out of scope = dataintrång även under pentest
6. ✅ **Lagligt** - Minimal testing + rapportering = responsible disclosure
7. ❌ **OLAGLIGT** - Ladda ner produktionsdata = brott
8. ✅ **Lagligt** - Din egen VM = OK
9. ❌ **OLAGLIGT** - Behöver skriftligt tillstånd för säkerhet
10. ✅ **Lagligt** - HTB ger explicit tillstånd

**Kunskapsfrågor:**

11. **C** - Böter eller fängelse upp till 2 år (BrB 4:9c)
12. **B** - Confidentiality, Integrity, Availability
13. **C** - 90 dagar (standard industry practice)
14. **C** - Rapportera enligt företagets process
15. **B** - Testade utan tillstånd trots goda avsikter

**Scoring:**
- 14-15 rätt: 🏆 Perfekt! Du förstår juridiken och etiken
- 12-13 rätt: ✅ Mycket bra! Läs igenom de du missade
- 10-11 rätt: 👍 OK förståelse - gå igenom nivån igen
- <10 rätt: 🔄 Läs igenom hela Nivå 0B igen - detta är kritiskt!

</details>

---

## ✅ Checklista - Klar för Nivå 1?

Säkerställ att du:

- [ ] Förstår Sveriges dataintrångslag (BrB 4:9c)
- [ ] Vet skillnaden mellan laglig och olaglig användning av Kali-verktyg
- [ ] Känner till konsekvenserna av olaglig hacking
- [ ] Förstår hur Responsible Disclosure fungerar
- [ ] Vet var du får öva säkert (Metasploitable, HTB, THM, etc.)
- [ ] Har läst och förstått alla 5 case studies
- [ ] Har klarat självtestet med minst 12/15 rätt
- [ ] Lovar att ENDAST testa system du äger eller har skriftligt tillstånd för

**🔴 PLEDGE:**

> Jag, [ditt namn], lovar att:
> - ALLTID följa lagen
> - ALDRIG testa system utan explicit tillstånd
> - ENDAST öva i säkra lab-miljöer
> - Rapportera sårbarheter ansvarsfullt
> - Använda min kunskap för att HJÄLPA, inte skada
>
> Datum: ___________  Signatur: ___________

---

## 🎯 Nästa steg

**Grattis!** 🎉 Du har nu den viktigaste grundkunskapen: **juridik och etik**.

Denna kunskap ska guida ALLT du gör i resten av guiden.

**👉 Nästa: [Nivå 1 - Installation & Setup](./niva-1-installation.md)**

Nu ska vi installera Kali Linux och sätta upp din lab-miljö!

---

**[⬅️ Föregående: Nivå 0A - Förkunskaper](./niva-0a-forkunskaper.md)** | **[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)** | **[➡️ Nästa: Nivå 1 - Installation](./niva-1-installation.md)**

---

**📌 Kom ihåg:**

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  "With great power comes great responsibility"            ║
║                                                            ║
║  "Med stor makt kommer stort ansvar"                       ║
║                                                            ║
║  Använd din kunskap etiskt och lagligt - ALLTID!          ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```
