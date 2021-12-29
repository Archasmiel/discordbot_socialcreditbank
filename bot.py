from discord.ext import commands
from modules.start.onload import OnLoad
from modules.commands.message_listener import Messaging
from modules.commands.music_listener import Music

# database location and bot token
db = 'data/storage/data.json'
bot_token = 'OTE2MDQzOTQ4NDkxOTY0NDg2.YakaaA.2lJFBd1Z2hLv6BoA-uwCuOAX024'
client = commands.Bot(command_prefix='$')

# load cogs
client.add_cog(OnLoad(client, db))
client.add_cog(Messaging(client, db))
client.add_cog(Music(client, db))

client.run(bot_token)
