# Nivå 3: Tekniska detaljer 🔧

[← Tillbaka: Nivå 2](./llm-agenter-niva2.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 4 →](./llm-agenter-niva4.md)

---

## Introduktion

Nu blir det på riktigt! I denna nivå lär du dig hur agenter faktiskt byggs, vilka komponenter de består av, och du kommer se riktiga kodexempel. Vi introducerar också olika typer av agent-arkitekturer och börjar arbeta med ramverk som LangChain.

**Vad ska du lära dig?**
- Agent-arkitektur (de 4 kärnkomponenterna)
- Olika agent-typer (ReAct, Plan-and-Execute, Conversational)
- Hur man bygger en enkel agent med kod
- Verktygsintegration (API:er, databaser)

**Förkunskaper:** Grundläggande programmering är bra men inte nödvändigt. Alla kodexempel förklaras steg för steg.

---

## Kärnkoncept

### 1. Agent-arkitektur - De 4 kärnkomponenterna

Alla LLM-agenter består av samma grundkomponenter:

```
┌─────────────────────────────────────────┐
│              AGENT                      │
│                                         │
│  ┌──────────┐      ┌───────────┐      │
│  │   LLM    │◄────►│  Memory   │      │
│  │ (Hjärna) │      │  (Minne)  │      │
│  └────┬─────┘      └───────────┘      │
│       │                                │
│       ▼                                │
│  ┌──────────┐      ┌───────────┐      │
│  │ Planner  │◄────►│   Tools   │      │
│  │ (Plan)   │      │ (Verktyg) │      │
│  └──────────┘      └───────────┘      │
└─────────────────────────────────────────┘
```

#### **Komponent 1: LLM (Brain)**
- **Funktion:** Förstår input, resonerar, fattar beslut
- **Exempel:** GPT-4, Claude, Gemini
- **Gör:** Läser din prompt, bestämmer vilka verktyg som behövs

#### **Komponent 2: Memory**
- **Funktion:** Lagrar kontext och historik
- **Typer:**
  - **Buffer Memory:** Senaste N meddelanden
  - **Summary Memory:** Sammanfattning av konversationen
  - **Vector Memory:** Semantisk sökning i tidigare interaktioner

#### **Komponent 3: Planner**
- **Funktion:** Bryter ner uppgifter i steg
- **Strategier:**
  - **ReAct:** Reason (tänk) → Act (agera) → Observe (observera)
  - **Plan-and-Execute:** Planera först, exekvera sen
  - **Reflexion:** Gör → Utvärdera → Förbättra

#### **Komponent 4: Tools**
- **Funktion:** Utför faktiska åtgärder
- **Exempel:**
  - Search API (Tavily, SerpAPI)
  - Database (SQL, Vector DB)
  - Code execution (Python REPL)
  - External APIs (Weather, Calendar, Email)

---

### 2. Agent-typer och när de används

#### **ReAct Agent** (Reasoning + Acting)

Mest använd typ. Växlar mellan "tänka" och "agera".

**Process:**
```
1. Thought: "Jag behöver veta vädret i Stockholm"
2. Action: Använd Weather API
3. Observation: "15°C, soligt"
4. Thought: "Nu kan jag svara användaren"
5. Final Answer: "Det är 15°C och soligt i Stockholm"
```

**Bäst för:**
- Uppgifter som kräver flera steg
- När du inte vet exakt hur många steg som behövs

**LangChain-exempel:**
```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool

# Definiera verktyg
def get_weather(location: str) -> str:
    """Hämtar väderdata för en plats"""
    # I verkligheten: API-anrop
    return f"Vädret i {location}: 15°C, soligt"

tools = [
    Tool(
        name="Weather",
        func=get_weather,
        description="Hämta väderinformation för en plats"
    )
]

# Skapa agent
llm = ChatOpenAI(model="gpt-4")
agent = create_react_agent(llm, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Kör agent
response = agent_executor.invoke({
    "input": "Hur är vädret i Stockholm?"
})
```

#### **Plan-and-Execute Agent**

Planerar ALLA steg först, exekverar sedan.

**Process:**
```
1. Plan:
   - Steg 1: Hämta vädret för Stockholm
   - Steg 2: Hämta vädret för Oslo
   - Steg 3: Jämför temperaturerna
2. Execute:
   - Kör steg 1 ✓
   - Kör steg 2 ✓
   - Kör steg 3 ✓
3. Return: "Stockholm är 2°C varmare än Oslo"
```

**Bäst för:**
- Komplexa uppgifter där du vet strukturen
- Uppgifter som kräver flera API-anrop
- När du vill optimera antal LLM-anrop (billigare!)

**LangChain-exempel:**
```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Plan-prompt
plan_prompt = PromptTemplate(
    input_variables=["task"],
    template="""
    Bryt ner denna uppgift i specifika steg:
    Uppgift: {task}

    Returnera en numrerad lista:
    """
)

# Skapa planner
planner = LLMChain(llm=llm, prompt=plan_prompt)

# Generera plan
plan = planner.run("Jämför vädret i Stockholm och Oslo")
# Output: "1. Hämta väder Stockholm\n2. Hämta väder Oslo\n3. Jämför..."

# Exekvera varje steg...
```

#### **Conversational Agent**

Fokuserar på dialog och kontext över tid.

**Kännetecken:**
- Starkt minne av tidigare konversationer
- Personalisering baserat på användarhistorik
- Naturlig turtagning

**Bäst för:**
- Kundtjänst
- Personliga assistenter
- Pedagogiska chatbots

---

### 3. Verktygsintegration - Tools i praktiken

#### Skapa ditt eget verktyg

**Exempel 1: Enkel kalkylator**
```python
from langchain.tools import tool

@tool
def calculate(expression: str) -> str:
    """
    Beräknar matematiska uttryck.
    Input: Ett matematiskt uttryck som sträng (t.ex. "2 + 2")
    Output: Resultatet
    """
    try:
        result = eval(expression)  # OBS: Använd aldrig eval() i produktion!
        return f"Resultat: {result}"
    except Exception as e:
        return f"Fel: {e}"

# Använd i agent
tools = [calculate]
```

