from aiogram import F, Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.keyboards import main_menu

router = Router()

HELP_TEXT = (
    "Buyruqlar:\n"
    "/start - botni ishga tushirish\n"
    "/help - yordam\n\n"
    "Istalgan matn yozsangiz, bot uni qaytaradi."
)


@router.message(CommandStart())
async def start_handler(message: Message):
    name = html.quote(message.from_user.full_name)
    await message.answer(f"Assalomu alaykum, <b>{name}</b>!", reply_markup=main_menu)


@router.message(Command('help'))
@router.message(F.text == "ℹ️ Yordam")
async def help_handler(message: Message):
    await message.answer(HELP_TEXT)


@router.message(F.text == "👤 Men haqimda")
async def about_handler(message: Message):
    user = message.from_user
    username = f"@{user.username}" if user.username else "yo'q"
    await message.answer(
        f"ID: <code>{user.id}</code>\n"
        f"Ism: {html.quote(user.full_name)}\n"
        f"Username: {username}"
    )
