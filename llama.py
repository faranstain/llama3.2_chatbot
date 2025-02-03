
from typing import Dict, List
from collections import defaultdict
import ollama

class LlamaChatManager:
    def __init__(self):
        self.histories = defaultdict(lambda: defaultdict(list))
        self.max_history = 10

    def get_response(self, user_id: str, conversation_id: str, message: str) -> str:
        try:
            
            history = self.histories[user_id][conversation_id]            
            history.append({"role": "user", "content": message})

            if len(history) > self.max_history:
                history = history[-self.max_history:]

            response = ollama.chat(model="llama3.2", messages=history)
            model_response = response["message"]["content"]
            history.append({"role": "assistant", "content": model_response})
            
            self.histories[user_id][conversation_id] = history
            
            return model_response
            
        except Exception as e:
            return f"Error: {str(e)}"


llama_manager = LlamaChatManager()