**Exempel 2: Web scraping**
```python
import requests
from bs4 import BeautifulSoup

@tool
def scrape_title(url: str) -> str:
    """Hämtar titeln från en webbsida"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text
        return f"Titel: {title}"
    except Exception as e:
        return f"Kunde inte hämta titel: {e}"
```

**Exempel 3: Databas-query**
```python
import sqlite3

@tool
def search_customers(name: str) -> str:
    """Söker kunder i databasen baserat på namn"""
    conn = sqlite3.connect('customers.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM customers WHERE name LIKE ?",
        (f"%{name}%",)
    )
    results = cursor.fetchall()
    conn.close()

    if results:
        return f"Hittade {len(results)} kunder: {results}"
    return "Inga kunder hittade"
```

---

### 4. Memory-system

#### Buffer Memory (Enklast)
Kommer ihåg de senaste N meddelandena.

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

# Spara konversation
memory.save_context(
    {"input": "Hej, jag heter Anna"},
    {"output": "Hej Anna! Hur kan jag hjälpa dig?"}
)

# Hämta historik
print(memory.load_memory_variables({}))
# Output: {'history': 'Human: Hej, jag heter Anna\nAI: Hej Anna!...'}
```

#### Summary Memory (Skalbar)
Sammanfattar gamla meddelanden för att spara tokens.

```python
from langchain.memory import ConversationSummaryMemory

summary_memory = ConversationSummaryMemory(llm=llm)

# Efter lång konversation:
# Senaste 3 meddelanden: Fullt innehåll
# Äldre meddelanden: "Användaren presenterade sig som Anna och frågade om..."
```

#### Vector Memory (Avancerat)
Lagrar i vektordatabas, hämtar semantiskt relaterat innehåll.

```python
from langchain.memory import VectorStoreRetrieverMemory
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# Skapa vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts([], embeddings)

# Memory med semantisk sökning
vector_memory = VectorStoreRetrieverMemory(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
)

# När användaren pratar om "hund" hämtas också minnen om "valp", "djur"
```

---

## Konkreta Exempel

### Exempel 1: FAQ-bot med memory

**Use case:** Kundtjänst som kommer ihåg vad kunden sagt.

```python
from langchain.agents import create_react_agent
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# Verktyg: FAQ-databas
faq_data = {
    "öppettider": "Vi har öppet 09-17 vardagar",
    "frakt": "Frakt kostar 49 kr, fri frakt över 500 kr",
    "retur": "30 dagars returrätt"
}

@tool
def search_faq(query: str) -> str:
    """Söker i FAQ-databasen"""
    query_lower = query.lower()
    for key, value in faq_data.items():
        if key in query_lower:
            return value
    return "Tyvärr hittade jag ingen information om detta."

# Skapa agent med minne
memory = ConversationBufferWindowMemory(
    k=5,  # Kom ihåg senaste 5 interaktionerna
    return_messages=True
)

llm = ChatOpenAI(model="gpt-4")
tools = [search_faq]

# Agent executor
from langchain.agents import AgentExecutor
agent = create_react_agent(llm, tools)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)

# Konversation
response1 = agent_executor.invoke({"input": "Vilka är era öppettider?"})
# Output: "Vi har öppet 09-17 vardagar"

response2 = agent_executor.invoke({"input": "Och vad kostar frakt?"})
# Output: "Frakt kostar 49 kr, fri frakt över 500 kr"

response3 = agent_executor.invoke({
    "input": "Tack! Sammanfatta vad vi pratat om"
})
# Output: "Vi har diskuterat våra öppettider (09-17 vardagar)
#          och fraktkostnader (49 kr, fri över 500 kr)."
```

---

### Exempel 2: Research-agent med web scraping

**Use case:** Samla information från flera källor.

```python
from langchain.tools import tool
import requests

@tool
def web_search(query: str) -> str:
    """Söker på webben (förenklad)"""
    # I verkligheten: Använd Tavily, SerpAPI, etc.
    return f"Sökresultat för '{query}': [Top 3 resultat...]"

@tool
def fetch_webpage(url: str) -> str:
    """Hämtar innehåll från en URL"""
    try:
        response = requests.get(url, timeout=5)
        # Förenkl ad - skulle använda BeautifulSoup för riktigt scraping
        return response.text[:500]  # Första 500 tecken
    except:
        return "Kunde inte hämta sidan"

@tool
def summarize_text(text: str) -> str:
    """Sammanfattar text"""
    llm = ChatOpenAI()
    prompt = f"Sammanfatta detta på 2-3 meningar:\n\n{text}"
    return llm.predict(prompt)

# Skapa research agent
tools = [web_search, fetch_webpage, summarize_text]
agent = create_react_agent(llm, tools)

# Använd
result = agent_executor.invoke({
    "input": "Hitta 3 artiklar om AI-agenter och sammanfatta huvudpunkterna"
})

# Agent kommer:
# 1. Söka på webben
# 2. Hämta de 3 bästa artiklarna
# 3. Sammanfatta varje artikel
# 4. Presentera resultatet
```

---

## 💡 Pro Tips

### Tip 1: Begränsa agent-loopar
Agenter kan hamna i oändliga loopar. Sätt alltid max iterations:

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,  # Stoppa efter 5 steg
    max_execution_time=30,  # Eller 30 sekunder
    early_stopping_method="generate"
)
```

### Tip 2: Använd `verbose=True` vid utveckling
Se exakt vad agenten tänker:

```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True  # Skriv ut varje steg
)

# Output:
# > Entering new AgentExecutor chain...
# Thought: Jag behöver använda Weather-verktyget
# Action: Weather
# Action Input: Stockholm
# Observation: 15°C, soligt
# ...
```

### Tip 3: Tool descriptions är KRITISKA
LLM:en väljer verktyg baserat på beskrivningen:

