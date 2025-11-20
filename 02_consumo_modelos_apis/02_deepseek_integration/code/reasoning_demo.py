"""
DeepSeek Reasoner (R1) Demo
---------------------------
Uso del modelo 'deepseek-reasoner' para tareas que requieren pensamiento complejo.
Using the 'deepseek-reasoner' model for tasks requiring complex thinking.
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def solve_logic_puzzle():
    print("--- DeepSeek R1 Logic Puzzle ---")
    
    puzzle = """
    Three people check into a hotel room. The clerk says the bill is $30, so each guest pays $10. 
    Later the clerk realizes the bill should only be $25. To fix this, he gives the bellboy $5 to return to the guests. 
    On the way to the room, the bellboy realizes that he cannot divide the money equally. 
    As the guests didn't know the total of the revised bill, the bellboy decides to just give each guest $1 back and keep $2 as a tip for himself. 
    Each guest got $1 back, so they paid $9 each, totaling $27. The bellboy has $2, totaling $29. 
    Where is the missing dollar?
    """
    
    try:
        # Usamos 'deepseek-reasoner' para activar la cadena de pensamiento
        response = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=[
                {"role": "user", "content": puzzle}
            ]
        )
        
        # En algunos SDKs/APIs, el proceso de pensamiento puede venir en un campo separado
        # o simplemente ser parte de una respuesta más elaborada.
        # DeepSeek R1 suele ser muy detallado en su explicación.
        
        print("🤖 Reasoning & Answer:")
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    solve_logic_puzzle()
