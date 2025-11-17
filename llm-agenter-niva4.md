# Nivå 4: Avancerade koncept 🚀

[← Tillbaka: Nivå 3](./llm-agenter-niva3.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 5 →](./llm-agenter-niva5.md)

---

## Introduktion

Välkommen till universitetsnivån! Här lär du dig avancerade tekniker som används i produktionsmiljöer: multi-agent systems där agenter samarbetar, RAG (Retrieval-Augmented Generation) för att ge agenter tillgång till kunskapsbaser, LangGraph för komplexa workflows, och mycket mer.

**Vad ska du lära dig?**
- Multi-agent collaboration (flera agenter jobbar tillsammans)
- RAG - ge agenter tillgång till dokument och data
- LangGraph - state machines för komplexa workflows
- Enterprise integration (databaser, authentication, APIs)
- Avancerad prompt engineering
- Plattformsjämförelser i praktiken

**Förkunskaper:** Nivå 3 + bekvämlighet med Python-programmering.

---

## Kärnkoncept

### 1. Multi-Agent Systems - Agenter som samarbetar

Istället för EN super-agent, låt flera specialiserade agenter jobba tillsammans.

**Koncept:**
```
┌──────────────────────────────────────────┐
│         MULTI-AGENT SYSTEM               │
├──────────────────────────────────────────┤
│                                          │
│  ┌────────┐    ┌────────┐    ┌────────┐│
│  │Research│───►│ Writer │───►│Reviewer││
│  │ Agent  │    │ Agent  │    │ Agent  ││
│  └────────┘    └────────┘    └────────┘│
│       │             │             │     │
│       └─────────────┴─────────────┘     │
│              COORDINATOR                 │
│           (Orchestrator)                 │
└──────────────────────────────────────────┘
```

**Varför multi-agent?**
- **Specialisering**: Varje agent bra på sin sak
- **Parallellisering**: Flera agenter jobbar samtidigt
- **Felsökning**: Enklare att debugga små agenter
- **Flexibilitet**: Lätt att lägga till/ta bort agenter

**Arkitektur-mönster:**

#### **Pattern 1: Sequential (Kedja)**
```
Agent A → Agent B → Agent C → Resultat
```
**Exempel:** Research → Write → Edit
**Verktyg:** LangChain Chains

#### **Pattern 2: Hierarchical (Hierarkisk)**
```
         Manager Agent
        /      |      \
    Agent A  Agent B  Agent C
```
**Exempel:** Manager delegerar uppgifter, samlar resultat
**Verktyg:** AutoGen, CrewAI

#### **Pattern 3: Collaborative (Kollaborativ)**
```
Agent A ←→ Agent B ←→ Agent C
    ↕         ↕         ↕
       Shared Memory
```
**Exempel:** Agenter diskuterar och når konsensus
**Verktyg:** AutoGen ConversableAgent

---

### 2. RAG - Retrieval-Augmented Generation

Ge din agent tillgång till dokument, wikis, databaser - utan att träna om modellen!

**Problemet RAG löser:**
```
User: "Vad står i vår företagspolicy om semester?"
Agent utan RAG: "Jag vet inte, jag har inte den informationen"
Agent med RAG: *Söker i företagsdokument* "Enligt er policy..."
```

**RAG-processen:**
```
1. INDEXING (Setup-fas)
   ├── Ta dokument (PDF, Word, etc.)
   ├── Dela upp i chunks (splitta)
   ├── Skapa embeddings (vektorer)
   └── Spara i vector database

2. RETRIEVAL (Runtime)
   ├── User ställer fråga
   ├── Konvertera fråga till embedding
   ├── Sök liknande chunks i vector DB
   └── Hämta top-k mest relevanta

3. GENERATION
   ├── Skicka fråga + kontext till LLM
   └── LLM genererar svar baserat på kontext
```

**Komponenter:**

