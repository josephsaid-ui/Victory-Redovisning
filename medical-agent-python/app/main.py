"""
FastAPI Application - Medical AI Agent Backend

Real-time WebSocket för transcription processing
REST endpoints för session management
"""
import os
import logging
from typing import Dict
from contextlib import asynccontextmanager

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.agents.medical_agent import MedicalAgent
from app.models.medical_types import (
    SessionStartRequest,
    SessionStartResponse,
    TranscriptionChunk,
    WebSocketMessage
)

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global agent instance
medical_agent: MedicalAgent = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager för startup/shutdown"""
    # Startup
    global medical_agent
    logger.info("🚀 Starting Medical Agent Backend...")

    medical_agent = MedicalAgent()
    await medical_agent.initialize()

    logger.info("✅ Backend ready!")

    yield

    # Shutdown
    logger.info("👋 Shutting down...")


# Create FastAPI app
app = FastAPI(
    title="Medical AI Agent API",
    description="Backend för ögonsekreterare-appen",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # I produktion: Specificera frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Active sessions
active_sessions: Dict[str, MedicalAgent] = {}


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "Medical AI Agent",
        "version": "1.0.0"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "agent_initialized": medical_agent.initialized if medical_agent else False,
        "active_sessions": len(active_sessions)
    }


@app.post("/sessions/start", response_model=SessionStartResponse)
async def start_session(request: SessionStartRequest):
    """Starta ny patient session"""
    from datetime import datetime
    import uuid

    session_id = str(uuid.uuid4())

    # Skapa ny agent instance för denna session
    agent = MedicalAgent()
    await agent.initialize()

    active_sessions[session_id] = agent

    logger.info(f"▶️ Started session: {session_id}")

    return SessionStartResponse(
        session_id=session_id,
        started_at=datetime.now()
    )


@app.post("/sessions/{session_id}/end")
async def end_session(session_id: str):
    """Avsluta session"""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    # Cleanup
    del active_sessions[session_id]

    logger.info(f"⏹️ Ended session: {session_id}")

    return {"status": "ended", "session_id": session_id}


@app.post("/sessions/{session_id}/journal")
async def generate_journal(session_id: str):
    """Generera journaltext för session"""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    agent = active_sessions[session_id]

    logger.info(f"📄 Generating journal for session: {session_id}")

    journal = await agent.generate_journal_entry()

    return {
        "session_id": session_id,
        "journal": journal
    }


@app.get("/sessions/{session_id}/context")
async def get_context(session_id: str):
    """Hämta nuvarande context för session"""
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    agent = active_sessions[session_id]
    context = agent.get_context()

    return context.model_dump()


@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    """
    WebSocket endpoint för real-time transcription processing

    Meddelande format:
    {
        "type": "transcription_chunk" | "generate_journal" | "get_context",
        "data": {...}
    }
    """
    await websocket.accept()
    logger.info(f"👤 WebSocket connected: {session_id}")

    # Hämta eller skapa agent för session
    if session_id not in active_sessions:
        agent = MedicalAgent()
        await agent.initialize()
        active_sessions[session_id] = agent
    else:
        agent = active_sessions[session_id]

    try:
        while True:
            # Ta emot meddelande från client
            data = await websocket.receive_json()
            message_type = data.get("type")

            if message_type == "transcription_chunk":
                # Processa transcription
                text = data.get("data", {}).get("text", "")

                logger.info(f"📝 Received transcription: {text}")

                # Processa med agent
                suggestions = await agent.process_transcription(text)

                # Skicka tillbaka suggestions
                await websocket.send_json({
                    "type": "suggestions",
                    "data": {
                        "suggestions": [s.model_dump() for s in suggestions],
                        "context": agent.get_context().model_dump()
                    }
                })

            elif message_type == "generate_journal":
                # Generera journal
                journal = await agent.generate_journal_entry()

                await websocket.send_json({
                    "type": "journal",
                    "data": {"journal": journal}
                })

            elif message_type == "get_context":
                # Skicka nuvarande context
                context = agent.get_context()

                await websocket.send_json({
                    "type": "context",
                    "data": context.model_dump()
                })

            elif message_type == "reset":
                # Reset agent
                agent.reset()

                await websocket.send_json({
                    "type": "reset_complete",
                    "data": {}
                })

    except WebSocketDisconnect:
        logger.info(f"👋 WebSocket disconnected: {session_id}")

    except Exception as e:
        logger.error(f"❌ WebSocket error: {e}")
        await websocket.send_json({
            "type": "error",
            "data": {"message": str(e)}
        })


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
