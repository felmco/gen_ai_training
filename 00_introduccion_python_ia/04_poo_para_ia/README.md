# Módulo 0.4: Programación Orientada a Objetos (POO) para IA

En librerías como PyTorch, TensorFlow o LangChain, **todo es una Clase**.

## 1. Clases y Objetos

*   **Clase (Plano):** `LLM`, `Agent`, `Tool`. Define qué propiedades y métodos tendrá.
*   **Objeto (Instancia):** `gpt_4o`, `sales_agent`. Una versión concreta de la clase.

## 2. Herencia

La herencia es clave. Por ejemplo, creamos una clase base `BaseModel` y luego `OpenAIModel` y `LlamaModel` heredan de ella. Esto permite cambiar de modelo sin cambiar el resto del código (Polimorfismo).

```python
class BaseModel:
    def generate(self, prompt):
        pass

class OpenAIModel(BaseModel):
    def generate(self, prompt):
        # Código específico de OpenAI
        return "GPT response"
```

## Ejercicio Práctico

Revisa `code/agent_class.py` para construir una estructura de Agente simple usando clases.
