"""
Archivo simple para ejecutar la aplicación.
"""
import os
import sys

# Añadir el directorio actual al path de Python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Importar lo necesario directamente de src/
from src.app import app

if __name__ == '__main__':
    print("Iniciando la aplicación...")
    app.run(debug=True)
