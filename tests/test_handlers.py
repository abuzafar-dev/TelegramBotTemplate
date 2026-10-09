import asyncio
import sys
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bot.handlers.main import command_start_handler  # noqa: E402


def greet(full_name):
    message = SimpleNamespace(from_user=SimpleNamespace(full_name=full_name), answer=AsyncMock())
    asyncio.run(command_start_handler(message))
    return message.answer.await_args.args[0]


def test_plain_name_unchanged():
    assert greet("Ali Valiyev") == "Hello, Ali Valiyev!"


def test_special_characters_are_escaped():
    assert greet("<3 Ali & <b>Vali</b>") == "Hello, &lt;3 Ali &amp; &lt;b&gt;Vali&lt;/b&gt;!"


def test_escaped_text_is_valid_telegram_html():
    """Ekranlangan matnda faqat Telegram ruxsat bergan entity'lar qoladi."""
    import re
    text = greet("a<b>c&d")
    assert "<" not in text and ">" not in text
    assert re.fullmatch(r"[^&]*(&(lt|gt|amp|quot);[^&]*)*", text)
