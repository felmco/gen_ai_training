"""
RAG Evaluation Demo using Ragas
-------------------------------
Demonostración de cómo evaluar pipelines de RAG usando métricas de Ragas.
Demonstrates how to evaluate RAG pipelines using Ragas metrics.

Requisitos/Requirements:
pip install ragas datasets
"""

import os
import pandas as pd
from datasets import Dataset
try:
    from ragas import evaluate
    from ragas.metrics import (
        faithfulness,
        answer_relevancy,
        context_precision,
        context_recall,
    )
except ImportError:
    print("Ragas not installed. Please run: pip install ragas datasets")
    exit()

# Datos de Ejemplo / Dummy Data
# En un caso real, esto vendría de tu pipeline de RAG (logs de producción o set de test).
# In a real case, this would come from your RAG pipeline (production logs or test set).
data = {
    'question': [
        'What is the capital of France?',
        'How does a transformer work?',
        'Who wrote "1984"?'
    ],
    'answer': [
        'Paris is the capital of France.',
        'Transformers use self-attention mechanisms to process input sequences in parallel, unlike RNNs.',
        'George Orwell wrote "1984".'
    ],
    'contexts': [
        ['Paris is the capital and most populous city of France. Validated by geography experts.'],
        ['The Transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data.'],
        ['Nineteen Eighty-Four is a dystopian social science fiction novel by English novelist George Orwell.']
    ],
    'ground_truth': [
        'Paris',
        'It relies on self-attention mechanisms to handle sequential data.',
        'George Orwell'
    ]
}

def run_evaluation():
    print("--- Starting RAG Evaluation ---")
    
    # Ragas usa OpenAI por defecto para evaluar (LLM-as-a-Judge)
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY missing. Ragas needs an LLM judge to run.")
        print("   Skipping actual execution to avoid errors in this demo.")
        print("   Set it with: export OPENAI_API_KEY='sk-...'")
        return

    # 1. Convertir a formato Dataset de HuggingFace
    dataset = Dataset.from_dict(data)
    
    print("Evaluating dataset with metrics: Faithfulness, Answer Relevancy, Precision, Recall...")
    
    # 2. Correr Evaluación
    # raise_exceptions=False ayuda a continuar si una métrica falla puntualmente
    results = evaluate(
        dataset=dataset,
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall
        ],
        raise_exceptions=False
    )
    
    print("\n--- Evaluation Results ---")
    print(results)
    
    # 3. Exportar resultados
    df = results.to_pandas()
    print("\nTop rows:")
    print(df[['question', 'faithfulness', 'answer_relevancy']].head())
    
    # Opcional: Guardar a CSV
    # df.to_csv("rag_evaluation_results.csv", index=False)

if __name__ == "__main__":
    run_evaluation()
