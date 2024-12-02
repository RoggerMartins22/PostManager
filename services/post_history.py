from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from repository.post_history import PostHistoryRepository
from schemas.post_history import PostHistoryBase
from utils.cache import SystemCache

class PostHistoryService:
    @staticmethod
    def get_post_history(db: Session, postagem_id: int):
        post_history = PostHistoryRepository.get_post_history_by_id(db, postagem_id)

        if not post_history:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Histórico não encontrado"
            )
        
        return post_history
    
class PostHistoryCache:
    @staticmethod
    def get_post_history_cache(db: Session, postagem_id: int):
        cache_key = f"historico_postagem:{postagem_id}"
        
        history_cache = SystemCache.get_cache(cache_key)
        if history_cache:
            return history_cache

        post_history = PostHistoryService.get_post_history(db=db, postagem_id=postagem_id)
        
        if not post_history:
            return []
        
        history_dict = [PostHistoryBase.from_orm(item).dict() for item in post_history]
        SystemCache.set_cache(cache_key, history_dict)

        return history_dict