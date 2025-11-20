"""
Asyncio for Concurrent LLM Calls
--------------------------------
Demostración de cómo usar asyncio para realizar múltiples "llamadas" simuladas
a un LLM en paralelo, reduciendo el tiempo total de ejecución.

Demonstration of how to use asyncio to perform multiple simulated LLM "calls"
in parallel, reducing total execution time.
"""

import asyncio
import time
import random

async def mock_llm_call(prompt_id: int, delay: float) -> str:
    """
    Simula una llamada a una API de LLM que tarda 'delay' segundos.
    Simulates an LLM API call that takes 'delay' seconds.
    """
    print(f"➡️  [Start] Request {prompt_id} (Delay: {delay}s)")
    await asyncio.sleep(delay) # Non-blocking sleep
    print(f"✅ [Finish] Request {prompt_id}")
    return f"Response for {prompt_id}"

async def main_sequential():
    print("\n--- Ejecución Secuencial / Sequential Execution ---")
    start_time = time.time()
    
    # Ejecutar uno tras otro / Run one after another
    await mock_llm_call(1, 1.0)
    await mock_llm_call(2, 1.0)
    await mock_llm_call(3, 1.0)
    
    total_time = time.time() - start_time
    print(f"⏱️  Total Sequential Time: {total_time:.2f}s")

async def main_parallel():
    print("\n--- Ejecución Paralela / Parallel Execution (Asyncio) ---")
    start_time = time.time()
    
    # Crear tareas para ejecutar concurrentemente / Create tasks to run concurrently
    tasks = [
        mock_llm_call(1, 1.0),
        mock_llm_call(2, 1.0),
        mock_llm_call(3, 1.0)
    ]
    
    # Esperar a que todas terminen / Wait for all to finish
    results = await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    print(f"⏱️  Total Parallel Time: {total_time:.2f}s")
    print(f"Results: {results}")

if __name__ == "__main__":
    # Asyncio entry point
    asyncio.run(main_sequential())
    asyncio.run(main_parallel())
