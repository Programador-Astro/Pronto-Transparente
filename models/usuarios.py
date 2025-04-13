from sqlalchemy import Column, Integer, String
from models.base import Base

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
