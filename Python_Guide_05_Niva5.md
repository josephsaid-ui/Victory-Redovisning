# 🐍 Nivå 5: Cutting-edge och moderna applikationer

## 🎯 Lärandemål för Nivå 5

Efter detta kapitel kommer du att kunna:
- ✅ Förstå och använda async/await för concurrent programming
- ✅ Arbeta med dataclasses och pattern matching (Python 3.10+)
- ✅ Sätta upp och använda virtual environments
- ✅ Skriva och köra tester med pytest
- ✅ Analysera data med pandas och numpy
- ✅ Bygga webb-API:er med FastAPI
- ✅ Förstå grunderna i machine learning med scikit-learn
- ✅ Använda Git för version control
- ✅ Tillämpa verkliga case studies från industrin

---

## 5.1 Async/Await - Asynkron programmering ⚡

**Asynkron programmering** låter programmet göra flera saker "samtidigt" utan att blockera.

### Synkron vs Asynkron

```python
import time

# SYNKRON - blockerande
def hämta_data_synk(namn):
    print(f"Börjar hämta {namn}...")
    time.sleep(2)  # Simulerar långsam operation
    print(f"Klar med {namn}!")
    return f"Data från {namn}"

# Detta tar 6 sekunder! (2+2+2)
start = time.time()
hämta_data_synk("Server 1")
hämta_data_synk("Server 2")
hämta_data_synk("Server 3")
print(f"Total tid: {time.time() - start:.1f}s")  # ~6 sekunder
```

```python
import asyncio

# ASYNKRON - icke-blockerande
async def hämta_data_async(namn):
    print(f"Börjar hämta {namn}...")
    await asyncio.sleep(2)  # Simulerar långsam operation
    print(f"Klar med {namn}!")
    return f"Data från {namn}"

# Detta tar bara 2 sekunder! (samtidigt)
async def main():
    start = time.time()
    # Kör alla tre samtidigt
    resultat = await asyncio.gather(
        hämta_data_async("Server 1"),
        hämta_data_async("Server 2"),
        hämta_data_async("Server 3")
    )
    print(f"Total tid: {time.time() - start:.1f}s")  # ~2 sekunder
    return resultat

# Kör async-funktionen
# asyncio.run(main())
```

### Grundläggande async-syntax

```python
import asyncio

# 1. Definiera async-funktion med 'async def'
async def säg_hej(namn, fördröjning):
    await asyncio.sleep(fördröjning)  # 'await' för async-operationer
    print(f"Hej {namn}!")
    return f"Hälsade på {namn}"

# 2. Kör async-funktion
async def main():
    # Kör en i taget
    await säg_hej("Anna", 1)
    await säg_hej("Erik", 1)

    # Kör parallellt med gather
    resultat = await asyncio.gather(
        säg_hej("Lisa", 1),
        säg_hej("Oscar", 1)
    )
    print(resultat)

# 3. Starta event loop
# asyncio.run(main())
```

### Praktiskt exempel: Hämta flera webbsidor

```python
import asyncio
import aiohttp  # pip install aiohttp

async def hämta_url(session, url):
    """Hämtar innehåll från en URL asynkront."""
    async with session.get(url) as response:
        innehåll = await response.text()
        print(f"✅ Hämtade {url}: {len(innehåll)} bytes")
        return innehåll

async def hämta_flera_urls(urls):
    """Hämtar flera URLs parallellt."""
    async with aiohttp.ClientSession() as session:
        tasks = [hämta_url(session, url) for url in urls]
        resultat = await asyncio.gather(*tasks)
        return resultat

# Användning
urls = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]
# resultat = asyncio.run(hämta_flera_urls(urls))
```

### Async-flödesschema 📊

```
SYNKRON:
Task 1 ████████
              Task 2 ████████
                           Task 3 ████████
Time: ————————————————————————————————————> 24s

ASYNKRON:
Task 1 ████████
Task 2 ████████
Task 3 ████████
Time: ————————> 8s
```

---

## 5.2 Dataclasses - Enklare klasser (Python 3.7+) 📦

**Dataclasses** automatiserar skapandet av vanliga klass-metoder.

### Utan dataclasses (gammalt sätt)

```python
class Person:
    def __init__(self, namn, ålder, email):
        self.namn = namn
        self.ålder = ålder
        self.email = email

    def __repr__(self):
        return f"Person(namn={self.namn!r}, ålder={self.ålder!r}, email={self.email!r})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (self.namn, self.ålder, self.email) == (other.namn, other.ålder, other.email)
```

