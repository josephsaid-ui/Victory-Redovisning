# 🎈 Nivå 1: Grunderna - Som en 5-åring Förstår Det

> **"Varje expert var en gång en nybörjare"**
>
> 📚 Läsningstid: 15-20 min | 🎯 Övningar: 3 | 💡 Svårighetsgrad: Nybörjare

---

## 🗺️ Navigation
**[⬅️ Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 2](OSINT_ZAP_Guide_Niva_2.md)**

---

## 🎯 Vad du lär dig i denna nivå

Efter att ha läst Nivå 1 kommer du att:
- ✅ Förstå vad OSINT är med hjälp av vardagliga analogier
- ✅ Veta vad säkerhetstestning innebär och varför det är viktigt
- ✅ Känna till grundläggande etik och ansvar
- ✅ Kunna hitta öppen information om dig själv online
- ✅ Förstå skillnaden mellan OSINT och "hacking"

---

## 🔍 Del 1: Vad är OSINT?

### Förklarat som för en 5-åring

Tänk dig att du är en **detektiv** 🕵️ som ska lösa ett mysterium. Men istället för att bryta dig in i hus eller sno hemliga dokument, samlar du ledtrådar från saker som alla kan se!

**OSINT** står för **O**pen **S**ource **Int**elligence (Öppen Underrättelseinhämtning på svenska).

Det betyder: **Information som ALLA kan hitta, men som kräver skicklighet att samla och förstå.**

### 🎪 Analogi 1: Skattjakten

Föreställ dig en skattjakt i parken:

```
🏞️ PARKEN = INTERNET
│
├─ 🪧 Skyltar med ledtrådar = Publika webbplatser
├─ 📰 Tidningar på bänkar = Nyhetsartiklar
├─ 👥 Människor som pratar = Sociala medier
├─ 📍 Kartor på väggar = Google Maps
└─ 🗑️ Papperskorgar = Dataläckor och gamla databaser
```

En duktig skattjägare:
- ✅ Läser alla skyltar noggrant
- ✅ Lyssnar på vad folk säger
- ✅ Tittar på kartor för att hitta platser
- ✅ Kombinerar ledtrådar för att hitta skatten

En OSINT-expert gör **exakt samma sak** - men på internet! 🌐

### 🕵️ Analogi 2: Pusselbitarna

OSINT är som att lägga ett stort pussel:

```
INFORMATION DU HITTAR:
┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
│ Foto │  │ Namn │  │Arbete│  │Email │
│ på   │  │ från │  │ från │  │ från │
│Insta │  │FB    │  │Linkd │  │webb  │
└───┬──┘  └───┬──┘  └───┬──┘  └───┬──┘
    │         │         │         │
    └─────────┴─────────┴─────────┘
                  │
         ┌────────▼─────────┐
         │  KOMPLETT BILD   │
         │  av en person    │
         │  eller företag   │
         └──────────────────┘
```

Varje pusselbit är **öppen information**. När du kombinerar dem får du en **komplett bild**!

### 📚 Var finns öppen information?

**Öppen information finns överallt:**

🌐 **Internet:**
- Webbplatser och bloggar
- Sociala medier (Facebook, LinkedIn, Twitter, Instagram)
- Företagsregister (Bolagsverket, allabolag.se)
- Google Maps och Street View
- YouTube-videos
- Forum och communities (Reddit, Flashback)

📄 **Offentliga Register:**
- Folkbokföringen (personnummer etc. - begränsad åtkomst!)
- Bolagsverket (företagsinfo)
- Ratsit, Hitta.se (adresser, telefon)
- Domänregistreringar (WHOIS)

📰 **Nyheter och Media:**
- Tidningsartiklar
- Pressmeddelanden
- TV-nyheter
- Podcasts

🗂️ **Metadata:**
- EXIF-data i bilder (GPS-koordinater, kameramodell, datum)
- PDF-dokument (författare, skapad med vilket program)
- Webbplatsers teknisk stack

