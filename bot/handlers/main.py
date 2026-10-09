import html

from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.dispatcher import dp


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # parse_mode=HTML: ismdagi <, > va & ekranlanmasa Telegram xabarni rad etadi
    # ("can't parse entities") yoki foydalanuvchi o'z ismiga HTML teg qo'sha oladi.
    await message.answer(f"Hello, {html.escape(message.from_user.full_name, quote=False)}!")
