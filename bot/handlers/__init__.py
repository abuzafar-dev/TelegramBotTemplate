from aiogram import Router

from bot.handlers import echo, start

router = Router()
router.include_routers(start.router, echo.router)
