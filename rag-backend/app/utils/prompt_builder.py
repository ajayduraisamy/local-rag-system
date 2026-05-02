class PromptBuilder:
    def __init__(self):
        self.template = """You are an expert AI assistant.

Use ONLY the context below and the conversation history to answer the question. If the answer is not in the context or history, say "I don't have enough information to answer this question."

Context:
{context}

Conversation History:
{history}

Question:
{question}

Answer clearly and accurately."""
    
    def build_prompt(self, context: str, question: str, history: list = None) -> str:
        history_text = ""
        if history:
            history_lines = [f"{msg['role'].upper()}: {msg['content']}" for msg in history]
            history_text = "\n".join(history_lines)
        else:
            history_text = "No previous conversation."
        
        return self.template.format(context=context, history=history_text, question=question)
