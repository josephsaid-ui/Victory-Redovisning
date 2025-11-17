import { DynamicStructuredTool } from '@langchain/core/tools';
import { medicalRAG } from '../rag/llamaindex-integration';
import { SearchTreatmentsInputSchema } from '../types/medical.types';

/**
 * Tool för att söka behandlingar för ögonsjukdomar
 */
export const searchTreatmentsTool = new DynamicStructuredTool({
  name: 'search_treatments',
  description: `Sök efter behandlingsalternativ för en ögonsjukdom.

Använd detta tool när:
- En diagnos har identifierats
- Patienten frågar om behandlingsmöjligheter
- Du behöver information om aktuella behandlingsprotokoll

Input: Sjukdomsnamn, patientens ålder (optional), kontraindikationer (optional)
Output: Lista av behandlingsalternativ med beskrivningar och KVÅ-koder`,

  schema: SearchTreatmentsInputSchema,

  func: async ({ disease, patientAge, contraindications }) => {
    try {
      console.log('💊 Searching treatments for:', disease);

      // Använd RAG för att hitta behandlingar
      const treatments = await medicalRAG.searchTreatments(disease);

      // Filtrera baserat på kontraindikationer om angivna
      const filteredTreatments = contraindications
        ? filterByContraindications(treatments, contraindications)
        : treatments;

      const result = {
        disease,
        foundTreatments: filteredTreatments.length,
        treatments: filteredTreatments.map((t) => ({
          name: t.name,
          type: t.type,
          description: t.description,
          kva: t.kva,
        })),
        recommendations: generateTreatmentRecommendations(
          disease,
          filteredTreatments,
          patientAge
        ),
      };

      return JSON.stringify(result, null, 2);
    } catch (error) {
      console.error('Error searching treatments:', error);
      return JSON.stringify({
        error: 'Failed to search treatments',
        message: error instanceof Error ? error.message : 'Unknown error',
      });
    }
  },
});

function filterByContraindications(treatments: any[], contraindications: string[]): any[] {
  // I produktion: Kolla faktiska kontraindikationer
  return treatments;
}

function generateTreatmentRecommendations(
  disease: string,
  treatments: any[],
  patientAge?: number
): string[] {
  const recommendations: string[] = [];

  // Sortera treatments efter invasivitet
  const medications = treatments.filter((t) => t.type === 'medication');
  const lasers = treatments.filter((t) => t.type === 'laser');
  const surgeries = treatments.filter((t) => t.type === 'surgery');

  if (medications.length > 0) {
    recommendations.push('Börja med medicinsk behandling om möjligt');
  }

  if (surgeries.length > 0 && patientAge && patientAge > 70) {
    recommendations.push('Beakta patientens ålder vid kirurgiska ingrepp');
  }

  return recommendations;
}
