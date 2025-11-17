# 🐍 Nivå 3: Mellanliggande koncept och verktyg

## 🎯 Lärandemål för Nivå 3

Efter detta kapitel kommer du att kunna:
- ✅ Skriva mer avancerade funktioner med scope och lambdas
- ✅ Importera och använda moduler
- ✅ Läsa från och skriva till filer
- ✅ Hantera fel med try/except
- ✅ Arbeta med dictionary och tuple
- ✅ Använda list comprehensions
- ✅ Sätta upp en professionell utvecklingsmiljö
- ✅ Debugga program effektivt

---

## 3.1 Fördjupning i funktioner 🔍

### Scope - Variablers räckvidd

**Scope** betyder "var en variabel kan användas". Det finns två typer:

```python
# Global variabel - kan användas överallt
globalt_namn = "Anna"

def min_funktion():
    # Lokal variabel - bara inom funktionen
    lokalt_namn = "Erik"
    print(f"Inne i funktionen: {globalt_namn}")  # Funkar!
    print(f"Lokalt namn: {lokalt_namn}")          # Funkar!

min_funktion()
print(f"Utanför funktionen: {globalt_namn}")  # Funkar!
# print(lokalt_namn)  # FEL! Variabeln finns inte här
```

### Visualisering av scope:

```
┌─────────────────────────────────────┐
│ GLOBALT SCOPE                       │
│                                     │
│ globalt_namn = "Anna"               │
│                                     │
│  ┌──────────────────────────────┐  │
│  │ LOKALT SCOPE (i funktionen)  │  │
│  │                              │  │
│  │ lokalt_namn = "Erik"         │  │
│  │ (kan använda globala vars)   │  │
│  └──────────────────────────────┘  │
│                                     │
└─────────────────────────────────────┘
```

### Ändra globala variabler från funktion

```python
räknare = 0

def öka_räknare():
    global räknare  # Säg åt Python att använda den globala variabeln
    räknare += 1

öka_räknare()
print(räknare)  # Output: 1

öka_räknare()
print(räknare)  # Output: 2
```

⚠️ **Varning**: Använd `global` sparsamt! Det är bättre att returnera värden från funktioner.

### *args och **kwargs - Flexibla parametrar

```python
# *args - okänt antal positionsparametrar
def summa(*tal):
    """Summera hur många tal som helst."""
    total = 0
    for nummer in tal:
        total += nummer
    return total

print(summa(1, 2, 3))        # Output: 6
print(summa(5, 10, 15, 20))  # Output: 50

# **kwargs - okänt antal namngivna parametrar
def skriv_info(**info):
    """Skriv ut information."""
    for nyckel, värde in info.items():
        print(f"{nyckel}: {värde}")

skriv_info(namn="Lisa", ålder=25, stad="Stockholm")
# Output:
# namn: Lisa
# ålder: 25
# stad: Stockholm
```

### Lambda-funktioner - Anonyma funktioner

Lambda är små, enkla funktioner som skrivs på en rad:

```python
# Vanlig funktion
def dubbla(x):
    return x * 2

# Samma sak med lambda
dubbla_lambda = lambda x: x * 2

print(dubbla(5))         # Output: 10
print(dubbla_lambda(5))  # Output: 10

# Lambda med flera parametrar
addera = lambda a, b: a + b
print(addera(3, 7))  # Output: 10

# Lambda är användbart med map(), filter(), sorted()
tal = [1, 2, 3, 4, 5]
dubblat = list(map(lambda x: x * 2, tal))
print(dubblat)  # Output: [2, 4, 6, 8, 10]

# Filtrera jämna tal
jämna = list(filter(lambda x: x % 2 == 0, tal))
print(jämna)  # Output: [2, 4]
```

---

## 3.2 Moduler och import 📦

**Moduler** är Python-filer som innehåller funktioner och kod du kan återanvända.

### Importera inbyggda moduler

