import { ChatAnthropic } from '@langchain/anthropic';
import { AgentExecutor, createToolCallingAgent } from 'langchain/agents';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { searchEyeDiseasesTool } from '../tools/search-diseases.tool';
import { searchTreatmentsTool } from '../tools/search-treatments.tool';
import { suggestAnamnesisQuestionsTool } from '../tools/anamnesis.tool';
import { MedicalContextManager } from '../memory/medical-context';
import { medicalRAG } from '../rag/llamaindex-integration';
import { OPHTHALMOLOGY_SYSTEM_PROMPT } from '../prompts/ophthalmology-prompt';
import type { AgentSuggestion } from '../types/medical.types';

/**
 * Medical AI Agent för ögonläkare
 *
 * Analyserar transkriberat patientsamtal i realtid och ger:
 * - Identifiering av ögonsjukdomar
 * - Förslag på behandlingar
 * - Smarta anamnesfrågor
 */
export class MedicalAgent {
  private llm: ChatAnthropic;
  private agent: AgentExecutor;
  private contextManager: MedicalContextManager;
  private isInitialized = false;

  constructor(options: {
    modelName?: string;
    temperature?: number;
    streaming?: boolean;
  } = {}) {
    const {
      modelName = 'claude-3-5-sonnet-20241022',
      temperature = 0.2,
      streaming = true,
    } = options;

    // Initialisera Claude LLM
    this.llm = new ChatAnthropic({
      modelName,
      temperature,
      streaming,
      maxTokens: 4096,
    });

    // Initialisera context manager
    this.contextManager = new MedicalContextManager();

    // Skapa agent (kommer fyllas i initialize())
    this.agent = null as any;
  }

  /**
   * Initialisera agenten
   * MÅSTE köras innan användning
   */
  async initialize() {
    if (this.isInitialized) {
      console.log('Agent already initialized');
      return;
    }

    console.log('🤖 Initializing Medical Agent...');

    // 1. Initialisera RAG
    await medicalRAG.initialize();
    console.log('✓ RAG initialized');

    // 2. Samla alla tools
    const tools = [
      searchEyeDiseasesTool,
      searchTreatmentsTool,
      suggestAnamnesisQuestionsTool,
    ];

    // 3. Skapa prompt template
    const prompt = ChatPromptTemplate.fromMessages([
      ['system', OPHTHALMOLOGY_SYSTEM_PROMPT],
      ['placeholder', '{chat_history}'],
      ['human', '{input}'],
      ['placeholder', '{agent_scratchpad}'],
    ]);

    // 4. Skapa agent
    const agent = await createToolCallingAgent({
      llm: this.llm,
      tools,
      prompt,
    });

    // 5. Skapa executor
    this.agent = new AgentExecutor({
      agent,
      tools,
      verbose: true,
      maxIterations: 5,
    });

    this.isInitialized = true;
    console.log('✓ Medical Agent ready!');
  }

  /**
   * Processa transkriberad text
   * Analyserar och returnerar suggestions
   */
  async processTranscription(
    transcriptionChunk: string
  ): Promise<AgentSuggestion[]> {
    if (!this.isInitialized) {
      throw new Error('Agent not initialized. Call initialize() first.');
    }

    console.log('\n📝 Processing transcription:', transcriptionChunk);

    // 1. Extrahera symptom från transcription
    const symptoms = this.contextManager.extractSymptomsFromText(transcriptionChunk);
    symptoms.forEach((s) => {
      const duration = this.contextManager.extractDuration(transcriptionChunk);
      if (duration) {
        s.duration = duration;
      }
      this.contextManager.addSymptom(s);
    });

    // 2. Bygg input till agenten
    const context = this.contextManager.getContext();
    const input = this.buildAgentInput(transcriptionChunk, context);

    // 3. Kör agenten
    const result = await this.agent.invoke({
      input,
    });

    console.log('\n🤖 Agent response:', result.output);

    // 4. Parse och returnera suggestions
    const suggestions = this.parseSuggestions(result.output);

    // 5. Uppdatera context baserat på suggestions
    this.updateContextFromSuggestions(suggestions);

    return suggestions;
  }