### Med dataclasses (nytt sätt)

```python
from dataclasses import dataclass

@dataclass
class Person:
    namn: str
    ålder: int
    email: str

# Får automatiskt __init__, __repr__, __eq__, etc.!
person = Person("Anna", 25, "anna@example.com")
print(person)  # Person(namn='Anna', ålder=25, email='anna@example.com')
```

### Dataclass-features

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    namn: str
    ålder: int
    kurser: List[str] = field(default_factory=list)  # Mutable default
    genomsnitt: float = 0.0  # Default värde

    def lägg_till_kurs(self, kurs: str) -> None:
        self.kurser.append(kurs)

# Användning
student = Student("Erik", 20)
student.lägg_till_kurs("Python")
student.lägg_till_kurs("Machine Learning")
print(student)

# Frozen dataclass (immutable)
@dataclass(frozen=True)
class Punkt:
    x: float
    y: float

p = Punkt(1.0, 2.0)
# p.x = 5  # FEL! dataclass är frozen
```

---

## 5.3 Pattern matching - Match/Case (Python 3.10+) 🎯

**Pattern matching** är ett kraftfullt sätt att matcha komplexa mönster.

### Grundläggande match/case

```python
def hantera_kommando(kommando):
    match kommando:
        case "start":
            print("Startar programmet...")
        case "stop":
            print("Stoppar programmet...")
        case "status":
            print("Programmet körs")
        case _:  # default/wildcard
            print("Okänt kommando!")

hantera_kommando("start")   # Startar programmet...
hantera_kommando("help")    # Okänt kommando!
```

### Pattern matching med strukturer

```python
def processera_data(data):
    match data:
        # Matcha specifika värden
        case 0:
            return "Noll"

        # Matcha lista med specifik längd
        case [x]:
            return f"Ett element: {x}"

        case [x, y]:
            return f"Två element: {x}, {y}"

        # Matcha lista med rest
        case [första, *rest]:
            return f"Första: {första}, Resten: {rest}"

        # Matcha dictionary
        case {"namn": namn, "ålder": ålder}:
            return f"{namn} är {ålder} år"

        # Default
        case _:
            return "Okänd struktur"

# Test
print(processera_data(0))                           # Noll
print(processera_data([42]))                        # Ett element: 42
print(processera_data([1, 2, 3, 4]))               # Första: 1, Resten: [2, 3, 4]
print(processera_data({"namn": "Anna", "ålder": 25}))  # Anna är 25 år
```

### Pattern matching med klasser

```python
from dataclasses import dataclass

@dataclass
class Punkt:
    x: float
    y: float

@dataclass
class Cirkel:
    radie: float

@dataclass
class Rektangel:
    bredd: float
    höjd: float

def beskriv_form(form):
    match form:
        case Punkt(x=0, y=0):
            return "Origo"
        case Punkt(x=x, y=0):
            return f"På X-axeln vid {x}"
        case Punkt(x=0, y=y):
            return f"På Y-axeln vid {y}"
        case Punkt(x=x, y=y):
            return f"Punkt vid ({x}, {y})"
        case Cirkel(radie=r):
            return f"Cirkel med radie {r}"
        case Rektangel(bredd=b, höjd=h):
            return f"Rektangel {b}x{h}"
        case _:
            return "Okänd form"

# Test
print(beskriv_form(Punkt(0, 0)))        # Origo
print(beskriv_form(Punkt(5, 0)))        # På X-axeln vid 5
print(beskriv_form(Cirkel(10)))         # Cirkel med radie 10
```

---

## 5.4 Virtual environments och pakethantering 📦

**Virtual environments** isolerar projektets dependencies.

### Skapa och använda venv

```bash
# Skapa virtual environment
python -m venv mitt_projekt_env

# Aktivera (Windows)
mitt_projekt_env\Scripts\activate

# Aktivera (Mac/Linux)
source mitt_projekt_env/bin/activate

# Nu är du i virtual environment!
# Installera paket
pip install pandas numpy flask

# Spara dependencies
pip freeze > requirements.txt

