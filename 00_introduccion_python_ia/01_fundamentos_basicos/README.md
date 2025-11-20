# Módulo 0.1: Fundamentos Básicos con Enfoque en IA

Bienvenido a la Fase 0. Aquí no aprenderemos Python con ejemplos de "fruterías", sino con conceptos que usarás en Inteligencia Artificial.

## 1. Variables y Tipos de Datos

En IA, las variables representan **hiperparámetros** y **datos**.

*   `int`: Número de épocas, semillas aleatorias.
*   `float`: Tasa de aprendizaje (learning rate), probabilidades.
*   `str`: Prompts, tokens.
*   `bool`: Flags de configuración (`use_gpu = True`).

## 2. Control de Flujo (Condicionales)

Los modelos toman decisiones basadas en umbrales (thresholds).

```python
confidence_score = 0.85
threshold = 0.7

if confidence_score > threshold:
    print("✅ Aceptar predicción")
else:
    print("❌ Rechazar predicción (Human Loop)")
```

## 3. Bucles (Loops)

El entrenamiento de una IA es esencialmente un bucle gigante.

*   **For Loops:** Iterar sobre épocas de entrenamiento o lotes de datos (batches).
*   **While Loops:** Agentes que corren hasta cumplir una condición de parada.

## Ejercicio Práctico

Revisa `code/training_loop_sim.py` para ver una simulación de un bucle de entrenamiento usando conceptos básicos.
