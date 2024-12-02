from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.post import PostService, PostServiceCache
from schemas.post import PostCreate, PostOut, UpdateStatusRequest
from auth import get_current_user
from models.user import Users
from database import get_db

router = APIRouter(
    prefix="/postagens",
    tags=["Postagens"],
)

@router.post("/cadastrar", response_model=PostOut)
async def create_post(post: PostCreate, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return PostService.create_post(db=db, post=post)

@router.get("/{id}", response_model=PostOut)
async def get_post(id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return PostServiceCache.list_post_by_id_service(db=db, post=id)

@router.get("/", response_model=list[PostOut])
async def list_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return PostServiceCache.list_post_service(db=db, skip=skip, limit=limit)

@router.patch("/atualizarStatus/{id}")
async def update_status(id: int, request: UpdateStatusRequest, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return PostService.update_status_post(db=db, post=id, statusPostagem=request.status, mensagem=request.mensagem)