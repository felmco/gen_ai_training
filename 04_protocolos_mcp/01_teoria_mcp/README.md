# Módulo 4.1: Teoría de MCP (Model Context Protocol)

Hasta ahora, cada integración de IA era un "silo". MCP es el estándar abierto que actúa como un "puerto USB" para aplicaciones de IA.

## 1. Arquitectura Cliente-Host-Servidor

MCP desacopla la IA de los datos.

```mermaid
graph LR
    Host[Host (Claude Desktop / IDE)] <--> |Protocolo MCP| Server[Servidor MCP]
    Server <--> |Acceso Nativo| Data[(Base de Datos / API)]
    
    Host --> LLM[Modelo de IA]
```

*   **Host:** La aplicación donde vive el usuario (ej. Claude Desktop, Cursor).
*   **Servidor:** Un proceso ligero que expone capacidades.
*   **Cliente:** El conector dentro del Host.

## 2. Primitivas de MCP

MCP define tres tipos de capacidades principales:

1.  **Resources (Recursos):** Datos pasivos que el LLM puede leer (como archivos o logs). Son como `GET` requests.
2.  **Tools (Herramientas):** Funciones ejecutables que pueden modificar el estado o realizar cálculos (como `POST` requests).
3.  **Prompts:** Plantillas predefinidas para tareas comunes.

## ¿Por qué es revolucionario?
Antes, si querías conectar Claude a tu base de datos Postgres, tenías que esperar a que Anthropic construyera esa integración. Ahora, tú construyes un **Servidor MCP** para Postgres una vez, y funciona con Claude, con IDEs, y con cualquier futuro cliente MCP.
