-- ============================================================================
-- DATABASE SCHEMA FÖR MEDICAL AI AGENT
-- Version: 1.0.0
-- Created: 2024-01-15
-- ============================================================================

-- Enable Extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ============================================================================
-- PATIENT SESSIONS
-- ============================================================================
CREATE TABLE IF NOT EXISTS patient_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id TEXT NOT NULL,
    started_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    ended_at TIMESTAMP WITH TIME ZONE,
    status TEXT NOT NULL CHECK (status IN ('active', 'completed', 'cancelled')) DEFAULT 'active',

    -- Patient metadata
    patient_age INTEGER,
    patient_gender TEXT,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_patient_sessions_user_id ON patient_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_patient_sessions_status ON patient_sessions(status);
CREATE INDEX IF NOT EXISTS idx_patient_sessions_started_at ON patient_sessions(started_at DESC);

-- Update timestamp function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger
DROP TRIGGER IF EXISTS update_patient_sessions_updated_at ON patient_sessions;
CREATE TRIGGER update_patient_sessions_updated_at
    BEFORE UPDATE ON patient_sessions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- TRANSCRIPTIONS
-- ============================================================================
CREATE TABLE IF NOT EXISTS transcriptions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Transcription data
    text TEXT NOT NULL,
    chunk_index INTEGER NOT NULL DEFAULT 0,
    is_final BOOLEAN DEFAULT false,

    -- Speaker identification (optional)
    speaker TEXT, -- 'doctor' or 'patient'

    -- Timestamps
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_transcriptions_session_id ON transcriptions(session_id);
CREATE INDEX IF NOT EXISTS idx_transcriptions_timestamp ON transcriptions(timestamp);
CREATE INDEX IF NOT EXISTS idx_transcriptions_speaker ON transcriptions(speaker);

-- ============================================================================
-- JOURNAL ENTRIES
-- ============================================================================
CREATE TABLE IF NOT EXISTS journal_entries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Journal content
    content TEXT NOT NULL,
    generated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),

    -- Structured sections (JSONB)
    sections JSONB DEFAULT '{}'::jsonb,
    -- Example: {"aktuellt": "...", "status": "...", "bedömning": "...", "planering": "..."}

    -- Editing
    edited_content TEXT,
    edited_at TIMESTAMP WITH TIME ZONE,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_journal_entries_session_id ON journal_entries(session_id);
CREATE INDEX IF NOT EXISTS idx_journal_entries_generated_at ON journal_entries(generated_at DESC);

-- Trigger
DROP TRIGGER IF EXISTS update_journal_entries_updated_at ON journal_entries;
CREATE TRIGGER update_journal_entries_updated_at
    BEFORE UPDATE ON journal_entries
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- AGENT SUGGESTIONS
-- ============================================================================
CREATE TABLE IF NOT EXISTS agent_suggestions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Suggestion data
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'question', 'analysis')),
    content JSONB NOT NULL,
    confidence DECIMAL(3,2) CHECK (confidence >= 0 AND confidence <= 1),

    -- User interaction
    accepted BOOLEAN,
    dismissed BOOLEAN DEFAULT false,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_agent_suggestions_session_id ON agent_suggestions(session_id);
CREATE INDEX IF NOT EXISTS idx_agent_suggestions_type ON agent_suggestions(type);
CREATE INDEX IF NOT EXISTS idx_agent_suggestions_created_at ON agent_suggestions(created_at);

-- ============================================================================
-- MEDICAL CONTEXT (per session)
-- ============================================================================
CREATE TABLE IF NOT EXISTS medical_contexts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL UNIQUE REFERENCES patient_sessions(id) ON DELETE CASCADE,

    -- Context data (JSONB för flexibilitet)
    symptoms JSONB DEFAULT '[]'::jsonb,
    suspected_diseases JSONB DEFAULT '[]'::jsonb,
    current_medications JSONB DEFAULT '[]'::jsonb,
    asked_questions JSONB DEFAULT '[]'::jsonb,
    medical_history JSONB DEFAULT '[]'::jsonb,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_medical_contexts_session_id ON medical_contexts(session_id);

-- Trigger
DROP TRIGGER IF EXISTS update_medical_contexts_updated_at ON medical_contexts;
CREATE TRIGGER update_medical_contexts_updated_at
    BEFORE UPDATE ON medical_contexts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- MEDICAL DOCUMENTS (för RAG knowledge base)
