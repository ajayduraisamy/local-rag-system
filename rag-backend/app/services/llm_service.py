import requests
import json

class LLMService:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "qwen3:4b"):
        self.base_url = base_url
        self.model = model
        self.api_endpoint = f"{base_url}/api/generate"
    
    async def generate(self, prompt: str) -> str:
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9
                }
            }
            
            response = requests.post(self.api_endpoint, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "").strip()
        except requests.exceptions.RequestException as e:
            return f"Error communicating with Ollama: {str(e)}"
