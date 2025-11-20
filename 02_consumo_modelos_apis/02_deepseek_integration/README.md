# Módulo 2.2: Integración de DeepSeek (El Retador Open Source)

DeepSeek ha irrumpido en el mercado ofreciendo rendimiento comparable a GPT-4 a una fracción del costo. Su integración es sencilla gracias a la compatibilidad con la API de OpenAI.

## 1. Economía de Tokens

DeepSeek-V3 ofrece precios extremadamente competitivos. Esto permite arquitecturas donde un modelo "barato" pero inteligente maneja el 90% de la carga, y solo se escala a modelos más costosos para tareas críticas.

## 2. Compatibilidad SDK (Drop-in Replacement)

DeepSeek usa el mismo formato de mensajes que OpenAI. Solo necesitas cambiar:
1.  `base_url`: Generalmente `https://api.deepseek.com`
2.  `api_key`: Tu clave de DeepSeek.
3.  `model`: `deepseek-chat` o `deepseek-reasoner`.

## 3. Modelos de Razonamiento (R1)

DeepSeek R1 es un modelo "Thinking" (similar a o1 de OpenAI).
*   **Chain of Thought (CoT):** El modelo "piensa" antes de responder.
*   **Visualización:** A diferencia de otros, DeepSeek a veces expone el proceso de pensamiento, lo cual es valioso para depurar la lógica del agente.

## 4. Context Caching

Para conversaciones largas o documentos grandes que se reutilizan (ej. un libro de reglas de 500 páginas), el Context Caching guarda los tokens procesados en memoria.
*   **Beneficio:** Reduce el costo de entrada hasta en un 90% y la latencia significativamente.

## Ejercicio Práctico

Revisa los scripts en `code/`:
1.  `deepseek_chat.py`: Conexión básica usando el SDK de OpenAI modificado.
2.  `reasoning_demo.py`: Ejemplo de cómo invocar al modelo R1.
