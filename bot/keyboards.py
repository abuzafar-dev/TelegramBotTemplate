from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 Men haqimda"), KeyboardButton(text="ℹ️ Yordam")],
    ],
    resize_keyboard=True,
)
