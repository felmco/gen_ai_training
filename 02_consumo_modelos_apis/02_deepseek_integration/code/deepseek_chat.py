"""
DeepSeek Integration
--------------------
Uso de DeepSeek como reemplazo directo de OpenAI.
Using DeepSeek as a drop-in replacement for OpenAI.
"""

import os
from openai import OpenAI

# Configuración para DeepSeek / DeepSeek Configuration
# Se usa el mismo cliente de OpenAI, pero apuntando a otra URL
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek():
    print("--- DeepSeek Chat ---")
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat", # O 'deepseek-coder'
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Explain the concept of 'Context Caching' briefly."}
            ],
            stream=False
        )
        
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Ensure DEEPSEEK_API_KEY is set.")

if __name__ == "__main__":
    chat_with_deepseek()