```python
# Dålig beskrivning
@tool
def my_tool(x: str) -> str:
    """Gör något"""  # Vad??
    return x

# Bra beskrivning
@tool
def search_products(product_name: str) -> str:
    """
    Söker efter produkter i databasen.

    Input: Produktnamn eller del av namn (t.ex. "iPhone")
    Output: Lista med matchande produkter inkl. pris och lagerstatus

    Exempel:
    Input: "iPhone"
    Output: "iPhone 15: 12 990 kr (5 i lager), iPhone 14: 9 990 kr (12 i lager)"
    """
    # Implementation...
```

---

## ✏️ Övningar

### Övning 3.1: Identifiera agent-typ 🔍

**Svårighetsgrad**: ⭐⭐
**Tid**: ~10 minuter

**Uppgift:**
Vilken agent-typ (ReAct, Plan-and-Execute, eller Conversational) är bäst för dessa scenarier?

1. "Boka flyg + hotell + hyrbil för en resa till Barcelona"
2. "Chatta med kunder som har frågor om produkter"
3. "Hitta den senaste nyheten om AI och sammanfatta"
4. "Skapa en komplett marknadsföringsplan med budget, timeline och innehåll"

<details>
<summary>💡 Lösning</summary>

1. **Plan-and-Execute**
   - Anledning: Du vet exakt vilka steg (flyg → hotell → bil), kan planeras i förväg
   - Fördel: Billigare (färre LLM-anrop), kan optimera priserna mot varandra

2. **Conversational**
   - Anledning: Dialog-fokuserat, behöver komma ihåg vad kunden sagt tidigare
   - Fördel: Personlig, kan följa upp tidigare frågor

3. **ReAct**
   - Anledning: Okänt hur många steg, kanske behöver söka flera gånger
   - Fördel: Flexibel, kan anpassa baserat på vad som hittas

4. **Plan-and-Execute**
   - Anledning: Stor uppgift med tydlig struktur
   - Fördel: Systematisk, inget glöms bort

</details>

---

### Övning 3.2: Skapa ditt första verktyg 🔧

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Skriv en Python-funktion som kan användas som ett verktyg. Välj ett av dessa:

A) `get_random_fact()` - Returnerar ett random roligt faktum
B) `convert_currency(amount, from_currency, to_currency)` - Konverterar valutor
C) `check_password_strength(password)` - Kollar om lösenord är starkt

**Krav:**
- Använd `@tool` decorator
- Skriv en BRA beskrivning (se Pro Tip 3)
- Hantera fel (try/except)

**Starter code:**
```python
from langchain.tools import tool

@tool
def my_tool(param: str) -> str:
    """
    [DIN BESKRIVNING HÄR]
    """
    # Din kod här
    pass
```

<details>
<summary>💡 Lösning A: Random Fact</summary>

```python
from langchain.tools import tool
import random

@tool
def get_random_fact(category: str = "general") -> str:
    """
    Returnerar ett slumpmässigt roligt faktum.

    Input: Kategori ("general", "animals", "space", "history")
    Output: Ett roligt faktum som sträng

    Exempel:
    Input: "animals"
    Output: "En bläckfisk har tre hjärtan!"
    """
    facts = {
        "general": [
            "En dag på Venus är längre än ett år på Venus!",
            "Honung förstörs aldrig - man har hittat ätbar honung i 3000 år gamla egyptiska gravar",
        ],
        "animals": [
            "En bläckfisk har tre hjärtan!",
            "Delfiner sover med ena hjärnhalvan i taget",
        ],
        "space": [
            "Det finns fler stjärnor i universum än sandkorn på jorden",
            "En tesked av en neutronstjärna väger 6 miljarder ton",
        ],
        "history": [
            "Kleopatra levde närmare iPhone än pyramiderna",
            "Oxford-universitetet är äldre än Aztekerna",
        ]
    }

    try:
        if category not in facts:
            category = "general"
        return random.choice(facts[category])
    except Exception as e:
        return f"Kunde inte hämta faktum: {e}"

# Test
print(get_random_fact.run("animals"))
```

</details>

<details>
<summary>💡 Lösning B: Currency Converter</summary>

```python
from langchain.tools import tool

@tool
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Konverterar mellan valutor.

    Input:
    - amount: Summa att konvertera (nummer)
    - from_currency: Från-valuta (SEK, USD, EUR, GBP)
    - to_currency: Till-valuta (SEK, USD, EUR, GBP)

    Output: Konverterat belopp med valuta

    Exempel:
    Input: amount=100, from_currency="SEK", to_currency="EUR"
    Output: "100 SEK = 8.85 EUR"
    """

    # Förenklad växelkurstabell (i verkligheten: använd API)
    rates = {
        ("SEK", "EUR"): 0.0885,
        ("SEK", "USD"): 0.096,
        ("SEK", "GBP"): 0.077,
        ("EUR", "SEK"): 11.30,
        ("USD", "SEK"): 10.42,
        ("GBP", "SEK"): 12.99,
        ("EUR", "USD"): 1.08,
        ("USD", "EUR"): 0.93,
    }

    try:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == to_currency:
            return f"{amount} {from_currency} = {amount} {to_currency}"

        key = (from_currency, to_currency)
        if key not in rates:
            return f"Växelkurs för {from_currency} → {to_currency} inte tillgänglig"

        converted = round(amount * rates[key], 2)
        return f"{amount} {from_currency} = {converted} {to_currency}"

    except Exception as e:
        return f"Fel vid konvertering: {e}"

# Test
print(convert_currency.run({"amount": 100, "from_currency": "SEK", "to_currency": "EUR"}))
```

</details>

<details>
<summary>💡 Lösning C: Password Strength</summary>