**Text Splitter:**
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Max 1000 tecken per chunk
    chunk_overlap=200,    # 200 tecken overlap (undvik att klippa midt i koncept)
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(long_document)
```

**Embeddings:**
```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# Konvertera text till vektor
vector = embeddings.embed_query("Vad är en AI-agent?")
# → [0.123, -0.456, 0.789, ...] (1536 dimensioner för OpenAI)
```

**Vector Store:**
```python
from langchain.vectorstores import FAISS

# Skapa och populera
vectorstore = FAISS.from_texts(
    texts=chunks,
    embedding=embeddings
)

# Sök
results = vectorstore.similarity_search(
    "Hur fungerar semester?",
    k=3  # Top 3 relevanta chunks
)
```

**Komplett RAG-exempel:**
```python
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# 1. Ladda dokument
loader = PyPDFLoader("company_policy.pdf")
documents = loader.load()

# 2. Splitta
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(documents)

# 3. Skapa embeddings och vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)

# 4. Skapa retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# 5. Skapa QA chain
llm = ChatOpenAI(model="gpt-4", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" = stoppa all kontext i en prompt
    retriever=retriever,
    return_source_documents=True
)

# 6. Använd!
response = qa_chain({"query": "Hur många semesterdagar har jag?"})
print(response['result'])
print("Källor:", response['source_documents'])
```

---

### 3. LangGraph - State Machines för Workflows

LangGraph låter dig bygga cykliska workflows med state management.

**Skillnad mot Chains:**
- **Chains**: Linjär A→B→C
- **LangGraph**: Kan ha loopar, villkor, flera vägar

**Koncept:**
```python
from langgraph.graph import StateGraph, END

# Definiera state
from typing import TypedDict

class AgentState(TypedDict):
    messages: list
    next_step: str
    iteration: int

# Skapa graph
workflow = StateGraph(AgentState)

# Definiera nodes (funktioner)
def research_node(state):
    # Gör research
    state['messages'].append("Research klar")
    state['next_step'] = "write"
    return state

def write_node(state):
    # Skriv
    state['messages'].append("Skrivning klar")
    state['next_step'] = "review"
    return state

def review_node(state):
    # Granska
    if quality_check(state):
        state['next_step'] = END
    else:
        state['iteration'] += 1
        if state['iteration'] < 3:
            state['next_step'] = "write"  # Skriv om!
        else:
            state['next_step'] = END
    return state

# Lägg till nodes
workflow.add_node("research", research_node)
workflow.add_node("write", write_node)
workflow.add_node("review", review_node)

# Lägg till edges
workflow.set_entry_point("research")
workflow.add_edge("research", "write")
workflow.add_edge("write", "review")

# Conditional edge från review
workflow.add_conditional_edges(
    "review",
    lambda state: state['next_step'],
    {
        "write": "write",  # Om inte godkänd, skriv om
        END: END           # Om godkänd, sluta
    }
)

# Kompilera
app = workflow.compile()

# Kör
result = app.invoke({
    "messages": [],
    "next_step": "",
    "iteration": 0
})
```

**När använda LangGraph:**
- Komplexa beslut baserat på output
- Behöver loopar (t.ex. "försök igen tills det fungerar")
- Multi-agent med dynamisk routing
- Self-correction workflows

---

### 4. Multi-Agent med AutoGen

Microsoft's AutoGen gör multi-agent super enkelt.

**Exempel: Code review system**
```python
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# Config
llm_config = {"model": "gpt-4", "api_key": "..."}

# Agents
coder = AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message="Du är en Python-utvecklare. Skriv ren, vältestad kod."
)

reviewer = AssistantAgent(
    name="Reviewer",
    llm_config=llm_config,
    system_message="Du är en code reviewer. Hitta buggar och föreslå förbättringar."
)

tester = AssistantAgent(
    name="Tester",
    llm_config=llm_config,
    system_message="Du skriver unit tests. Testa alla edge cases."
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",  # Kör automatiskt
    code_execution_config={"work_dir": "coding"}
)

