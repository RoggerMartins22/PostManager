from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.usuario import Base


class Postagem(Base):
    __tablename__ = "postagens"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="PN")
    data_criacao = Column(DateTime, default=func.now())

    historico = relationship("HistoricoPostagem", back_populates="postagem")
