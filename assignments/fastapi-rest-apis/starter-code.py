from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="My API", description="A simple REST API built with FastAPI")

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

# In-memory storage for items
items = []

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment!"}

# TODO: Implement the remaining endpoints here

# GET /items - Get all items
@app.get("/items", response_model=List[Item])
def get_items():
    return items

# POST /items - Create a new item
@app.post("/items", response_model=Item)
def create_item(item: Item):
    # Check if item with same id already exists
    if any(existing_item.id == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item)
    return item

# TODO: Add the remaining CRUD endpoints