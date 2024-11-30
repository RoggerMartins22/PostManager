from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    pendente = "PN"
    enviada = "EV"
    entregue = "ET"
    cancelada = "CN"

class HistoricoPostagemBase(BaseModel):
    postagem_id: int
    status: StatusEnum
    mensagem: str
    data_criacao: datetime

    class Config:
        orm_mode = True