```python
# Importera hela modulen
import math

print(math.pi)           # Output: 3.141592653589793
print(math.sqrt(16))     # Output: 4.0
print(math.floor(4.7))   # Output: 4

# Importera specifika funktioner
from math import pi, sqrt

print(pi)       # Output: 3.141592653589793
print(sqrt(25)) # Output: 5.0

# Importera med alias (kortare namn)
import math as m

print(m.pi)  # Output: 3.141592653589793
```

### Användbara inbyggda moduler 🛠️

#### random - Slumptal och slumpmässighet

```python
import random

# Slumptal mellan 1 och 10
tal = random.randint(1, 10)
print(tal)

# Slumpmässigt float mellan 0 och 1
decimaltal = random.random()
print(decimaltal)

# Välj slumpmässigt från en lista
frukter = ["äpple", "banan", "päron"]
vald_frukt = random.choice(frukter)
print(vald_frukt)

# Blanda en lista
kort = ["Ess", "Kung", "Dam", "Knekt"]
random.shuffle(kort)
print(kort)
```

#### datetime - Arbeta med datum och tid

```python
from datetime import datetime, timedelta

# Nuvarande datum och tid
nu = datetime.now()
print(f"Nu är klockan: {nu}")

# Formatera datum
print(nu.strftime("%Y-%m-%d"))      # Output: 2024-11-17
print(nu.strftime("%H:%M:%S"))      # Output: 14:30:45

# Räkna med datum
om_en_vecka = nu + timedelta(days=7)
print(f"Om en vecka: {om_en_vecka}")

# Få komponenter
print(f"År: {nu.year}")
print(f"Månad: {nu.month}")
print(f"Dag: {nu.day}")
```

#### os - Operativsystem-interaktion

```python
import os

# Nuvarande arbetskatalog
print(os.getcwd())

# Lista filer i katalog
filer = os.listdir(".")
print(filer)

# Kolla om fil/katalog finns
if os.path.exists("min_fil.txt"):
    print("Filen finns!")
```

### Skapa egna moduler

**Fil: matte_verktyg.py**
```python
"""Egna matematiska verktyg."""

def kvadrat(tal):
    """Returnera talet i kvadrat."""
    return tal ** 2

def kub(tal):
    """Returnera talet i kubik."""
    return tal ** 3

PI = 3.14159
```

**Fil: main.py**
```python
# Importera din egen modul
import matte_verktyg

print(matte_verktyg.kvadrat(5))  # Output: 25
print(matte_verktyg.kub(3))      # Output: 27
print(matte_verktyg.PI)          # Output: 3.14159

# Eller importera specifika delar
from matte_verktyg import kvadrat, PI

print(kvadrat(4))  # Output: 16
print(PI)          # Output: 3.14159
```

---

## 3.3 Filhantering - Läsa och skriva filer 📄

### Skriva till en fil

```python
# Skriva text till fil (skriver över om filen finns)
with open("min_fil.txt", "w", encoding="utf-8") as fil:
    fil.write("Hej från Python!\n")
    fil.write("Detta är rad 2.\n")
    fil.write("Och detta är rad 3.\n")

print("Filen skapad!")
```

💡 **Tips**: `with open()` stänger automatiskt filen när vi är klara!

### Läsa från en fil

```python
# Läsa hela filen
with open("min_fil.txt", "r", encoding="utf-8") as fil:
    innehåll = fil.read()
    print(innehåll)

# Läsa rad för rad
with open("min_fil.txt", "r", encoding="utf-8") as fil:
    for rad in fil:
        print(rad.strip())  # strip() tar bort whitespace
```

### Lägga till i en fil (append)

```python
# Lägg till i slutet utan att skriva över
with open("min_fil.txt", "a", encoding="utf-8") as fil:
    fil.write("Denna rad läggs till i slutet.\n")
```

### Fil-modes tabell 📊

