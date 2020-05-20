"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`MY BOT IS RUNNING SUCCESFULLY"
                     "`☞Telethon version: 6.9.0`"
                     # ☞Python: 3.8.2
                     "`'.)..)..)..)..)..\n\n"
                     "███████ ═╮\n"
                     "███████ ▏ ∥\n"
                     "███████ ═╯\n"
                     "◥█████◤\n"
                     
                   "''༊IAM  A⃟⃠LIVE𖣘'"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     
