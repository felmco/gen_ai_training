# Módulo 1.2: Sintaxis Core con Enfoque en Datos No Estructurados

En la ingeniería de IA Generativa, el 80% del trabajo es manipular texto y estructuras de datos antes de enviarlos al modelo o después de recibir la respuesta. Este módulo se enfoca en las habilidades críticas de Python para estas tareas.

## 1. Manipulación de Texto Avanzada

Los LLMs (Large Language Models) "comen" texto. La capacidad de limpiar, formatear y estructurar strings es fundamental.

### f-strings para Prompts
Las `f-strings` son la forma más eficiente y legible de construir prompts dinámicos.

```python
user_input = "Explícame la computación cuántica"
system_role = "físico experto"

# Construcción limpia del prompt
prompt = f"""
Actúa como un {system_role}.
Responde a la siguiente pregunta de manera concisa:
"{user_input}"
"""
```

### Regex (Expresiones Regulares)
A menudo, los modelos devuelven texto con "ruido" (markdown extra, espacios, prefijos). Regex es tu bisturí para limpiar estas salidas.

## 2. Diccionarios y JSON

JSON (JavaScript Object Notation) es el lenguaje universal de las APIs de IA (OpenAI, Anthropic, Google).

*   **Python Dict** $\leftrightarrow$ **JSON String**
*   Las APIs reciben JSON y devuelven JSON.
*   Entender cómo navegar estructuras anidadas es vital.

## Ejercicio Práctico

Revisa los scripts en `code/`:
1.  `text_processing.py`: Técnicas de limpieza de texto y construcción de prompts.
2.  `json_handling.py`: Manipulación robusta de JSON y manejo de errores comunes.
