from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

# Obtener la ruta base del proyecto (carpeta raíz)
BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Crear una ruta específica para la carpeta instance
INSTANCE_PATH = os.path.join(BASEDIR, 'instance')

# Asegurar que la carpeta instance existe
os.makedirs(INSTANCE_PATH, exist_ok=True)

app = Flask(__name__, instance_path=INSTANCE_PATH)

# Rutas absolutas para las bases de datos
DB_PATH = os.path.join(INSTANCE_PATH, 'gym_experto.db')
KB_PATH = os.path.join(INSTANCE_PATH, 'gym_knowledge.db')

# Base de datos transaccional con ruta absoluta
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
# Base de conocimiento con ruta absoluta
app.config['SQLALCHEMY_BINDS'] = {
    'knowledge': f'sqlite:///{KB_PATH}'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

# Inicialización de la base de datos transaccional
db = SQLAlchemy(app)