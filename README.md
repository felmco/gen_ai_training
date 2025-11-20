# Ingeniería de IA Generativa Aplicada: De Fundamentos a Agentes Autónomos

Bienvenido al repositorio oficial del curso **Ingeniería de IA Generativa Aplicada**. Este material ha sido diseñado para llevarte desde los conceptos fundamentales de Python para IA hasta la construcción de sistemas agénticos complejos y arquitecturas empresariales.

## 🎯 Objetivo del Curso

Formar ingenieros capaces de diseñar, implementar y desplegar soluciones de Inteligencia Artificial Generativa robustas, utilizando el stack tecnológico más moderno de 2025 (OpenAI, DeepSeek, Google ADK, LangGraph, MCP y n8n).

## 📚 Estructura del Contenido

El curso está dividido en fases progresivas. Cada módulo contiene documentación teórica (`README.md`) y código ejecutable (`code/`).

### [Fase 0: Introducción a Python para IA](./00_introduccion_python_ia/README.md)
*   **[Módulo 0.1: Fundamentos Básicos](./00_introduccion_python_ia/01_fundamentos_basicos/README.md)** - Variables (hiperparámetros), bucles (épocas) y condicionales.
*   **[Módulo 0.2: Estructuras de Datos](./00_introduccion_python_ia/02_estructuras_datos/README.md)** - Listas, Diccionarios (JSON) y Sets para NLP.
*   **[Módulo 0.3: Funciones y Modularidad](./00_introduccion_python_ia/03_funciones_modularidad/README.md)** - Funciones de pérdida, activación y tipado.
*   **[Módulo 0.4: POO para IA](./00_introduccion_python_ia/04_poo_para_ia/README.md)** - Clases `Model` y `Agent`.
*   **[Módulo 0.5: Intro Librerías Data Science](./00_introduccion_python_ia/05_intro_librerias_ds/README.md)** - NumPy vs Listas, Matplotlib.

### [Fase 1: Los Cimientos – Python para la Era de la IA](./01_fundamentos_python/README.md)
*   **[Módulo 1.1: Entorno y Configuración](./01_fundamentos_python/01_entorno_configuracion/README.md)** - Gestión profesional de dependencias con `uv`.
*   **[Módulo 1.2: Sintaxis Core](./01_fundamentos_python/02_sintaxis_core/README.md)** - Manipulación avanzada de texto, Regex y JSON.
*   **[Módulo 1.3: Bibliotecas Esenciales](./01_fundamentos_python/03_bibliotecas_esenciales/README.md)** - Pandas para RAG, Pydantic y Asyncio.

### [Fase 2: Consumo de Modelos y APIs](./02_consumo_modelos_apis/README.md)
*   **[Módulo 2.1: OpenAI API](./02_consumo_modelos_apis/01_openai_api/README.md)** - Chat Completions y Structured Outputs.
*   **[Módulo 2.2: Integración DeepSeek](./02_consumo_modelos_apis/02_deepseek_integration/README.md)** - Modelos de Razonamiento (R1) y Context Caching.
*   **[Módulo 2.3: Modelos Locales y Antrópicos](./02_consumo_modelos_apis/03_modelos_locales_antropicos/README.md)** - Ollama y Claude 3.5 Sonnet.

### [Fase 3: RAG Avanzado (Retrieval Augmented Generation)](./03_rag_avanzado/README.md)
*   **[Módulo 3.1: Arquitectura RAG](./03_rag_avanzado/01_arquitectura_rag/README.md)** - Pipelines de ingesta y chunking.
*   **[Módulo 3.2: Embeddings y Vector DBs](./03_rag_avanzado/02_embeddings_vector_dbs/README.md)** - Implementación con ChromaDB.
*   **[Módulo 3.3: Técnicas Avanzadas](./03_rag_avanzado/03_tecnicas_avanzadas/README.md)** - Hybrid Search, Re-ranking y Evaluación (RAGAS).

### [Fase 4: Model Context Protocol (MCP)](./04_protocolos_mcp/README.md)
*   **[Módulo 4.1: Teoría MCP](./04_protocolos_mcp/01_teoria_mcp/README.md)** - El estándar "USB para IA".
*   **[Módulo 4.2: Servidores MCP](./04_protocolos_mcp/02_servidores_mcp/README.md)** - Creación de servidores con FastMCP.
*   **[Módulo 4.3: Integración y Depuración](./04_protocolos_mcp/03_integracion_depuracion/README.md)** - Conexión con Claude Desktop e IDEs.

### [Fase 5: Sistemas Agénticos y Orquestación](./05_sistemas_agenticos/README.md)
*   **[Módulo 5.1: LangChain y LangGraph](./05_sistemas_agenticos/01_langchain_langgraph/README.md)** - Grafos cíclicos y memoria.
*   **[Módulo 5.2: OpenAI Swarm](./05_sistemas_agenticos/02_openai_agents_swarm/README.md)** - Patrones de Handoff y multi-agente.
*   **[Módulo 5.3: Google ADK](./05_sistemas_agenticos/03_google_adk/README.md)** - Agentes empresariales y multimodales.
*   **[Módulo 5.4: Protocolo A2A](./05_sistemas_agenticos/04_protocolo_a2a/README.md)** - Interoperabilidad Agente-a-Agente.

### [Fase 6: Automatización Híbrida con n8n](./06_automatizacion_n8n/README.md)
*   **[Módulo 6.1: Fundamentos n8n](./06_automatizacion_n8n/01_fundamentos_n8n/README.md)** - Webhooks y triggers.
*   **[Módulo 6.2: Agentes en n8n](./06_automatizacion_n8n/02_agentes_n8n/README.md)** - Nodos de IA visuales.
*   **[Módulo 6.3: Arquitectura Final](./06_automatizacion_n8n/03_arquitectura_final/README.md)** - Orquestación Python + n8n.

### [Fase 7: Proyecto Capstone](./07_proyecto_capstone/README.md)
*   **[El Agente Corporativo Autónomo](./07_proyecto_capstone/README.md)** - Integración final de todo el stack.

---

## 🛠️ Requisitos Previos

*   **Python 3.10+** instalado.
*   **Claves de API:** OpenAI, Anthropic, DeepSeek (opcional).
*   **Entorno:** Recomendamos usar VS Code o Cursor.

## 🚀 Cómo empezar

1.  Clona este repositorio.
2.  Crea un entorno virtual:
    ```bash
    uv venv  # o python -m venv .venv
    ```
3.  Navega al módulo que desees estudiar y sigue las instrucciones de su `README.md`.

---
*Generado para el curso de Ingeniería de IA Generativa - 2025*
