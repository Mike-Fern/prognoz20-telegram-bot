import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
REDIRECT_URL = os.getenv("REDIRECT_URL")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("💸 ЗАБРАТЬ ПРОГНОЗ / БОНУС", url=REDIRECT_URL)
    )
    await message.answer(
        "Добро пожаловать в «Прогнозы 2.0» 💰\n"
        "🔥 Только точные прогнозы и бонусы до +500% на первое пополнение.\n\n"
        "⏬ Жми кнопку ниже ⏬",
        reply_markup=keyboard
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
