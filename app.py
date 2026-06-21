from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion=DataIngestionConfig()
        data_ingestion_obj=DataIngestion()
        train_data_path, test_data_path = data_ingestion_obj.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation_obj=DataTransformation()
        data_transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)