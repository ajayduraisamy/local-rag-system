from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import query, ingest

app = FastAPI(
    title="RAG Backend",
    description="Production-level RAG system with local LLM",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])

@app.get("/")
async def root():
    return {"message": "RAG Backend is running"}
