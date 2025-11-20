"""
Pydantic Validation
-------------------
Uso de Pydantic para validar y estructurar datos, esencial para 'Tool Calling'.
Using Pydantic to validate and structure data, essential for 'Tool Calling'.
"""

from pydantic import BaseModel, ValidationError, Field
from typing import List, Optional

# Definición del Esquema / Schema Definition
class ProductExtraction(BaseModel):
    product_name: str = Field(description="Name of the product mentioned")
    price: Optional[float] = Field(description="Price if mentioned, else None")
    features: List[str] = Field(description="List of product features")
    sentiment: str = Field(description="Sentiment of the review: positive, negative, neutral")

def validate_llm_output(data: dict):
    """
    Intenta validar un diccionario contra el esquema Pydantic.
    Attempts to validate a dictionary against the Pydantic schema.
    """
    print(f"\nValidating: {data}")
    try:
        product = ProductExtraction(**data)
        print("✅ Validation Successful!")
        print(f"Object: {product}")
        print(f"JSON: {product.model_dump_json()}")
    except ValidationError as e:
        print("❌ Validation Failed!")
        print(e)

if __name__ == "__main__":
    # Caso 1: Datos válidos (Simulando una buena respuesta del LLM)
    valid_response = {
        "product_name": "SuperPhone X",
        "price": 999.99,
        "features": ["5G", "OLED Screen"],
        "sentiment": "positive"
    }
    validate_llm_output(valid_response)
    
    # Caso 2: Datos inválidos (Falta campo requerido, tipo incorrecto)
    invalid_response = {
        "product_name": "OldPhone",
        # "features" is missing
        "sentiment": "mixed", # Valid string, but maybe logic requires specific enum (not enforced here yet)
        "price": "expensive" # Should be float
    }
    validate_llm_output(invalid_response)
