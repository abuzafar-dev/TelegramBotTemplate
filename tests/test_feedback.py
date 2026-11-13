import asyncio
from unittest.mock import AsyncMock, MagicMock

from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.base import StorageKey
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers.feedback import (
    comment_skipped,
    comment_written,
    feedback_start,
    rating_chosen,
    start_deep_link,
)
from bot.keyboards import rating_keyboard, stars
from bot.states import FeedbackState


def make_state():
    return FSMContext(storage=MemoryStorage(), key=StorageKey(bot_id=1, chat_id=1, user_id=1))


def make_message(text=''):
    message = AsyncMock()
    message.text = text
    return message


def make_callback(data):
    callback = AsyncMock()
    callback.data = data
    callback.message = AsyncMock()
    return callback


def test_stars():
    assert stars(3) == '★★★☆☆'
    assert stars(5) == '★★★★★'
    assert [row[0].text for row in rating_keyboard().inline_keyboard][0] == '★☆☆☆☆'


def test_full_flow_with_comment():
    async def run():
        state = make_state()
        await feedback_start(make_message('/feedback'), state)
        assert await state.get_state() == FeedbackState.rating.state

        callback = make_callback('rating:4')
        await rating_chosen(callback, state)
        assert await state.get_state() == FeedbackState.comment.state
        assert '★★★★☆' in callback.message.edit_text.call_args.args[0]

        message = make_message('Zo\'r <b>xizmat</b>')
        await comment_written(message, state)
        text = message.answer.call_args.args[0]
        assert '★★★★☆' in text
        assert '&lt;b&gt;' in text  # HTML escape
        assert await state.get_state() is None

    asyncio.run(run())


def test_deep_link_source_and_skip():
    async def run():
        state = make_state()
        await start_deep_link(make_message('/start filial_3'), CommandObject(command='start', args='filial_3'), state)
        await rating_chosen(make_callback('rating:2'), state)
        callback = make_callback('comment:skip')
        await comment_skipped(callback, state)
        text = callback.message.edit_text.call_args.args[0]
        assert '★★☆☆☆' in text
        assert 'filial_3' in text

    asyncio.run(run())


def test_invalid_rating_rejected():
    async def run():
        state = make_state()
        await feedback_start(make_message(), state)
        callback = make_callback('rating:9')
        await rating_chosen(callback, state)
        assert await state.get_state() == FeedbackState.rating.state
        callback.answer.assert_called_once()

    asyncio.run(run())
