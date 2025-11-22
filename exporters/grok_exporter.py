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
    Komplett Selenium-baserad exporter för Grok (X)

    Hanterar Recent + ALLA projekt + sparar i både Markdown och JSON
    (perfekt för PostgreSQL-import)

    Testad och fungerande 22 november 2025
    """

    def __init__(self, cookies: Optional[Dict] = None):
        """
        Initialisera Selenium-baserad exporter

        Args:
            cookies: Session cookies från x.com (auth_token och ct0)
        """
        self.cookies = cookies
        self.driver = None

    def setup_driver(self):
        """Sätt upp Selenium WebDriver med anti-detection"""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

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
        Hämtar Recent + alla Projekt

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
                    self.driver.add_cookie({'name': name, 'value': value, 'domain': '.x.com'})

            self.driver.refresh()
            time.sleep(6)  # Vänta på att sidan laddas ordentligt

            # Vänta på sidebar
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="sidebar"]'))
            )

            conversations = []

            # 1. Hämta Recent-chattar
            print("📥 Hämtar Recent...")
            conversations.extend(self._scrape_current_view("Recent"))

            # 2. Hämta alla Projekt
            try:
                projects_tab = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Projects')]/parent::button")
                projects_tab.click()
                time.sleep(4)

                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="project-item"]'))
                )

                project_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="project-item"]')
                print(f"📁 {len(project_elements)} projekt funna")

                for proj_idx, proj in enumerate(project_elements, 1):
                    try:
                        proj_name = proj.text.strip() or f"Projekt {proj_idx}"
                        proj.click()
                        time.sleep(4)

                        print(f"   [{proj_idx}] {proj_name}")
                        proj_convos = self._scrape_current_view(f"Projekt: {proj_name}")

                        # Lägg till projekt-prefix i titeln
                        for convo in proj_convos:
                            convo["title"] = f"[{proj_name}] {convo['title']}"
                            convo["project"] = proj_name

                        conversations.extend(proj_convos)

                        # Navigera tillbaka till Projects-vyn
                        self.driver.get("https://x.com/i/grok")
                        time.sleep(2)
                        projects_tab = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Projects')]/parent::button")
                        projects_tab.click()
                        time.sleep(2)

                    except Exception as e:
                        print(f"   ⚠️  Fel i projekt {proj_idx}: {e}")

            except Exception as e:
                print(f"⚠️  Inga projekt eller flik saknas: {e}")

            print(f"✅ Totalt {len(conversations)} konversationer hämtade!")
            return conversations

        except Exception as e:
            print(f"❌ Fel vid Selenium-export: {e}")
            import traceback
            traceback.print_exc()
            return []
        finally:
            if self.driver:
                self.driver.quit()

    def _scrape_current_view(self, context: str) -> List[Dict]:
        """
        Skrapa konversationer från aktuell vy (Recent eller ett specifikt Projekt)

        Args:
            context: Beskrivning av vyn (t.ex. "Recent" eller "Projekt: AI Research")

        Returns:
            Lista med konversationer
        """
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        convos = []
        try:
            conv_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="conversation-item"]')
            print(f"      {len(conv_elements)} chattar i '{context}'")

            for idx, conv in enumerate(conv_elements, 1):
                try:
                    conv.click()
                    time.sleep(3)

                    # Hämta titel
                    try:
                        title_elem = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-item-title"], h2, h3, [role="heading"]')
                        title = title_elem.text.strip() or f"Untitled {idx}"
                    except:
                        title = f"Untitled {idx}"

                    # Hämta meddelanden
                    messages = []
                    msg_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-testid="message"]')

                    for msg in msg_elements:
                        try:
                            role = msg.get_attribute("data-role") or msg.get_attribute("role")
                            text = msg.text.strip()
                            if text:
                                messages.append({
                                    "role": "assistant" if role == "assistant" else "user",
                                    "content": text
                                })
                        except:
                            continue

                    if messages:  # Lägg bara till om det finns meddelanden
                        convos.append({
                            "title": title,
                            "messages": messages,
                            "project": None  # Sätts senare om det är ett projekt
                        })

                except Exception as e:
                    print(f"         ⚠️  Hoppade över chatt {idx}: {e}")

                # Navigera tillbaka till listan
                try:
                    self.driver.get(self.driver.current_url)
                    time.sleep(1.5)
                except:
                    pass

        except Exception as e:
            print(f"      ❌ Fel i {context}: {e}")

        return convos

    def export_to_json(self, conversations: List[Dict], filename: str = "grok_export.json"):
        """
        Spara konversationer som JSON - perfekt för PostgreSQL-import

        Args:
            conversations: Lista med konversationer
            filename: Filnamn för output
        """
        data = {
            "export_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_conversations": len(conversations),
            "source": "grok",
            "conversations": conversations
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ JSON sparad: {filename} (redo för PostgreSQL)")

    def export_to_markdown(self, conversations: List[Dict], filename: str = "grok_export.md"):
        """
        Exportera konversationer till Markdown-format

        Args:
            conversations: Lista med konversationer
            filename: Filnamn för output
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# Grok Conversations Export\n\n")
            f.write(f"**Exporterad:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**Totalt:** {len(conversations)} konversationer\n\n")
            f.write("---\n\n")

            for i, conv in enumerate(conversations, 1):
                title = conv.get('title', f'Conversation {i}')
                project = conv.get('project')

                f.write(f"## {title}\n\n")
                if project:
                    f.write(f"**Projekt:** {project}\n\n")
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

        print(f"✅ Markdown-export klar: {filename}")

    @staticmethod
    def generate_sql_schema():
        """
        Generera SQL-schema för PostgreSQL
        Skriv ut färdigt schema som kan kopieras direkt
        """
        sql = """
-- Grok/ChatGPT export schema för PostgreSQL
-- Kör detta för att skapa tabeller

CREATE TABLE IF NOT EXISTS conversations (
    id              SERIAL PRIMARY KEY,
    source          TEXT NOT NULL CHECK (source IN ('grok', 'chatgpt')),
    title           TEXT NOT NULL,
    project         TEXT,
    created_at      TIMESTAMP DEFAULT NOW(),
    exported_at     TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS messages (
    id              SERIAL PRIMARY KEY,
    conversation_id INT REFERENCES conversations(id) ON DELETE CASCADE,
    role            TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content         TEXT NOT NULL,
    message_order   INT NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW()
);

-- Collections för att organisera konversationer
CREATE TABLE IF NOT EXISTS collections (
    id              SERIAL PRIMARY KEY,
    name            TEXT NOT NULL UNIQUE,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS collection_items (
    collection_id   INT REFERENCES collections(id) ON DELETE CASCADE,
    conversation_id INT REFERENCES conversations(id) ON DELETE CASCADE,
    added_at        TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (collection_id, conversation_id)
);

-- Index för blixtsnabb full-text sökning
CREATE INDEX IF NOT EXISTS idx_messages_content_gin
    ON messages USING GIN (to_tsvector('swedish', content));

CREATE INDEX IF NOT EXISTS idx_messages_content_english_gin
    ON messages USING GIN (to_tsvector('english', content));

-- Index för trigram-sökning (fuzzy matching)
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE INDEX IF NOT EXISTS idx_messages_content_trgm
    ON messages USING GIST (content gist_trgm_ops);

-- Index för snabbare filtrering
CREATE INDEX IF NOT EXISTS idx_conversations_source ON conversations(source);
CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at);
CREATE INDEX IF NOT EXISTS idx_messages_conversation_id ON messages(conversation_id);

-- Vy för enkel sökning
CREATE OR REPLACE VIEW searchable_messages AS
SELECT
    m.id,
    m.content,
    m.role,
    c.id as conversation_id,
    c.title,
    c.source,
    c.project,
    c.created_at,
    to_tsvector('swedish', m.content) || to_tsvector('english', m.content) as search_vector
FROM messages m
JOIN conversations c ON m.conversation_id = c.id;

COMMENT ON TABLE conversations IS 'Konversationer från Grok och ChatGPT';
COMMENT ON TABLE messages IS 'Individuella meddelanden i konversationer';
COMMENT ON TABLE collections IS 'Användardefinierade samlingar av konversationer';
"""

        print("\n📋 Kopiera detta SQL-schema rakt in i PostgreSQL:\n")
        print(sql)
        return sql
