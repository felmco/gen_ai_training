"""
Pandas for RAG Preparation
--------------------------
Uso de Pandas para preparar datos textuales antes de la vectorización.
Using Pandas to prepare textual data before vectorization.
"""

import pandas as pd
import io

# Simulación de un archivo CSV cargado / Simulated CSV file
csv_data = """id,title,content,category
1,Introduction to AI,AI is a branch of computer science...,Tech
2,Recipe for Cake,Mix flour and sugar...,Cooking
3,,Empty row should be removed,
4,Quantum Physics,Particles behave differently...,Science
"""

def prepare_dataset_for_rag():
    print("--- Carga de Datos / Data Loading ---")
    # Leer CSV desde string (simulando archivo)
    df = pd.read_csv(io.StringIO(csv_data))
    print(f"Original DataFrame shape: {df.shape}")
    print(df.head())
    
    print("\n--- Limpieza / Cleaning ---")
    # 1. Eliminar filas con datos faltantes en columnas críticas
    df_clean = df.dropna(subset=['title', 'content'])
    print(f"Shape after dropna: {df_clean.shape}")
    
    print("\n--- Transformación / Transformation ---")
    # 2. Crear un campo 'text_chunk' que combine título y contenido
    # Esto es lo que realmente se vectorizará
    df_clean['text_chunk'] = "Title: " + df_clean['title'] + "\nContent: " + df_clean['content']
    
    # Mostrar un ejemplo de chunk
    print("Example Chunk:")
    print("-" * 20)
    print(df_clean.iloc[0]['text_chunk'])
    print("-" * 20)
    
    # 3. Filtrar por categoría si fuera necesario
    tech_docs = df_clean[df_clean['category'] == 'Tech']
    print(f"\nTech docs count: {len(tech_docs)}")

if __name__ == "__main__":
    prepare_dataset_for_rag()
