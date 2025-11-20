"""
Data Structures for AI
----------------------
Manipulación de listas y diccionarios en el contexto de un chatbot.
Manipulation of lists and dictionaries in a chatbot context.
"""

def manage_chat_history():
    # Lista de Diccionarios: La estructura estándar de OpenAI
    messages = [
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¿Quién ganó el mundial 2022?"}
    ]
    
    print("--- Historial Inicial ---")
    for msg in messages:
        print(f"[{msg['role'].upper()}]: {msg['content']}")
        
    # Agregar nuevo mensaje (Append)
    new_response = {
        "role": "assistant",
        "content": "Argentina ganó el mundial 2022.",
        "metadata": {"tokens": 15, "latency": 0.4} # Diccionario anidado
    }
    messages.append(new_response)
    
    # Acceder a datos anidados
    last_msg = messages[-1]
    tokens = last_msg["metadata"]["tokens"]
    print(f"\nÚltima respuesta usó {tokens} tokens.")
    
    # List Comprehension (Técnica Avanzada y muy usada)
    # Extraer solo el contenido de los mensajes del usuario
    user_contents = [m["content"] for m in messages if m["role"] == "user"]
    print(f"\nMensajes de usuario: {user_contents}")

def vocabulary_demo():
    text = "inteligencia artificial generativa inteligencia de datos"
    words = text.split()
    
    # Set para eliminar duplicados
    vocab = set(words)
    print(f"\nTexto original: {len(words)} palabras")
    print(f"Vocabulario único: {len(vocab)} palabras ({vocab})")

if __name__ == "__main__":
    manage_chat_history()
    vocabulary_demo()
