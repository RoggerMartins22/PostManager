from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.user import UserService
from schemas.user import UserCreate, LoginRequest
from auth import authenticate_user, create_access_token
from database import get_db

router = APIRouter(
    prefix="/usuario",
    tags=["users"],
)

@router.post("/cadastrar")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user_service(db=db, user=user)

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.email, request.senha)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciais Inválidas")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}