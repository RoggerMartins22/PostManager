from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.postagem import PostagemService, PostagemServiceCache
from schemas.postagens import PostagemCreate, PostagemOut, UpdateStatusRequest
from auth import get_current_user
from models.usuario import Usuario
from database import get_db

router = APIRouter(
    prefix="/postagens",
    tags=["Postagens"],
)

@router.post("/cadastrar", response_model=PostagemOut)
async def criar_postagem(postagem: PostagemCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return PostagemService.create_postagem(db=db, postagem=postagem)

@router.get("/{id}", response_model=PostagemOut)
async def consultar_postagem(id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return PostagemServiceCache.listar_postagem_por_id_service(db=db, postagem_id=id)

@router.get("/", response_model=list[PostagemOut])
async def listar_postagens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return PostagemServiceCache.listar_postagens_service(db=db, skip=skip, limit=limit)

@router.patch("/atualizarStatus/{id}")
async def update_status(id: int, request: UpdateStatusRequest, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return PostagemService.update_status_postagem(db=db, postagem_id=id, statusPostagem=request.status, mensagem=request.mensagem)