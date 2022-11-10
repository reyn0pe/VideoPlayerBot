"""
© thesanzu
"""

import os
import re
import sys
import time
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from plugins.nopm import User
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from helpers.bot_utils import USERNAME
from config import AUDIO_CALL, VIDEO_CALL
from youtubesearchpython import VideosSearch
from helpers.decorators import authorized_users_only
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


ydl_opts = {
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)
group_call = GroupCallFactory(User, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM).get_group_call()


@Client.on_callback_query(filters.regex("pause_callback"))
async def pause_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"» ᴘᴀᴜsᴇ «"
        await AUDIO_CALL[chat_id].set_audio_pause(True)
    elif chat_id in VIDEO_CALL:
        text = f"» ᴘᴀᴜsᴇ «"
        await VIDEO_CALL[chat_id].set_video_pause(True)
    else:
        text = f"ᴍᴀɴᴀ ʙɪsᴀ ʙᴀʙɪ ʟᴏ ʟᴀɢɪ ᴋᴀɢᴀ ᴘʟᴀʏ ᴛᴏʟᴏʟ ᴀᴍᴀᴛ sɪ ɴɪ ʙᴏᴄᴀʜ"
    await Client.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )

@Client.on_callback_query(filters.regex("resume_callback"))
async def resume_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"» ʀᴇsᴜᴍᴇ «"
        await AUDIO_CALL[chat_id].set_audio_pause(False)
    elif chat_id in VIDEO_CALL:
        text = f"» ʀᴇsᴜᴍᴇ «"
        await VIDEO_CALL[chat_id].set_video_pause(False)
    else:
        text = f"ᴍᴀɴᴀ ʙɪsᴀ ʙᴀʙɪ ʟᴏ ʟᴀɢɪ ᴋᴀɢᴀ ᴘʟᴀʏ ᴛᴏʟᴏʟ ᴀᴍᴀᴛ sɪ ɴɪ ʙᴏᴄᴀʜ"
    await Client.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )


@Client.on_callback_query(filters.regex("end_callback"))
async def end_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"» sᴛᴏᴘᴘᴇᴅ «"
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
    elif chat_id in VIDEO_CALL:
        text = f"» sᴛᴏᴘᴘᴇᴅ «"
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
    else:
        text = f"ᴍᴀɴᴀ ʙɪsᴀ ʙᴀʙɪ ʟᴏ ʟᴀɢɪ ᴋᴀɢᴀ ᴘʟᴀʏ ᴛᴏʟᴏʟ ᴀᴍᴀᴛ sɪ ɴɪ ʙᴏᴄᴀʜ"
    await Client.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )
    await Client.send_message(
        chat_id=CallbackQuery.message.chat.id,
        text=f" **ɢɪᴛᴜ ᴅᴏɴɢ ɢᴜᴇ ᴄᴀᴘᴇ ᴘᴇɴɢᴇɴ ɴɢᴏᴘɪ ᴅᴜʟᴜ, ᴊᴏɪɴ ᴅᴜʟᴜ ʟᴀʜ ʙᴀʙɪ ᴋᴀʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴋᴇʟᴀᴍɪɴ ʟᴏ ʙᴜsᴜᴋ @reyn0pe !**"
    )
    await CallbackQuery.message.delete()


