from src.mlproject.config.configuration import ConfiguratioManager
from src.mlproject import logger
from pathlib import Path
from src.mlproject.components.model_evaluation import ModelEvaluation



STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguratioManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)  
        model_evaluation_config.save_results()