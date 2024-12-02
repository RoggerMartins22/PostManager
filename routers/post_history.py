from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.post_history import PostHistoryCache
from schemas.post_history import PostHistoryBase
from database import get_db
from auth import get_current_user
from models.user import Users

router = APIRouter(
    prefix="/HistoricoPostagem",
    tags=["HistoricoPostagem"],
)

@router.get("/{postagem_id}", response_model=list[PostHistoryBase])
async def get_post_history(postagem_id: int, db: Session = Depends(get_db), current_user: Users = Depends(get_current_user)):
    return PostHistoryCache.get_post_history_cache(db=db, postagem_id=postagem_id)
