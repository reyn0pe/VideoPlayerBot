import os
import re
import sys
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message
from helpers.bot_utils import USERNAME
from config import AUDIO_CALL, VIDEO_CALL
from plugins.video import ydl, group_call
from helpers.decorators import authorized_users_only, sudo_users_only
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_message(filters.command(["play", f"play@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def play(client, m: Message):
    msg = await m.reply_text("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("ᴋɪʀɪᴍ ʟɪɴᴋ ᴀᴛᴀᴜ ɢᴀ ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ɴʏᴀ ʏᴀ ᴋᴏɴᴛᴏʟ")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        if not 'http' in query:
            return await msg.edit(ᴋɪʀɪᴍ ʟɪɴᴋ ᴀᴛᴀᴜ ɢᴀ ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ɴʏᴀ ʏᴀ ᴋᴏɴᴛᴏʟ")
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ ...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                    ytstreamlink = f['url']
                link = ytstreamlink
            except Exception as e:
                return await msg.edit(f"ᴍᴀᴍᴘᴜs ᴅᴏᴡɴʟᴏᴀᴅ ᴇʀʀᴏʀ** \n\n`{e}`")
                print(e)

        else:
            await msg.edit("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ ...`")
            link = query

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(link, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_text(f"**ɴɢᴇɴɢɢ [Audio Streaming]({query}) ᴅɪ {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="ᴘᴀᴜsᴇ",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="ʀᴇsᴜᴍᴇ️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="ᴇɴᴅ",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"**ᴍᴀᴍᴘᴜs ᴇʀʀᴏʀ ᴀᴡᴏᴋᴀᴡᴏᴋ!** \n\nError: `{e}`")
            return await group_call.stop()

    elif media.audio or media.document:
        await msg.edit("`sᴀʙᴀʀ ɢᴜᴇ ʟᴀɢɪ ᴅᴏᴡɴʟᴏᴀᴅ...`")
        audio = await client.download_media(media)

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_audio(audio, repeat=False)
            AUDIO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_text(f" **ɴɢᴇɴɢ [Audio Streaming](https://t.me/reyn0pe) ᴅɪ {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="ᴘᴀᴜsᴇ",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="ʀᴇsᴜᴍᴇ",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="ᴇɴᴅ️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f" **ᴍᴀᴍᴘᴜs ᴇʀʀᴏғ ᴀᴡᴏᴋᴀᴡᴏᴋ** \n\nError: `{e}`")
            return await group_call.stop()

    else:
        await msg.edit(
            "ʟᴏ ᴍᴀᴜ ɴʏᴀʀɪ ᴀᴘᴀᴀɴsɪ ɢᴏʙʟᴏᴋ ʏᴀɴɢ ʟᴏ ᴘᴇɴɢᴇɴ ᴄᴀʀɪ ᴋᴀɢᴀ ᴀᴅᴀ ᴛᴏʟᴏʟ",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ʏᴇᴀʜ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "ᴏɢᴀʜ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command(["restart", f"restart@{USERNAME}"]))
@sudo_users_only
async def restart(client, m: Message):
    k = await m.reply_text("`ᴍᴀᴜ ʙᴇʟɪ ɢᴏʀᴇɴɢᴀɴ ᴅᴜʟᴜ sᴀᴍᴀ ʙᴏs sᴀɴᴢᴜ ɴᴀɴᴛɪ ʙᴀʟɪᴋ ʟᴀɢɪ...`")
    await sleep(3)
    os.execl(sys.executable, sys.executable, *sys.argv)
    try:
        await k.edit(" **ᴍᴀᴜ ɢᴏʀᴇᴀɴɢᴀɴ ɴʏᴀ ɢᴀ? ᴛᴀᴘɪ ʜᴀʙɪs sᴀᴍᴀ sɪ ʙᴏs. \nᴊᴏɪɴ @reyn0pe ᴋᴀɢᴀ ᴊᴏɪɴ ᴋᴇʟᴀᴍɪɴ ɴʏᴀ ʙᴜsᴜᴋ**")
    except:
        pass
