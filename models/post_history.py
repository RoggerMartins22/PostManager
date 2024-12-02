from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from models.user import Base

class PostHistory(Base):
    __tablename__ = "post_history"

    id = Column(Integer, primary_key=True, index=True)
    postagem_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    status = Column(String, nullable=False)
    mensagem = Column(String, nullable=False)
    data_criacao = Column(DateTime, default=lambda: datetime.now() - timedelta(hours=3))

    post = relationship("Post", back_populates="histories")

