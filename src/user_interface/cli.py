class CLI:
    def __init__(self, inference_engine):
        self.inference_engine = inference_engine

    def start(self):
        print("Bienvenido al Sistema Experto de Gimnasio")
        print("=======================================")
        
        # Obtener información del usuario
        user_facts = self._get_user_facts()
        
        # Obtener recomendaciones
        recommendations = self.inference_engine.get_recommendations(user_facts)
        
        # Mostrar recomendaciones
        self._display_recommendations(recommendations)

    def _get_user_facts(self):
        facts = {}
        
        # Nivel de condición física
        print("\n¿Cuál es tu nivel de condición física?")
        print("1. Principiante")
        print("2. Intermedio")
        print("3. Avanzado")
        level_choice = input("Selecciona una opción (1-3): ")
        level_map = {'1': 'beginner', '2': 'intermediate', '3': 'advanced'}
        facts['fitness_level'] = level_map.get(level_choice, 'beginner')
        
        # Objetivo
        print("\n¿Cuál es tu objetivo principal?")
        print("1. Fuerza")
        print("2. Resistencia")
        goal_choice = input("Selecciona una opción (1-2): ")
        goal_map = {'1': 'strength', '2': 'endurance'}
        facts['goal'] = goal_map.get(goal_choice, 'strength')
        
        # Equipo disponible
        print("\n¿Tienes acceso a equipo de gimnasio?")
        equipment_choice = input("Responde (s/n): ").lower()
        facts['equipment_available'] = equipment_choice == 's'
        
        # Grupos musculares preferidos
        print("\n¿Qué grupos musculares te gustaría trabajar? (puedes seleccionar varios)")
        print("1. Pecho")
        print("2. Espalda")
        print("3. Piernas")
        print("4. Core")
        print("5. Todos")
        muscle_choice = input("Selecciona una opción (1-5): ")
        muscle_map = {
            '1': ['chest'],
            '2': ['back'],
            '3': ['legs'],
            '4': ['core'],
            '5': ['chest', 'back', 'legs', 'core']
        }
        facts['preferred_muscle_groups'] = muscle_map.get(muscle_choice, ['chest', 'back', 'legs', 'core'])
        
        return facts

    def _display_recommendations(self, recommendations):
        if not recommendations:
            print("\nLo siento, no se encontraron ejercicios que coincidan con tus criterios.")
            return
        
        print("\nRutina recomendada:")
        print("==================")
        for i, exercise in enumerate(recommendations, 1):
            print(f"\n{i}. {exercise.name}")
            print(f"   Grupo muscular: {exercise.muscle_group}")
            print(f"   Dificultad: {exercise.difficulty}")
            print(f"   Descripción: {exercise.description}")
            if exercise.equipment_needed:
                print("   Requiere equipo: Sí")
            else:
                print("   Requiere equipo: No") 