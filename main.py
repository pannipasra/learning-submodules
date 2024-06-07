from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/")
async def hello_world():
    return {"msg": "Hello World!"}
