from aiogram import types
from config import CONTACTS

async def contacts_handler(message: types.Message):
    await message.answer(CONTACTS)