```python
from langchain.tools import tool
import re

@tool
def check_password_strength(password: str) -> str:
    """
    Kontrollerar styrkan på ett lösenord.

    Input: Ett lösenord som sträng
    Output: Bedömning (Svagt/Medel/Starkt) + rekommendationer

    Kriterier:
    - Längd >= 12 tecken
    - Innehåller stora och små bokstäver
    - Innehåller siffror
    - Innehåller specialtecken

    Exempel:
    Input: "password123"
    Output: "Svagt lösenord. Rekommendationer: Lägg till stora bokstäver, specialtecken. Öka längden till minst 12 tecken."
    """

    try:
        score = 0
        feedback = []

        # Kolla längd
        if len(password) >= 12:
            score += 1
        else:
            feedback.append(f"Öka längden till minst 12 tecken (nu: {len(password)})")

        # Stora bokstäver
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Lägg till stora bokstäver")

        # Små bokstäver
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Lägg till små bokstäver")

        # Siffror
        if re.search(r'\d', password):
            score += 1
        else:
            feedback.append("Lägg till siffror")

        # Specialtecken
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1
        else:
            feedback.append("Lägg till specialtecken (!@#$...)")

        # Bedömning
        if score >= 5:
            strength = "Starkt"
        elif score >= 3:
            strength = "Medel"
        else:
            strength = "Svagt"

        result = f"{strength} lösenord (Poäng: {score}/5)"
        if feedback:
            result += f"\n\nRekommendationer:\n- " + "\n- ".join(feedback)

        return result

    except Exception as e:
        return f"Fel vid kontroll: {e}"

# Test
print(check_password_strength.run("password123"))
print(check_password_strength.run("MyP@ssw0rd2024!"))
```

</details>

---

### Övning 3.3: Bygg en enkel ReAct-agent 🤖

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~20 minuter
**Verktyg**: LangChain

**Uppgift:**
Skapa en agent som kan:
1. Berätta vad klockan är
2. Kasta en tärning (1-6)
3. Komma ihåg användarens namn

**Starter code:**
```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.memory import ConversationBufferMemory
from datetime import datetime
import random

# TODO: Skapa dina 3 verktyg här

# TODO: Skapa agent med memory

# TODO: Testa agenten
```

<details>
<summary>💡 Lösning</summary>

```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from datetime import datetime
import random

# Verktyg 1: Klocka
@tool
def get_current_time() -> str:
    """
    Returnerar nuvarande tid och datum.
    Använd detta när användaren frågar efter tid eller datum.
    """
    now = datetime.now()
    return now.strftime("Det är %H:%M den %Y-%m-%d")

# Verktyg 2: Tärningskast
@tool
def roll_dice(num_dice: int = 1) -> str:
    """
    Kastar tärningar.

    Input: Antal tärningar att kasta (1-10)
    Output: Resultaten

    Exempel: Input: 2 → Output: "Du kastade 2 tärningar: [4, 6]. Totalt: 10"
    """
    if num_dice < 1 or num_dice > 10:
        return "Kan bara kasta 1-10 tärningar"

    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    total = sum(rolls)
    return f"Du kastade {num_dice} tärning(ar): {rolls}. Totalt: {total}"

# Verktyg 3: Spara namn
user_data = {}  # Enkel "databas"

@tool
def save_user_name(name: str) -> str:
    """
    Sparar användarens namn.

    Input: Användarens namn
    Output: Bekräftelse
    """
    user_data['name'] = name
    return f"Jag har sparat att du heter {name}!"

@tool
def get_user_name() -> str:
    """
    Hämtar användarens sparade namn.

    Output: Användarens namn eller meddelande om inget namn sparats
    """
    if 'name' in user_data:
        return f"Du heter {user_data['name']}"
    return "Jag vet inte vad du heter än. Berätta för mig!"

# Skapa agent
llm = ChatOpenAI(model="gpt-4", temperature=0)
tools = [get_current_time, roll_dice, save_user_name, get_user_name]

# Memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Prompt template
template = '''Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

# Skapa agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=5
)

# Testa!
print("=== Test 1: Klockan ===")
response = agent_executor.invoke({"input": "Vad är klockan?"})
print(response['output'])

print("\n=== Test 2: Tärning ===")
response = agent_executor.invoke({"input": "Kasta 2 tärningar"})
print(response['output'])

print("\n=== Test 3: Spara namn ===")
response = agent_executor.invoke({"input": "Mitt namn är Anna"})
print(response['output'])

print("\n=== Test 4: Kom ihåg namn ===")
response = agent_executor.invoke({"input": "Vad heter jag?"})
print(response['output'])
```

**Förväntad output:**
```
> Entering new AgentExecutor chain...
Thought: Användaren vill veta vad klockan är
Action: get_current_time
Action Input:
Observation: Det är 14:32 den 2025-01-17
Thought: Nu kan jag svara
Final Answer: Klockan är 14:32

> Finished chain.
```

</details>

---

### Övning 3.4: Memory-experiment 💭

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Jämför `ConversationBufferMemory` (kom ihåg allt) vs `ConversationBufferWindowMemory` (kom bara ihåg senaste N).

Skriv kod som:
1. Skapar två identiska agenter, en med varje memory-typ
2. Har samma konversation med båda (minst 5 meddelanden)
3. Testar om de kommer ihåg något från början

**Tips:** Använd `k=2` för WindowMemory (kom bara ihåg senaste 2)

<details>
<summary>💡 Lösning</summary>

```python
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory

# Agent 1: Buffer (kommer ihåg allt)
memory_full = ConversationBufferMemory()

# Agent 2: Window (bara senaste 2)
memory_window = ConversationBufferWindowMemory(k=2)

# Simulera konversation
messages = [
    ("Jag heter Lisa", "Trevligt att träffas, Lisa!"),
    ("Jag är 15 år", "Okej, Lisa, 15 år!"),
    ("Jag gillar fotboll", "Kul att du gillar fotboll!"),
    ("Jag bor i Stockholm", "Stockholm är en fin stad!"),
    ("Vad vet du om mig?", "...")
]

# Spara i båda memories
for user_msg, ai_msg in messages[:-1]:  # Alla utom sista
    memory_full.save_context({"input": user_msg}, {"output": ai_msg})
    memory_window.save_context({"input": user_msg}, {"output": ai_msg})

# Jämför vad de kommer ihåg
print("=== BUFFER MEMORY (kommer ihåg allt) ===")
print(memory_full.load_memory_variables({}))

print("\n=== WINDOW MEMORY (k=2, bara senaste 2) ===")
print(memory_window.load_memory_variables({}))

# Output visar:
# Buffer: Minns namn, ålder, fotboll, Stockholm
# Window: Minns bara fotboll och Stockholm (senaste 2)
```

