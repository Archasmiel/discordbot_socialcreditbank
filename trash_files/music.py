import discord
import yt_dlp
from yt_dlp import YoutubeDL


YDL_CFG = {
    'format': 'bestaudio',
    'outtmpl': 'song.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'weba',
        'preferredquality': '192',
    }],
}
FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}
ydl = yt_dlp.YoutubeDL(YDL_CFG)
queues = {}
queue = []
names = []


def get_link(string):
    return string.content.split()[1]


def get_url(string):
    return get_link(string).split('&')[0]


def get_song(string, download):
    return ydl.extract_info(get_url(string), download=download)


def add_to_queues(guild, link, title):
    queues.update({guild: (queues.get(guild) + [link, title])})


'''
async def join(message):
    member_voice = message.author.voice
    member_channel = message.author.voice.channel
    if member_voice and channel:
        try:
            await
        except:
        message.channel.send('You are not in voice channel!')
    else:

        if message.author.guild.voice_client is None:
            await channel.connect()
        else:
            await message.author.guild.voice_client.move_to(channel)


async def disconnect(message):
    await clear_queue(message)
    await message.author.guild.voice_client.disconnect()


async def pause(message):
    message.author.guild.voice_client.pause()
    await message.channel.send('Paused playing!')


async def resume(message):
    message.author.guild.voice_client.resume()
    await message.channel.send('Resumed playing!')


async def stop(message):
    message.author.guild.voice_client.stop()
    await message.channel.send('Stopped playing!')


async def play(client, message, repeat=0):
    global queue

    if repeat == 0:
        queues.update()

        await message.channel.send(f'Successfully added song to playlist!\n'
                                   f'Queue size now is {len(queue)}')
    await play_song(client, message)


async def play_song(client, message):
    voice = message.author.guild.voice_client
    if queue != [] and not voice.is_playing():
        title = queue[0]['title']
        link = queue[0]['url']
        await message.channel.send(f'Playing **{title}** now.')
        queue.pop(0)
        voice.play(discord.FFmpegPCMAudio(link, before_options=FFMPEG_OPTIONS),
                   after=lambda error: client.loop.create_task(play_song(client, message)))


async def show_queue(message):
    guild = message.author.guild.voice_client
    res = ''
    if len(queue) != 0:
        for i in queues[guild]:
            title = i[1]
            if i == 0:
                res += f'[current]: **{title}**\n'
            else:
                res += f'[{i}]: **{title}**\n'
        await message.channel.send(res)
    else:
        await message.channel.send('Queue is empty!')


async def clear_queue(message):
    global queue
    queue.clear()
    await stop(message)
    await message.channel.send('Queue was cleared!')
'''