# Deaktivera
deactivate
```

### requirements.txt

```txt
# requirements.txt
pandas==2.1.0
numpy==1.25.2
flask==3.0.0
requests>=2.31.0
pytest~=7.4.0
```

```bash
# Installera alla dependencies
pip install -r requirements.txt
```

### pip - Pakethanterare 🎁

```bash
# Installera paket
pip install paketet

# Installera specifik version
pip install paketet==1.2.3

# Uppgradera paket
pip install --upgrade paketet

# Avinstallera
pip uninstall paketet

# Lista installerade paket
pip list

# Sök paket
pip search sökord

# Visa paketinfo
pip show paketet
```

---

## 5.5 Testing med pytest 🧪

**Pytest** är det populäraste test-ramverket för Python.

### Installera pytest

```bash
pip install pytest
```

### Enkel test-fil

```python
# test_calculator.py

def addera(a, b):
    return a + b

def subtrahera(a, b):
    return a - b

# Test-funktioner börjar med 'test_'
def test_addera():
    assert addera(2, 3) == 5
    assert addera(-1, 1) == 0
    assert addera(0, 0) == 0

def test_subtrahera():
    assert subtrahera(5, 3) == 2
    assert subtrahera(0, 5) == -5

def test_addera_negativa():
    assert addera(-2, -3) == -5
```

### Kör tester

```bash
# Kör alla tester
pytest

# Kör specifik fil
pytest test_calculator.py

# Verbose output
pytest -v

# Visa print-statements
pytest -s
```

### Fixtures - Återanvändbar test-data

```python
import pytest

@pytest.fixture
def exempel_lista():
    """Skapar en test-lista för tester."""
    return [1, 2, 3, 4, 5]

def test_längd(exempel_lista):
    assert len(exempel_lista) == 5

def test_första_element(exempel_lista):
    assert exempel_lista[0] == 1

def test_summa(exempel_lista):
    assert sum(exempel_lista) == 15
```

### Testa exceptions

```python
import pytest

def dela(a, b):
    if b == 0:
        raise ValueError("Kan inte dela med 0")
    return a / b

def test_dela():
    assert dela(10, 2) == 5

def test_dela_med_noll():
    with pytest.raises(ValueError, match="Kan inte dela med 0"):
        dela(10, 0)
```

### Parametriserade tester

```python
import pytest

def är_jämn(n):
    return n % 2 == 0

@pytest.mark.parametrize("tal, förväntat", [
    (2, True),
    (3, False),
    (0, True),
    (-2, True),
    (7, False)
])
def test_är_jämn(tal, förväntat):
    assert är_jämn(tal) == förväntat
```

---

## 5.6 Data Science - pandas och numpy 📊

### NumPy - Numeriska beräkningar

```python
import numpy as np

# Skapa arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]

# 2D array (matris)
matris = np.array([[1, 2, 3], [4, 5, 6]])
print(matris)
# [[1 2 3]
#  [4 5 6]]

# Matematiska operationer (vektoriserade!)
print(arr * 2)        # [2 4 6 8 10]
print(arr ** 2)       # [1 4 9 16 25]
print(np.sqrt(arr))   # [1. 1.41 1.73 2. 2.24]

# Statistik
print(np.mean(arr))   # 3.0
print(np.std(arr))    # 1.41
print(np.sum(arr))    # 15

# Skapa arrays
nollor = np.zeros((3, 3))
ettor = np.ones((2, 4))
sekvens = np.arange(0, 10, 2)  # [0 2 4 6 8]
slump = np.random.rand(5)       # 5 slumptal mellan 0 och 1
```

### Pandas - Dataanalys

```python
import pandas as pd

# Skapa DataFrame från dictionary
data = {
    "Namn": ["Anna", "Erik", "Lisa", "Oscar"],
    "Ålder": [25, 30, 22, 27],
    "Stad": ["Stockholm", "Göteborg", "Malmö", "Uppsala"],
    "Lön": [45000, 52000, 38000, 48000]
}

df = pd.DataFrame(data)
print(df)
#      Namn  Ålder       Stad    Lön
# 0    Anna     25  Stockholm  45000
# 1    Erik     30   Göteborg  52000
# 2    Lisa     22      Malmö  38000
# 3  Oscar     27    Uppsala  48000

# Grundläggande operationer
print(df.head())          # Första raderna
print(df.info())          # Information om DataFrame
print(df.describe())      # Statistik

# Välja kolumner
print(df["Namn"])         # En kolumn
print(df[["Namn", "Ålder"]])  # Flera kolumner

