from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from repository.user import UserRepository
from schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def create_user_service(db: Session, user: UserCreate):
        hashed_password = pwd_context.hash(user.senha)
        user.senha = hashed_password
        
        try:
            return UserRepository.create_user_repository(db=db, user=user)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Já existe um usuário com este e-mail cadastrado."
            )
