"""
Medical Context Manager

Håller koll på nuvarande samtals-kontext:
- Nämnda symptom
- Misstänkta sjukdomar
- Aktuella läkemedel
- Ställda frågor
"""
import re
import logging
from typing import List, Optional

from app.models.medical_types import (
    MedicalContext,
    Symptom,
    EyeDisease,
    Medication
)

logger = logging.getLogger(__name__)


class MedicalContextManager:
    """
    Hanterar medicinsk kontext under ett patientsamtal
    """

    def __init__(self):
        self.context = MedicalContext()

    def add_symptom(self, symptom: Symptom) -> None:
        """Lägg till symptom"""
        self.context.add_symptom(symptom)
        logger.info(f"➕ Added symptom: {symptom.name}")

    def add_suspected_disease(self, disease: EyeDisease) -> None:
        """Lägg till misstänkt sjukdom"""
        self.context.add_disease(disease)
        logger.info(f"➕ Added suspected disease: {disease.name}")

    def add_medication(self, medication: Medication) -> None:
        """Lägg till läkemedel"""
        self.context.add_medication(medication)
        logger.info(f"➕ Added medication: {medication.name}")

    def mark_question_asked(self, question: str) -> None:
        """Markera fråga som ställd"""
        self.context.mark_question_asked(question)
        logger.debug("✓ Marked question as asked")

    def get_context(self) -> MedicalContext:
        """Hämta nuvarande kontext"""
        return self.context

    def update_context(self, context: MedicalContext) -> None:
        """Uppdatera hela kontexten"""
        self.context = context

    def reset(self) -> None:
        """Rensa kontext (nytt samtal)"""
        self.context = MedicalContext()
        logger.info("🔄 Context reset")

    def get_summary(self) -> str:
        """Sammanfatta nuvarande status"""
        return self.context.get_summary()

    def extract_symptoms_from_text(self, text: str) -> List[Symptom]:
        """
        Extrahera symptom från transcription text
        Använder keyword matching - i produktion använd NER/LLM
        """
        symptoms = []
        text_lower = text.lower()

        # Symptom keywords mapping
        symptom_keywords = {
            "suddig syn": ["suddig", "suddigt", "oskarp", "grumlig"],
            "synförlust": ["förlorat syn", "ser inte", "blind"],
            "ljusblixtar": ["blixtar", "ljusblixtar", "flash"],
            "floaters": ["floaters", "svävande", "flugor", "fläckar"],
            "smärta": ["ont", "smärta", "värk", "gör ont"],
            "rött öga": ["rött", "röda ögon", "blodsprängd"],
            "klåda": ["kliar", "kliande", "klåda"],
            "torra ögon": ["torra", "torrt", "sandkorn"],
            "halos": ["halos", "ringar", "ljuskransar"],
            "dubbelseende": ["dubbel", "dubbelseende", "ser dubbelt"]
        }

        for symptom_name, keywords in symptom_keywords.items():
            for keyword in keywords:
                if keyword in text_lower:
                    # Försök extrahera duration
                    duration = self.extract_duration(text)

                    symptoms.append(Symptom(
                        name=symptom_name,
                        duration=duration
                    ))
                    break  # Hitta bara en gång per symptom

        return symptoms

    def extract_duration(self, text: str) -> Optional[str]:
        """Extrahera duration från text"""
        duration_patterns = [
            r'(\d+)\s*(dag|dagar|vecka|veckor|månad|månader|år)',
            r'sedan\s+(i\s+går|förra\s+veckan|i\s+somras)'
        ]

        for pattern in duration_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)

        return None

    def extract_age(self, text: str) -> Optional[int]:
        """Extrahera patientens ålder från text"""
        patterns = [
            r'(\d{1,3})\s*år',
            r'är\s+(\d{1,3})',
        ]

        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                age = int(match.group(1))
                if 0 < age < 120:  # Sanity check
                    return age

        return None

    def extract_medications(self, text: str) -> List[str]:
        """
        Extrahera läkemedelsnamn från text
        I produktion: Använd medical NER (medspaCy, BioBERT)
        """
        medications = []
        text_lower = text.lower()

        # Vanliga ögonläkemedel
        known_medications = [
            "latanoprost", "xalatan",
            "timolol", "timoptic",
            "dorzolamid", "trusopt",
            "brinzolamid", "azopt",
            "bimatoprost", "lumigan",
            "travoprost", "travatan",
            "cosopt", "combigan", "ganfort"
        ]

        for med in known_medications:
            if med in text_lower:
                medications.append(med.capitalize())

        return medications

    def has_red_flags(self) -> bool:
        """
        Kontrollera om det finns red flags (akuta tillstånd)
        """
        red_flag_symptoms = [
            "plötslig synförlust",
            "ljusblixtar",
            "gardinsymptom",
            "mycket kraftig smärta",
            "synfältsbortfall",
            "dubbelseende"
        ]

        for symptom in self.context.symptoms:
            if any(flag in symptom.name.lower() for flag in red_flag_symptoms):
                return True

        # Kontrollera också misstänkta sjukdomar
        red_flag_diseases = ["retinal avlossning", "akut glaukom", "endoftalmit"]
        for disease in self.context.suspected_diseases:
            if any(flag in disease.name.lower() for flag in red_flag_diseases):
                return True

        return False

    def get_most_likely_disease(self) -> Optional[EyeDisease]:
        """Hämta mest sannolika sjukdomen"""
        if not self.context.suspected_diseases:
            return None
        return self.context.suspected_diseases[0]

    def get_symptom_count(self) -> int:
        """Antal identifierade symptom"""
        return len(self.context.symptoms)

    def get_disease_count(self) -> int:
        """Antal misstänkta sjukdomar"""
        return len(self.context.suspected_diseases)

    def to_dict(self) -> dict:
        """Konvertera context till dictionary för API response"""
        return self.context.model_dump()
