from models.usuarios import Usuario
from models.base import engine, Base
#from models.calculo import Calculo

def criar_tabelas():
    Base.metadata.create_all(bind=engine)