from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)  # Removi unique do nome, pois você pode ter nomes iguais
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hashed = Column(String, nullable=False)  # Alterei o nome para refletir o hash da senha
    data_cadastro = Column(DateTime, default=func.now())
