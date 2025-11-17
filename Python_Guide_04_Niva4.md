# 🐍 Nivå 4: Avancerade koncept och OOP

## 🎯 Lärandemål för Nivå 4

Efter detta kapitel kommer du att kunna:
- ✅ Förstå objektorienterad programmering (OOP)
- ✅ Skapa och använda klasser och objekt
- ✅ Implementera arv och polymorfism
- ✅ Använda decorators och generators
- ✅ Arbeta med context managers
- ✅ Skriva type hints för bättre kodkvalitet
- ✅ Följa PEP 8 style guide
- ✅ Bygga en komplett TODO-app med GUI

---

## 4.1 Objektorienterad programmering - Introduktion 🏗️

**OOP** (Object-Oriented Programming) är ett sätt att organisera kod genom att gruppera relaterad data och funktioner tillsammans.

### Varför OOP?

Tänk dig att du ska programmera ett spel med 100 olika karaktärer. Utan OOP:

```python
# Utan OOP - rörigt! 😰
spelare1_namn = "Anna"
spelare1_hälsa = 100
spelare1_attack = 15

spelare2_namn = "Erik"
spelare2_hälsa = 100
spelare2_attack = 15
# ...och 98 till!
```

Med OOP:

```python
# Med OOP - snyggt! 😊
class Spelare:
    def __init__(self, namn):
        self.namn = namn
        self.hälsa = 100
        self.attack = 15

spelare1 = Spelare("Anna")
spelare2 = Spelare("Erik")
```

### Grundläggande terminologi 📚

```
┌──────────────────────────────────────────────────┐
│ KLASS (Class)                                    │
│ ├─ Blueprint/ritning för objekt                  │
│ └─ Definierar attribut och metoder               │
│                                                   │
│ OBJEKT (Object)                                  │
│ ├─ Instans av en klass                           │
│ └─ Konkret "exemplar" skapat från klassen        │
│                                                   │
│ ATTRIBUT (Attributes)                            │
│ ├─ Variabler som tillhör objektet                │
│ └─ Beskriver objektets tillstånd/egenskaper      │
│                                                   │
│ METOD (Method)                                   │
│ ├─ Funktion som tillhör klassen                  │
│ └─ Beskriver vad objektet kan göra               │
└──────────────────────────────────────────────────┘
```

---

## 4.2 Skapa din första klass 🎨

### Grundläggande klassstruktur

```python
class Hund:
    """En enkel klass som representerar en hund."""

    # Konstruktor - körs när objekt skapas
    def __init__(self, namn, ålder):
        # Attribut (instansvariabler)
        self.namn = namn
        self.ålder = ålder

    # Metod (funktion i klassen)
    def skäll(self):
        print(f"{self.namn} säger: Voff!")

    def info(self):
        print(f"{self.namn} är {self.ålder} år gammal")

# Skapa objekt (instanser av klassen)
min_hund = Hund("Bella", 3)
din_hund = Hund("Max", 5)

# Använd metoder
min_hund.skäll()    # Output: Bella säger: Voff!
din_hund.skäll()    # Output: Max säger: Voff!

# Visa info
min_hund.info()     # Output: Bella är 3 år gammal
din_hund.info()     # Output: Max är 5 år gammal

# Åtkomst till attribut
print(min_hund.namn)    # Output: Bella
print(din_hund.ålder)   # Output: 5
```

### Viktiga detaljer om klasser 🔍

**`self`** - Referens till objektet själv:
```python
class Exempel:
    def __init__(self, värde):
        self.värde = värde  # self.värde = objektets attribut

    def visa(self):
        print(self.värde)   # Använd self för att komma åt attribut

obj = Exempel(10)
obj.visa()  # Output: 10
```

**`__init__`** - Konstruktor (kallas automatiskt när objekt skapas):
```python
class Person:
    def __init__(self, namn, ålder):
        print(f"Skapar person: {namn}")
        self.namn = namn
        self.ålder = ålder

p = Person("Anna", 25)  # Output: Skapar person: Anna
```

