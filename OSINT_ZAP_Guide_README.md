# 🔍 Pedagogisk Guide: OSINT och OWASP ZAP
## Från Grunderna till Expertkunskap i Säkerhetstestning

> **Din kompletta resa genom Open Source Intelligence och webbapplikationssäkerhet**
>
> 📚 Total läsningstid: 2-3 timmar | 💪 Nivåer: 5 (Nybörjare → Expert) | 🎯 Övningar: 33+ | 🛠️ Praktiska projekt: 2

---

## 🎯 Välkommen!

Hej och välkommen till den mest omfattande svenska guiden om **OSINT** (Open Source Intelligence) och **OWASP ZAP** (Zed Attack Proxy)!

Oavsett om du är nyfiken på cybersäkerhet, vill bli penetrationstestare, bug bounty hunter, eller bara vill förstå hur man hittar och åtgärdar säkerhetsbrister - denna guide är för dig!

### Vad kommer du att lära dig?

I denna guide kommer du att:
- 🕵️ Bemästra OSINT-tekniker för att samla öppen information
- 🛡️ Lära dig säkerhetstesta webbapplikationer med OWASP ZAP
- 🔐 Identifiera vanliga sårbarheter (OWASP Top 10)
- 🤖 Automatisera säkerhetstestning i CI/CD-pipelines
- 🚀 Utforska moderna tekniker som AI-driven OSINT och cloud security
- 💼 Tillämpa din kunskap i verkliga case studies och bug bounty

---

## ⚖️ VIKTIGT: Etik och Legalitet

**🚨 LÄS DETTA FÖRST - EXTREMT VIKTIGT! 🚨**

### Vad är tillåtet?
✅ **ALLTID OKEJ:**
- Testa dina egna system och webbplatser
- Testa med explicit skriftligt tillstånd från ägaren
- Använda officiella test-miljöer (DVWA, WebGoat, Juice Shop)
- Deltaga i lagliga bug bounty-program (HackerOne, Bugcrowd)
- Samla ÖPPEN information som är publikt tillgänglig
- Utbilda dig själv i etiska hacking-kurser

❌ **ALDRIG OKEJ:**
- Testa andras system utan tillstånd (OLAGLIGT!)
- Skrapa eller överbelasta webbplatser (DoS)
- Exploatera sårbarheter du hittar utan tillåtelse
- Sprida eller sälja sårbarhetsdata
- Använda OSINT för stalking eller trakasserier
- Bryta mot dataskyddslagstiftning (GDPR)

### Svensk Lagstiftning
🇸🇪 **Enligt Brottsbalken Kap 4 § 9c:**
- Dataintrång är straffbart med böter eller fängelse upp till 2 år
- "Olovligen bereda sig tillgång till uppgift för automatisk databehandling"
- **Du måste ha tillstånd!**

### Etisk kod
```
Jag lovar att:
1. Alltid få tillstånd innan jag testar system
2. Rapportera sårbarheter ansvarsfull (responsible disclosure)
3. Aldrig skada eller exploatera sårbarheter för egen vinning
4. Respektera privatlivet och dataskydd
5. Följa alla lagar och regler i mitt land
6. Använda mina kunskaper för att göra internet säkrare
```

**Om du använder tekniker från denna guide oetiskt eller olagligt tar du själv ansvaret för konsekvenserna!**

---

## 📊 Guidens Struktur

Guiden är uppdelad i **7 välstrukturerade filer** för optimal läsbarhet:

### 📁 Filstruktur

```
OSINT & ZAP Guide/
│
├── 📄 OSINT_ZAP_Guide_README.md (DU ÄR HÄR!)
│   └── Översikt, etik, navigering
│
├── 🎈 OSINT_ZAP_Guide_Niva_1.md
│   └── Grunderna - För Alla (3 övningar)
│       • OSINT-analogier och koncept
│       • ZAP introduction med enkla exempel
│       • Första stegen
│
├── 🏠 OSINT_ZAP_Guide_Niva_2.md
│   └── Grundläggande Verktyg (4 övningar)
│       • Google Dorking och WHOIS
│       • ZAP installation och första scan
│       • Test-miljöer (DVWA/WebGoat)
│
├── 🔬 OSINT_ZAP_Guide_Niva_3.md
│   └── Tekniska Verktyg och Metoder (5 övningar)
│       • Maltego, theHarvester, Shodan
│       • ZAP Spider, Fuzzing, Authentication
│       • Hitta XSS och andra sårbarheter
│
├── 🎓 OSINT_ZAP_Guide_Niva_4.md
│   └── Avancerade Tekniker (7 övningar + projekt)
│       • Corporate OSINT och DNS enumeration
│       • ZAP API och automation med Python
│       • OWASP Top 10 testing
│       • Projekt: Fullständig säkerhetsaudit
│
├── 🚀 OSINT_ZAP_Guide_Niva_5.md
│   └── Expert-nivå och Modern Teknik (8 övningar + projekt)
│       • AI-driven OSINT och Dark Web
│       • ZAP i CI/CD pipelines (Jenkins, GitLab)
│       • Cloud security och API testing
│       • Case studies: Bellingcat, Bug Bounty
│       • Stort projekt: Security Assessment Pipeline
│
└── 📚 OSINT_ZAP_Guide_Extra.md
    └── FAQ, Ordlista, Resurser, Självutvärdering
        • 10 vanliga frågor med svar
        • 25 termer (svenska/engelska)
        • Böcker, kurser, YouTube, verktyg
        • Checklista för alla nivåer
```

