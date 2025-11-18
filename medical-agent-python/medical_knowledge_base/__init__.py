"""
Medical Knowledge Base - Medicinsk Kunskapsbas
Complete database of 200 common eye diseases

This module provides comprehensive medical information about 200 common eye diseases,
organized by category with detailed clinical information in Swedish.
"""

from .retina_macula_diseases import RETINA_MACULA_DISEASES
from .glaucoma_diseases import GLAUCOMA_DISEASES
from .cataract_diseases import CATARACT_DISEASES
from .cornea_diseases import CORNEA_DISEASES
from .inflammatory_diseases import INFLAMMATORY_DISEASES
from .neuro_ophthalmic_diseases import NEURO_OPHTHALMIC_DISEASES
from .refractive_diseases import REFRACTIVE_DISEASES
from .eyelid_lacrimal_diseases import EYELID_LACRIMAL_DISEASES
from .orbital_diseases import ORBITAL_DISEASES
from .other_diseases import OTHER_DISEASES


# Category mapping
DISEASE_CATEGORIES = {
    'retina_macula': RETINA_MACULA_DISEASES,
    'glaucoma': GLAUCOMA_DISEASES,
    'cataract': CATARACT_DISEASES,
    'cornea': CORNEA_DISEASES,
    'inflammatory': INFLAMMATORY_DISEASES,
    'neuro_ophthalmic': NEURO_OPHTHALMIC_DISEASES,
    'refractive': REFRACTIVE_DISEASES,
    'eyelid_lacrimal': EYELID_LACRIMAL_DISEASES,
    'orbital': ORBITAL_DISEASES,
    'other': OTHER_DISEASES
}


def get_all_diseases():
    """
    Get all 200 diseases from all categories

    Returns:
        list: All disease dictionaries from all categories
    """
    all_diseases = []
    for category_diseases in DISEASE_CATEGORIES.values():
        all_diseases.extend(category_diseases)
    return all_diseases


def get_diseases_by_category(category):
    """
    Get diseases from a specific category

    Args:
        category (str): Category name (e.g., 'retina_macula', 'glaucoma')

    Returns:
        list: Disease dictionaries from the specified category
    """
    return DISEASE_CATEGORIES.get(category, [])


def get_disease_by_name(name):
    """
    Search for a disease by name (Swedish or English)

    Args:
        name (str): Disease name to search for

    Returns:
        dict: Disease dictionary if found, None otherwise
    """
    name_lower = name.lower()
    all_diseases = get_all_diseases()

    for disease in all_diseases:
        if (name_lower in disease.get('name', '').lower() or
            name_lower in disease.get('name_en', '').lower()):
            return disease

    return None


def get_diseases_by_urgency(urgency):
    """
    Get all diseases with a specific urgency level

    Args:
        urgency (str): 'routine', 'urgent', or 'emergency'

    Returns:
        list: Disease dictionaries matching the urgency level
    """
    all_diseases = get_all_diseases()
    return [d for d in all_diseases if d.get('urgency') == urgency]


def get_diseases_by_severity(severity):
    """
    Get all diseases with a specific severity level

    Args:
        severity (str): 'mild', 'moderate', or 'severe'

    Returns:
        list: Disease dictionaries matching the severity level
    """
    all_diseases = get_all_diseases()
    return [d for d in all_diseases if severity in d.get('severity', '')]


def get_emergency_diseases():
    """
    Get all emergency diseases that require immediate attention

    Returns:
        list: Disease dictionaries with urgency='emergency'
    """
    return get_diseases_by_urgency('emergency')


def search_diseases(keyword):
    """
    Search for diseases by keyword in name, symptoms, or treatment

    Args:
        keyword (str): Keyword to search for

    Returns:
        list: Disease dictionaries matching the keyword
    """
    keyword_lower = keyword.lower()
    all_diseases = get_all_diseases()
    results = []

    for disease in all_diseases:
        # Search in name
        if keyword_lower in disease.get('name', '').lower():
            results.append(disease)
            continue
        if keyword_lower in disease.get('name_en', '').lower():
            results.append(disease)
            continue

        # Search in symptoms
        symptoms = disease.get('symptoms', [])
        if any(keyword_lower in symptom.lower() for symptom in symptoms):
            results.append(disease)
            continue

        # Search in treatment
        treatment = disease.get('treatment', '')
        if keyword_lower in treatment.lower():
            results.append(disease)
            continue

    return results


