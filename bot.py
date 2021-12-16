from discord.ext import commands
from modules.start.onload import OnLoad
from modules.messaging.messagelistener import Messaging
from modules.commands.usercommands_delete import UserCommands

db = 'data/storage/data.json'
bot_token = ''
client = commands.Bot(command_prefix='$')

client.add_cog(OnLoad(client, db))
client.add_cog(Messaging(client, db))
client.add_cog(UserCommands(client, db))
client.run(bot_token)