### ❓ Varför är OSINT viktigt?

OSINT används av:

👮 **Polis och brottsbekämpning** - Hitta brottslingar
🛡️ **Säkerhetsföretag** - Skydda mot hot
💼 **Företag** - Konkurrensbevaka och rekrytering
📰 **Journalister** - Investigativ journalism (ex. Bellingcat)
🔐 **Penetrationstestare** - Första fasen i säkerhetstest
🕵️ **Privatpersoner** - Kontrollera sin digitala fotavtryck

### ⚖️ OSINT vs "Hacking" - Viktiga Skillnader

```
OSINT (LAGLIGT ✅)              vs    HACKING (OFTA OLAGLIGT ❌)
════════════════════════════════════════════════════════════════
• Använder ÖPPEN information          • Bryter sig in i system
• Allt är publikt tillgängligt        • Tar sig förbi säkerhet
• Kräver INGEN tillgång till system   • Kräver exploits/verktyg
• Som att läsa tidningen              • Som att bryta sig in i hus
• 100% lagligt (med viss etik)        • Olagligt utan tillstånd

EXEMPEL:
✅ Googla på någons namn               ❌ Hacka någons email
✅ Läsa företags webbplats             ❌ Bryta sig in i deras databas
✅ Kolla public GitHub-repos           ❌ Stjäla källkod från privat repo
✅ Se public Instagram-bilder          ❌ Bryta sig in i privat Instagram
════════════════════════════════════════════════════════════════
```

**VIKTIGT:** Även om OSINT är lagligt, finns det etiska gränser!
- ❌ Stalka eller trakassera personer
- ❌ Sprida privat information (doxxing)
- ❌ Använda info för bedrägeri eller utpressning

---

## 🛡️ Del 2: Vad är Säkerhetstestning och OWASP ZAP?

### Förklarat som för en 5-åring

Tänk dig att du har byggt ett **stort slott av LEGO** 🏰

Innan du visar det för alla, vill du kolla att:
- Väggarna inte faller ner 🧱
- Ingen kan smyga in genom hemliga vägar 🚪
- Skattkammaren är säker 💎
- Bron håller när folk går över den 🌉

**Säkerhetstestning** är när du testar om ditt "digitala slott" (webbplats/app) är säkert!

**OWASP ZAP** är ditt **testverktyg** - som en magisk lupp 🔍 som hittar sprickor i väggen innan de elaka draken hittar dem! 🐉

### 🔧 Analogi: Låssmedens Arbete

```
LÅSSMED (Säkerhetstestare)
═══════════════════════════════════════════════════════════

1. KUNDEN ANSTÄLLER LÅSSMEDEN
   "Testa om någon kan bryta sig in i mitt hus!"
   └─→ Företaget anställer dig för att testa deras webbplats

2. LÅSSMEDEN TESTAR ALLA DÖ RRAR OCH FÖNSTER
   🚪 Huvuddörr (login-sida)
   🪟 Fönster (formulär, input-fält)
   🚪 Bakdörr (admin-panel)
   🔓 Lås (autentisering)
   └─→ ZAP testar alla delar av webbplatsen

3. LÅSSMEDEN HITTAR PROBLEM
   "Din bakdörr är olåst!"
   "Fönstret i köket kan öppnas utifrån!"
   └─→ ZAP rapporterar sårbarheter

4. KUNDEN FIXAR PROBLEMEN
   Byter lås, förstärker fönster
   └─→ Utvecklarna fixar sårbarheterna

5. HUSET ÄR NU SÄKRARE! 🎉
   └─→ Webbplatsen är säkrare!
```

**Viktigt:** Låssmeden har **TILLSTÅND** att testa! Samma sak gäller för dig - testa bara det du har lov att testa!

### 🎨 Vad är OWASP ZAP?

