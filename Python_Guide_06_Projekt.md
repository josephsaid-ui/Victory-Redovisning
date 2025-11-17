# 🐍 Praktiska projekt

Detta kapitel innehåller tre kompletta projekt som integrerar allt du lärt dig. Varje projekt ökar i komplexitet och täcker olika områden av Python-programmering.

---

## Projekt 1: Komplett kalkylator 🧮

**Nivå:** 2-3 (Nybörjare till mellanliggande)
**Tidsåtgång:** 1-2 timmar
**Koncept:** Funktioner, loopar, error handling, filhantering

### Projektbeskrivning

Bygg en interaktiv kalkylator som kan:
- Utföra grundläggande operationer (+, -, *, /, %, **)
- Spara beräkningshistorik till fil
- Ladda tidigare historik
- Hantera felaktig input

### Fullständig kod

```python
"""
Avancerad Kalkylator
Skapad som del av Python-guide
"""

import json
from datetime import datetime
from typing import List, Dict

class Kalkylator:
    """En avancerad kalkylator med historik-funktion."""

    def __init__(self):
        self.historik: List[Dict] = []
        self.historik_fil = "kalkylator_historik.json"
        self.ladda_historik()

    def addera(self, a: float, b: float) -> float:
        """Adderar två tal."""
        return a + b

    def subtrahera(self, a: float, b: float) -> float:
        """Subtraherar b från a."""
        return a - b

    def multiplicera(self, a: float, b: float) -> float:
        """Multiplicerar två tal."""
        return a * b

    def dividera(self, a: float, b: float) -> float:
        """Dividerar a med b."""
        if b == 0:
            raise ValueError("Kan inte dela med 0")
        return a / b

    def modulo(self, a: float, b: float) -> float:
        """Returnerar resten vid division."""
        if b == 0:
            raise ValueError("Kan inte dela med 0")
        return a % b

    def potens(self, a: float, b: float) -> float:
        """Upphöjer a till potensen b."""
        return a ** b

    def lägg_till_historik(self, operation: str, tal1: float, tal2: float, resultat: float) -> None:
        """Lägger till beräkning i historiken."""
        post = {
            "tidpunkt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operation": operation,
            "tal1": tal1,
            "tal2": tal2,
            "resultat": resultat
        }
        self.historik.append(post)

    def visa_historik(self) -> None:
        """Visar beräkningshistoriken."""
        if not self.historik:
            print("\n📊 Historiken är tom")
            return

        print("\n📊 === BERÄKNINGSHISTORIK ===")
        for i, post in enumerate(self.historik[-10:], 1):  # Senaste 10
            print(f"{i}. [{post['tidpunkt']}] {post['tal1']} {post['operation']} {post['tal2']} = {post['resultat']}")

    def rensa_historik(self) -> None:
        """Rensar historiken."""
        self.historik = []
        print("✅ Historiken rensad")

    def spara_historik(self) -> None:
        """Sparar historiken till JSON-fil."""
        try:
            with open(self.historik_fil, "w", encoding="utf-8") as fil:
                json.dump(self.historik, fil, ensure_ascii=False, indent=2)
            print(f"✅ Historik sparad till {self.historik_fil}")
        except Exception as e:
            print(f"❌ Kunde inte spara historik: {e}")

    def ladda_historik(self) -> None:
        """Laddar historik från JSON-fil."""
        try:
            with open(self.historik_fil, "r", encoding="utf-8") as fil:
                self.historik = json.load(fil)
            print(f"✅ Laddade {len(self.historik)} poster från historik")
        except FileNotFoundError:
            print("ℹ️ Ingen tidigare historik funnen")
        except Exception as e:
            print(f"⚠️ Kunde inte ladda historik: {e}")

    def kör(self) -> None:
        """Huvudloop för kalkylatorn."""
        print("=" * 50)
        print("🧮 VÄLKOMMEN TILL KALKYLATORN")
        print("=" * 50)

        while True:
            print("\n=== MENY ===")
            print("1. Addition (+)")
            print("2. Subtraktion (-)")
            print("3. Multiplikation (*)")
            print("4. Division (/)")
            print("5. Modulo (resten vid division, %)")
            print("6. Potens (**)")
            print("7. Visa historik")
            print("8. Rensa historik")
            print("9. Spara historik")
            print("0. Avsluta")

            val = input("\n👉 Välj operation (0-9): ").strip()

            if val == "0":
                print("\n👋 Tack för att du använde kalkylatorn!")
                self.spara_historik()
                break

            elif val == "7":
                self.visa_historik()

            elif val == "8":
                bekräfta = input("Är du säker på att du vill rensa historiken? (ja/nej): ").strip().lower()
                if bekräfta == "ja":
                    self.rensa_historik()

            elif val == "9":
                self.spara_historik()

            elif val in ["1", "2", "3", "4", "5", "6"]:
                try:
                    # Ta emot input
                    tal1 = float(input("Ange första talet: "))
                    tal2 = float(input("Ange andra talet: "))

                    # Utför operation
                    operationer = {
                        "1": (self.addera, "+"),
                        "2": (self.subtrahera, "-"),
                        "3": (self.multiplicera, "*"),
                        "4": (self.dividera, "/"),
                        "5": (self.modulo, "%"),
                        "6": (self.potens, "**")
                    }

                    funktion, symbol = operationer[val]
                    resultat = funktion(tal1, tal2)

                    # Visa resultat
                    print(f"\n✅ {tal1} {symbol} {tal2} = {resultat}")

                    # Spara i historik
                    self.lägg_till_historik(symbol, tal1, tal2, resultat)

                except ValueError as e:
                    print(f"\n❌ Fel: {e}")
                except Exception as e:
                    print(f"\n❌ Ett oväntat fel uppstod: {e}")

            else:
                print("\n❌ Ogiltigt val! Välj 0-9")

def main():
    """Huvudfunktion."""
    kalkylator = Kalkylator()
    kalkylator.kör()

if __name__ == "__main__":
    main()
```

