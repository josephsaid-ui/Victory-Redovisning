# 🐉 Kali Linux - Komplett Guide 2025
## Från Total Nybörjare till Cybersäkerhetsproffs

**Version:** 2.0
**Senast uppdaterad:** November 2025
**Målgrupp:** Windows 11-användare som vill lära sig Kali Linux och etisk hacking
**Svårighetsgrad:** Nybörjare → Avancerad (progressiv inlärning)
**Beräknad genomförande-tid:** 40-60 timmar

---

## 📚 Innehållsförteckning

### 🚨 [LÄSA FÖRST - JURIDISK DISCLAIMER](#-juridisk-disclaimer-och-etisk-användning)

### 🎮 [Välj Din Inlärningsväg](#-välj-din-inlärningsväg)

### 📖 Nivåer

#### **[Nivå 0: Förkunskaper & Legalitet](./guides/niva-0-forkunskaper.md)** (10 min)
- Vad är Kali Linux?
- Vem är guiden för?
- Cybersäkerhet - Etik och juridik
- White Hat vs Gray Hat vs Black Hat
- Certifieringar och karriärvägar - översikt
- Krav och förväntningar

#### **[Nivå 1: Installation & Setup](./guides/niva-1-installation.md)** (30-60 min)
- Systemkrav
- Jämförelse: VirtualBox vs WSL2 vs Dual Boot vs Live USB
- **Installation:**
  - VirtualBox (Rekommenderad för nybörjare)
  - WSL2 (För Windows-integration)
  - Dual Boot (För avancerade)
  - Live USB (För portabilitet)
- Initial konfiguration
- Systemuppdatering och pakethantering
- Vanliga problem och lösningar

#### **[Nivå 2: Linux-grunderna via Kali](./guides/niva-2-linux-grunder.md)** (45-90 min)
- Terminal/Shell basics (bash)
- Filsystem och navigation
- Grundläggande kommandon
- Användarhantering och permissions
- Texteditors (nano, vim, gedit)
- Pakethantering (apt, dpkg)
- Processer och services
- Praktiska övningar

#### **[Nivå 3: Reconnaissance - Information Gathering](./guides/niva-3-reconnaissance.md)** (2-3 timmar)
- **Nmap** - Network Mapping & Port Scanning (DJUPGÅENDE)
- **Netdiscover** - Network Discovery
- **Wireshark** - Packet Analysis
- **theHarvester** - OSINT & Email Harvesting
- **Maltego** - Data Mining & Link Analysis
- **Recon-ng** - Web Reconnaissance Framework
- **Shodan** - Internet-Wide Scanning
- Praktiska lab-övningar

#### **[Nivå 4A: Vulnerability Assessment](./guides/niva-4a-vulnerability.md)** (1.5 timmar)
- **OpenVAS** - Vulnerability Scanner
- **Nikto** - Web Server Scanner
- **WPScan** - WordPress Security Scanner
- **SQLmap** - SQL Injection Testing

#### **[Nivå 4B: Exploitation](./guides/niva-4b-exploitation.md)** (2-3 timmar)
- **Metasploit Framework** (DJUPGÅENDE)
- **Burp Suite** - Web Application Testing
- **BeEF** - Browser Exploitation Framework
- **SET** - Social Engineering Toolkit

#### **[Nivå 4C: Password Attacks](./guides/niva-4c-password-attacks.md)** (1.5 timmar)
- **John the Ripper** - Password Cracking
- **Hashcat** - Advanced Hash Cracking
- **Hydra** - Network Login Cracker
- **Medusa** - Parallel Login Brute-Forcer
- **CeWL** - Custom Wordlist Generator

#### **[Nivå 4D: Wireless Attacks](./guides/niva-4d-wireless.md)** (1.5 timmar)
- **Aircrack-ng Suite** - WiFi Security Testing
- **Wifite** - Automated Wireless Auditor
- **Reaver** - WPS Attack Tool

#### **[Nivå 5: Advanced Topics](./guides/niva-5-advanced.md)** (3-4 timmar)
- Post-Exploitation (Meterpreter, Persistence)
- Maintaining Access (Etiskt!)
- Anonymity & Privacy (VPN, Tor, ProxyChains)
- Custom Scripts & Automation
- Report Writing & Documentation
- Building Your Own Pentest Lab
- CTF (Capture The Flag) Introduction
- Bug Bounty Programs
- Real-World Pentest Workflow

