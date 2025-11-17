# 🐍 Nivå 1: Grundläggande koncept

## 🎯 Lärandemål för Nivå 1

Efter detta kapitel kommer du att kunna:
- ✅ Förklara vad programmering är med enkla ord
- ✅ Skriva ditt första Python-program
- ✅ Förstå variabler genom enkla analogier
- ✅ Utföra grundläggande beräkningar
- ✅ Ta emot input från användaren och visa output

---

## 1.1 Vad är programmering? 🤔

Tänk dig att du ska lära en robot att göra en smörgås. Du kan inte bara säga "gör en smörgås" - du måste förklara varje steg:

1. Ta en bit bröd
2. Öppna burken med jordnötssmör
3. Ta en kniv
4. Stick ner kniven i burken
5. Bred jordnötssmöret på brödet
6. ... och så vidare

**Det är exakt vad programmering är!** Du ger datorn mycket detaljerade instruktioner, steg för steg, för att utföra en uppgift.

### Varför Python? 🐍

Python är som att prata med en väldigt smart vän som förstår enkla instruktioner:
- **Lätt att läsa**: Koden ser nästan ut som vanlig engelska
- **Förlåtande**: Den hjälper dig att hitta fel
- **Kraftfull**: Kan göra nästan vad som helst - från enkla räknare till AI

---

## 1.2 Ditt första Python-program 🎉

Låt oss skriva det klassiska "Hello World"-programmet:

```python
# Detta är en kommentar - Python ignorerar den
# Kommentarer används för att förklara vad koden gör

print("Hej världen!")
```

**Vad händer här?**
- `print()` är som att säga till Python: "visa detta på skärmen"
- Texten innanför citattecknen `" "` visas exakt som den är
- Kommentarer börjar med `#` och används för att förklara koden

### Prova själv! 💻

Öppna Python (IDLE, VS Code eller terminalen) och skriv:

```python
print("Mitt namn är [ditt namn]")
print("Jag lär mig Python!")
print("Det här är kul! 🎉")
```

**Output:**
```
Mitt namn är Anna
Jag lär mig Python!
Det här är kul! 🎉
```

---

## 1.3 Variabler - Lådor för dina saker 📦

Föreställ dig att du har flera lådor i ditt rum. I varje låda kan du lägga olika saker:
- En låda för leksaker
- En låda för kläder
- En låda för böcker

**Variabler är exakt som dessa lådor!** De lagrar information som du kan använda senare.

### Skapa din första variabel

```python
# Skapa en variabel som heter "namn" och lägg in din namn i den
namn = "Lisa"

# Visa vad som finns i lådan
print(namn)  # Output: Lisa

# Du kan ändra vad som finns i lådan
namn = "Erik"
print(namn)  # Output: Erik
```

### Fler exempel med variabler 🎈

```python
# Variabel för ålder (nummer)
ålder = 10

# Variabel för favoritfärg (text)
favoritfärg = "blå"

# Variabel för antal husdjur (nummer)
antal_husdjur = 2

# Visa allt!
print("Mitt namn är", namn)
print("Jag är", ålder, "år gammal")
print("Min favoritfärg är", favoritfärg)
print("Jag har", antal_husdjur, "husdjur")
```

**Output:**
```
Mitt namn är Erik
Jag är 10 år gammal
Min favoritfärg är blå
Jag har 2 husdjur
```

### Regler för variabelnamn 📝

1. **Kan innehålla**: bokstäver, siffror, understrykning `_`
2. **Får INTE börja med**: siffra
3. **Är skiftlägeskänsliga**: `namn` och `Namn` är olika variabler
4. **Använd beskrivande namn**: `ålder` är bättre än `x`

```python
# BRA exempel ✅
mitt_namn = "Anna"
alder = 25
antal_applen = 5

# DÅLIGA exempel ❌
1namn = "Anna"        # Får inte börja med siffra!
mitt-namn = "Anna"    # Bindestreck fungerar inte!
n = "Anna"           # För kort, otydligt vad det är
```

---

## 1.4 Datatyper - Olika sorters information 🔢

Precis som vi har olika lådor för olika saker, har Python olika **datatyper** för olika information.

### De tre viktigaste datatyperna för nybörjare:

#### 1. Heltal (Integer/int) - Hela nummer

```python
antal_äpplen = 5
ålder = 12
temperatur = -3

print(antal_äpplen)  # Output: 5
```

