from fastapi import FastAPI
from .libs.thai_dishes import m_rand

app = FastAPI()

@app.get("/ping")
async def ping():
    return "pong"

@app.get("/")
async def hello_world():
    return {"msg": "Hello World!"}

@app.get("/demo")
async def demo_module():
    return {"dish": m_rand()}
