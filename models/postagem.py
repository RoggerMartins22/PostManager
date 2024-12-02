from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from models.usuario import Base


class Postagem(Base):
    __tablename__ = "postagens"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="PN")
    data_criacao = Column(DateTime, default=lambda: datetime.now() - timedelta(hours=3))

    historico = relationship("HistoricoPostagem", back_populates="postagem")