  /**
   * Bygg input till agenten
   */
  private buildAgentInput(transcription: string, context: any): string {
    const parts: string[] = [];

    parts.push('## NY TRANSCRIPTION:');
    parts.push(transcription);
    parts.push('');

    if (context.symptoms.length > 0) {
      parts.push('## IDENTIFIERADE SYMPTOM:');
      parts.push(
        context.symptoms
          .map(
            (s: any) =>
              `- ${s.name}${s.duration ? ` (${s.duration})` : ''}${s.severity ? ` [${s.severity}]` : ''}`
          )
          .join('\n')
      );
      parts.push('');
    }

    if (context.suspectedDiseases.length > 0) {
      parts.push('## MISSTÄNKTA SJUKDOMAR:');
      parts.push(
        context.suspectedDiseases
          .map(
            (d: any) =>
              `- ${d.name} (sannolikhet: ${Math.round(d.probability * 100)}%)`
          )
          .join('\n')
      );
      parts.push('');
    }

    parts.push('## UPPGIFT:');
    parts.push('Analysera transcriptionen och:');
    parts.push('1. Använd search_eye_diseases om nya symptom nämnts');
    parts.push(
      '2. Använd suggest_anamnesis_questions för att generera relevanta följdfrågor'
    );
    parts.push(
      '3. Om diagnos är trolig, använd search_treatments för behandlingsalternativ'
    );
    parts.push('');
    parts.push('Ge konkreta, actionable suggestions till läkaren.');

    return parts.join('\n');
  }

  /**
   * Parse suggestions från agent output
   * I produktion: Använd structured output
   */
  private parseSuggestions(output: string): AgentSuggestion[] {
    const suggestions: AgentSuggestion[] = [];

    // Simplified parsing - i produktion använd structured output med Zod
    // För nu returnera baserat på output

    return suggestions;
  }

  /**
   * Uppdatera context från suggestions
   */
  private updateContextFromSuggestions(suggestions: AgentSuggestion[]) {
    for (const suggestion of suggestions) {
      if (suggestion.type === 'disease' && 'name' in suggestion.content) {
        this.contextManager.addSuspectedDisease(suggestion.content as any);
      } else if (
        suggestion.type === 'medication' &&
        'name' in suggestion.content
      ) {
        this.contextManager.addMedication(suggestion.content as any);
      } else if (
        suggestion.type === 'question' &&
        'question' in suggestion.content
      ) {
        this.contextManager.markQuestionAsked(
          (suggestion.content as any).question
        );
      }
    }
  }

  /**
   * Hämta nuvarande kontext
   */
  getContext() {
    return this.contextManager.getContext();
  }

  /**
   * Hämta sammanfattning
   */
  getSummary() {
    return this.contextManager.getSummary();
  }

  /**
   * Rensa kontext (nytt samtal)
   */
  reset() {
    this.contextManager.reset();
  }

  /**
   * Generera journaltext baserat på conversation
   */
  async generateJournalEntry(): Promise<string> {
    const context = this.contextManager.getContext();

    const prompt = `Baserat på följande information, generera en strukturerad journalanteckning:

## SYMPTOM:
${context.symptoms.map((s) => `- ${s.name}${s.duration ? ` (${s.duration})` : ''}`).join('\n')}

## MISSTÄNKTA DIAGNOSER:
${context.suspectedDiseases.map((d) => `- ${d.name} (${d.icd10})`).join('\n')}

## AKTUELLA LÄKEMEDEL:
${context.currentMedications.map((m) => `- ${m.name}`).join('\n') || 'Inga'}

Formatera som en ögonjournal med:
1. AKTUELLT (anamnes)
2. AKTUELLA LÄKEMEDEL
3. ÖGONSTATUS (baserat på beskrivna symptom)
4. BEDÖMNING (misstänkta diagnoser med ICD-10)
5. PLANERING (förslag på utredning/behandling)
`;

    const response = await this.llm.invoke(prompt);
    return response.content.toString();
  }
}
