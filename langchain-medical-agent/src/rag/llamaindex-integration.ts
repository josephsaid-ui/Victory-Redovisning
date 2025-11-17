import {
  VectorStoreIndex,
  Document,
  StorageContext,
  VectorStoreQueryMode,
  serviceContextFromDefaults,
} from 'llamaindex';
import { createClient } from '@supabase/supabase-js';
import type { EyeDisease, Treatment, Medication } from '../types/medical.types';

/**
 * LlamaIndex RAG Integration för medicinsk kunskapsbas
 *
 * Använder Supabase pgvector för att lagra och söka i:
 * - Ögonsjukdomar
 * - Behandlingsprotokoll
 * - Läkemedelsinformation
 * - Svenska medicinska riktlinjer
 */

export class MedicalKnowledgeRAG {
  private vectorIndex: VectorStoreIndex | null = null;
  private supabase;

  constructor() {
    this.supabase = createClient(
      process.env.SUPABASE_URL!,
      process.env.SUPABASE_ANON_KEY!
    );
  }

  /**
   * Initialisera RAG med medicinsk kunskapsbas
   */
  async initialize() {
    console.log('Initializing Medical Knowledge RAG...');

    // Ladda medicinsk data
    const medicalDocuments = await this.loadMedicalKnowledge();

    // Skapa vector index med LlamaIndex
    const serviceContext = serviceContextFromDefaults({
      chunkSize: 512,
      chunkOverlap: 50,
    });

    this.vectorIndex = await VectorStoreIndex.fromDocuments(
      medicalDocuments,
      { serviceContext }
    );

    console.log(`Indexed ${medicalDocuments.length} medical documents`);
  }

  /**
   * Ladda medicinsk kunskap från olika källor
   */
  private async loadMedicalKnowledge(): Promise<Document[]> {
    const documents: Document[] = [];

    // 1. Ladda ögonsjukdomar från databas
    const diseases = await this.loadEyeDiseases();
    documents.push(...diseases);

    // 2. Ladda behandlingsprotokoll
    const treatments = await this.loadTreatmentProtocols();
    documents.push(...treatments);

    // 3. Ladda läkemedelsinformation
    const medications = await this.loadMedications();
    documents.push(...medications);

    return documents;
  }

  /**
   * Ladda ögonsjukdomar från kunskapsbas
   */
  private async loadEyeDiseases(): Promise<Document[]> {
    // I produktion: Ladda från Supabase eller fil
    // För demo: Hårdkodad data
    const eyeDiseases = [
      {
        name: 'Katarakt (Grå starr)',
        icd10: 'H25-H28',
        symptoms: [
          'suddig syn',
          'gradvis synförsämring',
          'halos runt lampor',
          'svårt att köra bil i mörker',
          'färger verkar blekare',
          'behov av starkare glasögon',
        ],
        ageGroup: 'främst äldre >60 år',
        description:
          'Grumling av ögats lins som leder till gradvis synförsämring. Den vanligaste orsaken till behandlingsbar blindhet.',
        riskFactors: [
          'ålder',
          'diabetes',
          'rökning',
          'långvarig kortisonbehandling',
          'UV-exponering',
        ],
        treatment:
          'Kataraktoperation med inläggning av konstgjord lins (IOL). KVÅ: CJE00',
      },
      {
        name: 'Glaukom (Grön starr)',
        icd10: 'H40-H42',
        symptoms: [
          'synfältsbortfall (perifer syn först)',
          'förhöjt ögontryck',
          'ofta symtomfritt tidigt',
          'tunnelseende i sena stadier',
          'huvudvärk (vid akut glaukom)',
          'rött öga (vid akut glaukom)',
        ],
        ageGroup: 'främst >40 år',
        description:
          'Progressiv skada på synnerven, ofta kopplad till förhöjt ögontryck. Kan leda till permanent synförlust om obehandlad.',
        riskFactors: [
          'hög ålder',
          'hereditet',
          'högt ögontryck',
          'diabetes',
          'migrän',
        ],
        treatment:
          'Ögondroppar (trycknedsättande), laserbehandling (SLT), kirurgi (trabekulektomi KVÅ: CJD00)',
      },
      {
        name: 'Åldersrelaterad Makuladegeneration (AMD)',
        icd10: 'H35.3',
        symptoms: [
          'böjda linjer (Amsler grid)',
          'central synförlust',
          'svårt att läsa',
          'förvrängd syn',
          'mörk fläck i centrum',
        ],
        ageGroup: '>50 år, mest >65 år',
        description:
          'Degeneration av makula (gula fläcken) som ger central synförlust. Finns i torr och våt form.',
        riskFactors: ['ålder', 'rökning', 'hereditet', 'ljus ögonfärg'],
        treatment:
          'Våt AMD: Anti-VEGF injektioner (KVÅ: CJB10). Torr AMD: Kosttillskott (AREDS2), rökstopp',
      },
      {
        name: 'Diabetesretinopati',
        icd10: 'E11.3 / H36.0',
        symptoms: [
          'suddig syn',
          'floaters',
          'synfältsbortfall',
          'ofta symtomfritt tidigt',
        ],
        ageGroup: 'diabetiker, alla åldrar',
        description:
          'Skador på retinan orsakade av diabetes. En ledande orsak till blindhet hos arbetsför ålder.',
        riskFactors: [
          'dålig glukoskontroll',
          'lång diabetesduration',
          'högt blodtryck',
          'höga blodfetter',
        ],
        treatment:
          'Laserbehandling (PRP KVÅ: CJF20), Anti-VEGF injektioner, bra diabeteskontroll',
      },
      {
        name: 'Retinal Avlossning',
        icd10: 'H33',
        symptoms: [
          'plötsliga ljusblixtar',
          'många nya floaters',
          'gardinsymptom (skugga i synfältet)',
          'plötslig synförlust',
        ],
        ageGroup: 'alla åldrar, ökad risk >50 år',
        description:
          'AKUT tillstånd där näthinnan lossnar från underliggande vävnad. Kräver akut behandling.',
        riskFactors: [
          'närsynthet',
          'ögontrauma',
          'tidigare kataraktoperation',
          'hereditet',
        ],
        treatment:
          'AKUT kirurgi: Vitrektomi, buckle, pneumatisk retinopex. Laser/kryoterapi.',
      },
      {
        name: 'Torra Ögon (Keratoconjunctivitis sicca)',
        icd10: 'H04.1',
        symptoms: [
          'brännande känsla',
          'sandkornskänsla',
          'rinnande ögon (paradoxalt)',
          'röda ögon',
          'trötta ögon vid läsning',
        ],
        ageGroup: 'alla åldrar, vanligare hos kvinnor >40 år',
        description:
          'Otillräcklig tårproduktion eller snabb avdunstning av tårfilm.',
        riskFactors: [
          'ålder',
          'Sjögrens syndrom',
          'skärmarbete',
          'vissa mediciner',
          'kontaktlinser',
        ],
        treatment:
          'Artificiella tårar, punktumplugg, omega-3, behandla bakomliggande orsak',
      },
    ];

    return eyeDiseases.map(
      (disease) =>
        new Document({
          text: this.formatDiseaseAsText(disease),
          metadata: {
            type: 'disease',
            name: disease.name,
            icd10: disease.icd10,
          },
        })
    );
  }

