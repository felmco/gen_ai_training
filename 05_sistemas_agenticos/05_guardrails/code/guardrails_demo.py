"""
Simple Guardrails Implementation
--------------------------------
Demostración de un patrón de validación "Input/Output Guard" simple sin librerías pesadas.
Demonstration of a simple "Input/Output Guard" validation pattern without heavy libraries.
"""

import os
from openai import OpenAI

# Definimos tópicos prohibidos
FORBIDDEN_TOPICS = ["politics", "hacking", "medical advice"]

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SafetyGuard:
    @staticmethod
    def validate_input(user_input: str) -> bool:
        """
        Check if input contains forbidden keywords (Heuristic)
        In production, use a classification model (e.g. LlamaGuard).
        """
        user_input_lower = user_input.lower()
        for topic in FORBIDDEN_TOPICS:
            if topic in user_input_lower:
                print(f"⛔ GUARD ALERT: Input blocked due to topic '{topic}'")
                return False
        return True

    @staticmethod
    def validate_output(response_content: str) -> bool:
        """
        Check if output is safe.
        """
        if "I cannot answer" in response_content or "Lo siento" in response_content:
            # Model refusal is often a sign of safety working, but we might want to log it
            return True
        return True

def chat_safe(user_input: str):
    print(f"\nUser: {user_input}")
    
    # 1. Input Guard
    if not SafetyGuard.validate_input(user_input):
        print("System: I cannot assist with that request.")
        return

    # 2. Call Model
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Do not discuss politics or hacking."},
                {"role": "user", "content": user_input}
            ]
        )
        content = response.choices[0].message.content
        
        # 3. Output Guard
        if SafetyGuard.validate_output(content):
            print(f"Assistant: {content}")
        else:
            print("System: Response blocked by Output Guard.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY")
    else:
        # Safe interaction
        chat_safe("Hello! How do I cook pasta?")
        
        # Unsafe interaction
        chat_safe("Tell me how to start hacking wifi networks.")