### 📋 Resurser

#### **[Cheat Sheets](./resources/cheat-sheets.md)**
- Linux Command Cheat Sheet
- Nmap Cheat Sheet
- Metasploit Cheat Sheet
- Burp Suite Cheat Sheet
- Reverse Shell Cheat Sheet

#### **[Lab Environment Setup](./resources/lab-setup.md)**
- Metasploitable 2/3 Installation
- DVWA Setup
- VulnHub VMs
- Hack The Box Setup
- TryHackMe Recommendations

#### **[Career Roadmap](./resources/career-roadmap.md)**
- Certifieringsväg (Security+ → CEH → OSCP → OSEP)
- Karriärvägar (Pentester, Red Team, Bug Bounty)
- Rekommenderade böcker
- Communities & Conferences
- Continuous Learning Resources

#### **[Troubleshooting & FAQ](./resources/troubleshooting.md)**
- Installations-problem
- Nätverksproblem
- Verktyg som inte fungerar
- Vanliga fel och lösningar

#### **[Appendix & Glossary](./resources/appendix.md)**
- Ordlista (tekniska termer)
- Användbara länkar
- Referensmaterial
- Uppdateringshistorik

---

## ⚖️ JURIDISK DISCLAIMER OCH ETISK ANVÄNDNING

> **🔴 LÄSA DETTA FÖRST INNAN DU FORTSÄTTER!**
>
> Denna guide är ett utbildningsmaterial för cybersäkerhet och etisk hacking. All information presenteras i pedagogiskt syfte och för laglig användning.

### ✅ Denna guide är avsedd för:

| Tillåten Användning | Beskrivning |
|---------------------|-------------|
| 🎓 **Utbildning** | Lärande i akademiska sammanhang, självstudier, certifieringsprep |
| 🔬 **Kontrollerade Lab-miljöer** | Övning på egna VMs (Metasploitable, DVWA, VulnHub) |
| ✍️ **Explicit Tillstånd** | Penetrationstestning med SKRIFTLIGT auktoriserat avtal |
| 💼 **Professionell Pentest** | Som anställd eller konsult med tydlig Scope of Work |
| 🐛 **Bug Bounty Programs** | Inom programmets definierade scope och regler |
| 🏆 **CTF Competitions** | Capture The Flag-tävlingar och hackingutmaningar |
| 🛡️ **Defensiv Säkerhet** | Förstå attackvektorer för att bygga bättre försvar |

### ❌ FÖRBJUDEN användning:

| Illegal Användning | Konsekvens |
|--------------------|------------|
| 🚫 **Obehörig åtkomst** | Dataintrång - Brott mot BrB 4:9c |
| 🚫 **Testa utan tillstånd** | Även på arbetsplatsens/skolans system |
| 🚫 **ISP/Offentlig infrastruktur** | Allvarliga brott med fängelsestraff |
| 🚫 **Personlig vinning** | Stöld, bedrägeri, utpressning |
| 🚫 **Skadlig avsikt** | Sabotage, ransomware, DDoS |
| 🚫 **Privacy-intrång** | Doxxing, stalking, spionage |

### ⚖️ Lagstiftning i Sverige

**Dataintrång (BrB 4:9c):**
> Den som olovligen genom användning av en teknisk anordning skaffar sig tillgång till en upptagning för automatisk databehandling eller annan sådan överföring eller genom olovlig befattning med en sådan upptagning, ändrar, utplånar, blockerar eller i registret för in en uppgift eller vidtar någon annan sådan åtgärd, dömes för dataintrång...

**Straffskala:**
- 💰 Böter eller
- 🔒 Fängelse upp till **2 år**
- ⚖️ Grovt dataintrång: Fängelse **6 månader - 6 år**
- 💸 Skadestånd till offer

**Internationella lagar:**
- 🇺🇸 USA: Computer Fraud and Abuse Act (CFAA)
- 🇪🇺 EU: Network and Information Security Directive
- 🇬🇧 UK: Computer Misuse Act 1990

