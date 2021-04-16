from pyrogram import (
    Client,
    filters
)

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


@Client.on_message(filters.caption & filters.private)
async def addorno(client, message):
    msg = message.message_id
    await message.reply_text('Do You Need Caption ? 🤔',
                             quote=True,
                             reply_markup=InlineKeyboardMarkup(
                               [[InlineKeyboardButton(
                                   text="Yes ✅",
                                   callback_data=f"yes-{msg}"),
                                 InlineKeyboardButton(
                                     text="No ❌",
                                     callback_data=f"no-{msg}")]])
                             )


@Client.on_callback_query()
async def cb(client, call):
    k = call.data
    msgid = int(k.split("-")[1])
    chat = call.message.chat.id
    if k.startswith("yes"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid)
    if k.startswith("no"):
        await call.message.delete()
        await call.message._client.copy_message(chat, chat, msgid,
                                                caption="")
