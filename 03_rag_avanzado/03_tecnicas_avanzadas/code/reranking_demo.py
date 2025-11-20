"""
Reranking Concept Demo
----------------------
Simulación de cómo un Reranker reordena resultados para mejorar la relevancia.
Simulation of how a Reranker reorders results to improve relevance.
"""

def mock_reranker(query: str, documents: list[str]) -> list[tuple[str, float]]:
    """
    Simula un modelo Cross-Encoder que asigna un score a cada par (query, doc).
    Simulates a Cross-Encoder model that assigns a score to each (query, doc) pair.
    """
    print(f"🤖 Reranking {len(documents)} documents for query: '{query}'")
    
    scored_docs = []
    for doc in documents:
        # Lógica simulada: Si el documento contiene palabras clave de la query, sube el score.
        # Simulated logic: If doc contains keywords from query, boost score.
        score = 0.1 # Base score
        
        # Simple keyword matching for demo purposes
        query_words = query.lower().split()
        for word in query_words:
            if word in doc.lower():
                score += 0.3
                
        scored_docs.append((doc, score))
    
    # Ordenar por score descendente
    scored_docs.sort(key=lambda x: x[1], reverse=True)
    return scored_docs

if __name__ == "__main__":
    query = "apple pie recipe"
    
    # Resultados iniciales de una búsqueda vectorial (pueden ser ruidosos)
    # Initial vector search results (can be noisy)
    retrieved_docs = [
        "Apple Inc. reported record profits.", # Semánticamente cerca a 'apple' pero irrelevante
        "The history of pies in England.",     # Cerca a 'pie'
        "Best Apple Pie Recipe: Flour, apples, sugar...", # El que queremos
        "Apple orchard maintenance guide."
    ]
    
    print("--- Before Reranking (Random Order from Vector DB) ---")
    for doc in retrieved_docs:
        print(f"- {doc}")
        
    reranked = mock_reranker(query, retrieved_docs)
    
    print("\n--- After Reranking (Top 2) ---")
    for doc, score in reranked[:2]:
        print(f"[{score:.2f}] {doc}")
