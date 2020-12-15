from fastapi import FastAPI

import base
import api
app = FastAPI()


@app.get("/start")
def read_root(id : int, time : int):
    api.main(id, time)
    return


@app.post("/add")
async def show(category:str,region:str):
    id = base.write(category,region)
    return {'id' : id}