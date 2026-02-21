from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from Entity import User, Base

app = FastAPI()
engine = create_engine(
    "postgresql://admin:password@localhost:5432/fastapi",
    echo= False
)

class Item(BaseModel):
    name: str
    price: float
    is_onsale: bool | None = None

@app.get("/")
def index():
    return {"app": "MyFastAPI"}

@app.get("/version")
def version():
    return {"version": "0.1.0"}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if (__name__ == "__main__"):
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        mika = User.User(name = 'michaelis')
        bob = User.User(name = 'bob')
        # session.add_all([mika, bob])
        User.select_users(session)
        session.commit()