**Analys:**
- **Buffer**: Bra för korta sessioner, personliga assistenter
- **Window**: Bra för långa konversationer, sparar tokens (= billigare)

</details>

---

### Övning 3.5: Debugging - Hitta felet 🐛

**Svårighetsgrad**: ⭐⭐⭐
**Tid**: ~15 minuter

**Uppgift:**
Denna kod fungerar inte. Hitta och fixa felen!

```python
from langchain.tools import tool
from langchain.agents import create_react_agent

@tool
def add_numbers(a, b):
    """Lägger ihop två nummer"""
    return a + b

tools = [add_numbers]

agent = create_react_agent(llm, tools)
response = agent.invoke("Vad är 5 + 3?")
print(response)
```

**Hint:** Det finns 3 fel!

<details>
<summary>💡 Lösning</summary>

**Fel 1: Missing type hints**
```python
# Fel:
def add_numbers(a, b):

# Rätt:
def add_numbers(a: int, b: int) -> int:
```
LangChain-verktyg behöver type hints för att förstå input/output.

**Fel 2: Dålig description**
```python
# Fel:
"""Lägger ihop två nummer"""

# Rätt:
"""
Lägger ihop två nummer.

Input: a (int) - Första numret
Input: b (int) - Andra numret
Output: Summan av a och b

Exempel: a=5, b=3 → Output: 8
"""
```

**Fel 3: Glömde AgentExecutor**
```python
# Fel:
agent = create_react_agent(llm, tools)
response = agent.invoke("Vad är 5 + 3?")

# Rätt:
from langchain.agents import AgentExecutor

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
response = agent_executor.invoke({"input": "Vad är 5 + 3?"})
```

**Komplett fungerande kod:**
```python
from langchain.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

@tool
def add_numbers(a: int, b: int) -> int:
    """
    Lägger ihop två nummer.

    Input: a (int) - Första numret
    Input: b (int) - Andra numret
    Output: Summan av a och b

    Exempel: a=5, b=3 → Output: 8
    """
    return a + b

llm = ChatOpenAI(model="gpt-4")
tools = [add_numbers]

# Prompt (förenklad)
prompt = PromptTemplate.from_template("""
Answer: {input}
Use tools: {tools}
{agent_scratchpad}
""")

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

response = agent_executor.invoke({"input": "Vad är 5 + 3?"})
print(response['output'])  # "8"
```

</details>

---

### Övning 3.6: No-code alternativ med n8n 🎨

**Svårighetsgrad**: ⭐⭐
**Tid**: ~20 minuter
**Verktyg**: n8n (gratis demo på n8n.io/demo)

**Uppgift:**
Skapa samma FAQ-bot som i exempel 1, men utan kod!

**Steg:**
1. Gå till n8n.io och testa deras demo
2. Skapa ett workflow:
   - Trigger: Webhook (tar emot frågor)
   - Node 1: AI Agent (OpenAI)
   - Node 2: HTTP Request (till din FAQ-databas)
   - Node 3: Return response

**Dokumentation:** https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/

*(Denna övning är praktisk - testa själv!)*

---

### Övning 3.7: Arkitektur-design 📐

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~20 minuter

**Uppgift:**
Designa agent-arkitekturen för: **"En resebokningsagent som kan söka flyg, hotell, och skapa en reseplan"**

Rita (eller beskriv) ett diagram som visar:
- Vilka komponenter behövs (LLM, Memory, Planner, Tools)
- Vilka verktyg specifikt (t.ex. "Flight Search API")
- Vilket typ av agent (ReAct/Plan-and-Execute/Conversational)
- Vilket memory-system
- Vilken chain/workflow

<details>
<summary>💡 Lösning</summary>

```
┌─────────────────────────────────────────────────────────┐
│         RESEBOKNINGS-AGENT                              │
│         (Plan-and-Execute typ)                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐         ┌──────────────┐            │
│  │     LLM      │◄───────►│   Memory     │            │
│  │  (GPT-4)     │         │  (Summary)   │            │
│  │              │         │              │            │
│  └──────┬───────┘         └──────────────┘            │
│         │                                               │
│         ▼                                               │
│  ┌──────────────┐                                      │
│  │   PLANNER    │                                      │
│  │              │                                      │
│  │ Skapar plan: │                                      │
│  │ 1. Sök flyg  │                                      │
│  │ 2. Sök hotell│                                      │
│  │ 3. Jämför    │                                      │
│  │ 4. Boka      │                                      │
│  └──────┬───────┘                                      │
│         │                                               │
│         ▼                                               │
│  ┌─────────────────────────────────────┐              │
│  │          TOOLS                       │              │
│  ├─────────────────────────────────────┤              │
│  │ 1. Flight Search API (Skyscanner)   │              │
│  │ 2. Hotel Search API (Booking.com)   │              │
│  │ 3. Price Comparison Tool            │              │
│  │ 4. Calendar Integration             │              │
│  │ 5. Payment API (Stripe)             │              │
│  │ 6. PDF Generator (reseplan)         │              │
│  └─────────────────────────────────────┘              │
└─────────────────────────────────────────────────────────┘

WORKFLOW:
┌─────────────────────────────────────────────────────┐
│ 1. User Input                                       │
│    "Jag vill åka till Barcelona 15-22 juli"        │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 2. PLANNER skapar steg:                            │
│    Step 1: Search flights Stockholm→Barcelona      │
│    Step 2: Search hotels in Barcelona              │
│    Step 3: Compare prices                          │
│    Step 4: Present top 3 options                   │
│    Step 5: Wait for user choice                    │
│    Step 6: Book selected option                    │
│    Step 7: Generate itinerary PDF                  │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 3. EXECUTOR kör varje steg:                        │
│                                                     │
│    [Step 1] Call Flight Search API                 │
│             → 15 results                           │
│                                                     │
│    [Step 2] Call Hotel Search API                  │
│             → 30 results                           │
│                                                     │
│    [Step 3] Use Price Comparison Tool              │
│             → Rank by price + rating               │
│                                                     │
│    [Step 4] LLM summarizes top 3                   │
│                                                     │
│    [Step 5] Present to user                        │
│             User picks Option 2                     │
│                                                     │
│    [Step 6] Call Payment API                       │
│             Call Booking APIs                      │
│                                                     │
│    [Step 7] Generate PDF with full itinerary       │
└────────────────┬────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────┐
│ 4. Output                                          │
│    "Bokat! Din resa 15-22 juli Barcelona.         │
│     Flyg: 09:00 ARN→BCN, Return 18:00             │
│     Hotell: Hotel Arts (4★)                        │
│     Total: 8,500 SEK                               │
│     Se bifogad reseplan (PDF)"                     │
└─────────────────────────────────────────────────────┘
```

