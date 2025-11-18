# 🚀 Career Roadmap & Resources

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

## 📚 Innehållsförteckning

1. [Karriärvägar inom Cybersäkerhet](#karriarvagar)
2. [Färdighetsmatris och Progression](#fardighetsmatris)
3. [Certifieringar](#certifieringar)
4. [Learning Paths](#learning-paths)
5. [Böcker](#bocker)
6. [Online Kurser och Plattformar](#kurser)
7. [YouTube Kanaler och Podcasts](#youtube-podcasts)
8. [Communities och Networking](#communities)
9. [Portfolio Building](#portfolio)
10. [Jobbsökning och Intervjuer](#jobbsokning)
11. [Löneutveckling](#loneutveckling)
12. [Fortsatt Utveckling](#fortsatt-utveckling)

---

## 🎯 Karriärvägar inom Cybersäkerhet {#karriarvagar}

### Översikt av Roller

```
┌────────────────────────────────────────────────────┐
│  CYBERSECURITY CAREER TREE                         │
└────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │  CISO / Manager │
                    │   (10+ years)   │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
    ┌─────▼─────┐     ┌─────▼─────┐    ┌──────▼──────┐
    │ Red Team  │     │ Blue Team │    │   GRC       │
    │  Leader   │     │  Manager  │    │  Manager    │
    │ (7-10y)   │     │  (7-10y)  │    │  (7-10y)    │
    └─────┬─────┘     └─────┬─────┘    └──────┬──────┘
          │                 │                  │
    ┌─────▼─────┐     ┌─────▼─────┐    ┌──────▼──────┐
    │ Sr. Pen-  │     │ Sr. SOC   │    │ Sr. Security│
    │  tester   │     │ Analyst   │    │  Analyst    │
    │ (4-7y)    │     │ (4-7y)    │    │  (4-7y)     │
    └─────┬─────┘     └─────┬─────┘    └──────┬──────┘
          │                 │                  │
    ┌─────▼─────┐     ┌─────▼─────┐    ┌──────▼──────┐
    │Penetration│     │   SOC     │    │  Security   │
    │  Tester   │     │ Analyst   │    │  Analyst    │
    │ (1-4y)    │     │ (1-4y)    │    │  (1-4y)     │
    └───────────┘     └───────────┘    └─────────────┘
```

### Red Team (Offensive Security)

| Roll | Beskrivning | Erfarenhet | Lön (Sverige) |
|------|-------------|------------|---------------|
| **Junior Penetration Tester** | Basic pentesting, följer checklists | 0-2 år | 35-45k/mån |
| **Penetration Tester** | Självständiga tester, reportering | 2-4 år | 45-60k/mån |
| **Senior Penetration Tester** | Komplexa miljöer, metodutveckling | 4-7 år | 60-80k/mån |
| **Red Team Operator** | Advanced persistent threats, stealth | 5-8 år | 70-90k/mån |
| **Red Team Leader** | Planerar operationer, leder team | 7-10 år | 80-100k/mån |

**Typiska Arbetsuppgifter:**
- Penetrationstestning (web, nätverk, mobil)
- Vulnerability assessments
- Social engineering-tester
- Red team-operationer
- Rapportskrivning och presentationer
- Security awareness training

**Färdigheter:**
- ✅ Kali Linux och offensiva verktyg
- ✅ Programmering (Python, Bash, PowerShell)
- ✅ Nätverksprotokoll (TCP/IP, HTTP, SMB)
- ✅ Web application security (OWASP Top 10)
- ✅ Active Directory exploitation
- ✅ Rapportskrivning och kommunikation

### Blue Team (Defensive Security)

| Roll | Beskrivning | Erfarenhet | Lön (Sverige) |
|------|-------------|------------|---------------|
| **SOC Analyst L1** | Monitoring, incident triage | 0-2 år | 30-40k/mån |
| **SOC Analyst L2** | Incident investigation, response | 2-4 år | 40-55k/mån |
| **SOC Analyst L3/Senior** | Advanced threats, hunting | 4-7 år | 55-75k/mån |
| **Incident Responder** | Breach response, forensics | 3-6 år | 60-80k/mån |
| **Threat Hunter** | Proaktiv threat detection | 5-8 år | 70-90k/mån |
| **SOC Manager** | Leder SOC-team, strategi | 7-10 år | 80-100k/mån |

**Typiska Arbetsuppgifter:**
- Security monitoring (SIEM)
- Incident response och forensics
- Threat intelligence analysis
- Security tool management (IDS/IPS, firewall)
- Log analysis
- Playbook development

**Färdigheter:**
- ✅ SIEM-plattformar (Splunk, Elastic, QRadar)
- ✅ Network analysis (Wireshark, tcpdump)
- ✅ Forensics tools (Volatility, Autopsy)
- ✅ Threat intelligence (MITRE ATT&CK)
- ✅ Scripting (Python, PowerShell)
- ✅ Windows och Linux internals

### GRC (Governance, Risk, Compliance)

| Roll | Beskrivning | Erfarenhet | Lön (Sverige) |
|------|-------------|------------|---------------|
| **Security Analyst** | Risk assessments, compliance | 0-2 år | 35-45k/mån |
| **Security Consultant** | Rådgivning, policies | 2-5 år | 45-65k/mån |
| **Security Architect** | Design av säkerhetslösningar | 5-8 år | 65-85k/mån |
| **Compliance Manager** | GDPR, ISO 27001, regulatoriskt | 5-10 år | 70-90k/mån |
| **CISO** | Overall security strategy | 10+ år | 100-150k+/mån |

**Typiska Arbetsuppgifter:**
- Risk assessments
- Policy development
- Compliance audits (GDPR, ISO 27001, NIS2)
- Security awareness training
- Vendor risk management
- Security governance

### Specialiseringar

**Cloud Security:**
- AWS/Azure/GCP security
- Container security (Docker, Kubernetes)
- Serverless security
- Cloud pentesting

**Application Security:**
- Secure code review
- SAST/DAST tools
- DevSecOps
- Threat modeling

**OT/ICS Security:**
- Industrial control systems
- SCADA security
- Critical infrastructure protection

**Mobile Security:**
- iOS/Android pentesting
- Mobile app security
- Reverse engineering

---

## 📊 Färdighetsmatris och Progression {#fardighetsmatris}

### Nivå 1: Nybörjare (0-6 månader)

**Tekniska Färdigheter:**
- [ ] Linux basics (navigering, filhantering)
- [ ] Nätverk fundamentals (TCP/IP, DNS, HTTP)
- [ ] Kali Linux installation och setup
- [ ] Basic Nmap scanning
- [ ] Metasploit grundläggande användning
- [ ] Enkel web app testing (DVWA low)

**Certifieringar:**
- CompTIA Security+
- CompTIA Network+
- eJPT (eLearnSecurity Junior Penetration Tester)

**Praktisk Erfarenhet:**
- TryHackMe: Complete Beginner path
- HackTheBox: Starting Point
- DVWA challenges (Low security)

### Nivå 2: Junior (6-18 månader)

**Tekniska Färdigheter:**
- [ ] Advanced Nmap och enumeration
- [ ] Web app pentesting (OWASP Top 10)
- [ ] Basic exploit development
- [ ] Password cracking (John, Hashcat)
- [ ] Burp Suite proficiency
- [ ] Basic Active Directory exploitation
- [ ] Rapportskrivning

**Certifieringar:**
- CEH (Certified Ethical Hacker)
- PNPT (Practical Network Penetration Tester)
- eWPT (Web Application Penetration Tester)

**Praktisk Erfarenhet:**
- TryHackMe: Offensive Pentesting path
- HackTheBox: 20+ easy boxes
- Bug bounty program (start)
- Personal blog med writeups

### Nivå 3: Intermediate (1.5-3 år)

**Tekniska Färdigheter:**
- [ ] Advanced web app pentesting
- [ ] Active Directory full compromise
- [ ] Custom exploit development
- [ ] Privilege escalation expertise (Windows/Linux)
- [ ] Wireless security testing
- [ ] Social engineering campaigns
- [ ] Professional reporting

**Certifieringar:**
- **OSCP** (Offensive Security Certified Professional) - KRITISK!
- GPEN (GIAC Penetration Tester)
- eWPTX (Advanced Web Application PT)

**Praktisk Erfarenhet:**
- HackTheBox: Pro Labs
- OSCP lab + certification
- Bug bounty submissions (actual findings)
- GitHub portfolio (tools, scripts)

### Nivå 4: Advanced (3-5 år)

**Tekniska Färdigheter:**
- [ ] Advanced exploit development (buffer overflows, ROP)
- [ ] Zero-day research
- [ ] Red team operations
- [ ] Advanced persistence techniques
- [ ] Advanced AD attacks (Kerberos, NTLM relay)
- [ ] C2 framework development
- [ ] Cloud pentesting (AWS, Azure)

**Certifieringar:**
- **OSEP** (Offensive Security Experienced Penetration Tester)
- **OSWE** (Offensive Security Web Expert)
- GXPN (GIAC Exploit Researcher and Advanced PT)
- CRTO (Certified Red Team Operator)

**Praktisk Erfarenhet:**
- HackTheBox: Pro Labs completion
- Real-world pentesting engagements
- Bug bounty earnings
- Conference speaking (BsidesStockholm, etc.)

### Nivå 5: Expert (5+ år)

**Tekniska Färdigheter:**
- [ ] Full-stack exploit development
- [ ] Advanced malware analysis
- [ ] Kernel exploitation
- [ ] 0-day discovery and weaponization
- [ ] Advanced Red Team TTPs
- [ ] Custom tool development
- [ ] Research and publication

**Certifieringar:**
- **OSCE3** (Offensive Security Certified Expert 3)
- OSEE (Offensive Security Exploitation Expert)
- GREM (GIAC Reverse Engineering Malware)

**Praktisk Erfarenhet:**
- Leading red team operations
- CVE discoveries
- Security research publications
- Training/mentoring junior pentesters

---

## 🎓 Certifieringar {#certifieringar}

### Entry-Level Certifieringar

#### CompTIA Security+

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | ~$370 (exam) |
| **Svårighetsgrad** | Lätt |
| **Tid att förbereda** | 2-3 månader (nybörjare) |
| **Förnyelse** | 3 år (CEUs) |
| **Värde** | ⭐⭐⭐ (bra första cert) |

**Vad det täcker:**
- Threats, attacks, vulnerabilities
- Architecture and design
- Implementation
- Operations and incident response
- Governance, risk, compliance

**Rekommenderas för:**
- Total nybörjare
- SOC analyst L1 roller
- Förberedelse för mer avancerade certs

#### eJPT (eLearnSecurity Junior Penetration Tester)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $200 (ink. kurs) |
| **Svårighetsgrad** | Lätt-Medel |
| **Tid att förbereda** | 1-2 månader (med denna guide!) |
| **Format** | Practical lab-based exam (48h) |
| **Värde** | ⭐⭐⭐⭐ (bästa första praktiska cert) |

**Varför eJPT?**
- Helt praktisk (ingen multiplechoice)
- Beginner-friendly
- Bra förberedelse för OSCP
- Billigt

### Intermediate Certifieringar

#### CEH (Certified Ethical Hacker)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $1,199 (exam) + ~$800 (kurs optional) |
| **Svårighetsgrad** | Medel |
| **Tid att förbereda** | 3-6 månader |
| **Format** | 125 multiplechoice (4h) |
| **Värde** | ⭐⭐⭐ (HR-vänlig, international recognition) |

**Pros:**
- Välkänd i industrin
- HR-vänlig (lätt att förstå för non-technical)
- Täcker bred kunskapsbas
- DoD 8570 godkänd (USA government)

**Cons:**
- Dyr
- Främst theoretical (multiplechoice)
- EC-Council's material är ibland utdaterat
- Mindre respekterad av tekniska personer jämfört med OSCP

#### OSCP (Offensive Security Certified Professional)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $1,649 (Learn One package: 90 days lab + exam) |
| **Svårighetsgrad** | Hög |
| **Tid att förbereda** | 6-12 månader |
| **Format** | 24h hands-on lab exam + 24h rapport |
| **Värde** | ⭐⭐⭐⭐⭐ (BÄSTA pentesting cert!) |

**🏆 VARFÖR OSCP ÄR "THE GOLD STANDARD":**

```
✅ Helt praktisk (ingen multiplechoice)
✅ "Try Harder" mentalitet
✅ Respekterad av ALLA i industrin
✅ Bevisar faktiska färdigheter
✅ Öppnar dörrar för jobb
✅ Challenging men extremt givande
```

**OSCP Exam Format:**
- 24 timmar att kompromettera flera machines
- Samla 70 poäng (av 100) för att klara
- 24 timmar extra för rapportskrivning
- Buffer overflow mandatory (tidigare, nu optional)

**Förberedelse:**
1. Slutför denna guide först!
2. HackTheBox: 30+ easy/medium boxes
3. TryHackMe: Offensive Pentesting path
4. PEN-200 course material (included)
5. PWK lab (90 dagar): Root 50+ boxes
6. Practice exams (TJ Null's list)

**Tips:**
- Dokumentera ALLT (screenshots, kommandon)
- Sov inför examen!
- Börja med easy wins (quick points)
- Enum, enum, enum!
- "Try Harder" - men ta breaks också

### Advanced Certifieringar

#### OSEP (Offensive Security Experienced Penetration Tester)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $1,649 |
| **Svårighetsgrad** | Mycket hög |
| **Förutsättningar** | OSCP eller likvärdig erfarenhet |
| **Format** | 48h hands-on exam |
| **Värde** | ⭐⭐⭐⭐⭐ (för advanced roles) |

**Fokus:**
- Advanced exploitation techniques
- Antivirus evasion
- Advanced Active Directory attacks
- Process injection och migration
- C2 operations

#### OSWE (Offensive Security Web Expert)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $1,649 |
| **Svårighetsgrad** | Mycket hög |
| **Fokus** | White-box web app pentesting |
| **Format** | 48h exam + 24h rapport |

**Perfekt för:**
- Application security specialists
- Bug bounty hunters
- Secure code reviewers

#### GPEN (GIAC Penetration Tester)

| Aspekt | Detalj |
|--------|--------|
| **Kostnad** | $2,499 (ink. SANS kurs) |
| **Svårighetsgrad** | Medel-Hög |
| **Format** | Multiplechoice (115 frågor, 3h) |
| **Värde** | ⭐⭐⭐⭐ (SANS kvalitet) |

**Pros:**
- SANS training är excellent
- Täcker modern pentesting methodology
- Respekterad cert
- Good for government/DoD jobs

**Cons:**
- Mycket dyr
- Multiplechoice (ej praktisk)

### Certifieringsroadmap

```
┌─────────────────────────────────────────────────┐
│  REKOMMENDERAD CERTIFIERINGSVÄG                 │
└─────────────────────────────────────────────────┘

År 1:
└─► CompTIA Security+ eller eJPT
    └─► Grundläggande förståelse

År 1-2:
└─► OSCP (prioritet!)
    └─► Industry standard för pentesting

År 2-3:
└─► Specialisering:
    ├─► OSWE (Web app focus)
    ├─► CRTO (Red team focus)
    └─► GPEN (SANS approach)

År 3-5:
└─► Advanced:
    ├─► OSEP (Advanced exploitation)
    ├─► GXPN (Expert level)
    └─► OSCE3 (Elite)

Blue Team Alternativ:
└─► GCIH → GCIA → GREM
```

---

## 🛤️ Learning Paths {#learning-paths}

### Path 1: Penetration Tester (Denna Guides Fokus)

```
Månad 1-2:
├─ Slutför Nivå 0-2 i denna guide
├─ TryHackMe: Linux Fundamentals
└─ Basic networking (Cisco CCNA videos)

Månad 3-4:
├─ Slutför Nivå 3-4 i denna guide
├─ TryHackMe: Complete Beginner
├─ HackTheBox: Starting Point
└─ Setup local lab (Metasploitable, DVWA)

Månad 5-6:
├─ Slutför Nivå 5 i denna guide
├─ TryHackMe: Offensive Pentesting
├─ HackTheBox: 10 easy boxes
└─ eJPT certification

Månad 7-12:
├─ HackTheBox: 30+ boxes (easy/medium)
├─ TryHackMe: Advanced paths
├─ OSCP förberedelse
└─ Bug bounty (start)

Månad 13-18:
├─ OSCP PWK course + lab
├─ OSCP exam
├─ Portfolio building (GitHub, blog)
└─ Jobbansökningar

Månad 18+:
├─ Professional work experience
├─ Advanced certs (OSWE, OSEP)
├─ Specialisering
└─ Continued learning
```

### Path 2: SOC Analyst

```
Månad 1-3:
├─ CompTIA Security+
├─ Basic networking
├─ Windows/Linux fundamentals
└─ TryHackMe: Cyber Defense

Månad 4-6:
├─ SIEM training (Splunk fundamentals)
├─ Log analysis
├─ Incident response basics
└─ TryHackMe: SOC Level 1

Månad 7-12:
├─ Blue Team Labs Online
├─ Practice incident response
├─ MITRE ATT&CK framework
└─ Jobbansökningar (SOC L1)

Månad 12+:
├─ Professional SOC experience
├─ Advanced certs (GCIH, BTL1)
├─ Threat hunting
└─ Progression till L2/L3
```

### Path 3: Application Security

```
Månad 1-3:
├─ Webbutveckling basics (HTML, JS, PHP)
├─ OWASP Top 10
├─ Burp Suite training
└─ DVWA completion

Månad 4-6:
├─ PortSwigger Web Security Academy
├─ Bug bounty programs (start)
├─ Source code review
└─ TryHackMe: Web Fundamentals

Månad 7-12:
├─ Advanced web attacks
├─ Bug bounty submissions
├─ eWPT certification
└─ Portfolio (HackerOne, Bugcrowd)

Månad 12+:
├─ OSWE förberedelse
├─ Professional AppSec role
├─ DevSecOps integration
└─ SAST/DAST tools
```

---

## 📖 Böcker {#bocker}

### Must-Read för Penetration Testing

#### 1. "The Hacker Playbook 3" - Peter Kim

**Rating:** ⭐⭐⭐⭐⭐

**Varför:**
- Praktisk, hands-on approach
- Täcker modern pentesting
- Real-world scenarios
- OSCP-relevant

**Pris:** ~$40

#### 2. "The Web Application Hacker's Handbook" - Stuttard & Pinto

**Rating:** ⭐⭐⭐⭐⭐

**Varför:**
- Bibeln för web app pentesting
- Djupgående OWASP coverage
- Fortfarande relevant (även om lite äldre)

**Pris:** ~$50

#### 3. "Penetration Testing: A Hands-On Introduction to Hacking" - Georgia Weidman

**Rating:** ⭐⭐⭐⭐

**Varför:**
- Nybörjarvänlig
- Praktiska övningar
- Metasploit focus

**Pris:** ~$45

#### 4. "Rtfm: Red Team Field Manual" - Ben Clark

**Rating:** ⭐⭐⭐⭐⭐

**Varför:**
- Perfekt cheat sheet
- Compact reference
- Tar med på exam (vissa certs)

**Pris:** ~$15 (MYCKET BÄSTA VALUE!)

#### 5. "Black Hat Python" - Justin Seitz

**Rating:** ⭐⭐⭐⭐

**Varför:**
- Lär Python för hacking
- Custom tool development
- Praktiska exempel

**Pris:** ~$40

### Blue Team / Defensive

#### 1. "Blue Team Handbook" - Don Murdoch

**Rating:** ⭐⭐⭐⭐

**Fokus:** Incident response, forensics

#### 2. "The Art of Memory Forensics" - Ligh et al.

**Rating:** ⭐⭐⭐⭐⭐

**Fokus:** Memory analysis, Volatility

### Fundamentals

#### 1. "Computer Networking: A Top-Down Approach" - Kurose & Ross

**Rating:** ⭐⭐⭐⭐⭐

**Varför:** Bästa networking-boken

#### 2. "Linux Basics for Hackers" - OccupyTheWeb

**Rating:** ⭐⭐⭐⭐

**Varför:** Perfect Linux introduction för hacking

---

## 💻 Online Kurser och Plattformar {#kurser}

### Penetration Testing Platforms

#### HackTheBox (hackthebox.com)

**Kostnad:** $14/mån (VIP) eller $22/mån (VIP+)

**Fördelar:**
- 300+ vulnerable machines
- Real-world scenarios
- Huge community
- Ranking system (motivation)

**Rekommendation:** ⭐⭐⭐⭐⭐

**Hur använda:**
1. Börja med "Starting Point" (gratis)
2. TJ Null's OSCP-like box list
3. Dokumentera alla writeups
4. Fokus på metodik, inte bara "flag"

#### TryHackMe (tryhackme.com)

**Kostnad:** $11/mån (Premium)

**Fördelar:**
- Nybörjarvänlig
- Guided learning paths
- Web-based Kali (ingen VPN krävs)
- 1000+ rooms

**Rekommendation:** ⭐⭐⭐⭐⭐ (för nybörjare)

**Bästa Learning Paths:**
- Complete Beginner
- Offensive Pentesting
- Web Fundamentals
- Red Teaming

#### PortSwigger Web Security Academy

**Kostnad:** GRATIS!

**Fördelar:**
- Gratis, hög kvalitet
- Interaktiva labs
- Täcker alla web vulnerabilities
- Burp Suite training

**Rekommendation:** ⭐⭐⭐⭐⭐

**Must-do:** Alla labs, alla topics!

#### Offensive Security (Learn Platform)

**Kostnad:** $1,649 per course

**Courses:**
- PEN-200 (OSCP)
- PEN-300 (OSEP)
- WEB-300 (OSWE)
- EXP-401 (OSEE)

**Rekommendation:** ⭐⭐⭐⭐⭐ (industry best)

### Blue Team Platforms

#### Blue Team Labs Online (blueteamlabs.online)

**Kostnad:** $15/mån

**Fokus:** Incident response, forensics, threat hunting

**Rekommendation:** ⭐⭐⭐⭐

#### CyberDefenders (cyberdefenders.org)

**Kostnad:** GRATIS!

**Fokus:** Blue team challenges, forensics

**Rekommendation:** ⭐⭐⭐⭐

### Video Courses

#### Udemy

**Rekommenderade Kurser:**
- "The Complete Ethical Hacking Course" - Heath Adams
- "Practical Ethical Hacking" - TCM Security
- "Learn Python & Ethical Hacking From Scratch"

**Kostnad:** $10-20 (during sales)

**Tips:** Vänta alltid på Udemy sale (happens ofta)!

#### Cybrary (cybrary.it)

**Kostnad:** Freemium ($0-399/år)

**Kurser:** CEH, CISSP, CompTIA, etc.

**Rekommendation:** ⭐⭐⭐ (bra för certs prep)

---

## 🎥 YouTube Kanaler och Podcasts {#youtube-podcasts}

### YouTube Kanaler

#### 1. IppSec

**URL:** youtube.com/@ippsec

**Innehåll:** HackTheBox walkthroughs

**Varför:** ⭐⭐⭐⭐⭐
- Bästa HTB walkthroughs
- Metodisk approach
- Lär tänkesätt, inte bara tools

#### 2. John Hammond

**URL:** youtube.com/@_JohnHammond

**Innehåll:** CTF, malware analysis, tutorials

**Varför:** ⭐⭐⭐⭐⭐
- Energisk, rolig
- Bred täckning
- Bra för nybörjare

#### 3. LiveOverflow

**URL:** youtube.com/@LiveOverflow

**Innehåll:** Advanced hacking, binary exploitation

**Varför:** ⭐⭐⭐⭐⭐
- Djupgående tekniskt
- Exploit development
- Security research

#### 4. The Cyber Mentor (TCM Security)

**URL:** youtube.com/@TCMSecurityAcademy

**Innehåll:** Pentesting tutorials, career advice

**Varför:** ⭐⭐⭐⭐⭐
- Practical tutorials
- Career guidance
- OSCP tips

#### 5. NetworkChuck

**URL:** youtube.com/@NetworkChuck

**Innehåll:** Networking, Linux, career tips

**Varför:** ⭐⭐⭐⭐
- Nybörjarvänlig
- Entertaining
- Coffee memes!

#### 6. STÖK

**URL:** youtube.com/@STOKfredrik

**Innehåll:** Bug bounty, web hacking

**Varför:** ⭐⭐⭐⭐
- Bug bounty focus
- Real findings
- Motivational

#### 7. Hak5

**URL:** youtube.com/@hak5

**Innehåll:** Pentesting tools, tutorials

**Varför:** ⭐⭐⭐⭐
- Hardware hacking
- Tool reviews
- Weekly shows

### Podcasts

#### 1. Darknet Diaries

**Host:** Jack Rhysider

**Varför:** ⭐⭐⭐⭐⭐
- Storytelling om verkliga hacks
- Incredibly entertaining
- Motivational

#### 2. Smashing Security

**Hosts:** Graham Cluley, Carole Theriault

**Varför:** ⭐⭐⭐⭐
- Weekly security news
- British humor
- Accessible

#### 3. Risky Business

**Host:** Patrick Gray

**Varför:** ⭐⭐⭐⭐
- In-depth security news
- Expert guests

---

## 👥 Communities och Networking {#communities}

### Discord Servers

#### 1. TryHackMe Official

**Storlek:** 500,000+ members

**Varför joina:**
- Hjälp med rooms
- Hints utan spoilers
- Networking med learners

#### 2. HackTheBox Official

**Storlek:** 300,000+ members

**Varför joina:**
- Box discussions (spoiler channels)
- Community events
- Challenges

#### 3. The Cyber Mentor

**Varför joina:**
- Career advice
- Study groups
- OSCP support

#### 4. InfoSec Prep (OSCP Discord)

**Varför joina:**
- OSCP förberedelse
- Study buddies
- Resource sharing

### Reddit Communities

#### r/netsec

**Subscribers:** 1M+

**Fokus:** Security research, news

#### r/AskNetsec

**Fokus:** Career questions, advice

#### r/oscp

**Fokus:** OSCP preparation, tips

#### r/HowToHack

**Fokus:** Learning resources för nybörjare

### Twitter (X)

**Följ dessa:**
- @SecurityWeekly
- @thegrugq
- @malwareunicorn
- @gynvael
- @LiveOverflow
- @IppSec
- @TheHackerNews
- @SwiftOnSecurity

### Lokala Communities (Sverige)

#### SEC-T (Stockholm)

**Event:** Årlig security conference

**Varför:** Networking, talks, workshops

#### BSides Stockholm

**Event:** Community-driven conference

**Varför:** Gratis/billigt, nybörjarvänligt

#### Stockholm Cyber Security Meetup

**Platform:** Meetup.com

**Varför:** Monthly meetups, presentations

---

## 📁 Portfolio Building {#portfolio}

### Varför Portfolio?

```
✅ BEVISAR färdigheter (inte bara säger)
✅ Visar passion och drive
✅ Differenterar dig från andra kandidater
✅ Conversation starter i intervjuer
✅ Visar kontinuerligt lärande
```

### Portfolio Components

#### 1. GitHub Profile

**Vad inkludera:**
- Custom security tools (Python scripts)
- Automation scripts
- CTF writeups (in Markdown)
- Contributions till open-source security tools

**Exempel struktur:**

```
github.com/yourname/
├── security-tools/
│   ├── port-scanner/
│   ├── password-cracker/
│   └── web-fuzzer/
├── ctf-writeups/
│   ├── hackthebox/
│   ├── tryhackme/
│   └── ctftime/
└── learning-notes/
    ├── oscp-notes.md
    └── cheat-sheets.md
```

**Tips:**
- Commit regelbundet (green squares!)
- Write clean code med comments
- Include README.md för varje projekt
- Star relevant repos (shows interests)

#### 2. Personal Blog

**Platforms:**
- Medium.com (enklast)
- GitHub Pages (Hugo/Jekyll - gratis)
- WordPress (mer flexibilitet)

**Vad skriva:**
- HackTheBox writeups (retired boxes)
- TryHackMe room writeups
- Tutorial guides
- Tool reviews
- Conference notes
- "What I learned this week"

**Exempel posts:**
- "How I Rooted My First HackTheBox Machine"
- "OSCP Journey: Lessons Learned"
- "Top 5 Nmap Techniques for Pentesting"
- "Building a Custom Python Port Scanner"

**Tips:**
- Skriv regelbundet (monthly minimum)
- SEO-friendly titles
- Include screenshots/code
- Dela på social media

#### 3. Bug Bounty Profiles

**Platforms:**
- HackerOne
- Bugcrowd
- Intigriti (EU-fokus)
- YesWeHack (EU)

**Även om du inte hittar bugs:**
- Visar du testat på riktiga systems
- Lär real-world web apps
- Potentiell income

**Tips:**
- Börja med VDP (Vulnerability Disclosure Programs) - no payout but learning
- Dokumentera process även för duplicates
- Skriv bra reports (practice)

#### 4. Certifications

**Visa dem:**
- LinkedIn profile
- CV
- Personal website
- Digital badges (Credly, Accredible)

#### 5. Video Content (Optional, Advanced)

**YouTube/TwITCH:**
- Live hacking sessions
- Tutorial videos
- Explain complex concepts

**Fördelar:**
- Builds personal brand
- Demonstrerar kommunikationsförmåga
- Can lead to opportunities

### Portfolio Do's and Don'ts

**DO:**
- ✅ Be consistent (regular updates)
- ✅ Quality over quantity
- ✅ Show process, not just results
- ✅ Explain what you learned
- ✅ Include failures (learning moments)
- ✅ Make it easy to navigate

**DON'T:**
- ❌ Plagiarize others' writeups
- ❌ Post active HTB/THM solutions
- ❌ Share credentials eller sensitive data
- ❌ Over-complicate (keep it simple)
- ❌ Abandon it (outdated portfolio = red flag)

---

## 💼 Jobbsökning och Intervjuer {#jobbsokning}

### När är Du Redo?

**Junior Penetration Tester:**
- [ ] OSCP eller eJPT certification
- [ ] 30+ HackTheBox boxes (documented)
- [ ] GitHub portfolio med tools
- [ ] Blog med writeups
- [ ] Grundläggande networking kunskap
- [ ] Strong report writing skills

**Du behöver INTE:**
- ❌ Kunna allt
- ❌ 10 års erfarenhet för "junior" roll
- ❌ Alla certifikationer

**"Fake it till you make it"? NO - Men "Learn it while you earn it"? YES!**

### Var Hitta Jobb

#### Sverige

**Jobbsajter:**
- LinkedIn (bästa för cybersecurity)
- Blocket Jobb
- Indeed
- Glassdoor
- Arbetsförmedlingen

**Cybersecurity-specifika:**
- Infosec-jobs.com
- CyberSecJobs.com

**Rekryteringsföretag (Sverige):**
- Academic Work (ofta junior roller)
- Nexer Recruit
- Jefferson Wells
- Randstad

**Direkta Företag:**
- Konsultföretag: Truesec, Sentor, Tietoevry, CGI, Deloitte
- Interna SOC: Banker (SEB, Swedbank), Telcos (Telia, Tele2)
- Produktbolag: Spotify, Klarna, King

#### Internationellt (Remote)

**Platforms:**
- WeWorkRemotely
- Remote.co
- AngelList (startups)

### CV Tips

**Struktur:**

```
1. CONTACT INFO & SUMMARY
   ├─ Name, Email, Phone, LinkedIn, GitHub
   └─ 2-3 sentence pitch

2. CERTIFICATIONS (top of CV!)
   ├─ OSCP - 2024
   ├─ eJPT - 2023
   └─ Security+ - 2023

3. SKILLS
   ├─ Technical: Linux, Nmap, Metasploit, Burp Suite, Python
   ├─ Certifications: (repeat)
   └─ Languages: Swedish (native), English (fluent)

4. PROJECTS / PORTFOLIO
   ├─ GitHub: github.com/yourname (link)
   ├─ Blog: yourblog.com (link)
   ├─ HackTheBox: Profile link (show ranking)
   └─ Bug Bounty: Profile link

5. EXPERIENCE
   ├─ Even non-security jobs (show transferable skills)
   └─ Internships, freelance, volunteer

6. EDUCATION
   └─ University, relevant courses
```

**Tips:**
- **1 sida för junior** (max 2 för senior)
- Quantify resultat ("Rooted 40+ HTB machines")
- Use action verbs (Discovered, Exploited, Reported)
- Tailor för varje jobb
- Include keywords från job description

### Cover Letter

**Struktur (kort!):**

```
Paragraph 1: Varför detta företag
Paragraph 2: Varför du passar (skills, passion)
Paragraph 3: Call to action

Keep it under 250 words!
```

### Intervjuförberedelse

#### Tekniska Intervjuer

**Vanliga Frågor:**

1. **"Walk me through how you'd test a web application."**

   **Svar:**
   - Reconnaissance (subdomains, tech stack)
   - Content discovery (dirs, files)
   - Vulnerability testing (OWASP Top 10)
   - Authentication testing
   - Authorization testing
   - Reporting

2. **"Explain how you'd exploit an SQL injection."**

   **Svar:** (visa process)
   - Identify injection point
   - Determine database type
   - Extract data (UNION-based, Error-based, Boolean-based)
   - Escalate (file read, OS command execution)

3. **"What's the difference between a vulnerability and an exploit?"**

4. **"Explain the CIA triad."**

5. **"How does NTLM authentication work?"**

**Praktiska Tester:**
- Kan få live pentest en webb app
- Analysera nmap output
- Skriva basic Python script
- Förklara terminal kommandon

#### Behavioral Intervjuer

**STAR Method (Situation, Task, Action, Result):**

**Exempel Fråga:** "Tell me about a time you faced a difficult challenge."

**Svar:**
- **Situation:** "During my OSCP preparation, I struggled with a privilege escalation challenge for 3 days."
- **Task:** "I needed to get root access to continue."
- **Action:** "I went back to basics, ran LinPEAS again, researched the specific kernel version, found a CVE, and compiled the exploit."
- **Result:** "Successfully got root, learned the importance of thorough enumeration, and documented the process for my blog."

**Andra Frågor:**
- Why cybersecurity?
- Why this company?
- Where do you see yourself in 5 years?
- How do you keep up with security news?
- Describe a time you failed.

### Salary Negotiation

**Tips:**
1. Research beforehand (Glassdoor, levels.fyi för Sverige data)
2. Let them give first number (if possible)
3. Negotiate hela paketet (lön, benefits, remote, training budget)
4. Don't accept first offer immediately
5. Be prepared to walk away

**"What's your salary expectation?"**

**Svar:** "Based on my research and the value I bring, I'm looking for something in the range of X to Y SEK. However, I'm open to discussing the complete package."

---

## 💰 Löneutveckling {#loneutveckling}

### Sverige Lönestatistik (2024-2025)

| Roll | Entry (0-2y) | Mid (2-5y) | Senior (5-10y) | Expert (10y+) |
|------|--------------|------------|----------------|---------------|
| **Penetration Tester** | 35-45k | 50-65k | 70-85k | 90-110k |
| **SOC Analyst** | 30-40k | 45-60k | 65-80k | 80-95k |
| **Security Consultant** | 40-50k | 55-70k | 75-90k | 95-120k |
| **Security Architect** | - | 60-75k | 80-100k | 100-130k |
| **CISO** | - | - | 90-120k | 120-180k |

**OBS:** Stockholm löner generellt 10-20% högre än resten av Sverige.

### Faktorer Som Påverkar Lön

**Positiva:**
- ✅ Certifikationer (OSCP +10-15k)
- ✅ Erfarenhet (real-world, not just labs)
- ✅ Specialisering (Cloud, OT, AppSec)
- ✅ Stockholm/Göteborg location
- ✅ Konsultföretag (ofta högre än interna roller)
- ✅ Programmeringsfärdigheter (Python, Go)

**Neutrala/Negativa:**
- ❌ Endast teoretiska certifikationer (CEH utan praktik)
- ❌ Gaps i CV
- ❌ Brist på soft skills
- ❌ Mindre städer

### Karriärprogression Exempel

**År 0 (Learning):**
- Student/självstudier
- Lön: 0 SEK (investering i utbildning)

**År 1 (Junior Pentester):**
- OSCP certified
- 30+ HTB boxes
- Lön: 38,000 SEK/mån

**År 2-3 (Pentester):**
- Real-world experience
- Additional cert (OSWE or CRTO)
- Lön: 55,000 SEK/mån

**År 4-6 (Senior Pentester):**
- Leading small projects
- Mentoring juniors
- Lön: 75,000 SEK/mån

**År 7-10 (Red Team Lead):**
- Leading operations
- Strategy and planning
- Lön: 95,000 SEK/mån

**År 10+ (CISO/Security Director):**
- Management role
- Business alignment
- Lön: 130,000+ SEK/mån

### Öka Din Lön

**Strategier:**

1. **Certifications:**
   - OSCP = +10-15k
   - OSEP/OSWE = +15-20k
   - CISSP (management) = +10-15k

2. **Job Hopping:**
   - Oftast snabbaste sättet att öka lön
   - Var 2-3 år för max increase
   - Men byggnot reputation också

3. **Specialisering:**
   - Cloud security (AWS, Azure)
   - OT/ICS security (kritisk infrastruktur)
   - Red team operations

4. **Management Track:**
   - Lead roles betalar mer
   - Men mindre hands-on

5. **Freelance/Consulting:**
   - Potential för högre timtaxa
   - Men mindre stabilitet

---

## 🔄 Fortsatt Utveckling {#fortsatt-utveckling}

### Håll Dig Uppdaterad

**Dagligen:**
- [ ] Security news (TheHackerNews, BleepingComputer)
- [ ] Twitter feed
- [ ] Reddit r/netsec

**Veckovis:**
- [ ] Podcast (Darknet Diaries, Risky Business)
- [ ] YouTube (IppSec, John Hammond)
- [ ] Blog posts från experts

**Månadsvis:**
- [ ] CTF participation
- [ ] HTB/THM new boxes
- [ ] Read security whitepapers

**Årligen:**
- [ ] Attend conference (SEC-T, BSides)
- [ ] Renew certifications
- [ ] New certification
- [ ] Review och uppdatera skills

### Specialiseringar att Utforska

**Efter du bemästrar grunderna:**

#### Cloud Security
- AWS, Azure, GCP pentesting
- Kubernetes security
- Serverless security
- Cloud misconfigurations

**Resources:**
- "Hacking the Cloud" (bok)
- RhinoSecurityLabs tools (Pacu, CloudGoat)

#### Mobile Security
- iOS/Android pentesting
- Mobile app reverse engineering
- Frida, objection tools

**Resources:**
- OWASP MSTG
- Mobile Security Framework (MobSF)

#### Active Directory / Red Teaming
- Advanced AD attacks
- Bloodhound, Mimikatz mastery
- C2 framework operations
- OPSEC och evasion

**Resources:**
- "Attacking Active Directory" posts
- CRTO certification

#### Exploit Development
- Buffer overflows
- Return-oriented programming
- Heap exploitation
- Browser exploitation

**Resources:**
- OSEE certification
- Corelan tutorials
- LiveOverflow videos

### Ge Tillbaka till Community

**När du blir erfaren:**

- 🎓 **Mentor juniors** (Discord, Twitter DMs)
- 📝 **Skriv tutorials** (blog, Medium)
- 🛠️ **Contribute open-source** (GitHub)
- 🎤 **Speak at conferences** (BSides, lokala meetups)
- 📺 **Create content** (YouTube, Twitch)

---

## 🏆 Success Metrics

### Track Din Progress

**Use a Notion/Trello board:**

```
TODO:
├─ Complete OSCP PWK labs
├─ Root 10 more HTB boxes
└─ Publish 2 blog posts this month

IN PROGRESS:
├─ OSCP exam prep (week 3/12)
└─ HTB "Heist" machine

DONE:
├─ ✅ Completed Nivå 0-5 av denna guide
├─ ✅ Rooted 30 HTB boxes
├─ ✅ Published 5 blog posts
└─ ✅ eJPT certified
```

### Celebrate Wins!

- 🎉 First HTB box rooted
- 🎉 First blog post published
- 🎉 First certification
- 🎉 First job application sent
- 🎉 First job interview
- 🎉 First job offer
- 🎉 OSCP PASSED!

---

## 📝 Final Tips

```
💡 "The best time to start was yesterday.
    The second best time is now."

1. Be patient - Cybersecurity är en resa, inte ett mål
2. Stay curious - Fråga alltid "hur fungerar detta?"
3. Document everything - Ditt framtida jag tackar dig
4. Network actively - Jobb kommer ofta från connections
5. Never stop learning - Teknologi förändras ständigt
6. Teach others - Bästa sättet att lära är att undervisa
7. Stay ethical - Reputation tar år att bygga, sekunder att förstöra
8. Have fun! - Om du inte tycker det är roligt, varför då?
```

---

[🏠 Tillbaka till huvudguiden](../KALI_LINUX_GUIDE_2025.md)

---

**📅 Senast uppdaterad:** 2025-01-18
**✍️ Författare:** Victory Redovisning Kali Linux Guide Project
**📄 Licens:** Endast för utbildningsändamål

---

**🚀 "Your cybersecurity journey starts now. Try Harder. You got this!"**
