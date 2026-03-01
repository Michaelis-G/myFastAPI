from fastapi import FastAPI, Depends
from .routers import items
from sqlmodel import SQLModel, Session, create_engine
from .models.items import Item
from .dependencies import engine

app = FastAPI()
app.include_router(items.router)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)    

@app.get("/")
def index():
    return {"message": "this is my first API!"}