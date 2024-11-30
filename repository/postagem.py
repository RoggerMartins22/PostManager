from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.postagem import Postagem
from schemas.postagens import PostagemCreate, StatusEnum

def create_postagem(db: Session, postagem: PostagemCreate):
    db_postagem_existente = db.query(Postagem).filter(Postagem.titulo == postagem.titulo).first()

    if db_postagem_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe uma postagem com esse título"
        )
    
    db_postagem = Postagem(**postagem.dict())
    try:
        db.add(db_postagem)
        db.commit()
        db.refresh(db_postagem)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar postagem: {str(e)}"
        )
    return db_postagem

def get_postagem(db: Session, postagem_id: int):
    postagem = db.query(Postagem).filter(Postagem.id == postagem_id).first()
    
    if not postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Postagem não encontrada"
        )
    return postagem

def get_postagens(db: Session, skip: int = 0, limit: int = 10):
    postagens = db.query(Postagem).offset(skip).limit(limit).all()
    
    if not postagens:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma postagem encontrada"
        )
    
    return postagens


def update_status_postagem(db: Session, postagem_id: int, status: StatusEnum):
    db_postagem = db.query(Postagem).filter(Postagem.id == postagem_id).first()
    if not db_postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Postagem não encontrada"
        )
    
    db_postagem.status = status
    
    try:
        db.commit()
        db.refresh(db_postagem)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao atualizar o status: {str(e)}"
        )
    
    return {
        "message": "Status atualizado com sucesso",
        "postagem": {
            "id": db_postagem.id,
            "titulo": db_postagem.titulo,
            "descricao": db_postagem.descricao,
            "status": db_postagem.status
        }
    }
