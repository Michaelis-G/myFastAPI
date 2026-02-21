from fastapi import FastAPI
from pydantic import BaseModel
from Entity import Base
from Entity.User import User, select_users
from sqlalchemy.orm import Session

app = FastAPI()

class UserApi(BaseModel):
    id: int
    name: str

# i have to work with router in the next session

@app.get("/users")
def index():
    users = select_users()
    return {"users": users}

# @app.get("/version")
# def version():
#     return {"version": "0.1.0"}

# @app.get("/item/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/item/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