**OWASP ZAP** = **O**pen **W**eb **A**pplication **S**ecurity **P**roject **Z**ed **A**ttack **P**roxy

Enklare förklarat:
- 🆓 **Gratis** verktyg (open source)
- 🕷️ **Spider** - Kryper genom webbplatser och kartlägger dem
- 🔍 **Scanner** - Letar efter säkerhetshål
- 🕵️ **Proxy** - Låter dig se och ändra trafik mellan webbläsare och server
- 📊 **Rapporter** - Visar vad som är fel och hur man fixar det

**ZAP är som:**
- En säkerhets-robot som testar din webbplats 🤖
- En röntgen-maskin för webbapplikationer 🔬
- Din personliga säkerhetsassistent 🛡️

### 🎯 Vad testar ZAP för?

De vanligaste säkerhetshålen (mer om detta i Nivå 3-4):

```
VANLIGA SÅRBARHETER
═══════════════════════════════════════════════════════════

🚨 SQL Injection (SQLi)
   Angripare kan komma åt din databas
   Exempel: Stjäla alla användarlösenord

🚨 Cross-Site Scripting (XSS)
   Angripare kan köra skadlig kod i andras webbläsare
   Exempel: Stjäla session cookies

🚨 Broken Authentication
   Dålig inloggning/autentisering
   Exempel: Svaga lösenordskrav, ingen rate-limiting

🚨 Sensitive Data Exposure
   Känslig data läcker ut
   Exempel: Kreditkortsnummer i klartext

🚨 Security Misconfiguration
   Servern är felkonfigurerad
   Exempel: Default-lösenord, öppna portar
```

---

## 🔐 Del 3: Etik och Ansvar (SUPERVIKTIGT!)

### Guldreglerna för OSINT och Säkerhetstestning

```
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║         10 GULDREGLER DU MÅSTE FÖLJA                     ║
║                                                          ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  1️⃣  Få ALLTID tillstånd innan du testar system          ║
║     (Skriftligt om möjligt!)                            ║
║                                                          ║
║  2️⃣  Testa ENDAST:                                       ║
║     • Dina egna system                                  ║
║     • Test-miljöer (DVWA, WebGoat, Juice Shop)         ║
║     • Bug bounty-program med scope                     ║
║                                                          ║
║  3️⃣  Använd INTE OSINT för:                              ║
║     • Stalking eller trakasserier                       ║
║     • Doxxing (sprida privatinfo)                       ║
║     • Bedrägeri eller utpressning                       ║
║                                                          ║
║  4️⃣  Rapportera sårbarheter ANSVARSFULLT                 ║
║     • Kontakta företaget privat först                   ║
║     • Ge tid att fixa (90 dagar standard)              ║
║     • Publicera INTE sårbarheter direkt                 ║
║                                                          ║
║  5️⃣  Respektera privatlivet                              ║
║     • Bara för att info är publik = inte OK att dela   ║
║     • Tänk på konsekvenser                              ║
║                                                          ║
║  6️⃣  Följ lagar (även om du TEKNISKT kan göra något)     ║
║     • Dataintrång = upp till 2 års fängelse i Sverige  ║
║     • GDPR-brott = stora böter                          ║
║                                                          ║
║  7️⃣  Använd VPN och anonymisering FÖRSIKTIGT             ║
║     • VPN för att skydda DIG, inte för att dölja brott ║
║     • TOR för legitima ändamål                          ║
║                                                          ║
║  8️⃣  Dokumentera ALLT                                    ║
║     • Timestamp, screenshots, logs                      ║
║     • Kan bevisa du inte gjort något olagligt           ║
║                                                          ║
║  9️⃣  Lär dig KONTINUERLIGT                               ║
║     • Säkerhet förändras snabbt                         ║
║     • Håll dig uppdaterad                               ║
║                                                          ║
║  🔟  Använd kunskap för GOTT                             ║
║     • Gör internet säkrare                              ║
║     • Hjälp företag förbättra säkerhet                  ║
║     • Dela kunskap (ansvarsfull)                        ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

### 🇸🇪 Svensk Lag - Vad du MÅSTE veta

**Brottsbalken Kapitel 4 § 9c - Dataintrång:**

> "Den som olovligen bereder sig tillgång till uppgift för automatisk databehandling eller olovligen ändrar, utplånar, blockerar eller i register för in sådan uppgift döms för dataintrång till böter eller fängelse i högst två år."

**Vad betyder det?**
- ❌ Testa INTE system utan tillstånd
- ❌ Ändra INTE data utan tillstånd
- ❌ Logga INTE in med annans uppgifter
- ✅ Få skriftligt OK innan du testar

**GDPR (Dataskyddsförordningen):**
- Persondata ska behandlas lagligt och korrekt
- Du får inte samla mer info än nödvändigt
- Respektera rätten att bli glömd

---

## 🎯 Övningar - Nivå 1

Nu är det dags att testa dina kunskaper! 🚀

### Övning 1.1: Hitta Information om Dig Själv 🔍

**Mål:** Förstå hur mycket öppen information som finns om dig.

**Steg:**
1. **Google dig själv:**
   ```
   Sök: "Ditt Förnamn Efternamn"
   Sök: "Ditt Förnamn Efternamn" + stad
   Sök: "Ditt email"
   Sök: "Ditt telefonnummer"
   ```

2. **Kolla publika register:**
   - Hitta.se
   - Ratsit.se (Obs: viss info kräver inloggning)
   - LinkedIn

3. **Reverse image search:**
   - Ta en bild från ditt sociala media
   - Ladda upp på https://images.google.com/
   - Se var den dyker upp!

4. **Email-check:**
   - Gå till https://haveibeenpwned.com/
   - Kolla om din email finns i dataläckor

**Dokumentera:**
```
MIN DIGITALA FOTAVTRYCK
═══════════════════════════════════════════
Vad hittade jag om mig själv?

