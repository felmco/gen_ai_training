"""
ChromaDB Demo
-------------
Uso de ChromaDB para almacenamiento vectorial persistente.
Using ChromaDB for persistent vector storage.

Requisitos/Requirements:
pip install chromadb
"""

import chromadb

def chroma_example():
    print("--- ChromaDB Vector Store ---")
    
    # Cliente efímero (en memoria) para pruebas
    # Ephemeral client (in-memory) for testing
    client = chromadb.Client()
    
    # Crear una colección (como una tabla SQL)
    # Create a collection (like a SQL table)
    collection = client.create_collection(name="my_knowledge_base")
    
    # Agregar documentos
    # Chroma usa un modelo de embedding por defecto (all-MiniLM-L6-v2) si no especificas uno
    print("Adding documents...")
    collection.add(
        documents=[
            "This is a document about engineering.",
            "This is a document about steak and wine."
        ],
        metadatas=[{"source": "doc1"}, {"source": "doc2"}],
        ids=["id1", "id2"]
    )
    
    # Query
    query_text = "I am hungry"
    print(f"\n🔎 Query: '{query_text}'")
    
    results = collection.query(
        query_texts=[query_text],
        n_results=1
    )
    
    print("\n--- Result ---")
    print(f"Document: {results['documents'][0][0]}")
    print(f"Distance: {results['distances'][0][0]}")

if __name__ == "__main__":
    try:
        chroma_example()
    except ImportError:
        print("❌ ChromaDB not installed. Run: pip install chromadb")
    except Exception as e:
        print(f"❌ Error: {e}")
