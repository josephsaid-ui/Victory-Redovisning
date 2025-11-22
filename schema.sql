-- PostgreSQL Schema för Chat History Exporter
-- Grok och ChatGPT konversationer
--
-- Kör detta script för att skapa alla tabeller och index:
-- psql -U postgres -d chat_history -f schema.sql

-- Skapa databas (kör detta manuellt först om databasen inte finns)
-- CREATE DATABASE chat_history;

-- Aktivera nödvändiga extensions
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- Huvudtabeller

CREATE TABLE IF NOT EXISTS conversations (
    id              SERIAL PRIMARY KEY,
    source          TEXT NOT NULL CHECK (source IN ('grok', 'chatgpt')),
    title           TEXT NOT NULL,
    project         TEXT,
    created_at      TIMESTAMP DEFAULT NOW(),
    exported_at     TIMESTAMP DEFAULT NOW(),
    metadata        JSONB DEFAULT '{}'::jsonb
);

CREATE TABLE IF NOT EXISTS messages (
    id              SERIAL PRIMARY KEY,
    conversation_id INT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role            TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
    content         TEXT NOT NULL,
    message_order   INT NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW(),
    metadata        JSONB DEFAULT '{}'::jsonb
);

-- Collections för att organisera konversationer
CREATE TABLE IF NOT EXISTS collections (
    id              SERIAL PRIMARY KEY,
    name            TEXT NOT NULL UNIQUE,
    description     TEXT,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS collection_items (
    collection_id   INT NOT NULL REFERENCES collections(id) ON DELETE CASCADE,
    conversation_id INT NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    added_at        TIMESTAMP DEFAULT NOW(),
    notes           TEXT,
    PRIMARY KEY (collection_id, conversation_id)
);

-- Index för blixtsnabb sökning

-- Full-text search index (svensk och engelsk)
CREATE INDEX IF NOT EXISTS idx_messages_content_sv_gin
    ON messages USING GIN (to_tsvector('swedish', content));

CREATE INDEX IF NOT EXISTS idx_messages_content_en_gin
    ON messages USING GIN (to_tsvector('english', content));

-- Trigram index för fuzzy matching
CREATE INDEX IF NOT EXISTS idx_messages_content_trgm
    ON messages USING GIST (content gist_trgm_ops);

CREATE INDEX IF NOT EXISTS idx_conversations_title_trgm
    ON conversations USING GIST (title gist_trgm_ops);

-- Vanliga index för filtrering och joins
CREATE INDEX IF NOT EXISTS idx_conversations_source
    ON conversations(source);

CREATE INDEX IF NOT EXISTS idx_conversations_created_at
    ON conversations(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_conversations_project
    ON conversations(project) WHERE project IS NOT NULL;

CREATE INDEX IF NOT EXISTS idx_messages_conversation_id
    ON messages(conversation_id);

CREATE INDEX IF NOT EXISTS idx_messages_role
    ON messages(role);

-- JSONB index för metadata
CREATE INDEX IF NOT EXISTS idx_conversations_metadata_gin
    ON conversations USING GIN (metadata);

CREATE INDEX IF NOT EXISTS idx_messages_metadata_gin
    ON messages USING GIN (metadata);

-- Views för enkel åtkomst

-- Sökvy som kombinerar svenska och engelska full-text search
CREATE OR REPLACE VIEW searchable_messages AS
SELECT
    m.id,
    m.content,
    m.role,
    m.message_order,
    c.id as conversation_id,
    c.title,
    c.source,
    c.project,
    c.created_at,
    to_tsvector('swedish', m.content) || to_tsvector('english', m.content) as search_vector
FROM messages m
JOIN conversations c ON m.conversation_id = c.id;

-- Konversationsöversikt med meddelanderäknare
CREATE OR REPLACE VIEW conversation_overview AS
SELECT
    c.id,
    c.source,
    c.title,
    c.project,
    c.created_at,
    c.exported_at,
    COUNT(m.id) as message_count,
    COUNT(DISTINCT CASE WHEN m.role = 'user' THEN m.id END) as user_messages,
    COUNT(DISTINCT CASE WHEN m.role = 'assistant' THEN m.id END) as assistant_messages,
    MAX(m.created_at) as last_message_at
FROM conversations c
LEFT JOIN messages m ON c.id = m.conversation_id
GROUP BY c.id;

-- Collection översikt
CREATE OR REPLACE VIEW collection_overview AS
SELECT
    col.id,
    col.name,
    col.description,
    col.created_at,
    COUNT(ci.conversation_id) as conversation_count
FROM collections col
LEFT JOIN collection_items ci ON col.id = ci.collection_id
GROUP BY col.id;

-- Funktioner för sökning

-- Sök i meddelanden (full-text)
CREATE OR REPLACE FUNCTION search_messages(
    search_query TEXT,
    source_filter TEXT DEFAULT NULL,
    limit_count INT DEFAULT 50
)
RETURNS TABLE (
    conversation_id INT,
    message_id INT,
    title TEXT,
    source TEXT,
    role TEXT,
    content TEXT,
    rank REAL,
    created_at TIMESTAMP
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        m.id,
        c.title,
        c.source,
        m.role,
        m.content,
        ts_rank_cd(
            to_tsvector('swedish', m.content) || to_tsvector('english', m.content),
            plainto_tsquery('swedish', search_query)
        ) AS rank,
        c.created_at
    FROM messages m
    JOIN conversations c ON m.conversation_id = c.id
    WHERE
        (to_tsvector('swedish', m.content) || to_tsvector('english', m.content))
        @@ plainto_tsquery('swedish', search_query)
        AND (source_filter IS NULL OR c.source = source_filter)
    ORDER BY rank DESC, c.created_at DESC
    LIMIT limit_count;
END;
$$ LANGUAGE plpgsql;

-- Fuzzy search i titlar
CREATE OR REPLACE FUNCTION fuzzy_search_titles(
    search_query TEXT,
    similarity_threshold REAL DEFAULT 0.3
)
RETURNS TABLE (
    conversation_id INT,
    title TEXT,
    source TEXT,
    similarity REAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.id,
        c.title,
        c.source,
        similarity(c.title, search_query) AS sim
    FROM conversations c
    WHERE similarity(c.title, search_query) > similarity_threshold
    ORDER BY sim DESC
    LIMIT 20;
END;
$$ LANGUAGE plpgsql;

-- Kommentarer för dokumentation
COMMENT ON TABLE conversations IS 'Konversationer från Grok och ChatGPT';
COMMENT ON TABLE messages IS 'Individuella meddelanden i konversationer';
COMMENT ON TABLE collections IS 'Användardefinierade samlingar av konversationer';
COMMENT ON TABLE collection_items IS 'Länkar mellan collections och konversationer';

COMMENT ON COLUMN conversations.source IS 'Källa: grok eller chatgpt';
COMMENT ON COLUMN conversations.project IS 'Projekt-namn för Grok-konversationer';
COMMENT ON COLUMN conversations.metadata IS 'Extra metadata i JSONB-format';
COMMENT ON COLUMN messages.message_order IS 'Ordning av meddelande i konversationen (0-indexerad)';

COMMENT ON VIEW searchable_messages IS 'Vy för full-text search i både svenska och engelska';
COMMENT ON VIEW conversation_overview IS 'Översikt av konversationer med meddelanderäknare';

-- Exempel på användning
/*

-- 1. Sök i meddelanden
SELECT * FROM search_messages('python async', NULL, 10);

-- 2. Fuzzy search i titlar
SELECT * FROM fuzzy_search_titles('async programming');

-- 3. Full-text search med highlight
SELECT
    c.title,
    m.role,
    ts_headline(
        'swedish',
        m.content,
        plainto_tsquery('swedish', 'python'),
        'StartSel=<mark>, StopSel=</mark>, MaxWords=40'
    ) as snippet
FROM messages m
JOIN conversations c ON m.conversation_id = c.id
WHERE to_tsvector('swedish', m.content) @@ plainto_tsquery('swedish', 'python')
LIMIT 10;

-- 4. Statistik per källa
SELECT
    source,
    COUNT(*) as conversations,
    SUM(message_count) as total_messages
FROM conversation_overview
GROUP BY source;

-- 5. Skapa en collection
INSERT INTO collections (name, description)
VALUES ('AI Research', 'Konversationer om AI och machine learning');

-- 6. Lägg till konversationer i collection
INSERT INTO collection_items (collection_id, conversation_id)
SELECT 1, id FROM conversations WHERE title ILIKE '%AI%' OR title ILIKE '%machine learning%';

*/

-- Skapa en default collection för favoriter
INSERT INTO collections (name, description)
VALUES ('Favoriter', 'Sparade favorit-konversationer')
ON CONFLICT (name) DO NOTHING;

-- Visa framgångsmeddelande
DO $$
BEGIN
    RAISE NOTICE '✅ Schema skapat framgångsrikt!';
    RAISE NOTICE '📊 Tabeller: conversations, messages, collections, collection_items';
    RAISE NOTICE '🔍 Views: searchable_messages, conversation_overview, collection_overview';
    RAISE NOTICE '⚡ Funktioner: search_messages(), fuzzy_search_titles()';
    RAISE NOTICE '';
    RAISE NOTICE '🚀 Nästa steg:';
    RAISE NOTICE '   1. Konfigurera .env med databasuppgifter';
    RAISE NOTICE '   2. Kör: python unified_import.py <export-fil>.json';
    RAISE NOTICE '   3. Testa: SELECT * FROM conversation_overview;';
END $$;
