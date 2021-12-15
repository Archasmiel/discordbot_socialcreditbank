deny_text = "You don't has permission for this!"


async def send(message, text):
    await message.channel.send(text)


async def require_role_send(message, role, text):
    has_permission = False
    for r in message.author.roles:
        if r == role:
            await message.channel.send(text)
            has_permission = True
    if not has_permission:
        await message.channel.send(deny_text)
