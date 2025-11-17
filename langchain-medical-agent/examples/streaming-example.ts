/**
 * STREAMING EXAMPLE: Real-time transcription processing
 *
 * Simulerar en verklig användning där:
 * 1. Audio strömmar från mikrofonen
 * 2. AssemblyAI transkriberar i realtid
 * 3. Agenten analyserar kontinuerligt
 * 4. UI:t uppdateras med suggestions
 */

import { StreamingMedicalAgent } from '../src/agent/streaming-agent';

async function streamingExample() {
  console.log('='.repeat(80));
  console.log('STREAMING MEDICAL AGENT EXAMPLE');
  console.log('='.repeat(80));

  // 1. Skapa streaming agent
  const agent = new StreamingMedicalAgent({
    modelName: 'claude-3-5-sonnet-20241022',
    temperature: 0.2,
  });

  await agent.initialize();

  // 2. Registrera event listeners
  agent.on('transcription_update', (data) => {
    console.log('\n📝 Transcription update:', data.chunk);
  });

  agent.on('suggestion', (suggestion) => {
    console.log('\n💡 NEW SUGGESTION:');
    console.log(JSON.stringify(suggestion, null, 2));
  });

  agent.on('context_update', (context) => {
    console.log('\n📊 Context updated');
    console.log(`  Symptoms: ${context.symptoms.length}`);
    console.log(`  Suspected diseases: ${context.suspectedDiseases.length}`);
  });

  agent.on('error', (error) => {
    console.error('\n❌ Error:', error.message);
  });

  // 3. Starta streaming (processar var 2:a sekund)
  agent.startStreaming(2000);

  // 4. Simulera transkribering i realtid
  console.log('\n🎙️ Starting simulated transcription...\n');

  // Simulera chunks som kommer från AssemblyAI
  const transcriptionChunks = [
    'Patienten klagar på',
    'suddig syn',
    'i båda ögonen',
    'sedan ungefär',
    'två veckor tillbaka.',
    'Särskilt på kvällen',
    'ser hon halos',
    'runt lampor.',
    'Hon är 72 år',
    'och har diabetes',
    'typ 2.',
  ];

  // Skicka chunks med fördröjning (simulerar real-time)
  for (const chunk of transcriptionChunks) {
    agent.addTranscriptionChunk(chunk);
    await sleep(800); // 800ms mellan chunks
  }

  // 5. Vänta på sista processingen
  await sleep(3000);

  // 6. Force process för att säkerställa allt är klart
  await agent.processNow();

  // 7. Visa slutlig kontext
  console.log('\n' + '='.repeat(80));
  console.log('FINAL CONTEXT:');
  console.log('='.repeat(80));
  const finalContext = agent.getContext();
  console.log(JSON.stringify(finalContext, null, 2));

  // 8. Generera journal
  console.log('\n' + '='.repeat(80));
  console.log('JOURNAL ENTRY:');
  console.log('='.repeat(80));
  const journal = await agent.generateJournalEntry();
  console.log(journal);

  // 9. Stoppa streaming
  agent.stopStreaming();

  console.log('\n✅ Streaming example completed!\n');
}

function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// Kör exempel
if (require.main === module) {
  streamingExample().catch(console.error);
}

export { streamingExample };
