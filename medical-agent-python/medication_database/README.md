# Läkemedelsdatabas - 100 Vanligaste Ögonläkemedel

## Struktur

Denna databas innehåller detaljerad information om de 100 vanligaste läkemedlen som används inom ögonmedicin.

## Kategorier

1. **Trycknedsättande läkemedel** - 20 läkemedel (Prostaglandiner, Beta-blockerare, CAI, Alfa-agonister, Kombinationer)
2. **Övriga kategorier** - Kommer att läggas till

## Användning

```python
from medication_database import get_all_medications

# Hämta alla läkemedel
all_meds = get_all_medications()
```

## Källor

- FASS (Farmacevtiska Specialiteter i Sverige)
- European Medicines Agency (EMA)
- American Academy of Ophthalmology
