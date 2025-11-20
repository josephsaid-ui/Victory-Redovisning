# Chat History Exporter 💬

Ett Python-script för att exportera chatthistorik från Grok (X) och ChatGPT.

## 📋 Funktioner

- ✅ Exportera ChatGPT-konversationer
- ✅ Exportera Grok (X)-konversationer
- ✅ Spara som JSON och Markdown
- ✅ Automatisk rate limiting
- ✅ Stöd för både API och web scraping

## 🚀 Snabbstart

### 1. Installation

```bash
# Klona repot
git clone <repo-url>
cd Victory-Redovisning

# Installera dependencies
pip install -r requirements.txt
```

### 2. Konfiguration

Kopiera exempel-konfigurationen:
```bash
cp config.example.json config.json
```

Redigera `config.json` med dina autentiseringsuppgifter (se nedan).

### 3. Kör scriptet

```bash
# Exportera från alla tjänster
python chat_history_exporter.py

# Exportera endast från ChatGPT
python chat_history_exporter.py --service chatgpt

# Exportera endast från Grok
python chat_history_exporter.py --service grok

# Specificera output-katalog
python chat_history_exporter.py --output my_exports
```

## 🔑 Autentisering

### ChatGPT

#### Metod 1: Via Session Cookies (Rekommenderas)

1. Gå till [chatgpt.com](https://chatgpt.com) och logga in
2. Öppna Developer Tools (F12)
3. Gå till **Application** > **Cookies** > `https://chatgpt.com`
4. Kopiera värdet för `__Secure-next-auth.session-token`
5. Lägg till i `config.json`:

```json
{
  "chatgpt": {
    "cookies": {
      "__Secure-next-auth.session-token": "din-session-token-här"
    }
  }
}
```

#### Metod 2: Via OpenAI API

```json
{
  "chatgpt": {
    "api_key": "sk-..."
  }
}
```

**OBS:** OpenAI API:et lagrar inte chatthistorik automatiskt. Använd cookies-metoden för att exportera befintliga konversationer.

### Grok (X)

1. Gå till [x.com](https://x.com) och logga in
2. Öppna Developer Tools (F12)
3. Gå till **Application** > **Cookies** > `https://x.com`
4. Kopiera följande cookies:
   - `auth_token`
   - `ct0` (CSRF token)
5. Lägg till i `config.json`:

```json
{
  "grok": {
    "auth_token": "din-auth-token-här",
    "cookies": {
      "auth_token": "din-auth-token-här",
      "ct0": "din-csrf-token-här"
    }
  }
}
```

**OBS:** Grok har inget officiellt API ännu. Scriptet försöker reverse-engineera deras webbgränssnitt, men manuell export kan behövas.

## 📁 Projektstruktur

```
Victory-Redovisning/
├── chat_history_exporter.py   # Huvudscript
├── exporters/
│   ├── __init__.py
│   ├── chatgpt_exporter.py    # ChatGPT-modul
│   └── grok_exporter.py       # Grok-modul
├── config.json                # Din konfiguration (skapa från example)
├── config.example.json        # Exempel-konfiguration
├── requirements.txt           # Python dependencies
├── exports/                   # Output-katalog (skapas automatiskt)
│   ├── chatgpt_export_*.json
│   └── grok_export_*.json
└── README.md                  # Denna fil
```

## 🔧 Konfiguration

### Fullständig config.json

```json
{
  "output_directory": "exports",
  "chatgpt": {
    "api_key": "",
    "cookies": {
      "__Secure-next-auth.session-token": "your-session-token-here",
      "__Secure-next-auth.callback-url": "https://chatgpt.com"
    }
  },
  "grok": {
    "auth_token": "your-x-auth-token-here",
    "cookies": {
      "auth_token": "your-x-auth-token-here",
      "ct0": "your-csrf-token-here"
    }
  }
}
```

## 📊 Export-format

### JSON

Konversationer exporteras som JSON med fullständig metadata:

```json
[
  {
    "id": "conv-123",
    "title": "Konversationstitel",
    "create_time": "2024-01-01T12:00:00Z",
    "messages": [
      {
        "role": "user",
        "content": "Hej!"
      },
      {
        "role": "assistant",
        "content": "Hej! Hur kan jag hjälpa dig?"
      }
    ]
  }
]
```

### Markdown

Du kan också exportera till Markdown-format för bättre läsbarhet.

## 🛠️ Avancerad användning

### Selenium-baserad export (för Grok)

För mer robust export från Grok, använd Selenium:

```python
from exporters.grok_exporter import GrokSeleniumExporter

exporter = GrokSeleniumExporter(cookies={"auth_token": "..."})
conversations = exporter.export_conversations()
```

Detta kräver Chrome/Chromium installerat på systemet.

## ⚠️ Viktiga noteringar

### ChatGPT
- ✅ Fungerar via session cookies
- ⚠️ Tokens kan upphöra - logga in igen om det inte fungerar
- ⚠️ Rate limiting kan tillämpas - scriptet pausar automatiskt

### Grok
- ⚠️ Inget officiellt API tillgängligt
- ⚠️ Metoden baseras på reverse engineering
- ⚠️ Kan sluta fungera om X ändrar sitt API
- 💡 Manuell export kan behövas (se instruktioner i output)

## 🔒 Säkerhet

**VIKTIGT:**
- ⚠️ Dela **ALDRIG** din `config.json` med andra
- ⚠️ Lägg aldrig till `config.json` i git
- ✅ `config.json` är redan i `.gitignore`
- ✅ Session tokens och API-nycklar är känsliga
- ✅ Behandla dem som lösenord

## 🐛 Felsökning

### "Kunde inte autentisera"
- Kontrollera att dina cookies/tokens är korrekta
- Logga in igen och hämta nya cookies
- Tokens kan ha upphört

### "Inga konversationer hittades"
- Kontrollera att du har konversationer att exportera
- Verifiera autentiseringen
- Kolla console output för mer detaljer

### Rate limiting
- Scriptet pausar automatiskt mellan requests
- Om du får för många fel, vänta några minuter

### Grok fungerar inte
- Grok har inget officiellt API
- Reverse engineering kan sluta fungera
- Prova manuell export (se instruktioner i output)

## 📝 Licens

MIT License - Se LICENSE-fil för detaljer.

## 🤝 Bidrag

Bidrag är välkomna! Öppna gärna en issue eller pull request.

## 📞 Support

Om du stöter på problem:
1. Kontrollera felsökningssektionen ovan
2. Se till att dependencies är installerade
3. Verifiera din konfiguration
4. Öppna en issue på GitHub

## 🔄 Uppdateringar

Scriptet uppdateras regelbundet för att följa ändringar i API:er. Kör:

```bash
git pull
pip install -r requirements.txt --upgrade
```

## ⚡ Tips

- Kör export regelbundet för att hålla backup uppdaterad
- Spara exports på en säker plats
- Överväg att automatisera med cron/Task Scheduler
- Använd `--output` för att organisera exports per datum