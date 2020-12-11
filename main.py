from fastapi import FastAPI
import avito
app = FastAPI()


@app.get("/start")
def read_root(id : int):
    pair = avito.pairs[id]
    # category = pair[0]
    # region = pair[1]
    region = 'mytischi'
    category = 'lada'
    return avito.main(region,category)


@app.post("/add")
async def show(category:str,region:str):
    return avito.Register(category, region).get_id()