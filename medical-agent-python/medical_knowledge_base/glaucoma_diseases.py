"""
Glaukom Sjukdomar - 25 vanligaste
"""

GLAUCOMA_DISEASES = [
    {
        "name": "Primär Öppenvinklat Glaukom (POAG)",
        "name_en": "Primary Open-Angle Glaucoma",
        "icd10": "H40.1",
        "symptoms": [
            "oftast asymtomatisk i tidiga stadier",
            "gradvis perifer synfältsinskränkning",
            "tunnelseende i sent stadium",
            "ingen smärta",
            "central syn bevarad länge"
        ],
        "anamnesis_questions": [
            "Har du glaukom i familjen?",
            "Har du högt ögontryck upptäckts tidigare?",
            "Märker du att du missar saker i periferin?",
            "Snublar du över saker?",
            "Använder du kortisonmedicin (tabletter, ögondroppar, inhalation)?",
            "Har du diabetes eller högt blodtryck?",
            "När mättes ögontrycket senast?"
        ],
        "clinical_signs": [
            "förhöjt ögontryck (>21 mmHg, men ej alltid)",
            "ökad cup/disc ratio (>0.6)",
            "vertikal cupping",
            "notching av neuroretinal rim",
            "RNFL-defekter (retinal nervfiberlager)",
            "öppen kammarvinkel vid gonioskopi",
            "synfältsdefekter (nasal step, arcuate scotoma, temporal wedge)",
            "asymmetri mellan ögonen"
        ],
        "risk_factors": [
            "högt ögontryck (viktigaste modifierbara)",
            "hög ålder (>60 år)",
            "familjehistoria (5x ökad risk)",
            "afrikanskt ursprung",
            "myopi",
            "tunn central hornhinna (<520 μm)",
            "stora cup/disc ratio",
            "diabetes",
            "kardiovaskulär sjukdom"
        ],
        "treatment": "Trycknedsättande ögondroppar (prostaglandinanaloger förstahandsval: latanoprost, tafluprost, travoprost), betablockerare (timolol), alfa-agonister (brimonidin), karboanhydrashämmare (dorzolamid), kombinationsdroppar vid otillräcklig effekt, laser trabekuloplastik (SLT) som alternativ/tillägg, trabekulektomi vid svårkontrollerat, måltryck individuellt (ofta <15-18 mmHg)",
        "kva": "CKA10",  # Trabekulektomi
        "differential_diagnoses": [
            "Normaltrycksglaukom",
            "Sekundärt glaukom",
            "Okulär hypertension (högt tryck utan skada)",
            "Fysiologisk stor excavation"
        ],
        "description": "POAG är den vanligaste glaukomformen (70-80%) med progressiv optikusneuropati trots öppen kammarvinkel. Tyst sjukdom - viktigt med screening hos riskgrupper.",
        "severity": "moderate-severe",
        "urgency": "routine"
    },
    {
        "name": "Normaltrycksglaukom (NTG)",
        "name_en": "Normal-Tension Glaucoma",
        "icd10": "H40.1",
        "symptoms": [
            "som POAG - oftast asymtomatisk",
            "gradvis synfältsinskränkning",
            "kan ha vaskulära symptom (kalla händer, migrän)"
        ],
        "anamnesis_questions": [
            "Har du lågt blodtryck?",
            "Har du migrän eller vasospastiska besvär?",
            "Har du sömnstörningar eller sömnapné?",
            "Har du kärlkramp eller tidigare hjärtinfarkt?",
            "Har du Raynauds fenomen (kalla fingrar)?",
            "Har du japanskt ursprung?"
        ],
        "clinical_signs": [
            "glaukom-skada (cupping, RNFL-defekt, synfältsdefekt)",
            "ögontryck konsekvent ≤21 mmHg",
            "öppen kammarvinkel",
            "ofta mer fokala/djupa notches i papillen",
            "disc hemorrhages vanligare än POAG",
            "ofta mer paracentral synfältspåverkan"
        ],
        "risk_factors": [
            "vaskulär dysregulation",
            "lågt blodtryck/nattlig hypotension",
            "migrän",
            "Raynauds fenomen",
            "sömnapné",
            "japanskt ursprung",
            "hög ålder",
            "kvinnligt kön"
        ],
        "treatment": "Trycknedsättande droppar (mål 30% tryckreduktion eller <12 mmHg), behandla vaskulära faktorer (sömnapné, hypotension), undvik nattliga blodtryckssänkande, överväg neuroprotection (kontroversiellt), samma droppbehandling som POAG men lägre måltryck, laser/kirurgi vid progression",
        "kva": "CKA10",
        "differential_diagnoses": [
            "POAG med missad trycktopp",
            "Sekundärt glaukom tidigare",
            "Icke-glaukomatös optikusneuropati",
            "Anteriör ischemisk optikusneuropati (AION)"
        ],
        "description": "NTG är glaukom med 'normalt' ögontryck. Mer vaskulär komponent. Vanligare i Asien (upp till 90% av glaukom i Japan). Kräver aggressiv trycknedsättning ändå.",
        "severity": "moderate-severe",
        "urgency": "routine"
    },
    {
        "name": "Primär Trångvinklat Glaukom - Akut (Akut Glaukom)",
        "name_en": "Acute Angle-Closure Glaucoma",
        "icd10": "H40.2",
        "symptoms": [
            "kraftig ögonsmärta",
            "huvudvärk (ofta halvsidig)",
            "illamående och kräkningar",
            "kraftigt nedsatt syn/suddig syn",
            "halos runt lampor",
            "rött öga"
        ],
        "anamnesis_questions": [
            "När började smärtan? (akut!)",
            "Har du kräkts?",
            "Ser du regnbågsfärgade ringar runt lampor?",
            "Har du haft liknande attacker tidigare?",
            "Är du översynt (hyperop)?",
            "Har du använt pupillvidgande medicin (antihistamin, urologiska)?",
            "Har du asiatiskt ursprung?"
        ],
        "clinical_signs": [
            "mycket högt ögontryck (40-80 mmHg)",
            "korneal ödem (grumlig hornhinna)",
            "injicerade konjunktivala kärl",
            "grund främre kammare",
            "medelwid, fixerad pupill",
            "sluten kammarvinkel vid gonioskopi",
            "eventuell sektor-iris atrofi efter attack"
        ],
        "risk_factors": [
            "hyperopi (översynthet)",
            "grund främre kammare",
            "tjock lins",
            "liten kornea",
            "asiatiskt ursprung (särskilt östasiatiskt)",
            "hög ålder",
            "kvinnligt kön",
            "pupillvidgande medicin",
            "mörker/skum belysning"
        ],
        "treatment": "AKUT! Sänk trycket omedelbart: pilokarpin 2% (efter initial trycksänkning), acetazolamid 500mg IV/PO, topikala trycknedsättande (timolol, brimonidin, dorzolamid), hyperosmotics (mannitol IV eller glykerin PO), smärtlindring och antiemetika, laser iridotomi AKUT (när tryck och inflammation sjunkit), profylaktisk iridotomi i andra ögat, kataraktkirurgi ofta bästa långsiktiga lösning",
        "kva": "CKD05",  # Laser iridotomi
        "differential_diagnoses": [
            "Akut konjunktivit (men ej högt tryck)",
            "Akut uveit (men oftast lågt tryck)",
            "Sekundärt trångvinkelglaukom",
            "Malign glaukom"
        ],
        "description": "Akut trångvinkelglaukom är en oftalmologisk NÖDSITUATION! Iris blockerar trabekelverket. Risk för permanent synförlust inom timmar-dagar. Kräver akut behandling.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Primär Trångvinklat Glaukom - Kronisk/Intermittent",
        "name_en": "Chronic/Intermittent Angle-Closure Glaucoma",
        "icd10": "H40.2",
        "symptoms": [
            "intermittenta episoder av suddighet",
            "milda halos runt lampor",
            "lätt huvudvärk eller ögonsmärta",
            "symptom ofta på kvällen/i mörker",
            "kan vara asymtomatisk mellan attacker"
        ],
        "anamnesis_questions": [
            "Har du återkommande episoder av suddig syn?",
            "Värre på kvällen eller i mörka rum?",
            "Ser du ibland regnbågsringar runt lampor?",
            "Lätta huvudvärk över ögat?",
            "Försvinner symptomen spontant?"
        ],
        "clinical_signs": [
            "grund främre kammare",
            "iridotrabecular contact (PAS) vid gonioskopi",
            "ögontryck kan vara normalt mellan attacker",
            "eventual glaukomskada vid kronisk form",
            "pigmentdeposition i kammarvinkel"
        ],
        "risk_factors": [
            "som akut trångvinkelglaukom",
            "hyperopi, grund kammare, asiatiskt ursprung"
        ],
        "treatment": "Laser iridotomi profylaktiskt (båda ögon), överväg tidig kataraktkirurgi, trycknedsättande droppar vid kronisk form med skada, undvik pupillvidgande medicin/situationer",
        "kva": "CKD05",
        "differential_diagnoses": [
            "Plateau iris",
            "Okulär hypertension",
            "Tidiga POAG"
        ],
        "description": "Intermittent trångvinkelglaukom ger återkommande subakuta attacker. Kronisk form utvecklas vid persisterande vinkelslutning. Laser iridotomi förebygger akuta attacker.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Plateau Iris Syndrom",
        "name_en": "Plateau Iris Syndrome",
        "icd10": "H40.2",
        "symptoms": [
            "liknande intermittent trångvinkelglaukom",
            "symptom kvarstår trots iridotomi",
            "oftast yngre patienter än typiskt trångvinkelglaukom"
        ],
        "anamnesis_questions": [
            "Har du fått laser iridotomi men fortfarande problem?",
            "Är du relativt ung för glaukom?",
            "Har du intermittenta symptom vid pupillvidgning?"
        ],
        "clinical_signs": [
            "patent iridotomi men kvarstående trång vinkel",
            "främre kammare centralt normal djup",
            "anteriort roterad ciliarutskott (UBM/OCT)",
            "plateauliknande iris-konfiguration",
            "vinkelslutning vid mydriasis"
        ],
        "risk_factors": [
            "yngre ålder (30-50 år)",
            "hyperopi",
            "tjock perifer iris",
            "anteriort roterade ciliarutskott"
        ],
        "treatment": "Laser iridotomi först, laser iridoplastik (ALPI) vid kvarstående risk, pilokarpin långtidsbehandling möjlig, undvik mydriasis, kataraktkirurgi eller lens extraction kan behövas",
        "kva": "CKD05",
        "differential_diagnoses": [
            "Primär trångvinkelglaukom",
            "Sekundär vinkelslutning"
        ],
        "description": "Plateau iris är en anatomisk variant med anteriort roterade ciliarutskott. Trångvinkelrisk kvarstår trots iridotomi. Kräver iridoplastik eller långtidspilokarpin.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Pseudoexfoliationsglaukom (PEX-glaukom)",
        "name_en": "Pseudoexfoliation Glaucoma",
        "icd10": "H40.1",
        "symptoms": [
            "som POAG - oftast asymtomatisk",
            "kan ha snabbare progression",
            "ofta högre ögontryck"
        ],
        "anamnesis_questions": [
            "Har du skandinaviskt ursprung?",
            "Har du opererat grå starr (kan vara komplicerad)?",
            "Varierar ditt ögontryck mycket?",
            "Har ögontrycket varit mycket högt?"
        ],
        "clinical_signs": [
            "vitt exfoliationsmaterial på främre linskap (target pattern)",
            "exfoliation på pupillkant",
            "pigmentdeposition i kammarvinkel (Sampaolesi line)",
            "zonulautsvagning",
            "ofta högre och mer fluktuerande tryck än POAG",
            "glaukomskada ofta mer avancerad vid diagnos",
            "fakodonesis (linsvackling) möjlig"
        ],
        "risk_factors": [
            "hög ålder",
            "skandinaviskt ursprung (vanligast)",
            "hereditet",
            "kardiovaskulär sjukdom möjligen"
        ],
        "treatment": "Aggressivare trycknedsättning än POAG (ofta behövs lägre måltryck), prostaglandinanaloger förstahandsval, kombinationsbehandling ofta nödvändig, SLT-laser ofta effektivt, trabekulektomi vid otillräcklig kontroll, var försiktig vid kataraktkirurgi (zonulasvagheter!)",
        "kva": "CKA10",
        "differential_diagnoses": [
            "POAG",
            "Pigmentdispersionsglaukom",
            "Sekundärt glaukom"
        ],
        "description": "PEX-glaukom är vanligaste sekundära glaukomet. Exfoliationsmaterial täpper till trabekelverket. Vanligast i Skandinavien. Ofta aggressivare förlopp än POAG.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Pigmentdispersionsglaukom/Pigmentglaukom",
        "name_en": "Pigmentary Glaucoma",
        "icd10": "H40.1",
        "symptoms": [
            "oftast asymtomatisk",
            "ibland halos efter träning/pupillvidgning",
            "episoder av suddig syn",
            "oftast unga myopa män"
        ],
        "anamnesis_questions": [
            "Är du myop (närsynt)?",
            "Är du man 20-50 år?",
            "Märker du suddig syn efter träning?",
            "Ser du halos ibland efter fysisk aktivitet?"
        ],
        "clinical_signs": [
            "Krukenberg spindle (vertikal pigmentdeposition på hornhinneendotel)",
            "radiära transilluminationsdefekter i perifer iris",
            "tät pigmentering av kammarvinkel",
            "posteriort böjd iris (konkav konfiguration)",
            "tryckstegringar efter träning/mydriasis",
            "glaukomskada vid pigmentglaukom"
        ],
        "risk_factors": [
            "myopi",
            "manligt kön",
            "ung ålder (20-50 år)",
            "kaukasiskt ursprung",
            "djup främre kammare",
            "posteriort böjd iris"
        ],
        "treatment": "Laser iridotomi (kontroversiellt men kan minska pigmentdispersion), trycknedsättande droppar vid glaukomskada, undvik kraftig fysisk aktivitet som utlöser tryckstegringar?, många utvecklar aldrig glaukomskada - observera noga, SLT kan vara mindre effektivt (redan mycket pigment)",
        "kva": "CKD05",
        "differential_diagnoses": [
            "POAG",
            "Pseudoexfoliationsglaukom",
            "Okulär hypertension"
        ],
        "description": "Pigmentdispersionssyndrom uppstår när iris gnider mot zonulae och frigör pigment. Pigmentglaukom utvecklas hos ca 50% med tryckstegring och skada. Typiskt: ung myop man.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Kongenitalt Glaukom (Infantilt Glaukom)",
        "name_en": "Congenital Glaucoma",
        "icd10": "Q15.0",
        "symptoms": [
            "tårrinnande (epifora)",
            "ljuskänslighet (fotophobi)",
            "ögonknipning (blefarospasm)",
            "grumlig kornea",
            "förstorat öga (buftalmus)",
            "föräldrar märker stort öga"
        ],
        "anamnesis_questions": [
            "Har barnet stora ögon?",
            "Rinner det tårar mycket?",
            "Är barnet ljuskänsligt?",
            "Kniper barnet ofta med ögonen?",
            "I vilken ålder började symptomen?",
            "Är hornhinnan grumlig?",
            "Finns konsanguinitet (släktskap föräldrar)?"
        ],
        "clinical_signs": [
            "förhöjt ögontryck",
            "förstorad kornea (>12 mm)",
            "korneal ödem och Haab's striae",
            "djup främre kammare",
            "buftalmus (förstorat öga)",
            "ökad cup/disc ratio",
            "myopisering",
            "dysgenesis av kammarvinkel"
        ],
        "risk_factors": [
            "hereditet (autosomalt recessivt oftast)",
            "consanguinitet",
            "CYP1B1-mutation vanligast",
            "sporadiska fall också"
        ],
        "treatment": "Kirurgi är primär behandling (goniotomi eller trabekulotomi), kombinerad trabekulotomi-trabekulektomi vid svåra fall, glaukomdränimplantat vid terapiresistent, droppar har begränsad effekt men används som tillägg, tidig diagnos och behandling kritisk för prognos, narkos vid undersökning och kirurgi",
        "kva": "CKA20",  # Goniotomi
        "differential_diagnoses": [
            "Megalocornea (stor kornea utan glaukom)",
            "Dakryostenoos (tårvägsstenosering)",
            "Kongenital korneal dystrofi",
            "Juvenilt glaukom (senare debut)"
        ],
        "description": "Kongenitalt glaukom är sällsynt (1:10000) men allvarligt tillstånd med defekt kammarvinkelutveckling. Klassisk triad: tårrinnande, fotophobi, blefarospasm. Kräver tidig kirurgi.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Juvenilt Glaukom",
        "name_en": "Juvenile Open-Angle Glaucoma",
        "icd10": "H40.1",
        "symptoms": [
            "oftast asymtomatisk",
            "kan upptäckas vid rutinkontroll",
            "eventuell myopisering"
        ],
        "anamnesis_questions": [
            "Hur gammal är patienten? (4-35 år)",
            "Finns glaukom i familjen?",
            "Har glasögonstyrkan ändrats (mot myopi)?",
            "Har högt ögontryck upptäckts?"
        ],
        "clinical_signs": [
            "högt ögontryck (ofta >30 mmHg)",
            "öppen kammarvinkel",
            "glaukomskada (cupping, synfältsdefekt)",
            "ingen annat sekundär orsak",
            "ofta stor cup/disc ratio"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant oftast)",
            "MYOC-genmutation vanlig",
            "familjehistoria"
        ],
        "treatment": "Aggressiv medicinsk behandling, ofta behövs kirurgi (trabekulektomi) tidigt, droppar ofta otillräckliga vid mycket höga tryck, livslång uppföljning kritisk, genetisk rådgivning",
        "kva": "CKA10",
        "differential_diagnoses": [
            "Sekundärt glaukom (uveit, trauma, steroid)",
            "POAG med tidig debut",
            "Kongenitalt glaukom sent diagnosticerat"
        ],
        "description": "Juvenilt glaukom debuterar mellan kongenitalt och POAG (4-35 år). Ofta hereditet med MYOC-mutation. Höga tryck kräver ofta tidig kirurgi.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Steroidinducerat Glaukom",
        "name_en": "Steroid-Induced Glaucoma",
        "icd10": "H40.6",
        "symptoms": [
            "oftast asymtomatisk",
            "gradvis synnedsättning vid långvarig steroidbehandling",
            "symptom som POAG"
        ],
        "anamnesis_questions": [
            "Använder du kortisonögondroppar?",
            "Hur länge har du använt steroiddroppar?",
            "Använder du nässpray med kortison?",
            "Tar du kortisontabletter?",
            "Använder du inhalatorer med steroider?",
            "Har du fått steroidinjektion i ögat?",
            "Har du astma eller allergi som behandlas med steroider?"
        ],
        "clinical_signs": [
            "förhöjt ögontryck (kan vara mycket högt)",
            "öppen kammarvinkel",
            "glaukomskada vid långvarig exponering",
            "reversibelt om upptäcks tidigt",
            "steroid responders: ~30% befolkningen"
        ],
        "risk_factors": [
            "steroidbehandling (lokal eller systemisk)",
            "hög steroidpotens (dexametason, betamethason värst)",
            "lång behandlingstid",
            "hereditet för steroid-respons",
            "POAG eller familjehistoria av glaukom",
            "diabetes",
            "höga myopi",
            "barn och äldre mer känsliga"
        ],
        "treatment": "PRIMÄRT: avsluta eller minska steroidbehandling, byt till lågpotent steroid (fluorometolon) eller steroid-sparande (NSAID, immunosuppressiva), trycknedsättande droppar vid behov, trycket normaliseras ofta inom veckor efter steroidavbrott, permanent skada vid långvarig exponering, övervaka tryck vid all steroidbehandling >2 veckor",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "POAG (men historia av steroid!)",
            "Okulär hypertension"
        ],
        "description": "Steroidinducerat glaukom är viktigt att känna till - ca 30% är 'steroid responders'. Särskilt farligt vid ointment eller depotinjektioner. Tryckmätning obligatorisk vid steroidbehandling!",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Uveitiskt Glaukom",
        "name_en": "Uveitic Glaucoma",
        "icd10": "H40.4",
        "symptoms": [
            "rött, smärtsamt öga (uveit)",
            "synnedsättning",
            "fotophobi",
            "kan ha högt eller lågt tryck beroende på fas"
        ],
        "anamnesis_questions": [
            "Har du inflammation i ögat (uveit)?",
            "Har du autoimmun sjukdom?",
            "Har du Bechterews, sarkoidos eller JIA?",
            "Används steroiddroppar?",
            "Har du haft återkommande röda ögon?"
        ],
        "clinical_signs": [
            "tecken på uveit: cellreaktion, KP, synechiae",
            "förhöjt tryck (trabekulit eller steroidinducerat)",
            "eller lågt tryck (ciliarkropps avstängning)",
            "posteriora synechiae kan ge pupillblock",
            "PAS (perifera anteriora synechiae) kan ge vinkelslutning",
            "sekundär trångvinkel möjlig"
        ],
        "risk_factors": [
            "kronisk eller recidiverande uveit",
            "Fuchs heterokrom iridocyklit (ofta högt tryck)",
            "juvenil idiopatisk artrit (JIA)",
            "sarkoidos",
            "Bechterews (ankyloserande spondylit)",
            "herpesuveit"
        ],
        "treatment": "Behandla underliggande uveit aggressivt (steroider, immunosuppression), cykloplegika (atropin, homatropin) för att förhindra synechiae, trycknedsättande droppar (undvik prostaglandiner vid aktiv inflammation!), laser iridotomi vid pupillblock, kirurgi ofta riskabelt - vänta till inflammation lugn, behandla både inflammation OCH tryck samtidigt",
        "kva": "Varierar beroende på behandling",
        "differential_diagnoses": [
            "POAG (men historia av uveit!)",
            "Steroidinducerat glaukom",
            "Akut trångvinkelglaukom"
        ],
        "description": "Uveitiskt glaukom är komplext - både lågt tryck (akut uveit) och högt tryck (trabekulit, steroidbehandling, synechiae) möjligt. Kräver behandling av både inflammation och tryck.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Neovaskulärt Glaukom (Rubeotiskt Glaukom)",
        "name_en": "Neovascular Glaucoma",
        "icd10": "H40.4",
        "symptoms": [
            "kraftig ögonsmärta",
            "kraftigt nedsatt syn",
            "rött öga",
            "ofta historia av diabetesretinopati eller venockklusion"
        ],
        "anamnesis_questions": [
            "Har du diabetes med ögonpåverkan?",
            "Har du haft blodpropp i ögat (venockklusion)?",
            "Har du fått laserbehandling i ögat?",
            "Har du mycket dålig syn sedan tidigare?",
            "Har du smärta i ögat?"
        ],
        "clinical_signs": [
            "neovaskulationer på iris (rubeosis iridis)",
            "neovaskulationer i kammarvinkel",
            "mycket högt ögontryck (ofta >40 mmHg)",
            "korneal ödem",
            "hyphema möjlig",
            "ektropion uvea",
            "underliggande retinal ischemi (PDR, CRVO)"
        ],
        "risk_factors": [
            "proliferativ diabetesretinopati (PDR)",
            "central retinal venockklusion (CRVO) - ischemisk typ",
            "ocular ischemic syndrome",
            "retinal avlossning (långvarig)",
            "intraokulär tumör"
        ],
        "treatment": "Behandla underliggande orsak: panretinal laserkoagulation (PRP) AKUT vid PDR/CRVO, intravitreal anti-VEGF (bevacizumab) kan regridera neovaskulationer, aggressiv trycknedsättning (aqueous suppressants, systemiska CAI), cyklodiod laser (destruktiv behandling) vid refraktär glaukom, glaukomdränimplantat vid kirurgi, smärtlindring viktigt, dålig prognos för syn",
        "kva": "CKD96",  # Panretinal fotokoagulation
        "differential_diagnoses": [
            "Akut trångvinkelglaukom",
            "Uveitiskt glaukom",
            "Trauma-glaukom"
        ],
        "description": "Neovaskulärt glaukom är ett svårt sekundärglaukom orsakat av retinal ischemi. '100-dagars glaukom' efter CRVO. Mycket smärtsamt med dålig prognos. Kräver aggressiv behandling av både retina och glaukom.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Traumatiskt Glaukom",
        "name_en": "Traumatic Glaucoma",
        "icd10": "H40.3",
        "symptoms": [
            "historia av ögontrauma",
            "varierar beroende på mekanism",
            "kan vara akut eller kronisk",
            "smärta, synnedsättning beroende på skada"
        ],
        "anamnesis_questions": [
            "Har du haft skada mot ögat?",
            "Vad träffades ögat av?",
            "Blev det blod i ögat efter skadan?",
            "Hur länge sedan var traumat?",
            "Har du haft operation efter skadan?"
        ],
        "clinical_signs": [
            "akut: hyphema (blod i främre kammaren), vinkelblödning",
            "akut: recessionsskada av kammarvinkel",
            "kronisk: PAS (synechiae), vinkelslutning",
            "förhöjt tryck akut (blod, inflammation) eller kroniskt (vinkelpåverkan)",
            "linsluxation möjlig",
            "retinal/choroidal avlossning möjlig"
        ],
        "risk_factors": [
            "trubbigt ögontrauma",
            "penetrerande skada",
            "hyphema",
            "omfattande vinkelrecession (>180°)"
        ],
        "treatment": "Akut hyphema: sängvila med huvudända 30°, cykloplegika, steroider, trycknedsättande (undvik prostaglandiner och miotika), AC-paracentesis vid mycket högt tryck/corneal bloodstaining, kirurgi vid kroniskt glaukom (vinkelskador läker ej), långtidsuppföljning livslångt (glaukom kan komma decennier senare)",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Akut trångvinkelglaukom",
            "Glaukom av annan orsak"
        ],
        "description": "Traumatiskt glaukom kan vara akut (hyphema, inflammation) eller kroniskt (vinkelskador, synechiae). Viktigt: även lätta trauman kan ge sent glaukom. Livslång uppföljning efter betydande trauma!",
        "severity": "moderate-severe",
        "urgency": "emergency (akut), urgent (kronisk)"
    },
    {
        "name": "Fakolytiskt Glaukom",
        "name_en": "Phacolytic Glaucoma",
        "icd10": "H40.4",
        "symptoms": [
            "akut ögonsmärta",
            "kraftig synnedsättning",
            "rött öga",
            "historia av hypermaturt katarakt"
        ],
        "anamnesis_questions": [
            "Har du mycket mogen grå starr?",
            "Har du väntat länge med starroperationen?",
            "Fick du plötslig försämring och smärta?"
        ],
        "clinical_signs": [
            "hypermaturt/morgensomt katarakt",
            "vita partiklar i främre kammaren (linsprotein)",
            "cellreaktion i främre kammaren",
            "högt ögontryck",
            "öppen kammarvinkel"
        ],
        "risk_factors": [
            "övermaturt katarakt",
            "länge väntat med starrkirurgi",
            "traumatiserad lins"
        ],
        "treatment": "Kataraktkirurgi så snart möjligt (kuratativ!), trycknedsättande droppar preoperativt, steroider för inflammation, god prognos efter operation",
        "kva": "CJE00",  # Kataraktkirurgi
        "differential_diagnoses": [
            "Fakoanafylaktiskt glaukom",
            "Uveitiskt glaukom",
            "Akut trångvinkelglaukom"
        ],
        "description": "Fakolytiskt glaukom uppstår när linsprotein från övermaturt katarakt läcker ut och täpper till trabekelverket. Kataraktkirurgi är behandling.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Fakomorft Glaukom",
        "name_en": "Phacomorphic Glaucoma",
        "icd10": "H40.4",
        "symptoms": [
            "akut ögonsmärta",
            "synnedsättning",
            "rött öga",
            "halos runt lampor"
        ],
        "anamnesis_questions": [
            "Har du mogen grå starr?",
            "Har du fått plötsligt smärtsamt öga?",
            "Är du översynt?"
        ],
        "clinical_signs": [
            "intumescent (svullnad) katarakt",
            "grund främre kammare",
            "sekundär vinkelslutning (linsen trycker iris framåt)",
            "högt ögontryck",
            "sluten kammarvinkel vid gonioskopi"
        ],
        "risk_factors": [
            "mogen katarakt",
            "hyperopi",
            "grund främre kammare"
        ],
        "treatment": "Sänk tryck medicinskt först (som akut trångvinkelglaukom), laser iridotomi kan ge temporär lindring, kataraktkirurgi är definitiv behandling, operation när inflammation/tryck kontrollerat",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Akut trångvinkelglaukom",
            "Linsluxation"
        ],
        "description": "Fakomorft glaukom uppstår när svullande katarakt skjuter fram iris och stänger kammarvinkeln. Sekundärt trångvinkelglaukom. Kataraktoperation kurativ.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Linsluxation med Glaukom",
        "name_en": "Lens Dislocation with Glaucoma",
        "icd10": "H40.4",
        "symptoms": [
            "plötslig synnedsättning",
            "diplopi monokulär",
            "eventuell ögonsmärta",
            "historia av trauma eller Marfan"
        ],
        "anamnesis_questions": [
            "Har du Marfans syndrom?",
            "Har du homocystinuri?",
            "Har du haft ögontrauma?",
            "Har du märkt att linsen sitter fel?",
            "Ser du dubbelt med ett öga?"
        ],
        "clinical_signs": [
            "linsen i främre kammaren (anterior luxation) eller",
            "linsen i glaskroppen (posterior luxation) eller",
            "subluxerad lins (partiell luxation)",
            "högt tryck vid pupillblock eller",
            "högt tryck vid direkt trabekulär påverkan",
            "fakodonesis (linsvackling)"
        ],
        "risk_factors": [
            "Marfans syndrom",
            "homocystinuri",
            "Weill-Marchesani syndrom",
            "trauma",
            "pseudoexfoliation med zonulasvagheter"
        ],
        "treatment": "Anterior luxation: akut pupillkonstriktion (pilokarpin) eller mydriasis för att flytta bort lins från pupillen, laser iridotomi om pupillblock, linsextraktion kirurgiskt, posterior luxation: observation om asymtomatisk, eller vitrektomi med lensectomy, hantera underliggande syndrom",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Akut trångvinkelglaukom",
            "Pupillblock av annan orsak"
        ],
        "description": "Linsluxation kan ge pupillblock (högt tryck) eller direkt skada på trabekelverket. Marfan och trauma vanliga orsaker. Kräver ofta kirurgisk lensextraktion.",
        "severity": "severe",
        "urgency": "emergency (anterior), urgent (posterior)"
    },
    {
        "name": "Malign Glaukom (Aqueous Misdirection)",
        "name_en": "Malignant Glaucoma",
        "icd10": "H40.8",
        "symptoms": [
            "ögonsmärta",
            "synnedsättning",
            "oftast efter glaukomkirurgi eller kataraktkirurgi",
            "plötsligt högt tryck trots patent iridotomi"
        ],
        "anamnesis_questions": [
            "Har du opererats för glaukom nyligen?",
            "Har du opererats för grå starr?",
            "Hade du trångvinkelglaukom tidigare?",
            "Är du hyperop?"
        ],
        "clinical_signs": [
            "grund eller flat främre kammare i HELA kammaren",
            "högt ögontryck",
            "patent iridotomi (om gjort)",
            "glaskroppen/ciliarkroppen trycker linsen framåt",
            "kammarvatska dirigeras felaktigt bakåt i glaskroppen"
        ],
        "risk_factors": [
            "tidigare trångvinkelglaukom",
            "hyperopi",
            "kort axiallängd",
            "efter glaukomkirurgi",
            "efter kataraktkirurgi"
        ],
        "treatment": "Medicinskt först: aggressiv cykloplegia (atropin 1% 2x dagligen), hyperosmotics (mannitol IV), aqueous suppressants (CAI, betablockerare), Nd:YAG-laser: hyaloidotomi/zonulolysis/capsulotomi, vitrektomi om medicinsk behandling misslyckas, lens extraction ofta kurativ, undvik miotika (pilokarpin försvärra!)",
        "kva": "CJE20",  # Vitrektomi
        "differential_diagnoses": [
            "Akut trångvinkelglaukom",
            "Pupillblock",
            "Koroidal effusion/avlossning",
            "Suprachoroidal blödning"
        ],
        "description": "Malign glaukom är sällsynt men allvarlig komplikation efter ögonkirurgi. Kammarvatten dirigeras bakåt i glaskroppen istället för framåt. Kräver aggressiv cykloplegia och ofta vitrektomi.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Posner-Schlossman Syndrom (Glaukomatocyklitisk Kris)",
        "name_en": "Posner-Schlossman Syndrome",
        "icd10": "H20.8",
        "symptoms": [
            "återkommande episoder",
            "ensidig suddig syn",
            "halos runt lampor",
            "lätt obehag (ej kraftig smärta)",
            "episoder varar dagar-veckor"
        ],
        "anamnesis_questions": [
            "Har du haft återkommande episoder av högt ögontryck?",
            "Påverkas bara ett öga?",
            "Ser du halos runt lampor under episoderna?",
            "Har du minimal smärta trots högt tryck?",
            "Är episoderna självläkande?"
        ],
        "clinical_signs": [
            "mycket högt ögontryck (ofta 40-60 mmHg) under attack",
            "minimal inflammation (få celler i främre kammaren)",
            "små vita KP (keratiska precipitat)",
            "öppen kammarvinkel",
            "ensidig (90%)",
            "episoder självlimiterade",
            "mellan attacker: normalt tryck, ingen inflammation"
        ],
        "risk_factors": [
            "CMV (cytomegalovirus) - funnen i kammarvatten hos många",
            "ålder 20-50 år",
            "manligt kön (liten övervikt)",
            "oklar etiologi men trolig viral"
        ],
        "treatment": "Under attack: trycknedsättande droppar, steroider (mild dosering), behandling ofta behövs bara kort tid, antivirala (ganciklovir, valganciklovir) vid CMV-positiv - kan minska recidiv, profylax med antivirala om frekventa recidiv, god prognos men kan utveckla glaukom vid upprepade attacker",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Akut trångvinkelglaukom (men öppen vinkel)",
            "Fuchs heterokrom iridocyklit",
            "Herpes-uveit",
            "Intermittent trångvinkelglaukom"
        ],
        "description": "Posner-Schlossman är återkommande episoder av mycket högt tryck med minimal inflammation. Troligen CMV-relaterad. God prognos men upprepade attacker kan ge permanent glaukom.",
        "severity": "moderate",
        "urgency": "urgent (under attack)"
    },
    {
        "name": "Fuchs Heterokrom Iridocyklit med Glaukom",
        "name_en": "Fuchs Heterochromic Iridocyclitis with Glaucoma",
        "icd10": "H20.8",
        "symptoms": [
            "oftast asymtomatisk",
            "gradvis synnedsättning",
            "flygers",
            "heterokromi (olika irisfärg) kan märkas"
        ],
        "anamnesis_questions": [
            "Har du olika färg på iris i de två ögonen?",
            "Har du haft långvarig inflammation utan smärta?",
            "Ser du flygers?",
            "Är bara ett öga påverkat?"
        ],
        "clinical_signs": [
            "iris heterokromi (påverkat öga ljusare)",
            "små stella KP över hela kornea",
            "minimal cellreaktion",
            "inga synechiae",
            "glaukom utvecklas hos 10-15%",
            "katarakt vanlig",
            "glaskroppsblödning vid kirurgi (iris neovaskulationer)",
            "ensidig"
        ],
        "risk_factors": [
            "okänd etiologi",
            "möjligen viral (rubella kongenitalt, HSV, CMV)",
            "sporadisk",
            "ung till medelålder"
        ],
        "treatment": "Steroider har minimal effekt och behövs sällan, behandla glaukom om utvecklas (droppar, SLT, kirurgi), kataraktkirurgi när behövs (risk för blödning!), god prognos generellt, inflammation oftast mild och kräver ingen behandling",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Posner-Schlossman syndrom",
            "Kronisk uveit av annan orsak",
            "Pigmentdispersionssyndrom"
        ],
        "description": "Fuchs heterokrom iridocyklit är en mild kronisk unilateral uveit med karakteristisk iris-depigmentering. Ofta asymtomatisk. Glaukom utvecklas hos 10-15%. God prognos.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "ICE-syndrom (Iridocorneal Endothelial Syndrome)",
        "name_en": "ICE Syndrome",
        "icd10": "H40.4",
        "symptoms": [
            "gradvis synnedsättning",
            "märker förändrad pupill eller iris",
            "ensidig",
            "oftast kvinnor 20-50 år"
        ],
        "anamnesis_questions": [
            "Har du märkt att pupillen ser annorlunda ut?",
            "Har iris förändrats?",
            "Påverkas bara ett öga?",
            "Är du kvinna 20-50 år?"
        ],
        "clinical_signs": [
            "hornhinneendotelförändringar (hammered silver/ICE cells)",
            "PAS (perifera anteriora synechiae)",
            "irisförändringar: atrofi, hål, corectopi (pupillförvrängning)",
            "tre subtyper: Chandlers, progressiv iris atrofi, Cogan-Reese (iris nevus)",
            "sekundärt glaukom vanligt (50%)",
            "korneal ödem möjligt"
        ],
        "risk_factors": [
            "okänd etiologi",
            "möjligen viral (HSV)",
            "kvinnligt kön",
            "ålder 20-50 år",
            "sporadisk"
        ],
        "treatment": "Trycknedsättande droppar vid glaukom, glaukomkirurgi ofta behövs (trabekulektomi, dränimplantat), hornhinnetransplantation vid korneal ödem, laser iridotomi ineffektivt (synechiae progressiva), prognos varierande - vissa progressiva",
        "kva": "CKA10",
        "differential_diagnoses": [
            "Axenfeld-Rieger syndrom",
            "Posterior polymorf hornhinnedystrofi",
            "Trångvinkelglaukom"
        ],
        "description": "ICE-syndrom är en grupp sällsynta tillstånd med hornhinneendotelavvikelser som växer över kammarvinkeln och iris. Unilateral hos kvinnor 20-50 år. Ofta svårkontrollerat glaukom.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Okulär Hypertension",
        "name_en": "Ocular Hypertension",
        "icd10": "H40.0",
        "symptoms": [
            "asymtomatisk",
            "högt tryck upptäckt vid rutinkontroll"
        ],
        "anamnesis_questions": [
            "Har högt ögontryck upptäckts?",
            "Finns glaukom i familjen?",
            "Har du diabetes eller högt blodtryck?",
            "Använder du steroider?"
        ],
        "clinical_signs": [
            "ögontryck >21 mmHg (ofta 22-28 mmHg)",
            "normal papill (cup/disc <0.5)",
            "normalt RNFL",
            "normalt synfält",
            "INGEN glaukomskada"
        ],
        "risk_factors": [
            "tjock central hornhinna (>600 μm)",
            "hög ålder",
            "afrikanskt ursprung",
            "familjehistoria av glaukom",
            "myopi",
            "diabetes"
        ],
        "treatment": "Observation oftast tillräckligt (lågrisk patienter), behandling om högrisk (tunna hornhinna, hög ålder, familjehistoria, mycket högt tryck >30 mmHg), OHTS-studien: 10% utvecklar glaukom på 5 år utan behandling, behandling halverar risk, kontroller 6-12 månader med tryckmätning, OCT, synfält",
        "kva": "Ingen (observation)",
        "differential_diagnoses": [
            "Tidigt POAG",
            "Sekundärt glaukom (uteslut!)",
            "Normalt tryck med tjock hornhinna"
        ],
        "description": "Okulär hypertension är högt ögontryck UTAN glaukomskada. Riskfaktor för att utveckla glaukom (10% på 5 år). Kräver observation och riskstratifiering. Behandling vid högriskpatienter.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Sekundärt Glaukom efter Vitreoretinal Kirurgi",
        "name_en": "Secondary Glaucoma Post-Vitrectomy",
        "icd10": "H40.5",
        "symptoms": [
            "symtom efter vitrektomi",
            "ögonsmärta eller obehag",
            "synnedsättning",
            "beroende på orsak"
        ],
        "anamnesis_questions": [
            "Har du opererats med vitrektomi?",
            "Fick du gasbubbla eller silikonomja?",
            "Hur länge sedan var operationen?",
            "Har du haft inflammation efter operation?"
        ],
        "clinical_signs": [
            "förhöjt tryck efter vitrektomi",
            "orsaker: gasbubbla (pupillblock), silikonomja i främre kammaren, inflammation, steroidbehandling postop, neovaskulationer",
            "beroende på mekanism olika fynd"
        ],
        "risk_factors": [
            "gasbubbla (C3F8, SF6) - pupillblock",
            "silikonomja - särskilt om afak",
            "postoperativ inflammation",
            "neovaskulationer vid diabetes/ischemisk retina",
            "steroidbehandling postop"
        ],
        "treatment": "Gas-relaterat: laser iridotomi profylaktiskt, mydriasis för att förhindra pupillblock, silikon-relaterat: avlägsna silikon från främre kammaren, eventuell silikon removal senare, inflammation: steroider + trycknedsättande, neovaskulationer: anti-VEGF + trycknedsättande, kirurgi vid refraktär",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Malign glaukom",
            "Akut trångvinkelglaukom",
            "Steroidinducerat glaukom"
        ],
        "description": "Glaukom efter vitrektomi har många orsaker: gas, silikon, inflammation, neovaskulationer, steroider. Kräver identifiering av orsak och specifik behandling. Profylaktisk iridotomi vid gas.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Vinkelrecessions-Glaukom (Angle Recession Glaucoma)",
        "name_en": "Angle Recession Glaucoma",
        "icd10": "H40.3",
        "symptoms": [
            "ofta asymtomatisk tidigt",
            "gradvis synförlust (sent)",
            "historia av ögontrauma (kan vara åratal sedan)",
            "ofta unilateralt",
            "inga akuta symtom"
        ],
        "anamnesis_questions": [
            "Har du haft trauma mot ögat? När?",
            "Vilken typ av trauma? (trubbigt slag mest vanligt)",
            "Har du märkt synförsämring?",
            "Har du smärta eller rodnad?",
            "Har du haft högt ögontryck tidigare?",
            "Använder du trycknedsättande droppar?"
        ],
        "clinical_signs": [
            "förhöjt IOP (oftast måttligt förhöjt, 25-35 mmHg)",
            "gonioskopi: vinkelrecession (ciliarkropp synlig, sliten iris vid basen)",
            "ofta >180 grader recession för glaukom",
            "glaukomatös optikusskada",
            "synfältsdefekter",
            "kan ha andra traumatecken: cataract, subluxerad lins, iridodialys"
        ],
        "risk_factors": [
            "trubbigt ögontrauma (oftast sportverletzningar, slag)",
            "tid sedan trauma (kan utvecklas månader-åratal senare)",
            "grad av vinkelrecession (>180 grader högre risk)",
            "unilateralt trauma"
        ],
        "treatment": "Medicinsk behandling: prostaglandinanalog, beta-blockerare, CAI (topikalt eller systemiskt), alpha-agonister. Ofta svårbehandlat och kräver flera läkemedel. Laser trabekuloplastik (SLT/ALT) - varierande resultat, ofta mindre effektivt än vid POAG. KIRURGI om medicinsk behandling otillräcklig: trabekulektomi eller glaukom drainage devices (tube shunts) - tube shunts ofta föredragna pga tidigare trauma. Livslång uppföljning. Viktigt: jämför alltid med andra ögat (asymmetri i IOP och optikusskada). Behandla aggressivt - glaukomskadan kan progressera snabbt.",
        "kva": "CJE96 (gonioskopi), CJF30 (trabekulektomi)",
        "differential_diagnoses": [
            "primär öppenvinklat glaukom (men historia av trauma)",
            "traumatisk katarakt med sekundärt glaukom",
            "glaukom vid linsluxation",
            "steroidglaukom (om steroider använts efter trauma)"
        ],
        "description": "Vinkelrecessions-glaukom uppstår efter trubbigt ögontrauma som skadar trabekulärt meshwork och ciliarkropp. Kan utvecklas åratal efter trauma. Diagnos med gonioskopi.",
        "severity": "moderate-severe",
        "urgency": "routine (men behandla när diagnostiserat)"
    },
    {
        "name": "Plateau Iris Syndrom",
        "name_en": "Plateau Iris Syndrome",
        "icd10": "H40.2",
        "symptoms": [
            "intermittenta episoder av suddig syn och halo",
            "lätt huvudvärk eller ögonsmärta",
            "symtom kan utlösas av mydriasis (mörker, pupilldilaterande droger)",
            "ofta unga till medelålders patienter",
            "symtom liknar trångvinkelglaukom men mildare"
        ],
        "anamnesis_questions": [
            "Har du haft episoder av suddig syn eller halo runt ljus?",
            "Kommer besvären i mörker eller efter pupilldilation?",
            "Har du haft laser iridotomi tidigare?",
            "Har du fortfarande symtom efter iridotomi?",
            "Är du närsint eller översint?",
            "Finns det familjehistoria av glaukom?"
        ],
        "clinical_signs": [
            "patent laser iridotomi (pupillblock är eliminerat)",
            "trång kammarvinkel trots patent iridotomi",
            "gonioskopi: plateau iris konfiguration (irisinsertion framåt, plan iris)",
            "UBM (ultrasound biomicroscopy): framåtrotererade ciliarprocesser",
            "normalt eller förhöjt IOP",
            "normal eller grund främre kammare",
            "ofta hypermetropi (översynthet)"
        ],
        "risk_factors": [
            "hypermetropi",
            "kort axellängd",
            "tjock perifer iris",
            "anteriorläge av ciliarkropp",
            "yngre ålder jämfört med vanligt trångvinkelglaukom",
            "asiatiskt ursprung (högre prevalens)"
        ],
        "treatment": "FÖRSTA LINJE: laser iridotomi (för att utesluta pupillblock-komponent). Efter iridotomi, om vinkel fortfarande trång: Laser peripheral iridoplasty (LPIP/gonioplasty) - argonlaser kontraherar perifera iris, öppnar vinkeln. Medicinsk behandling: pilokarpin (konstringerar pupillen, öppnar vinkeln), undvik mydriasis-utlösande droger, trycknedsättande medicin om IOP förhöjt. KIRURGI om refraktär: lens extraction (kataraktkirurgi) även hos unga kan öppna vinkeln dramatiskt (kontroversiellt men alltmer accepterat), trabekulektomi eller tube shunt om kirurgi behövs. Långtidsuppföljning: gonioskopi årligen, risk för akut attack om obehandlad.",
        "kva": "CJF05 (laser iridotomi), CJF06 (laser iridoplasti), CJE96 (gonioskopi + UBM)",
        "differential_diagnoses": [
            "primärt trångvinkelglaukom med pupillblock",
            "creeping angle closure (kronisk trångvinkel utan plateau)",
            "malign glaukom",
            "ciliokroidal effusion med vinkelstängning"
        ],
        "description": "Plateau iris är en anatomisk konfiguration där framåtrotererade ciliarprocesser skjuter perifera iris framåt, trots att pupillblock är eliminerat. Kan ge intermittenta angle closure episoder.",
        "severity": "moderate",
        "urgency": "urgent (om akuta episoder)"
    },
    {
        "name": "Steroidinducerat Glaukom",
        "name_en": "Steroid-Induced Glaucoma",
        "icd10": "H40.6",
        "symptoms": [
            "oftaymptomatisk (smygande)",
            "gradvis synförlust",
            "inga smärtor eller rodnad",
            "historia av steroidanvändning (ögondroppar, topikalt på hud, inhalation, systemiskt, intravitreala injektioner)"
        ],
        "anamnesis_questions": [
            "Använder du steroidögondroppar? Hur länge?",
            "Har du fått steroidinjektioner i ögat?",
            "Använder du steroidkräm runt ögonen?",
            "Använder du inhalationssteroider för astma/KOL?",
            "Tar du steroider i tablettform (prednisolon)?",
            "När började du med steroider och har trycket mätts sedan dess?",
            "Finns det familjehistoria av glaukom?"
        ],
        "clinical_signs": [
            "förhöjt IOP (kan vara kraftigt förhöjt, >30 mmHg)",
            "öppen kammarvinkel vid gonioskopi",
            "glaukomatös optikusskada (om långvarig exponering)",
            "synfältsdefekter (vid etablerad skada)",
            "inga inflammatoriska tecken (viktigt skiljetecken från uveitisk glaukom)"
        ],
        "risk_factors": [
            "genetisk predisposition (steroid responders - 30-40% av befolkningen)",
            "POAG eller familjehistoria av glaukom (högre risk)",
            "diabetes",
            "höggradmyopi",
            "barn (högre känslighet)",
            "längd och potens av steroidbehandling",
            "intravitreala steroidimplantat (Ozurdex, Iluvien) - hög risk"
        ],
        "treatment": "PRIMÄRT: AVBRYT eller MINSKA steroiddos om medicinskt möjligt (samråd med förskrivande läkare). Byt till lägpotent steroid eller steroid-sparande alternativ (t.ex. immunsuppressiva vid uveit, anti-VEGF istället för steroid vid makulaödem). Trycknedsättande behandling: prostaglandinanalog, beta-blockerare, CAI, alpha-agonister - behandla som POAG. IOP normaliseras ofta inom veckor-månader efter steroidutsättning, men kan kräva längre tid. Intravitreala implantat: överväg kirurgisk borttagning om möjligt och IOP okontrollerbart. KIRURGI om medicinsk behandling otillräcklig eller implant finns kvar: trabekulektomi, tube shunt. VIKTIGT: Screena IOP regelbundet hos alla patienter på steroider (särskilt långtidsbehandling).",
        "kva": "AT001 (tryckmätning och uppföljning)",
        "differential_diagnoses": [
            "primär öppenvinklat glaukom",
            "uveitiskt glaukom (men steroidglaukom har INGEN inflammation)",
            "traumatiskt glaukom",
            "neovaskulärt glaukom"
        ],
        "description": "Steroidinducerat glaukom orsakas av ökad resistans i trabekulärt meshwork vid steroidexponering. Kan uppstå efter topikala, systemiska, inhalerade eller intravitreala steroider. Genetisk predisposition finns.",
        "severity": "moderate-severe",
        "urgency": "urgent (när diagnostiserat - agera snabbt)"
    }
]
