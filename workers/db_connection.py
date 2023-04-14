import os
from dotenv import load_dotenv
import sqlalchemy as sa

load_dotenv()
DATABASE = os.getenv("DATABASE")
USER = os.getenv("USERDB")
PASSWORD = os.getenv("PWDDB")
HOST = os.getenv("HOSTDB")
PORT = os.getenv("PORTDB")

def db_con():
    connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (
        USER,
        PASSWORD,
        HOST,
        PORT,
        DATABASE,
    )
    engine = sa.create_engine(connection_string)
   # connection = engine.connect()
    
    return engine
     
db_con()
