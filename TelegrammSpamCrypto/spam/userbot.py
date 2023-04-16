import asyncio, random, time
from pyrogram import Client
from config import *
from pyrogram.errors.exceptions.bad_request_400 import InputUserDeactivated, PeerFlood

from config import *
from Parsers import parse_members
from spam_func import spam_messege, send_bot
from Database import *
from members_purse import members_pars

friend_id = ("Alexander_CRT", "Makar_CRT", "Daniil_CRT", "Eldar_CRT")

start = input("Напиши pars или spam: ")


async def main():
    app = Client("my_account")

    if start == "pars":
        await parse_members(app)

    try:
        if start == "spam":
            await spam_messege(app)



    except InputUserDeactivated:
        time.sleep(10)
        print("sleep")
        await main()
        print("main")
    except PeerFlood:
        print("ban_flood")
        await send_bot(app)
        await main()
        print("main")


if __name__ == "__main__":
    asyncio.run(main())