---

## 🗺️ Din Läsväg

### För Absoluta Nybörjare
```
Start här → Nivå 1 → Nivå 2 → Öva! → Nivå 3
```
**Tips:** Ta det lugnt, testa alla övningar, bygg förståelse steg för steg.

### För IT-kunniga som vill lära sig säkerhet
```
Nivå 1 (snabbt) → Nivå 2 → Nivå 3 → Nivå 4 → Bug Bounty!
```
**Tips:** Fokusera på praktiska övningar, bygg ett homelab.

### För Erfarna som vill bli Experts
```
Nivå 3 (refresh) → Nivå 4 → Nivå 5 → Case Studies → Automation
```
**Tips:** Bygg egna verktyg, integrera i CI/CD, bidra till open source.

### För Bug Bounty Hunters
```
Nivå 2-3 (verktyg) → Nivå 4 (OWASP Top 10) → Nivå 5 (automation) → 💰
```
**Tips:** Fokusera på reconnaissance, automation, rapportskrivning.

---

## 🎯 Progression Översikt

```
📊 FULLSTÄNDIG PROGRESSION
│
├─ 🎈 NIVÅ 1: Grunderna (För Alla)
│   ├─ OSINT: Vad är öppen information?
│   ├─ ZAP: Vad är säkerhetstestning?
│   ├─ Analogier: Detektiv, skattjakt, låssmed
│   └─ ✅ 3 övningar (Google-sökning, hitta din data, identifiera risker)
│
├─ 🏠 NIVÅ 2: Grundläggande Verktyg
│   ├─ OSINT: Google Dorking, WHOIS, Wayback Machine
│   ├─ ZAP: Installation, första scan, alerts
│   ├─ Test-miljöer: DVWA, WebGoat setup
│   └─ ✅ 4 övningar (Dorking, WHOIS, ZAP install, första scan)
│
├─ 🔬 NIVÅ 3: Tekniska Verktyg
│   ├─ OSINT: Maltego, theHarvester, Shodan, Recon-ng
│   ├─ ZAP: Spider, Fuzzing, Session management, XSS-hunting
│   ├─ Metodologi: Systematiskt arbetsflöde
│   └─ ✅ 5 övningar (Maltego, theHarvester, Spider, XSS, Intercept)
│
├─ 🎓 NIVÅ 4: Avancerade Tekniker
│   ├─ OSINT: Corporate, DNS enum, Network recon, LinkedIn mining
│   ├─ ZAP: API automation, Custom scripts, OWASP Top 10, SQL injection
│   ├─ Projekt: Fullständig säkerhetsaudit av webbapp
│   └─ ✅ 7 övningar + 1 projekt (Corporate OSINT, Shodan API, ZAP automation, SQLi, WAF bypass)
│
└─ 🚀 NIVÅ 5: Expert och Modern Teknik
    ├─ OSINT: AI/ML, Dark Web, Blockchain, Spiderfoot automation
    ├─ ZAP: CI/CD integration, Docker, API testing, GraphQL
    ├─ Case Studies: Bellingcat, Bug Bounty success stories
    ├─ Stort Projekt: Full Security Assessment Pipeline
    └─ ✅ 8 övningar + 1 stort projekt (AI OSINT, Jenkins+ZAP, Docker, GraphQL, Full pipeline)
```

---

## 🛠️ Vad du behöver

### Mjukvara (Allt är gratis!)
- **OS:** Windows, macOS eller Linux (Kali Linux rekommenderas)
- **OWASP ZAP:** https://www.zaproxy.org/download/
- **Webbläsare:** Firefox eller Chrome
- **Python:** 3.8+ (för automation)
- **Git:** För versionshantering
- **Optional:** Docker, VirtualBox (för test-miljöer)

### Test-miljöer (Lagliga övningsmål!)
- **DVWA** (Damn Vulnerable Web App): http://www.dvwa.co.uk/
- **OWASP WebGoat**: https://owasp.org/www-project-webgoat/
- **OWASP Juice Shop**: https://owasp.org/www-project-juice-shop/
- **HackTheBox**: https://www.hackthebox.com/ (gratis tier)
- **TryHackMe**: https://tryhackme.com/ (gratis tier)

