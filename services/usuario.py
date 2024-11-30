from sqlalchemy.orm import Session
from repository.usuario import create_user
from schemas.usuario import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user_service(db: Session, usuario: UserCreate):
    hashed_password = pwd_context.hash(usuario.senha)
    usuario.senha = hashed_password
    return create_user(db=db, usuario=usuario)
