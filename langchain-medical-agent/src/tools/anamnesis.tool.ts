import { DynamicStructuredTool } from '@langchain/core/tools';
import { ChatAnthropic } from '@langchain/anthropic';
import { SuggestQuestionsInputSchema, AnamnesisQuestion } from '../types/medical.types';
import { ANAMNESIS_QUESTION_PROMPT } from '../prompts/ophthalmology-prompt';

/**
 * Tool för att generera relevanta anamnesfrågor
 *
 * Analyserar nuvarande kontext och föreslår intelligenta följdfrågor
 * baserat på vad som redan diskuterats
 */
export const suggestAnamnesisQuestionsTool = new DynamicStructuredTool({
  name: 'suggest_anamnesis_questions',
  description: `Generera relevanta anamnesfrågor baserat på nuvarande samtal.

Använd detta tool när:
- Du behöver mer information för att avgränsa diagnoser
- Patienten har nämnt symptom som behöver utforskas djupare
- Du vill följa upp på tidigare svar
- Det är dags att fråga om medicinsk historik eller läkemedel

Input: Nuvarande medicinsk kontext (symptom, misstänkta sjukdomar, redan ställda frågor)
Output: Lista av 3-5 prioriterade anamnesfrågor med rationale`,

  schema: SuggestQuestionsInputSchema,

  func: async ({ currentContext, focus = 'general' }) => {
    try {
      console.log('💭 Generating anamnesis questions...');

      // Använd Claude för att generera intelligenta frågor
      const llm = new ChatAnthropic({
        modelName: 'claude-3-5-sonnet-20241022',
        temperature: 0.3, // Låg temp för konsekventa, relevanta frågor
      });

      const prompt = buildQuestionPrompt(currentContext, focus);

      const response = await llm.invoke(prompt);

      // Parse response till strukturerade frågor
      const questions = parseQuestions(response.content.toString());

      return JSON.stringify(
        {
          questions,
          context_summary: summarizeContext(currentContext),
          focus_area: focus,
        },
        null,
        2
      );
    } catch (error) {
      console.error('Error generating questions:', error);
      return JSON.stringify({
        error: 'Failed to generate questions',
        message: error instanceof Error ? error.message : 'Unknown error',
      });
    }
  },
});

/**
 * Bygg prompt för question generation
 */
function buildQuestionPrompt(context: any, focus: string): string {
  const { symptoms, suspectedDiseases, askedQuestions, currentMedications } = context;

  return `${ANAMNESIS_QUESTION_PROMPT}

## NUVARANDE KONTEXT:

### Nämnda symptom:
${symptoms.map((s: any) => `- ${s.name}${s.duration ? ` (${s.duration})` : ''}`).join('\n') || 'Inga symptom nämnda än'}

### Misstänkta sjukdomar:
${suspectedDiseases?.map((d: any) => `- ${d.name} (sannolikhet: ${d.probability})`).join('\n') || 'Inga diagnoser misstänkta än'}

### Redan ställda frågor:
${askedQuestions?.join('\n') || 'Inga frågor ställda än'}

### Nuvarande läkemedel:
${currentMedications?.map((m: any) => `- ${m.name}`).join('\n') || 'Inga läkemedel nämnda'}

### Fokusområde: ${focus}

## UPPGIFT:
Generera 3-5 relevanta anamnesfrågor som:
1. INTE upprepar redan ställda frågor
2. Hjälper till att avgränsa mellan de misstänkta diagnoserna
3. Följer upp på nämnda symptom
4. Är naturliga i samtalsflödet
5. Prioriterar allvarliga tillstånd ("red flags")

Formatera varje fråga som:
FRÅGA: [frågan]
KATEGORI: [symptom_clarification|duration|severity|related_symptoms|medical_history|medications|family_history]
PRIORITET: [high|medium|low]
RATIONALE: [varför denna fråga är relevant]
---`;
}

/**
 * Parse frågor från LLM response
 */
