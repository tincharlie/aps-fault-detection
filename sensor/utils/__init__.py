import pandas as pd
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException
import sys, os


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Desc: This function returns collection as dataframe.
    :params database_name: database name 
    :params collection_name: collection_name
    =====================================================
    :return: Pandas DataFrame collection of data.
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found Columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id")
            df = df.drop("_id", axis = 1)
        logging.info(f"Rows and Columns: {df.shape}")
        return df

    except Exception as e:
        raise SensorException(e,sys)