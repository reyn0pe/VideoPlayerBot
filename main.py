"""
© thesanzu
"""

import os
from plugins.nopm import User
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN

Bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

Bot.start()
User.start()
print("\n[𝗜𝗡𝗙𝗢] - ᴀᴊɢ ʙᴀʀᴜ ᴊᴜɢᴀ ɴɢᴏᴘɪ ᴅᴀʜ sᴜʀᴜʜ ɴᴀɪᴋ ᴀᴊᴀ sᴀᴍᴀ ᴀɴᴀᴋ ʜᴀʀᴀᴍ, ᴊᴏɪɴ ᴅᴜʟᴜ ʟᴀʜ ʙᴀʙɪ ᴋᴀʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴋᴇʟᴀᴍɪɴ ʟᴏ ʙᴜsᴜᴋ @reyn0pe !")

idle()
Bot.stop()
User.stop()
print("\n[𝗜𝗡𝗙𝗢] - ɢɪᴛᴜ ᴅᴏɴɢ ɢᴜᴇ ᴄᴀᴘᴇ ᴘᴇɴɢᴇɴ ɴɢᴏᴘɪ ᴅᴜʟᴜ, ᴊᴏɪɴ ᴅᴜʟᴜ ʟᴀʜ ʙᴀʙɪ ᴋᴀʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴋᴇʟᴀᴍɪɴ ʟᴏ ʙᴜsᴜᴋ @reyn0pe !")