### Körningsexempel

```
==================================================
🧮 VÄLKOMMEN TILL KALKYLATORN
==================================================
ℹ️ Ingen tidigare historik funnen

=== MENY ===
1. Addition (+)
2. Subtraktion (-)
3. Multiplikation (*)
4. Division (/)
5. Modulo (resten vid division, %)
6. Potens (**)
7. Visa historik
8. Rensa historik
9. Spara historik
0. Avsluta

👉 Välj operation (0-9): 1
Ange första talet: 15
Ange andra talet: 7

✅ 15.0 + 7.0 = 22.0

👉 Välj operation (0-9): 7

📊 === BERÄKNINGSHISTORIK ===
1. [2024-11-17 14:30:45] 15.0 + 7.0 = 22.0
```

### Utmaningar för att utöka projektet

1. **Lägg till fler operationer**: kvadratrot, logaritm, trigonometri
2. **Grafiskt gränssnitt**: Använd tkinter för GUI
3. **Vetenskaplig räknare**: Stöd för parenteser och uttryck som "2 * (3 + 4)"
4. **Export till Excel**: Spara historik till Excel-fil
5. **Statistik**: Visa mest använda operation

---

## Projekt 2: TODO-app med GUI 📝

**Nivå:** 4 (Avancerad)
**Tidsåtgång:** 3-4 timmar
**Koncept:** OOP, tkinter, filhantering, dataclasses

### Projektbeskrivning

Bygg en TODO-applikation med grafiskt gränssnitt som kan:
- Lägga till, redigera och ta bort uppgifter
- Markera uppgifter som klara
- Filtrera uppgifter (alla, aktiva, klara)
- Spara och ladda uppgifter från JSON-fil
- Prioritetsnivåer (låg, medium, hög)

### Fullständig kod

