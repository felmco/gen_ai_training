"""
Activation Functions & Type Hinting
-----------------------------------
Implementación de funciones matemáticas comunes en redes neuronales.
Implementation of common neural network mathematical functions.
"""

import math

# Type Hinting: indicamos que 'x' es float y retorna float
def sigmoid(x: float) -> float:
    """
    Función de activación Sigmoid.
    Transforma cualquier valor a un rango entre 0 y 1 (probabilidad).
    """
    return 1 / (1 + math.exp(-x))

def relu(x: float) -> float:
    """
    Rectified Linear Unit (ReLU).
    Si x > 0, devuelve x. Si no, 0.
    La función más usada en Deep Learning moderno.
    """
    return max(0.0, x)

def soft_max_simulated(logits: list[float]) -> list[float]:
    """
    Simulación simplificada de Softmax.
    Convierte una lista de números (logits) en probabilidades que suman 1.
    """
    exp_values = [math.exp(l) for l in logits]
    total_sum = sum(exp_values)
    return [v / total_sum for v in exp_values]

if __name__ == "__main__":
    print("--- Sigmoid ---")
    print(f"sigmoid(0) = {sigmoid(0):.4f} (Debería ser 0.5)")
    print(f"sigmoid(10) = {sigmoid(10):.4f} (Casi 1.0)")
    
    print("\n--- ReLU ---")
    print(f"relu(-5) = {relu(-5)}")
    print(f"relu(5) = {relu(5)}")
    
    print("\n--- Softmax (Simulado) ---")
    logits = [2.0, 1.0, 0.1]
    probs = soft_max_simulated(logits)
    print(f"Logits: {logits}")
    print(f"Probs: {[f'{p:.4f}' for p in probs]}")
    print(f"Suma: {sum(probs):.4f}")
