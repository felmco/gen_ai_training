# Módulo 3.2: Embeddings y Bases Vectoriales

Los Embeddings son la magia que permite a las máquinas entender el significado. Transforman texto en vectores numéricos donde conceptos similares están cerca geométricamente.

## 1. Espacio Latente

Imagina un gráfico 3D.
*   "Rey" y "Reina" están cerca.
*   "Manzana" está lejos de "Rey".
*   "Rey" - "Hombre" + "Mujer" ≈ "Reina".

Esta distancia se mide comúnmente con la **Similitud Coseno**.

## 2. Bases de Datos Vectoriales (Vector DBs)

Las bases de datos SQL tradicionales no sirven para buscar "vectores cercanos". Necesitamos índices especializados (HNSW).

### Opciones Populares
*   **ChromaDB:** Open source, corre en local (en memoria o disco). Ideal para desarrollo.
*   **Pinecone:** Gestionado (SaaS). Escalable a millones de vectores.
*   **Weaviate:** Híbrido y potente.

## Ejercicio Práctico

Revisa `code/chroma_demo.py` para ver cómo usar ChromaDB para almacenar y recuperar información persistentemente.
