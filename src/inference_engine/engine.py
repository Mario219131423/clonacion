class InferenceEngine:
    def __init__(self, rule_base, exercise_db):
        self.rule_base = rule_base
        self.exercise_db = exercise_db
        self.dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
        import logging
        self.logger = logging.getLogger(__name__)

    def _extraer_numero(self, texto):
        """Extrae el primer número de un texto."""
        import re
        match = re.search(r'\d+', texto)
        return int(match.group()) if match else 0

    def _variar_series_repeticiones(self, ejercicio, dia_semana, nivel):
        """Varía las series y repeticiones según el día y nivel."""
        try:
            series_base = self._extraer_numero(ejercicio.series_recomendadas)
            repeticiones_base = self._extraer_numero(ejercicio.repeticiones_recomendadas)
            
            # Variación según el día de la semana
            if dia_semana in ['lunes', 'miercoles', 'viernes']:
                # Días de alta intensidad
                if nivel == 'principiante':
                    return f"{series_base} series", f"{repeticiones_base-2}-{repeticiones_base} repeticiones"
                elif nivel == 'intermedio':
                    return f"{series_base+1} series", f"{repeticiones_base-3}-{repeticiones_base} repeticiones"
                else:  # avanzado
                    return f"{series_base+2} series", f"{repeticiones_base-4}-{repeticiones_base} repeticiones"
            else:
                # Días de volumen
                if nivel == 'principiante':
                    return f"{series_base} series", f"{repeticiones_base}-{repeticiones_base+2} repeticiones"
                elif nivel == 'intermedio':
                    return f"{series_base+1} series", f"{repeticiones_base}-{repeticiones_base+3} repeticiones"
                else:  # avanzado
                    return f"{series_base+2} series", f"{repeticiones_base}-{repeticiones_base+4} repeticiones"
        except Exception as e:
            self.logger.error(f"Error en _variar_series_repeticiones: {str(e)}")
            return "3 series", "10-12 repeticiones"  # Valores por defecto

    def _variar_descanso(self, ejercicio, dia_semana, nivel):
        """Varía el tiempo de descanso según el día y nivel."""
        try:
            descanso_base = self._extraer_numero(ejercicio.descanso_recomendado)
            
            # Variación según el día de la semana
            if dia_semana in ['lunes', 'miercoles', 'viernes']:
                # Días de alta intensidad - menos descanso
                if nivel == 'principiante':
                    return f"{descanso_base-15} segundos"
                elif nivel == 'intermedio':
                    return f"{descanso_base-30} segundos"
                else:  # avanzado
                    return f"{descanso_base-45} segundos"
            else:
                # Días de volumen - más descanso
                if nivel == 'principiante':
                    return f"{descanso_base+15} segundos"
                elif nivel == 'intermedio':
                    return f"{descanso_base+30} segundos"
                else:  # avanzado
                    return f"{descanso_base+45} segundos"
        except Exception as e:
            self.logger.error(f"Error en _variar_descanso: {str(e)}")
            return "60 segundos"  # Valor por defecto

    def _distribuir_grupos_musculares(self, dias_entrenamiento, grupos_musculares):
        """Distribuye los grupos musculares entre los días disponibles."""
        try:
            import random
            from collections import defaultdict
            
            # Crear un diccionario para rastrear qué grupos musculares se han usado
            grupos_usados = defaultdict(int)
            
            # Distribuir grupos musculares entre los días
            distribucion = {}
            for dia in dias_entrenamiento:
                # Seleccionar grupos musculares para este día
                grupos_dia = []
                for grupo in grupos_musculares:
                    if grupos_usados[grupo] < 2:  # No usar el mismo grupo más de 2 veces por semana
                        grupos_dia.append(grupo)
                        grupos_usados[grupo] += 1
                
                # Si no hay suficientes grupos, agregar algunos aleatorios
                while len(grupos_dia) < 2:
                    grupo_extra = random.choice(grupos_musculares)
                    if grupos_usados[grupo_extra] < 2:
                        grupos_dia.append(grupo_extra)
                        grupos_usados[grupo_extra] += 1
                
                distribucion[dia] = grupos_dia
            
            return distribucion
        except Exception as e:
            self.logger.error(f"Error en _distribuir_grupos_musculares: {str(e)}")
            return {dia: grupos_musculares[:2] for dia in dias_entrenamiento}

    def get_recommendations(self, user_facts):
        """
        Obtiene recomendaciones basadas en los hechos del usuario.
        """
        try:
            self.logger.info("Iniciando generación de recomendaciones")
            
            # Validar datos de entrada
            if not user_facts.get('fitness_level') or not user_facts.get('goal'):
                self.logger.error("Faltan datos requeridos: fitness_level o goal")
                return {
                    'error': 'Faltan datos requeridos. Por favor, complete todos los campos.'
                }
            
            # Obtener reglas que coinciden con los hechos del usuario
            self.logger.info("Buscando reglas coincidentes...")
            matching_rules = self.rule_base.get_matching_rules(user_facts)
            
            if not matching_rules:
                self.logger.warning("No se encontraron reglas coincidentes")
                return {
                    'error': 'No se encontraron rutinas que coincidan con tus preferencias. Por favor, ajusta tus criterios.'
                }
            
            self.logger.info(f"Reglas encontradas: {len(matching_rules)}")
            
            # Obtener ejercicios recomendados de las reglas
            self.logger.info("Obteniendo ejercicios recomendados...")
            recommended_exercises = []
            for rule in matching_rules:
                exercise_names = rule.conclusion.get('recommended_exercises', [])
                for name in exercise_names:
                    exercise = self.exercise_db.get_exercise(name)
                    if exercise:
                        # Filtrar por disponibilidad de equipo
                        if not exercise.requiere_equipo or user_facts.get('equipment_available', False):
                            # Filtrar por grupos musculares preferidos
                            if not user_facts.get('preferred_muscle_groups') or \
                               exercise.grupo_muscular in user_facts['preferred_muscle_groups']:
                                recommended_exercises.append(exercise)
            
            self.logger.info(f"Ejercicios recomendados encontrados: {len(recommended_exercises)}")
            
            if not recommended_exercises:
                self.logger.warning("No se encontraron ejercicios recomendados")
                return {
                    'error': 'No se encontraron ejercicios que coincidan con tus preferencias. Por favor, ajusta tus criterios.'
                }
            
            # Generar rutina semanal
            dias_entrenamiento = user_facts.get('dias_entrenamiento', [])
            if not dias_entrenamiento:
                dias_entrenamiento = ['lunes', 'miercoles', 'viernes']  # Default para principiantes
            
            self.logger.info(f"Días de entrenamiento: {dias_entrenamiento}")
            
            # Distribuir grupos musculares entre los días
            self.logger.info("Distribuyendo grupos musculares...")
            distribucion_grupos = self._distribuir_grupos_musculares(
                dias_entrenamiento,
                user_facts.get('preferred_muscle_groups', [])
            )
            
            rutina_semanal = {}
            for dia in dias_entrenamiento:
                self.logger.info(f"Generando rutina para {dia}")
                
                # Determinar ejercicios para el día
                ejercicios_dia = self._seleccionar_ejercicios_dia(
                    recommended_exercises,
                    user_facts,
                    dia,
                    distribucion_grupos[dia]
                )
                
                if not ejercicios_dia:
                    self.logger.warning(f"No se encontraron ejercicios para {dia}")
                    continue
                
                # Calcular duración total del día
                duracion_total = 0
                rutina_dia = []
                
                for ejercicio in ejercicios_dia:
                    try:
                        # Variar series, repeticiones y descanso según el día y nivel
                        series, repeticiones = self._variar_series_repeticiones(
                            ejercicio, dia, user_facts['fitness_level']
                        )
                        descanso = self._variar_descanso(
                            ejercicio, dia, user_facts['fitness_level']
                        )
                        
                        # Calcular duración
                        series_num = self._extraer_numero(series)
                        repeticiones_num = self._extraer_numero(repeticiones)
                        descanso_num = self._extraer_numero(descanso)
                        
                        # Tiempo por serie (30 segundos por repetición + descanso)
                        tiempo_por_serie = (30 * repeticiones_num) + descanso_num
                        duracion_total += series_num * tiempo_por_serie
                        
                        rutina_dia.append({
                            'nombre': ejercicio.nombre,
                            'grupo_muscular': ejercicio.grupo_muscular,
                            'dificultad': ejercicio.dificultad,
                            'series': series,
                            'repeticiones': repeticiones,
                            'descanso': descanso,
                            'instrucciones': ejercicio.instrucciones,
                            'duracion_aproximada': self._formatear_duracion(series_num * tiempo_por_serie)
                        })
                    except Exception as e:
                        self.logger.error(f"Error procesando ejercicio {ejercicio.nombre}: {str(e)}")
                        continue
                
                if rutina_dia:  # Solo agregar el día si tiene ejercicios
                    rutina_semanal[dia] = {
                        'ejercicios': rutina_dia,
                        'duracion_total': duracion_total,
                        'duracion_formateada': self._formatear_duracion(duracion_total)
                    }
            
            if not rutina_semanal:
                self.logger.warning("No se pudo generar ninguna rutina")
                return {
                    'error': 'No se pudo generar una rutina con los criterios seleccionados. Por favor, intenta con diferentes opciones.'
                }
            
            self.logger.info("Rutina generada exitosamente")
            
            return {
                'rutina_semanal': rutina_semanal,
                'nivel': user_facts['fitness_level'],
                'objetivo': user_facts['goal'],
                'grupos_musculares': user_facts.get('preferred_muscle_groups', []),
                'requiere_equipo': user_facts.get('equipment_available', False),
                'dias_entrenamiento': dias_entrenamiento,
                'recomendaciones': self._generar_recomendaciones(user_facts)
            }
        except Exception as e:
            self.logger.error(f"Error general en get_recommendations: {str(e)}")
            return {
                'error': 'Ocurrió un error al generar la rutina. Por favor, intente nuevamente.'
            }
    
    def _calcular_duracion_entrenamiento(self, user_facts):
        """Calcula la duración recomendada del entrenamiento basada en el nivel y objetivo."""
        nivel = user_facts['fitness_level']
        objetivo = user_facts['goal']
        
        if nivel == 'principiante':
            if objetivo in ['fuerza', 'hipertrofia']:
                return 45  # 45 minutos
            else:
                return 30  # 30 minutos
        elif nivel == 'intermedio':
            if objetivo in ['fuerza', 'hipertrofia']:
                return 60  # 60 minutos
            else:
                return 45  # 45 minutos
        else:  # avanzado
            if objetivo in ['fuerza', 'hipertrofia']:
                return 90  # 90 minutos
            else:
                return 60  # 60 minutos
    
    def _seleccionar_ejercicios_dia(self, ejercicios, user_facts, dia, grupos_dia):
        """Selecciona los ejercicios para un día específico basado en el nivel, objetivo y grupos musculares."""
        try:
            nivel = user_facts['fitness_level']
            objetivo = user_facts['goal']
            
            # Determinar número de ejercicios por día
            if nivel == 'principiante':
                num_ejercicios = 4
            elif nivel == 'intermedio':
                num_ejercicios = 5
            else:  # avanzado
                num_ejercicios = 6
            
            # Filtrar ejercicios por grupos musculares del día
            ejercicios_filtrados = [
                ej for ej in ejercicios
                if ej.grupo_muscular in grupos_dia
            ]
            
            # Si no hay suficientes ejercicios para los grupos del día, agregar algunos de otros grupos
            if len(ejercicios_filtrados) < num_ejercicios:
                ejercicios_extra = [
                    ej for ej in ejercicios
                    if ej.grupo_muscular not in grupos_dia
                ]
                ejercicios_filtrados.extend(ejercicios_extra)
            
            # Seleccionar ejercicios basados en el objetivo y día
            if dia in ['lunes', 'miercoles', 'viernes']:
                # Días de alta intensidad
                if objetivo == 'fuerza':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'avanzado', reverse=True)
                elif objetivo == 'resistencia':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'principiante')
                elif objetivo == 'hipertrofia':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'intermedio', reverse=True)
                else:  # pérdida de peso
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'principiante')
            else:
                # Días de volumen
                if objetivo == 'fuerza':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'intermedio')
                elif objetivo == 'resistencia':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'principiante', reverse=True)
                elif objetivo == 'hipertrofia':
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'avanzado')
                else:  # pérdida de peso
                    ejercicios_filtrados = sorted(ejercicios_filtrados, key=lambda x: x.dificultad == 'intermedio')
            
            # Mezclar los ejercicios para evitar patrones predecibles
            import random
            random.shuffle(ejercicios_filtrados)
            
            return ejercicios_filtrados[:num_ejercicios]
        except Exception as e:
            self.logger.error(f"Error en _seleccionar_ejercicios_dia: {str(e)}")
            return ejercicios[:4]  # Retornar primeros 4 ejercicios en caso de error
    
    def _formatear_duracion(self, segundos):
        """Formatea la duración en segundos a un formato legible."""
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        
        if minutos == 0:
            return f"{segundos_restantes} segundos"
        elif segundos_restantes == 0:
            return f"{minutos} minutos"
        else:
            return f"{minutos} minutos y {segundos_restantes} segundos"
    
    def _generar_recomendaciones(self, user_facts):
        """Genera recomendaciones personalizadas basadas en los datos del usuario."""
        recomendaciones = []
        
        # Recomendaciones basadas en el nivel
        if user_facts['fitness_level'] == 'principiante':
            recomendaciones.append("Comienza con pesos ligeros y enfócate en la técnica correcta.")
            recomendaciones.append("Descansa 2-3 minutos entre series para permitir una recuperación adecuada.")
        elif user_facts['fitness_level'] == 'intermedio':
            recomendaciones.append("Varía la intensidad de tus entrenamientos para evitar estancamientos.")
            recomendaciones.append("Considera implementar técnicas avanzadas como superseries o dropsets.")
        else:
            recomendaciones.append("Implementa periodización en tu entrenamiento para maximizar resultados.")
            recomendaciones.append("Considera trabajar con un entrenador para perfeccionar tu técnica.")
        
        # Recomendaciones basadas en el objetivo
        if user_facts['goal'] == 'fuerza':
            recomendaciones.append("Mantén las repeticiones bajas (3-6) y los pesos altos.")
            recomendaciones.append("Asegúrate de calentar adecuadamente antes de cada sesión.")
        elif user_facts['goal'] == 'resistencia':
            recomendaciones.append("Mantén las repeticiones altas (12-15) y los descansos cortos.")
            recomendaciones.append("Incluye ejercicios cardiovasculares en tu rutina.")
        elif user_facts['goal'] == 'hipertrofia':
            recomendaciones.append("Mantén las repeticiones en el rango de 8-12 para maximizar el crecimiento muscular.")
            recomendaciones.append("Asegúrate de consumir suficientes proteínas y calorías.")
        else:  # pérdida de peso
            recomendaciones.append("Combina entrenamiento de fuerza con cardio para maximizar la quema de calorías.")
            recomendaciones.append("Mantén un déficit calórico moderado y asegúrate de consumir suficientes proteínas.")
        
        # Recomendaciones basadas en condiciones médicas
        if user_facts.get('condiciones_medicas'):
            recomendaciones.append("Consulta con un profesional de la salud antes de comenzar cualquier rutina de ejercicio.")
            recomendaciones.append("Modifica los ejercicios según sea necesario para adaptarlos a tus condiciones.")
        
        return recomendaciones 