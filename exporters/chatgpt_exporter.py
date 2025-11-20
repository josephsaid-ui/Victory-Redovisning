"""
ChatGPT Exporter
Exporterar konversationshistorik från ChatGPT
"""

import requests
import json
import time
from typing import List, Dict, Optional


class ChatGPTExporter:
    """Exporterar konversationer från ChatGPT"""

    def __init__(self, api_key: Optional[str] = None, cookies: Optional[Dict] = None):
        """
        Initialisera ChatGPT-exportern

        Args:
            api_key: OpenAI API-nyckel (för API-baserad export)
            cookies: Session cookies från chatgpt.com (för web scraping)
        """
        self.api_key = api_key
        self.cookies = cookies
        self.base_url = "https://chatgpt.com/backend-api"
        self.session = requests.Session()

        if cookies:
            self.session.cookies.update(cookies)

    def _get_auth_headers(self) -> Dict[str, str]:
        """Skapa autentiseringsheaders"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        return headers

    def export_conversations(self) -> List[Dict]:
        """
        Exportera alla konversationer från ChatGPT

        Returns:
            Lista med konversationer
        """
        if self.cookies:
            return self._export_via_web()
        elif self.api_key:
            return self._export_via_api()
        else:
            print("⚠️  Ingen autentisering konfigurerad för ChatGPT")
            print("   Lägg till antingen 'api_key' eller 'cookies' i config.json")
            return []

    def _export_via_web(self) -> List[Dict]:
        """
        Exportera via ChatGPT webbgränssnitt

        Denna metod använder ChatGPT's backend API som används av webbgränssnittet.
        """
        try:
            # Hämta användarens session
            session_url = f"{self.base_url}/me"
            response = self.session.get(session_url, headers=self._get_auth_headers())

            if response.status_code != 200:
                print(f"❌ Kunde inte autentisera: {response.status_code}")
                return []

            # Hämta konversationslista
            conversations_url = f"{self.base_url}/conversations?offset=0&limit=100"
            response = self.session.get(conversations_url, headers=self._get_auth_headers())

            if response.status_code != 200:
                print(f"❌ Kunde inte hämta konversationer: {response.status_code}")
                return []

            data = response.json()
            conversation_list = data.get('items', [])

            print(f"📥 Hämtar {len(conversation_list)} konversationer...")

            # Hämta detaljer för varje konversation
            detailed_conversations = []
            for i, conv_summary in enumerate(conversation_list, 1):
                conv_id = conv_summary.get('id')
                if not conv_id:
                    continue

                print(f"   [{i}/{len(conversation_list)}] Hämtar konversation: {conv_id[:8]}...")

                conv_url = f"{self.base_url}/conversation/{conv_id}"
                response = self.session.get(conv_url, headers=self._get_auth_headers())

                if response.status_code == 200:
                    detailed_conversations.append(response.json())
                else:
                    print(f"   ⚠️  Kunde inte hämta konversation {conv_id}: {response.status_code}")

                # Rate limiting
                time.sleep(0.5)

            return detailed_conversations

        except Exception as e:
            print(f"❌ Fel vid web-export: {e}")
            return []

    def _export_via_api(self) -> List[Dict]:
        """
        Exportera via OpenAI API

        OBS: OpenAI API:et lagrar inte chatthistorik automatiskt.
        Denna metod är främst för framtida integrationer.
        """
        print("⚠️  OpenAI API lagrar inte chatthistorik automatiskt")
        print("   För att exportera befintliga konversationer, använd web-metoden")
        print("   med cookies från chatgpt.com")
        return []

    def export_to_markdown(self, conversations: List[Dict], output_file: str):
        """
        Exportera konversationer till Markdown-format

        Args:
            conversations: Lista med konversationer
            output_file: Output-fil
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            for conv in conversations:
                title = conv.get('title', 'Untitled')
                create_time = conv.get('create_time', 'Unknown')

                f.write(f"# {title}\n\n")
                f.write(f"**Created:** {create_time}\n\n")
                f.write("---\n\n")

                # Skriv meddelanden
                mapping = conv.get('mapping', {})
                for node_id, node in mapping.items():
                    message = node.get('message')
                    if not message:
                        continue

                    role = message.get('author', {}).get('role', 'unknown')
                    content_parts = message.get('content', {}).get('parts', [])

                    if content_parts:
                        text = '\n'.join(str(part) for part in content_parts)

                        if role == 'user':
                            f.write(f"**User:**\n{text}\n\n")
                        elif role == 'assistant':
                            f.write(f"**Assistant:**\n{text}\n\n")

                f.write("\n---\n\n")

        print(f"✅ Markdown-export klar: {output_file}")
