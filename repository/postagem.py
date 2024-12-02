from sqlalchemy.orm import Session
from models.postagem import Postagem
from schemas.postagens import PostagemCreate, StatusEnum

class PostagemRepository:

    @staticmethod
    def get_postagem_by_titulo(db: Session, titulo: str):
        return db.query(Postagem).filter(Postagem.titulo == titulo).first()

    @staticmethod
    def create_postagem_db(db: Session, postagem: PostagemCreate):
        db_postagem = Postagem(**postagem.dict())
        db.add(db_postagem)
        db.commit()
        db.refresh(db_postagem)
        return db_postagem

    @staticmethod
    def get_postagem_by_id(db: Session, postagem_id: int):
        return db.query(Postagem).filter(Postagem.id == postagem_id).first()

    @staticmethod
    def get_all_postagens(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Postagem).offset(skip).limit(limit).all()

    @staticmethod
    def update_postagem_status(db: Session, postagem_id: int, statusPostagem: StatusEnum):
        db_postagem = PostagemRepository.get_postagem_by_id(db, postagem_id)
        
        if not db_postagem:
            return None
        
        db_postagem.status = statusPostagem
        db.commit()
        db.refresh(db_postagem)
        return db_postagem