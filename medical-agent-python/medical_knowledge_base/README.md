# Medicinsk Kunskapsbas - 200 Vanligaste Ögonsjukdomar

## Struktur

Denna kunskapsbas innehåller detaljerad information om de 200 vanligaste ögonsjukdommarna, organiserade i kategorier.

## Kategorier

1. **Retina och Macula** (`retina_macula_diseases.py`) - 40 sjukdomar
   - Diabetesretinopati, AMD, Retinal avlossning, Centrala venocklusioner, etc.

2. **Glaukom** (`glaucoma_diseases.py`) - 25 sjukdomar
   - Primär öppenvinklat glaukom, Trångvinklat glaukom, Normaltrycksglaukom, etc.

3. **Katarakt** (`cataract_diseases.py`) - 15 sjukdomar
   - Ålderskatarakt, Traumatisk katarakt, Kongenital katarakt, etc.

4. **Hornhinna** (`cornea_diseases.py`) - 30 sjukdomar
   - Keratit, Keratokonus, Fuchs dystrofi, Erosio corneae, etc.

5. **Inflammatoriska** (`inflammatory_diseases.py`) - 25 sjukdomar
   - Uveit, Sklerit, Episklerit, Blepharit, Konjunktivit, etc.

6. **Neuro-oftalmologi** (`neuro_ophthalmic_diseases.py`) - 20 sjukdomar
   - Optikusneurit, Papillödem, Papilatrofi, Ögonmuskelparalys, etc.

7. **Refraktionsfel** (`refractive_diseases.py`) - 15 sjukdomar
   - Myopi, Hyperopi, Astigmatism, Presbyopi, etc.

8. **Ögonlock och Tårvägar** (`eyelid_lacrimal_diseases.py`) - 15 sjukdomar
   - Chalazion, Hordeolum, Entropion, Ektropion, Dakryocystit, etc.

9. **Orbitala** (`orbital_diseases.py`) - 10 sjukdomar
   - Orbitalt cellulitis, Thyreoideaorbitopati, Orbitala tumörer, etc.

10. **Övriga** (`other_diseases.py`) - 5 sjukdomar
    - Synfältsbortfall, Dubbelseende, etc.

## Datastruktur

Varje sjukdom innehåller:

```python
{
    "name": "Svenska namnet",
    "name_en": "English name",
    "icd10": "ICD-10 kod",
    "symptoms": ["symptom 1", "symptom 2", ...],
    "anamnesis_questions": ["fråga 1", "fråga 2", ...],
    "clinical_signs": ["fynd 1", "fynd 2", ...],
    "risk_factors": ["riskfaktor 1", "riskfaktor 2", ...],
    "treatment": "Behandlingsbeskrivning",
    "kva": "KVÅ-kod (om tillämpligt)",
    "differential_diagnoses": ["DD 1", "DD 2", ...],
    "description": "Detaljerad beskrivning",
    "severity": "mild|moderate|severe",
    "urgency": "routine|urgent|emergency"
}
```

## Användning

```python
from medical_knowledge_base import get_all_diseases, get_diseases_by_category

# Hämta alla sjukdomar
all_diseases = get_all_diseases()

# Hämta specifik kategori
retina_diseases = get_diseases_by_category("retina_macula")
```

## Källor

- ICD-10-SE (Socialstyrelsen)
- KVÅ (Klassifikation av vårdåtgärder)
- AAO (American Academy of Ophthalmology) Guidelines
- Svensk Oftalmologisk Förening
- UpToDate, BMJ Best Practice
