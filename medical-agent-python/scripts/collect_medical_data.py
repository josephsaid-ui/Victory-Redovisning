"""
Script för att samla medicinsk data från olika källor

Använd detta för att bygga upp din medicinska kunskapsbas.
"""
import asyncio
import json
from pathlib import Path
from typing import List, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MedicalDataCollector:
    """Samlar medicinsk data från olika källor"""

    def __init__(self):
        self.diseases = []
        self.medications = []
        self.treatments = []

    def load_curated_diseases(self) -> List[Dict]:
        """
        Ladda manuellt curerad data för vanligaste ögonsjukdomar

        Detta är den rekommenderade startpunkten - 20 sjukdomar
        som täcker ~90% av fall i ögonmottagning
        """
        curated_diseases = [
            # 1. Katarakt
            {
                "name": "Katarakt (Grå starr)",
                "icd10": "H25",
                "description": """
                Katarakt är en grumling av ögats lins som leder till gradvis synförsämring.
                Det är den vanligaste orsaken till behandlingsbar blindhet och påverkar främst
                personer över 60 år.
                """,
                "symptoms": [
                    "suddig syn",
                    "halos runt lampor",
                    "försämrad syn i mörker",
                    "färger verkar blekare",
                    "behov av starkare glasögon",
                    "dubbelseende i ett öga"
                ],
                "risk_factors": [
                    "ålder >60 år",
                    "diabetes",
                    "rökning",
                    "långvarig kortisonbehandling",
                    "UV-exponering",
                    "ögontrauma"
                ],
                "anamnesis_questions": [
                    "Ser du halos eller ringar runt lampor, särskilt på kvällen?",
                    "Har synen försämrats gradvis under flera månader/år?",
                    "Har du svårt att köra bil på natten?",
                    "Verkar färger mindre klara än tidigare?",
                    "Har du diabetes?"
                ],
                "examination": [
                    "Visus",
                    "Slitslampundersökning (linsgrumling)",
                    "Funduskopi (måste se genom katarakten)"
                ],
                "treatment": """
                Kataraktoperation med fakoemulsifikation och inläggning av konstgjord lins (IOL).
                Operation indicerad när synförsämringen påverkar dagliga aktiviteter eller
                visus <0.5.
                """,
                "kva": "CJE00",
                "medications": [],
                "urgency": "non-urgent",
                "red_flags": [],
                "prognosis": "Excellent med operation. 95% når visus 0.5 eller bättre.",
                "follow_up": "Kontroll dag 1 och vecka 4 postoperativt"
            },

            # 2. Glaukom
            {
                "name": "Primär öppenvinkelglaukom",
                "icd10": "H40.1",
                "description": """
                Kronisk progressiv optikusneuropati karakteriserad av typiska synfältsbortfall
                och optikusskada, ofta associerad med förhöjt intraokulart tryck.
                """,
                "symptoms": [
                    "synfältsbortfall (perifer syn först)",
                    "förhöjt ögontryck",
                    "ofta symtomfritt i tidigt skede",
                    "tunnelseende i sena stadier"
                ],
                "risk_factors": [
                    "ålder >40 år",
                    "hereditet",
                    "högt ögontryck",
                    "diabetes",
                    "högt blodtryck",
                    "migrän",
                    "hög närsynthet"
                ],
                "anamnesis_questions": [
                    "Har du märkt förändringar i din perifera syn?",
                    "Har någon i din familj glaukom?",
                    "Har du diabetes eller högt blodtryck?",
                    "Använder du kortison (tabletter eller droppar)?"
                ],
                "examination": [
                    "Ögontryck (Goldmann tonometri)",
                    "Synfält (Humphrey)",
                    "OCT papilla (nervfiberlager)",
                    "Gonioskopi (kammarvinkel)"
                ],
                "treatment": """
                Målstyrd behandling för att sänka ögontrycket:
                1:a linje: Prostaglandinanaloger (Latanoprost)
                2:a linje: Laser (SLT)
                3:e linje: Kirurgi (Trabekulektomi)
                """,
                "kva": "CJD00 (trabekulektomi)",
                "medications": ["Latanoprost", "Timolol", "Dorzolamid", "Brinzolamid"],
                "urgency": "semi-urgent",
                "red_flags": [
                    "akut tryckökning >30 mmHg",
                    "smärta + röda ögon (akut vinkelblockglaukom)"
                ],
                "prognosis": "God prognos med tidig diagnos och behandling",
                "follow_up": "Ögontryck var 3-6 mån, synfält årligen"
            },

            # 3. Retinal avlossning
            {
                "name": "Retinal avlossning (Rhegmatogen)",
                "icd10": "H33.0",
                "description": """
                AKUT tillstånd där sensorisk retina separerar från retinalt pigmentepitel
                genom ett retinalt hål eller bristning.
                """,
                "symptoms": [
                    "plötsliga ljusblixtar",
                    "många nya floaters",
                    "gardinsymptom (skugga i synfältet)",
                    "plötslig synförlust"
                ],
                "risk_factors": [
                    "hög närsynthet",
                    "ögontrauma",
                    "tidigare kataraktkirurgi",
                    "hereditet",
                    "retinal degeneration"
                ],
                "anamnesis_questions": [
                    "Ser du plötsliga ljusblixtar?",
                    "Ser du många nya svävande prickar eller fläckar?",
                    "Ser du en gardin eller skugga som täcker delar av synfältet?",
                    "Kom detta plötsligt?",
                    "Har du haft ögontrauma?"
                ],
                "examination": [
                    "AKUT funduskopi med skleral indentation",
                    "OCT makula",
                    "Ultraljud B-scan om oklart media"
                ],
                "treatment": """
                AKUT kirurgi inom 24-48 timmar:
                - Vitrektomi + gastamponad
                - Skleral buckle
                - Pneumatisk retinopex (vissa fall)
                - Laser/kryoterapi av hål
                """,
                "kva": "CJC30 (vitrektomi)",
                "medications": [],
                "urgency": "ACUTE",
                "red_flags": [
                    "makula-off (central syn påverkad)",
                    "symtom >7 dagar (sämre prognos)"
                ],
                "prognosis": "85-90% anatomisk återläggning, visus beror på makula-status",
                "follow_up": "Täta kontroller första månaden, sedan 3-6 mån"
            },

            # 4. AMD
            {
                "name": "Åldersrelaterad makuladegeneration (AMD)",
                "icd10": "H35.3",
                "description": """
                Degenerativ sjukdom i makula (gula fläcken) som ger central synförlust.
                Finns i torr (90%) och våt (10%) form.
                """,
                "symptoms": [
                    "böjda linjer (Amsler grid)",
                    "central synförlust",
                    "svårt att läsa",
                    "förvrängd syn (metamorfopsi)",
                    "mörk fläck i centrum",
                    "nedsatt kontrastkänslighet"
                ],
                "risk_factors": [
                    "ålder >65 år",
                    "rökning (största påverkbara faktorn)",
                    "hereditet",
                    "ljus ögonfärg",
                    "kardiovaskulär sjukdom"
                ],
                "anamnesis_questions": [
                    "Ser linjer böjda när du tittar på rutmönster?",
                    "Har du svårt att läsa trots glasögon?",
                    "Ser du en mörk fläck i centrum av synfältet?",
                    "Röker du eller har du rökt?",
                    "Har någon i familjen AMD?"
                ],
                "examination": [
                    "Visus (nära och distans)",
                    "Amsler grid",
                    "Funduskopi (drusen, pigmentförändringar)",
                    "OCT makula",
                    "Angiografi (ICGA/FA) vid våt AMD"
                ],
                "treatment": """
                Torr AMD: AREDS2 vitaminer, rökstopp, livsstilsråd
                Våt AMD: Anti-VEGF injektioner (Ranibizumab, Aflibercept)
                KVÅ: CJB10 (intravitreal injektion)
                """,
                "kva": "CJB10",
                "medications": ["AREDS2", "Lucentis", "Eylea"],
                "urgency": "våt AMD = urgent (inom dagar), torr = non-urgent",
                "red_flags": ["plötslig försämring = våt AMD"],
                "prognosis": "Våt AMD: 30-40% får tillbaka syn med behandling",
                "follow_up": "Våt AMD: månadsinjektioner initialt, sedan PRN/T&E"
            },

            # 5. Diabetesretinopati
            {
                "name": "Diabetesretinopati",
                "icd10": "E11.3",
                "description": """
                Mikrovaskulär komplikation av diabetes som påverkar retina.
                Ledande orsak till blindhet i arbetsför ålder.
                """,
                "symptoms": [
                    "ofta symtomfritt tidigt",
                    "suddig syn",
                    "floaters",
                    "synfältsbortfall",
                    "plötslig synförlust (vid blödning)"
                ],
                "risk_factors": [
                    "dålig glukoskontroll (HbA1c)",
                    "lång diabetesduration",
                    "högt blodtryck",
                    "höga blodfetter",
                    "njursvikt",
                    "graviditet"
                ],
                "anamnesis_questions": [
                    "Hur länge har du haft diabetes?",
                    "Hur är din blodsockerkontroll? Vet du ditt senaste HbA1c?",
                    "Har du högt blodtryck?",
                    "När kontrollerade du ögonen senast?"
                ],
                "examination": [
                    "Funduskopi i mydriasis",
                    "OCT makula (ödem)",
                    "Angiografi vid behov",
                    "Klassificering (NPDR vs PDR)"
                ],
                "treatment": """
                Prevention: Optimal glukoskontroll, blodtryckskontroll

                Proliferativ DR: Panretinal fotokoagulation (PRP) KVÅ: CJF20
                Makulaödem: Anti-VEGF injektioner, focal/grid laser
                Vitrektomi vid blödning/traktion
                """,
                "kva": "CJF20 (PRP), CJB10 (anti-VEGF)",
                "medications": ["Lucentis", "Eylea", "Avastin"],
                "urgency": "PDR = urgent, mild NPDR = non-urgent",
                "red_flags": ["preretinal blödning", "traktionsablatio"],
                "prognosis": "God med tidig upptäckt och optimal diabeteskontroll",
                "follow_up": "Beroende på stadium: 3-12 månader"
            },

            # Lägg till fler sjukdomar här...
            # 6. Torra ögon
            # 7. Konjunktivit
            # 8. Keratit
            # 9. Uveit
            # 10. Närsynthet
            # ... upp till 20 st

        ]

        logger.info(f"Loaded {len(curated_diseases)} curated diseases")
        return curated_diseases

    def load_curated_medications(self) -> List[Dict]:
        """Ladda curerad läkemedelsinformation"""
        medications = [
            {
                "name": "Latanoprost",
                "brand_names": ["Xalatan", "Latanoprost"],
                "atc": "S01EE01",
                "category": "Prostaglandinanalog",
                "indication": "Glaukom, okulär hypertension",
                "mechanism": "Ökar uveoskleralt utflöde av kammarvatten",
                "dosage": "1 droppe i drabbat öga 1 gång dagligen på kvällen",
                "administration": "Ögondroppar",
                "side_effects": [
                    "Hyperemi (rodnad)",
                    "Ökad irispigmentering (permanent)",
                    "Förlängda fransar",
                    "Periorbitalt ödem",
                    "Makulaödem (sällsynt)"
                ],
                "contraindications": ["Överkänslighet"],
                "interactions": [],
                "pregnancy_category": "C",
                "cost": "~100 kr/flaska (generika)",
                "notes": "Första linjens behandling för glaukom. Tag ur linser före dosering."
            },
            {
                "name": "Timolol",
                "brand_names": ["Timoptic", "Timolol"],
                "atc": "S01ED01",
                "category": "Betablockerare",
                "indication": "Glaukom, okulär hypertension",
                "mechanism": "Minskar produktion av kammarvatten",
                "dosage": "1 droppe 2 gånger dagligen",
                "administration": "Ögondroppar",
                "side_effects": [
                    "Lokal: Sveda, rodnad",
                    "Systemisk: Bradykardi, bronkospasm, trötthet"
                ],
                "contraindications": [
                    "Astma",
                    "KOL",
                    "Bradykardi",
                    "AV-block",
                    "Hjärtsvikt"
                ],
                "interactions": ["Systemiska betablockerare", "Kalciumantagonister"],
                "pregnancy_category": "C",
                "cost": "~80 kr/flaska",
                "notes": "VARNING: Systemisk absorption kan ge bradykardi och bronkospasm"
            },
            # Lägg till fler läkemedel...
        ]

        logger.info(f"Loaded {len(medications)} medications")
        return medications

    async def fetch_from_pubmed(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Hämta forskningsartiklar från PubMed

        Kräver: pip install biopython
        """
        try:
            from Bio import Entrez
            Entrez.email = "your.email@example.com"  # REQUIRED by NCBI

            logger.info(f"Searching PubMed for: {query}")

            # Search
            handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
            record = Entrez.read(handle)
            handle.close()

            articles = []

            # Fetch details
            for pmid in record["IdList"]:
                handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="xml")
                article_data = Entrez.read(handle)
                handle.close()

                try:
                    article = article_data['PubmedArticle'][0]
                    medline = article['MedlineCitation']
                    article_info = medline['Article']

                    # Extract abstract
                    abstract_parts = article_info.get('Abstract', {}).get('AbstractText', [])
                    abstract = ' '.join([str(part) for part in abstract_parts])

                    articles.append({
                        "pmid": pmid,
                        "title": str(article_info.get('ArticleTitle', '')),
                        "abstract": abstract,
                        "year": str(medline.get('DateCompleted', {}).get('Year', '')),
                        "journal": str(article_info.get('Journal', {}).get('Title', '')),
                        "source": "PubMed"
                    })
                except (KeyError, IndexError) as e:
                    logger.warning(f"Could not parse article {pmid}: {e}")

            logger.info(f"Fetched {len(articles)} articles from PubMed")
            return articles

        except ImportError:
            logger.error("biopython not installed. Run: pip install biopython")
            return []

    def export_to_json(self, filename: str = "medical_data.json"):
        """Exportera all insamlad data till JSON"""
        data = {
            "diseases": self.load_curated_diseases(),
            "medications": self.load_curated_medications(),
            "metadata": {
                "version": "1.0",
                "created": "2024-01-15",
                "source": "Curated by ophthalmologist"
            }
        }

        output_path = Path(__file__).parent.parent / "data" / filename
        output_path.parent.mkdir(exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logger.info(f"Exported data to {output_path}")
        return output_path


async def main():
    """Huvudfunktion"""
    collector = MedicalDataCollector()

    # 1. Ladda curated data
    diseases = collector.load_curated_diseases()
    medications = collector.load_curated_medications()

    print(f"\n✅ Loaded {len(diseases)} diseases")
    print(f"✅ Loaded {len(medications)} medications")

    # 2. Optional: Hämta från PubMed
    print("\n📚 Fetching from PubMed...")
    pubmed_articles = await collector.fetch_from_pubmed(
        "cataract treatment guidelines",
        max_results=5
    )
    print(f"✅ Found {len(pubmed_articles)} PubMed articles")

    # 3. Exportera till JSON
    print("\n💾 Exporting data...")
    output_file = collector.export_to_json()
    print(f"✅ Data exported to: {output_file}")

    print("\n🎉 Data collection complete!")
    print("\nNext step: Run import_to_database.py to load into Supabase")


if __name__ == "__main__":
    asyncio.run(main())
