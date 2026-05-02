# RAG System - Complete Documentation

A production-level Retrieval-Augmented Generation (RAG) system with a modern ChatGPT-like UI.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Usage Guide](#usage-guide)
- [Session Management](#session-management)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## 🎯 Overview

This RAG system enables you to:
- Ingest documents (text files, raw text)
- Convert documents into vector embeddings
- Store embeddings in ChromaDB (vector database)
- Retrieve relevant context based on user queries
- Generate accurate answers using local LLM (Ollama with qwen3:4b)
- Maintain conversation history with session-based memory
- Chat via a modern Next.js frontend interface

## 🏗 Architecture

```
┌─────────────────┐     HTTP API      ┌──────────────────┐
│   Frontend      │ ◄──────────────► │    Backend       │
│   (Next.js)     │                   │   (FastAPI)      │
│                 │                   │                  │
│ - Chat UI       │                   │ - RAG Service    │
│ - Session Mgmt  │                   │ - Embedding Svc  │
│ - API Client    │                   │ - LLM Service    │
└─────────────────┘                   │ - Retriever Svc  │
                                      │ - Session Svc    │
                                      └────────┬─────────┘
                                               │
                    ┌──────────────────────────┼──────────────────────────┐
                    │                          │                          │
            ┌───────▼────────┐         ┌──────▼──────┐         ┌────────▼────────┐
            │  ChromaDB      │         │ Ollama LLM  │         │  Document      │
            │  (Vectors)     │         │ (qwen3:4b)  │         │  Ingestion     │
            └────────────────┘         └─────────────┘         └────────────────┘
```

## 🛠 Tech Stack

### Backend
- **Python 3.10+**
- **FastAPI** - Modern web framework
- **ChromaDB** - Vector database
- **sentence-transformers** - Embedding generation
- **Ollama** - Local LLM runtime
- **qwen3:4b** - Language model

### Frontend
- **Next.js 14** (App Router)
- **TypeScript**
- **Tailwind CSS**
- **Fetch API**

## 📁 Project Structure

```
rag/
├── rag-backend/                    # Python FastAPI Backend
│   ├── app/
│   │   ├── main.py                # FastAPI app entry point
│   │   ├── routes/
│   │   │   ├── query.py           # Query endpoint with session support
│   │   │   └── ingest.py          # Document ingestion endpoint
│   │   ├── services/
│   │   │   ├── rag_service.py     # Main RAG orchestration
│   │   │   ├── embedding_service.py  # Text to vector embeddings
│   │   │   ├── llm_service.py     # Ollama LLM integration
│   │   │   ├── retriever_service.py   # Vector similarity search
│   │   │   └── session_service.py # Conversation memory
│   │   ├── utils/
│   │   │   ├── chunking.py        # Text splitting logic
│   │   │   └── prompt_builder.py  # LLM prompt construction
│   │   └── db/
│   │       └── chroma_client.py   # ChromaDB client wrapper
│   ├── data/                      # Persistent storage
│   └── requirements.txt           # Python dependencies
│
├── rag-frontend/                   # Next.js Frontend
│   ├── app/
│   │   ├── chat/
│   │   │   └── page.tsx           # Main chat interface
│   │   ├── layout.tsx             # Root layout
│   │   ├── page.tsx               # Redirects to /chat
│   │   └── globals.css            # Global styles
│   ├── components/
│   │   ├── ChatContainer.tsx      # Message list with auto-scroll
│   │   ├── ChatInput.tsx          # Input field with send button
│   │   └── ChatMessage.tsx        # Individual message bubble
│   ├── lib/
│   │   └── api.ts                 # Backend API client
│   ├── types/
│   │   └── chat.ts                # TypeScript type definitions
│   ├── package.json               # Node dependencies
│   ├── tsconfig.json              # TypeScript config
│   ├── tailwind.config.js         # Tailwind CSS config
│   └── next.config.js             # Next.js config
│
└── README.md                       # This file
```

## ⚙️ Installation

### Prerequisites

1. **Python 3.10+** installed
2. **Node.js 18+** installed
3. **Ollama** installed and running

### Step 1: Install Ollama and Pull Model

```bash
# Install Ollama (if not installed)
# Visit https://ollama.com for installation

# Pull the required model
ollama pull qwen3:4b
```

### Step 2: Backend Setup

```bash
cd rag-backend

# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

**Note:** If you encounter dependency conflicts, install compatible versions:
```bash
pip install fastapi==0.109.0 uvicorn[standard]==0.27.0
pip install chromadb==0.4.22 sentence-transformers==2.2.2
pip install python-multipart==0.0.6 pydantic==2.5.3 requests==2.31.0
```

### Step 3: Frontend Setup

```bash
cd rag-frontend

# Install dependencies
npm install

# Or using yarn
yarn install
```

## 🚀 Running the Application

### Start Backend Server

```bash
cd rag-backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: http://localhost:8000
API docs: http://localhost:8000/docs

### Start Frontend Server

```bash
cd rag-frontend
npm run dev
```

Frontend will be available at: http://localhost:3000/chat

## 📡 API Documentation

### 1. Ingest Documents

**Endpoint:** `POST /ingest/`

**Content-Type:** `multipart/form-data`

**Parameters:**
- `file` (optional): Text file to upload
- `text` (optional): Raw text string
- `metadata` (optional): JSON string with metadata

**Example:**
```bash
# Ingest raw text
curl -X POST "http://localhost:8000/ingest/" \
  -F "text=Spec engineering is the practice of designing effective prompts for AI systems." \
  -F "metadata={\"source\": \"glossary\"}"

# Ingest file
curl -X POST "http://localhost:8000/ingest/" \
  -F "file=@document.txt" \
  -F "metadata={\"source\": \"uploaded_doc\"}"
```

**Response:**
```json
{
  "status": "success",
  "message": "Document ingested",
  "chunks": 5
}
```

### 2. Query with Session Memory

**Endpoint:** `POST /query/`

**Content-Type:** `application/json`

**Request Body:**
```json
{
  "question": "What is spec engineering?",
  "session_id": "optional-session-uuid"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/query/" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is spec engineering?",
    "session_id": "session-123"
  }'
```

**Response:**
```json
{
  "answer": "Spec engineering is the practice of designing effective prompts for AI systems.",
  "sources": ["glossary"]
}
```

### 3. Clear Session

**Endpoint:** `DELETE /query/{session_id}`

**Example:**
```bash
curl -X DELETE "http://localhost:8000/query/session-123"
```

## 💬 Session Management (Memory)

The RAG system now supports conversation memory using session IDs:

- Each chat session has a unique `session_id`
- Previous messages in the session are included in the LLM prompt
- Last 10 messages are retained per session
- Sessions persist in memory while backend is running

**Frontend Implementation:**
- Session ID is auto-generated on page load
- Sent with every query to maintain context
- Enables follow-up questions with context

**Example Conversation:**
```
User: "What is machine learning?"
Assistant: [Answers based on ingested docs]

User: "How does it differ from deep learning?"  ← Context retained
Assistant: [Answers with knowledge of previous question]
```

## 🧪 Testing

### Test Backend Endpoints

```bash
# Test health check
curl http://localhost:8000/

# Ingest test document
curl -X POST "http://localhost:8000/ingest/" \
  -F "text=Python is a programming language. Machine learning uses Python."

# Query the document
curl -X POST "http://localhost:8000/query/" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Python?", "session_id": "test-1"}'
```

### Test Frontend Connection

1. Open http://localhost:3000/chat
2. Type a question and send
3. Verify response appears
4. Check browser console for any errors

## 🎨 Frontend Features

- **Dark Theme**: ChatGPT-like dark interface
- **Auto-scroll**: Automatically scrolls to latest message
- **Loading States**: Shows "Thinking..." while waiting
- **Error Handling**: Displays connection errors
- **Session Memory**: Maintains conversation context
- **Responsive Design**: Works on desktop and mobile

## ⚡ Performance Optimizations

1. **Early Return in Retrieval**: Returns immediately if no relevant context found
2. **Session-based Caching**: Avoids re-processing same session queries
3. **Chunked Embeddings**: Efficient batch processing
4. **Cosine Similarity**: Fast vector search with ChromaDB

## 🔧 Configuration

### Backend Configuration

Edit `app/services/embedding_service.py` to change embedding model:
```python
class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
```

Edit `app/services/llm_service.py` to change LLM settings:
```python
def __init__(self, base_url: str = "http://localhost:11434", model: str = "qwen3:4b"):
    ...
    "temperature": 0.7,  # Adjust creativity
    "top_p": 0.9         # Adjust randomness
```

### Frontend Configuration

Edit `lib/api.ts` to change backend URL:
```typescript
const res = await fetch("http://localhost:8000/query/", ...);
```

## ❗ Troubleshooting

### Backend Issues

**Problem:** `NameError: name 'nn' is not defined`
**Solution:** Install compatible versions:
```bash
pip install transformers==4.36.2 sentence-transformers==2.2.2
```

**Problem:** Ollama connection error
**Solution:** Ensure Ollama is running:
```bash
ollama serve
ollama pull qwen3:4b
```

**Problem:** ChromaDB persistence error
**Solution:** Check `data/` directory permissions

### Frontend Issues

**Problem:** CORS errors
**Solution:** Backend already includes CORS middleware for all origins

**Problem:** Can't connect to backend
**Solution:** Ensure backend is running on port 8000

## 📝 Development Notes

- Backend uses in-memory session storage (resets on restart)
- For production, consider Redis or database-backed sessions
- ChromaDB persists to `data/chroma_db/` directory
- LLM calls have 120-second timeout

## 🔒 Security Considerations

For production deployment:
1. Add authentication to API endpoints
2. Use proper CORS origins (not `*`)
3. Validate and sanitize all inputs
4. Rate limit API endpoints
5. Use HTTPS in production
6. Consider containerization (Docker)

## 📄 License

MIT License

## 👥 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

**Last Updated:** May 2026
**Version:** 1.0.0
#   l o c a l - r a g - s y s t e m  
 