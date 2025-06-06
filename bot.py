from pyrogram import Client
from io import BytesIO

@app.on_message(filters.command("getpfp"))
async def get_user_pfp(client, message):
    user = message.from_user
    photos = await client.get_profile_photos(user.id, limit=1)

    if not photos:
        return await message.reply("❌ No profile picture found.")

    # Download the photo
    file = await client.download_media(photos[0].file_id)

    # Send the photo with a caption
    await message.reply_photo(
        photo=file,
        caption=f"👤 **{user.first_name}'s Profile Picture**",
        parse_mode="markdown"
    )