  /**
   * Formatera sjukdom som text för embedding
   */
  private formatDiseaseAsText(disease: any): string {
    return `
Sjukdom: ${disease.name}
ICD-10: ${disease.icd10}
Åldersgrupp: ${disease.ageGroup}

Beskrivning: ${disease.description}

Symptom:
${disease.symptoms.map((s: string) => `- ${s}`).join('\n')}

Riskfaktorer:
${disease.riskFactors.map((r: string) => `- ${r}`).join('\n')}

Behandling: ${disease.treatment}
    `.trim();
  }

  /**
   * Ladda behandlingsprotokoll
   */
  private async loadTreatmentProtocols(): Promise<Document[]> {
    const treatments = [
      {
        disease: 'Katarakt',
        protocol: `
Behandling av Katarakt:

Indikation för operation:
- Synförsämring som påverkar dagliga aktiviteter
- Visus <0.5 eller patientens subjektiva besvär
- Katarakt som hindrar undersökning/behandling av retina

Preoperativ utredning:
- Biometri (IOL-beräkning)
- Keratometri
- Ev. OCT/fundus

Operation (KVÅ: CJE00):
- Fakoemulsifikation med IOL-inläggning
- Lokalbedövning (drops eller block)
- Dagskirurgi

Postoperativ behandling:
- Antibiotikadrops 1 vecka
- Steroiddrops nedtrappning 4 veckor
- Kontroll efter 1 dag och 1 månad

Förväntad visus: Ofta 1.0 om inga andra ögonsjukdomar
        `,
      },
      {
        disease: 'Glaukom',
        protocol: `
Behandling av Primär Öppenvinkelglaukom:

Mål: Sänka ögontrycket för att förhindra synnervssk ada

1:a linjen - Medicin:
- Prostaglandinanaloger (S01EE): Latanoprost 1 droppe kväll
- Alt: Betablockerare (S01ED): Timolol 2 ggr/dag
- Alt: CAI (S01EC): Dorzolamid 2-3 ggr/dag

2:a linjen - Laser:
- Selektiv Laser Trabekuloplastik (SLT)
- Sänker IOP 20-30%
- Kan upprepas

3:e linjen - Kirurgi:
- Trabekulektomi (KVÅ: CJD00)
- Shunt/stent (KVÅ: CJD96)
- För svåra/avancerade fall

Uppföljning:
- Tryckkontroll var 3-6 månad
- Synfältsundersökning årligen
- OCT papilla årligen
        `,
      },
    ];

    return treatments.map(
      (t) =>
        new Document({
          text: t.protocol,
          metadata: { type: 'treatment_protocol', disease: t.disease },
        })
    );
  }