-- ============================================================================
CREATE TABLE IF NOT EXISTS medical_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),

    -- Document metadata
    type TEXT NOT NULL CHECK (type IN ('disease', 'treatment', 'medication', 'protocol')),
    name TEXT NOT NULL,

    -- Content
    content TEXT NOT NULL,
    metadata JSONB DEFAULT '{}'::jsonb,

    -- Vector embedding (768 dimensions för PubMedBERT)
    embedding vector(768),

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Vector similarity search index (HNSW för bästa performance)
CREATE INDEX IF NOT EXISTS idx_medical_documents_embedding
ON medical_documents USING hnsw (embedding vector_cosine_ops);

-- Other indexes
CREATE INDEX IF NOT EXISTS idx_medical_documents_type ON medical_documents(type);
CREATE INDEX IF NOT EXISTS idx_medical_documents_name ON medical_documents(name);
CREATE INDEX IF NOT EXISTS idx_medical_documents_metadata ON medical_documents USING GIN (metadata);

-- Full-text search index (Swedish)
CREATE INDEX IF NOT EXISTS idx_medical_documents_content
ON medical_documents USING GIN (to_tsvector('swedish', content));

-- Trigger
DROP TRIGGER IF EXISTS update_medical_documents_updated_at ON medical_documents;
CREATE TRIGGER update_medical_documents_updated_at
    BEFORE UPDATE ON medical_documents
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- SEED DATA - Medical Knowledge Base
-- ============================================================================
INSERT INTO medical_documents (type, name, content, metadata) VALUES
(
    'disease',
    'Katarakt (Grå starr)',
    'Katarakt är en grumling av ögats lins som leder till gradvis synförsämring. Vanliga symptom inkluderar suddig syn, halos runt lampor, svårt att köra bil i mörker, och färger som verkar blekare. Främst äldre över 60 år. Riskfaktorer: ålder, diabetes, rökning, långvarig kortisonbehandling, UV-exponering. Behandling: Kataraktoperation med inläggning av konstgjord lins (IOL). KVÅ: CJE00',
    '{"icd10": "H25-H28", "age_group": "främst äldre >60 år", "symptoms": ["suddig syn", "halos runt lampor", "gradvis synförsämring", "färger verkar blekare"], "risk_factors": ["ålder", "diabetes", "rökning"]}'::jsonb
),
(
    'disease',
    'Glaukom (Grön starr)',
    'Glaukom är progressiv skada på synnerven, ofta kopplad till förhöjt ögontryck. Kan leda till permanent synförlust om obehandlad. Symptom: synfältsbortfall (perifer syn först), förhöjt ögontryck, ofta symtomfritt tidigt, tunnelseende i sena stadier. Vid akut glaukom: huvudvärk, rött öga, kraftig smärta. Behandling: Ögondroppar (trycknedsättande), laserbehandling (SLT), kirurgi (trabekulektomi KVÅ: CJD00)',
    '{"icd10": "H40-H42", "age_group": "främst >40 år", "symptoms": ["synfältsbortfall", "förhöjt ögontryck", "tunnelseende"], "risk_factors": ["hög ålder", "hereditet", "högt ögontryck"]}'::jsonb
),
(
    'disease',
    'Åldersrelaterad Makuladegeneration (AMD)',
    'AMD är degeneration av makula (gula fläcken) som ger central synförlust. Finns i torr och våt form. Symptom: böjda linjer (Amsler grid), central synförlust, svårt att läsa, förvrängd syn, mörk fläck i centrum. Behandling: Våt AMD: Anti-VEGF injektioner (KVÅ: CJB10). Torr AMD: Kosttillskott (AREDS2), rökstopp',
    '{"icd10": "H35.3", "age_group": ">50 år, mest >65 år", "symptoms": ["böjda linjer", "central synförlust", "svårt att läsa", "förvrängd syn"]}'::jsonb
),
(
    'disease',
    'Diabetesretinopati',
    'Skador på retinan orsakade av diabetes. En ledande orsak till blindhet hos arbetsför ålder. Symptom: suddig syn, floaters, synfältsbortfall, ofta symtomfritt tidigt. Behandling: Laserbehandling (PRP KVÅ: CJF20), Anti-VEGF injektioner, bra diabeteskontroll',
    '{"icd10": "E11.3", "age_group": "diabetiker, alla åldrar", "symptoms": ["suddig syn", "floaters", "synfältsbortfall"], "risk_factors": ["dålig glukoskontroll", "lång diabetesduration"]}'::jsonb
),
(
    'disease',
    'Retinal Avlossning',
    'AKUT tillstånd där näthinnan lossnar från underliggande vävnad. Kräver akut behandling. Symptom: plötsliga ljusblixtar, många nya floaters, gardinsymptom (skugga i synfältet), plötslig synförlust. Behandling: AKUT kirurgi: Vitrektomi, buckle, pneumatisk retinopex. Laser/kryoterapi.',
    '{"icd10": "H33", "age_group": "alla åldrar, ökad risk >50 år", "symptoms": ["plötsliga ljusblixtar", "många nya floaters", "gardinsymptom"], "urgency": "AKUT"}'::jsonb
),
(
    'disease',
    'Torra Ögon (Keratoconjunctivitis sicca)',
    'Otillräcklig tårproduktion eller snabb avdunstning av tårfilm. Symptom: brännande känsla, sandkornskänsla, rinnande ögon (paradoxalt), röda ögon, trötta ögon vid läsning. Behandling: Artificiella tårar, punktumplugg, omega-3, behandla bakomliggande orsak',
    '{"icd10": "H04.1", "age_group": "alla åldrar, vanligare hos kvinnor >40 år", "symptoms": ["brännande känsla", "sandkornskänsla", "röda ögon"]}'::jsonb
)
ON CONFLICT DO NOTHING;

