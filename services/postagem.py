from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.postagem import get_postagem_by_titulo, create_postagem_db, create_historico_postagem, get_postagem_by_id, get_all_postagens, update_postagem_status
from schemas.postagens import PostagemCreate, StatusEnum


def create_postagem(db: Session, postagem: PostagemCreate):
    db_postagem_existente = get_postagem_by_titulo(db, postagem.titulo)

    if db_postagem_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe uma postagem com esse título"
        )
    
    db_postagem = create_postagem_db(db, postagem)

    try:
        create_historico_postagem(db, db_postagem.id, db_postagem.status)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao criar histórico de postagem: {str(e)}"
        )

    return db_postagem


def get_postagem(db: Session, postagem_id: int):
    postagem = get_postagem_by_id(db, postagem_id)
    
    if not postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Postagem não encontrada"
        )
    
    return postagem


def get_postagens(db: Session, skip: int = 0, limit: int = 10):
    postagens = get_all_postagens(db, skip, limit)
    
    if not postagens:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nenhuma postagem encontrada"
        )
    
    return postagens

def update_status_postagem(db: Session, postagem_id: int, statusPostagem: StatusEnum, mensagem: str):
    db_postagem = get_postagem_by_id(db, postagem_id)

    if not db_postagem:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Postagem não encontrada"
        )
    updated_postagem = update_postagem_status(db, postagem_id, statusPostagem)

    if not updated_postagem:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao atualizar o status da postagem"
        )

    db_historico = create_historico_postagem(db, postagem_id, statusPostagem, mensagem)

    return {
        "message": "Status atualizado com sucesso",
        "postagem": {
            "id": updated_postagem.id,
            "titulo": updated_postagem.titulo,
            "descricao": updated_postagem.descricao,
            "mensagem": db_historico.mensagem,
            "status": updated_postagem.status
        },
    }