**Tänk på det som**: Antal saker du kan räkna (1, 2, 3...)

#### 2. Decimaltal (Float) - Nummer med decimaler

```python
längd = 1.65  # meter
pris = 49.90  # kronor
temperatur = 23.5  # grader

print(pris)  # Output: 49.9
```

**Tänk på det som**: Nummer med decimalpunkt

#### 3. Text (String/str) - Ord och meningar

```python
namn = "Emma"
meddelande = "Hej och välkommen!"
adress = "Storgatan 12"

print(meddelande)  # Output: Hej och välkommen!
```

**Tänk på det som**: Allt som står inom citattecken `" "` eller `' '`

### Visuell tabell över datatyper 📊

```
┌─────────────┬──────────────┬────────────────┬─────────────────────┐
│ Datatyp     │ Python-namn  │ Exempel        │ Användning          │
├─────────────┼──────────────┼────────────────┼─────────────────────┤
│ Heltal      │ int          │ 42, -7, 0      │ Räkna saker         │
│ Decimaltal  │ float        │ 3.14, -0.5     │ Mätningar, pengar   │
│ Text        │ str          │ "Hej", 'Anna'  │ Namn, meddelanden   │
└─────────────┴──────────────┴────────────────┴─────────────────────┘
```

### Kolla datatypen 🔍

```python
ålder = 10
namn = "Lisa"
längd = 1.45

# Använd type() för att se datatypen
print(type(ålder))    # Output: <class 'int'>
print(type(namn))     # Output: <class 'str'>
print(type(längd))    # Output: <class 'float'>
```

---

## 1.5 Enkla beräkningar - Python som miniräknare 🧮

Python är superbra på matematik! Du kan använda den som en avancerad miniräknare.

### Grundläggande operatorer

```python
# Addition (plus)
äpplen = 3 + 2
print("Jag har", äpplen, "äpplen")  # Output: Jag har 5 äpplen

# Subtraktion (minus)
kvar = 10 - 3
print("Jag har", kvar, "kvar")  # Output: Jag har 7 kvar

# Multiplikation (gånger)
totalt = 4 * 5
print("Totalt:", totalt)  # Output: Totalt: 20

# Division (delat)
delat = 10 / 2
print("Resultat:", delat)  # Output: Resultat: 5.0
```

### Operatorer - Översikt 📐

```
┌──────────────┬──────────┬────────────────┬────────────┐
│ Operator     │ Symbol   │ Exempel        │ Resultat   │
├──────────────┼──────────┼────────────────┼────────────┤
│ Addition     │ +        │ 5 + 3          │ 8          │
│ Subtraktion  │ -        │ 10 - 4         │ 6          │
│ Multiplik.   │ *        │ 3 * 4          │ 12         │
│ Division     │ /        │ 10 / 2         │ 5.0        │
│ Upphöjt till │ **       │ 2 ** 3         │ 8          │
└──────────────┴──────────┴────────────────┴────────────┘
```

### Praktiskt exempel: Räkna äpplen 🍎

```python
# Du har några äpplen
äpplen_jag_har = 5

# Din kompis ger dig 3 äpplen till
äpplen_från_kompis = 3

# Hur många har du nu?
totalt_äpplen = äpplen_jag_har + äpplen_från_kompis

print("Jag har totalt", totalt_äpplen, "äpplen!")  # Output: Jag har totalt 8 äpplen!

# Du äter 2 äpplen
äpplen_ätna = 2
äpplen_kvar = totalt_äpplen - äpplen_ätna

print("Nu har jag", äpplen_kvar, "äpplen kvar")  # Output: Nu har jag 6 äpplen kvar
```

### Mer avancerade beräkningar 🎓

```python
# Upphöjt till (t.ex. 2 upphöjt till 3 = 2*2*2)
kvadrat = 5 ** 2  # 5 upphöjt till 2 = 25
print("5 i kvadrat är:", kvadrat)

# Kombinera operationer
resultat = 10 + 5 * 2  # Python räknar * före +
print(resultat)  # Output: 20 (inte 30!)

# Använd paranteser för att ändra ordning
resultat2 = (10 + 5) * 2  # Parentesen räknas först
print(resultat2)  # Output: 30
```

💡 **Tips**: Python följer samma matematiska regler som du lär dig i skolan:
1. Parenteser först
2. Upphöjt till
3. Multiplikation och division
4. Addition och subtraktion

