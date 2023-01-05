import asyncio, time, random
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from config import *

async def change_name():
    list_emoji = ["🎊","🎉","🥂","🎁","🪄","🍾","🍾","🍾","✨","☃️","🎄","🥳","🥂","🎉","🎊"]
    loop = asyncio.new_event_loop()
    client = TelegramClient('emojiki', API_ID, API_HASH, loop=loop)
    async with client:
        emoji = random.choice(list_emoji)
        first = emoji + "Артём"
        last = "Андреевич" + emoji
        await client(UpdateProfileRequest(first, last))

if __name__ == "__main__":
    while True:
        asyncio.run(change_name())
        time.sleep(60)
