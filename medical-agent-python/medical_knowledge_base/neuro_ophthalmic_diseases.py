"""
Neuro-Oftalmologiska Sjukdomar - 20 vanligaste
"""

NEURO_OPHTHALMIC_DISEASES = [
    {
        "name": "Optikusneurit (Synnervsinflamation)",
        "name_en": "Optic Neuritis",
        "icd10": "H46",
        "symptoms": [
            "snabb synnedsättning (timmar-dagar)",
            "ensidig (90%)",
            "smärta vid ögonrörelser (90%)",
            "nedsatt färgseende",
            "central skotom",
            "synnedsättning varierar (lätt till LP)",
            "ofta unga vuxna (20-40 år)"
        ],
        "anamnesis_questions": [
            "Försämrades synen snabbt över dagar?",
            "Gör det ont när du rör ögat?",
            "Ser färger blekare ut (särskilt rött)?",
            "Är du 20-40 år?",
            "Har du multipel skleros?",
            "Har du haft synproblem tidigare?",
            "Har du andra neurologiska symptom?"
        ],
        "clinical_signs": [
            "RAPD (relativ afferent pupilldefekt) - viktigaste tecknet!",
            "nedsatt synskärpa (varierar)",
            "central synfältsbortfall",
            "nedsatt färgseende (rött-grönt)",
            "papillen ofta normal (retrobulbär - 2/3) eller svullen (papillitis - 1/3)",
            "MRI: T2-hyperintensitet i synnerv, kontrastuppladdning",
            "ingen retinal patologi"
        ],
        "risk_factors": [
            "multipel skleros (50% får MS inom 15 år)",
            "kvinnligt kön (3:1)",
            "ålder 20-40 år",
            "kaukasiskt ursprung",
            "NMOSD (neuromyelitis optica) - sämre prognos",
            "MOGAD (MOG antibody disease)"
        ],
        "treatment": "IV methylprednisolon 1g dagligen i 3-5 dagar (snabbare återhämtning men påverkar ej slutlig syn), följt av oral prednison nedtrappning, alternativ: oral högdos prednison, MRI hjärna + rygg (screena för MS), LP om atypisk (uteslut NMOSD, infektion), vid NMOSD: plasmaferes/IVIG + immunosuppression, ONTT-studien: 95% återfår ≥20/40 syn spontant, MS-profylax: tidigt DMT (disease-modifying therapy) minskar risk för MS",
        "kva": "Ingen specifik (medicinsk behandling)",
        "differential_diagnoses": [
            "AION (äldre, ingen smärta vid ögonrörelser)",
            "Posteriör uveit",
            "Kompressiv optikusneuropati (tumör)",
            "NMOSD (bilateral, sämre återhämtning)"
        ],
        "description": "Optikusneurit är inflammation i synnerven, starkt associerad med MS. Typisk triad: snabb synnedsättning + smärta vid ögonrörelser + ung kvinna. RAPD är diagnostiskt. IV steroider påskyndar återhämtning. MRI för MS-screening essentiellt. God prognos - 95% återfår god syn.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Anteriör Ischemisk Optikusneuropati - Icke-Arteritisk (NAION)",
        "name_en": "Non-Arteritic Anterior Ischemic Optic Neuropathy",
        "icd10": "H47.0",
        "symptoms": [
            "plötslig smärtfri synförlust",
            "ensidig",
            "märks ofta vid uppvaknande",
            "altitudinalt synfältsbortfall",
            "äldre patient (>50 år)",
            "ingen smärta vid ögonrörelser"
        ],
        "anamnesis_questions": [
            "Vaknade du med synförlust?",
            "Har du smärta? (bör vara nej)",
            "Hur gammal är du? (oftast >50 år)",
            "Har du högt blodtryck?",
            "Har du diabetes?",
            "Har du sömnapné?",
            "Har du huvudvärk eller käkklaudikation? (uteslut GCA!)"
        ],
        "clinical_signs": [
            "svullen, blekfärgad papill (sectoriell svullnad vanligt)",
            "RAPD",
            "altitudinalt synfältsbortfall (ofta inferior)",
            "senare: papillatrofi",
            "liten cup/disc ratio ('disc at risk' - crowded disc)",
            "normala kärl (ingen embolus)",
            "SR/CRP normal (uteslut GCA!)"
        ],
        "risk_factors": [
            "ålder >50 år",
            "hypertoni",
            "diabetes",
            "sömnapné",
            "rökning",
            "nattlig hypotension",
            "liten cup/disc ratio ('disc at risk')",
            "PDE5-hämmare möjligen (Viagra, Cialis)"
        ],
        "treatment": "Ingen beprövad behandling!, behandla riskfaktorer: hypertoni, diabetes, sömnapné, rökstopp, undvik nattliga blodtryckssänkare, UTESLUT GCA (SR, CRP akut!) - livsviktigt!, aspirin kan övervägas (förhindra andra ögat?), andra ögat: 15% risk inom 5 år, uppföljning synfält, OCT RNFL (följ atrofi), prognos: viss förbättring möjlig (40% förbättras något), men oftast permanent synnedsättning",
        "kva": "Ingen",
        "differential_diagnoses": [
            "AAION (arteritisk - uteslut GCA!)",
            "Optikusneurit (yngre, smärta vid ögonrörelser)",
            "Central retinal artärocklusion",
            "Posteriör AION"
        ],
        "description": "NAION är vanligaste akuta optikusneuropati hos äldre. Ischemi i synnervshuvudet. 'Disc at risk' med liten cup/disc ratio. Plötslig smärtfri synförlust, ofta vid uppvaknande. VIKTIGT: uteslut GCA (SR/CRP)! Ingen effektiv behandling. Behandla riskfaktorer. Risk 15% i andra ögat.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Anteriör Ischemisk Optikusneuropati - Arteritisk (AAION/GCA)",
        "name_en": "Arteritic Anterior Ischemic Optic Neuropathy (Giant Cell Arteritis)",
        "icd10": "H47.0 + M31.6",
        "symptoms": [
            "plötslig, svår synförlust",
            "smärtfri ögonmässigt",
            "patient >60 år",
            "huvudvärk (temporal)",
            "käkklaudikation",
            "allmän sjukdomskänsla, viktförlust, feber",
            "polymyalgia reumatika symptom möjliga"
        ],
        "anamnesis_questions": [
            "Hur gammal är du? (nästan alltid >60 år)",
            "Har du huvudvärk i tinningen?",
            "Har du ont i käken när du tuggar?",
            "Är temporalartären öm vid beröring?",
            "Har du haft feber eller viktnedgång?",
            "Har du ont i axlar och höfter på morgonen? (PMR)",
            "Har du haft övergående synförlust (amaurosis fugax)?"
        ],
        "clinical_signs": [
            "kraftigt svullen, kritvit papill (chalk-white)",
            "RAPD",
            "ofta sämre syn än NAION (LP eller NLP)",
            "kan ha retinal ischemisk whitening",
            "SR kraftigt förhöjt (ofta >50, kan vara >100)",
            "CRP förhöjt",
            "temporalarteriet kan vara ömt, förtjockat, pulsationfritt",
            "bilateralisering inom dagar-veckor om obehandlad"
        ],
        "risk_factors": [
            "ålder >60 år (nästan aldrig <50 år)",
            "kvinnligt kön (3:1)",
            "nordeuropeiskt ursprung",
            "polymyalgia reumatika (PMR) - 50% association",
            "hereditet"
        ],
        "treatment": "AKUT! IV methylprednisolon 1g dagligen i 3-5 dagar, sedan oral prednison 1mg/kg (minst 60mg) dagligen, långsam nedtrappning över månader-år, temporalarteribiopsi inom 1 vecka (men starta steroider FÖRE biopsi!), biopsi: jätteceller, intimaförtjockning, behandla även om negativ biopsi om klinisk misstanke stark, tocilizumab (IL-6-hämmare) som steroid-sparande, VIKTIGT: behandla omedelbart vid misstanke - räddar andra ögat!, utan behandling: 50-95% risk för bilateralisering, prognos för redan drabbat öga: dålig (oftast permanent synförlust)",
        "kva": "Temporalarteribiopsi",
        "differential_diagnoses": [
            "NAION (men normal SR/CRP, mindre svår synförlust)",
            "Optikusneurit",
            "CRAO"
        ],
        "description": "AAION vid GCA är oftalmologisk och medicinsk NÖDSITUATION! Jättecellsarterit hos äldre >60 år. Triad: huvudvärk + käkklaudikation + synförlust. Kraftigt förhöjd SR. Akuta höga doser steroider räddar andra ögat. Temporalarteribiopsi men behandla FÖRE! Prognos för drabbat öga dålig.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Posteriör Ischemisk Optikusneuropati (PION)",
        "name_en": "Posterior Ischemic Optic Neuropathy",
        "icd10": "H47.0",
        "symptoms": [
            "plötslig synförlust",
            "smärtfri",
            "ofta bilateral",
            "efter kirurgi (ryggrad, hjärta) eller massiv blödning",
            "kan vara arteritisk (GCA) eller icke-arteritisk"
        ],
        "anamnesis_questions": [
            "Har du opererats nyligen? (särskilt ryggrad i bukläge)",
            "Var operationen lång (>6 timmar)?",
            "Har du haft stor blodförlust eller hypotension?",
            "Har du huvudvärk eller käkklaudikation? (GCA)",
            "Märkte du synförlust efter operation/blödning?"
        ],
        "clinical_signs": [
            "normal papill initialt (ischemi posteriort i synnerv)",
            "RAPD",
            "synfältsbortfall",
            "efter 4-6 veckor: papillatrofi",
            "inga retinala fynd",
            "SR/CRP (uteslut GCA om äldre)"
        ],
        "risk_factors": [
            "perioperativ (ryggradskirurgi i bukläge, hjärtkirurgi)",
            "massiv blodförlust",
            "utdragen hypotension",
            "anemi",
            "GCA (om äldre >60 år)",
            "hyperkoagulabilitet"
        ],
        "treatment": "Icke-arteritisk PION: ingen beprövad behandling, behandla underliggande orsak (anemi, hypotension), Arteritisk PION (GCA): som AAION - akuta höga steroider, förebyggande: vid riskoperationer (minimera hypotension, anemi), prognos: ofta dålig, permanent synnedsättning vanligt",
        "kva": "Ingen",
        "differential_diagnoses": [
            "AION (papillsvullnad synlig)",
            "Optikusneurit (yngre, smärta, återhämtning bättre)",
            "Kompressiv neuropati"
        ],
        "description": "PION är ischemi bakom ögat i synnerven. Vanligast perioperativt (ryggradskirurgi) eller vid massiv blödning. Normal papill initialt. Ofta bilateral. Dålig prognos. Uteslut GCA hos äldre. Ingen effektiv behandling för perioperativ form.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Papillödem (Svullen Papill vid Förhöjt Intrakraniellt Tryck)",
        "name_en": "Papilledema",
        "icd10": "H47.1",
        "symptoms": [
            "övergående synförlust (sekunders duration) - typiskt!",
            "huvudvärk (särskilt morgon, värre liggande)",
            "illamående/kräkningar",
            "dubbelseende (VI-nervpares)",
            "syn ofta relativt bevarad tidigt",
            "progressiv synfältsinskränkning",
            "pulsatil tinnitus möjlig"
        ],
        "anamnesis_questions": [
            "Har du övergående synsvartning (sekunders duration)?",
            "Värre när du böjer dig ner eller hostar?",
            "Har du huvudvärk på morgonen?",
            "Har du kräkningar?",
            "Ser du dubbelt?",
            "Har du haft viktuppgång? (IIH)",
            "Tar du vitamin A, tetracyklin eller andra mediciner?"
        ],
        "clinical_signs": [
            "bilateral papillsvullnad",
            "hyperemi av papillen",
            "oskarp papillkant",
            "inga spontana venösa pulsationer",
            "retinala blödningar vid papillen möjliga",
            "Paton's lines (omkringsvärmning av makula)",
            "syn ofta relativt god tidigt",
            "perifera synfältsinskränkningar vid kronisk",
            "förstorad blind spot"
        ],
        "risk_factors": [
            "hjärntumör",
            "idiopatisk intrakraniell hypertension (IIH) - överviktiga kvinnor",
            "cerebral venös sinustrombos",
            "hydrocephalus",
            "meningit/encefalit",
            "tetracyklin, vitamin A (läkemedel)",
            "hypoparatyreoidism"
        ],
        "treatment": "AKUT neurologi/neurokirurgi-konsult!, CT/MRI hjärna + MR-venografi (uteslut tumör, hydrocephalus, sinustrombos), LP (mät öppningstryck) om bilddiagnostik normal, behandla underliggande orsak: tumör: kirurgi/strålning, IIH: viktnedgång (10-15%), acetazolamid, eventuellt LP-shunt eller optikusnerv fenestration, venös sinustrombos: antikoagulation, uppföljning synfält och OCT RNFL, kroniskt papillödem leder till optikusatrofi och permanent synförlust",
        "kva": "Varierar beroende på orsak",
        "differential_diagnoses": [
            "Papillitis (optikusneurit med papillsvullnad - unilateral, sämre syn)",
            "AION (unilateral, äldre)",
            "Pseudopapillödem (drusen)",
            "Diabetisk papillopati"
        ],
        "description": "Papillödem är bilateral papillsvullnad vid förhöjt intrakraniellt tryck. Övergående synförlust (sekunder) är karakteristiskt. Syn ofta god initialt men kroniskt leder till atrofi. AKUT neurologi-konsult! CT/MRI för att utesluta tumör. IIH hos överviktiga kvinnor vanligt.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Idiopatisk Intrakraniell Hypertension (IIH/Pseudotumor Cerebri)",
        "name_en": "Idiopathic Intracranial Hypertension",
        "icd10": "G93.2",
        "symptoms": [
            "huvudvärk (daglig, värre morgon/liggande)",
            "övergående synförlust",
            "pulsatil tinnitus (whooshing ljud)",
            "dubbelseende (VI-nervpares)",
            "syn ofta bevarad tidigt men försämras gradvis",
            "illamående"
        ],
        "anamnesis_questions": [
            "Är du överviktig kvinna i fertil ålder?",
            "Har du kraftig huvudvärk?",
            "Hör du ett pulserande ljud i huvudet?",
            "Har du övergående synsvartningar?",
            "Har du nyligen gått upp i vikt eller tagit mediciner?",
            "Tar du tetracykliner, tillväxthormon, vitamin A?"
        ],
        "clinical_signs": [
            "bilateral papillödem",
            "relativt god syn tidigt",
            "förstorad blind spot",
            "perifer synfältsinskränkning vid progression",
            "VI-nervpares möjlig (dubbelseende)",
            "MRI hjärna: tom sella, tortuous optic nerves, eventuell transverse sinus stenosering",
            "LP: öppningstryck >250 mmH2O (>200 barn), normalt CSF-protein/celler"
        ],
        "risk_factors": [
            "övervikt/fetma (BMI >30)",
            "kvinnligt kön (10:1)",
            "fertil ålder (20-40 år)",
            "nylig viktuppgång",
            "mediciner: tetracyklin, minocyklin, vitamin A, tillväxthormon",
            "PCOS möjligen"
        ],
        "treatment": "Viktnedgång (10-15% kroppsvikt) - viktigast!, acetazolamid 500mg-2g dagligen (minskar CSF-produktion), topiramat alternativ (viktminskning + minskar CSF), upprepad LP vid akut svår, kirurgiskt vid hotande synförlust eller refraktär: LP-shunt (ventrikuloperitoneal eller lumboperitoneal), optikusnerv sheath fenestration, venös sinus stenting vid stenosering, uppföljning: synfält och OCT RNFL regelbundet, prognos: god med viktnedgång och behandling, utan behandling: risk för permanent synförlust",
        "kva": "CDK00 (optikusnerv fenestration) eller shunt",
        "differential_diagnoses": [
            "Cerebralt venös sinustrombos (liknar IIH)",
            "Hjärntumör (uteslut med MRI)",
            "Hydrocephalus",
            "Meningit"
        ],
        "description": "IIH är ökat intrakraniellt tryck utan tumör eller hydrocephalus. Typisk patient: överviktig kvinna 20-40 år. Papillödem med relativt god syn initialt. Pulsatil tinnitus karakteristiskt. Viktnedgång är behandling. Acetazolamid. Risk för permanent synförlust utan behandling.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Optisk Nervdrusen",
        "name_en": "Optic Disc Drusen",
        "icd10": "H47.3",
        "symptoms": [
            "oftast asymtomatisk",
            "upptäckts-fynd",
            "gradvis synfältsinskränkning möjlig",
            "övergående synförlust möjlig",
            "kan simulera papillödem"
        ],
        "anamnesis_questions": [
            "Har papillerna sett onormala ut tidigare?",
            "Märker du någon synfältsinskränkning?",
            "Har du huvudvärk? (bör vara nej - uteslut papillödem)",
            "Finns synproblem i familjen?"
        ],
        "clinical_signs": [
            "glänsande, gula depositioner i papillen",
            "upphöjd papill utan hyperemi (vs papillödem)",
            "inga retinala blödningar",
            "spontana venösa pulsationer ofta bevarade",
            "autofluorescens: hyperautofluorescent drusen",
            "OCT: klumpar under eller i papillen",
            "ultrasound B-scan: hyperreflektiva med skuggning",
            "synfältsdefekter: förstorad blind spot, arcuate defekter"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant vanligt)",
            "liten papill med liten cup",
            "bilateral hos 75%",
            "hyperopi"
        ],
        "treatment": "Observation om asymtomatisk, uppföljning synfält årligen (gradvis försämring möjlig), ingen specifik behandling, viktigt: skilja från papillödem (undvik onödig utredning), autofluorescens och ultrasound diagnostiskt, uteslut intrakraniellt tryckstegring om symptom",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Papillödem (hyperemi, oskarp kant, blödningar)",
            "Papillitis",
            "Tilted disc",
            "Myelinerade nervfibrer"
        ],
        "description": "Optikusdrusen är kalkdepositioner i papillen. Oftast asymtomatisk upptäcktsfynd. Kan simulera papillödem men INGEN hyperemi, INGA blödningar, spontana venösa pulsationer kvarstår. Autofluorescens diagnostiskt. Gradvis synfältsinskränkning möjlig. Observation.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "III Kranialnerv-pares (Okulomotorpares)",
        "name_en": "Third Nerve Palsy",
        "icd10": "H49.0",
        "symptoms": [
            "dubbelseende",
            "hängande ögonlock (ptosis)",
            "ögat pekar ner och ut",
            "eventuellt dilaterad pupill (komplett pares)",
            "smärta möjlig (särskilt aneurysm)"
        ],
        "anamnesis_questions": [
            "Ser du dubbelt?",
            "Hänger ögonlocket?",
            "Är pupillen stor? (viktigt! - tyder på kompression)",
            "Har du huvudvärk eller smärta? (aneurysm-varningssignal)",
            "Har du diabetes eller högt blodtryck?",
            "Kom det plötsligt?"
        ],
        "clinical_signs": [
            "ptosis",
            "ögat i 'ner och ut' position (lateral rectus och superior oblique bevarade)",
            "begränsad adduktion, elevation, depression",
            "pupill-involvering: dilaterad, ljusstel pupill (komplett pares) eller",
            "pupill-sparad: normal pupill (mikrovaskulär/diabetisk)",
            "huvud kan lutas för att kompensera"
        ],
        "risk_factors": [
            "mikrovaskulär (diabetes, hypertoni, ålder) - pupill-sparad",
            "kompression: aneurysm (posterior communicating artery) - pupill-involverad!",
            "trauma",
            "tumör",
            "inflammation (Tolosa-Hunt)",
            "kongenitalt"
        ],
        "treatment": "AKUT om pupill-involverad: CTA/MRA akut (uteslut aneurysm - livshotande!), mikrovaskulär (pupill-sparad): observation, förbättring inom 3 månader förväntas, behandla vaskulära riskfaktorer, prismglasögon för diplopi, aneurysm: akut neurokirurgisk konsult, coiling eller clipping, tumör/inflammation: behandla underliggande orsak, ptosis-kirurgi endast efter stabilisering (6-12 mån), prognos mikrovaskulär: 80% full återhämtning inom 3 månader",
        "kva": "Varierar (neurokirurgi vid aneurysm)",
        "differential_diagnoses": [
            "Myasthenia gravis (variabel ptosis/diplopi)",
            "Orbital apex syndrom",
            "Cavernous sinus syndrom",
            "Thyreoidorbitopati"
        ],
        "description": "III-nervpares ger ptosis, 'ner och ut' öga, diplopi. KRITISKT: pupill-involverad = kompression (aneurysm!) → akut CTA/MRA. Pupill-sparad = mikrovaskulär (diabetes) → observation. Mikrovaskulär förbättras spontant inom 3 månader. Pupill-status avgörande för akuthandläggning!",
        "severity": "moderate-severe (emergency om pupill-involverad)",
        "urgency": "emergency (pupill-involverad), urgent (pupill-sparad)"
    },
    {
        "name": "IV Kranialnerv-pares (Troklearispares)",
        "name_en": "Fourth Nerve Palsy",
        "icd10": "H49.1",
        "symptoms": [
            "vertikalt dubbelseende",
            "värre vid nedåtblick (läsa, gå i trappor)",
            "huvudlutar (kompensatorisk - lutar mot motsatt axel)",
            "binocular diplopi (försvinner vid täckning av öga)",
            "kan vara subtil"
        ],
        "anamnesis_questions": [
            "Ser du dubbelt vertikalt?",
            "Värre när du läser eller går i trappor?",
            "Lutar du huvudet åt sidan?",
            "Har du haft skalltrauma?",
            "Har du diabetes?",
            "Är dubbelseendet nytt eller sedan länge? (kongenitalt?)"
        ],
        "clinical_signs": [
            "hypertropi i drabbat öga",
            "begränsad depression när ögat addukerar",
            "Bielschowsky head tilt test positiv (hypertropi ökar vid huvudlutar mot samma sida)",
            "Parks-Bielschowsky 3-step test lokaliserar superior oblique pares",
            "kongenitalt: stora vertikala fusion-amplituder, gamla bilder med huvudlutning"
        ],
        "risk_factors": [
            "trauma (vanligaste förvärvade orsaken - även milt trauma)",
            "mikrovaskulär (diabetes, hypertoni)",
            "kongenitalt (dekom­penserar i vuxen ålder)",
            "tumör (sällsynt)",
            "hydrocephalus"
        ],
        "treatment": "Kongenitalt (dekompenserad): observation, prismglasögon, kirurgi (superior oblique tuck eller inferior oblique recession), Förvärvat mikrovaskulärt: observation 6 månader (många återhämtar), behandla vaskulära riskfaktorer, prismglasögon temporärt, kirurgi om ej återhämtning efter 6-12 mån, trauma: observation (kan ta 1 år att återhämta), prognos: mikrovaskulär 50% full återhämtning, traumatisk varierande",
        "kva": "Ögonmuskelkirurgi vid behov",
        "differential_diagnoses": [
            "Skew deviation (central orsak)",
            "Blown-out floor fracture (trauma)",
            "Thyreoidorbitopati (restriktivt)",
            "Myasthenia gravis"
        ],
        "description": "IV-nervpares ger vertikalt dubbelseende, värst vid nedåtblick och läsning. Karakteristisk huvudlutning mot motsatt axel. Bielschowsky head tilt test diagnostiskt. Vanligaste orsaker: trauma (även milt), mikrovaskulär, kongenital dekompensation. Observation 6-12 månader.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "VI Kranialnerv-pares (Abducenspares)",
        "name_en": "Sixth Nerve Palsy",
        "icd10": "H49.2",
        "symptoms": [
            "horisontellt dubbelseende",
            "värre vid tittar på avstånd och åt sidan",
            "esotropi (inåtvridet öga)",
            "huvudvridning (kompensatoriskt - vrid mot pares-sida)",
            "diplopi försvinner vid nära"
        ],
        "anamnesis_questions": [
            "Ser du dubbelt horisontellt?",
            "Värre när du tittar åt sidan eller på avstånd?",
            "Har du diabetes eller högt blodtryck?",
            "Har du huvudvärk eller förhöjt intrakraniellt tryck?",
            "Har du haft skalltrauma?",
            "Har du cancer (metastaser)?"
        ],
        "clinical_signs": [
            "esotropi (konvergerande strabismus)",
            "begränsad abduktion (rörelse utåt)",
            "dubbelseende vid horisontell blick mot pares-sida",
            "huvudvridning mot paresen (för att undvika diplopi)",
            "isolerad VI-pares vs. andra kranialnerver (VII vid cerebellopontine angle)"
        ],
        "risk_factors": [
            "förhöjt intrakraniellt tryck (nonlocalizing sign!)",
            "mikrovaskulär (diabetes, hypertoni)",
            "trauma",
            "tumör (pontine, cerebellopontine angle, nasopharynx)",
            "multipel skleros",
            "Wernicke's encefalopati (tiamin-brist)",
            "graviditet/post-partum (benign intrakraniell hypertension)"
        ],
        "treatment": "Utred beroende på ålder och presentation: Barn/ung utan vaskulära riskfaktorer: MRI (uteslut tumör, demyelinisering), Äldre med vaskulära riskfaktorer: observation 3-6 mån, Förhöjt ICP symptom: MRI + LP, Isolerad mikrovaskulär: observation, förbättring inom 3-6 mån förväntas, behandla diabetes/hypertoni, prismglasögon eller täckning temporärt, botulinumtoxin i medial rectus vid persisterande, kirurgi om ej återhämtning efter 6-12 mån, prognos mikrovaskulär: 70% full återhämtning",
        "kva": "Ögonmuskelkirurgi vid behov",
        "differential_diagnoses": [
            "Thyreoidorbitopati (restriktiv, bilateral ofta)",
            "Myasthenia gravis (variabel, tröttbar)",
            "Duanes retractionssyndrom (kongenitalt)",
            "Convergence insufficiency"
        ],
        "description": "VI-nervpares ger esotropi och horisontellt dubbelseende vid blick utåt. Vanligaste kranialnervpares. 'Nonlocalizing sign' vid förhöjt ICP. Mikrovaskulär hos äldre diabetiker vanligt. MRI om barn/ung eller atypisk. Observation 3-6 månader. 70% spontan återhämtning.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Horner's Syndrom",
        "name_en": "Horner's Syndrome",
        "icd10": "G90.2",
        "symptoms": [
            "liten pupill (miosis) på ena sidan",
            "lätt hängande ögonlock (ptosis - 1-2mm)",
            "nedsatt svettning på ena ansiktshalvan (anhidros) - om preganglionär",
            "'omvänd' anisokori (mer i mörker)",
            "ofta asymtomatisk - upptäckts-fynd"
        ],
        "anamnesis_questions": [
            "Har någon sagt att du har olika stora pupiller?",
            "Hänger ena ögonlocket lite?",
            "Har du haft smärta i nacke/axel? (Pancoast tumör)",
            "Har du haft stroke eller huvudvärk? (dissektion)",
            "Har du fött barn nyligen? (neonatal Horner vid brachial plexus skada)",
            "Har du känt ansiktssmärta eller huvudvärk?",
            "Är ena ögat ljusare färgat? (kongenitalt)"
        ],
        "clinical_signs": [
            "miosis (liten pupill) på drabbad sida",
            "ptosis (1-2mm)",
            "anhidros (om preganglionär/central)",
            "upside-down ptosis (nedre locket högre - apparent enophtalmos)",
            "dilation lag i mörker (pupillen utvidgas långsammare)",
            "iris heterokromi (ljusare iris om kongenitalt)",
            "farmakologisk testning: apraclonidin eller kokain"
        ],
        "risk_factors": [
            "dissektion av carotis/vertebralis (spontan eller trauma)",
            "Pancoast tumör (apex lung)",
            "stroke (lateral medullary - Wallenberg)",
            "cluster headache (under attack)",
            "cervical/thoracic kirurgi",
            "kongenitalt/födseltrauma"
        ],
        "treatment": "Ingen behandling av Horner själv (kosmetiskt ofarlig), UTRED orsaken (viktigast!): Central (1:a neuron): MRI hjärna och halsrygg (stroke, demyelinisering, tumor), Preganglionär (2:a neuron): CT thorax (Pancoast), halsrygg-MRI, MRA halsartärer (dissektion), Postganglionär (3:a neuron): MRI orbita och cavernous sinus, Karotis dissektion: antikoagulation, kontroll imaging, Pancoast tumör: onkologisk behandling, Farmakologisk testning (apraclonidin, kokain, hydroxyamfetamin) kan lokalisera nivå",
        "kva": "Ingen (utredning)",
        "differential_diagnoses": [
            "Fysiologisk anisokori (pupiller olika men båda reagerar normalt)",
            "Adie's pupill (stor pupill, dålig ljusrespons)",
            "III-nervpares (stor pupill + ptosis + ögonrörelsepåverkan)",
            "Mekanisk ptosis"
        ],
        "description": "Horner's syndrom är sympatikusavbrott som ger triad: miosis + ptosis + anhidros. Kan vara central (stroke), preganglionär (Pancoast, dissektion) eller postganglionär. VIKTIGT: utred orsak - kan vara allvarlig (dissektion, tumör). Apraclonidin-test diagnostiskt.",
        "severity": "mild (själva syndromet), men underliggande orsak kan vara allvarlig",
        "urgency": "urgent (utredning)"
    },
    {
        "name": "Myasthenia Gravis - Okulär Form",
        "name_en": "Ocular Myasthenia Gravis",
        "icd10": "G70.0",
        "symptoms": [
            "variabel ptosis (värre på kvällen)",
            "variabel diplopi",
            "tröttbar (förvärras vid upprepad användning)",
            "ofta bilateral men asymmetrisk",
            "inga pupillförändringar",
            "förbättras efter vila"
        ],
        "anamnesis_questions": [
            "Varierar ögonlocken - hänger mer på kvällen?",
            "Förbättras det efter vila?",
            "Försämras symptomen vid upprepad ögonrörelse?",
            "Har du svårt att svälja eller andas? (generaliserad)",
            "Har du muskelsvaghet i armar/ben?",
            "Har du thymom eller autoimmun sjukdom?"
        ],
        "clinical_signs": [
            "variabel, tröttbar ptosis",
            "Cogan's lid twitch (ögonlock twitchar vid uppåtblick)",
            "förbättrad ptosis efter ispack (ice-test)",
            "variabel ögonmuskelsvaghet",
            "kan simulera vilken kranialnervpares som helst",
            "ofta bilateral men asymmetrisk",
            "normala pupiller (alltid!)",
            "förbättring efter edrophonium (Tensilon test) - används mindre nu"
        ],
        "risk_factors": [
            "kvinnor 20-40 år (bimodal distribution)",
            "män 60-80 år",
            "thymom (15% - särskilt hos äldre män)",
            "andra autoimmuna sjukdomar",
            "hereditet"
        ],
        "treatment": "Acetylkolinesterashämmare: pyridostigmin (Mestinon) 60mg 3-4x dagligen, immunsuppression vid generaliserad eller svår okulär: steroider (prednison), azathioprin, mykofenolatmofetil, cyclosporin, thymektomi vid thymom eller generaliserad MG hos unga, CT thorax (screena för thymom), serologiska tester: AChR-antikroppar (50% okulär, 85% generaliserad), MuSK-antikroppar, uppföljning: 50% okulär MG blir generaliserad inom 2 år, prognos okulär: god med behandling, sällan livshotande",
        "kva": "Thymektomi vid thymom",
        "differential_diagnoses": [
            "Kranialnerv-pares (ej variabel)",
            "Thyreoidorbitopati (restriktivt, inte tröttbart)",
            "CPEO (kronisk progressiv extern oftalmoplegi)",
            "Miller Fisher syndrom"
        ],
        "description": "Myasthenia gravis är autoimmun sjukdom med antikroppar mot acetylkolinreceptorer. Okulär form: variabel, tröttbar ptosis/diplopi. Värre på kvällen, förbättras efter vila. Ice-test diagnostiskt. Cogan's lid twitch typiskt. CT thorax för thymom. Pyridostigmin behandling.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Miller Fisher Syndrom",
        "name_en": "Miller Fisher Syndrome",
        "icd10": "G61.0",
        "symptoms": [
            "oftalmoplegi (dubbelseende, begränsade ögonrörelser)",
            "ataxi (balansproblem)",
            "areflexi (förlorade senreflexer)",
            "klassisk triad!",
            "ofta efter infektion (gastroenterit, URTI)",
            "progressivt över dagar-veckor"
        ],
        "anamnesis_questions": [
            "Har du haft magsjuka eller luftvägsinfektion nyligen?",
            "Har du svårt att gå stadigt?",
            "Ser du dubbelt?",
            "Har du svårt att röra ögonen?",
            "Har du muskelsvaghet i armar/ben? (GBS-överlapp)",
            "Försämras det gradvis?"
        ],
        "clinical_signs": [
            "oftalmoplegi (bilateral ögonmuskelsvaghet)",
            "kan börja som ensidig",
            "ataxi (cerebellar test abnorm)",
            "areflexi eller hyporeflexia",
            "pupiller ofta sparade initialt",
            "kan övergå till Guillain-Barré syndrom (20%)",
            "liquor: förhöjt protein, normala celler (albuminocytologisk dissociation)",
            "GQ1b-antikroppar i 90%"
        ],
        "risk_factors": [
            "föregående infektion (Campylobacter jejuni vanligast)",
            "2-4 veckor efter infektion",
            "alla åldrar men oftast vuxna",
            "män något vanligare"
        ],
        "treatment": "Ofta självläkande men kan behandlas: IVIG (intravenös immunglobulin) 0.4g/kg dagligen i 5 dagar - förkortar återhämtningstid, alternativ: plasmaferes, steroider INTE effektivt, monitorera andning och sväljning (risk för GBS-progression), fysioterapi, stödjande vård, prognos: god - 85% full återhämtning inom 6 månader, återhämtning börjar inom veckor, kan ha kvarstående balansproblem",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Guillain-Barré syndrom (mer motorisk svaghet)",
            "Myasthenia gravis (variabel, inte ataxi)",
            "Brainstem stroke (akut, fokala neurologiska tecken)",
            "Wernicke's encefalopati"
        ],
        "description": "Miller Fisher syndrom är variant av Guillain-Barré. Klassisk triad: oftalmoplegi + ataxi + areflexi. Ofta efter Campylobacter-infektion. GQ1b-antikroppar diagnostiskt. IVIG förkortar återhämtning. God prognos - 85% full återhämtning inom 6 månader.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Kronisk Progressiv Extern Oftalmoplegi (CPEO)",
        "name_en": "Chronic Progressive External Ophthalmoplegia",
        "icd10": "H49.4",
        "symptoms": [
            "gradvis bilateral ptosis",
            "progressiva ögonrörelsebegränsningar",
            "vanligen ingen diplopi (så långsam att hjärnan anpassar sig)",
            "symmetrisk påverkan",
            "debut vuxen ålder",
            "inga tröttbarhet (vs myasthenia)"
        ],
        "anamnesis_questions": [
            "Har ögonlocken hängt gradvis över många år?",
            "Har du svårt att röra ögonen?",
            "Ser du dubbelt? (ofta nej trots ögonrörelsepåverkan)",
            "Har du muskelsvaghet, hörselnedsättning eller diabetes? (Kearns-Sayre)",
            "Finns liknande i familjen?",
            "I vilken ålder började symptomen?"
        ],
        "clinical_signs": [
            "bilateral symmetrisk ptosis",
            "begränsade ögonrörelser (alla riktningar)",
            "frontalis-överaktivitet (höjda ögonbryn för att kompensera ptosis)",
            "orbicularis svaghet ofta",
            "normala pupiller",
            "inget tröttbarhet",
            "eventuella systemiska tecken (Kearns-Sayre, MELAS)"
        ],
        "risk_factors": [
            "mitokondriella sjukdomar (vanligaste orsaken)",
            "Kearns-Sayre syndrom (CPEO + pigmentär retinopati + hjärtledningsblock)",
            "MELAS, MERRF (andra mitokondriella syndrom)",
            "sporadisk eller maternellt ärftlig",
            "mtDNA-deletioner"
        ],
        "treatment": "Ingen specifik behandling för CPEO, ptosis-kirurgi för att förbättra synfält (frontalis sling vanligtvis), utvärdera för Kearns-Sayre: EKG (hjärtledningsblock!), retinal undersökning (pigmentär retinopati), hörseltest, laktat, muskelbiospsi (ragged-red fibers), genetisk testning (mtDNA-deletioner), pacemaker vid hjärtledningsblock (livshotande!), CoQ10-tillskott (evidens svag), stödjande vård",
        "kva": "Ptosis-kirurgi (frontalis suspension)",
        "differential_diagnoses": [
            "Myasthenia gravis (variabel, tröttbar)",
            "Okulofaryng. muskeldystrofi",
            "Thyreoidorbitopati (restriktiv)",
            "Multipla kranialnervpareser"
        ],
        "description": "CPEO är mitokondriell sjukdom med gradvis bilateral ptosis och oftalmoplegi. Symmetrisk, långsam progression. Ofta ingen diplopi (hjärnan anpassar sig). Kearns-Sayre-syndrom: CPEO + pigmentär retinopati + hjärtledningsblock (pacemaker nödvändig!). Ptosis-kirurgi symptomatisk behandling.",
        "severity": "moderate",
        "urgency": "routine (urgent om Kearns-Sayre med hjärtblock)"
    },
    {
        "name": "Thyreoidorbitopati (Graves Oftalmopati)",
        "name_en": "Thyroid Eye Disease",
        "icd10": "H06.2",
        "symptoms": [
            "utbuktande ögon (proptosis)",
            "dubbelseende",
            "rodnade, svullna ögonlock",
            "torra ögon",
            "ljuskänslighet",
            "smärta vid ögonrörelser",
            "synnedsättning (vid optikusneuropati - sällsynt men allvarligt)"
        ],
        "anamnesis_questions": [
            "Har du sköldkörtelproblem? (Graves sjukdom)",
            "Står ögonen ut mer än tidigare?",
            "Ser du dubbelt?",
            "Har ögonen blivit röda och svullna?",
            "Röker du? (förvärrar kraftigt!)",
            "Har du svårt att stänga ögonen helt?"
        ],
        "clinical_signs": [
            "proptosis (utbuktande ögon)",
            "ögonlocksretraktion (scleral show)",
            "lid lag (von Graefe's tecken)",
            "konjunktival injektion och chemosis",
            "restriktiv myopati (oftast inferior rectus → begränsad elevation)",
            "exponeringskeratopati möjlig",
            "kompressiv optikusneuropati (DON) - sällsynt men allvarligt: synnedsättning, RAPD, papillsvullning",
            "CT/MRI: förstorade extraokulära muskler (muskelbuk, INTE senor)"
        ],
        "risk_factors": [
            "Graves sjukdom (autoimmun hypertyreos)",
            "rökning (största påverkbara faktorn - 8x ökad risk)",
            "kvinnligt kön (5:1)",
            "ålder 40-60 år",
            "radioaktivt jod-behandling (kan förvärra TED)",
            "dålig tyreoidakontroll",
            "stress"
        ],
        "treatment": "Mild: artificiella tårar, lubricering, nattpåse/tape, solglasögon, prisma för diplopi, Måttlig-svår: systemiska steroider (prednison 0.5-1mg/kg), intravenös methylprednisolon (mer effektivt), selenium-tillskott kan hjälpa mild TED, Svår/DON (nödsituation!): höga doser IV steroider, akut orbital dekompression (kirurgi), orbital strålning som tillägg till steroider, Rehabiliterings-fas (efter inflammation lugnad): orbital dekompression för proptosis, strabismus-kirurgi för diplopi, ögonlockskirurgi för retraktion, RÖKSTOPP KRITISKT!, tyreoidkontroll (euthyroid), teprotumumab (IGF-1R-antikropp) - ny behandling, mycket effektiv",
        "kva": "Orbital dekompression, strabismus-kirurgi, ögonlockskirurgi",
        "differential_diagnoses": [
            "Orbital cellulitis/abscess",
            "Orbital tumör",
            "Carotid-cavernous fistula",
            "Idiopatisk orbital inflammation (pseudotumör)"
        ],
        "description": "Thyreoidorbitopati är autoimmun inflammation i orbita vid Graves sjukdom. Proptosis, diplopi, exponering. Restriktiv myopati (inferior rectus vanligast). Rökning förvärrar kraftigt - RÖKSTOPP! DON (kompressiv optikusneuropati) är nödsituation. Teprotumumab revolutionerar behandling. Rehabiliteringskirurgi efter inflammation lugnad.",
        "severity": "moderate-severe (severe vid DON)",
        "urgency": "urgent (emergency vid DON)"
    },
    {
        "name": "Tolosa-Hunt Syndrom",
        "name_en": "Tolosa-Hunt Syndrome",
        "icd10": "G44.8",
        "symptoms": [
            "ensidig periorbitalt smärta (kraftig, molande)",
            "oftalmoplegi (kranialnerv III, IV, VI påverkan)",
            "smärtan kommer före oftalmoplegin (dagar-veckor)",
            "kan ha ansiktskänslöhet (V1)",
            "eventuell proptosis"
        ],
        "anamnesis_questions": [
            "Har du kraftig smärta runt ögat?",
            "Kom smärtan före dubbelseendet?",
            "Har du ansiktskänslöhet?",
            "Har du haft detta tidigare? (recidiv vanligt)",
            "Förbättrades du snabbt av kortison?"
        ],
        "clinical_signs": [
            "kranialnerv-pareser (III, IV, VI - ensam eller kombination)",
            "ansiktskänslöhet (V1)",
            "eventuell proptosis",
            "Horner's syndrom möjlig",
            "MRI: kontrastuppladdning i cavernous sinus/orbital apex",
            "dramatisk förbättring på steroider (inom dagar)"
        ],
        "risk_factors": [
            "idiopatisk granulomatös inflammation",
            "kan recidivera (30-50%)",
            "alla åldrar men oftast vuxna",
            "ingen känd trigger"
        ],
        "treatment": "Höga doser systemiska steroider (prednison 1mg/kg), dramatisk förbättring inom 24-72 timmar (diagnostiskt!), nedtrappning över veckor-månader, recidiv vanligt vid för snabb nedtrappning, immunosuppression (MTX, azathioprin) vid recidiverande eller steroid-beroende, VIKTIGT: diagnos per exclusionem - uteslut annat först: MRI med kontrast (tumör, aneurysm, AVM, lymphom, sarkoid, Wegeners, IgG4-relaterad sjukdom), biopsi vid atypisk presentation",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Orbital apex syndrom/cavernous sinus syndrom (tumör, infektion)",
            "Tumörer (meningiom, lymphom, metastas)",
            "Aneurysm",
            "Diabetisk kranialnerv-pares (ingen smärta)",
            "Herpes zoster (V1-distribution, vesikler)"
        ],
        "description": "Tolosa-Hunt är idiopatisk granulomatös inflammation i cavernous sinus/orbital apex. Triad: kraftig periorbitalt smärta + oftalmoplegi + dramatisk steroidrespons. Smärta före kranialnerv-pares typiskt. MRI visar kontrastuppladdning. Diagnos per exclusionem - uteslut tumör/aneurysm! Recidiv vanligt.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Pseudotumor Cerebri (se Idiopatisk Intrakraniell Hypertension)",
        "name_en": "Pseudotumor Cerebri",
        "icd10": "G93.2",
        "symptoms": [
            "(Se IIH ovan - samma tillstånd)"
        ],
        "anamnesis_questions": [
            "(Se IIH)"
        ],
        "clinical_signs": [
            "(Se IIH)"
        ],
        "risk_factors": [
            "(Se IIH)"
        ],
        "treatment": "(Se IIH)",
        "kva": "(Se IIH)",
        "differential_diagnoses": [
            "(Se IIH)"
        ],
        "description": "Pseudotumor cerebri är äldre term för Idiopatisk Intrakraniell Hypertension (IIH). Se IIH ovan för full beskrivning.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Vertebrobasilär Insufficiens med Synstörning",
        "name_en": "Vertebrobasilar Insufficiency with Visual Symptoms",
        "icd10": "G45.0",
        "symptoms": [
            "övergående bilateral synförlust (sekunders-minuters duration)",
            "ofta vid huvudrörelse eller reser sig snabbt",
            "diplopi möjlig",
            "yrsel, balansproblem",
            "drop attacks möjliga",
            "symptom vid fysisk ansträngning"
        ],
        "anamnesis_questions": [
            "Blir synen svart i båda ögonen?",
            "Hur länge varar episoderna?",
            "Utlöses det av huvudrörelse eller när du reser dig?",
            "Har du yrsel samtidigt?",
            "Har du balansproblem eller fallit plötsligt?",
            "Har du nacksmärta eller artros i nacken?"
        ],
        "clinical_signs": [
            "oftast normala fynd mellan attacker",
            "synfältsbortfall kan dokumenteras under attack",
            "eventuella posteriora cirkulationens stroke-tecken",
            "MRI: posteriora cirkulationens infarkter möjliga",
            "MRA/CTA: vertebralis eller basilaris stenosering/ocklusion",
            "doppler ultraljud halsartärer"
        ],
        "risk_factors": [
            "ålder >60 år",
            "ateroskleros",
            "hypertoni",
            "diabetes",
            "rökning",
            "vertebral artär dissekation",
            "cervical spondylos/artros",
            "subclavian steal syndrom"
        ],
        "treatment": "Antitrombotisk behandling (ASA, clopidogrel), behandla vaskulära riskfaktorer (blodtryck, diabetes, lipider), antikoagulation om förmaksflimmer, fysioterapi för cervical spondylos, kirurgisk revaskularisering sällan indicerat, prognos: risk för stroke i posteriora cirkulationen, uppföljning med neurolog",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Bilateral occipital stroke (permanent vs övergående)",
            "Migränaura",
            "Hypotension/synkope",
            "Papillödem med övergående synförlust"
        ],
        "description": "Vertebrobasilär insufficiens ger övergående bilateral synförlust vid otillräckligt flöde i posteriora cirkulationen. Ofta vid huvudrörelse eller positionsändring. Yrsel och balansproblem samtidigt. Utred med MRA/CTA. Antitrombotisk behandling. Risk för stroke.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Kortikalt Blindhet (Occipital Stroke)",
        "name_en": "Cortical Blindness",
        "icd10": "H47.6",
        "symptoms": [
            "bilateral synförlust",
            "normala pupillreaktioner (viktigt!)",
            "kan ha Anton's syndrom (förnekar blindhet - anosognosi)",
            "eventuella andra stroke-symptom",
            "kan vara partiell (hemianopsi)"
        ],
        "anamnesis_questions": [
            "Förlorade du synen plötsligt?",
            "Påverkas båda ögonen?",
            "Har du haft huvudvärk före? (migränaura)",
            "Har du haft stroke-symptom? (tal, motorik)",
            "Har du haft hjärtinfarkt eller förmaksflimmer?",
            "Ser du saker som inte finns? (Charles Bonnet - efter synförlust)"
        ],
        "clinical_signs": [
            "normala pupillreaktioner (ingen RAPD) - avgörande tecken!",
            "normala ögonbottnar",
            "bilateral homonyn hemianopsi eller total blindhet",
            "Anton's syndrom möjlig (förnekar blindhet, konfabulerar)",
            "eventuella andra neurologiska tecken",
            "MRI: bilateral occipital infarkt",
            "VEP (visuellt framkallad potential) avvikande"
        ],
        "risk_factors": [
            "stroke (embolisk, trombotisk)",
            "cardiac arrest (global hypoxisk-ischemisk skada)",
            "posteriort reversibelt encefalopati syndrom (PRES)",
            "hypertensiv kris",
            "eklampsi",
            "angiografi-komplikation",
            "vertebrobasilär insufficiens"
        ],
        "treatment": "Akut stroke-behandling om inom tidsfönster (trombolys, trombektomi), behandla underliggande orsak (förmaksflimmer, hypertoni), antitrombotisk profylax, rehabilitering och visuell träning, behandla Anton's syndrom (konfrontera försiktigt), prognos: varierande, viss återhämtning möjlig särskilt hos unga, Charles Bonnet hallucinationer kan uppstå (visuella hallucinationer efter synförlust - godartat, förklara för patient)",
        "kva": "Ingen (neurologisk stroke-behandling)",
        "differential_diagnoses": [
            "Bilateral optikusneuropati (RAPD, abnorma papiller)",
            "Funktionell synförlust (normalt VEP)",
            "Bilateral occipital tumör",
            "Posteriort reversibelt encefalopati syndrom (PRES)"
        ],
        "description": "Kortikalt blindhet är synförlust från bilateral occipital cortex-skada. Normala pupiller avgörande (skiljer från optiska neuropatier). Anton's syndrom: förnekar blindhet och konfabulerar. Orsaker: stroke, cardiac arrest, PRES. Varierande prognos.",
        "severity": "severe",
        "urgency": "emergency (akut stroke)"
    },
    {
        "name": "Funktionell Synförlust (Icke-Organisk)",
        "name_en": "Functional Vision Loss (Non-Organic)",
        "icd10": "H53.8",
        "symptoms": [
            "'tunnel vision' som inte varierar med avstånd",
            "påstådd blindhet med normal navigering",
            "inkonsistenta fynd",
            "överdramatiska reaktioner",
            "ofta barn/ungdomar eller efter trauma/stress",
            "sekundär vinst möjlig"
        ],
        "anamnesis_questions": [
            "Hur gammal är patienten? (ofta barn/tonår)",
            "Snubblar du över möbler? (bör vara nej om verklig blindhet)",
            "Har du haft stress eller trauma nyligen?",
            "Påverkas skola eller ekonomi av synförlust?",
            "Varierar symptomen mycket?",
            "Har du andra medicinska problem?"
        ],
        "clinical_signs": [
            "normala pupillreaktioner",
            "normal ögonbotten",
            "inkonsistenta synfältsbortfall",
            "tunnel vision som ej utvidgas med avstånd",
            "spiralformad synfältsinskränkning vid upprepat test",
            "normalt OKN (optokinetiskt nystagmus) - visar att patienten ser",
            "VEP normal",
            "förmåga navigera trots påstådd blindhet"
        ],
        "risk_factors": [
            "barn och ungdomar vanligast",
            "psykosociala stressorer",
            "efter trauma (även lätt) - 'posttraumatisk synförlust'",
            "sekundär vinst (ekonomisk kompensation, undvika skola/arbete)",
            "konversionsstörning",
            "malingering (medveten simulering)"
        ],
        "treatment": "Empatisk, icke-konfrontativ approach, försäkra att inga allvarliga ögonsjukdomar hittats, ge 'face-saving exit': 'Dina ögon är friska, synen kommer tillbaka gradvis', positiv förstärkning vid förbättring, psykologisk/psykiatrisk bedömning vid behov, behandla underliggande stress/ångest, undvik omfattande utredning (förstärker beteende), prognos: oftast full återhämtning hos barn med stöd, svårare hos vuxna med sekundär vinst",
        "kva": "Ingen (psykologisk behandling)",
        "differential_diagnoses": [
            "Faktisk organisk synförlust (uteslut först!)",
            "Kortikalt blindhet med anosognosi",
            "Bilateral optikusneuropati",
            "Malingering (medveten simulering vs omedveten konversion)"
        ],
        "description": "Funktionell synförlust är synnedsättning utan organisk orsak. Vanligast hos barn/ungdomar. Karakteristiska inkonsistenta fynd, tunnel vision, normal navigering. Normal VEP och OKN. Empatisk approach, ge 'face-saving exit'. Uteslut organisk orsak först. God prognos hos barn.",
        "severity": "mild (ögonmässigt)",
        "urgency": "routine"
    }
]
