from discord.ext import commands
from modules.start.onload import OnLoad
from modules.messaging.messagelistener import Messaging
from modules.commands.usercommands import UserCommands

db = 'data/storage/data.json'
bot_token = 'OTE2MDQzOTQ4NDkxOTY0NDg2.YakaaA.c2GYXtREAAw8MWIpnJfY2w3zRj8'
client = commands.Bot(command_prefix='$')

client.add_cog(OnLoad(client, db))
client.add_cog(Messaging(client, db))
client.add_cog(UserCommands(client, db))
client.run(bot_token)
