"""
© thesanzu
"""

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

bot = Client(
    "VideoPlayer",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)
bot.start()
ok = bot.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
