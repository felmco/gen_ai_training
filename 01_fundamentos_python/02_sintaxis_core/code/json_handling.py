"""
JSON Handling for AI APIs
-------------------------
Demostración de serialización y deserialización de JSON, simulando
interacciones con APIs de IA.

Demonstration of JSON serialization and deserialization, simulating
AI API interactions.
"""

import json
from typing import Dict, Any

def simulate_api_payload(user_query: str, model: str = "gpt-4o") -> str:
    """
    Crea un payload JSON para enviar a una API.
    Creates a JSON payload to send to an API.
    """
    # Python Dictionary
    payload_dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ],
        "temperature": 0.7
    }
    
    # Convert Dict -> JSON String (Serialization)
    # ensure_ascii=False permite caracteres especiales (tildes, ñ)
    json_str = json.dumps(payload_dict, indent=2, ensure_ascii=False)
    return json_str

def parse_api_response(json_response: str) -> Dict[str, Any]:
    """
    Parsea una respuesta JSON string a un diccionario de Python.
    Parses a JSON string response into a Python dictionary.
    """
    try:
        # Convert JSON String -> Dict (Deserialization)
        data = json.loads(json_response)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON: {e}")
        return {}

if __name__ == "__main__":
    # 1. Preparar datos para la API / Prepare data for API
    query = "¿Cuál es la capital de España?"
    payload = simulate_api_payload(query)
    print(f"--- API Payload (JSON String) ---\n{payload}\n")
    
    # 2. Simular recibir respuesta / Simulate receiving response
    # Simulamos una respuesta típica de OpenAI
    mock_response_str = """
    {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "La capital de España es Madrid."
            },
            "finish_reason": "stop"
        }],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21
        }
    }
    """
    
    response_dict = parse_api_response(mock_response_str)
    
    # Acceder a datos anidados / Access nested data
    if response_dict:
        content = response_dict["choices"][0]["message"]["content"]
        print(f"--- Parsed Content ---\n{content}")