```python
"""
TODO-applikation med GUI
Använder tkinter för grafiskt gränssnitt
"""

import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List
import json

@dataclass
class Todo:
    """Representerar en TODO-uppgift."""
    id: int
    titel: str
    beskrivning: str
    prioritet: str  # "Låg", "Medium", "Hög"
    klar: bool = False
    skapad: str = ""

    def __post_init__(self):
        if not self.skapad:
            self.skapad = datetime.now().strftime("%Y-%m-%d %H:%M")

class TodoApp:
    """Huvudapplikation för TODO-hantering."""

    def __init__(self, root):
        self.root = root
        self.root.title("📝 TODO-applikation")
        self.root.geometry("800x600")

        self.todos: List[Todo] = []
        self.nästa_id = 1
        self.filnamn = "todos.json"
        self.filter_läge = "Alla"  # "Alla", "Aktiva", "Klara"

        self.skapa_gui()
        self.ladda_todos()
        self.uppdatera_lista()

    def skapa_gui(self):
        """Skapar det grafiska gränssnittet."""

        # Header
        header_frame = tk.Frame(self.root, bg="#2c3e50", height=60)
        header_frame.pack(fill="x")

        tk.Label(
            header_frame,
            text="📝 Mina TODO-uppgifter",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=10)

        # Input-sektion
        input_frame = tk.LabelFrame(self.root, text="Ny uppgift", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=10)

        # Titel
        tk.Label(input_frame, text="Titel:").grid(row=0, column=0, sticky="w")
        self.titel_entry = tk.Entry(input_frame, width=40)
        self.titel_entry.grid(row=0, column=1, padx=5, pady=5)

        # Beskrivning
        tk.Label(input_frame, text="Beskrivning:").grid(row=1, column=0, sticky="w")
        self.beskrivning_entry = tk.Entry(input_frame, width=40)
        self.beskrivning_entry.grid(row=1, column=1, padx=5, pady=5)

        # Prioritet
        tk.Label(input_frame, text="Prioritet:").grid(row=2, column=0, sticky="w")
        self.prioritet_var = tk.StringVar(value="Medium")
        prioritet_combo = ttk.Combobox(
            input_frame,
            textvariable=self.prioritet_var,
            values=["Låg", "Medium", "Hög"],
            state="readonly",
            width=37
        )
        prioritet_combo.grid(row=2, column=1, padx=5, pady=5)

        # Lägg till-knapp
        tk.Button(
            input_frame,
            text="➕ Lägg till",
            command=self.lägg_till_todo,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold")
        ).grid(row=3, column=1, pady=10, sticky="e")

        # Filter-knappar
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(
            filter_frame,
            text="Alla",
            command=lambda: self.sätt_filter("Alla"),
            width=10
        ).pack(side="left", padx=5)

        tk.Button(
            filter_frame,
            text="Aktiva",
            command=lambda: self.sätt_filter("Aktiva"),
            width=10
        ).pack(side="left", padx=5)

        tk.Button(
            filter_frame,
            text="Klara",
            command=lambda: self.sätt_filter("Klara"),
            width=10
        ).pack(side="left", padx=5)

        # Lista över TODOs
        lista_frame = tk.Frame(self.root)
        lista_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")

        # Listbox
        self.todo_listbox = tk.Listbox(
            lista_frame,
            yscrollcommand=scrollbar.set,
            font=("Courier", 10),
            selectmode=tk.SINGLE
        )
        self.todo_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.todo_listbox.yview)

        # Bindningar
        self.todo_listbox.bind("<Double-Button-1>", self.togglera_klar)

        # Knappar för hantering
        knapp_frame = tk.Frame(self.root)
        knapp_frame.pack(fill="x", padx=10, pady=10)

        tk.Button(
            knapp_frame,
            text="✅ Markera klar/aktiv",
            command=self.togglera_klar,
            bg="#3498db",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            knapp_frame,
            text="❌ Ta bort",
            command=self.ta_bort_todo,
            bg="#e74c3c",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            knapp_frame,
            text="💾 Spara",
            command=self.spara_todos,
            bg="#9b59b6",
            fg="white"
        ).pack(side="right", padx=5)

    def lägg_till_todo(self):
        """Lägger till en ny TODO-uppgift."""
        titel = self.titel_entry.get().strip()
        beskrivning = self.beskrivning_entry.get().strip()
        prioritet = self.prioritet_var.get()

        if not titel:
            messagebox.showwarning("Varning", "Titel får inte vara tom!")
            return

        todo = Todo(
            id=self.nästa_id,
            titel=titel,
            beskrivning=beskrivning,
            prioritet=prioritet
        )

        self.todos.append(todo)
        self.nästa_id += 1

        # Rensa input-fält
        self.titel_entry.delete(0, tk.END)
        self.beskrivning_entry.delete(0, tk.END)
        self.prioritet_var.set("Medium")

        self.uppdatera_lista()
        messagebox.showinfo("Framgång", f"TODO '{titel}' tillagd!")

    def togglera_klar(self, event=None):
        """Togglerar klar-status för vald TODO."""
        selection = self.todo_listbox.curselection()
        if not selection:
            messagebox.showwarning("Varning", "Välj en TODO först!")
            return

        index = selection[0]
        filtrerade = self.få_filtrerade_todos()

        if index < len(filtrerade):
            todo = filtrerade[index]
            todo.klar = not todo.klar
            self.uppdatera_lista()

    def ta_bort_todo(self):
        """Tar bort vald TODO."""
        selection = self.todo_listbox.curselection()
        if not selection:
            messagebox.showwarning("Varning", "Välj en TODO att ta bort!")
            return

        index = selection[0]
        filtrerade = self.få_filtrerade_todos()

        if index < len(filtrerade):
            todo = filtrerade[index]
            bekräfta = messagebox.askyesno(
                "Bekräfta",
                f"Vill du ta bort '{todo.titel}'?"
            )

            if bekräfta:
                self.todos.remove(todo)
                self.uppdatera_lista()
                messagebox.showinfo("Framgång", "TODO borttagen!")

    def få_filtrerade_todos(self) -> List[Todo]:
        """Returnerar filtrerade TODOs baserat på nuvarande filter."""
        if self.filter_läge == "Aktiva":
            return [t for t in self.todos if not t.klar]
        elif self.filter_läge == "Klara":
            return [t for t in self.todos if t.klar]
        else:  # "Alla"
            return self.todos

    def sätt_filter(self, läge: str):
        """Sätter filter-läge och uppdaterar listan."""
        self.filter_läge = läge
        self.uppdatera_lista()

    def uppdatera_lista(self):
        """Uppdaterar listboxen med TODOs."""
        self.todo_listbox.delete(0, tk.END)

        filtrerade = self.få_filtrerade_todos()

        for todo in filtrerade:
            status = "✅" if todo.klar else "⬜"
            prioritet_ikon = {"Låg": "🟢", "Medium": "🟡", "Hög": "🔴"}[todo.prioritet]

            text = f"{status} {prioritet_ikon} {todo.titel}"
            if todo.beskrivning:
                text += f" - {todo.beskrivning}"

            self.todo_listbox.insert(tk.END, text)

            # Färgkodning
            if todo.klar:
                self.todo_listbox.itemconfig(tk.END, fg="gray")

    def spara_todos(self):
        """Sparar TODOs till JSON-fil."""
        try:
            data = [asdict(todo) for todo in self.todos]
            with open(self.filnamn, "w", encoding="utf-8") as fil:
                json.dump(data, fil, ensure_ascii=False, indent=2)
            messagebox.showinfo("Framgång", f"TODOs sparade till {self.filnamn}")
        except Exception as e:
            messagebox.showerror("Fel", f"Kunde inte spara: {e}")

    def ladda_todos(self):
        """Laddar TODOs från JSON-fil."""
        try:
            with open(self.filnamn, "r", encoding="utf-8") as fil:
                data = json.load(fil)
                self.todos = [Todo(**item) for item in data]

            if self.todos:
                self.nästa_id = max(t.id for t in self.todos) + 1
        except FileNotFoundError:
            pass  # Ingen fil ännu
        except Exception as e:
            messagebox.showerror("Fel", f"Kunde inte ladda: {e}")

def main():
    """Startar applikationen."""
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
```