Google:
- [ ] Mitt namn syns på: ___________________
- [ ] Bilder på mig: ______________________
- [ ] Adress synlig: Ja / Nej
- [ ] Telefon synlig: Ja / Nej

Sociala Medier:
- [ ] Facebook: Publik / Privat / Ingen profil
- [ ] LinkedIn: Publik / Privat / Ingen profil
- [ ] Instagram: Publik / Privat / Ingen profil
- [ ] Twitter/X: Publik / Privat / Ingen profil

Dataläckor:
- [ ] Email i HIBP: Ja / Nej
- [ ] Vilka breaches: _____________________

REFLEKTION:
Var jag överraskad över något?
___________________________________________
___________________________________________

Vad vill jag ändra?
___________________________________________
___________________________________________
```

**Facit/Insikter:**
- De flesta hittar MER information än de trodde
- Gammal info kan finnas kvar länge (Wayback Machine!)
- Metadata i bilder kan avslöja plats och tid
- Dataläckor påverkar nästan alla

**Bonus:**
- Ändra privacy-inställningar på sociala medier
- Radera gamla konton du inte använder
- Använd unika lösenord (passwordmanager!)

---

### Övning 1.2: Grundläggande Google-sökning med Operatorer 🔎

**Mål:** Lära sig hitta specifik information effektivt.

**Google Search Operators (Grundläggande):**

```
OPERATOR         BESKRIVNING                EXEMPEL
═══════════════════════════════════════════════════════════════
"exacta ord"     Exakt fras                "säkerhetstestning"

site:            Sök på specifik site      site:github.com password

filetype:        Specifik filtyp           filetype:pdf säkerhet

-                Uteslut ord               säkerhet -kamera

OR               Antingen eller            hacking OR pentesting

*                Wildcard                  "best * for hacking"

