import os
from inspect import getfullargspec

from pyrogram import filters
from pyrogram.types import Message

from ZeebMusic import app
from ZeebMusic.misc import SUDOERS
from ZeebMusic.utils.database import get_client


@app.on_message(filters.command("setpfp", prefixes=".") & SUDOERS)
async def set_pfp(client, message):
    from ZeebMusic.core.userbot import assistants

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="<blockquote>Reply to a photo</blockquote>")
    for num in assistants:
        client = await get_client(num)
        photo = await message.reply_to_message.download()
        try:
            await client.set_profile_photo(photo=photo)
            await eor(message, text="<blockquote>Successfully Changed PFP.</blockquote>")
            os.remove(photo)
        except Exception as e:
            await eor(message, text=e)
            os.remove(photo)


@app.on_message(filters.command("setbio", prefixes=".") & SUDOERS)
async def set_bio(client, message):
    from ZeebMusic.core.userbot import assistants

    if len(message.command) == 1:
        return await eor(message, text="<blockquote>Give some text to set as bio.</blockquote>")
    elif len(message.command) > 1:
        for num in assistants:
            client = await get_client(num)
            bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await eor(message, text="<blockquote>Changed Bio.</blockquote>")
        except Exception as e:
            await eor(message, text=e)
    else:
        return await eor(message, text="<blockquote>Give some text to set as bio.</blockquote>")


@app.on_message(filters.command("setname", prefixes=".") & SUDOERS)
async def set_name(client, message):
    from ZeebMusic.core.userbot import assistants

    if len(message.command) == 1:
        return await eor(message, text="<blockquote>Give some text to set as name.</blockquote>")
    elif len(message.command) > 1:
        for num in assistants:
            client = await get_client(num)
            name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await eor(message, text=f"<blockquote>name Changed to {name} .</blockquote>")
        except Exception as e:
            await eor(message, text=e)
    else:
        return await eor(message, text="<blockquote>Give some text to set as name.</blockquote>")


@app.on_message(filters.command("delpfp", prefixes=".") & SUDOERS)
async def del_pfp(client, message):
    from ZeebMusic.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos(photos[0].file_id)
                await eor(message, text="<blockquote>Successfully deleted photo</blockquote>")
            else:
                await eor(message, text="<blockquote>No profile photos found.</blockquote>")
        except Exception as e:
            await eor(message, text=e)


@app.on_message(filters.command("delallpfp", prefixes=".") & SUDOERS)
async def delall_pfp(client, message):
    from ZeebMusic.core.userbot import assistants

    for num in assistants:
        client = await get_client(num)
        photos = [p async for p in client.get_chat_photos("me")]
        try:
            if photos:
                await client.delete_profile_photos([p.file_id for p in photos[1:]])
                await eor(message, text="<blockquote>Successfully deleted photos</blockquote>")
            else:
                await eor(message, text="<blockquote>No profile photos found.</blockquote>")
        except Exception as e:
            await eor(message, text=e)


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})


__MODULE__ = "Ass"
__HELP__ = """<blockquote expandable><b>

<u> ᴀssɪsᴛᴀɴᴛ's ᴄᴏᴍᴍᴀɴᴅ:</u>
.setpfp - ʀᴇᴘʟʏ ɪɴ ᴘʜᴏᴛᴏ ᴛᴏ sᴇᴛ ᴀʟʟ ʙᴏᴛ ᴀssɪsᴛᴀɴᴛ ᴘʀᴏғɪʟᴇ ᴘɪᴄᴛᴜʀᴇ [ᴏɴʟʏ ᴘʜᴏᴛᴏ] [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀ]

.setname [ᴛᴇxᴛ] - ᴛᴏ sᴇᴛ ᴀʟʟ ᴀssɪsᴛᴀɴᴛ ɴᴀᴍᴇ [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀ]

.setbio [ᴛᴇxᴛ] - ᴛᴏ sᴇᴛ ᴀʟʟ ᴀssɪsᴛᴀɴᴛ ʙɪᴏ [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀ]


.delpfp - ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛs ᴘʀɪғɪʟᴇ ᴘɪᴄ [ᴏɴʟʏ ᴏɴᴇ ᴘʀᴏғɪʟᴇ ᴘɪᴄ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ] [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀ]

.delallpfp - ᴅᴇʟᴇᴛᴇ ᴀssɪsᴛᴀɴᴛs ᴀʟʟ ᴘʀɪғɪʟᴇ ᴘɪᴄ [ᴏɴʟʏ ᴏɴᴇ ᴘʀᴏғɪʟᴇ ᴘɪᴄ ᴡɪʟʟ ʙᴇ ʀᴇᴍᴀɪɴ] [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀ]

<u> ɢʀᴏᴜᴘ ᴀssɪsᴛᴀɴᴛ's ᴄᴏᴍᴍᴀɴᴅ:</u>

/checkassistant - ᴄʜᴇᴄᴋ ᴅᴇᴛᴀɪʟs ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀssɪsᴛᴀɴᴛ

/setassistant - ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ sᴘᴇᴄɪғɪᴄ ᴀssɪsᴛᴀɴᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ

/changeassistant - ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʀᴀɴᴅᴏᴍ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀssɪsᴛᴀɴᴛ ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ's

</b></blockquote>
"""
