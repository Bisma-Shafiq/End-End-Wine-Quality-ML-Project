from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.components.data_validation import DataValidation
from src.mlproject import logger
from src.mlproject.config.configuration import ConfiguratioManager
import os

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfiguratioManager()
        data_valiadtion_config = config.get_data_validation_config()
        data_validation= DataValidation(config=data_valiadtion_config)
        data_validation.validation_all_columns()
