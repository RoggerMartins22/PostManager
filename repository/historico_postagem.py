from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.historico_postagem import HistoricoPostagem

def get_historico_postagem(db: Session, postagem_id: int):
    historico_postagem = db.query(HistoricoPostagem).filter(HistoricoPostagem.postagem_id == postagem_id).all()
    
    if not historico_postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Historico não encontrado"
        )
    return historico_postagem