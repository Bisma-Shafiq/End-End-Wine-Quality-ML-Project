from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.components.data_ingestiion import DataIngestion
from src.mlproject import logger
from src.mlproject.config.configuration import ConfiguratioManager
import os

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfiguratioManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion= DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    