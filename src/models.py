from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_employee = db.Column(db.Boolean, default=False)  # Nuevo campo para identificar empleados
    
    # Información personal
    nombre_completo = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    genero = db.Column(db.String(20))
    altura = db.Column(db.Float)  # en centímetros
    peso = db.Column(db.Float)    # en kilogramos
    
    # Información de salud
    condiciones_medicas = db.Column(db.String(200))
    lesiones_previas = db.Column(db.String(200))
    medicamentos = db.Column(db.String(200))
    
    # Preferencias de entrenamiento
    fitness_level = db.Column(db.String(20))
    goal = db.Column(db.String(20))
    equipment_available = db.Column(db.Boolean, default=False)
    preferred_muscle_groups = db.Column(db.String(200))
    dias_entrenamiento = db.Column(db.String(100))  # Días disponibles para entrenar
    duracion_entrenamiento = db.Column(db.Integer)  # Duración preferida en minutos
    
    # Relaciones
    workout_history = db.relationship('WorkoutHistory', backref='user', lazy=True)
    exercises_added = db.relationship('Exercise', backref='added_by', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class WorkoutHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    exercises = db.Column(db.String(500))
    duration = db.Column(db.Integer)  # en minutos
    notes = db.Column(db.Text)
    intensidad = db.Column(db.String(20))  # Baja, Media, Alta
    satisfaccion = db.Column(db.Integer)   # 1-5 estrellas
    dificultad = db.Column(db.String(20))  # Fácil, Moderado, Difícil

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    grupo_muscular = db.Column(db.String(50), nullable=False)
    dificultad = db.Column(db.String(20), nullable=False)  # Principiante, Intermedio, Avanzado
    requiere_equipo = db.Column(db.Boolean, default=False)
    descripcion = db.Column(db.Text, nullable=False)
    instrucciones = db.Column(db.Text)
    video_url = db.Column(db.String(200))
    imagen_url = db.Column(db.String(200))
    variaciones = db.Column(db.String(200))
    musculos_secundarios = db.Column(db.String(200))
    series_recomendadas = db.Column(db.String(50))
    repeticiones_recomendadas = db.Column(db.String(50))
    descanso_recomendado = db.Column(db.String(50))
    added_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'grupo_muscular': self.grupo_muscular,
            'dificultad': self.dificultad,
            'requiere_equipo': self.requiere_equipo,
            'descripcion': self.descripcion,
            'instrucciones': self.instrucciones,
            'video_url': self.video_url,
            'imagen_url': self.imagen_url,
            'variaciones': self.variaciones,
            'musculos_secundarios': self.musculos_secundarios,
            'series_recomendadas': self.series_recomendadas,
            'repeticiones_recomendadas': self.repeticiones_recomendadas,
            'descanso_recomendado': self.descanso_recomendado
        } 