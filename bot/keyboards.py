from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

BTN_ABOUT = "👤 Men haqimda"
BTN_HELP = "ℹ️ Yordam"
BTN_FEEDBACK = "⭐ Baho berish"

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_ABOUT), KeyboardButton(text=BTN_HELP)],
        [KeyboardButton(text=BTN_FEEDBACK)],
    ],
    resize_keyboard=True,
)


def stars(rating: int) -> str:
    """3 -> ★★★☆☆ (to'lgan va bo'sh yulduzchalar)"""
    return "★" * rating + "☆" * (5 - rating)


def rating_keyboard() -> InlineKeyboardMarkup:
    # Har bir tugmada nechta yulduz to'lgani ko'rinadi: ★☆☆☆☆ ... ★★★★★
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=stars(i), callback_data=f"rating:{i}")] for i in range(1, 6)
    ])


skip_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⏭ O'tkazib yuborish", callback_data="comment:skip")],
])
