"""
Ollama Local Inference
----------------------
Conexión a un modelo Llama 3 corriendo localmente vía Ollama.
Connecting to a locally running Llama 3 model via Ollama.

Requisitos/Requirements:
pip install ollama
Ollama running (ollama serve)
"""

import ollama

def chat_local():
    print("--- Local Llama 3 Chat ---")
    
    try:
        # No necesitamos API Key
        response = ollama.chat(model='llama3', messages=[
            {
                'role': 'user',
                'content': 'Why is the sky blue? Answer in one sentence.',
            },
        ])
        
        print(f"🦙 Llama says: {response['message']['content']}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Ensure Ollama is installed and running 'ollama serve'")
        print("Ensure you have pulled the model: 'ollama pull llama3'")

if __name__ == "__main__":
    chat_local()
