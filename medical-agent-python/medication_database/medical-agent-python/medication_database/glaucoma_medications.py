"""
Trycknedsättande läkemedel (Glaukom)
20 vanligaste läkemedel för behandling av förhöjt IOP och glaukom
"""

GLAUCOMA_MEDICATIONS = [
    # PROSTAGLANDINANALOGER
    {
        "name": "Xalatan (Latanoprost)",
        "generic_name": "Latanoprost",
        "category": "Prostaglandinanalog",
        "formulation": "Ögondroppar",
        "concentration": "50 μg/ml (0.005%)",
        "indications": [
            "primär öppenvinklat glaukom (POAG)",
            "okulär hypertension",
            "normaltrycksglaukom"
        ],
        "mechanism": "Ökar uveoskleralt utflöde av kammarvatten via prostaglandin F2-alfa receptorer",
        "dosage": "1 droppe i drabbat öga en gång dagligen på kvällen",
        "contraindications": [
            "överkänslighet mot latanoprost eller konserveringsmedel",
            "aktiv uveit eller CME-historia"
        ],
        "side_effects": [
            "ökad irispigmentering (permanent, särskilt i hazel ögon)",
            "förlängda fransar (längre, tjockare, mörkare)",
            "konjunktival hyperemi",
            "periorbitalt ökad pigmentering",
            "hypertrikos på ögonlock",
            "cystoid maculaödem (CME) - sällsynt, risk vid afaki/pseudofaki med öppen bakre kapsel",
            "reaktiverad HSV-keratit"
        ],
        "pregnancy_category": "C (undvik under graviditet)",
        "interactions": ["kan interagera med andra prostaglandiner"],
        "special_considerations": "Applicera på kvällen för bästa effekt. Vänta 5 min mellan olika droppar. Ta ut kontaktlinser före applicering (sätt in efter 15 min). IOP-sänkning 25-35%. Varning till patient om ökad irispigmentering (irreversibel) och förlängda fransar.",
        "storage": "Oöppnad: kylskåp (2-8°C). Öppnad: rumstemperatur, använd inom 4 veckor",
        "atc_code": "S01EE01"
    },
    {
        "name": "Lumigan (Bimatoprost)",
        "generic_name": "Bimatoprost",
        "category": "Prostaglandinanalog",
        "formulation": "Ögondroppar",
        "concentration": "0.1 mg/ml och 0.3 mg/ml",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Prostamid-analog, ökar uveoskleralt och trabekulärt utflöde",
        "dosage": "1 droppe en gång dagligen på kvällen",
        "contraindications": ["överkänslighet"],
        "side_effects": [
            "konjunktival hyperemi (mer än latanoprost)",
            "ökad irispigmentering",
            "förlängda fransar (ofta mer än latanoprost)",
            "periorbitalt ökad pigmentering",
            "CME (sällsynt)",
            "lokal inflammation"
        ],
        "pregnancy_category": "C",
        "interactions": [],
        "special_considerations": "Mest effektiv prostaglandinanalog (IOP-sänkning 30-35%). Mer hyperemi än andra. Finns konserveringsmedelfri formulering (Lumigan 0.1 mg/ml). Används off-label för fransförlängning (Latisse).",
        "storage": "Rumstemperatur, använd inom 4 veckor efter öppning",
        "atc_code": "S01EE03"
    },
    {
        "name": "Travatan (Travoprost)",
        "generic_name": "Travoprost",
        "category": "Prostaglandinanalog",
        "formulation": "Ögondroppar",
        "concentration": "40 μg/ml",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Prostaglandin F2-alfa analog, ökar uveoskleralt utflöde",
        "dosage": "1 droppe en gång dagligen på kvällen",
        "contraindications": ["överkänslighet"],
        "side_effects": [
            "konjunktival hyperemi",
            "ökad irispigmentering",
            "förlängda fransar",
            "ögonirritation",
            "CME (sällsynt)"
        ],
        "pregnancy_category": "C",
        "interactions": [],
        "special_considerations": "Liknar latanoprost i effekt. IOP-sänkning 25-30%. Mindre hyperemi än bimatoprost.",
        "storage": "Rumstemperatur, använd inom 4 veckor",
        "atc_code": "S01EE04"
    },
    {
        "name": "Tafluprost (Saflutan/Taflotan)",
        "generic_name": "Tafluprost",
        "category": "Prostaglandinanalog",
        "formulation": "Ögondroppar (konserveringsmedelfri)",
        "concentration": "15 μg/ml",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Prostaglandin F2-alfa analog, ökar uveoskleralt utflöde",
        "dosage": "1 droppe en gång dagligen på kvällen",
        "contraindications": ["överkänslighet"],
        "side_effects": [
            "konjunktival hyperemi (mindre än andra pga konserveringsmedelfri)",
            "ökad irispigmentering",
            "förlängda fransar",
            "ögonirritation (mindre pga konserveringsmedelfri)"
        ],
        "pregnancy_category": "C",
        "interactions": [],
        "special_considerations": "KONSERVERINGSMEDELFRI - bättre tolerans. IOP-sänkning 25-30%. Bra val vid torrt ögon, okulär ytsjukdom, eller planerad glaukomkirurgi. Endos-behållare (en droppe per behållare).",
        "storage": "Kylskåp före öppning. Rumstemperatur efter, använd omedelbart (endosbehållare)",
        "atc_code": "S01EE05"
    },
    {
        "name": "Omidria (Fenylefrin + Ketorolac intrakamralt)",
        "generic_name": "Phenylephrine 10 mg/ml + Ketorolac 3 mg/ml",
        "category": "Intrakamral mydriasis och antiinflammatorisk",
        "formulation": "Intrakamral lösning (används under kataraktkirurgi)",
        "concentration": "Fenylefrin 10 mg/ml + Ketorolak 3 mg/ml",
        "indications": [
            "upprätthålla mydriasis under kataraktkirurgi",
            "förhindra intraoperativ mios",
            "minska postoperativ smärta"
        ],
        "mechanism": "Fenylefrin: alfa-1-agonist (mydriasis). Ketorolac: NSAID (minskar inflammation och smärta)",
        "dosage": "Tillsätt 4 ml till 500 ml irrigationslösning under kataraktkirurgi",
        "contraindications": ["överkänslighet mot fenylefrin eller ketorolak"],
        "side_effects": [
            "ögonsmärta (postoperativt)",
            "fotopsi",
            "konjunktival hyperemi",
            "korneal ödem",
            "anterior chamber inflammation"
        ],
        "pregnancy_category": "C",
        "interactions": ["undvik NSAID om aspirin-allergi"],
        "special_considerations": "Används ENDAST intrakamralt under kataraktkirurgi. Minskar risk för intraoperativ floppy iris syndrom (IFIS). Dyrt men effektivt vid svår mios eller IFIS-risk (t.ex. Tamsulosin-användare).",
        "storage": "Kylskåp",
        "atc_code": "S01EX (kombination)"
    },

    # BETA-BLOCKERARE
    {
        "name": "Timolol (Timoptic/Titempol)",
        "generic_name": "Timolol maleat",
        "category": "Beta-blockerare (icke-selektiv)",
        "formulation": "Ögondroppar",
        "concentration": "2.5 mg/ml (0.25%) och 5 mg/ml (0.5%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension",
            "sekundära glaukom"
        ],
        "mechanism": "Icke-selektiv beta-1 och beta-2 receptor blockad, minskar kammarvattenproduktion",
        "dosage": "1 droppe 0.25-0.5% två gånger dagligen (eller en gång dagligen med gel-formulering)",
        "contraindications": [
            "astma eller svår KOL",
            "bradykardi (<50 slag/min)",
            "AV-block grad II-III",
            "manifest hjärtsvikt",
            "kardiogen chock",
            "spädbarn (risk för apné)"
        ],
        "side_effects": [
            "bronkospasm (farligt vid astma!)",
            "bradykardi",
            "hypotension",
            "trötthet, depression",
            "minskad libido",
            "maskerar hypoglykemi-symtom (diabetiker)",
            "torrt ögon",
            "superficiell punktat keratopati"
        ],
        "pregnancy_category": "C (beta-blockerare kan påverka foster)",
        "interactions": [
            "kalciumantagonister (ökad bradykardi-risk)",
            "andra beta-blockerare (additiv effekt)",
            "insulin/antidiabetika (maskerar hypoglykemi)"
        ],
        "special_considerations": "VARNING vid astma/KOL - kan utlösa livshotande bronkospasm! IOP-sänkning 20-25%. Takyfylaxi kan utvecklas (minskad effekt över tid). Punktal ocklusion rekommenderas (minskar systemisk absorption). Kontrollera puls och andning hos äldre. Finns gel-formulering (Timoptic-XE) för en gång daglig dosering.",
        "storage": "Rumstemperatur",
        "atc_code": "S01ED01"
    },
    {
        "name": "Betoptic (Betaxolol)",
        "generic_name": "Betaxolol",
        "category": "Beta-1 selektiv blockerare",
        "formulation": "Ögondroppar",
        "concentration": "5 mg/ml (0.5%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Selektiv beta-1 receptor blockad, minskar kammarvattenproduktion",
        "dosage": "1 droppe två gånger dagligen",
        "contraindications": [
            "bradykardi",
            "hjärtblock grad II-III",
            "manifest hjärtsvikt"
        ],
        "side_effects": [
            "mindre bronkospasm än timolol (beta-1 selektiv)",
            "bradykardi",
            "torrt ögon",
            "trötthet (mindre än timolol)"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister"],
        "special_considerations": "BÄTTRE val än timolol vid mild astma/KOL (men fortfarande försiktighet!). Beta-1 selektivitet minskar bronkospasm-risk. Mindre effektiv än timolol (IOP-sänkning 15-20%). Bättre okulär blodflöde än timolol (teoretisk fördel vid normaltrycksglaukom).",
        "storage": "Rumstemperatur",
        "atc_code": "S01ED02"
    },
    {
        "name": "Carteolol",
        "generic_name": "Carteolol",
        "category": "Beta-blockerare (icke-selektiv med ISA)",
        "formulation": "Ögondroppar",
        "concentration": "10 mg/ml (1%) och 20 mg/ml (2%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Icke-selektiv beta-blockad med intrinsic sympathomimetic activity (ISA), minskar kammarvattenproduktion",
        "dosage": "1 droppe två gånger dagligen",
        "contraindications": [
            "astma/KOL",
            "bradykardi",
            "hjärtblock"
        ],
        "side_effects": [
            "mindre bradykardi än timolol (pga ISA)",
            "bronkospasm (mindre risk än timolol)",
            "torrt ögon",
            "trötthet"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister"],
        "special_considerations": "ISA-aktivitet ger mindre bradykardi och bronkospasm än timolol. IOP-sänkning liknande timolol (20-25%). Mindre använd i Sverige än timolol.",
        "storage": "Rumstemperatur",
        "atc_code": "S01ED05"
    },
    {
        "name": "Levobunolol",
        "generic_name": "Levobunolol",
        "category": "Beta-blockerare (icke-selektiv)",
        "formulation": "Ögondroppar",
        "concentration": "2.5 mg/ml (0.25%) och 5 mg/ml (0.5%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Icke-selektiv beta-blockad, minskar kammarvattenproduktion",
        "dosage": "1 droppe en eller två gånger dagligen",
        "contraindications": [
            "astma/KOL",
            "bradykardi",
            "hjärtblock"
        ],
        "side_effects": [
            "bronkospasm",
            "bradykardi",
            "torrt ögon",
            "trötthet"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister"],
        "special_considerations": "Liknar timolol i effekt och biverkningar. Något längre verkningstid (kan doseras en gång dagligen hos vissa). IOP-sänkning 20-25%.",
        "storage": "Rumstemperatur",
        "atc_code": "S01ED03"
    },

    # KARBOANHYDRASHÄMMARE (CAI)
    {
        "name": "Azopt (Brinzolamid)",
        "generic_name": "Brinzolamid",
        "category": "Karboanhydrashämmare (CAI) - topikal",
        "formulation": "Ögondroppar (suspension)",
        "concentration": "10 mg/ml (1%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension",
            "tillägg till andra trycknedsättande läkemedel"
        ],
        "mechanism": "Hämmar karboanhydras II i ciliarkroppen, minskar kammarvattenproduktion",
        "dosage": "1 droppe två till tre gånger dagligen",
        "contraindications": [
            "svår njursvikt (GFR <30)",
            "hyperklor acidosis",
            "sulfonamid-allergi"
        ],
        "side_effects": [
            "bitter smak i munnen",
            "suddig syn (temporärt, pga suspension)",
            "lokal irritation, brännande känsla",
            "blefarit",
            "torrt ögon",
            "sällan: systemiska effekter (trötthet, parestesier) men mycket mindre än acetazolamid"
        ],
        "pregnancy_category": "C",
        "interactions": [
            "salicylater (teoretisk risk vid höga doser)",
            "andra CAI (additiv effekt)"
        ],
        "special_considerations": "SKAKA flaskan före användning (suspension). IOP-sänkning 15-20%. Mindre systemiska biverkningar än Diamox. Bättre tolerans än dorzolamid (mindre brännande känsla). Ofta i kombination med prostaglandin eller betablockerare.",
        "storage": "Rumstemperatur",
        "atc_code": "S01EC04"
    },
    {
        "name": "Trusopt (Dorzolamid)",
        "generic_name": "Dorzolamid",
        "category": "Karboanhydrashämmare (CAI) - topikal",
        "formulation": "Ögondroppar",
        "concentration": "20 mg/ml (2%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension",
            "pseudoexfoliativ glaukom"
        ],
        "mechanism": "Hämmar karboanhydras II, minskar kammarvattenproduktion",
        "dosage": "1 droppe tre gånger dagligen (monoterapi) eller två gånger dagligen (tillägg)",
        "contraindications": [
            "svår njursvikt",
            "hyperklor acidosis",
            "sulfonamid-allergi"
        ],
        "side_effects": [
            "brännande och stickande känsla (mer än brinzolamid)",
            "bitter smak",
            "konjunktival hyperemi",
            "superficiell punktat keratopati",
            "blefarit",
            "sällan systemiska effekter"
        ],
        "pregnancy_category": "C",
        "interactions": ["salicylater"],
        "special_considerations": "MER brännande känsla än Azopt (därför mindre använd som monoterapi). IOP-sänkning 15-20%. Bättre compliance med Azopt. Ofta i kombination (Cosopt = dorzolamid + timolol).",
        "storage": "Rumstemperatur",
        "atc_code": "S01EC03"
    },
    {
        "name": "Diamox (Acetazolamid)",
        "generic_name": "Acetazolamid",
        "category": "Karboanhydrashämmare (CAI) - systemisk",
        "formulation": "Tabletter, IV-injektion",
        "concentration": "250 mg tabletter, 500 mg IV",
        "indications": [
            "akut glaukom (nödbehandling)",
            "peroperativ IOP-kontroll",
            "sekundära glaukom",
            "malign glaukom"
        ],
        "mechanism": "Systemisk karboanhydrashämning, minskar kammarvattenproduktion kraftigt",
        "dosage": "250-500 mg två till fyra gånger dagligen (akut: 500 mg IV, sedan 250 mg p.o. 4 ggr/dag)",
        "contraindications": [
            "svår njur- eller leversvikt",
            "Addisons sjukdom",
            "hypokalemi, hyponatremi",
            "hyperklor acidosis",
            "sulfonamid-allergi"
        ],
        "side_effects": [
            "parestesier (stickningar i fingrar/tår) - mycket vanligt",
            "trötthet, illamående",
            "smakförändringar (metallisk smak)",
            "polyuri, polydipsi",
            "hypokalemi (farligt!)",
            "metabolisk acidos",
            "njursten (vid långtidsbehandling)",
            "aplastisk anemi (sällsynt men allvarligt)",
            "Stevens-Johnson syndrom (sällsynt)"
        ],
        "pregnancy_category": "C",
        "interactions": [
            "diuretika (ökad hypokalemi-risk)",
            "aspirin (ökad toxicitet)"
        ],
        "special_considerations": "KRAFTIG IOP-sänkning (30-40%). Används främst AKUT (akut glaukom, preoperativt). Inte för långtidsbehandling pga biverkningar. MONITORERA elektrolyter (K+, Na+, HCO3-) vid långtidsbehandling. Kaliumtillskott ofta nödvändigt. Sekventiell användning rekommenderas (250 mg 2 ggr dagligen i 3 dagar, sedan uppehåll 1 dag, upprepa).",
        "storage": "Rumstemperatur",
        "atc_code": "S01EC01"
    },
    {
        "name": "Neptazane (Metazolamid)",
        "generic_name": "Metazolamid",
        "category": "Karboanhydrashämmare (CAI) - systemisk",
        "formulation": "Tabletter",
        "concentration": "25-50 mg tabletter",
        "indications": [
            "primär öppenvinklat glaukom",
            "sekundära glaukom",
            "akut glaukom"
        ],
        "mechanism": "Systemisk karboanhydrashämning, minskar kammarvattenproduktion",
        "dosage": "50-100 mg två till tre gånger dagligen",
        "contraindications": [
            "svår njur- eller leversvikt",
            "sulfonamid-allergi",
            "hypokalemi"
        ],
        "side_effects": [
            "MINDRE parestesier än acetazolamid",
            "trötthet",
            "illamående",
            "hypokalemi (mindre än acetazolamid)",
            "metabolisk acidos"
        ],
        "pregnancy_category": "C",
        "interactions": ["diuretika"],
        "special_considerations": "BÄTTRE tolerans än Diamox (färre parestesier). IOP-sänkning liknande Diamox men något svagare. Kan användas längre tid än Diamox. Mindre tillgänglig än Diamox i många länder.",
        "storage": "Rumstemperatur",
        "atc_code": "S01EC05"
    },

    # ALFA-2-AGONISTER
    {
        "name": "Alphagan (Brimonidin)",
        "generic_name": "Brimonidin tartrat",
        "category": "Alfa-2-adrenerg agonist",
        "formulation": "Ögondroppar",
        "concentration": "2 mg/ml (0.2%) och 1.5 mg/ml (0.15%)",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension",
            "tillägg till andra trycknedsättande läkemedel"
        ],
        "mechanism": "Alfa-2-adrenerg agonist: minskar kammarvattenproduktion OCH ökar uveoskleralt utflöde",
        "dosage": "1 droppe två till tre gånger dagligen",
        "contraindications": [
            "barn <2 år (risk för CNS-depression, apné)",
            "MAO-hämmare-behandling",
            "svår kardiovaskulär sjukdom"
        ],
        "side_effects": [
            "allergisk konjunktivit (15-20% utvecklar allergi vid långtidsbehandling - VANLIG orsak till utsättning!)",
            "torrt mun",
            "trötthet, dåsighet",
            "hypotension",
            "blefarit, konjunktival hyperemi",
            "blekning av konjunktiva",
            "CNS-depression hos barn (FARLIGT!)"
        ],
        "pregnancy_category": "B",
        "interactions": [
            "MAO-hämmare (kontraindicerat)",
            "tricykliska antidepressiva",
            "CNS-depressiva läkemedel"
        ],
        "special_considerations": "HÖG allergi-risk (takyfylaxi/allergi i 15-20%). IOP-sänkning 20-25%. Neuroprotektiv effekt (teoretisk fördel vid normaltrycksglaukom). Används ofta som tillägg vid otillräcklig effekt. ALDRIG till små barn (<2 år)! Finns konserveringsmedelfri form (Alphagan-P 0.15%) - bättre tolerans.",
        "storage": "Rumstemperatur",
        "atc_code": "S01EA05"
    },
    {
        "name": "Iopidine (Apraklonidin)",
        "generic_name": "Apraklonidin",
        "category": "Alfa-2-adrenerg agonist",
        "formulation": "Ögondroppar",
        "concentration": "5 mg/ml (0.5%) och 10 mg/ml (1%)",
        "indications": [
            "förebygga IOP-stegring efter laser (YAG, SLT, ALT)",
            "korttids-IOP-kontroll preoperativt",
            "akut IOP-sänkning"
        ],
        "mechanism": "Alfa-2-adrenerg agonist, minskar kammarvattenproduktion",
        "dosage": "1 droppe 1 timme före och omedelbart efter laserprocedur. INTE för långtidsbehandling.",
        "contraindications": [
            "MAO-hämmare",
            "barn"
        ],
        "side_effects": [
            "MYCKET HÖG allergi-risk vid långtidsbehandling (upp till 50%!)",
            "blekning av konjunktiva",
            "mydriasis",
            "torrt mun",
            "trötthet"
        ],
        "pregnancy_category": "C",
        "interactions": ["MAO-hämmare"],
        "special_considerations": "Används ENDAST kort tid (runt laser-procedurer). INTE för långtidsbehandling pga extrem allergi-risk. IOP-sänkning 20-30% kortvarigt. 1% används 1h före + efter laser, 0.5% kan användas upp till 1 vecka postop.",
        "storage": "Rumstemperatur",
        "atc_code": "S01EA03"
    },

    # MIOTIKA (parasympatomimetika)
    {
        "name": "Pilokarpin",
        "generic_name": "Pilokarpin",
        "category": "Parasympatomimetikum (miotikum)",
        "formulation": "Ögondroppar",
        "concentration": "10 mg/ml (1%), 20 mg/ml (2%), 40 mg/ml (4%)",
        "indications": [
            "akut trångvinkelglaukom (EMERGENCY-behandling)",
            "plateau iris syndrom",
            "adjuvans vid primär öppenvinklat glaukom (numera sällan)",
            "motverka mydriasis (diagnostiskt)"
        ],
        "mechanism": "Muskarinerg agonist, kontraherar iris-sphincter (mios) och ciliarmuskeln, öppnar trabekulärt meshwork, ökar kammarvattenutflöde",
        "dosage": "1-2 droppar 3-4 gånger dagligen (akut glaukom: var 15-30 min initialt)",
        "contraindications": [
            "akut uveit (inflammation)",
            "irido-corneal touch",
            "ung ålder med myopi (ökad myopiseringsrisk)"
        ],
        "side_effects": [
            "inducerad myopi (närsynthet, särskilt hos unga)",
            "huvudvärk, browache (ciliarspasm)",
            "minskad mörkerseende (mios)",
            "ackommodationskramp",
            "retinal avlossning (sällsynt, hos höggradsmyoper)",
            "ökad uveit-risk",
            "katarakt (vid långtidsbehandling)",
            "posterior synechiae (vid uveit)",
            "systemiska effekter (sällan): svettning, salivation, bradykardi"
        ],
        "pregnancy_category": "C",
        "interactions": ["antikolinergika (motverkar effekt)"],
        "special_considerations": "ÄLDRE läkemedel, nu mindre använt för POAG (ersatt av prostaglandiner). Fortfarande VIKTIGT vid akut glaukom. VARNING till patient: suddig närseende, minskad mörkerseende (bilkörning!). Ung myop: risk för retinal avlossning. Pupillen blir mycket liten (\"pinpoint pupil\"). Svårt att undersöka fundus.",
        "storage": "Rumstemperatur",
        "atc_code": "S01EB01"
    },

    # KOMBINATIONSPREPARAT
    {
        "name": "Xalacom (Latanoprost + Timolol)",
        "generic_name": "Latanoprost 50 μg/ml + Timolol 5 mg/ml",
        "category": "Kombinationspreparat (prostaglandin + beta-blockerare)",
        "formulation": "Ögondroppar",
        "concentration": "Latanoprost 0.005% + Timolol 0.5%",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension otillräckligt kontrollerad med monoterapi"
        ],
        "mechanism": "Dubbel mekanism: latanoprost ökar utflöde, timolol minskar produktion",
        "dosage": "1 droppe en gång dagligen på morgonen",
        "contraindications": [
            "astma/KOL (timolol-komponent)",
            "bradykardi, hjärtblock",
            "manifest hjärtsvikt"
        ],
        "side_effects": [
            "kombinerade biverkningar från båda läkemedlen",
            "irispigmentering (latanoprost)",
            "förlängda fransar (latanoprost)",
            "bronkospasm (timolol)",
            "bradykardi (timolol)"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister (timolol)"],
        "special_considerations": "Bättre compliance (en gång dagligen vs två separata droppar). IOP-sänkning 30-35%. Applicera på morgonen (inte kväll som monoterapi latanoprost). SAMMA kontraindikationer som timolol.",
        "storage": "Oöppnad: kylskåp. Öppnad: rumstemperatur, använd inom 4 veckor",
        "atc_code": "S01ED51"
    },
    {
        "name": "Cosopt (Dorzolamid + Timolol)",
        "generic_name": "Dorzolamid 20 mg/ml + Timolol 5 mg/ml",
        "category": "Kombinationspreparat (CAI + beta-blockerare)",
        "formulation": "Ögondroppar",
        "concentration": "Dorzolamid 2% + Timolol 0.5%",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension otillräckligt kontrollerad med monoterapi"
        ],
        "mechanism": "Dubbel mekanism: båda minskar kammarvattenproduktion via olika vägar",
        "dosage": "1 droppe två gånger dagligen",
        "contraindications": [
            "astma/KOL",
            "bradykardi, hjärtblock",
            "svår njursvikt (dorzolamid)",
            "sulfonamid-allergi"
        ],
        "side_effects": [
            "brännande känsla (dorzolamid)",
            "bitter smak",
            "bronkospasm (timolol)",
            "bradykardi (timolol)",
            "trötthet"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister", "salicylater"],
        "special_considerations": "IOP-sänkning 25-30%. Bättre compliance än separata droppar. SAMMA kontraindikationer som timolol. Finns konserveringsmedelfri variant (Cosopt PF).",
        "storage": "Rumstemperatur",
        "atc_code": "S01ED51"
    },
    {
        "name": "DuoTrav (Travoprost + Timolol)",
        "generic_name": "Travoprost 40 μg/ml + Timolol 5 mg/ml",
        "category": "Kombinationspreparat (prostaglandin + beta-blockerare)",
        "formulation": "Ögondroppar",
        "concentration": "Travoprost 0.004% + Timolol 0.5%",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Travoprost ökar utflöde, timolol minskar produktion",
        "dosage": "1 droppe en gång dagligen på morgonen",
        "contraindications": [
            "astma/KOL",
            "bradykardi, hjärtblock"
        ],
        "side_effects": [
            "konjunktival hyperemi",
            "irispigmentering",
            "bronkospasm (timolol)",
            "bradykardi"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister"],
        "special_considerations": "IOP-sänkning 30-35%. En gång daglig dosering. Liknar Xalacom i effekt. Finns konserveringsmedelfri variant (DuoTrav PF) - BAK-fri.",
        "storage": "Rumstemperatur, använd inom 4 veckor",
        "atc_code": "S01ED51"
    },
    {
        "name": "Ganfort (Bimatoprost + Timolol)",
        "generic_name": "Bimatoprost 0.3 mg/ml + Timolol 5 mg/ml",
        "category": "Kombinationspreparat (prostaglandin + beta-blockerare)",
        "formulation": "Ögondroppar",
        "concentration": "Bimatoprost 0.03% + Timolol 0.5%",
        "indications": [
            "primär öppenvinklat glaukom",
            "okulär hypertension"
        ],
        "mechanism": "Bimatoprost ökar utflöde, timolol minskar produktion",
        "dosage": "1 droppe en gång dagligen på morgonen",
        "contraindications": [
            "astma/KOL",
            "bradykardi, hjärtblock"
        ],
        "side_effects": [
            "konjunktival hyperemi (mer än andra kombinationer)",
            "irispigmentering",
            "förlängda fransar",
            "bronkospasm",
            "bradykardi"
        ],
        "pregnancy_category": "C",
        "interactions": ["kalciumantagonister"],
        "special_considerations": "MEST effektiv kombination (IOP-sänkning upp till 35-40%). MER hyperemi än andra kombinationer. En gång daglig dosering.",
        "storage": "Rumstemperatur, använd inom 4 veckor",
        "atc_code": "S01ED51"
    }
]


def get_glaucoma_medications():
    """Return all glaucoma medications"""
    return GLAUCOMA_MEDICATIONS


def get_medication_by_name(name: str):
    """Get a specific medication by name"""
    name_lower = name.lower()
    for med in GLAUCOMA_MEDICATIONS:
        if (name_lower in med['name'].lower() or
            name_lower in med['generic_name'].lower()):
            return med
    return None


def get_medications_by_category(category: str):
    """Get medications by category"""
    return [m for m in GLAUCOMA_MEDICATIONS if category.lower() in m['category'].lower()]


if __name__ == "__main__":
    print(f"Loaded {len(GLAUCOMA_MEDICATIONS)} glaucoma medications")
    print("\nCategories:")
    categories = {}
    for med in GLAUCOMA_MEDICATIONS:
        cat = med['category']
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in categories.items():
        print(f"  {cat}: {count}")
