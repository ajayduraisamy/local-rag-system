# RAG Backend - FastAPI Service

Production-level RAG (Retrieval-Augmented Generation) backend using FastAPI.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- `POST /ingest/` - Ingest documents
- `POST /query/` - Query with session memory
- `DELETE /query/{session_id}` - Clear session
- `GET /` - Health check

See main [README.md](../README.md) for full documentation.
