import { DynamicStructuredTool } from '@langchain/core/tools';
import { medicalRAG } from '../rag/llamaindex-integration';
import { SearchDiseasesInputSchema } from '../types/medical.types';

/**
 * Tool för att söka ögonsjukdomar baserat på symptom
 *
 * Använder LlamaIndex RAG för att hitta matchande sjukdomar
 */
export const searchEyeDiseasesTool = new DynamicStructuredTool({
  name: 'search_eye_diseases',
  description: `Sök efter ögonsjukdomar baserat på patientens symptom.

Använd detta tool när:
- Patienten beskriver symptom
- Du behöver identifiera möjliga diagnoser
- Du vill hitta differentialdiagnoser

Input: Lista av symptom, patientens ålder (optional), medicinsk historik (optional)
Output: Lista av möjliga ögonsjukdomar med sannolikheter och matchande symptom`,

  schema: SearchDiseasesInputSchema,

  func: async ({ symptoms, patientAge, medicalHistory }) => {
    try {
      console.log('🔍 Searching diseases for symptoms:', symptoms);

      // Använd RAG för att hitta matchande sjukdomar
      const diseases = await medicalRAG.searchDiseases(symptoms, 5);

      // Formatera resultat för agenten
      const result = {
        foundDiseases: diseases.length,
        diseases: diseases.map((d) => ({
          name: d.name,
          icd10: d.icd10,
          probability: d.probability,
          matchingSymptoms: d.matchingSymptoms,
          description: d.description,
        })),
        recommendations: generateRecommendations(diseases, patientAge),
      };

      return JSON.stringify(result, null, 2);
    } catch (error) {
      console.error('Error searching diseases:', error);
      return JSON.stringify({
        error: 'Failed to search diseases',
        message: error instanceof Error ? error.message : 'Unknown error',
      });
    }
  },
});

/**
 * Generera rekommendationer baserat på hittade sjukdomar
 */
function generateRecommendations(diseases: any[], patientAge?: number): string[] {
  const recommendations: string[] = [];

  // Kolla efter allvarliga tillstånd
  const seriousDiseases = diseases.filter((d) =>
    ['retinal avlossning', 'akut glaukom', 'endoftalmit'].some((serious) =>
      d.name.toLowerCase().includes(serious)
    )
  );

  if (seriousDiseases.length > 0) {
    recommendations.push(
      '⚠️ AKUT: Misstanke om allvarligt tillstånd - överväg akut remiss'
    );
  }

  // Åldersrelaterade rekommendationer
  if (patientAge && patientAge > 60) {
    const ageRelated = diseases.filter((d) =>
      ['katarakt', 'amd', 'glaukom'].some((age) =>
        d.name.toLowerCase().includes(age)
      )
    );
    if (ageRelated.length > 0) {
      recommendations.push(
        'Åldersrelaterade tillstånd identifierade - överväg screening'
      );
    }
  }

  // Hög sannolikhet
  const highProbability = diseases.filter((d) => d.probability > 0.7);
  if (highProbability.length > 0) {
    recommendations.push(
      `Hög sannolikhet för: ${highProbability.map((d) => d.name).join(', ')}`
    );
  }

  return recommendations;
}
