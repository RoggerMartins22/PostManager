from fastapi import FastAPI
from routers import postagens
from routers import historico_postagem
from routers import usuario

app = FastAPI()

app.include_router(router=postagens.router)
app.include_router(router=historico_postagem.router)
app.include_router(router=usuario.router)

@app.get("/")
async def root():
    return {"message": "API de Postagens funcionando!"}


