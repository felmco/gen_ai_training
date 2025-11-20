# Módulo 6.3: El "Pegamento" del Sistema

La arquitectura final de un sistema de IA empresarial combina lo mejor de ambos mundos: la flexibilidad visual de n8n y la potencia de código de Python.

## Arquitectura de Referencia

1.  **Trigger (Disparador):** Un evento de negocio (nuevo lead en CRM, email de cliente).
2.  **Router (n8n):** Decide qué hacer. ¿Es spam? ¿Es urgente?
3.  **Hero Agent (Python):** Si es complejo, n8n llama a un contenedor Docker corriendo un Agente LangGraph o ADK.
    *   El agente tiene memoria, herramientas y acceso a BD.
    *   El agente piensa y genera una respuesta estructurada.
4.  **Delivery (n8n):** n8n toma la respuesta y la formatea (PDF, HTML) y la entrega por el canal adecuado (WhatsApp, Email).

Esta separación de responsabilidades hace que el sistema sea mantenible. Los desarrolladores tocan Python; los analistas de negocio tocan n8n.