**Val av komponenter - Motivering:**

**Agent-typ: Plan-and-Execute**
- Varför: Uppgiften har tydlig struktur (sök → jämför → boka)
- Fördel: Kan planera optimalt (t.ex. söka flyg och hotell parallellt)

**Memory: Summary Memory**
- Varför: Konversationen kan bli lång ("Jag vill ändra datum", etc.)
- Fördel: Håller koll på preferenser utan att använda för många tokens

**Tools:**
1. **Flight Search** - Nödvändig för flygbiljetter
2. **Hotel Search** - Nödvändig för boende
3. **Price Comparison** - Optimerar kostnad
4. **Calendar** - Kollar användarens schema
5. **Payment** - För att faktiskt boka
6. **PDF Generator** - Skapar reseplan

**Potential extensions:**
- Weather API (packlista baserat på väder)
- Restaurant recommendations
- Activity suggestions
- Travel insurance quotes

</details>

---

## 🚀 Projekt

### Projekt 3.1: FAQ-bot med långtidsminne

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~45 minuter
**Mål**: Bygg en kundtjänst-bot som kommer ihåg användare mellan sessioner

**Specifikation:**
- Verktyg 1: Sök i FAQ-databas (minst 10 frågor/svar)
- Verktyg 2: Spara kundinfo (namn, email, tidigare ärenden)
- Verktyg 3: Eskalera till människa (om för komplext)
- Memory: Spara till JSON-fil mellan sessioner
- Bonus: Använd sentiment analysis för att upptäcka frustrerade kunder

**Starter template:**
```python
# faq_bot.py
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
import json

# FAQ database
faq_db = {
    "öppettider": "Vi har öppet 09-17 vardagar",
    # ... lägg till 9 till
}

@tool
def search_faq(query: str) -> str:
    """Söker i FAQ"""
    # Din implementation
    pass

@tool
def save_customer_data(name: str, email: str, issue: str) -> str:
    """Sparar kunddata till JSON"""
    # Din implementation
    pass

@tool
def escalate_to_human(reason: str) -> str:
    """Eskalerar till mänsklig support"""
    return f"Ärendet eskalerat: {reason}. En medarbetare kontaktar dig inom 1 timme."

# TODO: Skapa agent
# TODO: Spara/ladda memory från fil
# TODO: CLI-loop för konversation
```

<details>
<summary>💡 Lösningsförslag</summary>

```python
# faq_bot.py
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import json
import os

# FAQ database
faq_db = {
    "öppettider": "Vi har öppet 09-17 vardagar, stängt helger",
    "frakt": "Frakt kostar 49 kr, fri frakt över 500 kr",
    "retur": "30 dagars öppet köp, returnera kostnadsfritt",
    "betalning": "Vi tar emot kort, Swish och Klarna",
    "leverans": "Leverans inom 2-5 arbetsdagar",
    "garanti": "2 års garanti på alla produkter",
    "kontakt": "Email: info@exempel.se, Tel: 08-123 456",
    "spårning": "Du får spårningsnummer via email när paketet skickas",
    "storleksguide": "Se vår storleksguide på produktsidan",
    "miljö": "Vi använder 100% återvunna förpackningar"
}

# Customer database file
CUSTOMER_DB = "customers.json"

def load_customers():
    if os.path.exists(CUSTOMER_DB):
        with open(CUSTOMER_DB, 'r') as f:
            return json.load(f)
    return {}

def save_customers(customers):
    with open(CUSTOMER_DB, 'w') as f:
        json.dump(customers, f, indent=2)

customers = load_customers()

@tool
def search_faq(query: str) -> str:
    """
    Söker i FAQ-databasen.

    Input: Fråga eller sökord (t.ex. "öppettider", "frakt")
    Output: Svar från FAQ eller meddelande om inget hittas
    """
    query_lower = query.lower()

    # Sök efter matchande nyckelord
    for key, value in faq_db.items():
        if key in query_lower or query_lower in key:
            return f"FAQ: {value}"

    return "Tyvärr hittade jag inget svar på det i vår FAQ. Vill du att jag eskalerar till en medarbetare?"

@tool
def save_customer_data(name: str, email: str = "", issue: str = "") -> str:
    """
    Sparar eller uppdaterar kunddata.

    Input:
    - name: Kundens namn
    - email: Email (optional)
    - issue: Beskrivning av ärendet (optional)

    Output: Bekräftelse
    """
    if name not in customers:
        customers[name] = {
            "email": email,
            "issues": []
        }
    else:
        if email:
            customers[name]["email"] = email

    if issue:
        customers[name]["issues"].append(issue)

    save_customers(customers)

    return f"Tack {name}! Jag har sparat din information."

@tool
def get_customer_history(name: str) -> str:
    """
    Hämtar tidigare ärenden för en kund.

    Input: Kundens namn
    Output: Historik eller meddelande om ny kund
    """
    if name in customers:
        issues = customers[name].get("issues", [])
        if issues:
            return f"Tidigare ärenden för {name}:\n- " + "\n- ".join(issues)
        return f"Välkommen tillbaka {name}! Jag ser inga tidigare ärenden."

    return f"Välkommen {name}! Jag ser att du är ny här."

@tool
def escalate_to_human(reason: str) -> str:
    """
    Eskalerar ärendet till mänsklig support.

    Input: Anledning till eskalering
    Output: Bekräftelse
    """
    return f"""
Ärendet har eskalerats till vår support-team.

Anledning: {reason}

En medarbetare kommer att kontakta dig inom 1 timme under kontorstid (09-17).
För brådskande ärenden, ring 08-123 456.
    """.strip()

# Setup agent
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
tools = [search_faq, save_customer_data, get_customer_history, escalate_to_human]

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

template = '''Du är en hjälpsam kundtjänstassistent. Var vänlig och professionell.

Om kunden verkar frustrerad eller arg, var extra empatisk.
Om du inte kan hjälpa, eskalera till mänsklig support.

Du har tillgång till dessa verktyg:
{tools}

Använd detta format:

Question: {input}
Thought: [dina tankar]
Action: [verktyg att använda]
Action Input: [input till verktyget]
Observation: [resultat]
... (upprepa vid behov)
Thought: Nu kan jag svara
Final Answer: [ditt svar till kunden]

Begin!

Question: {input}
{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)

# CLI Interface
def main():
    print("=" * 50)
    print("   KUNDTJÄNST-BOT")
    print("   Skriv 'exit' för att avsluta")
    print("=" * 50)

    while True:
        user_input = input("\nDu: ").strip()

        if user_input.lower() in ['exit', 'quit', 'avsluta']:
            print("Tack för att du kontaktade oss! Hej då!")
            break

        if not user_input:
            continue

        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"\nBot: {response['output']}")
        except Exception as e:
            print(f"\nBot: Ursäkta, något gick fel. Låt mig eskalera detta till vår support.")
            print(f"(Fel: {e})")

if __name__ == "__main__":
    main()
```

