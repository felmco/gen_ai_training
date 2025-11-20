"""
Anthropic Claude API
--------------------
Uso del SDK de Anthropic para tareas de alto contexto.
Using the Anthropic SDK for high-context tasks.

Requisitos/Requirements:
pip install anthropic
"""

import os
from anthropic import Anthropic

# Asegúrate de tener ANTHROPIC_API_KEY
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analyze_large_text():
    print("--- Claude 3.5 Analysis ---")
    
    # Simulamos un texto largo
    long_text = "..." * 1000 # Placeholder
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are a summarization expert.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Summarize this text: {long_text}"
                        }
                    ]
                }
            ]
        )
        
        print(message.content[0].text)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Please set ANTHROPIC_API_KEY")
    else:
        analyze_large_text()
