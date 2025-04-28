from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from models import db, User, WorkoutHistory, Exercise
from inference_engine.engine import InferenceEngine
from knowledge_base.exercises import ExerciseDatabase
from knowledge_base.rules import RuleBase
import os
from werkzeug.exceptions import HTTPException
import logging
import sqlite3

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gym_experto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar extensiones
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor inicia sesión para acceder a esta página.'
login_manager.login_message_category = 'info'

# Inicializar componentes del sistema experto
exercise_db = ExerciseDatabase()
rule_base = RuleBase()
inference_engine = InferenceEngine(rule_base, exercise_db)

def init_db():
    """Inicializa la base de datos y asegura que todas las tablas existan"""
    with app.app_context():
        try:
            # Intentar eliminar todas las tablas existentes
            db.drop_all()
            logger.info("Tablas anteriores eliminadas")
            
            # Crear la base de datos con el esquema actualizado
            db.create_all()
            logger.info("Base de datos creada exitosamente con el esquema actualizado")
        except Exception as e:
            logger.error(f"Error al inicializar la base de datos: {str(e)}")
            raise

# Inicializar la base de datos
init_db()

@login_manager.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except Exception as e:
        logger.error(f"Error al cargar usuario: {str(e)}")
        return None

@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        return e
    logger.error(f"Error no manejado: {str(e)}")
    return render_template('error.html', error=str(e)), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            user = User.query.filter_by(username=request.form['username']).first()
            if user is None or not user.check_password(request.form['password']):
                flash('Usuario o contraseña inválidos', 'error')
                return redirect(url_for('login'))
            
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        except Exception as e:
            logger.error(f"Error en login: {str(e)}")
            flash('Error al iniciar sesión. Por favor intente nuevamente.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        is_employee = 'is_employee' in request.form
        
        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya está en uso')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('El email ya está registrado')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, is_employee=is_employee)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('¡Registro exitoso! Por favor inicia sesión.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/evaluacion', methods=['GET', 'POST'])
@login_required
def evaluacion():
    if request.method == 'POST':
        # Obtener datos del formulario
        user_facts = {
            'fitness_level': request.form.get('fitness_level'),
            'goal': request.form.get('goal'),
            'equipment_available': request.form.get('equipment_available') == 'true',
            'preferred_muscle_groups': request.form.getlist('preferred_muscle_groups'),
            'dias_entrenamiento': request.form.getlist('dias_entrenamiento'),
            'edad': int(request.form.get('edad')),
            'peso': float(request.form.get('peso')),
            'altura': float(request.form.get('altura')),
            'genero': request.form.get('genero'),
            'condiciones_medicas': request.form.get('condiciones_medicas')
        }
        
        # Actualizar perfil del usuario
        current_user.fitness_level = user_facts['fitness_level']
        current_user.goal = user_facts['goal']
        current_user.equipment_available = user_facts['equipment_available']
        current_user.preferred_muscle_groups = ','.join(user_facts['preferred_muscle_groups'])
        current_user.edad = user_facts['edad']
        current_user.peso = user_facts['peso']
        current_user.altura = user_facts['altura']
        current_user.genero = user_facts['genero']
        current_user.condiciones_medicas = user_facts['condiciones_medicas']
        db.session.commit()
        
        # Obtener recomendaciones
        recommendations = inference_engine.get_recommendations(user_facts)
        
        return render_template('resultados.html', recommendations=recommendations)
    
    return render_template('evaluacion.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/historial')
@login_required
def historial():
    workouts = WorkoutHistory.query.filter_by(user_id=current_user.id).order_by(WorkoutHistory.date.desc()).all()
    return render_template('historial.html', workouts=workouts)

@app.route('/guardar_entrenamiento', methods=['POST'])
@login_required
def guardar_entrenamiento():
    workout = WorkoutHistory(
        user_id=current_user.id,
        exercises=request.form.get('exercises'),
        duration=request.form.get('duration'),
        notes=request.form.get('notes')
    )
    db.session.add(workout)
    db.session.commit()
    flash('Entrenamiento guardado exitosamente')
    return redirect(url_for('historial'))

@app.route('/agregar_ejercicio', methods=['GET', 'POST'])
@login_required
def agregar_ejercicio():
    if not current_user.is_employee:
        flash('No tienes permisos para acceder a esta página')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        exercise = Exercise(
            nombre=request.form.get('nombre'),
            grupo_muscular=request.form.get('grupo_muscular'),
            dificultad=request.form.get('dificultad'),
            requiere_equipo=request.form.get('requiere_equipo') == 'true',
            descripcion=request.form.get('descripcion'),
            instrucciones=request.form.get('instrucciones'),
            video_url=request.form.get('video_url'),
            imagen_url=request.form.get('imagen_url'),
            variaciones=request.form.get('variaciones'),
            musculos_secundarios=request.form.get('musculos_secundarios'),
            series_recomendadas=request.form.get('series_recomendadas'),
            repeticiones_recomendadas=request.form.get('repeticiones_recomendadas'),
            descanso_recomendado=request.form.get('descanso_recomendado'),
            added_by_id=current_user.id
        )
        db.session.add(exercise)
        db.session.commit()
        
        # Agregar el ejercicio a la base de conocimientos
        exercise_db.add_exercise(exercise)
        
        flash('Ejercicio agregado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('agregar_ejercicio.html')

if __name__ == '__main__':
    app.run(debug=True) 