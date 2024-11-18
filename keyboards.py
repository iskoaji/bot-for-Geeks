from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("О нас"), KeyboardButton("Направления")],
            [KeyboardButton("Контакты")]
        ],
        resize_keyboard=True
    )

def directions_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton("backend"), KeyboardButton("frontend")],
            [KeyboardButton("ux/ui"), KeyboardButton("Назад")]
        ],
        resize_keyboard=True
    )
