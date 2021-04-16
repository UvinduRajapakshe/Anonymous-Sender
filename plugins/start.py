from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **ANONYMOUS SENDER BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!


"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("👥 Group",
                          url="https://t.me/Uvindubr")],
    [InlineKeyboardButton("🔊 Channel",
                          url="https://t.me/UvinduBro")]],
    [InlineKeyboardButton("📦 Source Code",
                          url="https://github.com/UvinduBro/Anonymous-Sender")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