### Praktiskt exempel: Bankkonto 💰

```python
class Bankkonto:
    """Representerar ett bankkonto."""

    def __init__(self, ägare, saldo=0):
        self.ägare = ägare
        self.saldo = saldo

    def sätt_in(self, belopp):
        """Sätt in pengar på kontot."""
        if belopp > 0:
            self.saldo += belopp
            print(f"✅ Satte in {belopp} kr. Nytt saldo: {self.saldo} kr")
        else:
            print("❌ Beloppet måste vara positivt!")

    def ta_ut(self, belopp):
        """Ta ut pengar från kontot."""
        if belopp > self.saldo:
            print(f"❌ Otillräckligt saldo! Du har {self.saldo} kr")
        elif belopp <= 0:
            print("❌ Beloppet måste vara positivt!")
        else:
            self.saldo -= belopp
            print(f"✅ Tog ut {belopp} kr. Nytt saldo: {self.saldo} kr")

    def visa_saldo(self):
        """Visa kontoinformation."""
        print(f"💰 Konto: {self.ägare}")
        print(f"   Saldo: {self.saldo} kr")

# Användning
konto = Bankkonto("Anna", 1000)
konto.visa_saldo()      # Saldo: 1000 kr
konto.sätt_in(500)      # Satte in 500 kr
konto.ta_ut(200)        # Tog ut 200 kr
konto.visa_saldo()      # Saldo: 1300 kr
```

---

## 4.3 Arv - Återanvända kod 🧬

**Arv** (inheritance) låter en klass ärva attribut och metoder från en annan klass.

### Grundläggande arv

```python
# Föräldraklass (basklass, superklass)
class Djur:
    def __init__(self, namn):
        self.namn = namn

    def äta(self):
        print(f"{self.namn} äter")

    def sov(self):
        print(f"{self.namn} sover")

# Barnklass (subklass) ärver från Djur
class Hund(Djur):
    def skäll(self):
        print(f"{self.namn} säger: Voff!")

class Katt(Djur):
    def jamal(self):
        print(f"{self.namn} säger: Mjau!")

# Användning
hund = Hund("Bella")
hund.äta()      # Ärvd metod från Djur
hund.skäll()    # Egen metod

katt = Katt("Whiskers")
katt.äta()      # Ärvd metod från Djur
katt.jamal()    # Egen metod
```

### Överskugga metoder (Override)

```python
class Fordon:
    def __init__(self, märke):
        self.märke = märke

    def starta(self):
        print("Fordonet startar...")

class Bil(Fordon):
    # Överskugga starta-metoden
    def starta(self):
        print(f"Vroom! {self.märke} startar motorn! 🚗")

class Cykel(Fordon):
    def starta(self):
        print(f"Börjar trampa på {self.märke}! 🚴")

# Test
bil = Bil("Volvo")
bil.starta()    # Output: Vroom! Volvo startar motorn! 🚗

cykel = Cykel("Crescent")
cykel.starta()  # Output: Börjar trampa på Crescent! 🚴
```

### super() - Anropa föräldraklassens metod

```python
class Person:
    def __init__(self, namn, ålder):
        self.namn = namn
        self.ålder = ålder

    def presentera(self):
        print(f"Jag heter {self.namn} och är {self.ålder} år")

class Student(Person):
    def __init__(self, namn, ålder, skola):
        # Anropa föräldraklassens __init__
        super().__init__(namn, ålder)
        self.skola = skola

    def presentera(self):
        # Anropa föräldraklassens presentera
        super().presentera()
        print(f"Jag går på {self.skola}")

# Test
student = Student("Anna", 16, "Gymnasiet")
student.presentera()
# Output:
# Jag heter Anna och är 16 år
# Jag går på Gymnasiet
```

### Arv-hierarki visualisering 🌳

```
        Djur
         |
    ┌────┴────┐
    │         │
  Hund      Katt
    │
  ┌─┴─┐
  │   │
Pudel Labrador
```

---

## 4.4 Polymorfism - En form, många beteenden 🎭

**Polymorfism** betyder att samma metod kan ha olika beteenden i olika klasser.

```python
class Form:
    def area(self):
        pass

class Rektangel(Form):
    def __init__(self, bredd, höjd):
        self.bredd = bredd
        self.höjd = höjd

    def area(self):
        return self.bredd * self.höjd

class Cirkel(Form):
    def __init__(self, radie):
        self.radie = radie

    def area(self):
        return 3.14159 * self.radie ** 2

# Polymorfism i aktion!
former = [
    Rektangel(5, 3),
    Cirkel(4),
    Rektangel(10, 2)
]

# Samma metod-namn, olika beteende
for form in former:
    print(f"Area: {form.area():.2f}")

# Output:
# Area: 15.00
# Area: 50.27
# Area: 20.00
```

---

## 4.5 Speciella metoder (Magic methods) ✨

Python har speciella metoder som börjar och slutar med `__` (double underscore/"dunder").

### Vanliga magic methods

```python
class Bok:
    def __init__(self, titel, författare, sidor):
        self.titel = titel
        self.författare = författare
        self.sidor = sidor

    # __str__ - snygg string-representation för användare
    def __str__(self):
        return f"'{self.titel}' av {self.författare}"

    # __repr__ - teknisk representation för debugging
    def __repr__(self):
        return f"Bok('{self.titel}', '{self.författare}', {self.sidor})"

    # __len__ - vad len() ska returnera
    def __len__(self):
        return self.sidor

    # __eq__ - jämförelse med ==
    def __eq__(self, other):
        return self.titel == other.titel and self.författare == other.författare

    # __lt__ - jämförelse med <
    def __lt__(self, other):
        return self.sidor < other.sidor

# Test
bok1 = Bok("Python 101", "Anna Andersson", 200)
bok2 = Bok("Python 101", "Anna Andersson", 200)
bok3 = Bok("Advanced Python", "Erik Eriksson", 350)

print(bok1)              # Output: 'Python 101' av Anna Andersson
print(repr(bok1))        # Output: Bok('Python 101', 'Anna Andersson', 200)
print(len(bok1))         # Output: 200
print(bok1 == bok2)      # Output: True
print(bok1 < bok3)       # Output: True (200 < 350)
```

### Tabell över magic methods 📊

```
┌────────────────┬──────────────────────────────┐
│ Metod          │ Beskrivning                  │
├────────────────┼──────────────────────────────┤
│ __init__       │ Konstruktor                  │
│ __str__        │ String-representation        │
│ __repr__       │ Teknisk representation       │
│ __len__        │ Längd (len())                │
│ __eq__         │ Jämförelse (==)              │
│ __lt__         │ Mindre än (<)                │
│ __gt__         │ Större än (>)                │
│ __add__        │ Addition (+)                 │
│ __getitem__    │ Index-åtkomst ([])           │
│ __call__       │ Gör objektet anropbart ()    │
└────────────────┴──────────────────────────────┘
```

---

## 4.6 Decorators - Utöka funktionalitet 🎀

**Decorators** är ett sätt att modifiera eller utöka funktioner utan att ändra deras kod.

### Enkel decorator

```python
# Definiera en decorator
def min_decorator(func):
    def wrapper():
        print("=== Före funktionen ===")
        func()
        print("=== Efter funktionen ===")
    return wrapper

# Använd decorator med @-syntax
@min_decorator
def säg_hej():
    print("Hej!")

# När vi anropar funktionen körs wrapper
säg_hej()
# Output:
# === Före funktionen ===
# Hej!
# === Efter funktionen ===
```

### Decorator med parametrar

```python
def repeat(antal_gånger):
    """Decorator som upprepar funktion N gånger."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(antal_gånger):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hälsa(namn):
    print(f"Hej {namn}!")

hälsa("Anna")
# Output:
# Hej Anna!
# Hej Anna!
# Hej Anna!
```

