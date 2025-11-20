"""
Simple RAG Pipeline (In-Memory)
-------------------------------
Una implementación conceptual de RAG sin bases de datos complejas.
A conceptual implementation of RAG without complex databases.
"""

import numpy as np
from typing import List, Dict

# Simulación de función de embedding (normalmente usarías OpenAI o HuggingFace)
# Mock embedding function (normally you'd use OpenAI or HuggingFace)
def get_mock_embedding(text: str) -> np.ndarray:
    # Retorna un vector aleatorio determinista basado en la longitud del texto
    # Returns a deterministic random vector based on text length
    np.random.seed(len(text))
    return np.random.rand(128)

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

class SimpleVectorStore:
    def __init__(self):
        self.documents: List[Dict] = []
    
    def add_documents(self, texts: List[str]):
        for text in texts:
            vector = get_mock_embedding(text)
            self.documents.append({"text": text, "vector": vector})
            
    def search(self, query: str, k: int = 2) -> List[str]:
        query_vector = get_mock_embedding(query)
        
        # Calcular similitud con todos los documentos
        # Calculate similarity with all documents
        scores = []
        for doc in self.documents:
            score = cosine_similarity(query_vector, doc["vector"])
            scores.append((score, doc["text"]))
            
        # Ordenar por score descendente
        # Sort by descending score
        scores.sort(key=lambda x: x[0], reverse=True)
        
        return [item[1] for item in scores[:k]]

if __name__ == "__main__":
    # 1. Base de Conocimiento / Knowledge Base
    knowledge_base = [
        "Python is a programming language created by Guido van Rossum.",
        "The capital of France is Paris.",
        "Photosynthesis is how plants make food using sunlight.",
        "Java is a class-based, object-oriented programming language."
    ]
    
    # 2. Indexación / Indexing
    db = SimpleVectorStore()
    db.add_documents(knowledge_base)
    print("✅ Knowledge Base Indexed.")
    
    # 3. Búsqueda / Retrieval
    query = "Tell me about coding languages"
    print(f"\n🔎 Query: {query}")
    
    results = db.search(query)
    
    print("\n--- Retrieved Context ---")
    for i, res in enumerate(results):
        print(f"{i+1}. {res}")
