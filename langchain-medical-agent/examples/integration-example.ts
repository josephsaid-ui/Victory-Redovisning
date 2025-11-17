/**
 * INTEGRATION EXAMPLE: Full stack integration
 *
 * Visar hur LangChain agent integreras med:
 * 1. AssemblyAI för transcription
 * 2. Supabase för storage
 * 3. React Native frontend via WebSocket
 */

import { StreamingMedicalAgent } from '../src/agent/streaming-agent';
import { createClient } from '@supabase/supabase-js';
import WebSocket from 'ws';

/**
 * Backend Service som kör agenten
 */
class MedicalAgentBackendService {
  private agent: StreamingMedicalAgent;
  private supabase;
  private wss: WebSocket.Server | null = null;
  private currentSessionId: string | null = null;

  constructor() {
    // Initialisera agent
    this.agent = new StreamingMedicalAgent({
      modelName: 'claude-3-5-sonnet-20241022',
      temperature: 0.2,
    });

    // Initialisera Supabase
    this.supabase = createClient(
      process.env.SUPABASE_URL!,
      process.env.SUPABASE_SERVICE_KEY!
    );
  }

  /**
   * Starta backend service
   */
  async start(port: number = 8080) {
    console.log('🚀 Starting Medical Agent Backend Service...');

    // 1. Initialisera agent
    await this.agent.initialize();

    // 2. Setup WebSocket server
    this.wss = new WebSocket.Server({ port });
    console.log(`✓ WebSocket server listening on port ${port}`);

    // 3. Setup event listeners
    this.setupAgentListeners();

    // 4. Handle WebSocket connections
    this.setupWebSocketHandlers();

    console.log('✅ Backend service ready!');
  }

  /**
   * Setup agent event listeners
   */
  private setupAgentListeners() {
    // När agent genererar suggestions, skicka till frontend
    this.agent.on('suggestion', async (suggestion) => {
      console.log('💡 Suggestion generated:', suggestion.type);

      // Broadcast till alla anslutna clients
      this.broadcast({
        type: 'agent_suggestion',
        data: suggestion,
      });

      // Spara i databas
      if (this.currentSessionId) {
        await this.saveSuggestion(this.currentSessionId, suggestion);
      }
    });

    // När context uppdateras
    this.agent.on('context_update', (context) => {
      this.broadcast({
        type: 'context_update',
        data: context,
      });
    });

    // Error handling
    this.agent.on('error', (error) => {
      console.error('❌ Agent error:', error);
      this.broadcast({
        type: 'error',
        data: { message: error.message },
      });
    });
  }

  /**
   * Setup WebSocket handlers
   */
  private setupWebSocketHandlers() {
    if (!this.wss) return;

    this.wss.on('connection', (ws: WebSocket) => {
      console.log('👤 New client connected');

      ws.on('message', async (message: string) => {
        try {
          const data = JSON.parse(message.toString());
          await this.handleClientMessage(ws, data);
        } catch (error) {
          console.error('Error handling message:', error);
          ws.send(
            JSON.stringify({
              type: 'error',
              data: { message: 'Invalid message format' },
            })
          );
        }
      });

      ws.on('close', () => {
        console.log('👋 Client disconnected');
      });
    });
  }

  /**
   * Handle messages från frontend
   */
  private async handleClientMessage(ws: WebSocket, data: any) {
    switch (data.type) {
      case 'start_session':
        await this.startSession(ws, data.userId);
        break;

      case 'transcription_chunk':
        // Transcription chunk från AssemblyAI
        this.agent.addTranscriptionChunk(data.text);
        break;

      case 'end_session':
        await this.endSession(ws);
        break;

      case 'generate_journal':
        await this.generateAndSaveJournal(ws);
        break;

      default:
        console.warn('Unknown message type:', data.type);
    }
  }

  /**
   * Starta ny session
   */
  private async startSession(ws: WebSocket, userId: string) {
    console.log('▶️ Starting new session for user:', userId);

    // Skapa session i databas
    const { data: session, error } = await this.supabase
      .from('patient_sessions')
      .insert({
        user_id: userId,
        started_at: new Date().toISOString(),
        status: 'active',
      })
      .select()
      .single();

    if (error) {
      console.error('Error creating session:', error);
      ws.send(
        JSON.stringify({
          type: 'error',
          data: { message: 'Failed to create session' },
        })
      );
      return;
    }

    this.currentSessionId = session.id;

    // Reset agent för ny session
    this.agent.reset();

    // Starta streaming
    this.agent.startStreaming(2000);

    ws.send(
      JSON.stringify({
        type: 'session_started',
        data: { sessionId: session.id },
      })
    );
  }

