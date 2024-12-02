from sqlalchemy.orm import Session
from models.post_history import PostHistory

class PostHistoryRepository:
    @staticmethod
    def get_post_history_by_id(db: Session, postagem_id: int):
        return db.query(PostHistory).filter(PostHistory.postagem_id == postagem_id).all()


    @staticmethod
    def create_post_history(db: Session, postagem_id: int, status: str, mensagem: str = "Postagem Solicitada"):
        db_history = PostHistory(
            postagem_id=postagem_id,
            status=status,
            mensagem=mensagem
        )
        db.add(db_history)
        db.commit()
        db.refresh(db_history)
        return db_history