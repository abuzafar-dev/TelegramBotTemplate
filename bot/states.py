from aiogram.fsm.state import State, StatesGroup


class FeedbackState(StatesGroup):
    rating = State()   # 1-5 yulduz tanlashni kutish
    comment = State()  # izoh matnini kutish
