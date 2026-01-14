# Módulo 5.5: Seguridad y Guardrails
# Module 5.5: Safety & Guardrails

En entornos corporativos, no podemos confiar ciegamente en la salida de un LLM. Necesitamos "barandillas" (guardrails) que aseguren que el modelo se comporte dentro de parámetros seguros y éticos.

## ¿Qué son los Guardrails?
Capas de software que interceptan:
1.  **Input:** Antes de llegar al modelo (ej. detectar intentos de Jailbreak o PII).
2.  **Output:** Antes de llegar al usuario (ej. verificar que no haya alucinaciones o contenido tóxico).

## Estrategias de Implementación
1.  **Validación de Sintaxis:** Asegurar que la salida sea JSON válido (pydantic).
2.  **Validación Semántica:** Usar un modelo más pequeño o reglas heurísticas para verificar el contenido.
3.  **Librerías:** `guardrails-ai`, `NeMo Guardrails`.

## Código
Ver `code/guardrails_demo.py` para un ejemplo de implementación del patrón "Self-Check" o validación defensiva.
