"""
Medical domain types using Pydantic for validation

Motsvarar TypeScript/Zod schemas men med Python's type system
"""
from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator


# ============================================================================
# ENUMS
# ============================================================================

class Severity(str, Enum):
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"


class Laterality(str, Enum):
    RIGHT = "höger"
    LEFT = "vänster"
    BILATERAL = "bilateral"


class TreatmentType(str, Enum):
    MEDICATION = "medication"
    SURGERY = "surgery"
    LASER = "laser"
    OBSERVATION = "observation"
    OTHER = "other"


class QuestionCategory(str, Enum):
    SYMPTOM_CLARIFICATION = "symptom_clarification"
    DURATION = "duration"
    SEVERITY = "severity"
    RELATED_SYMPTOMS = "related_symptoms"
    MEDICAL_HISTORY = "medical_history"
    MEDICATIONS = "medications"
    FAMILY_HISTORY = "family_history"


class Priority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class SuggestionType(str, Enum):
    DISEASE = "disease"
    TREATMENT = "treatment"
    MEDICATION = "medication"
    QUESTION = "question"
    ANALYSIS = "analysis"


# ============================================================================
# MEDICAL DOMAIN MODELS
# ============================================================================

class Symptom(BaseModel):
    """Symptom model"""
    name: str = Field(..., description="Symptomets namn, t.ex. 'suddig syn'")
    severity: Optional[Severity] = None
    duration: Optional[str] = Field(None, description="Hur länge, t.ex. '2 veckor'")
    laterality: Optional[Laterality] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "suddig syn",
                "severity": "moderate",
                "duration": "2 veckor",
                "laterality": "bilateral"
            }
        }
    }


class EyeDisease(BaseModel):
    """Ögonsjukdom model"""
    name: str = Field(..., description="Sjukdomens namn")
    icd10: Optional[str] = Field(None, description="ICD-10 kod")
    probability: float = Field(..., ge=0, le=1, description="Sannolikhet 0-1")
    matching_symptoms: List[str] = Field(default_factory=list, description="Matchande symptom")
    description: str = Field(..., description="Kort beskrivning")

    @field_validator('probability')
    @classmethod
    def validate_probability(cls, v: float) -> float:
        if not 0 <= v <= 1:
            raise ValueError('Probability must be between 0 and 1')
        return v

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Katarakt",
                "icd10": "H25",
                "probability": 0.85,
                "matching_symptoms": ["suddig syn", "halos runt lampor"],
                "description": "Grumling av ögats lins"
            }
        }
    }


class Treatment(BaseModel):
    """Behandling model"""
    name: str
    type: TreatmentType
    description: str
    kva: Optional[str] = Field(None, description="KVÅ åtgärdskod")

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Kataraktoperation",
                "type": "surgery",
                "description": "Fakoemulsifikation med IOL-inläggning",
                "kva": "CJE00"
            }
        }
    }


class Medication(BaseModel):
    """Läkemedel model"""
    name: str
    atc: Optional[str] = Field(None, description="ATC kod")
    dosage: Optional[str] = None
    frequency: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Latanoprost",
                "atc": "S01EE01",
                "dosage": "1 droppe",
                "frequency": "kväll"
            }
        }
    }


class AnamnesisQuestion(BaseModel):
    """Anamnesfråga model"""
    question: str = Field(..., description="Frågan att ställa")
    category: QuestionCategory
    priority: Priority
    rationale: str = Field(..., description="Varför denna fråga är relevant")

    model_config = {
        "json_schema_extra": {
            "example": {
                "question": "Ser du halos runt lampor på kvällen?",
                "category": "related_symptoms",
                "priority": "high",
                "rationale": "Klassiskt tecken på katarakt"
            }
        }
    }


# ============================================================================
# AGENT OUTPUT TYPES
# ============================================================================

class AgentSuggestion(BaseModel):
    """Agent suggestion output"""
    type: SuggestionType
    content: Union[EyeDisease, Treatment, Medication, AnamnesisQuestion, dict]
    confidence: float = Field(..., ge=0, le=1)
    timestamp: datetime = Field(default_factory=datetime.now)

    model_config = {
        "json_schema_extra": {
            "example": {
                "type": "disease",
                "content": {
                    "name": "Katarakt",
                    "icd10": "H25",
                    "probability": 0.85
                },
                "confidence": 0.9,
                "timestamp": "2024-01-15T10:30:00"
            }
        }
    }


