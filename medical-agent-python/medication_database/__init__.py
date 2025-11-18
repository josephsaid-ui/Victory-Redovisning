"""
Medication Database - Läkemedelsdatabas
100 vanligaste ögonläkemedel

Denna modul innehåller detaljerad information om läkemedel inom ögonmedicin.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from glaucoma_medications import GLAUCOMA_MEDICATIONS

# Sammanfattning av övriga 80 läkemedel
ANTIBIOTICS = [
    {"name": "Ciloxan (Ciprofloxacin)", "category": "Antibiotikum - Fluorokinolon"},
    {"name": "Oftaquix (Levofloxacin)", "category": "Antibiotikum - Fluorokinolon"},
    {"name": "Vigamox (Moxifloxacin)", "category": "Antibiotikum - Fluorokinolon"},
    {"name": "Exocin (Ofloxacin)", "category": "Antibiotikum - Fluorokinolon"},
    {"name": "Kloramfenikol", "category": "Antibiotikum - Bredspektrum"},
    {"name": "Fucithalmic (Fusidinsyra)", "category": "Antibiotikum"},
    {"name": "Tobrex (Tobramycin)", "category": "Antibiotikum - Aminoglykosid"},
    {"name": "Gentalline (Gentamicin)", "category": "Antibiotikum - Aminoglykosid"},
    {"name": "Polytrim", "category": "Antibiotikum - Kombination"},
    {"name": "Vankomycin IV", "category": "Antibiotikum - Systemiskt"},
    {"name": "Ceftazidim IV", "category": "Antibiotikum - Cefalosporin"},
    {"name": "Ceftriaxon IV", "category": "Antibiotikum - Cefalosporin"},
    {"name": "Augmentin", "category": "Antibiotikum - Penicillin"},
    {"name": "Doxycyklin", "category": "Antibiotikum - Tetracyklin"},
    {"name": "Azitromycin oral/topikal", "category": "Antibiotikum - Makrolid"},
]  # 15 antibiotika

ANTI_INFLAMMATORY = [
    {"name": "Prednisolon 1%", "category": "Kortikosteroid - Topikal"},
    {"name": "Dexametason 0.1%", "category": "Kortikosteroid - Topikal"},
    {"name": "Fluorometolon (FML)", "category": "Kortikosteroid - svag"},
    {"name": "Lotemax (Loteprednol)", "category": "Kortikosteroid"},
    {"name": "Ozurdex implantat", "category": "Kortikosteroid - Intravitrealt"},
    {"name": "Triamcinolon intravitrealt", "category": "Kortikosteroid"},
    {"name": "Betametason subkonjunktivalt", "category": "Kortikosteroid"},
    {"name": "Prednisolon oralt", "category": "Kortikosteroid - Systemiskt"},
    {"name": "Acular (Ketorolak)", "category": "NSAID - Topikal"},
    {"name": "Voltaren Oftabak (Diklofenak)", "category": "NSAID"},
    {"name": "Nevanac (Nepafenac)", "category": "NSAID"},
    {"name": "Indometacin", "category": "NSAID"},
    {"name": "Flurbiprofen", "category": "NSAID"},
    {"name": "Xibrom (Bromfenac)", "category": "NSAID"},
    {"name": "Ibuprofen/Naproxen oralt", "category": "NSAID - Systemiskt"},
]  # 15 anti-inflammatoriska

LUBRICANTS = [
    {"name": "Hypromellos 0.3%", "category": "Tårsubstitut"},
    {"name": "Carbomer gel (Viscotears)", "category": "Tårsubstitut - Gel"},
    {"name": "Artelac (Hyaluronsyra)", "category": "Tårsubstitut"},
    {"name": "Refresh (CMC)", "category": "Tårsubstitut"},
    {"name": "Systane", "category": "Tårsubstitut"},
    {"name": "Optive", "category": "Tårsubstitut"},
    {"name": "Cationorm", "category": "Tårsubstitut - Emulsion"},
    {"name": "Lacrilube salva", "category": "Tårsubstitut - Salva"},
    {"name": "Restasis (Ciklosporin 0.05%)", "category": "Immunmodulerande"},
    {"name": "Ikervis (Ciklosporin 0.1%)", "category": "Immunmodulerande"},
]  # 10 smörjande

ANTIVIRAL_ANTIFUNGAL = [
    {"name": "Aciklovir salva", "category": "Antiviral - Topikal"},
    {"name": "Ganciklovir gel", "category": "Antiviral - Topikal"},
    {"name": "Aciklovir oralt", "category": "Antiviral - Systemiskt"},
    {"name": "Valaciklovir", "category": "Antiviral - Systemiskt"},
    {"name": "Ganciklovir IV/intravitrealt", "category": "Antiviral"},
    {"name": "Foscarnet", "category": "Antiviral"},
    {"name": "Natamycin 5%", "category": "Antimykotikum"},
    {"name": "Vorikonazol", "category": "Antimykotikum"},
    {"name": "Amfotericin B", "category": "Antimykotikum"},
    {"name": "Flukonazol", "category": "Antimykotikum"},
]  # 10 antivirala/antimykotika

ANTIALLERGIC = [
    {"name": "Olopatadin (Opatanol)", "category": "Antiallergisk"},
    {"name": "Ketotifen (Zaditen)", "category": "Antiallergisk"},
    {"name": "Azelastin", "category": "Antiallergisk"},
    {"name": "Emedastine", "category": "Antiallergisk"},
    {"name": "Kromoglikat", "category": "Mastcellsstabilisator"},
    {"name": "Nedokromil", "category": "Mastcellsstabilisator"},
    {"name": "Bepotas", "category": "Antiallergisk - Kombination"},
    {"name": "Azitromycin 1% (Azyter)", "category": "Antibiotikum/Antiinflammatorisk"},
]  # 8 antiallergiska

PUPIL_MEDICATIONS = [
    {"name": "Tropikamid 0.5-1%", "category": "Mydriasis"},
    {"name": "Ciklopentolat 1%", "category": "Cykloplegikum"},
    {"name": "Atropin 0.5-1%", "category": "Cykloplegikum - lång"},
    {"name": "Fenylefrin 2.5-10%", "category": "Mydriasis - alfa-agonist"},
    {"name": "Homatropin 2%", "category": "Cykloplegikum"},
]  # 5 pupillläkemedel

ANTI_VEGF = [
    {"name": "Eylea (Aflibercept)", "category": "Anti-VEGF"},
    {"name": "Lucentis (Ranibizumab)", "category": "Anti-VEGF"},
    {"name": "Avastin (Bevacizumab)", "category": "Anti-VEGF"},
    {"name": "Beovu (Brolucizumab)", "category": "Anti-VEGF"},
    {"name": "Vabysmo (Faricimab)", "category": "Anti-VEGF + Anti-Ang2"},
    {"name": "Iluvien implantat", "category": "Kortikosteroid - Intravitrealt"},
]  # 6 anti-VEGF

OTHER_MEDICATIONS = [
    {"name": "Fluorescein 1%", "category": "Diagnostiskt"},
    {"name": "Rose Bengal 1%", "category": "Diagnostiskt"},
    {"name": "Lissaminegrönt", "category": "Diagnostiskt"},
    {"name": "Tetrakain 0.5-1%", "category": "Lokalanestesi"},
    {"name": "Oxybuprokain 0.4%", "category": "Lokalanestesi"},
    {"name": "Proparakain 0.5%", "category": "Lokalanestesi"},
    {"name": "Lidokain gel 2%", "category": "Lokalanestesi"},
    {"name": "Mitomycin C 0.02-0.04%", "category": "Antimetabolit"},
]  # 8 övriga

# Samla alla läkemedel
ALL_MEDICATIONS = (
    GLAUCOMA_MEDICATIONS +  # 20
    ANTIBIOTICS +  # 15
    ANTI_INFLAMMATORY +  # 15
    LUBRICANTS +  # 10
    ANTIVIRAL_ANTIFUNGAL +  # 10
    ANTIALLERGIC +  # 8
    PUPIL_MEDICATIONS +  # 5
    ANTI_VEGF +  # 6
    OTHER_MEDICATIONS  # 8
)  # Total: 97 (behöver 3 till för 100)

# Lägg till 3 till för att nå 100
ADDITIONAL_MEDS = [
    {"name": "Alphagan P 0.15% (konserveringsmedelfri)", "category": "Alfa-2-agonist - konserveringsmedelfri"},
    {"name": "Cosopt PF (konserveringsmedelfri)", "category": "Kombination - konserveringsmedelfri"},
    {"name": "Simbrinza (Brinzolamid + Brimonidin)", "category": "Kombination - CAI + alfa-agonist"},
]

ALL_MEDICATIONS = ALL_MEDICATIONS + ADDITIONAL_MEDS


def get_all_medications():
    """Hämta alla läkemedel"""
    return ALL_MEDICATIONS


def get_statistics():
    """Få statistik om läkemedelsdatabasen"""
    stats = {
        "total": len(ALL_MEDICATIONS),
        "glaucoma": len(GLAUCOMA_MEDICATIONS),
        "antibiotics": len(ANTIBIOTICS),
        "anti_inflammatory": len(ANTI_INFLAMMATORY),
        "lubricants": len(LUBRICANTS),
        "antiviral_antifungal": len(ANTIVIRAL_ANTIFUNGAL),
        "antiallergic": len(ANTIALLERGIC),
        "pupil_meds": len(PUPIL_MEDICATIONS),
        "anti_vegf": len(ANTI_VEGF),
        "other": len(OTHER_MEDICATIONS),
        "additional": len(ADDITIONAL_MEDS),
    }
    return stats


if __name__ == "__main__":
    stats = get_statistics()
    print("=" * 60)
    print("LÄKEMEDELSDATABAS - STATISTIK")
    print("=" * 60)
    print(f"\nTotalt antal läkemedel: {stats['total']}")
    print("\nFördelning per kategori:")
    print("-" * 60)
    print(f"  Trycknedsättande (Glaukom):      {stats['glaucoma']:3d} läkemedel")
    print(f"  Antibiotika:                     {stats['antibiotics']:3d} läkemedel")
    print(f"  Anti-inflammatoriska:            {stats['anti_inflammatory']:3d} läkemedel")
    print(f"  Smörjande/Tårsubstitut:          {stats['lubricants']:3d} läkemedel")
    print(f"  Antivirala och Antimykotika:     {stats['antiviral_antifungal']:3d} läkemedel")
    print(f"  Antiallergiska:                  {stats['antiallergic']:3d} läkemedel")
    print(f"  Pupillpåverkande:                {stats['pupil_meds']:3d} läkemedel")
    print(f"  Anti-VEGF och Intravitreala:     {stats['anti_vegf']:3d} läkemedel")
    print(f"  Övriga (Diagnostiska, etc):      {stats['other']:3d} läkemedel")
    print(f"  Tillägg (kompletterar till 100): {stats['additional']:3d} läkemedel")
    print("\n" + "=" * 60)
    if stats['total'] == 100:
        print("✅ FRAMGÅNG! Databasen innehåller exakt 100 läkemedel!")
    else:
        print(f"⚠️  VARNING: Förväntat 100 läkemedel, har {stats['total']}")
    print("=" * 60)
