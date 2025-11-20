"""
Structured Outputs (JSON Mode)
------------------------------
Cómo forzar al modelo a responder en JSON válido.
How to force the model to respond in valid JSON.
"""

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_movie_info(movie_name: str):
    print(f"🎬 Fetching info for: {movie_name}")
    
    system_prompt = """
    You are a movie database assistant.
    You MUST respond with a valid JSON object containing:
    - title: str
    - year: int
    - director: str
    - genres: list[str]
    - summary: str (1 sentence)
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Tell me about '{movie_name}'"}
            ],
            response_format={"type": "json_object"}, # 👈 MAGIC SWITCH
            temperature=0.1 # Low temp for consistency
        )
        
        json_content = response.choices[0].message.content
        print("\n--- Raw JSON Response ---")
        print(json_content)
        
        # Parse to Python Dict to prove it's valid
        data = json.loads(json_content)
        print(f"\n✅ Parsed Director: {data.get('director')}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Please set OPENAI_API_KEY")
    else:
        get_movie_info("Inception")
