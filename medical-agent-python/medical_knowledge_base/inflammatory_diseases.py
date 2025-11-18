"""
Inflammatoriska Sjukdomar - 25 vanligaste
"""

INFLAMMATORY_DISEASES = [
    {
        "name": "Akut Anterior Uveit (Irit/Iridocyklit)",
        "name_en": "Acute Anterior Uveitis",
        "icd10": "H20.0",
        "symptoms": [
            "rött öga",
            "smärta",
            "ljuskänslighet (fotophobi)",
            "tårrinnande",
            "synnedsättning (suddig)",
            "oftast ensidig",
            "akut debut"
        ],
        "anamnesis_questions": [
            "Har du smärta i ögat?",
            "Är du ljuskänslig?",
            "Har du haft detta tidigare?",
            "Har du ryggvärk eller ledvärk (Bechterews)?",
            "Har du psoriasis eller inflammatorisk tarmsjukdom?",
            "Har du HLA-B27-positivitet?",
            "Är det bara ett öga påverkat?"
        ],
        "clinical_signs": [
            "cellreaktion i främre kammaren",
            "keratiska precipitat (KP) på hornhinneendotel",
            "flare (protein i främre kammaren)",
            "posteriora synechiae (iris fäster vid lins)",
            "miosis (liten pupill)",
            "perilimbal injektion (ciliar flush)",
            "eventuell hypopyon vid svår inflammation"
        ],
        "risk_factors": [
            "HLA-B27-positiv (50% av akut anterior uveit)",
            "Bechterews sjukdom (ankyloserande spondylit)",
            "reaktiv artrit",
            "psoriasisartrit",
            "inflammatorisk tarmsjukdom (Crohns, ulcerös kolit)",
            "juvenil idiopatisk artrit (barn)",
            "idiopatisk (50%)"
        ],
        "treatment": "Topikala steroider (prednisolon 1% var 1-2h initialt, trappa ned), cykloplegika (atropin 1% eller cyklopentolat) - förhindrar synechiae och lindrar smärta, behandla underliggande systemsjukdom, periokulärt steroidinjektion vid svår, systemiska steroider vid bilateral eller svår, uppföljning tills helt inflammationsfritt, långsam nedtrappning (risk för rebound)",
        "kva": "Ingen specifik (medicinsk behandling)",
        "differential_diagnoses": [
            "Akut trångvinkelglaukom (men högt tryck)",
            "Keratit",
            "Sklerit",
            "Akut konjunktivit (men ingen smärta/fotophobi)"
        ],
        "description": "Akut anterior uveit är inflammation i iris och ciliarkropp. Vanligaste uveitformen. Stark association med HLA-B27 och Bechterews. Recidiv vanligt (50%). Kräver aggressiv steroidbehandling och cykloplegika. God prognos vid snabb behandling.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Kronisk Anterior Uveit",
        "name_en": "Chronic Anterior Uveitis",
        "icd10": "H20.1",
        "symptoms": [
            "ofta minimal smärta (jämfört med akut)",
            "lätt rodnad eller ingen rodnad",
            "gradvis synnedsättning",
            "kan vara asymtomatisk tidigt",
            "oftast barn (JIA) eller Fuchs heterokrom"
        ],
        "anamnesis_questions": [
            "Har barnet ledvärk eller artrit?",
            "Upptäcktes detta vid rutinkontroll?",
            "Har du haft detta länge utan symptom?",
            "Är irisfärgen olika mellan ögonen?",
            "Har du juvenil idiopatisk artrit?"
        ],
        "clinical_signs": [
            "långvarig inflammation (>3 månader eller insidiös debut)",
            "ofta minimal cellreaktion",
            "bundna posteriora synechiae",
            "bandformad keratopati (hos barn)",
            "katarakt (komplikation)",
            "cystoid maculaödem (vanlig komplikation)",
            "vid JIA: ofta bilateral, white quiet eye"
        ],
        "risk_factors": [
            "juvenil idiopatisk artrit (JIA) - särskilt oligoartikulär, ANA-positiv, flickor",
            "Fuchs heterokrom iridocyklit",
            "sarkoidos",
            "syfilis",
            "tuberkulos"
        ],
        "treatment": "Topikala steroider (ofta långvarigt), cykloplegika, behandla komplikationer (CME, katarakt, glaukom, bandformad keratopati), vid JIA: aggressiv behandling, ofta systemisk immunosuppression (MTX, adalimumab/biologiska), screening av JIA-patienter kritisk (var 3-6 mån), behandling av underliggande orsak",
        "kva": "Varierar",
        "differential_diagnoses": [
            "Akut anterior uveit (mer symptom)",
            "Fuchs heterokrom iridocyklit (särskild form)",
            "Posner-Schlossman syndrom"
        ],
        "description": "Kronisk anterior uveit är långvarig eller insidiöst debuterande inflammation. JIA-associerad uveit är särskilt viktig - ofta asymtomatisk 'white quiet eye' men kan ge blindhet. Kräver screening av JIA-barn. Komplikationer vanliga: CME, katarakt, glaukom, bandformad keratopati.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Intermediär Uveit (Pars Planitis)",
        "name_en": "Intermediate Uveitis",
        "icd10": "H20.1",
        "symptoms": [
            "flygers (flytande fläckar)",
            "suddig syn",
            "oftast bilateral",
            "minimal smärta",
            "gradvis debut",
            "ofta unga vuxna"
        ],
        "anamnesis_questions": [
            "Ser du flygers eller svarta fläckar?",
            "Är synen suddig?",
            "Påverkas båda ögonen?",
            "Har du multipel skleros?",
            "Har du sarkoidos eller Lyme?",
            "Är du ung vuxen (20-40 år)?"
        ],
        "clinical_signs": [
            "vitrit (celler i glaskroppen)",
            "'snowballs' i inferiora glaskroppen",
            "'snowbanking' på pars plana",
            "periphlebit (venomhöljning)",
            "cystoid maculaödem (CME) vanlig komplikation",
            "minimal främre kammarreaktion",
            "eventuell papillödem"
        ],
        "risk_factors": [
            "idiopatisk (80% - då kallas pars planitis)",
            "multipel skleros",
            "sarkoidos",
            "Lyme disease",
            "syfilis",
            "HTLV-1",
            "ålder 20-40 år"
        ],
        "treatment": "Observation om asymtomatisk och ingen CME, periokulärt steroidinjektion vid CME, systemiska steroider vid bilateral eller svår, immunosuppression (MTX, mykofenolatmofetil, azathioprin) vid kronisk, biologiska läkemedel (adalimumab) vid refraktär, vitrektomi vid tät vitrit eller epiretinal membran, behandla underliggande orsak (MS, sarkoidos)",
        "kva": "CJE20 (vitrektomi vid behov)",
        "differential_diagnoses": [
            "Posterior uveit",
            "Endoftalmit (men mer akut)",
            "Vitreous blödning",
            "Primär intraokulär lymfom (masquerade)"
        ],
        "description": "Intermediär uveit är inflammation främst i glaskroppen och pars plana. 'Pars planitis' när idiopatisk. Karakteristiska snowballs och snowbanking. CME är vanligaste komplikation. Ofta behövs systemisk immunosuppression. God prognos med behandling.",
        "severity": "moderate",
        "urgency": "routine-urgent"
    },
    {
        "name": "Toxoplasma Retinokoroidit",
        "name_en": "Toxoplasma Retinochoroiditis",
        "icd10": "B58.0",
        "symptoms": [
            "suddig syn",
            "flygers",
            "fotopsi (ljusblixtar)",
            "synfältsbortfall",
            "oftast ensidig",
            "kan ha minimal smärta"
        ],
        "anamnesis_questions": [
            "Har du katter eller hanterar du kattlåda?",
            "Äter du rått/otillräckligt tillagat kött?",
            "Har du haft detta tidigare? (recidiv vanligt)",
            "Har du HIV eller immunsuppression?",
            "Var det vitt ärr i ögat tidigare?"
        ],
        "clinical_signs": [
            "vit, fluffig focal retinokoroidit (aktiv lesion)",
            "ofta intill gammalt pigmenterat ärr ('headlight in the fog')",
            "vitrit (kraftig)",
            "papillitis möjlig",
            "vaskulit",
            "läker med pigmenterat ärr",
            "kan vara bilateralt vid kongenital"
        ],
        "risk_factors": [
            "kattexponering",
            "konsumtion av rått kött",
            "kongenital toxoplasma (om gravid smittad)",
            "immunsuppression (HIV, transplantation)",
            "odlade toxoplasma-cystor i retina (reactiveras)"
        ],
        "treatment": "Behandla om: makula hotad, papill involverad, stor lesion, svår vitrit, Klassisk trippelterapi: pyrimethamin + sulfadiazin + folininsyra i 4-6 veckor, Alternativ: trimetoprim-sulfametoxazol (Bactrim), azithromycin + pyrimethamin, clindamycin + pyrimethamin, Steroider ENDAST tillsammans med antibiotika (aldrig ensamt!), ofta självläkande hos immunokompetenta om perifer lesion",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Cytomegalovirus (CMV) retinit (hos HIV)",
            "Akut retinal nekros (ARN)",
            "Endoftalmit",
            "Sarkoidos"
        ],
        "description": "Toxoplasma är vanligaste posterior uveit i Sverige. Oftast reaktivering av kongenitalt förvärvad infektion. Karakteristisk 'headlight in fog' med lesion intill gammalt ärr. Recidiv vanligt. Behandling endast vid hotande makula/papill eller svår inflammation.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Sarkoidos-Uveit",
        "name_en": "Sarcoid Uveitis",
        "icd10": "D86.8",
        "symptoms": [
            "suddig syn",
            "flygers",
            "variabel smärta/rodnad",
            "kan vara anterior, intermediär, posterior eller panuveit",
            "ofta bilateral",
            "systemiska symptom (trötthet, feber, hosta)"
        ],
        "anamnesis_questions": [
            "Har du sarkoidos diagnosticerad?",
            "Har du andningsproblem eller hosta?",
            "Har du hudförändringar (erythema nodosum)?",
            "Har du trötthet eller viktförlust?",
            "Har du högt kalcium?",
            "Påverkas båda ögonen?"
        ],
        "clinical_signs": [
            "granulomatös inflammation (mutton-fat KP)",
            "iris noduler (Koeppe, Busacca)",
            "periphlebit ('candle-wax drippings')",
            "chorioretinala lesioner",
            "cystoid maculaödem",
            "optikusneuropati möjlig",
            "kan påverka alla delar av ögat"
        ],
        "risk_factors": [
            "sarkoidos (systemisk sjukdom)",
            "afrikanskt eller skandinaviskt ursprung",
            "kvinnligt kön",
            "ålder 20-40 år",
            "hereditet"
        ],
        "treatment": "Topikala steroider vid främst anterior uveit, systemiska steroider (prednison) vid posterior/intermediär/svår, immunosuppression (MTX, mykofenolatmofetil, azathioprin) ofta behövs som steroid-sparande, biologiska (adalimumab, infliximab) vid refraktär, behandla systemisk sarkoidos, samarbete med lungläkare, långvarig behandling ofta nödvändig",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Tuberkulos (liknande granulomatös bild)",
            "Syfilis",
            "Toxoplasma",
            "Multipel skleros (vid intermediär uveit)"
        ],
        "description": "Sarkoidos kan ge alla former av uveit. Granulomatös inflammation karakteristisk. 'Candle-wax drippings' periphlebit typiskt. Ofta bilateral. Kräver systemisk behandling. Samarbete med lungläkare viktigt. God prognos med behandling men ofta kroniskt förlopp.",
        "severity": "moderate-severe",
        "urgency": "urgent"
    },
    {
        "name": "Behçets Sjukdom med Uveit",
        "name_en": "Behçet's Disease with Uveitis",
        "icd10": "M35.2",
        "symptoms": [
            "recidiverande uveit",
            "kraftig synnedsättning",
            "smärta",
            "rodnad",
            "hypopyon vanligt",
            "systemiska symptom (munsår, genitala sår)"
        ],
        "anamnesis_questions": [
            "Har du återkommande munsår (aftösa sår)?",
            "Har du genitala sår?",
            "Har du hudproblem (erythema nodosum, acne)?",
            "Har du ledvärk?",
            "Har du haft återkommande ögoninflamationer?",
            "Är du från Mellanöstern, Medelhavsområdet eller Asien?",
            "Har du blodpropp haft (venös trombos)?"
        ],
        "clinical_signs": [
            "bilateral recidiverande panuveit",
            "hypopyon (pus i främre kammaren) - typiskt!",
            "retinal vaskulit (occlusiv)",
            "retinit",
            "vitrit",
            "papillitis",
            "kan ge retinal ischemi och neovaskulationer"
        ],
        "risk_factors": [
            "Behçets sjukdom (systemisk)",
            "HLA-B51-positiv",
            "manligt kön (värre prognos)",
            "ursprung från 'Silk Road' (Turkiet, Iran, Japan, Medelhavet)",
            "ålder 20-40 år vid debut"
        ],
        "treatment": "Systemisk behandling ESSENTIELL: höga doser systemiska steroider, immunosuppression (azathioprin, cyclosporin, mykofenolatmofetil), biologiska läkemedel (adalimumab, infliximab, interferon-alfa) - ofta förstahandsval nu, intravitreal anti-VEGF vid maculaödem, colchicin för systemiska manifestationer, topikala steroider + cykloplegika för anterior uveit, aggressiv behandling kritisk - risk för blindhet hög",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "HLA-B27-uveit (men annat mönster)",
            "Sarkoidos",
            "Syfilis",
            "Tuberkulös uveit"
        ],
        "description": "Behçets är en systemisk vaskulit med svår, recidiverande uveit. Hypopyon och retinal vaskulit karakteristiskt. Vanligast längs 'Silk Road'. Mycket dålig prognos utan behandling - 25% blir blinda. Kräver aggressiv systemisk immunosuppression. Biologiska läkemedel har förbättrat prognos avsevärt.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Sklerit - Anterior Diffus",
        "name_en": "Anterior Diffuse Scleritis",
        "icd10": "H15.0",
        "symptoms": [
            "kraftig ögonsmärta (djup, molande)",
            "smärta strålar ut till kind, käke, huvudet",
            "värre på natten",
            "rodnad (djupt röd, blålila)",
            "tårrinnande",
            "ljuskänslighet",
            "synnedsättning"
        ],
        "anamnesis_questions": [
            "Har du djup, molande smärta?",
            "Strålar smärtan ut till ansiktet?",
            "Är smärtan värre på natten?",
            "Väcktes du av smärtan?",
            "Har du reumatoid artrit eller annan autoimmun sjukdom?",
            "Har du Wegeners granulomatos (GPA)?",
            "Hjälper vanliga smärtstillande?"
        ],
        "clinical_signs": [
            "djup skleral inflammation",
            "djupt röd, blålila färg (vs ljusröd vid episklerit)",
            "scleral ödem",
            "dilaterade djupa episkleral kärl",
            "fenylefrin-test negativ (kärl bleknar ej - djupa kärl)",
            "kan ha anterior uveit samtidigt",
            "eventuell corneal involvement (sclerosing keratitis)"
        ],
        "risk_factors": [
            "reumatoid artrit (vanligaste - 40%)",
            "Wegeners granulomatos (GPA)",
            "polyarteritis nodosa",
            "SLE",
            "relapsing polychondritis",
            "inflammatorisk tarmsjukdom",
            "kvinnligt kön",
            "ålder 40-60 år"
        ],
        "treatment": "Systemiska NSAIDs (hög dos) vid mild, systemiska steroider (prednison 1mg/kg) vid måttlig-svår, immunosuppression (MTX, mykofenolatmofetil, cyclophosphamid) ofta behövs, biologiska (rituximab, infliximab) vid refraktär eller nekrotiserande, topikala steroider som tillägg, behandla underliggande autoimmun sjukdom, ALDRIG topikala NSAIDs ensamt (otillräckligt), samarbete med reumatolog",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Episklerit (lindrigare, ytlig, ingen smärta)",
            "Konjunktivit (ingen smärta)",
            "Anterior uveit (annan rodnadsmönster)"
        ],
        "description": "Sklerit är allvarlig inflammation av sklera, ofta associerad med systemisk autoimmun sjukdom. Kraftig molande smärta karakteristisk. Risk för skleral förtunning och perforation. Kräver systemisk behandling. Utred alltid för underliggande systemsjukdom (särskilt RA, GPA).",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Nekrotiserande Sklerit",
        "name_en": "Necrotizing Scleritis",
        "icd10": "H15.0",
        "symptoms": [
            "mycket kraftig smärta",
            "kraftig synnedsättning",
            "rodnad",
            "ofta historia av autoimmun sjukdom",
            "systemiska symptom (feber, viktnedgång)"
        ],
        "anamnesis_questions": [
            "Har du olidlig smärta?",
            "Har du reumatoid artrit?",
            "Har du Wegeners granulomatos?",
            "Har skleran blivit tunnare?",
            "Kan du se mörkare vävnad under sklera?"
        ],
        "clinical_signs": [
            "skleral nekros med sequester",
            "skleral förtunning",
            "uvea synligt genom tunn sklera (blå-grå)",
            "avaskulära områden",
            "perforation möjlig (scleromalacia perforans)",
            "ofta associerad anterior uveit och keratit",
            "ibland minimal inflammation (scleromalacia perforans)"
        ],
        "risk_factors": [
            "reumatoid artrit (särskilt långvarig, seropositiv)",
            "Wegeners granulomatos (GPA)",
            "polyarteritis nodosa",
            "relapsing polychondritis",
            "systemisk vaskulit"
        ],
        "treatment": "MYCKET AGGRESSIV behandling nödvändig: höga doser systemiska steroider IV, immunosuppression (cyclophosphamid traditionellt), biologiska läkemedel (rituximab förstahandsval vid GPA), mykofenolatmofetil eller MTX, skleral patch graft vid perforation eller hotande perforation, behandla underliggande vaskulit aggressivt, samarbete med reumatolog kritiskt, prognos allvarlig - hög mortalitet utan behandling (systemisk vaskulit)",
        "kva": "Skleral patch graft vid perforation",
        "differential_diagnoses": [
            "Infektiös sklerit (sällsynt)",
            "Anterior diffus sklerit (lindrigare)",
            "Skleral neoplasm"
        ],
        "description": "Nekrotiserande sklerit är livshotande tillstånd med skleral nekros. Associerad med systemisk vaskulit. Risk för perforation och synförlust. Hög systemisk mortalitet (25% 5-års mortalitet utan behandling). Kräver akut aggressiv immunosuppression. Oftast RA eller Wegeners.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Episklerit",
        "name_en": "Episcleritis",
        "icd10": "H15.1",
        "symptoms": [
            "lätt till måttlig rodnad",
            "minimal eller ingen smärta",
            "lätt obehag eller brännande känsla",
            "oftast ensidig",
            "kan vara sektoriell",
            "självläkande"
        ],
        "anamnesis_questions": [
            "Har du smärta? (oftast nej eller minimal)",
            "Kommer rödheten och går spontant?",
            "Har du haft detta tidigare?",
            "Har du autoimmun sjukdom?",
            "Påverkas synen? (oftast nej)"
        ],
        "clinical_signs": [
            "lokal eller diffus rodnad",
            "ytlig inflammation (episklerala kärl)",
            "ljusröd färg (vs blålila vid sklerit)",
            "fenylefrin 2.5% bleknar kärl (skillnad från sklerit)",
            "ingen skleral ödem eller förtunning",
            "ingen uveit",
            "två typer: simple (diffus) eller nodular"
        ],
        "risk_factors": [
            "oftast idiopatisk (70%)",
            "kan associeras med: reumatoid artrit, inflammatorisk tarmsjukdom, gikt, rosacea",
            "recidiv vanligt",
            "kvinnor något vanligare"
        ],
        "treatment": "Observation (självläkande på 1-3 veckor), artificiella tårar för comfort, kalla kompresser, topikala NSAIDs (ketorolac, diclofenac) vid besvärande symptom, topikala svaga steroider ibland (oftast ej nödvändigt), orala NSAIDs vid recidiverande eller bilateral, uteslut sklerit!, ingen systemisk behandling behövs vanligtvis, god prognos - inga komplikationer",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Sklerit (djup smärta, blålila, fenylefrin-negativ)",
            "Konjunktivit (ytligare, sekretion)",
            "Subkonjunktival blödning (ingen inflammation)"
        ],
        "description": "Episklerit är benign, självläkande inflammation av episklera. Minimal smärta (viktigt skiljetecken från sklerit). Fenylefrin-test positiv. Ofta idiopatisk. Självläkande. Uteslut sklerit viktigt! God prognos utan komplikationer.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Bakteriell Konjunktivit",
        "name_en": "Bacterial Conjunctivitis",
        "icd10": "H10.0",
        "symptoms": [
            "rött öga",
            "purulent sekretion (gul-grön)",
            "ihopklistrade ögonlock på morgonen",
            "främmande kropps-känsla",
            "minimal ljuskänslighet",
            "ingen eller lätt synpåverkan",
            "kan vara bilateral"
        ],
        "anamnesis_questions": [
            "Har du gul-grön flytning?",
            "Klistras ögonlocken ihop på morgonen?",
            "Smittas det lätt? (barn på dagis, familjemedlemmar)",
            "Har du smärta? (oftast nej)",
            "Använder du kontaktlinser?",
            "Är synen påverkad? (oftast nej)"
        ],
        "clinical_signs": [
            "konjunktival hyperemi (diffus rodnad)",
            "purulent eller mukopurulent sekretion",
            "papillär reaktion i konjunktiva",
            "inga korneal infiltrat (normalt)",
            "ingen anterior uveit",
            "vanliga bakterier: Staphylococcus, Streptococcus, Haemophilus (barn), Moraxella"
        ],
        "risk_factors": [
            "barn (dagis, skola)",
            "kontaktlinsbärare",
            "otillräcklig handhygien",
            "torrt öga",
            "dakryostenoos (barn)"
        ],
        "treatment": "Oftast självläkande på 7-10 dagar utan behandling, antibiotika-ögondroppar förkortar förlopp och minskar smittsamhet: chloramphenicol, fusidinsyra, fluorokinoloner (ofloxacin, moxifloxacin), 4x dagligen i 5-7 dagar, god handhygien!, byt ut smink och kontaktlinser, hyperakut form (Neisseria gonorrhoeae): systemiska antibiotika (ceftriaxone), uteslut gonorré och klamydia vid neonatal konjunktivit",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Viral konjunktivit (vattnig sekretion)",
            "Allergisk konjunktivit (klåda dominant)",
            "Keratit (smärta, ljuskänslighet, synpåverkan)"
        ],
        "description": "Bakteriell konjunktivit är vanlig, självläkande infektion. Purulent sekretion karakteristisk. Antibiotika förkortar förlopp men ej essentiellt. God handhygien viktigt. Uteslut keratit (ingen korneal involvering vid ren konjunktivit).",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Viral Konjunktivit (Adenoviral)",
        "name_en": "Viral Conjunctivitis (Adenoviral)",
        "icd10": "B30.0",
        "symptoms": [
            "rött öga",
            "vattnig sekretion",
            "främmande kropps-känsla",
            "ljuskänslighet (om korneal involvering)",
            "ofta bilateral (ena ögat först)",
            "mycket smittsamt",
            "kan ha övre luftvägsinfektion"
        ],
        "anamnesis_questions": [
            "Har du vattnig flytning?",
            "Började det i ett öga och spred sig till det andra?",
            "Har du haft förkylning nyligen?",
            "Har andra i familjen/arbetet fått samma?",
            "Har du ljuskänslighet? (tyder på korneal involvering)",
            "Har du svullna lymfkörtlar framför örat?"
        ],
        "clinical_signs": [
            "konjunktival hyperemi och ödem (chemosis)",
            "vattnig sekretion",
            "folliklar i nedre fornix",
            "preaurikulär lymfadenopati",
            "subkonjunktivala blödningar möjliga",
            "pseudomembran möjligt vid svår",
            "efter 5-7 dagar: subepitelial infiltrat på kornea (kan ge ljuskänslighet och sämre syn)",
            "EKC (epidemic keratoconjunctivitis) vid serotöyp 8, 19, 37"
        ],
        "risk_factors": [
            "exponering för smittad person",
            "otillräcklig handhygien",
            "ögonkliniker (sjukvårdspersonal)",
            "dagis, skola",
            "sommar-höst (mer vanligt)"
        ],
        "treatment": "Ingen specifik antiviral behandling, självläkande på 2-3 veckor, stödjande: kalla kompresser, artificiella tårar, eventuellt topikala antihistaminer för comfort, vid subepiteliala infiltrat: svaga steroider (FML) kan användas för symptom men INTE rutin, förhindra spridning: handtvätt!, separata handdukar, stanna hemma från jobb/skola 2 veckor, steroider förkortar ej sjukdomstid och kan förlänga viral shedding, povidon-jod 1.0% kan ha viss antiviral effekt",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Bakteriell konjunktivit (purulent sekretion)",
            "Allergisk konjunktivit (klåda, bilateral)",
            "Keratit (mer smärta och synpåverkan)"
        ],
        "description": "Adenoviral konjunktivit är mycket smittsam viral infektion. 'Ögoninflammation på sommaren'. Vattnig sekretion, folliklar, preaurikulära lymfkörtlar karakteristiskt. Subepitelial infiltrat efter 1 vecka kan ge långvariga symptom. Självläkande men mycket smittsamt - god handhygien!",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Allergisk Konjunktivit (Säsongsbunden)",
        "name_en": "Seasonal Allergic Conjunctivitis",
        "icd10": "H10.1",
        "symptoms": [
            "KLÅDA (dominerande symptom)",
            "rodnad",
            "tårrinnande (vattnig)",
            "bilateral",
            "säsongsbunden (vår-sommar)",
            "ofta samtidig rinit",
            "ingen synpåverkan"
        ],
        "anamnesis_questions": [
            "Kliar ögonen? (viktigt!)",
            "Kommer symptomen vissa årstider (pollen)?",
            "Har du hösnuva eller astma?",
            "Påverkas båda ögonen?",
            "Har du allergi mot pollen, damm eller pälsdjur?",
            "Förbättras det inomhus eller med antihistamin?"
        ],
        "clinical_signs": [
            "bilateral konjunktival hyperemi",
            "chemosis (konjunktival ödem)",
            "papillär reaktion (mjölkaktig konjunktiva)",
            "vattnig sekretion",
            "ingen purulent sekretion",
            "ingen korneal involvering"
        ],
        "risk_factors": [
            "atopi",
            "allergi (pollen, damm, djur)",
            "säsong (vår-sommar för pollen)",
            "hereditet",
            "astma, eksem"
        ],
        "treatment": "Undvik allergen om möjligt, kalla kompresser, artificiella tårar (spola bort allergener), topikala antihistaminer (olopatadin, ketotifen) 2x dagligen - mycket effektivt, topikala mastcellstabilisatorer (natriumkromoglikat) - profylax, kombination antihistamin + mastcellstabilisator (olopatadin), orala antihistaminer vid systemiska symptom, topikala steroider ENDAST vid svår och kortvarigt (FML), immunterapi (desensibilisering) vid svår",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Viral konjunktivit (ingen klåda)",
            "Bakteriell konjunktivit (purulent)",
            "Torrt öga (mer brännande än klåda)",
            "VKC/AKC (mer kronisk, svår)"
        ],
        "description": "Säsongsbunden allergisk konjunktivit ('hösnuva i ögonen') är IgE-medierad överkänslighet mot pollen. KLÅDA är nyckelsymptom. Bilateral, säsongsbunden. Topikala antihistaminer mycket effektiva. God prognos. Ingen komplikation.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Vernal Keratokonjunktivit (VKC)",
        "name_en": "Vernal Keratoconjunctivitis",
        "icd10": "H10.4",
        "symptoms": [
            "kraftig klåda",
            "ljuskänslighet",
            "tårrinnande",
            "främmande kropps-känsla",
            "synnedsättning (vid korneal involvering)",
            "trådiga mukus-sekretion",
            "barn/unga män",
            "säsongsbunden initialt, sedan året runt"
        ],
        "anamnesis_questions": [
            "Hur gammal är patienten? (barn/ungdom)",
            "Kraftig klåda?",
            "Är det värre på våren/sommaren?",
            "Har du atopi eller allergi?",
            "Bor du i varmt klimat?",
            "Ser du trådiga sekretion?"
        ],
        "clinical_signs": [
            "jätte papiller på övre tarsala konjunktiva ('cobblestone')",
            "limbal form: Horner-Trantas dots (eosinofila aggregat vid limbus)",
            "tjock, trådiga mukussekretion",
            "korneal involvering: shield ulcer (sterilt sår), superficiell keratit",
            "bilateral",
            "ptosis vid svår (tung övre lock)"
        ],
        "risk_factors": [
            "barn och unga (5-20 år)",
            "manligt kön (3:1)",
            "atopi",
            "varmt, torrt klimat",
            "hereditet"
        ],
        "treatment": "Topikala mastcellstabilisatorer (lodoxamid 4x dagligen), topikala antihistaminer (olopatadin 2x dagligen), kalla kompresser, topikala steroider vid svår (flumethalon FML eller loteprednol), topikalt cyclosporin A 0.05-2% eller tacrolimus - steroid-sparande, systemiska antihistaminer, supratarsal steroidinjektion vid svår papiller, skrapa papiller (debulking) vid massiva, behandla shield ulcer aggressivt (lubricering, bandagelinser, tacrolimus), oftast självläkande i vuxen ålder (efter puberteten)",
        "kva": "Ingen vanligtvis",
        "differential_diagnoses": [
            "Atopisk keratokonjunktivit (AKC - vuxna)",
            "Jätte papillär konjunktivit (GPC - kontaktlinser)",
            "Säsongsbunden allergisk konjunktivit (lindrigare)"
        ],
        "description": "VKC är svår allergisk ögonsjukdom hos barn/ungdomar i varmt klimat. Jätte papiller och shield ulcer karakteristiskt. Kan ge permanent synnedsättning. Kräver aggressiv behandling. Cyclosporin/tacrolimus steroid-sparande. Oftast självläkande efter puberteten.",
        "severity": "moderate-severe",
        "urgency": "urgent (vid shield ulcer)"
    },
    {
        "name": "Atopisk Keratokonjunktivit (AKC)",
        "name_en": "Atopic Keratoconjunctivitis",
        "icd10": "H10.1",
        "symptoms": [
            "kraftig klåda",
            "ljuskänslighet",
            "tårrinnande",
            "synnedsättning",
            "året runt symptom",
            "vuxna med atopisk dermatit",
            "kroniskt förlopp"
        ],
        "anamnesis_questions": [
            "Har du atopiskt eksem?",
            "Har du astma?",
            "Kliar det kraftigt året runt?",
            "Har du hudförändringar runt ögonen?",
            "Har synen försämrats gradvis?"
        ],
        "clinical_signs": [
            "papillär reaktion på tarsala konjunktiva",
            "konjunktival scarring och symblepharon",
            "limbal fibros",
            "korneal neovaskularisation",
            "korneal scarring",
            "shield ulcer",
            "blepharit",
            "ektropion/entropion",
            "katarakt (posterior subkapsulär)",
            "keratokonus association"
        ],
        "risk_factors": [
            "atopisk dermatit (svår)",
            "vuxen ålder (jämfört med VKC)",
            "atopisk hereditet",
            "astma, hösnuva"
        ],
        "treatment": "Topikala antihistaminer + mastcellstabilisatorer, topikalt cyclosporin A eller tacrolimus (förstahandsval för kronisk), topikala steroider vid exacerbation (kortvarigt), behandla blepharit (ögonlockshygien), behandla atopisk dermatit (minskar ögongnuggning), behandla komplikationer: shield ulcer (lubricering, tacrolimus, bandagelinser), katarakt (kirurgi), limbal stammcellsbrist (transplantation), kornealtransplantation vid scarring, långvarig uppföljning nödvändig",
        "kva": "Varierar beroende på komplikation",
        "differential_diagnoses": [
            "VKC (barn/ungdomar)",
            "Kronisk blepharit",
            "Rosacea-relaterad keratokonjunktivit"
        ],
        "description": "AKC är kronisk svår allergisk ögonsjukdom hos vuxna med atopisk dermatit. Risk för permanenta komplikationer: korneal scarring, katarakt, limbal stammcellsbrist. Kräver långvarig behandling. Cyclosporin/tacrolimus viktigt. Behandla samtidig hudsjukdom.",
        "severity": "severe",
        "urgency": "urgent"
    },
    {
        "name": "Jätte Papillär Konjunktivit (GPC)",
        "name_en": "Giant Papillary Conjunctivitis",
        "icd10": "H10.4",
        "symptoms": [
            "klåda (särskilt vid avlägsnande av linser)",
            "mukussekretion",
            "främmande kropps-känsla",
            "kontaktlinser 'rör sig' eller faller ut",
            "nedsatt linsbärartid",
            "suddig syn med linser"
        ],
        "anamnesis_questions": [
            "Använder du kontaktlinser?",
            "Vilken typ? (mjuka linser vanligast)",
            "Hur länge per dag bär du dem?",
            "Byter du dem regelbundet?",
            "Känns linserna obekväma?",
            "Har du mukus på linserna?",
            "Har du protesögat eller exponerade suturer?"
        ],
        "clinical_signs": [
            "jätte papiller (>0.3mm) på övre tarsala konjunktiva",
            "mukussekretion och coating på linser",
            "mild konjunktival hyperemi",
            "kan ha korneal scarring vid svår",
            "förbättras när linsbärande upphör"
        ],
        "risk_factors": [
            "kontaktlinsbärare (särskilt mjuka linser)",
            "långvarig linsbärande",
            "dålig lensrengöring",
            "proteindepositioner på linser",
            "exponerade suturer efter kirurgi",
            "protesögat (okulärt protes)"
        ],
        "treatment": "Sluta med kontaktlinser (minst 1 månad), topikala mastcellstabilisatorer (lodoxamid, nedocromil), topikala antihistaminer, byte till daglinser när återupptar (minsta proteindeposition), byte till RGP-linser (bättre än mjuka), förbättrad lenshygien, eventuellt topikala steroider kortvarigt vid svår, ta bort exponerade suturer om tillämpligt, god prognos när linsbärande upphör",
        "kva": "Ingen",
        "differential_diagnoses": [
            "VKC (barn, ej linsbärare)",
            "AKC (atopiker, kronisk)",
            "Normal papillär reaktion (mindre papiller)"
        ],
        "description": "GPC är mekanisk och allergisk reaktion mot kontaktlinser eller främmande material. Jätte papiller på övre tarsala konjunktiva. Vanligast hos mjuka linsbärare. Behandling: upphör linsbärande, byte till daglinser. God prognos.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Blepharit - Anterior (Stafylokock)",
        "name_en": "Anterior Blepharitis",
        "icd10": "H01.0",
        "symptoms": [
            "klåda och irritation i ögonlock",
            "brännande känsla",
            "fjällande ögonlock",
            "rodnade ögonlockskanter",
            "torra ögon",
            "ofta värre på morgonen",
            "kroniska symptom"
        ],
        "anamnesis_questions": [
            "Kliar ögonlocken?",
            "Har du fjäll på ögonfransarna?",
            "Har du rött på ögonlockskanten?",
            "Har du haft detta länge?",
            "Har du seborré eller mjäll?",
            "Faller ögonfransar av?"
        ],
        "clinical_signs": [
            "rodnade ögonlockskanter",
            "fjäll (scales) runt fransbas (seborrheic) eller",
            "hårda krusts (stafylokock)",
            "madarosis (fransförlust)",
            "poliosis (vita fransar)",
            "trichiasis möjlig",
            "konjunktival injektion",
            "eventuella korneal infiltrat (marginala)"
        ],
        "risk_factors": [
            "seborroisk dermatit",
            "rosacea",
            "torrt öga",
            "Staphylococcus aureus kolonisering",
            "dålig ögonlockshygien",
            "Demodex-kvalster"
        ],
        "treatment": "Ögonlockshygien (viktigast!): varma kompresser 5-10 min 2x dagligen, massage av ögonlock, rengöring med mild schampo eller ögonlocksskum, antibiotisk salva (fusidinsyra, bacitracin) till ögonlockskant nattetid, vid svår: oral doxycyklin 50-100mg dagligen (anti-inflammatorisk dos), behandla seborré och rosacea, artificiella tårar för torrt öga, tea tree oil för Demodex (om misstänkt), kronisk sjukdom - långvarig behandling",
        "kva": "Ingen",
        "differential_diagnoses": [
            "Posterior blepharit (MGD)",
            "Seborroisk dermatit",
            "Demodex blepharit",
            "Ögonlockstumör (om asymmetrisk)"
        ],
        "description": "Anterior blepharit är kronisk inflammation av ögonlockskanter. Stafylokock eller seborroisk typ. Ögonlockshygien är grundpelare i behandling. Ofta associerad med torrt öga. Kronisk sjukdom som kräver långvarig behandling.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Blepharit - Posterior (Meibomian Gland Dysfunction)",
        "name_en": "Posterior Blepharitis (MGD)",
        "icd10": "H01.0",
        "symptoms": [
            "torra, brännande ögon",
            "variabel suddig syn",
            "irritation",
            "fremmat ögonlock på morgonen",
            "svårt bära kontaktlinser",
            "rodnade ögonlockskanter"
        ],
        "anamnesis_questions": [
            "Känner dina ögon torra och brännande?",
            "Är synen suddig som varierar?",
            "Har du rosacea?",
            "Ser du olja/vax på ögonlockskanten?",
            "Har du tappade meibomkörtlar?"
        ],
        "clinical_signs": [
            "täppta meibomkörtlar (inspissated)",
            "abnorm meibum (tjock, tandkrämsliknande eller ingen sekretion)",
            "rodnade, rundade ögonlockskanter",
            "dilated meibomkörtelorifices",
            "meibomkörtelatrofi (dropout på meibografi)",
            "skummig tårfilm",
            "teleangiektasi vid ögonlockskant",
            "korneal färgning vid torrt öga"
        ],
        "risk_factors": [
            "rosacea",
            "seborroisk dermatit",
            "hög ålder",
            "långvarig kontaktlinsanvändning",
            "isotretinoin (Roaccutan) användning",
            "menopaus",
            "asiatiskt ursprung"
        ],
        "treatment": "Ögonlockshygien (essentiellt): varma kompresser 10-15 min 2x dagligen (smälter meibum), ögonlocksmassage (tömma körtlar), ögonlocksrengöring, Omega-3 tillskott (EPA/DHA 1000-2000mg dagligen), oral doxycyklin 50-100mg dagligen i 3-6 månader, artificiella tårar (konserveringsfria), behandla rosacea (dermatolog), Intense Pulsed Light (IPL) terapi vid refraktär, LipiFlow/TearCare (termisk pulsation) vid svår, kronisk sjukdom - livslång behandling",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Anterior blepharit",
            "Torrt öga (överlappande)",
            "Chalazion/hordeolum (akuta former)"
        ],
        "description": "MGD är vanligaste orsaken till evaporativt torrt öga. Täppta meibomkörtlar leder till abnorm lipidsekretion. Starkt associerad med rosacea. Varma kompresser + massage + omega-3 är grundpelare. Doxycyklin effektivt. Kronisk sjukdom.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Dakryocystit - Akut",
        "name_en": "Acute Dacryocystitis",
        "icd10": "H04.3",
        "symptoms": [
            "smärtsam svullnad medialt vid nedre ögonlock",
            "rodnad",
            "tårrinnande",
            "purulent flytning från tårpunkten vid tryck",
            "feber möjlig",
            "ensidig"
        ],
        "anamnesis_questions": [
            "Har du svullnad vid näsan nära ögat?",
            "Gör det ont när du trycker där?",
            "Kommer det var/pus från ögat?",
            "Har du haft tårvägsstenosering tidigare?",
            "Rinner tårar ofta?",
            "Har du feber?"
        ],
        "clinical_signs": [
            "ömöm svullnad över tårsäcken (medialt nedre ögonlock)",
            "rodnad och ödem",
            "pus kan tryckas ut från tårpunkten",
            "epifora (tårrinnande)",
            "preseptal cellulitis möjlig",
            "preaurikulär lymfadenopati möjlig",
            "feber vid svår"
        ],
        "risk_factors": [
            "tårvägsstenosering (nasolakrimala kanalen)",
            "kronisk dakryocystit",
            "tidigare tårvägskirurgi",
            "trauma",
            "dacryolitiasis (sten i tårsäck)",
            "tumör (sällsynt)",
            "bakterier: Staphylococcus, Streptococcus"
        ],
        "treatment": "Systemiska antibiotika (viktigt!): amoxicillin-clavulanat eller cefalosporin eller clindamycin, 7-10 dagar, värme/varma kompresser, smärtlindring (paracetamol, NSAIDs), UNDVIK massage/tryck vid akut (risk för spridning), incision och dränage om abscess, efter akut fas lugnat sig: DCR (dacryocystorhinostomi) för att åtgärda underliggande stenosering, förebyggande: behandla kronisk tårsäcksinflammation",
        "kva": "CDH00 (DCR - senare)",
        "differential_diagnoses": [
            "Preseptal/orbital cellulitis",
            "Etmoidit",
            "Dermoid cysta",
            "Hordeolum/chalazion (men annat läge)"
        ],
        "description": "Akut dakryocystit är bakteriell infektion i tårsäcken sekundärt till nasolakrimala stenosering. Smärtsam svullnad medialt. Pus kan tryckas ut från tårpunkt. Kräver systemiska antibiotika. Efter akut fas: DCR för att åtgärda stenosering.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Hordeolum (Vagel)",
        "name_en": "Hordeolum (Stye)",
        "icd10": "H00.0",
        "symptoms": [
            "smärtsam svullnad i ögonlock",
            "rodnad",
            "ömmhet",
            "lokaliserad puck",
            "eventuellt pus-huvud",
            "akut debut"
        ],
        "anamnesis_questions": [
            "Har du en smärtsam puck i ögonlocket?",
            "Kom den plötsligt?",
            "Ser du gult pus-huvud?",
            "Är det på ögonlockskanten (externt) eller insidan (internt)?",
            "Har du haft detta tidigare?",
            "Har du blepharit eller rosacea?"
        ],
        "clinical_signs": [
            "lokaliserad rodnad och svullnad",
            "ömmhet vid palpation",
            "externt hordeolum: vid fransbas (Zeiss eller Moll körtel)",
            "internt hordeolum: i meibomkörtel (tarsalt)",
            "eventuellt pus-huvud",
            "kan dränera spontant"
        ],
        "risk_factors": [
            "blepharit",
            "rosacea",
            "dålig ögonlockshygien",
            "diabetes",
            "seborrhoisk dermatit",
            "immunsuppression"
        ],
        "treatment": "Varma kompresser 10-15 min 4x dagligen (främjar spontan dränage), ögonlockshygien, topikala antibiotika (fusidinsyra salva) om rupturerat, undvik att klämma!, oftast självläkande på 1-2 veckor, incision och dränage om inte spontan dränage efter 1 vecka, systemiska antibiotika sällan nödvändiga (om cellulitis), förebyggande: behandla blepharit",
        "kva": "Ingen (vanligtvis spontan läkning)",
        "differential_diagnoses": [
            "Chalazion (mindre smärtsamt, kroniskt)",
            "Preseptal cellulitis (mer utbredd inflammation)",
            "Ögonlockstumör (sakta växande, ej smärtsam)"
        ],
        "description": "Hordeolum är akut bakteriell infektion i talgkörtel (Zeiss/Moll) eller meibomkörtel. Smärtsamt, akut. Staphylococcus aureus vanligast. Varma kompresser och spontan dränage. Oftast självläkande. Undvik att klämma!",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Chalazion (Hagelkorn)",
        "name_en": "Chalazion",
        "icd10": "H00.1",
        "symptoms": [
            "smärtfri eller minimalt öm puck i ögonlock",
            "gradvis utveckling",
            "svullnad",
            "eventuell kosmetisk påverkan",
            "tryck mot öga kan ge astigmatism",
            "ofta ingen rodnad (om ej inflammerad)"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft pucken?",
            "Gör det ont? (oftast nej)",
            "Växer den långsamt?",
            "Har du haft flera?",
            "Har du blepharit eller MGD?",
            "Har du diabetes?"
        ],
        "clinical_signs": [
            "fast, rund, smärtfri massa i ögonlock",
            "kan vara på tarsala ytan eller hud-sidan",
            "ofta inget pus-huvud (sterilt granulom)",
            "kan vara multipla",
            "röd/gul vid eversion av lock (lipogranulom)",
            "ingen akut inflammation (om ej sekundärt infekterad)"
        ],
        "risk_factors": [
            "blepharit",
            "meibomian gland dysfunction",
            "rosacea",
            "seborroisk dermatit",
            "recidiverande chalazion: överväg sebaceös carcinöm (sällsynt)",
            "diabetes"
        ],
        "treatment": "Observation (många försvinner spontant över månader), varma kompresser + massage, ögonlockshygien, intralesional steroidinjektion (triamcinolon) - effektivt, 50-80% resolution, incision och curettage om persisterande >2-3 månader eller kosmetiskt störande, topikala antibiotika INTE effektiva (sterilt), vid multipla eller recidiverande: behandla underliggande MGD/blepharit, biopsiera om atypiskt (uteslut sebaceöst carcinöm)",
        "kva": "ACH00 (incision och curettage)",
        "differential_diagnoses": [
            "Hordeolum (akut, smärtsamt)",
            "Sebaceöst carcinöm (recidiverande, äldre, madarosis)",
            "Dermoid cysta",
            "Benigna ögonlockstumörer"
        ],
        "description": "Chalazion är sterilt kroniskt lipogranulom i meibomkörtel. Smärtfri puck. Långsam utveckling. Ofta sekundärt till MGD. Varma kompresser, steroidinjektion eller kirurgisk excision. Recidiverande chalazion: uteslut sebaceöst carcinöm (särskilt hos äldre).",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Preseptal Cellulitis",
        "name_en": "Preseptal Cellulitis",
        "icd10": "H05.0",
        "symptoms": [
            "svullna ögonlock",
            "rodnad runt öga",
            "ömmhet",
            "ingen synpåverkan",
            "inga dubbelseende",
            "inga ögonrörelsepåverkan",
            "kan ha feber"
        ],
        "anamnesis_questions": [
            "Har du haft hudskada eller insektsbett?",
            "Har du haft bihåleinflammation?",
            "Har barnet feber?",
            "Gör det ont att röra ögat? (bör vara nej)",
            "Ser du dubbelt? (bör vara nej)",
            "Har du smärta när du rör ögat? (bör vara nej)"
        ],
        "clinical_signs": [
            "ögonlocksödem och rodnad",
            "erytem periorbital",
            "normal syn",
            "normala ögonrörelser",
            "ingen proptosis",
            "ingen RAPD",
            "ingen smärta vid ögonrörelser (viktigt!)",
            "septum orbitale intakt (inflammation anterior till septum)"
        ],
        "risk_factors": [
            "hudskada (snitt, insektsbett)",
            "bihåleinflammation (mild)",
            "hordeolum/chalazion",
            "barn vanligare",
            "immunsuppression",
            "diabetes"
        ],
        "treatment": "Orala antibiotika (täcker Staphylococcus, Streptococcus): amoxicillin-clavulanat, cephalexin, clindamycin, 7-10 dagar, barn <1 år eller svåra fall: IV-antibiotika (cefuroxim, cefotaxim), dagliga kontroller tills förbättring, varma kompresser, smärtlindring, VIKTIGT: uteslut orbital cellulitis (se nedan)!, CT om osäker diagnos, bra prognos med antibiotika",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Orbital cellulitis (smärta vid ögonrörelser, proptosis, synpåverkan)",
            "Insektsbett",
            "Kontaktallergi",
            "Angioödem"
        ],
        "description": "Preseptal cellulitis är infektion anterior till orbital septum. Svullna lock men INGEN ögonrörelse-påverkan eller synpåverkan. Viktigt att skilja från orbital cellulitis. Orala antibiotika vanligtvis tillräckligt. God prognos.",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Orbital Cellulitis",
        "name_en": "Orbital Cellulitis",
        "icd10": "H05.0",
        "symptoms": [
            "svullna ögonlock",
            "rodnad",
            "SMÄRTA vid ögonrörelser (kritiskt tecken!)",
            "synnedsättning",
            "dubbelseende",
            "proptosis (utbuktande öga)",
            "feber",
            "systemisk sjukdom"
        ],
        "anamnesis_questions": [
            "Har du haft bihåleinflammation?",
            "Gör det ont när du rör ögat? (JA - varningssignal)",
            "Ser du dubbelt?",
            "Har synen försämrats?",
            "Står ögat ut mer än vanligt?",
            "Har du feber?",
            "Har du huvudvärk eller är allmänpåverkad?"
        ],
        "clinical_signs": [
            "proptosis",
            "smärta vid ögonrörelser (viktigast tecken!)",
            "begränsade ögonrörelser (ofthalmoplegia)",
            "synnedsättning möjlig",
            "RAPD möjlig (optikusneuropati)",
            "ögonlocksödem och rodnad",
            "chemosis (konjunktival ödem)",
            "feber och systemiska tecken"
        ],
        "risk_factors": [
            "akut bakteriell bihåleinflammation (etmoidit vanligast)",
            "trauma",
            "post-kirurgiskt (bisinuskirurgi)",
            "odontogen infektion",
            "immunsuppression",
            "barn vanligare",
            "bakterier: Staphylococcus, Streptococcus, anaerober"
        ],
        "treatment": "AKUT INLÄGGNING! IV-antibiotika (bred-spektrum): cefotaxim eller ceftriaxone + metronidazol (anaerober), eller piperacillin-tazobactam, vancomycin om MRSA-risk, CT orbita och bihålor (uteslut abscess), ÖNH-konsult (dränage av bihålor om behövs), ögonkirurg-konsult, abscess >10mm eller optikusneuropati: akut kirurgisk dränage, täta kontroller av syn, ögonrörelser, pupillrespons, IV-antibiotika minst 48h, sedan orala i 2-3 veckor totalt, komplikationer: optikusneuropati, cavernous sinus trombos, meningit, hjärnabscess, livshotande!",
        "kva": "Dränage av abscess vid behov",
        "differential_diagnoses": [
            "Preseptal cellulitis (INGEN smärta vid ögonrörelser)",
            "Orbital pseudotumör",
            "Tyreoideaorbitopati",
            "Orbital tumör"
        ],
        "description": "Orbital cellulitis är allvarlig, potentiellt livshotande infektion posterior till orbital septum. Smärta vid ögonrörelser är kritiskt tecken! Vanligen från etmoidit. Kräver akut inläggning och IV-antibiotika. Risk för optikusneuropati, meningit, cavernous sinus trombos. Oftast god prognos med snabb behandling.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Endoftalmit - Postoperativ",
        "name_en": "Postoperative Endophthalmitis",
        "icd10": "H44.0",
        "symptoms": [
            "kraftig synnedsättning",
            "smärta",
            "rodnad",
            "ljuskänslighet",
            "efter ögonkirurgi (kataraktkirurgi vanligast)",
            "symptom oftast 2-7 dagar postop"
        ],
        "anamnesis_questions": [
            "Har du opererats nyligen?",
            "Vilken operation? (katarakt vanligast)",
            "När började symptomen?",
            "Försämras synen snabbt?",
            "Har du kraftig smärta?",
            "Ser du bara ljus eller sämre?"
        ],
        "clinical_signs": [
            "kraftig vitrit",
            "hypopyon (pus i främre kammaren)",
            "korneal ödem",
            "synnedsättning (ofta LP eller sämre)",
            "rodnad och konjunktival injektion",
            "svullna ögonlock möjligt",
            "fundusreflex dålig eller absent",
            "bakterier: Staphylococcus epidermidis (70%), S. aureus, Streptococcus"
        ],
        "risk_factors": [
            "kataraktkirurgi (0.05-0.3%)",
            "vitrektomi",
            "trauma",
            "komplicerad kirurgi",
            "immunsuppression",
            "diabetes",
            "blepharit/MGD preoperativt",
            "kapselruptur vid kataraktkirurgi"
        ],
        "treatment": "AKUT! Intravitreal antibiotika (vancomycin + ceftazidim eller amikacin) - ger högst koncentration direkt, vitreus och främre kammarkultur före antibiotika, vitrektomi vid syn <LP eller svår (EVS-studien), topikala antibiotika (fortifierade eller fluorokinoloner) intensivt, topikala steroider efter antibiotika startat, cykloplegika, systemiska antibiotika kontroversiellt (hjälper ej enligt EVS), täta kontroller, intravitreal steroid (dexamethason) kan övervägas dag 2-3, prognos beroende på virulens: S. epidermidis - god (70% >20/40), S. aureus/Streptococcus - dålig (enukleation möjlig)",
        "kva": "CJE20 (vitrektomi vid behov)",
        "differential_diagnoses": [
            "Steril postoperativ inflammation (TASS - toxic anterior segment syndrome)",
            "Retinal avlossning",
            "Svår uveit",
            "Glaskroppsblödning"
        ],
        "description": "Postoperativ endoftalmit är ögonkirurgisk katastrof. Bakteriell infektion intraokulär. Vanligast efter kataraktkirurgi (0.05-0.3%). Kräver akut intravitreal antibiotika. Prognos beroende på bakterie - S. epidermidis bäst, S. aureus/Strep värst. EVS-studien: vitrektomi om syn <LP.",
        "severity": "severe",
        "urgency": "emergency"
    },
    {
        "name": "Toxisk Anterior Segment Syndrom (TASS)",
        "name_en": "Toxic Anterior Segment Syndrome",
        "icd10": "H59.8",
        "symptoms": [
            "suddig syn",
            "smärta (mindre än endoftalmit)",
            "ljuskänslighet",
            "efter kataraktkirurgi",
            "symptom inom 12-48 timmar (tidigare än endoftalmit)"
        ],
        "anamnesis_questions": [
            "Opererades du för grå starr i går eller i förrgår?",
            "Har flera patienter som opererades samma dag samma problem? (ofta cluster)",
            "Är smärtan måttlig (inte fruktansvärd som endoftalmit)?",
            "Började det inom 24-48h?"
        ],
        "clinical_signs": [
            "diffus korneal ödem (limbus-till-limbus)",
            "cellreaktion i främre kammaren",
            "hypopyon möjligt",
            "pupillär fibrin",
            "IOL-klar initialt (vs endoftalmit där IOL täcks av exsudat)",
            "vitrit SAKNAS (viktigt!)",
            "ofta bilateral om båda ögonen opererade samma dag",
            "clusters av patienter samma dag"
        ],
        "risk_factors": [
            "kontaminerade lösningar (BSS, viscoelatiska)",
            "desinfektionsmedel-residual (glutaraldehyd, detergenter)",
            "instrumentkontamination",
            "endotoxin från bakterier",
            "talkpulver från handskar",
            "IOL-förpackning-lösningar"
        ],
        "treatment": "STERIL inflammation (INTE infektion!): intensiva topikala steroider (prednisolon 1% varje timme), eventuellt periokulärt/intravitreal steroid, cykloplegika, INGEN antibiotika nödvändig (men kan ge för säkerhets skull initialt tills endoftalmit utesluten), hypertonisk saltvätska för korneal ödem, oftast god prognos med steroidbehandling, utred källa för att förhindra fler fall (instrumentsterilisering, lösningar, operationsrutiner), viktigt: uteslut endoftalmit (kultur om osäker)!",
        "kva": "Ingen (medicinsk behandling)",
        "differential_diagnoses": [
            "Endoftalmit (vitrit, sämre prognos, senare debut)",
            "Postoperativ uveit",
            "Retainerad linssubstans-uveit"
        ],
        "description": "TASS är steril toxisk inflammation efter kataraktkirurgi. Orsakad av kontaminanter. Tidig debut (12-48h) vs endoftalmit (2-7 dagar). Saknar vitrit (viktigt!). Ofta clusters. Behandlas med intensiva steroider. God prognos. Viktigt att uteslut endoftalmit!",
        "severity": "moderate",
        "urgency": "urgent"
    },
    {
        "name": "Dakrioadenit (Tårkörtelinflammation)",
        "name_en": "Dacryoadenitis",
        "icd10": "H04.0",
        "symptoms": [
            "svullnad och smärta i yttre övre ögonlocket",
            "rodnad över laterala övre lock",
            "S-formad ptosis (karakteristiskt!)",
            "tårflöde",
            "feber (vid akut bakteriell)",
            "ömmhet vid palpation",
            "kan ha dubbelseende (om svullnad stor)",
            "lymfkörtelsvullnad preaurikulärt"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft svullnaden?",
            "Har du feber eller känner dig sjuk?",
            "Har du haft liknande tidigare?",
            "Har du körtelfeber (mononukleos)?",
            "Har du torrt ögon eller mun (Sjögrens)?",
            "Har du sarkoid eller annan systemsjukdom?",
            "Har du haft trauma mot ögat?",
            "Har du svullna lymfkörtlar på andra ställen?"
        ],
        "clinical_signs": [
            "synlig svullnad yttre övre ögonlock",
            "S-formad ptosis (från dakriadalkörteln)",
            "palpabel, öm massa i laterala övre orbita",
            "konjunktival injektion (ofta temporal)",
            "can ha purulent sekret från tårkörtelgångar",
            "förstorad tårkörtel (synlig/palpabel)",
            "preaurikulär lymfadenopati",
            "kan ha proptosis (om stor)"
        ],
        "risk_factors": [
            "virala infektioner (EBV, mumps, influensa)",
            "bakteriell infektion (Staph aureus, Streptococcus)",
            "systemiska sjukdomar (Sjögrens syndrom, sarkoid, IgG4-sjukdom)",
            "immunsuppression",
            "trauma",
            "tårkörtel-tumör (kronisk dakrioadenit kan vara tumör!)"
        ],
        "treatment": "AKUT BAKTERIELL: oral antibiotika (flukloxacillin, amoxicillin-clavulanat, klindamycin) i 10-14 dagar. Varma kompress. Smärtlindring (NSAID, paracetamol). Om abscess: kirurgisk dränage. IV antibiotika om systemisk sjukdom eller svår infektion. VIRAL (vanligast): stödjande behandling (virus går över spontant på 2-3 veckor), varma kompress, smärtlindring. INGEN antibiotika vid viral etiologi. KRONISK: utred underliggande orsak! Biopsi om kronisk (uteslut tumör, sarkoid, IgG4-sjukdom, Sjögrens). Behandla underliggande systemsjukdom. Steroider vid inflammatoriska systemsjukdomar (sarkoid, IgG4). Uppföljning: kontroll efter 1-2 veckor, längre uppföljning vid kronisk. VIKTIGT: kronisk dakrioadenit kan vara tecken på lymfom eller annan tumör - utred!",
        "kva": "AT001 (konsultation), PA001 (biopsi om kronisk)",
        "differential_diagnoses": [
            "preseptal cellulitis",
            "dermatochalasis med inflammation",
            "tårkörtel-tumör (pleomorf adenom, lymfom)",
            "orbital cellulitis",
            "chalazion (stor, i laterala övre lock)",
            "Sjögrens syndrom",
            "sarkoidosis",
            "IgG4-relaterad sjukdom"
        ],
        "description": "Dakrioadenit är inflammation av tårkörteln (lakrimalkörteln). Kan vara akut (oftast viral eller bakteriell) eller kronisk (systemiska sjukdomar, tumör). Karakteristisk S-formad ptosis och svullnad i yttre övre lock. Akut viral går över spontant, bakteriell kräver antibiotika. Kronisk kräver utredning för underliggande orsak.",
        "severity": "moderate",
        "urgency": "urgent (akut bakteriell)"
    }
]
