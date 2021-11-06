from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"saat ini hanya mendukung satu url, bukan playlist"
    await message.reply_text(helptxt)