### Praktisk decorator: Timer ⏱️

```python
import time

def timer(func):
    """Mät hur lång tid en funktion tar."""
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = func(*args, **kwargs)
        slut = time.time()
        print(f"⏱️ {func.__name__} tog {slut - start:.4f} sekunder")
        return resultat
    return wrapper

@timer
def långsam_funktion():
    """Simulerar långsam operation."""
    total = 0
    for i in range(1000000):
        total += i
    return total

resultat = långsam_funktion()
# Output: ⏱️ långsam_funktion tog 0.0523 sekunder
```

---

## 4.7 Generators - Minneseffektiva iteratorer 🔄

**Generators** skapar värden "on-the-fly" istället för att lagra alla i minnet.

### Vanlig funktion vs Generator

```python
# Vanlig funktion - lagrar alla värden i minnet
def kvadrater_lista(n):
    resultat = []
    for i in range(n):
        resultat.append(i ** 2)
    return resultat

# Generator - genererar värden ett i taget
def kvadrater_generator(n):
    for i in range(n):
        yield i ** 2  # yield istället för return!

# Användning
lista = kvadrater_lista(5)
print(lista)  # Output: [0, 1, 4, 9, 16]

gen = kvadrater_generator(5)
for värde in gen:
    print(värde, end=" ")  # Output: 0 1 4 9 16
```

### Fördelar med generators 💡

```python
# Lista tar mycket minne för stora N
# lista = [i**2 for i in range(10000000)]  # Många MB!

# Generator tar minimal minne
gen = (i**2 for i in range(10000000))  # Några bytes!

# Generator expression (som list comprehension men med ())
jämna = (x for x in range(100) if x % 2 == 0)
for tal in jämna:
    if tal > 20:
        break
    print(tal)
```

### Praktiskt exempel: Fibonacci-generator

```python
def fibonacci():
    """Oändlig Fibonacci-sekvens."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Använd generator
fib = fibonacci()
for i, värde in enumerate(fib):
    print(värde, end=" ")
    if i >= 10:  # Stoppa efter 11 tal
        break
# Output: 0 1 1 2 3 5 8 13 21 34 55
```

---

## 4.8 Context managers - Resurshantering 🔐

**Context managers** hanterar resurser (filer, nätverk, etc.) på ett säkert sätt.

### with-statement

```python
# Utan with - måste komma ihåg att stänga!
fil = open("test.txt", "w")
fil.write("Hej!")
fil.close()  # Lätt att glömma!

# Med with - stängs automatiskt!
with open("test.txt", "w") as fil:
    fil.write("Hej!")
# Filen stängs automatiskt här, även vid fel!
```

### Skapa egen context manager

```python
class Timer:
    """Context manager för att mäta tid."""

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.slut = time.time()
        self.tid = self.slut - self.start
        print(f"⏱️ Tog {self.tid:.4f} sekunder")

# Användning
with Timer():
    total = sum(range(1000000))
    print(f"Summa: {total}")
# Output:
# Summa: 499999500000
# ⏱️ Tok 0.0342 sekunder
```

---

## 4.9 Type hints - Tydligare kod 📝

**Type hints** anger vilka datatyper funktioner förväntar sig och returnerar.

### Grundläggande type hints

```python
# Utan type hints
def hälsa(namn):
    return f"Hej {namn}!"

# Med type hints
def hälsa(namn: str) -> str:
    return f"Hej {namn}!"

# Fler exempel
def addera(a: int, b: int) -> int:
    return a + b

def är_vuxen(ålder: int) -> bool:
    return ålder >= 18

# Type hints för listor, dict, etc.
from typing import List, Dict, Optional

def summera_lista(tal: List[int]) -> int:
    return sum(tal)

def få_person(person_id: int) -> Optional[Dict[str, str]]:
    # Optional betyder: returnerar Dict eller None
    if person_id == 1:
        return {"namn": "Anna", "stad": "Stockholm"}
    return None
```

