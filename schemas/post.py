from pydantic import BaseModel
from enum import Enum

class StatusEnum(str, Enum):
    pendente = "PN"
    enviada = "EV"
    entregue = "ET"
    cancelada = "CN"

class PostBase(BaseModel):
    titulo: str
    descricao: str

class PostCreate(PostBase):
    status: StatusEnum = StatusEnum.pendente

class PostOut(PostBase):
    id: int
    status: StatusEnum

    class Config:
        orm_mode = True

class UpdateStatusRequest(BaseModel):
    status: StatusEnum
    mensagem: str