from fastapi import FastAPI
from routers import postagens

app = FastAPI()

app.include_router(router=postagens.router)

@app.get("/")
async def root():
    return {"message": "API de Postagens funcionando!"}


