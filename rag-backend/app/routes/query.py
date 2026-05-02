from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.rag_service import RAGService

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    session_id: str | None = None

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]

@router.post("/")
async def query(request: QueryRequest) -> QueryResponse:
    try:
        rag_service = RAGService()
        result = await rag_service.process_query(request.question, request.session_id)
        return QueryResponse(
            answer=result["answer"],
            sources=result["sources"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{session_id}")
async def clear_session(session_id: str):
    try:
        rag_service = RAGService()
        rag_service.clear_session(session_id)
        return {"status": "success", "message": f"Session {session_id} cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
