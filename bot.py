from pyrogram import Client, filters
from pyrogram.types import Message
import random
from AuthNex.Database import user_col, sessions_col

# 🔐 AuthGiverBot
auth_bot = Client(
    "AuthGiverBot",
    api_id=27548865,  # 🔁 Replace with your API ID
    api_hash="db07e06a5eb288c706d4df697b71ab61",  # 🔁 Replace with your API Hash
    bot_token="7883663341:AAEXp8lzLUlY5JVmF770v8bnmp8lsklXhgQ"  # 🔁 Replace with Auth Bot Token
)

# 🟢 Store codes temporarily
code_store = {}

@auth_bot.on_message(filters.command("start") & filters.private)
async def start_msg(_, m: Message):
    await m.reply_text(
        "**👋 Welcome to AuthNex Helper Bot!**\n\n"
        "Use /code <your_mail@AuthNex.Codes> to get your login authentication code.",
        disable_web_page_preview=True
    )

