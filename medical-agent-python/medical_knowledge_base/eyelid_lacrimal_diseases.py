"""
Ögonlock och Tårvägar - 15 vanligaste
"""

EYELID_LACRIMAL_DISEASES = [
    {
        "name": "Entropion",
        "name_en": "Entropion",
        "icd10": "H02.0",
        "symptoms": [
            "främmande kropps-känsla",
            "irritation och rodnad",
            "tårrinnande",
            "ljuskänslighet",
            "smärta (fransar repar kornea)",
            "korneal erosion möjlig",
            "ofta nedre ögonlock hos äldre"
        ],
        "anamnesis_questions": [
            "Känns det som du har nåt i ögat?",
            "Rinner tårar ofta?",
            "Har ögonlocket vänt sig inåt?",
            "Är det värre när du blinkar hårt eller kisar?",
            "Hur gammal är du?",
            "Har du ärr från inflammation eller trauma?"
        ],
        "clinical_signs": [
            "ögonlockskant vikt inåt",
            "fransar repar kornea",
            "korneal epitheldefekter eller erosion",
            "konjunktival injektion",
            "typer: involutionell (ålder - vanligast), spastisk, cikatrisell (ärr), kongenitalt"
        ],
        "risk_factors": [
            "hög ålder (involutionell - vanligast)",
            "horizontal lid laxity",
            "orbicularis override",
            "trachom/cicatricerande konjunktivit (cikatrisell)",
            "Stevens-Johnson syndrom",
            "kraftig blefarospasm",
            "okulär pemfigoid"
        ],
        "treatment": "Temporär: lubricering, tejpa ögonlock utåt nattetid, botulinum toxin i orbicularis (tillfälligt), Kirurgisk (definitiv behandling): involutionell: horizontal lid tightening + retractor reinsertion/plication, everting sutures temporärt, cikatrisell: anteriort lamellar repositionering, tarsalmargin rotation, mukosalt graft, spastiskt: behandla underliggande irritation, botox, Prognos: utmärkt med kirurgi",
        "kva": "ACF00 (entropionkorrigering)",
        "differential_diagnoses": [
            "Trichiasis (fransar inåtvända men lock normalt)",
            "Distichiasis (extra fransrad)",
            "Epiblepharon (extra hudfold - barn)"
        ],
        "description": "Entropion är inåtvridet ögonlock där fransar repar kornea. Involutionell typ vanligast hos äldre (lid laxity + orbicularis override). Ger kraftig irritation och korneal skada. Kirurgisk korrektion kurativ. Temporärt: lubricering och everting sutures.",
        "severity": "moderate",
        "urgency": "urgent (korneal skada-risk)"
    },
    {
        "name": "Ektropion",
        "name_en": "Ectropion",
        "icd10": "H02.1",
        "symptoms": [
            "tårrinnande (epifora)",
            "rodnat, exponerat konjunktiva",
            "torra ögon (paradoxalt - dålig tårfördelning)",
            "irritation",
            "kronisk konjunktivit",
            "keratopati vid exponering",
            "ofta nedre ögonlock"
        ],
        "anamnesis_questions": [
            "Rinner tårar ner på kinden?",
            "Är ögonlockskanten utåtvänd?",
            "Känns ögat torrt trots tårrinnande?",
            "Hur gammal är du?",
            "Har du haft Bell's pares?",
            "Har du ärr från trauma eller kirurgi?"
        ],
        "clinical_signs": [
            "ögonlockskant utåtvänd",
            "exponerad tarsalkonjunktiva",
            "punktum (tårpunkt) ej i kontakt med ögat",
            "epifora (tåroverflow)",
            "konjunktival keratinisering möjlig",
            "typer: involutionell (vanligast), paralytisk (VII-nervpares), cikatrisell, mekaniskt"
        ],
        "risk_factors": [
            "hög ålder (involutionell)",
            "horizontal lid laxity",
            "Bell's pares/VII-nervpares (paralytiskt)",
            "actinic damage (solskada)",
            "tidigare ögonlockskirurgi/trauma (cikatrisell)",
            "ögonlockstumör (mekaniskt)"
        ],
        "treatment": "Temporär: lubricering (droppar + salva), tejpa lock uppåt, behandla exponeringskeratopati, Kirurgisk: involutionell: lateral tarsal strip/horizontal shortening, medial spindle excision, paralytiskt: lateral tarsal strip + medial canthoplasty, eventuellt gold weight i övre lock, cikatrisell: posterior lamellar graft (slemhinna, hårdmembran), hudgraft, Prognos: god med kirurgi",
        "kva": "ACF10 (ektropionkorrigering)",
        "differential_diagnoses": [
            "Punctal eversion (endast tårpunkt utåtvänd)",
            "Cicatricial changes",
            "Floppy eyelid syndrome"
        ],
        "description": "Ektropion är utåtvridet ögonlock. Involutionell typ vanligast hos äldre. Ger epifora (tårpunkt ej kontakt med öga) och exponeringskeratopati. Paralytiskt ektropion vid Bell's pares. Kirurgisk korrektion med lateral tarsal strip. Lubricering tills kirurgi.",
        "severity": "moderate",
        "urgency": "routine (urgent vid exponeringskeratopati)"
    },
    {
        "name": "Ptosis (Hängande Ögonlock)",
        "name_en": "Ptosis",
        "icd10": "H02.4",
        "symptoms": [
            "hängande övre ögonlock",
            "nedsatt synfält (övre)",
            "trötthet i ögon/panna",
            "höjda ögonbryn (kompensatoriskt)",
            "huvudlutning bakåt (chin-up position)",
            "kan vara medfödd eller förvärvad"
        ],
        "anamnesis_questions": [
            "Har ögonlocket hängt sedan födseln? (kongenitalt)",
            "Kom det plötsligt? (III-nervpares, myasthenia)",
            "Varierar det under dagen? (myasthenia - värre kvällen)",
            "Har du dubbelseende också? (III-nervpares)",
            "Har du använt kontaktlinser länge?",
            "Har du haft ögonkirurgi?"
        ],
        "clinical_signs": [
            "nedsatt MRD (margin-reflex distance) - normalt 4-5mm",
            "nedsatt levator-funktion (övre rektus funktion)",
            "typer: neurogen (III-nervpares, Horner's), myogen (myasthenia, CPEO, dystrofi), aponeurotisk (ålder, kontaktlinser - vanligast), mekaniskt, kongenitalt",
            "fenylefrin-test (Horner's), ice-test (myasthenia), cyklopegi (reaktiv ptosis vid hyperopi)"
        ],
        "risk_factors": [
            "ålder (aponeurotisk dehiscence - vanligast)",
            "långvarig kontaktlinsanvändning",
            "ögonoperation/trauma",
            "III-nervpares",
            "myasthenia gravis",
            "Horner's syndrom",
            "kongenitalt (dystrofi av levator)"
        ],
        "treatment": "Konservativ: ptosis crutches på glasögon (tillfälligt), Kirurgisk (beroende på typ): aponeurotisk: levator advancement/tuck, kongenitalt med dålig levator: frontalis suspension (sling), måttlig: levator resection, neurogen: åtgärda orsak först (myasthenia: pyridostigmin; III-pares: vänta 6-12 mån), Müller muscle-konjunktival resection (MMCR) vid mild ptosis, Timing: kongenitalt med amblyopi-risk: tidig kirurgi, annars vänta stabilitet",
        "kva": "ACE00 (ptosis-korrigering)",
        "differential_diagnoses": [
            "Pseudoptosis (dermatokalasis, brow ptosis)",
            "Kontralateral lid retraction (ser ut som ptosis)",
            "Mikroftalmus"
        ],
        "description": "Ptosis är hängande övre ögonlock. Aponeurotisk ptosis vanligast (ålder, kontaktlinser). Kongenitalt kräver tidig kirurgi om amblyopi-risk. Neurogen: utred orsak (myasthenia, III-pares, Horner's). Kirurgi: levator advancement (aponeurotisk), frontalis sling (kongenitalt med dålig levator).",
        "severity": "mild-moderate (severe om amblyopi-risk)",
        "urgency": "routine (urgent vid kongenitalt med amblyopi)"
    },
    {
        "name": "Dermatokalasis",
        "name_en": "Dermatochalasis",
        "icd10": "H02.3",
        "symptoms": [
            "överflödig hud på övre ögonlock",
            "tyngdkänsla i ögonlock",
            "nedsatt övre synfält",
            "trötthet i panna",
            "kosmetiskt störande",
            "smink samlas i veck",
            "kan ge funktionell synfältsinskränkning"
        ],
        "anamnesis_questions": [
            "Hänger huden över ögonlocken?",
            "Påverkar det synfältet uppåt/åt sidorna?",
            "Har du trötthet i pannan?",
            "Försämras det när du är trött?",
            "Hur gammal är du?",
            "Stör det kosmetiskt?"
        ],
        "clinical_signs": [
            "redundant, lös hud på övre (och nedre) ögonlock",
            "huden hänger över ögonfransar",
            "kan täcka synfält",
            "levator-funktion normal (vs ptosis)",
            "ofta kombinerat med brow ptosis",
            "herniation av orbital fett möjligt"
        ],
        "risk_factors": [
            "hög ålder (elasticitetsförlust)",
            "solskada",
            "rökning",
            "hereditet",
            "floppy eyelid syndrome",
            "tyreoidsjukdom",
            "amyloidos (sällsynt)"
        ],
        "treatment": "Konservativt: ingen behandling om asymptomatisk, tejpa överskott uppåt vid aktiviteter, Kirurgiskt: blefaroplastik (övre och/nedre), brow lift om brow ptosis bidrar, avlägsna överskottshud och eventuellt hernierande fett, Indikationer för kirurgi: funktionell synfältsinskränkning (dokumentera med synfält), kosmetisk (patientens önskemål), Prognos: utmärkt resultat",
        "kva": "ACB00 (blefaroplastik)",
        "differential_diagnoses": [
            "Ptosis (levator-dysfunktion)",
            "Brow ptosis",
            "Ögonlockstumör",
            "Angioödem (akut svullnad)"
        ],
        "description": "Dermatokalasis är överflödig ögonlockshud, vanligt hos äldre. Ger tyngd, nedsatt övre synfält, kosmetiska besvär. Behandling: blefaroplastik. Indikationer: funktionell synfältsinskränkning eller kosmetisk. Dokumentera synfältsinskränkning före kirurgi (försäkring).",
        "severity": "mild",
        "urgency": "routine (elektiv)"
    },
    {
        "name": "Trichiasis",
        "name_en": "Trichiasis",
        "icd10": "H02.0",
        "symptoms": [
            "främmande kropps-känsla",
            "irritation",
            "tårrinnande",
            "rodnad",
            "smärta (fransar repar kornea)",
            "ljuskänslighet",
            "recidiverande korneal erosioner"
        ],
        "anamnesis_questions": [
            "Känner du som du har hårstrån i ögat?",
            "Ser du fransar som växer inåt?",
            "Har du inflammation eller ärr i ögonlocken?",
            "Har du trachom (endemiska områden)?",
            "Har du Stevens-Johnson eller okulär pemfigoid?",
            "Har du recidiverande irritation?"
        ],
        "clinical_signs": [
            "fransar växer inåt mot kornea",
            "ögonlockskant kan vara normal (skiljer från entropion)",
            "korneal epitheldefekter/erosioner",
            "konjunktival injektion",
            "kan vara sektion av fransraden eller enstaka fransar",
            "orsaker: cikatrisell (trachom, SJS, pemfigoid), idiopatisk, blepharit"
        ],
        "risk_factors": [
            "trachom (Chlamydia trachomatis - endemiskt Afrika/Asien)",
            "Stevens-Johnson syndrom",
            "okulär cicatricial pemfigoid",
            "kemisk brännskada",
            "kronisk blepharit",
            "herpes zoster oftalmicus"
        ],
        "treatment": "Temporärt: epilering (pincett - håller 4-6 veckor), lubricering, Permanent: elektrolys (destruera hårsäck), kryoterapi (frys hårsäck), laser ablation (argon), kirurgi vid omfattande: anterior lamellar repositionering, tarsalmargin rotation, cryotherapy till fransraden, behandla underliggande orsak (blepharit, inflammation), Prognos: recidiv vanligt efter epilering, bättre med permanent behandling",
        "kva": "ACF05 (trichiasisbehandling)",
        "differential_diagnoses": [
            "Entropion (hela locket inåtvänt)",
            "Distichiasis (extra fransrad posteriort)",
            "Epiblepharon (barn - hudfold)"
        ],
        "description": "Trichiasis är fransar som växer inåt och repar kornea. Skiljer från entropion där hela locket är inåtvänt. Vanligaste orsak globalt: trachom. Behandling: epilering (temporärt), elektrolys/kryoterapi/laser (permanent). Vid omfattande: kirurgisk rotation av ögonlockskant.",
        "severity": "moderate",
        "urgency": "urgent (korneal skada)"
    },
    {
        "name": "Distichiasis",
        "name_en": "Distichiasis",
        "icd10": "Q10.3",
        "symptoms": [
            "irritation och främmande kropps-känsla",
            "tårrinnande",
            "rodnad",
            "ofta mildare än trichiasis (extra fransar mjukare)",
            "kan vara asymtomatisk",
            "oftast bilateral"
        ],
        "anamnesis_questions": [
            "Har du haft detta sedan födseln?",
            "Finns det i familjen?",
            "Har du extra fransrad bakom den normala?",
            "Har du haft inflammation eller ärr?",
            "Är det bilateral?"
        ],
        "clinical_signs": [
            "extra fransrad växer från meibomkörtel-öppningar (posteriort på ögonlockskant)",
            "kongenitalt (primärt) eller förvärvat (sekundärt - ärr)",
            "extra fransar oftast mjukare och mindre irriterande än normala fransar",
            "kan vara sektoriell eller hel fransrad",
            "bilateral oftast vid kongenitalt"
        ],
        "risk_factors": [
            "kongenitalt (hereditet - autosomalt dominant)",
            "lymphedema-distichiasis syndrom (FOXC2-mutation)",
            "förvärvat: inflammation, ärr (trachom, SJS, etc.)"
        ],
        "treatment": "Asymtomatisk: ingen behandling, Symptomatisk: epilering (temporärt), elektrolys/kryoterapi/laser till extra fransrad, kirurgi: excision av extra fransrad med posteriort ögonlock, behandla underliggande om förvärvat, Lymphedema-distichiasis syndrom: screena för lymfödem, Prognos: kongenitalt ofta mild, behandling lindrande",
        "kva": "ACF05",
        "differential_diagnoses": [
            "Trichiasis (samma fransrad inåtvända)",
            "Metaplastiska fransar vid meibomkörtlar"
        ],
        "description": "Distichiasis är extra fransrad växer från meibomkörtel-öppningar. Kongenitalt (hereditet) eller förvärvat (ärr). Ofta mildare än trichiasis (mjukare fransar). Lymphedema-distichiasis syndrom: screena lymfödem. Behandling: elektrolys/kryoterapi/laser eller kirurgisk excision.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Blepharokalasis",
        "name_en": "Blepharochalasis",
        "icd10": "H02.3",
        "symptoms": [
            "recidiverande episoder av ögonlockssvullnad",
            "tunna, atrofiska ögonlock mellan episoder",
            "ptosis kan utvecklas",
            "debut tonår-ung vuxen",
            "episoder varar dagar",
            "bilateral ofta"
        ],
        "anamnesis_questions": [
            "Har du återkommande svullnader i ögonlocken?",
            "Började det i tonåren?",
            "Varar episoderna några dagar och försvinner?",
            "Har ögonlocken blivit tunnare och slappare?",
            "Har du utvecklat ptosis?",
            "Finns det i familjen?"
        ],
        "clinical_signs": [
            "mellan attacker: tunna, atrofiska ögonlock, synliga kärl, redundant hud",
            "under attack: ödem av övre ögonlock, ingen rodnad",
            "ptosis utvecklas (levator-skada från recidiverande inflammation)",
            "herniation av orbital fett (lysergul massa)",
            "kan ha tårkörtelprolaps",
            "ofta bilateral men kan vara asymmetrisk"
        ],
        "risk_factors": [
            "debut tonår-20 år (ungdomar)",
            "okänd etiologi",
            "kan vara hereditet (autosomalt dominant)",
            "Ascher syndrom (blepharokalasis + dubbelhaka + non-toxisk struma)"
        ],
        "treatment": "Under attack: kalla kompresser, eventuellt orala steroider om svår, mellan attacker: observation, Kirurgi efter attacker upphört (oftast slutar i 20-30 årsåldern): blefaroplastik för atrofisk hud, ptosis-korrigering om nödvändigt, avlägsna hernierande fett, behandla tårkörtelprolaps, Prognos: attacker minskar med åldern, kirurgi ger gott resultat",
        "kva": "ACB00 + ACE00",
        "differential_diagnoses": [
            "Angioödem (akut, allergi)",
            "Dermatokalasis (ingen recidiverande inflammation)",
            "Kontaktallergi"
        ],
        "description": "Blepharokalasis är sällsynt tillstånd med recidiverande ögonlocksödem hos ungdomar. Leder till tunna atrofiska ögonlock och ptosis. Attacker upphör oftast i 20-30 årsåldern. Blefaroplastik + ptosis-korrigering efter attacker slutat. Ascher syndrom: blepharokalasis + dubbelhaka + struma.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Floppy Eyelid Syndrome",
        "name_en": "Floppy Eyelid Syndrome",
        "icd10": "H02.8",
        "symptoms": [
            "kronisk ögonirritation",
            "mukoid sekretion på morgonen",
            "rodnade ögon",
            "ofta bilateral",
            "symptom värre på morgonen",
            "ofta överviktiga män",
            "sömnapné ofta samtidigt"
        ],
        "anamnesis_questions": [
            "Är du överviktig man?",
            "Sover du på mage/sida med ansiktet i kudden?",
            "Är ögonen värst röda på morgonen?",
            "Har du sömnapné?",
            "Kan du lätt vända ögonlocken?",
            "Har du mycket mukus på morgonen?"
        ],
        "clinical_signs": [
            "övre ögonlock mycket elastiskt och slapp (lätt everterar)",
            "kronisk papillär konjunktivit på övre tarsalkonjunktiva",
            "ögonlocken everterar lätt spontant (vid sömn)",
            "superior limbisk keratokonjunktivit (SLK) möjlig",
            "konjunktival hyperemi",
            "ofta bilateral"
        ],
        "risk_factors": [
            "övervikt/fetma",
            "manligt kön",
            "sömnapné (hög association - 90%!)",
            "sömner på mage med ansikte i kudde",
            "keratokonus association (20%)"
        ],
        "treatment": "Konservativt: sov på rygg!, skyddsglasögon eller ögonlockstejp nattetid, lubricering, behandla papillär konjunktivit (steroider/mastcellstabilisatorer), behandla sömnapné (CPAP), viktnedgång, Kirurgiskt om konservativt misslyckas: horizontal lid tightening (lateral tarsal strip), full-thickness wedge resection, Prognos: god med konservativ behandling oftast",
        "kva": "ACF10 (lid tightening)",
        "differential_diagnoses": [
            "Kronisk blepharit/konjunktivit av annan orsak",
            "Allergisk konjunktivit",
            "SLK av annan orsak"
        ],
        "description": "Floppy eyelid syndrome är slappa elastiska övre ögonlock som everterar spontant vid sömn. Typisk patient: överviktig man med sömnapné. Papillär konjunktivit från mekanisk irritation. Behandling: sov på rygg, tejp/skydd nattetid, behandla sömnapné. Kirurgi om refraktär.",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Dakryostenoos hos Barn (Kongenital Tårvägsstenosering)",
        "name_en": "Congenital Nasolacrimal Duct Obstruction",
        "icd10": "Q10.5",
        "symptoms": [
            "tårrinnande (epifora) hos spädbarn",
            "mukoid/purulent sekretion",
            "ofta från födseln eller första veckorna",
            "försämras vid förkylning",
            "ofta ensidig men kan vara bilateral",
            "inga smärtor (vs dakryocystit)"
        ],
        "anamnesis_questions": [
            "Hur gammal är barnet?",
            "Har det runnit tårar sedan födseln?",
            "Kommer det gul-grön sekretion?",
            "Är det bara ett öga?",
            "Har det varit svullnad eller rodnad vid näsan? (nej vid simpel stenosis)",
            "Försämras det vid förkylning?"
        ],
        "clinical_signs": [
            "epifora (tåroverflow)",
            "mukopurulent sekretion vid tryck på tårsäck",
            "ökad tear meniscus",
            "ingen svullnad över tårsäck (vs akut dakryocystit)",
            "tårväg kan ej spolas igenom",
            "Hasner's ventil (vid öppning till näsan) ej öppnad - vanligaste orsak"
        ],
        "risk_factors": [
            "mycket vanligt (6-20% av nyfödda)",
            "Hasner's ventil ej öppnad",
            "ofta bilateral (30%)",
            "Down syndrom (högre risk)"
        ],
        "treatment": "Konservativt (spontan öppning hos 90% inom 1 år): massage av tårsäck (nedåt mot näsan) 4-5x dagligen, rengöring med koksalt/rent vatten, antibiotika-droppar vid purulent sekretion, vänta till 12-15 månader, Probing (sondning) om ej spontan öppning vid 12-15 månader: nasolacrimala sondning i narkos, 90% lyckas efter 1:a probing, upprepa om behövs, balloon dacryoplasty om upprepade probings misslyckas, DCR (dacryocystorhinostomi) mycket sällsynt hos barn, Prognos: utmärkt - >95% löser sig",
        "kva": "CDH10 (nasolacrimal probing)",
        "differential_diagnoses": [
            "Kongenital dacryocystocele (svullnad vid födseln)",
            "Akut dakryocystit (smärta, rodnad, svullnad)",
            "Kongenital glaukom (stor kornea, korneal ödem)"
        ],
        "description": "Kongenital dakryostenoos är stenosering av tårvägen (Hasner's ventil ej öppnad). 6-20% av nyfödda. Epifora + mukoid sekretion. 90% spontan öppning inom 1 år. Behandling: massage + vänta till 12-15 månader. Probing om ej löst. Utmärkt prognos.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Förvärvad Dakryostenoos (Vuxen)",
        "name_en": "Acquired Nasolacrimal Duct Obstruction",
        "icd10": "H04.4",
        "symptoms": [
            "kroniskt tårrinnande (epifora)",
            "mukoid sekretion",
            "recidiverande dakryocystit möjlig",
            "ofta ensidig",
            "försämras i vind, kyla",
            "äldre kvinnor vanligast"
        ],
        "anamnesis_questions": [
            "Rinner tårar konstant ner på kinden?",
            "Hur länge har det pågått?",
            "Har du haft infektioner i tårsäcken?",
            "Försämras det ute i kyla/vind?",
            "Har du purulent sekretion?",
            "Har du haft trauma, inflammation eller operation?"
        ],
        "clinical_signs": [
            "epifora",
            "ökad tear lake",
            "tårväg kan ej spolas igenom (reflux)",
            "ingen tårsäcksvullnad (vs akut dakryocystit)",
            "eventuell mukoid sekretion vid tryck på tårsäck",
            "dacryoscintigrafi eller DCG (dacryocystografi) kan visa nivå av stenosering"
        ],
        "risk_factors": [
            "idiopatisk (vanligast - inflammation och fibros)",
            "post-inflammation (nasal/sinusinflammation)",
            "trauma (nasal/facial fraktur)",
            "tidigare nasal/sinuskirurgi",
            "läkemedel (5-FU, docetaxel)",
            "tumör (sällsynt men uteslut)",
            "sarkoidos, Wegeners"
        ],
        "treatment": "Uteslut andra orsaker till epifora först (entropion, ektropion, torrt öga, lagoftalmus), Kirurgisk (definitiv behandling): DCR (dacryocystorhinostomi) - extern eller endonasal, skapar ny passage från tårsäck till näsan, lycksam hos 85-95%, intubation med silikontub under läkning, Balloon dacryoplasty mindre invasivt (sämre resultat), Prognos: god med DCR",
        "kva": "CDH00 (DCR)",
        "differential_diagnoses": [
            "Funktionell epifora (tårproduktionsökning)",
            "Punktal stenosering",
            "Canalicular stenosering",
            "Tårsäckstumör (uteslut vid ensidig hos äldre!)"
        ],
        "description": "Förvärvad dakryostenoos är nasolakrimala stenosering hos vuxna. Kronisk epifora. Vanligast idiopatisk fibros hos äldre kvinnor. DCR (dacryocystorhinostomi) är definitiv behandling med 85-95% framgång. Uteslut tumör vid ensidig hos äldre (DCG/MRI).",
        "severity": "mild-moderate",
        "urgency": "routine"
    },
    {
        "name": "Punktal Stenosering",
        "name_en": "Punctal Stenosis",
        "icd10": "H04.5",
        "symptoms": [
            "tårrinnande (epifora)",
            "ofta bilateral",
            "gradvis försämring",
            "mindre mukoid sekretion än nasolakrimala stenosering",
            "kan vara iatrogen (från mediciner)"
        ],
        "anamnesis_questions": [
            "Rinner tårar?",
            "Använder du ögondroppar länge? (glaukomdroppar)",
            "Tar du cancer-mediciner?",
            "Har du haft inflammation i ögonlocken?",
            "Är tårpunkterna små eller stängda?",
            "Påverkas båda ögonen?"
        ],
        "clinical_signs": [
            "små eller stängda tårpunkter (normalt 0.3mm öppning)",
            "epifora",
            "kan ej sonderas eller spola tårvägen",
            "membranutbildning över punktum möjlig",
            "bilateral ofta"
        ],
        "risk_factors": [
            "ålder (involutionell)",
            "kronisk blepharit",
            "glaukomdroppar (särskilt prostaglandinanaloger och timolol)",
            "kemoterapi (5-FU, docetaxel)",
            "inflammatoriska tillstånd (SJS, pemfigoid)",
            "tidigare punktal plugs (iatrogent)"
        ],
        "treatment": "Dilatation av punktum (ofta temporärt resultat), puncctal snip (1-3 snips operation) - mer permanent, intubation med silikontub, avsluta utlösande medicin om möjligt, behandla blepharit, Prognos: god med puncctal snip",
        "kva": "CDG00 (punctal dilatation/snip)",
        "differential_diagnoses": [
            "Nasolakrimala stenosering",
            "Kanalikulär stenosering",
            "Funktionell epifora"
        ],
        "description": "Punktal stenosering är förträngning av tårpunkten. Ger epifora. Orsaker: ålder, blepharit, glaukomdroppar (prostaglandiner), kemoterapi. Ofta bilateral. Behandling: punctal dilatation (temporärt) eller punctal snip (permanent). God prognos.",
        "severity": "mild",
        "urgency": "routine"
    },
    {
        "name": "Kanalikulär Stenosering",
        "name_en": "Canalicular Stenosis",
        "icd10": "H04.5",
        "symptoms": [
            "epifora",
            "ofta efter herpes zoster oftalmicus eller HSV",
            "kan vara post-traumatisk",
            "ensidig ofta",
            "kan ha rodnad i mediala kantus"
        ],
        "anamnesis_questions": [
            "Har du haft herpes zoster oftalmicus?",
            "Har du haft trauma mot mediala ögonvrån?",
            "Använder du mediciner länge?",
            "Har du strålbehandlats?",
            "Är det ensidig epifora?"
        ],
        "clinical_signs": [
            "epifora",
            "kan spola men reflux från gemensam kanalikulus eller motstående punktum",
            "rodnad/inflammation i mediala kantus möjlig",
            "ofta ensidig",
            "DCG visar stenoseringsnivå"
        ],
        "risk_factors": [
            "herpes simplex/zoster (vanlig orsak!)",
            "trauma (särskilt medial kantus)",
            "läkemedel (antivirala, 5-FU, docetaxel)",
            "strålning",
            "kongenital (sällsynt)",
            "SJS, pemfigoid"
        ],
        "treatment": "Svårbehandlat: intubation med silikontub (Crawford tubes) - månad-3 månader, canaliculoplasty med DCR, conjunctivodacryocystorhinostomy (CDCR) med Jones tube (bypass med permanrör), behandla underliggande inflammation (herpes: antivirala), Prognos: sämre än nasolakrimala stenosering, ofta kräver Jones tube",
        "kva": "CDH05 (canaliculoplasty/Jones tube)",
        "differential_diagnoses": [
            "Nasolakrimala stenosering",
            "Punctal stenosering",
            "Gemensam kanalikulus stenosering"
        ],
        "description": "Kanalikulär stenosering är förträngning i tårkanalerna. Ofta efter herpes zoster/simplex eller trauma. Svårbehandlat. Intubation med silikontub eller Jones tube (permanent bypass). Sämre prognos än nasolakrimala stenosering.",
        "severity": "moderate",
        "urgency": "routine"
    },
    {
        "name": "Kongenital Dakryocystocele",
        "name_en": "Congenital Dacryocystocele",
        "icd10": "Q10.6",
        "symptoms": [
            "blåaktig svullnad under mediala kantus vid födseln",
            "epifora",
            "kan bli infekterad (dakryocystit)",
            "ibland nasalcysta samtidigt (andningssvårigheter)",
            "ofta ensidig"
        ],
        "anamnesis_questions": [
            "Fanns svullnaden vid födseln?",
            "Är den blåaktig?",
            "Har den blivit röd och ömöm? (infektion)",
            "Har barnet andningssvårigheter? (nasal cysta)"
        ],
        "clinical_signs": [
            "blå-grå cystisk svullnad under mediala kantus",
            "stenosering proximalt OCH distalt (dubbel stenosering)",
            "Hasner's ventil + Rosenmuller's ventil stenös",
            "kan bukta ut i näsan (intranasal cysta)",
            "kan bli infekterad (röd, ömmande)"
        ],
        "risk_factors": [
            "dubbel stenosering av tårvägen",
            "kongenital"
        ],
        "treatment": "Massage av tårsäcken (försök komprimera och öppna Hasner's ventil), kan spontan öppning ske, om infektion: systemiska antibiotika, om andningssvårigheter från nasal cysta: akut probing/marsupialisation, annars: probing vid 4-6 veckor (tidigare än simpel dakryostenoos), oftast behövs probing, Prognos: god med behandling",
        "kva": "CDH10 (probing)",
        "differential_diagnoses": [
            "Dermoid cysta (mer lateralt)",
            "Encefalocele (pulserar)",
            "Hemangiom",
            "Akut dakryocystit"
        ],
        "description": "Kongenital dakryocystocele är tårsäckscysta vid födseln från dubbel stenosering (proximal + distal). Blåaktig svullnad under mediala kantus. Kan ge nasalcysta med andningssvårigheter. Risk för infektion. Behandling: massage, tidig probing (4-6 veckor). God prognos.",
        "severity": "moderate (severe om andningssvårigheter)",
        "urgency": "urgent (om infektion eller andningspåverkan)"
    },
    {
        "name": "Tårsäckstumör",
        "name_en": "Lacrimal Sac Tumor",
        "icd10": "C69.5",
        "symptoms": [
            "ensidig epifora (tårrinnande)",
            "svullnad över tårsäck",
            "blodtårar (epistaxis via tårvägen) - varningssignal!",
            "kronisk dakryocystit som ej svarar på behandling",
            "ofta äldre patient"
        ],
        "anamnesis_questions": [
            "Har du ensidig epifora?",
            "Är du över 50 år?",
            "Har du blod i tårarna?",
            "Har du svullnad som växer?",
            "Har dakryocystit-behandling ej hjälpt?",
            "Rinner blod från näsan när du trycker på tårsäcken?"
        ],
        "clinical_signs": [
            "ensidig fast massa över tårsäck",
            "blodtårar (viktigt tecken!)",
            "nasolakrimala stenosering",
            "eventuell epistaxis",
            "DCG/MRI/CT visar massa i tårsäck",
            "vanligaste: papillom (benign) eller skivepitel-cancer (malign)"
        ],
        "risk_factors": [
            "ålder >50 år",
            "ensidig presentation",
            "papillom kan maligna degenera",
            "snuff (snus) möjligen"
        ],
        "treatment": "UTRED med bilddiagnostik (DCG, CT, MRI) före DCR!, biopsi nödvändig, Benign (papillom): komplett excision + DCR, Malign: radikal excision (ofta inkl. maxillektomi), strålning/kemoterapi beroende på typ och utbredning, onkologisk uppföljning, Prognos: beroende på typ - papillom god, malign varierande",
        "kva": "Varierar (excision, onkologisk behandling)",
        "differential_diagnoses": [
            "Kronisk dakryocystit",
            "Dakryocystocele",
            "Mucocele"
        ],
        "description": "Tårsäckstumör är sällsynt men viktig differentialdiagnos vid ensidig epifora hos äldre. BLODTÅRAR är varningssignal! Papillom vanligast (benign), skivepitelcancer är malign. ALLTID utred med DCG/CT/MRI före DCR vid atypisk presentation. Biopsi nödvändig.",
        "severity": "moderate-severe (malign)",
        "urgency": "urgent (utredning)"
    },
    {
        "name": "Medial Kantus Trauma/Lakrimala Systemskada",
        "name_en": "Medial Canthal Trauma/Lacrimal System Injury",
        "icd10": "S05.8",
        "symptoms": [
            "trauma mot medial ögonvrå",
            "blödning",
            "sårskada",
            "epifora (om tårväg skadad)",
            "medialt kantus-deformitet"
        ],
        "anamnesis_questions": [
            "Vad hände? (hundbit, trauma)",
            "Var träffades du? (medial vs lateral)",
            "Blöder det från tårpunkt?",
            "Har tårvägen skadats?",
            "Är medial canthal tendon skadad?"
        ],
        "clinical_signs": [
            "sårskada medial kantus",
            "avsliten punktum eller kanalikulus",
            "medialt kantus-displacement möjlig (medial canthal tendon avulsion)",
            "telecanthus (ökad avstånd mellan mediala kanthi)",
            "eventuell nasal/etmoidfraktur",
            "blödning från tårväg vid trauma"
        ],
        "risk_factors": [
            "hundbit (vanlig orsak)",
            "ansiktstrauma",
            "nasal/etmoidfraktur"
        ],
        "treatment": "AKUT reparation (inom 24-48h): mikrokirurgisk anastomosering av kanaliken över silikontub (Crawford tubes), tub lämnas 3-6 månader, medial canthal tendon-rekonstruktion om avsliten, antibiotika, tetanusprofylax, uppföljning för att säkerställa kanalikulär patency, Prognos: bäst om reparerat inom 24h, sämre om försenad",
        "kva": "Varierar (mikrokirurgisk reparation)",
        "differential_diagnoses": [
            "Andra ansiktstrauma utan tårvägsengagemang"
        ],
        "description": "Medial kantus-trauma kan skada tårvägen (kanalikulus). Hundbit vanlig orsak. AKUT mikrokirurgisk reparation inom 24-48h över silikontub ger bäst prognos. Försenad reparation ger sämre resultat. Medial canthal tendon-rekonstruktion om avulsion. Viktigt att känna igen tidigt!",
        "severity": "moderate-severe",
        "urgency": "emergency (inom 24-48h)"
    }
]
