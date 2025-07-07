from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from ZeebMusic import app
from ZeebMusic.core.call import Zb
from ZeebMusic.utils import bot_sys_stats
from ZeebMusic.utils.decorators.language import language
from ZeebMusic.utils.inline import supp_markup


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS & filters.group)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_text(_["ping_1"].format(app.mention),
    )
    start = datetime.now()
    pytgping = await Zb.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp,
            app.mention,
            UP,
            DISK,
            CPU,
            RAM,
            pytgping,
        ),
        reply_markup=supp_markup(_),
    )
