import discord
from discord.ext import commands


class PictureCommands(commands.Cog):

    root = '../../'

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.command(aliases=['showleader'])
    async def _showkimchanin(self, ctx):
        await ctx.send(file=discord.File('kimchanin.png'))

    @commands.command(aliases=['showmessiah'])
    async def _showjohnxina(self, ctx):
        await ctx.send(file=discord.File('johnxina.jpg'))

    @commands.command(aliases=['showgod'])
    async def _showxinping(self, ctx):
        await ctx.send(file=discord.File('xinping.jpg'))