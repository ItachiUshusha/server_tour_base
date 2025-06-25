from aiogram import Bot, Dispatcher
import os
from tg_bot.handlers import router
import asyncio
import logging
import os
from dotenv import load_dotenv
from tg_bot.keyboards import settings
from model import OrderData

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN")) 
dp = Dispatcher()
chat_id = os.getenv("CHAT_ID")

async def start_bot():
    dp.include_router(router)
    await dp.start_polling(bot)

async def send_message(order: OrderData):
    message = (
        f"Новый заказ:\n"
        f"<b>Даты:</b> {', '.join(order.dates)}\n"
        f"<b>Количество кроватей:</b> {order.room_type}\n"
        f"<b>Способ связи:</b> {order.connection}\n"
        f"<b>Контакт:</b> {order.user_con}"
    )

    await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML', reply_markup=settings)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print('Exit')