**Test scenarios:**
```
Du: Hej, vad har ni för öppettider?
Bot: Vi har öppet 09-17 vardagar, stängt helger

Du: Mitt namn är Anna Andersson
Bot: Tack Anna! Jag har sparat din information.

Du: Jag beställde för 3 veckor sedan och inget har hänt!
Bot: [Känner av frustration] Jag förstår att detta är frustrerande, Anna...
     [Eskalerar förmodligen]

Du: exit
```

</details>

---

### Projekt 3.2: Research-assistent med webbsökning

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~60 minuter
**Mål**: Agent som kan söka på webben, läsa artiklar, och sammanfatta

**Specifikation:**
- Verktyg 1: Web search (använd Tavily API eller SerpAPI)
- Verktyg 2: Fetch webpage (BeautifulSoup)
- Verktyg 3: Summarize (LLM chain)
- Verktyg 4: Save to file (markdown output)
- Output: Researc rapport med källor

**Bonus:**
- Validera källor (kolla att de är trovärdiga)
- Citera specifika delar
- Skapa innehållsförteckning

**Starter template:**
```python
# research_agent.py
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def web_search(query: str, num_results: int = 5) -> str:
    """Söker på webben"""
    # TODO: Implementera (använd Tavily eller DuckDuckGo)
    pass

@tool
def fetch_webpage(url: str) -> str:
    """Hämtar innehåll från URL"""
    # TODO: Implementera med requests + BeautifulSoup
    pass

@tool
def summarize_text(text: str, max_words: int = 200) -> str:
    """Sammanfattar text"""
    # TODO: Använd LLM
    pass

@tool
def save_report(content: str, filename: str = "research_report.md") -> str:
    """Sparar rapport till fil"""
    # TODO: Skriv till markdown-fil
    pass

# TODO: Bygg Plan-and-Execute agent
# TODO: CLI för att ta emot research-frågor
```

<details>
<summary>💡 Lösningsförslag (förenklad utan externa API:er)</summary>

