from aiogram import types
from config import GEOKS_INFO

async def about_handler(message: types.Message):
    await message.answer(GEOKS_INFO, disable_web_page_preview=True)
