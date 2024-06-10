from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/")
async def hello_world():
    return {"msg": "Hello World!"}

@app.get("/demo")
async def demo_module():
    return {"dish": "xxxx"}
