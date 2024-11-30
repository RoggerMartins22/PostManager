from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from repository.postagem import create_postagem, get_postagem, get_postagens, update_status_postagem
from schemas.postagens import PostagemCreate, PostagemOut, StatusEnum, UpdateStatusRequest
from database import get_db

router = APIRouter(
    prefix="/postagens",
    tags=["Postagens"],
)

@router.post("/cadastrar", response_model=PostagemOut)
async def criar_postagem(postagem: PostagemCreate, db: Session = Depends(get_db)):
    return create_postagem(db=db, postagem=postagem)

@router.get("/{id}", response_model=PostagemOut)
async def consultar_postagem(id: int, db: Session = Depends(get_db)):
    postagem = get_postagem(db=db, postagem_id=id)
    if not postagem:
        raise HTTPException(status_code=404, detail="Postagem não encontrada")
    return postagem

@router.get("/", response_model=list[PostagemOut])
async def listar_postagens(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_postagens(db=db, skip=skip, limit=limit)

@router.patch("/atualizarStatus/{id}")
def update_status(id: int, request: UpdateStatusRequest, db: Session = Depends(get_db)):
    return update_status_postagem(db=db, postagem_id=id, status=request.status)