```
┌──────┬──────────────────────────────────────┐
│ Mode │ Beskrivning                          │
├──────┼──────────────────────────────────────┤
│ "r"  │ Read - läsa (filen måste finnas)    │
│ "w"  │ Write - skriva (skapar/skriver över) │
│ "a"  │ Append - lägg till i slutet          │
│ "r+" │ Läs och skriv                        │
│ "b"  │ Binary mode (t.ex. "rb", "wb")       │
└──────┴──────────────────────────────────────┘
```

### Praktiskt exempel: Enkel anteckningsbok

```python
def anteckningsbok():
    """Enkel app för att spara anteckningar."""

    filnamn = "anteckningar.txt"

    while True:
        print("\n=== ANTECKNINGSBOK ===")
        print("1. Läs anteckningar")
        print("2. Skriv ny anteckning")
        print("3. Avsluta")

        val = input("\nDitt val: ")

        if val == "1":
            # Läs anteckningar
            try:
                with open(filnamn, "r", encoding="utf-8") as fil:
                    innehåll = fil.read()
                    if innehåll:
                        print("\n--- ANTECKNINGAR ---")
                        print(innehåll)
                    else:
                        print("Inga anteckningar än.")
            except FileNotFoundError:
                print("Inga anteckningar än.")

        elif val == "2":
            # Skriv ny anteckning
            anteckning = input("Din anteckning: ")
            with open(filnamn, "a", encoding="utf-8") as fil:
                from datetime import datetime
                tidsstämpel = datetime.now().strftime("%Y-%m-%d %H:%M")
                fil.write(f"[{tidsstämpel}] {anteckning}\n")
            print("Anteckning sparad!")

        elif val == "3":
            print("Hej då!")
            break

# anteckningsbok()  # Avkommentera för att köra
```

---

## 3.4 Error handling - Hantera fel 🛡️

Fel händer! Men vi kan fånga dem och hantera dem snyggt med **try/except**.

### Grundläggande try/except

```python
# Utan error handling
# tal = int("abc")  # ValueError: invalid literal for int()

# Med error handling
try:
    tal = int("abc")
    print(f"Talet är: {tal}")
except ValueError:
    print("Fel! Det där var inte ett tal.")

print("Programmet fortsätter...")  # Detta körs!
```

### Flera exception-typer

```python
def dela(a, b):
    try:
        resultat = a / b
        print(f"{a} / {b} = {resultat}")
    except ZeroDivisionError:
        print("Fel! Kan inte dela med 0.")
    except TypeError:
        print("Fel! Båda värdena måste vara nummer.")

dela(10, 2)    # Output: 10 / 2 = 5.0
dela(10, 0)    # Output: Fel! Kan inte dela med 0.
dela(10, "x")  # Output: Fel! Båda värdena måste vara nummer.
```

### try/except/else/finally

```python
def läs_fil(filnamn):
    try:
        with open(filnamn, "r") as fil:
            innehåll = fil.read()
    except FileNotFoundError:
        print(f"Filen {filnamn} finns inte.")
    else:
        # Körs om inget fel uppstod
        print(f"Filen lästes framgångsrikt!")
        print(innehåll)
    finally:
        # Körs alltid, oavsett om fel uppstod eller inte
        print("Läsoperation avslutad.")

läs_fil("existerar_inte.txt")
```

### Vanliga exception-typer 📋

```
┌────────────────────┬─────────────────────────────┐
│ Exception          │ När den uppstår             │
├────────────────────┼─────────────────────────────┤
│ ValueError         │ Fel värdetyp                │
│ TypeError          │ Fel datatyp                 │
│ ZeroDivisionError  │ Division med 0              │
│ FileNotFoundError  │ Fil finns inte              │
│ IndexError         │ Index utanför lista         │
│ KeyError           │ Nyckel finns inte i dict    │
│ AttributeError     │ Attribut finns inte         │
└────────────────────┴─────────────────────────────┘
```

### Praktiskt exempel: Säker input

```python
def få_heltal(prompt):
    """Fråga efter heltal tills användaren ger ett giltigt."""
    while True:
        try:
            värde = int(input(prompt))
            return värde
        except ValueError:
            print("❌ Ogiltigt! Ange ett heltal.")

# Användning
ålder = få_heltal("Ange din ålder: ")
print(f"Du är {ålder} år gammal.")
```

