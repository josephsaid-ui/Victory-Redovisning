# Medical Data Sources Guide

Komplett guide för att bygga upp din medicinska kunskapsbas för ögonsekreterare-appen.

## 📋 Innehåll

1. [Svenska Officiella Källor](#svenska-officiella-källor)
2. [Internationella Källor](#internationella-källor)
3. [Medicinska Databaser & API:er](#medicinska-databaser--apier)
4. [Kommersiella Lösningar](#kommersiella-lösningar)
5. [Strukturera & Importera Data](#strukturera--importera-data)
6. [Generera Embeddings](#generera-embeddings)
7. [Legal & Etik](#legal--etik)
8. [Implementation Guide](#implementation-guide)

---

## Svenska Officiella Källor

### **1. Socialstyrelsen**

#### **Nationella Riktlinjer**
- **URL:** https://www.socialstyrelsen.se/kunskapsstod-och-regler/regler-och-riktlinjer/nationella-riktlinjer/
- **Innehåll:** Evidensbaserade nationella riktlinjer för olika sjukdomar
- **Format:** PDF-dokument
- **Kostnad:** Gratis
- **Licens:** Öppen data

**Relevant för ögonvård:**
- Nationella riktlinjer för diabetesvård (inkl. diabetesretinopati)
- Vårdprogram för olika ögonsjukdomar

**Hur använda:**
```python
# Ladda ner PDF och konvertera till text
from pypdf import PdfReader

reader = PdfReader("socialstyrelsen_diabetes.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

# Insertiera i database
await supabase.table("medical_documents").insert({
    "type": "protocol",
    "name": "Nationella riktlinjer för diabetesvård",
    "content": text,
    "metadata": {
        "source": "Socialstyrelsen",
        "year": 2024,
        "url": "..."
    }
})
```

#### **ICD-10-SE (Svenska versionen)**
- **URL:** https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/
- **Innehåll:** Internationell klassifikation av sjukdomar och hälsoproblem, svensk version
- **Format:** Excel, PDF
- **Kostnad:** Gratis

**Ladda ner:**
```bash
# Manuellt från webbplatsen
# Eller använd deras öppna API (om tillgängligt)
```

#### **KVÅ (Klassifikation av vårdåtgärder)**
- **URL:** https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/kva/
- **Innehåll:** Klassifikation av medicinska procedurer och operationer
- **Format:** Excel, PDF
- **Kostnad:** Gratis

**Exempel ögon-KVÅ koder:**
- CJE00: Kataraktoperation
- CJD00: Trabekulektomi (glaukom)
- CJF20: Panretinal fotokoagulation

---

### **2. Läkemedelverket**

#### **FASS (Farmaceutiska Specialiteter i Sverige)**
- **URL:** https://www.fass.se/
- **Innehåll:** Alla läkemedel godkända i Sverige
- **Format:** Web scraping eller API
- **Kostnad:** Gratis för användning, men check terms of service

**API (Officiellt):**
```python
# FASS har inget public API, men data finns på:
# https://www.lakemedelsverket.se/sv/apotek/lakemedelsprodukt

# Alternativ: Web scraping (respektera robots.txt)
import requests
from bs4 import BeautifulSoup

def scrape_fass(medication_name):
    url = f"https://www.fass.se/LIF/product?nplId={medication_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrahera information
    indication = soup.find('div', {'class': 'indication'}).text
    dosage = soup.find('div', {'class': 'dosage'}).text

    return {
        "name": medication_name,
        "indication": indication,
        "dosage": dosage
    }
```

#### **ATC-koder**
- **URL:** https://www.whocc.no/atc_ddd_index/
- **Innehåll:** Anatomical Therapeutic Chemical (ATC) klassifikation
- **Format:** Web, kan scrapa
- **Kostnad:** Gratis

**Ögonläkemedel (S01):**
- S01E: Antiglaukommedel
- S01A: Antiinfektiva medel
- S01H: Lokalanestetika
- S01X: Övriga oftalmologika

---

### **3. 1177 Vårdguiden**

- **URL:** https://www.1177.se/
- **Innehåll:** Patientinformation om sjukdomar, symtom, behandlingar
- **Format:** HTML (web scraping)
- **Kostnad:** Gratis
- **Licens:** Check terms - kan kräva tillstånd för kommersiell användning

**Relevant innehåll:**
```python
# Exempel: Scrapa information om katarakt
import requests
from bs4 import BeautifulSoup

url = "https://www.1177.se/sjukdomar--besvar/ogon/ogonsjukdomar-och-synrubbningar/gra-starr/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extrahera symptom, behandling, etc.
content = soup.find('article').text
```

**Viktigt:** 1177 innehåll är upphovsrättsskyddat. För kommersiell användning behövs tillstånd.

---

### **4. Janusinfo (Region Stockholm)**

- **URL:** https://janusinfo.se/
- **Innehåll:** Läkemedelsinformation, behandlingsrekommendationer
- **Format:** PDF, HTML
- **Kostnad:** Gratis
- **Relevant för:** Behandlingsriktlinjer

---

## Internationella Källor

### **5. PubMed / MEDLINE (NIH)**

- **URL:** https://pubmed.ncbi.nlm.nih.gov/
- **Innehåll:** 35+ miljoner medicinska forskningsartiklar
- **Format:** API (gratis!)
- **Kostnad:** Gratis

**E-utilities API:**
```python
from Bio import Entrez

Entrez.email = "your.email@example.com"

# Sök artiklar om katarakt
handle = Entrez.esearch(db="pubmed", term="cataract treatment", retmax=100)
record = Entrez.read(handle)
handle.close()

# Hämta abstracts
for pubmed_id in record["IdList"]:
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="abstract", retmode="text")
    abstract = handle.read()
    handle.close()

    # Spara i databas
    print(abstract)
```

**Fördelar:**
- Högkvalitativ vetenskaplig data
- Gratis API
- Automatiskt uppdaterad

**Nackdelar:**
- Engelska (kan behöva översättning)
- Forskningsartiklar, inte kliniska guidelines

---

### **6. WHO ICD-11**

- **URL:** https://icd.who.int/
- **Innehåll:** Senaste versionen av ICD
- **Format:** API, REST
- **Kostnad:** Gratis

**API:**
```python
import requests

# Search for cataract
url = "https://id.who.int/icd/entity/search?q=cataract"
headers = {
    "API-Version": "v2",
    "Accept-Language": "en"
}

response = requests.get(url, headers=headers)
data = response.json()

for entity in data["destinationEntities"]:
    print(f"{entity['title']}: {entity['theCode']}")
```

---

### **7. UpToDate / DynaMed / BMJ Best Practice**

**UpToDate:**
- **URL:** https://www.uptodate.com/
- **Innehåll:** Evidensbaserad klinisk information
- **Kostnad:** **$500+/år** (subscription required)
- **Kvalitet:** Mycket hög, gold standard

**DynaMed:**
- Liknande UpToDate
- Kostnad: Subscription

**BMJ Best Practice:**
- UK-baserad
- Kostnad: Subscription

**Problem:** Alla är bakom paywall. Inte lämpligt för automatisk scraping.

---

## Medicinska Databaser & API:er

### **8. OpenFDA (US Food & Drug Administration)**

- **URL:** https://open.fda.gov/
- **Innehåll:** Drug labels, adverse events, device data
- **Format:** REST API
- **Kostnad:** Gratis

```python
import requests

# Sök ögondroppar
url = "https://api.fda.gov/drug/label.json?search=ophthalmic"
response = requests.get(url)
data = response.json()

for result in data["results"]:
    print(result["openfda"]["brand_name"])
    print(result["indications_and_usage"])
```

---

### **9. SNOMED CT**

- **URL:** https://www.snomed.org/
- **Innehåll:** Systematisk nomenklatur för medicin (kodverk)
- **Format:** MySQL, SQLite downloads
- **Kostnad:** Gratis för SNOMED International members

**Svenska SNOMED CT:**
Kan få via Socialstyrelsen för svenska termer.

---

### **10. DrugBank**

- **URL:** https://go.drugbank.com/
- **Innehåll:** Omfattande läkemedelsdatabas
- **Format:** API, CSV downloads
- **Kostnad:**
  - **Academic:** Gratis
  - **Commercial:** $2,500+/år

---

## Kommersiella Lösningar

### **11. Ferring Medical Database**

Kommersiella medicinska databaser som säljer strukturerad data:

- **Elsevier ClinicalKey**
- **Wolters Kluwer UpToDate**
- **IBM Watson Health**

**Kostnad:** $10,000-$100,000+/år

**För din use case:** Troligen för dyrt för MVP.

---

## Strukturera & Importera Data

### **Workflow för att bygga din knowledge base:**

#### **Steg 1: Samla Data från Öppna Källor**

```python
# collect_medical_data.py
import asyncio
from pathlib import Path
import json

class MedicalDataCollector:
    def __init__(self):
        self.data = []

    async def collect_from_socialstyrelsen(self):
        """Samla ICD-10 och KVÅ koder"""
        # Manuell download först, sedan parse Excel
        import pandas as pd

        icd10_df = pd.read_excel("icd10_se.xlsx")

        for _, row in icd10_df.iterrows():
            if row['Kapitel'].startswith('H'):  # Ögonsjukdomar
                self.data.append({
                    "type": "disease_code",
                    "code": row['Kod'],
                    "name": row['Benämning'],
                    "source": "Socialstyrelsen ICD-10-SE"
                })

    async def collect_from_pubmed(self, query, max_results=100):
        """Samla från PubMed"""
        from Bio import Entrez

        Entrez.email = "your@email.com"

        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)

        for pmid in record["IdList"]:
            handle = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="xml")
            article = Entrez.read(handle)

            # Parse och spara
            abstract = article['PubmedArticle'][0]['MedlineCitation']['Article']['Abstract']['AbstractText'][0]

            self.data.append({
                "type": "research",
                "pmid": pmid,
                "content": str(abstract),
                "source": "PubMed"
            })

    async def save_to_database(self, supabase):
        """Spara till Supabase"""
        for item in self.data:
            await supabase.table("medical_documents").insert({
                "type": item["type"],
                "name": item.get("name", ""),
                "content": item["content"],
                "metadata": {
                    "source": item["source"],
                    "code": item.get("code")
                }
            }).execute()

# Använd
collector = MedicalDataCollector()
await collector.collect_from_socialstyrelsen()
await collector.collect_from_pubmed("cataract treatment guidelines")
await collector.save_to_database(supabase)
```

#### **Steg 2: Manuell Curation (Viktigt!)**

För medicinsk accuracy bör du:

1. **Granska all automatiskt insamlad data**
2. **Verifiera mot auktoritativa källor**
3. **Lägg till svensk kontext**
4. **Review av medicinskt kunnig person** (dig som ögonläkare!)

```python
# manual_curation.py
# Skapa mallar för vanliga ögonsjukdomar

CURATED_EYE_DISEASES = [
    {
        "name": "Katarakt (Grå starr)",
        "icd10": "H25-H28",
        "description": "...",
        "symptoms": ["suddig syn", "halos", ...],
        "treatment": "...",
        "differential_diagnosis": ["Nuclear cataract", "Cortical cataract", ...],
        "red_flags": [],
        "reviewed_by": "Dr. [Ditt namn]",
        "last_updated": "2024-01-15"
    },
    # ... fler sjukdomar
]

# Importera curated data
for disease in CURATED_EYE_DISEASES:
    await medical_rag.add_disease(disease)
```

---

## Generera Embeddings

### **Steg 1: Välj Embedding Model**

För medicinsk data, använd **PubMedBERT** (bättre än generic BERT):

```python
from sentence_transformers import SentenceTransformer

# Ladda PubMedBERT model
model = SentenceTransformer('pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb')

# Cache model lokalt
model.save('./model_cache/pubmedbert')
```

### **Steg 2: Generera Embeddings för All Data**

```python
# generate_embeddings.py
import asyncio
from sentence_transformers import SentenceTransformer
from supabase import create_client
import numpy as np

async def generate_embeddings():
    # Load model
    model = SentenceTransformer('pritamdeka/PubMedBERT-mnli-snli-scinli-scitail-mednli-stsb')

    # Connect to Supabase
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Hämta alla dokument utan embeddings
    response = supabase.table("medical_documents")\
        .select("*")\
        .is_("embedding", None)\
        .execute()

    for doc in response.data:
        # Generera embedding
        embedding = model.encode(doc['content'])

        # Konvertera till lista (pgvector format)
        embedding_list = embedding.tolist()

        # Uppdatera i databas
        supabase.table("medical_documents")\
            .update({"embedding": embedding_list})\
            .eq("id", doc['id'])\
            .execute()

        print(f"✅ Generated embedding for: {doc['name']}")

if __name__ == "__main__":
    asyncio.run(generate_embeddings())
```

**Kör:**
```bash
python generate_embeddings.py
```

---

## Legal & Etik

### **Upphovsrätt**

#### **Gratis att använda:**
- ✅ Socialstyrelsen data (öppen data)
- ✅ Läkemedelverket data
- ✅ PubMed abstracts
- ✅ WHO ICD data
- ✅ OpenFDA data

#### **Kräver tillstånd:**
- ⚠️ 1177 innehåll (upphovsrättsskyddat)
- ⚠️ FASS (check terms of service)
- ⚠️ Janusinfo (check licens)

#### **Ej tillåtet:**
- ❌ UpToDate (paywall + TOS)
- ❌ DynaMed (paywall + TOS)
- ❌ Andra subscription services

### **GDPR**

Din app hanterar **patientdata**, så GDPR är kritiskt:

- ✅ Medical knowledge base: Ej persondata, OK
- ❌ Patient transcriptions: Persondata, kräver GDPR compliance

### **Rekommendation för Kommersiell Användning**

1. **Använd öppna källor** (Socialstyrelsen, PubMed, etc.)
2. **Komplettera med egen curation** (du som ögonläkare!)
3. **För subscription content:** Betala eller få licens
4. **Konsultera jurist** för kommers bruk

---

## Implementation Guide

### **Rekommenderad Strategi (MVP)**

#### **Fas 1: Core Knowledge Base (Vecka 1)**

**Manuell curation av topp 20 ögonsjukdomar:**

```python
# curated_diseases.py
CORE_EYE_DISEASES = [
    # 1. Katarakt
    {
        "name": "Katarakt (Grå starr)",
        "icd10": "H25",
        "symptoms": ["suddig syn", "halos runt lampor", "försämrad syn i mörker"],
        "anamnesis_questions": [
            "Ser du halos eller ringar runt lampor?",
            "Har synen försämrats gradvis?",
            "Har du svårt att köra bil på natten?"
        ],
        "treatment": "Kataraktoperation med IOL-inläggning",
        "kva": "CJE00",
        "urgency": "non-urgent"
    },

    # 2. Glaukom
    {
        "name": "Primär öppenvinkelglaukom",
        "icd10": "H40.1",
        "symptoms": ["synfältsbortfall", "förhöjt ögontryck"],
        "anamnesis_questions": [
            "Har du märkt förändringar i din perifera syn?",
            "Har du hereditet för glaukom?"
        ],
        "treatment": "Trycknedsättande ögondroppar (prostaglandinanaloger)",
        "medications": ["Latanoprost", "Timolol"],
        "urgency": "semi-urgent"
    },

    # 3. Retinal avlossning
    {
        "name": "Retinal avlossning",
        "icd10": "H33",
        "symptoms": ["ljusblixtar", "floaters", "gardinsymptom"],
        "anamnesis_questions": [
            "Ser du plötsliga ljusblixtar?",
            "Ser du många nya svävande prickar?",
            "Ser du en gardin eller skugga i synfältet?"
        ],
        "treatment": "AKUT kirurgi - vitrektomi eller buckle",
        "urgency": "ACUTE",
        "red_flags": ["plötslig synförlust", "ljusblixtar", "gardinsymptom"]
    },

    # ... 17 fler sjukdomar
]
```

**Importera:**
```python
for disease in CORE_EYE_DISEASES:
    # Generera embedding
    embedding = model.encode(json.dumps(disease))

    # Insert
    supabase.table("medical_documents").insert({
        "type": "disease",
        "name": disease["name"],
        "content": json.dumps(disease),
        "metadata": disease,
        "embedding": embedding.tolist()
    }).execute()
```

#### **Fas 2: Läkemedel från FASS (Vecka 2)**

Scrapa eller manuellt lägga till de 20 vanligaste ögonläkemedlen:

```python
CORE_EYE_MEDICATIONS = [
    {
        "name": "Latanoprost (Xalatan)",
        "atc": "S01EE01",
        "indication": "Glaukom",
        "dosage": "1 droppe kväll",
        "side_effects": "Ökad irispigmentering, hyperemi",
        "contraindications": "Överkänslighet"
    },
    # ... fler
]
```

#### **Fas 3: PubMed Research (Vecka 3)**

Automatiskt hämta och indexera research för varje sjukdom:

```python
for disease in CORE_EYE_DISEASES:
    # Hämta 10 senaste artiklarna
    articles = fetch_pubmed_articles(
        query=f"{disease['name']} treatment guidelines",
        max_results=10
    )

    for article in articles:
        # Generera embedding och spara
        ...
```

#### **Fas 4: Kontinuerlig Uppdatering (Ongoing)**

```python
# Scheduled job (kör månatligen)
async def update_knowledge_base():
    # Check PubMed för nya artiklar
    # Scrapa uppdateringar från Socialstyrelsen
    # Re-generera embeddings för uppdaterad content
    ...
```

---

## Quick Start: Minimal Knowledge Base

För att komma igång IDAG:

```python
# minimal_kb.py - 30 minuter att implementera

MINIMAL_EYE_DISEASES = [
    "Katarakt", "Glaukom", "AMD", "Diabetesretinopati",
    "Retinal avlossning", "Torra ögon", "Konjunktivit",
    "Keratit", "Uveit", "Närsynthet"
]

# För varje sjukdom:
# 1. Googla "1177 [sjukdom]"
# 2. Copy-paste text
# 3. Lägg till egen expertis
# 4. Generera embedding
# 5. Insert i databas

# Total tid: ~3 timmar för 10 sjukdomar
```

---

## Sammanfattning

### **Rekommenderad Approach:**

1. **Start med manuell curation (20 sjukdomar)**
   - Tid: 1-2 veckor
   - Kostnad: $0
   - Kvalitet: Hög (din expertise!)

2. **Komplettera med Socialstyrelsen data**
   - ICD-10 koder
   - KVÅ koder
   - Nationella riktlinjer

3. **Lägg till PubMed research**
   - Automatisk indexering
   - Kontinuerlig uppdatering

4. **Framtida: Subscription till UpToDate**
   - När du har revenue
   - Kostnad: $500-1000/år

### **Kostnad för MVP:**

```
Manuell curation: $0 (din tid)
Socialstyrelsen data: $0
PubMed API: $0
Embeddings (compute): $5-10
Total: ~$10 + din tid
```

### **Nästa steg:**

Vill du att jag:
1. **Skapar en pre-populated database** med 20 curerade ögonsjukdomar?
2. **Skriver scripts** för att scrapa Socialstyrelsen data?
3. **Implementerar PubMed integration**?

Säg bara till! 🚀
