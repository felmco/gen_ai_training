"""
Capstone Project: Corporate Autonomous Agent
--------------------------------------------
Esqueleto del agente final. Tu misión es implementar las herramientas y el grafo.
Skeleton of the final agent. Your mission is to implement the tools and the graph.
"""

from typing import TypedDict, List

# 1. Estado del Agente / Agent State
class AgentState(TypedDict):
    query: str
    internal_data: str
    external_data: str
    final_report: str
    steps: List[str]

# 2. Herramientas Simuladas / Mock Tools

def search_internal_policy(query: str) -> str:
    """
    TODO: Implementar RAG real aquí usando ChromaDB.
    """
    print(f"🔎 Searching internal DB for: {query}")
    return "Policy 101: Invest in AI companies with >20% growth."

def search_web(query: str) -> str:
    """
    TODO: Implementar búsqueda real (Tavily, Serper).
    """
    print(f"🌐 Searching web for: {query}")
    return "Market News: AI stocks are up 5% today."

# 3. Nodos del Grafo / Graph Nodes

def research_node(state: AgentState) -> AgentState:
    print("--- [Research Node] Gathering Info ---")
    internal = search_internal_policy(state['query'])
    external = search_web(state['query'])
    
    return {
        "internal_data": internal,
        "external_data": external,
        "steps": state['steps'] + ["research_complete"]
    }

def writing_node(state: AgentState) -> AgentState:
    print("--- [Writing Node] Synthesizing Report ---")
    # TODO: Llamar a un LLM real aquí para escribir el reporte
    report = f"""
    # Market Report
    Based on internal policy '{state['internal_data']}' and external news '{state['external_data']}',
    the recommendation is to BUY.
    """
    return {
        "final_report": report,
        "steps": state['steps'] + ["writing_complete"]
    }

# 4. Ejecución / Execution
def run_agent(query: str):
    # En un sistema real, usaríamos LangGraph para compilar esto
    # In a real system, we would use LangGraph to compile this
    
    initial_state = {
        "query": query,
        "internal_data": "",
        "external_data": "",
        "final_report": "",
        "steps": []
    }
    
    # Simulación de flujo lineal
    state_after_research = research_node(initial_state)
    final_state = writing_node(state_after_research)
    
    print("\n✅ Final Output:")
    print(final_state['final_report'])

if __name__ == "__main__":
    run_agent("Should we invest in NVIDIA?")
