"""
Advanced Prompt Engineering
---------------------------
Ejemplos de técnicas avanzadas: Few-Shot y Chain of Thought (CoT).
Examples of advanced techniques: Few-Shot and Chain of Thought (CoT).

Requisitos: pip install openai
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(messages, model="gpt-4o"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.0 # Deterministic for logic
    )
    return response.choices[0].message.content

def few_shot_demo():
    print("\n--- 1. Few-Shot Prompting Demo ---")
    print("Task: Classify customer sentiment into categories (Urgent, General, Spam).")
    
    # Sin ejemplos (Zero-Shot) - A veces falla en formato
    # Without examples (Zero-Shot) - Sometimes fails formatting
    
    # Con Ejemplos (Few-Shot)
    prompt = """
    Clasifica los siguientes mensajes.
    
    Mensaje: "Mi tarjeta fue robada, ayúdenme ya!"
    Clasificación: Urgent
    
    Mensaje: "¿A qué hora abren mañana?"
    Clasificación: General
    
    Mensaje: "Gana 1000 dólares hoy click aquí"
    Clasificación: Spam
    
    Mensaje: "Hice una transferencia y no llegó, necesito el dinero para pagar la renta hoy."
    Clasificación:
    """
    
    messages = [{"role": "user", "content": prompt}]
    result = get_completion(messages)
    print(f"Input: ...necesito el dinero para pagar la renta hoy.")
    print(f"Output: {result}")

def chain_of_thought_demo():
    print("\n--- 2. Chain of Thought (CoT) Demo ---")
    print("Task: Solve a logic puzzle.")
    
    question = "If I have 3 apples, eat one, buy two more, and then give half of my total to a friend, how many do I have left?"
    
    # Standard Prompt (Zero-Shot) - Models might guess quickly
    # CoT Prompt (Zero-Shot CoT) - "Let's think step by step"
    
    prompt = f"""
    Q: {question}
    A: Let's think step by step.
    """
    
    messages = [{"role": "user", "content": prompt}]
    result = get_completion(messages)
    print(f"Question: {question}")
    print(f"Reasoning:\n{result}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY")
    else:
        few_shot_demo()
        chain_of_thought_demo()
