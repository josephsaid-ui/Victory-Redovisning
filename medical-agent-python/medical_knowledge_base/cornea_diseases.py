"""
Hornhinne Sjukdomar - 30 vanligaste
"""

CORNEA_DISEASES = [
    {
        "name": "Bakteriell Keratit",
        "name_en": "Bacterial Keratitis",
        "icd10": "H16.0",
        "symptoms": [
            "kraftig ögonsmärta",
            "rodnad",
            "ljuskänslighet (fotophobi)",
            "tårrinnande",
            "synnedsättning",
            "purulent flytning",
            "snabb försämring"
        ],
        "anamnesis_questions": [
            "Använder du kontaktlinser?",
            "Sov du med linserna på?",
            "Har du skadat hornhinnan (repa, främmande kropp)?",
            "Använder du kortikosteroidögondroppar?",
            "Har du torrt öga?",
            "När började symptomen?",
            "Försämras det snabbt?"
        ],
        "clinical_signs": [
            "korneal infiltrat (vitt, suppurativt)",
            "epitheldefekt",
            "stromal abscess",
            "hypopyon (pus i främre kammaren)",
            "konjunktival injektion",
            "framåtskridande infiltrat",
            "bakterier: Pseudomonas (gröna), Staphylococcus, Streptococcus"
        ],
        "risk_factors": [
            "kontaktlinsbärare (största riskfaktorn!)",
            "sovande med linser",
            "dålig lenshygien",
            "korneal trauma/erosion",
            "torrt öga",
            "steroidbehandling",
            "ögonyteoperation",
            "immunsuppression"
        ],
        "treatment": "AKUT! Kornealskrap för odling, bred-spektrum antibiotika-droppar omedelbart (fluorokinolon eller fortifierade droppar), intensiv dosering (varje timme initialt, dygnet runt), Pseudomonas: ciprofloxacin eller tobramycin + ceftazidim, Gram-positiva: vancomycin eller cefazolin, undvik steroider initialt, dagliga kontroller, eventuell korneatransplantation vid perforation",
        "kva": "AKC00",  # Hornhinneskrap
        "differential_diagnoses": [
            "Viral keratit (herpes)",
            "Fungal keratit",
            "Akantamoeba keratit",
            "Steril korneal infiltrat"
        ],
        "description": "Bakteriell keratit är en oftalmologisk nödsituation med risk för permanent synförlust och perforation. Vanligast hos kontaktlinsbärare. Pseudomonas är aggressivast. Kräver akut behandling med intensiva antibiotika-droppar.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Herpes Simplex Keratit (Dendritisk Keratit)",
        "name_en": "Herpes Simplex Keratitis",
        "icd10": "B00.5",
        "symptoms": [
            "ögonsmärta (mindre än bakteriell)",
            "ljuskänslighet",
            "tårrinnande",
            "rodnad",
            "synnedsättning",
            "känsla av främmande kropp",
            "ofta recidiverande"
        ],
        "anamnesis_questions": [
            "Har du haft detta tidigare?",
            "Har du haft munsår (herpes labialis)?",
            "Har du känt dig sjuk eller stressad nyligen?",
            "Använder du kortikosteroidögondroppar?",
            "Har du haft feber eller förkylning?"
        ],
        "clinical_signs": [
            "dendritisk (grenliknande) epitheldefekt med terminala bulber",
            "fluorescein-positiv",
            "nedsatt korneal sensibilitet",
            "eventuell geografisk ulceration vid större defekt",
            "stromal keratit vid djupare infektion",
            "disciform keratit (endotelit)"
        ],
        "risk_factors": [
            "tidigare HSV-infektion",
            "immunsuppression",
            "steroidbehandling (kan reaktivera och förvärra)",
            "UV-exponering",
            "stress",
            "feber",
            "trauma"
        ],
        "treatment": "Antiviral behandling: aciklovir-salva 5x dagligen eller ganciklovir-gel 5x dagligen, fortsätt 3 dagar efter läkning, debridering av dendrit kan påskynda läkning, UNDVIK STEROIDER vid epithelial sjukdom! (förvärrar), steroider endast vid stromal/endotelial sjukdom tillsammans med antivirala, oral aciklovir 400mg 5x dagligen vid stromal/svår, profylaktisk oral aciklovir vid recidiv (400mg 2x dagligen i 1 år minskar recidiv 50%)",
        "kva": "Ingen specifik",
        "differential_diagnoses": [
            "Herpes zoster oftalmicus",
            "Bakteriell keratit",
            "Recidiverande erosion",
            "Neurotrofisk keratit"
        ],
        "description": "HSV-keratit är vanligaste infektiösa kornealsjukdom i utvecklade länder. Dendritisk epitelkeratit karakteristisk. ALDRIG steroider vid aktiv epithelial sjukdom! Recidiv vanligt (25% inom 1 år). Profylaktisk antiviral minskar recidiv.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Herpes Zoster Oftalmicus (HZO)",
        "name_en": "Herpes Zoster Ophthalmicus",
        "icd10": "B02.3",
        "symptoms": [
            "ensidig smärta i pannan/ögat",
            "utslag i V1-distribution (panna, övre ögonlock)",
            "rodnad",
            "ljuskänslighet",
            "synnedsättning",
            "ofta äldre patient",
            "postherpetisk neuralgi"
        ],
        "anamnesis_questions": [
            "Har du haft vattkoppor tidigare?",
            "Fick du smärta före utslagen?",
            "Har du utslag på näsan (Hutchinson's tecken)?",
            "Är du över 60 år?",
            "Är du immunsupprimerad?",
            "Har du HIV?"
        ],
        "clinical_signs": [
            "vesikler i V1-distribution (trigeminus första gren)",
            "Hutchinson's tecken (utslag på näsans spets = ökad risk för ögoninvolvering)",
            "konjunktivit, episklerit, sklerit",
            "dendritisk eller geografisk keratit",
            "uveit",
            "förhöjt ögontryck",
            "retinal nekros (sällsynt men allvarligt)"
        ],
        "risk_factors": [
            "hög ålder (>60 år)",
            "immunsuppression",
            "HIV",
            "cancer",
            "tidigare vattkoppor (alla som haft)"
        ],
        "treatment": "Oral antiviral AKUT (inom 72h): valaciklovir 1g 3x dagligen i 7 dagar eller famciclovir 500mg 3x dagligen, smärtlindring (paracetamol, NSAIDs, eventuellt gabapentin/amitriptylin för neuralgi), steroider topikalt vid uveit, cykloplegika vid uveit, behandla förhöjt tryck, eventuell IV-behandling vid retinal nekros eller immunsupprimerade, profylax: zoster-vaccin för >50 år",
        "kva": "Ingen specifik",
        "differential_diagnoses": [
            "HSV-keratit",
            "Bakteriell keratit",
            "Akut uveit av annan orsak"
        ],
        "description": "HZO påverkar 10-20% med herpes zoster. Kan ge allvarliga ögonkomplikationer. Hutchinson's tecken ökar risk för ögoninvolvering. Tidig antiviral behandling kritisk. Postherpetisk neuralgi vanligt hos äldre. Zoster-vaccin rekommenderas >50 år.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Akantamoeba Keratit",
        "name_en": "Acanthamoeba Keratitis",
        "icd10": "H16.8",
        "symptoms": [
            "kraftig smärta (oproportionerlig till fynd)",
            "rodnad",
            "ljuskänslighet",
            "tårrinnande",
            "synnedsättning",
            "långsam progression",
            "smärtan förvärras på natten"
        ],
        "anamnesis_questions": [
            "Använder du kontaktlinser?",
            "Har du badat/duschast med linser på?",
            "Har du använt kranvatten till linsvätska?",
            "Har du simmat i sjö, pool eller badtunna?",
            "Har symptomen pågått länge med dålig effekt av behandling?",
            "Har du mycket smärta trots läkning?"
        ],
        "clinical_signs": [
            "tidig: pseudodendriter, epitheldefekt",
            "radial keratoneurit (diagnostiskt!)",
            "ringinfiltrat (karakteristiskt)",
            "stromal infiltrat",
            "ofta misstagas för HSV initialt",
            "långsam progression över veckor",
            "eventuell perforation vid sent stadium"
        ],
        "risk_factors": [
            "kontaktlinsbärare (nästan alla fall)",
            "exponering för förorenat vatten",
            "användning av kranvatten för linser",
            "badande med linser",
            "dålig lenshygien",
            "korneal trauma"
        ],
        "treatment": "Mycket svårbehandlad! Polyhexamethylene biguanide (PHMB) 0.02% + propamidine isethionate 0.1%, initial intensiv dosering (varje timme första dygnet), fortsätt månader!, oral vorikonazol eller ketokonazol som tillägg, smärtlindring (ofta kraftig smärta), kan kräva korneatransplantation, dålig prognos vid sent diagnosticerad",
        "kva": "AKC00",
        "differential_diagnoses": [
            "HSV-keratit (ofta initial feldiagnos)",
            "Fungal keratit",
            "Bakteriell keratit",
            "Steril infiltrat"
        ],
        "description": "Akantamoeba keratit är sällsynt men förödande infektion hos kontaktlinsbärare. Karakteristisk kraftig smärta och radial keratoneurit. Ofta försenad diagnos (misstagas för HSV). Behandling svår och långvarig. Förebygg genom god lenshygien!",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Fungal Keratit",
        "name_en": "Fungal Keratitis",
        "icd10": "H16.8",
        "symptoms": [
            "gradvis smärta (mindre än bakteriell)",
            "rodnad",
            "ljuskänslighet",
            "synnedsättning",
            "långsam progression över dagar-veckor",
            "historia av trauma med växtmaterial"
        ],
        "anamnesis_questions": [
            "Har du skadats av gren, växt eller organiskt material?",
            "Arbetar du inom jordbruk eller trädgårdsarbete?",
            "Använder du steroiddroppar?",
            "Har du använt kontaktlinser?",
            "Bor du i tropiskt klimat?",
            "Har infektionen försämrats trots antibiotika?"
        ],
        "clinical_signs": [
            "fjädrad/fjällig kant på infiltrat (feathery edge)",
            "satellitlesioner",
            "endotelial plack",
            "hypopyon vanligt",
            "torr, upphöjd yta på infiltrat",
            "Filamentösa svampar (Fusarium, Aspergillus): mer aggressiva",
            "Jästsvampar (Candida): mer indolent"
        ],
        "risk_factors": [
            "korneal trauma med växtmaterial",
            "jordbruksarbete",
            "tropiskt klimat",
            "kontaktlinsbärare",
            "steroidbehandling",
            "preexisterande kornealsjukdom",
            "immunsuppression"
        ],
        "treatment": "Kornealskrap för odling/mikroskopi (KOH-prep), topikal antimykotika: natamycin 5% (filamentösa) eller amfotericin B 0.15% (jästsvampar), intensiv dosering (varje timme initialt), oral vorikonazol eller ketokonazol vid djup infektion, kan behöva intrastromal injektion av vorikonazol, lång behandlingstid (veckor-månader), korneatransplantation vid svårkontrollerad, UNDVIK STEROIDER initialt",
        "kva": "AKC00",
        "differential_diagnoses": [
            "Bakteriell keratit",
            "Akantamoeba keratit",
            "Atypisk HSV-keratit"
        ],
        "description": "Fungal keratit är vanligare i tropiska länder och hos jordbruksarbetare. Karakteristisk fjädrad kant och satellitlesioner. Långsam progression. Svårbehandlad med lång behandlingstid. Trauma med växtmaterial typisk historia.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Keratokonus",
        "name_en": "Keratoconus",
        "icd10": "H18.6",
        "symptoms": [
            "progressiv synnedsättning",
            "ökande myopi och astigmatism",
            "frekventa glasögonändringar",
            "bländning och halos",
            "monokulär diplopi/polyopi",
            "debut tonår-ung vuxen",
            "nedsatt kontrastkänslighet"
        ],
        "anamnesis_questions": [
            "Ändras dina glasögon ofta?",
            "Gnuggar du mycket i ögonen?",
            "Har du allergi eller atopi?",
            "Har du Downs syndrom?",
            "Finns keratokonus i familjen?",
            "I vilken ålder började synproblemen?",
            "Blir du mycket bländad?"
        ],
        "clinical_signs": [
            "konisk frambuktning av hornhinnan (ofta inferiort)",
            "Fleischer ring (järndeposition vid basen av konus)",
            "Vogt's striae (vertikala strecks i Descemet)",
            "Munson's tecken (V-formad nedre ögonlock vid nedåtblick)",
            "Rizutti's tecken",
            "topografi visar asymmetrisk bow-tie astigmatism",
            "hornhinneförtunning"
        ],
        "risk_factors": [
            "ögongnuggning (viktig faktor!)",
            "atopi och allergi",
            "Downs syndrom",
            "Ehlers-Danlos syndrom",
            "Marfans syndrom",
            "hereditet",
            "sydasiatiskt ursprung"
        ],
        "treatment": "Tidigt stadium: glasögon, RGP-kontaktlinser (bästa synskärpa), Cross-linking (CXL) för att stoppa progression (standard <35 år med progression), Intacs/ring segments vid intolerans för linser, Avancerat: korneatransplantation (penetrerande eller DALK), Akut hydrops: hypertonisk saltvätska, eventuellt luftbubbla i främre kammaren, VIKTIGT: minska ögongnuggning!",
        "kva": "AKD20",  # Korneatransplantation
        "differential_diagnoses": [
            "Pellucid marginal degeneration",
            "Post-LASIK ektasi",
            "Keratoglobus",
            "Terrien's marginal degeneration"
        ],
        "description": "Keratokonus är progressiv frambuktning och förtunning av hornhinnan, oftast bilateral men asymmetrisk. Debut tonår-30 år. Ögongnuggning accelererar progression. Cross-linking stoppar progression hos majoriteten. Kan kräva transplantation vid avancerade stadier.",
        "severity": "moderate-severe",
        "urgency": "routine (urgent vid akut hydrops)"
    },
    {
        "name": "Recidiverande Korneal Erosion",
        "name_en": "Recurrent Corneal Erosion",
        "icd10": "H18.8",
        "symptoms": [
            "plötslig kraftig smärta vid uppvaknande",
            "tårrinnande",
            "ljuskänslighet",
            "rodnad",
            "känsla av främmande kropp",
            "episoder varar timmar-dagar",
            "recidiverande pattern"
        ],
        "anamnesis_questions": [
            "Vaknar du med kraftig ögonsmärta?",
            "Är det värre på morgonen?",
            "Har du haft kornealtrauma tidigare (fingernagelrepa, pappersrepa)?",
            "Har det hänt flera gånger?",
            "Har du korneal dystrofi i familjen?",
            "Hur länge sedan var första episoden?"
        ],
        "clinical_signs": [
            "epitheldefekt (under attack)",
            "svaga epitel-stroma-adhesioner",
            "epithelial basement membrane förändringar",
            "mellan attacker kan kornea se normal ut",
            "eventuell karta-liknande dystrofi (EBMD)",
            "fluorescein visar defekt under attack"
        ],
        "risk_factors": [
            "tidigare korneal trauma (fingernagelrepa vanligast)",
            "epithelial basement membrane dystrofi (EBMD)",
            "korneal dystrofier (lattice, granular)",
            "torrt öga",
            "diabetes"
        ],
        "treatment": "Akut: lubricerande salva nattetid, hypertonisk saltvätska (NaCl 5%) droppar dag + salva natt, bandagelinser, eventuellt debridering av löst epitel, Förebyggande: fortsätt lubricering 3-6 månader, hypertonisk NaCl långvarigt, omega-3 tillskott, Vid refraktära: anterior stromal punktur, phototherapeutic keratectomy (PTK) med excimerlaser, mycket god prognos med rätt behandling",
        "kva": "AKC10",  # PTK
        "differential_diagnoses": [
            "Akut korneal erosion (engångsförekomst)",
            "HSV-keratit",
            "Bakteriell keratit",
            "Torrt öga"
        ],
        "description": "RCE uppstår när epitelet inte fäster ordentligt på basement membrane. Trauma eller dystrofi vanligaste orsaker. Typisk presentation: kraftig smärta vid uppvaknande (ögonlocket river loss epitelet). Oftast god prognos med lubricering och hypertonisk saltvätska.",
        "severity": "mild-moderate",
        "urgency": "urgent (vid attack)"
    },
    {
        "name": "Torrt Öga (Keratoconjunctivitis Sicca)",
        "name_en": "Dry Eye Disease",
        "icd10": "H04.1",
        "symptoms": [
            "torr, brännande känsla",
            "gruskänsla eller främmande kropp",
            "rodnad",
            "tårrinnande (paradoxalt - reflexvätskande)",
            "suddig syn (varierar med blinkning)",
            "trötthet i ögonen",
            "svårt att bära kontaktlinser",
            "värre sent på dagen eller vid datorarbete"
        ],
        "anamnesis_questions": [
            "Känner dina ögon torra?",
            "Har du gruskänsla?",
            "Förbättras synen när du blinkar?",
            "Arbetar du mycket vid dator?",
            "Är du kvinna i menopaus?",
            "Har du Sjögrens syndrom eller annan autoimmun sjukdom?",
            "Tar du mediciner (antihistamin, antidepressiva, betablockerare)?",
            "Använder du kontaktlinser?"
        ],
        "clinical_signs": [
            "nedsatt tårbytestid (TBUT <10 sek)",
            "Schirmer test <10 mm/5 min (aqueous deficiency)",
            "konjunktival injektion",
            "korneal/konjunktival fluorescein-färgning",
            "trådig mukus",
            "ökad tårosmolaritet",
            "meibomian gland dysfunction ofta"
        ],
        "risk_factors": [
            "kvinnligt kön",
            "hög ålder",
            "menopaus",
            "Sjögrens syndrom",
            "reumatoid artrit, SLE",
            "kontaktlinsbärare",
            "LASIK/refraktiv kirurgi",
            "mediciner (antihistamin, antidepressiva, isotretinoin)",
            "skärmarbete",
            "låg luftfuktighet"
        ],
        "treatment": "Artificiella tårar (konserveringsfria om >4x/dag), lubricerande salva nattetid, Omega-3 tillskott (fiskoljor), behandla meibomian gland dysfunction (varma kompresser, ögonlocksmassage), cyklosporin A 0.05% eller lifitegrast vid inflammation, punctal plugs vid svår, behandla underliggande sjukdom (Sjögrens), minska skärmtid, luftbefuktare, scleral linser vid svår",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Allergisk konjunktivit",
            "Blepharit",
            "Meibomian gland dysfunction",
            "Konjunktivit"
        ],
        "description": "Torrt öga är mycket vanligt (15-30% av befolkningen). Kan vara aqueous-deficient (Sjögrens, ålder) eller evaporativ (MGD vanligaste). Kroniskt tillstånd som kräver långsiktig behandling. Påverkar livskvalitet betydligt.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Fuchs Endotel Dystrofi",
        "name_en": "Fuchs Endothelial Dystrophy",
        "icd10": "H18.5",
        "symptoms": [
            "suddig syn på morgonen (förbättras under dagen)",
            "bländning",
            "halos runt lampor",
            "gradvis försämring",
            "smärta vid bullös keratopati (sent stadium)",
            "debut medelålder-äldre",
            "kvinnor vanligare"
        ],
        "anamnesis_questions": [
            "Är synen sämst på morgonen?",
            "Förbättras den under dagen?",
            "Blir du bländad av lampor?",
            "Har du smärta i ögat?",
            "Har andra i familjen samma problem?",
            "Hur gammal är du?"
        ],
        "clinical_signs": [
            "guttata (dropliknande utväxter på Descemet)",
            "endoteldysfunktion",
            "korneal ödem (stromal och epithelial)",
            "nedsatt endotelcellstäthet",
            "ökad hornhinnetjocklek (pachymetri)",
            "bullae i epitel vid avancerad sjukdom"
        ],
        "risk_factors": [
            "hög ålder",
            "kvinnligt kön (3:1)",
            "hereditet (autosomalt dominant ofta)",
            "TCF4-genmutation vanlig"
        ],
        "treatment": "Tidigt: hypertonisk saltvätska (NaCl 5%) för att minska ödem, hårtork över ögat på morgonen (minskar ödem), Avancerat: DMEK (Descemet Membrane Endothelial Keratoplasty) - modernaste, DSAEK (Descemet Stripping Automated Endothelial Keratoplasty), penetrerande korneatransplantation (mindre använd nu), smärtlindring vid bullös keratopati, god prognos med DMEK",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Pseudoexfoliativ endoteldysfunktion",
            "Post-kirurgisk korneal ödem",
            "Posteriör polymorf dystrofi"
        ],
        "description": "Fuchs dystrofi är vanligaste indikation för korneatransplantation. Progressiv endotelcellsförlust leder till korneal ödem. Karakteristisk morgonförsämring (ödem byggs upp nattetid). DMEK har revolutionerat behandlingen med snabb återhämtning och utmärkt syn.",
        "severity": "moderate-severe",
        "urgency": "routine (elective för transplantation)"
    },
    {
        "name": "Pterygium",
        "name_en": "Pterygium",
        "icd10": "H11.0",
        "symptoms": [
            "synligt vävnadsväxt från konjunktiva på kornea",
            "rodnad och irritation",
            "främmande kropps-känsla",
            "torrhets känsla",
            "synnedsättning om över pupillen",
            "astigmatism",
            "kosmetiskt störande"
        ],
        "anamnesis_questions": [
            "Har du märkt vävnadsväxt på ögat?",
            "Bor du i soligt klimat?",
            "Är du mycket utomhus?",
            "Använder du solglasögon?",
            "Växer det?",
            "Är det irriterat och rött ibland?",
            "Påverkar det synen?"
        ],
        "clinical_signs": [
            "triangelliknande vävnad från nasal konjunktiva på kornea",
            "Stocker's line (järndeposition vid toppen)",
            "korneal traction lines",
            "fibrovascular vävnad",
            "mestadels nasal (90%), kan vara temporal",
            "kan vara bilateral"
        ],
        "risk_factors": [
            "UV-exponering (viktigaste!)",
            "soligt, varmt, torrt klimat",
            "utomhusarbete",
            "närheten till ekvatorn",
            "hereditet",
            "manligt kön (något vanligare)"
        ],
        "treatment": "Observation om liten och asymtomatisk, lubricerande droppar för irritation, NSAID-droppar vid inflammation, kirurgisk excision om: växer över pupillen, betydande astigmatism, kosmetiskt störande, kronisk inflammation, Kirurgi: excision + konjunktival autograft (lägst recidiv) eller amnion membrane graft, mitomycin C intraoperativt minskar recidiv, recidiv 5-15% trots optimal teknik, UV-skydd viktigt postop och livslångt",
        "kva": "AKB10",  # Pterygiumexcision
        "differential_diagnoses": [
            "Pinguecula (växer ej på kornea)",
            "Konjunktival tumor (sällsynt)",
            "Pseudopterygium (efter trauma/inflammation)"
        ],
        "description": "Pterygium är fibrovascular växt från konjunktiva på kornea. UV-relaterad. Vanligast i tropiska områden ('surfareöga'). Kan ge astigmatism och synnedsättning. Kirurgi med autograft ger lägst recidiv. UV-skydd kritiskt för förebyggande.",
        "severity": "mild-moderate",
        "urgency": "routine (elective kirurgi)"
    },
    {
        "name": "Epithelial Basement Membrane Dystrofi (Map-Dot-Fingerprint)",
        "name_en": "Epithelial Basement Membrane Dystrophy",
        "icd10": "H18.5",
        "symptoms": [
            "ofta asymtomatisk",
            "recidiverande erosioner (se RCE ovan)",
            "lätt synnedsättning eller suddig syn",
            "variabel symptom"
        ],
        "anamnesis_questions": [
            "Har du recidiverande ögonsmärta på morgonen?",
            "Har du märkt lätt suddig syn?",
            "Finns korneal dystrofi i familjen?",
            "Är båda ögonen påverkade?"
        ],
        "clinical_signs": [
            "karta-liknande linjer (maps)",
            "grå-vita dots",
            "fingeravtryck-liknande linjer",
            "abnormt basement membrane",
            "ofta bilateral",
            "kan vara svårt att se - kräver retro-illumination"
        ],
        "risk_factors": [
            "hereditet (kan vara autosomalt dominant)",
            "hög ålder (vanligare hos äldre)",
            "kan vara sporadisk"
        ],
        "treatment": "Observation om asymtomatisk, behandling av recidiverande erosioner (se RCE), lubricering, hypertonisk saltvätska, PTK (phototherapeutic keratectomy) vid refraktära erosioner, epithelial debridering, god prognos",
        "kva": "AKC10",
        "differential_diagnoses": [
            "Andra korneal dystrofier",
            "Recidiverande erosion utan dystrofi"
        ],
        "description": "EBMD är vanligaste korneal dystrofi. Ofta asymtomatisk upptäcks-fynd. Huvudproblem är recidiverande erosioner. Map-dot-fingerprint pattern karakteristiskt. God prognos med lubricering och hypertonisk saltvätska.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Lattice Korneal Dystrofi",
        "name_en": "Lattice Corneal Dystrophy",
        "icd10": "H18.5",
        "symptoms": [
            "gradvis synnedsättning från barndom-ungdom",
            "recidiverande erosioner",
            "ljuskänslighet",
            "bländning",
            "bilateral"
        ],
        "anamnesis_questions": [
            "I vilken ålder började synproblemen?",
            "Har du recidiverande erosioner?",
            "Finns korneal dystrofi i familjen?",
            "Påverkas båda ögonen?"
        ],
        "clinical_signs": [
            "gitter-liknande linjer i stroma (amyloiddepositioner)",
            "vita dots mellan linjerna",
            "kan få korneal opacitet över tid",
            "bilateral och symmetrisk",
            "flera typer (typ 1 vanligast)"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant)",
            "TGFBI-genmutation",
            "familjehistoria"
        ],
        "treatment": "Lubricering för erosioner, PTK för erosioner eller ytlig opacitet, korneatransplantation vid avancerad opacitet, kan recidivera i graft (amyloid deponeras igen), PRK/LASIK kontraindicerat",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Granular dystrofi",
            "Avellino dystrofi",
            "Andra stromala dystrofier"
        ],
        "description": "Lattice dystrofi orsakas av amyloiddepositioner i stroma. Autosomalt dominant. Debut barndom-ungdom. Recidiverande erosioner och gradvis synnedsättning. Kan kräva transplantation men recidiverar ofta i graft.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Granular Korneal Dystrofi",
        "name_en": "Granular Corneal Dystrophy",
        "icd10": "H18.5",
        "symptoms": [
            "gradvis synnedsättning",
            "bländning",
            "debut barndom-ungdom",
            "bilateral",
            "långsammare progression än lattice"
        ],
        "anamnesis_questions": [
            "När började synproblemen?",
            "Finns korneal dystrofi i familjen?",
            "Blir du mycket bländad?"
        ],
        "clinical_signs": [
            "vita, breadcrumb-like opaciteter i anterior-mid stroma",
            "klar stroma mellan lesionerna (viktigt!)",
            "bilateral och symmetrisk",
            "typ 1: hyalin deposits, typ 2 (Avellino): hyalin + amyloid"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant)",
            "TGFBI-genmutation",
            "familjehistoria"
        ],
        "treatment": "PTK för ytliga opaciteter, korneatransplantation vid avancerad, PTK kontraindicerat vid Avellino-typ! (kan förvärra), LASIK/PRK kontraindicerat (Avellino kan accelerera efter laser)",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Lattice dystrofi",
            "Avellino dystrofi (granular typ 2)",
            "Reis-Bücklers dystrofi"
        ],
        "description": "Granular dystrofi orsakar hyalin-depositioner. Långsammare progression än lattice. Klar stroma mellan opaciteter (vs lattice). Avellino-variant särskilt viktig att känna till - ALDRIG LASIK/PRK (kan ge kraftig försämring).",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Korneal Sår (Corneal Ulcer) - Steril",
        "name_en": "Sterile Corneal Ulcer",
        "icd10": "H16.0",
        "symptoms": [
            "ögonsmärta",
            "rodnad",
            "ljuskänslighet",
            "tårrinnande",
            "synnedsättning",
            "mindre akut än bakteriell"
        ],
        "anamnesis_questions": [
            "Har du autoimmun sjukdom (RA, Wegeners)?",
            "Har du torrt öga?",
            "Har du haft ögonkirurgi nyligen?",
            "Använder du kontaktlinser?",
            "Har du exposition (lagoftalmus, bells pares)?"
        ],
        "clinical_signs": [
            "korneal epitheldefekt med ulceration",
            "steril (negativ odling)",
            "ofta perifer lokalisering",
            "underliggande stromal förtunning möjlig",
            "ingen suppuration",
            "olika orsaker ger olika mönster"
        ],
        "risk_factors": [
            "torrt öga (neurotrofiskt)",
            "exposition (lagoftalmus)",
            "autoimmun sjukdom",
            "post-kirurgisk",
            "vitamin A-brist (utvecklingsländer)"
        ],
        "treatment": "Beroende på orsak: Neurotrofiskt: lubricering, bandagelinser, tarsorrafi, autologt serum, cenegermin (NGF), Autoimmunt: steroider + immunosuppression, behandla underliggande sjukdom, Exposition: tarsorrafi, lubricering, behandla lagoftalmus, Uteslut infektion först (odling)!",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Infektiös keratit (bakteriell, viral, fungal)",
            "Mooren's ulcer",
            "Marginal keratit"
        ],
        "description": "Sterila korneal sår har många orsaker: neurotrofiska, exposition, autoimmuna, postkirurgiska. Viktigt att utesluta infektion med odling. Behandling riktas mot underliggande orsak. Risk för perforation vid djupa sår.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Mooren's Ulcer",
        "name_en": "Mooren's Ulcer",
        "icd10": "H16.0",
        "symptoms": [
            "kraftig smärta",
            "rodnad",
            "ljuskänslighet",
            "tårrinnande",
            "gradvis perifer korneal förtunning",
            "synnedsättning"
        ],
        "anamnesis_questions": [
            "Är smärtan kraftig?",
            "Har såret börjat perifert och växer centralt?",
            "Är du från Afrika eller Indien?",
            "Har du haft hepatit C?",
            "Har såret försämrats trots antibiotika?"
        ],
        "clinical_signs": [
            "perifer ulcerativ keratit",
            "underminerad, framåtskridande kant",
            "början perifert, växer circumferentiellt och centralt",
            "steril (ingen infektion)",
            "stromal förtunning",
            "två former: bilateral (yngre) och unilateral (äldre)"
        ],
        "risk_factors": [
            "okänd etiologi (autoimmmun?)",
            "parasitinfektion (helminter) i endemiska områden",
            "hepatit C möjligen",
            "vanligare i Afrika, Indien"
        ],
        "treatment": "Svårbehandlad! Steroider topikalt + systemiskt, immunosuppression (cyclosporin, cyclophosphamid, MTX), conjunctival excision/resektion, eventuell korneatransplantation, behandla hepatit C om present, kan vara refraktär mot behandling, dålig prognos vid bilateral form",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Perifer ulcerativ keratit vid RA/Wegeners",
            "Infektiös keratit",
            "Terrien's marginal degeneration"
        ],
        "description": "Mooren's ulcer är en idiopatisk perifer ulcerativ keratit. Smärtsam och progressiv. Steril trots ulceration. Vanligare i utvecklingsländer. Svårbehandlad med risk för perforation. Kräver aggressiv immunosuppression.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Perifer Ulcerativ Keratit vid Reumatoid Artrit",
        "name_en": "Peripheral Ulcerative Keratitis in RA",
        "icd10": "H16.0 + M05.9",
        "symptoms": [
            "smärta (kan vara mild eller kraftig)",
            "rodnad",
            "ljuskänslighet",
            "synnedsättning",
            "kan vara associerad med skleral inflammation",
            "patient med känd RA oftast"
        ],
        "anamnesis_questions": [
            "Har du reumatoid artrit?",
            "Hur aktiv är din ledsjukdom?",
            "Har du andra autoimmuna sjukdomar?",
            "Tar du immunosuppressiva läkemedel?",
            "Har du haft liknande tidigare?"
        ],
        "clinical_signs": [
            "perifer korneal ulceration och förtunning",
            "ofta vid limbus",
            "kan vara circumferentiell",
            "steril",
            "ofta associerad sklerit",
            "risk för perforation"
        ],
        "risk_factors": [
            "reumatoid artrit (särskilt seropositiv)",
            "aktiv systemsjukdom",
            "vaskulit",
            "andra autoimmuna sjukdomar (Wegeners, SLE, PAN)"
        ],
        "treatment": "AKUT systemisk behandling nödvändig! Höga doser systemiska steroider, immunosuppression (cyclophosphamid, MTX, rituximab, biologiska), behandla underliggande RA aggressivt, cyanoacrylat-lim vid hotande perforation, korneatransplantation vid perforation, tarsorrafi, samarbete med reumatolog kritiskt",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Mooren's ulcer",
            "PUK vid Wegeners granulomatosis",
            "Infektiös keratit",
            "Terrien's marginal degeneration"
        ],
        "description": "PUK vid RA är en allvarlig komplikation som speglar systemisk vaskulit. Risk för perforation och synförlust. Kräver akut systemisk immunosuppression. Ofta associerad med sklerit. Samarbete med reumatolog essentiellt.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Terrien's Marginal Degeneration",
        "name_en": "Terrien's Marginal Degeneration",
        "icd10": "H18.4",
        "symptoms": [
            "gradvis synnedsättning",
            "astigmatism (ökande)",
            "oftast asymtomatisk tidigt",
            "sällan smärta",
            "långsam progression över år-decennier"
        ],
        "anamnesis_questions": [
            "Har din astigmatism ökat över åren?",
            "Är du man 20-40 år?",
            "Har du märkt perifer förtunning av hornhinnan?",
            "Har du smärta? (oftast nej)"
        ],
        "clinical_signs": [
            "perifer korneal förtunning, oftast superior",
            "lipiddeposition framför förtunningen",
            "neovaskularisation",
            "klar zone mellan förtunning och limbus",
            "asymmetrisk astigmatism",
            "långsam progression",
            "bilateral hos 50%"
        ],
        "risk_factors": [
            "manligt kön (4:1)",
            "ålder 20-40 år vid debut",
            "okänd etiologi",
            "kan vara hereditet"
        ],
        "treatment": "Observation vid mild, korrigera astigmatism med glasögon/RGP-linser, intrastromal korneal ringsegment (Intacs) kan minska astigmatism, korneatransplantation vid kraftig förtunning eller perforation (sällsynt), cyanoacrylat-lim vid hotande perforation, god prognos - sällan perforation",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Pellucid marginal degeneration (inferior lokalisering)",
            "Perifer ulcerativ keratit",
            "Mooren's ulcer (men inflammation och smärta)"
        ],
        "description": "Terrien's degeneration är en bilateral perifer korneal förtunning hos unga-medelålders män. Långsam progression. Huvudproblem är astigmatism. Sällan inflammation eller perforation. God prognos.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Pellucid Marginal Degeneration",
        "name_en": "Pellucid Marginal Degeneration",
        "icd10": "H18.7",
        "symptoms": [
            "progressiv synnedsättning",
            "ökande astigmatism",
            "debut ung vuxen (20-40 år)",
            "bländning",
            "monokulär diplopi"
        ],
        "anamnesis_questions": [
            "Har din astigmatism ökat kraftigt?",
            "Behöver du byta glasögon ofta?",
            "Är du 20-40 år?",
            "Påverkas båda ögonen?"
        ],
        "clinical_signs": [
            "inferior perifer korneal förtunning (4-8 o'clock position)",
            "band av förtunning 1-2 mm från limbus",
            "protrusion ovanför förtunningen",
            "klar kornea (ingen scarring)",
            "topografi: 'claw' pattern eller 'kissing birds'",
            "bilateral"
        ],
        "risk_factors": [
            "okänd etiologi",
            "debut 20-40 år",
            "kan ha hereditet",
            "ögongnuggning möjligen"
        ],
        "treatment": "RGP-kontaktlinser eller scleral linser, intrastromal ringsegment (Intacs), kan inte göra cross-linking (degeneration, ej ektasi), korneatransplantation vid avancerad, wedge resection i vissa fall, undvik LASIK/PRK",
        "kva": "AKD20",
        "differential_diagnoses": [
            "Keratokonus (central/paracentral vs inferior perifer)",
            "Terrien's degeneration (superior)",
            "Inferior keratokonus"
        ],
        "description": "PMD är inferior perifer korneal förtunning hos unga vuxna. Ger kraftig against-the-rule astigmatism. Bilateral. Skiljer sig från keratokonus genom lokalisering och 'claw'-topografi. Kontaktlinser eller kirurgi behövs ofta.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Korneal Hydrops vid Keratokonus",
        "name_en": "Acute Corneal Hydrops",
        "icd10": "H18.6",
        "symptoms": [
            "plötslig kraftig synförsämring",
            "smärta",
            "ljuskänslighet",
            "tårrinnande",
            "mjölkvit kornea",
            "historia av keratokonus"
        ],
        "anamnesis_questions": [
            "Har du keratokonus?",
            "Fick du plötslig försämring?",
            "Blev ögat mjölkvitt/grumligt?",
            "Har du smärta?"
        ],
        "clinical_signs": [
            "ruptur av Descemet's membran",
            "akut korneal ödem (stroma fylls med vätska)",
            "mjölkvit kornea",
            "Descemet's break synlig",
            "kan ha luftbubbla i främre kammaren (Amsler sign)",
            "gradvis clearing över 2-4 månader"
        ],
        "risk_factors": [
            "keratokonus (framskriden)",
            "pellucid marginal degeneration",
            "post-LASIK ektasi",
            "ögongnuggning",
            "akut tryckstegring (lyfta tungt)"
        ],
        "treatment": "Konservativ behandling oftast: hypertonisk saltvätska (NaCl 5%), cykloplegika för comfort, steroider för att minska inflammation, smärtlindring, bandagelinser ibland, undvik ögongnuggning!, Kirurgiskt (sällan): intracameral luftbubbla (för att täppa Descemet's break), korneatransplantation endast vid svår scarring eller ej clearing, oftast clearing på 2-4 månader, paradoxalt: synen kan förbättras efter läkning (konusen plattas ut av scarring)",
        "kva": "Ingen vanligtvis (konservativ)",
        "differential_diagnoses": [
            "Infektiös keratit med ödem",
            "Akut korneal ödem av annan orsak",
            "Endotelial dekompensation"
        ],
        "description": "Akut hydrops är ruptur av Descemet's membran vid keratokonus som leder till akut korneal ödem. Plötslig synförsämring. Behandlas oftast konservativt. Clearing över 2-4 månader. Paradoxalt kan synen förbättras efter läkning pga utplattning.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Korneal Neovaskularisation",
        "name_en": "Corneal Neovascularization",
        "icd10": "H16.8",
        "symptoms": [
            "synnedsättning (om över pupillen)",
            "rodnade kärl på kornea",
            "ofta asymtomatisk om perifer",
            "underliggande orsak ger symptom"
        ],
        "anamnesis_questions": [
            "Använder du kontaktlinser?",
            "Hur länge bär du dem per dag?",
            "Har du haft korneal infektion?",
            "Har du haft korneal transplantation?",
            "Har du limbal stammcellsbrist?"
        ],
        "clinical_signs": [
            "blodkärl växer in på kornea från limbus",
            "kan vara ytliga eller djupa",
            "kan vara 360° eller sektorielt",
            "underliggande orsak ofta synlig",
            "scarring möjlig"
        ],
        "risk_factors": [
            "kronisk kontaktlinsanvändning (hypoxi)",
            "korneal infektion/inflammation",
            "korneal transplantation (risk för rejektion)",
            "limbal stammcellsbrist",
            "keratit (alla typer)",
            "pterygium",
            "trachom"
        ],
        "treatment": "Behandla underliggande orsak: sluta med kontaktlinser eller byt till daglinser/högre Dk, behandla inflammation (steroider), anti-VEGF (bevacizumab) subkonjunktivalt eller topikalt - minskar kärl temporärt, fine-needle diathermy, argon laser photocoagulation, limbal transplantation vid stammcellsbrist, kärl återkommer ofta om orsak ej åtgärdas",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Normal limbal vascularisation (<1mm)",
            "Pannus (vid trachom)"
        ],
        "description": "Korneal neovaskularisation uppstår vid hypoxi, inflammation eller skada. Kontaktlinser är vanligaste orsaken i utvecklade länder. Kärl kan ge synnedsättning och ökar risk för transplantationsrejektion. Behandla underliggande orsak.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Salzmann's Nodulär Degeneration",
        "name_en": "Salzmann's Nodular Degeneration",
        "icd10": "H18.4",
        "symptoms": [
            "gradvis synnedsättning",
            "främmande kropps-känsla",
            "irritation",
            "astigmatism",
            "ofta historia av kronisk inflammation"
        ],
        "anamnesis_questions": [
            "Har du haft kronisk ögonirritation?",
            "Har du haft keratit tidigare?",
            "Har du haft pterygium operation?",
            "Märker du upphöjda knutor på ögat?",
            "Är du kvinna 40-70 år?"
        ],
        "clinical_signs": [
            "upphöjda blåvita noduler på kornea",
            "oftast mitt-perifer",
            "subepiteliala depositioner",
            "kan vara 360° eller sektorielt",
            "klar kornea mellan noduler"
        ],
        "risk_factors": [
            "kronisk keratit",
            "phlyctenular keratitis historia",
            "pterygium operation",
            "kontaktlinsrelaterad keratit",
            "kvinnligt kön",
            "ålder 40-70 år"
        ],
        "treatment": "Observation om asymtomatisk, lubricering för irritation, superficial keratectomy (skrapa bort noduler) vid symptomatisk, PTK (phototherapeutic keratectomy), bandagelinser postop, kan recidivera men oftast god prognos",
        "kva": "AKC10",
        "differential_diagnoses": [
            "Bandformad keratopati",
            "Korneal scarring",
            "Spheroidal degeneration"
        ],
        "description": "Salzmann's nodulära degeneration utvecklas efter kronisk korneal inflammation. Blåvita upphöjda noduler. Vanligare hos kvinnor. Behandlas med superficial keratectomy om symptomatisk. God prognos.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Bandformad Keratopati",
        "name_en": "Band Keratopathy",
        "icd10": "H18.4",
        "symptoms": [
            "gradvis synnedsättning",
            "bländning",
            "främmande kropps-känsla",
            "irritation",
            "synlig vit band över kornea"
        ],
        "anamnesis_questions": [
            "Har du haft kronisk inflammation (uveit)?",
            "Har du njurproblem eller högt kalcium?",
            "Har du Still's sjukdom (JIA)?",
            "Har du haft silikon-oljefyllt öga?",
            "Använder du fosfatdroppar?"
        ],
        "clinical_signs": [
            "vit, kalkaktig band på kornea",
            "börjar vid 3 och 9 o'clock limbus",
            "växer över kornea horisontellt",
            "kalciumdepositioner i Bowman's layer",
            "'Swiss cheese' utseende (luckor för nervpassage)",
            "kan vara hela kornea vid avancerad"
        ],
        "risk_factors": [
            "kronisk uveit (särskilt JIA)",
            "hyperkalcemi",
            "kronisk njursvikt",
            "phthisis bulbi",
            "långvarig silikon-olja",
            "fosfat-innehållande ögondroppar",
            "hereditet (sällsynt)"
        ],
        "treatment": "EDTA-kelatbehandling (avlägsnar kalcium kemiskt), debridering av lucknade kalciumdepåer, PTK (excimerlaser), behandla underliggande orsak (uveit, hyperkalcemi), lubricering, bandagelinser, kan recidivera om underliggande orsak kvarstår",
        "kva": "AKC10",
        "differential_diagnoses": [
            "Salzmann's degeneration",
            "Korneal scarring",
            "Spheroidal degeneration"
        ],
        "description": "Bandformad keratopati är kalciumdepositioner i Bowman's layer, ofta sekundärt till kronisk uveit eller hyperkalcemi. Karakteristisk horisontell band. Behandlas med EDTA-kelation. Recidiverar om underliggande orsak kvarstår.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Exponeringskeratopati (Lagoftalmus)",
        "name_en": "Exposure Keratopathy",
        "icd10": "H16.2",
        "symptoms": [
            "torrhet",
            "främmande kropps-känsla",
            "rodnad",
            "tårrinnande (reflexvätskande)",
            "synnedsättning",
            "smärta vid ulceration",
            "värre på morgonen"
        ],
        "anamnesis_questions": [
            "Stänger dina ögonlock helt?",
            "Har du Bell's pares eller ansiktspares?",
            "Har du sköldkörtelsjukdom (tyreoideaorbitopati)?",
            "Vaknar du med torra ögon?",
            "Har du haft stroke eller ansiktsskada?",
            "Har du ektropion?"
        ],
        "clinical_signs": [
            "inkomplett lockstängning (lagoftalmus)",
            "inferior korneal färgning/torrhettecken",
            "epitheldefekt eller ulceration",
            "stromal scarring vid kronisk",
            "eventuell perforation vid svår",
            "underliggande orsak synlig (pares, exoftalmus, ektropion)"
        ],
        "risk_factors": [
            "Bell's pares/ansiktspares",
            "tyreoideaorbitopati (Graves)",
            "exoftalmus av annan orsak",
            "ektropion",
            "floppy eyelid syndrome",
            "neuromuscular sjukdom",
            "post-blepharoplasty"
        ],
        "treatment": "Lubricering: artificiella tårar dag, tjock salva natt, moisture chamber glasses eller täckning nattetid, taping av lock nattetid, bandagelinser, botulinum toxin till levator (temporär ptosis), tarsorrafi (temporär eller permanent), gold weight i övre lock (vid pares), korrigera ektropion/exoftalmus om möjligt, orbital dekompression vid tyreoideaorbitopati",
        "kva": "Varierar (tarsorrafi, ektropionkorrigering)",
        "differential_diagnoses": [
            "Torrt öga av annan orsak",
            "Neurotrofisk keratopati",
            "Korneal ulcer av annan orsak"
        ],
        "description": "Exponeringskeratopati uppstår vid inkomplett lockstängning. Inferior kornea exponeras och torkar ut. Riskerar ulceration och perforation. Kräver aggressiv lubricering och eventuellt kirurgiska åtgärder. Behandla underliggande orsak om möjligt.",
        "severity": "moderate-severe",
        "urgency": "urgent (vid ulceration)"
    },
    {
        "name": "Neurotrofisk Keratopati",
        "name_en": "Neurotrophic Keratopathy",
        "icd10": "H16.2",
        "symptoms": [
            "ofta asymtomatisk (nedsatt sensibilitet)",
            "synnedsättning",
            "rodnad",
            "minimal smärta (viktigt!)",
            "korneal opacitet"
        ],
        "anamnesis_questions": [
            "Har du haft herpes i ögat tidigare?",
            "Har du diabetes?",
            "Har du haft stroke eller ansiktspares?",
            "Har du haft operation vid trigeminus neuralgi?",
            "Känner du smärta? (ofta nej trots stora sår)"
        ],
        "clinical_signs": [
            "nedsatt eller avsend korneal sensibilitet (viktigt!)",
            "persistent epitheldefekt",
            "ofta oval/rund defekt centralt",
            "rullade kanter på defekten",
            "kan progrediera till stromal ulceration",
            "risk för perforation",
            "underliggande orsak till nervskada ofta synlig"
        ],
        "risk_factors": [
            "herpes simplex/zoster keratit (vanligaste)",
            "diabetes",
            "trigeminus nervskada (kirurgi, stroke, tumör)",
            "långvarig kontaktlinsanvändning",
            "LASIK/PRK",
            "topikala anestetika-missbruk"
        ],
        "treatment": "Lubricering (artificiella tårar, salva), bandagelinser, autologt serum 20% (innehåller tillväxtfaktorer), tarsorrafi, cenegermin (rhNGF - rekombinant nerve growth factor) - nytt och effektivt!, amniotic membrane transplantation, korneaplastik vid perforation, UNDVIK STEROIDER (hämmar läkning), behandla underliggande diabetes/orsak",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Exponeringskeratopati",
            "Persistent epitheldefekt av annan orsak",
            "Indolent ulcer"
        ],
        "description": "Neurotrofisk keratopati uppstår vid skada på korneal innervation. Karakteristisk nedsatt sensibilitet och persistent epitheldefekt trots minimal inflammation. Vanligaste orsak: tidigare herpes-keratit. Svårläkt. Cenegermin (NGF) har revolutionerat behandlingen.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Thygeson's Superficiell Punktat Keratit",
        "name_en": "Thygeson's Superficial Punctate Keratitis",
        "icd10": "H16.1",
        "symptoms": [
            "främmande kropps-känsla",
            "ljuskänslighet",
            "tårrinnande",
            "lätt synnedsättning",
            "recidiverande episoder",
            "bilateral",
            "kroniskt förlopp över år"
        ],
        "anamnesis_questions": [
            "Har du återkommande episoder av ögonirritation?",
            "Påverkas båda ögonen?",
            "Varar episoderna veckor-månader?",
            "Har du haft detta i år?",
            "Förbättras det av steroiddroppar?"
        ],
        "clinical_signs": [
            "små gråvita korneal epitheliala infiltrat",
            "coarse punctate opacities",
            "oftast 10-20 lesioner per öga",
            "ingen korneal neovaskularisation",
            "ingen uveit",
            "bilateral men ofta asymmetrisk",
            "minimal konjunktival injektion"
        ],
        "risk_factors": [
            "okänd etiologi",
            "troligen viral (ej bevisad)",
            "ej hereditet",
            "alla åldrar men ofta ung-medelålder"
        ],
        "treatment": "Lubricering för milda symptom, steroiddroppar (låg dos) vid symptomatiska episoder - mycket effektivt!, bandagelinser, topikalt cyclosporin A kan användas som steroid-sparande, oftast självbegränsande över år (5-10 år), god prognos utan scarring, undvik långvariga steroider (använd minsta effektiva dos)",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Viral keratit",
            "Adenoviral keratokonjunktivit (men mer akut)",
            "Torrt öga",
            "Toxic keratopathy"
        ],
        "description": "Thygeson's SPK är en kronisk, recidiverande bilateral keratit av okänd orsak. Karakteristiska gråvita epitheliala infiltrat. Svarar mycket bra på steroider. Självbegränsande över år. God prognos utan scarring.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Filamentär Keratit",
        "name_en": "Filamentary Keratitis",
        "icd10": "H16.1",
        "symptoms": [
            "främmande kropps-känsla",
            "smärta (särskilt vid blinkning)",
            "ljuskänslighet",
            "tårrinnande",
            "rodnad",
            "synliga 'trådar' på hornhinnan"
        ],
        "anamnesis_questions": [
            "Har du torrt öga?",
            "Har du haft ögonkirurgi nyligen?",
            "Har du Sjögrens syndrom?",
            "Känner du att något drar i ögat när du blinkar?",
            "Har du haft herpes i ögat?"
        ],
        "clinical_signs": [
            "mukus-filament fästade på kornea",
            "filament består av mukus + epithelceller",
            "smärta när filament drar i epitel vid blinkning",
            "fluorescein-färgning vid filamentbas",
            "underliggande torrt öga eller kornealsjukdom"
        ],
        "risk_factors": [
            "svårt torrt öga",
            "Sjögrens syndrom",
            "post-vitrektomi",
            "post-korneatransplantation",
            "neurotrofisk keratopati",
            "superior limbic keratoconjunctivitis (SLK)",
            "långvarig patching/bandage"
        ],
        "treatment": "Lubricering (artificiella tårar frekvent, salva), mekanisk removal av filament (pincett), acetylcystein 10% (mukolytiskt), bandagelinser, autologt serum, behandla underliggande orsak (torrt öga, Sjögrens), eventuellt botulinum toxin-inducerad ptosis (minskar exponering)",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Mukusstråmmar vid torrt öga (men ej fästade)",
            "Superior limbic keratoconjunctivitis"
        ],
        "description": "Filamentär keratit uppstår när mukus-strängar fäster på kornea och drar i epitel vid blinkning. Smärtsamt. Vanligast vid svårt torrt öga. Behandla underliggande orsak och avlägsna filament mekaniskt.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Interstitiell Keratit (IK)",
        "name_en": "Interstitial Keratitis",
        "icd10": "H16.3",
        "symptoms": [
            "synnedsättning",
            "ljuskänslighet",
            "smärta",
            "tårrinnande",
            "rodnad",
            "ofta bilateral",
            "historia av systemsjukdom"
        ],
        "anamnesis_questions": [
            "Har du haft syfilis?",
            "Har du haft tuberkulös?",
            "Har du Lyme disease?",
            "Har du Cogan's syndrom (hörselnedsättning)?",
            "Föddes du med kongenital syfilis?"
        ],
        "clinical_signs": [
            "djup stromal inflammation",
            "korneal ödem",
            "neovaskularisation djupt i stroma",
            "'ghost vessels' vid läkt (tomma kärl)",
            "eventuell anterior uveit",
            "stromal scarring",
            "kan se 'salmon patch' vid syfilis"
        ],
        "risk_factors": [
            "kongenital syfilis (vanligaste orsak historiskt)",
            "förvärvad syfilis",
            "tuberkulos",
            "Lyme disease",
            "Cogan's syndrom",
            "HSV/VZV (sällsynt orsak)"
        ],
        "treatment": "Behandla underliggande infektion: syfilis: penicillin systemiskt, TB: antituberkulös behandling, Lyme: doxycyklin, Topikalt: steroider för inflammation, cykloplegika, behandla uveit om present, ghost vessels kräver ingen behandling, scarring kan kräva korneatransplantation",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Stromal HSV-keratit",
            "Sarkoid keratit",
            "Cogan's syndrom"
        ],
        "description": "Interstitiell keratit är djup stromal inflammation, historiskt vanligast vid kongenital syfilis (sällsynt nu). Ger djup neovaskularisation och scarring. 'Ghost vessels' är karakteristiska. Behandla underliggande infektion.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Kornealerosion (Corneal Abrasion)",
        "name_en": "Corneal Abrasion",
        "icd10": "S05.0",
        "symptoms": [
            "akut, svår ögonsmärta",
            "främmande kropps-känsla",
            "ljuskänslighet (fotophobi)",
            "tårflöde",
            "blefarospasm (ögonlockkramp)",
            "synnedsättning (om central)",
            "smärtan ofta värre vid blinking eller ögonöppning"
        ],
        "anamnesis_questions": [
            "Vad hände? Fick du något i ögat?",
            "Var det en skada med nagel, papper, gren, kontaktlins?",
            "Hur länge sedan hände det?",
            "Har du mycket smärta?",
            "Kan du öppna ögat?",
            "Ser du sämre?",
            "Använder du kontaktlinser?",
            "Har du haft liknande tidigare?"
        ],
        "clinical_signs": [
            "epitheldefekt synlig med fluorescein (grön färgning)",
            "konjunktival injektion",
            "tårfilm instabil",
            "kan ha främmande kropp (subtarsal!)",
            "anterior chamber reaction (mild, om stor abrasion)",
            "blefarospasm",
            "normal pupill (viktigt - uteslut penetrerande skada)"
        ],
        "risk_factors": [
            "trauma (finger, nagel, papper, gren, kontaktlins)",
            "kontaktlinsbärare (särskilt övernattning)",
            "arbete med slagverktyg (uteslut främmande kropp!)",
            "torrt ögon",
            "dystrofier (recidiverar lättare)"
        ],
        "treatment": "AKUT: Smärtlindring: topikala NSAID (ketorolac, diklofenak) OCH systemiska analgetika. Antibiotika: oftalmisk salva (kloramfenikol, fusidinsyra) för att förhindra infektion. Cykloplegika: ciklopentolat vid svår smärta/fotophobi (minskar ciliarspasm). INGEN bindel/lapp (ökar infektionsrisk). Kontaktlinsbärare: ALDRIG mono-antibiotika - använd fluorokinolon (ciprofloxacin/levofloxacin) pga Pseudomonas-risk. Uppföljning: små abrasioner (24-48h), stora abrasioner (24h OBLIGATORISKT). Läkning: små abrasioner läker på 24-48h, stora kan ta 3-5 dagar. VARNING: uteslut penetrerande skada, främmande kropp (speciellt subtarsal), kontaktlins-relaterad infektion. Bandage contact lens kan användas vid stora, smärtsamma abrasioner (endast av erfaren oftalmolog).",
        "kva": "AT001 (akut konsultation)",
        "differential_diagnoses": [
            "främmande kropp i cornea",
            "recidiverande kornealerosion",
            "infektiös keratit",
            "UV-keratit (svetsarbete)",
            "korneal främmande kropp under övre lock (subtarsal)"
        ],
        "description": "Kornealerosion är akut skada på kornealepitelet, vanligast trauma-relaterad. Mycket smärtsamt. Läker oftast på 24-48h med behandling. Risk för infektion, särskilt hos kontaktlinsbärare.",
        "severity": "mild-moderate",
        "urgency": "urgent (akut)"
    },
    {
        "name": "Recidiverande Kornealerosion (RCE)",
        "name_en": "Recurrent Corneal Erosion",
        "icd10": "H18.8",
        "symptoms": [
            "plötsliga, svåra ögonsmärta vid uppvaknande (klassiskt!)",
            "episodiska attacker av smärta, fotophobi, tårflöde",
            "symtom värst på morgonen (ögat torrt efter sömn)",
            "ofta historia av tidigare kornealerosion/trauma",
            "kan ha recidiv månader-åratal efter initial skada",
            "attackerna kan vara korta (timmar) eller pågå dagar"
        ],
        "anamnesis_questions": [
            "Vaknar du med plötslig ögonsmärta?",
            "Har du haft liknande episoder tidigare?",
            "Hade du en kornealerosion eller skada för länge sedan?",
            "Hur länge pågår attackerna?",
            "Hur ofta kommer de?",
            "Finns det familjehistoria av korneal sjukdom?",
            "Använder du smörjande droppar eller salva?"
        ],
        "clinical_signs": [
            "under attack: epitheldefekt (oftast samma plats som tidigare skada)",
            "fluorescein visar loose eller absent epitelet",
            "mellan attacker: kan vara helt normalt eller subtila förändringar",
            "negativ fluorescein (ingen erosion synlig mellan attacker)",
            "anterior basement membrane dystrophy (ABMD) kan coexistera",
            "mikrocystor, mapliknande linjer i epitelet"
        ],
        "risk_factors": [
            "tidigare kornealerosion/trauma (oftast fingernagelskada)",
            "anterior basement membrane dystrophy (ABMD/map-dot-fingerprint)",
            "dystrofier (Reis-Bücklers, lattice, granulär)",
            "diabetes",
            "torrt ögon",
            "kontaktlinsbärare"
        ],
        "treatment": "AKUT (vid attack): samma som kornealerosion - smärtlindring, antibiotika salva, cykloplegika. PROFYLAX (förhindra recidiv - VIKTIGT!): Hypertonisk salva (NaCl 5%) nattetid i 3-6 månader (drar vätska ut epitelet, förbättrar adhesion). Smörjande droppar dagligen + riklig salva nattetid (artificiella tårar). Behandla torrt ögon aggressivt. Bandage contact lens under akut episod. KIRURGI om medicinsk behandling misslyckas: anterior stromal puncture (nål skapar ärr som fixerar epitelet) - enkelt, kontor-procedur, effektivt för små centrala erosioner. Phototherapeutic keratectomy (PTK) - excimer laser avlägsnar onormalt basement membrane - effektivt men dyrare. Alkohol-delamination av epitelet (vid dystrofier). Framgång: 70-80% med hypertonisk salva, 90% med PTK. Långtidsuppföljning.",
        "kva": "CJF25 (PTK), CJE20 (stromal puncture)",
        "differential_diagnoses": [
            "akut kornealerosion (första gången)",
            "infektiös keratit",
            "anterior basement membrane dystrophy (ofta underliggande)",
            "torrt ögon med epiteliella defekter"
        ],
        "description": "Recidiverande kornealerosion är återkommande episoder av spontan epitelavlossning, oftast på morgonen. Orsakas av dålig epiteladhesion till basement membrane efter tidigare trauma eller vid dystrofier. Mycket smärtsamt men godartad.",
        "severity": "moderate",
        "urgency": "urgent (under attack)"
    },
    {
        "name": "Exponeringskeratopati (Exposure Keratopathy)",
        "name_en": "Exposure Keratopathy",
        "icd10": "H16.2",
        "symptoms": [
            "torrhet och irritation",
            "främmande kropps-känsla",
            "rodnad",
            "suddig syn",
            "smärta (om allvarlig)",
            "sår på hornhinnan (om kronisk)",
            "ofta värre på morgonen (exponering nattetid)",
            "kan vara asymtomatisk i tidiga stadier"
        ],
        "anamnesis_questions": [
            "Kan du blunda helt?",
            "Har du haft ansiktsförlamning eller stroke?",
            "Har du framträngande ögon (tyreoidea-sjukdom)?",
            "Sover du med ögonen öppna? (fråga partner)",
            "Vaknar du med torra, irriterade ögon?",
            "Har du haft ögonlockskirurgi?",
            "Har du eksem eller annan hudsjukdom?",
            "Är du medvetslös eller sövd på IVA? (för läkare)"
        ],
        "clinical_signs": [
            "lagophthalmos (ofullständig blunkning)",
            "SPK (superficiell punktat keratopati), ofta inferior",
            "fluorescein-färgning inferior cornea",
            "kan ha kornealulcus (om svår)",
            "torr, matt cornealyta",
            "förkortat tear break-up time",
            "konjunktival injektion",
            "i svåra fall: korneal perforation (sällsynt men allvarligt)"
        ],
        "risk_factors": [
            "facialispares (Bell's pares, stroke)",
            "Graves oftalmopati (proptosis)",
            "ektropion (utåtvänt ögonlock)",
            "ögonlocksretraktion",
            "nocturnal lagophthalmos (sover med ögat öppet)",
            "nedsatt medvetande/IVA-vård (inkomplett blunkning)",
            "post-blepharoplasty (kosmetisk ögonlockskirurgi)",
            "congenital lagophthalmos"
        ],
        "treatment": "BEHANDLINGSMÅL: skydda hornhinnan från exponering och uttorkning. MILD: Smörjande droppar frekvent dagtid (varje 1-2h), riklig salva nattetid, fuktkammare-glasögon, tapeband över ögat nattetid (om lagophthalmos). MÅTTLIG: Bandage contact lens (skyddar epitelet), behandla underliggande orsak (tyreoidea, facialispares), botulinum toxin till levator (sänker övre lock temporärt). SVÅR eller ULCUS: Tarsorafi (kirurgisk partial/komplett sys ihop av ögonlocken - temporärt eller permanent), vätska-fyllda chambers/Moisture chambers, autolog serum eyedrops. ÖGONLOCKSKIRURGI: lateral tarsal strip (vid ektropion), lateral canthal tightening, övre locksretraktion repair, gold weight implant i övre lock (vid kronisk facialispares). IVA-patienter: profylax med salva + ögonlock-tejp. VIKTIGT: behandla aggressivt - risk för perforation vid svår exponering.",
        "kva": "ACF00 (tarsorafi), ACF10 (ögonlockskirurgi)",
        "differential_diagnoses": [
            "torrt ögon (aqueous deficiency)",
            "neurotrofisk keratopati",
            "infektiös keratit",
            "limbal stem cell deficiency"
        ],
        "description": "Exponeringskeratopati orsakas av otillräcklig blunkning eller ögonlocksstängning, vilket leder till korneal uttorkning och skada. Kan vara mild (SPK) till svår (kornealulcus, perforation). Kräver aggressiv smörjning och ibland kirurgi.",
        "severity": "moderate-severe (severe om ulcus/perforation)",
        "urgency": "urgent (emergency om ulcus/perforation)"
    }
]