..               Nummerintervall           laptop 5000..10000 kr
```

**Uppgifter:**

1. **Hitta PDF-dokument om cybersäkerhet:**
   ```
   Sök: filetype:pdf cybersäkerhet
   ```
   Antal resultat: _______

2. **Hitta information på en specifik webbplats:**
   ```
   Sök: site:reddit.com OSINT
   ```
   Hitta 3 intressanta trådar: ________________

3. **Exakt frassökning:**
   ```
   Sök: "penetration testing guide"
   ```
   Första relevanta resultat: ________________

4. **Kombinera operatorer:**
   ```
   Sök: site:github.com filetype:md OSINT
   ```
   Hittar du några bra OSINT-guider? ________________

5. **Uteslut oönskat:**
   ```
   Sök: OWASP ZAP tutorial -burp
   ```
   (Hittar ZAP-tutorials utan att få Burp Suite-resultat)

**Facit:**
Du borde hitta:
- Tusentals PDFs om cybersäkerhet
- Reddit har aktiva OSINT-communities
- Många bra GitHub-repos med OSINT-verktyg
- ZAP har officiella tutorials på owasp.org

**Bonus:**
Testa dessa avancerade sökningar:
```
intitle:"index of" password.txt
inurl:admin login
cache:example.com  (Googles cachade version)
```

⚠️ **VARNING:** Sök INTE efter känslig info för att exploatera den! Detta är för LÄRANDE.

---

### Övning 1.3: Identifiera Publika vs Privata Data 🔐

**Mål:** Förstå skillnaden mellan vad som ÄR öppet och vad som KÄNNS öppet.

**Scenario:** Utvärdera följande situationer - är det OSINT (lagligt) eller intrång?

```
SITUATION                                          OSINT?  INTRÅNG?
═══════════════════════════════════════════════════════════════════
1. Läsa någons publika tweets                      ✅      ❌

2. Googla på ett företagsnamn                      ✅      ❌

3. Använda Shodan för att hitta öppna             ✅      ❌
   webcams (publika utan lösen)

4. Gissa lösenord för att logga in                ❌      ✅
   på någons email

5. Läsa offentliga företagsdokument               ✅      ❌
   på Bolagsverket

6. Scrapa LinkedIn för emails                     ⚠️      ⚠️
   (gråzon - bryter mot ToS!)

7. Läsa kod på publikt GitHub-repo                ✅      ❌

8. Klona privat GitHub-repo med läckt key         ❌      ✅

9. Använda Wayback Machine för att se             ✅      ❌
   gammal version av webbplats

10. Exploatera SQL injection du hittade           ❌      ✅
    för att dumpa databas

11. Läsa EXIF-data från publik bild               ✅      ❌

12. Phisha någon för att få deras lösen           ❌      ✅

13. Använda theHarvester på egen domän            ✅      ❌

14. Använda theHarvester på andras domän          ✅      ❌
    (för publik info!)

15. Använda ZAP på din egen webbplats             ✅      ❌

16. Använda ZAP på andras webbplats               ❌      ✅
    utan tillstånd

17. Rapportera sårbarhet du hittat                ✅      ❌
    (responsible disclosure)

18. Sälja sårbarhet till högstbjudande            ❌      ⚠️
    utan att rapportera till företag              (oetiskt!)

19. Gå med i bug bounty-program och testa         ✅      ❌
    enligt deras scope

