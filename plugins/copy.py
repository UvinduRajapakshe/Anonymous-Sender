from pyrogram import (
    Client,
    filters
    )


@Client.on_message(filters.private & ~filters.caption &
                   ~filters.command("start"))
async def copy(client, message):
    chat = message.chat.id
    await message.copy(chat)
