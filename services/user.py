from sqlalchemy.orm import Session
from repository.user import UserRepository
from schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def create_user_service(db: Session, user: UserCreate):
        hashed_password = pwd_context.hash(user.senha)
        user.senha = hashed_password
        return UserRepository.create_user_repository(db=db, user=user)
