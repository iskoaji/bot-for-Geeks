from aiogram import types
from keyboards import main_menu

async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Я Geeks бот . Чем могу помочь?",
        reply_markup=main_menu()
    )
