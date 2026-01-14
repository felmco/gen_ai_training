"""
Simple LangGraph Implementation
-------------------------------
Implementación real usando la librería `langgraph`.
Real implementation using the `langgraph` library.

Requisitos/Requirements:
pip install langgraph langchain
"""

import random
from typing import TypedDict, Literal, Annotated
import operator
from langgraph.graph import StateGraph, END, START

# 1. Definir el Estado / Define State
# Usamos operator.add para que los mensajes se acumulen (append) en lugar de sobrescribirse
class AgentState(TypedDict):
    messages: Annotated[list[str], operator.add]
    quality_score: float
    iterations: int

# 2. Definir Nodos / Define Nodes

def generator_node(state: AgentState):
    print(f"   [Generator] Drafting content (Iter: {state['iterations'] + 1})...")
    # Generar contenido simulado
    new_msg = f"Draft content v{state['iterations'] + 1}"
    
    # Retornamos solo lo que queremos actualizar
    return {
        "messages": [new_msg], # Se agregará a la lista gracias a Annotated
        "quality_score": random.random(), # 0.0 a 1.0
        "iterations": state['iterations'] + 1
    }

def critic_node(state: AgentState):
    score = state['quality_score']
    print(f"   [Critic] Reviewing quality: {score:.2f}")
    # El crítico no modifica el estado en este ejemplo simple, solo lee
    return {}

# 3. Definir Lógica Condicional / Define Conditional Logic

def should_continue(state: AgentState) -> Literal["generator", "end"]:
    if state['quality_score'] > 0.8:
        print("   --> Quality PASS. Finishing.")
        return "end"
    
    if state['iterations'] >= 3:
        print("   --> Max iterations reached. Finishing anyway.")
        return "end"
    
    print("   --> Quality FAIL (Score too low). Back to Generator.")
    return "generator"

# 4. Construir el Grafo / Build the Graph

builder = StateGraph(AgentState)

# Agregar nodos
builder.add_node("generator", generator_node)
builder.add_node("critic", critic_node)

# Definir flujo
builder.add_edge(START, "generator")
builder.add_edge("generator", "critic")

# Arista condicional desde el crítico
builder.add_conditional_edges(
    "critic",
    should_continue,
    {
        "generator": "generator",
        "end": END
    }
)

# Compilar
graph = builder.compile()

def run_demo():
    print("--- Starting Real LangGraph Execution ---")
    
    # Estado inicial
    initial_state = {
        "messages": [],
        "quality_score": 0.0,
        "iterations": 0
    }
    
    # Ejecutar
    # stream_mode="values" nos da el estado actualizado tras cada paso
    try:
        final_state = graph.invoke(initial_state)
        
        print("\n--- Final Result ---")
        print(f"Final Content: {final_state['messages'][-1]}")
        print(f"Total Iterations: {final_state['iterations']}")
        print(f"Final Score: {final_state['quality_score']:.2f}")
        
    except Exception as e:
        print(f"Error running graph: {e}")

if __name__ == "__main__":
    run_demo()
