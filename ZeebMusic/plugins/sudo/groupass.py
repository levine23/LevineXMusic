from pyrogram import filters
from pyrogram.types import Message

from ZeebMusic import app
from ZeebMusic.core.userbot import assistants
from ZeebMusic.utils.assistant import assistant, get_assistant_details
from ZeebMusic.utils.database import get_assistant, save_assistant, set_assistant
from ZeebMusic.utils.filter import admin_filter
from config import LOG_GROUP_ID


@app.on_message(filters.command("changeassistant") & admin_filter)
async def assis_change(_, message: Message):
    avt = await assistant()
    if avt == True:
        return await message.reply_text(
            "<blockquote expandable>sᴏʀʀʏ sɪʀ! ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ ᴏɴʟʏ ᴏɴʀ ᴀssɪsᴛᴀɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʜᴇʀᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴᴛ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ</blockquote>"
        )
    usage = f"<blockquote expandable>**ᴅᴇᴛᴇᴄᴛᴇᴅ ᴡʀᴏɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴀsɢᴇ \n**ᴜsᴀsɢᴇ:**\n/changeassistant - ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ's ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʀᴀɴᴅᴏᴍ ᴀssɪsᴛᴀɴᴛ ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ</blockquote>"
    if len(message.command) > 2:
        return await message.reply_text(usage)
    a = await get_assistant(message.chat.id)
    DETAILS = f"<blockquote>ʏᴏᴜʀ ᴄʜᴀᴛ's ᴀssɪsᴛᴀɴᴛ ʜᴀs ʙᴇᴇɴ ᴄʜᴀɴɢᴇᴅ ғʀᴏᴍ [{a.name}](https://t.me/{a.username}) </blockquote>"
    if not message.chat.id == LOG_GROUP_ID:
        try:
            await a.leave_chat(message.chat.id)
        except:
            pass
    b = await set_assistant(message.chat.id)
    DETAILS += f"<blockquote>ᴛᴏ [{b.name}](https://t.me/{b.username})</blockquote>"
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(DETAILS, disable_web_page_preview=True)


@app.on_message(filters.command("setassistant") & admin_filter)
async def assis_set(_, message: Message):
    avt = await assistant()
    if avt == True:
        return await message.reply_text(
            "<blockquote expandable>sᴏʀʀʏ sɪʀ! ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ ᴏɴʟʏ ᴏɴᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʜᴇʀᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ</blockquote>"
        )
    usage = await get_assistant_details()
    if len(message.command) != 2:
        return await message.reply_text(usage, disable_web_page_preview=True)
    query = message.text.split(None, 1)[1].strip()
    if query not in assistants:
        return await message.reply_text(usage, disable_web_page_preview=True)
    a = await get_assistant(message.chat.id)
    try:
        await a.leave_chat(message.chat.id)
    except:
        pass
    await save_assistant(message.chat.id, query)
    b = await get_assistant(message.chat.id)
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    DETAILS = f"""<blockquote expandable> ʏᴏᴜʀ ᴄʜᴀᴛ's  ɴᴇᴡ ᴀssɪsᴛᴀɴᴛ ᴅᴇᴛᴀɪʟs:
                   ᴀssɪsᴛᴀɴᴛ ɴᴀᴍᴇ :- {a.name}
                   ᴀssɪsᴛᴀɴᴛ ᴜsᴇʀɴᴀᴍᴇ :- {a.username}
                   ᴀssɪsᴛᴀɴᴛ ɪᴅ:- @{a.id}</blockquote>"""
    await message.reply_text(DETAILS, disable_web_page_preview=True)


@app.on_message(filters.command("checkassistant") & filters.group & admin_filter)
async def check_ass(_, message: Message):
    assistant = await get_assistant(message.chat.id)
    DETAILS = f"""<blockquote expandable>Your chat's assistant details:
Assistant Name :- {assistant.name}
Assistant Username :- {assistant.username}
Assistant ID:- @{assistant.id}</blockquote>"""
    await message.reply_text(DETAILS, disable_web_page_preview=True)
