from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lugx Game Service",
    openapi_url="/api/games/openapi.json",
    docs_url="/api/games/docs",       
    redoc_url=None
)

app.include_router(router, prefix="/api/games")

@app.get("/api/games/health")
def health_check():
    return {"status": "ok"}
