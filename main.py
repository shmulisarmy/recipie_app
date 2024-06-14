import os, time
from fastapi import FastAPI, Depends, HTTPException, status, Request, APIRouter, WebSocket
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import List, Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory='templates')
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
@app.get('/recipes')
async def index():
    return recipes


@app.websocket("/ws")
async def websocket_main(webSocket: WebSocket):
    await webSocket.accept()
    print(f"connection from {webSocket}")
    await webSocket.send_text("alert-hello from server")
    while True:
        text = await webSocket.receive_text()
        if text:
            recieved_messages.append(text)
            print(f"recieved: {text}")

recieved_messages = []



recipes = [
            {
                "name": "shepherd's pie",
                "oven temp": 350,
                "cook time": 30,
                "ingredients": [
                    { "ingredient": "potatoes", "amount": 3 },
                    { "ingredient": "meat", "amount": 2 },
                    { "ingredient": "eggs", "amount": 4 }
                ]
            },
            {
                "name": "spaghetti bolognese",
                "oven temp": 350,
                "cook time": 30,
                "ingredients": [
                    { "ingredient": "spaghetti", "amount": 1 },
                    { "ingredient": "ground beef", "amount": 1 },
                    { "ingredient": "tomato sauce", "amount": 1 }
                ]
            },
            {
                "name": "chocolate chip cookies",
                "oven temp": 350,
                "cook time": 30,
                "ingredients": [
                    { "ingredient": "flour", "amount": 2 },
                    { "ingredient": "sugar", "amount": 1 },
                    { "ingredient": "chocolate chips", "amount": 1 },
                    { "ingredient": "butter", "amount": 1 }
                ]
            }
        ]



link = 'http://127.0.0.1:8000'
for route in app.routes[3:]:
    print(route)

    # print(f"{link}{route.path}")

os.system("open http://127.0.0.1:8000")
#run command: uvicorn main:app --reload

