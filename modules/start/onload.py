from discord.ext import commands
from modules.basicio import io as io


class OnLoad(commands.Cog):

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is working')
