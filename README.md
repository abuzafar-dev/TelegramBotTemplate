# Telegram Bot Template

A minimal aiogram 3 bot skeleton: polling setup, a dataclass-based config
loaded from `.env`, and handlers registered on a shared dispatcher — the
structure to start a new bot from rather than a finished bot.

## Stack

- Python 3.12+
- aiogram 3.31 (long polling)
- python-dotenv

## Getting started

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt

cp .env.example .env          # then set BOT_TOKEN from @BotFather

.venv/bin/python main.py
```

The bot replies to `/start` with a greeting. `load_config()` raises if
`BOT_TOKEN` is missing, so a misconfigured run fails immediately instead of
starting without a token.

## Layout

```
main.py              # entry point: builds the Bot, drops pending updates, starts polling
bot/config.py        # frozen Config dataclass, read from .env
bot/dispatcher.py    # the shared Dispatcher instance
bot/handlers/        # handlers, registered on dp via decorators
```

To add a handler, create a module under `bot/handlers/` and import it in
`bot/handlers/__init__.py` — importing is what registers it on the dispatcher.

## Environment variables

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Telegram bot token from @BotFather (required) |
