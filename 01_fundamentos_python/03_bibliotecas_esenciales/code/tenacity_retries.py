"""
Tenacity for API Retries
------------------------
Uso de la librería 'tenacity' para manejar fallos transitorios en APIs
de forma robusta.

Using the 'tenacity' library to robustly handle transient API failures.
"""

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import random
import time

# Definir una excepción personalizada para simular errores de API
class APIError(Exception):
    pass

# Decorador de Tenacity / Tenacity Decorator
# - stop_after_attempt(3): Reintentar máximo 3 veces.
# - wait_exponential(...): Esperar 1s, luego 2s, luego 4s... (backoff).
# - retry_if_exception_type(...): Solo reintentar si es APIError.
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type(APIError)
)
def call_unstable_api():
    """
    Simula una API inestable que falla el 70% de las veces.
    Simulates an unstable API that fails 70% of the time.
    """
    print("📞 Calling API...")
    if random.random() < 0.7:
        print("❌ API Failed! (Simulated 500 Error)")
        raise APIError("Server Busy")
    
    print("✅ API Success!")
    return "Data received"

if __name__ == "__main__":
    try:
        print("--- Iniciando llamadas con reintentos / Starting calls with retries ---")
        result = call_unstable_api()
        print(f"Final Result: {result}")
    except Exception as e:
        print(f"💀 Failed after retries: {e}")
