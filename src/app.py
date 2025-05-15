from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
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
app.config['SQLALCHEMY_BINDS'] = {
    'knowledge': 'sqlite:///gym_knowledge.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Importar configuración y modelos correctamente
try:
    # Intentar importar desde la carpeta actual (src)
    from src.config import db
    from src.models import User, WorkoutHistory, Exercise, KnowledgeExercise, KnowledgeRule
    from src.inference_engine.engine import InferenceEngine
    from src.knowledge_base.exercises import ExerciseDatabase
    from src.knowledge_base.rules import RuleBase
except ImportError:
    # Si falla, intentar importar de manera relativa
    from .config import db
    from .models import User, WorkoutHistory, Exercise, KnowledgeExercise, KnowledgeRule
    from .inference_engine.engine import InferenceEngine
    from .knowledge_base.exercises import ExerciseDatabase
    from .knowledge_base.rules import RuleBase

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
inference_engine = InferenceEngine()

# Preguntas del asistente (ordenadas) - Ampliado a 25 preguntas
ASSISTANT_QUESTIONS = [
    # Información básica
    {"id": "age", "text": "¿Cuál es tu edad?", "type": "number", "min": 15, "max": 80},
    {"id": "gender", "text": "¿Cuál es tu género?", "type": "select", "options": ["Masculino", "Femenino", "Otro"]},
    {"id": "height", "text": "¿Cuál es tu altura en centímetros?", "type": "number", "min": 140, "max": 220},
    {"id": "weight", "text": "¿Cuál es tu peso en kilogramos?", "type": "number", "min": 40, "max": 180},
    
    # Experiencia y objetivos
    {"id": "experience", "text": "¿Cuántos años de experiencia tienes en el gimnasio?", "type": "number", "min": 0, "max": 30},
    {"id": "goal", "text": "¿Cuál es tu objetivo principal?", "type": "select", "options": ["Fuerza", "Músculo", "Resistencia", "Pérdida de peso", "Mantenimiento"]},
    {"id": "secondary_goal", "text": "¿Tienes algún objetivo secundario?", "type": "select", "options": ["Ninguno", "Fuerza", "Músculo", "Resistencia", "Pérdida de peso", "Mantenimiento", "Flexibilidad"]},
    
    # Disponibilidad
    {"id": "frequency", "text": "¿Cuántos días a la semana puedes entrenar?", "type": "number", "min": 1, "max": 7},
    {"id": "session_duration", "text": "¿Cuántos minutos puedes dedicar a cada sesión de entrenamiento?", "type": "number", "min": 15, "max": 180},
    {"id": "preferred_time", "text": "¿En qué momento del día prefieres entrenar?", "type": "select", "options": ["Mañana", "Mediodía", "Tarde", "Noche"]},
    
    # Condiciones médicas
    {"id": "injuries", "text": "¿Tienes alguna lesión o condición médica?", "type": "boolean"},
    {"id": "injury_type", "text": "Si tienes lesiones, ¿qué áreas están afectadas?", "type": "select", "options": ["Ninguna", "Espalda", "Rodillas", "Hombros", "Codos", "Muñecas", "Tobillos", "Otra"]},
    {"id": "heart_condition", "text": "¿Tienes alguna condición cardíaca?", "type": "boolean"},
    {"id": "diabetes", "text": "¿Padeces diabetes?", "type": "boolean"},
    {"id": "high_blood_pressure", "text": "¿Padeces hipertensión?", "type": "boolean"},
    
    # Equipamiento
    {"id": "equipment", "text": "¿Tienes acceso a equipo de gimnasio?", "type": "boolean"},
    {"id": "equipment_type", "text": "¿Qué tipo de equipo tienes disponible?", "type": "select", "options": ["Ninguno", "Básico (mancuernas/bandas)", "Intermedio (barras/máquinas básicas)", "Completo (gimnasio completo)"]},
    
    # Preferencias de entrenamiento
    {"id": "preferred_exercises", "text": "¿Qué tipo de ejercicios prefieres?", "type": "select", "options": ["Peso libre", "Máquinas", "Calistenia", "Cardio", "Mixto"]},
    {"id": "intensity_preference", "text": "¿Qué nivel de intensidad prefieres en tus entrenamientos?", "type": "select", "options": ["Baja", "Moderada", "Alta", "Muy alta"]},
    {"id": "cardio_preference", "text": "¿Qué tipo de ejercicio cardiovascular prefieres?", "type": "select", "options": ["Ninguno", "Caminata", "Correr", "Ciclismo", "Natación", "HIIT", "Otro"]},
    {"id": "muscle_groups", "text": "¿Qué grupos musculares quieres priorizar?", "type": "select", "options": ["Ninguno específico", "Pecho", "Espalda", "Piernas", "Brazos", "Core", "Hombros"]},
    
    # Estilo de vida
    {"id": "sleep_quality", "text": "¿Cómo calificarías tu calidad de sueño?", "type": "select", "options": ["Mala", "Regular", "Buena", "Excelente"]},
    {"id": "stress_level", "text": "¿Cómo calificarías tu nivel de estrés diario?", "type": "select", "options": ["Bajo", "Moderado", "Alto", "Muy alto"]},
    {"id": "activity_level", "text": "¿Cómo describirías tu nivel de actividad diaria aparte del ejercicio?", "type": "select", "options": ["Sedentario", "Ligeramente activo", "Moderadamente activo", "Muy activo"]},
    {"id": "diet_quality", "text": "¿Cómo calificarías tu alimentación actual?", "type": "select", "options": ["Deficiente", "Regular", "Buena", "Excelente"]},
    {"id": "expected_timeline", "text": "¿En cuánto tiempo esperas ver resultados significativos? (meses)", "type": "number", "min": 1, "max": 24}
]

def init_all_db():
    """Inicializa ambas bases de datos y asegura que todas las tablas existan"""
    with app.app_context():
        try:
            db.drop_all()
            db.create_all()
            print("Todas las tablas creadas en ambas bases de datos.")
        except Exception as e:
            logger.error(f"Error al inicializar las bases de datos: {str(e)}")
            raise

# Inicializar ambas bases de datos
init_all_db()

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
        return redirect(url_for('asistente'))
    
    if request.method == 'POST':
        try:
            user = User.query.filter_by(username=request.form['username']).first()
            if user is None or not user.check_password(request.form['password']):
                flash('Usuario o contraseña inválidos', 'error')
                return redirect(url_for('login'))
            
            login_user(user)
            # Siempre redirigir al asistente tras login
            return redirect(url_for('asistente'))
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

@app.route('/asistente')
@login_required
def asistente():
    session['assistant_answers'] = {}
    session['assistant_step'] = 0
    return redirect(url_for('asistente_pregunta'))

@app.route('/asistente/pregunta', methods=['GET', 'POST'])
@login_required
def asistente_pregunta():
    step = session.get('assistant_step', 0)
    answers = session.get('assistant_answers', {})
    if request.method == 'POST':
        # Guardar respuesta
        qid = ASSISTANT_QUESTIONS[step]['id']
        value = request.form.get('respuesta')
        # Convertir a tipo adecuado
        if ASSISTANT_QUESTIONS[step]['type'] == 'number':
            value = int(value)
        elif ASSISTANT_QUESTIONS[step]['type'] == 'boolean':
            value = value == 'true'
        answers[qid] = value
        session['assistant_answers'] = answers
        session['assistant_step'] = step + 1
        step += 1
    if step >= len(ASSISTANT_QUESTIONS):
        return redirect(url_for('asistente_resultado'))
    question = ASSISTANT_QUESTIONS[step]
    return render_template('asistente_pregunta.html', question=question, step=step+1, total=len(ASSISTANT_QUESTIONS))

@app.route('/submit_answer', methods=['POST'])
@login_required
def submit_answer():
    # Recibir datos de la petición AJAX
    data = request.json
    question_id = data.get('question_id')
    answer = data.get('answer')
    
    # Guardar en la sesión
    answers = session.get('assistant_answers', {})
    answers[question_id] = answer
    session['assistant_answers'] = answers
    
    step = session.get('assistant_step', 0)
    step += 1
    session['assistant_step'] = step
    
    # Verificar si hemos completado todas las preguntas
    if step >= len(ASSISTANT_QUESTIONS):
        return jsonify({
            'status': 'complete',
            'redirect': url_for('asistente_resultado')
        })
    else:
        # Enviar la siguiente pregunta
        return jsonify({
            'status': 'continue',
            'question': ASSISTANT_QUESTIONS[step]
        })

@app.route('/asistente/resultado')
@login_required
def asistente_resultado():
    # Verificar si hay respuestas en la sesión
    if 'assistant_answers' not in session:
        return redirect(url_for('asistente'))
    
    # Obtener recomendación
    result = inference_engine.make_recommendation(current_user.id, session['assistant_answers'])
    session['result'] = result
    
    return render_template('asistente_resultado.html', result=result)

@app.route('/asistente/rutina/<int:rutina_id>')
@login_required
def ver_rutina(rutina_id):
    """Muestra los detalles completos de una rutina específica."""
    # Importar rutinas detalladas primero
    try:
        from src.inference_engine.workout_routines import obtener_rutina_detallada
    except ImportError:
        from .inference_engine.workout_routines import obtener_rutina_detallada
    
    # Método 1: Intentar obtener desde la sesión actual (caso ideal)
    if 'result' in session:
        result = session['result']
        
        # Encontrar la rutina por su ID
        rutina = None
        for r in result['all_routines']:
            if r['id'] == rutina_id:
                rutina = r
                break
                
        if rutina:
            # Obtener más detalles de la rutina
            detalles = obtener_rutina_detallada(rutina['hipotesis'])
            # Hacer una copia para no modificar la original en la sesión
            rutina_completa = dict(rutina)
            rutina_completa.update(detalles)
            return render_template('rutina_detalle.html', rutina=rutina_completa)
    
    # Método 2: Si no está en la sesión, recrear la información de la rutina por su ID
    # Las rutinas tienen IDs del 1 al 25 (5 tipos x 5 rutinas cada uno)
    if 1 <= rutina_id <= 25:
        # Mapeo de IDs a tipos de rutinas (cada 5 IDs es un nuevo tipo)
        categorias = [
            "Fuerza", "Fuerza", "Fuerza", "Fuerza", "Fuerza",
            "Músculo", "Músculo", "Músculo", "Músculo", "Músculo",
            "Resistencia", "Resistencia", "Resistencia", "Resistencia", "Resistencia",
            "Pérdida de peso", "Pérdida de peso", "Pérdida de peso", "Pérdida de peso", "Pérdida de peso",
            "Mantenimiento", "Mantenimiento", "Mantenimiento", "Mantenimiento", "Mantenimiento"
        ]
        
        # Mapeo de IDs a nombres específicos de rutinas
        nombres_rutinas = [
            # Fuerza
            "Rutina de Fuerza Máxima", "Rutina de Fuerza Explosiva", "Rutina de Fuerza-Resistencia", 
            "Rutina de Fuerza Funcional", "Rutina de Fuerza Compuesta",
            # Músculo (Hipertrofia)
            "Rutina de Hipertrofia Volumen", "Rutina de Hipertrofia Intensidad", "Rutina de Hipertrofia Frecuencia", 
            "Rutina de Hipertrofia Split", "Rutina de Hipertrofia Full Body",
            # Resistencia
            "Rutina de Resistencia Cardiovascular", "Rutina de Resistencia Muscular", "Rutina de Resistencia Mixta", 
            "Rutina de Resistencia Intervalos", "Rutina de Resistencia Circuitos",
            # Pérdida de peso
            "Rutina de Pérdida de Peso HIIT", "Rutina de Pérdida de Peso Cardio", "Rutina de Pérdida de Peso Fuerza", 
            "Rutina de Pérdida de Peso Circuitos", "Rutina de Pérdida de Peso Mixta",
            # Mantenimiento
            "Rutina de Mantenimiento Equilibrio", "Rutina de Mantenimiento Flexibilidad", "Rutina de Mantenimiento Fuerza", 
            "Rutina de Mantenimiento Cardio", "Rutina de Mantenimiento Funcional"
        ]
        
        # Obtener el índice en la lista (rutina_id es 1-based, pero los índices son 0-based)
        idx = rutina_id - 1
        
        if idx < len(nombres_rutinas):
            nombre_rutina = nombres_rutinas[idx]
            categoria = categorias[idx]
            
            # Crear una rutina ficticia con la información básica
            rutina_recreada = {
                'id': rutina_id,
                'hipotesis': nombre_rutina,
                'probabilidad': "N/A (vista directa)",
                'probabilidad_numerica': 0,
                'categoria': categoria
            }
            
            # Obtener los detalles completos de la rutina
            detalles = obtener_rutina_detallada(nombre_rutina)
            rutina_recreada.update(detalles)
            
            return render_template('rutina_detalle.html', rutina=rutina_recreada)
    
    # Si no se encontró la rutina por ninguno de los métodos
    flash('Rutina no encontrada. Por favor, realiza una nueva consulta.', 'error')
    return redirect(url_for('asistente'))

if __name__ == '__main__':
    app.run(debug=True)