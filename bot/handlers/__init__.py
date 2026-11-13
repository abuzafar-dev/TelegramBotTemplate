from aiogram import Router

from bot.handlers import echo, feedback, start

router = Router()
# Tartib muhim: feedback (FSM holatlari) echo dan oldin turishi kerak
router.include_routers(feedback.router, start.router, echo.router)
