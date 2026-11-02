import sys
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging

from src.entity.config_entity import TrainingPipelineConfig

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

if __name__ == '__main__':
    try:
        trainingpipelineconfig= TrainingPipelineConfig()
        dataingestionconfig= DataIngestionConfig(trainingpipelineconfig)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact= data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
