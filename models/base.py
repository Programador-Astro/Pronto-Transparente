from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

# Dados da conexão
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "3306")
DB = os.getenv("DB_NAME")

# String de conexão
URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

# Criação do engine e base
engine = create_engine(URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)