#!/usr/bin/env python3
"""
Chat History Exporter
Exporterar chatthistorik från Grok (X) och ChatGPT
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path

# Importera exportmoduler
from exporters.chatgpt_exporter import ChatGPTExporter
from exporters.grok_exporter import GrokExporter


class ChatHistoryExporter:
    """Huvudklass för att exportera chatthistorik från olika tjänster"""

    def __init__(self, config_path="config.json"):
        """
        Initialisera exportören

        Args:
            config_path: Sökväg till konfigurationsfil
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.output_dir = Path(self.config.get("output_directory", "exports"))
        self.output_dir.mkdir(exist_ok=True)

    def _load_config(self):
        """Ladda konfiguration från fil"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️  Konfigurationsfil {self.config_path} hittades inte.")
            print("Använder standardinställningar.")
            return {}
        except json.JSONDecodeError as e:
            print(f"❌ Fel vid läsning av konfigurationsfil: {e}")
            return {}

    def export_chatgpt(self):
        """Exportera ChatGPT-historik"""
        print("\n🤖 Exporterar ChatGPT-historik...")
        try:
            config = self.config.get("chatgpt", {})
            exporter = ChatGPTExporter(
                api_key=config.get("api_key"),
                cookies=config.get("cookies")
            )

            conversations = exporter.export_conversations()

            if conversations:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = self.output_dir / f"chatgpt_export_{timestamp}.json"

                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(conversations, f, ensure_ascii=False, indent=2)

                print(f"✅ ChatGPT-historik exporterad till: {output_file}")
                print(f"   Antal konversationer: {len(conversations)}")
                return True
            else:
                print("⚠️  Inga konversationer hittades")
                return False

        except Exception as e:
            print(f"❌ Fel vid export av ChatGPT: {e}")
            return False

    def export_grok(self):
        """Exportera Grok/X-historik"""
        print("\n🔷 Exporterar Grok (X)-historik...")
        try:
            config = self.config.get("grok", {})
            exporter = GrokExporter(
                auth_token=config.get("auth_token"),
                cookies=config.get("cookies")
            )

            conversations = exporter.export_conversations()

            if conversations:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_file = self.output_dir / f"grok_export_{timestamp}.json"

                with open(output_file, 'w', encoding='utf-8') as f:
                    json.dump(conversations, f, ensure_ascii=False, indent=2)

                print(f"✅ Grok-historik exporterad till: {output_file}")
                print(f"   Antal konversationer: {len(conversations)}")
                return True
            else:
                print("⚠️  Inga konversationer hittades")
                return False

        except Exception as e:
            print(f"❌ Fel vid export av Grok: {e}")
            return False

    def export_all(self):
        """Exportera från alla tjänster"""
        print("🚀 Startar export från alla tjänster...")
        print("=" * 60)

        results = {
            "chatgpt": self.export_chatgpt(),
            "grok": self.export_grok()
        }

        print("\n" + "=" * 60)
        print("📊 Sammanfattning:")
        for service, success in results.items():
            status = "✅ Lyckades" if success else "❌ Misslyckades"
            print(f"   {service.upper()}: {status}")

        return all(results.values())


def main():
    """Huvudfunktion"""
    parser = argparse.ArgumentParser(
        description="Exportera chatthistorik från Grok och ChatGPT"
    )
    parser.add_argument(
        '--service',
        choices=['all', 'chatgpt', 'grok'],
        default='all',
        help='Vilken tjänst att exportera från (standard: all)'
    )
    parser.add_argument(
        '--config',
        default='config.json',
        help='Sökväg till konfigurationsfil (standard: config.json)'
    )
    parser.add_argument(
        '--output',
        help='Output-katalog (överskrider config)'
    )

    args = parser.parse_args()

    # Skapa exportör
    exporter = ChatHistoryExporter(config_path=args.config)

    # Överskriv output-katalog om specificerad
    if args.output:
        exporter.output_dir = Path(args.output)
        exporter.output_dir.mkdir(exist_ok=True)

    # Exportera baserat på val
    if args.service == 'all':
        success = exporter.export_all()
    elif args.service == 'chatgpt':
        success = exporter.export_chatgpt()
    elif args.service == 'grok':
        success = exporter.export_grok()

    # Exit med lämplig statuskod
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