---

## 1.6 Input och Output - Prata med användaren 💬

Nu ska vi lära oss hur programmet kan prata med användaren!

### Output med print() 📢

Vi har redan använt `print()` för att visa text:

```python
print("Hej!")
print("Mitt namn är Python")
print("Jag är här för att hjälpa dig!")
```

**Output:**
```
Hej!
Mitt namn är Python
Jag är här för att hjälpa dig!
```

### Input - Ta emot information 📥

`input()` låter användaren skriva in information:

```python
# Fråga användaren vad de heter
namn = input("Vad heter du? ")

# Hälsa på dem
print("Hej", namn, "!")
print("Trevligt att träffas!")
```

**Så här ser det ut när programmet körs:**
```
Vad heter du? Lisa
Hej Lisa !
Trevligt att träffas!
```

### Komplett exempel: Personligt hälsning 🎁

```python
# Fråga om namn
namn = input("Vad heter du? ")

# Fråga om ålder
ålder = input("Hur gammal är du? ")

# Fråga om favoritfärg
färg = input("Vad är din favoritfärg? ")

# Skriv ut ett personligt meddelande
print("=== Din profil ===")
print("Namn:", namn)
print("Ålder:", ålder, "år")
print("Favoritfärg:", färg)
print("Trevligt att lära känna dig,", namn, "!")
```

**Körningsexempel:**
```
Vad heter du? Emma
Hur gammal är du? 11
Vad är din favoritfärg? Rosa
=== Din profil ===
Namn: Emma
Ålder: 11 år
Favoritfärg: Rosa
Trevligt att lära känna dig, Emma !
```

### ⚠️ Viktigt om input()

Input ger alltid tillbaka **text** (string), även om användaren skriver ett nummer!

```python
# Detta kommer INTE fungera som förväntat!
ålder = input("Hur gammal är du? ")  # Användaren skriver: 10
nästa_år = ålder + 1  # FEL! Kan inte lägga ihop text och nummer

# Rätt sätt (konvertera till nummer):
ålder = int(input("Hur gammal är du? "))  # Gör om till heltal
nästa_år = ålder + 1
print("Nästa år blir du", nästa_år, "år!")
```

---

## 1.7 F-strings - Snyggare textutskrifter ✨

F-strings är ett modernt och enkelt sätt att sätta ihop text och variabler:

```python
namn = "Oliver"
ålder = 9
favoritdjur = "katt"

# Gammalt sätt (fungerar men är krångligt)
print("Mitt namn är", namn, "och jag är", ålder, "år")

# Nytt sätt med f-string (mycket snyggare!)
print(f"Mitt namn är {namn} och jag är {ålder} år")
print(f"Jag älskar {favoritdjur}er!")
```

**Output:**
```
Mitt namn är Oliver och jag är 9 år
Jag älskar katter!
```

### Varför f-strings är bra 🌟

```python
pris = 49.90
antal = 3

# Lägg till beräkningar direkt i f-string!
print(f"Totalt pris för {antal} st: {pris * antal} kr")
# Output: Totalt pris för 3 st: 149.7 kr

# Formatera decimaler snyggt
print(f"Totalt pris: {pris * antal:.2f} kr")
# Output: Totalt pris: 149.70 kr
```

💡 **Tips**: `:.2f` betyder "visa 2 decimaler"

---

## 🎯 Övningar för Nivå 1

Nu är det dags att testa dina nya kunskaper! Försök lösa övningarna nedan.

### Övning 1.1: Ditt första program ⭐
Skriv ett program som skriver ut ditt namn, ålder och favoritmat.

```python
# Din kod här
print("Mitt namn är ...")
# Fortsätt själv!
```

<details>
<summary>💡 Lösningsförslag</summary>

```python
print("Mitt namn är Anna")
print("Jag är 10 år gammal")
print("Min favoritmat är pizza")
```
</details>

### Övning 1.2: Variabler ⭐
Skapa variabler för ditt namn, din ålder och din favoritfärg. Skriv sedan ut dem med `print()`.

<details>
<summary>💡 Lösningsförslag</summary>

```python
namn = "Erik"
ålder = 12
favoritfärg = "grön"

print("Namn:", namn)
print("Ålder:", ålder)
print("Favoritfärg:", favoritfärg)
```
</details>

