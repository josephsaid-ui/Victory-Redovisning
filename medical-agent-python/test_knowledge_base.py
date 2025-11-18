"""
Test script for medical knowledge base
Verifies that we have exactly 200 diseases and prints statistics
"""

import sys
sys.path.insert(0, '/home/user/Victory-Redovisning/medical-agent-python')

from medical_knowledge_base.retina_macula_diseases import RETINA_MACULA_DISEASES
from medical_knowledge_base.glaucoma_diseases import GLAUCOMA_DISEASES
from medical_knowledge_base.cataract_diseases import CATARACT_DISEASES
from medical_knowledge_base.cornea_diseases import CORNEA_DISEASES
from medical_knowledge_base.inflammatory_diseases import INFLAMMATORY_DISEASES
from medical_knowledge_base.neuro_ophthalmic_diseases import NEURO_OPHTHALMIC_DISEASES
from medical_knowledge_base.refractive_diseases import REFRACTIVE_DISEASES
from medical_knowledge_base.eyelid_lacrimal_diseases import EYELID_LACRIMAL_DISEASES
from medical_knowledge_base.orbital_diseases import ORBITAL_DISEASES
from medical_knowledge_base.other_diseases import OTHER_DISEASES


# Count diseases in each category
categories = {
    'Retina och Macula': RETINA_MACULA_DISEASES,
    'Glaukom': GLAUCOMA_DISEASES,
    'Katarakt': CATARACT_DISEASES,
    'Hornhinna': CORNEA_DISEASES,
    'Inflammatoriska': INFLAMMATORY_DISEASES,
    'Neuro-oftalmologi': NEURO_OPHTHALMIC_DISEASES,
    'Refraktionsfel': REFRACTIVE_DISEASES,
    'Ögonlock och Tårvägar': EYELID_LACRIMAL_DISEASES,
    'Orbitala': ORBITAL_DISEASES,
    'Övriga': OTHER_DISEASES
}

# Combine all diseases
all_diseases = []
for diseases in categories.values():
    all_diseases.extend(diseases)

# Count urgency levels
urgency_counts = {'emergency': 0, 'urgent': 0, 'routine': 0}
for disease in all_diseases:
    urgency = disease.get('urgency', 'routine')
    if 'emergency' in urgency:
        urgency_counts['emergency'] += 1
    elif 'urgent' in urgency:
        urgency_counts['urgent'] += 1
    else:
        urgency_counts['routine'] += 1

# Count severity levels
severity_counts = {'severe': 0, 'moderate': 0, 'mild': 0}
for disease in all_diseases:
    severity = disease.get('severity', '')
    if 'severe' in severity:
        severity_counts['severe'] += 1
    if 'moderate' in severity:
        severity_counts['moderate'] += 1
    if 'mild' in severity:
        severity_counts['mild'] += 1

# Print statistics
print("=" * 70)
print("MEDICINSK KUNSKAPSBAS - STATISTIK")
print("=" * 70)
print(f"\n✅ Totalt antal sjukdomar: {len(all_diseases)}")

print("\n📊 Fördelning per kategori:")
print("-" * 70)
for category, diseases in categories.items():
    print(f"  {category:35s}: {len(diseases):3d} sjukdomar")

print("\n🚨 Fördelning per akutgrad:")
print("-" * 70)
print(f"  {'AKUT (Emergency)':35s}: {urgency_counts['emergency']:3d} sjukdomar")
print(f"  {'Brådskande (Urgent)':35s}: {urgency_counts['urgent']:3d} sjukdomar")
print(f"  {'Rutin (Routine)':35s}: {urgency_counts['routine']:3d} sjukdomar")

print("\n⚠️  Fördelning per svårighetsgrad:")
print("-" * 70)
print(f"  {'Svår (Severe)':35s}: {severity_counts['severe']:3d} sjukdomar")
print(f"  {'Måttlig (Moderate)':35s}: {severity_counts['moderate']:3d} sjukdomar")
print(f"  {'Lindrig (Mild)':35s}: {severity_counts['mild']:3d} sjukdomar")

print("\n🔥 Exempel på akuta tillstånd (Emergency):")
print("-" * 70)
emergency_diseases = [d for d in all_diseases if 'emergency' in d.get('urgency', '')]
for disease in emergency_diseases[:15]:
    print(f"  • {disease['name']}")
if len(emergency_diseases) > 15:
    print(f"  ... och {len(emergency_diseases) - 15} fler")

print("\n" + "=" * 70)
if len(all_diseases) == 200:
    print("✅ FRAMGÅNG! Kunskapsbasen är komplett med exakt 200 sjukdomar!")
else:
    print(f"⚠️  VARNING: Förväntat 200 sjukdomar, har {len(all_diseases)}")
print("=" * 70)
