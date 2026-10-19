from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def echo_handler(message: Message):
    await message.answer(message.text)


@router.message()
async def other_handler(message: Message):
    await message.answer("Men faqat matnli xabarlarni tushunaman")
