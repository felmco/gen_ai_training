# Módulo 2.4: Ingeniería de Prompts Avanzada
# Module 2.4: Advanced Prompt Engineering

La calidad de las respuestas de un LLM depende directamente de la calidad de las instrucciones (prompts). Este módulo cubre técnicas avanzadas para movernos más allá del simple "pregunta y respuesta".
The quality of LLM responses depends directly on the quality of the instructions (prompts). This module covers advanced techniques to move beyond simple "Q&A".

## Conceptos Clave / Key Concepts

### 1. Zero-Shot vs Few-Shot Prompting
*   **Zero-Shot:** Pedir al modelo que haga algo sin ejemplos, confiando en su entrenamiento general.
*   **Few-Shot:** Proveer ejemplos explícitos (input -> output) dentro del contexto para guiar el formato y el estilo de la respuesta. Esta es una de las técnicas más efectivas para mejorar la fiabilidad.

### 2. Chain of Thought (CoT)
Pedir al modelo que "piense paso a paso" antes de dar la respuesta final. Esto mejora drásticamente el rendimiento en tareas de razonamiento, matemáticas y lógica.
Asking the model to "think step by step" before giving the final answer. This drastically improves performance on reasoning, math, and logic tasks.

### 3. Prompt Chaining vs System Prompts
*   **System Prompts:** Definir la "persona" y restricciones globales.
*   **Chaining:** Dividir una tarea compleja en varios prompts secuenciales (ej. primero resume, luego traduce el resumen).

### 4. DSPy (Declarative Self-improving Language Programs)
Una mención al futuro: DSPy busca optimizar prompts automáticamente tratando a los LLMs como módulos programables, en lugar de escribir strings a mano.

## Código Ejecutable

Revisa `code/advanced_prompts.py` para ver estas técnicas en acción usando la API de OpenAI.
