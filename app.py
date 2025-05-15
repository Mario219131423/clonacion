"""
Archivo para ejecutar la aplicación Gym Experto desde la raíz del proyecto.
Este archivo simplemente importa la aplicación Flask de src/app.py y la ejecuta.
"""

import os
import sys

# Añadir la ruta actual al path de Python para encontrar el módulo src
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importar la aplicación desde src/app.py
from src.app import app

if __name__ == '__main__':
    print("Iniciando aplicación Gym Experto...")
    app.run(debug=True)