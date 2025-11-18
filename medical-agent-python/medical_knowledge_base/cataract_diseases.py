"""
Katarakt Sjukdomar - 15 vanligaste
"""

CATARACT_DISEASES = [
    {
        "name": "Ålderskatarakt - Nukleär",
        "name_en": "Age-Related Nuclear Cataract",
        "icd10": "H25.1",
        "symptoms": [
            "gradvis synnedsättning",
            "svårigheter se på avstånd",
            "myopisering (närsynt-skift)",
            "nedsatt kontrastkänslighet",
            "bländningsproblem",
            "gulaktig färgton på syn",
            "svårigheter köra bil"
        ],
        "anamnesis_questions": [
            "Har synen försämrats gradvis?",
            "Behöver du starkare glasögon ofta?",
            "Har glasögonstyrkan gått mot närsynt?",
            "Ser färger gulaktiga ut?",
            "Har du svårt att se på avstånd?",
            "Har du svårt att köra bil, särskilt på natten?",
            "Hur gammal är du?"
        ],
        "clinical_signs": [
            "brunaktig/gulaktig färgning av linsnukleus",
            "gradvis ökande opacitet centralt",
            "kan läsa utan glasögon (myopiserng kompenserar presbyopi)",
            "nedsatt röd reflex",
            "grumling synlig vid spallampsundersökning"
        ],
        "risk_factors": [
            "hög ålder (>60 år)",
            "rökning",
            "UV-exponering",
            "diabetes",
            "myopi",
            "hereditet",
            "koststfaktorer (lågt vitamin C/E)"
        ],
        "treatment": "Kataraktkirurgi (fakoemulsifikation + IOL-inläggning) när patientens synbehov ej uppfylls, uppdatera glasögon innan operation övervägs, ingen medicinsk behandling förhindrar progression, operation mycket säker (95-98% lyckas), monofokala eller multifokala IOL beroende på patientens önskemål",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Posteriör subkapsulär katarakt",
            "Kortikal katarakt",
            "Andra orsaker till synnedsättning (AMD, glaukom)"
        ],
        "description": "Nukleär katarakt är vanligaste ålderskatarakt med grumling av linsnukleus. Ger myopiserng vilket ibland tillåter läsning utan glasögon ('second sight'). Gradvis progression över år.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Ålderskatarakt - Posteriör Subkapsulär (PSC)",
        "name_en": "Posterior Subcapsular Cataract",
        "icd10": "H25.0",
        "symptoms": [
            "bländning i starkt ljus/motljus",
            "kraftigt nedsatt syn vid stark belysning",
            "halos runt lampor",
            "svårigheter läsa trots relativt god syn",
            "snabbare progression än nukleär katarakt",
            "stora pupiller förbättrar syn (paradoxalt)"
        ],
        "anamnesis_questions": [
            "Är det värre att se i starkt ljus?",
            "Blir du kraftigt bländad av motljus?",
            "Har du svårt att läsa trots relativt god syn?",
            "Använder du kortison (tabletter, inhalation, ögondroppar)?",
            "Har du diabetes?",
            "Är du yngre än typisk starrpatient?"
        ],
        "clinical_signs": [
            "grumling precis under bakre linskap",
            "syns tydligare vid retroilluminering",
            "kan blockera central syn trots liten storlek",
            "ofta axial position"
        ],
        "risk_factors": [
            "kortikosteroidanvändning (viktigaste!)",
            "diabetes",
            "strålningsexponering",
            "myopi",
            "retinitis pigmentosa",
            "intraokulär inflammation",
            "yngre ålder än nukleär katarakt"
        ],
        "treatment": "Kataraktkirurgi ofta nödvändig tidigare än nukleär katarakt (bländning begränsar mer), YAG-laser capsulotomi ofta behövs postop (PCO vanligare), undvik kortisonbehandling om möjligt",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Posterior capsule opacification (efter operation)",
            "Nukleär katarakt",
            "Vitreous opacitet"
        ],
        "description": "PSC ger oproportionerligt mycket symptom relativt storleken pga central lokalisering. Starkt kopplad till kortikosteroidanvändning. Ofta hos yngre patienter. Snabbare progression.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Ålderskatarakt - Kortikal",
        "name_en": "Cortical Cataract",
        "icd10": "H25.0",
        "symptoms": [
            "gradvis synnedsättning",
            "bländning och halos",
            "monokulär diplopi möjlig",
            "asymmetrisk progression mellan ögonen ofta",
            "symptom varierar beroende på position av grumling"
        ],
        "anamnesis_questions": [
            "Ser du dubbelt med ett öga?",
            "Har du halos runt lampor?",
            "Varierar symptomen mycket?",
            "Är ett öga sämre än det andra?"
        ],
        "clinical_signs": [
            "radiära spoke-like opaciteter i linskortan",
            "vacuoles och water clefts",
            "cortical wedges",
            "kan vara perifera eller axial",
            "brunaktig diskolorering mindre än nukleär"
        ],
        "risk_factors": [
            "hög ålder",
            "kvinnligt kön (något vanligare)",
            "diabetes",
            "UV-exponering",
            "dehydrering",
            "låg kost av antioxidanter"
        ],
        "treatment": "Kataraktkirurgi när symptom påverkar funktion, kan vara asymtomatisk länge om perifert belägen, operation på båda ögonen ofta ej samtidigt behövs",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Nukleär katarakt",
            "PSC katarakt",
            "Traumatisk katarakt"
        ],
        "description": "Kortikal katarakt bildar spegeliknande opaciteter i linskortan. Kan vara asymtomatisk länge om perifer. Vanligare hos kvinnor och diabetiker.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Diabetisk Katarakt",
        "name_en": "Diabetic Cataract",
        "icd10": "H28.0",
        "symptoms": [
            "snabbare progression än typisk ålderskatarakt",
            "kan debutera yngre",
            "oftast PSC eller kortikal typ",
            "'true diabetic cataract' (sällsynt): akut bilateral snöflingeliknande grumling hos unga",
            "symptom som andra kataraktformer"
        ],
        "anamnesis_questions": [
            "Har du diabetes?",
            "Hur länge har du haft diabetes?",
            "Hur är din blodsockerkontroll?",
            "Har katarakten kommit snabbt?",
            "Har du diabetesretinopati?"
        ],
        "clinical_signs": [
            "PSC vanligast hos diabetiker",
            "kortikal näst vanligast",
            "snöflingeliknande opaciteter (true diabetic, sällsynt)",
            "ofta bilateral",
            "kan komma snabbare än ålderskatarakt"
        ],
        "risk_factors": [
            "diabetes (både typ 1 och 2)",
            "dålig glykemisk kontroll",
            "lång diabetesduration",
            "diabetesretinopati",
            "hyperglykemiska episoder"
        ],
        "treatment": "Förbättra glykemisk kontroll (bromsar progression), kataraktkirurgi när behövs, viktigt: screena och behandla diabetesretinopati FÖRE kataraktkirurgi, högre risk för postoperativa komplikationer (CME, progression av retinopati), överväg anti-VEGF preoperativt vid PDR",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Ålderskatarakt (men snabbare hos diabetiker)",
            "Steroidinducerad katarakt"
        ],
        "description": "Diabetiker utvecklar katarakt tidigare och snabbare. PSC och kortikal vanligast. Viktigt att behandla retinopati före operation. Ökad risk för CME postoperativt.",
        "severity": "moderate",
        "urgency": "routine (urgent vid retinopati)"
    },
    {
        "name": "Steroidinducerad Katarakt",
        "name_en": "Steroid-Induced Cataract",
        "icd10": "H26.3",
        "symptoms": [
            "gradvis synnedsättning",
            "bländning",
            "typiskt PSC-typ symptom",
            "historia av steroidanvändning"
        ],
        "anamnesis_questions": [
            "Använder du kortison?",
            "Vilken typ: tabletter, inhalation, nässpray, ögondroppar, hudkräm?",
            "Hur länge har du använt steroider?",
            "Vilken dos använder du?",
            "Har du astma, KOL, autoimmun sjukdom, transplantation?"
        ],
        "clinical_signs": [
            "PSC (posteriör subkapsulär) grumling",
            "dosberoende",
            "kan komma efter månader-år av behandling",
            "ofta bilateral men kan vara asymmetrisk"
        ],
        "risk_factors": [
            "systemisk steroidbehandling (tabletter)",
            "inhalationssteroider (särskilt höga doser)",
            "topikala ögondroppar med steroider",
            "intranasala steroider (mindre risk)",
            "intravitreala steroidinjektioner (Ozurdex, triamcinolon)",
            "dos och duration viktigast"
        ],
        "treatment": "Minska eller avsluta steroid om möjligt (saktar progression), kataraktkirurgi när symptom påverkar funktion, operation ofta säker, kommunicera med ordinarie läkare om steroidbehandling",
        "kva": "CJE00",
        "differential_diagnoses": [
            "PSC av annan orsak",
            "Ålderskatarakt"
        ],
        "description": "Steroidinducerad katarakt är vanlig biverkan vid långvarig steroidbehandling. PSC-typ. Dosberoende. Även inhalationssteroider kan ge katarakt. Viktigt att överväga vid steroidbehandling >1 år.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Traumatisk Katarakt",
        "name_en": "Traumatic Cataract",
        "icd10": "H26.1",
        "symptoms": [
            "synnedsättning efter ögontrauma",
            "kan komma akut eller månader-år senare",
            "ensidig",
            "symptom beroende på omfattning"
        ],
        "anamnesis_questions": [
            "Har du skadat ögat?",
            "Vad träffades ögat av?",
            "När var traumat?",
            "Penetrerade skadan ögat?",
            "Blev det blod i ögat?",
            "Opererades ögat efter skadan?"
        ],
        "clinical_signs": [
            "Contusionskatarakt: rosettliknande grumling, Vossius ring (pigment på främre linskap)",
            "Penetrerande: kapselruptur, kortikal grumling, eventuell linsmassa i främre kammaren",
            "lokaliserad grumling vid impactställe",
            "kan utvecklas långsamt efter trauma"
        ],
        "risk_factors": [
            "trubbigt trauma (slag, tennisboll, etc.)",
            "penetrerande skada",
            "intraokulära främmande kroppar",
            "elektrisk skada",
            "strålning"
        ],
        "treatment": "Akut: behandla eventuell kapselruptur, inflammation, uteslut främmande kropp, kataraktkirurgi när ögat lugnat sig (minst 6-8 veckor efter trauma om möjligt), kan vara komplicerad operation (zonulaskador, kapseldefekter), eventuellt suturer, kapsulära tensionsringar eller skleral-fixerad IOL",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Tidigare katarakt som upptäcks vid trauma",
            "Glaskroppsblödning (kan påverka syn)"
        ],
        "description": "Traumatisk katarakt uppstår efter trubbigt eller penetrerande trauma. Kan komma akut eller fördröjt. Ofta komplicerad kirurgi pga zonulaskador och kapseldefekter. Viktigt att vänta tills inflammation lugnat sig.",
        "severity": "moderate-severe",
        "urgency": "urgent (penetrerande), routine (stängd trauma)"
    },
    {
        "name": "Kongenital Katarakt",
        "name_en": "Congenital Cataract",
        "icd10": "Q12.0",
        "symptoms": [
            "vit pupill (leukokori) hos spädbarn",
            "nystagmus",
            "strabismus",
            "dålig fixation",
            "föräldrar märker att barnet ej följer med blicken"
        ],
        "anamnesis_questions": [
            "Såg pupillen vit ut hos barnet?",
            "Fixerar barnet blicken?",
            "Följer barnet rörelser?",
            "Finns katarakt i familjen?",
            "Hade mamman infektioner under graviditeten? (TORCH)",
            "Har barnet andra missbildningar eller syndrom?",
            "Är föräldrarna släkt (konsanguinitet)?"
        ],
        "clinical_signs": [
            "leukokori (vit pupill)",
            "katarakt synlig vid födsel eller tidigt",
            "kan vara total, polar, lamellar, sutural",
            "bilateral eller unilateral",
            "eventuella systemiska syndrom (Down, Marfan, etc.)"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant vanligast)",
            "TORCH-infektioner (Toxoplasma, Rubella, CMV, Herpes)",
            "metabola sjukdomar (galaktosemi, Lowe syndrom)",
            "syndrom (Down, Marfan, etc.)",
            "intrauterin hypoglykemi eller hypokalcemi",
            "läkemedel under graviditet"
        ],
        "treatment": "TIDIG kirurgi kritisk för att förhindra amblyopi (helst <6 veckor vid bilateral, <8 veckor vid unilateral), lensektomi/aspiration, IOL-inläggning kontroversiellt hos spädbarn (ofta afaka + kontaktlinser), aggressiv amblyopibehandling postop, livslång uppföljning, risk för glaukom postop, behandla underliggande orsak (galaktosemi kräver galaktosfri kost)",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Retinoblastom (viktigt att utesluta!)",
            "Persistent hyperplastiskt primär vitreum (PHPV)",
            "Retinopati av prematuritet",
            "Toxocara"
        ],
        "description": "Kongenital katarakt kräver tidig diagnos och behandling för att undvika permanent amblyopi. Viktigt att utesluta retinoblastom! Kan vara hereditet eller TORCH-infektioner. Tidig kirurgi ger bäst visuell prognos.",
        "severity": "severe",
        "urgency": "emergency (bilateral), urgent (unilateral)"
    },
    {
        "name": "Posterior Capsule Opacification (PCO) - Efterstarr",
        "name_en": "Posterior Capsule Opacification",
        "icd10": "H26.4",
        "symptoms": [
            "gradvis synnedsättning månader-år efter kataraktoperation",
            "bländning",
            "nedsatt kontrastkänslighet",
            "symptom liknar pre-operativ katarakt"
        ],
        "anamnesis_questions": [
            "Har du opererats för grå starr?",
            "Hur länge sedan var operationen?",
            "Var synen bra direkt efter operation men försämrats gradvis?",
            "Blir du bländad av ljus?",
            "Har du svårt att läsa trots operation?"
        ],
        "clinical_signs": [
            "grumling av bakre linskap efter kataraktkirurgi",
            "kan vara fibrotisk eller pärlformad (Elschnig pearls)",
            "IOL på plats",
            "grumling synlig bakom IOL"
        ],
        "risk_factors": [
            "yngre ålder vid kataraktkirurgi (barn 100% risk)",
            "uveit",
            "diabetes",
            "retinitis pigmentosa",
            "myopi",
            "typ av IOL (PMMA > akryl/silikon)"
        ],
        "treatment": "YAG-laser capsulotomi (öppning i bakre linskap) - poliklinisk, smärtfri behandling, effektiv hos 95%+, komplikationer sällsynta: tryckökning temporär, retinal avlossning (0.5-1%), cystoid maculaödem (sällsynt), IOL-pitting, kirurgisk capsulektomi mycket sällsynt",
        "kva": "CJD30",
        "differential_diagnoses": [
            "Ny katarakt (ovanligt med moderna IOL)",
            "Maculaödem",
            "AMD",
            "Andra retinala orsaker till synnedsättning"
        ],
        "description": "PCO (efterstarr) är vanligaste komplikationen efter kataraktkirurgi. Uppstår hos 20-40% inom 5 år. Linsepitelceller prolifererar på bakre kapseln. YAG-laser capsulotomi är enkel och effektiv behandling.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Komplikerad Katarakt vid Uveit",
        "name_en": "Complicated Cataract due to Uveitis",
        "icd10": "H26.2",
        "symptoms": [
            "gradvis synnedsättning hos patient med känd uveit",
            "kan ha episoder av rött, smärtsamt öga",
            "oftast PSC-typ symptom"
        ],
        "anamnesis_questions": [
            "Har du inflammation i ögat (uveit)?",
            "Har du autoimmun sjukdom?",
            "Använder du steroidögondroppar långvarigt?",
            "Har du Bechterews, sarkoidos eller JIA?",
            "Har du haft återkommande röda ögon?"
        ],
        "clinical_signs": [
            "katarakt (ofta PSC-typ)",
            "tecken på uveit: KP, synechiae, cellreaktion",
            "posteriora synechiae vanliga",
            "kan vara ung patient"
        ],
        "risk_factors": [
            "kronisk eller recidiverande uveit",
            "juvenil idiopatisk artrit (JIA)",
            "Fuchs heterokrom iridocyklit",
            "intermediär uveit",
            "långvarig steroidbehandling av uveit"
        ],
        "treatment": "Kontrollera inflammation FÖRE kirurgi (minst 3 månader lugn), perioperativ steroidbehandling, överväg immunosuppression, riskfylld operation (synechiae, inflammation, CME, hypotoni), god preoperativ planering essentiell, postoperativ inflammation ofta kraftigare",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Steroidinducerad katarakt (kan vara samma patient)",
            "Ålderskatarakt"
        ],
        "description": "Komplikerad katarakt vid uveit kan bero på själva inflammationen eller steroidbehandlingen. Kirurgi kräver god inflammationskontroll preoperativt. Högre risk för postoperativa komplikationer (CME, inflammation, hypotoni).",
        "severity": "moderate",
        "urgency": "routine (planerad efter inflammationskontroll)"
    },
    {
        "name": "Morgensotisk Katarakt (Hypermatur Katarakt)",
        "name_en": "Hypermature Cataract",
        "icd10": "H25.2",
        "symptoms": [
            "mycket dålig syn eller blindhet",
            "långvarig katarakt som ej opererats",
            "eventuell smärta om fakolytiskt glaukom utvecklas"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft grå starr?",
            "Varför har du inte opererat tidigare?",
            "Har du fått plötslig smärta eller rodnad? (fakolytiskt glaukom)",
            "Ser du ljusreflex fortfarande?"
        ],
        "clinical_signs": [
            "vit, tätt grumlig lins",
            "eventuell cortical liquefaction",
            "brunaktig eller vit lins",
            "eventuell fakodonesis (linsvackling) om zonulär svaghet",
            "risk för fakolytiskt glaukom",
            "fakomorft glaukom möjligt"
        ],
        "risk_factors": [
            "långa väntetider för operation",
            "socioekonomiska faktorer",
            "avsaknad av tillgång till sjukvård",
            "rädsla för operation",
            "hög ålder med multisjuklighet"
        ],
        "treatment": "Kataraktkirurgi, kan vara tekniskt svårare: risk för zonulär svaghet, kapselruptur, vitreous loss, överväg kapsulära tensionsringar, eventuellt suturer eller skleral-fixerad IOL, behandla fakolytiskt glaukom om present först",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Annan orsak till blindhet (glaukom, retinal avlossning)",
            "Endoftalmit (om smärta och rodnad)"
        ],
        "description": "Hypermatur katarakt uppstår när katarakt ej behandlas under lång tid. Linskortan kan liquefiera. Risk för fakolytiskt eller fakomorft glaukom. Kirurgi tekniskt svårare. Vanligare i utvecklingsländer.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Katarakt vid Myotonic Dystrofi",
        "name_en": "Cataract in Myotonic Dystrophy",
        "icd10": "H28.2",
        "symptoms": [
            "gradvis synnedsättning hos yngre patient",
            "polykromatiska fläckar i synfältet",
            "historia av muskelsvaghet"
        ],
        "anamnesis_questions": [
            "Har du muskelsvaghet?",
            "Har du svårt att släppa taget (myotoni)?",
            "Finns muskeldystrofi i familjen?",
            "Har du hjärtproblem?",
            "Är du relativt ung för katarakt?"
        ],
        "clinical_signs": [
            "'Christmas tree' katarakt (polykromatiska kristaller)",
            "PSC-typ grumling",
            "kan vara relativt ung patient (30-50 år)",
            "systemiska fynd: myotoni, muskelatrofi, bald frontal, ptosis"
        ],
        "risk_factors": [
            "myotonic dystrofi typ 1 (DM1)",
            "hereditet (autosomalt dominant)",
            "CTG-repeat expansion i DMPK-genen"
        ],
        "treatment": "Kataraktkirurgi när behövs, viktig anestesiologisk planering (malign hypertermi-risk, hjärtledningsrubbningar, andningsproblem), undvik suxamethonium, överväg lokal anestesi, god prognos för syn men systemsjukdom progressiv",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Ålderskatarakt hos ung patient",
            "Andra former av komplikerad katarakt"
        ],
        "description": "Myotonic dystrofi är vanligaste muskeldystrofi hos vuxna. Karakteristisk 'Christmas tree' katarakt med polykromatiska kristaller. Debuterar yngre. Viktig preoperativ bedömning pga anestesirisker.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Strålningsinducerad Katarakt",
        "name_en": "Radiation-Induced Cataract",
        "icd10": "H26.8",
        "symptoms": [
            "gradvis synnedsättning efter strålningsexponering",
            "latenstid månader-år",
            "symptom som PSC katarakt"
        ],
        "anamnesis_questions": [
            "Har du fått strålbehandling mot huvudet/ögat?",
            "Har du arbetat med strålning?",
            "Har du utsatts för radioaktiv strålning?",
            "När var exponeringen?",
            "Vilken dos fick du?"
        ],
        "clinical_signs": [
            "PSC-typ katarakt",
            "dosberoende",
            "latenstid: månader till år beroende på dos",
            "bilateral om systemisk strålning",
            "eventuell strålningsretinopati samtidigt"
        ],
        "risk_factors": [
            "strålbehandling mot hjärntumör, näsa-svalg-tumör",
            "radioterapi mot intraokulär tumör",
            "total body irradiation (benmärgstransplantation)",
            "radioaktiv exponering (olyckor)",
            "UV-strålning (bidragande)"
        ],
        "treatment": "Kataraktkirurgi när symptomatisk, ingen profylax förhindrar utveckling efter exponering, moderna stråltekniker (IMRT) minskar risk, behandla eventuell samtidig strålningsretinopati",
        "kva": "CJE00",
        "differential_diagnoses": [
            "PSC av annan orsak",
            "Steroidinducerad katarakt (ofta kombinerat vid cancerbehandling)"
        ],
        "description": "Strålningsinducerad katarakt uppstår efter joniserande strålning mot ögat/huvudet. Dosberoende med latenstid. PSC-typ vanligast. Risk redan vid doser >2 Gy. Moderna radiotekniker minskar risk.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Katarakt vid Atopisk Dermatit",
        "name_en": "Atopic Cataract",
        "icd10": "H28.0",
        "symptoms": [
            "bilateral katarakt hos ung patient med atopi",
            "snabb progression",
            "ofta PSC eller anterior subkapsulär",
            "historia av eksem och allergi"
        ],
        "anamnesis_questions": [
            "Har du atopiskt eksem?",
            "Har du astma eller allergi?",
            "Gnuggar du mycket i ögonen?",
            "Är du ung för att få grå starr?",
            "Har du eksem i ansiktet?"
        ],
        "clinical_signs": [
            "PSC eller anterior subkapsulär katarakt",
            "shield-formad katarakt vid vernal keratokonjunktivit",
            "oftast bilateral",
            "kan utvecklas snabbt hos unga (10-30 år)",
            "eventuell keratokonus (associerad)"
        ],
        "risk_factors": [
            "atopisk dermatit (särskilt svår)",
            "vernal keratokonjunktivit",
            "trauma från ögongnuggning",
            "steroidbehandling av atopi (bidragande)"
        ],
        "treatment": "Kataraktkirurgi när symptomatisk, kontrollera atopisk sjukdom, minska ögongnuggning, behandla blepharit/konjunktivit samtidigt, högre risk för postoperativ inflammation",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Steroidinducerad katarakt (ofta kombinerat)",
            "Traumatisk katarakt (från gnuggning)"
        ],
        "description": "Atopisk katarakt utvecklas hos 10-25% med svår atopisk dermatit. Ofta unga patienter. Kan vara relaterad till ögongnuggning och/eller steroidbehandling. Snabb progression.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Katarakt vid Pseudoexfoliation",
        "name_en": "Cataract with Pseudoexfoliation",
        "icd10": "H26.8",
        "symptoms": [
            "symptom som vanlig ålderskatarakt",
            "ofta nukleär typ",
            "kan ha förhöjt ögontryck samtidigt"
        ],
        "anamnesis_questions": [
            "Har du glaukom eller högt ögontryck?",
            "Har du skandinaviskt ursprung?",
            "Hur gammalt är du? (oftast >60 år)"
        ],
        "clinical_signs": [
            "exfoliationsmaterial på främre linskap (target pattern)",
            "katarakt (oftast nukleär)",
            "zonulär svaghet/utsvagning",
            "fakodonesis (linsvackling) möjlig",
            "förhöjt ögontryck vanligt"
        ],
        "risk_factors": [
            "pseudoexfoliation syndrom",
            "hög ålder",
            "skandinaviskt ursprung",
            "hereditet"
        ],
        "treatment": "Kataraktkirurgi MEN högre risk för komplikationer: zonulär svaghet/dialysis, kapselruptur, vitreous loss, linsdrop, använd kapsulära tensionsringar ofta, överväg iris hooks/retraktorer, miosis intraoperativt (zonulärt stöd), postoperativt: IOL-decentrering/subluxation kan ske senare, behandla samtidigt glaukom",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Vanlig ålderskatarakt (men exfoliation märks vid spallampa)",
            "Traumatisk katarakt med zonulaskada"
        ],
        "description": "Katarakt vid pseudoexfoliation har högre kirurgisk risk pga zonulär svaghet. Vanligast i Skandinavien. Ofta kombinerad med glaukom. Kräver erfaren kirurg och ibland extra tekniker (CTR, iris hooks).",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Katarakt efter Vitrektomi",
        "name_en": "Post-Vitrectomy Cataract",
        "icd10": "H26.8",
        "symptoms": [
            "gradvis synnedsättning månader-år efter vitrektomikirurgi",
            "snabbare progression än normal ålderskatarakt"
        ],
        "anamnesis_questions": [
            "Har du opererats med vitrektomi?",
            "Hur länge sedan var operationen?",
            "Var du fak (med lins) när du opererades?",
            "Fick du gasbubbla eller silikonomja?"
        ],
        "clinical_signs": [
            "nukleär eller PSC katarakt",
            "snabbare progression än vanligt",
            "ofta inom 1-2 år efter vitrektomi",
            "nästan 100% vid fak vitrektomi hos äldre"
        ],
        "risk_factors": [
            "vitrektomi (särskilt fak)",
            "gasbubbla (accelererar kataraktutveckling)",
            "silikonomja (särskilt långvarig)",
            "lins-touch under operation",
            "hög ålder vid vitrektomi"
        ],
        "treatment": "Kombinerad vitrektomi + kataraktkirurgi kan övervägas primärt hos äldre, kataraktkirurgi när symptomatisk efter vitrektomi, operation oftast okomplicerad, eventuellt silikonomja kvar under operation (silikon-fyllt öga)",
        "kva": "CJE00",
        "differential_diagnoses": [
            "Ålderskatarakt (men snabbare progression)",
            "Epiretinal membran (kan också ge synnedsättning postvitrektomi)"
        ],
        "description": "Katarakt utvecklas hos nästan alla äldre som genomgår fak vitrektomi. Gasbubbla och silikonomja accelererar utveckling. Många kirurger gör nu kombinerad vitrektomi + fakoemulsifikation primärt hos äldre >60 år.",
        "severity": "moderate",
        "urgency": "routine"
    }
]
