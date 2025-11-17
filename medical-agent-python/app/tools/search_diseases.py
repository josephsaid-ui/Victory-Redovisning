"""
LangChain tool för att söka ögonsjukdomar baserat på symptom
"""
import logging
from typing import List
from langchain.tools import StructuredTool
from pydantic import Field

from app.rag.llamaindex_rag import medical_rag
from app.models.medical_types import EyeDisease

logger = logging.getLogger(__name__)


async def search_eye_diseases_func(
    symptoms: List[str] = Field(..., description="Lista av symptom att söka på"),
    patient_age: int = Field(None, description="Patientens ålder (optional)"),
) -> str:
    """
    Sök efter ögonsjukdomar baserat på patientens symptom

    Använd detta tool när:
    - Patienten beskriver symptom
    - Du behöver identifiera möjliga diagnoser
    - Du vill hitta differentialdiagnoser
    """
    try:
        logger.info(f"🔍 Searching diseases for symptoms: {symptoms}")

        # Använd RAG för att hitta matchande sjukdomar
        diseases = await medical_rag.search_diseases(symptoms, top_k=5)

        # Formatera resultat
        result = {
            "found_diseases": len(diseases),
            "diseases": [
                {
                    "name": d.name,
                    "icd10": d.icd10,
                    "probability": d.probability,
                    "matching_symptoms": d.matching_symptoms,
                    "description": d.description
                }
                for d in diseases
            ],
            "recommendations": _generate_recommendations(diseases, patient_age)
        }

        return str(result)

    except Exception as e:
        logger.error(f"Error searching diseases: {e}")
        return str({"error": "Failed to search diseases", "message": str(e)})


def _generate_recommendations(diseases: List[EyeDisease], patient_age: int = None) -> List[str]:
    """Generera rekommendationer baserat på hittade sjukdomar"""
    recommendations = []

    # Kolla efter allvarliga tillstånd
    serious_diseases = [
        d for d in diseases
        if any(serious in d.name.lower() for serious in [
            "retinal avlossning", "akut glaukom", "endoftalmit"
        ])
    ]

    if serious_diseases:
        recommendations.append(
            "⚠️ AKUT: Misstanke om allvarligt tillstånd - överväg akut remiss"
        )

    # Åldersrelaterade rekommendationer
    if patient_age and patient_age > 60:
        age_related = [
            d for d in diseases
            if any(age in d.name.lower() for age in ["katarakt", "amd", "glaukom"])
        ]
        if age_related:
            recommendations.append(
                "Åldersrelaterade tillstånd identifierade - överväg screening"
            )

    # Hög sannolikhet
    high_probability = [d for d in diseases if d.probability > 0.7]
    if high_probability:
        recommendations.append(
            f"Hög sannolikhet för: {', '.join(d.name for d in high_probability)}"
        )

    return recommendations


# Skapa LangChain tool
search_eye_diseases_tool = StructuredTool.from_function(
    coroutine=search_eye_diseases_func,
    name="search_eye_diseases",
    description="Sök efter ögonsjukdomar baserat på symptom. Returnerar lista av möjliga diagnoser med sannolikheter."
)