---

## 3.5 Dictionary - Nyckel-värde-par 🗂️

**Dictionary** (ordbok) lagrar data som par av nycklar och värden.

### Skapa och använda dictionary

```python
# Skapa en dictionary
person = {
    "namn": "Anna",
    "ålder": 25,
    "stad": "Stockholm",
    "yrke": "Programmerare"
}

# Hämta värden
print(person["namn"])   # Output: Anna
print(person["ålder"])  # Output: 25

# Säkrare: använd .get()
print(person.get("namn"))     # Output: Anna
print(person.get("email"))    # Output: None (inget fel!)
print(person.get("email", "Ingen email"))  # Output: Ingen email

# Ändra värde
person["ålder"] = 26
print(person["ålder"])  # Output: 26

# Lägg till ny nyckel
person["email"] = "anna@example.com"
print(person)
```

### Dictionary-metoder

```python
person = {"namn": "Lisa", "ålder": 30, "stad": "Göteborg"}

# Få alla nycklar
print(person.keys())    # Output: dict_keys(['namn', 'ålder', 'stad'])

# Få alla värden
print(person.values())  # Output: dict_values(['Lisa', 30, 'Göteborg'])

# Få alla par
print(person.items())   # Output: dict_items([('namn', 'Lisa'), ...])

# Loopa genom dictionary
for nyckel, värde in person.items():
    print(f"{nyckel}: {värde}")

# Kolla om nyckel finns
if "namn" in person:
    print("Namnet finns i dictionaryn!")
```

### Praktiskt exempel: Telefonbok

```python
def telefonbok():
    """Enkel telefonbok."""

    kontakter = {}

    while True:
        print("\n=== TELEFONBOK ===")
        print("1. Lägg till kontakt")
        print("2. Sök kontakt")
        print("3. Visa alla")
        print("4. Avsluta")

        val = input("\nDitt val: ")

        if val == "1":
            namn = input("Namn: ")
            nummer = input("Telefonnummer: ")
            kontakter[namn] = nummer
            print(f"✅ {namn} tillagd!")

        elif val == "2":
            namn = input("Sök efter namn: ")
            if namn in kontakter:
                print(f"📞 {namn}: {kontakter[namn]}")
            else:
                print("❌ Kontakt finns inte.")

        elif val == "3":
            if kontakter:
                print("\n--- ALLA KONTAKTER ---")
                for namn, nummer in kontakter.items():
                    print(f"{namn}: {nummer}")
            else:
                print("Inga kontakter ännu.")

        elif val == "4":
            break

# telefonbok()  # Avkommentera för att köra
```

---

## 3.6 Tuple - Oföränderliga listor 🔒

**Tuple** är som listor, men de kan inte ändras efter de skapats.

### Skapa och använda tuples

```python
# Skapa tuple med parenteser
koordinater = (10, 20)
färger = ("röd", "grön", "blå")

# Hämta värden (som listor)
print(koordinater[0])  # Output: 10
print(färger[1])       # Output: grön

# Tuple kan inte ändras!
# färger[0] = "gul"  # TypeError: 'tuple' object does not support item assignment

# Unpacking - dela upp tuple
x, y = koordinater
print(f"x={x}, y={y}")  # Output: x=10, y=20

# Returnera flera värden från funktion
def min_max(lista):
    return min(lista), max(lista)

minimum, maximum = min_max([3, 7, 1, 9, 4])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 9
```

### Lista vs Tuple 📊

```
┌────────────────┬──────────┬───────────┐
│ Egenskap       │ Lista    │ Tuple     │
├────────────────┼──────────┼───────────┤
│ Syntax         │ []       │ ()        │
│ Kan ändras     │ Ja       │ Nej       │
│ Snabbare       │ Nej      │ Ja        │
│ Användning     │ Dynamisk │ Fast data │
└────────────────┴──────────┴───────────┘
```