### Hårdvara
- **Minimum:** 8GB RAM, 20GB disk, modern CPU
- **Rekommenderat:** 16GB RAM, 50GB disk (för VMs)
- **Nätverk:** Stabil internetanslutning

---

## 📈 Lärandemål per Nivå

### 🎈 Nivå 1 Mål
- [ ] Förstå vad OSINT är och varför det är viktigt
- [ ] Känna till grundläggande etik och legalitet
- [ ] Kunna förklara säkerhetstestning med enkla ord
- [ ] Veta var öppen information finns

### 🏠 Nivå 2 Mål
- [ ] Använda Google Dorking för att hitta specifik information
- [ ] Utföra WHOIS-lookups och domänundersökningar
- [ ] Installera och konfigurera OWASP ZAP
- [ ] Genomföra din första automatiska säkerhetsskanning
- [ ] Tolka ZAP-alerts och förstå severity-nivåer

### 🔬 Nivå 3 Mål
- [ ] Bemästra flera OSINT-verktyg (Maltego, theHarvester, Shodan)
- [ ] Använda ZAP Spider för att kartlägga webbplatser
- [ ] Hitta och verifiera XSS-sårbarheter
- [ ] Intercepta och modifiera HTTP-requests
- [ ] Följa en systematisk penetrationstestningsmetodik

### 🎓 Nivå 4 Mål
- [ ] Genomföra corporate OSINT och DNS enumeration
- [ ] Automatisera ZAP med Python och API
- [ ] Testa för OWASP Top 10 sårbarheter
- [ ] Hitta och exploatera SQL Injection
- [ ] Skriva professionella sårbarhetsrapporter
- [ ] Genomföra fullständig säkerhetsaudit (projekt)

### 🚀 Nivå 5 Mål
- [ ] Använda AI/ML för automatiserad OSINT
- [ ] Integrera ZAP i CI/CD-pipelines
- [ ] Testa moderna API:er (REST, GraphQL)
- [ ] Bygga egen säkerhetsautomation
- [ ] Förstå Dark Web OSINT (etiskt och säkert)
- [ ] Skapa komplett Security Assessment Pipeline (stort projekt)

---

## 🏆 Certifieringar att Sikta På

Efter att ha genomgått denna guide är du förberedd för:

**Nybörjare/Medel:**
- 🎓 **CompTIA Security+** - Grundläggande säkerhet
- 🎓 **CEH** (Certified Ethical Hacker) - Etisk hacking
- 🎓 **eJPT** (eLearnSecurity Junior Penetration Tester) - Pentesting intro

**Avancerad:**
- 🎓 **OSCP** (Offensive Security Certified Professional) - Hands-on pentesting
- 🎓 **GWAPT** (GIAC Web Application Penetration Tester) - Web app focus
- 🎓 **OSWE** (Offensive Security Web Expert) - Advanced web

**Expert:**
- 🎓 **OSCE** (Offensive Security Certified Expert) - Expert-level
- 🎓 **GXPN** (GIAC Exploit Researcher and Advanced Penetration Tester)

---

## 💰 Bug Bounty och Karriärmöjligheter

### Bug Bounty-plattformar
Med kunskaperna från denna guide kan du delta i:
- **HackerOne**: https://www.hackerone.com/
- **Bugcrowd**: https://www.bugcrowd.com/
- **Intigriti**: https://www.intigriti.com/ (Europeisk)
- **Synack**: https://www.synack.com/ (invite-only)
- **YesWeHack**: https://www.yeswehack.com/

**Genomsnittliga bounties:**
- 💵 Low severity: $50-200
- 💵💵 Medium: $200-1000
- 💵💵💵 High: $1000-5000
- 💵💵💵💵 Critical: $5000-50,000+

### Karriärvägar
- 🔐 **Penetration Tester** - Testa företags säkerhet
- 🕵️ **Security Analyst** - Analysera hot och sårbarheter
- 🛡️ **Application Security Engineer** - Säkra applikationer
- 👨‍💻 **Bug Bounty Hunter** - Frilans säkerhetsforskare
- 🎓 **Security Consultant** - Rådgivning till företag
- 🚀 **DevSecOps Engineer** - Säkerhet i utvecklingsprocessen

**Löneindikationer (Sverige 2024-2025):**
- Junior Pentester: 35,000-45,000 kr/mån
- Medior Security Analyst: 45,000-60,000 kr/mån
- Senior Pentester: 60,000-80,000 kr/mån
- Security Consultant: 70,000-100,000+ kr/mån

---

## 🚀 Kom Igång Nu!

