from discord.ext import commands
from modules.start.onload import OnLoad
from modules.commands.message_listener import Messaging

# database location and bot token
db = 'data/storage/data.json'
bot_token = 'OTE2MDQzOTQ4NDkxOTY0NDg2.YakaaA.ylVeMzJkF88aOm5rmhAAvByRh-A'
client = commands.Bot(command_prefix='#')
client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'russia'
    }
]

# load cogs
client.add_cog(OnLoad(client, db))
client.add_cog(Messaging(client, db))
client.load_extension('dismusic')

client.run(bot_token)
