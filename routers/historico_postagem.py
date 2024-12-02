from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.historico_postagem import HistoricoPostagemCache
from schemas.historico_postagem import HistoricoPostagemBase
from database import get_db
from auth import get_current_user
from models.usuario import Usuario

router = APIRouter(
    prefix="/HistoricoPostagem",
    tags=["HistoricoPostagem"],
)

@router.get("/{postagem_id}", response_model=list[HistoricoPostagemBase])
async def consultar_historico_postagem(postagem_id: int, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return HistoricoPostagemCache.consultar_historico_postagem_service(db=db, postagem_id=postagem_id)
