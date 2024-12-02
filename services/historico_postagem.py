from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.historico_postagem import HistoricoPostagemRepository
from schemas.historico_postagem import HistoricoPostagemBase
from utils.cache import SystemCache

class HistoricoPostagemService:
    @staticmethod
    def get_historico_postagem(db: Session, postagem_id: int):
        historico_postagem = HistoricoPostagemRepository.get_historico_postagem_by_id(db, postagem_id)

        if not historico_postagem:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Histórico não encontrado"
            )
        
        return historico_postagem
    
class HistoricoPostagemCache:
    @staticmethod
    def consultar_historico_postagem_service(db: Session, postagem_id: int):
        cache_key = f"historico_postagem:{postagem_id}"
        
        historico_cache = SystemCache.get_cache(cache_key)
        if historico_cache:
            return historico_cache

        historico_postagem = HistoricoPostagemService.get_historico_postagem(db=db, postagem_id=postagem_id)
        
        if not historico_postagem:
            return []
        
        historico_dict = [HistoricoPostagemBase.from_orm(item).dict() for item in historico_postagem]
        SystemCache.set_cache(cache_key, historico_dict)

        return historico_dict