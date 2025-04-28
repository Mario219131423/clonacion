# Sistema Experto para Gimnasio

Este sistema experto está diseñado para ayudar a los usuarios a crear rutinas de ejercicio personalizadas basadas en sus objetivos, nivel de condición física y preferencias.

## Características
- Evaluación inicial del usuario
- Recomendación de rutinas personalizadas
- Seguimiento de progreso
- Base de conocimientos de ejercicios
- Sistema de reglas para recomendaciones

## Estructura del Proyecto
```
gym-experto/
├── src/
│   ├── knowledge_base/
│   │   ├── exercises.py
│   │   └── rules.py
│   ├── inference_engine/
│   │   └── engine.py
│   ├── user_interface/
│   │   └── cli.py
│   └── main.py
├── tests/
│   └── test_engine.py
├── requirements.txt
└── README.md
```

## Requisitos
- Python 3.8+
- Dependencias listadas en requirements.txt

## Instalación
1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar el programa: `python src/main.py` 