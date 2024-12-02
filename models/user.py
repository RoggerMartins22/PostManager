from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    senha_hashed = Column(String, nullable=False)
    data_cadastro = Column(DateTime, default=lambda: datetime.now() - timedelta(hours=3))
