from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .config import db

# Modelos transaccionales
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
    __tablename__ = 'exercise'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group = db.Column(db.String(50))
    difficulty = db.Column(db.String(20))
    added_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, name, muscle_group=None, difficulty=None):
        self.name = name
        self.muscle_group = muscle_group
        self.difficulty = difficulty
        
    def add_expert_knowledge(self, muscle_group, difficulty_level, target_muscles,
                           secondary_muscles=None, equipment_needed=None,
                           proper_form_notes=None, common_mistakes=None,
                           safety_precautions=None, contraindications=None,
                           benefits=None, created_by=None):
        """Añade conocimiento experto sobre el ejercicio a la base de conocimiento."""
        from .knowledge_base.manager import KnowledgeBaseManager
        kb_manager = KnowledgeBaseManager()
        kb_manager.add_exercise_knowledge(
            exercise_id=self.id,
            muscle_group=muscle_group,
            difficulty_level=difficulty_level,
            target_muscles=target_muscles,
            secondary_muscles=secondary_muscles,
            equipment_needed=equipment_needed,
            proper_form_notes=proper_form_notes,
            common_mistakes=common_mistakes,
            safety_precautions=safety_precautions,
            contraindications=contraindications,
            benefits=benefits,
            created_by=created_by
        )
    
    def get_expert_knowledge(self):
        """Obtiene el conocimiento experto sobre el ejercicio."""
        from .knowledge_base.manager import KnowledgeBaseManager
        kb_manager = KnowledgeBaseManager()
        return kb_manager.get_exercise_knowledge(self.id)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'muscle_group': self.muscle_group,
            'difficulty': self.difficulty
        }

# Modelos para la base de conocimiento
class KnowledgeExercise(db.Model):
    __bind_key__ = 'knowledge'
    __tablename__ = 'knowledge_exercise'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    muscle_group = db.Column(db.String(50))
    difficulty = db.Column(db.String(20))
    description = db.Column(db.Text)
    created_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class KnowledgeRule(db.Model):
    __bind_key__ = 'knowledge'
    __tablename__ = 'knowledge_rule'
    id = db.Column(db.Integer, primary_key=True)
    rule_name = db.Column(db.String(100), nullable=False)
    antecedent = db.Column(db.Text)
    consequent = db.Column(db.Text)
    priority = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class KnowledgeDecision(db.Model):
    __bind_key__ = 'knowledge'
    __tablename__ = 'knowledge_decision'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    decision_type = db.Column(db.String(50))
    input_facts = db.Column(db.Text)
    applied_rules = db.Column(db.Text)
    conclusion = db.Column(db.Text)
    confidence_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 