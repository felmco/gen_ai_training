"""
Environment Check Script
------------------------
Este script verifica si se está ejecutando dentro de un entorno virtual
y lista los paquetes instalados clave para el desarrollo de IA.

This script checks if it is running inside a virtual environment
and lists key installed packages for AI development.
"""

import sys
import os
import importlib.util

def check_virtual_env():
    """
    Verifica si estamos en un entorno virtual.
    Checks if we are in a virtual environment.
    """
    # Check for standard virtual env indicators
    is_venv = (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )
    
    print(f"Python Executable: {sys.executable}")
    
    if is_venv:
        print("✅ ESTADO: Ejecutando dentro de un entorno virtual.")
        print("✅ STATUS: Running inside a virtual environment.")
    else:
        print("⚠️  ADVERTENCIA: No se detectó un entorno virtual activo.")
        print("⚠️  WARNING: No active virtual environment detected.")
        print("   Se recomienda usar 'uv venv' o 'python -m venv .venv' antes de instalar paquetes.")

def check_dependencies():
    """
    Verifica la instalación de bibliotecas clave.
    Checks for key library installations.
    """
    key_packages = ['openai', 'langchain', 'google.generativeai', 'pydantic', 'fastapi']
    
    print("\nVerificando paquetes clave / Checking key packages:")
    for package in key_packages:
        spec = importlib.util.find_spec(package)
        found = "✅ Instalado" if spec else "❌ No encontrado"
        print(f"- {package}: {found}")

if __name__ == "__main__":
    print("--- Configuración del Entorno / Environment Configuration ---\n")
    check_virtual_env()
    check_dependencies()
    print("\n-----------------------------------------------------------")
