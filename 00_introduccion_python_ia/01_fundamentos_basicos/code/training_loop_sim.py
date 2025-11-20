"""
Training Loop Simulation
------------------------
Simulación de un bucle de entrenamiento básico para entender variables y control de flujo.
Simulation of a basic training loop to understand variables and flow control.
"""

import time
import random

def simulate_training():
    # Hiperparámetros (Variables)
    epochs = 5              # Número de veces que pasamos por los datos
    learning_rate = 0.01    # Velocidad de aprendizaje
    target_accuracy = 0.90  # Meta a alcanzar
    
    current_accuracy = 0.50 # Precisión inicial (azar)
    
    print(f"🚀 Iniciando entrenamiento. Meta: {target_accuracy*100}%")
    
    # Bucle de entrenamiento (For Loop)
    for epoch in range(1, epochs + 1):
        print(f"\n--- Epoch {epoch}/{epochs} ---")
        
        # Simular mejora (o empeoramiento) aleatorio
        change = random.uniform(-0.02, 0.15)
        current_accuracy += change
        
        # Asegurar que no pase de 1.0 o baje de 0.0
        current_accuracy = max(0.0, min(1.0, current_accuracy))
        
        print(f"   Loss: {1 - current_accuracy:.4f}")
        print(f"   Accuracy: {current_accuracy:.4f}")
        
        # Condicional (Early Stopping)
        if current_accuracy >= target_accuracy:
            print("\n✅ Meta alcanzada. Deteniendo entrenamiento prematuramente (Early Stopping).")
            break
            
        time.sleep(0.5) # Simular tiempo de cómputo

    if current_accuracy < target_accuracy:
        print("\n⚠️  Entrenamiento finalizado sin alcanzar la meta.")

if __name__ == "__main__":
    simulate_training()
