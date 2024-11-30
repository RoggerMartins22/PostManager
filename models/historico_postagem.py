from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.postagem import Base
from datetime import datetime, timezone
current_utc_time = datetime.now(timezone.utc)
formatted_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')


class HistoricoPostagem(Base):
    __tablename__ = "historico_postagem"

    id = Column(Integer, primary_key=True, index=True)
    postagem_id = Column(Integer, ForeignKey("postagens.id"), nullable=False)
    status = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=formatted_time)

    postagem = relationship("Postagem", back_populates="historico")
