from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..dependencies import get_token_header, get_session
from ..models.items import Item

router = APIRouter(
    prefix = "/items",
    tags = ["items"],
    dependencies = [Depends(get_token_header)],
    responses = {404: {"description": "Not Found!"}},
)

session = Annotated[Session, Depends(get_session)]

@router.get("")
async def getall(session: session):
    stmt = select(Item)
    items = session.exec(stmt)
    return items.all()

@router.post("")
async def post(item: Item, session: session) -> Item:
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.get("/{id}")
async def get(id: int, session: session) -> Item:
    item = session.get(Item, id)
    if item == None:
        raise HTTPException(status_code = 404, detail = "Item not found")
    return item

@router.put("/{id}")
async def get(id: int, item: Item, session: session) -> Item:
    currentItem = session.get(Item, id)
    if currentItem == None:
        raise HTTPException(status_code = 404, detail = "Item not found")
    item = item.model_dump(exclude_unset=True)
    currentItem.sqlmodel_update(item)
    session.commit()
    # session.refresh(item)
    return item

@router.delete("/{id}")
async def get(id: int, session: session) -> Item:
    item = session.get(Item, id)
    if item == None:
        raise HTTPException(status_code = 404, detail = "Item not found")
    session.delete(item)
    session.commit()
    return item


