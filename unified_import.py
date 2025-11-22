#!/usr/bin/env python3
"""
Unified Import Script för PostgreSQL
Importerar BÅDE Grok och ChatGPT JSON-filer till samma databas

Användning:
    python unified_import.py grok_export.json chatgpt_export.json
    python unified_import.py exports/*.json
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

# Ladda environment variables
load_dotenv()


class UnifiedImporter:
    """Importerar chat-historik från Grok och ChatGPT till PostgreSQL"""

    def __init__(self):
        """Initialisera databas-connection"""
        self.conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            dbname=os.getenv("POSTGRES_DB", "chat_history"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", "")
        )
        self.cur = self.conn.cursor()
        print(f"✅ Ansluten till databas: {os.getenv('POSTGRES_DB', 'chat_history')}")

    def import_grok(self, file_path: str) -> int:
        """
        Importera Grok JSON-export

        Args:
            file_path: Sökväg till JSON-fil

        Returns:
            Antal importerade konversationer
        """
        print(f"\n📥 Importerar Grok från: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        conversations = data.get('conversations', [])
        if not conversations:
            print("⚠️  Inga konversationer hittades")
            return 0

        count = 0
        for conv in conversations:
            try:
                title = conv.get('title', 'Untitled')
                project = conv.get('project')

                # Infoga konversation
                self.cur.execute(
                    """
                    INSERT INTO conversations (source, title, project)
                    VALUES ('grok', %s, %s)
                    RETURNING id
                    """,
                    (title, project)
                )
                conv_id = self.cur.fetchone()[0]

                # Infoga meddelanden
                messages = conv.get('messages', [])
                if messages:
                    msg_values = [
                        (conv_id, msg.get('role', 'user'), msg.get('content', ''), idx)
                        for idx, msg in enumerate(messages)
                    ]
                    execute_values(
                        self.cur,
                        """
                        INSERT INTO messages (conversation_id, role, content, message_order)
                        VALUES %s
                        """,
                        msg_values
                    )

                count += 1

            except Exception as e:
                print(f"⚠️  Fel vid import av konversation '{title}': {e}")
                continue

        self.conn.commit()
        print(f"✅ Importerade {count} Grok-konversationer")
        return count

    def import_chatgpt(self, file_path: str) -> int:
        """
        Importera ChatGPT JSON-export

        Args:
            file_path: Sökväg till JSON-fil

        Returns:
            Antal importerade konversationer
        """
        print(f"\n📥 Importerar ChatGPT från: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # ChatGPT-export kan vara antingen en lista eller ett objekt med 'conversations'
        if isinstance(data, list):
            conversations = data
        else:
            conversations = data.get('conversations', [])

        if not conversations:
            print("⚠️  Inga konversationer hittades")
            return 0

        count = 0
        for conv in conversations:
            try:
                title = conv.get('title', 'Untitled ChatGPT')
                create_time = conv.get('create_time')

                # Infoga konversation
                self.cur.execute(
                    """
                    INSERT INTO conversations (source, title, created_at)
                    VALUES ('chatgpt', %s, %s)
                    RETURNING id
                    """,
                    (title, create_time)
                )
                conv_id = self.cur.fetchone()[0]

                # Extrahera meddelanden från ChatGPT's mapping-struktur
                mapping = conv.get('mapping', {})
                messages = []

                for node_id in sorted(
                    mapping.keys(),
                    key=lambda k: mapping[k].get('message', {}).get('create_time', 0) or 0
                ):
                    node = mapping[node_id]
                    msg = node.get('message')

                    if not msg:
                        continue

                    content_parts = msg.get('content', {}).get('parts', [])
                    if not content_parts:
                        continue

                    role = msg.get('author', {}).get('role', 'user')
                    content = '\n'.join(str(part) for part in content_parts)

                    messages.append({
                        'role': role,
                        'content': content
                    })

                # Infoga meddelanden
                if messages:
                    msg_values = [
                        (conv_id, msg['role'], msg['content'], idx)
                        for idx, msg in enumerate(messages)
                    ]
                    execute_values(
                        self.cur,
                        """
                        INSERT INTO messages (conversation_id, role, content, message_order)
                        VALUES %s
                        """,
                        msg_values
                    )

                count += 1

            except Exception as e:
                print(f"⚠️  Fel vid import av konversation: {e}")
                continue

        self.conn.commit()
        print(f"✅ Importerade {count} ChatGPT-konversationer")
        return count

    def import_file(self, file_path: str) -> int:
        """
        Importera från fil - detektera automatiskt typ

        Args:
            file_path: Sökväg till JSON-fil

        Returns:
            Antal importerade konversationer
        """
        file_path = str(file_path)

        # Detektera filtyp från filnamn eller innehåll
        if 'grok' in file_path.lower():
            return self.import_grok(file_path)
        elif 'chatgpt' in file_path.lower():
            return self.import_chatgpt(file_path)
        else:
            # Försök detektera från innehåll
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                if data.get('source') == 'grok':
                    return self.import_grok(file_path)
                elif isinstance(data, list) or 'mapping' in str(data):
                    return self.import_chatgpt(file_path)
                else:
                    print(f"⚠️  Kunde inte detektera filtyp för: {file_path}")
                    print("   Försöker importera som ChatGPT...")
                    return self.import_chatgpt(file_path)

            except Exception as e:
                print(f"❌ Fel vid läsning av fil {file_path}: {e}")
                return 0

    def get_stats(self):
        """Visa statistik om importerad data"""
        print("\n📊 Databasstatistik:")
        print("=" * 60)

        # Totalt antal konversationer
        self.cur.execute("SELECT COUNT(*) FROM conversations")
        total_convs = self.cur.fetchone()[0]
        print(f"Totalt konversationer: {total_convs:,}")

        # Per källa
        self.cur.execute("""
            SELECT source, COUNT(*) as count
            FROM conversations
            GROUP BY source
            ORDER BY count DESC
        """)
        for row in self.cur.fetchall():
            print(f"  - {row[0].upper()}: {row[1]:,}")

        # Totalt antal meddelanden
        self.cur.execute("SELECT COUNT(*) FROM messages")
        total_msgs = self.cur.fetchone()[0]
        print(f"\nTotalt meddelanden: {total_msgs:,}")

        # Meddelanden per roll
        self.cur.execute("""
            SELECT role, COUNT(*) as count
            FROM messages
            GROUP BY role
            ORDER BY count DESC
        """)
        for row in self.cur.fetchall():
            print(f"  - {row[0].capitalize()}: {row[1]:,}")

        # Collections
        self.cur.execute("SELECT COUNT(*) FROM collections")
        total_colls = self.cur.fetchone()[0]
        if total_colls > 0:
            print(f"\nCollections: {total_colls:,}")

        print("=" * 60)

    def close(self):
        """Stäng databas-connection"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("\n✅ Databas-connection stängd")


