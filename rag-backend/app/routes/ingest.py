from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.rag_service import RAGService

router = APIRouter()

@router.post("/")
async def ingest(
    file: UploadFile | None = None,
    text: str | None = None,
    metadata: str | None = None
):
    try:
        rag_service = RAGService()
        
        if file:
            content = await file.read()
            text_content = content.decode("utf-8")
            result = await rag_service.ingest_text(text_content, metadata)
        elif text:
            result = await rag_service.ingest_text(text, metadata)
        else:
            raise HTTPException(status_code=400, detail="Either file or text must be provided")
        
        return {"status": "success", "message": "Document ingested", "chunks": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
