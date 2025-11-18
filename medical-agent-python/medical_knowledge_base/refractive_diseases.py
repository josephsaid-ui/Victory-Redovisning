"""
Refraktionsfel och Ackommodation - 15 vanligaste
"""

REFRACTIVE_DISEASES = [
    {
        "name": "Myopi (Närsynt)",
        "name_en": "Myopia",
        "icd10": "H52.1",
        "symptoms": [
            "suddig syn på avstånd",
            "kisande för att se bättre",
            "huvudvärk vid ansträngning",
            "svårigheter se tavlan i skolan",
            "god syn på nära håll",
            "bländning vid körning på natten"
        ],
        "anamnesis_questions": [
            "Har du svårt att se på avstånd?",
            "Behöver du sitta nära TV:n?",
            "Kisar du ofta?",
            "Försämras synen gradvis?",
            "Har du mycket myopi i familjen?",
            "Hur mycket läser/skärmar du?"
        ],
        "clinical_signs": [
            "minusstyrka vid refraktion",
            "längre axiallängd (>24mm vid hög myopi)",
            "vid hög myopi (>-6 D): lattice-degeneration, tunn retina perifert, myopisk makuladegeneration, förhöjd risk retinal avlossning",
            "fundus: tigroid/tessellated fundus, temporal crescent, posteriort stafylom vid patologisk myopi"
        ],
        "risk_factors": [
            "hereditet (starkaste faktorn)",
            "östasiatiskt ursprung (epidemi i Asien)",
            "mycket närsarbete (läsning, skärmar)",
            "begränsad utomhustid (barn)",
            "prematuritet",
            "progression vanligast under tillväxt"
        ],
        "treatment": "Korrektion: minusglas (konkava linser), kontaktlinser (mjuka, RGP, ortokeratologi - natt-linser), refraktiv kirurgi (LASIK, PRK) hos vuxna med stabil refraktion, Progressionshämning hos barn: atropindroppar 0.01% nattetid (bromsar progression 50%), ökad utomhustid (2h/dag minskar risk), defokus-linser/glasögon (Miyosmart, Stellest), ortokeratologi, Komplikationer vid hög myopi: screena för retinal avlossning, behandla myopisk CNV (anti-VEGF), behandla lattice-degeneration (profylaktisk laser)",
        "kva": "CKB00 (LASIK/PRK)",
        "differential_diagnoses": [
            "Pseudomyopi (ciliarspasm - reversibel med cykloplegia)",
            "Nukleär katarakt (myopiserande)",
            "Akut hyperglykemi (svullande lins)"
        ],
        "description": "Myopi är när ögat är för långt eller hornhinnan för krökt, och bilden fokuseras före retina. Epidemi i Asien (80-90% hos unga). Hög myopi (>-6 D) är patologisk med risk för retinal avlossning, myopisk CNV. Progressionshämning hos barn med atropin 0.01% och utomhustid.",
        "severity": "mild-moderate (severe vid patologisk myopi)",
        "urgency": "routine"
    },
    {
        "name": "Hyperopi (Översynt)",
        "name_en": "Hyperopia",
        "icd10": "H52.0",
        "symptoms": [
            "suddig syn på nära håll (värre med åldern)",
            "ansträngningshuvudvärk vid läsning",
            "svårigheter fokusera på nära",
            "trötta ögon efter läsning",
            "barn ofta asymtomatiska (ackommoderar)",
            "esotropi möjlig hos barn"
        ],
        "anamnesis_questions": [
            "Har du svårt att läsa eller se på nära håll?",
            "Får du huvudvärk vid läsning?",
            "Blir ögonen trötta?",
            "Har barnet skelat (esotropi)?",
            "Behöver du hålla boken längre bort?",
            "Förbättras det med plusglas?"
        ],
        "clinical_signs": [
            "plusstyrka vid refraktion",
            "kort axiallängd (<22mm)",
            "liten papill med liten cup (crowded disc)",
            "barn: latent hyperopi maskerad av ackommodation (kräver cykloplegia)",
            "ackommodativ esotropi hos barn möjlig",
            "risk för trångvinkelglaukom (grund främre kammare)"
        ],
        "risk_factors": [
            "hereditet",
            "kort axiallängd (kongenitalt kort öga)",
            "mikroftalmus",
            "nanoftalmus (mycket kort öga med tjock sklera)"
        ],
        "treatment": "Korrektion: plusglas (konvexa linser), kontaktlinser, refraktiv kirurgi (LASIK, PRK) möjlig men mindre vanligt än vid myopi, Barn med ackommodativ esotropi: plusglas FULLKORRIGERAR latent hyperopi (förhindrar skelning), cykloplegisk refraktion nödvändig hos barn, överväg bifokala glas om AC/A-ratio hög, Komplikationer: behandla trångvinkelglaukom-risk (profylaktisk laser iridotomi vid grund främre kammare)",
        "kva": "CKB00 (refraktiv kirurgi)",
        "differential_diagnoses": [
            "Presbyopi (åldersrelaterad, börjar ~40 år)",
            "Linsförflyttning posteriort (trauma)",
            "Afaki (saknar lins)"
        ],
        "description": "Hyperopi är när ögat är för kort eller hornhinnan för platt. Bilden fokuseras bakom retina. Barn ackommoderar och kan vara asymtomatiska. Vuxna får besvär vid läsning. Ackommodativ esotropi vanligt hos barn. Risk för trångvinkelglaukom. Korrektion med plusglas.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Astigmatism",
        "name_en": "Astigmatism",
        "icd10": "H52.2",
        "symptoms": [
            "suddig eller förvrängt syn på alla avstånd",
            "förvrängda linjer",
            "svårigheter läsa text",
            "huvudvärk och ögontrötthet",
            "kisande",
            "nattbländning vid körning"
        ],
        "anamnesis_questions": [
            "Ser linjer förvrängda ut?",
            "Är synen suddig på både avstånd och nära?",
            "Får du huvudvärk?",
            "Har du svårt att köra på natten?",
            "Lutar du huvudet för att se bättre?"
        ],
        "clinical_signs": [
            "cylinderstyrka vid refraktion",
            "olika brytning i olika meridianer",
            "hornhinneastigmatism (vanligast) eller linsastigmatism",
            "keratometri: olika kurvaturer",
            "topografi: asymmetrisk bow-tie pattern",
            "regulär (ortogonal) eller irreguliär astigmatism"
        ],
        "risk_factors": [
            "hereditet",
            "keratokonus",
            "hornhinnescarring",
            "pterygium",
            "chalazion (tryck på kornea)",
            "post-kataraktkirurgi",
            "post-keratoplasti"
        ],
        "treatment": "Korrektion: cylinderglas (toriska linser), toriska kontaktlinser (mjuka eller RGP), refraktiv kirurgi: LASIK, PRK (korrigerar astigmatism), toriska IOL vid kataraktkirurgi, limbal relaxing incisions (LRI) eller astigmatisk keratotomi (AK), behandla underliggande orsak: chalazion-excision, pterygium-kirurgi, RGP-linser kan maskera irreguliär astigmatism (keratokonus)",
        "kva": "CKB00 (LASIK/PRK)",
        "differential_diagnoses": [
            "Keratokonus (progressiv, irreguliär astigmatism)",
            "Pellucid marginal degeneration",
            "Post-kirurgisk astigmatism"
        ],
        "description": "Astigmatism är när kornea eller lins har olika brytning i olika meridianer. Ger suddig syn på alla avstånd. Regulär astigmatism korrigeras med cylinderglas. Irreguliär astigmatism (keratokonus) kräver RGP-linser. Toriska IOL vid kataraktkirurgi.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Presbyopi (Ålderssynt)",
        "name_en": "Presbyopia",
        "icd10": "H52.4",
        "symptoms": [
            "svårigheter läsa på nära håll (40-45 års ålder)",
            "behöver hålla boken längre bort",
            "behöver starkare ljus för läsning",
            "huvudvärk vid läsning",
            "suddig syn vid byte mellan avstånd och nära",
            "trötta ögon"
        ],
        "anamnesis_questions": [
            "Hur gammal är du? (oftast >40 år)",
            "Håller du boken längre bort för att läsa?",
            "Behöver du ta av glasögonen för att läsa? (om myop)",
            "Har du svårt att läsa menyer eller mobiltelefon?",
            "Har symptomen försämrats gradvis över några år?"
        ],
        "clinical_signs": [
            "nedsatt ackommodationsförmåga",
            "näradditionen behövs vid refraktion",
            "ackommodationsamplitud minskar med åldern: 40 år: ~6D, 50 år: ~2D, 60 år: ~1D",
            "push-up test visar minskad nära-punkt",
            "normala ögonbottnar",
            "alla får presbyopi (universell åldersförändring)"
        ],
        "risk_factors": [
            "ålder >40 år (oundvikligt!)",
            "hyperopi (märker tidigare)",
            "diabetes (tidigare debut)",
            "vissa mediciner (antihistamin, antidepressiva)",
            "varmare klimat (lite tidigare debut möjligen)"
        ],
        "treatment": "Korrektion - flera alternativ: läsglasögon (single vision), bifokala glas (två zoner), progressiva glas (multifokala), kontaktlinser: monovision (ett öga avstånd, ett nära), multifokala/bifokala kontaktlinser, Kirurgi: multifokala/EDOF IOL vid kataraktkirurgi, korneal inlays (kamra, presbia - mindre använda), laser presbyopilaser (PresbyLASIK - blandade resultat), linsbyte (refractive lens exchange) med multifokal IOL",
        "kva": "CJE00 (linsbyte med multifokal IOL)",
        "differential_diagnoses": [
            "Hyperopi (men finns hela livet)",
            "Ackommodativ insufficiens (yngre patient)",
            "Medicin-inducerad cyklopegi"
        ],
        "description": "Presbyopi är normal åldersförändring där linsen förlorar elasticitet och ackommodationsförmåga. Börjar ~40-45 år. Alla drabbas. Progressiva glas eller läsglasögon vanligaste korrektion. Multifokal IOL vid kataraktkirurgi. Universell åldersprocess.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Anisometropi",
        "name_en": "Anisometropia",
        "icd10": "H52.3",
        "symptoms": [
            "svårigheter med djupseende",
            "huvudvärk och ögontrötthet",
            "dubbelseende möjlig",
            "amblyopi risk hos barn (om okorrigerad)",
            "kan vara asymtomatisk om hjärnan supprimerar ena ögat"
        ],
        "anamnesis_questions": [
            "Har du mycket olika styrkor i glasögonen?",
            "Har du svårt med djupseende?",
            "Får du huvudvärk med glasögon?",
            "Har barnet amblyopi eller skelning?",
            "Tolererar du glasögonen dåligt?"
        ],
        "clinical_signs": [
            "skillnad ≥1.00-1.50 D mellan ögonen (definition varierar)",
            "kan vara sfärisk, cylindrisk eller axiallängd-skillnad",
            "amblyopi hos barn om okorrigerad",
            "eventuell mikrostrabismus",
            "bildstorleksskillnad (aniseikoni) vid stora skillnader"
        ],
        "risk_factors": [
            "hereditet",
            "unilateral katarakt hos barn",
            "unilateral retinal patologi",
            "post-traumatisk",
            "post-kirurgisk (LASIK på ett öga)"
        ],
        "treatment": "Barn: KORRIGERA FULLT för att förhindra amblyopi!, behandla amblyopi (lappning av bättre öga), kontaktlinser bättre än glasögon (mindre aniseikoni), Vuxna: glasögon om tolereras, kontaktlinser (minskar aniseikoni), refraktiv kirurgi (LASIK/PRK) på ena eller båda ögonen, monovision (ett öga avstånd, ett nära) vid presbyopi, IOL vid kataraktkirurgi (justera styrka för att minska anisometropi), vid intolerans: korrigera endast ett öga eller undervisa hjärnan att supprimera",
        "kva": "CKB00 (LASIK)",
        "differential_diagnoses": [
            "Unilateral katarakt",
            "Unilateral retinal patologi",
            "Fel glasögonrecept"
        ],
        "description": "Anisometropi är signifikant refraktionsskillnad mellan ögonen. Risk för amblyopi hos barn om okorrigerad. Vuxna kan ha besvär med djupseende och aniseikoni. Kontaktlinser minskar aniseikoni bättre än glasögon. Barn MÅSTE korrigeras fullt.",
        "severity": "mild-moderate (severe hos barn - amblyopi-risk)",
        "urgency": "urgent (barn), routine (vuxna)"
    },
    {
        "name": "Ackommodativ Insufficiens",
        "name_en": "Accommodative Insufficiency",
        "icd10": "H52.5",
        "symptoms": [
            "suddig syn på nära håll",
            "huvudvärk vid läsning",
            "trötta ögon",
            "svårigheter fokusera vid byte mellan avstånd och nära",
            "ofta yngre patienter (<40 år - före presbyopi)",
            "symptom värre sent på dagen"
        ],
        "anamnesis_questions": [
            "Hur gammal är du? (oftast <40 år)",
            "Har du svårt att läsa på nära håll?",
            "Får du huvudvärk vid läsning?",
            "Tar det tid att fokusera när du byter från avstånd till nära?",
            "Försämras det sent på dagen?",
            "Tar du mediciner? (antihistamin, etc.)"
        ],
        "clinical_signs": [
            "nedsatt ackommodationsamplitud för åldern",
            "push-up test: nära-punkt längre än förväntat",
            "förväntad amplitud (Hofstetter): 15 - 0.25 x ålder",
            "positiv relativt ackommodation (PRA) nedsatt",
            "normala ögonbottnar",
            "ingen organisk orsak"
        ],
        "risk_factors": [
            "långvarigt närsarbete",
            "mediciner (antikolinergika, antihistamin, antidepressiva)",
            "trauma",
            "encefalit/meningit (sällsynt)",
            "systemsjukdom (diabetes, myasthenia)",
            "stress/trötthet"
        ],
        "treatment": "Plusglas för närsarbete (läsaddition hos unga), synträning/ackommodationsträning (push-up övningar, flipper-övningar), behandla underliggande orsak (byt medicin om möjligt), pauser vid närsarbete (20-20-20 regel: var 20:e minut, titta 20 fot/6m bort i 20 sekunder), prognos: oftast god med träning eller plusglas",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Presbyopi (men >40 år)",
            "Farmakologisk cyklopegi (mediciner)",
            "Adie's pupill (med tonisk ackommodation)",
            "Latent hyperopi"
        ],
        "description": "Ackommodativ insufficiens är nedsatt ackommodationsförmåga hos yngre (<40 år) utan organisk orsak. Huvudvärk och suddig syn vid närsarbete. Push-up test diagnostiskt. Synträning eller plusglas för närsarbete. Uteslut mediciner som orsak.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Ackommodativ Spasm (Pseudomyopi)",
        "name_en": "Accommodative Spasm (Pseudomyopia)",
        "icd10": "H52.5",
        "symptoms": [
            "intermittent suddig syn på avstånd",
            "huvudvärk",
            "ögontrötthet",
            "variabel refraktion",
            "ofta unga patienter",
            "myopi som försvinner med cykloplegia"
        ],
        "anamnesis_questions": [
            "Varierar synen på avstånd?",
            "Har du haft plötslig myopi?",
            "Har du mycket stress eller ångest?",
            "Läser du mycket eller använder datorer mycket?",
            "Tar du mediciner? (pilokarpin, organiska fosfater)",
            "Har du huvudvärk?"
        ],
        "clinical_signs": [
            "myopi vid refraktion utan cykloplegia",
            "refraktion normaliseras med cykloplegia (diagnostiskt!)",
            "liten pupill (miosis) möjlig",
            "variabel refraktion vid upprepade mätningar",
            "kan ha esophoria",
            "normala ögonbottnar"
        ],
        "risk_factors": [
            "långvarigt närsarbete",
            "stress och ångest",
            "konversionstörning",
            "mediciner (miotika, organiska fosfater)",
            "efter ögontrauma",
            "post-operativt (efter strabismuskirurgi)"
        ],
        "treatment": "Cykloplegika (cyklopentolat, atropin) för att bryta spasm, behandla underliggande stress/ångest, minska närsarbete, plusglas tillfälligt under återhämtning, psykologisk bedömning vid konversionstörning, undvik onödig minus-korrektion (förvärrar!), prognos: oftast god med behandling av underliggande orsak",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Äkta progressiv myopi",
            "Farmakologisk miosis",
            "Funktionell synstörning"
        ],
        "description": "Ackommodativ spasm är kontinuerlig ciliarmuskelkontraktion som ger pseudomyopi. Variabel refraktion. Normaliseras med cykloplegia (diagnostiskt test!). Ofta stress-relaterad hos unga. Cykloplegika bryter spasm. Undvik minus-korrektion utan cykloplegia hos barn/unga!",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Konvergens Insufficiens",
        "name_en": "Convergence Insufficiency",
        "icd10": "H51.1",
        "symptoms": [
            "asthenopi (ögontrötthet vid läsning)",
            "diplopi vid läsning (intermittent)",
            "huvudvärk",
            "svårigheter koncentrera vid läsning",
            "måste stänga ett öga vid läsning",
            "ord 'hoppar' på sidan"
        ],
        "anamnesis_questions": [
            "Ser du dubbelt när du läser?",
            "Blir du trött i ögonen vid läsning?",
            "Måste du stänga ett öga för att läsa?",
            "Har du svårt att koncentrera dig vid läsning?",
            "Har du haft skalltrauma eller hjärnskakning?",
            "Försämras det vid trötthet?"
        ],
        "clinical_signs": [
            "fjärran nära-punkt (>10 cm - normalt <6 cm)",
            "nedsatt positiv fusional vergence vid nära",
            "exophoria större på nära än avstånd",
            "normal ackommodation (skiljer från ackommodativ insufficiens)",
            "normala ögonrörelser",
            "kan ha receded near point of convergence"
        ],
        "risk_faktorer": [
            "post-skalltrauma/hjärnskakning (vanligt!)",
            "Parkinson's sjukdom",
            "stroke",
            "myasthenia gravis",
            "ofta idiopatisk hos barn/unga",
            "långvarigt närsarbete kan förvärra"
        ],
        "treatment": "Konvergensträning (pencil push-ups, base-out prism övningar, dator-baserad synträning), effektivt hos 70-80%!, base-in prisma i läsglasögon (temporärt eller permanent), plusglas för närsarbete (minskar ackommodativ konvergens), läsglasögon med prisma, behandla underliggande orsak (post-concussion syndrom), prognos: mycket god med synträning",
        "kva": "Ingen",
        "differential_diagnoses": [
            "VI-nervpares (begränsad abduktion)",
            "Divergence insufficiency (dubbelseende på avstånd)",
            "Myasthenia gravis (variabel)"
        ],
        "description": "Konvergens insufficiens är oförmåga att konvergera ögonen tillräckligt vid närsarbete. Ger asthenopi och diplopi vid läsning. Fjärran nära-punkt diagnostiskt (>10 cm). Pencil push-ups mycket effektivt (70-80%). Vanligt post-hjärnskakning.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Ackommodativ Esotropi",
        "name_en": "Accommodative Esotropia",
        "icd10": "H50.0",
        "symptoms": [
            "inåtvridet öga (esotropi) vid fixation på nära",
            "debut 2-3 års ålder oftast",
            "kan vara konstant eller intermittent",
            "barnet kan knipa ena ögat i starkt ljus",
            "amblyopi-risk om obehandlad"
        ],
        "anamnesis_questions": [
            "Hur gammal är barnet? (oftast 2-3 år)",
            "Skelar barnet mer när det tittar på saker på nära håll?",
            "Kniper barnet ofta ena ögat?",
            "Finns hyperopi eller skelning i familjen?",
            "Har barnet blivit undersökt med ögondroppar tidigare?"
        ],
        "clinical_signs": [
            "esotropi som minskar eller försvinner med fullkorrektion av hyperopi",
            "måttlig till hög hyperopi (+2 till +7 D) vid cykloplegisk refraktion",
            "hög AC/A-ratio möjlig (ackommodativ konvergens/ackommodation)",
            "kan ha amblyopi om obehandlad",
            "normalt fundus"
        ],
        "risk_factors": [
            "hyperopi (framför allt måttlig till hög)",
            "hereditet",
            "hög AC/A-ratio",
            "ålder 2-3 år (när ackommodation utvecklas)"
        ],
        "treatment": "Fullkorrektion av hyperopi med glasögon (efter cykloplegisk refraktion) - ofta kurativt!, bifokala glas om hög AC/A-ratio (esotropi kvarstår på nära trots distans-korrektion), behandla amblyopi om present (lappning), miotika (pilokarpin) sällan använt numera, kirurgi endast om kvarstående esotropi trots optimal glaskorrektion, prognos: utmärkt med tidig fullkorrektion - skelningen försvinner!",
        "kva": "Eventuell strabismuskirurgi",
        "differential_diagnoses": [
            "Infantil esotropi (börjar <6 månader, stor vinkel)",
            "Partially accommodative esotropia (kräver glasögon + kirurgi)",
            "VI-nervpares (begränsad abduktion)"
        ],
        "description": "Ackommodativ esotropi är skelning orsakat av okorrigerad hyperopi. När barnet ackommoderar för att se klart triggas konvergens. Debut 2-3 år. Fullkorrektion av hyperopi med glasögon ofta kurativt! Cykloplegisk refraktion nödvändig. Bifokala om hög AC/A-ratio.",
        "severity": "moderate",
        "urgency": "urgent (förhindra amblyopi)"
    },
    {
        "name": "Aniseikonii",
        "name_en": "Aniseikonia",
        "icd10": "H53.3",
        "symptoms": [
            "bilder är olika stora i de två ögonen",
            "svårigheter med djupseende och spatial orientation",
            "ögontrötthet och huvudvärk",
            "illamående möjlig",
            "svårigheter anpassa till glasögon",
            "asthenopi"
        ],
        "anamnesis_questions": [
            "Verkar saker olika stora med olika ögon?",
            "Har du svårt att tolerera nya glasögon?",
            "Har du anisometropi (olika styrkor)?",
            "Har du opererats för grå starr i ett öga?",
            "Får du huvudvärk med glasögon?",
            "Har du svårt med djupseende?"
        ],
        "clinical_signs": [
            "bildstorleksskillnad mellan ögonen (>5% kliniskt signifikant)",
            "orsaker: anisometropi (olika refraktion), olika IOL-styrkor post-katarakt, retinal patologi (epiretinal membran), Eikonometer kan mäta exakt bildstorleksskillnad",
            "oftast sekundärt till anisometropi eller olika IOL"
        ],
        "risk_factors": [
            "signifikant anisometropi (>2-3 D)",
            "post-kataraktkirurgi med olika IOL-styrkor",
            "unilateral afaki",
            "epiretinal membran (retinal orsak)",
            "unilateral LASIK/refraktiv kirurgi"
        ],
        "treatment": "Kontaktlinser (minskar aniseikonii signifikant jämfört med glasögon), refraktiv kirurgi för att minska anisometropi, size lenses (iseikonic lenses) - specialdesignade glasögon, vid post-katarakt: IOL-byte om intolerabelt, vid retinal orsak (ERM): vitrektomi med membranplockning, monovision som lösning (ena ögat för avstånd, andra för nära), vissa lär sig tolerera med tiden",
        "kva": "CJE00 (IOL-byte), CJE20 (vitrektomi)",
        "differential_diagnoses": [
            "Metamorfopsi (förvrängning från retinal patologi)",
            "Vertikal strabismus (ger höjdskillnad, inte storleksskillnad)"
        ],
        "description": "Aniseikonii är när bilder är olika stora i de två ögonen, oftast från anisometropi eller olika IOL. >5% skillnad ger symptom. Kontaktlinser minskar aniseikonii bättre än glasögon. Iseikonic lenses kan hjälpa. Vissa tolererar med tiden.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Sykloplegi (Ackommodationspares)",
        "name_en": "Cycloplegia (Paralysis of Accommodation)",
        "icd10": "H52.5",
        "symptoms": [
            "suddig syn på nära håll",
            "ljuskänslighet (om pupillen dilaterad)",
            "oförmåga att fokusera på nära",
            "kan vara efter ögondroppar (iatrogenisk) eller neurologisk skada"
        ],
        "anamnesis_questions": [
            "Har du fått ögondroppar nyligen?",
            "Har du haft ögontrauma?",
            "Har du neurologiska symptom?",
            "Tar du mediciner? (antikolinergika)",
            "Har pupillen varit stor?",
            "Är det bilateral eller unilateral?"
        ],
        "clinical_signs": [
            "ingen ackommodationsrespons",
            "dilaterad pupill ofta (om mydriasis samtidigt)",
            "push-up test: ingen ackommodation",
            "bilateral: farmakologisk, neurologisk",
            "unilateral: Adie's pupill, lokal skada",
            "synnerv och retina normala"
        ],
        "risk_factors": [
            "farmakologisk: atropin, cyklopentolat, scopolamin, antikolinergika systemiskt",
            "neurologisk: Adie's syndrom, encefalit, botulism",
            "trauma: direkt ögontrauma, orbitaltrauma",
            "bilateral: farmakologiskt vanligast"
        ],
        "treatment": "Farmakologisk: upphör med medel, vänta ut (atropin 1-2 veckor, cyklopentolat 24h, tropikamid 6h), plusglas för närsarbete temporärt, Neurologisk orsak: behandla underliggande (Adie's: pilokarpin 0.125% kan hjälpa något), permanent cyklopegi: läsglasögon/bifokala",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Presbyopi (men åldersrelaterad, gradvis)",
            "Ackommodativ insufficiens (partiell nedsättning)",
            "III-nervpares (oftalmoplegi samtidigt)"
        ],
        "description": "Cyklopegi är ackommodationspares. Vanligaste orsaken är iatrogen (ögondroppar). Adie's pupill ger cyklopegi unilateralt. Behandling beroende på orsak - farmakologisk upphör spontant. Plusglas för närsarbete under tiden.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Induced Myopi (Läkemedels/Sjukdomsinducerad)",
        "name_en": "Drug-Induced or Disease-Induced Myopia",
        "icd10": "H52.1",
        "symptoms": [
            "plötslig myopi (timmar-dagar)",
            "suddig syn på avstånd",
            "ofta bilateral",
            "kan ha samtidig trångvinkel (vid ciliary body ödem)"
        ],
        "anamnesis_questions": [
            "Började närsynten plötsligt?",
            "Tar du nya mediciner? (topiramtat, sulfonamider, SSRI)",
            "Har du diabetes med dålig kontroll?",
            "Har du högt blodsocker nyligen?",
            "Har symptomen kommit efter start av medicin?"
        ],
        "clinical_signs": [
            "myopi vid refraktion (kan vara -2 till -10D)",
            "grund främre kammare möjlig (vid ciliary body ödem)",
            "linsen kan vara svullen (hyperglykemi)",
            "normaliseras när medicin/orsak upphör",
            "uveal effusion möjlig (topiramat)"
        ],
        "risk_factors": [
            "mediciner: topiramat (Topimax), sulfonamider, acetazolamid, SSRI, tetracyklin, hydralazin",
            "hyperglykemi vid diabetes (osmotisk linssvullnad)",
            "graviditet (hormonella förändringar)",
            "ciliary body ödem (idiopatisk eller medicin-inducerad)"
        ],
        "treatment": "Avsluta utlösande medicin (konsultera förskrivande läkare), kontrollera blodsocker vid diabetes, cykloplegika vid ciliary body spasm, steroider vid inflammation, symtomatisk korrektion temporärt (minusglas), vänta 2-4 veckor efter avslutad medicin innan permanent glaskorrektion, vid topiramat: avsluta AKUT om trångvinkel utvecklas",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Progressiv myopi (gradvis)",
            "Nukleär katarakt (myopiserande)",
            "Akut trångvinkelglaukom (smärta, rodnad)"
        ],
        "description": "Inducerad myopi uppstår plötsligt från mediciner (topiramat, sulfonamider) eller hyperglykemi. Bilateral plötslig myopi. Kan ge samtidig trångvinkel (topiramat). Avsluta medicin - reversibelt inom veckor. Viktigt att känna till - undvik permanent korrektion innan orsak behandlad!",
        "severity": "mild-moderate (severe om trångvinkel)",
        "urgency": "urgent (om trångvinkel), routine (annars)"
    },
    {
        "name": "Post-Refraktiv Kirurgi Komplikationer",
        "name_en": "Post-Refractive Surgery Complications",
        "icd10": "H59.0",
        "symptoms": [
            "torrt öga (mycket vanligt)",
            "bländning och halos (nattköming)",
            "nedsatt kontrastkänslighet",
            "regression av korrektion",
            "ektasi (corneal förtunning - allvarligt)",
            "irregulär astigmatism"
        ],
        "anamnesis_questions": [
            "Har du opererats med LASIK eller PRK?",
            "Känner dina ögon torra?",
            "Har du bländning vid nattköring?",
            "Har synen försämrats efter operationen?",
            "Ser du halos runt lampor?",
            "När opererades du?"
        ],
        "clinical_signs": [
            "torrt öga: nedsatt TBUT, korneal färgning",
            "irregulär astigmatism: topografi-avvikelser",
            "ektasi: progressiv korneal steepening, keratokonus-liknande",
            "decentrerad ablation: asymmetrisk topografi",
            "flap-komplikationer (LASIK): striae, epitelial ingrowth, DLK",
            "haze (PRK): subepiteliala opacitet"
        ],
        "risk_factors": [
            "pre-operativ torrt öga",
            "hög korrektion (>-6D)",
            "tunn kornea preoperativt",
            "forme fruste keratokonus (ej diagnosticerad)",
            "stor pupill (ger bländning/halos)",
            "ögongnuggning postoperativt"
        ],
        "treatment": "Torrt öga: intensiv lubricering, punktal plugs, Omega-3, cyklosporin, Bländning/halos: ofta förbättras över tid (6-12 mån), dilaterade pupiller kan hjälpa, brimonidintroppar minskar pupillstorlek, Regression: förstärkningsbehandling (enhancement) om stabil, Ektasi: RGP-linser, cross-linking, eventuellt korneatransplantation, DLK (diffus lamellar keratit): intensiva steroider, Epithelial ingrowth: lyfta flap och scrape, Haze (PRK): steroider, MMC vid svår",
        "kva": "Varierar (enhancement, cross-linking, keratoplasti)",
        "differential_diagnoses": [
            "Torrt öga av annan orsak",
            "Keratokonus (vs post-LASIK ektasi)",
            "Residual refraktionsfel"
        ],
        "description": "Post-LASIK/PRK komplikationer inkluderar torrt öga (vanligast), bländning, ektasi (allvarligast). Torrt öga behandlas med lubricering. Ektasi kräver cross-linking. Viktigt med pre-operativ screening (topografi, pachymetri). Bländning ofta self-limited.",
        "severity": "mild-moderate (severe vid ektasi)",
        "urgency": "routine (emergency vid ektasi)"
    },
    {
        "name": "Amblyopi (Latsöga)",
        "name_en": "Amblyopia",
        "icd10": "H53.0",
        "symptoms": [
            "nedsatt syn i ett öga trots korrektion",
            "barn ofta asymtomatiskt (upptäcks vid screening)",
            "dåligt djupseende",
            "lutar huvudet eller täcker ett öga",
            "föredrar ett öga"
        ],
        "anamnesis_questions": [
            "Hur gammal är barnet? (behandling bäst <7 år)",
            "Har barnet skelat?",
            "Har barnet haft grå starr eller ögonsjukdom?",
            "Finns mycket olika styrkor i glasögonen?",
            "Täcker barnet ett öga?",
            "Har någon märkt att barnet favoriserar ett öga?"
        ],
        "clinical_signs": [
            "nedsatt syn (synskärpa) i ett öga utan organisk orsak",
            "förbättras EJ med glasögon-korrektion",
            "kan ha strabismus (skelning) - 50%",
            "eller anisometropi (olika refraktion) - 40%",
            "eller deprivation (katarakt, ptosis) - 10%",
            "normalt fundus (uteslut organisk orsak!)",
            "fixationspreferens för bättre öga"
        ],
        "risk_factors": [
            "strabismus (skelning)",
            "anisometropi (>1.5-2D skillnad)",
            "deprivation (kongenital katarakt, ptosis)",
            "hög bilateral refraktionsfel (okorrigerad)",
            "prematuritet",
            "hereditet"
        ],
        "treatment": "Korrigera underliggande orsak: glasögon för refraktionsfel/anisometropi, kataraktkirurgi vid deprivation, strabismuskirurgi efter amblyopi-behandling, Amblyopi-behandling: lappning av bättre öga (2-6 timmar dagligen), atropin-penalisering av bättre öga (alternativ till lappning), kombinationsbehandling, Compliance kritiskt!, Treatment efficacy bäst <7 år men kan hjälpa till tonår, Uppföljning tätt - risk för reverse amblyopia vid överlappning, Prognos: utmärkt om tidig diagnos och behandling (<7 år)",
        "kva": "Eventuell strabismuskirurgi",
        "differential_diagnoses": [
            "Organisk synnedsättning (retinal, optisk neuropati)",
            "Funktionell synförlust",
            "Okorrigerad refraktionsfel"
        ],
        "description": "Amblyopi är nedsatt syn i ett öga utan organisk orsak, från strabismus, anisometropi eller deprivation i kritisk period (<7 år). Behandling: korrigera orsak + lappning av bättre öga. Bäst prognos <7 år. Screening viktigt! 'Use it or lose it' - hjärnan supprimerar dåliga ögat.",
        "severity": "moderate",
        "urgency": "urgent (barn <7 år)"
    },
    {
        "name": "Högre Ordens Aberrationer",
        "name_en": "Higher-Order Aberrations",
        "icd10": "H52.7",
        "symptoms": [
            "bländning och halos runt ljus",
            "nedsatt kontrastkänslighet",
            "natt-syn problem",
            "symptom trots korrekt refraktion",
            "'ghost images' eller diplopi monokulär",
            "ofta värre i mörker (stor pupill)"
        ],
        "anamnesis_questions": [
            "Har du bländning eller halos?",
            "Är det värre på natten?",
            "Har du opererats med LASIK?",
            "Har du keratokonus?",
            "Ser du flera bilder med ett öga?",
            "Är synen suddig trots rätt glasögon?"
        ],
        "clinical_signs": [
            "ökade högre ordens aberrationer på wavefront-analys",
            "vanliga typer: coma, trefoil, sfärisk aberration",
            "normala lågre ordens (sfärisk, cylindrisk) kan vara korrigerade",
            "orsaker: post-LASIK, keratokonus, korneal scarring, stora pupiller",
            "topografi visar irregulariteter"
        ],
        "risk_factors": [
            "post-refraktiv kirurgi (LASIK, PRK)",
            "keratokonus",
            "hornhinnescarring",
            "stora pupiller (>6mm)",
            "post-keratoplastik",
            "pellucid marginal degeneration"
        ],
        "treatment": "RGP-linser (maskerar irregulära aberrationer), scleral linser, wavefront-guided LASIK enhancement (vid post-LASIK), pupill-konstrigerande droppar (brimonid) för nattbländning, behandla underliggande (cross-linking vid keratokonus), specialdesignade kontaktlinser för aberration-korrektion, penetrerande keratoplastik vid svår irregularitet, vissa aberrationer kan ej korrigeras helt",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Torrt öga (variabel syn)",
            "Posterior subkapsulär katarakt (bländning)",
            "Korneal ödem"
        ],
        "description": "Högre ordens aberrationer är optiska imperfektioner bortom sfärisk/cylindrisk fel. Ger bländning, halos, nedsatt kontrastkänslighet. Vanligt post-LASIK och vid keratokonus. Wavefront-analys diagnostiskt. RGP/scleral linser bästa behandling. Värre med stora pupiller.",
        "severity": "mild-moderate",
        "urgency": "routine"
    }
]