def main():
    """Huvudfunktion"""
    if len(sys.argv) < 2:
        print("❌ Användning: python unified_import.py <fil1.json> <fil2.json> ...")
        print("\nExempel:")
        print("  python unified_import.py grok_export.json")
        print("  python unified_import.py exports/*.json")
        print("  python unified_import.py grok.json chatgpt.json")
        sys.exit(1)

    # Kontrollera .env
    if not os.path.exists('.env'):
        print("⚠️  .env-fil saknas!")
        print("   Kopiera .env.example till .env och fyll i databasuppgifter")
        print("   Fortsätter med standardvärden...")

    # Skapa importer
    try:
        importer = UnifiedImporter()
    except Exception as e:
        print(f"❌ Kunde inte ansluta till databas: {e}")
        print("\n💡 Tips:")
        print("  1. Kontrollera att PostgreSQL körs")
        print("  2. Verifiera databasuppgifter i .env")
        print("  3. Kör SQL-schemat först (se README)")
        sys.exit(1)

    # Importera alla filer
    total_imported = 0
    for file_path in sys.argv[1:]:
        path = Path(file_path)
        if path.exists():
            count = importer.import_file(file_path)
            total_imported += count
        else:
            print(f"⚠️  Fil hittades inte: {file_path}")

    # Visa statistik
    if total_imported > 0:
        importer.get_stats()
    else:
        print("\n⚠️  Inga konversationer importerades")

    # Stäng connection
    importer.close()

    print(f"\n🎉 Import klar! {total_imported} konversationer importerade totalt.")


if __name__ == "__main__":
    main()
