
import os
import re
import sys
import time
import datetime
import random 
import asyncio

from pyrogram import filters, Client, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus, ChatType

from apscheduler.schedulers.background import BackgroundScheduler


API_ID = 6 
API_HASH = "Abcdefg1234"
BOT_TOKEN = ""
DEVS = [1517994352, 1854700253]

ALL_GROUPS = []
TOTAL_USERS = []
MEDIA_GROUPS = []
DISABLE_CHATS = []
GROUP_MEDIAS = {}

DELETE_MESSAGE = [
"1 ʜᴏᴜʀ ᴄᴏᴍᴘʟᴇᴛᴇ, ɪ'ᴍ ᴅᴏɪɴɢ ᴍʏ ᴡᴏʀᴋ...",
"ɪᴛꜱ ᴛɪᴍᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇᴅɪᴀꜱ!",
"ɴᴏ ᴏɴᴇ ᴄᴀɴ ᴄᴏᴘʏʀɪɢʜᴛ ᴜɴᴛɪʟ ɪ'ᴍ ᴀʟɪᴠᴇ 😤",
"ʜᴜᴇ ʜᴜᴇ, ʟᴇᴛ'ꜱ ᴅᴇʟᴇᴛᴇ ᴍᴇᴅɪᴀ...",
"ɪ'ᴍ ʜᴇʀᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇᴅɪᴀꜱ 🙋",
"😮‍💨 ꜰɪɴᴀʟʟʏ ɪ ᴅᴇʟᴇᴛᴇ ᴍᴇᴅɪᴀꜱ",
"ɢʀᴇᴀᴛ ᴡᴏʀᴋ ᴅᴏɴᴇ ʙʏ ᴍᴇ 🥲",
"ᴀʟʟ ᴍᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ!",
"ʜᴜᴇ ʜᴜᴇ ᴍᴇᴅɪᴀꜱ ᴅᴇʟᴇᴛᴇᴅ ʙʏ ᴍᴇ 😮‍💨",
"ᴍᴇᴅɪᴀꜱ....",
"ɪᴛ'ꜱ ʜᴀʀᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇᴅɪᴀꜱ 🙄",
]

START_MESSAGE = """
**ʜᴇʟʟᴏ {}, ɪ'ᴍ ᴀɴᴛɪ - ᴄᴏᴘʏʀɪɢʜᴛ ʙᴏᴛ**

**ɪ ᴄᴀɴ ꜱᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ꜰʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛꜱ 😉**

**ᴡᴏʀᴋ:** ɪ'ʟʟ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇᴅɪᴀꜱ ᴏꜰ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪɴ ᴇᴠᴇʀʏ 1 ʜᴏᴜʀ ➰

**ᴘʀᴏᴄᴇꜱꜱ?:** ꜱɪᴍᴘʟʏ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ʀɪɢʜᴛ!
"""

