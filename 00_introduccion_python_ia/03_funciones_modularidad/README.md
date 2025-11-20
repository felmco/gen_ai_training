# Módulo 0.3: Funciones y Modularidad

El código "spaghetti" (todo en un archivo sin orden) es el enemigo de la IA escalable. Las funciones nos permiten encapsular lógica.

## 1. Funciones Matemáticas (Simuladas)

En Deep Learning, todo son funciones.
*   $y = f(x)$
*   **Loss Function:** Calcula qué tan mal lo hizo el modelo.
*   **Activation Function:** Decide si una neurona se "enciende" (ReLU, Sigmoid).

## 2. Type Hinting (Tipado)

Python es dinámico, pero en IA profesional (y con Google ADK) usamos **Type Hints** para saber qué entra y qué sale.

```python
def calcular_costo(tokens: int, precio_por_k: float) -> float:
    return (tokens / 1000) * precio_por_k
```

## 3. Modularidad

Dividir el código en archivos (`utils.py`, `models.py`) permite reutilizar componentes y facilita la colaboración.

## Ejercicio Práctico

Revisa `code/activation_funcs.py` para ver implementaciones de funciones de activación comunes.
