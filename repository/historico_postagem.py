from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.historico_postagem import HistoricoPostagem


def get_historico_postagem_by_id(db: Session, postagem_id: int):
    return db.query(HistoricoPostagem).filter(HistoricoPostagem.postagem_id == postagem_id).all()