### Steg 1: Förberedelser (15 min)
1. ✅ Läs igenom etik-sektionen igen (viktigt!)
2. ✅ Ladda ner OWASP ZAP
3. ✅ Installera Firefox med FoxyProxy (för ZAP proxy)
4. ✅ Skapa konto på TryHackMe eller HackTheBox

### Steg 2: Välj Din Nivå (5 min)
- **Aldrig testat säkerhet?** → Börja på Nivå 1
- **Har lite IT-kunskap?** → Börja på Nivå 2
- **Utvecklare som vill lära sig?** → Börja på Nivå 2-3
- **Har använt Burp/ZAP förut?** → Hoppa till Nivå 4

### Steg 3: Läs och Öva (ditt tempo!)
- 📖 Läs en nivå
- ✍️ Gör ALLA övningar (inte bara läsa!)
- 🔄 Repetera tills du känner dig bekväm
- ➡️ Gå vidare till nästa nivå

### Steg 4: Bygg Projekt
- 🏗️ Genomför projekt i Nivå 4 och 5
- 📝 Dokumentera dina fynd
- 💼 Lägg till i din portfolio
- 🐛 Börja jaga bug bounties!

---

## 📚 Navigering

### 📖 Börja Läsa:
- **[➡️ Nivå 1: Grunderna](OSINT_ZAP_Guide_Niva_1.md)** - Start här om du är nybörjare!
- **[➡️ Nivå 2: Grundläggande Verktyg](OSINT_ZAP_Guide_Niva_2.md)** - Google Dorking & ZAP installation
- **[➡️ Nivå 3: Tekniska Verktyg](OSINT_ZAP_Guide_Niva_3.md)** - Maltego, Shodan, ZAP Spider
- **[➡️ Nivå 4: Avancerade Tekniker](OSINT_ZAP_Guide_Niva_4.md)** - Corporate OSINT, ZAP automation
- **[➡️ Nivå 5: Expert-nivå](OSINT_ZAP_Guide_Niva_5.md)** - AI, CI/CD, Case studies
- **[➡️ Extra: FAQ, Ordlista & Resurser](OSINT_ZAP_Guide_Extra.md)** - Referensmaterial

---

## 🤝 Community och Support

### Ställ Frågor
- 💬 **Reddit:** r/OSINT, r/websecurity, r/netsec, r/bugbounty
- 💬 **Discord:** Information Security Community servers
- 💬 **Twitter/X:** Följ #OSINT #BugBounty #InfoSec

### Bidra
Hittat ett fel? Har förbättringsförslag?
- Skapa en issue på GitHub
- Pull requests välkomnas!
- Dela din kunskap med andra

---

## 📊 Guide-statistik

| Metric | Värde |
|--------|-------|
| **Total längd** | ~10,000+ ord |
| **Antal filer** | 7 |
| **Nivåer** | 5 |
| **Övningar** | 33+ |
| **Projekt** | 2 stora |
| **Verktyg täckta** | 20+ |
| **Kod-exempel** | 50+ |
| **Diagram** | 15+ ASCII |
| **FAQ** | 10 frågor |
| **Ordlista** | 25 termer |
| **Böcker** | 5 rekommendationer |
| **Kurser** | 5 rekommendationer |
| **YouTube** | 5 kanaler |

---

## ⚡ Snabbnavigering efter Behov

**Vill du:**
- 🔍 **Lära dig hitta information online?** → Nivå 1-3 OSINT
- 🛡️ **Testa webbapplikationer?** → Nivå 2-4 ZAP
- 🐛 **Hitta din första sårbarhet?** → Nivå 3-4
- 💰 **Börja med bug bounty?** → Nivå 4-5
- 🤖 **Automatisera säkerhetstester?** → Nivå 5
- 🎓 **Förbereda för OSCP?** → Alla nivåer + fokus på praktik
- 💼 **Bli penetrationstestare?** → Alla nivåer + certifieringar

---

## 🎉 Lycka Till!

Du står nu inför en spännande resa in i cybersäkerhetens värld. Kom ihåg:

✨ **Övning ger färdighet** - Labba, labba, labba!
✨ **Etik först** - Använd dina kunskaper för gott
✨ **Community** - Hjälp andra och lär tillsammans
✨ **Aldrig sluta lära** - Säkerhet utvecklas konstant
✨ **Ha kul!** - Cybersäkerhet är som ett pussel att lösa

**Låt äventyret börja! 🚀**

---

**Version:** 1.0
**Senast uppdaterad:** November 2024
**Författare:** Pedagogisk Guide-serien
**Licens:** Creative Commons BY-SA 4.0

🔐 **"The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards."** - Gene Spafford

*...men vi kan göra våra system mycket säkrare! Börja din resa här →* **[Nivå 1](OSINT_ZAP_Guide_Niva_1.md)**