### Type hints för klasser

```python
from typing import List

class Student:
    def __init__(self, namn: str, ålder: int) -> None:
        self.namn: str = namn
        self.ålder: int = ålder
        self.kurser: List[str] = []

    def lägg_till_kurs(self, kurs: str) -> None:
        self.kurser.append(kurs)

    def få_kurser(self) -> List[str]:
        return self.kurser
```

### Varför type hints? 🤔

✅ **Bättre dokumentation** - Lätt att se vad funktioner förväntar sig
✅ **IDE-stöd** - Bättre auto-complete
✅ **Färre buggar** - Verktyg kan hitta typ-fel
✅ **Lättare refaktorering**

⚠️ **OBS**: Type hints är *hints*, inte krav - Python kontrollerar dem inte automatiskt!

---

## 4.10 PEP 8 - Python Style Guide 📐

**PEP 8** är den officiella style guide för Python-kod.

### Viktiga PEP 8-regler

#### Namngivning
```python
# RÄTT ✅
class MinKlass:           # CapWords för klasser
    pass

def min_funktion():       # lowercase_with_underscores för funktioner
    pass

KONSTANT = 100            # UPPERCASE för konstanter
min_variabel = 10         # lowercase för variabler

# FEL ❌
class min_klass:          # Klasser ska vara CapWords
    pass

def MinFunktion():        # Funktioner ska vara lowercase
    pass
```

#### Indentering och mellanslag
```python
# RÄTT ✅ - 4 mellanslag för indentering
def exempel():
    if True:
        print("Rätt indentering!")

# Mellanslag runt operatorer
x = 1 + 2
lista = [1, 2, 3]

# FEL ❌
def exempel():
  print("Bara 2 mellanslag")  # Borde vara 4!

x=1+2  # Inget mellanslag!
```

#### Radlängd
```python
# Max 79 tecken per rad
# RÄTT ✅
lång_text = (
    "Detta är en mycket lång text som "
    "är uppdelad på flera rader"
)

# FEL ❌
# lång_text = "Detta är en mycket lång text som är över 79 tecken och därför bryter mot PEP 8-reglerna"
```

#### Imports
```python
# RÄTT ✅
import os
import sys
from typing import List, Dict

# FEL ❌
import os, sys  # En import per rad!
from typing import *  # Undvik wildcard-imports!
```

#### Docstrings
```python
# RÄTT ✅
def min_funktion(a: int, b: int) -> int:
    """
    Summerar två tal.

    Args:
        a: Första talet
        b: Andra talet

    Returns:
        Summan av a och b
    """
    return a + b
```

### Verktyg för att följa PEP 8 🛠️

```bash
# Installera formatters och linters
pip install black flake8 pylint

# Black - automatisk formatering
black min_fil.py

# Flake8 - hitta stil-problem
flake8 min_fil.py

# Pylint - omfattande kodanalys
pylint min_fil.py
```

---

## 🎯 Övningar för Nivå 4

### Övning 4.1: Enkel klass ⭐⭐
Skapa en klass `Bok` med attribut för titel, författare och antal sidor. Lägg till en metod för att visa information.

<details>
<summary>💡 Lösningsförslag</summary>

```python
class Bok:
    def __init__(self, titel: str, författare: str, sidor: int) -> None:
        self.titel = titel
        self.författare = författare
        self.sidor = sidor

    def info(self) -> None:
        print(f"'{self.titel}' av {self.författare} ({self.sidor} sidor)")

# Test
bok = Bok("Python 101", "Anna Andersson", 250)
bok.info()  # Output: 'Python 101' av Anna Andersson (250 sidor)
```
</details>

### Övning 4.2: Arv med fordon ⭐⭐
Skapa en basklass `Fordon` och subklasser `Bil` och `Cykel`. Implementera olika `starta()`-metoder.

