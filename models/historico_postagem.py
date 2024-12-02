from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from models.usuario import Base

class HistoricoPostagem(Base):
    __tablename__ = "historico_postagem"

    id = Column(Integer, primary_key=True, index=True)
    postagem_id = Column(Integer, ForeignKey("postagens.id"), nullable=False)
    status = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=lambda: datetime.now() - timedelta(hours=3))

    postagem = relationship("Postagem", back_populates="historico")

