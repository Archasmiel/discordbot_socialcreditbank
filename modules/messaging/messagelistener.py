from datetime import datetime as t
from discord.ext import commands
from modules.basicio import moduleio as io


class Messaging(commands.Cog):

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.Cog.listener()
    async def on_message(self, message):
        author = f'<@!{message.author.id}>'

        if message.content == '?greet':
            temp = await io.get_greettime(self.db, author)

            if t.now().strftime("%d.%m.%Y %H:%M:%S").split(' ')[0] != temp.split(' ')[0]:
                await message.channel.send(f'**Oh, hello {author}! Thank you for greeting!**\n'
                                           f'Now your rate increased by 10!')
                await io.update(self.db, author, await io.get_credits(self.db, author) + 10)
            else:
                if t.now().strftime("%d.%m.%Y %H:%M:%S").split(' ')[1].split(':')[0] != temp.split(' ')[1].split(':')[0]:
                    await message.channel.send('**Oh hello again! Thank you very much, pal.**\n'
                                               'You now have 1 more global social credits!')
                    await io.update(self.db, author, await io.get_credits(self.db, author) + 1)
                    await io.updategreettime(self.db, author, t.now().strftime("%d.%m.%Y %H:%M:%S"))
                else:
                    await message.channel.send('**Pal, I\'m working now, don\'t bother me!**')

        if message.content.find('#deletemsg') == 0:
            await message.channel.purge(limit=int(message.content.split()[1])+1)
            await message.channel.send(f'Deleted {int(message.content.split()[1])+1}')
