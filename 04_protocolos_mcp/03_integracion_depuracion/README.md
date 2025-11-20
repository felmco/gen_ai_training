# Módulo 4.3: Integración y Depuración

Una vez creado el servidor, hay que usarlo.

## 1. Conexión a Clientes

### Claude Desktop
Para usar tu servidor en Claude Desktop, edita el archivo de configuración (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "weather": {
      "command": "python",
      "args": ["/path/to/weather_server.py"]
    }
  }
}
```

### IDEs (Cursor/VS Code)
Muchos IDEs modernos están adoptando MCP para permitir que sus asistentes de IA accedan a herramientas locales.

## 2. Inspector MCP

Depurar agentes es difícil. El **MCP Inspector** es una herramienta web que te permite conectar tu servidor y probar las herramientas manualmente antes de conectarlas a un LLM real.

```bash
npx @modelcontextprotocol/inspector python weather_server.py
```

Esto abrirá una interfaz web donde puedes ver la lista de herramientas y ejecutarlas con un clic.
