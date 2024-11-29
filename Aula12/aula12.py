from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# Obter dados

try: 
    print('Obtendo dados..')
    # Carregar variaveis de ambiente do arquivo .env
    load_dotenv

    # Obtendo as variaveis de ambiente
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    user = os.getenv('DB_USER')
    passaword = os.getenv('DB_PASSAWORD')
    database = os.getenv('DB_DATABASE')

    engine = create_engine(f'mysql+pymysql://{user}:{passaword}@{host}:{port}/{database}')
    