BUTTON = [[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ 🧸", url="http://t.me/StormAntiCopyright_bot?startgroup=s&admin=delete_messages")]]

RiZoeL = Client('RiZoeL-Anti-CopyRight', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def add_user(user_id):
   if user_id not in TOTAL_USERS:
      TOTAL_USERS.append(user_id)

@RiZoeL.on_message(filters.command(["ping", "speed"]))
async def ping(_, e: Message):
   start = datetime.datetime.now()
   add_user(e.from_user.id)
   rep = await e.reply_text("⚡")
   end = datetime.datetime.now()
   ms = (end-start).microseconds / 1000
   await rep.edit_text(f"🤖 **ᴘᴏɴɢ**: `{ms}`ᴍs")

@RiZoeL.on_message(filters.command(["help", "start"]))
async def start_message(_, message: Message):
   add_user(message.from_user.id)
   await message.reply(START_MESSAGE.format(message.from_user.mention), reply_markup=InlineKeyboardMarkup(BUTTON))

@RiZoeL.on_message(filters.user(DEVS) & filters.command(["restart", "reboot"]))
async def restart_(_, e: Message):
    await e.reply("**ʀᴇꜱᴛᴀʀᴛɪɴɢ.....**")
    try:
        await RiZoeL.stop()
    except Exception as ex:
        print(f"ᴇʀʀᴏʀ ꜱᴛᴏᴘᴘɪɴɢ ᴛʜᴇ ʙᴏᴛ: {ex}")
    
    try:
        args = [sys.executable, "start.sh"]
        os.execl(sys.executable, *args)
    except Exception as ex:
        print(f"ᴇʀʀᴏʀ ʀᴇꜱᴛᴀʀᴛɪɴɢ ᴛʜᴇ ʙᴏᴛ: {ex}")
        await e.reply("**ꜰᴀɪʟᴇᴅ ᴛᴏ ʀᴇꜱᴛᴀʀᴛ. ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ʟᴏɢꜱ ꜰᴏʀ ᴅᴇᴛᴀɪʟꜱ.**")
    finally:
        quit()


@RiZoeL.on_message(filters.user(DEVS) & filters.command(["stat", "stats"]))
async def status(_, message: Message):
   wait = await message.reply("ꜰᴇᴛᴄʜɪɴɢ.....")
   stats = "**ʜᴇʀᴇ ɪꜱ ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ ᴏꜰ ʙᴏᴛ** \n\n"
   stats += f"ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: `{len(ALL_GROUPS)}` \n"
   stats += f"ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: `{len(TOTAL_USERS)}` \n"
   stats += f"ᴅɪꜱᴀʙʟᴇᴅ ᴄʜᴀᴛꜱ: `{len(DISABLE_CHATS)}` \n"
   stats += f"ᴛᴏᴛᴀʟ ᴍᴇᴅɪᴀ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛꜱ: `{len(MEDIA_GROUPS)}` \n\n"
   stats += f"**© @ll_KEX_ll**"
   await wait.edit_text(stats)


   
@RiZoeL.on_message(filters.command(["anticopyright", "copyright"]))
async def enable_disable(Rizoel: RiZoeL, message: Message):
   chat = message.chat
   if chat.id == message.from_user.id:
      await message.reply("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ")
      return
   txt = ' '.join(message.command[1:])
   if txt:
      member = await Rizoel.get_chat_member(chat.id, message.from_user.id)
      if re.search("on|yes|enable".lower(), txt.lower()):
         if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or member.user.id in DEVS:
            if chat.id in DISABLE_CHATS:
               await message.reply(f"ᴇɴᴀʙʟᴇᴅ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ.. ꜰᴏʀ {chat.title}")
               DISABLE_CHATS.remove(chat.id)
               return
            await message.reply("ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ")

      elif re.search("no|off|disable".lower(), txt.lower()):
         if member.status == ChatMemberStatus.OWNER or member.user.id in DEVS:
            if chat.id in DISABLE_CHATS:
               await message.reply("ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ")
               return
            DISABLE_CHATS.append(chat.id)
            if chat.id in MEDIA_GROUPS:
               MEDIA_GROUPS.remove(chat.id)
            await message.reply(f"ᴅɪꜱᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ ꜰᴏʀ {chat.title}!")
         else:
            await message.reply("ᴏɴʟʏ ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴄᴀɴ ᴅɪꜱᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ")
            return 
      else:
         if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or member.user.id in DEVS:
            if chat.id in DISABLE_CHATS:
               await message.reply("ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱ ᴅɪꜱᴀʙʟᴇ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ! \n\nᴛʏᴘᴇ `/ᴀɴᴛɪᴄᴏᴘʏʀɪɢʜᴛ ᴇɴᴀʙʟᴇ` ᴛᴏ ᴇɴᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ")
            else:
               await message.reply("ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱ ᴇɴᴀʙʟᴇ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ! \n\nᴛʏᴘᴇ `/ᴀɴᴛɪᴄᴏᴘʏʀɪɢʜᴛ ᴅɪꜱᴀʙʟᴇ` ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ")
              
   else:
       if chat.id in DISABLE_CHATS:
          await message.reply("ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱ ᴅɪꜱᴀʙʟᴇ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ! \n\nᴛʏᴘᴇ `/ᴀɴᴛɪᴄᴏᴘʏʀɪɢʜᴛ ᴇɴᴀʙʟᴇ` ᴛᴏ ᴇɴᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ")
       else:
          await message.reply("ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱ ᴇɴᴀʙʟᴇ ꜰᴏʀ ᴛʜɪꜱ ᴄʜᴀᴛ! \n\nᴛʏᴘᴇ `/ᴀɴᴛɪᴄᴏᴘʏʀɪɢʜᴛ ᴅɪꜱᴀʙʟᴇ` ᴛᴏ ᴅɪꜱᴀʙʟᴇ ᴀɴᴛɪ-ᴄᴏᴘʏʀɪɢʜᴛ")

@RiZoeL.on_message(filters.all & filters.group)
async def watcher(_, message: Message):
   chat = message.chat
   user_id = message.from_user.id
   if chat.type == ChatType.GROUP or chat.type == ChatType.SUPERGROUP:
      

      if chat.id not in ALL_GROUPS:
         ALL_GROUPS.append(chat.id)
      if chat.id in DISABLE_CHATS:
         return
      if chat.id not in MEDIA_GROUPS:
         if chat.id in DISABLE_CHATS:
            return
         MEDIA_GROUPS.append(chat.id)
      if (message.video or message.photo or message.animation or message.document):
         check = GROUP_MEDIAS.get(chat.id)
         if check:
            GROUP_MEDIAS[chat.id].append(message.id)
            print(f"ᴄʜᴀᴛ: {chat.title}, ᴍᴇꜱꜱᴀɢᴇ ɪᴅ: {message.id}")
         else:
            GROUP_MEDIAS[chat.id] = [message.id]
            print(f"ᴄʜᴀᴛ: {chat.title}, ᴍᴇꜱꜱᴀɢᴇ ɪᴅ: {message.id}")

def AutoDelete():
    if len(MEDIA_GROUPS) == 0:
       return

    for i in MEDIA_GROUPS:
       addchat(i)
       if i in DISABLE_CHATS:
         return
       message_list = list(GROUP_MEDIAS.get(i))
       try:
          hue = RiZoeL.send_message(i, random.choice(DELETE_MESSAGE))
          RiZoeL.delete_messages(i, message_list, revoke=True)
          asyncio.sleep(1)
          hue.delete()
          GROUP_MEDIAS[i].delete()
       except Exception:
          pass
    MEDIA_GROUPS.remove(i)
    print("ᴄʟᴇᴀɴ ᴀʟʟ ᴍᴇᴅɪᴀꜱ......")
    print("ᴡᴀɪᴛɪɴɢ ꜰᴏʀ 1 ʜᴏᴜʀ ⌛")

scheduler = BackgroundScheduler()
scheduler.add_job(AutoDelete, "interval", seconds=3600)

scheduler.start()

def starter():
   print('ꜱᴛᴀʀᴛɪɴɢ ʙᴏᴛ...')
   RiZoeL.start()
   print('ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ....')
   idle()

if __name__ == "__main__":
   starter()
