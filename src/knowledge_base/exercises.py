class Exercise:
    def __init__(self, nombre, grupo_muscular, dificultad, requiere_equipo, descripcion, 
                 instrucciones=None, video_url=None, imagen_url=None, variaciones=None,
                 musculos_secundarios=None, series_recomendadas=None, repeticiones_recomendadas=None,
                 descanso_recomendado=None):
        self.nombre = nombre
        self.grupo_muscular = grupo_muscular
        self.dificultad = dificultad  # 'principiante', 'intermedio', 'avanzado'
        self.requiere_equipo = requiere_equipo
        self.descripcion = descripcion
        self.instrucciones = instrucciones
        self.video_url = video_url
        self.imagen_url = imagen_url
        self.variaciones = variaciones
        self.musculos_secundarios = musculos_secundarios
        self.series_recomendadas = series_recomendadas
        self.repeticiones_recomendadas = repeticiones_recomendadas
        self.descanso_recomendado = descanso_recomendado

class ExerciseDatabase:
    def __init__(self):
        self.exercises = self._initialize_exercises()
        self.custom_exercises = {}  # Almacena ejercicios personalizados

    def _initialize_exercises(self):
        return {
            # Ejercicios para Principiantes
            'flexiones': Exercise(
                nombre='Flexiones',
                grupo_muscular='pecho',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio básico para fortalecer el pecho, hombros y tríceps.',
                instrucciones='Colócate en posición de plancha con las manos separadas al ancho de los hombros. Baja el cuerpo hasta que el pecho casi toque el suelo y luego empuja hacia arriba.',
                series_recomendadas='3',
                repeticiones_recomendadas='10-12',
                descanso_recomendado='60 segundos'
            ),
            'sentadillas': Exercise(
                nombre='Sentadillas',
                grupo_muscular='piernas',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio fundamental para fortalecer las piernas y glúteos.',
                instrucciones='Párate con los pies separados al ancho de los hombros. Baja el cuerpo como si te sentaras en una silla, manteniendo la espalda recta.',
                series_recomendadas='3',
                repeticiones_recomendadas='12-15',
                descanso_recomendado='60 segundos'
            ),
            'plancha': Exercise(
                nombre='Plancha',
                grupo_muscular='core',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio isométrico para fortalecer el core y mejorar la estabilidad.',
                instrucciones='Apoya los antebrazos y las puntas de los pies en el suelo, manteniendo el cuerpo en línea recta.',
                series_recomendadas='3',
                repeticiones_recomendadas='30 segundos',
                descanso_recomendado='45 segundos'
            ),
            'dominadas': Exercise(
                nombre='Dominadas',
                grupo_muscular='espalda',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio para desarrollar la espalda y bíceps.',
                instrucciones='Cuelga de una barra con las manos separadas al ancho de los hombros. Tira del cuerpo hacia arriba hasta que la barbilla pase la barra.',
                series_recomendadas='3',
                repeticiones_recomendadas='8-10',
                descanso_recomendado='90 segundos'
            ),
            'peso_muerto': Exercise(
                nombre='Peso Muerto',
                grupo_muscular='espalda',
                dificultad='avanzado',
                requiere_equipo=True,
                descripcion='Ejercicio compuesto para desarrollar la espalda, glúteos y piernas.',
                instrucciones='Párate con los pies separados al ancho de los hombros. Agarra la barra con las manos separadas al ancho de los hombros. Levanta la barra manteniendo la espalda recta.',
                series_recomendadas='4',
                repeticiones_recomendadas='6-8',
                descanso_recomendado='120 segundos'
            ),
            'press_banca': Exercise(
                nombre='Press de Banca',
                grupo_muscular='pecho',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio clásico para desarrollar el pecho y tríceps.',
                instrucciones='Acuéstate en un banco plano. Agarra la barra con las manos separadas al ancho de los hombros. Baja la barra al pecho y luego empuja hacia arriba.',
                series_recomendadas='4',
                repeticiones_recomendadas='8-10',
                descanso_recomendado='90 segundos'
            ),
            'zancadas': Exercise(
                nombre='Zancadas',
                grupo_muscular='piernas',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio para fortalecer las piernas y mejorar el equilibrio.',
                instrucciones='Da un paso hacia adelante y baja el cuerpo hasta que ambas rodillas formen ángulos de 90 grados.',
                series_recomendadas='3',
                repeticiones_recomendadas='12-15 por pierna',
                descanso_recomendado='60 segundos'
            ),
            'abdominales': Exercise(
                nombre='Abdominales',
                grupo_muscular='core',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio básico para fortalecer los músculos abdominales.',
                instrucciones='Acuéstate boca arriba con las rodillas flexionadas. Coloca las manos detrás de la cabeza y levanta el torso hacia las rodillas.',
                series_recomendadas='3',
                repeticiones_recomendadas='15-20',
                descanso_recomendado='45 segundos'
            ),
            'remo': Exercise(
                nombre='Remo con Barra',
                grupo_muscular='espalda',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio para desarrollar la espalda y bíceps.',
                instrucciones='Inclina el torso hacia adelante, agarra la barra y tira hacia el pecho.',
                series_recomendadas='4',
                repeticiones_recomendadas='10-12',
                descanso_recomendado='90 segundos'
            ),
            'extensiones': Exercise(
                nombre='Extensiones de Tríceps',
                grupo_muscular='brazos',
                dificultad='principiante',
                requiere_equipo=True,
                descripcion='Ejercicio para aislar y fortalecer los tríceps.',
                instrucciones='Sujeta una mancuerna con ambas manos detrás de la cabeza. Extiende los brazos hacia arriba.',
                series_recomendadas='3',
                repeticiones_recomendadas='12-15',
                descanso_recomendado='60 segundos'
            ),
            'burpees': Exercise(
                nombre='Burpees',
                grupo_muscular='full body',
                dificultad='intermedio',
                requiere_equipo=False,
                descripcion='Ejercicio completo que combina fuerza y cardio.',
                instrucciones='Comienza en posición de pie, baja a sentadilla, coloca las manos en el suelo, salta los pies hacia atrás, haz una flexión, salta los pies hacia adelante y salta hacia arriba.',
                series_recomendadas='3',
                repeticiones_recomendadas='10-12',
                descanso_recomendado='60 segundos'
            ),
            'saltos': Exercise(
                nombre='Saltos',
                grupo_muscular='piernas',
                dificultad='principiante',
                requiere_equipo=False,
                descripcion='Ejercicio cardiovascular para mejorar la potencia de las piernas.',
                instrucciones='Salta verticalmente lo más alto posible, aterrizando suavemente.',
                series_recomendadas='3',
                repeticiones_recomendadas='15-20',
                descanso_recomendado='45 segundos'
            ),
            'mountain_climbers': Exercise(
                nombre='Mountain Climbers',
                grupo_muscular='core',
                dificultad='intermedio',
                requiere_equipo=False,
                descripcion='Ejercicio dinámico para el core y cardio.',
                instrucciones='En posición de plancha, alterna llevando las rodillas al pecho.',
                series_recomendadas='3',
                repeticiones_recomendadas='30 segundos',
                descanso_recomendado='45 segundos'
            ),
            'handstand_pushups': Exercise(
                nombre='Flexiones en Pino',
                grupo_muscular='hombros',
                dificultad='avanzado',
                requiere_equipo=False,
                descripcion='Ejercicio avanzado para hombros y tríceps.',
                instrucciones='Apoya las manos en el suelo y eleva las piernas contra la pared. Realiza flexiones en esta posición.',
                series_recomendadas='3',
                repeticiones_recomendadas='5-8',
                descanso_recomendado='90 segundos'
            ),
            'muscle_ups': Exercise(
                nombre='Muscle Ups',
                grupo_muscular='espalda',
                dificultad='avanzado',
                requiere_equipo=True,
                descripcion='Ejercicio avanzado que combina dominadas y fondos.',
                instrucciones='Realiza una dominada explosiva y continúa el movimiento para pasar por encima de la barra.',
                series_recomendadas='3',
                repeticiones_recomendadas='3-5',
                descanso_recomendado='120 segundos'
            ),
            'box_jumps': Exercise(
                nombre='Saltos al Cajón',
                grupo_muscular='piernas',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio pliométrico para mejorar la potencia de las piernas.',
                instrucciones='Salta sobre un cajón o plataforma elevada, aterrizando suavemente.',
                series_recomendadas='3',
                repeticiones_recomendadas='10-12',
                descanso_recomendado='60 segundos'
            ),
            'curl_biceps': Exercise(
                nombre='Curl de Bíceps',
                grupo_muscular='brazos',
                dificultad='principiante',
                requiere_equipo=True,
                descripcion='Ejercicio para aislar y desarrollar los bíceps.',
                instrucciones='Sujeta una mancuerna con la palma hacia arriba y levanta el peso flexionando el codo.',
                series_recomendadas='3',
                repeticiones_recomendadas='12-15',
                descanso_recomendado='60 segundos'
            ),
            'prensa': Exercise(
                nombre='Prensa de Piernas',
                grupo_muscular='piernas',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio para desarrollar la fuerza de las piernas.',
                instrucciones='Siéntate en la máquina y empuja la plataforma con las piernas.',
                series_recomendadas='4',
                repeticiones_recomendadas='10-12',
                descanso_recomendado='90 segundos'
            ),
            'military_press': Exercise(
                nombre='Press Militar',
                grupo_muscular='hombros',
                dificultad='intermedio',
                requiere_equipo=True,
                descripcion='Ejercicio para desarrollar los hombros.',
                instrucciones='De pie, levanta la barra desde los hombros hasta arriba de la cabeza.',
                series_recomendadas='4',
                repeticiones_recomendadas='8-10',
                descanso_recomendado='90 segundos'
            ),
            'clean': Exercise(
                nombre='Clean',
                grupo_muscular='full body',
                dificultad='avanzado',
                requiere_equipo=True,
                descripcion='Ejercicio olímpico para desarrollar potencia y coordinación.',
                instrucciones='Levanta la barra desde el suelo hasta los hombros en un movimiento explosivo.',
                series_recomendadas='4',
                repeticiones_recomendadas='5-6',
                descanso_recomendado='120 segundos'
            ),
            'snatch': Exercise(
                nombre='Snatch',
                grupo_muscular='full body',
                dificultad='avanzado',
                requiere_equipo=True,
                descripcion='Ejercicio olímpico para desarrollar potencia y coordinación.',
                instrucciones='Levanta la barra desde el suelo hasta arriba de la cabeza en un movimiento explosivo.',
                series_recomendadas='4',
                repeticiones_recomendadas='3-5',
                descanso_recomendado='120 segundos'
            )
        }

    def get_exercise(self, nombre):
        """Obtiene un ejercicio por su nombre, buscando tanto en ejercicios predefinidos como personalizados."""
        # Primero buscar en ejercicios personalizados
        if nombre.lower() in self.custom_exercises:
            return self.custom_exercises[nombre.lower()]
        # Si no se encuentra, buscar en ejercicios predefinidos
        return self.exercises.get(nombre.lower())

    def get_exercises_by_muscle_group(self, grupo_muscular):
        """Obtiene todos los ejercicios de un grupo muscular específico."""
        ejercicios = []
        # Buscar en ejercicios predefinidos
        ejercicios.extend([ex for ex in self.exercises.values() if ex.grupo_muscular == grupo_muscular])
        # Buscar en ejercicios personalizados
        ejercicios.extend([ex for ex in self.custom_exercises.values() if ex.grupo_muscular == grupo_muscular])
        return ejercicios

    def get_exercises_by_difficulty(self, dificultad):
        """Obtiene todos los ejercicios de una dificultad específica."""
        ejercicios = []
        # Buscar en ejercicios predefinidos
        ejercicios.extend([ex for ex in self.exercises.values() if ex.dificultad == dificultad])
        # Buscar en ejercicios personalizados
        ejercicios.extend([ex for ex in self.custom_exercises.values() if ex.dificultad == dificultad])
        return ejercicios
        
    def add_exercise(self, exercise):
        """Agrega un nuevo ejercicio a la base de conocimiento."""
        self.custom_exercises[exercise.nombre.lower()] = exercise
        # También agregar a la base de datos si es necesario
        if hasattr(self, 'db'):
            self.db.session.add(exercise)
            self.db.session.commit()

    def get_all_exercises(self):
        """Obtiene todos los ejercicios disponibles."""
        ejercicios = list(self.exercises.values())
        ejercicios.extend(list(self.custom_exercises.values()))
        return ejercicios 