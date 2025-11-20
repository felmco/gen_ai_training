# Módulo 1.3: Bibliotecas Esenciales para IA Generativa

Más allá de NumPy, la ingeniería de IA moderna requiere un set específico de herramientas para manejar datos no estructurados, validar salidas probabilísticas y gestionar latencia.

## 1. Pandas para RAG (Retrieval Augmented Generation)

En IA, no usamos Pandas para series temporales financieras, sino como el "Excel programable" para preparar nuestra Base de Conocimiento.

*   **Carga de Datos:** Leer CSVs, Parquets o JSONs masivos.
*   **Limpieza:** Eliminar filas vacías, concatenar columnas de texto (Título + Cuerpo).
*   **Chunking:** Preparar el texto para ser vectorizado.

## 2. Pydantic: Validación de Datos

Los LLMs son probabilísticos; el software es determinista. Pydantic es el puente.
Usamos Pydantic para definir la "forma" exacta que debe tener la respuesta del LLM (Structured Outputs).

```python
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    interests: list[str]
```

## 3. Asyncio: Concurrencia

Las llamadas a LLMs son lentas (segundos). Si tienes que procesar 100 documentos y lo haces secuencialmente, tardarás minutos. Con `asyncio`, puedes lanzar las 100 llamadas a la vez y esperar a que terminen, reduciendo el tiempo total drásticamente.

## 4. Tenacity: Resiliencia

Las APIs fallan (Rate Limits, Server Errors). `tenacity` nos permite reintentar automáticamente con una estrategia inteligente (Exponential Backoff) para no saturar el servidor y asegurar que nuestra aplicación sea robusta.

## Ejercicio Práctico

Revisa los scripts en `code/`:
1.  `pandas_rag_prep.py`: Preparación de un dataset para RAG.
2.  `pydantic_validation.py`: Validación de salidas de LLM.
3.  `async_llm.py`: Ejecución paralela de llamadas simuladas.
4.  `tenacity_retries.py`: Manejo robusto de errores de API.
