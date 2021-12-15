import discord
import discord.utils as util

from modules.basicio import io as io

common_roles = ['Good worker', 'Average slave', 'Already dead']
common_roles_colour = [discord.Color.green(), discord.Color.orange(), discord.Color.red()]
admin_roles = ['SocialCreditAdmin']
admin_roles_colour = [discord.Color.purple()]
admin_permission = discord.Permissions(administrator=True)

common_commands = ['#transferc', '#show', '#showme', '#addu', '#help', '#ping', '#createroles', '#greet']
admin_commands = ['#addc', '#setc', '#minusc', '#deleteroles', '#showroles', '#initroles']


async def init_roles_guild(guild, guild_roles):
    for r in range(len(common_roles)):
        if common_roles[r] not in guild_roles:
            print(f'CREATED COMMON ROLE {common_roles[r]} ON {guild.name}')
            await guild.create_role(name=common_roles[r], colour=common_roles_colour[r])
    for r in range(len(admin_roles)):
        if admin_roles[r] not in guild_roles:
            print(f'CREATED ADMIN ROLE ON {guild.name}')
            await guild.create_role(name=admin_roles[r], colour=admin_roles_colour[r], permissions=admin_permission)


async def add_roles(db, member, member_id):
    mem_credits = await io.get_credits(db, member_id)
    if mem_credits > 1000:
        await member.add_roles(util.get(member.guild.roles, name=common_roles[0]))
    elif 0 <= mem_credits <= 1000:
        await member.add_roles(util.get(member.guild.roles, name=common_roles[1]))
    else:
        await member.add_roles(util.get(member.guild.roles, name=common_roles[2]))


async def delete_roles(member):
    for r in common_roles:
        await member.remove_roles(util.get(member.guild.roles, name=r))


async def check_server_role(db, member, member_id, roles):
    count = 0
    for i in roles:
        if i in common_roles:
            count += 1
    if count > 1:
        await delete_roles(member)
        await add_roles(db, member, member_id)


def usable_cmd(command, roles):
    if command in common_commands:
        return True
    for i in range(len(roles)):
        if roles[i] == admin_roles[0]:
            return True
    return False
