
from fastapi import FastAPI
from app.routers import auth, places
from app.database import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(places.router, prefix="/places", tags=["places"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tourist Place API"}