# Group chat
groupchat = GroupChat(
    agents=[coder, reviewer, tester, user_proxy],
    messages=[],
    max_round=10
)

manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Starta konversation
user_proxy.initiate_chat(
    manager,
    message="Skriv en funktion som kollar om ett nummer är primtal"
)

# Output:
# Coder: "Här är funktionen..."
# Reviewer: "Det finns en bug på rad 5..."
# Coder: "Fixat!"
# Tester: "Här är 5 test cases..."
# User: "TERMINATE" (när alla är nöjda)
```

---

### 5. CrewAI - Role-based Multi-Agent

CrewAI fokuserar på roller och uppgifter.

```python
from crewai import Agent, Task, Crew

# Definiera agents med roller
researcher = Agent(
    role="Research Analyst",
    goal="Hitta aktuell information om {topic}",
    backstory="Du är en erfaren researcher med PhD i informationsvetenskap",
    tools=[web_search_tool],
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Skriv engagerande artiklar baserat på research",
    backstory="Du är en prisbelönt journalist med 10 års erfarenhet",
    tools=[],
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Granska och förbättra artiklar",
    backstory="Du är chefredaktör på en stor tidning",
    tools=[grammar_check_tool],
    verbose=True
)

# Definiera tasks
research_task = Task(
    description="Researcha om {topic}. Hitta minst 5 källor.",
    agent=researcher,
    expected_output="Sammanfattning med källor"
)

write_task = Task(
    description="Skriv en 500-ords artikel om {topic} baserat på research",
    agent=writer,
    expected_output="Färdig artikel",
    context=[research_task]  # Använd output från research
)

edit_task = Task(
    description="Granska artikeln och förbättra kvaliteten",
    agent=editor,
    expected_output="Polerad artikel",
    context=[write_task]
)

# Skapa crew
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, write_task, edit_task],
    verbose=True
)

# Kör
result = crew.kickoff(inputs={"topic": "AI Agents 2025"})
print(result)
```

---

## Konkreta Exempel

### Exempel 1: RAG-baserad dokumentations-bot

**Use case:** Support-bot som svarar baserat på företagets dokumentation.

```python
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

# 1. Ladda alla markdown-filer från docs/
loader = DirectoryLoader(
    'docs/',
    glob="**/*.md",
    loader_cls=TextLoader
)
documents = loader.load()

# 2. Splitta med overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300,
    separators=["\n## ", "\n### ", "\n", " "]
)
splits = text_splitter.split_documents(documents)

print(f"Skapade {len(splits)} chunks från {len(documents)} dokument")

# 3. Skapa persistent vector store (Chroma istället för FAISS)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 4. Setup conversational RAG chain
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
    output_key='answer'
)

llm = ChatOpenAI(model="gpt-4", temperature=0.3)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
    memory=memory,
    return_source_documents=True,
    verbose=True
)

# 5. Använd
while True:
    question = input("\nFråga (eller 'exit'): ")
    if question.lower() == 'exit':
        break

    result = qa_chain({"question": question})

    print(f"\nSvar: {result['answer']}")
    print(f"\nKällor:")
    for doc in result['source_documents']:
        print(f"- {doc.metadata['source']}")
```

---

### Exempel 2: Multi-agent content creation pipeline

```python
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# Shared state
pipeline_state = {}

# Tools för olika agents
@tool
def research_topic(topic: str) -> str:
    """Researchar ett ämne"""
    # I verkligheten: web search
    pipeline_state['research'] = f"Research om {topic}: [5 källor...]"
    return pipeline_state['research']

@tool
def create_outline(topic: str) -> str:
    """Skapar outline från research"""
    outline = f"""
    Outline för {topic}:
    1. Introduktion
    2. Huvudpunkter
    3. Slutsats
    """
    pipeline_state['outline'] = outline
    return outline

