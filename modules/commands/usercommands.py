from discord.ext import commands
from modules.basicio import moduleio as io


class UserCommands(commands.Cog):

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.command(aliases=['ping'])
    async def _pingme(self, ctx):
        await ctx.send(f'Your ping is {round(self.client.latency * 1000)}ms')

    @commands.command(aliases=['helpme'])
    async def _helpbot(self, ctx):
        await ctx.send(open('data/help/help.txt', 'r').read())

    @commands.command(aliases=['addu'])
    async def _addcomrade(self, ctx, member):
        if await io.search(self.db, member):
            await ctx.send('User already exists, try again!')
        else:
            await io.insert(self.db, member, 0)
            await ctx.send(f'Wow! Welcome new member!\n '
                           f'Global social credits of {member} are {await io.get_credits(self.db, member)}.')

    @commands.command(aliases=['show'])
    async def _showcredits(self, ctx, member):
        if not await io.search(self.db, member):
            await ctx.send('User not found, try again!')
        else:
            text = f'Global social credits of {member} are {await io.get_credits(self.db, member)}.'

            if await io.get_credits(self.db, member) >= 1000:
                text += f'\nCongratulations, you can rest!'
            elif 1000 > await io.get_credits(self.db, member) >= 0:
                text += f'\nGood job, keep working!'
            else:
                text += f'\nYour execution date is tomorrow!'

            await ctx.send(text)

    @commands.command(aliases=['addc'])
    async def _addcredits(self, ctx, member, num):
        if not await io.search(self.db, member):
            await ctx.send('User not found, try again!')
        else:
            await io.update(self.db, member, await io.get_credits(self.db, member) + int(num))
            await ctx.send(f'Wow! {member}\'s global social credits has increased by {num}!\n '
                           f'Global social credits of {member} are {await io.get_credits(self.db, member)}.')

    @commands.command(aliases=['setc'])
    async def _setcredits(self, ctx, member, num):
        if not await io.search(self.db, member):
            await ctx.send('User not found, try again!')
        else:
            await io.update(self.db, member, int(num))
            await ctx.send(f'Hmmm... {member} has {await io.get_credits(self.db, member)} global social credits now!')

    @commands.command(aliases=['minusc'])
    async def _minuscredits(self, ctx, member, num):
        if not await io.search(self.db, member):
            await ctx.send('User not found, try again!')
        else:
            await io.update(self.db, member, await io.get_credits(self.db, member) - int(num))
            await ctx.send(f'Oh no! {member}\'s global social credits was decreased by {num}!\n '
                           f'Current global social credits of {member} are {await io.get_credits(self.db, member)}.')

    @commands.command(aliases=['transferc'])
    async def _transfercredits(self, ctx, member1, member2, num):
        if not await io.search(self.db, member1) or not await io.search(self.db, member2):
            await ctx.send('User not found, try again!')
        else:
            await io.update(self.db, member1, await io.get_credits(self.db, member1) - int(num))
            await io.update(self.db, member2, await io.get_credits(self.db, member2) + int(num))
            await ctx.send(f'Wow! {member2}\'s global social credits was increased by {num}, but at what price!\n'
                           f'{member1}\'s {num} global credits was transferred to {member2}!\n'
                           f'Current global social credits of {member1} are {await io.get_credits(self.db, member1)}.\n'
                           f'Current global social credits of {member2} are {await io.get_credits(self.db, member2)}.')

    @commands.command(aliases=['showroles'])
    async def _bshowroles(self, ctx):
        for i in ctx.guild.roles:
            await ctx.send(i)

    @commands.command(aliases=['deletemsg'])
    async def _msgdelete(self, ctx):
        await ctx.message.delete()