<details>
<summary>💡 Lösningsförslag</summary>

```python
class Fordon:
    def __init__(self, märke: str) -> None:
        self.märke = märke

    def starta(self) -> None:
        print(f"{self.märke} startar...")

class Bil(Fordon):
    def __init__(self, märke: str, bränsle: str) -> None:
        super().__init__(märke)
        self.bränsle = bränsle

    def starta(self) -> None:
        print(f"🚗 {self.märke} startar motorn! (Bränsle: {self.bränsle})")

class Cykel(Fordon):
    def starta(self) -> None:
        print(f"🚴 Börjar trampa på {self.märke}!")

# Test
bil = Bil("Volvo", "Bensin")
cykel = Cykel("Crescent")

bil.starta()
cykel.starta()
```
</details>

### Övning 4.3: Magic methods ⭐⭐⭐
Skapa en klass `Punkt` som representerar en punkt i 2D. Implementera `__str__`, `__add__` (för att addera punkter) och `__eq__`.

<details>
<summary>💡 Lösningsförslag</summary>

```python
class Punkt:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: 'Punkt') -> 'Punkt':
        return Punkt(self.x + other.x, self.y + other.y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Punkt):
            return False
        return self.x == other.x and self.y == other.y

# Test
p1 = Punkt(1, 2)
p2 = Punkt(3, 4)
p3 = p1 + p2

print(p1)           # Output: (1, 2)
print(p3)           # Output: (4, 6)
print(p1 == p2)     # Output: False
print(p3 == Punkt(4, 6))  # Output: True
```
</details>

### Övning 4.4: Enkel decorator ⭐⭐⭐
Skapa en decorator `logga` som skriver ut när en funktion kallas och vad den returnerar.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def logga(func):
    def wrapper(*args, **kwargs):
        print(f"📞 Anropar {func.__name__}")
        resultat = func(*args, **kwargs)
        print(f"✅ {func.__name__} returnerade: {resultat}")
        return resultat
    return wrapper

@logga
def addera(a, b):
    return a + b

@logga
def hälsa(namn):
    return f"Hej {namn}!"

# Test
addera(3, 5)
hälsa("Anna")
```
</details>

### Övning 4.5: Generator för primtal ⭐⭐⭐
Skapa en generator som genererar primtal.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def primtal_generator():
    """Genererar primtal."""
    def är_primtal(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    n = 2
    while True:
        if är_primtal(n):
            yield n
        n += 1

# Test - första 10 primtalen
primtal = primtal_generator()
for i in range(10):
    print(next(primtal), end=" ")
# Output: 2 3 5 7 11 13 17 19 23 29
```
</details>

### Övning 4.6: Komplett spelarklass ⭐⭐⭐⭐
Skapa en `Spelare`-klass för ett RPG-spel med:
- Attribut: namn, hälsa, attack, försvar
- Metoder: attackera, ta_skada, är_vid_liv
- Magic method: `__str__`

<details>
<summary>💡 Lösningsförslag</summary>

```python
class Spelare:
    def __init__(self, namn: str) -> None:
        self.namn = namn
        self.hälsa = 100
        self.attack = 10
        self.försvar = 5

    def attackera(self, motståndare: 'Spelare') -> None:
        skada = max(0, self.attack - motståndare.försvar)
        motståndare.ta_skada(skada)
        print(f"⚔️ {self.namn} attackerar {motståndare.namn} för {skada} skada!")

    def ta_skada(self, skada: int) -> None:
        self.hälsa -= skada
        if self.hälsa < 0:
            self.hälsa = 0

    def är_vid_liv(self) -> bool:
        return self.hälsa > 0

    def __str__(self) -> str:
        return f"{self.namn} (HP: {self.hälsa})"

# Test
spelare1 = Spelare("Anna")
spelare2 = Spelare("Erik")

print(spelare1)
spelare1.attackera(spelare2)
print(spelare2)
print(f"Erik lever: {spelare2.är_vid_liv()}")
```
</details>

