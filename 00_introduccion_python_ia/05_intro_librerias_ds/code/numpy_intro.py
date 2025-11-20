"""
NumPy & Matplotlib Intro
------------------------
Operaciones vectorizadas y visualización básica.
Vectorized operations and basic visualization.

Requisitos: pip install numpy matplotlib
"""

import time
import random

# Intentamos importar, si falla mostramos mensaje amigable
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    print("❌ Missing libraries. Run: pip install numpy matplotlib")
    exit()

def compare_speed():
    size = 1_000_000
    
    print(f"--- Speed Test (Summing {size} elements) ---")
    
    # Python Lists
    list_a = [random.random() for _ in range(size)]
    list_b = [random.random() for _ in range(size)]
    
    start = time.time()
    # Suma elemento a elemento manual
    list_c = [a + b for a, b in zip(list_a, list_b)]
    py_time = time.time() - start
    print(f"Python List time: {py_time:.4f}s")
    
    # NumPy Arrays
    arr_a = np.array(list_a)
    arr_b = np.array(list_b)
    
    start = time.time()
    # Suma vectorizada (C++ backend)
    arr_c = arr_a + arr_b
    np_time = time.time() - start
    print(f"NumPy Array time: {np_time:.4f}s")
    
    print(f"🚀 NumPy is {py_time / np_time:.1f}x faster!")

def plot_loss():
    print("\n--- Generating Plot ---")
    # Simular curva de aprendizaje
    epochs = np.arange(1, 21)
    loss = 1 / np.sqrt(epochs) + np.random.normal(0, 0.02, 20)
    
    plt.figure(figsize=(8, 4))
    plt.plot(epochs, loss, marker='o', linestyle='-', color='b', label='Training Loss')
    plt.title("Simulated Training Curve")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.legend()
    
    # Guardar en lugar de mostrar (para evitar bloqueo en algunos entornos)
    output_file = "training_plot.png"
    plt.savefig(output_file)
    print(f"✅ Plot saved to {output_file}")

if __name__ == "__main__":
    compare_speed()
    plot_loss()
