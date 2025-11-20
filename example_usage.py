#!/usr/bin/env python3
"""
Exempel på hur man använder chatthistorik-exportörerna programmatiskt
"""

import json
from pathlib import Path
from exporters.chatgpt_exporter import ChatGPTExporter
from exporters.grok_exporter import GrokExporter, GrokSeleniumExporter


def export_chatgpt_example():
    """Exempel: Exportera ChatGPT-konversationer"""
    print("=" * 60)
    print("ChatGPT Export Exempel")
    print("=" * 60)

    # Metod 1: Med session cookies
    cookies = {
        "__Secure-next-auth.session-token": "din-session-token-här"
    }

    exporter = ChatGPTExporter(cookies=cookies)
    conversations = exporter.export_conversations()

    # Spara som JSON
    output_file = "chatgpt_backup.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(conversations, f, ensure_ascii=False, indent=2)

    print(f"✅ Exporterade {len(conversations)} konversationer till {output_file}")

    # Spara som Markdown
    markdown_file = "chatgpt_backup.md"
    exporter.export_to_markdown(conversations, markdown_file)

    # Metod 2: Med API-nyckel (för framtida användning)
    # api_exporter = ChatGPTExporter(api_key="sk-...")
    # conversations = api_exporter.export_conversations()


def export_grok_example():
    """Exempel: Exportera Grok-konversationer"""
    print("\n" + "=" * 60)
    print("Grok Export Exempel")
    print("=" * 60)

    # Metod 1: Med auth token
    auth_token = "din-auth-token-här"
    cookies = {
        "auth_token": auth_token,
        "ct0": "din-csrf-token-här"
    }

    exporter = GrokExporter(auth_token=auth_token, cookies=cookies)
    conversations = exporter.export_conversations()

    if conversations:
        # Spara som JSON
        output_file = "grok_backup.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, ensure_ascii=False, indent=2)

        print(f"✅ Exporterade {len(conversations)} konversationer till {output_file}")

        # Spara som Markdown
        markdown_file = "grok_backup.md"
        exporter.export_to_markdown(conversations, markdown_file)


def export_grok_with_selenium():
    """Exempel: Exportera Grok med Selenium"""
    print("\n" + "=" * 60)
    print("Grok Selenium Export Exempel")
    print("=" * 60)

    cookies = {
        "auth_token": "din-auth-token-här",
        "ct0": "din-csrf-token-här"
    }

    exporter = GrokSeleniumExporter(cookies=cookies)
    conversations = exporter.export_conversations()

    if conversations:
        output_file = "grok_selenium_backup.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, ensure_ascii=False, indent=2)

        print(f"✅ Exporterade {len(conversations)} konversationer")


def scheduled_backup_example():
    """Exempel: Automatiserad backup"""
    print("\n" + "=" * 60)
    print("Automatiserad Backup Exempel")
    print("=" * 60)

    # Skapa backup-katalog med datum
    from datetime import datetime
    backup_dir = Path("backups") / datetime.now().strftime("%Y-%m-%d")
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Ladda config
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Exportera ChatGPT
    chatgpt_config = config.get('chatgpt', {})
    if chatgpt_config.get('cookies'):
        print("\n📥 Exporterar ChatGPT...")
        exporter = ChatGPTExporter(cookies=chatgpt_config['cookies'])
        conversations = exporter.export_conversations()

        output_file = backup_dir / "chatgpt.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, ensure_ascii=False, indent=2)

        print(f"✅ ChatGPT-backup klar: {output_file}")

    # Exportera Grok
    grok_config = config.get('grok', {})
    if grok_config.get('auth_token'):
        print("\n📥 Exporterar Grok...")
        exporter = GrokExporter(
            auth_token=grok_config['auth_token'],
            cookies=grok_config.get('cookies')
        )
        conversations = exporter.export_conversations()

        if conversations:
            output_file = backup_dir / "grok.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(conversations, f, ensure_ascii=False, indent=2)

            print(f"✅ Grok-backup klar: {output_file}")

    print(f"\n✅ Alla backups sparade i: {backup_dir}")


def filter_conversations_example():
    """Exempel: Filtrera konversationer"""
    print("\n" + "=" * 60)
    print("Filtrera Konversationer Exempel")
    print("=" * 60)

    # Ladda exporterade konversationer
    with open('exports/chatgpt_export_latest.json', 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    # Filtrera efter datum
    from datetime import datetime, timedelta
    one_month_ago = datetime.now() - timedelta(days=30)

    recent_conversations = [
        conv for conv in conversations
        if datetime.fromisoformat(conv.get('create_time', '')) > one_month_ago
    ]

    print(f"📊 Totalt: {len(conversations)} konversationer")
    print(f"📊 Senaste månaden: {len(recent_conversations)} konversationer")

    # Filtrera efter sökord
    keyword = "python"
    keyword_conversations = [
        conv for conv in conversations
        if keyword.lower() in str(conv.get('title', '')).lower()
    ]

    print(f"📊 Med nyckelord '{keyword}': {len(keyword_conversations)} konversationer")

    # Spara filtrerade konversationer
    output_file = f"filtered_{keyword}_conversations.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(keyword_conversations, f, ensure_ascii=False, indent=2)

    print(f"✅ Filtrerade konversationer sparade: {output_file}")


def main():
    """Huvudfunktion - kör alla exempel"""
    print("\n🚀 Chat History Exporter - Användningsexempel")
    print("=" * 60)

    # Visa instruktioner
    print("\n📝 Instruktioner:")
    print("1. Kopiera config.example.json till config.json")
    print("2. Lägg till dina autentiseringsuppgifter i config.json")
    print("3. Kör detta script eller använd chat_history_exporter.py")
    print("\n" + "=" * 60)

    # Kör exempel (kommenterade som standard)
    # Avkommentera de exempel du vill köra:

    # export_chatgpt_example()
    # export_grok_example()
    # export_grok_with_selenium()
    # scheduled_backup_example()
    # filter_conversations_example()

    print("\n✅ För att köra exemplen, avkommentera dem i main()-funktionen")


if __name__ == "__main__":
    main()
