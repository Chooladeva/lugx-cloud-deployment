from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lugx Order Service",
    openapi_url="/api/orders/openapi.json",
    docs_url="/api/orders/docs",   
    redoc_url=None
)

app.include_router(router, prefix="/api/orders")

@app.get("/api/orders/health")
def health_check():
    return {"status": "ok"}
