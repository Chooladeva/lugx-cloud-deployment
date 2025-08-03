from fastapi import FastAPI
from app.schemas import Event
from app.clickhouse import insert_event
from app.models import create_table
import asyncio

app = FastAPI()

@app.on_event("startup")
def startup():
    create_table()

@app.post("/api/analytics/event")
async def capture_event(event: Event):
    # Run blocking insert_event in threadpool
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, insert_event, event)
    return {"status": "ok"}

@app.get("/api/analytics/event")
async def healthcheck():
    return {"status": "API is up, use POST to send events"}

@app.get("/api/analytics/health")
def health_check():
    return {"status": "ok"}
