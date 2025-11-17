/**
 * BASIC EXAMPLE: Enkel användning av Medical Agent
 *
 * Visar hur man:
 * 1. Initialiserar agenten
 * 2. Processar en transcription
 * 3. Genererar journaltext
 */

import { MedicalAgent } from '../src/agent/medical-agent';

async function basicExample() {
  console.log('='.repeat(80));
  console.log('BASIC MEDICAL AGENT EXAMPLE');
  console.log('='.repeat(80));

  // 1. Skapa och initialisera agent
  const agent = new MedicalAgent({
    modelName: 'claude-3-5-sonnet-20241022',
    temperature: 0.2,
    streaming: false, // Non-streaming för enklare exempel
  });

  await agent.initialize();

  // 2. Simulera patientsamtal
  const transcription = `
    Patient: Jag har haft problem med suddig syn i cirka två veckor nu.
    Läkare: Är det båda ögonen eller bara ett öga?
    Patient: Främst höger öga. Och jag ser lite ringar runt lamporna på kvällen.
    Läkare: Har du diabetes eller några andra sjukdomar?
    Patient: Ja, jag har typ 2 diabetes sedan 10 år tillbaka.
  `;

  console.log('\n📝 TRANSCRIPTION:');
  console.log(transcription);

  // 3. Processa transcription
  console.log('\n🤖 PROCESSING...\n');
  const suggestions = await agent.processTranscription(transcription);

  // 4. Visa context
  console.log('\n📊 MEDICAL CONTEXT:');
  console.log(agent.getSummary());

  // 5. Visa full context
  console.log('\n📋 FULL CONTEXT:');
  console.log(JSON.stringify(agent.getContext(), null, 2));

  // 6. Generera journaltext
  console.log('\n📄 GENERATED JOURNAL ENTRY:');
  const journalEntry = await agent.generateJournalEntry();
  console.log(journalEntry);

  console.log('\n' + '='.repeat(80));
}

// Kör exempel
if (require.main === module) {
  basicExample().catch(console.error);
}

export { basicExample };
