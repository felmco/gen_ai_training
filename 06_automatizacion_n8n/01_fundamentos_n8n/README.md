# Módulo 6.1: Fundamentos de n8n para Desarrolladores

n8n no es solo una herramienta "No-Code" para marketing. Es un middleware visual potente para orquestar sistemas complejos de IA.

## 1. Flujos de Trabajo Híbridos

El patrón más potente es usar n8n para la "fontanería" (recibir emails, conectar a Slack, guardar en Google Sheets) y usar Python para la "inteligencia".

```mermaid
graph LR
    Email[Gmail] --> |Webhook| n8n[n8n Workflow]
    n8n --> |HTTP Request| Python[API Python (FastAPI/MCP)]
    Python --> |JSON Response| n8n
    n8n --> |Slack API| Slack[Notificación]
```

## 2. Webhooks

n8n expone URLs que pueden recibir datos JSON. Esto permite que tus scripts de Python "despierten" flujos de trabajo.

## Ejercicio Práctico

Revisa `code/webhook_trigger.py` para ver cómo disparar un flujo de n8n desde Python.