20. Testa utanför bug bounty scope                ❌      ✅
```

**Facit:**
- ✅ OSINT = 11 situationer är OK
- ❌ INTRÅNG = 7 situationer är INTE OK
- ⚠️ GRÅZON = 2 situationer är komplicerade

**Nyckeln:**
```
╔══════════════════════════════════════════════════════╗
║  ÄR DET OSINT?                                       ║
║  ───────────────────────────────────────────────────║
║  ✅ JA om:                                           ║
║     • Informationen är PUBLIKT tillgänglig          ║
║     • Du inte behöver bryta dig förbi säkerhet     ║
║     • Du inte gissar lösenord                       ║
║     • Du inte exploaterar sårbarheter               ║
║                                                      ║
║  ❌ NEJ om:                                          ║
║     • Du behöver logga in med andras uppgifter     ║
║     • Du gissar/bruteforcar lösenord                ║
║     • Du exploaterar säkerhetsbrister               ║
║     • Du kringgår autentisering                     ║
╚══════════════════════════════════════════════════════╝
```

---

## 🎓 Sammanfattning Nivå 1

### Vad du har lärt dig:

✅ **OSINT** = Samla öppen information (som en detektiv!)
✅ **Säkerhetstestning** = Testa system för brister (som en låssmed!)
✅ **OWASP ZAP** = Gratis verktyg för att hitta säkerhetsbrister
✅ **Etik** = Få ALLTID tillstånd, använd kunskap för gott
✅ **Lagar** = Dataintrång är OLAGLIGT, respektera GDPR
✅ **Google Dorking** = Kraftfulla sökoperatorer
✅ **Din digitala fotavtryck** = Mer synlig än du tror!

### Nästa Steg:

🎯 **Om du känner dig bekväm:**
→ Gå vidare till **[Nivå 2: Grundläggande Verktyg](OSINT_ZAP_Guide_Niva_2.md)**

🔄 **Om du vill öva mer:**
→ Repetera övningarna
→ Googla på fler personer/företag (etiskt!)
→ Utforska haveibeenpwned.com

📚 **Extra läsning:**
→ OWASP ZAP Getting Started: https://www.zaproxy.org/getting-started/
→ OSINT Framework: https://osintframework.com/ (förhandsvisning)

---

## 🤔 Reflektionsfrågor

Innan du går vidare, fundera över:

1. **Vad är skillnaden mellan OSINT och hacking?**
   <details>
   <summary>Svar</summary>
   OSINT använder ÖPPEN information som alla kan se. Hacking bryter sig in i system och tar sig förbi säkerhet.
   </details>

2. **Varför måste jag ha tillstånd för att säkerhetstesta?**
   <details>
   <summary>Svar</summary>
   För att det annars räknas som dataintrång och är OLAGLIGT! Samma som att en låssmed måste ha tillstånd att testa lås.
   </details>

3. **Är all öppen information OK att dela vidare?**
   <details>
   <summary>Svar</summary>
   NEJ! Även om något är publikt betyder det inte att det är etiskt eller lagligt att sprida det. Tänk på GDPR och privatlivet.
   </details>

4. **Vad gör jag om jag hittar en sårbarhet på en webbplats?**
   <details>
   <summary>Svar</summary>
   Rapportera ANSVARSFULLT! Kontakta företaget privat, ge dem tid att fixa (90 dagar standard), exploatera INTE sårbarheten.
   </details>

---

## 🎉 Grattis!

Du har nu klarat Nivå 1! 🎈

Du förstår nu grunderna i OSINT och säkerhetstestning. Det här är fundamentet som allt annat bygger på.

**Kom ihåg:**
- 🛡️ Etik först - alltid!
- 📚 Övning ger färdighet
- 🤝 Community - fråga när du fastnar
- 🚀 Ha kul och lär dig!

---

**Redo för nästa nivå?**

👉 **[Fortsätt till Nivå 2: Grundläggande Verktyg →](OSINT_ZAP_Guide_Niva_2.md)**

Där lär du dig:
- Google Dorking på djupet
- WHOIS och domänundersökningar
- Installera och köra OWASP ZAP
- Skanna din första webbapplikation!

---

**[⬅️ Tillbaka till Översikt](OSINT_ZAP_Guide_README.md)** | **[➡️ Nästa: Nivå 2](OSINT_ZAP_Guide_Niva_2.md)**

---

**Nivå 1 Komplett! ✅**
*Fortsätt till Nivå 2 när du känner dig redo!*
