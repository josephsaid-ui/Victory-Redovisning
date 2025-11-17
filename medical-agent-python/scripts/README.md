# Medical Data Collection Scripts

Scripts för att bygga upp din medicinska kunskapsbas.

## 🎯 Quick Start

### **Steg 1: Samla Data**

```bash
# Kör data collection script
python scripts/collect_medical_data.py
```

Detta skapar `data/medical_data.json` med:
- 5 curerade ögonsjukdomar (exempel)
- 2 läkemedel (exempel)
- Optional: PubMed artiklar

### **Steg 2: Importera till Database**

```bash
# Säkerställ att .env är konfigurerad
# SUPABASE_URL=...
# SUPABASE_SERVICE_KEY=...

# Importera data och generera embeddings
python scripts/import_to_database.py
```

Detta:
- ✅ Laddar data från JSON
- ✅ Genererar PubMedBERT embeddings
- ✅ Importerar till Supabase
- ✅ Verifierar import

### **Steg 3: Testa**

```bash
python examples/basic_example.py
```

---

## 📁 Scripts

### **collect_medical_data.py**

Samlar medicinsk data från olika källor.

**Vad det gör:**
- Laddar curerad data för ögonsjukdomar
- Laddar curerad läkemedelsinformation
- Optional: Hämtar från PubMed API
- Exporterar till JSON

**Användning:**
```python
from scripts.collect_medical_data import MedicalDataCollector

collector = MedicalDataCollector()

# Ladda curated data
diseases = collector.load_curated_diseases()
medications = collector.load_curated_medications()

# Hämta från PubMed (kräver biopython)
articles = await collector.fetch_from_pubmed("cataract treatment", max_results=10)

# Exportera
collector.export_to_json("medical_data.json")
```

**Output:**
```
data/medical_data.json
```

---

### **import_to_database.py**

Importerar data till Supabase och genererar embeddings.

**Vad det gör:**
- Läser JSON data
- Genererar PubMedBERT embeddings (768-dim)
- Importerar till `medical_documents` table
- Verifierar import

**Användning:**
```bash
python scripts/import_to_database.py
```

**Kräver:**
- Supabase project setup
- Environment variables (SUPABASE_URL, SUPABASE_SERVICE_KEY)
- `pip install sentence-transformers torch`

**Output:**
```
✅ Imported: Katarakt (Grå starr)
✅ Imported: Glaukom
...
✅ Verification complete!
```

---

## 🔧 Customization

### **Lägg Till Fler Sjukdomar**

Edit `collect_medical_data.py`:

```python
CURATED_EYE_DISEASES = [
    {
        "name": "Din Sjukdom",
        "icd10": "H00.0",
        "description": "Beskrivning...",
        "symptoms": ["symptom 1", "symptom 2"],
        "treatment": "Behandling...",
        # ... mer data
    },
    # ... existing diseases
]
```

### **Lägg Till Fler Läkemedel**

```python
CURATED_MEDICATIONS = [
    {
        "name": "Läkemedelsnamn",
        "atc": "S01XX01",
        "indication": "Indikation...",
        # ... mer data
    },
]
```

### **Hämta från PubMed**

```python
# I collect_medical_data.py main():
pubmed_articles = await collector.fetch_from_pubmed(
    query="diabetic retinopathy treatment guidelines",
    max_results=20
)
```

---

## 📊 Data Format

### **Disease Object**

```json
{
  "name": "Katarakt (Grå starr)",
  "icd10": "H25",
  "description": "Grumling av ögats lins...",
  "symptoms": ["suddig syn", "halos"],
  "risk_factors": ["ålder", "diabetes"],
  "anamnesis_questions": ["Ser du halos?", "..."],
  "examination": ["Visus", "Slitslampundersökning"],
  "treatment": "Kataraktoperation...",
  "kva": "CJE00",
  "medications": [],
  "urgency": "non-urgent",
  "red_flags": [],
  "prognosis": "Excellent med operation",
  "follow_up": "Kontroll dag 1 och vecka 4"
}
```

