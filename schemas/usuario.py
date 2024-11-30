from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    email: str

class UserCreate(UsuarioBase):
    senha: str

class LoginRequest(BaseModel):
    email: str
    senha: str
    
class UserOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True