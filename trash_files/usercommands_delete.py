from discord.ext import commands


class UserCommands(commands.Cog):

    def __init__(self, client, db):
        self.client = client
        self.db = db

