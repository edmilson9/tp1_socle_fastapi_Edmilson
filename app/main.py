from fastapi import FastAPI
from app.api.routers.users_router import router

def create_app() -> FastAPI:
    app = FastAPI(
        title="TP SOCLE FastAPI",
        description="API de gestion des utilisateurs",
        version="1"
    )
    app.include_router(router)
    return app

app = create_app()