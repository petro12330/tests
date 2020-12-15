from fastapi import FastAPI

import base
import api
app = FastAPI()


@app.get("/start")
def read_root(id : int, time : int):
    count = api.main(id, time)
    return {'count': count}


@app.post("/add")
async def show(category:str,region:str):
    id = base.write(category,region)
    return {'id' : id}