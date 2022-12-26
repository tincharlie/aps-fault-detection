from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys, os


if __name__ == "__main__":
     try: 
          
          training_pipeline_config = config_entity.training_pipeline_config()
          data_ingestion_config = DataIngestionConfig(training_pipeline_config = training_pipeline_config)
          print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)