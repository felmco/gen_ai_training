"""
FastMCP Weather Server
----------------------
Un servidor MCP simple que expone una herramienta para consultar el clima.
A simple MCP server exposing a weather lookup tool.

Requisitos/Requirements:
pip install "mcp[cli]"
"""

from mcp.server.fastmcp import FastMCP

# Inicializar el servidor / Initialize server
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(city: str) -> str:
    """
    Get the current weather for a specific city.
    Args:
        city: The name of the city (e.g., 'Madrid', 'New York')
    """
    # En un caso real, llamaríamos a una API externa (OpenWeatherMap, etc.)
    # In a real case, we would call an external API
    
    city_lower = city.lower()
    if "madrid" in city_lower:
        return "Sunny, 25°C"
    elif "london" in city_lower:
        return "Rainy, 15°C"
    elif "new york" in city_lower:
        return "Cloudy, 20°C"
    else:
        return "Weather data not available for this city."

@mcp.resource("weather://alerts")
def get_weather_alerts() -> str:
    """
    Get active weather alerts.
    """
    return "No active severe weather alerts."

if __name__ == "__main__":
    # Esto permite ejecutar el servidor directamente
    # This allows running the server directly
    mcp.run()