@tool
def write_section(section: str) -> str:
    """Skriver en sektion"""
    content = f"Innehåll för {section}: [500 ord...]"
    if 'content' not in pipeline_state:
        pipeline_state['content'] = {}
    pipeline_state['content'][section] = content
    return content

@tool
def review_content(content: str) -> str:
    """Granskar innehåll"""
    return f"Review: Bra! Några små fixes behövs..."

# Skapa specialiserade agents
researcher = AgentExecutor(
    agent=create_react_agent(llm, [research_topic]),
    tools=[research_topic],
    verbose=True
)

writer = AgentExecutor(
    agent=create_react_agent(llm, [create_outline, write_section]),
    tools=[create_outline, write_section],
    verbose=True
)

reviewer = AgentExecutor(
    agent=create_react_agent(llm, [review_content]),
    tools=[review_content],
    verbose=True
)

# Orchestrate
def content_pipeline(topic):
    # 1. Research
    research_result = researcher.invoke({
        "input": f"Researcha om {topic}"
    })

    # 2. Outline
    outline_result = writer.invoke({
        "input": f"Skapa outline för {topic}"
    })

    # 3. Write
    sections = ["Introduktion", "Huvuddel", "Slutsats"]
    for section in sections:
        writer.invoke({
            "input": f"Skriv sektion: {section}"
        })

    # 4. Review
    review_result = reviewer.invoke({
        "input": "Granska allt innehåll"
    })

    return pipeline_state

result = content_pipeline("AI Agents")
```

---

## 💡 Pro Tips

### Tip 1: RAG chunk size är kritiskt

```python
# För lång chunk size
chunk_size=5000  # Problem: För mycket irrelevant info kommer med

# För kort chunk size
chunk_size=100   # Problem: Förlorar kontext

# Sweet spot (beror på use case)
chunk_size=1000-1500  # Bra för de flesta dokument
chunk_overlap=200-300  # 20% overlap
```

### Tip 2: Hybrid search är bättre än bara similarity

```python
# Bara semantic search
retriever = vectorstore.as_retriever()

# Hybrid: Semantic + Keyword (BM25)
from langchain.retrievers import EnsembleRetriever
from langchain.retrievers import BM25Retriever

bm25_retriever = BM25Retriever.from_documents(documents)
ensemble_retriever = EnsembleRetriever(
    retrievers=[vectorstore.as_retriever(), bm25_retriever],
    weights=[0.6, 0.4]  # 60% semantic, 40% keyword
)
```

### Tip 3: Multi-agent behöver tydliga roller

```python
# Dåligt: Vaga roller
agent1 = Agent(role="Helper")  # Vad hjälper den med??

# Bra: Specifika roller
research_agent = Agent(
    role="Market Research Analyst",
    goal="Analyze market trends in {industry}",
    backstory="10 years experience in {industry} analysis"
)
```

---

## ✏️ Övningar

### Övning 4.1: Bygg en enkel RAG-applikation 📚

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~30 minuter

**Uppgift:**
Skapa en RAG-app som kan svara på frågor om 3-5 textfiler.

**Steg:**
1. Skapa 3 textfiler med olika ämnen (t.ex. python_guide.txt, git_guide.txt, docker_guide.txt)
2. Ladda, splitta, och indexera i FAISS
3. Skapa en QA-chain
4. Testa med frågor

<details>
<summary>💡 Lösning</summary>

```python
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# 1. Ladda dokument
loader = DirectoryLoader(
    './docs',
    glob="*.txt",
    loader_cls=TextLoader
)
documents = loader.load()
print(f"Laddade {len(documents)} dokument")

# 2. Splitta
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = splitter.split_documents(documents)
print(f"Skapade {len(splits)} chunks")

# 3. Skapa vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(splits, embeddings)

# 4. Skapa chain
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
llm = ChatOpenAI(model="gpt-4", temperature=0)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# 5. Testa
questions = [
    "Hur använder man git commit?",
    "Vad är Docker containers?",
    "Hur definierar man en funktion i Python?"
]