@Client.on_message(filters.command(["stream", f"stream@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def stream(client, m: Message):
    msg = await m.reply_text("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("ᴋɪʀɪᴍ ʟɪɴᴋ ᴀᴛᴀᴜ ɢᴀ ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ɴʏᴀ ʏᴀ ᴋᴏɴᴛᴏʟ")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        if not 'http' in query:
            return await msg.edit("ᴋɪʀɪᴍ ʟɪɴᴋ ᴀᴛᴀᴜ ɢᴀ ʀᴇᴘʟʏ ᴠɪᴅᴇᴏ ɴʏᴀ ʏᴀ ᴋᴏɴᴛᴏʟ")
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
                search = VideosSearch(query, limit=1)
                opp = search.result()["result"]
                oppp = opp[0]
                thumbid = oppp["thumbnails"][0]["url"]
                split = thumbid.split("?")
                thumb = split[0].strip()
            except Exception as e:
                return await msg.edit(f" **ᴍᴀᴍᴘᴜs ᴅᴏᴡɴʟᴏᴀᴅ ᴇʀʀᴏʀ** \n\n`{e}`")
                print(e)

        else:
            await msg.edit("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ ...`")
            link = query
            thumb = "https://telegra.ph/file/3e14128ad5c9ec47801bd.jpg"

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
            await group_call.start_video(link, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb, 
               caption=f" **ɴɢᴇɴɢɢ [Video Streaming]({query}) ᴅɪ {m.chat.title} !**",
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
            await msg.edit(f" **ᴍᴀᴍᴘᴜs ᴇʀʀᴏʀ ᴀᴡᴏᴋᴀᴡᴏᴋ!** \n\nError: `{e}`")
            return await group_call.stop()

    elif media.video or media.document:
        await msg.edit("`sᴀʙᴀʀ ʟᴀɢɪ ᴅᴏᴡɴʟᴏᴀᴅ ...`")
        if media.video and media.video.thumbs:
            lol = media.video.thumbs[0]
            lel = await client.download_media(lol['file_id'])
            thumb = lel
        else:
            thumb = "https://telegra.ph/file/62e86d8aadde9a8cbf9c2.jpg"

        video = await client.download_media(media)

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
            await group_call.start_video(video, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb,
               caption=f" **ɴɢᴇɴɢɢɢ [Video Streaming](https://t.me/reyn0pe) ᴅɪ {m.chat.title} !**",
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
                          text="ᴇɴᴅ️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f" **ᴍᴀᴍᴘᴜs ᴇʀʀᴏʀ ᴀᴡᴏᴋᴀᴡᴏᴋ !** \n\nError: `{e}`")
            return await group_call.stop()

    else:
        await msg.edit(
            "ᴀᴘᴀᴀɴ ʟᴏ ᴍᴀᴜ ɴʏᴀʀɪ ᴠɪᴅᴇᴏ ʏᴏᴜᴛᴜʙᴇ?",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪʏᴀ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "ᴏɢᴀʜ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(filters.command(["pause", f"pause@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def pause(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(True)
        await m.reply_text(" **ɴᴀʜʜ ɢɪᴛᴜ ɢᴜᴇ ᴄᴀᴘᴇ**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(True)
        await m.reply_text(" **ɴᴀʜ ɢɪᴛᴜ ɢᴜᴇ ᴄᴀᴘᴇ**")

    else:
        await m.reply_text(" **ᴍᴀɴᴀ ʙɪsᴀ ᴀᴊɢ ʟᴏ ᴀᴊᴀ ʙᴇʟᴜᴍ ᴘʟᴀʏ ᴀᴘᴀ ᴀᴘᴀ ᴅᴀsᴀʀ ᴀɴᴀᴋ ᴛᴏʟᴏʟ**")


@Client.on_message(filters.command(["resume", f"resume@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def resume(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(False)
        await m.reply_text(" **ᴄᴀᴘᴇ ᴀᴊɢ ʙᴀʀᴜ ᴊᴜɢᴀ ɢᴜᴇ ɴɢᴏᴘɪ sᴀᴍᴀ ʙᴇʟɪ ʙᴀᴋᴡᴀɴ ᴅᴀʜ ʟᴏ ɢᴀs ʟᴀɢɪ**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(False)
        await m.reply_text(" **ᴄᴀᴘᴇ ᴀᴊɢ ʙᴀʀᴜ ᴊᴜɢᴀ ɢᴜᴅ ɴɢᴏᴘɪ sᴀᴍᴀ ʙᴇʟɪ ʙᴀᴋᴡᴀɴ ᴅᴀʜ ʟᴏ ɢᴀs ᴀᴊᴀ!**")

    else:
        await m.reply_text(" **ᴍᴀɴᴀ ʙɪsᴀ ᴀᴊɢᴏ ᴀᴊᴀ ʙᴇʟᴜᴍ ᴘʟᴀʏ ᴀᴘᴀ ᴀᴘᴀ ᴅᴀsᴀʀ ᴀɴᴀᴋ ᴛᴏʟᴏʟ**")


@Client.on_message(filters.command(["endstream", f"endstream@{USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def endstream(client, m: Message):
    msg = await m.reply_text("`sᴀʙᴀʀ ʟᴀɢɪ ᴏᴛᴡ ...`")
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
        await msg.edit(" **ᴀᴋʜɪʀɴʏᴀ ʟᴏ ᴘᴇᴋᴀ ᴊᴜɢᴀ**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
        await msg.edit(" **ᴀᴋʜɪʀɴʏᴀ ʟᴏ ᴘᴇᴋᴀ ᴊᴜɢᴀ**")

    else:
        await msg.edit("**ᴡᴏʏ ᴀɴᴀᴋ ᴋᴏɴᴛᴏʟ ʟᴏ ʜᴀʀᴜs ᴘʟᴀʏ ᴅᴜʟᴜ ʙᴀʙɪ **")


# pytgcalls handlers

@group_call.on_audio_playout_ended
async def audio_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[𝗜𝗡𝗙𝗢] - ɢɪᴛᴜ ᴅᴏɴɢ ɢᴜᴇ ᴄᴀᴘᴇ ᴘᴇɴɢᴇɴ ɴɢᴏᴘɪ ᴅᴜʟᴜ, ᴊᴏɪɴ ᴅᴜʟᴜ ʟᴀʜ ʙᴀʙɪ ᴋᴀʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴋᴇʟᴀᴍɪɴ ʟᴏ ʙᴜsᴜᴋ @reyn0pe !")

@group_call.on_video_playout_ended
async def video_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[𝗜𝗡𝗙𝗢] - ɢɪᴛᴜ ᴅᴏɴɢ ɢᴜᴇ ᴄᴀᴘᴇ ᴘᴇɴɢᴇɴ ɴɢᴏᴘɪ ᴅᴜʟᴜ, ᴊᴏɪɴ ᴅᴜʟᴜ ʟᴀʜ ʙᴀʙɪ ᴋᴀʟᴏ ᴋᴀɢᴀ ᴊᴏɪɴ ɢᴜᴇ sᴜᴍᴘᴀʜɪɴ ᴋᴇʟᴀᴍɪɴ ʟᴏ ʙᴜsᴜᴋ @reyn0pe !")
