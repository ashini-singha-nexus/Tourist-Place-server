
from fastapi import FastAPI, Request
from app.routers import auth, places
from app.database import create_db_and_tables
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    logger.info(f"Handled request {request.method} {request.url.path} in {duration:.2f}s")
    return response

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(places.router, prefix="/places", tags=["places"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tourist Place API"}
