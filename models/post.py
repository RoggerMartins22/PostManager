from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from models.user import Base


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descricao = Column(String)
    status = Column(String, default="PN")
    data_criacao = Column(DateTime, default=lambda: datetime.now() - timedelta(hours=3))

    histories = relationship("PostHistory", back_populates="post")
