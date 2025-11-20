"""
Grok (X) Exporter
Exporterar konversationshistorik från Grok (X's AI)
"""

import requests
import json
import time
from typing import List, Dict, Optional


class GrokExporter:
    """Exporterar konversationer från Grok (X)"""

    def __init__(self, auth_token: Optional[str] = None, cookies: Optional[Dict] = None):
        """
        Initialisera Grok-exportern

        Args:
            auth_token: X/Twitter auth token
            cookies: Session cookies från x.com/twitter.com
        """
        self.auth_token = auth_token
        self.cookies = cookies or {}
        self.base_url = "https://api.x.com"
        self.grok_api_url = "https://grok.x.ai/api"
        self.session = requests.Session()

        # Sätt cookies
        if cookies:
            self.session.cookies.update(cookies)

        # Sätt auth token som cookie om tillgänglig
        if auth_token:
            self.session.cookies.set('auth_token', auth_token, domain='.x.com')

    def _get_headers(self) -> Dict[str, str]:
        """Skapa request headers"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/json',
            'Origin': 'https://x.com',
            'Referer': 'https://x.com/',
        }

        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'

        return headers

    def export_conversations(self) -> List[Dict]:
        """
        Exportera alla konversationer från Grok

        Returns:
            Lista med konversationer
        """
        if not self.auth_token and not self.cookies:
            print("⚠️  Ingen autentisering konfigurerad för Grok")
            print("   Lägg till 'auth_token' eller 'cookies' i config.json")
            print("\n📝 Så här hämtar du auth_token:")
            print("   1. Gå till x.com och logga in")
            print("   2. Öppna Developer Tools (F12)")
            print("   3. Gå till Application/Storage > Cookies")
            print("   4. Kopiera värdet för 'auth_token'")
            return []

        try:
            return self._export_via_api()
        except Exception as e:
            print(f"❌ Fel vid export: {e}")
            return []

    def _export_via_api(self) -> List[Dict]:
        """
        Exportera via Grok API

        OBS: Grok API:et är inte officiellt dokumenterat.
        Denna implementation baseras på reverse engineering av webbgränssnittet.
        """
        try:
            # Först, hämta användarens CSRF token
            csrf_token = self._get_csrf_token()
            if csrf_token:
                self.session.headers.update({'x-csrf-token': csrf_token})

            # Försök hämta konversationer från olika endpoints
            conversations = []

            # Endpoint 1: Grok-specifikt API (om det finns)
            print("🔍 Söker efter Grok-konversationer...")

            # Eftersom Grok API:et inte är officiellt dokumenterat,
            # måste användaren själv extrahera konversationer via browser
            print("\n⚠️  Grok har inget officiellt API för export av historik ännu.")
            print("\n📝 Manual export krävs:")
            print("   1. Gå till https://x.com/i/grok")
            print("   2. Öppna Developer Tools (F12)")
            print("   3. Gå till Network-fliken")
            print("   4. Klicka på en konversation")
            print("   5. Leta efter API-anrop i Network-fliken")
            print("   6. Kopiera responses och lägg i en JSON-fil")
            print("\n   Alternativt: Använd browser automation (Selenium/Playwright)")

            # Returnera tom lista tills API:et är dokumenterat
            return conversations

        except Exception as e:
            print(f"❌ Fel vid API-anrop: {e}")
            return []

    def _get_csrf_token(self) -> Optional[str]:
        """Hämta CSRF token från cookies"""
        for cookie in self.session.cookies:
            if cookie.name == 'ct0':
                return cookie.value
        return None

    def export_to_markdown(self, conversations: List[Dict], output_file: str):
        """
        Exportera konversationer till Markdown-format

        Args:
            conversations: Lista med konversationer
            output_file: Output-fil
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Grok Conversations Export\n\n")

            for i, conv in enumerate(conversations, 1):
                title = conv.get('title', f'Conversation {i}')
                timestamp = conv.get('created_at', 'Unknown')

                f.write(f"## {title}\n\n")
                f.write(f"**Created:** {timestamp}\n\n")
                f.write("---\n\n")

                # Skriv meddelanden
                messages = conv.get('messages', [])
                for msg in messages:
                    role = msg.get('role', 'unknown')
                    content = msg.get('content', '')

                    if role == 'user':
                        f.write(f"**You:**\n{content}\n\n")
                    elif role == 'assistant':
                        f.write(f"**Grok:**\n{content}\n\n")

                f.write("\n---\n\n")

        print(f"✅ Markdown-export klar: {output_file}")


class GrokSeleniumExporter:
    """
    Alternativ exporter som använder Selenium för att automatisera webbläsaren

    Detta är en mer robust lösning som faktiskt kan extrahera konversationer
    från Grok's webbgränssnitt.
    """

    def __init__(self, cookies: Optional[Dict] = None):
        """
        Initialisera Selenium-baserad exporter

        Args:
            cookies: Session cookies från x.com
        """
        self.cookies = cookies
        self.driver = None

    def setup_driver(self):
        """Sätt upp Selenium WebDriver"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            options = Options()
            options.add_argument('--headless')  # Kör i bakgrunden
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)

            return True
        except ImportError:
            print("❌ Selenium inte installerad")
            print("   Kör: pip install selenium webdriver-manager")
            return False
        except Exception as e:
            print(f"❌ Kunde inte starta WebDriver: {e}")
            return False

    def export_conversations(self) -> List[Dict]:
        """
        Exportera konversationer med Selenium

        Returns:
            Lista med konversationer
        """
        if not self.setup_driver():
            return []

        try:
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC

            # Gå till Grok
            self.driver.get("https://x.com/i/grok")

            # Lägg till cookies
            if self.cookies:
                for name, value in self.cookies.items():
                    self.driver.add_cookie({'name': name, 'value': value})

            # Uppdatera sidan
            self.driver.refresh()

            # Vänta på att sidan laddas
            wait = WebDriverWait(self.driver, 10)

            # Hitta konversationer (detta beror på DOM-strukturen)
            # Detta är en placeholder - faktisk implementation beror på Grok's UI
            conversations = []

            print("⚠️  Selenium-export kräver mer detaljerad DOM-mapping")
            print("   Detta är en placeholder-implementation")

            return conversations

        except Exception as e:
            print(f"❌ Fel vid Selenium-export: {e}")
            return []
        finally:
            if self.driver:
                self.driver.quit()