def get_statistics():
    """
    Get statistics about the knowledge base

    Returns:
        dict: Statistics including total count, category breakdown, urgency distribution
    """
    all_diseases = get_all_diseases()

    stats = {
        'total_diseases': len(all_diseases),
        'by_category': {
            category: len(diseases)
            for category, diseases in DISEASE_CATEGORIES.items()
        },
        'by_urgency': {
            'emergency': len(get_diseases_by_urgency('emergency')),
            'urgent': len(get_diseases_by_urgency('urgent')),
            'routine': len(get_diseases_by_urgency('routine'))
        },
        'by_severity': {
            'severe': len(get_diseases_by_severity('severe')),
            'moderate': len(get_diseases_by_severity('moderate')),
            'mild': len(get_diseases_by_severity('mild'))
        }
    }

    return stats


# Export main functions
__all__ = [
    'get_all_diseases',
    'get_diseases_by_category',
    'get_disease_by_name',
    'get_diseases_by_urgency',
    'get_diseases_by_severity',
    'get_emergency_diseases',
    'search_diseases',
    'get_statistics',
    'DISEASE_CATEGORIES',
    'RETINA_MACULA_DISEASES',
    'GLAUCOMA_DISEASES',
    'CATARACT_DISEASES',
    'CORNEA_DISEASES',
    'INFLAMMATORY_DISEASES',
    'NEURO_OPHTHALMIC_DISEASES',
    'REFRACTIVE_DISEASES',
    'EYELID_LACRIMAL_DISEASES',
    'ORBITAL_DISEASES',
    'OTHER_DISEASES'
]


if __name__ == "__main__":
    # Print statistics when module is run directly
    stats = get_statistics()

    print("=" * 60)
    print("MEDICINSK KUNSKAPSBAS - STATISTIK")
    print("=" * 60)
    print(f"\nTotalt antal sjukdomar: {stats['total_diseases']}")

    print("\n📊 Fördelning per kategori:")
    print("-" * 60)
    category_names = {
        'retina_macula': 'Retina och Macula',
        'glaucoma': 'Glaukom',
        'cataract': 'Katarakt',
        'cornea': 'Hornhinna',
        'inflammatory': 'Inflammatoriska',
        'neuro_ophthalmic': 'Neuro-oftalmologi',
        'refractive': 'Refraktionsfel',
        'eyelid_lacrimal': 'Ögonlock och Tårvägar',
        'orbital': 'Orbitala',
        'other': 'Övriga'
    }

    for category, count in stats['by_category'].items():
        print(f"  {category_names.get(category, category):30s}: {count:3d} sjukdomar")

    print("\n🚨 Fördelning per akutgrad:")
    print("-" * 60)
    for urgency, count in stats['by_urgency'].items():
        urgency_sv = {
            'emergency': 'AKUT (Emergency)',
            'urgent': 'Brådskande (Urgent)',
            'routine': 'Rutin (Routine)'
        }
        print(f"  {urgency_sv.get(urgency, urgency):30s}: {count:3d} sjukdomar")

    print("\n⚠️  Fördelning per svårighetsgrad:")
    print("-" * 60)
    for severity, count in stats['by_severity'].items():
        severity_sv = {
            'severe': 'Svår (Severe)',
            'moderate': 'Måttlig (Moderate)',
            'mild': 'Lindrig (Mild)'
        }
        print(f"  {severity_sv.get(severity, severity):30s}: {count:3d} sjukdomar")

    print("\n🔥 Akuta tillstånd (Emergency):")
    print("-" * 60)
    emergency = get_emergency_diseases()
    for disease in emergency[:10]:  # Show first 10
        print(f"  • {disease['name']}")
    if len(emergency) > 10:
        print(f"  ... och {len(emergency) - 10} fler")

    print("\n" + "=" * 60)
    print("Kunskapsbasen är komplett och redo att användas!")
    print("=" * 60)
