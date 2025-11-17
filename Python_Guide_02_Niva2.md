# 🐍 Nivå 2: Introduktion till programmering

## 🎯 Lärandemål för Nivå 2

Efter detta kapitel kommer du att kunna:
- ✅ Arbeta med listor och strängar
- ✅ Använda if-statements för att fatta beslut
- ✅ Skapa loopar med for och while
- ✅ Definiera och använda egna funktioner
- ✅ Bygga kompletta små program
- ✅ Skapa dina första projekt: Gissningslek och kalkylator

---

## 2.1 Listor - Samla många saker 📋

En **lista** är som en låda där du kan ha många saker istället för bara en. Tänk på en inköpslista eller en lista med dina vänner.

### Skapa och använda listor

```python
# Skapa en lista med frukt
frukter = ["äpple", "banan", "päron", "apelsin"]

# Visa hela listan
print(frukter)  # Output: ['äpple', 'banan', 'päron', 'apelsin']

# Visa första frukten (index börjar på 0!)
print(frukter[0])  # Output: äpple

# Visa andra frukten
print(frukter[1])  # Output: banan

# Visa sista frukten
print(frukter[-1])  # Output: apelsin
```

### Viktig regel: Index börjar på 0! 🔢

```
Lista:  ["äpple", "banan", "päron", "apelsin"]
Index:     0        1        2         3
```

### Ändra och lägga till i listor

```python
frukter = ["äpple", "banan"]

# Lägg till en frukt i slutet
frukter.append("mango")
print(frukter)  # Output: ['äpple', 'banan', 'mango']

# Ändra ett element
frukter[0] = "jordgubbe"
print(frukter)  # Output: ['jordgubbe', 'banan', 'mango']

# Ta bort en frukt
frukter.remove("banan")
print(frukter)  # Output: ['jordgubbe', 'mango']

# Hur många frukter finns det?
antal = len(frukter)
print(f"Jag har {antal} frukter")  # Output: Jag har 2 frukter
```

### Användbara list-metoder 🛠️

```python
min_lista = [3, 1, 4, 1, 5]

# Sortera listan
min_lista.sort()
print(min_lista)  # Output: [1, 1, 3, 4, 5]

# Vänd på ordningen
min_lista.reverse()
print(min_lista)  # Output: [5, 4, 3, 1, 1]

# Räkna hur många gånger ett värde finns
antal_ettor = min_lista.count(1)
print(f"Antal 1:or: {antal_ettor}")  # Output: Antal 1:or: 2
```

---

## 2.2 Strängar - Arbeta med text 📝

Strängar (text) är också som listor - de är gjorda av många tecken!

### String-operationer

```python
namn = "Anna"

# Få längden på en sträng
print(len(namn))  # Output: 4

# Få ett specifikt tecken (börjar på 0)
print(namn[0])  # Output: A
print(namn[1])  # Output: n

# Stora bokstäver
print(namn.upper())  # Output: ANNA

# Små bokstäver
print(namn.lower())  # Output: anna

# Första bokstaven stor
print("hej världen".capitalize())  # Output: Hej världen

# Alla ord börjar med stor bokstav
print("hej världen".title())  # Output: Hej Världen
```

### Sätta ihop strängar

```python
förnamn = "Lisa"
efternamn = "Andersson"

# Sätt ihop med +
hela_namnet = förnamn + " " + efternamn
print(hela_namnet)  # Output: Lisa Andersson

# Eller använd f-string (bättre!)
print(f"{förnamn} {efternamn}")  # Output: Lisa Andersson

# Upprepa strängar
print("Ha" * 3)  # Output: HaHaHa
```

### Kolla om något finns i en sträng

```python
mening = "Python är kul att lära sig"

# Kolla om ett ord finns
if "kul" in mening:
    print("Ja, det är kul!")  # Detta körs!

# Dela upp sträng till lista
ord = mening.split()  # Delar på mellanslag
print(ord)  # Output: ['Python', 'är', 'kul', 'att', 'lära', 'sig']
```

---

## 2.3 If-statements - Få programmet att välja 🤔

**If-statements** låter ditt program göra olika saker beroende på villkor. Det är som att säga: "OM det regnar, ta ett paraply".

### Grundläggande if

```python
ålder = 15

if ålder >= 13:
    print("Du är en tonåring!")
    print("Välkommen till tonårsklubben!")

# Output: Du är en tonåring!
#         Välkommen till tonårsklubben!
```

⚠️ **Viktigt**: Notera **indenteringen** (mellanslaget framför print). Python använder indentering för att veta vad som hör till if-satsen!

