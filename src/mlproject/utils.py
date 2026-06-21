import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

import pickle
import numpy as np

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading data from mysql database started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            ssl_disabled=True  # 1. Fixes the ssl.SSLError: [ASN1: NOT_ENOUGH_DATA] bug
        )
        # 2. Fixes logging syntax (changed from comma to f-string format)
        logging.info(f"Connection established: {mydb}") 
        
        df = pd.read_sql('Select * from students', mydb)
        print(df.head())

        return df
    except Exception as ex:
        # 3. Fixes the TypeError by passing 'sys' to provide error details
        raise CustomException(ex, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)