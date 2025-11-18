"""
Other/Miscellaneous Eye Conditions - Övriga Ögonsjukdomar
5 additional common eye conditions

Database of miscellaneous eye diseases for the medical knowledge base.
"""

OTHER_DISEASES = [
    {
        "name": "Subkonjunktival Blödning",
        "name_en": "Subconjunctival Hemorrhage",
        "icd10": "H11.3",
        "symptoms": [
            "synlig, klarröd blödning i ögonvitan",
            "ofta asymtomatisk",
            "ingen synpåverkan",
            "ingen smärta (oftast)",
            "upptäcks ofta av patient eller närstående i spegel",
            "kan ha lätt främmande kropps-känsla"
        ],
        "anamnesis_questions": [
            "Märkte du när blödningen uppstod?",
            "Har du haft kraftig hosta, kräkning eller ansträngning?",
            "Använder du blodförtunnande mediciner (Waran, NOAK, ASA)?",
            "Har du högt blodtryck?",
            "Har du haft trauma mot ögat?",
            "Har detta hänt tidigare?",
            "Har du blödningsbenägenhet på andra ställen?",
            "Ser du lika bra som vanligt?"
        ],
        "clinical_signs": [
            "klarröd, väldefinierad blödning under konjunktivan",
            "oftast ensidigt",
            "ingen påverkan på cornea eller iris",
            "normalt syntest",
            "normalt IOP",
            "ingen uveitt eller inflammation",
            "blödningen kan vara begränsad eller täcka stora delar av sclera"
        ],
        "risk_factors": [
            "antikoagulantia (Waran, NOAK, ASA, Trombyl)",
            "hypertoni (högt blodtryck)",
            "kraftig hosta eller kräkning (Valsalva)",
            "ansträngning (tunga lyft, krystning)",
            "trauma (även lindrigt, t.ex. ögongnuggning)",
            "konjunktivit",
            "kontaktlinser",
            "koagulationsrubbningar (hemofili, trombocytopeni)",
            "högre ålder (sköra kärl)"
        ],
        "treatment": "Oftast INGEN behandling nödvändig - spontan resorption på 1-3 veckor. Lugnande besked till patient (ser värre ut än det är). Kalla kompress första dygnet kan begränsa blödning. Smörjande ögondroppar om lätt irritation. VIKTIGT: Mät blodtryck (kan vara tecken på okontrollerad hypertoni). Kontrollera koagulationsstatus om patient tar antikoagulantia eller recidiverande blödningar. Justera INTE antikoagulation pga subkonjunktival blödning (diskutera med kardiolog/internmedicin om recidiv). Återkom om: smärta, synförsämring, blödningen inte går tillbaka på 2-3 veckor, frekventa recidiv. Differentialdiagnostik: om bilaterala eller recidiverande blödningar - utred för blödningsrubbning, hypertoni, vaskulit.",
        "kva": "AT001 (konsultation)",
        "differential_diagnoses": [
            "episklerit (mer inflammation, inte bara blödning)",
            "konjunktivit (sekret, mer irritation)",
            "sklerit (smärta, djupare inflammation)",
            "karotiko-kavernös fistel (korkskruvsformade episkelära kärl)",
            "hyphema (blod i främre kammaren, INTE subkonjunktivalt)"
        ],
        "severity": "mild",
        "urgency": "routine (oftast inget akut)"
    },
    {
        "name": "Pinguecula och Pterygium",
        "name_en": "Pinguecula and Pterygium",
        "icd10": "H11.1 (pinguecula), H11.0 (pterygium)",
        "symptoms": [
            "gulaktig upphöjning på ögonvitan (pinguecula)",
            "triangulär hudvävnad som växer in på hornhinnan (pterygium)",
            "ofta asymtomatisk",
            "irritation och rodnad (inflammerad pinguecula/pterygium)",
            "torrhetskänsla",
            "främmande kropps-känsla",
            "synförsämring (om pterygium täcker pupill)",
            "kosmetiskt störande"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft förändringen?",
            "Har den vuxit?",
            "Har du irritation eller rodnad?",
            "Har du försämrad syn?",
            "Är du mycket utomhus eller exponerad för sol, vind, damm?",
            "Använder du skyddsglasögon?",
            "Har det opererats tidigare? (recidiv?)",
            "Stör det dig kosmetiskt?"
        ],
        "clinical_signs": [
            "pinguecula: gulaktig, upphöjd lesion på bulbär konjunktiva (oftast nasal eller temporal)",
            "pterygium: fibrövaskulär vävnad som växer från limbus in på cornea",
            "ofta bilateral",
            "kan vara inflammerad (rodnad, svullnad)",
            "pterygium kan orsaka astigmatism (corneal dragning)",
            "synförsämring om optisk zon involverad"
        ],
        "risk_factors": [
            "UV-exponering (solljus)",
            "vind och damm",
            "torrt klimat",
            "utomhusarbete",
            "ekvatornära breddgrader",
            "manligt kön (högre prevalens)",
            "ögontorrhet",
            "genetisk predisposition"
        ],
        "treatment": "Pinguecula: oftast INGEN behandling. Smörjande droppar vid irritation. Kortison-droppar kortvarigt vid inflammerad pinguecula. Kirurgisk excision endast om kosmetiskt mycket störande eller kronisk inflammation. Pterygium: Observation om liten och icke-progressiv. Smörjande droppar. UV-skydd (solglasögon). KIRURGI indikerat vid: tillväxt mot pupill (synhot), betydande astigmatism, kosmetiskt besvärande, kronisk inflammation. Kirurgisk teknik: excision med konjunktival autograft eller amnionmembran (minskar recidiv). Intraoperativ mitomycin C för att minska recidivrisk. VARNING: hög recidivrisk (10-30%) särskilt hos yngre patienter. Postoperativt: steroid-droppar, UV-skydd livslångt.",
        "kva": "ACH10 (excision pinguecula/pterygium)",
        "differential_diagnoses": [
            "conjunctival intraepithelial neoplasia (CIN)",
            "squamous cell carcinoma (mer oroväckande lesion)",
            "Salzmann nodular degeneration (corneal)",
            "limbal dermoid",
            "pannus (vid trachoma eller kontaktlinsbärare)"
        ],
        "severity": "mild (moderate om synpåverkan)",
        "urgency": "routine"
    },
    {
        "name": "Floaters och Photopsia (Glaskroppsavlossning)",
        "name_en": "Floaters and Flashes (Posterior Vitreous Detachment)",
        "icd10": "H43.9 (vitreous floaters)",
        "symptoms": [
            "flygande flugor, prickar eller spindelväv i synfältet",
            "ljusblixtar (photopsia), särskilt i periferin",
            "symtomen rör sig med ögat",
            "mer framträdande mot ljusa bakgrunder",
            "ofta plötslig debut",
            "oftast ensidigt (men kan bli bilateralt över tid)",
            "ingen smärta"
        ],
        "anamnesis_questions": [
            "Hur länge har du haft symtomen?",
            "Kom de plötsligt?",
            "Ser du ljusblixtar?",
            "Har du en gardin eller skugga i synfältet? (VARNING för retinal avlossning)",
            "Har du sett många nya floaters eller 'regn' av floaters?",
            "Har du synförsämring?",
            "Är du myop (närsint)?",
            "Har du haft ögonoperation eller ögontrauma?",
            "Har det andra ögat haft samma symtom tidigare?"
        ],
        "clinical_signs": [
            "Weiss ring (cirkulär opacity vid posterior vitreous face)",
            "vitreous syneresis och kondensation",
            "vitreous detachment vid oftalmoskopi",
            "VIKTIGT: uteslut retinal break eller avlossning (omedelbar utvidgad fundusundersökning)",
            "kan ha lätt vitreous hemorrhage",
            "synfält normalt (om ingen retinal skada)",
            "normalt IOP och anterior segment"
        ],
        "risk_factors": [
            "ålder (>50 år, fysiologisk process)",
            "myopi (närsynthet)",
            "tidigare PVD i andra ögat",
            "ögontrauma",
            "inflammation (uveit)",
            "intraokulärt kirurgi (t.ex. katarakt-op)",
            "YAG capsulotomy"
        ],
        "treatment": "AKUT utvidgad fundusundersökning (dilaterad pupill) för att utesluta retinal break eller avlossning - detta är AVGÖRANDE! Om ingen retinal patologi: lugnande besked, floaters förbättras ofta spontant över månader när de sjunker ner. INGEN specifik behandling för okomplicerad PVD. Patientutbildning: återkom AKUT om: plötslig ökning av floaters, 'regn' av floaters, ljusblixtar ökar, synfältsbortfall (gardin/skugga), synförsämring. Uppföljning: kontroll efter 4-6 veckor (retinal break kan utvecklas senare). Om retinal break: laser photocoagulation eller kryoterapi (profylaktiskt). Om retinal avlossning: akut vitreoretinal kirurgi. Vitrektomi för floaters är SÄLLAN indicerat (endast vid svåra symtom som påverkar ADL).",
        "kva": "CJE05 (utvidgad fundusundersökning), CJF20 (laser photocoagulation vid break)",
        "differential_diagnoses": [
            "retinal break/tear (akut risk!)",
            "retinal avlossning (akut!)",
            "vitreous hemorrhage",
            "uveit (inflammation)",
            "asteroid hyalosis (oftare bilateralt, asymtomatiskt)",
            "synchysis scintillans"
        ],
        "severity": "mild (men kan vara tecken på severe tillstånd)",
        "urgency": "urgent (akut fundusundersökning krävs)"
    },
    {
        "name": "Computer Vision Syndrome / Digital Eye Strain",
        "name_en": "Computer Vision Syndrome / Digital Eye Strain",
        "icd10": "H53.1 (subjektiva synstörningar)",
        "symptoms": [
            "trötta, ansträngda ögon",
            "huvudvärk (frontal eller temporal)",
            "suddig syn (särskilt på avstånd efter skärmarbete)",
            "torra, irriterade ögon",
            "dubbelseende (tillfälligt)",
            "nackvärk och axelvärk",
            "ökad ljuskänslighet",
            "svårighet att fokusera",
            "symtomen förvärras under dagen"
        ],
        "anamnesis_questions": [
            "Hur många timmar per dag arbetar du vid dator/skärm?",
            "Tar du pauser från skärmarbetet?",
            "Hur är din arbetsplatsergonomi? (skärmavstånd, höjd)",
            "Använder du glasögon? Är de uppdaterade?",
            "Har du torra ögon?",
            "Blinkar du mindre när du tittar på skärm?",
            "Använder du läsglasögon eller progressiva glas?",
            "Har du belysningsproblem (bländning, reflexer)?",
            "Förbättras symtomen på helger/semester?"
        ],
        "clinical_signs": [
            "oftast normalt oftalmologiskt status",
            "kan ha låggradig hyperopi eller astigmatism",
            "accommodationsinsufficiens (hos vissa)",
            "convergence insufficiency",
            "förkortat tårfilmens break-up time (torr ögon)",
            "reducerad blinkfrekvens vid skärmarbete",
            "kan ha latent hyperopi som ger symtom"
        ],
        "risk_factors": [
            "långvarigt skärmarbete (>2 timmar/dag)",
            "okorrigerat refraktionsfel",
            "hyperopi eller astigmatism",
            "presbyopi (svårighet med progressiva glas vid skärmarbete)",
            "torrt ögon",
            "dålig arbetsplatsergonomi",
            "bländning eller reflexer på skärmen",
            "för låg skärmkontrast eller liten text",
            "för nära skärmavstånd"
        ],
        "treatment": "Multifaktoriell approach: 1) REFRAKTIONSKORRIGERING: glasögon eller kontaktlinser (även små fel kan ge symtom). Speciella datorglasögon med anti-reflex och blåljusfilter kan hjälpa. 2) ERGONOMI: 20-20-20 regeln (var 20:e minut, titta 20 fot bort i 20 sekunder). Skärmen 50-70 cm från ögonen, något nedanför ögonhöjd. Minska bländning (gardiner, skärmfilter). 3) TORRA ÖGON: smörjande droppar (tårsubstitut), fuktig miljö, påminn om att blinka. 4) ACCOMMODATION/CONVERGENCE TRÄNING: ortoptistbedömning vid convergence insufficiency. 5) BELYSNING: indirekt belysning, undvik starkt overhead ljus. 6) PAUSER: regelbundna pauser från skärmarbete. Symtomen är reversibla med rätt åtgärder!",
        "kva": "CJA00 (synundersökning och refraktion), AT001 (konsultation)",
        "differential_diagnoses": [
            "okorrigerat refraktionsfel (hyperopi, astigmatism, presbyopi)",
            "accommodationsinsufficiens",
            "convergence insufficiency",
            "torrt ögon-syndrom",
            "migrän (om huvudvärk dominerande)",
            "cervikal spondylos (om nackvärk dominerande)"
        ],
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Okulär Migrän / Visual Aura",
        "name_en": "Ocular Migraine / Migraine with Visual Aura",
        "icd10": "G43.1 (migrän med aura)",
        "symptoms": [
            "tillfälliga synstörningar (10-30 minuter)",
            "flimmer, sicksackmönster (fortification spectra)",
            "scotom (mörk fläck i synfältet)",
            "oftast bilateral homonym",
            "symtomen sprider sig gradvis",
            "huvudvärk (kan komma efter auran, men inte alltid)",
            "illamående (ibland)",
            "fullständig återhämtning efter aura"
        ],
        "anamnesis_questions": [
            "Hur länge varar synstörningarna? (typiskt 10-30 min)",
            "Hur ser synstörningarna ut? (sicksack, flimmer, mörk fläck)",
            "Sprider de sig gradvis?",
            "Får du huvudvärk efteråt?",
            "Har du haft liknande episoder tidigare?",
            "Är det båda ögonen eller bara ett? (VIKTIGT - retinal migrän är monokulär)",
            "Finns det familjehistoria av migrän?",
            "Har du några triggerfaktorer? (stress, sömnbrist, mat, hormoner)",
            "Har du andra neurologiska symtom? (domningar, talsvårigheter)"
        ],
        "clinical_signs": [
            "NORMALT oftalmologiskt status mellan attacker",
            "normal synutvärdering",
            "normala pupiller",
            "normal fundus",
            "normalt synfält (utanför attack)",
            "inga fokalneurologiska bortfall"
        ],
        "risk_factors": [
            "familjehistoria av migrän",
            "kvinnligt kön",
            "ålder (20-50 år vanligast)",
            "stress",
            "sömnbrist",
            "hormonella förändringar (menstruation, p-piller)",
            "vissa livsmedel (ost, choklad, alkohol)",
            "koffeinintag/utsättning",
            "väderomslag"
        ],
        "treatment": "Migrän med aura: oftast INGEN specifik behandling för auran själv (går över spontant på 10-30 min). VIKTIGT: första gången - uteslut TIA, stroke, retinal vaskulär ocklusio (särskilt om >50 år, endast ett öga, vaskulära riskfaktorer). Vid huvudvärk efter aura: NSAID (ibuprofen, naproxen) eller paracetamol tidigt. Triptaner (sumatriptan) - OBS kontraindicerat vid migrän med aura hos vissa (stroke-risk hos dem med vaskulära riskfaktorer). Profylax om frekventa attacker (>4/månad): beta-blockerare, kalciumantagonister, topiramat, amitriptylin. CGRP-hämmare (erenumab) vid refraktär migrän. Livsstilsåtgärder: regelbunden sömn, undvik triggers, stresshantering, regelbunden motion. Retinal migrän (monokulär synförlust): uteslut retinal vaskulär patologi (amaurosis fugax, ocklusio)!",
        "kva": "AT001 (neurologkonsult om oklart)",
        "differential_diagnoses": [
            "TIA (transitorisk ischemisk attack) - särskilt om >50 år, vaskulära riskfaktorer",
            "amaurosis fugax (retinal TIA - monokulär)",
            "retinal artär/ven ocklusio",
            "posterior cortical infarkt",
            "occipital lobe seizure (epilepsi)",
            "vertebrobasilar insufficiens",
            "retinal avlossning (men inte transient)",
            "vitreous hemorrhage (plötslig men inte transient)"
        ],
        "severity": "mild (men uteslut vaskulära orsaker först!)",
        "urgency": "urgent (första episoden - uteslut stroke/TIA)"
    }
]


def get_other_diseases():
    """Return all other/miscellaneous diseases"""
    return OTHER_DISEASES


def get_disease_by_name(name: str):
    """Get a specific disease by name (Swedish or English)"""
    name_lower = name.lower()
    for disease in OTHER_DISEASES:
        if (name_lower in disease['name'].lower() or
            name_lower in disease['name_en'].lower()):
            return disease
    return None


def get_diseases_by_urgency(urgency: str):
    """Get diseases by urgency level"""
    return [d for d in OTHER_DISEASES if d['urgency'] == urgency]


if __name__ == "__main__":
    print(f"Loaded {len(OTHER_DISEASES)} miscellaneous eye diseases")
    for disease in OTHER_DISEASES:
        print(f"  - {disease['name']}")