### Övning 4.7: Bibliotekssystem ⭐⭐⭐⭐
Skapa klasser `Bok` och `Bibliotek`. Biblioteket kan:
- Lägga till böcker
- Låna ut böcker
- Returnera böcker
- Visa tillgängliga böcker

<details>
<summary>💡 Lösningsförslag</summary>

```python
from typing import List, Optional

class Bok:
    def __init__(self, titel: str, författare: str) -> None:
        self.titel = titel
        self.författare = författare
        self.utlånad = False

    def __str__(self) -> str:
        status = "Utlånad" if self.utlånad else "Tillgänglig"
        return f"'{self.titel}' av {self.författare} [{status}]"

class Bibliotek:
    def __init__(self) -> None:
        self.böcker: List[Bok] = []

    def lägg_till_bok(self, bok: Bok) -> None:
        self.böcker.append(bok)
        print(f"✅ Lade till: {bok.titel}")

    def låna_bok(self, titel: str) -> Optional[Bok]:
        for bok in self.böcker:
            if bok.titel.lower() == titel.lower() and not bok.utlånad:
                bok.utlånad = True
                print(f"📚 Lånade ut: {bok.titel}")
                return bok
        print(f"❌ Boken '{titel}' är inte tillgänglig")
        return None

    def returnera_bok(self, titel: str) -> None:
        for bok in self.böcker:
            if bok.titel.lower() == titel.lower() and bok.utlånad:
                bok.utlånad = False
                print(f"✅ Returnerade: {bok.titel}")
                return
        print(f"❌ Boken '{titel}' är inte utlånad")

    def visa_böcker(self) -> None:
        print("\n=== BÖCKER I BIBLIOTEKET ===")
        for bok in self.böcker:
            print(bok)

# Test
bib = Bibliotek()
bib.lägg_till_bok(Bok("Python 101", "Anna"))
bib.lägg_till_bok(Bok("Java Basics", "Erik"))
bib.visa_böcker()
bib.låna_bok("Python 101")
bib.visa_böcker()
bib.returnera_bok("Python 101")
bib.visa_böcker()
```
</details>

### Övning 4.8: Type hints refaktorering ⭐⭐
Ta en tidigare funktion utan type hints och lägg till korrekta type hints.

<details>
<summary>💡 Lösningsförslag</summary>

```python
from typing import List, Dict

# Innan
def processera_data(data, filter_värde):
    resultat = []
    for item in data:
        if item > filter_värde:
            resultat.append(item * 2)
    return resultat

# Efter med type hints
def processera_data(data: List[int], filter_värde: int) -> List[int]:
    """
    Processerar data och returnerar filtrerade och dubblerade värden.

    Args:
        data: Lista med heltal att processera
        filter_värde: Värde att filtrera mot

    Returns:
        Lista med dubblerade värden som är större än filter_värde
    """
    resultat: List[int] = []
    for item in data:
        if item > filter_värde:
            resultat.append(item * 2)
    return resultat
```
</details>

---

## 🎓 Sammanfattning av Nivå 4

**Fantastiskt!** 🎉 Du behärskar nu avancerade Python-koncept:

✅ **OOP**: Klasser, objekt, arv, polymorfism
✅ **Magic methods**: `__init__`, `__str__`, `__add__`, etc.
✅ **Decorators**: Utöka funktionalitet elegant
✅ **Generators**: Minneseffektiva iteratorer
✅ **Context managers**: Säker resurshantering
✅ **Type hints**: Tydligare och säkrare kod
✅ **PEP 8**: Professionell kodstil

### Nästa steg 🚀

Nu är du redo för **Nivå 5**, där du lär dig:
- Async/await programmering
- Data science med pandas och numpy
- Webbutveckling med FastAPI
- Testing med pytest
- Virtual environments
- Verkliga case studies

---

**Fortsätt till:** [Nivå 5: Cutting-edge →](Python_Guide_05_Niva5.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
