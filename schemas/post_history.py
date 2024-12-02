from pydantic import BaseModel
from datetime import datetime
from schemas.post import StatusEnum

class PostHistoryBase(BaseModel):
    postagem_id: int
    status: StatusEnum
    mensagem: str
    data_criacao: datetime
    
    class Config:
        orm_mode = True
