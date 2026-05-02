from app.db.chroma_client import ChromaClient

class RetrieverService:
    def __init__(self):
        self.chroma_client = ChromaClient()
        self.collection = self.chroma_client.get_collection()
    
    def store_embeddings(self, texts: list[str], embeddings: list[list[float]], metadatas: list[dict] | None = None):
        ids = [f"doc_{i}" for i in range(len(texts))]
        self.collection.add(
            ids=ids,
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas
        )
    
    def search(self, query_embedding: list[float], top_k: int = 3) -> list[dict]:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        chunks = []
        if results and "documents" in results:
            for i, doc in enumerate(results["documents"][0]):
                chunk = {
                    "text": doc,
                    "metadata": results["metadatas"][0][i] if results.get("metadatas") else {}
                }
                chunks.append(chunk)
        
        return chunks
