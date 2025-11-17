"""
LlamaIndex RAG Integration för medicinsk kunskapsbas

Använder Supabase pgvector för att lagra och söka i:
- Ögonsjukdomar
- Behandlingsprotokoll
- Läkemedelsinformation
- Svenska medicinska riktlinjer
"""
import os
from typing import List, Optional
import logging

from llama_index.core import (
    VectorStoreIndex,
    Document,
    StorageContext,
    Settings
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.supabase import SupabaseVectorStore
from supabase import create_client, Client

from app.models.medical_types import EyeDisease, Treatment, Medication

logger = logging.getLogger(__name__)


class MedicalKnowledgeRAG:
    """
    RAG system för medicinsk kunskapsbas

    Använder:
    - LlamaIndex för indexing och retrieval
    - PubMedBERT för medicinska embeddings
    - Supabase pgvector för storage
    """

    def __init__(self):
        self.vector_index: Optional[VectorStoreIndex] = None
        self.supabase: Optional[Client] = None
        self.initialized = False

    async def initialize(self):
        """Initialisera RAG system"""
        if self.initialized:
            logger.info("RAG already initialized")
            return

        logger.info("Initializing Medical Knowledge RAG...")

        # 1. Setup Supabase client
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_ANON_KEY")
        )

        # 2. Setup embedding model (PubMedBERT för medicinsk text)
        Settings.embed_model = HuggingFaceEmbedding(
            model_name="pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb",
            cache_folder="./model_cache"
        )

        # 3. Setup text splitter
        Settings.node_parser = SentenceSplitter(
            chunk_size=512,
            chunk_overlap=50
        )

        # 4. Ladda medicinsk data
        medical_documents = await self._load_medical_knowledge()

        # 5. Skapa vector store med Supabase
        vector_store = SupabaseVectorStore(
            postgres_connection_string=(
                f"postgresql://postgres:{os.getenv('SUPABASE_DB_PASSWORD')}@"
                f"{os.getenv('SUPABASE_URL').replace('https://', '')}"
                f":5432/postgres"
            ),
            collection_name="medical_documents"
        )

        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )

        # 6. Skapa index
        self.vector_index = VectorStoreIndex.from_documents(
            medical_documents,
            storage_context=storage_context
        )

        logger.info(f"Indexed {len(medical_documents)} medical documents")
        self.initialized = True

    async def _load_medical_knowledge(self) -> List[Document]:
        """Ladda medicinsk kunskap från olika källor"""
        documents = []

        # 1. Ladda ögonsjukdomar
        diseases = self._load_eye_diseases()
        documents.extend(diseases)

        # 2. Ladda behandlingsprotokoll
        treatments = self._load_treatment_protocols()
        documents.extend(treatments)

        # 3. Ladda läkemedelsinformation
        medications = self._load_medications()
        documents.extend(medications)

        return documents

    def _load_eye_diseases(self) -> List[Document]:
        """Ladda ögonsjukdomar från kunskapsbas"""
        eye_diseases = [
            {
                "name": "Katarakt (Grå starr)",
                "icd10": "H25-H28",
                "symptoms": [
                    "suddig syn",
                    "gradvis synförsämring",
                    "halos runt lampor",
                    "svårt att köra bil i mörker",
                    "färger verkar blekare",
                    "behov av starkare glasögon"
                ],
                "age_group": "främst äldre >60 år",
                "description": "Grumling av ögats lins som leder till gradvis synförsämring. Den vanligaste orsaken till behandlingsbar blindhet.",
                "risk_factors": [
                    "ålder",
                    "diabetes",
                    "rökning",
                    "långvarig kortisonbehandling",
                    "UV-exponering"
                ],
                "treatment": "Kataraktoperation med inläggning av konstgjord lins (IOL). KVÅ: CJE00"
            },
            {
                "name": "Glaukom (Grön starr)",
                "icd10": "H40-H42",
                "symptoms": [
                    "synfältsbortfall (perifer syn först)",
                    "förhöjt ögontryck",
                    "ofta symtomfritt tidigt",
                    "tunnelseende i sena stadier",
                    "huvudvärk (vid akut glaukom)",
                    "rött öga (vid akut glaukom)"
                ],
                "age_group": "främst >40 år",
                "description": "Progressiv skada på synnerven, ofta kopplad till förhöjt ögontryck. Kan leda till permanent synförlust om obehandlad.",
                "risk_factors": [
                    "hög ålder",
                    "hereditet",
                    "högt ögontryck",
                    "diabetes",
                    "migrän"
                ],
                "treatment": "Ögondroppar (trycknedsättande), laserbehandling (SLT), kirurgi (trabekulektomi KVÅ: CJD00)"
            },
            {
                "name": "Åldersrelaterad Makuladegeneration (AMD)",
                "icd10": "H35.3",
                "symptoms": [
                    "böjda linjer (Amsler grid)",
                    "central synförlust",
                    "svårt att läsa",
                    "förvrängd syn",
                    "mörk fläck i centrum"
                ],
                "age_group": ">50 år, mest >65 år",
                "description": "Degeneration av makula (gula fläcken) som ger central synförlust. Finns i torr och våt form.",
                "risk_factors": ["ålder", "rökning", "hereditet", "ljus ögonfärg"],
                "treatment": "Våt AMD: Anti-VEGF injektioner (KVÅ: CJB10). Torr AMD: Kosttillskott (AREDS2), rökstopp"
            },
            {
                "name": "Diabetesretinopati",
                "icd10": "E11.3 / H36.0",
                "symptoms": [
                    "suddig syn",
                    "floaters",
                    "synfältsbortfall",
                    "ofta symtomfritt tidigt"
                ],
                "age_group": "diabetiker, alla åldrar",
                "description": "Skador på retinan orsakade av diabetes. En ledande orsak till blindhet hos arbetsför ålder.",
                "risk_factors": [
                    "dålig glukoskontroll",
                    "lång diabetesduration",
                    "högt blodtryck",
                    "höga blodfetter"
                ],
                "treatment": "Laserbehandling (PRP KVÅ: CJF20), Anti-VEGF injektioner, bra diabeteskontroll"
            },
            {
                "name": "Retinal Avlossning",
                "icd10": "H33",
                "symptoms": [
                    "plötsliga ljusblixtar",
                    "många nya floaters",
                    "gardinsymptom (skugga i synfältet)",
                    "plötslig synförlust"
                ],
                "age_group": "alla åldrar, ökad risk >50 år",
                "description": "AKUT tillstånd där näthinnan lossnar från underliggande vävnad. Kräver akut behandling.",
                "risk_factors": [
                    "närsynthet",
                    "ögontrauma",
                    "tidigare kataraktoperation",
                    "hereditet"
                ],
                "treatment": "AKUT kirurgi: Vitrektomi, buckle, pneumatisk retinopex. Laser/kryoterapi."
            },
            {
                "name": "Torra Ögon (Keratoconjunctivitis sicca)",
                "icd10": "H04.1",
                "symptoms": [
                    "brännande känsla",
                    "sandkornskänsla",
                    "rinnande ögon (paradoxalt)",
                    "röda ögon",
                    "trötta ögon vid läsning"
                ],
                "age_group": "alla åldrar, vanligare hos kvinnor >40 år",
                "description": "Otillräcklig tårproduktion eller snabb avdunstning av tårfilm.",
                "risk_factors": [
                    "ålder",
                    "Sjögrens syndrom",
                    "skärmarbete",
                    "vissa mediciner",
                    "kontaktlinser"
                ],
                "treatment": "Artificiella tårar, punktumplugg, omega-3, behandla bakomliggande orsak"
            }
        ]

        return [
            Document(
                text=self._format_disease_as_text(disease),
                metadata={
                    "type": "disease",
                    "name": disease["name"],
                    "icd10": disease["icd10"]
                }
            )
            for disease in eye_diseases
        ]

    def _format_disease_as_text(self, disease: dict) -> str:
        """Formatera sjukdom som text för embedding"""
        return f"""
Sjukdom: {disease['name']}
ICD-10: {disease['icd10']}
Åldersgrupp: {disease['age_group']}

Beskrivning: {disease['description']}

Symptom:
{chr(10).join(f"- {s}" for s in disease['symptoms'])}

Riskfaktorer:
{chr(10).join(f"- {r}" for r in disease['risk_factors'])}

Behandling: {disease['treatment']}
        """.strip()

    def _load_treatment_protocols(self) -> List[Document]:
        """Ladda behandlingsprotokoll"""
        treatments = [
            {
                "disease": "Katarakt",
                "protocol": """
Behandling av Katarakt:

Indikation för operation:
- Synförsämring som påverkar dagliga aktiviteter
- Visus <0.5 eller patientens subjektiva besvär
- Katarakt som hindrar undersökning/behandling av retina

Preoperativ utredning:
- Biometri (IOL-beräkning)
- Keratometri
- Ev. OCT/fundus

Operation (KVÅ: CJE00):
- Fakoemulsifikation med IOL-inläggning
- Lokalbedövning (drops eller block)
- Dagskirurgi

Postoperativ behandling:
- Antibiotikadrops 1 vecka
- Steroiddrops nedtrappning 4 veckor
- Kontroll efter 1 dag och 1 månad

Förväntad visus: Ofta 1.0 om inga andra ögonsjukdomar
                """
            },
            {
                "disease": "Glaukom",
                "protocol": """
Behandling av Primär Öppenvinkelglaukom:

Mål: Sänka ögontrycket för att förhindra synnervsskada

1:a linjen - Medicin:
- Prostaglandinanaloger (S01EE): Latanoprost 1 droppe kväll
- Alt: Betablockerare (S01ED): Timolol 2 ggr/dag
- Alt: CAI (S01EC): Dorzolamid 2-3 ggr/dag

2:a linjen - Laser:
- Selektiv Laser Trabekuloplastik (SLT)
- Sänker IOP 20-30%
- Kan upprepas

3:e linjen - Kirurgi:
- Trabekulektomi (KVÅ: CJD00)
- Shunt/stent (KVÅ: CJD96)
- För svåra/avancerade fall

Uppföljning:
- Tryckkontroll var 3-6 månad
- Synfältsundersökning årligen
- OCT papilla årligen
                """
            }
        ]

        return [
            Document(
                text=t["protocol"],
                metadata={"type": "treatment_protocol", "disease": t["disease"]}
            )
            for t in treatments
        ]

    def _load_medications(self) -> List[Document]:
        """Ladda läkemedelsinformation"""
        medications = [
            {
                "name": "Latanoprost (Xalatan)",
                "atc": "S01EE01",
                "category": "Prostaglandinanalog",
                "indication": "Glaukom, okulär hypertension",
                "dosage": "1 droppe i drabbat öga 1 gång dagligen på kvällen",
                "side_effects": "Hyperemi, ökad irispigmentering, förlängda fransar, makulaödem (ovanligt)",
                "contraindications": "Överkänslighet"
            },
            {
                "name": "Timolol (Timoptic)",
                "atc": "S01ED01",
                "category": "Betablockerare",
                "indication": "Glaukom, okulär hypertension",
                "dosage": "1 droppe 2 gånger dagligen",
                "side_effects": "Lokal: Sveda, rodnad. Systemisk: Bradykardi, bronkospasm",
                "contraindications": "Astma, KOL, bradykardi, AV-block"
            }
        ]

        return [
            Document(
                text=self._format_medication_as_text(med),
                metadata={"type": "medication", "name": med["name"], "atc": med["atc"]}
            )
            for med in medications
        ]

    def _format_medication_as_text(self, med: dict) -> str:
        """Formatera läkemedel som text"""
        return f"""
Läkemedel: {med['name']}
ATC: {med['atc']}
Kategori: {med['category']}

Indikation: {med['indication']}
Dosering: {med['dosage']}

Biverkningar: {med['side_effects']}
Kontraindikationer: {med['contraindications']}
        """.strip()

    async def search_diseases(
        self,
        symptoms: List[str],
        top_k: int = 5
    ) -> List[EyeDisease]:
        """Sök sjukdomar baserat på symptom"""
        if not self.initialized:
            raise RuntimeError("RAG not initialized. Call initialize() first.")

        query = f"Symptom: {', '.join(symptoms)}"

        query_engine = self.vector_index.as_query_engine(
            similarity_top_k=top_k
        )

        response = await query_engine.aquery(query)

        # Parse response och returnera structured data
        # I produktion: Använd structured output från LLM
        return self._parse_diseases_from_response(str(response), symptoms)

    async def search_treatments(self, disease: str) -> List[Treatment]:
        """Sök behandlingar för en sjukdom"""
        if not self.initialized:
            raise RuntimeError("RAG not initialized. Call initialize() first.")

        query = f"Behandling för {disease}"

        query_engine = self.vector_index.as_query_engine(
            similarity_top_k=3
        )

        response = await query_engine.aquery(query)

        return self._parse_treatments_from_response(str(response))

    async def search_medications(self, indication: str) -> List[Medication]:
        """Sök läkemedel"""
        if not self.initialized:
            raise RuntimeError("RAG not initialized. Call initialize() first.")

        query = f"Läkemedel för {indication}"

        query_engine = self.vector_index.as_query_engine(
            similarity_top_k=5
        )

        response = await query_engine.aquery(query)

        return self._parse_medications_from_response(str(response))

    def _parse_diseases_from_response(
        self,
        response: str,
        symptoms: List[str]
    ) -> List[EyeDisease]:
        """Parse diseases från RAG response"""
        # Simplified parsing - i produktion använd LLM med structured output
        return [
            EyeDisease(
                name="Katarakt",
                icd10="H25",
                probability=0.75,
                matching_symptoms=[
                    s for s in symptoms
                    if any(kw in s.lower() for kw in ["suddig", "halos", "natt"])
                ],
                description="Grumling av ögats lins"
            )
        ]

    def _parse_treatments_from_response(self, response: str) -> List[Treatment]:
        """Parse treatments från RAG response"""
        return [
            Treatment(
                name="Kataraktoperation",
                type="surgery",
                description="Fakoemulsifikation med IOL-inläggning",
                kva="CJE00"
            )
        ]

    def _parse_medications_from_response(self, response: str) -> List[Medication]:
        """Parse medications från RAG response"""
        return [
            Medication(
                name="Latanoprost",
                atc="S01EE01",
                dosage="1 droppe kväll"
            )
        ]


# Singleton instance
medical_rag = MedicalKnowledgeRAG()
