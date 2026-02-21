from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

engine = create_engine(
    "postgresql://admin:password@localhost:5432/fastapi",
    echo = False
)