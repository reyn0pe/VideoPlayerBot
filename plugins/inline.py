"""
© thesanzu
"""

import asyncio
from config import REPLY_MESSAGE
from pyrogram import Client, errors
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch


buttons = [
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/TheSanzuXD"),
                InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/reyn0pe"),
            ],
            [
                InlineKeyboardButton("ᴏʀᴅᴇʀ ʙᴏᴛ", url="https://t.me/sanzetc"),
            ]
         ]

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "SAF_ONE":
        answers.append(
            InlineQueryResultArticle(
                title="ᴛᴇʀᴀᴘᴋᴀɴ ʙᴏᴛ ᴘᴇᴍᴜᴛᴀʀ ᴠɪᴅᴇᴏ sᴇɴᴅɪʀɪ",
                input_message_content=InputTextMessageContent(f"{REPLY_MESSAGE}\n\n<b>© ᴘᴏᴡᴇʀᴇᴅ ʙʏ : \n@sanzetx | @reyn0pe </b>", disable_web_page_preview=True),
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("ᴛʏᴘɪɴɢ ɴᴀᴍᴀ ᴠɪᴅᴇᴏ ɴʏᴀ ᴛᴏʟᴏʟ"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "/stream https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("ʟᴏ ɴʏᴀʀɪ ᴀᴘᴀᴀɴsɪ ʙᴇɢᴏ ʏᴀɴɢ ʟᴏ ᴄᴀʀɪ ᴋᴀɢᴀ ᴀᴅᴀ"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
