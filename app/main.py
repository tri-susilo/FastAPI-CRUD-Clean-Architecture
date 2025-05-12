from fastapi import FastAPI
from app.core.database import init_db
from app.api.v1 import user as user_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(user_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with SQLModel and MySQL"}