# Filtrera rader
över_25 = df[df["Ålder"] > 25]
print(över_25)

stockholm = df[df["Stad"] == "Stockholm"]
print(stockholm)

# Sortera
sorterad = df.sort_values("Lön", ascending=False)
print(sorterad)

# Statistik
print(f"Medelålder: {df['Ålder'].mean()}")
print(f"Högsta lön: {df['Lön'].max()}")

# Lägg till kolumn
df["Bonus"] = df["Lön"] * 0.1
print(df)
```

### Läsa och skriva filer med pandas

```python
import pandas as pd

# Läsa CSV
# df = pd.read_csv("data.csv")

# Skriva CSV
df.to_csv("output.csv", index=False)

# Läsa Excel
# df = pd.read_excel("data.xlsx")

# Skriva Excel
# df.to_excel("output.xlsx", index=False)

# Läsa JSON
# df = pd.read_json("data.json")

# Skriva JSON
df.to_json("output.json", orient="records", indent=2)
```

### Praktiskt exempel: Dataanalys

```python
import pandas as pd
import numpy as np

# Skapa exempel-data
np.random.seed(42)
försäljning = pd.DataFrame({
    "Månad": ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun"],
    "Produkt_A": np.random.randint(100, 500, 6),
    "Produkt_B": np.random.randint(100, 500, 6),
    "Produkt_C": np.random.randint(100, 500, 6)
})

# Total försäljning per månad
försäljning["Total"] = försäljning[["Produkt_A", "Produkt_B", "Produkt_C"]].sum(axis=1)

# Bästa månad
bästa_månad = försäljning.loc[försäljning["Total"].idxmax()]
print(f"Bästa månad: {bästa_månad['Månad']} med {bästa_månad['Total']} sålda")

# Genomsnitt per produkt
print("\nGenomsnitt per produkt:")
print(försäljning[["Produkt_A", "Produkt_B", "Produkt_C"]].mean())
```

---

## 5.7 Webbutveckling - FastAPI 🌐

**FastAPI** är ett modernt, snabbt webb-ramverk för att bygga API:er.

### Installera FastAPI

```bash
pip install fastapi uvicorn[standard]
```

### Enkel FastAPI-app

```python
# main.py
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def läs_root():
    return {"meddelande": "Välkommen till mitt API!"}

@app.get("/items/{item_id}")
def läs_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/användare/{namn}")
def hälsa_användare(namn: str):
    return {"meddelande": f"Hej {namn}!"}
```

### Kör servern

```bash
uvicorn main:app --reload

# Besök:
# http://127.0.0.1:8000
# http://127.0.0.1:8000/docs  (Automatisk API-dokumentation!)
```

### POST requests och Pydantic-modeller

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    namn: str
    ålder: int
    kurser: List[str] = []

# In-memory databas
studenter_db: List[Student] = []

@app.post("/studenter/")
def skapa_student(student: Student):
    studenter_db.append(student)
    return {"meddelande": "Student skapad!", "student": student}

@app.get("/studenter/")
def hämta_studenter():
    return {"studenter": studenter_db}

@app.get("/studenter/{namn}")
def hämta_student(namn: str):
    for student in studenter_db:
        if student.namn.lower() == namn.lower():
            return {"student": student}
    return {"error": "Student inte funnen"}
```

### Testa API:et

```python
import requests

# POST - skapa student
response = requests.post(
    "http://127.0.0.1:8000/studenter/",
    json={"namn": "Anna", "ålder": 20, "kurser": ["Python", "ML"]}
)
print(response.json())

# GET - hämta alla studenter
response = requests.get("http://127.0.0.1:8000/studenter/")
print(response.json())
```

---

## 5.8 Machine Learning - scikit-learn basics 🤖

### Installera scikit-learn

```bash
pip install scikit-learn matplotlib
```

### Enkel klassificering

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 1. Ladda data
iris = load_iris()
X = iris.data   # Features (längd/bredd av blomblad)
y = iris.target # Labels (art av iris)

# 2. Dela data i träning och test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Skapa och träna modell
modell = DecisionTreeClassifier()
modell.fit(X_train, y_train)

# 4. Gör prediktioner
prediktioner = modell.predict(X_test)

# 5. Utvärdera
noggrannhet = accuracy_score(y_test, prediktioner)
print(f"Noggrannhet: {noggrannhet * 100:.2f}%")

