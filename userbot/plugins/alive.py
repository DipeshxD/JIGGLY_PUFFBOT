
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) && @Hell boy_pikachu
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in Mafia Userbot by @D3_krish

import asyncio
import random
from telethon import events
from userbot import ALIVE_NAME, mafiaversion
from mafiabot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp

# ๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค๐ค
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "๐ป3๐๐๐_๐น๐๐"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for รรลฎ$HรณpBรศ

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/81a832f2434ba504f5b1c.jpg"
file2 = "https://telegra.ph/file/9820bcf4f9c57ac801860.jpg"
file3 = "https://telegra.ph/file/c42d5eddd24a9e6acd576.jpg"
file4 = "https://telegra.ph/file/81a832f2434ba504f5b1c.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "  __**๐ฅ๐ฅ๐ป3๐๐๐_๐น๐๐ ๐๐ ๐ธ๐๐๐๐ผ๐ฅ๐ฅ**__\n\n"

pm_caption += (
    f"                 ๐๐๐ธ๐๐๐ผโ๐\n**  ใ๐[{DEFAULTUSER}](tg://user?id={mafia})๐ใ**\n\n"
)

pm_caption += "๐ก๏ธTELETHON๐ก๏ธ : `1.15.0` \n\n"

pm_caption += f"๐๐ป3๐๐๐_๐น๐๐๐ : `{mafiaversion}`\n\n"

pm_caption += f"๐ฑSUDO๐ฑ            : `{sudou}`\n\n"

pm_caption += "๐USERBOT_GROUP๐๏ธ   : [๐๐๐๐](https://t.me/D3VIL_BOT_SUPPORT)\n\n"

pm_caption += "๐CREATOR๐    : [๐๐๐๐๐](https://t.me/D3_krish)\n\n"

pm_caption += "๐คฉSUPPORTER๐คฉ    :[TEAM D3VIL](https://t.me/D3VIL_0358)\n\n"

pm_caption += "      [๐ฅREPO๐ฅ](https://github.com/D3KRISH/D3VIL-BOT) ๐น [๐License๐](https://github.com/D3KRISH/D3VIL-BOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "d3vil", None, "To check am i alive with your favorite alive pic"
).add()
