# Módulo 5.4: Protocolo Agent-to-Agent (A2A)

El futuro no es un solo agente gigante, sino una economía de agentes colaborando. A2A es el protocolo para que esto suceda.

## 1. El Internet de los Agentes

*   **MCP:** Conecta Agente <-> Herramienta.
*   **A2A:** Conecta Agente <-> Agente.

Imagina que tu Agente de Ventas (construido en LangGraph) necesita consultar el stock. En lugar de tener acceso directo a la base de datos, contacta al Agente de Inventario (construido en Google ADK) mediante A2A.

## 2. Agent Cards (Tarjetas de Agente)

Para que un agente "contrate" a otro, necesita saber qué hace. Las Agent Cards son como el perfil de LinkedIn del agente.

```json
{
  "name": "InventoryManager",
  "capabilities": ["check_stock", "reserve_item"],
  "pricing": "0.01 USD per call",
  "protocol": "A2A-v1"
}
```

## 3. Interoperabilidad

A2A permite romper los silos tecnológicos. Tu orquestador en n8n puede hablar con un agente en Python, que a su vez subcontrata una tarea a un agente en Java.
