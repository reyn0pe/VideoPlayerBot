from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Hello**, \n\nKenalin gue **{BOT_NAME}** \nGue bisa play music,streaming youtube,play video juga.! \n\n**Made With ☕️ By @sanzuetc!** 👑"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Buka Obrolan Suara Di Gc Lo!
\u2022 Tambahin Gue (@{USERNAME}) Sama Babu Gue (@{ASSISTANT_NAME}) Ke Gc Lo!
\u2022 Jadiin (@{USERNAME}) Sama (@{ASSISTANT_NAME}) Di Gc Lo!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
