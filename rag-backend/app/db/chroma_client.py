import chromadb
from chromadb.config import Settings
import os

class ChromaClient:
    def __init__(self, persist_directory: str = "data/chroma_db"):
        self.persist_directory = persist_directory
        
        os.makedirs(persist_directory, exist_ok=True)
        
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(
                allow_reset=True,
                anonymized_telemetry=False
            )
        )
        
        self.collection_name = "rag_documents"
    
    def get_collection(self):
        return self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )
    
    def reset_collection(self):
        self.client.delete_collection(self.collection_name)
        return self.get_collection()
