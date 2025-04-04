#constantes que se usan en el codigo, para que el cpdigo se vea más limpio
#constants we use on our code, so the coding is cleaner

import os
from dotenv import load_dotenv

load_dotenv()
POSTGRES_USER=os.getenv('POSTGRES_USER')
POSTGRES_HOST= os.getenv('POSTGRES_HOST')
POSTGRES_PWD=os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB=os.getenv('POSTGRES_DB')
POSTGRES_PORT=os.getenv('POSTGRES_PORT')

COINMARKET_KEY=os.getenv('COINMARKET_API')

CLUSTER_ID=os.getenv('CLUSTER_ID')