function parseQuestions(response: string): AnamnesisQuestion[] {
  const questions: AnamnesisQuestion[] = [];
  const questionBlocks = response.split('---').filter((b) => b.trim());

  for (const block of questionBlocks) {
    const lines = block.trim().split('\n');
    const question: any = {};

    for (const line of lines) {
      if (line.startsWith('FRÅGA:')) {
        question.question = line.replace('FRÅGA:', '').trim();
      } else if (line.startsWith('KATEGORI:')) {
        question.category = line.replace('KATEGORI:', '').trim();
      } else if (line.startsWith('PRIORITET:')) {
        question.priority = line.replace('PRIORITET:', '').trim();
      } else if (line.startsWith('RATIONALE:')) {
        question.rationale = line.replace('RATIONALE:', '').trim();
      }
    }

    if (question.question && question.category && question.priority) {
      questions.push(question as AnamnesisQuestion);
    }
  }

  // Sortera efter prioritet
  const priorityOrder = { high: 0, medium: 1, low: 2 };
  questions.sort(
    (a, b) => priorityOrder[a.priority] - priorityOrder[b.priority]
  );

  return questions.slice(0, 5); // Max 5 frågor
}

/**
 * Sammanfatta kontext för output
 */
function summarizeContext(context: any): string {
  const { symptoms, suspectedDiseases } = context;

  const parts: string[] = [];

  if (symptoms?.length > 0) {
    parts.push(`${symptoms.length} symptom identifierade`);
  }

  if (suspectedDiseases?.length > 0) {
    const topDisease = suspectedDiseases[0];
    parts.push(`Misstänker främst: ${topDisease.name}`);
  }

  return parts.join('. ') || 'Inget samtal påbörjat än';
}

/**
 * Exempel på pre-defined questions för vanliga scenarion
 * Används som fallback om LLM misslyckas
 */
export const FALLBACK_QUESTIONS: Record<string, AnamnesisQuestion[]> = {
  sudden_vision_loss: [
    {
      question: 'Kom synförlusten plötsligt eller gradvis?',
      category: 'duration',
      priority: 'high',
      rationale: 'Avgör om akut tillstånd (retinal avlossning) eller kroniskt',
    },
    {
      question: 'Ser du ljusblixtar eller svävande fläckar?',
      category: 'related_symptoms',
      priority: 'high',
      rationale: 'Klassiska tecken på retinal avlossning - AKUT',
    },
    {
      question: 'Påverkar det hela synfältet eller bara en del?',
      category: 'symptom_clarification',
      priority: 'high',
      rationale: 'Lokalisera skadan',
    },
  ],

  blurry_vision: [
    {
      question: 'Är det bättre att se på nära håll eller långt avstånd?',
      category: 'symptom_clarification',
      priority: 'medium',
      rationale: 'Differentiera mellan refraktionsfel och annan patologi',
    },
    {
      question: 'Ser du halos eller ringar runt lampor?',
      category: 'related_symptoms',
      priority: 'medium',
      rationale: 'Tyder på katarakt eller korneal ödem',
    },
    {
      question: 'Har det försämrats gradvis eller kom det plötsligt?',
      category: 'duration',
      priority: 'high',
      rationale: 'Akuta förändringar kräver snabbare handläggning',
    },
  ],

  eye_pain: [
    {
      question: 'Är smärtan i ögat eller runt ögat?',
      category: 'symptom_clarification',
      priority: 'high',
      rationale: 'Lokalisera om intraokulär eller extraokulär',
    },
    {
      question: 'Upplever du ljuskänslighet?',
      category: 'related_symptoms',
      priority: 'high',
      rationale: 'Tecken på inflammation eller korneal skada',
    },
    {
      question: 'Har du fått något i ögat eller trauma?',
      category: 'medical_history',
      priority: 'high',
      rationale: 'Uteslut främmande kropp eller skada',
    },
  ],

  red_eye: [
    {
      question: 'Kliar det eller gör det ont?',
      category: 'symptom_clarification',
      priority: 'high',
      rationale: 'Allergi (klåda) vs infektion/inflammation (smärta)',
    },
    {
      question: 'Har du flytningar eller varbildning?',
      category: 'related_symptoms',
      priority: 'high',
      rationale: 'Tecken på bakteriell konjunktivit',
    },
    {
      question: 'Är synen påverkad?',
      category: 'related_symptoms',
      priority: 'high',
      rationale: 'Om ja, mer allvarligt tillstånd (keratit, uveit)',
    },
  ],
};
