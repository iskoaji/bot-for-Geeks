from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from handlers import start_handler, about_handler, directions_handler, contacts_handler

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await start_handler(message)

@dp.message_handler(lambda message: message.text == "О нас")
async def about(message: types.Message):
    await about_handler(message)

@dp.message_handler(lambda message: message.text in ["Направления", "backend", "frontend", "ux/ui", "Назад"])
async def directions(message: types.Message):
    await directions_handler(message)

@dp.message_handler(lambda message: message.text == "Контакты")
async def contacts(message: types.Message):
    await contacts_handler(message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