# 6. Använd modellen
ny_blomma = [[5.1, 3.5, 1.4, 0.2]]
förutsägelse = modell.predict(ny_blomma)
print(f"Förutsedd art: {iris.target_names[förutsägelse[0]]}")
```

### Regression - förutsäga priser

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Data: Storlek (m²) -> Pris (tkr)
storlek = np.array([50, 70, 90, 110, 130]).reshape(-1, 1)
pris = np.array([1500, 2100, 2700, 3300, 3900])

# Träna modell
modell = LinearRegression()
modell.fit(storlek, pris)

# Förutsäg pris för 100m²
nytt_pris = modell.predict([[100]])
print(f"Förutsagt pris för 100m²: {nytt_pris[0]:.0f} tkr")
```

---

## 5.9 Git - Version Control 🔄

### Grundläggande Git-kommandon

```bash
# Initiera nytt repository
git init

# Klona existerande repository
git clone https://github.com/användarnamn/repo.git

# Se status
git status

# Lägg till filer för commit
git add fil.py
git add .  # Alla filer

# Committa ändringar
git commit -m "Lagt till ny feature"

# Pusha till remote
git push origin main

# Hämta ändringar
git pull origin main

# Se historik
git log
git log --oneline

# Skapa ny branch
git branch ny-feature
git checkout ny-feature
# eller: git checkout -b ny-feature

# Merga branch
git checkout main
git merge ny-feature

# Se skillnader
git diff
```

### .gitignore för Python

```gitignore
# .gitignore

# Virtual environment
venv/
env/
ENV/

# Python cache
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/

# Environment variables
.env

# Distribution
dist/
build/
*.egg-info/

# Jupyter Notebooks
.ipynb_checkpoints/

# Data files (oftast)
*.csv
*.xlsx
*.db
```

---

## 5.10 Verkliga case studies 🌍

### Case Study 1: Python hos Google 🔍

**Användning:**
- YouTube: Backend-servrar
- Gmail: Spam-filter (ML)
- Google Search: Crawlers och indexering

**Lärdom:**
- Python skalas bra med rätt arkitektur
- Type hints och testing är kritiskt för stora kodbaser
- C-extensions för performance-kritiska delar

### Case Study 2: Netflix - Recommendation System 🎬

**Teknisk stack:**
- pandas och NumPy för databehandling
- scikit-learn och TensorFlow för ML-modeller
- FastAPI för interna API:er

**Lärdom:**
- Data science är Python:s styrka
- A/B-testing är essentiellt
- Asynkron programmering för skalbarhet

### Case Study 3: Instagram - Från Django till Scale 📸

**Utveckling:**
- Började med Django (Python web framework)
- 1 miljard+ användare på Python-backend
- Async workers för bildbehandling

**Lärdom:**
- Python kan hantera massiv skala
- Caching (Redis) är kritiskt
- Database-optimering viktigare än språkval

---

## 5.11 Framtidstrender 🚀

### Python 3.12+ features

**1. F-string förbättringar**
```python
# Python 3.12+
namn = "Anna"
ålder = 25

# Debug f-strings
print(f"{namn=}")  # namn='Anna'
print(f"{ålder=}")  # ålder=25

# Multi-line f-strings (bättre)
text = f"""
Namn: {namn}
Ålder: {ålder}
"""
```

**2. Bättre error-meddelanden**
```python
# Python 3.12 ger mer specifika felmeddelanden
d = {"nyckel": "värde"}
# print(d["felaktig_nyckel"])
# KeyError: 'felaktig_nyckel'. Did you mean: 'nyckel'?
```

**3. Performance-förbättringar**
- 10-60% snabbare än Python 3.11
- Bättre minneshantering

### Trender att följa 2024-2025

**1. AI/ML Integration**
- Större fokus på LLM-integration
- Python + OpenAI API
- Lokala ML-modeller

**2. Type safety**
- mypy blir standard
- Mer omfattande type hints
- Static analysis tools

**3. WebAssembly (WASM)**
- Python i browsern
- Pyscript
- Pyodide

**4. Edge Computing**
- Python på IoT-enheter
- MicroPython

---

## 🎯 Övningar för Nivå 5

### Övning 5.1: Async web scraper ⭐⭐⭐
Skapa ett async-program som hämtar titlar från flera webbsidor samtidigt.