### Utmaningar för att utöka projektet

1. **Deadlines**: Lägg till datum för när uppgifter ska vara klara
2. **Kategorier**: Organisera TODOs i kategorier (Jobb, Privat, etc.)
3. **Sök-funktion**: Sök efter TODOs baserat på titel/beskrivning
4. **Notifikationer**: Desktop-notiser för uppgifter nära deadline
5. **Databas**: Använd SQLite istället för JSON

---

## Projekt 3: Dataanalys-script med pandas 📊

**Nivå:** 5 (Expert)
**Tidsåtgång:** 2-3 timmar
**Koncept:** pandas, numpy, data science, visualisering

### Projektbeskrivning

Skapa ett komplett dataanalys-verktyg som kan:
- Läsa CSV/Excel-filer
- Rensa och transformera data
- Utföra statistisk analys
- Skapa visualiseringar
- Generera rapport

### Fullständig kod

```python
"""
Dataanalys-verktyg
Analyserar försäljningsdata och genererar rapport
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List
import json

class FörsäljningsAnalys:
    """Analyserar försäljningsdata och genererar insikter."""

    def __init__(self, csv_fil: str):
        """
        Initierar analysen med en CSV-fil.

        Args:
            csv_fil: Sökväg till CSV-fil med försäljningsdata
        """
        self.df = None
        self.csv_fil = csv_fil
        self.rapport_fil = "försäljningsrapport.txt"
        self.ladda_data()

    def ladda_data(self):
        """Laddar data från CSV-fil."""
        try:
            self.df = pd.read_csv(self.csv_fil)
            print(f"✅ Laddade {len(self.df)} rader från {self.csv_fil}")
        except FileNotFoundError:
            print(f"❌ Filen {self.csv_fil} hittades inte!")
            print("Skapar exempel-data...")
            self.skapa_exempel_data()

    def skapa_exempel_data(self):
        """Skapar exempel-data för demonstration."""
        np.random.seed(42)

        datum_range = pd.date_range("2024-01-01", "2024-12-31", freq="D")
        n = len(datum_range)

        data = {
            "Datum": datum_range,
            "Produkt": np.random.choice(["Laptop", "Telefon", "Surfplatta", "Hörlurar"], n),
            "Kategori": np.random.choice(["Elektronik"], n),
            "Försäljning": np.random.randint(10000, 100000, n),
            "Antal": np.random.randint(1, 20, n),
            "Region": np.random.choice(["Stockholm", "Göteborg", "Malmö", "Uppsala"], n)
        }

        self.df = pd.DataFrame(data)
        self.df.to_csv(self.csv_fil, index=False)
        print(f"✅ Skapade exempel-data med {len(self.df)} rader")

    def översikt(self):
        """Visar översikt av data."""
        print("\n" + "=" * 60)
        print("📊 DATAÖVERSIKT")
        print("=" * 60)

        print(f"\nAntal rader: {len(self.df)}")
        print(f"Antal kolumner: {len(self.df.columns)}")
        print(f"\nKolumner: {', '.join(self.df.columns)}")

        print("\n--- Första 5 raderna ---")
        print(self.df.head())

        print("\n--- Datatyper ---")
        print(self.df.dtypes)

        print("\n--- Saknade värden ---")
        print(self.df.isnull().sum())

    def rensa_data(self):
        """Rensar och förbereder data."""
        print("\n🧹 Rensar data...")

        # Ta bort dubbletter
        före = len(self.df)
        self.df = self.df.drop_duplicates()
        efter = len(self.df)

        if före != efter:
            print(f"  ✓ Tog bort {före - efter} dubbletter")

        # Konvertera datum
        if "Datum" in self.df.columns:
            self.df["Datum"] = pd.to_datetime(self.df["Datum"])
            print("  ✓ Konverterade datum")

        # Ta bort saknade värden
        före = len(self.df)
        self.df = self.df.dropna()
        efter = len(self.df)

        if före != efter:
            print(f"  ✓ Tog bort {före - efter} rader med saknade värden")

        print("✅ Data rensad!")

    def beräkna_statistik(self) -> Dict:
        """Beräknar statistik från data."""
        print("\n📈 Beräknar statistik...")

        stats = {}

        # Total försäljning
        stats["total_försäljning"] = self.df["Försäljning"].sum()
        stats["genomsnitt_försäljning"] = self.df["Försäljning"].mean()
        stats["median_försäljning"] = self.df["Försäljning"].median()

        # Försäljning per produkt
        stats["per_produkt"] = self.df.groupby("Produkt")["Försäljning"].sum().to_dict()

        # Försäljning per region
        stats["per_region"] = self.df.groupby("Region")["Försäljning"].sum().to_dict()

        # Bästa dag
        bästa_dag = self.df.groupby("Datum")["Försäljning"].sum().idxmax()
        bästa_dag_försäljning = self.df.groupby("Datum")["Försäljning"].sum().max()

        stats["bästa_dag"] = {
            "datum": str(bästa_dag),
            "försäljning": bästa_dag_försäljning
        }

        # Top 5 produkter
        top_produkter = self.df.groupby("Produkt")["Försäljning"].sum().nlargest(5)
        stats["top_5_produkter"] = top_produkter.to_dict()

        return stats

    def visa_statistik(self, stats: Dict):
        """Visar statistik på ett snyggt sätt."""
        print("\n" + "=" * 60)
        print("📊 FÖRSÄLJNINGSSTATISTIK")
        print("=" * 60)

        print(f"\n💰 Total försäljning: {stats['total_försäljning']:,.0f} kr")
        print(f"📊 Genomsnitt per dag: {stats['genomsnitt_försäljning']:,.0f} kr")
        print(f"📊 Median per dag: {stats['median_försäljning']:,.0f} kr")

        print(f"\n🏆 Bästa dag: {stats['bästa_dag']['datum']}")
        print(f"   Försäljning: {stats['bästa_dag']['försäljning']:,.0f} kr")

        print("\n📦 Försäljning per produkt:")
        for produkt, belopp in sorted(stats['per_produkt'].items(), key=lambda x: x[1], reverse=True):
            print(f"   {produkt:15}: {belopp:>10,.0f} kr")

        print("\n🗺️ Försäljning per region:")
        for region, belopp in sorted(stats['per_region'].items(), key=lambda x: x[1], reverse=True):
            print(f"   {region:15}: {belopp:>10,.0f} kr")

    def skapa_visualiseringar(self, stats: Dict):
        """Skapar visualiseringar av data."""
        print("\n📈 Skapar visualiseringar...")

        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle("Försäljningsanalys", fontsize=16, fontweight="bold")

        # 1. Försäljning per produkt (stapeldiagram)
        ax1 = axes[0, 0]
        produkter = list(stats['per_produkt'].keys())
        värden = list(stats['per_produkt'].values())
        ax1.bar(produkter, värden, color="skyblue")
        ax1.set_title("Försäljning per produkt")
        ax1.set_ylabel("Försäljning (kr)")
        ax1.tick_params(axis="x", rotation=45)

        # 2. Försäljning per region (cirkeldiagram)
        ax2 = axes[0, 1]
        regioner = list(stats['per_region'].keys())
        värden_region = list(stats['per_region'].values())
        ax2.pie(värden_region, labels=regioner, autopct="%1.1f%%", startangle=90)
        ax2.set_title("Försäljning per region (%)")

        # 3. Försäljning över tid (linjediagram)
        ax3 = axes[1, 0]
        per_datum = self.df.groupby("Datum")["Försäljning"].sum()
        ax3.plot(per_datum.index, per_datum.values, color="green")
        ax3.set_title("Försäljning över tid")
        ax3.set_ylabel("Försäljning (kr)")
        ax3.tick_params(axis="x", rotation=45)

        # 4. Antal sålda produkter (stapeldiagram)
        ax4 = axes[1, 1]
        per_produkt_antal = self.df.groupby("Produkt")["Antal"].sum()
        ax4.bar(per_produkt_antal.index, per_produkt_antal.values, color="coral")
        ax4.set_title("Antal sålda enheter")
        ax4.set_ylabel("Antal")
        ax4.tick_params(axis="x", rotation=45)

        plt.tight_layout()
        plt.savefig("försäljningsanalys.png", dpi=300, bbox_inches="tight")
        print("✅ Visualiseringar sparade till försäljningsanalys.png")

        # Visa grafer
        # plt.show()

    def generera_rapport(self, stats: Dict):
        """Genererar en textrapport."""
        print("\n📝 Genererar rapport...")

        with open(self.rapport_fil, "w", encoding="utf-8") as f:
            f.write("=" * 70 + "\n")
            f.write("FÖRSÄLJNINGSRAPPORT\n")
            f.write(f"Genererad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 70 + "\n\n")

            f.write("SAMMANFATTNING\n")
            f.write("-" * 70 + "\n")
            f.write(f"Total försäljning: {stats['total_försäljning']:,.0f} kr\n")
            f.write(f"Genomsnitt per dag: {stats['genomsnitt_försäljning']:,.0f} kr\n")
            f.write(f"Median per dag: {stats['median_försäljning']:,.0f} kr\n\n")

            f.write(f"Bästa dag: {stats['bästa_dag']['datum']}\n")
            f.write(f"Försäljning bästa dag: {stats['bästa_dag']['försäljning']:,.0f} kr\n\n")

            f.write("FÖRSÄLJNING PER PRODUKT\n")
            f.write("-" * 70 + "\n")
            for produkt, belopp in sorted(stats['per_produkt'].items(), key=lambda x: x[1], reverse=True):
                procent = (belopp / stats['total_försäljning']) * 100
                f.write(f"{produkt:20}: {belopp:>12,.0f} kr ({procent:5.1f}%)\n")

            f.write("\n")
            f.write("FÖRSÄLJNING PER REGION\n")
            f.write("-" * 70 + "\n")
            for region, belopp in sorted(stats['per_region'].items(), key=lambda x: x[1], reverse=True):
                procent = (belopp / stats['total_försäljning']) * 100
                f.write(f"{region:20}: {belopp:>12,.0f} kr ({procent:5.1f}%)\n")

        print(f"✅ Rapport sparad till {self.rapport_fil}")

    def kör_fullständig_analys(self):
        """Kör komplett analys-pipeline."""
        print("\n🚀 Startar fullständig analys...\n")

        # 1. Visa översikt
        self.översikt()

        # 2. Rensa data
        self.rensa_data()

        # 3. Beräkna statistik
        stats = self.beräkna_statistik()

        # 4. Visa statistik
        self.visa_statistik(stats)

        # 5. Skapa visualiseringar
        self.skapa_visualiseringar(stats)

        # 6. Generera rapport
        self.generera_rapport(stats)

        print("\n✅ Analys klar!")
        print(f"   📊 Grafer: försäljningsanalys.png")
        print(f"   📝 Rapport: {self.rapport_fil}")

def main():
    """Huvudfunktion."""
    analys = FörsäljningsAnalys("försäljning.csv")
    analys.kör_fullständig_analys()

if __name__ == "__main__":
    main()
```