### **Medication Object**

```json
{
  "name": "Latanoprost",
  "brand_names": ["Xalatan"],
  "atc": "S01EE01",
  "category": "Prostaglandinanalog",
  "indication": "Glaukom",
  "mechanism": "Ökar uveoskleralt utflöde",
  "dosage": "1 droppe kväll",
  "side_effects": ["Hyperemi", "Ökad irispigmentering"],
  "contraindications": ["Överkänslighet"],
  "pregnancy_category": "C",
  "cost": "~100 kr/flaska"
}
```

---

## 🚀 Advanced Usage

### **Batch Import från Flera Källor**

```python
# custom_import.py
import asyncio
from scripts.collect_medical_data import MedicalDataCollector
from scripts.import_to_database import MedicalDataImporter

async def batch_import():
    collector = MedicalDataCollector()
    importer = MedicalDataImporter()

    # 1. Samla från PubMed för varje sjukdom
    diseases = collector.load_curated_diseases()

    for disease in diseases:
        articles = await collector.fetch_from_pubmed(
            f"{disease['name']} treatment guidelines",
            max_results=5
        )

        # Importera artiklar
        for article in articles:
            embedding = importer.generate_embedding(article['abstract'])

            await importer.supabase.table("medical_documents").insert({
                "type": "research",
                "name": article['title'],
                "content": article['abstract'],
                "metadata": {"pmid": article['pmid'], "disease": disease['name']},
                "embedding": embedding
            }).execute()

asyncio.run(batch_import())
```

### **Auto-Update från PubMed**

```python
# Scheduled job (kör månatligen)
async def update_knowledge_base():
    """Uppdatera kunskapsbas med nya PubMed artiklar"""
    collector = MedicalDataCollector()

    # Hämta artiklar från senaste månaden
    for disease in ["cataract", "glaucoma", "AMD"]:
        articles = await collector.fetch_from_pubmed(
            f"{disease} treatment guidelines AND (\"last 30 days\"[PDat])",
            max_results=10
        )

        # Importera nya artiklar...
```

---

## 🐛 Troubleshooting

### Problem: "biopython not installed"

```bash
pip install biopython
```

### Problem: "sentence-transformers not installed"

```bash
pip install sentence-transformers torch
```

### Problem: "SUPABASE_URL not set"

Skapa `.env` fil:
```bash
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_KEY=eyJxxx
```

### Problem: Import tar lång tid

Embedding generation är långsam första gången (modellen måste laddas).

**Lösning:** Använd cache:
```python
model = SentenceTransformer(
    'pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb',
    cache_folder='./model_cache'  # Cache lokalt
)
```

### Problem: Out of memory

PubMedBERT kräver ~2GB RAM.

**Lösning:** Stäng andra program eller använd mindre model:
```python
# Mindre model (snabbare men mindre accuracy)
model = SentenceTransformer('all-MiniLM-L6-v2')
```

---

## 📚 Resources

- [PubMed E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
- [Sentence Transformers Docs](https://www.sbert.net/)
- [PubMedBERT Paper](https://arxiv.org/abs/2007.15779)
- [Socialstyrelsen Öppna Data](https://www.socialstyrelsen.se/statistik-och-data/oppna-data/)

---

## 🎯 Next Steps

1. **Expand disease coverage:**
   - Lägg till 20+ ögonsjukdomar
   - Inkludera sällsynta tillstånd

2. **Add treatment protocols:**
   - Svenska vårdprogram
   - Socialstyrelsen riktlinjer

3. **Integrate more sources:**
   - FASS för läkemedel
   - 1177 för patientinformation
   - Janusinfo för behandlingsriktlinjer

4. **Auto-update:**
   - Scheduled PubMed sync
   - Version control för medical data

5. **Quality assurance:**
   - Medical review process
   - Accuracy validation
   - Source verification

Se [MEDICAL_DATA_SOURCES.md](../MEDICAL_DATA_SOURCES.md) för mer information!
