from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.post import PostRepository
from repository.post_history import PostHistoryRepository
from utils.cache import SystemCache
from schemas.post import PostCreate, StatusEnum, PostOut

class PostService:

    @staticmethod
    def create_post(db: Session, post: PostCreate):
        db_post_existis = PostRepository.get_post_by_title(db, post.titulo)

        if db_post_existis:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Já existe uma postagem com esse título"
            )
        
        db_post = PostRepository.create_post_db(db, post)

        try:
            PostHistoryRepository.create_post_history(db, db_post.id, db_post.status)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao criar histórico de postagem: {str(e)}"
            )
        
        return db_post

    @staticmethod
    def get_post(db: Session, post: int):
        post = PostRepository.get_post_by_id(db, post)
        
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Postagem não encontrada"
            )
        
        return post

    @staticmethod
    def get_posts(db: Session, skip: int = 0, limit: int = 10):
        posts = PostRepository.get_all_posts(db, skip, limit)
        
        if not posts:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Nenhuma postagem encontrada"
            )
        
        return posts
    
    @staticmethod
    def update_status_post(db: Session, post: int, statusPostagem: StatusEnum, mensagem: str):
        db_post = PostRepository.get_post_by_id(db, post)

        if not db_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Postagem não encontrada"
            )
        updated_post = PostRepository.update_post_status(db, post, statusPostagem)

        if not updated_post:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Erro ao atualizar o status da postagem"
            )

        db_history = PostHistoryRepository.create_post_history(db, post, statusPostagem, mensagem)

        return {
            "message": "Status atualizado com sucesso",
            "postagem": {
                "id": updated_post.id,
                "titulo": updated_post.titulo,
                "descricao": updated_post.descricao,
                "mensagem": db_history.mensagem,
                "status": updated_post.status
            },
        }
    

class PostServiceCache:
    @staticmethod
    def list_post_service(db: Session, skip: int = 0, limit: int = 10):
        cache_key = f"postagens:{skip}:{limit}"
        
        post_cache = SystemCache.get_cache(cache_key)
        if post_cache:
            return post_cache

        posts = PostService.get_posts(db=db, skip=skip, limit=limit)
        
        posts_dict = [PostOut.from_orm(post).dict() for post in posts]

        SystemCache.set_cache(cache_key, posts_dict)

        return posts
    
    @staticmethod
    def list_post_by_id_service(db: Session, post: int):
        cache_key = f"postagem:{post}"

        post_cache = SystemCache.get_cache(cache_key)
        if post_cache:
            return post_cache

        posts = PostService.get_post(db=db, post=post)

        if not posts:
            return None

        post_dict = PostOut.from_orm(posts).dict() 
        SystemCache.set_cache(cache_key, post_dict)

        return post_dict