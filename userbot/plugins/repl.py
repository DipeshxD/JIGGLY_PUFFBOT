# this plugin made by D3vil Userbot

"""Plugin for D3VILBot string
\nCode by @D3KRISH
type '.repl' to get D3VILBot String
"""

import random, re
from mafiabot.utils import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="repl ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("Click [here](https://replit.com/@D3krish/D3VILSTRINGSESSION-1#main.py) to open this 🔥**Lit AF!!**🔥 **D3VIL BOT** sting.. Join channel :- @D3VIL_SUPPORT Repo Uploaded By @D3_krish")
    
        
