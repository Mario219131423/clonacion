class Rule:
    def __init__(self, conditions, conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

class RuleBase:
    def __init__(self):
        self.rules = self._initialize_rules()

    def _initialize_rules(self):
        return [
            # Reglas para Principiantes - Fuerza
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'fuerza',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'abdominales', 'zancadas']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'fuerza',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'press_banca', 'remo', 'extensiones', 'dominadas']}
            ),
            
            # Reglas para Principiantes - Resistencia
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'resistencia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'resistencia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'press_banca', 'remo', 'extensiones', 'burpees']}
            ),
            
            # Reglas para Principiantes - Hipertrofia
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'hipertrofia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'abdominales', 'zancadas', 'burpees']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'hipertrofia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'dominadas', 'curl_biceps']}
            ),
            
            # Reglas para Principiantes - Pérdida de peso
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'pérdida de peso',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees', 'saltos']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'principiante',
                    'goal': 'pérdida de peso',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'burpees', 'saltos', 'dominadas']}
            ),
            
            # Reglas para Intermedios - Fuerza
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'fuerza',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'dominadas', 'abdominales', 'zancadas', 'burpees']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'fuerza',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'peso_muerto', 'remo', 'dominadas', 'extensiones', 'curl_biceps']}
            ),
            
            # Reglas para Intermedios - Resistencia
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'resistencia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees', 'saltos', 'dominadas']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'resistencia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'dominadas', 'burpees', 'saltos', 'curl_biceps']}
            ),
            
            # Reglas para Intermedios - Hipertrofia
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'hipertrofia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'dominadas', 'abdominales', 'zancadas', 'burpees', 'saltos']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'hipertrofia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'peso_muerto', 'remo', 'dominadas', 'extensiones', 'curl_biceps', 'prensa']}
            ),
            
            # Reglas para Intermedios - Pérdida de peso
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'pérdida de peso',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees', 'saltos', 'dominadas', 'mountain_climbers']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'intermedio',
                    'goal': 'pérdida de peso',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'dominadas', 'burpees', 'saltos', 'curl_biceps', 'mountain_climbers']}
            ),
            
            # Reglas para Avanzados - Fuerza
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'fuerza',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'dominadas', 'abdominales', 'zancadas', 'burpees', 'saltos', 'mountain_climbers', 'handstand_pushups']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'fuerza',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'peso_muerto', 'remo', 'dominadas', 'extensiones', 'curl_biceps', 'prensa', 'military_press', 'clean']}
            ),
            
            # Reglas para Avanzados - Resistencia
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'resistencia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees', 'saltos', 'dominadas', 'mountain_climbers', 'handstand_pushups', 'muscle_ups']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'resistencia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'dominadas', 'burpees', 'saltos', 'curl_biceps', 'mountain_climbers', 'military_press', 'clean']}
            ),
            
            # Reglas para Avanzados - Hipertrofia
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'hipertrofia',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'dominadas', 'abdominales', 'zancadas', 'burpees', 'saltos', 'mountain_climbers', 'handstand_pushups', 'muscle_ups']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'hipertrofia',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'peso_muerto', 'remo', 'dominadas', 'extensiones', 'curl_biceps', 'prensa', 'military_press', 'clean', 'snatch']}
            ),
            
            # Reglas para Avanzados - Pérdida de peso
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'pérdida de peso',
                    'equipment_available': False
                },
                conclusion={'recommended_exercises': ['flexiones', 'sentadillas', 'plancha', 'zancadas', 'abdominales', 'burpees', 'saltos', 'dominadas', 'mountain_climbers', 'handstand_pushups', 'muscle_ups', 'box_jumps']}
            ),
            Rule(
                conditions={
                    'fitness_level': 'avanzado',
                    'goal': 'pérdida de peso',
                    'equipment_available': True
                },
                conclusion={'recommended_exercises': ['press_banca', 'sentadillas', 'remo', 'extensiones', 'dominadas', 'burpees', 'saltos', 'curl_biceps', 'mountain_climbers', 'military_press', 'clean', 'box_jumps']}
            ),
            
            # Reglas específicas por grupo muscular - Principiantes
            Rule(
                conditions={
                    'preferred_muscle_groups': ['pecho'],
                    'fitness_level': 'principiante'
                },
                conclusion={'recommended_exercises': ['flexiones', 'press_banca', 'plancha']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['espalda'],
                    'fitness_level': 'principiante'
                },
                conclusion={'recommended_exercises': ['remo', 'dominadas', 'plancha']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['piernas'],
                    'fitness_level': 'principiante'
                },
                conclusion={'recommended_exercises': ['sentadillas', 'zancadas', 'burpees']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['core'],
                    'fitness_level': 'principiante'
                },
                conclusion={'recommended_exercises': ['plancha', 'abdominales', 'mountain_climbers']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['brazos'],
                    'fitness_level': 'principiante'
                },
                conclusion={'recommended_exercises': ['flexiones', 'extensiones', 'curl_biceps']}
            ),
            
            # Reglas específicas por grupo muscular - Intermedios
            Rule(
                conditions={
                    'preferred_muscle_groups': ['pecho'],
                    'fitness_level': 'intermedio'
                },
                conclusion={'recommended_exercises': ['flexiones', 'press_banca', 'plancha', 'dominadas']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['espalda'],
                    'fitness_level': 'intermedio'
                },
                conclusion={'recommended_exercises': ['remo', 'dominadas', 'peso_muerto', 'plancha']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['piernas'],
                    'fitness_level': 'intermedio'
                },
                conclusion={'recommended_exercises': ['sentadillas', 'zancadas', 'burpees', 'prensa']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['core'],
                    'fitness_level': 'intermedio'
                },
                conclusion={'recommended_exercises': ['plancha', 'abdominales', 'mountain_climbers', 'handstand_pushups']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['brazos'],
                    'fitness_level': 'intermedio'
                },
                conclusion={'recommended_exercises': ['flexiones', 'extensiones', 'curl_biceps', 'dominadas']}
            ),
            
            # Reglas específicas por grupo muscular - Avanzados
            Rule(
                conditions={
                    'preferred_muscle_groups': ['pecho'],
                    'fitness_level': 'avanzado'
                },
                conclusion={'recommended_exercises': ['flexiones', 'press_banca', 'plancha', 'dominadas', 'handstand_pushups']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['espalda'],
                    'fitness_level': 'avanzado'
                },
                conclusion={'recommended_exercises': ['remo', 'dominadas', 'peso_muerto', 'plancha', 'muscle_ups']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['piernas'],
                    'fitness_level': 'avanzado'
                },
                conclusion={'recommended_exercises': ['sentadillas', 'zancadas', 'burpees', 'prensa', 'clean', 'snatch']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['core'],
                    'fitness_level': 'avanzado'
                },
                conclusion={'recommended_exercises': ['plancha', 'abdominales', 'mountain_climbers', 'handstand_pushups', 'muscle_ups']}
            ),
            Rule(
                conditions={
                    'preferred_muscle_groups': ['brazos'],
                    'fitness_level': 'avanzado'
                },
                conclusion={'recommended_exercises': ['flexiones', 'extensiones', 'curl_biceps', 'dominadas', 'muscle_ups']}
            )
        ]

    def get_matching_rules(self, facts):
        matching_rules = []
        for rule in self.rules:
            if all(facts.get(condition) == value for condition, value in rule.conditions.items()):
                matching_rules.append(rule)
        return matching_rules 