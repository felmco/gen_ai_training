"""
Simple LangGraph Simulation
---------------------------
Simulación conceptual de un grafo cíclico sin dependencias pesadas.
Conceptual simulation of a cyclic graph without heavy dependencies.
"""

import random
from typing import TypedDict, Literal

# 1. Definir el Estado / Define State
class AgentState(TypedDict):
    messages: list[str]
    quality_score: float
    iterations: int

# 2. Definir Nodos / Define Nodes

def generator_node(state: AgentState) -> AgentState:
    print("   [Generator] Drafting content...")
    # Simular generación
    new_msg = "Draft content v" + str(state['iterations'])
    return {
        "messages": state['messages'] + [new_msg],
        "quality_score": random.random(), # Random quality
        "iterations": state['iterations'] + 1
    }

def critic_node(state: AgentState) -> AgentState:
    print(f"   [Critic] Reviewing quality: {state['quality_score']:.2f}")
    # El critico no cambia el mensaje, solo evalua (ya simulado en generator para simplificar)
    return state

# 3. Definir Lógica Condicional / Define Conditional Logic

def should_continue(state: AgentState) -> Literal["generator", "end"]:
    if state['quality_score'] > 0.8:
        print("   --> Quality PASS. Finishing.")
        return "end"
    
    if state['iterations'] >= 3:
        print("   --> Max iterations reached. Finishing anyway.")
        return "end"
    
    print("   --> Quality FAIL. Back to Generator.")
    return "generator"

# 4. Simular Ejecución del Grafo / Simulate Graph Execution
def run_graph():
    print("--- Starting Agent Loop ---")
    
    # Estado Inicial
    state = {"messages": [], "quality_score": 0.0, "iterations": 0}
    
    current_node = "generator"
    
    while current_node != "end":
        if current_node == "generator":
            state = generator_node(state)
            state = critic_node(state) # In this simple loop, critic follows generator
            
            # Decidir siguiente paso
            next_step = should_continue(state)
            current_node = next_step

    print("\n--- Final Result ---")
    print(f"Final Content: {state['messages'][-1]}")
    print(f"Iterations: {state['iterations']}")

if __name__ == "__main__":
    run_graph()
