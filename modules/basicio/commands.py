import modules.basicio.roles as role_io
import re


async def command_check(regex, msg, roles, channel):
    if compare(regex, msg):
        if role_io.usable_cmd(regex, roles):
            return True
        else:
            await channel.send('You cannot use this command!')
            return False


async def command_check_advanced(regex1, regex2, msg, roles, channel):
    if compare(regex1, msg):
        if role_io.usable_cmd(regex2, roles):
            return True
        else:
            await channel.send('You cannot use this command!')
            return False


async def init_roles(db, member, member_id):
    await role_io.delete_roles(member)
    await role_io.add_roles(db, member, member_id)


def compare(regex, text):
    return len(re.compile(regex).findall(text)) == 1