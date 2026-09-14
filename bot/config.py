from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    bot_token: str

def load_config() -> Config:
    token = getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN .env faylda topilmadi")
    return Config(bot_token=token)