---

## 3.7 List comprehensions - Kompakt list-skapande ✨

**List comprehensions** är ett elegant sätt att skapa listor på en rad!

### Grundläggande list comprehension

```python
# Traditionellt sätt
kvadrater = []
for i in range(1, 6):
    kvadrater.append(i ** 2)
print(kvadrater)  # Output: [1, 4, 9, 16, 25]

# Med list comprehension - mycket kortare!
kvadrater = [i ** 2 for i in range(1, 6)]
print(kvadrater)  # Output: [1, 4, 9, 16, 25]
```

### List comprehension med villkor

```python
# Alla jämna tal från 1 till 20
jämna = [i for i in range(1, 21) if i % 2 == 0]
print(jämna)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Kvadrat av alla udda tal
udda_kvadrater = [i ** 2 for i in range(1, 11) if i % 2 != 0]
print(udda_kvadrater)  # Output: [1, 9, 25, 49, 81]

# Versaler för ord som börjar med 'A'
ord = ["anna", "erik", "amanda", "oskar"]
a_ord = [namn.upper() for namn in ord if namn.startswith("a")]
print(a_ord)  # Output: ['ANNA', 'AMANDA']
```

### Mer avancerade exempel

```python
# Nested list comprehension - multiplikationstabell
tabell = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for rad in tabell:
    print(rad)

# Dictionary comprehension!
tal = [1, 2, 3, 4, 5]
kvadrat_dict = {tal: tal ** 2 for tal in tal}
print(kvadrat_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Set comprehension!
jämna_set = {i for i in range(20) if i % 2 == 0}
print(jämna_set)  # Output: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
```

---

## 3.8 Utvecklingsmiljö - VS Code 💻

### Varför VS Code?

- ✅ Gratis och open source
- ✅ Python-extension med IntelliSense
- ✅ Inbyggd debugger
- ✅ Git-integration
- ✅ Stort community och många extensions

### Installera Python-extension

1. Öppna VS Code
2. Gå till Extensions (Ctrl+Shift+X)
3. Sök efter "Python" (från Microsoft)
4. Klicka Install

### Användbara kortkommandon ⌨️

```
┌───────────────────────┬─────────────────────┐
│ Funktion              │ Kortkommando        │
├───────────────────────┼─────────────────────┤
│ Kör Python-fil        │ Ctrl+Alt+N eller F5 │
│ Kommentera kod        │ Ctrl+/              │
│ Formatera kod         │ Shift+Alt+F         │
│ Öppna terminal        │ Ctrl+`              │
│ Sök i filer           │ Ctrl+Shift+F        │
│ Auto-complete         │ Ctrl+Space          │
└───────────────────────┴─────────────────────┘
```

### Debugging i VS Code 🐛

```python
# Exempel-kod att debugga
def räkna_summa(lista):
    summa = 0
    for tal in lista:
        summa += tal
    return summa

tal = [1, 2, 3, 4, 5]
resultat = räkna_summa(tal)
print(f"Summa: {resultat}")
```

**Steg för debugging:**
1. Sätt en **breakpoint** (klicka till vänster om radnumret)
2. Tryck F5 eller välj "Run and Debug"
3. Programmet pausar vid breakpoint
4. Använd debug-kontroller:
   - **Continue** (F5): Fortsätt till nästa breakpoint
   - **Step Over** (F10): Kör nästa rad
   - **Step Into** (F11): Gå in i funktion
   - **Step Out** (Shift+F11): Gå ut från funktion
5. Inspektera variabler i "Variables"-panelen

---

## 🎯 Övningar för Nivå 3

### Övning 3.1: Lambda-sortering ⭐⭐
Använd lambda med `sorted()` för att sortera en lista av tuples efter andra elementet.

```python
personer = [("Anna", 25), ("Erik", 30), ("Lisa", 22)]
# Sortera efter ålder
```

<details>
<summary>💡 Lösningsförslag</summary>

```python
personer = [("Anna", 25), ("Erik", 30), ("Lisa", 22)]
sorterat = sorted(personer, key=lambda person: person[1])
print(sorterat)  # Output: [('Lisa', 22), ('Anna', 25), ('Erik', 30)]
```
</details>

### Övning 3.2: Modul för omvandlingar ⭐⭐
Skapa en modul `omvandlingar.py` med funktioner för temperatur-omvandling (Celsius till Fahrenheit och vice versa).

<details>
<summary>💡 Lösningsförslag</summary>

```python
# omvandlingar.py
def celsius_till_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_till_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# test.py
from omvandlingar import celsius_till_fahrenheit, fahrenheit_till_celsius

