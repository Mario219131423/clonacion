"""
Definiciones de rutinas de entrenamiento detalladas para el sistema experto.
Cada rutina contiene días, ejercicios e instrucciones específicas.
"""

# Definir rutinas detalladas para cada tipo de entrenamiento
rutinas_detalladas = {
    # RUTINAS DE FUERZA
    "Rutina de Fuerza Máxima": {
        "descripcion": "Rutina enfocada en desarrollar la máxima fuerza con pesos pesados y bajas repeticiones.",
        "dias": [
            {
                "nombre": "Día 1: Piernas",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 5, "repeticiones": "3-5", "instrucciones": "Peso máximo que puedas manejar con buena técnica."},
                    {"nombre": "Peso muerto", "series": 5, "repeticiones": "3-5", "instrucciones": "Mantén la espalda recta, empuja con los talones."},
                    {"nombre": "Prensa de piernas", "series": 3, "repeticiones": "6-8", "instrucciones": "Complementario, usa un peso desafiante."}
                ],
                "notas": "Descanso de 3-5 minutos entre series. Enfócate en la técnica perfecta."
            },
            {
                "nombre": "Día 2: Pecho y Tríceps",
                "ejercicios": [
                    {"nombre": "Press de banca", "series": 5, "repeticiones": "3-5", "instrucciones": "Usa un peso que sea desafiante pero que permita buena técnica."},
                    {"nombre": "Press inclinado", "series": 4, "repeticiones": "4-6", "instrucciones": "Mantén los hombros hacia atrás."},
                    {"nombre": "Fondos", "series": 3, "repeticiones": "6-8", "instrucciones": "Añade peso si puedes hacer más de 8 repeticiones."}
                ],
                "notas": "Descanso de 3 minutos entre series."
            },
            {
                "nombre": "Día 3: Espalda y Bíceps",
                "ejercicios": [
                    {"nombre": "Dominadas lastradas", "series": 5, "repeticiones": "3-5", "instrucciones": "Añade peso para alcanzar el rango de repeticiones objetivo."},
                    {"nombre": "Remo con barra", "series": 4, "repeticiones": "4-6", "instrucciones": "Mantén la espalda recta, lleva la barra al abdomen."},
                    {"nombre": "Curl de bíceps", "series": 3, "repeticiones": "6-8", "instrucciones": "Usa un peso que permita mantener buena técnica."}
                ],
                "notas": "Descanso de 3 minutos entre series."
            }
        ]
    },
    
    "Rutina de Fuerza Explosiva": {
        "descripcion": "Rutina que combina fuerza y velocidad para desarrollar potencia explosiva.",
        "dias": [
            {
                "nombre": "Día 1: Potencia de Piernas",
                "ejercicios": [
                    {"nombre": "Saltos con carga", "series": 4, "repeticiones": "5", "instrucciones": "Máxima explosividad en cada repetición."},
                    {"nombre": "Sentadilla con salto", "series": 4, "repeticiones": "6", "instrucciones": "Extensión completa, aterriza suavemente."},
                    {"nombre": "Arrancadas", "series": 4, "repeticiones": "3-4", "instrucciones": "Técnica perfecta, velocidad en la fase de tracción."}
                ],
                "notas": "Descanso de 2-3 minutos entre series. La velocidad de ejecución es clave."
            },
            {
                "nombre": "Día 2: Potencia de Empuje",
                "ejercicios": [
                    {"nombre": "Press banca explosivo", "series": 4, "repeticiones": "4-5", "instrucciones": "70% de 1RM, máxima velocidad en la fase concéntrica."},
                    {"nombre": "Lanzamiento de balón medicinal", "series": 4, "repeticiones": "6", "instrucciones": "Lanzamiento explosivo desde el pecho."},
                    {"nombre": "Fondos pliométricos", "series": 3, "repeticiones": "5", "instrucciones": "Empuja con fuerza para separar las manos del soporte."}
                ],
                "notas": "Descanso de 2 minutos entre series. Calidad sobre cantidad."
            },
            {
                "nombre": "Día 3: Potencia de Tracción",
                "ejercicios": [
                    {"nombre": "Dominadas explosivas", "series": 4, "repeticiones": "4-6", "instrucciones": "Sube lo más rápido posible, baja controladamente."},
                    {"nombre": "Remo con mancuerna explosivo", "series": 4, "repeticiones": "6", "instrucciones": "Fase concéntrica explosiva, excéntrica controlada."},
                    {"nombre": "Cargada de potencia", "series": 4, "repeticiones": "3-4", "instrucciones": "Enfócate en la velocidad de la segunda tracción."}
                ],
                "notas": "Descanso completo entre series para mantener la calidad."
            }
        ]
    },
    
    # RUTINAS DE RESISTENCIA
    "Rutina de Resistencia Circuitos": {
        "descripcion": "Rutina basada en circuitos que combina ejercicios cardiovasculares y de fuerza para mejorar la resistencia global.",
        "dias": [
            {
                "nombre": "Día 1: Circuito de Cuerpo Completo",
                "ejercicios": [
                    {"nombre": "Burpees", "series": 3, "repeticiones": "12-15", "instrucciones": "Realiza el movimiento completo con salto y flexión."},
                    {"nombre": "Mountain Climbers", "series": 3, "repeticiones": "30 segundos", "instrucciones": "Mantiene ritmo constante y core estabilizado."},
                    {"nombre": "Sentadillas con salto", "series": 3, "repeticiones": "15", "instrucciones": "Busca altura en el salto, aterriza suavemente."},
                    {"nombre": "Flexiones", "series": 3, "repeticiones": "12-15", "instrucciones": "Mantiene el cuerpo alineado durante todo el movimiento."},
                    {"nombre": "Jumping Jacks", "series": 3, "repeticiones": "30 segundos", "instrucciones": "Realiza el movimiento explosivamente."}
                ],
                "notas": "Realiza los ejercicios en circuito sin descanso entre ellos. Descansa 1-2 minutos entre series de circuito completas."
            },
            {
                "nombre": "Día 2: Circuito HIIT",
                "ejercicios": [
                    {"nombre": "Sprint en el sitio", "series": 4, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Máxima intensidad durante el trabajo."},
                    {"nombre": "Saltos al cajón", "series": 4, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Altura moderada, enfocado en rapidez."},
                    {"nombre": "Escaladores", "series": 4, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Mantiene las caderas bajas y estables."},
                    {"nombre": "Saltos laterales", "series": 4, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Salta de lado a lado con rapidez y control."},
                    {"nombre": "Planchas con toques", "series": 4, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Alterna tocar hombro derecho e izquierdo."}
                ],
                "notas": "Completa cada intervalo a máxima intensidad posible. Descansa 2 minutos entre cada serie completa del circuito."
            },
            {
                "nombre": "Día 3: Circuito de Resistencia Muscular",
                "ejercicios": [
                    {"nombre": "Zancadas alternas", "series": 3, "repeticiones": "20 (10 por pierna)", "instrucciones": "Mantiene el torso erguido durante todo el movimiento."},
                    {"nombre": "Remo con mancuernas", "series": 3, "repeticiones": "15", "instrucciones": "Peso moderado, contracción completa."},
                    {"nombre": "Press de hombros", "series": 3, "repeticiones": "15", "instrucciones": "Peso ligero, mantiene buena técnica."},
                    {"nombre": "Elevación de cadera", "series": 3, "repeticiones": "20", "instrucciones": "Extiende completamente las caderas en cada repetición."},
                    {"nombre": "Superman", "series": 3, "repeticiones": "15", "instrucciones": "Mantiene la posición elevada 2 segundos."}
                ],
                "notas": "Realizar los ejercicios en formato circuito con 30 segundos de descanso entre ejercicios y 1-2 minutos entre circuitos completos."
            },
            {
                "nombre": "Día 4: Circuito Cardío-Core",
                "ejercicios": [
                    {"nombre": "Saltos de comba", "series": 3, "repeticiones": "45 segundos", "instrucciones": "Mantiene ritmo constante."},
                    {"nombre": "Crunch bicicleta", "series": 3, "repeticiones": "20 (10 por lado)", "instrucciones": "Toca codo con rodilla opuesta."},
                    {"nombre": "Step-ups", "series": 3, "repeticiones": "20 (10 por pierna)", "instrucciones": "Alterna piernas, usa un banco o plataforma estable."},
                    {"nombre": "Plancha lateral", "series": 3, "repeticiones": "30 segundos por lado", "instrucciones": "Mantiene cadera elevada y cuerpo alineado."},
                    {"nombre": "Skipping", "series": 3, "repeticiones": "45 segundos", "instrucciones": "Rodillas altas, movimiento rápido."}
                ],
                "notas": "Realiza los ejercicios en circuito, con 30-45 segundos de descanso entre ejercicios si es necesario. Completa 3 circuitos en total."
            }
        ]
    },
    
    # RUTINAS DE HIPERTROFIA
    "Rutina de Hipertrofia Volumen": {
        "descripcion": "Rutina enfocada en maximizar el volumen de entrenamiento para estimular el crecimiento muscular.",
        "dias": [
            {
                "nombre": "Día 1: Pecho y Bíceps",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 4, "repeticiones": "10-12", "instrucciones": "Control total del movimiento, 2 segundos de fase excéntrica."},
                    {"nombre": "Press Inclinado con Mancuernas", "series": 4, "repeticiones": "10-12", "instrucciones": "Baja hasta sentir estiramiento en el pecho."},
                    {"nombre": "Aperturas en Polea", "series": 3, "repeticiones": "12-15", "instrucciones": "Enfoca la tensión en los pectorales durante todo el movimiento."},
                    {"nombre": "Curl de Bíceps con Barra", "series": 4, "repeticiones": "10-12", "instrucciones": "Evita balancear el cuerpo, movimiento controlado."},
                    {"nombre": "Curl Martillo", "series": 3, "repeticiones": "12-15", "instrucciones": "Alterna brazos, mantiene codos pegados al cuerpo."}
                ],
                "notas": "Descanso de 60-90 segundos entre series. Enfoca la mente-músculo y la conexión neuromuscular."
            },
            {
                "nombre": "Día 2: Piernas",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "10-12", "instrucciones": "Profundidad completa, rodillas alineadas con pies."},
                    {"nombre": "Prensa de Piernas", "series": 4, "repeticiones": "12-15", "instrucciones": "Varias posiciones de pies para trabajar diferentes ángulos."},
                    {"nombre": "Extensiones de Cuadriceps", "series": 3, "repeticiones": "15-20", "instrucciones": "Contrae completamente en la parte superior, desciende lentamente."},
                    {"nombre": "Curl Femoral Acostado", "series": 4, "repeticiones": "12-15", "instrucciones": "Enfoca la tensión en los isquiotibiales."},
                    {"nombre": "Elevación de Pantorrillas", "series": 4, "repeticiones": "15-20", "instrucciones": "Estiramiento completo en la parte inferior."}
                ],
                "notas": "Descanso de 90-120 segundos entre series de ejercicios compuestos, 60 segundos para aislamiento."
            },
            {
                "nombre": "Día 3: Espalda y Tríceps",
                "ejercicios": [
                    {"nombre": "Dominadas o Jalones al Pecho", "series": 4, "repeticiones": "10-12", "instrucciones": "Amplitud completa, enfoca la contracción de la espalda."},
                    {"nombre": "Remo con Barra", "series": 4, "repeticiones": "10-12", "instrucciones": "Mantiene espalda recta, lleva la barra al abdomen."},
                    {"nombre": "Remo en Máquina", "series": 3, "repeticiones": "12-15", "instrucciones": "Contrae la espalda al final del movimiento."},
                    {"nombre": "Extensiones de Tríceps con Polea", "series": 4, "repeticiones": "12-15", "instrucciones": "Codos fijos, solo mueve antebrazos."},
                    {"nombre": "Press Francés con Mancuerna", "series": 3, "repeticiones": "12-15", "instrucciones": "Desciende hasta estirar completamente el tríceps."}
                ],
                "notas": "Descanso de 60-90 segundos entre series. Usa una variedad de agarres para estimular diferentes partes de los músculos."
            },
            {
                "nombre": "Día 4: Hombros y Abdominales",
                "ejercicios": [
                    {"nombre": "Press Militar", "series": 4, "repeticiones": "10-12", "instrucciones": "Mantiene core estable, evita arquear la espalda."},
                    {"nombre": "Elevaciones Laterales", "series": 4, "repeticiones": "12-15", "instrucciones": "Codos ligeramente flexionados, mueve solo los brazos."},
                    {"nombre": "Pájaro/Elevaciones Posteriores", "series": 3, "repeticiones": "12-15", "instrucciones": "Inclina ligeramente el torso hacia adelante."},
                    {"nombre": "Crunch en Máquina", "series": 4, "repeticiones": "15-20", "instrucciones": "Contrae abdominales al máximo en cada repetición."},
                    {"nombre": "Elevación de Piernas Colgando", "series": 3, "repeticiones": "15-20", "instrucciones": "Evita el balanceo, usa abdominales para elevar piernas."}
                ],
                "notas": "Descanso de 60 segundos entre series. Para desarrollo completo de hombros, asegúrate de trabajar todas las cabezas del deltoides."
            }
        ]
    },

    # RUTINAS DE PÉRDIDA DE PESO
    "Rutina de Pérdida de Peso HIIT": {
        "descripcion": "Rutina de alta intensidad diseñada para maximizar el gasto calórico y el efecto EPOC (quema de calorías post-entrenamiento).",
        "dias": [
            {
                "nombre": "Día 1: HIIT Tren Inferior",
                "ejercicios": [
                    {"nombre": "Sentadillas con Salto", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Explota hacia arriba, aterriza suavemente flexionando rodillas."},
                    {"nombre": "Zancadas Alternas", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Mantiene ritmo rápido, pasos amplios."},
                    {"nombre": "Escaladores", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Ritmo rápido, abdomen contraído."},
                    {"nombre": "Burpees", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Movimiento completo: flexion, salto y palmada arriba."},
                    {"nombre": "Skipping Alto", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Rodillas a la altura de la cadera, ritmo rápido."}
                ],
                "notas": "Completa 5 rondas del circuito con 1-2 minutos de descanso entre rondas. Bebe agua entre rondas para mantener la hidratación."
            },
            {
                "nombre": "Día 2: HIIT Tren Superior + Core",
                "ejercicios": [
                    {"nombre": "Flexiones Explosivas", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Explota hacia arriba en cada repetición."},
                    {"nombre": "Remo con Mancuerna", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Alterna brazos rápidamente, mantiene espalda recta."},
                    {"nombre": "Mountain Climbers Cruzados", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Lleva rodilla al codo opuesto, ritmo rápido."},
                    {"nombre": "Planchas con Toques al Hombro", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Mantén caderas estables mientras alternas toques."},
                    {"nombre": "Burpees sin Flexiones", "series": 5, "repeticiones": "30s trabajo/20s descanso", "instrucciones": "Mantiene ritmo constante durante todo el intervalo."}
                ],
                "notas": "Mantiene alta intensidad durante los intervalos de trabajo. Registra tiempos/repeticiones y trata de superarlos en cada sesión."
            },
            {
                "nombre": "Día 3: HIIT de Cuerpo Completo",
                "ejercicios": [
                    {"nombre": "Sprints", "series": 8, "repeticiones": "20s sprint/40s caminar", "instrucciones": "Máxima intensidad durante los 20 segundos de sprint."},
                    {"nombre": "Jumping Jacks", "series": 8, "repeticiones": "20s trabajo/40s descanso", "instrucciones": "Movimientos amplios y rápidos."},
                    {"nombre": "Sentadilla a Press de Hombros", "series": 8, "repeticiones": "20s trabajo/40s descanso", "instrucciones": "Usa mancuernas ligeras, movimiento fluido."},
                    {"nombre": "Saltos Laterales", "series": 8, "repeticiones": "20s trabajo/40s descanso", "instrucciones": "Salta de lado a lado a máxima velocidad."},
                    {"nombre": "Plancha", "series": 8, "repeticiones": "20s trabajo/40s descanso", "instrucciones": "Mantiene posición correcta, abdomen contraído."}
                ],
                "notas": "Este es un protocolo tabata modificado. Completa 2 rondas de Tabata por ejercicio antes de pasar al siguiente."
            }
        ]
    },
    
    # RUTINAS DE MANTENIMIENTO
    "Rutina de Mantenimiento Equilibrio": {
        "descripcion": "Rutina de entrenamiento equilibrada que mantiene los niveles actuales de fuerza, resistencia y composición corporal.",
        "dias": [
            {
                "nombre": "Día 1: Fuerza de Cuerpo Completo",
                "ejercicios": [
                    {"nombre": "Sentadilla con Barra", "series": 3, "repeticiones": "8-10", "instrucciones": "Peso moderado que permita buena técnica."},
                    {"nombre": "Press de Banca", "series": 3, "repeticiones": "8-10", "instrucciones": "Mantiene escapúla retraída durante todo el movimiento."},
                    {"nombre": "Remo con Barra", "series": 3, "repeticiones": "8-10", "instrucciones": "Espalda recta, contrae escapúla al final del movimiento."},
                    {"nombre": "Press Militar", "series": 3, "repeticiones": "8-10", "instrucciones": "Evita arquear la zona lumbar."},
                    {"nombre": "Zancadas", "series": 2, "repeticiones": "10 por pierna", "instrucciones": "Mantiene torso erguido, paso amplio."}
                ],
                "notas": "Descanso de 1-2 minutos entre series. El objetivo es mantener la fuerza, no necesariamente aumentarla."
            },
            {
                "nombre": "Día 2: Cardio Moderado + Core",
                "ejercicios": [
                    {"nombre": "Cardio (Correr/Eliptica/Bicicleta)", "series": 1, "repeticiones": "20-30 minutos", "instrucciones": "Intensidad moderada, 65-75% de FC máxima."},
                    {"nombre": "Plancha Frontal", "series": 3, "repeticiones": "30-45 segundos", "instrucciones": "Mantiene posición neutra de columna."},
                    {"nombre": "Plancha Lateral", "series": 3, "repeticiones": "30 segundos por lado", "instrucciones": "Mantén cadera elevada, cuerpo alineado."},
                    {"nombre": "Crunch Abdominal", "series": 3, "repeticiones": "15-20", "instrucciones": "Contrae abdominales al elevar hombros del suelo."},
                    {"nombre": "Bird-Dog", "series": 2, "repeticiones": "10 por lado", "instrucciones": "Extiende extremidades opuestas, mantiene estabilidad."}
                ],
                "notas": "Enfoca en la calidad de los movimientos y la estabilidad central. Cardio de intensidad moderada para mantener resistencia cardiovascular."
            },
            {
                "nombre": "Día 3: Entrenamiento por Intervalos",
                "ejercicios": [
                    {"nombre": "Calentamiento Cardio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Ritmo suave para elevar temperatura corporal."},
                    {"nombre": "Intervalos (30s intenso/90s suave)", "series": 6, "repeticiones": "2 minutos cada uno", "instrucciones": "Alterna entre 85-90% y 60% de intensidad."},
                    {"nombre": "Circuito de Fuerza (cualquier máquina)", "series": 2, "repeticiones": "12-15 por ejercicio", "instrucciones": "Elige 4-5 ejercicios, realiza circuito completo 2 veces."},
                    {"nombre": "Estiramientos Dinámicos", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Movilidad de todas las articulaciones principales."}
                ],
                "notas": "Este entrenamiento combina ejercicio cardiovascular y muscular en una sola sesión. Ideal para mantener niveles generales de fitness."
            },
            {
                "nombre": "Día 4: Flexibilidad y Recuperación Activa",
                "ejercicios": [
                    {"nombre": "Yoga o Estiramientos", "series": 1, "repeticiones": "20-30 minutos", "instrucciones": "Mantiene cada posición 30-60 segundos, respiración profunda."},
                    {"nombre": "Foam Rolling", "series": 1, "repeticiones": "10-15 minutos", "instrucciones": "Trabaja puntos de tensión en principales grupos musculares."},
                    {"nombre": "Caminata Ligera", "series": 1, "repeticiones": "15-20 minutos", "instrucciones": "Ritmo tranquilo para aumentar circulación sin fatiga."},
                    {"nombre": "Movilidad Articular", "series": 2, "repeticiones": "8-10 por movimiento", "instrucciones": "Movimientos circulares de todas las articulaciones."}
                ],
                "notas": "La recuperación activa es fundamental para mantener un buen rendimiento a largo plazo. No subestimes su importancia en tu programa."
            }
        ]
    },
    
    # Continuación de RUTINAS DE FUERZA
    "Rutina de Fuerza Funcional": {
        "descripcion": "Rutina que enfatiza movimientos funcionales y patrones de movimiento naturales para mejorar la fuerza aplicable a la vida diaria.",
        "dias": [
            {
                "nombre": "Día 1: Empuje Funcional",
                "ejercicios": [
                    {"nombre": "Turkish Get-Up", "series": 3, "repeticiones": "5 por lado", "instrucciones": "Movimiento completo, mantiene control total y mirada en la pesa."},
                    {"nombre": "Press de Hombros con Kettlebell", "series": 4, "repeticiones": "8 por lado", "instrucciones": "Una mano a la vez, mantiene core estabilizado."},
                    {"nombre": "Flexiones con Rotación", "series": 3, "repeticiones": "8 por lado", "instrucciones": "Rota al final de cada flexión, alterna lados."},
                    {"nombre": "Elevación Frontal y Lateral", "series": 3, "repeticiones": "10 de cada una", "instrucciones": "Alterna entre elevación frontal y lateral, movimiento controlado."},
                    {"nombre": "Plancha con Soporte de Peso", "series": 3, "repeticiones": "30 segundos", "instrucciones": "Coloca peso en la espalda, mantiene posición estable."}
                ],
                "notas": "Enfoca en la calidad del movimiento, no en la carga. La estabilidad es clave en todos los ejercicios funcionales."
            },
            {
                "nombre": "Día 2: Tracción Funcional",
                "ejercicios": [
                    {"nombre": "Peso Muerto Unilateral", "series": 4, "repeticiones": "8 por lado", "instrucciones": "Mantiene espalda recta, cadera como bisagra, pierna libre extendida."},
                    {"nombre": "Remo con Rotación", "series": 3, "repeticiones": "8 por lado", "instrucciones": "Remo seguido de rotación de torso, estabilidad en la posición."},
                    {"nombre": "Face Pull con Cuerda", "series": 3, "repeticiones": "12-15", "instrucciones": "Lleva codos altos, retrae escapúla al final del movimiento."},
                    {"nombre": "Escalador en TRX", "series": 3, "repeticiones": "10 por lado", "instrucciones": "Mantiene cadera estable mientras alterna rodillas al pecho."},
                    {"nombre": "Superman", "series": 3, "repeticiones": "12", "instrucciones": "Eleva brazos y piernas simultáneamente, sostiene 2 segundos."}
                ],
                "notas": "Estos ejercicios trabajan la cadena posterior y los estabilizadores, fundamentales para el movimiento funcional."
            },
            {
                "nombre": "Día 3: Lower Body y Core Funcional",
                "ejercicios": [
                    {"nombre": "Sentadilla Goblet", "series": 4, "repeticiones": "10-12", "instrucciones": "Sostiene kettlebell o mancuerna a la altura del pecho, profundidad completa."},
                    {"nombre": "Step-Up con Press", "series": 3, "repeticiones": "8 por lado", "instrucciones": "Paso completo a plataforma, press al estar arriba, controla el descenso."},
                    {"nombre": "Puente de Cadera Unilateral", "series": 3, "repeticiones": "10 por lado", "instrucciones": "Extiende una pierna, eleva completamente la cadera, aprieta glúteos."},
                    {"nombre": "Plancha con Arrastre", "series": 3, "repeticiones": "45 segundos", "instrucciones": "En posición de plancha, arrastra peso con una mano alternándolas."},
                    {"nombre": "Mountain Climber", "series": 3, "repeticiones": "20 por lado", "instrucciones": "Ritmo moderado, mantiene cadera baja y core contraído."}
                ],
                "notas": "Enfatiza la estabilidad central durante todos los movimientos de piernas. La conexión core-extremidades es esencial para la fuerza funcional."
            }
        ]
    },
    
    # Continuación de RUTINAS DE HIPERTROFIA
    "Rutina de Hipertrofia Intensidad": {
        "descripcion": "Rutina de alta intensidad con técnicas avanzadas para estimular máximo crecimiento muscular.",
        "dias": [
            {
                "nombre": "Día 1: Pecho/Hombros - Técnicas de Intensidad",
                "ejercicios": [
                    {"nombre": "Press de Banca + Drop Set", "series": 4, "repeticiones": "8 + drop set", "instrucciones": "Al fallar, reduce 30% del peso y continúa hasta fallar nuevamente."},
                    {"nombre": "Press Inclinado - Rest-Pause", "series": 3, "repeticiones": "8-6-4", "instrucciones": "Haz 8 reps, descansa 15 segundos, 6 reps, descansa 15 segundos, 4 reps."},
                    {"nombre": "Cruces en Polea - Series Gigantes", "series": 3, "repeticiones": "12 en 3 posiciones", "instrucciones": "12 reps arriba, media y baja sin descanso entre posiciones."},
                    {"nombre": "Press Militar - 1.5 reps", "series": 4, "repeticiones": "8 (cada rep: abajo-mitad-arriba)", "instrucciones": "Baja completamente, sube a la mitad, baja, sube completamente = 1 repetición."},
                    {"nombre": "Elevaciones Laterales - Parciales", "series": 3, "repeticiones": "12 + 8 parciales", "instrucciones": "12 reps completas + 8 parciales en la parte alta del movimiento."}
                ],
                "notas": "Muy alta intensidad, asegúrate de calentar adecuadamente. Usa peso que permita completar técnicas de intensidad con buena forma."
            },
            {
                "nombre": "Día 2: Piernas - Supersets",
                "ejercicios": [
                    {"nombre": "A1: Sentadilla", "series": 4, "repeticiones": "10", "instrucciones": "Sin lock-out en la parte superior, mantiene tensión constante."},
                    {"nombre": "A2: Extensiones de Cuádriceps", "series": 4, "repeticiones": "15", "instrucciones": "Inmediatamente después de sentadillas, mantiene pico de contracción."},
                    {"nombre": "B1: Peso Muerto Rumano", "series": 4, "repeticiones": "10", "instrucciones": "Desciende controladamente, siente estiramiento en isquiotibiales."},
                    {"nombre": "B2: Curl Femoral", "series": 4, "repeticiones": "15", "instrucciones": "Inmediatamente después de peso muerto, contracción completa."},
                    {"nombre": "C: Prensa 21s", "series": 3, "repeticiones": "21 (7+7+7)", "instrucciones": "7 reps en rango inferior, 7 en rango medio, 7 en rango completo."}
                ],
                "notas": "Utiliza supersets para maximizar la intensidad. 60-90 segundos de descanso entre supersets completos."
            },
            {
                "nombre": "Día 3: Espalda/Bíceps - Tempo Negativo",
                "ejercicios": [
                    {"nombre": "Dominadas Asistidas Negativas", "series": 4, "repeticiones": "6-8", "instrucciones": "Uses asistencia para subir, 4-5 segundos en la fase de descenso."},
                    {"nombre": "Remo T Barra Tempo 4010", "series": 4, "repeticiones": "8", "instrucciones": "4s fase excéntrica, 0s pausa inferior, 1s concéntrica, 0s arriba."},
                    {"nombre": "Pullover con Mancuerna", "series": 3, "repeticiones": "10", "instrucciones": "Mantiene brazos ligeramente flexionados, enfoca en la latísimos."},
                    {"nombre": "Curl Predicador 21s", "series": 3, "repeticiones": "21 (7+7+7)", "instrucciones": "7 reps mitad inferior, 7 mitad superior, 7 rango completo."},
                    {"nombre": "Curl de Bíceps en Polea Negativas", "series": 3, "repeticiones": "8", "instrucciones": "Usa dos brazos para subir, uno para bajar controladamente (4s)."}
                ],
                "notas": "El trabajo negativo (excéntrico) causa mayor micro-daño muscular que favorece la hipertrofia. Requiere mayor recuperación."
            },
            {
                "nombre": "Día 4: Tríceps/Hombros/Abdominales - FST-7",
                "ejercicios": [
                    {"nombre": "Extensión de Tríceps FST-7", "series": 7, "repeticiones": "10-12", "instrucciones": "7 series con 30 segundos de descanso, enfoca en la contracción."},
                    {"nombre": "Skull Crushers", "series": 4, "repeticiones": "8-10", "instrucciones": "Lleva barra a la frente, mantiene codos fijos apuntando al techo."},
                    {"nombre": "Elevaciones Laterales Parciales", "series": 4, "repeticiones": "15-20", "instrucciones": "Movimiento parcial en la parte superior del rango, bombeo constante."},
                    {"nombre": "Crunch con Resistencia", "series": 3, "repeticiones": "15", "instrucciones": "Añade resistencia con disco o mancuerna en el pecho."},
                    {"nombre": "Elevación de Piernas Colgando", "series": 3, "repeticiones": "fallo", "instrucciones": "Lleva las piernas hasta la horizontal, contrae abdominales activamente."}
                ],
                "notas": "La técnica FST-7 (Fascia Stretch Training) busca expandir la fascia muscular a través de bombeo y congestión muscular para permitir mayor crecimiento."
            }
        ]
    },
    
    # RUTINAS DE FUERZA ADICIONALES
    "Rutina de Fuerza-Resistencia": {
        "descripcion": "Rutina que combina elementos de fuerza y resistencia muscular, ideal para desarrollar resistencia a la fatiga con cargas moderadas-altas.",
        "dias": [
            {
                "nombre": "Día 1: Tren Superior - Fuerza-Resistencia",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 4, "repeticiones": "12-15", "instrucciones": "70% de 1RM, sin llegar al fallo muscular."},
                    {"nombre": "Remo con Barra", "series": 4, "repeticiones": "12-15", "instrucciones": "Mantiene la espalda recta, contracción completa."},
                    {"nombre": "Press Militar", "series": 3, "repeticiones": "12-15", "instrucciones": "Evita arquear la espalda, movimiento controlado."},
                    {"nombre": "Jalon al Pecho", "series": 3, "repeticiones": "12-15", "instrucciones": "Lleva la barra hasta el pecho, extensión completa arriba."},
                    {"nombre": "Fondos en Paralelas", "series": 3, "repeticiones": "Máximas posibles", "instrucciones": "Realiza todas las que puedas con buena técnica."}
                ],
                "notas": "Descanso de 60-90 segundos entre series. Mantén la técnica impecable en todas las repeticiones."
            },
            {
                "nombre": "Día 2: Tren Inferior - Fuerza-Resistencia",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "15-20", "instrucciones": "65% de 1RM, profundidad completa si la movilidad lo permite."},
                    {"nombre": "Peso Muerto Rumano", "series": 4, "repeticiones": "12-15", "instrucciones": "Enfoca la tensión en isquiotibiales, espalda neutra."},
                    {"nombre": "Prensa de Piernas", "series": 3, "repeticiones": "15-20", "instrucciones": "Control en la fase excéntrica, no bloquees rodillas."},
                    {"nombre": "Extensiones de Cuádriceps", "series": 3, "repeticiones": "15-20", "instrucciones": "Contracción completa en cada repetición."},
                    {"nombre": "Elevación de Talones", "series": 4, "repeticiones": "20-25", "instrucciones": "Estiramiento completo y contracción máxima."}
                ],
                "notas": "Descanso de 90 segundos entre series. La clave es completar todas las repeticiones con buena técnica."
            },
            {
                "nombre": "Día 3: Circuito de Fuerza-Resistencia",
                "ejercicios": [
                    {"nombre": "Dominadas", "series": 4, "repeticiones": "Máximas posibles", "instrucciones": "Si no puedes hacer más de 8, usa banda elástica."},
                    {"nombre": "Flexiones", "series": 4, "repeticiones": "Máximas posibles", "instrucciones": "Mantén el cuerpo alineado, pecho al suelo."},
                    {"nombre": "Sentadilla con Peso Corporal", "series": 4, "repeticiones": "20-25", "instrucciones": "Mantén rodillas alineadas con los pies."},
                    {"nombre": "Remo Invertido en TRX/Barras", "series": 4, "repeticiones": "15-20", "instrucciones": "Mantén el cuerpo rígido, tíralo desde los codos."},
                    {"nombre": "Plancha", "series": 4, "repeticiones": "45-60 segundos", "instrucciones": "Mantén alineación perfecta, abdomen contraido."}
                ],
                "notas": "Realiza este circuito con mínimo descanso entre ejercicios (30s) y 2 minutos entre vueltas completas al circuito."
            }
        ]
    },

    "Rutina de Fuerza Compuesta": {
        "descripcion": "Rutina basada en ejercicios compuestos multi-articulares para desarrollar fuerza general y funcional en todo el cuerpo.",
        "dias": [
            {
                "nombre": "Día 1: Empuje Compuesto",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 5, "repeticiones": "5", "instrucciones": "85% de 1RM, concentración total en la técnica."},
                    {"nombre": "Press Militar", "series": 5, "repeticiones": "5", "instrucciones": "Mantiene el core estable, no arquees la espalda."},
                    {"nombre": "Dips/Fondos Lastrados", "series": 4, "repeticiones": "6-8", "instrucciones": "Añade peso si puedes hacer más de 8 rep."},
                    {"nombre": "Press Inclinado con Mancuernas", "series": 3, "repeticiones": "8-10", "instrucciones": "Desciende hasta sentir estiramiento en el pecho."},
                    {"nombre": "Elevaciones Laterales", "series": 3, "repeticiones": "10-12", "instrucciones": "Mantiene ligera flexión en los codos."}
                ],
                "notas": "Descanso de 2-3 minutos entre series de ejercicios principales, 90 segundos para accesorios."
            },
            {
                "nombre": "Día 2: Tracción Compuesta",
                "ejercicios": [
                    {"nombre": "Peso Muerto", "series": 5, "repeticiones": "5", "instrucciones": "85% de 1RM, mantiene espalda recta, empuja con los talones."},
                    {"nombre": "Dominadas Lastradas", "series": 5, "repeticiones": "5", "instrucciones": "Añade peso para alcanzar el rango de 5 repeticiones."},
                    {"nombre": "Remo Pendlay", "series": 4, "repeticiones": "6-8", "instrucciones": "Desde el suelo en cada rep, espalda paralela al piso."},
                    {"nombre": "Remo en T", "series": 3, "repeticiones": "8-10", "instrucciones": "Lleva los codos lo más atrás posible, contrae la espalda."},
                    {"nombre": "Curl de Bíceps", "series": 3, "repeticiones": "10-12", "instrucciones": "No balancees el cuerpo, mantiene los codos fijos."}
                ],
                "notas": "Descanso completo entre series de pesos pesados. El peso muerto es un ejercicio técnicamente exigente, prioriza la forma correcta."
            },
            {
                "nombre": "Día 3: Piernas Compuesto",
                "ejercicios": [
                    {"nombre": "Sentadilla Trasera", "series": 5, "repeticiones": "5", "instrucciones": "85% de 1RM, mantiene espalda recta, rodillas en línea con pies."},
                    {"nombre": "Hip Thrust con Barra", "series": 4, "repeticiones": "6-8", "instrucciones": "Extiende completamente las caderas, aprieta glúteos en la parte superior."},
                    {"nombre": "Zancadas con Mancuernas", "series": 3, "repeticiones": "8-10 por pierna", "instrucciones": "Paso largo, rodilla trasera cerca del suelo."},
                    {"nombre": "Prensa de Piernas", "series": 3, "repeticiones": "10-12", "instrucciones": "Rango completo de movimiento, sin bloquear rodillas."},
                    {"nombre": "Extensiones de Cuádriceps", "series": 3, "repeticiones": "12-15", "instrucciones": "Contracción máxima en la parte superior."}
                ],
                "notas": "Enfoca en mantener el core estable en todos los ejercicios. Descanso completo entre series pesadas."
            }
        ]
    },
        
    # Continuación de RUTINAS DE RESISTENCIA
    "Rutina de Resistencia Muscular": {
        "descripcion": "Rutina diseñada para mejorar la resistencia muscular local y la capacidad de trabajo repetido con cargas moderadas.",
        "dias": [
            {
                "nombre": "Día 1: Superior - Series Largas",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 3, "repeticiones": "15-20", "instrucciones": "Peso moderado, mantiene ritmo constante sin pausas."},
                    {"nombre": "Remo en Máquina", "series": 3, "repeticiones": "15-20", "instrucciones": "Contracción completa en cada repetición, ritmo controlado."},
                    {"nombre": "Curl de Bíceps Alternado", "series": 3, "repeticiones": "15 por brazo", "instrucciones": "Alterna brazos sin descanso entre ellos."},
                    {"nombre": "Press Francés", "series": 3, "repeticiones": "15-20", "instrucciones": "Estira completamente el tríceps en cada repetición."},
                    {"nombre": "Elevaciones Laterales", "series": 3, "repeticiones": "20", "instrucciones": "Peso ligero, enfoca en la contracción del deltoides medio."}
                ],
                "notas": "Descanso de 60 segundos entre series. El objetivo es mantener buena técnica incluso al acercarse a la fatiga."
            },
            {
                "nombre": "Día 2: Piernas - Resistencia Local",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "20", "instrucciones": "Peso moderado, mantiene profundidad constante en todas las repeticiones."},
                    {"nombre": "Estocadas Caminando", "series": 3, "repeticiones": "30 pasos totales", "instrucciones": "15 por pierna, mantiene torso erguido y da pasos amplios."},
                    {"nombre": "Peso Muerto Rumano", "series": 3, "repeticiones": "15-20", "instrucciones": "Peso moderado, enfoca en el estiramiento posterior."},
                    {"nombre": "Elevación de Pantorrillas", "series": 4, "repeticiones": "25", "instrucciones": "Completa extensión en la parte superior, estiramiento en la inferior."},
                    {"nombre": "Step-Ups", "series": 3, "repeticiones": "15 por pierna", "instrucciones": "Altura moderada, extiende completamente la pierna al subir."}
                ],
                "notas": "Descanso de 90 segundos entre series. La acumulación de ácido láctico es esperada, entrena para tolerar la sensación de quema muscular."
            },
            {
                "nombre": "Día 3: Método Tabata",
                "ejercicios": [
                    {"nombre": "Flexiones", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Máximas repeticiones posibles en cada intervalo de 20s."},
                    {"nombre": "Sentadilla Corporal", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Máximas repeticiones con buena técnica en cada intervalo."},
                    {"nombre": "Remo Invertido TRX", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Ajusta el ángulo según tu nivel, mantiene el cuerpo recto."},
                    {"nombre": "Burpees Modificados", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Versión adaptada enfocada en completar más repeticiones."}
                ],
                "notas": "Completa los 8 intervalos (4 minutos) para un ejercicio antes de pasar al siguiente. Descansa 1 minuto entre ejercicios."
            },
            {
                "nombre": "Día 4: Circuito de Resistencia Total",
                "ejercicios": [
                    {"nombre": "Remo con Mancuerna", "series": 4, "repeticiones": "15", "instrucciones": "Alterna brazos sin descanso entre repeticiones."},
                    {"nombre": "Zancadas Alternas", "series": 4, "repeticiones": "20 total", "instrucciones": "Alterna piernas, 10 por cada una."},
                    {"nombre": "Press de Hombros con Mancuernas", "series": 4, "repeticiones": "15", "instrucciones": "Peso ligero a moderado, técnica perfecta."},
                    {"nombre": "Peso Muerto con Mancuernas", "series": 4, "repeticiones": "15", "instrucciones": "Cadera como bisagra, espalda recta durante todo el movimiento."},
                    {"nombre": "Crunch Bicicleta", "series": 4, "repeticiones": "30 total", "instrucciones": "15 por cada lado, toca codo con rodilla opuesta."}
                ],
                "notas": "Realiza los ejercicios en circuito con descanso mínimo entre ellos. Descansa 2 minutos entre rondas completas. Mantiene la intensidad a través del circuito."
            }
        ]
    },
    
    # RUTINAS DE RESISTENCIA ADICIONALES
    "Rutina de Resistencia Cardiovascular": {
        "descripcion": "Rutina enfocada en mejorar la capacidad cardiovascular y el rendimiento aeróbico general.",
        "dias": [
            {
                "nombre": "Día 1: Carrera Continua",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Trote suave y movilidad articular."},
                    {"nombre": "Carrera continua", "series": 1, "repeticiones": "30-45 minutos", "instrucciones": "Ritmo moderado, 60-70% de FC máxima. Mantiene conversación posible."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Caminar y estiramientos suaves."}
                ],
                "notas": "Busca terreno variado si es posible. Mantén ritmo constante durante toda la sesión."
            },
            {
                "nombre": "Día 2: Ciclismo o Eliptica",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Pedaleo suave, aumentando gradualmente."},
                    {"nombre": "Ciclismo/Elíptica constante", "series": 1, "repeticiones": "40-50 minutos", "instrucciones": "Intensidad moderada, 65-75% FC máxima."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Disminuye gradualmente la intensidad."}
                ],
                "notas": "Mantén cadencia constante. Ajusta la resistencia para mantener el rango de frecuencia cardiaca objetivo."
            },
            {
                "nombre": "Día 3: Natación o Remo",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Nado suave o remo de baja intensidad."},
                    {"nombre": "Natación/Remo constante", "series": 1, "repeticiones": "25-30 minutos", "instrucciones": "Ritmo moderado, técnica correcta."},
                    {"nombre": "Técnica y habilidad", "series": 5, "repeticiones": "2 minutos", "instrucciones": "Enfoca en mejorar técnica, descansa 30 segundos entre series."}
                ],
                "notas": "Prioriza técnica sobre velocidad. La natación es excelente para desarrollo cardiovascular con bajo impacto."
            },
            {
                "nombre": "Día 4: Cross-Training",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Movilidad general y activación."},
                    {"nombre": "Cardio combinado", "series": 3, "repeticiones": "10 minutos", "instrucciones": "Alterna entre máquina de step, eliptica y remo, 10 min en cada una."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Estiramiento general y respiración."}
                ],
                "notas": "La variedad previene el aburrimiento y estimula diferentes patrones de movimiento."
            }
        ]
    },

    "Rutina de Resistencia Mixta": {
        "descripcion": "Rutina que combina resistencia cardiovascular y muscular para una mejora integral del sistema cardiorrespiratorio y muscular.",
        "dias": [
            {
                "nombre": "Día 1: Fuerza-Cardio",
                "ejercicios": [
                    {"nombre": "Sentadilla con Mancuerna", "series": 3, "repeticiones": "15-20", "instrucciones": "Mantiene espalda recta, peso moderado."},
                    {"nombre": "Cardio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Cinta o elíptica, intensidad moderada-alta."},
                    {"nombre": "Press de Banca", "series": 3, "repeticiones": "15-20", "instrucciones": "Peso moderado, técnica perfecta."},
                    {"nombre": "Cardio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Jump rope o mountain climbers, alta intensidad."},
                    {"nombre": "Remo con Mancuerna", "series": 3, "repeticiones": "15-20", "instrucciones": "Mantiene espalda recta, contracción completa."},
                    {"nombre": "Cardio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Bicicleta estática, intensidad alta."}
                ],
                "notas": "Alterna entre ejercicios de fuerza y cardio con mínimo descanso entre ellos. Descanso de 1 minuto entre cada par."
            },
            {
                "nombre": "Día 2: Cardio Largo + Core",
                "ejercicios": [
                    {"nombre": "Cardio continuo", "series": 1, "repeticiones": "30-40 minutos", "instrucciones": "Eliptica, cinta o ciclismo a intensidad moderada (65-75% FCM)."},
                    {"nombre": "Circuito de core", "series": 3, "repeticiones": "Circuito completo", "instrucciones": "Plancha (45s), Crunch (20 rep), Plancha lateral (30s cada lado), Russian twist (20 rep)."}
                ],
                "notas": "El entrenamiento de core al final ayuda a mejorar la resistencia de los músculos estabilizadores."
            },
            {
                "nombre": "Día 3: Circuito Mixto",
                "ejercicios": [
                    {"nombre": "Burpees", "series": 4, "repeticiones": "45s trabajo/15s descanso", "instrucciones": "Movimiento completo con flexión y salto."},
                    {"nombre": "Remo", "series": 4, "repeticiones": "45s trabajo/15s descanso", "instrucciones": "Remo intenso en máquina o con mancuernas."},
                    {"nombre": "Step-ups", "series": 4, "repeticiones": "45s trabajo/15s descanso", "instrucciones": "Alternando piernas, banco de altura media."},
                    {"nombre": "Push-press", "series": 4, "repeticiones": "45s trabajo/15s descanso", "instrucciones": "Con mancuernas o barra ligera, movimiento explosivo."}
                ],
                "notas": "Completa el circuito 4 veces con 1 minuto de descanso entre cada ronda completa. Mantiene intensidad alta durante intervalos de trabajo."
            },
            {
                "nombre": "Día 4: Escalera de Repeticiones",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio suave y movilidad general."},
                    {"nombre": "Complejo con barra ligera", "series": 5, "repeticiones": "Escalera 10-8-6-4-2", "instrucciones": "Complejo: Peso muerto + Remo + Clean + Press frontal + Squat"},
                    {"nombre": "Cardio", "series": 5, "repeticiones": "3 minutos", "instrucciones": "Cardio intenso entre cada serie del complejo."}
                ],
                "notas": "El número de repeticiones disminuye pero la intensidad/peso aumenta en cada serie. Completa todas las repeticiones de cada movimiento antes de pasar al siguiente."
            }
        ]
    },

    "Rutina de Resistencia Intervalos": {
        "descripcion": "Rutina basada en intervalos de alta intensidad seguidos de períodos de recuperación para mejorar la capacidad aeróbica y anaeróbica.",
        "dias": [
            {
                "nombre": "Día 1: Intervalos de Sprints",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Trote suave gradual y movilidad dinámica."},
                    {"nombre": "Intervalos cortos", "series": 8, "repeticiones": "30s sprint/90s recuperación", "instrucciones": "Sprint a máxima intensidad, recuperación caminando."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Caminar y estiramientos."}
                ],
                "notas": "Los intervalos deben ser a máxima intensidad. Si corres en cinta, ajusta velocidad previamente para evitar perdida de tiempo."
            },
            {
                "nombre": "Día 2: Intervalos Tabata",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio suave y movilidad general."},
                    {"nombre": "Tabata Jump Squats", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Sentadillas con salto, máxima intensidad."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación completa."},
                    {"nombre": "Tabata Mountain Climbers", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Ritmo máximo, mantiene posición correcta."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación completa."},
                    {"nombre": "Tabata Burpees", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Burpees a máxima velocidad posible."}
                ],
                "notas": "El protocolo Tabata es extremadamente intenso: 20s de esfuerzo máximo seguido de 10s de descanso, repetido 8 veces (4 minutos por ejercicio)."
            },
            {
                "nombre": "Día 3: Intervalos en Rampa",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio progresivo y movilidad dinámica."},
                    {"nombre": "Bloque 1", "series": 5, "repeticiones": "1 min trabajo/1 min descanso", "instrucciones": "Intensidad 80% de tu máximo."},
                    {"nombre": "Bloque 2", "series": 4, "repeticiones": "2 min trabajo/1 min descanso", "instrucciones": "Intensidad 75% de tu máximo."},
                    {"nombre": "Bloque 3", "series": 3, "repeticiones": "3 min trabajo/1 min descanso", "instrucciones": "Intensidad 70% de tu máximo."}
                ],
                "notas": "Puedes realizar estos intervalos en cualquier máquina de cardio: bicicleta, remo, elíptica o cinta de correr."
            },
            {
                "nombre": "Día 4: Piramidal",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "8-10 minutos", "instrucciones": "Cardio ligero y movilidad."},
                    {"nombre": "Piramidal ascendente", "series": 5, "repeticiones": "1-2-3-4-5 minutos", "instrucciones": "Intensidad moderada-alta, recuperación de 1 minuto entre series."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "3 minutos", "instrucciones": "Recuperación activa, caminar o muy suave."},
                    {"nombre": "Piramidal descendente", "series": 5, "repeticiones": "5-4-3-2-1 minutos", "instrucciones": "Aumenta intensidad a medida que disminuye duración, 1 minuto de descanso."}
                ],
                "notas": "La intensidad debe ser inversamente proporcional a la duración: intervalos más cortos a mayor intensidad."
            }
        ]
    },

    # RUTINAS DE HIPERTROFIA ADICIONALES
    "Rutina de Hipertrofia Frecuencia": {
        "descripcion": "Rutina de hipertrofia que divide el volumen en más sesiones semanales para estimular el crecimiento muscular mediante una mayor frecuencia de entrenamiento.",
        "dias": [
            {
                "nombre": "Día 1: Pecho/Espalda",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 4, "repeticiones": "8-10", "instrucciones": "Peso moderado-alto, enfoque en técnica perfecta."},
                    {"nombre": "Jalon al Pecho", "series": 4, "repeticiones": "8-10", "instrucciones": "Enfoca en la contracción de dorsales."},
                    {"nombre": "Press Inclinado con Mancuernas", "series": 3, "repeticiones": "10-12", "instrucciones": "Completo rango de movimiento."},
                    {"nombre": "Remo en Máquina", "series": 3, "repeticiones": "10-12", "instrucciones": "Contrae completamente la espalda al final del movimiento."},
                    {"nombre": "Cruces en Polea", "series": 2, "repeticiones": "12-15", "instrucciones": "Estiramiento completo y contracción máxima."}
                ],
                "notas": "Descanso de 60-90 segundos entre series. Volumen moderado por grupo muscular para permitir recuperación antes de la próxima sesión."
            },
            {
                "nombre": "Día 2: Piernas/Hombros",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "8-10", "instrucciones": "Profundidad completa si es posible."},
                    {"nombre": "Press Militar", "series": 4, "repeticiones": "8-10", "instrucciones": "Mantiene core estable durante todo el movimiento."},
                    {"nombre": "Prensa de Piernas", "series": 3, "repeticiones": "10-12", "instrucciones": "Foco en la fase excéntrica, 2 segundos de bajada."},
                    {"nombre": "Elevaciones Laterales", "series": 3, "repeticiones": "12-15", "instrucciones": "Movimiento controlado, sin impulso."},
                    {"nombre": "Curl Femoral", "series": 3, "repeticiones": "10-12", "instrucciones": "Contracción completa en el punto más alto."}
                ],
                "notas": "Alterna entre ejercicios de piernas y hombros para optimizar el tiempo de descanso."
            },
            {
                "nombre": "Día 3: Brazos/Core",
                "ejercicios": [
                    {"nombre": "Curl de Bíceps con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Mantiene codos pegados al cuerpo."},
                    {"nombre": "Extensión de Tríceps con Polea", "series": 4, "repeticiones": "8-10", "instrucciones": "Codos fijos, sólo se mueven los antebrazos."},
                    {"nombre": "Curl Martillo", "series": 3, "repeticiones": "10-12", "instrucciones": "Rotación neutra de las muñecas."},
                    {"nombre": "Fondos en Máquina", "series": 3, "repeticiones": "10-12", "instrucciones": "Desciende hasta estirar completamente el tríceps."},
                    {"nombre": "Circuito de Abdominales", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Crunch, oblicuos y elevación de piernas."}
                ],
                "notas": "Menor volumen total pero mayor frecuencia semanal para estos grupos musculares."
            },
            {
                "nombre": "Día 4: Pecho/Espalda (Variaciones)",
                "ejercicios": [
                    {"nombre": "Press Declinado", "series": 4, "repeticiones": "8-10", "instrucciones": "Enfoca la parte inferior del pecho."},
                    {"nombre": "Remo con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Lleva la barra al abdomen, espalda ligeramente arqueada."},
                    {"nombre": "Aperturas con Mancuernas", "series": 3, "repeticiones": "10-12", "instrucciones": "Movimiento de abrazo, estiramiento controlado."},
                    {"nombre": "Pull-over", "series": 3, "repeticiones": "10-12", "instrucciones": "Estiramiento completo para dorsales y serrato."},
                    {"nombre": "Facepull", "series": 3, "repeticiones": "12-15", "instrucciones": "Enfoca en la rotación externa y retracción escapular."}
                ],
                "notas": "Usa variaciones de ángulos y ejercicios diferentes a los del Día 1 para estimular nuevas fibras musculares."
            },
            {
                "nombre": "Día 5: Piernas/Hombros (Variaciones)",
                "ejercicios": [
                    {"nombre": "Peso Muerto Rumano", "series": 4, "repeticiones": "8-10", "instrucciones": "Enfoca isquiotibiales, mantiene espalda recta."},
                    {"nombre": "Press Militar con Mancuernas", "series": 4, "repeticiones": "8-10", "instrucciones": "Sentado o de pie, rotación neutra de muñecas."},
                    {"nombre": "Zancadas con Mancuernas", "series": 3, "repeticiones": "10-12 por pierna", "instrucciones": "Paso largo, rodilla trasera casi tocando el suelo."},
                    {"nombre": "Pájaro/Elevaciones Posteriores", "series": 3, "repeticiones": "12-15", "instrucciones": "Ligera inclinación hacia adelante, contracción en la parte posterior del hombro."},
                    {"nombre": "Abducción de Cadera", "series": 3, "repeticiones": "12-15", "instrucciones": "Enfoca los glúteos, mantiene tensión constante."}
                ],
                "notas": "Al igual que con pecho/espalda, utiliza variantes distintas para estimular diferentes ángulos musculares."
            },
            {
                "nombre": "Día 6: Brazos/Core (Variaciones)",
                "ejercicios": [
                    {"nombre": "Curl de Bíceps en Predicador", "series": 4, "repeticiones": "8-10", "instrucciones": "Aislamiento completo del bíceps."},
                    {"nombre": "Press Francés", "series": 4, "repeticiones": "8-10", "instrucciones": "Mantiene codos apuntando al techo, estiramiento completo del tríceps."},
                    {"nombre": "Curl Concentrado", "series": 3, "repeticiones": "10-12", "instrucciones": "Enfoca en el pico del bíceps."},
                    {"nombre": "Extensión de Tríceps Over-Head", "series": 3, "repeticiones": "10-12", "instrucciones": "Estiramiento completo en la posición inferior."},
                    {"nombre": "Plancha con Variaciones", "series": 3, "repeticiones": "30-45 segundos cada", "instrucciones": "Plancha frontal, lateral y con movimiento."}
                ],
                "notas": "Completa la semana con estas variaciones para brazos. El día 7 es de descanso completo."
            }
        ]
    },

    "Rutina de Hipertrofia Split": {
        "descripcion": "Rutina dividida por grupos musculares para maximizar el volumen e intensidad por sesión, con varios días para recuperación muscular entre entrenamientos del mismo grupo.",
        "dias": [
            {
                "nombre": "Día 1: Pecho",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 4, "repeticiones": "8-10", "instrucciones": "Peso desafiante, pausa breve en la parte inferior."},
                    {"nombre": "Press Inclinado con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Inclinación moderada para enfocarse en la parte superior del pecho."},
                    {"nombre": "Press Declinado", "series": 3, "repeticiones": "10-12", "instrucciones": "Enfoca la parte inferior del pecho."},
                    {"nombre": "Aperturas con Mancuernas", "series": 3, "repeticiones": "12-15", "instrucciones": "Estiramiento completo, sensación de 'abrazo'."},
                    {"nombre": "Cruces en Polea", "series": 3, "repeticiones": "15-20", "instrucciones": "Contracción intensa, bombeo de sangre al finalizar."},
                    {"nombre": "Flexiones (Drop Set)", "series": 2, "repeticiones": "Hasta el fallo", "instrucciones": "Al fallar, apoyándote en rodillas para continuar."}
                ],
                "notas": "Alto volumen e intensidad, enfocado exclusivamente en pecho. Descansos de 60-90 segundos entre series."
            },
            {
                "nombre": "Día 2: Espalda",
                "ejercicios": [
                    {"nombre": "Dominadas", "series": 4, "repeticiones": "8-10", "instrucciones": "Si es necesario, usa asistencia para alcanzar el rango de repeticiones."},
                    {"nombre": "Remo con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Torso inclinado a 45°, lleva barra al abdomen."},
                    {"nombre": "Jalon al Pecho", "series": 3, "repeticiones": "10-12", "instrucciones": "Agarre abierto, lleva la barra hacia el pecho."},
                    {"nombre": "Remo con Mancuerna", "series": 3, "repeticiones": "10-12 por brazo", "instrucciones": "Apoyo sobre banco, completamente enfocado en la contracción de la espalda."},
                    {"nombre": "Pull-over", "series": 3, "repeticiones": "12-15", "instrucciones": "Movimiento amplio para estirar latísimos."},
                    {"nombre": "Remo en Polea Baja (Drop Set)", "series": 2, "repeticiones": "15-20", "instrucciones": "Finaliza con drop set reduciendo peso 30% dos veces."}
                ],
                "notas": "Trabaja desde diferentes ángulos para estimular todas las zonas de la espalda. Enfatiza la contracción completa."
            },
            {
                "nombre": "Día 3: Piernas",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "8-10", "instrucciones": "Profundidad completa, mantiene tensión constante."},
                    {"nombre": "Prensa de Piernas", "series": 4, "repeticiones": "10-12", "instrucciones": "Pies en diferentes posiciones para trabajar distintas zonas."},
                    {"nombre": "Hack Squat", "series": 3, "repeticiones": "10-12", "instrucciones": "Enfoca cuádriceps, mantiene espalda contra el respaldo."},
                    {"nombre": "Extensiones de Cuádriceps", "series": 3, "repeticiones": "12-15", "instrucciones": "Contracción completa en la parte superior, enfoca mente-músculo."},
                    {"nombre": "Curl Femoral", "series": 4, "repeticiones": "10-12", "instrucciones": "Trabajo completo de isquiotibiales."},
                    {"nombre": "Elevación de Pantorrillas", "series": 4, "repeticiones": "15-20", "instrucciones": "Elevación completa, pausa en la contracción."}
                ],
                "notas": "Sesión de alto volumen para piernas. Descanso adecuado entre series pesadas para mantener intensidad."
            },
            {
                "nombre": "Día 4: Hombros y Trápezio",
                "ejercicios": [
                    {"nombre": "Press Militar", "series": 4, "repeticiones": "8-10", "instrucciones": "Pueden ser por delante o por detrás de la cabeza si la movilidad lo permite."},
                    {"nombre": "Press Arnold", "series": 3, "repeticiones": "10-12", "instrucciones": "Rotación completa de las mancuernas durante el movimiento."},
                    {"nombre": "Elevaciones Laterales", "series": 4, "repeticiones": "12-15", "instrucciones": "Mantiene codos ligeramente flexionados, elevación controlada."},
                    {"nombre": "Elevaciones Frontales", "series": 3, "repeticiones": "12-15", "instrucciones": "Alterna brazos o realiza con ambos simultáneamente."},
                    {"nombre": "Pájaro/Elevaciones Posteriores", "series": 3, "repeticiones": "12-15", "instrucciones": "Inclinación hacia adelante, contracción de deltoides posterior."},
                    {"nombre": "Encogimientos de Hombros", "series": 4, "repeticiones": "12-15", "instrucciones": "Control total del movimiento, pausa en la posición superior."}
                ],
                "notas": "Trabajo completo de los tres cabezas del deltoides y trápezio. Ejercicios de aislamiento para finalizar."
            },
            {
                "nombre": "Día 5: Brazos y Abdominales",
                "ejercicios": [
                    {"nombre": "Curl de Bíceps con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Mantiene codos fijos al lado del cuerpo."},
                    {"nombre": "Press Francés", "series": 4, "repeticiones": "8-10", "instrucciones": "Extensión completa de tríceps, control en bajada."},
                    {"nombre": "Curl Martillo", "series": 3, "repeticiones": "10-12", "instrucciones": "Trabaja tanto bíceps como braquial."},
                    {"nombre": "Extensión de Tríceps en Polea", "series": 3, "repeticiones": "10-12", "instrucciones": "Codos pegados al cuerpo, extensión completa."},
                    {"nombre": "Curl Predicador", "series": 3, "repeticiones": "12-15", "instrucciones": "Bíceps completamente aislado, contracción máxima."},
                    {"nombre": "Fondos en Banco", "series": 3, "repeticiones": "12-15", "instrucciones": "Codos apuntando hacia atrás, enfoca tríceps."},
                    {"nombre": "Circuito de Abdominales", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Crunch, elevación de piernas, rotaciones y plancha."}
                ],
                "notas": "Alto volumen para brazos, alternando bíceps y tríceps. Finaliza con trabajo de abdominales completo."
            }
        ]
    },

    "Rutina de Hipertrofia Full Body": {
        "descripcion": "Rutina de cuerpo completo para hipertrofia, enfocada en los principales grupos musculares en cada sesión con un volumen equilibrado.",
        "dias": [
            {
                "nombre": "Día 1: Cuerpo Completo - Enfoque en Empuje",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 4, "repeticiones": "8-10", "instrucciones": "Profundidad completa, empuje a través de los talones."},
                    {"nombre": "Press de Banca", "series": 4, "repeticiones": "8-10", "instrucciones": "Agarre medio, enfoque en contracción pectoral."},
                    {"nombre": "Press Militar", "series": 3, "repeticiones": "10-12", "instrucciones": "De pie o sentado, mantiene core estable."},
                    {"nombre": "Dominadas o Jalones", "series": 3, "repeticiones": "10-12", "instrucciones": "Agarre ancho, enfoca dorsales, contracción completa."},
                    {"nombre": "Curl de Bíceps con Barra", "series": 3, "repeticiones": "10-12", "instrucciones": "Movimiento controlado, sin balanceo."},
                    {"nombre": "Extensiones de Tríceps", "series": 3, "repeticiones": "10-12", "instrucciones": "Codos estables, enfoca en extensión completa."}
                ],
                "notas": "Descanso de 90 segundos entre series. Prioriza la técnica sobre el peso, especialmente en ejercicios compuestos iniciales."
            },
            {
                "nombre": "Día 2: Cuerpo Completo - Enfoque en Tracción",
                "ejercicios": [
                    {"nombre": "Peso Muerto Rumano", "series": 4, "repeticiones": "8-10", "instrucciones": "Espalda recta, enfoca tensión en isquiotibiales."},
                    {"nombre": "Remo con Barra", "series": 4, "repeticiones": "8-10", "instrucciones": "Espalda paralela al suelo, lleva barra al abdomen."},
                    {"nombre": "Press Inclinado", "series": 3, "repeticiones": "10-12", "instrucciones": "Enfoca parte superior del pecho."},
                    {"nombre": "Elevaciones Laterales", "series": 3, "repeticiones": "12-15", "instrucciones": "Movimiento controlado, codos ligeramente flexionados."},
                    {"nombre": "Skull Crushers", "series": 3, "repeticiones": "10-12", "instrucciones": "Codos apuntando al techo, aislamiento del tríceps."},
                    {"nombre": "Curl Martillo", "series": 3, "repeticiones": "10-12", "instrucciones": "Trabaja tanto bíceps como antebrazo."}
                ],
                "notas": "Mayor enfoque en ejercicios de tracción en esta sesión, manteniendo un equilibrio general con ejercicios de empuje."
            },
            {
                "nombre": "Día 3: Cuerpo Completo - Enfoque en Piernas",
                "ejercicios": [
                    {"nombre": "Prensa de Piernas", "series": 4, "repeticiones": "10-12", "instrucciones": "Amplitud completa, sin bloquear rodillas en la extensión."},
                    {"nombre": "Jalones al Pecho", "series": 4, "repeticiones": "10-12", "instrucciones": "Lleva barra hacia el pecho, estiramiento completo arriba."},
                    {"nombre": "Press de Hombros con Mancuernas", "series": 3, "repeticiones": "10-12", "instrucciones": "Rotación neutra o pronada según preferencia."},
                    {"nombre": "Zancadas", "series": 3, "repeticiones": "10-12 por pierna", "instrucciones": "Paso amplio, rodilla trasera casi tocando el suelo."},
                    {"nombre": "Fondos en Paralelas", "series": 3, "repeticiones": "10-12", "instrucciones": "Inclinación ligera hacia adelante para pecho, vertical para tríceps."},
                    {"nombre": "Curl Femoral", "series": 3, "repeticiones": "12-15", "instrucciones": "Contracción completa de isquiotibiales."}
                ],
                "notas": "Mayor énfasis en piernas en esta sesión, pero manteniendo trabajo para torso superior para frecuencia óptima."
            }
        ]
    },

    # RUTINAS DE PÉRDIDA DE PESO ADICIONALES
    "Rutina de Pérdida de Peso Cardio": {
        "descripcion": "Rutina cardiovascular para pérdida de peso sostenida, enfocada en ejercicios aeróbicos de media-larga duración.",
        "dias": [
            {
                "nombre": "Día 1: Cardio Base + Core",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Movilidad dinámica y cardio ligero gradual."},
                    {"nombre": "Carrera/Caminata", "series": 1, "repeticiones": "40-45 minutos", "instrucciones": "Mantiene ritmo moderado constante (65-75% FCM)."},
                    {"nombre": "Circuito de Core", "series": 3, "repeticiones": "30-45 segundos cada", "instrucciones": "Plancha, plancha lateral, mountain climbers, crunch bicicleta."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Disminuye ritmo gradualmente y estiramientos básicos."}
                ],
                "notas": "Mantén la frecuencia cardiaca en zona de quema de grasa (65-75% de tu FCM). Puedes usar monitor de FC para precisar."
            },
            {
                "nombre": "Día 2: Cardio Cruzado (Elíptica/Ciclismo)",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Bajo impacto, incremento gradual de intensidad."},
                    {"nombre": "Elíptica/Bicicleta", "series": 1, "repeticiones": "50 minutos", "instrucciones": "Intensidad moderada, variar resistencia cada 5 minutos."},
                    {"nombre": "Estiramiento completo", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Estiramientos estáticos para piernas, caderas y espalda baja."}
                ],
                "notas": "El cardio cruzado reduce el impacto en las articulaciones mientras mantiene el gasto calórico. Ideal si tienes problemas articulares."
            },
            {
                "nombre": "Día 3: Cardio Intervalos Largos",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad progresiva."},
                    {"nombre": "Intervalos", "series": 5, "repeticiones": "5 minutos trabajo/2 minutos recuperación", "instrucciones": "Intensidad 80% FCM durante trabajo, 60% durante recuperación."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Reducción gradual y estiramientos básicos."}
                ],
                "notas": "Los intervalos largos son ideales para mejorar la capacidad aeróbica y quemar calorías adicionales. Puedes hacerlos en cualquier máquina."
            },
            {
                "nombre": "Día 4: Natación o Remo",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Nado suave o remo ligero para preparar el cuerpo."},
                    {"nombre": "Natación/Remo continuo", "series": 1, "repeticiones": "30-40 minutos", "instrucciones": "Ritmo constante moderado, alternando estilos si es natación."},
                    {"nombre": "Intervalos cortos", "series": 5, "repeticiones": "1 minuto rápido/1 minuto lento", "instrucciones": "Al final de la sesión, aumenta el ritmo para estimular el metabolismo."}
                ],
                "notas": "La natación y el remo involucran casi todos los músculos del cuerpo, maximizando el gasto calórico con impacto mínimo."
            },
            {
                "nombre": "Día 5: Cardio Mixto + Flexibilidad",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Movilidad dinámica general."},
                    {"nombre": "Circuito cardio", "series": 3, "repeticiones": "6 minutos por estación", "instrucciones": "Rotación entre cinta, bicicleta y elíptica, 6 minutos en cada una."},
                    {"nombre": "Sesión de flexibilidad", "series": 1, "repeticiones": "15-20 minutos", "instrucciones": "Rutina de estiramientos completa, manteniendo cada posición 30 segundos."}
                ],
                "notas": "La variación del tipo de cardio previene el aburrimiento y la adaptación. La flexibilidad al final mejora la recuperación."
            }
        ]
    },

    "Rutina de Pérdida de Peso Fuerza": {
        "descripcion": "Rutina de fuerza para mantener masa muscular durante la pérdida de peso, con entrenamiento en circuito para maximizar el gasto calórico.",
        "dias": [
            {
                "nombre": "Día 1: Circuito de Fuerza Tren Superior",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad de hombros y brazos."},
                    {"nombre": "Circuito de Fuerza 1", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Press de banca, remo con mancuerna, press hombro, curl bíceps, extensión tríceps."},
                    {"nombre": "Cardio intermedio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Cardio moderado entre circuitos."},
                    {"nombre": "Circuito de Fuerza 2", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Cruces en polea, jalones al pecho, elevaciones laterales, martillo, fondos."}
                ],
                "notas": "Usa pesos moderados que permitan buena técnica. Descanso mínimo entre ejercicios (30s) y 1-2 minutos entre circuitos."
            },
            {
                "nombre": "Día 2: Circuito de Fuerza Tren Inferior",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad de caderas y rodillas."},
                    {"nombre": "Circuito de Fuerza 1", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Sentadilla, peso muerto rumano, zancadas, abducción de cadera, elevación de talones."},
                    {"nombre": "Cardio intermedio", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Cardio moderado entre circuitos."},
                    {"nombre": "Circuito de Fuerza 2", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Prensa de piernas, curl femoral, extensión de cuádriceps, hip thrust, plancha."}
                ],
                "notas": "El volumen e intensidad moderados ayudan a mantener la masa muscular durante el déficit calórico."
            },
            {
                "nombre": "Día 3: Cardio Moderado",
                "ejercicios": [
                    {"nombre": "Cardio constante", "series": 1, "repeticiones": "40-60 minutos", "instrucciones": "Cardio a elección (caminata, natación, ciclismo) a intensidad moderada."}
                ],
                "notas": "Día de menor intensidad para permitir recuperación muscular. Mantiene zona de quema de grasa (65-75% FCM)."
            },
            {
                "nombre": "Día 4: Circuito de Fuerza Total",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad general."},
                    {"nombre": "Circuito Total 1", "series": 3, "repeticiones": "45 segundos trabajo/15 segundos descanso", "instrucciones": "Sentadilla, flexiones, peso muerto, remo, zancadas, press hombro."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "3 minutos", "instrucciones": "Recuperación activa entre circuitos."},
                    {"nombre": "Circuito Total 2", "series": 3, "repeticiones": "45 segundos trabajo/15 segundos descanso", "instrucciones": "Burpees, dominadas asistidas, kettlebell swing, mountain climbers, plancha, saltos."}
                ],
                "notas": "Circuito de alta intensidad que combina fuerza y cardio para maximizar el gasto calórico y el efecto post-ejercicio."
            },
            {
                "nombre": "Día 5: Circuito Metabólico",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad general."},
                    {"nombre": "Complejo con barra o mancuernas", "series": 5, "repeticiones": "8-10 por ejercicio", "instrucciones": "Realiza todos los movimientos sin soltar el peso: peso muerto, remo, cargada, press hombro, sentadilla frontal."},
                    {"nombre": "Cardio HIIT", "series": 8, "repeticiones": "20 segundos trabajo/10 segundos descanso", "instrucciones": "Sprint, burpees, mountain climbers o jump squats a máxima intensidad."}
                ],
                "notas": "Combinación potente de entrenamiento con resistencia y cardio intenso. Usa pesos ligeros para mantener buena técnica durante los complejos."
            }
        ]
    },

    "Rutina de Pérdida de Peso Circuitos": {
        "descripcion": "Rutina en circuito que combina cardio y fuerza para maximizar la quema de calorías y el efecto afterburn (EPOC).",
        "dias": [
            {
                "nombre": "Día 1: Circuito Full Body",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio ligero y movilidad dinámica."},
                    {"nombre": "Circuito Principal", "series": 4, "repeticiones": "12-15 cada ejercicio", "instrucciones": "Sentadilla, press banca, remo, press hombro, peso muerto, plancha 30s."},
                    {"nombre": "Burst de Cardio", "series": 4, "repeticiones": "1 minuto", "instrucciones": "Cardio intenso entre cada serie del circuito: burpees, jump rope, mountain climbers o high knees."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio suave y estiramientos."}
                ],
                "notas": "Realiza todo el circuito sin descanso entre ejercicios, descansa 1-2 minutos entre series completas."
            },
            {
                "nombre": "Día 2: Circuito EMOM (Every Minute On the Minute)",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio progresivo y movilidad básica."},
                    {"nombre": "EMOM 30 minutos", "series": 30, "repeticiones": "Ver instrucciones", "instrucciones": "Minuto 1: 15 sentadillas, Minuto 2: 12 flexiones, Minuto 3: 10 swing kettlebell, Minuto 4: 15 mountain climbers, Minuto 5: 10 burpees. Repite 6 veces."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Estiramientos y respiración."}
                ],
                "notas": "En cada minuto, realiza las repeticiones indicadas. El tiempo restante es tu descanso. Ejemplo: si terminas las sentadillas en 40 segundos, tienes 20 segundos de descanso antes del siguiente minuto."
            },
            {
                "nombre": "Día 3: Cardio Largo",
                "ejercicios": [
                    {"nombre": "Cardio constante", "series": 1, "repeticiones": "45-60 minutos", "instrucciones": "Cardio a elección a intensidad moderada (65-75% FCM)."}
                ],
                "notas": "Día de recuperación activa. Elige cardio de bajo impacto si tienes fatiga muscular de los días anteriores."
            },
            {
                "nombre": "Día 4: Circuito Tabata Completo",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Activación completa y movilidad."},
                    {"nombre": "Tabata 1: Tren Inferior", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Sentadillas con salto."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación."},
                    {"nombre": "Tabata 2: Empuje", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Flexiones (rodillas si es necesario)."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación."},
                    {"nombre": "Tabata 3: Core", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Mountain climbers."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación."},
                    {"nombre": "Tabata 4: Cardio", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Burpees."},
                    {"nombre": "Descanso", "series": 1, "repeticiones": "1 minuto", "instrucciones": "Recuperación."},
                    {"nombre": "Tabata 5: Tracción", "series": 8, "repeticiones": "20s trabajo/10s descanso", "instrucciones": "Remo con banda elástica o TRX."}
                ],
                "notas": "El formato Tabata es extremadamente intenso: 20s de esfuerzo máximo + 10s de descanso x 8 rondas = 4 minutos por ejercicio. Total: 20 minutos de trabajo intenso."
            },
            {
                "nombre": "Día 5: Circuito Tiempo/Estaciones",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio progresivo y movilidad completa."},
                    {"nombre": "Circuito por Estaciones", "series": 3, "repeticiones": "40 segundos trabajo/20 segundos transición", "instrucciones": "Estación 1: Battle ropes; Estación 2: Kettlebell swing; Estación 3: Box jumps; Estación 4: Ball slams; Estación 5: TRX rows; Estación 6: Planchas; Estación 7: Step-ups; Estación 8: Press de hombro."}
                ],
                "notas": "Completa todo el circuito 3 veces. Usa los 20 segundos para cambiar de estación y prepararte. Descansa 2-3 minutos entre circuitos completos."
            }
        ]
    },

    "Rutina de Pérdida de Peso Mixta": {
        "descripcion": "Rutina que combina diferentes métodos para pérdida de peso, incluyendo cardio, fuerza, HIIT y circuitos, para maximizar resultados y prevenir adaptaciones.",
        "dias": [
            {
                "nombre": "Día 1: Fuerza + HIIT",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio ligero y movilidad progresiva."},
                    {"nombre": "Fuerza: Tren Inferior", "series": 3, "repeticiones": "12-15", "instrucciones": "Sentadilla goblet, peso muerto rumano, zancadas, prensa de piernas."},
                    {"nombre": "HIIT", "series": 8, "repeticiones": "30s trabajo/30s descanso", "instrucciones": "Burpees, mountain climbers, saltos, sprint en el sitio. 2 rondas de cada uno."}
                ],
                "notas": "Comienza con fuerza para aprovechar las reservas de glucógeno, luego pasa a HIIT para maximizar la quema de grasa."
            },
            {
                "nombre": "Día 2: Cardio Estable + Core",
                "ejercicios": [
                    {"nombre": "Cardio constante", "series": 1, "repeticiones": "45 minutos", "instrucciones": "Mantiene 65-75% FCM, cualquier cardio a elección."},
                    {"nombre": "Circuito de Core", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "Planchas (60s), crunch bicicleta, russian twists, leg raises, mountain climbers lentos."}
                ],
                "notas": "El cardio estable en la zona de quema de grasa es ideal para entrenamientos más largos. Añadir core al final maximiza el tiempo de entrenamiento."
            },
            {
                "nombre": "Día 3: Entrenamiento en Circuito",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Movilidad dinámica completa."},
                    {"nombre": "Circuito Full Body", "series": 4, "repeticiones": "15 reps cada ejercicio", "instrucciones": "1. Sentadilla con press, 2. Remo con mancuerna, 3. Burpees, 4. Abdominales, 5. Zancadas alternas, 6. Dominadas asistidas o jalones, 7. Step-ups con mancuernas, 8. Flexiones."}
                ],
                "notas": "Mínimo descanso entre ejercicios (15-30s), 2 minutos entre circuitos completos. El circuito combina fuerza y cardio para efecto metabólico óptimo."
            },
            {
                "nombre": "Día 4: Intervalos Variados",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio progresivo."},
                    {"nombre": "Piramidal", "series": 9, "repeticiones": "Variable", "instrucciones": "Intensidad 80-85% FCM. Estructura: 1 min/2 min/3 min/4 min/5 min/4 min/3 min/2 min/1 min con 1 min descanso entre intervalos."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Ritmo suave y estiramientos."}
                ],
                "notas": "Los intervalos piramidales son excelentes para trabajar diferentes sistemas energéticos en una sola sesión. Puedes hacerlo en cualquier máquina de cardio."
            },
            {
                "nombre": "Día 5: Fuerza Metabólica",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Movilidad dinámica completa y activación muscular."},
                    {"nombre": "Superseries: Empuje/Tracción", "series": 3, "repeticiones": "12-15 cada ejercicio", "instrucciones": "A1: Press de banca, A2: Remo con barra. Sin descanso entre ejercicios, 1 min entre superseries."},
                    {"nombre": "Superseries: Piernas/Hombros", "series": 3, "repeticiones": "12-15 cada ejercicio", "instrucciones": "B1: Sentadilla, B2: Press militar. Sin descanso entre ejercicios, 1 min entre superseries."},
                    {"nombre": "Superseries: Brazos/Core", "series": 3, "repeticiones": "15-20 cada ejercicio", "instrucciones": "C1: Curl de bíceps + extensión de tríceps, C2: Plancha con movimiento. Sin descanso entre ejercicios, 1 min entre superseries."},
                    {"nombre": "Finalizador metabólico", "series": 3, "repeticiones": "30 segundos", "instrucciones": "Burpees a máxima intensidad posible, descanso de 30 segundos entre series."}
                ],
                "notas": "El entrenamiento en superseries minimiza el descanso y aumenta el gasto calórico. Usa pesos que te permitan completar todas las repeticiones con buena técnica."
            }
        ]
    },
    
    # RUTINAS DE MANTENIMIENTO ADICIONALES
    "Rutina de Mantenimiento Flexibilidad": {
        "descripcion": "Rutina enfocada en mejorar y mantener la flexibilidad, movilidad articular y elasticidad muscular.",
        "dias": [
            {
                "nombre": "Día 1: Flexibilidad Dinámica y Estática",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio ligero para aumentar temperatura corporal."},
                    {"nombre": "Movilidad articular", "series": 1, "repeticiones": "10 repeticiones por articulación", "instrucciones": "Circunducción de tobillos, rodillas, caderas, hombros y muñecas."},
                    {"nombre": "Estiramientos dinámicos", "series": 2, "repeticiones": "10 repeticiones cada uno", "instrucciones": "Leg swings, arm circles, lunges dinámicos, rotaciones de tronco."},
                    {"nombre": "Estiramientos estáticos", "series": 1, "repeticiones": "30-60 segundos cada posición", "instrucciones": "Cuadriceps, isquiotibiales, glúteos, gemelos, pectorales, dorsales, tríceps, antígravos."}
                ],
                "notas": "Combina métodos de estiramiento dinámico (con movimiento) al principio y estático (manteniendo posiciones) al final."
            },
            {
                "nombre": "Día 2: Yoga Básico",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Respiración profunda y movilidad suave."},
                    {"nombre": "Saludo al Sol (Surya Namaskar)", "series": 5, "repeticiones": "1 secuencia completa", "instrucciones": "Flujo continuo, sincronizando respiración y movimiento."},
                    {"nombre": "Posturas de pie", "series": 1, "repeticiones": "30-60 segundos cada postura", "instrucciones": "Triángulo, guerrero I y II, árbol, etc."},
                    {"nombre": "Posturas sentadas", "series": 1, "repeticiones": "30-60 segundos cada postura", "instrucciones": "Pinza sentada, mariposa, tortuga, etc."},
                    {"nombre": "Relajación final", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Savasana con respiración consciente."}
                ],
                "notas": "Enfoca en la respiración sincronizada con el movimiento. No fuerces ninguna postura, respeta los límites de tu cuerpo."
            },
            {
                "nombre": "Día 3: Pilates Básico",
                "ejercicios": [
                    {"nombre": "Respiración", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Respiración profunda, expansión de costillas."},
                    {"nombre": "Activación de Core", "series": 1, "repeticiones": "10-12 cada ejercicio", "instrucciones": "Hundred preparatorio, curl-up, pelvis neutral."},
                    {"nombre": "Serie de Suelo", "series": 1, "repeticiones": "8-10 cada ejercicio", "instrucciones": "Single leg stretch, double leg stretch, spine twist."},
                    {"nombre": "Estabilización de Columna", "series": 1, "repeticiones": "8-10 cada ejercicio", "instrucciones": "Swimming, shell stretch, child's pose."},
                    {"nombre": "Movilidad de Columna", "series": 1, "repeticiones": "8 repeticiones", "instrucciones": "Cat-cow, roll up, roll down."}
                ],
                "notas": "Pilates se enfoca en la calidad del movimiento, no en la cantidad. Mantiene elongación axial (columna alargada) durante todos los ejercicios."
            },
            {
                "nombre": "Día 4: Estiramientos y Movilidad Funcional",
                "ejercicios": [
                    {"nombre": "Rotación Torácica", "series": 3, "repeticiones": "10 por lado", "instrucciones": "En cuadrupedia, rotación completa siguiendo la mano con la mirada."},
                    {"nombre": "Hip Flow", "series": 3, "repeticiones": "8 repeticiones", "instrucciones": "Secuencia de movilidad de cadera: lizard pose, pigeon pose, frog stretch."},
                    {"nombre": "Shoulder Flow", "series": 3, "repeticiones": "8 repeticiones", "instrucciones": "Secuencia de movilidad de hombros: wall slides, reach & lift, sleeper stretch."},
                    {"nombre": "Foam Rolling", "series": 1, "repeticiones": "30-60 segundos por grupo muscular", "instrucciones": "Cuadriceps, IT band, isquiotibiales, glúteos, dorsales, pectorales."},
                    {"nombre": "Estiramientos FNP", "series": 2, "repeticiones": "3 ciclos por músculo", "instrucciones": "Contracción-relajación para isquiotibiales, cuadriceps y pectorales."}
                ],
                "notas": "La técnica FNP (Facilitación Neuromuscular Propioceptiva) implica contraer el músculo que estiras durante 5-6 segundos, luego relajar y profundizar el estiramiento."
            },
            {
                "nombre": "Día 5: Yoga Avanzado + Relajación",
                "ejercicios": [
                    {"nombre": "Meditación Inicial", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Respiración consciente, establecer intención."},
                    {"nombre": "Saludo al Sol B", "series": 3, "repeticiones": "1 secuencia completa", "instrucciones": "Versión avanzada incluyendo chattaranga y perro boca arriba."},
                    {"nombre": "Secuencia de Equilibrio", "series": 1, "repeticiones": "30-60 segundos cada postura", "instrucciones": "Poses de equilibrio: árbol, bailarín, guerrero III."},
                    {"nombre": "Secuencia de Apertura", "series": 1, "repeticiones": "1-2 minutos cada postura", "instrucciones": "Paloma, lagartija, split, puente."},
                    {"nombre": "Relajación Profunda", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Savasana con escaneo corporal completo."}
                ],
                "notas": "Sesiones de yoga más largas permiten profundizar en las posturas. Usa soportes (bloques, cinturones) si es necesario para mantener alineación correcta."
            }
        ]
    },
    
    "Rutina de Mantenimiento Fuerza": {
        "descripcion": "Rutina de fuerza para mantener la masa muscular y los niveles de fuerza adquiridos, con volumen e intensidad moderados.",
        "dias": [
            {
                "nombre": "Día 1: Mantenimiento Tren Superior",
                "ejercicios": [
                    {"nombre": "Press de Banca", "series": 3, "repeticiones": "8-10", "instrucciones": "Peso moderado-alto (70-75% de 1RM), técnica perfecta."},
                    {"nombre": "Dominadas o Jalones", "series": 3, "repeticiones": "8-10", "instrucciones": "Enfoca la contracción en dorsales, completa amplitud de movimiento."},
                    {"nombre": "Press Militar", "series": 3, "repeticiones": "8-10", "instrucciones": "Controla el movimiento en todo momento, estabilidad de core."},
                    {"nombre": "Remo con Barra", "series": 3, "repeticiones": "8-10", "instrucciones": "Mantén la espalda recta, tira desde los codos."},
                    {"nombre": "Fondos en Paralelas", "series": 2, "repeticiones": "8-10", "instrucciones": "Control completo, profundidad adecuada."}
                ],
                "notas": "Descanso de 90 segundos entre series. El enfoque está en mantener la fuerza con un volumen moderado, no en progresión constante."
            },
            {
                "nombre": "Día 2: Mantenimiento Tren Inferior",
                "ejercicios": [
                    {"nombre": "Sentadilla", "series": 3, "repeticiones": "8-10", "instrucciones": "Peso moderado-alto (70-75% de 1RM), profundidad completa."},
                    {"nombre": "Peso Muerto Rumano", "series": 3, "repeticiones": "8-10", "instrucciones": "Foco en la tensión de isquiotibiales, espalda neutra."},
                    {"nombre": "Zancadas con Mancuernas", "series": 2, "repeticiones": "10 por pierna", "instrucciones": "Paso largo, rodilla trasera cerca del suelo."},
                    {"nombre": "Elevación de Talones", "series": 3, "repeticiones": "10-12", "instrucciones": "Completa extensión, contracción en el punto más alto."},
                    {"nombre": "Abducción de Cadera", "series": 2, "repeticiones": "12-15", "instrucciones": "Controla el movimiento, evita impulsos."}
                ],
                "notas": "Descanso de 90-120 segundos entre series de ejercicios pesados. Mantiene la intensidad suficiente para evitar pérdidas de fuerza."
            },
            {
                "nombre": "Día 3: Cardio Moderado",
                "ejercicios": [
                    {"nombre": "Cardio de Elección", "series": 1, "repeticiones": "30-40 minutos", "instrucciones": "Intensidad moderada (65-75% FCM), ritmo constante."}
                ],
                "notas": "El cardio moderado ayuda a mantener la salud cardiovascular sin interferir con la recuperación muscular o los niveles de fuerza."
            },
            {
                "nombre": "Día 4: Mantenimiento Full Body",
                "ejercicios": [
                    {"nombre": "Press de Banca Inclinado", "series": 3, "repeticiones": "8-10", "instrucciones": "Variación del press estándar para estimular diferentes fibras."},
                    {"nombre": "Peso Muerto", "series": 3, "repeticiones": "6-8", "instrucciones": "Técnica impecable, peso moderado-alto."},
                    {"nombre": "Pull-ups o Jalones", "series": 3, "repeticiones": "8-10", "instrucciones": "Agarre diferente al Día 1, contracción completa."},
                    {"nombre": "Press Hombro con Mancuernas", "series": 2, "repeticiones": "10-12", "instrucciones": "Rotación neutra o pronada, estabilidad de core."},
                    {"nombre": "Curl de Bíceps", "series": 2, "repeticiones": "10-12", "instrucciones": "Contracción completa, sin balanceo."},
                    {"nombre": "Extensión de Tríceps", "series": 2, "repeticiones": "10-12", "instrucciones": "Codos estables, extensión completa."}
                ],
                "notas": "Entrenamiento de cuerpo completo con menor volumen por grupo muscular. Enfocado en mantener fuerza en los principales patrones de movimiento."
            }
        ]
    },

    "Rutina de Mantenimiento Cardio": {
        "descripcion": "Rutina cardiovascular para mantener la condición física aeróbica y la salud cardiovascular general.",
        "dias": [
            {
                "nombre": "Día 1: Cardio Constante",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Cardio suave, incremento gradual."},
                    {"nombre": "Carrera/Caminata/Eliptica", "series": 1, "repeticiones": "30-40 minutos", "instrucciones": "Intensidad moderada (65-75% FCM), ritmo constante."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5 minutos", "instrucciones": "Disminución gradual y estiramientos básicos."}
                ],
                "notas": "El cardio de estado estable es excelente para mantener la base aeróbica sin demasiado estrés para el cuerpo."
            },
            {
                "nombre": "Día 2: Fuerza Ligera",
                "ejercicios": [
                    {"nombre": "Circuito básico", "series": 3, "repeticiones": "12-15 cada ejercicio", "instrucciones": "Sentadilla con peso corporal, flexiones, remo con mancuerna ligera, plancha 30s, zancadas, elevaciones laterales."}
                ],
                "notas": "La fuerza ligera complementa el entrenamiento cardiovascular y ayuda a mantener tono muscular."
            },
            {
                "nombre": "Día 3: Cardio Intervalos",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Cardio progresivo y movilidad general."},
                    {"nombre": "Intervalos moderados", "series": 6, "repeticiones": "2 minutos trabajo/1 minuto recuperación", "instrucciones": "Intensidad 75-80% durante el trabajo, 60% en recuperación."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Ritmo suave decreciente y estiramientos."}
                ],
                "notas": "Los intervalos ayudan a mantener la capacidad aeróbica y anaeróbica sin la misma intensidad que sesiones HIIT completas."
            },
            {
                "nombre": "Día 4: Actividad Recreativa",
                "ejercicios": [
                    {"nombre": "Deporte o actividad de ocio", "series": 1, "repeticiones": "30-60 minutos", "instrucciones": "Cualquier actividad que disfrutes: ciclismo, natación, tenis, baloncesto, senderismo, etc."}
                ],
                "notas": "Las actividades recreativas mantienen la motivación alta y trabajan patrones de movimiento variados de forma natural."
            },
            {
                "nombre": "Día 5: Cardio Mixto + Movilidad",
                "ejercicios": [
                    {"nombre": "Cardio multimáquina", "series": 3, "repeticiones": "10 minutos cada una", "instrucciones": "Rota entre 3 máquinas diferentes: bicicleta, elíptica, remo, etc."},
                    {"nombre": "Movilidad completa", "series": 1, "repeticiones": "15-20 minutos", "instrucciones": "Secuencia de movilidad para todas las articulaciones principales."}
                ],
                "notas": "La variedad previene el aburrimiento y la adaptación excesiva. La movilidad ayuda a prevenir lesiones y mantener rango de movimiento completo."
            }
        ]
    },

    "Rutina de Mantenimiento Funcional": {
        "descripcion": "Rutina funcional para mantener la capacidad física general, enfocada en movimientos naturales y aplicables a la vida diaria.",
        "dias": [
            {
                "nombre": "Día 1: Patrones Funcionales Básicos",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Movilidad dinámica completa."},
                    {"nombre": "Sentadilla Goblet", "series": 3, "repeticiones": "10-12", "instrucciones": "Mantiene pecho alto, profundidad completa, peso moderado."},
                    {"nombre": "Push-up", "series": 3, "repeticiones": "10-12", "instrucciones": "Control total, core activo, línea recta desde cabeza a talones."},
                    {"nombre": "Peso Muerto con Mancuerna", "series": 3, "repeticiones": "10-12", "instrucciones": "Bisagra de cadera, espalda neutra, peso moderado."},
                    {"nombre": "Remo con TRX/inverted row", "series": 3, "repeticiones": "10-12", "instrucciones": "Cuerpo rígido, retracción escapular completa."}
                ],
                "notas": "Enfoca en los patrones básicos de movimiento: empujar, tirar, bisagra de cadera y sentadilla. La calidad del movimiento es clave."
            },
            {
                "nombre": "Día 2: Funcional Cardiovascular",
                "ejercicios": [
                    {"nombre": "Circuito metábolico", "series": 3, "repeticiones": "45 segundos trabajo/15 segundos descanso", "instrucciones": "Jumping jacks, mountain climbers, skipping, burpees, high knees."}
                ],
                "notas": "Circuito de ejercicios cardiovasculares que mantienen el componente funcional. Realiza 3-4 vueltas al circuito completo con 2 minutos de descanso entre vueltas."
            },
            {
                "nombre": "Día 3: Patrones Funcionales Unilaterales",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Movilidad dinámica enfocada en caderas y core."},
                    {"nombre": "Zancada hacia delante", "series": 3, "repeticiones": "10 por pierna", "instrucciones": "Paso largo, rodilla posterior cerca del suelo."},
                    {"nombre": "Press con mancuerna unilateral", "series": 3, "repeticiones": "10 por brazo", "instrucciones": "En banco, control total, estabilidad de core."},
                    {"nombre": "Peso Muerto a una pierna", "series": 3, "repeticiones": "10 por pierna", "instrucciones": "Mantiene cadera nivelada, pierna libre extendida atrás."},
                    {"nombre": "Remo unilateral", "series": 3, "repeticiones": "10 por brazo", "instrucciones": "Apoyado en banco, espalda paralela al suelo, contracción completa."}
                ],
                "notas": "El trabajo unilateral mejora el equilibrio, corrige descompensaciones y aumenta la estabilidad del core."
            },
            {
                "nombre": "Día 4: Circuito Funcional Completo",
                "ejercicios": [
                    {"nombre": "Calentamiento", "series": 1, "repeticiones": "10 minutos", "instrucciones": "Movilidad dinámica y activación."},
                    {"nombre": "Circuito Completo", "series": 3, "repeticiones": "12 cada ejercicio", "instrucciones": "Kettlebell swing, flexiones con rotación, sentadilla con press, turkish get-up, escaladores, battle rope (30s)."},
                    {"nombre": "Enfriamiento", "series": 1, "repeticiones": "5-10 minutos", "instrucciones": "Estiramiento y respiración."}
                ],
                "notas": "Este circuito combina patrones de movimiento funcionales multi-articulares. Realiza todos los ejercicios en secuencia con mínimo descanso entre ellos. Descansa 2 minutos entre circuitos completos."
            },
            {
                "nombre": "Día 5: Core Funcional y Estabilidad",
                "ejercicios": [
                    {"nombre": "Serie anti-rotación", "series": 3, "repeticiones": "10-12 cada lado", "instrucciones": "Pallof press, plancha con rotación, bird-dog."},
                    {"nombre": "Serie anti-extensión", "series": 3, "repeticiones": "30-45 segundos", "instrucciones": "Plancha frontal, plancha lateral, dead bug."},
                    {"nombre": "Serie anti-flexión lateral", "series": 3, "repeticiones": "10-12 cada lado", "instrucciones": "Side plank con elevaciones, farmer's walk, caminata con mancuerna overhead."}
                ],
                "notas": "El core funcional se enfoca en la estabilidad antes que en la estética. Estos ejercicios trabajan la resistencia del core a las fuerzas externas (rotación, extensión, flexión lateral)."
            }
        ]
    }
}

def obtener_rutina_detallada(nombre_rutina):
    """Obtiene los detalles completos de una rutina específica."""
    if nombre_rutina in rutinas_detalladas:
        return rutinas_detalladas[nombre_rutina]
    else:
        # Si no existe la rutina detallada, crear una estructura básica
        return {
            "descripcion": f"Detalles para {nombre_rutina} no disponibles.",
            "dias": [
                {
                    "nombre": "Programa en desarrollo",
                    "ejercicios": [
                        {"nombre": "Consulta con un entrenador", "series": 1, "repeticiones": "N/A", "instrucciones": "Esta rutina requiere personalización."}
                    ],
                    "notas": "Esta rutina está en desarrollo."
                }
            ]
        }
