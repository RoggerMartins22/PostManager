from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Postagem(Base):
    __tablename__ = "postagens"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="PN")

    historico = relationship("HistoricoPostagem", back_populates="postagem")
