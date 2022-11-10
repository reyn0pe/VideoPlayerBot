"""
© thesanzu
"""

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from helpers.bot_utils import BOT_NAME, USERNAME
from config import SUPPORT_GROUP, UPDATES_CHANNEL
from translations import START_TEXT, HELP_TEXT, ABOUT_TEXT
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("ᴀɴᴀᴋ ᴛᴏʟᴏʟ ɢᴀʙɪsᴀ ᴘᴀᴋᴇ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("ʙᴏs ʙᴇsᴀʀ", url=f"https://t.me/sanzetc"),
            ],
            [
                InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
            [
               InlineKeyboardButton("ᴍᴀsᴜᴋɪɴ ᴀᴋᴜ ʙᴀʙᴇ ᴀʜʜʜʜ", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply_text(f"**{BOT_NAME} ᴀᴋʜɪʀɴʏᴀ ɢᴜᴇ ʜɪᴅᴜᴘ ʜᴀʜᴀ**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="start"),
                InlineKeyboardButton ("sᴜᴘᴘᴏʀғ", url=f"https://t.me/{SUPPORT_GROUP}"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("ᴀɴᴀᴋ ᴛᴏʟᴏʟ ɢᴀʙɪsᴀ ᴘᴀᴋᴇ", callback_data="help"),
            ],
            [
                InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton("ʙᴏs ʙᴇsᴀʀ", url=f"https://t.me/sanzetc"),
            ],
            [
                InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ],
            [
               InlineKeyboardButton("ᴍᴀsᴜᴋɪɴ ᴀᴋᴜ ʙᴀʙᴇ ᴀʜʜʜʜ", url=f"https://t.me/{USERNAME}?startgroup=true"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass

