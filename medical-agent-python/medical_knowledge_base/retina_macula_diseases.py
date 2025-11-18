"""
Retina och Macula Sjukdomar - 40 vanligaste
"""

RETINA_MACULA_DISEASES = [
    {
        "name": "Diabetesretinopati - Icke-proliferativ (NPDR)",
        "name_en": "Non-Proliferative Diabetic Retinopathy",
        "icd10": "H36.0",
        "symptoms": [
            "ofta asymtomatisk i tidiga stadier",
            "gradvis synnedsättning",
            "suddig syn",
            "svårigheter att läsa",
            "förvrängd syn vid maculaödem"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft diabetes?",
            "Vilken typ av diabetes har du (typ 1 eller typ 2)?",
            "Vilket HbA1c har du haft senaste året?",
            "Hur är din blodtryckskontroll?",
            "Har du njurpåverkan?",
            "När gjordes senaste ögonbottenfotografering?",
            "Märker du någon förändring i synskärpan?"
        ],
        "clinical_signs": [
            "mikroaneurysm",
            "retinala blödningar (dot, blot)",
            "hårda exudat",
            "mjuka exudat (cotton-wool spots)",
            "retinalt ödem",
            "maculaödem",
            "vendilatation",
            "IRMA (intraretinal microvascular abnormalities)"
        ],
        "risk_factors": [
            "lång diabetesduration (>10 år)",
            "dålig glykemisk kontroll (HbA1c >8%)",
            "hypertoni",
            "hyperlipidemi",
            "njursvikt",
            "graviditet",
            "pubertet"
        ],
        "treatment": "Optimal metabol kontroll (HbA1c <7%), blodtryckskontroll, kontroller var 6-12 mån beroende på svårighetsgrad, laser vid kliniskt signifikant maculaödem, anti-VEGF vid centralt involverat maculaödem",
        "kva": "CJD96",  # Laserkoagulation av retina
        "differential_diagnoses": [
            "Hypertensiv retinopati",
            "Venockklusion med maculaödem",
            "Strålningsretinopati"
        ],
        "description": "NPDR är ett tidigt stadium av diabetesretinopati där retinala kärl skadas av långvarig hyperglykemi. Karakteriseras av mikrovaskulära förändringar utan neovaskulära proliferationer.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Diabetesretinopati - Proliferativ (PDR)",
        "name_en": "Proliferative Diabetic Retinopathy",
        "icd10": "H36.0",
        "symptoms": [
            "plötslig synnedsättning",
            "flimmer eller blixtar",
            "svarta fläckar eller spindelnät",
            "glaskroppsblödning",
            "synfältsbortfall",
            "total synförlust möjlig"
        ],
        "anamnesis_questions": [
            "Har du fått plötslig synförsämring?",
            "Ser du svarta fläckar eller ett 'skynke' i synfältet?",
            "Har du haft tidigare laserbehandling?",
            "Har du gjort tidigare vitrektomi?",
            "Vilken är din nuvarande synskärpa?"
        ],
        "clinical_signs": [
            "neovaskulationer på papillen (NVD)",
            "neovaskulationer på retina (NVE)",
            "glaskroppsblödning",
            "preretinal blödning",
            "fibrovaskulära proliferationer",
            "traktionsavlossning",
            "rubeosis iridis",
            "neovaskulärt glaukom"
        ],
        "risk_factors": [
            "långvarig diabetes (>15 år)",
            "mycket dålig metabol kontroll",
            "graviditet",
            "kataraktkirurgi utan preoperativ screening",
            "tidigare NPDR som ej följts"
        ],
        "treatment": "Akut: panretinal laserkoagulation (PRP) eller anti-VEGF, vitrektomi vid glaskroppsblödning/traktionsavlossning, anti-VEGF (Aflibercept, Ranibizumab) som alternativ eller komplement till laser",
        "kva": "CJD96",
        "differential_diagnoses": [
            "Venockklusion med neovaskulationer",
            "Sicklecellretinopati",
            "Strålingretinopati",
            "Ocular ischemic syndrome"
        ],
        "description": "PDR är ett avancerat stadium med retinal ischemi som leder till neovaskulationer. Risk för allvarliga komplikationer som glaskroppsblödning och traktionsavlossning.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Åldersrelaterad Makuladegeneration - Torr (AMD)",
        "name_en": "Dry Age-Related Macular Degeneration",
        "icd10": "H35.3",
        "symptoms": [
            "gradvis central synnedsättning",
            "svårigheter att läsa",
            "behov av starkare ljus",
            "suddig syn centralt",
            "förvrängda linjer (metamorfopsi)",
            "nedsatt kontrastkänslighet",
            "svårigheter känna igen ansikten"
        ],
        "anamnesis_questions": [
            "Hur gammal är du?",
            "Röker du eller har du rökt?",
            "Har någon i familjen haft makuladegeneration?",
            "Märker du att linjer ser böjda ut?",
            "Har du svårt att läsa trots rätt glasögon?",
            "Ser du en suddig fläck centralt?",
            "Använder du Amsler-rutnät hemma?"
        ],
        "clinical_signs": [
            "drusen (små, mellanstora, stora)",
            "pigmentförändringar i makula",
            "geografisk atrofi",
            "förtunning av RPE (retinalt pigmentepitel)",
            "nedsatt fundusautofluorescens vid atrofi"
        ],
        "risk_factors": [
            "hög ålder (>60 år)",
            "rökning (största påverkbara faktorn)",
            "hereditet",
            "ljus hudpigmentering",
            "kardiovaskulär sjukdom",
            "högt BMI",
            "högt intag av mättat fett"
        ],
        "treatment": "AREDS2-vitaminer (vitamin C, E, zink, koppar, lutein, zeaxantin) vid intermediär AMD eller avancerad AMD i ett öga, rökstopp (viktigt!), synrehabilitering, förstoringshjälpmedel, regelbundna kontroller, Amsler-rutnät hemmonitorering",
        "kva": "Ingen specifik",
        "differential_diagnoses": [
            "Mönsterdystrofi",
            "Central serös korioretinopati",
            "Makulärt hål",
            "Toxisk makulopati (Plaquenil)"
        ],
        "description": "Torr AMD är den vanligaste formen (85-90%) med gradvis degeneration av makula, RPE och korioidea. Progression till geografisk atrofi kan ske.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Åldersrelaterad Makuladegeneration - Våt (neovaskulär AMD)",
        "name_en": "Wet (Neovascular) Age-Related Macular Degeneration",
        "icd10": "H35.3",
        "symptoms": [
            "akut eller snabb central synnedsättning",
            "kraftig metamorfopsi (förvrängda linjer)",
            "central skotom",
            "minskat färgseende",
            "positiv Amsler-rutnät"
        ],
        "anamnesis_questions": [
            "När började synförsämringen?",
            "Ser linjer böjda eller vågiga ut?",
            "Ser du en mörk fläck centralt?",
            "Har du torr AMD i det andra ögat?",
            "Har du fått anti-VEGF-behandling tidigare?"
        ],
        "clinical_signs": [
            "subretinal vätska",
            "intraretinal vätska",
            "subretinal blödning",
            "RPE-avlossning",
            "CNV (choroidal neovascularization) på OCT/angiografi",
            "hårda exudat",
            "subretinal fibros"
        ],
        "risk_factors": [
            "torr AMD i samma eller andra ögat",
            "stor drusen",
            "pigmentepitelavlossning",
            "alla riskfaktorer för torr AMD"
        ],
        "treatment": "Intravitreal anti-VEGF (Aflibercept 8 mg varannan-tredje månad, Ranibizumab, Brolucizumab), treat-and-extend eller PRN-regim, OCT-monitorering, fortsatta kontroller livslångt",
        "kva": "CJE10",  # Intravitreal injektion
        "differential_diagnoses": [
            "Polypoidal koroidal vaskulopati (PCV)",
            "Myopisk CNV",
            "Central serös korioretinopati",
            "Makulärt hål med vätska"
        ],
        "description": "Våt AMD utgör 10-15% av AMD men står för majoriteten av svår synnedsättning. Koroidal neovaskulisation leder till vätskeansamling och blödning under makula.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Retinal Avlossning - Rhegmatogen",
        "name_en": "Rhegmatogenous Retinal Detachment",
        "icd10": "H33.0",
        "symptoms": [
            "plötsliga ljusblixtar (fotopsier)",
            "kraftigt ökad mängd flygers",
            "skynkeliknande synfältsbortfall",
            "vattenvågsliknande syn",
            "central synnedsättning (om makula avlossnad)"
        ],
        "anamnesis_questions": [
            "När började symptomen?",
            "Såg du först blixtar och flygers?",
            "Ser du ett skynke eller gardin över synfältet?",
            "Är det värre på morgonen?",
            "Har du varit med om ögontrauma?",
            "Är du myop (närsynt)?",
            "Har du haft avlossning i andra ögat?"
        ],
        "clinical_signs": [
            "grå, veckad, löst rörlig retina",
            "ett eller flera retinala hål/rifter",
            "tobaksöksskott",
            "subretinal vätska",
            "Shafer's tecken (pigment i glaskroppen)",
            "relativ afferent pupilldefekt vid större avlossning",
            "förhöjt ögontryck möjligt (Schwartz syndrom)"
        ],
        "risk_factors": [
            "hög myopi",
            "lattice-degeneration",
            "ögontrauma",
            "tidigare kataraktkirurgi",
            "tidigare avlossning i andra ögat (10% risk)",
            "familjehistoria",
            "PVD (posterior vitreous detachment)"
        ],
        "treatment": "Akut remiss till vitreoretinal kirurg, pneumatisk retinopex i (intravitreal gasbubbla) vid små, välbelägna hål, skleral buckle vid lokaliserade hål, pars plana vitrektomi med eller utan buckle, endolaser/kryopexi, gasbubbla (SF6, C3F8) eller silikonomja, specifik positionering postoperativt",
        "kva": "CJE20",  # Vitrektomi
        "differential_diagnoses": [
            "Traktionsavlossning",
            "Exsudativ avlossning",
            "Retinoschisis",
            "Koroidal avlossning"
        ],
        "description": "Rhegmatogen avlossning uppstår när retinalt hål/rift tillåter glaskroppsvätska att tränga under retina. Kirurgisk akutsjukdom med risk för permanent synförlust.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Central Retinal Venockklusion (CRVO)",
        "name_en": "Central Retinal Vein Occlusion",
        "icd10": "H34.8",
        "symptoms": [
            "plötslig, smärtfri synnedsättning",
            "suddig syn",
            "synnedsättningen varierar (lätt till svår)",
            "eventuellt synfältsbortfall"
        ],
        "anamnesis_questions": [
            "När märkte du synförsämringen?",
            "Var det plötsligt eller gradvist?",
            "Har du högt blodtryck?",
            "Har du glaukom eller högt ögontryck?",
            "Har du diabetes?",
            "Tar du blodförtunnande medicin?",
            "Har du haft blodpropp tidigare?"
        ],
        "clinical_signs": [
            "utbredda retinala blödningar i alla kvadranter",
            "venkaliber ökad och slingrande",
            "cotton-wool spots",
            "maculaödem",
            "papillödem",
            "neovaskulationer (i 20% efter 3-4 mån)",
            "rubeosis iridis",
            "neovaskulärt glaukom (svår komplikation)"
        ],
        "risk_factors": [
            "hypertoni (viktigaste)",
            "glaukom/okulär hypertension",
            "diabetes",
            "högt BMI",
            "hög ålder",
            "hyperkoagulabilitet",
            "ateroskleros"
        ],
        "treatment": "Anti-VEGF vid maculaödem (Aflibercept, Ranibizumab), kontroll av systemiska riskfaktorer, månadsvis uppföljning första 6 mån (risk för neovaskulationer), panretinal laser vid neovaskulationer/rubeosis",
        "kva": "CJE10",
        "differential_diagnoses": [
            "Hypertensiv retinopati",
            "Ocular ischemic syndrome",
            "Diabetesretinopati med blödningar",
            "Venösa stasis retinopati"
        ],
        "description": "CRVO uppstår vid ocklusion av centralvenen, ofta vid lamina cribrosa. Kan vara icke-ischemisk (bättre prognos) eller ischemisk (sämre prognos, risk för neovaskulationer).",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Grenretinal Venockklusion (BRVO)",
        "name_en": "Branch Retinal Vein Occlusion",
        "icd10": "H34.8",
        "symptoms": [
            "plötslig, smärtfri synnedsättning i del av synfältet",
            "suddig syn",
            "varierar beroende på lokalisation",
            "kan vara asymtomatisk om perifert"
        ],
        "anamnesis_questions": [
            "Märkte du plötslig synförändring?",
            "Ser du suddig i en viss del av synfältet?",
            "Har du högt blodtryck?",
            "Har du diabetes?",
            "Har du högt ögontryck?"
        ],
        "clinical_signs": [
            "retinala blödningar i en sektor/gren",
            "vendilatation uppströms ocklusion",
            "cotton-wool spots",
            "maculaödem (om makula involverad)",
            "arteriovenös korsning ofta vid ocklusionsställe",
            "eventuella neovaskulationer"
        ],
        "risk_factors": [
            "hypertoni",
            "diabetes",
            "glaukom",
            "hög ålder",
            "hyperkoagulabilitet",
            "ateroskleros"
        ],
        "treatment": "Anti-VEGF vid maculaödem, grenlaser vid ischemiska områden med risk för neovaskulationer, kontroll av systemiska faktorer, uppföljning 4-6 månader",
        "kva": "CJE10",
        "differential_diagnoses": [
            "CRVO",
            "Retinal artärocklusion (ger annan bild)",
            "Diabetesretinopati",
            "Lokaliserad retinal blödning av annan orsak"
        ],
        "description": "BRVO uppstår vid ocklusion av en retinal vengren, vanligtvis vid en arteriovenös korsning. Bättre prognos än CRVO om makula ej involverad.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Central Retinal Artärocklusion (CRAO)",
        "name_en": "Central Retinal Artery Occlusion",
        "icd10": "H34.1",
        "symptoms": [
            "plötslig, svår synförlust (ljusperception-fingerkänning)",
            "smärtfri",
            "eventuell amaurosis fugax (TIA) tidigare",
            "mycket dålig prognos för synåterhämtning"
        ],
        "anamnesis_questions": [
            "Exakt när inträffade synförlusten? (tidsfönster kritiskt!)",
            "Har du haft övergående synförlust tidigare?",
            "Har du kärlkramp eller hjärtinfarkt?",
            "Har du förmaksflimmer?",
            "Har du diabetes?",
            "Har du jättecellsarterit-symptom (huvudvärk, käkklaudikation)?"
        ],
        "clinical_signs": [
            "cherry-red spot i fovea",
            "mjölkvit, ödematos retina",
            "attenuerade artärer",
            "box-carring i artärer (segmenterat blodflöde)",
            "eventuell embolus synlig",
            "relativ afferent pupilldefekt (RAPD)",
            "eventuellt cilioretinal artär sparad (25%)"
        ],
        "risk_factors": [
            "högt blodtryck",
            "diabetes",
            "förmaksflimmer",
            "karotisstenosrök",
            "jättecellsarterit (över 60 år!)",
            "hyperkoagulabilitet",
            "hjärtklaffsjukdom"
        ],
        "treatment": "AKUT! (inom 24h, helst <4h): okulär massage, anterior chamber paracentesis (sänka IOT), hyperbar syrebehandling (om tillgänglig inom 24h), utred embolikälla (karotis duplex, ekokardiografi, EKG), kontrollera SR/CRP akut (GCA!), ASA + Clopidogrel profylax, behandla underliggande orsak",
        "kva": "Ingen specifik åtgärd (medicinskt akut omhändertagande)",
        "differential_diagnoses": [
            "Ophthalmica artärocklusion",
            "Optikusneurit med svår synnedsättning",
            "Posterior ischemisk optikusneuropati",
            "Kompressionsneuropati"
        ],
        "description": "CRAO är en oftalmologisk nödsituation orsakad av embolus eller trombos i centralartären. 'Ögats stroke' med mycket dålig prognos. Uteslut alltid GCA hos äldre!",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Grenretinal Artärocklusion (BRAO)",
        "name_en": "Branch Retinal Artery Occlusion",
        "icd10": "H34.2",
        "symptoms": [
            "plötslig synfältsbortfall i sektor",
            "altitudinalt defekt möjligt",
            "smärtfri",
            "bättre prognos än CRAO om makula ej berörd"
        ],
        "anamnesis_questions": [
            "När inträffade synfältsbortfallet?",
            "Har du haft TIA-symptom?",
            "Har du förmaksflimmer eller hjärtklaffsjukdom?",
            "Har du kärlsjukdomar?"
        ],
        "clinical_signs": [
            "mjölkvit retina i berörd sektor",
            "embolus ofta synlig i artärgren",
            "ättenuerad artär",
            "normalt utseende i ej berörda sektorer",
            "eventuell cotton-wool spot"
        ],
        "risk_factors": [
            "förmaksflimmer",
            "karotisstenosrök",
            "diabetes",
            "hjärtklaffsjukdom",
            "endokardit"
        ],
        "treatment": "Utred embolikälla (karotis duplex, EKG, ekokardiografi), ASA/Clopidogrel, behandla underliggande orsak, kontroll SR/CRP (GCA hos äldre)",
        "kva": "Ingen specifik",
        "differential_diagnoses": [
            "CRAO",
            "Posterior ischemisk optikusneuropati",
            "Retinal embolisering av annat skäl"
        ],
        "description": "BRAO ger sektoriellt synfältsbortfall. Bättre prognos än CRAO men kräver samma utredning för att förhindra framtida stroke/MI.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Epiretinal Membran (Makulaförband)",
        "name_en": "Epiretinal Membrane",
        "icd10": "H35.3",
        "symptoms": [
            "gradvis synnedsättning",
            "metamorfopsi (förvrängda linjer)",
            "diplopi monokulär",
            "svårigheter läsa",
            "ofta asymtomatisk i tidiga stadier"
        ],
        "anamnesis_questions": [
            "Ser linjer böjda eller vågiga ut?",
            "Ser du dubbelt med ett öga?",
            "Har du haft retinal avlossning eller ögonkirurgi?",
            "Har du diabetes eller uveit?",
            "Märker du gradvis försämring?"
        ],
        "clinical_signs": [
            "glansande membran över makula",
            "retinal veckbildning/striae",
            "vaskulär distorsion/tortuositet",
            "pseudo-makulärt hål (på OCT)",
            "förtjockad fovea på OCT",
            "eventuell minskning av foveal depressio"
        ],
        "risk_factors": [
            "hög ålder (>60 år)",
            "PVD (posterior vitreous detachment)",
            "tidigare retinal avlossning",
            "retinal laserbehandling",
            "diabetesretinopati",
            "uveit",
            "ögontrauma"
        ],
        "treatment": "Observation om asymtomatisk eller mild, vitrektomi med membranplockning om signifikant symptom (syn <0.5, besvärande metamorfopsi), god prognos vid kirurgi (80% förbättras)",
        "kva": "CJE20",
        "differential_diagnoses": [
            "Makulärt hål",
            "Vitreomakulär traktion",
            "Maculaödem av annan orsak",
            "Makulär pucker vs. fibros"
        ],
        "description": "Epiretinal membran är en tunn vävnad av gliaceller på retinal inneryta. Vanligen idiopatisk hos äldre, kan också vara sekundär till inflammation eller trauma.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Makulärt Hål - Fullständigt",
        "name_en": "Full-Thickness Macular Hole",
        "icd10": "H35.3",
        "symptoms": [
            "central synnedsättning",
            "metamorfopsi",
            "central skotom",
            "svårigheter läsa",
            "gradvis försämring"
        ],
        "anamnesis_questions": [
            "Ser du en mörk fläck centralt?",
            "Ser linjer förvrängda ut?",
            "Har du höga myopi?",
            "Har du haft ögontrauma?",
            "Märker du försämring över tid?"
        ],
        "clinical_signs": [
            "runt hål i central makula på OCT",
            "defekt i alla retinala lager",
            "eventuell gul ring (xantofyll)",
            "cuff av subretinal vätska",
            "Watzke-Allen test positiv",
            "eventuell vitreomakulär traktion",
            "stadieindelning 1-4"
        ],
        "risk_factors": [
            "hög ålder (60-80 år)",
            "kvinnligt kön",
            "vitreomakulär traktion",
            "höga myopi",
            "ögontrauma",
            "hål i andra ögat (10-15% risk)"
        ],
        "treatment": "Vitrektomi med ILM (internal limiting membrane) peeling, gasbubbla (C3F8 eller SF6), ansiktsned positionering 1-2 veckor, 85-95% slutningsfrekvens, bättre prognos vid mindre hål och kortare duration",
        "kva": "CJE20",
        "differential_diagnoses": [
            "Lamellärt makulärt hål",
            "Pseudo-hål (vid ERM)",
            "Maculaödem",
            "Central serös korioretinopati"
        ],
        "description": "Fullständigt makulärt hål innebär defekt genom alla retinala lager i fovea. Vanligen relaterat till vitreomakulär traktion vid PVD. Kirurgisk åtgärd ger ofta god prognos.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Vitreomakulär Traktion (VMT)",
        "name_en": "Vitreomacular Traction",
        "icd10": "H43.8",
        "symptoms": [
            "metamorfopsi",
            "mild synnedsättning",
            "ofta asymtomatisk",
            "gradvis progression möjlig"
        ],
        "anamnesis_questions": [
            "Ser linjer lite förvrängda ut?",
            "Märker du försämrad syn för läsning?",
            "Har symptomen försämrats över tid?"
        ],
        "clinical_signs": [
            "partiell glaskroppsavlossning på OCT",
            "persistent fäste vid fovea",
            "foveal förändring/distorsion",
            "intraretinal cystor möjliga",
            "risk för makulärt hål"
        ],
        "risk_factors": [
            "hög ålder",
            "PVD (posterior vitreous detachment) pågående",
            "stark vitreomakular adhesion"
        ],
        "treatment": "Observation om asymtomatisk eller mild, vitrektomi om signifikant symptom eller progression, ocriplasmin (Jetrea) enzymatisk vitreolys (sällan använd numera), spontan resolution möjlig i 10-30%",
        "kva": "CJE20",
        "differential_diagnoses": [
            "Epiretinal membran",
            "Makulärt hål stadium 1",
            "Maculaödem"
        ],
        "description": "VMT uppstår vid inkomplett PVD där glaskroppen kvarstår fäst vid makula och orsakar traktion. Kan leda till makulärt hål eller spontant lossna.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Central Serös Korioretinopati (CSC)",
        "name_en": "Central Serous Chorioretinopathy",
        "icd10": "H35.7",
        "symptoms": [
            "plötslig, mild-måttlig central synnedsättning",
            "central relativ skotom",
            "metamorfopsi",
            "mikropsi (objekt ser mindre ut)",
            "färgavvikelse",
            "eventuell hyperopi-skift"
        ],
        "anamnesis_questions": [
            "Är du man i 30-50-årsåldern?",
            "Har du haft mycket stress nyligen?",
            "Använder du kortison (tabletter, nässpray, inhalation)?",
            "Ser objekt mindre ut än normalt?",
            "Ser du en suddig fläck centralt?",
            "Har du haft detta tidigare?"
        ],
        "clinical_signs": [
            "neurosensorisk avlossning på OCT",
            "subretinal vätska",
            "RPE-förändring (pigmentepitel)",
            "fluoresceinangiografi: smokestack eller inkblot läckage",
            "OCT: serous PED möjlig",
            "pachykorioidea (tjock korioidea)"
        ],
        "risk_factors": [
            "manligt kön (6:1)",
            "ålder 30-50 år",
            "typ A-personlighet/stress",
            "kortikosteroidanvändning (systemiskt, inhalerat, intranasalt)",
            "graviditet",
            "hypertoni",
            "Helicobacter pylori-infektion möjligen"
        ],
        "treatment": "Observation i 3-6 månader (90% spontanläkning), undvik kortison om möjligt, stressreduktion, photodynamisk terapi (PDT) vid kronisk CSC (>6 mån), anti-VEGF mindre effektivt än PDT, subtröskel micropulse laser som alternativ",
        "kva": "CJD99",  # Annan laserbehandling
        "differential_diagnoses": [
            "Våt AMD (hos äldre)",
            "Makulärt hål med vätska",
            "Uveit med maculaödem",
            "Myopisk CNV"
        ],
        "description": "CSC är en oftast självläkande sjukdom med läckage genom RPE som leder till subretinal vätska. Vanligast hos stressade män 30-50 år. Recidiv vanligt (30-50%).",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Retinitis Pigmentosa",
        "name_en": "Retinitis Pigmentosa",
        "icd10": "H35.5",
        "symptoms": [
            "nattblindhet (första symptom, ofta i ungdomen)",
            "gradvis perifer synfältsinskränkning (tunnelseende)",
            "svårigheter se i dåligt ljus",
            "bländningskänslighet",
            "sen central synnedsättning",
            "färgseendedefekter"
        ],
        "anamnesis_questions": [
            "Har du svårt att se i mörker eller skymning?",
            "Snubblar du ofta över saker i periferin?",
            "Har du tunnelseende?",
            "Finns det andra i familjen med synproblem?",
            "I vilken ålder började symptomen?",
            "Har du hörselnedsättning? (Ushers syndrom)"
        ],
        "clinical_signs": [
            "bentakulärt pigment (bone spicules) i periferi",
            "attenuerade retinala artärer",
            "vaxgul blekhet av papillen",
            "posterior subkapsulär katarakt (hos många)",
            "maculaödem (CME) hos 10-50%",
            "ERG (elektroretinogram): kraftigt nedsatt eller släckt"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant, recessivt eller X-bundet)",
            "consanguinity (släktskap föräldrar)",
            "syndrom: Ushers (dövhet), Bardet-Biedl, etc."
        ],
        "treatment": "Ingen bot, vitamin A-palmitat 15000 IU dagligen (kan bromsa progression något), behandla maculaödem (Acetazolamid eller CAI, OCT-monitorering), behandla katarakt vid behov, genetisk rådgivning, synrehabilitering, vita käppen, registrering hos syncentralen, genterapi under utveckling (Luxturna för RPE65-mutation)",
        "kva": "Ingen kurativ",
        "differential_diagnoses": [
            "Korioideraömi",
            "Gyrate atrofi",
            "Medikamentinducerad retinopati (klorokin)",
            "Syfilis-retinit"
        ],
        "description": "RP är en grupp hereditära dystrofier med progressiv degeneration av fotoreceptorer (särskilt stavar). Leder till nattblindhet, synfältsinskränkning och slutligen blindhet. En av vanligaste orsakerna till hereditär blindhet.",
        "severity": "severe",
        "urgency": "routine"
    },
    {
        "name": "Myopisk Makuladegeneration",
        "name_en": "Myopic Macular Degeneration",
        "icd10": "H44.2",
        "symptoms": [
            "gradvis central synnedsättning",
            "metamorfopsi",
            "central skotom",
            "svårigheter läsa",
            "plötslig försämring vid CNV"
        ],
        "anamnesis_questions": [
            "Hur höga är dina minusglas?",
            "Har du mer än -6 dioptrier myopi?",
            "Märker du böjda linjer?",
            "Har synen försämrats gradvis eller plötsligt?"
        ],
        "clinical_signs": [
            "patologisk myopi (>-6 D, axiallängd >26 mm)",
            "posterior stafylom",
            "diffus korioretinal atrofi",
            "lacquer cracks (brister i Bruchs membran)",
            "Fuchs' fläck (subretinal blödning/fibros)",
            "CNV (koroidal neovaskulisation)",
            "myopisk CNV hos 5-10%"
        ],
        "risk_factors": [
            "hög myopi (>-6 D)",
            "östasiatisk etnicitet",
            "hereditet",
            "progression av myopi"
        ],
        "treatment": "Anti-VEGF vid myopisk CNV (god respons!), behandla lacquer cracks om symptomatiska, synrehabilitering, följa progression av myopi hos barn (atropindroppar, defokus kontaktlinser/glasögon)",
        "kva": "CJE10",
        "differential_diagnoses": [
            "AMD (hos äldre)",
            "Patologisk myopi utan CNV",
            "Central serös korioretinopati"
        ],
        "description": "Patologisk myopi med degenerativa förändringar i makula är en ledande orsak till blindhet hos unga-medelålders i Asien. CNV vid myopi svarar ofta bättre på anti-VEGF än AMD.",
        "severity": "moderate-severe",
        "urgency": "urgent (vid CNV)"
    },
    {
        "name": "Makulaödem vid Uveit",
        "name_en": "Uveitic Macular Edema",
        "icd10": "H20.9 + H35.81",
        "symptoms": [
            "central synnedsättning",
            "suddig syn",
            "metamorfopsi",
            "färgseendeförändring",
            "fotopsi möjlig"
        ],
        "anamnesis_questions": [
            "Har du inflammation i ögat (uveit)?",
            "Har du autoimmun sjukdom?",
            "Har du rött öga eller smärta?",
            "Använder du steroiddroppar?",
            "Har du Bechterews, sarkoid eller annan systemsjukdom?"
        ],
        "clinical_signs": [
            "cystoid maculaödem (CME) på OCT",
            "petaloid pattern på fluoresceinangiografi",
            "tecken på uveit: cellreaktion, KP, synechiae",
            "eventuell vitrit",
            "periphlebit möjlig"
        ],
        "risk_factors": [
            "kronisk eller recidiverande uveit",
            "intermediär uveit (pars planitis)",
            "posterior uveit",
            "Bechterews sjukdom",
            "sarkoidos",
            "Behçets sjukdom"
        ],
        "treatment": "Behandla underliggande uveit med steroider (lokalt och/eller systemiskt), CAI (carboanhydrashämmare) lokalt eller systemiskt, intravitreal steroidinjektion (Ozurdex, Iluvien, triamcinolon), systemisk immunsuppression vid kronisk uveit (MTX, azathioprin, biologiska läkemedel), anti-VEGF mindre effektivt än vid andra orsaker",
        "kva": "CJE10",
        "differential_diagnoses": [
            "Maculaödem vid diabetes",
            "Venockklusion",
            "Postoperativt CME (Irvine-Gass)",
            "Epiretinal membran"
        ],
        "description": "Maculaödem är vanlig komplikation vid uveit och en huvudorsak till synnedsättning. Kräver behandling av både inflammation och ödem.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Retinopati av Prematuritet (ROP)",
        "name_en": "Retinopathy of Prematurity",
        "icd10": "H35.1",
        "symptoms": [
            "screening-fynd hos prematura",
            "inga tidiga symptom",
            "risk för blindhet utan behandling",
            "dålig syn vid progression till stadium 4-5"
        ],
        "anamnesis_questions": [
            "Vilken graviditetsvecka föddes barnet?",
            "Vilken födelsevikt?",
            "Hur länge fick barnet syrebehandling?",
            "Har barnet screenpats för ROP?"
        ],
        "clinical_signs": [
            "demarcation line (stadium 1)",
            "ridge (stadium 2)",
            "extraretinal fibrovaskulär proliferation (stadium 3)",
            "partiell retinal avlossning (stadium 4)",
            "total retinal avlossning (stadium 5)",
            "plus disease (vendilatation, arterieökad tortuositet)",
            "pre-plus disease"
        ],
        "risk_factors": [
            "födsel <32 graviditetsveckor",
            "födelsevikt <1500 g",
            "syrebehandling",
            "respiratorbehandling",
            "låg Apgar score",
            "intraventrikulär blödning"
        ],
        "treatment": "Screening alla <31 veckor eller <1500g, laser eller anti-VEGF vid typ 1 ROP (zone I: stadium 1-3 med plus, zone II: stadium 2-3 med plus), vitrektomi vid stadium 4-5, uppföljning till full vaskulärt mogen retina",
        "kva": "CJD96",
        "differential_diagnoses": [
            "Familjär exsudativ vitreoretinopati (FEVR)",
            "Norrie disease",
            "Persistent fetal vasculature"
        ],
        "description": "ROP uppstår hos för tidigt födda barn där retinal vaskulär utveckling störs av syrebehandling och andra faktorer. Kan leda till blindhet men förhindras ofta med screening och tidig behandling.",
        "severity": "severe",
        "urgency": "emergency (vid typ 1)"
    },
    {
        "name": "Cystoid Maculaödem Postoperativt (Irvine-Gass)",
        "name_en": "Postoperative Cystoid Macular Edema",
        "icd10": "H59.0",
        "symptoms": [
            "gradvis synnedsättning 4-12 veckor postop",
            "suddig syn",
            "metamorfopsi möjlig",
            "ofta självläkande"
        ],
        "anamnesis_questions": [
            "När opererades du för grå starr?",
            "Var operationen komplicerad?",
            "Har du diabetes eller uveit?",
            "Använder du NSAID-droppar postoperativt?"
        ],
        "clinical_signs": [
            "cystoid pattern på OCT",
            "petaloid läckage på fluoresceinangiografi",
            "central foveal tjocklek ökad",
            "oftast 4-12 veckor efter kataraktkirurgi"
        ],
        "risk_factors": [
            "komplicerad kataraktkirurgi",
            "bakomkapsulär ruptur",
            "vitreosförlust",
            "tidigare uveit",
            "diabetes",
            "retinal venockklusion",
            "epiretinal membran"
        ],
        "treatment": "NSAID-droppar (ketorolac, bromfenac, nepafenac) 4x dagligen, steroidroppar lokalt, ofta spontanläkning inom 3-6 månader, intravitreal steroid vid refraktär (Ozurdex), CAI (acetazolamid) systemiskt vid svåra fall",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Diabetiskt maculaödem",
            "Maculaödem vid venockklusion",
            "Uveitiskt maculaödem"
        ],
        "description": "Irvine-Gass syndrom är cystoid maculaödem efter okomplicerad eller komplicerad kataraktkirurgi. Oftast självläkande men kan kräva behandling. Profylax med NSAID rekommenderas hos högriskpatienter.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Koroidal Neovaskulisation (CNV) - Icke-AMD",
        "name_en": "Choroidal Neovascularization (non-AMD)",
        "icd10": "H35.3",
        "symptoms": [
            "plötslig eller gradvis synnedsättning",
            "metamorfopsi",
            "central skotom",
            "beroende på underliggande orsak"
        ],
        "anamnesis_questions": [
            "Har du hög myopi?",
            "Har du haft inflammation i ögat?",
            "Har du haft laserbehandling (PDT)?",
            "Har du herediter makulasjukdom?",
            "Har du haft ögontrauma?"
        ],
        "clinical_signs": [
            "subretinal vätska/blödning",
            "CNV på OCT-angiografi",
            "underliggande orsak synlig: myopi, angioid streaks, etc."
        ],
        "risk_factors": [
            "patologisk myopi",
            "angioid streaks (pseudoxanthoma elasticum, Paget, sicklecell)",
            "multifocal choroiditis",
            "presumed ocular histoplasmosis",
            "ögontrauma",
            "choroidal rupture"
        ],
        "treatment": "Anti-VEGF (ofta god respons, särskilt myopisk CNV), behandla underliggande orsak, färre injektioner behövs ofta jämfört med AMD",
        "kva": "CJE10",
        "differential_diagnoses": [
            "AMD (hos äldre)",
            "Central serös korioretinopati",
            "Makulärt hål"
        ],
        "description": "CNV kan uppstå sekundärt till många tillstånd som skadar Bruchs membran. Myopisk CNV är vanligast hos yngre. Svarar ofta bra på anti-VEGF.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Retinal Makroaneurysm",
        "name_en": "Retinal Macroaneurysm",
        "icd10": "H35.0",
        "symptoms": [
            "plötslig synnedsättning (vid blödning)",
            "kan vara asymtomatisk",
            "suddig syn",
            "synfältsbortfall möjligt"
        ],
        "anamnesis_questions": [
            "Har du högt blodtryck?",
            "Är du kvinna över 60 år?",
            "Fick du plötslig synförsämring?",
            "Har du diabetes?"
        ],
        "clinical_signs": [
            "rund utbuktning på retinal artär",
            "ofta temporalt från papillen",
            "retinal blödning (preretinal, intraretinal, subretinal)",
            "hårda exudat runt",
            "eventuellt maculaödem"
        ],
        "risk_factors": [
            "hypertoni (80-90%)",
            "kvinnligt kön",
            "hög ålder (60-80 år)",
            "ateroskleros"
        ],
        "treatment": "Konservativ behandling (oftast spontan trombosering och resolution), kontroll av blodtryck, observation, laser endast vid persisterande läckage med maculaödem, anti-VEGF vid maculaödem",
        "kva": "Ingen vanligtvis",
        "differential_diagnoses": [
            "Retinal venockklusion med blödning",
            "Retinal vaskulit",
            "Diabetesretinopati"
        ],
        "description": "Retinal makroaneurysm är lokal utvidgning av retinal artär, vanligen hos äldre hypertensiva kvinnor. Ofta självläkande men kan ge kraftig blödning och synnedsättning.",
        "severity": "moderate",
        "urgency": "urgent (vid blödning)"
    },
    {
        "name": "Valsalva Retinopati",
        "name_en": "Valsalva Retinopathy",
        "icd10": "H35.6",
        "symptoms": [
            "plötslig synnedsättning efter fysisk ansträngning",
            "central skotom",
            "oftast unilateral",
            "historia av kraftansträngning, kräkning, hosta"
        ],
        "anamnesis_questions": [
            "Lyfte du något tungt nyligen?",
            "Har du krystst, hostat eller kräkts kraftigt?",
            "Spelade du blåsinstrument?",
            "När märkte du synförsämringen?"
        ],
        "clinical_signs": [
            "preretinal blödning",
            "round/boat-shaped blödning framför fovea",
            "oftast välavgränsad",
            "underliggande retina normal"
        ],
        "risk_factors": [
            "Valsalva-manöver (tungt lyft, kräkning, defekation, förlossning)",
            "blåsinstrument",
            "tung fysisk ansträngning"
        ],
        "treatment": "Konservativ (observation) - spontan resorption inom veckor-månader, Nd:YAG-laser hyaloidotomi om långsam resorption och dålig syn, vitrektomi endast vid stora blödningar som ej resorberas",
        "kva": "Ingen vanligtvis",
        "differential_diagnoses": [
            "Trauma-relaterad blödning",
            "Subarachnoidalblödning (Terson syndrom)",
            "Diabetesretinopati",
            "Retinal venockklusion"
        ],
        "description": "Valsalva retinopati uppstår vid plötslig ökning av intrathorakalt/intraabdominalt tryck som leder till venös tryckstegring och kärlruptur. God prognos med spontanläkning.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Angioid Streaks",
        "name_en": "Angioid Streaks",
        "icd10": "H35.3",
        "symptoms": [
            "ofta asymtomatisk",
            "gradvis synnedsättning",
            "metamorfopsi",
            "plötslig försämring vid CNV"
        ],
        "anamnesis_questions": [
            "Har du diagnosen pseudoxanthoma elasticum?",
            "Har du Pagets sjukdom?",
            "Har du sicklecellsjukdom?",
            "Har du elastisk hud?",
            "Finns systemsjukdom i familjen?"
        ],
        "clinical_signs": [
            "brunröda eller gråaktiga strimmor radiärt från papillen",
            "brister i Bruchs membran",
            "peau d'orange vid papillen",
            "risk för CNV (70-85% livstidsrisk)",
            "subretinal blödning vid CNV"
        ],
        "risk_factors": [
            "pseudoxanthoma elasticum (PXE) - 50%",
            "Pagets sjukdom",
            "sicklecellsjukdom",
            "Ehlers-Danlos syndrom",
            "idiopatisk - 50%"
        ],
        "treatment": "Behandla CNV med anti-VEGF, undvik kontaktsporter (risk för koroidal ruptur), genetisk utredning, internmedicinsk/dermatologisk uppföljning vid PXE (kardiovaskulär risk)",
        "kva": "CJE10",
        "differential_diagnoses": [
            "Myopiska lacquer cracks",
            "Choroidal ruptur",
            "Histoplasmosis-ärr"
        ],
        "description": "Angioid streaks är brister i Bruchs membran, ofta associerade med systemsjukdomar. Hög risk för CNV som kan leda till svår synnedsättning.",
        "severity": "moderate-severe",
        "urgency": "urgent (vid CNV)"
    },
    {
        "name": "Mönsterdystrofi (Pattern Dystrophy)",
        "name_en": "Pattern Dystrophy",
        "icd10": "H35.5",
        "symptoms": [
            "gradvis synnedsättning (vanligen mild)",
            "metamorfopsi",
            "ofta bilateral och symmetrisk",
            "variabel progression"
        ],
        "anamnesis_questions": [
            "Finns synproblem i familjen?",
            "I vilken ålder började symptomen?",
            "Har synen försämrats gradvis?",
            "Märker du förvrängda linjer?"
        ],
        "clinical_signs": [
            "olika mönster av pigment i makula",
            "butterfly pattern",
            "adult-onset foveomacular vitelliform dystrophy",
            "fundus pulverulentus",
            "fundus flavimaculatus",
            "autofluorescens ofta karakteristisk"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant oftast)",
            "PRPH2/RDS-genmutation vanlig",
            "familjehistoria"
        ],
        "treatment": "Ingen specifik behandling, AREDS-vitaminer kan övervägas, synrehabilitering vid behov, genetisk rådgivning, övervaka för CNV (sällsynt komplikation)",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Torr AMD",
            "Stargardt disease",
            "Best disease (vitelliform dystrophy)",
            "Toxisk makulopati"
        ],
        "description": "Mönsterdystrofier är en grupp hereditära makuladystrofier med karakteristiska pigmentmönster. Oftast god prognos med långsam progression.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Best Vitelliform Makuladystrofi",
        "name_en": "Best Vitelliform Macular Dystrophy",
        "icd10": "H35.5",
        "symptoms": [
            "ofta asymtomatisk i tidiga stadier",
            "gradvis synnedsättning",
            "metamorfopsi",
            "variabel ålder vid debut (barndom-vuxen)"
        ],
        "anamnesis_questions": [
            "Finns synproblem i familjen?",
            "I vilken ålder upptäcktes förändringarna?",
            "Hur är synen nu?",
            "Märker du förvrängningar?"
        ],
        "clinical_signs": [
            "\"äggula\" lesion i fovea (vitelliform stage)",
            "stadieindelning: previtelliform → vitelliform → pseudohypopyon → vitelliruptiv → atrofi",
            "EOG (elektrookulogram) abnormt (Arden ratio <1.5)",
            "autofluorescens hyperautofluorescent vid vitelliform stage"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant)",
            "BEST1-genmutation",
            "familjehistoria"
        ],
        "treatment": "Ingen specifik behandling, observation och uppföljning, behandla CNV om uppstår (anti-VEGF), genetisk rådgivning, variabel prognos (vissa behåller god syn, andra utvecklar atrofi)",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Adult-onset foveomacular vitelliform dystrophy (AOFVD)",
            "Central serös korioretinopati",
            "Toxisk makulopati"
        ],
        "description": "Best disease är en hereditär makuladystrofi med karakteristisk ägguleliknande lesion. Variabel prognos med progression genom olika stadier.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Stargardt Disease",
        "name_en": "Stargardt Disease",
        "icd10": "H35.5",
        "symptoms": [
            "bilateral central synnedsättning",
            "debut oftast 10-20 års ålder",
            "svårigheter läsa",
            "nedsatt färgseende",
            "gradvis progression",
            "nattblindhet mindre vanligt än RP"
        ],
        "anamnesis_questions": [
            "I vilken ålder började synproblemen?",
            "Finns synproblem i familjen?",
            "Har båda ögonen påverkats?",
            "Märker du svårighet med färger?",
            "Har du svårt att se i mörker?"
        ],
        "clinical_signs": [
            "bronsfärgad fovea (beaten-bronze appearance)",
            "gula fläckar (flecks) på posteriora polen",
            "geografisk atrofi i central makula",
            "silent choroid på fluoresceinangiografi",
            "fundusautofluorescens visar atrofi och flecks",
            "ERG normal initialt, senare nedsatt"
        ],
        "risk_factors": [
            "hereditet (autosomalt recessivt vanligast)",
            "ABCA4-genmutation",
            "consanguinity"
        ],
        "treatment": "Ingen bot, undvik höga doser vitamin A (kan försämra), synrehabilitering, förstoringshjälpmedel, genetisk rådgivning, genterapi under forskning, registrering hos syncentralen",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Cone-rod dystrophy",
            "AMD (hos äldre)",
            "Toxisk makulopati",
            "Pattern dystrophy"
        ],
        "description": "Stargardt disease är den vanligaste hereditära makuladystrofin. Debuterar oftast i ungdomsåren med bilateral central synnedsättning och karakteristiska gula fläckar.",
        "severity": "moderate-severe",
        "urgency": "routine"
    },
    {
        "name": "X-bunden Juvenil Retinoschisis",
        "name_en": "X-linked Juvenile Retinoschisis",
        "icd10": "H35.7",
        "symptoms": [
            "bilateral synnedsättning, debut barndom (5-10 år)",
            "gradvis progression",
            "variabel svårighetsgrad",
            "endast pojkar påverkade"
        ],
        "anamnesis_questions": [
            "Är patienten pojke?",
            "I vilken ålder upptäcktes synproblemen?",
            "Finns synproblem hos andra manliga släktingar?",
            "Har mamman bärare av gendefekt?"
        ],
        "clinical_signs": [
            "foveal schisis (spoke-wheel pattern på OCT)",
            "cystiska spaces i makula",
            "perifer retinoschisis (50%)",
            "eventuella vitreous veils",
            "risk för retinal avlossning",
            "ERG: nedsatt b-våg (negativt ERG)"
        ],
        "risk_factors": [
            "X-bundet recessivt (endast pojkar)",
            "RS1-genmutation",
            "familjehistoria"
        ],
        "treatment": "Ingen specifik behandling för schisis, behandla komplikationer (avlossning), undvik kontaktsporter, observation, genetisk rådgivning, genterapi under utveckling",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Cystoid maculaödem",
            "Familjär exsudativ vitreoretinopati",
            "Retinitis pigmentosa"
        ],
        "description": "X-bunden juvenil retinoschisis orsakar splitting av retina med foveal och eventuellt perifer schisis. Påverkar endast pojkar. Variabel prognos.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Koroidal Dystrofi",
        "name_en": "Choroideremia",
        "icd10": "H31.2",
        "symptoms": [
            "nattblindhet (tidigt symptom)",
            "gradvis perifer synfältsinskränkning",
            "sen central synnedsättning",
            "progression till blindhet i 40-60 års ålder",
            "endast män påverkade"
        ],
        "anamnesis_questions": [
            "Är patienten man?",
            "Har du nattblindhet?",
            "Har du tunnelseende?",
            "Finns synproblem hos manliga släktingar (morbror, morfar)?",
            "I vilken ålder började symptomen?"
        ],
        "clinical_signs": [
            "progressiv atrofi av korioidea, RPE och fotoreceptorer",
            "vita sklera synlig genom atrofisk korioidea",
            "stora koroidala kärl exponerade",
            "börjar i periferi, sprider sig centralt",
            "kvinnliga bärare: pigmentmottling men oftast god syn",
            "ERG progressivt nedsatt"
        ],
        "risk_factors": [
            "X-bundet recessivt (endast män)",
            "CHM-genmutation",
            "familjehistoria"
        ],
        "treatment": "Ingen bot, synrehabilitering, genetisk rådgivning, genterapi under klinisk prövning (lovande resultat), registrering hos syncentralen",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Retinitis pigmentosa",
            "Gyrate atrophy",
            "Diffus koroidal atrofi"
        ],
        "description": "Koroideraömi är en X-bunden progressiv degeneration av korioidea och retina. Endast män drabbas av sjukdom, kvinnor är bärare. Genterapi visar lovande resultat.",
        "severity": "severe",
        "urgency": "routine"
    },
    {
        "name": "Retinal Arteriolärt Makroaneurysm",
        "name_en": "Retinal Arteriolar Macroaneurysm",
        "icd10": "H35.0",
        "symptoms": [
            "oftast asymtomatisk",
            "plötslig synnedsättning vid blödning",
            "kan vara bifynd"
        ],
        "anamnesis_questions": [
            "Har du högt blodtryck?",
            "Är du kvinna över 60 år?",
            "Har du haft plötslig synförsämring?"
        ],
        "clinical_signs": [
            "som Retinal Makroaneurysm ovan",
            "rund utvidgning på artärgren",
            "blödningar möjliga"
        ],
        "risk_factors": [
            "som ovan - hypertoni, ålder, kön"
        ],
        "treatment": "Som Retinal Makroaneurysm - konservativ behandling",
        "kva": "Ingen vanligtvis",
        "differential_diagnoses": [
            "Venockklusion",
            "Diabetesretinopati"
        ],
        "description": "Liknande retinal makroaneurysm - lokal artärdilatation hos hypertensiva äldre.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Subretinal Fibrosis (Diskiform Ärr)",
        "name_en": "Subretinal Fibrosis (Disciform Scar)",
        "icd10": "H35.3",
        "symptoms": [
            "kraftig permanent central synnedsättning",
            "central skotom",
            "slutstadium av våt AMD eller annan CNV"
        ],
        "anamnesis_questions": [
            "Har du haft våt AMD?",
            "Har du fått anti-VEGF-behandling tidigare?",
            "Har du haft CNV av annan orsak?",
            "När försämrades synen?"
        ],
        "clinical_signs": [
            "gul-vit subretinal fibrotisk lesion",
            "RPE-hyperplasi",
            "ingen aktiv läckage",
            "irreversibel förändring",
            "syn ofta 0.1 eller sämre"
        ],
        "risk_factors": [
            "långvarig obehandlad våt AMD",
            "recidiverande CNV",
            "stort CNV initialt",
            "subretinal blödning"
        ],
        "treatment": "Ingen effektiv behandling (permanent ärr), synrehabilitering, förstoringshjälpmedel, behandla andra ögat om AMD där",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Toxoplasma-ärr",
            "Koroidal nevus",
            "Organiserad subretinal blödning"
        ],
        "description": "Diskiform ärr är slutstadiet av långvarig CNV med fibrosbildning. Leder till permanent svår central synnedsättning. Understryker vikten av tidig behandling.",
        "severity": "severe",
        "urgency": "routine (skadan redan skedd)"
    },
    {
        "name": "Polypoidal Koroidal Vaskulopati (PCV)",
        "name_en": "Polypoidal Choroidal Vasculopathy",
        "icd10": "H35.3",
        "symptoms": [
            "återkommande subretinal blödningar",
            "synnedsättning",
            "metamorfopsi",
            "oftare hos asiater och afroamerikaner"
        ],
        "anamnesis_questions": [
            "Har du haft återkommande blödningar i ögat?",
            "Är du av asiatiskt eller afroamerikanskt ursprung?",
            "Har du fått behandling för AMD tidigare?",
            "Svarar behandlingen dåligt?"
        ],
        "clinical_signs": [
            "orange-röda polypoidal lesioner",
            "branching vascular network på ICGA (indocyanine green angiography)",
            "recidiverande subretinal blödning",
            "serösa PED",
            "ofta peripapillärt beläget"
        ],
        "risk_factors": [
            "asiatiskt eller afroamerikanskt ursprung",
            "ålder >50 år",
            "hypertoni",
            "vissa genetiska varianter"
        ],
        "treatment": "Anti-VEGF (mindre effektivt än vid AMD), photodynamisk terapi (PDT), kombination PDT + anti-VEGF ofta bäst, förlängd behandlingsperiod behövs",
        "kva": "CJE10",
        "differential_diagnoses": [
            "Våt AMD",
            "Central serös korioretinopati",
            "Retinal makroaneurysm"
        ],
        "description": "PCV är en variant av neovaskulär makulopati med polypoida lesioner i korioidea. Vanligare hos asiater. Kräver ofta kombination av behandlingar.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Maculär Teleangiektasi Typ 2",
        "name_en": "Macular Telangiectasia Type 2",
        "icd10": "H35.0",
        "symptoms": [
            "gradvis synnedsättning i medelåldern",
            "metamorfopsi",
            "lässvårigheter",
            "ofta bilateral",
            "variabel progression"
        ],
        "anamnesis_questions": [
            "Hur gammal är du? (oftast 50-60 år)",
            "Ser du förvrängda linjer?",
            "Har båda ögonen påverkats?",
            "Har du diabetes? (viktigt att utesluta!)"
        ],
        "clinical_signs": [
            "parafoveal telangiektasi",
            "foveal atrofi",
            "kristalldepositioner temporalt om fovea",
            "right-angle venules",
            "OCT: hyperreflektiva foci, ellipsoid zone disruption",
            "autofluorescens: hypoautofluorescence temporalt",
            "OCT-angiografi visar telangiektasi",
            "sent: CNV i 10%"
        ],
        "risk_factors": [
            "ålder 50-60 år vid debut",
            "ingen känd hereditet",
            "oklar etiologi"
        ],
        "treatment": "Ingen beprövad behandling för själva tillståndet, observation, behandla CNV om uppstår (anti-VEGF), kliniska studier pågår (ciliary neurotrophic factor implant)",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Diabetiskt maculaödem (viktigt!)",
            "AMD",
            "Epiretinal membran",
            "Maculär teleangiektasi typ 1 (sällsynt)"
        ],
        "description": "MacTel typ 2 är en idiopatisk bilateral sjukdom med parafoveal telangiektasi och gradvis fotoreceptorförlust. Långsam progression, variabel prognos.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Acute Macular Neuroretinopathy (AMN)",
        "name_en": "Acute Macular Neuroretinopathy",
        "icd10": "H35.8",
        "symptoms": [
            "akuta paracentrala skotom",
            "oftast efter virusinfektion eller systemisk sjukdom",
            "kan vara unilateral eller bilateral",
            "unga till medelålders patienter"
        ],
        "anamnesis_questions": [
            "Har du haft influensa eller virusinfektion nyligen?",
            "Märkte du plötsliga mörka fläckar i synfältet?",
            "Använder du sympatomimetika (näsdroppar, efedrin)?",
            "Har du lågt blodtryck eller chock haft nyligen?"
        ],
        "clinical_signs": [
            "mörk rödbrun lesion i makula (svår att se vid funduskopi)",
            "petaloid pattern på NIR (near-infrared reflectance)",
            "OCT: hyperreflektivitet i yttre retina",
            "disruption av ellipsoid zone och interdigitation zone",
            "fluoresceinangiografi oftast normal"
        ],
        "risk_factors": [
            "virusinfektion",
            "sympatomimetika-användning",
            "hypotension/chock",
            "kvinnligt kön (70%)",
            "ålder 20-40 år"
        ],
        "treatment": "Ingen specifik behandling, oftast spontan förbättring (kan ta månader), skotom kan persista permanent, undvik triggerande faktorer",
        "kva": "Ingen",
        "differential_diagnoses": [
            "MEWDS (Multiple Evanescent White Dot Syndrome)",
            "AZOOR (Acute Zonal Occult Outer Retinopathy)",
            "Posterior uveitis",
            "Toxoplasmosis"
        ],
        "description": "AMN är en akut sjukdom i yttre retina som ger paracentrala skotom. Ofta associerad med virusinfektion eller vasokonstriktiiva läkemedel. God prognos men skotom kan persista.",
        "severity": "mild-moderate",
        "urgency": "urgent (initial bedömning)"
    },
    {
        "name": "Punctate Inner Choroidopathy (PIC)",
        "name_en": "Punctate Inner Choroidopathy",
        "icd10": "H30.8",
        "symptoms": [
            "flimmer (fotopsier)",
            "paracentrala skotom",
            "lätt suddig syn",
            "oftast unga myopa kvinnor"
        ],
        "anamnesis_questions": [
            "Är du myop (närsynt)?",
            "Ser du ljusblixtar?",
            "Märker du mörka fläckar i synfältet?",
            "Är du kvinna 20-40 år?"
        ],
        "clinical_signs": [
            "små (100-300 μm) gul-vita lesioner på posteriora polen",
            "minimal till ingen vitrit",
            "ingen anterior uveitis",
            "lesioner läker med atrofiska ärr",
            "CNV i 40% (viktigt!)",
            "autofluorescens: hypoautofluorescence vid ärr"
        ],
        "risk_factors": [
            "kvinnligt kön (80%)",
            "myopi",
            "ålder 20-40 år",
            "okänd etiologi (förmodad autoimmun)"
        ],
        "treatment": "Observation om mild/ingen CNV, steroider vid aktiv inflammation (diskutabelt), anti-VEGF vid CNV (vanlig komplikation!), immunosuppression vid recidiv",
        "kva": "CJE10 (vid CNV)",
        "differential_diagnoses": [
            "Multifocal choroiditis and panuveitis (MCP)",
            "MEWDS",
            "Presumed ocular histoplasmosis syndrome (POHS)",
            "Sarcoid choroiditis"
        ],
        "description": "PIC är en inflammatorisk korioretinopati som drabbar unga myopa kvinnor. Karakteristiska små lesioner. Hög risk för CNV som kan ge permanent synnedsättning.",
        "severity": "moderate",
        "urgency": "urgent (uteslut CNV)"
    },
    {
        "name": "Serpiginös Koroidit",
        "name_en": "Serpiginous Choroiditis",
        "icd10": "H30.8",
        "symptoms": [
            "central eller paracentral synnedsättning",
            "fotopsier",
            "skotom",
            "oftast bilateral men asymmetrisk",
            "recidiverande förlopp"
        ],
        "anamnesis_questions": [
            "Har du haft återkommande episoder av synförsämring?",
            "Ser du ljusblixtar?",
            "Har båda ögonen påverkats?",
            "Har du immunbrist eller TB?",
            "Är du från område med TB-prevalens?"
        ],
        "clinical_signs": [
            "grå-gula lesioner som börjar peripapillärt",
            "ormliknande (serpiginous) utbredning mot makula",
            "läker med atrofi och RPE-förändringar",
            "minimal vitrit",
            "risk för CNV",
            "fluoresceinangiografi: tidig hypofluorescens, sen hyperfluorescens"
        ],
        "risk_factors": [
            "ålder 30-60 år",
            "eventuellt HLA-B7 association",
            "okänd etiologi (förmodad autoimmun)",
            "TB kan imitera (serpiginous-like choroiditis)"
        ],
        "treatment": "Systemiska steroider vid aktiv inflammation, immunosuppression (azathioprin, mykofenolatmofetil, cyclosporin) för att förhindra recidiv, uteslut TB (QFT, tuberkulinskillit, lungröntgen), anti-VEGF vid CNV, dålig prognos om makula involverad",
        "kva": "Ingen specifik",
        "differential_diagnoses": [
            "Tuberkulös serpiginous-like choroiditis (viktigt!)",
            "APMPPE (Acute Posterior Multifocal Placoid Pigment Epitheliopathy)",
            "Sarkoid koroidit",
            "Syfilis"
        ],
        "description": "Serpiginös koroidit är en kronisk recidiverande inflammation som sprider sig ormliknande från papillen. Kräver aggressiv immunosuppression. Viktigt att utesluta TB!",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Retinal Pigmentepitel Rip/Tear",
        "name_en": "Retinal Pigment Epithelium Tear",
        "icd10": "H35.3",
        "symptoms": [
            "plötslig synförsämring",
            "metamorfopsi",
            "hos patient med våt AMD och PED",
            "oftast under eller efter anti-VEGF-behandling"
        ],
        "anamnesis_questions": [
            "Har du våt AMD med pigmentepitelavlossning?",
            "Har du nyligen fått anti-VEGF-injektion?",
            "Fick du plötslig försämring efter behandling?"
        ],
        "clinical_signs": [
            "område med exponerad korioidea (där RPE lossnat)",
            "uppvikt kant av RPE",
            "eventuell subretinal blödning",
            "ofta vid kant av stor PED",
            "OCT: tydlig avsaknad av RPE i område"
        ],
        "risk_factors": [
            "stor fibro-vaskulär PED vid våt AMD",
            "anti-VEGF-behandling (särskilt första injektionen)",
            "stor PED-höjd (>600 μm)"
        ],
        "treatment": "Kontroversiellt: vissa fortsätter anti-VEGF (för kvarvarande CNV), vissa stoppar behandling, dålig prognos för syn i område med tear, övervaka för CNV-aktivitet utanför tear",
        "kva": "CJE10",
        "differential_diagnoses": [
            "Stor subretinal blödning",
            "Koroidal ruptur",
            "Exsudativ AMD utan tear"
        ],
        "description": "RPE tear är en komplikation till våt AMD, särskilt vid stora PED. Kan uppstå spontant eller efter anti-VEGF. Leder till permanent synnedsättning i det berörda området.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Familjär Exsudativ Vitreoretinopati (FEVR)",
        "name_en": "Familial Exudative Vitreoretinopathy",
        "icd10": "H35.0",
        "symptoms": [
            "variabel presentation: asymtomatisk till blindhet",
            "synnedsättning beroende på svårighetsgrad",
            "kan upptäckas vid screening eller vid komplikationer",
            "bilateral men ofta asymmetrisk"
        ],
        "anamnesis_questions": [
            "Finns synproblem i familjen?",
            "Har barnet strabismus?",
            "Har andra familjemedlemmar opererats för retinal avlossning?",
            "Föddes barnet fullgånget? (viktigt - inte premaurt som ROP)"
        ],
        "clinical_signs": [
            "perifer avaskulär retina",
            "abnorm retinavaskulär utveckling",
            "vitreoretinal traktion",
            "retinal veck",
            "exsudation",
            "retinal avlossning i svåra fall",
            "fluoresceinangiografi visar avaskulära zoner"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant vanligast, även recessivt och X-bundet)",
            "FZD4, LRP5, NDP, TSPAN12 genmutationer",
            "familjehistoria"
        ],
        "treatment": "Laserbehandling av avaskulära zoner (profylaktiskt), behandla exsudation, vitrektomi vid traktionsavlossning, screening av familjemedlemmar viktigt, variabel prognos beroende på svårighetsgrad",
        "kva": "CJD96",
        "differential_diagnoses": [
            "ROP (men fullgånget barn!)",
            "Norrie disease",
            "Incontinentia pigmenti",
            "Coat's disease"
        ],
        "description": "FEVR är en hereditär sjukdom med abnorm retinal vaskulär utveckling som kan likna ROP men hos fullgångna barn. Viktigt att screena familj. Variabel prognos.",
        "severity": "moderate-severe",
        "urgency": "urgent (vid komplikationer)"
    },
    {
        "name": "Cone Dystrophy/Cone-Rod Dystrophy",
        "name_en": "Cone Dystrophy/Cone-Rod Dystrophy",
        "icd10": "H35.5",
        "symptoms": [
            "central synnedsättning",
            "färgseendedefekt (viktig ledtråd!)",
            "fotophobi",
            "nystagmus möjlig",
            "perifer syn ofta bevarad initialt (skiljer från RP)",
            "debut ofta barndom-ungdom"
        ],
        "anamnesis_questions": [
            "Har du svårt att se färger?",
            "Är du känslig för starkt ljus?",
            "Har du svårt att se centralt men kan se i periferin?",
            "I vilken ålder började problemen?",
            "Finns synproblem i familjen?"
        ],
        "clinical_signs": [
            "bull's eye makulopati möjlig",
            "central atrofi",
            "eventuella pigmentförändringar",
            "ERG: nedsatt fotopisk respons (tappar), eventuellt också skotopisk (stavreceptorer) vid cone-rod dystrophy",
            "autofluorescens: central hypoautofluorescens"
        ],
        "risk_factors": [
            "hereditet (autosomalt dominant, recessivt eller X-bundet)",
            "ABCA4, GUCA1A och många andra genmutationer",
            "familjehistoria"
        ],
        "treatment": "Ingen bot, solglasögon för fotophobi, synrehabilitering, genetisk rådgivning, differentialdiagnos mot medikamentell toxicitet (Plaquenil) viktigt, uppföljning",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Stargardt disease",
            "Plaquenil-toxicitet (viktigt!)",
            "Achromatopsia (fullständig färgblindhet)",
            "Bull's eye makulopati av annan orsak"
        ],
        "description": "Cone dystrophy påverkar främst tappreceptorer och ger central synnedsättning, färgseendedefekt och fotophobi. Cone-rod dystrophy involverar också stavar senare. Varierar i svårighetsgrad.",
        "severity": "moderate-severe",
        "urgency": "routine"
    },
    {
        "name": "Hypertensiv Retinopati",
        "name_en": "Hypertensive Retinopathy",
        "icd10": "H35.0",
        "symptoms": [
            "ofta asymtomatisk i tidiga stadier",
            "gradvis synnedsättning",
            "suddig syn",
            "huvudvärk",
            "synförlust (vid svår hypertoni eller malign hypertoni)"
        ],
        "anamnesis_questions": [
            "Har du högt blodtryck?",
            "Tar du blodtrycksmedicin? Vilken dos?",
            "Vilket blodtryck brukar du ha?",
            "När mättes blodtrycket senast?",
            "Har du njursjukdom?",
            "Har du haft stroke eller hjärtinfarkt?",
            "Märker du synförsämring?"
        ],
        "clinical_signs": [
            "arteriolärt förträngning (grad 1-2)",
            "arteriovenösa korsningsförändringar (AV-nicking)",
            "retinala blödningar (flamformade i nervfiberskiktet)",
            "cotton-wool spots (mjuka exsudat)",
            "hårda exsudat",
            "papillödem (vid malign hypertoni)",
            "makulastjärna (vid svår hypertoni)",
            "serös retinal avlossning (vid malign hypertoni)"
        ],
        "risk_factors": [
            "långvarig hypertoni",
            "okontrollerat blodtryck",
            "malign hypertoni (diastoliskt >120 mmHg)",
            "njursjukdom",
            "diabetes",
            "kardiovaskulär sjukdom",
            "ålder"
        ],
        "treatment": "PRIMÄRT: aggressiv blodtryckssänkning (samarbete med internmedicin/primärvård). Målblodtryck <140/90 mmHg (lägre vid diabetes/njursjukdom). Vid malign hypertoni med papillödem: AKUT sjukhusvård, IV blodtryckssänkning (försiktig, risk för ischemi vid för snabb sänkning). Behandla underliggande orsaker (njursjukdom, feokromocytom). Oftalmologisk uppföljning: retinala förändringar kan regrediera vid god blodtryckskontroll. Inga specifika ögonbehandlingar i de flesta fall. Långtidsuppföljning för att monitorera vaskulära komplikationer.",
        "kva": "CJD05 (fundusundersökning)",
        "differential_diagnoses": [
            "diabetesretinopati",
            "retinal venockklusion",
            "papillödem av annan orsak",
            "anterior ischemisk optisk neuropati"
        ],
        "description": "Hypertensiv retinopati orsakas av kroniskt högt blodtryck som skadar retinala kärl. Gradering: Grad 1 (arteriolärt förträngning), Grad 2 (AV-nicking), Grad 3 (blödningar, exsudat), Grad 4 (papillödem - malign hypertoni).",
        "severity": "moderate-severe (severe vid malign hypertoni)",
        "urgency": "urgent (emergency vid malign hypertoni med papillödem)"
    },
    {
        "name": "Retinal Riss/Hål (utan avlossning)",
        "name_en": "Retinal Tear/Break (without Detachment)",
        "icd10": "H33.3",
        "symptoms": [
            "ljusblixtar (photopsia)",
            "nya eller ökade floaters",
            "ofta plötslig debut",
            "ingen synfältspåverkan ännu (viktigt skiljetecken från avlossning)",
            "normal central syn"
        ],
        "anamnesis_questions": [
            "Ser du ljusblixtar?",
            "Har du fått nya flugor eller prickar i synfältet?",
            "Har du en skugga eller gardin i synfältet? (viktigt - tecken på avlossning)",
            "Hur länge sedan började symtomen?",
            "Har du haft liknande i det andra ögat?",
            "Är du närsint?",
            "Har du haft ögontrauma?"
        ],
        "clinical_signs": [
            "retinal break eller tear synlig vid oftalmoskopi",
            "kan ha liten vitreous hemorrhage",
            "posterior vitreous detachment (PVD) vanligt",
            "ingen retinal avlossning (ännu)",
            "normalt synfält",
            "normal visus"
        ],
        "risk_factors": [
            "myopi (närsynthet)",
            "lattice degeneration",
            "posterior vitreous detachment (PVD)",
            "ögontrauma",
            "tidigare retinal tear/detachment i andra ögat",
            "familjehistoria",
            "afaki (saknad lins)",
            "ögonkirurgi (särskilt kataraktkirurgi hos yngre myoper)"
        ],
        "treatment": "AKUT profylaktisk laser photocoagulation eller kryoterapi runt break/tear för att förhindra retinal avlossning. Behandla SNART (inom 24-48 timmar) - risk för progression till retinal avlossning är hög (30-50% om obehandlad). Teknik: laser skapar ärrbildning runt hålet som förankrar retina till underliggande vävnad. Patienten bör undvika tunga lyft och Valsalva-manövrer tills laser är utförd. Uppföljning efter 1-2 veckor, sedan efter 6 veckor, sedan efter 3-6 månader. Undersök andra ögat (15-20% risk för bilaterala tears). Långtidsuppföljning vid myopi och lattice degeneration.",
        "kva": "CJF20 (laser photocoagulation retina)",
        "differential_diagnoses": [
            "posterior vitreous detachment utan tear (endast floaters/flashes)",
            "retinal avlossning (mer allvarligt - synfältsbortfall)",
            "vitreous hemorrhage"
        ],
        "description": "Retinala riss/hål är brott i retina som kan leda till retinal avlossning om de inte behandlas. U-formade tears (hästsko-tears) är vanligast och mest riskabla. Runda hål är mindre riskabla.",
        "severity": "moderate (hög risk för severe om obehandlad)",
        "urgency": "urgent (behandla inom 24-48h)"
    },
    {
        "name": "Epiretinal Membran (Makulaförveckling)",
        "name_en": "Epiretinal Membrane (Macular Pucker)",
        "icd10": "H35.3",
        "symptoms": [
            "gradvis synnedsättning",
            "förvrängd syn (metamorfopsi)",
            "centralt synfältsbortfall (om svår)",
            "dubbelbilder på ett öga (monokulär diplopi)",
            "svårighet att läsa",
            "ofta asymtomatisk vid mild membran"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft problem med synen?",
            "Ser raka linjer böjda eller vågiga?",
            "Har du svårt att läsa?",
            "Har synen försämrats gradvis eller plötsligt?",
            "Har du haft retinal avlossning eller ögonkirurgi?",
            "Märker du någon skillnad mellan ögonen?"
        ],
        "clinical_signs": [
            "skrynklig, reflekterande membran på maculaytan",
            "retinal veckning och distorsion",
            "kan ha pseudohål i macula",
            "tortuösa retinala kärl i maculaområdet",
            "OCT visar epiretinal membran och retinal förtjockning",
            "kan ha cystoid maculaödem"
        ],
        "risk_factors": [
            "idiopatisk (vanligast hos äldre)",
            "posterior vitreous detachment (PVD)",
            "retinal vein ocklusion",
            "diabetesretinopati",
            "uveit",
            "tidigare retinal avlossning eller laser",
            "ögontrauma",
            "ögonkirurgi",
            "ålder >50 år"
        ],
        "treatment": "OBSERVATION om mild och minimala symtom (många patienter behöver ingen behandling). KIRURGI (pars plana vitrektomi med membranpeeling) indikerad vid: signifikant synnedsättning (visus <0.5), besvärande metamorfopsi som påverkar ADL, progression av membran. Postoperativ återhämtning kan ta månader. Visuell prognos generellt god om behandlad i tid. Risker med kirurgi: katarakt (nästan säker hos fakaöga), retinal avlossning (1-2%), infektion. Regelbunden uppföljning med OCT för att monitorera progression. Amsler grid för hemmonitorering.",
        "kva": "CJF10 (pars plana vitrektomi)",
        "differential_diagnoses": [
            "macular hole",
            "cystoid macular edema",
            "vitreomacular traction",
            "central serös chorioretinopati"
        ],
        "description": "Epiretinal membran är en tunn, fibrövaskulär membran som växer på maculaytan och orsakar retinal veckning och distorsion. Kan vara idiopatisk (vanligast) eller sekundär till annan ögonsjukdom.",
        "severity": "mild-moderate",
        "urgency": "routine"
    }
]
