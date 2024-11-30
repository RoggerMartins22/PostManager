from pydantic import BaseModel
from datetime import datetime
from schemas.postagens import StatusEnum

class HistoricoPostagemBase(BaseModel):
    postagem_id: int
    status: StatusEnum
    mensagem: str
    data_criacao: datetime
    
    class Config:
        orm_mode = True
