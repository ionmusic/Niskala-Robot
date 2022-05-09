# ⚠️ © @greyyvbss 

# ⚠️ Don't Remove Credits

import os

import random

from telethon.tl.types import InputMessagesFilterPhotos

from telethon.tl.types import InputMessagesFilterVideo

from Yuriko.events import register

from Yuriko import telethn as tbot, ubot2         
        

@register(pattern="^/asupan ?(.*)")

async def _(event):

    memeks = await event.reply("**Sedang Mencari Video Asupan...🔍**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@Asupan_Rzydx", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Nih Asupan nya Kak 🥵", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Asupannya Gaada Koncol")


@register(pattern="^/ngaji ?(.*)")

async def _(event):

    memeks = await event.reply("**Alhamdulillah, Wait Ku Cari Dulu...**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@kureenkeryam", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Dengarkan Dengan Khusyu Kak..", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Lu Haram, Jadi Gak Bisa Denger Qur'an..")


@register(pattern="^/ayang ?(.*)")

async def _(event):

    memeks = await event.reply("**Wait Ku Cariin Ayangnya...**") 

    try:

        asupannya = [

            asupan

            async for asupan in ubot2.iter_messages(

            "@CeweLogoPack", filter=InputMessagesFilterVideo

            )

        ]

        kontols = random.choice(asupannya)

        pantek = await ubot2.download_media(kontols)

        await tbot.send_file(

            event.chat.id, 

            caption="Dijaga Jan Di Nakalin Ya Ayangnya..", 

            file=pantek

            )

        await memeks.delete()

    except Exception:

        await memeks.edit("Haha Kasian Bet Lu Gak Punya Ayang..")

