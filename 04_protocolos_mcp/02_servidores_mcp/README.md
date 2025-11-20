# Módulo 4.2: Construcción de Servidores MCP

Crear un servidor MCP es sorprendentemente sencillo gracias al SDK de Python.

## 1. FastMCP

La forma más rápida de empezar es con `fastmcp`. Es un decorador similar a FastAPI.

```python
from fastmcp import FastMCP

mcp = FastMCP("Mi Servidor")

@mcp.tool()
def sumar(a: int, b: int) -> int:
    return a + b
```

## 2. Exposición de Datos

Podemos exponer:
*   **Sistemas de Archivos:** Permitir al LLM leer logs en tiempo real.
*   **Bases de Datos:** Permitir consultas SQL seguras (read-only).
*   **APIs Internas:** Conectar herramientas legacy.

## Ejercicio Práctico

Revisa `code/weather_server.py` para ver un servidor MCP completo que expone una herramienta de clima.