### if-else: Antingen eller

```python
ålder = int(input("Hur gammal är du? "))

if ålder >= 18:
    print("Du är vuxen!")
else:
    print("Du är barn/tonåring!")
```

### if-elif-else: Flera alternativ

```python
poäng = int(input("Hur många poäng fick du? "))

if poäng >= 90:
    print("Betyg: A - Utmärkt!")
elif poäng >= 80:
    print("Betyg: B - Mycket bra!")
elif poäng >= 70:
    print("Betyg: C - Bra!")
elif poäng >= 60:
    print("Betyg: D - Godkänt!")
else:
    print("Betyg: F - Underkänd")
```

### Jämförelseoperatorer 📊

```
┌────────────────┬──────────┬─────────────────┐
│ Operator       │ Symbol   │ Exempel         │
├────────────────┼──────────┼─────────────────┤
│ Lika med       │ ==       │ x == 5          │
│ Inte lika med  │ !=       │ x != 5          │
│ Större än      │ >        │ x > 5           │
│ Mindre än      │ <        │ x < 5           │
│ Större/lika    │ >=       │ x >= 5          │
│ Mindre/lika    │ <=       │ x <= 5          │
└────────────────┴──────────┴─────────────────┘
```

### Logiska operatorer: and, or, not

```python
ålder = 15
har_körkort = False

# AND - båda måste vara sanna
if ålder >= 18 and har_körkort:
    print("Du får köra bil!")
else:
    print("Du får inte köra bil ännu")

# OR - minst en måste vara sann
dag = "lördag"
if dag == "lördag" or dag == "söndag":
    print("Det är helg! 🎉")

# NOT - vänd på ett villkor
är_vardag = False
if not är_vardag:
    print("Det är inte en vardag!")
```

### ASCII-diagram för if-else flöde

```
Programstart
     |
     v
┌─────────┐
│ if test │
└────┬────┘
     |
     ├──── Sant ────> [Gör detta]
     |                     |
     └──── Falskt ──> [Gör detta istället]
                           |
                           v
                    Fortsätt program
```

---

## 2.4 Loopar - Upprepa saker 🔄

Loopar låter dig upprepa kod flera gånger utan att skriva samma sak om och om igen.

### for-loop: Gå igenom en lista

```python
# Skriva ut alla frukter
frukter = ["äpple", "banan", "päron"]

for frukt in frukter:
    print(f"Jag gillar {frukt}")

# Output:
# Jag gillar äpple
# Jag gillar banan
# Jag gillar päron
```

### for-loop med range()

```python
# Räkna från 0 till 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Räkna från 1 till 10
for i in range(1, 11):
    print(i)
# Output: 1, 2, 3, ..., 10

# Räkna i steg om 2
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

### Praktiskt exempel: Multiplikationstabell

```python
nummer = int(input("Vilken multiplikationstabell vill du se? "))

for i in range(1, 11):
    resultat = nummer * i
    print(f"{nummer} × {i} = {resultat}")

# Om användaren skriver 5:
# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 10 = 50
```

### while-loop: Upprepa medan villkor är sant

```python
# Räkna ner från 5
räknare = 5

while räknare > 0:
    print(räknare)
    räknare = räknare - 1  # eller: räknare -= 1

print("Start! 🚀")

# Output:
# 5
# 4
# 3
# 2
# 1
# Start! 🚀
```

### Viktigt: Undvik oändliga loopar! ⚠️

```python
# DÅLIGT - denna loop slutar aldrig!
# while True:
#     print("Hej")

# BRA - ha alltid en exit-condition
antal = 0
while antal < 5:
    print("Hej")
    antal += 1  # Öka räknaren!
```

### break och continue

```python
# break - avbryt loopen
for i in range(10):
    if i == 5:
        break  # Sluta när i är 5
    print(i)
# Output: 0, 1, 2, 3, 4

# continue - hoppa över resten av denna iteration
for i in range(5):
    if i == 2:
        continue  # Hoppa över när i är 2
    print(i)
# Output: 0, 1, 3, 4
```

### ASCII-diagram för loop-struktur

```
for-loop:
   Start
     |
     v
┌─────────────────┐
│ För varje item  │
└────────┬────────┘
         |
         v
    [Gör detta]
         |
    ┌────┴─────┐
    │ Fler?    │
    └──┬────┬──┘
       |    |
      Ja   Nej
       |    └──> Klar!
       └──┘ (upprepa)

while-loop:
   Start
     |
     v
