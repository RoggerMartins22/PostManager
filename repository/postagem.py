from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.postagem import Postagem
from models.historico_postagem import HistoricoPostagem
from schemas.postagens import PostagemCreate, StatusEnum

def get_postagem_by_titulo(db: Session, titulo: str):
    return db.query(Postagem).filter(Postagem.titulo == titulo).first()


def create_postagem_db(db: Session, postagem: PostagemCreate):
    db_postagem = Postagem(**postagem.dict())
    db.add(db_postagem)
    db.commit()
    db.refresh(db_postagem)
    return db_postagem


def create_historico_postagem(db: Session, postagem_id: int, status: str, mensagem: str = "Postagem Solicitada"):
    db_historico = HistoricoPostagem(
        postagem_id=postagem_id,
        status=status,
        mensagem="Postagem Solicitada"
    )
    db.add(db_historico)
    db.commit()
    db.refresh(db_historico)
    return db_historico


def get_postagem_by_id(db: Session, postagem_id: int):
    return db.query(Postagem).filter(Postagem.id == postagem_id).first()


def get_all_postagens(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Postagem).offset(skip).limit(limit).all()

def update_postagem_status(db: Session, postagem_id: int, statusPostagem: StatusEnum):
    db_postagem = get_postagem_by_id(db, postagem_id)
    
    if not db_postagem:
        return None
    
    db_postagem.status = statusPostagem
    db.commit()
    db.refresh(db_postagem)
    return db_postagem


def update_status_postagem(db: Session, postagem_id: int, statusPostagem: StatusEnum, mensagem: str):
    db_postagem = db.query(Postagem).filter(Postagem.id == postagem_id).first()

    if not db_postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Postagem não encontrada"
        )

    db_postagem.status = statusPostagem

    db_historico = HistoricoPostagem(
        postagem_id=postagem_id,
        status=statusPostagem,
        mensagem=mensagem
    )
    db.add(db_historico)

    try:
        db.commit()
        db.refresh(db_postagem)
        db.refresh(db_historico)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar o status da postagem: {str(e)}"
        )

    return {
        "message": "Status atualizado com sucesso",
        "postagem": {
            "id": db_postagem.id,
            "titulo": db_postagem.titulo,
            "descricao": db_postagem.descricao,
            "mensagem": db_historico.mensagem,
            "status": db_postagem.status
        },
    }