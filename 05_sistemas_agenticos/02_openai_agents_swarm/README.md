# Módulo 5.2: OpenAI Agents SDK & Swarm

OpenAI propone un enfoque más ligero y "Pythonic" para la orquestación de agentes.

## 1. Swarm: Enjambres de Agentes

La idea central de Swarm no es tener un agente superpoderoso, sino muchos agentes pequeños y especializados que se pasan la pelota ("Handoff").

*   **Agent:** Un objeto que encapsula instrucciones y herramientas.
*   **Handoff:** Una herramienta puede devolver *otro Agente* como respuesta. Esto transfiere la ejecución inmediatamente a ese nuevo agente.

### Ejemplo: Call Center
1.  **Triage Agent:** Recibe la llamada. Si es sobre facturación, devuelve `BillingAgent`.
2.  **Billing Agent:** Tiene herramientas de SQL. Si el usuario pide cancelar, devuelve `RetentionAgent`.
3.  **Retention Agent:** Tiene instrucciones de ofrecer descuentos.

## Ejercicio Práctico

Revisa `code/swarm_demo.py` para ver cómo implementar este patrón de traspaso de tareas.