┌─────────────┐
│ Villkor     │<───┐
│ sant?       │    |
└──┬────┬─────┘    |
   |    |          |
  Ja   Nej        |
   |    └──> Klar!|
   v              |
[Gör detta]       |
   |              |
   └──────────────┘
```

---

## 2.5 Funktioner - Återanvändbara kodblock 🧩

**Funktioner** är som recept - du definierar dem en gång och kan sedan använda dem om och om igen!

### Skapa din första funktion

```python
# Definiera funktionen
def säg_hej():
    print("Hej!")
    print("Välkommen till Python!")

# Använd funktionen (anropa den)
säg_hej()
# Output:
# Hej!
# Välkommen till Python!

# Anropa den igen
säg_hej()
# Output:
# Hej!
# Välkommen till Python!
```

### Funktioner med parametrar (input)

```python
def hälsa(namn):
    print(f"Hej {namn}, trevligt att träffas!")

# Anropa med olika namn
hälsa("Anna")   # Output: Hej Anna, trevligt att träffas!
hälsa("Erik")   # Output: Hej Erik, trevligt att träffas!
```

### Flera parametrar

```python
def addera(tal1, tal2):
    summa = tal1 + tal2
    print(f"{tal1} + {tal2} = {summa}")

addera(5, 3)    # Output: 5 + 3 = 8
addera(10, 20)  # Output: 10 + 20 = 30
```

### return - Ge tillbaka ett värde

```python
def multiplicera(tal1, tal2):
    resultat = tal1 * tal2
    return resultat  # Ge tillbaka värdet

# Spara resultatet i en variabel
produkt = multiplicera(4, 5)
print(f"Produkten är: {produkt}")  # Output: Produkten är: 20

# Eller använd direkt
print(multiplicera(3, 7))  # Output: 21
```

### Praktiskt exempel: Area-funktioner

```python
def rektangel_area(längd, bredd):
    """Räknar ut arean av en rektangel."""
    return längd * bredd

def cirkel_area(radie):
    """Räknar ut arean av en cirkel."""
    pi = 3.14159
    return pi * radie ** 2

# Använd funktionerna
rektangel = rektangel_area(5, 3)
print(f"Rektangelns area: {rektangel}")  # Output: 15

cirkel = cirkel_area(4)
print(f"Cirkelns area: {cirkel:.2f}")  # Output: 50.27
```

### Default-parametrar

```python
def hälsa(namn, språk="svenska"):
    if språk == "svenska":
        print(f"Hej {namn}!")
    elif språk == "engelska":
        print(f"Hello {namn}!")
    else:
        print(f"Hola {namn}!")

hälsa("Anna")                    # Output: Hej Anna!
hälsa("Bob", "engelska")         # Output: Hello Bob!
hälsa("Carlos", "spanska")       # Output: Hola Carlos!
```

---

## 2.6 Projekt 1: Gissningslek 🎲

Nu ska vi bygga vårt första riktiga projekt - en gissningslek!

### Spelregler:
1. Datorn väljer ett slumpmässigt nummer mellan 1 och 100
2. Användaren gissar
3. Datorn säger om gissningen är för hög eller för låg
4. Fortsätt tills användaren gissar rätt

### Komplett kod:

```python
import random  # Importera random-modulen för att få slumptal

def gissningslek():
    """Ett enkelt gissningsspel."""

    # Datorn väljer ett slumpmässigt nummer
    hemligt_nummer = random.randint(1, 100)
    antal_gissningar = 0

    print("🎲 Välkommen till Gissningsleken! 🎲")
    print("Jag tänker på ett nummer mellan 1 och 100")
    print("Kan du gissa vilket? 🤔")
    print()

    while True:
        # Ta emot gissning från användaren
        gissning = int(input("Din gissning: "))
        antal_gissningar += 1

        # Kolla om gissningen är rätt
        if gissning < hemligt_nummer:
            print("📉 För lågt! Gissa högre!")
        elif gissning > hemligt_nummer:
            print("📈 För högt! Gissa lägre!")
        else:
            print(f"🎉 Rätt! Numret var {hemligt_nummer}!")
            print(f"Du gissade rätt på {antal_gissningar} försök!")
            break  # Avsluta loopen

# Starta spelet
gissningslek()
```

### Körningsexempel:

```
🎲 Välkommen till Gissningsleken! 🎲
Jag tänker på ett nummer mellan 1 och 100
Kan du gissa vilket? 🤔