  /**
   * Ladda läkemedelsinformation
   */
  private async loadMedications(): Promise<Document[]> {
    const medications = [
      {
        name: 'Latanoprost (Xalatan)',
        atc: 'S01EE01',
        category: 'Prostaglandinanalog',
        indication: 'Glaukom, okulär hypertension',
        dosage: '1 droppe i drabbat öga 1 gång dagligen på kvällen',
        sideEffects:
          'Hyperemi, ökad irispigmentering, förlängda fransar, makulaödem (ovanligt)',
        contraindications: 'Överkänslighet',
      },
      {
        name: 'Timolol (Timoptic)',
        atc: 'S01ED01',
        category: 'Betablockerare',
        indication: 'Glaukom, okulär hypertension',
        dosage: '1 droppe 2 gånger dagligen',
        sideEffects:
          'Lokal: Sveda, rodnad. Systemisk: Bradykardi, bronkospasm',
        contraindications: 'Astma, KOL, bradykardi, AV-block',
      },
    ];

    return medications.map(
      (med) =>
        new Document({
          text: this.formatMedicationAsText(med),
          metadata: { type: 'medication', name: med.name, atc: med.atc },
        })
    );
  }

  /**
   * Formatera läkemedel som text
   */
  private formatMedicationAsText(med: any): string {
    return `
Läkemedel: ${med.name}
ATC: ${med.atc}
Kategori: ${med.category}

Indikation: ${med.indication}
Dosering: ${med.dosage}

Biverkningar: ${med.sideEffects}
Kontraindikationer: ${med.contraindications}
    `.trim();
  }

  /**
   * Sök sjukdomar baserat på symptom
   */
  async searchDiseases(
    symptoms: string[],
    topK: number = 5
  ): Promise<EyeDisease[]> {
    if (!this.vectorIndex) {
      throw new Error('RAG not initialized. Call initialize() first.');
    }

    const query = `Symptom: ${symptoms.join(', ')}`;

    const queryEngine = this.vectorIndex.asQueryEngine({
      similarityTopK: topK,
    });

    const response = await queryEngine.query({
      query,
    });

    // Parse response och returnera structured data
    // I produktion: Använd structured output från LLM
    return this.parseDiseasesFromResponse(response.toString(), symptoms);
  }

  /**
   * Sök behandlingar för en sjukdom
   */
  async searchTreatments(disease: string): Promise<Treatment[]> {
    if (!this.vectorIndex) {
      throw new Error('RAG not initialized. Call initialize() first.');
    }

    const query = `Behandling för ${disease}`;

    const queryEngine = this.vectorIndex.asQueryEngine({
      similarityTopK: 3,
    });

    const response = await queryEngine.query({
      query,
    });

    return this.parseTreatmentsFromResponse(response.toString());
  }

  /**
   * Sök läkemedel
   */
  async searchMedications(indication: string): Promise<Medication[]> {
    if (!this.vectorIndex) {
      throw new Error('RAG not initialized. Call initialize() first.');
    }

    const query = `Läkemedel för ${indication}`;

    const queryEngine = this.vectorIndex.asQueryEngine({
      similarityTopK: 5,
    });

    const response = await queryEngine.query({
      query,
    });

    return this.parseMedicationsFromResponse(response.toString());
  }

  /**
   * Parse diseases från RAG response
   * I produktion: Använd structured output med Zod
   */
  private parseDiseasesFromResponse(
    response: string,
    symptoms: string[]
  ): EyeDisease[] {
    // Simplified parsing - i produktion använd LLM med structured output
    // För nu returnera mock data
    return [
      {
        name: 'Katarakt',
        icd10: 'H25',
        probability: 0.75,
        matchingSymptoms: symptoms.filter((s) =>
          ['suddig', 'halos', 'natt'].some((kw) => s.toLowerCase().includes(kw))
        ),
        description: 'Grumling av ögats lins',
      },
    ];
  }

  private parseTreatmentsFromResponse(response: string): Treatment[] {
    // Simplified - använd structured output i produktion
    return [
      {
        name: 'Kataraktoperation',
        type: 'surgery' as const,
        description: 'Fakoemulsifikation med IOL-inläggning',
        kva: 'CJE00',
      },
    ];
  }

  private parseMedicationsFromResponse(response: string): Medication[] {
    return [
      {
        name: 'Latanoprost',
        atc: 'S01EE01',
        dosage: '1 droppe kväll',
      },
    ];
  }
}

// Singleton instance
export const medicalRAG = new MedicalKnowledgeRAG();
