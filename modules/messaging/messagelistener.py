import modules.basicio.roles as role_io
from discord.ext import commands
import modules.messaging.messagetypes as mt
import modules.basicio.commands as cmd
import modules.messaging.musiccommands as music


class Messaging(commands.Cog):

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.Cog.listener()
    async def on_message(self, message):

        author_id = f'<@!{message.author.id}>'
        author = message.author
        author_name = message.author
        guild = message.guild
        author_roles = [r.name for r in author.roles]
        channel = message.channel
        content = message.content

        if content.find('#') == 0:
            # create roles on server
            if await cmd.command_check('#createroles', content, author_roles, channel):
                await role_io.init_roles_guild(guild, [i.name for i in guild.roles])

            # delete common roles from user on server
            if await cmd.command_check_advanced('#deleteroles <@![0-9]+>', '#deleteroles', content, author_roles, channel):
                await role_io.delete_roles(message.mentions[0])

            # create common roles for user on server
            if await cmd.command_check_advanced('#initroles <@![0-9]+>', '#initroles', content, author_roles, channel):
                await cmd.init_roles(self.db, message.mentions[0], f'<@!{message.mentions[0].id}>')

            # bot ping command
            if await cmd.command_check('#ping', content, author_roles, channel):
                await mt.ping_client(self.client, message)

            # help comment command
            if await cmd.command_check('#help', content, author_roles, channel):
                await mt.help_client(message)

            # adding current user to system
            if await cmd.command_check('#addu', content, author_roles, channel):
                await mt.add_user(self.db, message)
                await cmd.init_roles(self.db, author, author_id)

            # showing credits of user
            if await cmd.command_check('#showme', content, author_roles, channel):
                await mt.show_credits_me(self.db, message)
                await cmd.init_roles(self.db, author, author_id)

            # showing credits of user
            if await cmd.command_check_advanced('#show <@![0-9]+>', '#show', content, author_roles, channel):
                await mt.show_credits(self.db, message)
                await cmd.init_roles(self.db, message.mentions[0], f'<@!{message.mentions[0].id}>')

            # adding credits to user
            if await cmd.command_check_advanced('#addc <@![0-9]+> -?[0-9]+', '#addc', content, author_roles, channel):
                await mt.add_credits(self.db, message)
                await cmd.init_roles(self.db, message.mentions[0], f'<@!{message.mentions[0].id}>')

            # setting credits to user
            if await cmd.command_check_advanced('#setc <@![0-9]+> -?[0-9]+', '#setc', content, author_roles, channel):
                await mt.set_credits(self.db, message)
                await cmd.init_roles(self.db, message.mentions[0], f'<@!{message.mentions[0].id}>')

            # setting credits to user
            if await cmd.command_check_advanced('#minusc <@![0-9]+> -?[0-9]+', '#minusc', content, author_roles, channel):
                await mt.minus_credits(self.db, message)
                await cmd.init_roles(self.db, message.mentions[0], f'<@!{message.mentions[0].id}>')

            # transferring credits
            if await cmd.command_check_advanced('#transferc <@![0-9]+> -?[0-9]+', '#transferc', content, author_roles, channel):
                await mt.transfer_credits(self.db, message)
                await cmd.init_roles(self.db, author, author_id)
                await cmd.init_roles(self.db, message.mentions[1], f'<@!{message.mentions[1].id}>')

            # greet to bot
            if await cmd.command_check('#greet', content, author_roles, channel):
                await mt.greet_message(self.db, message, author_name, author_id)
                await cmd.init_roles(self.db, author, author_id)

            # delete certain count of messages
            if await cmd.command_check_advanced('#deletemsg [0-9]+', '#deletemsg', content, author_roles, channel):
                await mt.delete_messages(message, author_name)

            # show all roles on server
            if await cmd.command_check('#showroles', content, author_roles, channel):
                await mt.show_roles(message)

            if await cmd.command_check('#play', content, author_roles, channel):
                await music.join(message)
                await music.play(message)

            if await cmd.command_check('#pause', content, author_roles, channel):
                await music.pause(message)

            if await cmd.command_check('#resume', content, author_roles, channel):
                await music.resume(message)

            if await cmd.command_check('#disconnect', content, author_roles, channel):
                await music.disconnect(message)