-- ============================================================================
-- VECTOR SEARCH FUNCTION
-- ============================================================================
CREATE OR REPLACE FUNCTION search_similar_documents(
    query_embedding vector(768),
    match_threshold float DEFAULT 0.7,
    match_count int DEFAULT 5,
    filter_type text DEFAULT NULL
)
RETURNS TABLE (
    id uuid,
    name text,
    content text,
    type text,
    metadata jsonb,
    similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        medical_documents.id,
        medical_documents.name,
        medical_documents.content,
        medical_documents.type,
        medical_documents.metadata,
        1 - (medical_documents.embedding <=> query_embedding) as similarity
    FROM medical_documents
    WHERE
        medical_documents.embedding IS NOT NULL
        AND (filter_type IS NULL OR medical_documents.type = filter_type)
        AND (1 - (medical_documents.embedding <=> query_embedding)) > match_threshold
    ORDER BY medical_documents.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- ============================================================================
-- UTILITY FUNCTIONS
-- ============================================================================

-- Get session summary
CREATE OR REPLACE FUNCTION get_session_summary(p_session_id UUID)
RETURNS TABLE (
    session_id uuid,
    user_id text,
    started_at timestamp with time zone,
    ended_at timestamp with time zone,
    status text,
    transcription_count bigint,
    journal_count bigint,
    suggestion_count bigint
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        ps.id,
        ps.user_id,
        ps.started_at,
        ps.ended_at,
        ps.status,
        (SELECT COUNT(*) FROM transcriptions WHERE session_id = ps.id),
        (SELECT COUNT(*) FROM journal_entries WHERE session_id = ps.id),
        (SELECT COUNT(*) FROM agent_suggestions WHERE session_id = ps.id)
    FROM patient_sessions ps
    WHERE ps.id = p_session_id;
END;
$$;

-- ============================================================================
-- VIEWS
-- ============================================================================

-- Active sessions view
CREATE OR REPLACE VIEW active_sessions AS
SELECT
    ps.*,
    COUNT(t.id) as transcription_count,
    MAX(t.timestamp) as last_transcription_at
FROM patient_sessions ps
LEFT JOIN transcriptions t ON t.session_id = ps.id
WHERE ps.status = 'active'
GROUP BY ps.id;

-- ============================================================================
-- COMMENTS (Documentation)
-- ============================================================================
COMMENT ON TABLE patient_sessions IS 'Patient konsultations-sessioner';
COMMENT ON TABLE transcriptions IS 'Transkriberad text från samtalet';
COMMENT ON TABLE journal_entries IS 'Genererade journaltexter';
COMMENT ON TABLE agent_suggestions IS 'AI-genererade förslag och insights';
COMMENT ON TABLE medical_contexts IS 'Medicinsk kontext per session';
COMMENT ON TABLE medical_documents IS 'RAG kunskapsbas för medicinska dokument';

-- ============================================================================
-- VERIFY INSTALLATION
-- ============================================================================
DO $$
BEGIN
    RAISE NOTICE 'Database schema installed successfully!';
    RAISE NOTICE 'Tables created: %', (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public');
    RAISE NOTICE 'Extensions enabled: %', (SELECT array_agg(extname) FROM pg_extension);
    RAISE NOTICE 'Medical documents: %', (SELECT COUNT(*) FROM medical_documents);
END $$;
