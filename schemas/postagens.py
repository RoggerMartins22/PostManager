from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    pendente = "PN"
    enviada = "EV"
    entregue = "ET"
    cancelada = "CN"

class PostagemBase(BaseModel):
    titulo: str
    descricao: str

class PostagemCreate(PostagemBase):
    status: StatusEnum = StatusEnum.pendente

class PostagemOut(PostagemBase):
    id: int
    status: StatusEnum

    class Config:
        orm_mode = True

class UpdateStatusRequest(BaseModel):
    status: StatusEnum