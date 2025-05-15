"""
Motor de inferencia para el sistema experto de gimnasio.
Implementa el razonamiento bayesiano para generar recomendaciones.
"""

# Importaciones compatibles con ejecución como módulo o directamente
try:
    from src.knowledge_base.manager import KnowledgeBaseManager
except ImportError:
    try:
        from knowledge_base.manager import KnowledgeBaseManager
    except ImportError:
        from ..knowledge_base.manager import KnowledgeBaseManager
import numpy as np
from typing import List, Dict, Tuple

class InferenceEngine:
    def __init__(self):
        self.kb_manager = KnowledgeBaseManager()
        self.hypotheses_by_goal = {
            "Fuerza": [
                "Rutina de Fuerza Máxima",
                "Rutina de Fuerza Explosiva",
                "Rutina de Fuerza-Resistencia",
                "Rutina de Fuerza Funcional",
                "Rutina de Fuerza Compuesta"
            ],
            "Músculo": [
                "Rutina de Hipertrofia Volumen",
                "Rutina de Hipertrofia Intensidad",
                "Rutina de Hipertrofia Frecuencia",
                "Rutina de Hipertrofia Split",
                "Rutina de Hipertrofia Full Body"
            ],
            "Resistencia": [
                "Rutina de Resistencia Cardiovascular",
                "Rutina de Resistencia Muscular",
                "Rutina de Resistencia Mixta",
                "Rutina de Resistencia Intervalos",
                "Rutina de Resistencia Circuitos"
            ],
            "Pérdida de peso": [
                "Rutina de Pérdida de Peso HIIT",
                "Rutina de Pérdida de Peso Cardio",
                "Rutina de Pérdida de Peso Fuerza",
                "Rutina de Pérdida de Peso Circuitos",
                "Rutina de Pérdida de Peso Mixta"
            ],
            "Mantenimiento": [
                "Rutina de Mantenimiento Equilibrio",
                "Rutina de Mantenimiento Flexibilidad",
                "Rutina de Mantenimiento Fuerza",
                "Rutina de Mantenimiento Cardio",
                "Rutina de Mantenimiento Funcional"
            ]
        }
        # Preguntas ya definidas en app.py

    def get_next_question(self, answered_questions: Dict) -> Dict:
        """Obtiene la siguiente pregunta basada en las respuestas anteriores."""
        from src.app import ASSISTANT_QUESTIONS
        for question in ASSISTANT_QUESTIONS:
            if question["id"] not in answered_questions:
                return question
        return None

    def calculate_bayesian_probabilities(self, evidence: Dict) -> List[Tuple[str, float]]:
        """
        Calcula las probabilidades bayesianas para las hipótesis específicas del objetivo.
        """
        if 'goal' not in evidence:
            return []

        goal = evidence['goal']
        hypotheses = self.hypotheses_by_goal.get(goal, [])
        
        # Probabilidades a priori para cada hipótesis del objetivo
        prior_probabilities = {h: 0.2 for h in hypotheses}  # Distribución uniforme inicial

        # Matriz de verosimilitud (P(E|H))
        likelihood_matrix = self._calculate_likelihood_matrix(evidence, goal)
        
        # Calcular probabilidades posteriores
        posterior_probabilities = []
        total_evidence_prob = 0.0

        for hypothesis in hypotheses:
            # Calcular P(E|H) * P(H) y aplicar factor de unicidad
            likelihood = likelihood_matrix[hypothesis]
            prior = prior_probabilities[hypothesis]
            
            # Crear factor de unicidad para esta hipótesis basado en su índice
            uniqueness_factor = 1.0 + (list(hypotheses).index(hypothesis) * 0.05)
            
            # Aplicar el factor de unicidad para garantizar probabilidades distintas
            joint_prob = likelihood * prior * uniqueness_factor
            
            total_evidence_prob += joint_prob
            posterior_probabilities.append((hypothesis, joint_prob))

        # Normalizar las probabilidades
        normalized_probabilities = []
        for hypothesis, prob in posterior_probabilities:
            normalized_prob = prob / total_evidence_prob if total_evidence_prob > 0 else 0
            normalized_probabilities.append((hypothesis, normalized_prob))

        # Ordenar por probabilidad descendente
        return sorted(normalized_probabilities, key=lambda x: x[1], reverse=True)

    def _calculate_likelihood_matrix(self, evidence: Dict, goal: str) -> Dict[str, float]:
        """Calcula la matriz de verosimilitud P(E|H) para cada hipótesis del objetivo."""
        hypotheses = self.hypotheses_by_goal[goal]
        likelihoods = {}
        
        # Asignar un pequeño factor de unicidad a cada hipótesis para garantizar que todas tengan probabilidades diferentes
        # El índice en la lista determina un pequeño ajuste para cada hipótesis (1%, 2%, 3%, etc.)
        uniqueness_factors = {hypothesis: 1.0 + (i * 0.05) for i, hypothesis in enumerate(hypotheses)}
        
        for hypothesis in hypotheses:
            likelihood = 1.0
            
            # Información básica
            # Edad
            if 'age' in evidence:
                age = evidence['age']
                if "Máxima" in hypothesis or "Explosiva" in hypothesis:
                    likelihood *= self._gaussian_probability(age, 25, 8)
                elif "Resistencia" in hypothesis:
                    likelihood *= self._gaussian_probability(age, 30, 10)
                elif "HIIT" in hypothesis:
                    likelihood *= self._gaussian_probability(age, 28, 12)
                else:
                    likelihood *= self._gaussian_probability(age, 35, 15)
            
            # Género
            if 'gender' in evidence:
                gender = evidence['gender']
                if gender == "Masculino":
                    if "Fuerza" in hypothesis or "Hipertrofia" in hypothesis:
                        likelihood *= 1.2
                    elif "Flexibilidad" in hypothesis:
                        likelihood *= 0.9
                elif gender == "Femenino":
                    if "Pérdida de Peso" in hypothesis or "Resistencia" in hypothesis:
                        likelihood *= 1.1
                    if "Flexibilidad" in hypothesis:
                        likelihood *= 1.2
            
            # Relación altura/peso (IMC aproximado)
            if 'height' in evidence and 'weight' in evidence:
                height_m = evidence['height'] / 100  # convertir a metros
                weight = evidence['weight']
                bmi = weight / (height_m * height_m)
                
                if bmi > 30:  # Sobrepeso significativo
                    if "Pérdida de Peso" in hypothesis:
                        likelihood *= 1.5
                    elif "Fuerza Máxima" in hypothesis:
                        likelihood *= 0.7
                elif bmi < 20:  # Bajo peso
                    if "Hipertrofia" in hypothesis or "Fuerza" in hypothesis:
                        likelihood *= 1.3
                    elif "Pérdida de Peso" in hypothesis:
                        likelihood *= 0.5
                else:  # Peso normal
                    if "Mantenimiento" in hypothesis:
                        likelihood *= 1.2
            
            # Experiencia y objetivos
            if 'experience' in evidence:
                exp = evidence['experience']
                if "Máxima" in hypothesis or "Explosiva" in hypothesis or "Intensidad" in hypothesis:
                    likelihood *= self._gaussian_probability(exp, 4, 1.5)
                elif "Resistencia" in hypothesis:
                    likelihood *= self._gaussian_probability(exp, 2, 1)
                elif "HIIT" in hypothesis:
                    likelihood *= self._gaussian_probability(exp, 1.5, 1)
                else:
                    likelihood *= self._gaussian_probability(exp, 2.5, 1.5)
            
            # Objetivo secundario
            if 'secondary_goal' in evidence:
                secondary_goal = evidence['secondary_goal']
                if secondary_goal != "Ninguno":
                    # Incrementar probabilidad si la rutina combina objetivo principal y secundario
                    if goal == "Fuerza" and secondary_goal == "Músculo":
                        if "Compuesta" in hypothesis:
                            likelihood *= 1.3
                    elif goal == "Músculo" and secondary_goal == "Fuerza":
                        if "Intensidad" in hypothesis:
                            likelihood *= 1.3
                    elif secondary_goal == "Flexibilidad":
                        if "Funcional" in hypothesis or "Equilibrio" in hypothesis:
                            likelihood *= 1.2
                    elif secondary_goal == "Resistencia":
                        if "Circuitos" in hypothesis or "Mixta" in hypothesis:
                            likelihood *= 1.2
            
            # Disponibilidad
            if 'frequency' in evidence:
                freq = evidence['frequency']
                if "Split" in hypothesis:
                    likelihood *= self._gaussian_probability(freq, 5, 1)
                elif "Full Body" in hypothesis:
                    likelihood *= self._gaussian_probability(freq, 3, 1)
                elif "HIIT" in hypothesis or "Circuitos" in hypothesis:
                    likelihood *= self._gaussian_probability(freq, 4, 1)
                else:
                    likelihood *= self._gaussian_probability(freq, 4, 1.5)
            
            # Duración de sesión
            if 'session_duration' in evidence:
                duration = evidence['session_duration']
                if duration < 30:
                    if "HIIT" in hypothesis or "Circuitos" in hypothesis:
                        likelihood *= 1.5
                    elif "Volumen" in hypothesis or "Split" in hypothesis:
                        likelihood *= 0.4
                elif duration > 90:
                    if "Volumen" in hypothesis or "Intensidad" in hypothesis:
                        likelihood *= 1.4
                    elif "HIIT" in hypothesis:
                        likelihood *= 0.6
            
            # Equipamiento
            if 'equipment' in evidence:
                has_equipment = evidence['equipment']
                if has_equipment:
                    if "Fuerza" in hypothesis or "Hipertrofia" in hypothesis:
                        likelihood *= 1.2
                else:
                    if "Funcional" in hypothesis or "Cardio" in hypothesis or "Pérdida de Peso" in hypothesis:
                        likelihood *= 1.3
                    elif "Máxima" in hypothesis or "Intensidad" in hypothesis:
                        likelihood *= 0.5
            
            # Lesiones
            if 'injuries' in evidence:
                has_injuries = evidence['injuries']
                if has_injuries:
                    if "Funcional" in hypothesis or "Flexibilidad" in hypothesis:
                        likelihood *= 1.2
                    elif "Máxima" in hypothesis or "Explosiva" in hypothesis or "HIIT" in hypothesis:
                        likelihood *= 0.4
            
            # Aplicar factor de unicidad para asegurar que cada hipótesis tenga una probabilidad única
            likelihood *= uniqueness_factors[hypothesis]
            
            likelihoods[hypothesis] = likelihood
        
        return likelihoods

    def _gaussian_probability(self, x: float, mean: float, std: float) -> float:
        """Calcula la probabilidad usando una distribución gaussiana."""
        return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))

    def make_recommendation(self, user_id: int, evidence: Dict) -> Dict:
        """
        Genera recomendaciones basadas en las probabilidades bayesianas.
        """
        if 'goal' not in evidence:
            return {
                'recommendation': "No se ha especificado un objetivo principal. Por favor, completa todas las preguntas.",
                'best_routine': None,
                'all_routines': []
            }
        
        # Calcular probabilidades para las hipótesis
        probabilities = self.calculate_bayesian_probabilities(evidence)
        
        # Generar recomendaciones detalladas para cada hipótesis
        all_routines = []
        for i, (hypothesis, probability) in enumerate(probabilities):
            routine_details = self._generate_recommendation(hypothesis, evidence)
            all_routines.append({
                'id': i + 1,  # ID único para cada rutina
                'hipotesis': hypothesis,
                'probabilidad': f"{probability * 100:.1f}%",
                'probabilidad_numerica': probability,
                'descripcion': routine_details['descripcion'],
                'dias': routine_details.get('dias', [])
            })
        
        # Obtener la hipótesis más probable
        best_routine = all_routines[0]
        
        # Crear mensaje de recomendación (sólo para la mejor hipótesis)
        recommendation_message = f"""
La rutina más recomendada para ti es: {best_routine['hipotesis']}
Con una probabilidad de: {best_routine['probabilidad']}

Descripción de la rutina recomendada:
{best_routine['descripcion']}
"""
        
        # Registrar la decisión
        self.kb_manager.record_decision(
            user_id=user_id,
            decision_type='routine_recommendation',
            input_facts=evidence,
            applied_rules=str(probabilities),
            conclusion=best_routine['descripcion'],
            confidence_score=best_routine['probabilidad_numerica']
        )
        
        return {
            'recommendation': recommendation_message,
            'best_routine': best_routine,
            'all_routines': all_routines
        }

    def _generate_recommendation(self, hypothesis: str, evidence: Dict) -> dict:
        """Genera una recomendación específica basada en la hipótesis más probable."""
        # Importar las rutinas detalladas de manera compatible
        try:
            from src.inference_engine.workout_routines import obtener_rutina_detallada
        except ImportError:
            try:
                from inference_engine.workout_routines import obtener_rutina_detallada
            except ImportError:
                from .workout_routines import obtener_rutina_detallada
        
        # Descripciones básicas de las rutinas (para compatibilidad)
        basic_descriptions = {
            # Fuerza
            "Rutina de Fuerza Máxima": "Rutina enfocada en desarrollar la máxima fuerza con pesos pesados y bajas repeticiones.",
            "Rutina de Fuerza Explosiva": "Rutina que combina fuerza y velocidad para desarrollar potencia explosiva.",
            "Rutina de Fuerza-Resistencia": "Rutina que combina elementos de fuerza y resistencia muscular.",
            "Rutina de Fuerza Funcional": "Rutina que enfatiza movimientos funcionales y patrones de movimiento naturales.",
            "Rutina de Fuerza Compuesta": "Rutina basada en ejercicios compuestos para desarrollar fuerza general.",
            
            # Hipertrofia
            "Rutina de Hipertrofia Volumen": "Rutina de alto volumen para maximizar el crecimiento muscular.",
            "Rutina de Hipertrofia Intensidad": "Rutina de alta intensidad con técnicas avanzadas de hipertrofia.",
            "Rutina de Hipertrofia Frecuencia": "Rutina que divide el volumen en más sesiones semanales.",
            "Rutina de Hipertrofia Split": "Rutina dividida por grupos musculares para mayor volumen por músculo.",
            "Rutina de Hipertrofia Full Body": "Rutina de cuerpo completo para hipertrofia general.",
            
            # Resistencia
            "Rutina de Resistencia Cardiovascular": "Rutina enfocada en mejorar la capacidad cardiovascular.",
            "Rutina de Resistencia Muscular": "Rutina para mejorar la resistencia muscular local.",
            "Rutina de Resistencia Mixta": "Rutina que combina resistencia cardiovascular y muscular.",
            "Rutina de Resistencia Intervalos": "Rutina basada en intervalos de alta intensidad.",
            "Rutina de Resistencia Circuitos": "Rutina en circuito para mejorar la resistencia general.",
            
            # Pérdida de peso
            "Rutina de Pérdida de Peso HIIT": "Rutina de intervalos de alta intensidad para maximizar la quema de calorías.",
            "Rutina de Pérdida de Peso Cardio": "Rutina cardiovascular para pérdida de peso sostenida.",
            "Rutina de Pérdida de Peso Fuerza": "Rutina de fuerza para mantener masa muscular durante la pérdida de peso.",
            "Rutina de Pérdida de Peso Circuitos": "Rutina en circuito para combinar cardio y fuerza.",
            "Rutina de Pérdida de Peso Mixta": "Rutina que combina diferentes métodos para pérdida de peso.",
            
            # Mantenimiento
            "Rutina de Mantenimiento Equilibrio": "Rutina que mantiene un equilibrio entre diferentes aspectos del fitness.",
            "Rutina de Mantenimiento Flexibilidad": "Rutina que enfatiza la flexibilidad y movilidad.",
            "Rutina de Mantenimiento Fuerza": "Rutina de fuerza para mantener la masa muscular.",
            "Rutina de Mantenimiento Cardio": "Rutina cardiovascular para mantener la condición física.",
            "Rutina de Mantenimiento Funcional": "Rutina funcional para mantener la capacidad física general."
        }
        
        # Obtener la rutina detallada
        rutina_detallada = obtener_rutina_detallada(hypothesis)
        
        # Si no existe descripción detallada, usar la básica
        if not rutina_detallada or "descripcion" not in rutina_detallada:
            rutina_detallada = {
                "descripcion": basic_descriptions.get(hypothesis, f"Descripción para {hypothesis} no disponible.")
            }
        
        return rutina_detallada

    def get_recommendations(self, user_facts: Dict) -> Dict:
        """Método de compatibilidad para la integración con el sistema existente."""
        # Mapear los hechos del usuario a evidencia
        evidence = {
            "goal": user_facts.get("goal", "Fuerza"),
            "age": user_facts.get("edad", 30),
            "experience": user_facts.get("fitness_level", "Intermedio"),
            "equipment": user_facts.get("equipment_available", True),
            "injuries": user_facts.get("condiciones_medicas", "").lower().find("ninguna") == -1,
            "frequency": len(user_facts.get("dias_entrenamiento", [])) or 3
        }
        
        # Inferir recomendaciones
        return self.make_recommendation(user_id=1, evidence=evidence)  # user_id genérico
