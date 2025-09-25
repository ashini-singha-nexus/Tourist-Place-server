
from fastapi import FastAPI, Request
from app.routers import auth, places
from app.database import create_db_and_tables
import time
import logging
from fastapi.middleware.cors import CORSMiddleware

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

# Allowed origins (your Angular app runs on localhost:4200)
origins = [
    "http://localhost:4200",
    # Add more if needed, e.g. deployed frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] to allow all (not recommended in production)
    allow_credentials=True,
    allow_methods=["*"],              # or specify: ["GET", "POST", "PUT", "DELETE"]
    allow_headers=["*"],              # or specify: ["Authorization", "Content-Type"]
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(places.router, prefix="/places", tags=["places"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tourist Place API"}
