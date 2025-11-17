import { MedicalContext, Symptom, EyeDisease, Medication } from '../types/medical.types';

/**
 * Medical Context Manager
 *
 * Håller koll på nuvarande samtals-kontext:
 * - Nämnda symptom
 * - Misstänkta sjukdomar
 * - Aktuella läkemedel
 * - Ställda frågor
 */
export class MedicalContextManager {
  private context: MedicalContext = {
    symptoms: [],
    suspectedDiseases: [],
    currentMedications: [],
    askedQuestions: [],
    medicalHistory: [],
  };

  /**
   * Lägg till symptom
   */
  addSymptom(symptom: Symptom) {
    // Undvik duplicates
    const exists = this.context.symptoms.find((s) => s.name === symptom.name);
    if (!exists) {
      this.context.symptoms.push(symptom);
      console.log('➕ Added symptom:', symptom.name);
    }
  }

  /**
   * Lägg till misstänkt sjukdom
   */
  addSuspectedDisease(disease: EyeDisease) {
    const exists = this.context.suspectedDiseases.find(
      (d) => d.name === disease.name
    );

    if (!exists) {
      this.context.suspectedDiseases.push(disease);
      // Sortera efter sannolikhet
      this.context.suspectedDiseases.sort((a, b) => b.probability - a.probability);
      console.log('➕ Added suspected disease:', disease.name);
    } else {
      // Uppdatera probability om den ändrats
      const index = this.context.suspectedDiseases.findIndex(
        (d) => d.name === disease.name
      );
      this.context.suspectedDiseases[index] = disease;
      this.context.suspectedDiseases.sort((a, b) => b.probability - a.probability);
    }
  }

  /**
   * Lägg till läkemedel
   */
  addMedication(medication: Medication) {
    const exists = this.context.currentMedications.find(
      (m) => m.name === medication.name
    );
    if (!exists) {
      this.context.currentMedications.push(medication);
      console.log('➕ Added medication:', medication.name);
    }
  }

  /**
   * Markera fråga som ställd
   */
  markQuestionAsked(question: string) {
    if (!this.context.askedQuestions.includes(question)) {
      this.context.askedQuestions.push(question);
      console.log('✓ Marked question as asked');
    }
  }

  /**
   * Hämta nuvarande kontext
   */
  getContext(): MedicalContext {
    return { ...this.context };
  }

  /**
   * Uppdatera hela kontexten
   */
  updateContext(context: Partial<MedicalContext>) {
    this.context = {
      ...this.context,
      ...context,
    };
  }

  /**
   * Rensa kontext (nytt samtal)
   */
  reset() {
    this.context = {
      symptoms: [],
      suspectedDiseases: [],
      currentMedications: [],
      askedQuestions: [],
      medicalHistory: [],
    };
    console.log('🔄 Context reset');
  }

  /**
   * Sammanfatta nuvarande status
   */
  getSummary(): string {
    const parts: string[] = [];

    if (this.context.symptoms.length > 0) {
      parts.push(
        `Symptom: ${this.context.symptoms.map((s) => s.name).join(', ')}`
      );
    }

    if (this.context.suspectedDiseases.length > 0) {
      const top = this.context.suspectedDiseases[0];
      parts.push(
        `Misstänker främst: ${top.name} (${Math.round(top.probability * 100)}%)`
      );
    }

    if (this.context.currentMedications.length > 0) {
      parts.push(
        `Läkemedel: ${this.context.currentMedications.map((m) => m.name).join(', ')}`
      );
    }

    return parts.join('\n') || 'Inget samtal påbörjat än';
  }

  /**
   * Extrahera symptom från transcription text
   * Använder enkel keyword matching - i produktion använd NER/LLM
   */
  extractSymptomsFromText(text: string): Symptom[] {
    const symptoms: Symptom[] = [];
    const lowerText = text.toLowerCase();

    // Symptom keywords mapping
    const symptomKeywords: Record<string, string[]> = {
      'suddig syn': ['suddig', 'suddigt', 'oskarp', 'grumlig'],
      'synförlust': ['förlorat syn', 'ser inte', 'blind'],
      'ljusblixtar': ['blixtar', 'ljusblixtar', 'flash'],
      floaters: ['floaters', 'svävande', 'flugor', 'fläckar'],
      'smärta': ['ont', 'smärta', 'värk', 'gör ont'],
      'rött öga': ['rött', 'röda ögon', 'blodsprängd'],
      'klåda': ['kliar', 'kliande', 'klåda'],
      'torra ögon': ['torra', 'torrt', 'sandkorn'],
      'halos': ['halos', 'ringar', 'ljuskransar'],
      'dubbelseende': ['dubbel', 'dubbelseende', 'ser dubbelt'],
    };

    for (const [symptom, keywords] of Object.entries(symptomKeywords)) {
      for (const keyword of keywords) {
        if (lowerText.includes(keyword)) {
          symptoms.push({
            name: symptom,
          });
          break; // Hitta bara en gång per symptom
        }
      }
    }

    return symptoms;
  }

  /**
   * Extrahera duration från text
   */
  extractDuration(text: string): string | undefined {
    const durationPatterns = [
      /(\d+)\s*(dag|dagar|vecka|veckor|månad|månader|år)/gi,
      /sedan\s+(i\s+går|förra\s+veckan|i\s+somras)/gi,
    ];

    for (const pattern of durationPatterns) {
      const match = text.match(pattern);
      if (match) {
        return match[0];
      }
    }

    return undefined;
  }
}
