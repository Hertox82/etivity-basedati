from sqlalchemy import create_engine
from sqlalchemy.engine import URL, Engine
from models import metadata
from dotenv import load_dotenv
import os

load_dotenv()

def define_engine() -> Engine:
    
    url_object = URL.create(
        "mysql+pymysql",
        username="root",
        password="password",
        host=os.environ['MYSQL_HOST'],
        database="ecommerce",
        query={"charset":"utf8mb4"}
    )
    
    engine = create_engine(url_object)
    
    return engine

def create_table(engine):
    print("Sto creando le tabelle...")
    # crea le tabelle riprese da models
    metadata.create_all(engine)
    print("...ho terminato la loro creazione")


