import { z } from 'zod';

// ============================================================================
// MEDICAL DOMAIN TYPES
// ============================================================================

export const SymptomSchema = z.object({
  name: z.string().describe('Symptomets namn, t.ex. "suddig syn"'),
  severity: z.enum(['mild', 'moderate', 'severe']).optional(),
  duration: z.string().optional().describe('Hur länge, t.ex. "2 veckor"'),
  laterality: z.enum(['höger', 'vänster', 'bilateral']).optional(),
});

export const EyeDiseaseSchema = z.object({
  name: z.string().describe('Sjukdomens namn'),
  icd10: z.string().optional().describe('ICD-10 kod'),
  probability: z.number().min(0).max(1).describe('Sannolikhet 0-1'),
  matchingSymptoms: z.array(z.string()).describe('Matchande symptom'),
  description: z.string().describe('Kort beskrivning'),
});

export const TreatmentSchema = z.object({
  name: z.string(),
  type: z.enum(['medication', 'surgery', 'laser', 'observation', 'other']),
  description: z.string(),
  kva: z.string().optional().describe('KVÅ åtgärdskod'),
});

export const MedicationSchema = z.object({
  name: z.string(),
  atc: z.string().optional().describe('ATC kod'),
  dosage: z.string().optional(),
  frequency: z.string().optional(),
});

export const AnamnesisQuestionSchema = z.object({
  question: z.string().describe('Frågan att ställa'),
  category: z.enum([
    'symptom_clarification',
    'duration',
    'severity',
    'related_symptoms',
    'medical_history',
    'medications',
    'family_history',
  ]),
  priority: z.enum(['high', 'medium', 'low']),
  rationale: z.string().describe('Varför denna fråga är relevant'),
});

// ============================================================================
// AGENT OUTPUT TYPES
// ============================================================================

export const AgentSuggestionSchema = z.object({
  type: z.enum(['disease', 'treatment', 'medication', 'question', 'analysis']),
  content: z.union([
    EyeDiseaseSchema,
    TreatmentSchema,
    MedicationSchema,
    AnamnesisQuestionSchema,
    z.object({ text: z.string() }),
  ]),
  confidence: z.number().min(0).max(1),
  timestamp: z.date(),
});

// ============================================================================
// CONVERSATION CONTEXT
// ============================================================================

export const MedicalContextSchema = z.object({
  symptoms: z.array(SymptomSchema),
  suspectedDiseases: z.array(EyeDiseaseSchema),
  currentMedications: z.array(MedicationSchema),
  askedQuestions: z.array(z.string()).describe('Frågor som redan ställts'),
  medicalHistory: z.array(z.string()).optional(),
});

// ============================================================================
// TYPESCRIPT TYPES (exported from Zod schemas)
// ============================================================================

export type Symptom = z.infer<typeof SymptomSchema>;
export type EyeDisease = z.infer<typeof EyeDiseaseSchema>;
export type Treatment = z.infer<typeof TreatmentSchema>;
export type Medication = z.infer<typeof MedicationSchema>;
export type AnamnesisQuestion = z.infer<typeof AnamnesisQuestionSchema>;
export type AgentSuggestion = z.infer<typeof AgentSuggestionSchema>;
export type MedicalContext = z.infer<typeof MedicalContextSchema>;

// ============================================================================
// TOOL INPUT/OUTPUT SCHEMAS
// ============================================================================

export const SearchDiseasesInputSchema = z.object({
  symptoms: z.array(z.string()).describe('Lista av symptom att söka på'),
  patientAge: z.number().optional(),
  medicalHistory: z.array(z.string()).optional(),
});

export const SearchTreatmentsInputSchema = z.object({
  disease: z.string().describe('Sjukdomen att hitta behandlingar för'),
  patientAge: z.number().optional(),
  contraindications: z.array(z.string()).optional(),
});

export const SuggestQuestionsInputSchema = z.object({
  currentContext: MedicalContextSchema.describe('Nuvarande medicinsk kontext'),
  focus: z
    .enum(['symptoms', 'history', 'medications', 'general'])
    .optional()
    .describe('Vad frågorna ska fokusera på'),
});

export type SearchDiseasesInput = z.infer<typeof SearchDiseasesInputSchema>;
export type SearchTreatmentsInput = z.infer<typeof SearchTreatmentsInputSchema>;
export type SuggestQuestionsInput = z.infer<typeof SuggestQuestionsInputSchema>;