Din gissning: 50
📈 För högt! Gissa lägre!
Din gissning: 25
📉 För lågt! Gissa högre!
Din gissning: 37
📈 För högt! Gissa lägre!
Din gissning: 31
🎉 Rätt! Numret var 31!
Du gissade rätt på 4 försök!
```

### 💡 Utmaningar för att förbättra spelet:

1. Lägg till en svårighetsgrad (lätt: 1-50, svår: 1-1000)
2. Begränsa antal gissningar till max 10
3. Fråga om användaren vill spela igen
4. Håll koll på bästa score (minst antal gissningar)

---

## 2.7 Projekt 2: Enkel kalkylator 🧮

Nu bygger vi en interaktiv kalkylator!

```python
def kalkylator():
    """En enkel miniräknare med grundläggande operationer."""

    print("🧮 Välkommen till Kalkylatorn! 🧮")
    print()
    print("Välj operation:")
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (*)")
    print("4. Division (/)")
    print("5. Avsluta")
    print()

    while True:
        val = input("Ditt val (1-5): ")

        if val == "5":
            print("Tack för att du använde kalkylatorn! 👋")
            break

        if val not in ["1", "2", "3", "4"]:
            print("❌ Ogiltigt val! Välj 1-5")
            continue

        # Ta emot två nummer
        tal1 = float(input("Ange första talet: "))
        tal2 = float(input("Ange andra talet: "))

        # Utför operation
        if val == "1":
            resultat = tal1 + tal2
            print(f"✅ {tal1} + {tal2} = {resultat}")
        elif val == "2":
            resultat = tal1 - tal2
            print(f"✅ {tal1} - {tal2} = {resultat}")
        elif val == "3":
            resultat = tal1 * tal2
            print(f"✅ {tal1} × {tal2} = {resultat}")
        elif val == "4":
            if tal2 == 0:
                print("❌ Fel! Kan inte dela med 0")
            else:
                resultat = tal1 / tal2
                print(f"✅ {tal1} ÷ {tal2} = {resultat}")

        print()  # Tom rad för läsbarhet

# Starta kalkylatorn
kalkylator()
```

### Körningsexempel:

```
🧮 Välkommen till Kalkylatorn! 🧮

Välj operation:
1. Addition (+)
2. Subtraktion (-)
3. Multiplikation (*)
4. Division (/)
5. Avsluta

Ditt val (1-5): 1
Ange första talet: 15
Ange andra talet: 7
✅ 15.0 + 7.0 = 22.0

Ditt val (1-5): 4
Ange första talet: 10
Ange andra talet: 0
❌ Fel! Kan inte dela med 0

Ditt val (1-5): 5
Tack för att du använde kalkylatorn! 👋
```

---

## 🎯 Övningar för Nivå 2

### Övning 2.1: Lista med favoritdjur ⭐
Skapa en lista med 5 favoritdjur. Skriv ut listan, lägg till ett djur, ta bort ett djur, och skriv ut den uppdaterade listan.

<details>
<summary>💡 Lösningsförslag</summary>

```python
djur = ["hund", "katt", "häst", "kanin", "hamster"]
print("Original lista:", djur)

djur.append("fisk")
print("Efter att lagt till:", djur)

djur.remove("hamster")
print("Efter borttagning:", djur)
```
</details>

### Övning 2.2: String-manipulation ⭐
Fråga användaren om deras namn. Skriv ut:
- Namnet i stora bokstäver
- Namnet i små bokstäver
- Längden på namnet
- Första bokstaven

<details>
<summary>💡 Lösningsförslag</summary>

```python
namn = input("Vad heter du? ")
print(f"Stora bokstäver: {namn.upper()}")
print(f"Små bokstäver: {namn.lower()}")
print(f"Längd: {len(namn)} bokstäver")
print(f"Första bokstaven: {namn[0]}")
```
</details>

### Övning 2.3: Ålderskontroll ⭐⭐
Skapa ett program som frågar efter ålder och säger:
- "Du är barn" (0-12)
- "Du är tonåring" (13-19)
- "Du är vuxen" (20+)

<details>
<summary>💡 Lösningsförslag</summary>

```python
ålder = int(input("Hur gammal är du? "))

if ålder <= 12:
    print("Du är barn")
elif ålder <= 19:
    print("Du är tonåring")
else:
    print("Du är vuxen")
```
</details>

### Övning 2.4: Loop genom listor ⭐⭐
Skapa en lista med 5 tal. Använd en for-loop för att skriva ut varje tal multiplicerat med 2.

<details>
<summary>💡 Lösningsförslag</summary>

```python
tal = [3, 7, 2, 9, 5]

