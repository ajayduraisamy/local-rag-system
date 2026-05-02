# 🤖 RAG System - Retrieval-Augmented Generation

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.109.0-green?style=flat-square&logo=fastapi" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Next.js-14-black?style=flat-square&logo=nextdotjs" alt="Next.js" />
  <img src="https://img.shields.io/badge/TypeScript-5.0-blue?style=flat-square&logo=typescript" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Tailwind%20CSS-3.3-38B2AC?style=flat-square&logo=tailwindcss" alt="Tailwind" />
  <img src="https://img.shields.io/badge/ChromaDB-Vector%20DB-orange?style=flat-square" alt="ChromaDB" />
  <img src="https://img.shields.io/badge/Ollama-qwen3%3A4b-purple?style=flat-square" alt="Ollama" />
</p>

<p align="center">
  <strong>A production-ready RAG (Retrieval-Augmented Generation) system with a modern ChatGPT-like interface</strong>
</p>

<p align="center">
  <a href="#overview">Quick Start</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#api-documentation">API</a> •
  <a href="#frontend-preview">Preview</a>
</p>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Session Management](#session-management-memory)
- [Testing](#testing)
- [Frontend Preview](#frontend-preview)
- [Performance Optimizations](#performance-optimizations)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This is a complete **Retrieval-Augmented Generation (RAG)** system that enables you to:

- ✅ Ingest documents (text files or raw text)
- ✅ Convert documents into vector embeddings using `sentence-transformers`
- ✅ Store embeddings in **ChromaDB** (vector database)
- ✅ Retrieve relevant context based on user queries
- ✅ Generate accurate answers using **local LLM** (Ollama with `qwen3:4b`)
- ✅ Maintain conversation history with **session-based memory**
- ✅ Chat via a modern **Next.js** frontend with dark theme

---

## 🏗 Architecture

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                          RAG System Architecture                        │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐     HTTP/REST API     ┌──────────────────────────────┐
│                 │ ◄───────────────────► │                              │
│   Frontend      │                       │     Backend (FastAPI)        │
│   (Next.js)     │                       │                              │
│                 │                       │  ┌────────────────────────┐  │
│  ┌───────────┐  │                       │  │   RAG Service          │  │
│  │ Chat UI   │  │                       │  │   - Orchestration      │  │
│  └───────────┘  │                       │  └──────────┬───────────┘  │
│  ┌───────────┐  │                       │             │              │
│  │Session Mgmt│  │                       │  ┌──────────▼───────────┐  │
│  └───────────┘  │                       │  │ Embedding Service    │  │
│  ┌───────────┐  │                       │  │ - sentence-transformers│ │
│  │ API Client │  │                       │  └──────────┬───────────┘  │
│  └───────────┘  │                       │             │              │
└─────────────────┘                       │  ┌──────────▼───────────┐  │
                                         │  │ Retriever Service    │  │
                                         │  │ - Vector Search      │  │
                                         │  └──────────┬───────────┘  │
                                         │             │              │
                                         │  ┌──────────▼───────────┐  │
                                         │  │ LLM Service          │  │
                                         │  │ - Ollama Integration │  │
                                         │  │ - qwen3:4b Model    │  │
                                         │  └──────────┬───────────┘  │
                                         │             │              │
                                         └─────────────┼──────────────┘
                                                          │
                          ┌───────────────────────────────┼───────────────────────────────┐
                          │                               │                               │
                   ┌──────▼──────┐                ┌───────▼───────┐                ┌──────▼──────┐
                   │  ChromaDB   │                │   Ollama LLM  │                │   Document  │
                   │  (Vectors)  │                │   (qwen3:4b)  │                │  Ingestion  │
                   └─────────────┘                └───────────────┘                └─────────────┘
```

---

## 🛠 Tech Stack

### Backend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Python** | 3.10+ | Programming Language |
| **FastAPI** | 0.109.0 | Web Framework |
| **ChromaDB** | 0.4.22 | Vector Database |
| **sentence-transformers** | 2.2.2 | Embedding Generation |
| **Ollama** | Latest | Local LLM Runtime |
| **qwen3:4b** | Latest | Language Model |

### Frontend
| Technology | Version | Purpose |
|-----------|---------|---------|
| **Next.js** | 14 | React Framework |
| **TypeScript** | 5.0+ | Type Safety |
| **Tailwind CSS** | 3.3+ | Styling |
| **React** | 18.2+ | UI Library |

---

## ✨ Features

### Backend Features
- 🚀 **FastAPI** with automatic OpenAPI documentation
- 📄 **Document Ingestion** - Support for text files and raw text
- 🔍 **Vector Search** - Efficient similarity search with ChromaDB
- 🧠 **Session Memory** - Maintains conversation context (last 10 messages)
- 🤖 **Local LLM** - No API costs, runs entirely locally
- 📦 **Batch Processing** - Efficient chunk embedding

### Frontend Features
- 🎨 **Dark Theme** - ChatGPT-like modern interface
- 💬 **Real-time Chat** - Instant message updates
- 🔄 **Auto-scroll** - Automatically scrolls to latest message
- ⏳ **Loading States** - "Thinking..." indicator
- ⚠️ **Error Handling** - Graceful error display
- 📱 **Responsive Design** - Works on desktop and mobile
- 🧠 **Session Memory** - Maintains conversation context

---

## 📁 Project Structure

```text
rag/
├── 📂 rag-backend/                    # Python FastAPI Backend
│   ├── 📂 app/
│   │   ├── main.py                # FastAPI app entry point
│   │   ├── 📂 routes/
│   │   │   ├── query.py           # Query endpoint with session support
│   │   │   └── ingest.py          # Document ingestion endpoint
│   │   ├── 📂 services/
│   │   │   ├── rag_service.py     # Main RAG orchestration
│   │   │   ├── embedding_service.py  # Text to vector embeddings
│   │   │   ├── llm_service.py     # Ollama LLM integration
│   │   │   ├── retriever_service.py   # Vector similarity search
│   │   │   └── session_service.py # Conversation memory
│   │   ├── 📂 utils/
│   │   │   ├── chunking.py        # Text splitting logic
│   │   │   └── prompt_builder.py  # LLM prompt construction
│   │   └── 📂 db/
│   │       └── chroma_client.py   # ChromaDB client wrapper
│   ├── 📂 data/                      # Persistent storage (ChromaDB)
│   └── requirements.txt              # Python dependencies
│
├── 📂 rag-frontend/                   # Next.js Frontend
│   ├── 📂 app/
│   │   ├── 📂 chat/
│   │   │   └── page.tsx              # Main chat interface
│   │   ├── layout.tsx                # Root layout
│   │   ├── page.tsx                  # Redirects to /chat
│   │   └── globals.css               # Global styles
│   ├── 📂 components/
│   │   ├── ChatContainer.tsx         # Message list with auto-scroll
│   │   ├── ChatInput.tsx             # Input field with send button
│   │   └── ChatMessage.tsx           # Individual message bubble
│   ├── 📂 lib/
│   │   └── api.ts                    # Backend API client
│   ├── 📂 types/
│   │   └── chat.ts                   # TypeScript type definitions
│   ├── package.json                  # Node dependencies
│   ├── tsconfig.json                 # TypeScript config
│   ├── tailwind.config.js            # Tailwind CSS config
│   └── next.config.js                # Next.js config
│
└── README.md                         # This file
```

---

## ⚙️ Installation

### Prerequisites

| Requirement | Version | Installation Link |
|------------|---------|-------------------|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| Node.js | 18+ | [nodejs.org](https://nodejs.org/) |
| Ollama | Latest | [ollama.com](https://ollama.com) |

### Step 1: Install Ollama and Pull Model

```bash
# Install Ollama from https://ollama.com

# Pull the required model
ollama pull qwen3:4b

# Verify installation
ollama list
```

### Step 2: Backend Setup

```bash
# Navigate to backend directory
cd rag-backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

<details>
<summary>⚠️ Having dependency issues? Click here</summary>

```bash
# Install compatible versions manually
pip install fastapi==0.109.0 uvicorn[standard]==0.27.0
pip install chromadb==0.4.22 sentence-transformers==2.2.2
pip install python-multipart==0.0.6 pydantic==2.5.3 requests==2.31.0

# If you encounter 'nn' not defined error:
pip install transformers==4.36.2
```
</details>

### Step 3: Frontend Setup

```bash
# Navigate to frontend directory
cd rag-frontend

# Install dependencies
npm install

# Or using yarn
yarn install
```

---

## 🔧 Configuration

### Backend Configuration

**Change Embedding Model** - Edit `app/services/embedding_service.py`:
```python
class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
```

**Change LLM Settings** - Edit `app/services/llm_service.py`:
```python
def __init__(self, base_url: str = "http://localhost:11434", model: str = "qwen3:4b"):
    ...
    "temperature": 0.7,  # Adjust creativity (0.0 - 1.0)
    "top_p": 0.9         # Adjust randomness (0.0 - 1.0)
```

### Frontend Configuration

**Change Backend URL** - Edit `lib/api.ts`:
```typescript
const res = await fetch("http://localhost:8000/query/", ...);
```

---

## 🚀 Running the Application

### Start Backend Server

```bash
cd rag-backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will be available at:**
- 🌐 API: http://localhost:8000
- 📚 API Docs (Swagger): http://localhost:8000/docs
- 📖 ReDoc: http://localhost:8000/redoc

### Start Frontend Server

```bash
cd rag-frontend
npm run dev
```

**Frontend will be available at:**
- 🌐 Chat Interface: http://localhost:3000/chat

---

## 📡 API Documentation

### 1. Ingest Documents

**Endpoint:** `POST /ingest/`

**Content-Type:** `multipart/form-data`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | File | Optional | Text file to upload |
| `text` | String | Optional | Raw text string |
| `metadata` | JSON String | Optional | Additional metadata |

**Examples:**

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

---

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

---

### 3. Clear Session

**Endpoint:** `DELETE /query/{session_id}`

**Example:**
```bash
curl -X DELETE "http://localhost:8000/query/session-123"
```

---

## 💬 Session Management (Memory)

The RAG system supports **conversation memory** using session IDs:

| Feature | Description |
|---------|-------------|
| **Session ID** | Each chat session has a unique identifier |
| **Context Retention** | Previous messages included in LLM prompt |
| **Message Limit** | Last 10 messages retained per session |
| **Persistence** | Sessions persist in memory while backend is running |

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

---

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

---

## 🎨 Frontend Preview

```text
┌─────────────────────────────────────────────────────────┐
│  🤖 RAG Chat System                     [🔄 New Chat]  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  🤖  Hello! I'm your RAG assistant. Ask me anything    │
│     about the documents you've ingested.                │
│                                                         │
│         💬 What is machine learning?                    │
│                                                         │
│  🤖  Machine learning is a subset of AI that enables   │
│     systems to learn from data...                       │
│                                                         │
│         💬 How does it work?                            │
│                                                         │
│  🤖  It works by... [uses context from previous Q&A]   │
│                                                         │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  [Type your message...               ]  [📤 Send]      │
└─────────────────────────────────────────────────────────┘
```

---

## ⚡ Performance Optimizations

| Optimization | Description |
|--------------|-------------|
| **Early Return** | Returns immediately if no relevant context found |
| **Session Caching** | Avoids re-processing same session queries |
| **Chunked Embeddings** | Efficient batch processing |
| **Cosine Similarity** | Fast vector search with ChromaDB |

---


## 📝 Development Notes

- Backend uses **in-memory session storage** (resets on restart)
- For production, consider **Redis** or database-backed sessions
- ChromaDB persists to `data/chroma_db/` directory
- LLM calls have **120-second timeout**
- All embeddings are computed locally (no external API calls)

---

## 🔒 Security Considerations

For **production deployment**, implement these:

- [ ] Add authentication to API endpoints
- [ ] Use proper CORS origins (not `*`)
- [ ] Validate and sanitize all inputs
- [ ] Rate limit API endpoints
- [ ] Use HTTPS in production
- [ ] Consider containerization (Docker)
- [ ] Add request/response logging
- [ ] Implement input size limits

---

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use TypeScript strict mode for frontend
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

---



## 👥 Authors & Acknowledgments

- **Developer:** [Ajay]
- **Built with:** FastAPI, Next.js, ChromaDB, Ollama

Special thanks to the open-source community!

---



<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=flat-square" alt="Made with Love" />
  <img src="https://img.shields.io/badge/Open%20Source-MIT-green?style=flat-square" alt="Open Source" />
</p>

<p align="center">
  <sub>Built with modern technologies for the AI community 🚀</sub>
</p>
