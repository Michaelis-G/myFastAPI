from typing import Annotated
from fastapi import Header, HTTPException
from sqlmodel import Session, create_engine
from os import environ, getenv

DATABASE_URL = getenv(
    "DATABASE_URL",
    "postgresql://admin:password@localhost:5432/fastapi"
)
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "my_fake_token":
        raise HTTPException(status_code = 400, detail = "Token required")