print(celsius_till_fahrenheit(0))    # 32.0
print(fahrenheit_till_celsius(100))  # 37.77...
```
</details>

### Övning 3.3: Filräknare ⭐⭐
Skriv ett program som läser en textfil och räknar:
- Antal rader
- Antal ord
- Antal tecken

<details>
<summary>💡 Lösningsförslag</summary>

```python
def analysera_fil(filnamn):
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            innehåll = fil.read()
            rader = innehåll.split("\n")
            ord = innehåll.split()

            print(f"Antal rader: {len(rader)}")
            print(f"Antal ord: {len(ord)}")
            print(f"Antal tecken: {len(innehåll)}")

    except FileNotFoundError:
        print(f"Filen {filnamn} finns inte.")

analysera_fil("test.txt")
```
</details>

### Övning 3.4: Säker division ⭐⭐
Skapa en funktion som frågar efter två tal och delar dem. Hantera fel (division med 0, ogiltiga tal).

<details>
<summary>💡 Lösningsförslag</summary>

```python
def säker_division():
    try:
        tal1 = float(input("Ange första talet: "))
        tal2 = float(input("Ange andra talet: "))
        resultat = tal1 / tal2
        print(f"{tal1} / {tal2} = {resultat}")
    except ValueError:
        print("Fel! Ogiltigt tal.")
    except ZeroDivisionError:
        print("Fel! Kan inte dela med 0.")

säker_division()
```
</details>

### Övning 3.5: Ordräknare med dictionary ⭐⭐⭐
Skriv ett program som räknar hur många gånger varje ord förekommer i en text.

<details>
<summary>💡 Lösningsförslag</summary>

```python
text = "python är kul och python är kraftfullt python är bäst"

ord_lista = text.lower().split()
ord_räkning = {}

for ord in ord_lista:
    if ord in ord_räkning:
        ord_räkning[ord] += 1
    else:
        ord_räkning[ord] = 1

# Eller med .get()
ord_räkning2 = {}
for ord in ord_lista:
    ord_räkning2[ord] = ord_räkning2.get(ord, 0) + 1

print(ord_räkning)
# Output: {'python': 3, 'är': 3, 'kul': 1, 'och': 1, 'kraftfullt': 1, 'bäst': 1}
```
</details>

### Övning 3.6: Tuple unpacking ⭐⭐
Skapa en funktion som returnerar min, max och medelvärde av en lista med tuple unpacking.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def statistik(lista):
    minimum = min(lista)
    maximum = max(lista)
    medel = sum(lista) / len(lista)
    return minimum, maximum, medel

tal = [5, 2, 9, 1, 7, 4]
min_val, max_val, medel_val = statistik(tal)

print(f"Min: {min_val}, Max: {max_val}, Medel: {medel_val:.2f}")
# Output: Min: 1, Max: 9, Medel: 4.67
```
</details>

### Övning 3.7: List comprehension - filter ⭐⭐⭐
Använd list comprehension för att skapa en lista med alla ord från en lista som är längre än 5 bokstäver.

<details>
<summary>💡 Lösningsförslag</summary>

```python
ord = ["hej", "python", "programmering", "kul", "fantastisk", "kod"]
långa_ord = [ord for ord in ord if len(ord) > 5]
print(långa_ord)  # Output: ['python', 'programmering', 'fantastisk']
```
</details>

