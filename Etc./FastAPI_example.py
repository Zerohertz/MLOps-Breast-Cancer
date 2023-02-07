from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item_parameter(item_id: int):
    return {"item_id": item_id}

@app.get("/items/")
def read_item_query(skip: int = 0, limit: int = 10):
    test_db = [{"item_name": "ze", "item_name": "ro", "item_name": "hertz"}]
    return test_db[skip: skip + limit]

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"},
        )
    return item