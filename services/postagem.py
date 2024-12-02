from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.postagem import PostagemRepository
from repository.historico_postagem import HistoricoPostagemRepository
from utils.cache import SystemCache
from schemas.postagens import PostagemCreate, StatusEnum, PostagemOut

class PostagemService:

    @staticmethod
    def create_postagem(db: Session, postagem: PostagemCreate):
        db_postagem_existente = PostagemRepository.get_postagem_by_titulo(db, postagem.titulo)

        if db_postagem_existente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Já existe uma postagem com esse título"
            )
        
        db_postagem = PostagemRepository.create_postagem_db(db, postagem)

        try:
            HistoricoPostagemRepository.create_historico_postagem(db, db_postagem.id, db_postagem.status)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar histórico de postagem: {str(e)}"
            )
        
        return db_postagem

    @staticmethod
    def get_postagem(db: Session, postagem_id: int):
        postagem = PostagemRepository.get_postagem_by_id(db, postagem_id)
        
        if not postagem:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Postagem não encontrada"
            )
        
        return postagem

    @staticmethod
    def get_postagens(db: Session, skip: int = 0, limit: int = 10):
        postagens = PostagemRepository.get_all_postagens(db, skip, limit)
        
        if not postagens:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Nenhuma postagem encontrada"
            )
        
        return postagens
    
    @staticmethod
    def update_status_postagem(db: Session, postagem_id: int, statusPostagem: StatusEnum, mensagem: str):
        db_postagem = PostagemRepository.get_postagem_by_id(db, postagem_id)

        if not db_postagem:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Postagem não encontrada"
            )
        updated_postagem = PostagemRepository.update_postagem_status(db, postagem_id, statusPostagem)

        if not updated_postagem:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro ao atualizar o status da postagem"
            )

        db_historico = HistoricoPostagemRepository.create_historico_postagem(db, postagem_id, statusPostagem, mensagem)

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
    

class PostagemServiceCache:
    @staticmethod
    def listar_postagens_service(db: Session, skip: int = 0, limit: int = 10):
        cache_key = f"postagens:{skip}:{limit}"
        
        postagens_cache = SystemCache.get_cache(cache_key)
        if postagens_cache:
            return postagens_cache

        postagens = PostagemService.get_postagens(db=db, skip=skip, limit=limit)
        
        postagens_dict = [PostagemOut.from_orm(postagem).dict() for postagem in postagens]

        SystemCache.set_cache(cache_key, postagens_dict)

        return postagens
    
    @staticmethod
    def listar_postagem_por_id_service(db: Session, postagem_id: int):
        cache_key = f"postagem:{postagem_id}"
        
        postagem_cache = SystemCache.get_cache(cache_key)
        if postagem_cache:
            return postagem_cache 

        postagem = PostagemService.get_postagem(db=db, postagem_id=postagem_id)
        
        if not postagem:
            return None 

        postagem_dict = PostagemOut.from_orm(postagem).dict()
        SystemCache.set_cache(cache_key, postagem_dict)

        return postagem_dict