from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.usuario import create_user_service
from schemas.usuario import UserCreate, LoginRequest
from auth import authenticate_user, create_access_token
from database import get_db

router = APIRouter(
    prefix="/usuario",
    tags=["users"],
)

@router.post("/cadastrar")
def create_user(usuario: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db=db, usuario=usuario)

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate_user(db, request.email, request.senha)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}