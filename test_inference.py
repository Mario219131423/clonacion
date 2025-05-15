from src.inference_engine.engine import InferenceEngine

def test_inference_engine():
    # Crear instancia del motor de inferencia
    engine = InferenceEngine()
    
    # Simular diferentes casos de prueba
    test_cases = [
        {
            "name": "Caso 1: Usuario joven con objetivo de pérdida de peso",
            "evidence": {
                "age": 25,
                "experience": 1,
                "goal": "Pérdida de peso",
                "frequency": 4,
                "injuries": False,
                "equipment": True
            }
        },
        {
            "name": "Caso 2: Usuario experimentado con objetivo de fuerza",
            "evidence": {
                "age": 35,
                "experience": 5,
                "goal": "Fuerza",
                "frequency": 5,
                "injuries": False,
                "equipment": True
            }
        },
        {
            "name": "Caso 3: Usuario con lesiones buscando mantenimiento",
            "evidence": {
                "age": 45,
                "experience": 2,
                "goal": "Mantenimiento",
                "frequency": 3,
                "injuries": True,
                "equipment": False
            }
        }
    ]
    
    # Probar cada caso
    for case in test_cases:
        print("\n" + "="*80)
        print(f"Probando: {case['name']}")
        print("="*80)
        
        # Obtener recomendación
        result = engine.make_recommendation(user_id=1, evidence=case['evidence'])
        
        # Mostrar resultados
        print("\nEvidencia del usuario:")
        for key, value in case['evidence'].items():
            print(f"- {key}: {value}")
        
        print("\nResultado:")
        print(result['recommendation'])

if __name__ == "__main__":
    test_inference_engine() 