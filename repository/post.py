from sqlalchemy.orm import Session
from models.post import Post
from schemas.post import PostCreate, StatusEnum

class PostRepository:

    @staticmethod
    def get_post_by_title(db: Session, titulo: str):
        return db.query(Post).filter(Post.titulo == titulo).first()

    @staticmethod
    def create_post_db(db: Session, postagem: PostCreate):
        db_post = Post(**postagem.dict())
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    def get_post_by_id(db: Session, post: int):
        return db.query(Post).filter(Post.id == post).first()

    @staticmethod
    def get_all_posts(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Post).offset(skip).limit(limit).all()

    @staticmethod
    def update_post_status(db: Session, post: int, statusPostagem: StatusEnum):
        db_post = PostRepository.get_post_by_id(db, post)
        
        if not db_post:
            return None
        
        db_post.status = statusPostagem
        db.commit()
        db.refresh(db_post)
        return db_post