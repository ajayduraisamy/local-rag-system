from app.services.embedding_service import EmbeddingService
from app.services.retriever_service import RetrieverService
from app.services.llm_service import LLMService
from app.services.session_service import SessionService
from app.utils.chunking import TextChunker
from app.utils.prompt_builder import PromptBuilder

class RAGService:
    def __init__(self):
        self.chunker = TextChunker()
        self.embedding_service = EmbeddingService()
        self.retriever = RetrieverService()
        self.llm_service = LLMService()
        self.prompt_builder = PromptBuilder()
        self.session_service = SessionService()

    async def ingest_text(self, text: str, metadata: str | None = None):
        chunks = self.chunker.chunk_text(text)
        embeddings = self.embedding_service.encode(chunks)
        
        meta_list = None
        if metadata:
            import json
            try:
                meta_list = [json.loads(metadata) for _ in chunks]
            except:
                meta_list = [{"source": "unknown"} for _ in chunks]
        
        self.retriever.store_embeddings(chunks, embeddings, meta_list)
        return len(chunks)

    async def process_query(self, question: str, session_id: str | None = None):
        query_embedding = self.embedding_service.encode([question])[0]
        relevant_chunks = self.retriever.search(query_embedding, top_k=3)
        
        if not relevant_chunks:
            return {"answer": "No relevant context found.", "sources": []}
        
        context = "\n\n".join([chunk["text"] for chunk in relevant_chunks])
        sources = [chunk.get("metadata", {}).get("source", "unknown") for chunk in relevant_chunks]
        
        history = []
        if session_id:
            self.session_service.add_message(session_id, "user", question)
            history = self.session_service.get_history(session_id)
        
        prompt = self.prompt_builder.build_prompt(context, question, history)
        answer = await self.llm_service.generate(prompt)
        
        if session_id:
            self.session_service.add_message(session_id, "assistant", answer)
        
        return {"answer": answer, "sources": sources}
    
    def clear_session(self, session_id: str):
        self.session_service.clear_session(session_id)
