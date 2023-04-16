admins = ("andrey_ksa","Andron_01")

async def parse_members(app):
    parsed = set()

    async with app:
        async for member in app.get_chat_members(chat_id="treyder001k", ):

            if not member.user.is_bot and member.user.username not in admins:
                member_id = member.user.id
                parsed.add(member_id)
        print(parsed)