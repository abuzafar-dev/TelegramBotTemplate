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
- "⭐ Baho berish" yoki `/feedback` — **FSM** namunasi: 1–5 yulduz (★★★☆☆) → izoh → natija
- Deep-link / QR: `https://t.me/<bot>?start=filial_3` → baho so'raladi, `filial_3` manba sifatida saqlanadi
- `/cancel` — har qanday holatdan chiqish
- Boshqa matnlarni qaytaradi (echo)

## Tuzilishi

```
bot/
  config.py        .env dan token o'qish
  keyboards.py     tugmalar (reply + inline yulduzchalar)
  states.py        FSM holatlari
  handlers/
    feedback.py    baho FSM, deep-link /start, inline callback
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