for nummer in tal:
    print(f"{nummer} × 2 = {nummer * 2}")
```
</details>

### Övning 2.5: Summa av tal ⭐⭐
Använd en while-loop för att fråga användaren om tal. När de skriver "klar", skriv ut summan av alla tal.

<details>
<summary>💡 Lösningsförslag</summary>

```python
summa = 0

while True:
    svar = input("Ange ett tal (eller 'klar'): ")

    if svar.lower() == "klar":
        break

    tal = float(svar)
    summa += tal

print(f"Summan är: {summa}")
```
</details>

### Övning 2.6: Funktion för betyg ⭐⭐
Skapa en funktion `få_betyg(poäng)` som returnerar ett betyg (A-F) baserat på poäng.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def få_betyg(poäng):
    if poäng >= 90:
        return "A"
    elif poäng >= 80:
        return "B"
    elif poäng >= 70:
        return "C"
    elif poäng >= 60:
        return "D"
    else:
        return "F"

# Testa funktionen
print(få_betyg(95))  # A
print(få_betyg(72))  # C
print(få_betyg(55))  # F
```
</details>

### Övning 2.7: Jämn eller udda ⭐⭐
Skriv en funktion som kollar om ett tal är jämnt eller udda.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def jämn_eller_udda(tal):
    if tal % 2 == 0:
        return "jämn"
    else:
        return "udda"

# Testa
nummer = int(input("Ange ett tal: "))
print(f"{nummer} är {jämn_eller_udda(nummer)}")
```
</details>

### Övning 2.8: FizzBuzz ⭐⭐⭐
Klassisk programmeringsutmaning! Skriv ett program som:
- För tal 1-100:
  - Om delbart med 3: skriv "Fizz"
  - Om delbart med 5: skriv "Buzz"
  - Om delbart med både 3 och 5: skriv "FizzBuzz"
  - Annars: skriv talet

<details>
<summary>💡 Lösningsförslag</summary>

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```
</details>

### Övning 2.9: Omvänd lista ⭐⭐⭐
Skapa en funktion som tar en lista och returnerar den baklänges (utan att använda `.reverse()`).

<details>
<summary>💡 Lösningsförslag</summary>

```python
def omvänd_lista(lista):
    ny_lista = []
    for i in range(len(lista) - 1, -1, -1):
        ny_lista.append(lista[i])
    return ny_lista

# Eller enklare med slicing:
def omvänd_lista_v2(lista):
    return lista[::-1]

# Testa
min_lista = [1, 2, 3, 4, 5]
print(omvänd_lista(min_lista))  # [5, 4, 3, 2, 1]
```
</details>

### Övning 2.10: Primtalscheck ⭐⭐⭐
Skriv en funktion som kollar om ett tal är ett primtal (endast delbart med 1 och sig själv).

<details>
<summary>💡 Lösningsförslag</summary>

```python
def är_primtal(tal):
    if tal < 2:
        return False

    for i in range(2, int(tal ** 0.5) + 1):
        if tal % i == 0:
            return False

    return True

# Testa
for num in range(1, 21):
    if är_primtal(num):
        print(f"{num} är ett primtal")
```
</details>

---

## 🎓 Sammanfattning av Nivå 2

**Fantastiskt jobbat!** 🎉 Du har nu lärt dig viktiga programmeringskoncept:

✅ **Listor**: Samla många värden i en variabel
✅ **Strängar**: Arbeta med text på avancerade sätt
✅ **If-statements**: Få programmet att fatta beslut
✅ **Loopar**: Upprepa kod effektivt (for och while)
✅ **Funktioner**: Skapa återanvändbara kodblock
✅ **Projekt**: Byggt gissningslek och kalkylator

### Viktiga koncept att komma ihåg 📝

```python
# Listor
min_lista = [1, 2, 3]
min_lista.append(4)

# If-statement
if villkor:
    # kod
elif annat_villkor:
    # kod
else:
    # kod

# For-loop
for item in lista:
    print(item)

# While-loop
while villkor:
    # kod

# Funktion
def min_funktion(parameter):
    return värde
```

### Nästa steg 🚀

Nu är du redo för **Nivå 3**, där du lär dig:
- Mer om funktioner (scope, lambdas)
- Moduler och import
- Filhantering (läsa och skriva filer)
- Error handling (try/except)
- Dictionary och tuple
- Utvecklingsmiljö och debugging

---

**Fortsätt till:** [Nivå 3: Mellanliggande koncept →](Python_Guide_03_Niva3.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