<details>
<summary>💡 Lösningsförslag</summary>

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # pip install beautifulsoup4

async def hämta_titel(session, url):
    try:
        async with session.get(url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            titel = soup.find('title').text
            print(f"{url}: {titel}")
            return titel
    except Exception as e:
        print(f"Fel för {url}: {e}")
        return None

async def main():
    urls = [
        "https://python.org",
        "https://github.com",
        "https://stackoverflow.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [hämta_titel(session, url) for url in urls]
        titlar = await asyncio.gather(*tasks)
        return titlar

# asyncio.run(main())
```
</details>

### Övning 5.2: Dataclass för e-handel ⭐⭐
Skapa dataclasses för en e-handelsapplikation (Produkt, Varukorg, Order).

<details>
<summary>💡 Lösningsförslag</summary>

```python
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Produkt:
    namn: str
    pris: float
    lager: int

@dataclass
class VarukorgsRad:
    produkt: Produkt
    antal: int

    @property
    def totalpris(self) -> float:
        return self.produkt.pris * self.antal

@dataclass
class Varukorg:
    rader: List[VarukorgsRad] = field(default_factory=list)

    def lägg_till(self, produkt: Produkt, antal: int) -> None:
        self.rader.append(VarukorgsRad(produkt, antal))

    @property
    def totalt(self) -> float:
        return sum(rad.totalpris for rad in self.rader)

@dataclass
class Order:
    varukorg: Varukorg
    tidpunkt: datetime = field(default_factory=datetime.now)
    order_id: int = 0

# Test
p1 = Produkt("Python-bok", 399.0, 10)
p2 = Produkt("Musmatta", 89.0, 50)

korg = Varukorg()
korg.lägg_till(p1, 2)
korg.lägg_till(p2, 1)

print(f"Totalt: {korg.totalt} kr")

order = Order(korg, order_id=1001)
print(order)
```
</details>

### Övning 5.3: Pattern matching för JSON-parser ⭐⭐⭐
Använd pattern matching för att hantera olika JSON-strukturer.

<details>
<summary>💡 Lösningsförslag</summary>

```python
def hantera_api_response(response):
    match response:
        case {"status": "success", "data": data}:
            return f"✅ Lyckades: {data}"

        case {"status": "error", "message": msg, "code": code}:
            return f"❌ Fel {code}: {msg}"

        case {"status": "pending"}:
            return "⏳ Väntar..."

        case {"results": results} if len(results) > 0:
            return f"📊 {len(results)} resultat"

        case _:
            return "Okänd response-format"

# Test
print(hantera_api_response({"status": "success", "data": [1, 2, 3]}))
print(hantera_api_response({"status": "error", "message": "Inte funnen", "code": 404}))
print(hantera_api_response({"results": [1, 2, 3, 4, 5]}))
```
</details>

### Övning 5.4: Pytest för bankkonto ⭐⭐⭐
Skriv kompletta tester för Bankkonto-klassen från Nivå 4.

<details>
<summary>💡 Lösningsförslag</summary>

```python
# test_bankkonto.py
import pytest

class Bankkonto:
    def __init__(self, ägare, saldo=0):
        self.ägare = ägare
        self.saldo = saldo

    def sätt_in(self, belopp):
        if belopp <= 0:
            raise ValueError("Belopp måste vara positivt")
        self.saldo += belopp

    def ta_ut(self, belopp):
        if belopp <= 0:
            raise ValueError("Belopp måste vara positivt")
        if belopp > self.saldo:
            raise ValueError("Otillräckligt saldo")
        self.saldo -= belopp

@pytest.fixture
def konto():
    return Bankkonto("Anna", 1000)

def test_initial_saldo(konto):
    assert konto.saldo == 1000
    assert konto.ägare == "Anna"

def test_sätt_in(konto):
    konto.sätt_in(500)
    assert konto.saldo == 1500

def test_ta_ut(konto):
    konto.ta_ut(200)
    assert konto.saldo == 800

def test_sätt_in_negativt(konto):
    with pytest.raises(ValueError, match="positivt"):
        konto.sätt_in(-100)

def test_ta_ut_för_mycket(konto):
    with pytest.raises(ValueError, match="Otillräckligt"):
        konto.ta_ut(2000)

@pytest.mark.parametrize("belopp,förväntat_saldo", [
    (100, 1100),
    (500, 1500),
    (1000, 2000)
])
def test_sätt_in_parametriserat(konto, belopp, förväntat_saldo):
    konto.sätt_in(belopp)
    assert konto.saldo == förväntat_saldo
```
</details>

### Övning 5.5: Pandas dataanalys ⭐⭐⭐
Analysera en CSV-fil med försäljningsdata och hitta trender.

<details>
<summary>💡 Lösningsförslag</summary>

```python
import pandas as pd
import numpy as np

# Skapa exempel-data
np.random.seed(42)
data = {
    "Datum": pd.date_range("2024-01-01", periods=30, freq="D"),
    "Produkt": np.random.choice(["A", "B", "C"], 30),
    "Försäljning": np.random.randint(100, 1000, 30),
    "Kunder": np.random.randint(10, 100, 30)
}
df = pd.DataFrame(data)

# Spara till CSV
df.to_csv("försäljning.csv", index=False)

# Analysera
print("=== FÖRSÄLJNINGSANALYS ===\n")

# Total försäljning per produkt
per_produkt = df.groupby("Produkt")["Försäljning"].sum()
print("Total per produkt:")
print(per_produkt)
print()

# Bästa försäljningsdag
bästa_dag = df.loc[df["Försäljning"].idxmax()]
print(f"Bästa dag: {bästa_dag['Datum'].strftime('%Y-%m-%d')}")
print(f"Försäljning: {bästa_dag['Försäljning']}")
print()

# Genomsnitt per vecka
df["Vecka"] = df["Datum"].dt.isocalendar().week
per_vecka = df.groupby("Vecka")["Försäljning"].mean()
print("Genomsnitt per vecka:")
print(per_vecka)
```
</details>

### Övning 5.6: FastAPI CRUD-applikation ⭐⭐⭐⭐
Bygg ett komplett CRUD API för att hantera böcker.

<details>
<summary>💡 Lösningsförslag</summary>

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Bok(BaseModel):
    id: int
    titel: str
    författare: str
    år: int

# In-memory databas
böcker: List[Bok] = []
nästa_id = 1

@app.post("/böcker/", response_model=Bok)
def skapa_bok(bok: Bok):
    global nästa_id
    bok.id = nästa_id
    nästa_id += 1
    böcker.append(bok)
    return bok

@app.get("/böcker/", response_model=List[Bok])
def hämta_böcker():
    return böcker

@app.get("/böcker/{bok_id}", response_model=Bok)
def hämta_bok(bok_id: int):
    for bok in böcker:
        if bok.id == bok_id:
            return bok
    raise HTTPException(status_code=404, detail="Bok inte funnen")

@app.put("/böcker/{bok_id}", response_model=Bok)
def uppdatera_bok(bok_id: int, uppdaterad_bok: Bok):
    for index, bok in enumerate(böcker):
        if bok.id == bok_id:
            uppdaterad_bok.id = bok_id
            böcker[index] = uppdaterad_bok
            return uppdaterad_bok
    raise HTTPException(status_code=404, detail="Bok inte funnen")

@app.delete("/böcker/{bok_id}")
def radera_bok(bok_id: int):
    for index, bok in enumerate(böcker):
        if bok.id == bok_id:
            böcker.pop(index)
            return {"meddelande": "Bok raderad"}
    raise HTTPException(status_code=404, detail="Bok inte funnen")

# Kör med: uvicorn main:app --reload
```
</details>

---

## 🎓 Sammanfattning av Nivå 5

**Otroligt!** 🎉 Du har nu lärt dig cutting-edge Python:

✅ **Async/await**: Concurrent programming
✅ **Dataclasses**: Moderna klasser
✅ **Pattern matching**: Elegant kod (3.10+)
✅ **Virtual environments**: Isolerade projekt
✅ **Pytest**: Professionell testing
✅ **Pandas/NumPy**: Data science
✅ **FastAPI**: Moderna webb-API:er
✅ **Scikit-learn**: Machine learning
✅ **Git**: Version control
✅ **Case studies**: Verkliga applikationer

### Du är nu en avancerad Python-utvecklare! 🚀

Du kan:
- Bygga skalbara applikationer
- Analysera stora datamängder
- Skapa AI/ML-modeller
- Utveckla moderna webb-API:er
- Testa och underhålla professionell kod

---

**Fortsätt till:** [Praktiska projekt →](Python_Guide_06_Projekt.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
