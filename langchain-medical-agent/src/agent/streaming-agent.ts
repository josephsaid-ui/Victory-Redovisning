import { ChatAnthropic } from '@langchain/anthropic';
import { AgentExecutor } from 'langchain/agents';
import { MedicalAgent } from './medical-agent';
import EventEmitter from 'events';

/**
 * Streaming Medical Agent
 *
 * Extends MedicalAgent med real-time streaming capabilities
 * Skickar suggestions i realtid när de genereras
 */
export class StreamingMedicalAgent extends EventEmitter {
  private baseAgent: MedicalAgent;
  private accumulatedTranscription = '';
  private processingInterval: NodeJS.Timeout | null = null;

  constructor(options: {
    modelName?: string;
    temperature?: number;
  } = {}) {
    super();

    this.baseAgent = new MedicalAgent({
      ...options,
      streaming: true,
    });
  }

  /**
   * Initialisera agenten
   */
  async initialize() {
    await this.baseAgent.initialize();
    console.log('✓ Streaming Agent ready!');
  }

  /**
   * Starta real-time processing
   * Processar transcription chunks kontinuerligt
   */
  startStreaming(intervalMs: number = 2000) {
    if (this.processingInterval) {
      console.warn('Streaming already started');
      return;
    }

    console.log(`🎙️ Starting streaming with ${intervalMs}ms interval`);

    this.processingInterval = setInterval(async () => {
      if (this.accumulatedTranscription.trim()) {
        await this.processAccumulatedTranscription();
      }
    }, intervalMs);
  }

  /**
   * Stoppa streaming
   */
  stopStreaming() {
    if (this.processingInterval) {
      clearInterval(this.processingInterval);
      this.processingInterval = null;
      console.log('🛑 Streaming stopped');
    }
  }

  /**
   * Lägg till transcription chunk
   * Kallas när ny text kommer från transkriberings-API
   */
  addTranscriptionChunk(chunk: string) {
    this.accumulatedTranscription += ' ' + chunk;
    this.emit('transcription_update', {
      chunk,
      accumulated: this.accumulatedTranscription,
    });
  }

  /**
   * Processa ackumulerad transcription
   */
  private async processAccumulatedTranscription() {
    const text = this.accumulatedTranscription.trim();
    if (!text) return;

    console.log('\n⚡ Processing accumulated transcription...');

    try {
      // Processa med base agent
      const suggestions = await this.baseAgent.processTranscription(text);

      // Emit suggestions i realtid
      for (const suggestion of suggestions) {
        this.emit('suggestion', suggestion);
      }

      // Emit context update
      this.emit('context_update', this.baseAgent.getContext());

      // Rensa processad transcription
      this.accumulatedTranscription = '';
    } catch (error) {
      console.error('Error processing transcription:', error);
      this.emit('error', error);
    }
  }

  /**
   * Force process nu (utan att vänta på interval)
   */
  async processNow() {
    if (this.accumulatedTranscription.trim()) {
      await this.processAccumulatedTranscription();
    }
  }

  /**
   * Hämta nuvarande kontext
   */
  getContext() {
    return this.baseAgent.getContext();
  }

  /**
   * Generera journaltext
   */
  async generateJournalEntry() {
    return this.baseAgent.generateJournalEntry();
  }

  /**
   * Rensa och börja nytt samtal
   */
  reset() {
    this.accumulatedTranscription = '';
    this.baseAgent.reset();
    this.emit('reset');
  }
}

/**
 * Event types som agenten kan emittera
 */
export interface StreamingAgentEvents {
  transcription_update: { chunk: string; accumulated: string };
  suggestion: any; // AgentSuggestion
  context_update: any; // MedicalContext
  error: Error;
  reset: void;
}
