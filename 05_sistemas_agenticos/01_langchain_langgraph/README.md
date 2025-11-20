# Módulo 5.1: LangChain y LangGraph (La Base del Grafo)

Las "Cadenas" (Chains) lineales no son suficientes para agentes autónomos que necesitan reintentar, corregirse o buclear. Necesitamos Grafos.

## 1. De Cadenas a Grafos

*   **DAG (Directed Acyclic Graph):** LangChain clásico. Flujo de A -> B -> C.
*   **Cyclic Graph:** LangGraph. Flujo de A -> B -> A (si hay error) -> C.

## 2. Conceptos Core de LangGraph

*   **State (Estado):** Un diccionario tipado que persiste a través de los pasos del grafo. Es la "memoria" compartida.
*   **Nodes (Nodos):** Funciones de Python que reciben el estado, hacen trabajo (llamar LLM, buscar en BD) y devuelven una actualización del estado.
*   **Edges (Aristas):** Conexiones entre nodos.
*   **Conditional Edges:** Lógica de decisión ("Si el LLM pide una herramienta, ve al nodo Tool; si responde, ve al nodo Final").

## Ejercicio Práctico

Revisa `code/simple_graph.py` para ver un grafo cíclico simple que simula un agente que se autocorrige.