### Övning 1.3: Enkel addition ⭐
Du har 7 bollar. Din kompis ger dig 5 bollar till. Hur många bollar har du nu? Använd variabler och skriv ut resultatet.

<details>
<summary>💡 Lösningsförslag</summary>

```python
bollar_jag_har = 7
bollar_från_kompis = 5
totalt = bollar_jag_har + bollar_från_kompis

print(f"Jag har totalt {totalt} bollar")
```
</details>

### Övning 1.4: Miniräknare ⭐⭐
Skapa variabler för två nummer och räkna ut:
- Summa (+)
- Skillnad (-)
- Produkt (*)
- Division (/)

<details>
<summary>💡 Lösningsförslag</summary>

```python
tal1 = 20
tal2 = 4

print(f"{tal1} + {tal2} = {tal1 + tal2}")
print(f"{tal1} - {tal2} = {tal1 - tal2}")
print(f"{tal1} * {tal2} = {tal1 * tal2}")
print(f"{tal1} / {tal2} = {tal1 / tal2}")
```
</details>

### Övning 1.5: Interaktiv hälsning ⭐⭐
Skriv ett program som frågar användaren om deras namn och sedan hälsar på dem.

<details>
<summary>💡 Lösningsförslag</summary>

```python
namn = input("Vad heter du? ")
print(f"Hej {namn}, välkommen!")
print(f"Kul att träffa dig, {namn}!")
```
</details>

### Övning 1.6: Åldersräknare ⭐⭐
Fråga användaren hur gammal de är och räkna ut hur gamla de blir nästa år och om 10 år.

<details>
<summary>💡 Lösningsförslag</summary>

```python
ålder = int(input("Hur gammal är du? "))
nästa_år = ålder + 1
om_tio_år = ålder + 10

print(f"Nästa år blir du {nästa_år} år")
print(f"Om 10 år blir du {om_tio_år} år")
```
</details>

### Övning 1.7: Område av rektangel ⭐⭐
Fråga användaren om längd och bredd på en rektangel. Räkna ut och skriv ut arean (längd * bredd).

<details>
<summary>💡 Lösningsförslag</summary>

```python
längd = float(input("Ange längd: "))
bredd = float(input("Ange bredd: "))
area = längd * bredd

print(f"Arean är {area} kvadratmeter")
```
</details>

### Övning 1.8: Personlig presentation ⭐⭐⭐
Skapa ett program som frågar efter:
- Namn
- Ålder
- Favoritfärg
- Favoritdjur

Skriv sedan ut en snygg presentation med f-strings.

<details>
<summary>💡 Lösningsförslag</summary>

```python
namn = input("Vad heter du? ")
ålder = input("Hur gammal är du? ")
färg = input("Favoritfärg? ")
djur = input("Favoritdjur? ")

print("\n=== MIN PRESENTATION ===")
print(f"Hej! Jag heter {namn}")
print(f"Jag är {ålder} år gammal")
print(f"Min favoritfärg är {färg}")
print(f"Och jag älskar {djur}!")
print("=======================")
```
</details>

---

## 🎓 Sammanfattning av Nivå 1

**Grattis!** 🎉 Du har nu lärt dig grunderna i Python! Här är vad du kan:

✅ **Programmering**: Du förstår att programmering är att ge datorn steg-för-steg instruktioner
✅ **Print**: Du kan visa text med `print()`
✅ **Variabler**: Du kan lagra information i variabler (som lådor)
✅ **Datatyper**: Du känner till int, float och str
✅ **Beräkningar**: Du kan använda Python som miniräknare (+, -, *, /)
✅ **Input**: Du kan ta emot information från användaren med `input()`
✅ **F-strings**: Du kan sätta ihop text och variabler snyggt

### Viktiga koncept att komma ihåg 📝

```python
# Kommentar - förklarar vad koden gör
print("Text att visa")           # Visa text på skärmen
variabel = "värde"                # Lagra information
ålder = int(input("Ålder? "))     # Ta emot nummer från användaren
print(f"Jag är {ålder} år")       # F-string för snygg output
```

### Nästa steg 🚀

Nu är du redo för **Nivå 2**, där du lär dig:
- Listor (samla många värden)
- If-statements (få programmet att göra val)
- Loopar (upprepa saker)
- Funktioner (återanvändbara kodblock)
- Bygga ditt första riktiga program!

---

**Fortsätt till:** [Nivå 2: Introduktion till programmering →](Python_Guide_02_Niva2.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
