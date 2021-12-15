from datetime import datetime as t

from modules.basicio import files as fio
from modules.basicio import io as io


async def greet_message(db, message, author_name, author_id):
    temp = await io.get_greettime(db, author_id)

    if t.now().strftime("%d.%m.%Y %H:%M:%S").split(' ')[0] != temp.split(' ')[0]:
        await message.channel.send(f'**Oh, hello {author_name}! Thank you for greeting!**\n'
                                   f'Now your credits increased by 10!')
        await fio.update(db, author_id, await io.get_credits(db, author_id) + 10)
        await fio.updategreettime(db, author_id, t.now().strftime("%d.%m.%Y %H:%M:%S"))
    else:
        if t.now().strftime("%H") != temp.split(' ')[1].split(':')[0]:
            await message.channel.send(f'**Oh hello again! Thank you very much, {author_name}.**\n'
                                       'You now have 1 more global social credits!')
            await fio.update(db, author_id, await io.get_credits(db, author_id) + 1)
            await fio.updategreettime(db, author_id, t.now().strftime("%d.%m.%Y %H:%M:%S"))
        else:
            await message.channel.send(f'**{author_name}, I\'m working now, don\'t bother me!**')


async def delete_messages(message, author):
    num = int(message.content.split()[1]) + 1
    await message.channel.purge(limit=num)
    await message.channel.send(f'Deleted {num} messages by {author.name}.')


async def show_roles(message):
    roles = ''
    for r in reversed(message.guild.roles):
        roles += r.name + '\n'
    await message.channel.send(roles)


async def transfer_credits(db, message):
    cnt = message.content
    member1 = f'<@!{message.author.id}>'
    member2 = cnt.split()[1]
    member1_name = '**' + message.author.name + '**'
    member2_name = '**' + message.mentions[0].name + '**'
    num = int(cnt.split()[2])
    if num > 0:
        if not await fio.search(db, member1) or not await fio.search(db, member2):
            await message.channel.send('Users not found, try again!')
        else:
            await fio.update(db, member1, await io.get_credits(db, member1) - int(num))
            await fio.update(db, member2, await io.get_credits(db, member2) + int(num))
            await message.channel.send(
                f'Wow! {member2_name}\'s global social credits was increased by {num}, but at what price!\n'
                f'{member1_name}\'s {num} global credits was transferred to {member2_name}!\n'
                f'Current global social credits of {member1_name} are {await io.get_credits(db, member1)}.\n'
                f'Current global social credits of {member2_name} are {await io.get_credits(db, member2)}.')
    else:
        await message.channel.send('Please type in positive number of credits!')


async def add_user(db, message):
    if await fio.search(db, message.author):
        await message.channel.send('User already exists, try again!')
    else:
        await fio.insert(db, message.author, 0)
        await message.channel.send(f'Wow! Welcome new member!\n '
                                   f'Global social credits of {message.author.name} are {await io.get_credits(db, message.author)}.')


async def ping_client(client, message):
    await message.channel.send(f'Your ping is {round(client.latency * 1000)}ms')


async def help_client(message):
    await message.channel.send(open('data/help/help.txt', 'r').read())


async def show_credits(db, message):
    member = message.content.split()[1]
    member_name = '**' + message.mentions[0].name + '**'
    if not await fio.search(db, member):
        await message.channel.send('User not found, try again!')
    else:
        text = f'Global social credits of {member_name} are {await io.get_credits(db, member)}.'

        if await io.get_credits(db, member) >= 1000:
            text += f'\nCongratulations, you can rest!'
        elif 1000 > await io.get_credits(db, member) >= 0:
            text += f'\nGood job, keep working!'
        else:
            text += f'\nYour execution date is tomorrow!'

        await message.channel.send(text)


async def show_credits_me(db, message):
    member = f'<@!{message.author.id}>'
    member_name = '**' + message.author.name + '**'
    if not await fio.search(db, member):
        await message.channel.send('User not found, try again!')
    else:
        text = f'Global social credits of {member_name} are {await io.get_credits(db, member)}.'

        if await io.get_credits(db, member) >= 1000:
            text += f'\nCongratulations, you can rest!'
        elif 1000 > await io.get_credits(db, member) >= 0:
            text += f'\nGood job, keep working!'
        else:
            text += f'\nYour execution date is tomorrow!'

        await message.channel.send(text)


async def add_credits(db, message):
    num = int(message.content.split(' ')[2])
    member = message.content.split()[1]
    member_name = '**' + message.mentions[0].name + '**'
    if num > 0:
        if not await fio.search(db, member):
            await message.channel.send('User not found, try again!')
        else:
            await fio.update(db, member, await io.get_credits(db, member) + num)
            await message.channel.send(f'Wow! {member_name}\'s global social credits has increased by {num}!\n '
                                       f'Global social credits of {member_name} are {await io.get_credits(db, member)}.')
    else:
        await message.channel.send('Please type in positive number of credits!')


async def set_credits(db, message):
    num = int(message.content.split(' ')[2])
    member = message.content.split()[1]
    member_name = '**' + message.mentions[0].name + '**'
    if not await fio.search(db, member):
        await message.channel.send('User not found, try again!')
    else:
        await fio.update(db, member, int(num))
        await message.channel.send(
            f'Hmmm... {member_name} has {await io.get_credits(db, member)} global social credits now!')


async def minus_credits(db, message):
    num = int(message.content.split(' ')[2])
    member = message.content.split()[1]
    member_name = '**' + message.mentions[0].name + '**'
    if num > 0:
        if not await fio.search(db, member):
            await message.channel.send('User not found, try again!')
        else:
            await fio.update(db, member, await io.get_credits(db, member) - num)
            await message.channel.send(f'Oh no! {member_name}\'s global social credits was decreased by {num}!\n '
                                       f'Current global social credits of {member_name} are {await io.get_credits(db, member)}.')
    else:
        await message.channel.send('Please type in positive number of credits!')
