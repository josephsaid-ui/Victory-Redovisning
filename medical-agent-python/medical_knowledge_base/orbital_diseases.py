"""
Orbital Diseases - Orbitala Sjukdomar
10 most common orbital conditions

Database of orbital diseases for the medical knowledge base.
"""

ORBITAL_DISEASES = [
    {
        "name": "Orbital Cellulitis - Orbital Cellulit",
        "name_en": "Orbital Cellulitis",
        "icd10": "H05.0",
        "symptoms": [
            "ögonsmärta och huvudvärk",
            "synförlust eller dubbelseende",
            "proptosis (framträngande öga)",
            "begränsad ögonmotorik",
            "feber och allmänpåverkan",
            "ödem och rodnad av ögonlock",
            "kemosis (konjunktival svullnad)"
        ],
        "anamnesis_questions": [
            "Har du haft förkylning eller bihåleinflammation nyligen?",
            "Har du feber?",
            "Har du smärta när du rör ögat?",
            "Ser du dubbelt eller sämre än vanligt?",
            "Har du diabetes eller är immunsupprimerad?",
            "Har du haft trauma mot ansiktet?",
            "Hur snabbt har symtomen utvecklats?"
        ],
        "clinical_signs": [
            "proptosis (framträngande öga)",
            "oftalmoplegia (begränsad ögonmotorik)",
            "periorbitalt ödem och erytem",
            "kemosis",
            "RAPD (relativ afferent pupilldefekt) vid optikusengagemang",
            "minskad visus",
            "feber",
            "smärta vid ögonrörelser",
            "resistens vid palpation"
        ],
        "risk_factors": [
            "sinuit (framför allt etmoidit och sfenoidit)",
            "dentalinfektion",
            "ansiktstrauma eller kirurgi",
            "immunsuppression",
            "diabetes mellitus",
            "barnalder (högre risk)",
            "främmande kropp i orbita"
        ],
        "treatment": "AKUT! Omedelbar sjukhusvård. IV bredspektrum antibiotika (vanligen ceftriaxon + metronidazol eller klindamycin). CT orbita och bihålor AKUT för att bedöma utbredning och utesluta subperiosteal abscess. Noggrann övervakning av synfunktion och ögonmotorik. Kirurgisk dränage om abscess föreligger eller vid utebliven förbättring på antibiotika. ÖNH-konsult för eventuell bihålekirurgi. Behandla underliggande bihåleinflammation.",
        "kva": "DC001 (CT orbita), ZXC00 (inläggning)",
        "differential_diagnoses": [
            "preseptal cellulit",
            "orbital pseudotumor",
            "kavernös sinus-trombos",
            "Graves oftalmopati (akut fas)",
            "orbital tumör med inflammation",
            "ruptured dermoid cyst"
        ],
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Preseptal Cellulitis - Preseptal Cellulit",
        "name_en": "Preseptal Cellulitis",
        "icd10": "H01.0",
        "symptoms": [
            "ödem och rodnad av ögonlock",
            "värme över ögonlocket",
            "normal syn",
            "ingen smärta vid ögonrörelser",
            "feber (kan förekomma)",
            "ingen proptosis",
            "ingen dubbelseende"
        ],
        "anamnesis_questions": [
            "Har du haft någon skada eller insektsbett på ögonlocket?",
            "Har du haft hordeolum eller chalazion?",
            "Hur är din syn? Kan du röra ögat normalt?",
            "Har du smärta när du rör ögat?",
            "Har du feber?",
            "Har du haft bihåleinflammation?",
            "Finns det eksem eller hudinfektioner i ansiktet?"
        ],
        "clinical_signs": [
            "periorbitalt ödem och erytem",
            "normal ögonmotorik",
            "normal visus",
            "ingen proptosis",
            "ingen kemosis",
            "ingen RAPD",
            "septum intakt (viktigt att verifiera)",
            "kan ha lindrig feber"
        ],
        "risk_factors": [
            "trauma mot ögonlock",
            "insektsbett",
            "hordeolum eller chalazion",
            "dermatit eller eksem",
            "barnalder",
            "övre luftvägsinfektion",
            "immunsuppression",
            "dakriocystit"
        ],
        "treatment": "Oral antibiotika (flukloxacillin eller klindamycin, om penicillinallergi). Varma kompress. Noggrann uppföljning efter 24-48 timmar för att utesluta progression till orbital cellulit. Sjukhusvård om: barnet är <1 år, tecken på systemisk sjukdom, immunsuppression, eller osäkerhet om avgränsning från orbital cellulit. Varningssignal för orbital cellulit: proptosis, dubbelseende, smärta vid ögonrörelser, synförsämring. Vid behandlingssvikt: byt till IV antibiotika och uteslut orbital engagemang med CT.",
        "kva": "AT001 (öppenvårdskonsultation)",
        "differential_diagnoses": [
            "orbital cellulit",
            "angioödem",
            "allergisk reaktion",
            "dermatomyosit",
            "hordeolum eller chalazion med inflammation",
            "dakirocystit"
        ],
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Thyroid Eye Disease / Graves Oftalmopati",
        "name_en": "Thyroid Eye Disease / Graves' Orbitopathy",
        "icd10": "H06.2",
        "symptoms": [
            "framträngande ögon (proptosis)",
            "dubbelseende (diplopi)",
            "retrakterat övre ögonlock (lid lag)",
            "torra och irriterade ögon",
            "ljuskänslighet",
            "rodnad och svullnad runt ögonen",
            "synförsämring (i svåra fall)",
            "känsla av tryck bakom ögonen"
        ],
        "anamnesis_questions": [
            "Har du fått diagnos av sköldkörtelsjukdom (Graves sjukdom eller tyreotoxikos)?",
            "Hur länge har du haft besvär från ögonen?",
            "Har besvären försämrats nyligen?",
            "Ser du dubbelt, och i så fall när?",
            "Har du svårt att blunda helt?",
            "Röker du eller har du rökt?",
            "Får du behandling för sköldkörteln och hur är dina senaste prover?",
            "Har du synförsämring?"
        ],
        "clinical_signs": [
            "proptosis (oftast bilateral)",
            "lid retraction (övre och nedre lock)",
            "lid lag vid nedåtblick",
            "begränsad elevation och abduktion",
            "konjunktival och karunkulär injektion",
            "kemosis",
            "korneal exponering",
            "ökad IOP vid uppåtblick",
            "optic neuropathy (i svåra fall - RAPD, synfältsdefekt)",
            "restrictive myopathy"
        ],
        "risk_factors": [
            "Graves sjukdom (autoimmun hypertyreoidism)",
            "rökning (största riskfaktorn för svår TED)",
            "radioaktivt jodbehandling (kan förvärra)",
            "dåligt kontrollerad tyreoideastatus",
            "kvinnligt kön (men män får svårare sjukdom)",
            "ålder 40-60 år",
            "genetisk predisposition",
            "stress"
        ],
        "treatment": "Multidisciplinär behandling med endokrinolog och oftalmolog. AKUT vid dystyroid optic neuropathy (DON): IV methylprednisolon, eventuellt akut orbital dekompression. Aktiv fas (inflammation): selen supplementering (mild sjukdom), IV steroider (måttlig-svår), orbital strålbehandling (i utvalda fall), teprotumumab (nya biologiska läkemedlet). Rehabilitativ fas (efter minst 6 månaders inaktivitet): skeleoperation först, sedan ögonlockskirurgi. Viktigast: optimal tyreoideakontroll (euthyroid status), SLUTA RÖKA. Smörjande droppar och salva för exponeringskeratopati. Tapeband eller fuktkammare nattetid vid inkomlett blunkning.",
        "kva": "DC001 (CT/MR orbita), CJB05 (synfältsundersökning), CJD05 (OCT), ACD10 (orbital dekompression), ACF (ögonlockskirurgi)",
        "differential_diagnoses": [
            "orbital pseudotumor",
            "orbital tumör (lymfom, metastas)",
            "karotico-kavernös fistel",
            "myosit",
            "IgG4-relaterad sjukdom",
            "orbital varices"
        ],
        "severity": "moderate-severe (DON är severe)",
        "urgency": "urgent (DON är emergency)"
    },
    {
        "name": "Idiopathic Orbital Inflammation (Orbital Pseudotumor)",
        "name_en": "Idiopathic Orbital Inflammation / Orbital Pseudotumor",
        "icd10": "H05.1",
        "symptoms": [
            "snabb debut av ögonsmärta",
            "proptosis",
            "dubbelseende",
            "ögonlockssvullnad",
            "rodnad",
            "synförsämring (kan förekomma)",
            "smärta vid ögonrörelser",
            "ofta unilateralt"
        ],
        "anamnesis_questions": [
            "Hur snabbt kom symtomen? (ofta akut debut över dagar)",
            "Har du mycket smärta?",
            "Har du feber eller känner dig sjuk på annat sätt?",
            "Har du systemiska inflammatoriska sjukdomar?",
            "Har du behandlats med steroider tidigare, och hjälpte det?",
            "Har du försämrad syn?",
            "Är det ena eller båda ögonen?"
        ],
        "clinical_signs": [
            "proptosis (ofta unilateral)",
            "begränsad ögonmotorik (ofta smärtsam)",
            "periorbitalt ödem och erytem",
            "kemosis",
            "ökad resistens vid retropulsion",
            "kan ha uveit eller sklerit samtidigt",
            "minskad visus (om optikus engageras)",
            "normala inflammationsmarkörer (oftast)"
        ],
        "risk_factors": [
            "ofta ingen känd riskfaktor (idiopatisk)",
            "ibland associerad med systemiska sjukdomar (IgG4-relaterad sjukdom, Wegeners granulomatos)",
            "kan följa infektion",
            "medelålder (40-50 år vanligast)"
        ],
        "treatment": "Uteslut infektion och tumör FÖRST (CT/MR orbita, blodprover inklusive SR, CRP, ANA, ANCA, IgG4). Om diagnosen är säker: systemiska kortikosteroider (prednisolon 1 mg/kg, gradvis nedtrappning). Ofta snabbt och dramatiskt svar på steroider (diagnostiskt tecken). Vid steroidberoende eller recidiv: steroidsparande immunsuppression (metotrexat, azatioprin, mykofenolat). Strålbehandling i refraktära fall. Biologiska läkemedel (rituximab) vid svår sjukdom. Viktigt: noga uppföljning för att utesluta underliggande systemsjukdom eller lymfom som kan debutera likt pseudotumor.",
        "kva": "DC001 (CT/MR orbita), PA001 (biopsi om diagnos oklar)",
        "differential_diagnoses": [
            "orbital cellulitis",
            "orbital lymfom",
            "IgG4-relaterad orbital sjukdom",
            "Graves oftalmopati",
            "orbital myosit (mer specifik variant av pseudotumor)",
            "sarkidos",
            "Wegeners granulomatos",
            "metastatisk tumör"
        ],
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Orbital Lymphoma - Orbital Lymfom",
        "name_en": "Orbital Lymphoma",
        "icd10": "C85.9 (ej specifik lymfom) / H05.8",
        "symptoms": [
            "långsam, progressiv proptosis",
            "palpabel resistens",
            "dubbelseende",
            "ptosis",
            "ofta smärtfritt",
            "synförsämring (om optikus kompression)",
            "sällan inflammation eller rodnad"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft framträngande öga?",
            "Kommer det smygande eller snabbt?",
            "Har du haft svullna lymfkörtlar på andra ställen?",
            "Har du viktnedgång, nattsvettningar eller feber (B-symtom)?",
            "Har du känd lymfom eller annan cancer?",
            "Har du försämrad syn?",
            "Har du smärta?"
        ],
        "clinical_signs": [
            "proptosis (ofta smygande)",
            "palpabel, fast orbital massa",
            "begränsad ögonmotorik",
            "ptosis (om masseffekt)",
            "konjunktival 'laxfärgad' lymfoid massa (om anterior)",
            "ofta minimal inflammation",
            "kan ha minskad visus vid kompression"
        ],
        "risk_factors": [
            "högre ålder (>60 år)",
            "autoimmuna sjukdomar (Sjögrens syndrom)",
            "immunsuppression",
            "tidigare strålbehandling",
            "extranodalt marginalzons-lymfom (EMZL) vanligast orbital lymfom"
        ],
        "treatment": "Biopsi för histopatologi och immunhistokemi (diagnos). Stadieindelning (systemisk utredning med hematolog/onkolog: PET-CT, benmärgsundersökning, blodprover). Behandling beroende på typ och stadium: lokal strålbehandling (om isolerad orbital sjukdom), kemoterapi (om systemiskt engagemang), rituximab (anti-CD20 för B-cellslymfom). Ofta god prognos vid lågmaligna, lokaliserade orbital lymfom (EMZL). Nära samarbete med hematolog/onkolog.",
        "kva": "DC001 (CT/MR orbita), PA001 (orbital biopsi), DN099 (PET-CT)",
        "differential_diagnoses": [
            "orbital pseudotumor",
            "dakriops (tårkörtelmassa)",
            "IgG4-relaterad orbital sjukdom",
            "sarkoid",
            "metastatisk tumör",
            "pleomorf adenom i tårkörteln",
            "orbital dermoid (hos barn)"
        ],
        "severity": "severe",
        "urgency": "urgent (behöver snabb utredning)"
    },
    {
        "name": "Cavernous Sinus Thrombosis - Sinus Cavernosus Trombos",
        "name_en": "Cavernous Sinus Thrombosis",
        "icd10": "G08",
        "symptoms": [
            "svår huvudvärk",
            "bilateral proptosis (ofta)",
            "svår ögonsmärta",
            "oftalmoplegia (CN III, IV, VI)",
            "hög feber och allmänpåverkan",
            "förändrad medvetandegrad",
            "dubbelseende",
            "synförsämring",
            "facial numbness (CN V1, V2)"
        ],
        "anamnesis_questions": [
            "Hur snabbt kom symtomen?",
            "Har du haft ansiktsinfektion, bihåleinflammation eller tandvärk?",
            "Har du hög feber?",
            "Känner du dig mycket sjuk?",
            "Har du dubbelseende eller synförlust?",
            "Har du domningar i ansiktet?",
            "Har du haft koagulationsrubbningar?"
        ],
        "clinical_signs": [
            "bilateral proptosis (karakteristiskt tecken)",
            "oftalmoplegia (CN III, IV, VI parese)",
            "kemosis",
            "periorbitalt ödem",
            "papillödem",
            "retinal venös stagnation",
            "minskad visus",
            "hög feber",
            "RAPD (om optisk neuropati)",
            "förändrat mentalt status"
        ],
        "risk_factors": [
            "ansikts- eller bihåleinfektion (sfenoidit, etmoidit)",
            "dental infektion",
            "facial furunkel eller cellulitis (farliga triangeln)",
            "otit eller mastoidit",
            "koagulationsrubbningar",
            "trauma",
            "kirurgi i ansiktsområdet",
            "graviditet och postpartum"
        ],
        "treatment": "AKUT LIVSHOTANDE TILLSTÅND! Omedelbar inläggning på IVA. Bredspektrum IV antibiotika (vanligen vankomycin + ceftriaxon + metronidazol för att täcka Staphylococcus aureus, streptokocker och anaerober). MR hjärna och MR venografi eller CT venografi AKUT för att bekräfta diagnos. Antikoagulation (låg-molekylärt heparin eller unfraktionerat heparin) - kontroversiellt men rekommenderas oftast. Kirurgisk dränage av infektionskälla (bihålor, abscess). Intensivvård med övervakning av neurologiskt status. Steroider (kontroversiellt). Mortalitet 20-30% trots behandling. Komplikationer: stroke, meningit, hjärnabscess, blindhet.",
        "kva": "DN001 (MR hjärna), DN002 (MR venografi), ZXC00 (IVA-vård)",
        "differential_diagnoses": [
            "bilateral orbital cellulitis",
            "Tolosa-Hunt syndrom",
            "orbital apex syndrom",
            "basilar meningit",
            "pituitary apoplexy",
            "mucormykos (hos diabetiker/immunsupprimerade)"
        ],
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Orbital Fracture - Orbitalfraktur",
        "name_en": "Orbital Fracture (Blowout Fracture)",
        "icd10": "S02.3 (golv), S02.8 (vägg)",
        "symptoms": [
            "dubbelseende (diplopi, särskilt vid uppåt/nedåtblick)",
            "svullnad och blåmärken runt ögat",
            "näsblod",
            "näskänsel i orbita vid snytning",
            "domningar i kind eller övre läpp (infraorbitala nerven)",
            "enophthalmos (insjunket öga)",
            "begränsad ögonrörlighet"
        ],
        "anamnesis_questions": [
            "Hur fick du skadan? Mekanismen? (slag, fall, trafikolycka)",
            "Ser du dubbelt, och i vilken blickriktning?",
            "Känner du domningar i ansiktet?",
            "Har du näsblod?",
            "Har du synförsämring?",
            "Har du smärta vid ögonrörelser?",
            "Fick du luftkänsla i ögonområdet när du snöt dig?"
        ],
        "clinical_signs": [
            "periorbitalt hematom och ödem",
            "subkonjunktival blödning",
            "diplopi (ofta vid uppåt- eller nedåtblick)",
            "begränsad elevation eller depression (inkarceration av muskler)",
            "forced duction test positiv (mekanisk restriktion)",
            "hypoestesi i infraorbitala nervens utbredning",
            "enophthalmos (kan vara maskerad av ödem akut)",
            "emfysem (subkutant luft)",
            "hypoglobus (sänkt bulbus)"
        ],
        "risk_factors": [
            "trauma mot ansikte/öga",
            "högenergetiska trauma (trafikolycka, misshandel)",
            "kontaktsport",
            "fall",
            "arbetsplatsolyckor"
        ],
        "treatment": "AKUT: uteslut ögontrauma (globusruptur, hyphema, retinalavlossning, traumatisk optikusneuropati) - detta har PRIORITET före fraktur! CT orbita (koronala och axiala snitt). AKUT kirurgi om: white-eyed blowout fracture med inkarceration och okulokardiell reflex (bradykardi, illamående) - operera inom 24-48h, framför allt hos barn. Antibiotika (om stor fraktur med risk för sinuit). RÅDET: snyt dig inte! Kirurgisk indikation vid: kvarstående diplopi i primärblick, signifikant enophthalmos (>2mm), stor frakturdefekt (>50% av golvet), inkarceration av mjukdelar. Oftast avvakta 1-2 veckor för att ödem ska gå ner innan kirurgi. Uppföljning med ortoptist för diplopi.",
        "kva": "DC001 (CT orbita), ACC20 (orbital frakturkirurgi)",
        "differential_diagnoses": [
            "blåtiradrauma utan fraktur",
            "globusruptur",
            "traumatisk optisk neuropati",
            "orbital hematom",
            "retrobulbär blödning",
            "zygomatisk fraktur"
        ],
        "severity": "moderate-severe",
        "urgency": "urgent (emergency om white-eyed blowout)"
    },
    {
        "name": "Orbital Varices - Orbital Varicer",
        "name_en": "Orbital Varices",
        "icd10": "H05.8",
        "symptoms": [
            "intermittent proptosis (ökar vid framåtböjning, Valsalva)",
            "dubbelseende (tillfälligt)",
            "känsla av tryck eller fullhet",
            "synförsämring (tillfällig vid trombos)",
            "ofta intermittenta symtom",
            "kan vara asymtomatisk"
        ],
        "anamnesis_questions": [
            "Kommer ögat mer framåt vid huvudet nedåt eller ansträngning?",
            "Kommer symtomen och går?",
            "Ser du dubbelt ibland?",
            "Har du haft blödningar i ögat?",
            "Har du synförsämring?",
            "Hur länge har du haft besvär?",
            "Finns det familjehistoria av kärlmissbildningar?"
        ],
        "clinical_signs": [
            "proptosis vid framåtböjning eller Valsalva",
            "tortuous conjunctival vessels",
            "kan ha subkonjunktival blödning",
            "oftast normalt status i vila",
            "ögat sjunker tillbaka när huvudet höjs",
            "kan ha kronisk proptosis om stor varix",
            "trombos kan ge akut smärta och proptosis"
        ],
        "risk_factors": [
            "medfödd kärlmissbildning",
            "kan vara associerad med andra vaskulära malformationer",
            "ofta sporadisk",
            "kan utvecklas efter trauma"
        ],
        "treatment": "Ofta konservativ behandling om minimala symtom. Regelbunden uppföljning. MR orbita med och utan kontrast (visar utvidgning vid Valsalva). Undvik Valsalva-manövrer (tunga lyft, ansträngning). AKUT om trombos: smärtlindring, eventuellt steroider, oftast spontan resolution. Kirurgi endast vid: kronisk proptosis med kosmetiskt besvär, svår diplopi, kompression av optiska nerven, recidiverande blödningar. Kirurgi är utmanande pga hög blödningsrisk. Embolisering är sällan effektivt för rena varicer.",
        "kva": "DN001 (MR orbita med dynamiska bilder)",
        "differential_diagnoses": [
            "karotiko-kavernös fistel",
            "arteriovenös malformation",
            "orbital tumör",
            "Graves oftalmopati",
            "orbital lymfangiom"
        ],
        "severity": "mild-moderate (severe vid trombos/blödning)",
        "urgency": "routine (urgent vid akut trombos)"
    },
    {
        "name": "Orbital Dermoid Cyst - Orbital Dermoidcysta",
        "name_en": "Orbital Dermoid Cyst",
        "icd10": "H05.8 / D31.6",
        "symptoms": [
            "långsamt växande, smärtfri svullnad",
            "ofta synlig eller palpabel massa",
            "proptosis (om djup)",
            "diplopi (om stor)",
            "vanligen diagnostiserad i barndomen",
            "kan rupturera och ge inflammation"
        ],
        "anamnesis_questions": [
            "Hur länge har svullnaden funnits? (ofta sedan födsel)",
            "Har den vuxit?",
            "Har den varit smärtsam eller inflammerad?",
            "Finns dubbelseende eller synproblem?",
            "Har barnet haft trauma mot området?",
            "Växer massan eller är den stabil?"
        ],
        "clinical_signs": [
            "väldefinierad, rund, fast massa",
            "oftast superolateralt (frontozygomatisk sutur)",
            "icke-mobil (fäst vid periost eller ben)",
            "hud ovanför normal",
            "ingen inflammation (om ej rupturerad)",
            "kan ha fördjupning i benet (på CT)",
            "proptosis om stor eller djup cysta",
            "diplopi om stor"
        ],
        "risk_factors": [
            "medfödd lesion (ectodermal inkludering under embryonal utveckling)",
            "oftast sporadisk",
            "majoriteten diagnostiseras före 5 års ålder"
        ],
        "treatment": "Kirurgisk exstirpation (oftast planerad, icke-akut). VIKTIG PRINCIP: excision EN BLOC utan ruptur - ruptur leder till svår inflammation (dermoidcystan innehåller keratin och sebum som är mycket irriterande). CT orbita preoperativt för att bedöma djup extension och benengagemang. Om superficiell: enkel excision. Om djup eller benengagemang: mer extensiv kirurgi, ibland neurokirurgisk samverkan. Akut kirurgi om rupturerad cysta med inflammation. Tidig kirurgi (2-5 års ålder) rekommenderas för att undvika ruptur och optimera kosmetiskt resultat. Risk vid att avvakta: tillväxt, ruptur, benerosion.",
        "kva": "ACC30 (excision orbital tumör), DC001 (CT orbita)",
        "differential_diagnoses": [
            "epidermoidcysta",
            "lipodermoid",
            "dermolipom",
            "orbital abscess",
            "lacrimal gland tumor",
            "rhabdomyosarkom (mer aggressiv tillväxt)",
            "meningiocele/encefalocele (om djup och medial)"
        ],
        "severity": "mild (moderate om rupturerad)",
        "urgency": "routine (urgent om rupturerad)"
    },
    {
        "name": "Retrobulbar Hemorrhage - Retrobulbär Blödning",
        "name_en": "Retrobulbar Hemorrhage",
        "icd10": "H05.2",
        "symptoms": [
            "snabb, smärtsam proptosis",
            "akut synförsämring",
            "svår ögonsmärta",
            "ofta efter trauma eller kirurgi",
            "rodnad och svullnad",
            "känsla av tryck bakom ögat",
            "dubbelseende"
        ],
        "anamnesis_questions": [
            "Har du haft trauma mot ögat eller ansiktet?",
            "Har du nyligen opererats runt ögat?",
            "Hur snabbt kom symtomen?",
            "Har du mycket smärta?",
            "Hur är din syn jämfört med innan?",
            "Använder du blodförtunnande mediciner?",
            "Har du koagulationsrubbning?"
        ],
        "clinical_signs": [
            "proptosis (ofta markerad och akut)",
            "mycket hårt öga (ökad IOP)",
            "begränsad ögonmotorik",
            "minskad visus",
            "RAPD (relativ afferent pupilldefekt)",
            "resistens vid retropulsion",
            "subkonjunktival blödning",
            "kemosis",
            "lid ecchymosis",
            "ögat kan inte reponeras"
        ],
        "risk_factors": [
            "trauma mot orbita",
            "orbital eller ögonlockskirurgi",
            "retrobulbära injektioner (anestesi)",
            "antikoagulantia eller antiplatelet medicinering",
            "koagulationsrubbningar",
            "kärlmissbildningar i orbita",
            "högt blodtryck"
        ],
        "treatment": "AKUT SIGHT-THREATENING EMERGENCY! Om tecken på orbital kompartment syndrom (markant ökad IOP, RAPD, synförsämring): AKUT lateral canthotomy och cantholysis (kan göras på akutmottagning utan dröjsmål). Mät IOP - om >40 mmHg och synförsämring: dekomprimera OMEDELBART. Höjd huvudända. Systemiska åtgärder: IV mannitol eller acetazolamid för att sänka IOP. Reversera antikoagulation om möjligt (vitamin K, TXA, prothrombinkomplexkoncentrat). CT orbita när patienten stabiliserats. Undvik retrobulbär block! Nästan alltid konservativ behandling efter initial dekompression - blödningen resorberas spontant. Kirurgisk evakuering av hematom endast om fortgående blödning från känt kärl. Uppföljning av synfunktion.",
        "kva": "ACE96 (lateral canthotomy/cantholysis), DC001 (CT orbita)",
        "differential_diagnoses": [
            "orbital cellulitis (men mer akut debut vid blödning)",
            "karotiko-kavernös fistel",
            "orbital varix trombos",
            "rupturerad orbital tumör"
        ],
        "severity": "severe",
        "urgency": "emergency"
    }
]


def get_orbital_diseases():
    """Return all orbital diseases"""
    return ORBITAL_DISEASES


def get_disease_by_name(name: str):
    """Get a specific disease by name (Swedish or English)"""
    name_lower = name.lower()
    for disease in ORBITAL_DISEASES:
        if (name_lower in disease['name'].lower() or
            name_lower in disease['name_en'].lower()):
            return disease
    return None


def get_diseases_by_urgency(urgency: str):
    """Get diseases by urgency level"""
    return [d for d in ORBITAL_DISEASES if d['urgency'] == urgency]


def get_emergency_diseases():
    """Get all emergency diseases"""
    return get_diseases_by_urgency('emergency')


if __name__ == "__main__":
    print(f"Loaded {len(ORBITAL_DISEASES)} orbital diseases")
    print("\nEmergency conditions:")
    for disease in get_emergency_diseases():
        print(f"  - {disease['name']}")