### 🎯 Gyllene regel för etisk hacking:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  "If it's not YOURS and you don't have WRITTEN        │
│   PERMISSION - DON'T TOUCH IT!"                        │
│                                                         │
│  Translation: Om det inte är DITT och du inte har      │
│  SKRIFTLIGT TILLSTÅND - RÖR DET INTE!                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 🔐 Säkra övningsmiljöer:

Använd **ENDAST** dessa för att öva:

1. **Din egen utrustning** - VMs på din egen dator
2. **Officiella lab-plattformar:**
   - 🏴 Hack The Box (https://hackthebox.com)
   - 🎮 TryHackMe (https://tryhackme.com)
   - 📚 PentesterLab (https://pentesterlab.com)
   - 🎯 VulnHub VMs (https://vulnhub.com)
   - 🏆 HackThisSite (https://hackthissite.org)
3. **Bug Bounty Programs** (med tydligt scope):
   - HackerOne
   - Bugcrowd
   - Intigriti
4. **Lokala VMs:**
   - Metasploitable 2/3
   - DVWA
   - WebGoat

### 📜 Etiska principer för denna guide:

1. **🎓 Education First** - Lärande är syftet, inte hacking
2. **⚖️ Legal Always** - All praktik sker i lagliga miljöer
3. **🛡️ Defense Mindset** - Förstå attacker för att försvara bättre
4. **📝 Transparency** - Alltid dokumentera och få tillstånd
5. **🤝 Responsible Disclosure** - Rapportera sårbarheter ansvarsfullt
6. **🚫 No Gray Areas** - Om du är osäker, GÖR DET INTE

### ⚠️ VARNING till läsaren:

> Författaren och distributören av denna guide ansvarar INTE för:
> - Illegal användning av information i guiden
> - Skador orsakade av oetisk användning av verktyg
> - Juridiska konsekvenser av användarens handlingar
>
> Genom att fortsätta läsa accepterar du FULLT ANSVAR för hur du använder denna kunskap.

**🔴 Om du INTE kan acceptera att använda denna kunskap etiskt och lagligt - SLUTA LÄSA NU.**

---

## 🎮 Välj Din Inlärningsväg

Inte säker på var du ska börja? Använd denna guide för att hitta rätt nivå:

### 🧭 Navigeringsguide

```
┌─────────────────────────────────────────────────────────────┐
│                 ÄR DU HELT NY TILL LINUX?                   │
│                                                             │
│  JA  ──────────────────────────▶  Börja på NIVÅ 1          │
│                                                             │
│  NEJ - Kan grundläggande       ──▶  Hoppa till NIVÅ 3      │
│        Linux-kommandon                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│            HAR DU KALI LINUX INSTALLERAT?                   │
│                                                             │
│  NEJ ──────────────────────────▶  Börja på NIVÅ 1          │
│                                                             │
│  JA - VirtualBox/VMware       ──▶  Fortsätt till NIVÅ 2     │
│                                                             │
│  JA - WSL2                     ──▶  Läs WSL-guiden i        │
│                                    Nivå 1, sedan Nivå 2     │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│         HAR DU TIDIGARE CYBERSÄKERHETSERFARENHET?           │
│                                                             │
│  NEJ ──────────────────────────▶  Börja på NIVÅ 0          │
│                                   (Förstå etik & legalitet) │
│                                                             │
│  JA - Security+ eller CEH     ──▶  Hoppa till NIVÅ 4        │
│                                                             │
│  JA - OSCP eller högre        ──▶  Hoppa till NIVÅ 5        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 📊 Nivå-översikt

| Nivå | Namn | Tidsåtgång | Svårighetsgrad | Du lär dig | Förutsättningar |
|------|------|------------|----------------|------------|-----------------|
| **0** | 🎓 Förkunskaper & Legalitet | 10 min | ⭐ | Etik, juridik, vad Kali är | Ingen |
| **1** | 💻 Installation & Setup | 30-60 min | ⭐⭐ | Installera Kali, första boot | Windows 11 kunskaper |
| **2** | 🐧 Linux-grunderna | 45-90 min | ⭐⭐ | Terminal, filsystem, kommandon | Nivå 1 klar |
| **3** | 🔍 Reconnaissance | 2-3 timmar | ⭐⭐⭐ | Nmap, Wireshark, OSINT | Nivå 2 klar |
| **4A** | 🛡️ Vulnerability Assessment | 1.5 timmar | ⭐⭐⭐ | Hitta sårbarheter | Nivå 3 klar |
| **4B** | 💥 Exploitation | 2-3 timmar | ⭐⭐⭐⭐ | Metasploit, Burp Suite | Nivå 4A klar |
| **4C** | 🔐 Password Attacks | 1.5 timmar | ⭐⭐⭐⭐ | John, Hydra, Hashcat | Nivå 3 klar |
| **4D** | 📡 Wireless Attacks | 1.5 timmar | ⭐⭐⭐⭐ | Aircrack-ng, WPA cracking | Nivå 3 klar |
| **5** | 🚀 Advanced Topics | 3-4 timmar | ⭐⭐⭐⭐⭐ | Post-exploitation, anonymitet | Alla Nivå 4 klara |

### 🎯 Rekommenderade vägar baserat på mål

#### 🏁 "Jag vill bara testa Kali Linux"
```
Nivå 1 → Nivå 2 → Nivå 3 (endast Nmap) → Klart!
Total tid: ~2 timmar
```

#### 🎓 "Jag pluggar till Security+ eller CEH"
```
Nivå 0 → Nivå 1 → Nivå 2 → Nivå 3 (alla verktyg) → Nivå 4A → Nivå 4B (Metasploit) → Klart!
Total tid: ~8-10 timmar
```

#### 💼 "Jag vill bli penetrationstestare"
```
Nivå 0 → Nivå 1 → Nivå 2 → Nivå 3 → Nivå 4A → Nivå 4B → Nivå 4C → Nivå 4D → Nivå 5 → Karriärguide
Total tid: 40-60 timmar + kontinuerlig övning
```

#### 🐛 "Jag vill göra bug bounty"
```
Nivå 0 → Nivå 2 → Nivå 3 (Nmap, theHarvester) → Nivå 4A (SQLmap) → Nivå 4B (Burp Suite) → Nivå 5 (Report Writing)
Total tid: 15-20 timmar
```

#### 🏆 "Jag vill plugga till OSCP"
```
ALLA NIVÅER + Intensiv lab-övning + Hack The Box
Total tid: 200+ timmar
```

### 📖 Hur man använder denna guide

#### ✅ Rekommenderad approach:

1. **📚 Läs sekventiellt** - Hoppa inte över nivåer (om du är nybörjare)
2. **💻 Praktisera aktivt** - Kör ALLA kommandon själv
3. **🔬 Gör övningarna** - Teori utan praktik är värdelöst
4. **✍️ Dokumentera** - Anteckna viktiga koncept
5. **🔁 Repetera** - Gå tillbaka och öva mer vid behov
6. **🧪 Bygg lab** - Sätt upp Metasploitable och öva kontinuerligt

#### ❌ Undvik dessa misstag:

- ⛔ Hoppa över den juridiska delen (Nivå 0)
- ⛔ Bara läsa utan att praktisera
- ⛔ Testa på riktiga system utan tillstånd
- ⛔ Ge upp när något är svårt
- ⛔ Försöka lära sig allt på en gång

### 🎓 Självbedömning - Är du redo?

**Innan Nivå 1:**
- [ ] Jag har läst och förstått den juridiska disclaimern
- [ ] Jag förstår skillnaden mellan etiskt och oetiskt hacking
- [ ] Jag har en dator med Windows 11 och minst 8GB RAM
- [ ] Jag är villig att lägga tid på att lära mig

**Innan Nivå 3:**
- [ ] Jag kan navigera i terminalen bekvämt
- [ ] Jag förstår filrättigheter i Linux
- [ ] Jag har en lab-miljö uppsatt (Metasploitable eller liknande)
- [ ] Jag förstår nätverksbasics (IP, portar, TCP/UDP)

**Innan Nivå 4:**
- [ ] Jag kan använda Nmap för port scanning
- [ ] Jag förstår skillnaden mellan olika sårbarhetstermer
- [ ] Jag har läst om exploit-etik
- [ ] Jag har en isolerad testmiljö

**Innan Nivå 5:**
- [ ] Jag har genomfört minst 5 lab-övningar framgångsrikt
- [ ] Jag förstår grundläggande exploit-koncept
- [ ] Jag kan skriva enkla bash-scripts
- [ ] Jag har börjat tänka på career path

---

## 🛠️ Vad behöver du för att komma igång?

### Hårdvarukrav (Minimum)

| Komponent | Minimum | Rekommenderat | Optimalt |
|-----------|---------|---------------|----------|
| **CPU** | Dual-core 2.0 GHz | Quad-core 2.5 GHz | 6+ kärnor, 3.0+ GHz |
| **RAM** | 4 GB (2GB för VM) | 8 GB (4GB för VM) | 16+ GB |
| **Lagring** | 40 GB fri disk | 80 GB SSD | 256+ GB NVMe SSD |
| **OS** | Windows 11 Home | Windows 11 Pro | Windows 11 Pro |
| **Virtualisation** | VT-x/AMD-V enabled | VT-x/AMD-V + VT-d | VT-x/AMD-V + VT-d |
| **Nätverk** | WiFi | Ethernet | Ethernet + Extern WiFi-adapter |

**💡 Tips:**
- För VirtualBox: Du behöver minst 4GB RAM totalt (2GB till Windows, 2GB till Kali)
- För WSL2: 8GB RAM rekommenderas starkt
- SSD gör ENORM skillnad för VM-prestanda

### Mjukvarukrav

- ✅ Windows 11 (uppdaterad)
- ✅ VirtualBox 7.0+ ELLER VMware Workstation Player (för VM-metoden)
- ✅ Minst 40GB fri diskutrymme
- ✅ Internetanslutning (för nedladdningar och uppdateringar)
- ✅ Texteditor (Notepad++, VS Code, eller liknande) för anteckningar

### Kunskap-prerequisites

| Nivå | Kunskapskrav |
|------|-------------|
| **Absolut minimum** | Kan använda Windows 11, installera program, grundläggande engelska |
| **Rekommenderat** | Förstår vad en IP-adress är, har använt kommandotolken (CMD), grundläggande IT-förståelse |
| **Optimalt** | Grundläggande nätverkskunskap, känner till OSI-modellen, har programmerat lite |

**🟢 Goda nyheter:** Även om du är total nybörjare täcker denna guide allt från grunden!

---

## 📚 Guidestruktur & Konventioner

### Symboler som används i guiden

| Symbol | Betydelse |
|--------|-----------|
| 🔴 **KRITISKT** | Juridisk varning, säkerhetshot, kan orsaka skada |
| 🟡 **VIKTIGT** | Best practice, viktigt koncept, läs noggrant |
| 🟢 **TIP** | Produktivitetstips, genvägar, rekommendationer |
| ⚠️ **VARNING** | Vanligt misstag, potentiellt problem |
| 💡 **INFO** | Bakgrundsinformation, "bra att veta" |
| ✅ **ALLOWED** | Tillåten/etisk användning |
| ❌ **FORBIDDEN** | Förbjuden/olaglig användning |
| 🎯 **MÅL** | Vad du kommer att lära dig |
| 🧪 **LAB** | Praktisk övning |
| 📝 **EXEMPEL** | Kodexempel, kommando-exempel |
| 🏆 **QUIZ** | Självtest, kunskapskontroll |

### Kodblock och kommandon

**Kommandon att köra:**
```bash
# Detta är ett kommando du ska köra i terminalen
nmap -sV 192.168.1.1
```

**Förväntad output:**
```
Starting Nmap 7.94 ( https://nmap.org ) at 2025-11-17
Nmap scan report for 192.168.1.1
PORT    STATE SERVICE
22/tcp  open  ssh
```

**Filinnehåll eller kod:**
```python
#!/usr/bin/env python3
# Detta är ett script-exempel
print("Hello, Kali!")
```

### Färgkodade rutor

> **🔴 KRITISK VARNING**
>
> Detta kan orsaka juridiska problem eller systemskador!

> **🟡 VIKTIGT ATT KOMMA IHÅG**
>
> Best practice som du bör följa.

> **🟢 PRODUKTIVITETSTIP**
>
> Gör ditt arbete enklare och snabbare.

---

## 🗺️ Vad händer härnäst?

Nu när du har läst denna introduktion och förstår guidens struktur:

### ✅ Steg 1: Bekräfta att du är redo
- [ ] Jag har läst och förstått den juridiska disclaimern
- [ ] Jag har hårdvara som uppfyller minimikraven
- [ ] Jag har valt vilken nivå jag ska börja på
- [ ] Jag förstår att jag ENDAST får testa i min egen lab-miljö

### ✅ Steg 2: Välj din väg

**För total nybörjare:**
👉 Gå till **[Nivå 0: Förkunskaper & Legalitet](./guides/niva-0-forkunskaper.md)**

**Har du grundläggande IT-kunskap men aldrig använt Kali:**
👉 Gå till **[Nivå 1: Installation & Setup](./guides/niva-1-installation.md)**

**Har du Kali installerat men inte använt verktygen:**
👉 Gå till **[Nivå 3: Reconnaissance](./guides/niva-3-reconnaissance.md)**

**Är erfaren och vill bara ha cheat sheets:**
👉 Gå till **[Cheat Sheets](./resources/cheat-sheets.md)**

### ✅ Steg 3: Förbered din miljö
- [ ] Säkerställ att virtualisering är aktiverad i BIOS
- [ ] Ha minst 40GB fri diskutrymme
- [ ] Ha en stabil internetanslutning
- [ ] Reservera 2-3 timmar ostörd tid för installation

### ✅ Steg 4: Börja lära dig!

---

## 📞 Support & Community

**🤔 Har du frågor?**
- 📖 Kolla **[Troubleshooting & FAQ](./resources/troubleshooting.md)** först
- 🌐 Officiellt Kali Forum: https://forums.kali.org/
- 💬 Reddit: r/Kalilinux, r/netsec, r/AskNetsec
- 📺 YouTube: Hackersploit, John Hammond, IppSec, NetworkChuck

**🐛 Hittat ett fel i guiden?**
- Guiden uppdateras regelbundet baserat på feedback
- Kontakta författaren eller bidra med förbättringar

**🎓 Vill du lära dig mer?**
- Se **[Career Roadmap](./resources/career-roadmap.md)** för certifieringsvägar
- Se **[Lab Setup](./resources/lab-setup.md)** för övningsmiljöer

---

## 📄 Licens & Användning

**Denna guide är:**
- ✅ Gratis att använda för personlig utbildning
- ✅ OK att dela med andra (med attribution)
- ✅ OK att använda i utbildningssyfte

**Denna guide är INTE:**
- ❌ Avsedd för kommersiell användning utan tillstånd
- ❌ En uppmaning till illegal aktivitet
- ❌ Juridisk rådgivning

---

## 🙏 Acknowledgments

Denna guide är byggd på kunskap från:
- Kali Linux Documentation Team
- Offensive Security (makers av OSCP)
- Cybersecurity community på GitHub, Reddit, och Discord
- Hundratals tutorials, böcker, och kurser

**Särskilt tack till:**
- Offensive Security för Kali Linux
- Rapid7 för Metasploit
- Gordon Lyon (Fyodor) för Nmap
- Alla open-source contributors som gör cybersäkerhet tillgänglig

---

## 🚀 Redo att börja din resa?

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     "The only way to learn hacking is by hacking"         ║
║                                                            ║
║     "Det enda sättet att lära sig hacka är genom          ║
║      att hacka (i en laglig lab-miljö såklart!)"          ║
║                                                            ║
║                  - Cybersecurity Community                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

**👉 Börja här: [Nivå 0 - Förkunskaper & Legalitet](./guides/niva-0-forkunskaper.md)**

---

**Version History:**
- v2.0 (November 2025) - Komplett omskrivning för Windows 11, uppdaterade verktyg
- v1.5 (Juli 2024) - Lade till WSL2-support
- v1.0 (Januari 2024) - Initial release

**Senast uppdaterad:** 2025-11-17
