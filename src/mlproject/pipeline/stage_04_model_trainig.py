from src.mlproject.config.configuration import ConfiguratioManager
from src.mlproject import logger
from pathlib import Path
from src.mlproject.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Training Stage"


class ModelTainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfiguratioManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)  
        model_trainer.train()  
    
