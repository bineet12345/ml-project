from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_tranier import ModelTrainerConfig, ModelTrainer
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion=DataIngestionConfig()
        data_ingestion_obj=DataIngestion()
        train_data_path, test_data_path = data_ingestion_obj.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation_obj=DataTransformation()
        train_arr,test_arr,_ =data_transformation_obj.initiate_data_transformation(train_data_path, test_data_path)

        #model_trainer_config=ModelTrainerConfig()
        model_trainer_obj=ModelTrainer()
        print(model_trainer_obj.initiate_model_trainer(train_arr, test_arr))

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)