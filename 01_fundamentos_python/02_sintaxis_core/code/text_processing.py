"""
Text Processing for AI
----------------------
Este script demuestra técnicas de manipulación de texto esenciales para
la ingeniería de prompts y la limpieza de respuestas de LLMs.

This script demonstrates text manipulation techniques essential for
prompt engineering and cleaning LLM responses.
"""

import re

def clean_llm_response(raw_text: str) -> str:
    """
    Limpia una respuesta típica de un LLM que puede contener bloques de código markdown.
    Cleans a typical LLM response that might contain markdown code blocks.
    """
    print(f"--- Raw Text ---\n{raw_text}\n")
    
    # Regex to remove ```json ... ``` or just ``` ... ```
    # Pattern explanation:
    # ```       : Match literal backticks
    # (?:json)? : Non-capturing group, optionally match 'json'
    # \s*       : Match any whitespace
    # (.*?)     : Non-greedy match of content
    # ```       : Match literal backticks
    pattern = r"```(?:json)?\s*(.*?)```"
    
    match = re.search(pattern, raw_text, re.DOTALL)
    
    if match:
        cleaned = match.group(1).strip()
        print(f"--- Cleaned Text (Regex Extracted) ---\n{cleaned}\n")
        return cleaned
    else:
        print("--- No markdown code block found, returning original ---\n")
        return raw_text.strip()

def create_dynamic_prompt(topic: str, level: str = "beginner") -> str:
    """
    Usa f-strings para crear un prompt estructurado.
    Uses f-strings to create a structured prompt.
    """
    # Multi-line f-string for clear prompt structure
    prompt = f"""
    Role: You are an expert teacher.
    Task: Explain the concept of '{topic}'.
    Target Audience: {level} level students.
    Format: Provide a bulleted list of key points.
    """
    return prompt.strip()

if __name__ == "__main__":
    # Ejemplo 1: Limpieza de respuesta / Example 1: Response Cleaning
    fake_llm_output = """
    Here is the JSON you requested:
    ```json
    {
        "answer": "Paris",
        "confidence": 0.98
    }
    ```
    Hope that helps!
    """
    clean_llm_response(fake_llm_output)
    
    # Ejemplo 2: Creación de Prompt / Example 2: Prompt Creation
    my_prompt = create_dynamic_prompt("Generative Adversarial Networks", "advanced")
    print(f"--- Generated Prompt ---\n{my_prompt}")
