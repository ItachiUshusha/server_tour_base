import asyncio
import uvicorn
import requests
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from tg_bot.run_bot import send_message, start_bot

from fastapi.middleware.cors import CORSMiddleware
from model import OrderData

load_dotenv()
app = FastAPI()

secret_key = os.getenv("SECRET_KEY")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def check_captcha(captcha_response: str):
    request = requests.post("https://www.google.com/recaptcha/api/siteverify",
                            data={"secret": secret_key, "response": captcha_response})
    return request.json().get("success", False)

async def run_bot_and_server():
    bot_task = asyncio.create_task(start_bot())
    
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    
    await server.serve()

@app.post("/send-to-telegram")
async def send_to_telegram(order: OrderData):
    if not await check_captcha(order.captcha_response):
        raise HTTPException(status_code=400, detail="Неверная капча")
    await send_message(order)
    

if __name__=='__main__':
    try:
        asyncio.run(run_bot_and_server())
    except KeyboardInterrupt:
        print('Exit')

