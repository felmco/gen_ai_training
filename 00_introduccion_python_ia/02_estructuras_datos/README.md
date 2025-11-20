# Módulo 0.2: Estructuras de Datos para IA

En Data Science, raramente manejamos variables sueltas. Manejamos colecciones masivas de datos.

## 1. Listas (Lists)

La estructura base para secuencias.
*   **Uso en IA:** Historial de mensajes en un chat, lista de documentos recuperados por RAG.
*   **Slicing:** `mensajes[-1]` (último mensaje), `tokens[:10]` (primeros 10 tokens).

## 2. Diccionarios (Dictionaries)

La estructura más importante para interactuar con APIs (JSON).
*   **Clave-Valor:** `{"role": "user", "content": "Hola"}`.
*   **Anidamiento:** Diccionarios dentro de listas dentro de diccionarios (común en respuestas de OpenAI).

## 3. Tuplas y Sets

*   **Tuplas:** Datos inmutables (ej. coordenadas `(x, y)` o dimensiones de una imagen `(1920, 1080)`).
*   **Sets:** Colecciones únicas. Útil para vocabularios (palabras únicas en un texto).

## Ejercicio Práctico

Revisa `code/data_structs_ai.py` para ver cómo manipular historiales de chat y configuraciones de modelos.
