from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.usuario import Usuario
from schemas.usuario import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, usuario: UserCreate):
    db_usuario = Usuario(email=usuario.email, nome=usuario.nome, senha_hashed=usuario.senha)
    
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