for q in questions:
    print(f"\nQ: {q}")
    result = qa({"query": q})
    print(f"A: {result['result']}")
    print(f"Källor: {[doc.metadata['source'] for doc in result['source_documents']]}")
```

</details>

---

### Övning 4.2: Multi-agent  med AutoGen 🤖🤖

**Svårighetsgrad**: ⭐⭐⭐⭐
**Tid**: ~30 minuter

**Uppgift:**
Skapa en multi-agent där en agent skriver kod och en annan granskar den.

<details>
<summary>💡 Lösningsexempel</summary>

```python
from autogen import AssistantAgent, UserProxyAgent
import os

# Setup
config_list = [{
    "model": "gpt-4",
    "api_key": os.getenv("OPENAI_API_KEY")
}]

# Coder agent
coder = AssistantAgent(
    name="Coder",
    llm_config={"config_list": config_list},
    system_message="""Du är en Python-utvecklare.
    Skriv ren, välkommenterad kod.
    Inkludera docstrings och type hints."""
)

# Reviewer agent
reviewer = AssistantAgent(
    name="Reviewer",
    llm_config={"config_list": config_list},
    system_message="""Du är en code reviewer.
    Granska koden för:
    - Buggar
    - Edge cases
    - Code style
    - Performance
    Ge konstruktiv feedback."""
)

