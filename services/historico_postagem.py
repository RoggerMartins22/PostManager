from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.historico_postagem import get_historico_postagem_by_id

def get_historico_postagem(db: Session, postagem_id: int):
    historico_postagem = get_historico_postagem_by_id(db, postagem_id)

    if not historico_postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Histórico não encontrado"
        )
    
    return historico_postagem