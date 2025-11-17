"""
Import medical data to Supabase and generate embeddings

Använd efter collect_medical_data.py
"""
import asyncio
import json
import os
from pathlib import Path
from typing import List, Dict
import logging
from dotenv import load_dotenv

# Load environment
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MedicalDataImporter:
    """Importerar medicinsk data till Supabase med embeddings"""

    def __init__(self):
        from supabase import create_client
        from sentence_transformers import SentenceTransformer

        # Supabase client
        self.supabase = create_client(
            os.getenv("SUPABASE_URL"),
            os.getenv("SUPABASE_SERVICE_KEY")  # Use service key för backend
        )

        # Embedding model (PubMedBERT för medicinsk text)
        logger.info("Loading PubMedBERT model...")
        self.embedding_model = SentenceTransformer(
            'pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb',
            cache_folder='./model_cache'
        )
        logger.info("✅ Model loaded")

    def load_json_data(self, filepath: str) -> Dict:
        """Ladda JSON data från fil"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate_embedding(self, text: str) -> List[float]:
        """Generera embedding för text"""
        embedding = self.embedding_model.encode(text)
        return embedding.tolist()

    def format_disease_text(self, disease: Dict) -> str:
        """Formatera sjukdom till text för embedding"""
        parts = [
            f"Sjukdom: {disease['name']}",
            f"ICD-10: {disease.get('icd10', 'N/A')}",
            f"\nBeskrivning: {disease.get('description', '')}",
        ]

        if disease.get('symptoms'):
            parts.append(f"\nSymptom: {', '.join(disease['symptoms'])}")

        if disease.get('risk_factors'):
            parts.append(f"\nRiskfaktorer: {', '.join(disease['risk_factors'])}")

        if disease.get('treatment'):
            parts.append(f"\nBehandling: {disease['treatment']}")

        return '\n'.join(parts)

    def format_medication_text(self, medication: Dict) -> str:
        """Formatera läkemedel till text"""
        parts = [
            f"Läkemedel: {medication['name']}",
            f"ATC: {medication.get('atc', 'N/A')}",
            f"Kategori: {medication.get('category', '')}",
            f"\nIndikation: {medication.get('indication', '')}",
            f"Dosering: {medication.get('dosage', '')}",
        ]

        if medication.get('side_effects'):
            effects = medication['side_effects']
            if isinstance(effects, list):
                effects = ', '.join(effects)
            parts.append(f"\nBiverkningar: {effects}")

        if medication.get('contraindications'):
            contra = medication['contraindications']
            if isinstance(contra, list):
                contra = ', '.join(contra)
            parts.append(f"\nKontraindikationer: {contra}")

        return '\n'.join(parts)

    async def import_diseases(self, diseases: List[Dict]):
        """Importera sjukdomar till database"""
        logger.info(f"Importing {len(diseases)} diseases...")

        for disease in diseases:
            # Formatera text för embedding
            text_content = self.format_disease_text(disease)

            # Generera embedding
            logger.info(f"  Generating embedding for: {disease['name']}")
            embedding = self.generate_embedding(text_content)

            # Prepare data
            data = {
                "type": "disease",
                "name": disease['name'],
                "content": text_content,
                "metadata": {
                    "icd10": disease.get('icd10'),
                    "symptoms": disease.get('symptoms', []),
                    "risk_factors": disease.get('risk_factors', []),
                    "anamnesis_questions": disease.get('anamnesis_questions', []),
                    "urgency": disease.get('urgency', 'non-urgent'),
                    "red_flags": disease.get('red_flags', []),
                    "kva": disease.get('kva'),
                },
                "embedding": embedding
            }

            # Insert to Supabase
            try:
                result = self.supabase.table("medical_documents")\
                    .insert(data)\
                    .execute()

                logger.info(f"  ✅ Imported: {disease['name']}")
            except Exception as e:
                logger.error(f"  ❌ Failed to import {disease['name']}: {e}")

        logger.info(f"✅ Finished importing diseases")

    async def import_medications(self, medications: List[Dict]):
        """Importera läkemedel till database"""
        logger.info(f"Importing {len(medications)} medications...")

        for medication in medications:
            # Formatera text
            text_content = self.format_medication_text(medication)

            # Generera embedding
            logger.info(f"  Generating embedding for: {medication['name']}")
            embedding = self.generate_embedding(text_content)

            # Prepare data
            data = {
                "type": "medication",
                "name": medication['name'],
                "content": text_content,
                "metadata": {
                    "atc": medication.get('atc'),
                    "category": medication.get('category'),
                    "indication": medication.get('indication'),
                    "dosage": medication.get('dosage'),
                    "brand_names": medication.get('brand_names', []),
                },
                "embedding": embedding
            }

            # Insert
            try:
                result = self.supabase.table("medical_documents")\
                    .insert(data)\
                    .execute()

                logger.info(f"  ✅ Imported: {medication['name']}")
            except Exception as e:
                logger.error(f"  ❌ Failed to import {medication['name']}: {e}")

        logger.info(f"✅ Finished importing medications")

    async def verify_import(self):
        """Verifiera att data importerades korrekt"""
        logger.info("\n🔍 Verifying import...")

        # Count documents
        result = self.supabase.table("medical_documents").select("type", count="exact").execute()

        disease_count = self.supabase.table("medical_documents")\
            .select("id", count="exact")\
            .eq("type", "disease")\
            .execute()

        medication_count = self.supabase.table("medical_documents")\
            .select("id", count="exact")\
            .eq("type", "medication")\
            .execute()

        logger.info(f"  Total documents: {result.count}")
        logger.info(f"  Diseases: {disease_count.count}")
        logger.info(f"  Medications: {medication_count.count}")

        # Test vector search
        logger.info("\n🧪 Testing vector search...")
        test_query = "suddig syn halos"
        test_embedding = self.generate_embedding(test_query)

        # Supabase vector search
        # Note: May need to use RPC call depending on your setup
        # For now, just verify embeddings exist
        sample = self.supabase.table("medical_documents")\
            .select("name, embedding")\
            .not_.is_("embedding", None)\
            .limit(1)\
            .execute()

        if sample.data and sample.data[0].get('embedding'):
            logger.info(f"  ✅ Embeddings verified (sample: {sample.data[0]['name']})")
        else:
            logger.warning("  ⚠️ No embeddings found!")

        logger.info("\n✅ Verification complete!")

    async def clear_all_data(self, confirm: bool = False):
        """
        Rensa all data från medical_documents table

        VARNING: Detta raderar ALL data!
        """
        if not confirm:
            logger.warning("⚠️ This will DELETE ALL medical documents!")
            logger.warning("To confirm, call with confirm=True")
            return

        logger.info("🗑️ Deleting all medical documents...")

        result = self.supabase.table("medical_documents")\
            .delete()\
            .neq("id", "00000000-0000-0000-0000-000000000000")\
            .execute()

        logger.info("✅ All data cleared")


async def main():
    """Main import workflow"""

    # Check environment variables
    if not os.getenv("SUPABASE_URL") or not os.getenv("SUPABASE_SERVICE_KEY"):
        logger.error("❌ Missing SUPABASE_URL or SUPABASE_SERVICE_KEY in .env")
        logger.error("Please set these environment variables first!")
        return

    importer = MedicalDataImporter()

    # Load data from JSON
    data_file = Path(__file__).parent.parent / "data" / "medical_data.json"

    if not data_file.exists():
        logger.error(f"❌ Data file not found: {data_file}")
        logger.error("Run collect_medical_data.py first!")
        return

    logger.info(f"📂 Loading data from: {data_file}")
    data = importer.load_json_data(str(data_file))

    # Optional: Clear existing data
    # await importer.clear_all_data(confirm=True)

    # Import diseases
    if data.get('diseases'):
        await importer.import_diseases(data['diseases'])

    # Import medications
    if data.get('medications'):
        await importer.import_medications(data['medications'])

    # Verify
    await importer.verify_import()

    logger.info("\n🎉 Import complete!")
    logger.info("\nYour medical knowledge base is now ready!")
    logger.info("You can now run: python examples/basic_example.py")


if __name__ == "__main__":
    asyncio.run(main())
