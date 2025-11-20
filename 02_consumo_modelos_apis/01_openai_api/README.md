# Módulo 2.1: Fundamentos de la API de OpenAI

La API de OpenAI definió el estándar de la industria. Entender su estructura es entender cómo interactuar con casi cualquier LLM moderno.

## 1. El Ciclo de Chat Completions

La interacción no es una pregunta y respuesta aislada; es una lista de mensajes que crece.

### Roles
*   **System:** Define el comportamiento, tono y reglas del asistente. Es la "instrucción maestra".
*   **User:** La entrada del usuario final.
*   **Assistant:** La respuesta del modelo (que volvemos a enviar para mantener el contexto).

```python
messages = [
    {"role": "system", "content": "Eres un experto en finanzas."},
    {"role": "user", "content": "¿Qué es el interés compuesto?"},
    {"role": "assistant", "content": "Es el interés sobre el interés..."},
    {"role": "user", "content": "Dame un ejemplo numérico."}
]
```

## 2. Parámetros de Control

*   **Temperature (0.0 - 2.0):** Creatividad vs. Determinismo.
    *   `0.0`: Respuestas precisas, repetibles (Código, Matemáticas).
    *   `0.7`: Balanceado (Chat general).
    *   `1.5+`: Caótico/Muy creativo (Lluvia de ideas).
*   **Top-P:** Una alternativa a la temperatura (nuclear sampling). Generalmente se modifica uno u otro, no ambos.
*   **Max Tokens:** Límite duro de la respuesta para controlar costos y latencia.

## 3. Structured Outputs (JSON Mode)

Para integrar LLMs en software, necesitamos que respondan en JSON, no en prosa.
OpenAI permite forzar esto con `response_format={"type": "json_object"}`.

> **Importante:** Siempre debes instruir al modelo en el *System Prompt* para que genere JSON, además de activar el parámetro.

## Ejercicio Práctico

Revisa los scripts en `code/`:
1.  `simple_chat.py`: Un chatbot de consola básico.
2.  `structured_output.py`: Extracción de datos en formato JSON garantizado.
