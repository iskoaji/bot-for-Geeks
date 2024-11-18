from aiogram import types
from keyboards import directions_menu, main_menu
from config import DIRECTIONS

async def directions_handler(message: types.Message):
    if message.text == "Назад":
        await message.answer("Возвращаюсь в главное меню.", reply_markup=main_menu())
    elif message.text in DIRECTIONS:
        direction = DIRECTIONS[message.text]
        await message.answer(
            f"{direction['description']}\nСтоимость: {direction['price']}\nОбучение: {direction['duration']}"
        )
    else:
        await message.answer("Выберите направление:", reply_markup=directions_menu())