# User proxy (kör kod)
user = UserProxyAgent(
    name="User",
    human_input_mode="TERMINATE",
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

# Starta workflow
user.initiate_chat(
    coder,
    message="""Skriv en funktion 'fibonacci(n)' som returnerar
    de första n fibonacci-talen som en lista.
    Inkludera error handling."""
)

# Efter coder svarar, låt reviewer granska
user.initiate_chat(
    reviewer,
    message="Granska koden ovan. Hitta förbättringar."
)
```

</details>

---

### Övning 4.3: LangGraph Workflow 🔄

**Svårighetsgrad**: ⭐⭐⭐⭐⭐
**Tid**: ~40 minuter

**Uppgift:**
Bygg ett workflow som:
1. Genererar content
2. Granskar kvalitet
3. Om dålig kvalitet → generera om (max 3 försök)
4. Om bra → returnera

<details>
<summary>💡 Lösning</summary>

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")

# State
class ContentState(TypedDict):
    topic: str
    content: str
    quality_score: int
    attempts: int

# Nodes
def generate_content(state: ContentState) -> ContentState:
    """Genererar innehåll"""
    prompt = f"Skriv 200 ord om {state['topic']}"
    state['content'] = llm.predict(prompt)
    state['attempts'] += 1
    return state

def review_content(state: ContentState) -> ContentState:
    """Granskar kvalitet (1-10)"""
    prompt = f"""Gradera detta innehåll 1-10:

{state['content']}

Returnera bara siffran."""

    score = int(llm.predict(prompt).strip())
    state['quality_score'] = score
    return state

def decide_next(state: ContentState) -> str:
    """Bestämmer nästa steg"""
    if state['quality_score'] >= 7:
        return END
    elif state['attempts'] < 3:
        return "generate"
    else:
        return END

# Bygg graph
workflow = StateGraph(ContentState)

workflow.add_node("generate", generate_content)
workflow.add_node("review", review_content)

workflow.set_entry_point("generate")
workflow.add_edge("generate", "review")
workflow.add_conditional_edges(
    "review",
    decide_next,
    {
        "generate": "generate",
        END: END
    }
)

app = workflow.compile()

# Kör
result = app.invoke({
    "topic": "AI agents",
    "content": "",
    "quality_score": 0,
    "attempts": 0
})

print(f"Färdigt efter {result['attempts']} försök")
print(f"Kvalitet: {result['quality_score']}/10")
print(f"\nInnehåll:\n{result['content']}")
```

</details>

---

### Övning 4.4-4.10: Snabbövningar ⚡

**4.4: Chunk size experiment**
Testa chunk_size 500, 1000, 2000 på samma dokument. Vilken ger bäst svar?

**4.5: CrewAI basics**
Skapa en Crew med 2 agents: Researcher + Writer

**4.6: Hybrid retrieval**
Implementera BM25 + semantic search ensemble

**4.7: Memory i RAG**
Lägg till ConversationBufferMemory i QA-chain

**4.8: Source citation**
Formatera RAG-svar med citat från källorna

**4.9: Agent communication**
Låt två AutoGen-agenter diskutera en frågeställning

**4.10: Error handling**
Lägg till retry-logic i multi-agent system

---

## 🚀 Projekt

### Projekt 4.1: Enterprise Documentation Q&A System

**Svårighetsgrad**: ⭐⭐⭐⭐⭐
**Tid**: ~90 minuter

**Specifikation:**
- Indexera minst 20 markdown/PDF dokument
- Hybrid search (semantic + keyword)
- Conversational (kom ihåg kontext)
- Source citation med sidnummer
- Filtrera efter dokument-typ eller kategori
- Web interface med Streamlit

**Starter template:**
```python
import streamlit as st
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

st.title("📚 Documentation Q&A")

# Setup (cache this)
@st.cache_resource
def setup_qa_chain():
    # TODO: Ladda dokument
    # TODO: Skapa vectorstore
    # TODO: Skapa chain med memory
    pass

qa_chain = setup_qa_chain()

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Ställ en fråga..."):
    # TODO: Kör qa_chain
    # TODO: Visa svar + källor
    pass
```

<details>
<summary>💡 Fullständig lösning</summary>

```python
# enterprise_qa.py
import streamlit as st
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os

st.set_page_config(page_title="Documentation Q&A", page_icon="📚")
st.title("📚 Enterprise Documentation Q&A")

# Sidebar för filters
with st.sidebar:
    st.header("Inställningar")

    doc_type = st.selectbox(
        "Dokumenttyp",
        ["Alla", "PDF", "Markdown", "Text"]
    )

    k_results = st.slider("Antal källor", 1, 10, 4)

# Setup QA system
@st.cache_resource
def setup_qa_chain():
    # Ladda dokument
    loader = DirectoryLoader(
        './docs',
        glob="**/*",
        show_progress=True
    )
    documents = loader.load()

    # Metadata enrichment
    for doc in documents:
        doc.metadata['type'] = doc.metadata['source'].split('.')[-1]

    # Splitta
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )
    splits = splitter.split_documents(documents)

    # Vectorstore (persistent)
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./chroma_enterprise"
    )

    return vectorstore

vectorstore = setup_qa_chain()

# Skapa retriever baserat på filters
def get_retriever(doc_type_filter, k):
    if doc_type_filter == "Alla":
        return vectorstore.as_retriever(search_kwargs={"k": k})
    else:
        # Filter by type
        extension_map = {
            "PDF": "pdf",
            "Markdown": "md",
            "Text": "txt"
        }
        return vectorstore.as_retriever(
            search_kwargs={
                "k": k,
                "filter": {"type": extension_map[doc_type_filter]}
            }
        )

# Memory (session-specific)
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key='answer'
    )

# QA Chain
llm = ChatOpenAI(model="gpt-4", temperature=0)
retriever = get_retriever(doc_type, k_results)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=st.session_state.memory,
    return_source_documents=True,
    verbose=True
)

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "sources" in msg:
            with st.expander("Källor"):
                for source in msg["sources"]:
                    st.write(f"- {source}")

# Chat input
if prompt := st.chat_input("Ställ en fråga om dokumentationen..."):
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Get response
    with st.chat_message("assistant"):
        with st.spinner("Söker i dokument..."):
            result = qa_chain({"question": prompt})

            answer = result['answer']
            sources = [
                f"{doc.metadata['source']} (sid {doc.metadata.get('page', 'N/A')})"
                for doc in result['source_documents']
            ]

            st.write(answer)

            with st.expander("Källor"):
                for source in sources:
                    st.write(f"- {source}")

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer,
        "sources": sources
    })

# Sidebar stats
with st.sidebar:
    st.markdown("---")
    st.subheader("Statistik")
    st.metric("Konversationer", len(st.session_state.messages) // 2)

    if st.button("Rensa historik"):
        st.session_state.messages = []
        st.session_state.memory.clear()
        st.rerun()
```

**Kör med:**
```bash
streamlit run enterprise_qa.py
```

</details>

---

### Projekt 4.2: Multi-Agent Content Pipeline

**Svårighetsgrad**: ⭐⭐⭐⭐⭐
**Tid**: ~120 minuter

**Specifikation:**
Bygg en content creation pipeline med 4 agenter:
1. **Researcher**: Samlar info om ämne
2. **Outline Creator**: Skapar struktur
3. **Writer**: Skriver varje sektion
4. **Editor**: Granskar och förbättrar

**Verktyg:** CrewAI
**Output:** Komplett artikel (markdown) med källor

<details>
<summary>💡 Lösningsförslag</summary>

```python
# content_pipeline.py
from crewai import Agent, Task, Crew
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import requests

# Tools
@tool
def web_search(query: str) -> str:
    """Söker på webben"""
    # Simplified - use real API in production
    return f"Sökresultat för '{query}': [5 källor...]"

@tool
def save_to_file(content: str, filename: str) -> str:
    """Sparar innehåll till fil"""
    with open(filename, 'w') as f:
        f.write(content)
    return f"Sparat till {filename}"

# Agents
researcher = Agent(
    role="Senior Research Analyst",
    goal="Hitta aktuell och korrekt information om {topic}",
    backstory="""Du är en erfaren researcher med expertis inom
    informationssökning och källkritik. Du verifierar alltid dina källor.""",
    tools=[web_search],
    verbose=True,
    llm=ChatOpenAI(model="gpt-4")
)

outliner = Agent(
    role="Content Strategist",
    goal="Skapa en välstrukturerad outline för {topic}",
    backstory="""Du är expert på att strukturera innehåll.
    Du skapar logiska, engagerande outlines som guidar läsaren.""",
    tools=[],
    verbose=True,
    llm=ChatOpenAI(model="gpt-4")
)

writer = Agent(
    role="Content Writer",
    goal="Skriv högkvalitativt, engagerande innehåll",
    backstory="""Du är en prisbelönt författare och journalist.
    Din text är klar, koncis och engagerande.""",
    tools=[],
    verbose=True,
    llm=ChatOpenAI(model="gpt-4")
)

editor = Agent(
    role="Chief Editor",
    goal="Granska och förbättra innehåll till publikationsstandard",
    backstory="""Du är chefredaktör med 15 års erfarenhet.
    Du förbättrar struktur, grammatik och flyt.""",
    tools=[save_to_file],
    verbose=True,
    llm=ChatOpenAI(model="gpt-4")
)

# Tasks
research_task = Task(
    description="""Researcha om {topic}.
    Hitta:
    - 5-10 aktuella källor
    - Huvudfakta och nyckelinsikter
    - Relevanta statistik och exempel

    Verifiera att källorna är trovärdiga.""",
    agent=researcher,
    expected_output="Sammanställning av research med källor"
)

outline_task = Task(
    description="""Baserat på research, skapa en outline för en artikel om {topic}.

    Outlinen ska ha:
    - Titel
    - Introduktion (hook)
    - 3-5 huvudsektioner
    - Slutsats
    - Call to action

    Varje sektion ska ha bullet points med vad som ska täckas.""",
    agent=outliner,
    expected_output="Detaljerad artikel-outline i markdown",
    context=[research_task]
)

write_task = Task(
    description="""Skriv en komplett artikel baserat på outline och research.

    Krav:
    - 800-1200 ord
    - Engagerande introduktion
    - Välstrukturerade stycken
    - Exempel och konkreta detaljer
    - Stark slutsats

    Använd markdown-formatering.""",
    agent=writer,
    expected_output="Färdig artikel i markdown",
    context=[research_task, outline_task]
)

edit_task = Task(
    description="""Granska och förbättra artikeln.

    Kontrollera:
    - Grammatik och stavning
    - Logiskt flöde
    - Tydlighet
    - Ton och stil
    - Källor är korrekt citerade

    Förbättra där det behövs. Spara slutresultat till 'article_{topic}.md'""",
    agent=editor,
    expected_output="Polerad artikel sparad till fil",
    context=[write_task]
)

# Crew
crew = Crew(
    agents=[researcher, outliner, writer, editor],
    tasks=[research_task, outline_task, write_task, edit_task],
    verbose=2
)

# Run
if __name__ == "__main__":
    topic = input("Vilket ämne vill du skriva om? ")

    result = crew.kickoff(inputs={"topic": topic})

    print("\n" + "="*50)
    print("PIPELINE KLAR!")
    print("="*50)
    print(f"\nResultat sparat till: article_{topic}.md")
    print(f"\nPreview:\n{result[:500]}...")
```

**Exempel output (article_AI_Agents.md):**
```markdown
# AI Agents: The Future of Automation

## Introduction

Imagine a world where your digital assistant doesn't just answer
questions, but actually gets things done...

## What Are AI Agents?

AI agents are autonomous systems that combine large language models
with the ability to use tools...

[...]

## Sources

1. "Building with Claude Agents" - Anthropic, 2024
2. "LangChain Documentation" - LangChain, 2024
[...]
```

</details>

---

## 📝 Sammanfattning Nivå 4

### Du har nu lärt dig:

✅ **Multi-Agent Systems**: Flera agenter samarbetar (AutoGen, CrewAI)
✅ **RAG**: Retrieval-Augmented Generation för kunskapsbaser
✅ **LangGraph**: State machines för komplexa workflows med loopar
✅ **Hybrid Search**: Kombinera semantic + keyword search
✅ **Enterprise Integration**: Production-ready patterns
✅ **Advanced Orchestration**: Role-based och task-based arkitekturer

### Viktiga ramverk:

| Ramverk | Bäst för | Svårighetsgrad |
|---------|----------|----------------|
| **LangChain** | RAG, Chains, Basic agents | Medel |
| **LangGraph** | Komplexa workflows, State management | Hög |
| **AutoGen** | Conversational multi-agent | Medel |
| **CrewAI** | Role-based pipelines | Medel-Låg |

### Nästa steg:

I **Nivå 5** kommer du lära dig:
- Production deployment (Docker, API:er, skalning)
- Säkerhet (prompt injection, data leakage)
- Observability (logging, monitoring, tracing)
- Kostnadsoptimering
- Cutting-edge research (2024-2025)

**Känner du dig redo för production?** 🚀

---

## 🎯 Självtest Nivå 4

**Kan du:**
- [ ] Förklara hur RAG fungerar steg-för-steg?
- [ ] Bygga en multi-agent med minst 2 agents?
- [ ] Implementera ett LangGraph workflow med loopar?
- [ ] Välja rätt chunk size för ett dokument?
- [ ] Sätta upp hybrid search (semantic + keyword)?
- [ ] Integrera RAG i en conversational chain?

**5-6 bockar:** Redo för Nivå 5!
**3-4 bockar:** Gör projekten, testa mer
**0-2 bockar:** Repetera viktiga delar

---

[← Tillbaka: Nivå 3](./llm-agenter-niva3.md) | [Huvudguiden](./llm-agenter-guide.md) | [Nästa: Nivå 5 - Expert 💎 →](./llm-agenter-niva5.md)
