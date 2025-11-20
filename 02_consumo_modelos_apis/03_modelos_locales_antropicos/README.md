# Módulo 2.3: Modelos Locales y Antrópicos

No todo es OpenAI. A veces necesitamos privacidad total (Local) o ventanas de contexto masivas (Anthropic).

## 1. Ollama: IA en tu Laptop

Ollama simplifica drásticamente la ejecución de modelos como Llama 3, Mistral o Gemma en local.
*   **Privacidad:** Los datos nunca salen de tu máquina.
*   **Costo:** Cero (solo electricidad).
*   **Latencia:** Depende de tu GPU/CPU.

```bash
# Instalación y ejecución
ollama run llama3
```

## 2. Anthropic (Claude)

Claude 3.5 Sonnet es considerado por muchos el mejor modelo para codificación y razonamiento complejo.
*   **Ventana de Contexto:** 200k tokens (ideal para analizar libros enteros o repositorios de código).
*   **Artifacts:** Capacidad de generar interfaces visuales (aunque esto es de su UI, la API es igual de potente).

## Ejercicio Práctico

Revisa los scripts en `code/`:
1.  `ollama_local.py`: Cómo conectar Python a tu servidor local de Ollama.
2.  `anthropic_claude.py`: Uso del SDK oficial de Anthropic.
