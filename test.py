from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name: str

@app.post("/create")
async def create(data: Data):
    return {"data": data}

@app.get("/test/{item_id}")
async def test(item_id: str, game_id = int):
    return{"hello": item_id}