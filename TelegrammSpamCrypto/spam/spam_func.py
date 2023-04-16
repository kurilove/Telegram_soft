import random, asyncio
from members_purse import members_pars, parce_complited

number_member = 0


async def spam_messege(app):
    async with app:
        for id in members_pars:
            if id not in parce_complited:
                await app.send_message(id, text="""Здравствуйте!
    Я - создатель проекта "Crypto emerald"
    и обратил внимание на ваш запрос на вступление в нашу группу. Я готов добавить вас, но перед этим хотел бы узнать ваше мнение по поводу торговой сессии, которая запланирована на сегодня вечером.
    Интересуетесь ли вы торговлей фьючерсами?""")
                await asyncio.sleep(random.randint(5, 15))
                parce_complited.append(id)
                print(id)
            else:
                print("Уже есть")
                continue


async def send_bot(app):
    async with app:
        await app.send_message('SpamBot', text="/start")
        await asyncio.sleep(3)
        await app.send_message("SpamBot", text="ОК")
