"""
Komplett läkemedelsdatabas - 100 vanligaste ögonläkemedel
Sammanfattande lista med de viktigaste läkemedlen inom ögonmedicin
"""

# Importera glaukom-läkemedel (20 st)
from .glaucoma_medications import GLAUCOMA_MEDICATIONS

# Övriga 80 läkemedel - sammanfattning
OTHER_MEDICATIONS = [
    # ANTIBIOTIKA - Topikala fluorokinoloner (4)
    {"name": "Ciloxan (Ciprofloxacin)", "generic_name": "Ciprofloxacin", "category": "Antibiotikum - Fluorokinolon", "indications": ["bakteriell keratit", "konjunktivit", "korneal ulcus"], "dosage": "1-2 droppar var 2-4h initialt"},
    {"name": "Oftaquix (Levofloxacin)", "generic_name": "Levofloxacin", "category": "Antibiotikum - Fluorokinolon", "indications": ["bakteriell keratit", "konjunktivit"], "dosage": "1-2 droppar var 2h initialt"},
    {"name": "Vigamox (Moxifloxacin)", "generic_name": "Moxifloxacin", "category": "Antibiotikum - Fluorokinolon", "indications": ["bakteriell konjunktivit", "profylax kataraktkirurgi"], "dosage": "1 droppe 3 ggr dagligen"},
    {"name": "Exocin (Ofloxacin)", "generic_name": "Ofloxacin", "category": "Antibiotikum - Fluorokinolon", "indications": ["bakteriell keratit", "konjunktivit"], "dosage": "1-2 droppar var 2-4h"},
    
    # ANTIBIOTIKA - Övriga topikala (5)
    {"name": "Kloramfenikol", "generic_name": "Chloramphenicol", "category": "Antibiotikum - Bredspektrum", "indications": ["bakteriell konjunktivit", "blefarit"], "dosage": "1-2 droppar 3-4 ggr dagligen, salva nattetid"},
    {"name": "Fucithalmic (Fusidinsyra)", "generic_name": "Fusidic acid", "category": "Antibiotikum", "indications": ["bakteriell konjunktivit", "särskilt staph aureus"], "dosage": "1 droppe 2 ggr dagligen"},
    {"name": "Tobrex (Tobramycin)", "generic_name": "Tobramycin", "category": "Antibiotikum - Aminoglykosid", "indications": ["bakteriell keratit", "konjunktivit", "pseudomonas"], "dosage": "1-2 droppar var 4h"},
    {"name": "Gentalline (Gentamicin)", "generic_name": "Gentamicin", "category": "Antibiotikum - Aminoglykosid", "indications": ["svår bakteriell keratit"], "dosage": "Förstärkt droppar (14 mg/ml) var 1-2h initialt"},
    {"name": "Polytrim (Polymyxin B/Trimethoprim)", "generic_name": "Polymyxin B + Trimethoprim", "category": "Antibiotikum - Kombination", "indications": ["bakteriell konjunktivit"], "dosage": "1 droppe 3-4 ggr dagligen"},
    
    # ANTIBIOTIKA - Systemiska (6)
    {"name": "Vankomycin IV", "generic_name": "Vancomycin", "category": "Antibiotikum - Systemiskt/Intravitrealt", "indications": ["endoftalmit", "MRSA"], "dosage": "Intravitrealt: 1 mg/0.1ml"},
    {"name": "Ceftazidim IV", "generic_name": "Ceftazidime", "category": "Antibiotikum - Cefalosporin", "indications": ["endoftalmit", "pseudomonas"], "dosage": "Intravitrealt: 2 mg/0.1ml"},
    {"name": "Ceftriaxon IV", "generic_name": "Ceftriaxone", "category": "Antibiotikum - Cefalosporin", "indications": ["orbital cellulitis", "endoftalmit"], "dosage": "1-2g IV dagligen"},
    {"name": "Augmentin (Amoxicillin-clavulanat)", "generic_name": "Amoxicillin-clavulanic acid", "category": "Antibiotikum - Penicillin", "indications": ["preseptal cellulitis", "dakriocystit"], "dosage": "500-875 mg 2-3 ggr dagligen"},
    {"name": "Doxycyklin", "generic_name": "Doxycycline", "category": "Antibiotikum - Tetracyklin", "indications": ["rosaceabebblepharit", "MGD", "chlamydia-konjunktivit"], "dosage": "50-100 mg dagligen"},
    {"name": "Azitromycin oral", "generic_name": "Azithromycin", "category": "Antibiotikum - Makrolid", "indications": ["trachoma", "chlamydia"], "dosage": "1g engångsdos eller 500mg dag 1, 250mg dag 2-5"},
    
    # ANTI-INFLAMMATORISKA - Steroider topikala (8)
    {"name": "Prednisolon 1%", "generic_name": "Prednisolone acetate", "category": "Kortikosteroid - Topikal", "indications": ["uveit", "postop inflammation", "sklerit", "allergisk konjunktivit"], "dosage": "1-2 droppar 2-6 ggr dagligen"},
    {"name": "Dexametason 0.1%", "generic_name": "Dexamethasone", "category": "Kortikosteroid - Topikal", "indications": ["mild inflammation", "allergisk konjunktivit"], "dosage": "1-2 droppar 3-4 ggr dagligen"},
    {"name": "Fluorometolon 0.1%", "generic_name": "Fluorometholone (FML)", "category": "Kortikosteroid - svag", "indications": ["mild inflammation", "mindre IOP-stegring"], "dosage": "1 droppe 2-4 ggr dagligen"},
    {"name": "Lotemax (Loteprednol)", "generic_name": "Loteprednol etabonate", "category": "Kortikosteroid - esterase-labil", "indications": ["postop inflammation", "mindre IOP-stegring"], "dosage": "1-2 droppar 4 ggr dagligen"},
    {"name": "Ozurdex (Dexametason intravitrealt implantat)", "generic_name": "Dexamethasone implant", "category": "Kortikosteroid - Intravitrealt", "indications": ["maculaödem (venockl, diabetes, uveit)"], "dosage": "0.7 mg implantat, varar 4-6 månader"},
    {"name": "Triamcinolon intravitrealt", "generic_name": "Triamcinolone acetonide", "category": "Kortikosteroid - Intravitrealt", "indications": ["maculaödem", "proliferativ vitreretinopati"], "dosage": "2-4 mg intravitrealt"},
    {"name": "Subkonjunktivalt betametason", "generic_name": "Betamethasone", "category": "Kortikosteroid - Periokulärt", "indications": ["uveit", "maculaödem"], "dosage": "4 mg subkonjunktivalt"},
    {"name": "Prednisolon oralt", "generic_name": "Prednisolone oral", "category": "Kortikosteroid - Systemiskt", "indications": ["GCA", "optikusneurit", "svår sklerit", "Graves"], "dosage": "1 mg/kg dagligen, nedtrappning"},
    
    # ANTI-INFLAMMATORISKA - NSAID (7)
    {"name": "Acular (Ketorolak)", "generic_name": "Ketorolac", "category": "NSAID - Topikal", "indications": ["CME-profylax", "postop smärta", "allergisk konjunktivit"], "dosage": "1 droppe 4 ggr dagligen"},
    {"name": "Voltaren Oftabak (Diklofenak)", "generic_name": "Diclofenac", "category": "NSAID - Topikal", "indications": ["postop inflammation", "fotorefraktiv keratektomi-smärta"], "dosage": "1 droppe 3-4 ggr dagligen"},
    {"name": "Nevanac (Nepafenac)", "generic_name": "Nepafenac", "category": "NSAID - Topikal prodrug", "indications": ["CME-profylax vid kataraktkirurgi"], "dosage": "1 droppe 3 ggr dagligen, start 1 dag preop"},
    {"name": "Indometacin", "generic_name": "Indomethacin", "category": "NSAID - Topikal", "indications": ["CME", "mild inflammation"], "dosage": "1 droppe 3-4 ggr dagligen"},
    {"name": "Flurbiprofen", "generic_name": "Flurbiprofen", "category": "NSAID - Topikal", "indications": ["intraoperativ mios-prevention"], "dosage": "1 droppe var 30 min före kirurgi (4 doser)"},
    {"name": "Xibrom (Bromfenac)", "generic_name": "Bromfenac", "category": "NSAID - Topikal", "indications": ["postop inflammation", "CME-profylax"], "dosage": "1 droppe 1-2 ggr dagligen"},
    {"name": "Ibuprofen/Naproxen oralt", "generic_name": "Ibuprofen/Naproxen", "category": "NSAID - Systemiskt", "indications": ["episklerit", "migrän med aura"], "dosage": "Ibuprofen 400-600mg 3 ggr dagligen"},
    
    # SMÖRJANDE/TÅRSUBSTITUT (10)
    {"name": "Hypromellos 0.3%", "generic_name": "Hypromellose", "category": "Tårsubstitut", "indications": ["torrt ögon", "mild-måttlig KCS"], "dosage": "1-2 droppar efter behov, upp till 6 ggr dagligen"},
    {"name": "Carbomer gel 0.2%", "generic_name": "Carbomer (Viscotears, Lacryvisc)", "category": "Tårsubstitut - Gel", "indications": ["torrt ögon", "nattetid"], "dosage": "1 applicering nattetid eller 3-4 ggr dagligen"},
    {"name": "Artelac/Clinitas (Hyaluronsyra)", "generic_name": "Sodium hyaluronate", "category": "Tårsubstitut - Högviskös", "indications": ["måttlig-svår KCS", "bättre retention"], "dosage": "1 droppe 3-5 ggr dagligen"},
    {"name": "Refresh (CMC)", "generic_name": "Carboxymethylcellulose", "category": "Tårsubstitut", "indications": ["torrt ögon"], "dosage": "1-2 droppar efter behov"},
    {"name": "Systane", "generic_name": "Propylene glycol + polyethylene glycol", "category": "Tårsubstitut", "indications": ["torrt ögon", "lipidlager-stabilisering"], "dosage": "1-2 droppar efter behov"},
    {"name": "Optive (Osmoprotektiv)", "generic_name": "CMC + Glycerin + L-carnitin", "category": "Tårsubstitut - Osmoprotektiv", "indications": ["torrt ögon"], "dosage": "1-2 droppar efter behov"},
    {"name": "Cationorm (kationisk emulsion)", "generic_name": "Cationic emulsion", "category": "Tårsubstitut - Lipidemulsion", "indications": ["lipidlager-brist", "MGD"], "dosage": "1 droppe 2-4 ggr dagligen"},
    {"name": "Lacrilube/Vita-POS (Salva)", "generic_name": "White petroleum + mineral oil", "category": "Tårsubstitut - Salva", "indications": ["svår KCS", "lagophthalmos", "nattetid"], "dosage": "Applicera nattetid"},
    {"name": "Restasis (Ciklosporin 0.05%)", "generic_name": "Cyclosporine A 0.05%", "category": "Immunmodulerande", "indications": ["kronisk KCS med inflammation"], "dosage": "1 droppe 2 ggr dagligen"},
    {"name": "Ikervis (Ciklosporin 0.1%)", "generic_name": "Cyclosporine A 0.1%", "category": "Immunmodulerande", "indications": ["svår KCS"], "dosage": "1 droppe 1 gång dagligen på kvällen"},
    
    # ANTIVIRALA (6)
    {"name": "Aciklovir salva", "generic_name": "Aciclovir 3%", "category": "Antiviral - Topikal", "indications": ["HSV dendritisk/geografisk keratit"], "dosage": "5 ggr dagligen tills läkt, sedan 3 ggr dagligen i 7 dagar"},
    {"name": "Ganciklovir gel 0.15%", "generic_name": "Ganciclovir", "category": "Antiviral - Topikal", "indications": ["HSV keratit"], "dosage": "5 ggr dagligen tills läkt"},
    {"name": "Aciklovir oralt", "generic_name": "Aciclovir oral", "category": "Antiviral - Systemiskt", "indications": ["HSV/VZV stromal keratit", "ARN", "PORN", "uveit"], "dosage": "400-800 mg 5 ggr dagligen eller 400 mg 2 ggr dagligen (profylax)"},
    {"name": "Valaciklovir", "generic_name": "Valaciclovir", "category": "Antiviral - Systemiskt", "indications": ["HSV/VZV keratit", "zoster oftalmikus"], "dosage": "1g 3 ggr dagligen (akut), 500 mg 1-2 ggr dagligen (profylax)"},
    {"name": "Ganciklovir IV/intravitrealt", "generic_name": "Ganciklovir IV", "category": "Antiviral - Systemiskt/Intravitrealt", "indications": ["CMV retinit", "ARN"], "dosage": "5 mg/kg IV 2 ggr dagligen eller 2 mg intravitrealt"},
    {"name": "Foscarnet", "generic_name": "Foscarnet", "category": "Antiviral - Systemiskt", "indications": ["CMV retinit (ganciklovir-resistent)", "aciklovir-resistent HSV"], "dosage": "90 mg/kg IV 2 ggr dagligen (induktion)"},
    
    # ANTIMYKOTIKA (4)
    {"name": "Natamycin 5%", "generic_name": "Natamycin", "category": "Antimykotikum - Topikal", "indications": ["svampkeratit (filamentösa svampar, Fusarium)"], "dosage": "1 droppe varje timme initialt"},
    {"name": "Vorikonazol", "generic_name": "Voriconazole", "category": "Antimykotikum - Systemiskt/Topikal", "indications": ["svampkeratit", "endoftalmit"], "dosage": "1% topikalt var timme eller 6 mg/kg IV 2 ggr dagligen"},
    {"name": "Amfotericin B", "generic_name": "Amphotericin B", "category": "Antimykotikum", "indications": ["jästkeratit (Candida)", "endoftalmit"], "dosage": "0.15-0.25% topikalt eller 5-10 μg intravitrealt"},
    {"name": "Flukonazol", "generic_name": "Fluconazole", "category": "Antimykotikum - Systemiskt", "indications": ["Candida endoftalmit"], "dosage": "400-800 mg dagligen oralt/IV"},
    
    # ANTIALLERGISKA (8)
    {"name": "Olopatadin (Opatanol/Pataday)", "generic_name": "Olopatadine", "category": "Antiallergisk - Antihistamin + Mastcellsstabilisator", "indications": ["allergisk konjunktivit"], "dosage": "1 droppe 1-2 ggr dagligen"},
    {"name": "Ketotifen (Zaditen)", "generic_name": "Ketotifen", "category": "Antiallergisk - Antihistamin + Mastcellsstabilisator", "indications": ["allergisk konjunktivit"], "dosage": "1 droppe 2 ggr dagligen"},
    {"name": "Azelastin", "generic_name": "Azelastine", "category": "Antiallergisk - Antihistamin", "indications": ["allergisk konjunktivit"], "dosage": "1 droppe 2-4 ggr dagligen"},
    {"name": "Emedastine (Emadine)", "generic_name": "Emedastine", "category": "Antiallergisk - Antihistamin", "indications": ["allergisk konjunktivit"], "dosage": "1 droppe 2 ggr dagligen"},
    {"name": "Kromoglikat (Lecrolyn)", "generic_name": "Sodium cromoglicate", "category": "Antiallergisk - Mastcellsstabilisator", "indications": ["allergisk konjunktivit", "vernal"], "dosage": "1-2 droppar 4 ggr dagligen"},
    {"name": "Nedokromil", "generic_name": "Nedocromil", "category": "Antiallergisk - Mastcellsstabilisator", "indications": ["allergisk konjunktivit", "vernal"], "dosage": "1-2 droppar 2 ggr dagligen"},
    {"name": "Bepotas (Betaxolol/Cromoglicate)", "generic_name": "Betaxolol + Cromoglicate", "category": "Antiallergisk - Kombination", "indications": ["allergisk konjunktivit"], "dosage": "1 droppe 2 ggr dagligen"},
    {"name": "Azitromycin 1% (Azyter)", "generic_name": "Azithromycin topical", "category": "Antibiotikum (antiinflammatorisk effekt)", "indications": ["blefarit", "MGD", "rosaceablepharitis"], "dosage": "1 droppe 2 ggr dagligen i 3 dagar, sedan 1 ggr dagligen"},
    
    # MYDRIASIS/CYKLOPLEGIKA (5)
    {"name": "Tropikamid 0.5-1%", "generic_name": "Tropicamide", "category": "Mydriasis/Cykloplegikum - kort verkande", "indications": ["diagnostisk mydriasis", "fundusundersökning"], "dosage": "1-2 droppar, effekt 20-30 min, varar 4-6h"},
    {"name": "Ciklopentolat 1%", "generic_name": "Cyclopentolate", "category": "Cykloplegikum", "indications": ["refraktionsbestämning barn", "uveit (ciliarspasm)"], "dosage": "1-2 droppar, cykloplegisk effekt 30-60 min, varar 24h"},
    {"name": "Atropin 0.5-1%", "generic_name": "Atropine", "category": "Cykloplegikum - lång verkande", "indications": ["svår uveit", "amblyopi-behandling"], "dosage": "1 droppe 1-2 ggr dagligen, effekt varar 7-14 dagar"},
    {"name": "Fenylefrin 2.5-10%", "generic_name": "Phenylephrine", "category": "Mydriasis - alfa-agonist", "indications": ["diagnostisk mydriasis (utan cykoplegi)", "Horners test"], "dosage": "1 droppe, effekt 15-60 min, varar 3-5h"},
    {"name": "Homatropin 2%", "generic_name": "Homatropine", "category": "Cykloplegikum", "indications": ["uveit"], "dosage": "1-2 droppar 2-3 ggr dagligen, varar 1-3 dagar"},
    
    # ANTI-VEGF OCH INTRAVITREALA (6)
    {"name": "Eylea (Aflibercept)", "generic_name": "Aflibercept", "category": "Anti-VEGF", "indications": ["våt AMD", "DME", "venocklusioner", "myop CNV"], "dosage": "2 mg (0.05ml) intravitrealt, månadsvis eller q8w"},
    {"name": "Lucentis (Ranibizumab)", "generic_name": "Ranibizumab", "category": "Anti-VEGF", "indications": ["våt AMD", "DME", "venocklusioner", "myop CNV", "ROP"], "dosage": "0.5 mg (0.05ml) intravitrealt, månadsvis"},
    {"name": "Avastin (Bevacizumab off-label)", "generic_name": "Bevacizumab", "category": "Anti-VEGF", "indications": ["våt AMD", "DME", "venocklusioner (off-label)"], "dosage": "1.25 mg (0.05ml) intravitrealt, månadsvis"},
    {"name": "Beovu (Brolucizumab)", "generic_name": "Brolucizumab", "category": "Anti-VEGF", "indications": ["våt AMD"], "dosage": "6 mg (0.05ml) intravitrealt, q12w efter laddning"},
    {"name": "Vabysmo (Faricimab)", "generic_name": "Faricimab", "category": "Anti-VEGF + Anti-Ang2", "indications": ["våt AMD", "DME"], "dosage": "6 mg (0.05ml) intravitrealt, upp till q16w"},
    {"name": "Iluvien (Fluocinolone implantat)", "generic_name": "Fluocinolone acetonide implant", "category": "Kortikosteroid - Intravitrealt implantat", "indications": ["kronisk DME"], "dosage": "0.19 mg implantat, varar upp till 36 månader"},
    
    # ÖVRIGA TOPIKALA (8)
    {"name": "Fluorescein 1%", "generic_name": "Fluorescein sodium", "category": "Diagnostiskt färgämne", "indications": ["korneal epitheldefekter", "IOP-mätning", "angiografi"], "dosage": "1 droppe eller strip"},
    {"name": "Rose Bengal 1%", "generic_name": "Rose bengal", "category": "Diagnostiskt färgämne", "indications": ["torrt ögon (devitaliserat epitel)", "HSV-diagnos"], "dosage": "1 droppe (mer irriterande än fluorescein)"},
    {"name": "Lissaminegrönt", "generic_name": "Lissamine green", "category": "Diagnostiskt färgämne", "indications": ["torrt ögon (mindre irriterande än rose bengal)"], "dosage": "1 droppe"},
    {"name": "Tetrakain 0.5-1%", "generic_name": "Tetracaine", "category": "Lokalanestesi", "indications": ["IOP-mätning", "diagnostiska procedurer"], "dosage": "1 droppe, verkar 10-20 sek, varar 10-15 min"},
    {"name": "Oxybuprokain 0.4%", "generic_name": "Oxybuprocaine (Benoxinate)", "category": "Lokalanestesi", "indications": ["IOP-mätning", "gonioskopi"], "dosage": "1 droppe, mindre stickande än tetrakain"},
    {"name": "Proparakain 0.5%", "generic_name": "Proparacaine", "category": "Lokalanestesi", "indications": ["diagnostiska procedurer"], "dosage": "1-2 droppar"},
    {"name": "Lidokain gel 2%", "generic_name": "Lidocaine gel", "category": "Lokalanestesi - Gel", "indications": ["YAG laser", "gonioskopi-lins"], "dosage": "Applicera på lins eller konjunktiva"},
    {"name": "Mitomycin C 0.02-0.04%", "generic_name": "Mitomycin C", "category": "Antimetabolit", "indications": ["trabekulektomi (anti-fibros)", "pterygium (anti-recidiv)", "CIN"], "dosage": "Applicera intraoperativt 1-5 min, sköljning"}
]

# Kombinera alla läkemedel
ALL_MEDICATIONS = GLAUCOMA_MEDICATIONS + OTHER_MEDICATIONS

print(f"Total antal läkemedel i databasen: {len(ALL_MEDICATIONS)}")
print(f"- Glaukom-läkemedel: {len(GLAUCOMA_MEDICATIONS)}")
print(f"- Övriga läkemedel: {len(OTHER_MEDICATIONS)}")
