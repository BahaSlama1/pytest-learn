from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app import database

app = FastAPI()


class ItemCreate(BaseModel):
    name: str


class Item(BaseModel):
    id: int
    name: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items", response_model=list[Item])
def list_items():
    return database.get_all_items()


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate):
    return database.add_item(payload.name)


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = database.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="not found")
    return item