  /**
   * Avsluta session
   */
  private async endSession(ws: WebSocket) {
    console.log('⏹️ Ending session');

    if (!this.currentSessionId) return;

    // Stoppa streaming
    this.agent.stopStreaming();

    // Uppdatera session i databas
    await this.supabase
      .from('patient_sessions')
      .update({
        ended_at: new Date().toISOString(),
        status: 'completed',
      })
      .eq('id', this.currentSessionId);

    ws.send(
      JSON.stringify({
        type: 'session_ended',
        data: { sessionId: this.currentSessionId },
      })
    );

    this.currentSessionId = null;
  }

  /**
   * Generera och spara journal
   */
  private async generateAndSaveJournal(ws: WebSocket) {
    console.log('📄 Generating journal entry...');

    try {
      const journal = await this.agent.generateJournalEntry();

      // Spara i databas
      if (this.currentSessionId) {
        await this.supabase.from('journal_entries').insert({
          session_id: this.currentSessionId,
          content: journal,
          generated_at: new Date().toISOString(),
        });
      }

      ws.send(
        JSON.stringify({
          type: 'journal_generated',
          data: { journal },
        })
      );
    } catch (error) {
      console.error('Error generating journal:', error);
      ws.send(
        JSON.stringify({
          type: 'error',
          data: { message: 'Failed to generate journal' },
        })
      );
    }
  }

  /**
   * Spara suggestion i databas
   */
  private async saveSuggestion(sessionId: string, suggestion: any) {
    await this.supabase.from('agent_suggestions').insert({
      session_id: sessionId,
      type: suggestion.type,
      content: suggestion.content,
      confidence: suggestion.confidence,
      created_at: new Date().toISOString(),
    });
  }

  /**
   * Broadcast message till alla clients
   */
  private broadcast(message: any) {
    if (!this.wss) return;

    const data = JSON.stringify(message);
    this.wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(data);
      }
    });
  }
}

/**
 * EXEMPEL: React Native Frontend Integration
 */
const reactNativeExample = `
// React Native komponent som använder WebSocket

import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList } from 'react-native';

export function PatientConsultation() {
  const [ws, setWs] = useState<WebSocket | null>(null);
  const [suggestions, setSuggestions] = useState([]);
  const [context, setContext] = useState(null);
  const [sessionId, setSessionId] = useState(null);

  // Connect WebSocket
  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8080');

    socket.onmessage = (event) => {
      const message = JSON.parse(event.data);

      switch (message.type) {
        case 'session_started':
          setSessionId(message.data.sessionId);
          break;

        case 'agent_suggestion':
          setSuggestions(prev => [...prev, message.data]);
          // Visa notification i UI
          showNotification(message.data);
          break;

        case 'context_update':
          setContext(message.data);
          break;

        case 'journal_generated':
          // Visa genererad journal
          navigateToJournal(message.data.journal);
          break;
      }
    };

    setWs(socket);
    return () => socket.close();
  }, []);

  const startSession = () => {
    ws?.send(JSON.stringify({
      type: 'start_session',
      userId: 'doctor-123'
    }));
  };

  const endSession = () => {
    ws?.send(JSON.stringify({
      type: 'end_session'
    }));
  };

  const generateJournal = () => {
    ws?.send(JSON.stringify({
      type: 'generate_journal'
    }));
  };

  return (
    <View>
      <Button title="Starta Konsultation" onPress={startSession} />

      {/* Visa suggestions i realtid */}
      <FlatList
        data={suggestions}
        renderItem={({ item }) => (
          <SuggestionCard suggestion={item} />
        )}
      />

      <Button title="Generera Journal" onPress={generateJournal} />
      <Button title="Avsluta" onPress={endSession} />
    </View>
  );
}
`;

/**
 * SUPABASE SCHEMA
 */
const supabaseSchema = `
-- Patient Sessions
create table patient_sessions (
  id uuid primary key default uuid_generate_v4(),
  user_id text not null,
  started_at timestamp with time zone not null,
  ended_at timestamp with time zone,
  status text not null check (status in ('active', 'completed', 'cancelled')),
  created_at timestamp with time zone default now()
);

-- Journal Entries
create table journal_entries (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  content text not null,
  generated_at timestamp with time zone not null,
  edited_content text,
  created_at timestamp with time zone default now()
);

-- Agent Suggestions
create table agent_suggestions (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  type text not null,
  content jsonb not null,
  confidence decimal(3,2),
  created_at timestamp with time zone default now()
);

-- Transcriptions
create table transcriptions (
  id uuid primary key default uuid_generate_v4(),
  session_id uuid references patient_sessions(id) on delete cascade,
  text text not null,
  timestamp timestamp with time zone default now()
);

-- RLS Policies
alter table patient_sessions enable row level security;
alter table journal_entries enable row level security;
alter table agent_suggestions enable row level security;

-- Policy: Users can only see their own data
create policy "Users can view own sessions"
  on patient_sessions for select
  using (auth.uid()::text = user_id);
`;

// Export
export {
  MedicalAgentBackendService,
  reactNativeExample,
  supabaseSchema,
};

// Kör exempel
if (require.main === module) {
  const service = new MedicalAgentBackendService();
  service.start(8080).catch(console.error);
}
