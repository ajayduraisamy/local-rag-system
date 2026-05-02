from collections import defaultdict
from typing import List, Dict

class SessionService:
    def __init__(self, max_history: int = 10):
        self.sessions: Dict[str, List[Dict[str, str]]] = defaultdict(list)
        self.max_history = max_history
    
    def get_history(self, session_id: str) -> List[Dict[str, str]]:
        return self.sessions.get(session_id, [])[-self.max_history:]
    
    def add_message(self, session_id: str, role: str, content: str):
        self.sessions[session_id].append({"role": role, "content": content})
        if len(self.sessions[session_id]) > self.max_history:
            self.sessions[session_id] = self.sessions[session_id][-self.max_history:]
    
    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]
    
    def has_session(self, session_id: str) -> bool:
        return session_id in self.sessions and len(self.sessions[session_id]) > 0
