# Módulo 3.3: Técnicas de RAG Avanzado

El RAG básico (Naive RAG) falla a menudo. Recupera documentos irrelevantes o pierde detalles técnicos. Aquí solucionamos eso.

## 1. Búsqueda Híbrida (Hybrid Search)

La búsqueda vectorial es excelente para conceptos ("coche" ≈ "automóvil"), pero mala para palabras clave exactas ("Error 504").
La búsqueda híbrida combina:
*   **Vector Search (Denso):** Entendimiento semántico.
*   **Keyword Search (BM25 - Disperso):** Coincidencia exacta de términos.

Se combinan los resultados usando un algoritmo como **Reciprocal Rank Fusion (RRF)**.

## 2. Re-Ranking

A veces, el vector DB recupera 50 documentos "posiblemente" relevantes. Pasarlos todos al LLM es costoso y confuso.
Un modelo **Reranker** (Cross-Encoder) lee la pregunta y cada documento y asigna un puntaje de relevancia preciso.

*   **Pipeline:** Retrieval (50 docs) -> Reranker (Top 5) -> LLM.
*   **Herramientas:** Cohere Rerank, BGE-Reranker.

## 3. Evaluación (RAGAS)

¿Cómo sabes si tu RAG funciona? No puedes mirar cada respuesta.
**RAGAS** (RAG Assessment) usa un LLM para evaluar a otro LLM en métricas como:
*   **Faithfulness:** ¿La respuesta se basa en el contexto o alucina?
*   **Answer Relevance:** ¿Responde a la pregunta del usuario?

## Ejercicio Práctico

Revisa `code/reranking_demo.py` para entender conceptualmente cómo el re-ranking mejora la precisión.