### Installation av beroenden

```bash
pip install pandas numpy matplotlib openpyxl
```

### Utmaningar för att utöka projektet

1. **Förutsägelse**: Använd ML för att förutsäga framtida försäljning
2. **Dashboard**: Skapa interaktiv dashboard med Plotly/Dash
3. **Flera filer**: Hantera och jämföra flera försäljnings-filer
4. **Anomali-detektion**: Hitta avvikande försäljningsmönster
5. **Export till Excel**: Generera Excel-rapport med grafer

---

## 🎯 Projektutmaningar

### Allmänna utmaningar för alla projekt

1. **Error handling**: Förbättra felhanteringen
2. **Unit testing**: Skriv pytest-tester för alla funktioner
3. **Dokumentation**: Lägg till detaljerade docstrings
4. **Logging**: Implementera logging istället för print
5. **Configuration**: Använd config-fil för inställningar

### Bonusutmaningar

1. **Kombinera projekten**: Skapa en dashboard som visar TODO + Försäljningsdata
2. **Webb-version**: Konvertera till Flask/FastAPI-applikation
3. **Databas**: Migrera till SQLite eller PostgreSQL
4. **CI/CD**: Sätt upp automatisk testning med GitHub Actions
5. **Docker**: Containerisera applikationerna

---

## 🎓 Sammanfattning

Dessa tre projekt täcker hela spektrumet av Python-programmering:

✅ **Projekt 1 (Kalkylator)**: Funktioner, loopar, filhantering, error handling
✅ **Projekt 2 (TODO-app)**: OOP, GUI, dataclasses, event-driven programming
✅ **Projekt 3 (Dataanalys)**: pandas, numpy, visualisering, rapportgenerering

Genom att bygga och utöka dessa projekt får du verklig erfarenhet av:
- Planering och arkitektur
- Clean code principles
- Testing och debugging
- Användarinteraktion
- Datahantering

**Grattis till att ha byggt tre kompletta Python-applikationer!** 🎉

---

**Fortsätt till:** [FAQ →](Python_Guide_07_FAQ.md)

**Tillbaka till:** [Översikt ←](Python_Guide_00_Overview.md)
