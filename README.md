# Telegram Bot Template

aiogram 3 asosidagi oddiy Telegram bot shablon.

## Quick start

```bash
make run     # creates .venv and .env, installs deps, starts the app
make test    # checks + tests
```

## Imkoniyatlar

- `/start` — salomlashish va asosiy menyu
- `/help` yoki "ℹ️ Yordam" tugmasi — yordam
- "👤 Men haqimda" — foydalanuvchi ID, ismi va username
- Boshqa matnlarni qaytaradi (echo)

## Tuzilishi

```
bot/
  config.py        .env dan token o'qish
  keyboards.py     tugmalar
  handlers/
    start.py       /start, /help, men haqimda
    echo.py        echo
main.py            botni ishga tushirish
tests/             testlar
```

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

`.env` ichiga @BotFather dan olingan tokenni yozing va:

```bash
python main.py
```

## Testlar

```bash
pytest
```
