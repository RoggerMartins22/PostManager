from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routers import postagens, historico_postagem, usuario

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Gerenciador de Postagem",
        version="1.0.0",
        description="Sistema para gerenciar fluxo de postagem de serviços de correios!",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
         "BearerAuth":{
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Bearer Token"
         }

    }

    openapi_schema["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


app.include_router(postagens.router)
app.include_router(historico_postagem.router)
app.include_router(usuario.router)