```python
# research_agent.py
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import requests
from bs4 import BeautifulSoup
from datetime import datetime

@tool
def web_search(query: str) -> str:
    """
    Söker på webben efter information.

    Input: Sökfråga
    Output: Lista med relevanta URLs och titlar

    Not: Denna förenklad version returnerar mockdata.
    I produktion: använd Tavily API eller SerpAPI.
    """
    # MOCK DATA (ersätt med riktig API i produktion)
    mock_results = {
        "ai agents": [
            "https://en.wikipedia.org/wiki/Intelligent_agent - Intelligent agent - Wikipedia",
            "https://www.anthropic.com/news/claude-agents - Building with Claude Agents",
            "https://python.langchain.com/docs/modules/agents/ - LangChain Agents Documentation"
        ],
        "climate change": [
            "https://climate.nasa.gov/ - Climate Change: Vital Signs of the Planet",
            "https://www.ipcc.ch/ - IPCC - Climate Change Reports",
        ]
    }

    # Simplified matching
    query_lower = query.lower()
    for key, urls in mock_results.items():
        if key in query_lower:
            result = f"Hittade {len(urls)} resultat för '{query}':\n\n"
            for url in urls:
                result += f"- {url}\n"
            return result

    return f"Sökte efter '{query}' men hittade inga resultat (mock mode). I produktion skulle riktig sökning användas."

@tool
def fetch_webpage(url: str) -> str:
    """
    Hämtar textinnehåll från en webbsida.

    Input: URL
    Output: Extraherad text (max 1000 tecken)
    """
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Research Bot)'}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        # Ta bort script och style
        for script in soup(["script", "style"]):
            script.decompose()

        # Hämta text
        text = soup.get_text()

        # Rensa
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)

        # Begränsa längd
        max_length = 1000
        if len(text) > max_length:
            text = text[:max_length] + "..."

        return f"Innehåll från {url}:\n\n{text}"

    except Exception as e:
        return f"Kunde inte hämta {url}: {e}"

@tool
def summarize_text(text: str, max_words: int = 200) -> str:
    """
    Sammanfattar text till ett specificerat antal ord.

    Input:
    - text: Texten att sammanfatta
    - max_words: Max antal ord (default 200)

    Output: Sammanfattning
    """
    llm = ChatOpenAI(model="gpt-4", temperature=0.3)

    prompt = f"""
Sammanfatta följande text i högst {max_words} ord.
Fokusera på huvudpunkterna.

Text:
{text[:3000]}  # Max 3000 tecken för att inte överbelasta

Sammanfattning:
"""

    summary = llm.predict(prompt)
    return summary.strip()

@tool
def save_report(content: str, topic: str = "research") -> str:
    """
    Sparar researchrapport till markdown-fil.

    Input:
    - content: Rapportinnehåll
    - topic: Ämne (används i filnamn)

    Output: Bekräftelse med filnamn
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_{topic.replace(' ', '_')}_{timestamp}.md"

    # Skapa rapport med metadata
    full_report = f"""# Research Report: {topic}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

{content}

---

*Report generated by Research Agent*
"""

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(full_report)

        return f"Rapport sparad till: {filename}"

    except Exception as e:
        return f"Kunde inte spara rapport: {e}"

# Setup agent
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
tools = [web_search, fetch_webpage, summarize_text, save_report]

template = '''Du är en research-assistent som hjälper användare samla och sammanfatta information.

Din process:
1. Sök efter relevanta källor
2. Läs innehåll från de bästa källorna
3. Sammanfatta informationen
4. Spara en strukturerad rapport

Du har tillgång till:
{tools}

Format:
Question: {input}
Thought: [dina tankar om hur du ska researcha]
Action: [verktyg]
Action Input: [input]
Observation: [resultat]
...
Final Answer: [sammanfattning + "Rapport sparad till X"]

Begin!

Question: {input}
{agent_scratchpad}'''

prompt = PromptTemplate.from_template(template)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=10,
    handle_parsing_errors=True
)

# CLI
def main():
    print("=" * 60)
    print("   RESEARCH ASSISTANT")
    print("   Ställ en fråga så researchar jag åt dig!")
    print("=" * 60)

    while True:
        topic = input("\nVad vill du researcha? (eller 'exit'): ").strip()

        if topic.lower() in ['exit', 'quit']:
            print("Hej då!")
            break

        if not topic:
            continue

        try:
            print(f"\n🔍 Researchar om: {topic}...")
            result = agent_executor.invoke({
                "input": f"Researcha om '{topic}' och skapa en rapport med källor och sammanfattning. Spara till fil."
            })

            print(f"\n✅ Klart!\n{result['output']}")

        except Exception as e:
            print(f"\n❌ Något gick fel: {e}")

if __name__ == "__main__":
    main()
```

**Exempel output (research_ai_agents_20250117_143022.md):**
```markdown
# Research Report: ai agents
**Generated:** 2025-01-17 14:30:22

---

## Sammanfattning

AI-agenter är autonoma system som använder stora språkmodeller (LLMs)
för att utföra uppgifter. De skiljer sig från vanliga chatbots genom
att kunna agera och använda verktyg, inte bara svara på frågor.

## Källor

1. **Wikipedia - Intelligent Agent**
   https://en.wikipedia.org/wiki/Intelligent_agent

   Sammanfattning: [...]

2. **Anthropic - Building with Claude Agents**
   https://www.anthropic.com/news/claude-agents

   Sammanfattning: [...]

3. **LangChain Agents Documentation**
   https://python.langchain.com/docs/modules/agents/

   Sammanfattning: [...]

## Slutsatser

AI-agenter representerar nästa steg i automation...

---

*Report generated by Research Agent*
```

</details>

---

## 📝 Sammanfattning Nivå 3

### Du har nu lärt dig:

✅ **Agent-arkitektur**: De 4 kärnkomponenterna (LLM, Memory, Planner, Tools)
✅ **Agent-typer**: ReAct, Plan-and-Execute, Conversational - och när man använder vilken
✅ **Verktygsintegration**: Hur man skapar och använder tools med `@tool` decorator
✅ **Memory-system**: Buffer, Window, Summary och Vector memory
✅ **LangChain basics**: create_react_agent, AgentExecutor, prompts
✅ **Production tips**: Max iterations, verbose mode, error handling
✅ **Praktisk implementation**: 2 fullständiga projekt

### Nya tekniska begrepp:

| Begrepp | Betydelse |
|---------|-----------|
| **ReAct** | Reason + Act agent-typ |
| **Plan-and-Execute** | Planerar först, exekverar sen |
| **Tool decorator** | `@tool` för att skapa LangChain-verktyg |
| **AgentExecutor** | Kör agenten med error handling |
| **ConversationBufferMemory** | Minne som sparar allt |
| **ConversationBufferWindowMemory** | Minne som sparar senaste N |
| **Verbose mode** | Debug-läge som visar agentens tankar |
| **Max iterations** | Stoppa agent efter N steg (undvik loopar) |

### Nästa steg:

I **Nivå 4** kommer du lära dig:
- Multi-agent systems (flera agenter som samarbetar)
- RAG (Retrieval-Augmented Generation) för kunskapsbaser
- Avancerad orchestration med LangGraph
- Enterprise-integration (databaser, APIs, auth)
- Plattformsjämförelse (när använder man vad?)

**Känner du dig bekväm med kod och verktyg?** Då är du redo! 🚀

---

## 🎯 Självtest Nivå 3

Innan du går vidare till Nivå 4:

**Kan du:**
- [ ] Förklara skillnaden mellan ReAct och Plan-and-Execute?
- [ ] Skapa ett eget verktyg med `@tool`?
- [ ] Sätta upp en agent med LangChain?
- [ ] Implementera minst ett av projekten?
- [ ] Debugga agent-fel med verbose mode?

**4-5 bockar:** Klar för Nivå 4!
**2-3 bockar:** Gör fler övningar, testa projekten
**0-1 bockar:** Gå tillbaka och repetera, inget stress!

---

[← Tillbaka: Nivå 2](./llm-agenter-niva2.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 4 - Avancerade koncept 🚀 →](./llm-agenter-niva4.md)
