from user_interface.cli import CLI
from inference_engine.engine import InferenceEngine
from knowledge_base.exercises import ExerciseDatabase
from knowledge_base.rules import RuleBase

def main():
    # Inicializar componentes
    exercise_db = ExerciseDatabase()
    rule_base = RuleBase()
    inference_engine = InferenceEngine(rule_base, exercise_db)
    cli = CLI(inference_engine)

    # Iniciar la interfaz de usuario
    cli.start()

if __name__ == "__main__":
    main() 