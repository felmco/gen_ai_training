"""
Simple OpenAI Chat
------------------
Un cliente de chat básico que mantiene el historial de conversación.
A basic chat client that maintains conversation history.

Requisitos/Requirements:
pip install openai
"""

import os
from openai import OpenAI

# Asegúrate de tener OPENAI_API_KEY en tus variables de entorno
# Ensure you have OPENAI_API_KEY in your environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_loop():
    print("--- OpenAI Chatbot (Type 'quit' to exit) ---")
    
    # Historial inicial / Initial history
    messages = [
        {"role": "system", "content": "You are a helpful and concise assistant."}
    ]
    
    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ['quit', 'exit']:
            break
            
        # Agregar mensaje del usuario al historial
        # Add user message to history
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.7
            )
            
            assistant_msg = response.choices[0].message.content
            print(f"Assistant: {assistant_msg}")
            
            # Agregar respuesta del asistente al historial para mantener contexto
            # Add assistant response to history to maintain context
            messages.append({"role": "assistant", "content": assistant_msg})
            
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  WARNING: OPENAI_API_KEY not found in environment variables.")
        print("   Set it with: export OPENAI_API_KEY='sk-...'(Linux/Mac) or $env:OPENAI_API_KEY='sk-...'(Windows)")
    else:
        chat_loop()
