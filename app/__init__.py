from dotenv import load_dotenv

load_dotenv("config.env")

from .config import Config
from .core.client import BOT

import os

if not os.environ.get("TERMUX_APK_RELEASE"):
    import uvloop
    uvloop.install()

bot = BOT()