### Övning 3.8: JSON-hantering ⭐⭐⭐
Spara en dictionary till JSON-fil och läs tillbaka den.

<details>
<summary>💡 Lösningsförslag</summary>

```python
import json

# Data att spara
data = {
    "namn": "Anna",
    "ålder": 25,
    "hobbies": ["läsa", "programmera", "löpning"]
}

# Spara till fil
with open("data.json", "w", encoding="utf-8") as fil:
    json.dump(data, fil, ensure_ascii=False, indent=2)

# Läsa från fil
with open("data.json", "r", encoding="utf-8") as fil:
    laddad_data = json.load(fil)

print(laddad_data)
print(f"Namn: {laddad_data['namn']}")
```
</details>

### Övning 3.9: CSV-läsare ⭐⭐⭐
Läs en CSV-fil (komma-separerade värden) och skriv ut data i snygg tabellformat.

<details>
<summary>💡 Lösningsförslag</summary>

```python
import csv

# Skapa test-fil först
with open("personer.csv", "w", encoding="utf-8", newline="") as fil:
    skrivare = csv.writer(fil)
    skrivare.writerow(["Namn", "Ålder", "Stad"])
    skrivare.writerow(["Anna", "25", "Stockholm"])
    skrivare.writerow(["Erik", "30", "Göteborg"])
    skrivare.writerow(["Lisa", "22", "Malmö"])

# Läs CSV-filen
with open("personer.csv", "r", encoding="utf-8") as fil:
    läsare = csv.reader(fil)
    for rad in läsare:
        print(f"{rad[0]:10} {rad[1]:5} {rad[2]:15}")
```
</details>

### Övning 3.10: Mini-databas ⭐⭐⭐
Skapa ett program som sparar student-information (namn, ålder, betyg) till fil och kan läsa tillbaka den.

<details>
<summary>💡 Lösningsförslag</summary>

```python
import json

def spara_studenter(studenter, filnamn="studenter.json"):
    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(studenter, fil, ensure_ascii=False, indent=2)

def ladda_studenter(filnamn="studenter.json"):
    try:
        with open(filnamn, "r", encoding="utf-8") as fil:
            return json.load(fil)
    except FileNotFoundError:
        return []

def main():
    studenter = ladda_studenter()

    while True:
        print("\n=== STUDENT-DATABAS ===")
        print("1. Lägg till student")
        print("2. Visa alla studenter")
        print("3. Avsluta")

        val = input("\nVal: ")

        if val == "1":
            namn = input("Namn: ")
            ålder = int(input("Ålder: "))
            betyg = input("Betyg: ")
            studenter.append({"namn": namn, "ålder": ålder, "betyg": betyg})
            spara_studenter(studenter)
            print("✅ Student tillagd!")

        elif val == "2":
            for student in studenter:
                print(f"{student['namn']} ({student['ålder']} år) - Betyg: {student['betyg']}")

        elif val == "3":
            break

# main()
```
</details>

---

## 🎓 Sammanfattning av Nivå 3

**Utmärkt!** 🎉 Du har nu lärt dig mellanliggande koncept:

✅ **Funktioner**: Scope, *args/**kwargs, lambda
✅ **Moduler**: Importera och skapa egna moduler
✅ **Filhantering**: Läsa, skriva, append
✅ **Error handling**: try/except/else/finally
✅ **Dictionary**: Nyckel-värde-par, användbara metoder
✅ **Tuple**: Oföränderliga listor
✅ **List comprehensions**: Elegant list-skapande
✅ **VS Code**: Professionell utvecklingsmiljö

### Nästa steg 🚀

Nu är du redo för **Nivå 4**, där du lär dig:
- Objektorienterad programmering (OOP)
- Klasser och arv
- Decorators och generators
- Type hints
- PEP 8 och best practices
- Bygga en TODO-app med GUI

---

**Fortsätt till:** [Nivå 4: Avancerade koncept →](Python_Guide_04_Niva4.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
