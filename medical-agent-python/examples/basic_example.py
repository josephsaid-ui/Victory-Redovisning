"""
BASIC EXAMPLE: Enkel användning av Medical Agent

Visar hur man:
1. Initialiserar agenten
2. Processar en transcription
3. Genererar journaltext
"""
import asyncio
import logging
from dotenv import load_dotenv

from app.agents.medical_agent import MedicalAgent

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


async def basic_example():
    print("=" * 80)
    print("BASIC MEDICAL AGENT EXAMPLE - Python")
    print("=" * 80)

    # 1. Skapa och initialisera agent
    print("\n🤖 Creating and initializing agent...")
    agent = MedicalAgent(
        model_name="claude-3-5-sonnet-20241022",
        temperature=0.2,
        streaming=False  # Non-streaming för enklare exempel
    )

    await agent.initialize()
    print("✅ Agent initialized!")

    # 2. Simulera patientsamtal
    transcription = """
    Patient: Jag har haft problem med suddig syn i cirka två veckor nu.
    Läkare: Är det båda ögonen eller bara ett öga?
    Patient: Främst höger öga. Och jag ser lite ringar runt lamporna på kvällen.
    Läkare: Har du diabetes eller några andra sjukdomar?
    Patient: Ja, jag har typ 2 diabetes sedan 10 år tillbaka.
    """

    print("\n📝 TRANSCRIPTION:")
    print(transcription)

    # 3. Processa transcription
    print("\n🤖 PROCESSING...\n")
    suggestions = await agent.process_transcription(transcription)

    # 4. Visa context
    print("\n📊 MEDICAL CONTEXT:")
    print(agent.get_summary())

    # 5. Visa full context
    print("\n📋 FULL CONTEXT:")
    context = agent.get_context()
    print(f"  Symptoms: {len(context.symptoms)}")
    for s in context.symptoms:
        print(f"    - {s.name}" + (f" ({s.duration})" if s.duration else ""))

    print(f"  Suspected diseases: {len(context.suspected_diseases)}")
    for d in context.suspected_diseases:
        print(f"    - {d.name} ({int(d.probability * 100)}%)")

    # 6. Generera journaltext
    print("\n📄 GENERATED JOURNAL ENTRY:")
    journal = await agent.generate_journal_entry()
    print(journal)

    print("\n" + "=" * 80)
    print("✅ Example completed!")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(basic_example())
