from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.user import Users
from schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    @staticmethod
    def create_user_repository(db: Session, user: UserCreate):
        db_user = Users(email=user.email, nome=user.nome, senha_hashed=user.senha)
        
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return db_user

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(Users).filter(Users.email == email).first()
