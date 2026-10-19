import asyncio
from unittest.mock import AsyncMock, MagicMock

from bot.handlers.echo import echo_handler
from bot.handlers.start import about_handler, help_handler, start_handler


def make_message(text=''):
    message = AsyncMock()
    message.text = text
    message.from_user = MagicMock(id=123, full_name='Ali <Valiyev>', username='ali')
    return message


def test_start_escapes_name():
    message = make_message('/start')
    asyncio.run(start_handler(message))
    text = message.answer.call_args.args[0]
    assert 'Ali &lt;Valiyev&gt;' in text


def test_help():
    message = make_message('/help')
    asyncio.run(help_handler(message))
    assert '/start' in message.answer.call_args.args[0]


def test_about():
    message = make_message()
    asyncio.run(about_handler(message))
    text = message.answer.call_args.args[0]
    assert '123' in text
    assert '@ali' in text


def test_echo():
    message = make_message('salom')
    asyncio.run(echo_handler(message))
    message.answer.assert_called_once_with('salom')
