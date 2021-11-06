from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "lapor bug 😊", url="https://t.me/aapikal")]
    ])
    welcomed = f"Hei <b>{message.from_user.first_name}</b>\n/help untuk info lebih"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