# ============================================================================
# CONVERSATION CONTEXT
# ============================================================================

class MedicalContext(BaseModel):
    """Medicinsk kontext för samtalet"""
    symptoms: List[Symptom] = Field(default_factory=list)
    suspected_diseases: List[EyeDisease] = Field(default_factory=list)
    current_medications: List[Medication] = Field(default_factory=list)
    asked_questions: List[str] = Field(
        default_factory=list,
        description="Frågor som redan ställts"
    )
    medical_history: Optional[List[str]] = None

    def add_symptom(self, symptom: Symptom) -> None:
        """Lägg till symptom om det inte redan finns"""
        if not any(s.name == symptom.name for s in self.symptoms):
            self.symptoms.append(symptom)

    def add_disease(self, disease: EyeDisease) -> None:
        """Lägg till misstänkt sjukdom"""
        # Ta bort befintlig om samma namn
        self.suspected_diseases = [
            d for d in self.suspected_diseases if d.name != disease.name
        ]
        self.suspected_diseases.append(disease)
        # Sortera efter sannolikhet
        self.suspected_diseases.sort(key=lambda d: d.probability, reverse=True)

    def add_medication(self, medication: Medication) -> None:
        """Lägg till läkemedel"""
        if not any(m.name == medication.name for m in self.current_medications):
            self.current_medications.append(medication)

    def mark_question_asked(self, question: str) -> None:
        """Markera fråga som ställd"""
        if question not in self.asked_questions:
            self.asked_questions.append(question)

    def get_summary(self) -> str:
        """Sammanfattning av kontext"""
        parts = []

        if self.symptoms:
            parts.append(f"Symptom: {', '.join(s.name for s in self.symptoms)}")

        if self.suspected_diseases:
            top = self.suspected_diseases[0]
            parts.append(
                f"Misstänker främst: {top.name} "
                f"({int(top.probability * 100)}%)"
            )

        if self.current_medications:
            parts.append(
                f"Läkemedel: {', '.join(m.name for m in self.current_medications)}"
            )

        return "\n".join(parts) if parts else "Inget samtal påbörjat än"


# ============================================================================
# TOOL INPUT SCHEMAS
# ============================================================================

class SearchDiseasesInput(BaseModel):
    """Input för search_eye_diseases tool"""
    symptoms: List[str] = Field(..., description="Lista av symptom att söka på")
    patient_age: Optional[int] = None
    medical_history: Optional[List[str]] = None


class SearchTreatmentsInput(BaseModel):
    """Input för search_treatments tool"""
    disease: str = Field(..., description="Sjukdomen att hitta behandlingar för")
    patient_age: Optional[int] = None
    contraindications: Optional[List[str]] = None


class SuggestQuestionsInput(BaseModel):
    """Input för suggest_anamnesis_questions tool"""
    current_context: MedicalContext = Field(
        ...,
        description="Nuvarande medicinsk kontext"
    )
    focus: Optional[str] = Field(
        None,
        description="Vad frågorna ska fokusera på"
    )


# ============================================================================
# API REQUEST/RESPONSE MODELS
# ============================================================================

class SessionStartRequest(BaseModel):
    """Request för att starta session"""
    user_id: str


class SessionStartResponse(BaseModel):
    """Response när session startar"""
    session_id: str
    started_at: datetime


class TranscriptionChunk(BaseModel):
    """Transcription chunk från frontend"""
    text: str
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)


class JournalEntry(BaseModel):
    """Genererad journaltext"""
    session_id: str
    content: str
    generated_at: datetime = Field(default_factory=datetime.now)
    sections: dict = Field(
        default_factory=dict,
        description="SOAP sections: aktuellt, status, bedömning, planering"
    )


class WebSocketMessage(BaseModel):
    """WebSocket meddelande format"""
    type: str
    data: dict
    timestamp: datetime = Field(default_factory=datetime.now)
