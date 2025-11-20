# Proyecto Capstone: El Agente Corporativo Autónomo

**Objetivo:** Construir un sistema que integra todo el stack aprendido.

## El Escenario
Eres el Ingeniero de IA Principal en "FinTech Corp". El equipo de marketing necesita un reporte diario de tendencias de mercado, pero están cansados de buscar en Google y en la base de datos interna manualmente.

## La Misión
Construir un sistema que:
1.  Reciba una solicitud vía **Webhook** (simulado o n8n).
2.  Active un **Agente Orquestador** (LangGraph).
3.  Use **RAG** para consultar las políticas de inversión internas (PDFs vectorizados).
4.  Use una **Herramienta de Búsqueda** (Tavily/Google) para noticias externas.
5.  Use un **Modelo de Razonamiento** (DeepSeek R1 o GPT-4o) para sintetizar la estrategia.
6.  Genere un reporte en Markdown/PDF.

## Arquitectura

```mermaid
graph TD
    Input[Webhook Request] --> Agent[Agente Orquestador]
    
    subgraph "Cerebro"
        Agent --> Planner[Planificador]
        Planner --> R1[DeepSeek R1]
    end
    
    subgraph "Herramientas"
        Agent --> RAG[RAG Tool (ChromaDB)]
        Agent --> Search[Search Tool (Tavily)]
    end
    
    Agent --> Output[Reporte Final]
```

## Entregable
El código en `code/main_agent.py` es el esqueleto de esta solución. Tu tarea es completar las funciones `TODO`.
