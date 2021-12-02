import discord
from discord.ext import commands

global usercount, creditbank
global usersf, creditf
usersf = 'savedusers.txt'
creditf = 'creditusers.txt'


async def readcredits():
    global usercount, creditbank, usersf, creditf
    users = [i.rstrip() for i in open(usersf, 'r')]
    credit = [int(i.rstrip()) for i in open(creditf, 'r')]
    creditbank = [users, credit]
    usercount = len(users)


async def writecredits():
    global usercount, creditbank, usersf, creditf
    with open(usersf, 'w') as f:
        for i in creditbank[0]:
            f.write(str(i) + '\n')

    with open(creditf, 'w') as f:
        for i in creditbank[1]:
            f.write(str(i) + '\n')


async def printcredits():
    global usercount
    for i in range(usercount):
        print(str(creditbank[0][i]) + ': ' + str(creditbank[1][i]))


welcome_text = ' has joined a server!'
leave_text = ' has left a server!'
bot_token = 'OTE2MDQzOTQ4NDkxOTY0NDg2.YakaaA.zGh9Mk2ci5T47TLQ9FItgon8D6M'
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Bot is working')
    await readcredits()
    await writecredits()


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    await readcredits()
    await ctx.send('Succesfully been enabled!')
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    await writecredits()
    await ctx.send('Succesfully been disabled!')
    client.unload_extension(f'cogs.{extension}')


@client.event
async def on_member_join(member):
    print(f'{member}' + welcome_text)


@client.event
async def on_member_remove(member):
    print(f'{member}' + leave_text)


@client.command()
async def ping(ctx):
    await ctx.send(f'Your ping is {round(client.latency * 1000)}ms')


@client.command(aliases=['helpme'])
async def _helpbot(ctx):
    await ctx.send(open('help.txt', 'r').read())


@client.command(aliases=['showleader'])
async def _showkimchanin(ctx):
    await ctx.send(file=discord.File('kimchanin.png'))


@client.command(aliases=['showmessiah'])
async def _showjohnxina(ctx):
    await ctx.send(file=discord.File('johnxina.jpg'))


@client.command(aliases=['showgod'])
async def _showxinping(ctx):
    await ctx.send(file=discord.File('xinping.jpg'))


@client.command(aliases=['show'])
async def _showcredits(ctx, member):
    await readcredits()
    for i in range(len(creditbank[0])):
        if creditbank[0][i] == member:
            text = f'Social credits of {creditbank[0][i]} are {creditbank[1][i]}.'
            if creditbank[1][i] >= 1000:
                text += f'\nCongratulations, you can rest!'
            elif 1000 > creditbank[1][i] >= 0:
                text += f'\nGood job, keep working!'
            else:
                text += f'\nYour execution date is tomorrow!'
            await ctx.send(text)



@client.command(aliases=['addu'])
async def _addcomrade(ctx, member):
    await readcredits()
    exists = False
    for i in range(len(creditbank[0])):
        if creditbank[0][i] == member:
            exists = True

    if not exists:
        print(member)
        creditbank[0].append(member)
        creditbank[1].append(0)
        await ctx.send(f'Wow! Welcome new member!\n '
                       f'Social credits of {creditbank[0][len(creditbank[0]) - 1]} are '
                       f'{creditbank[1][len(creditbank[1]) - 1]}.')
    else:
        await ctx.send(f'Error! Current users exists!')
    await writecredits()


@client.command(aliases=['addc'])
async def _addcredits(ctx, member, numcredits):
    await readcredits()
    current_user = -1
    for i in range(len(creditbank[0])):
        if creditbank[0][i] == member:
            current_user = i
            creditbank[1][i] += int(numcredits)
    if current_user > -1:
        await ctx.send(f'Wow! {creditbank[0][current_user]}\'s social credits has increased by {numcredits}!\n '
                       f'Social credits of {creditbank[0][current_user]} are {creditbank[1][current_user]}.')
    else:
        await ctx.send(f'Error! Current users don\'t exist!')
    await writecredits()


@client.command(aliases=['setc'])
async def _setcredits(ctx, member, numcredits):
    await readcredits()
    current_user = -1
    for i in range(len(creditbank[0])):
        if creditbank[0][i] == member:
            current_user = i
            creditbank[1][i] = int(numcredits)

    if current_user > -1:
        await ctx.send(f'Hmmm... {creditbank[0][current_user]} has {numcredits} social credits now!')
    else:
        await ctx.send(f'Error! Current users don\'t exist!')
    await writecredits()


@client.command(aliases=['minusc'])
async def _minuscredits(ctx, member, numcredits):
    await readcredits()
    current_user = 0
    for i in range(len(creditbank[0])):
        if creditbank[0][i] == member:
            current_user = i
            creditbank[1][i] -= int(numcredits)

    await ctx.send(f'Oh no! {creditbank[0][current_user]}\'s social credits was decreased by {numcredits}!\n '
                   f'Current social credits of {creditbank[0][current_user]} are {creditbank[1][current_user]}.')
    await writecredits()


client.run(bot_token)
