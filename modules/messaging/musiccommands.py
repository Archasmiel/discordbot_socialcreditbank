import discord
import youtube_dl


async def join(message):
    if message.author.voice is None:
        message.channel.send('You are not in voice channel!')
    else:
        channel = message.author.voice.channel
        if message.author.guild.voice_client is None:
            await channel.connect()
        else:
            await message.author.guild.voice_client.move_to(channel)


async def disconnect(message):
    await message.author.guild.voice_client.disconnect()


async def pause(message):
    await message.author.guild.voice_client.pause()
    await message.channel.send('Paused')


async def resume(message):
    await message.author.guild.voice_client.resume()
    await message.channel.send('Resumed')


async def play(message):
    link = message.content.split()[1]
    message.author.guild.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'noplaylist': 'True',
        'outtmpl': 'song.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'weba',
            'preferredquality': '192',
        }],
    }
    vc = message.author.guild.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(link, download=False)
        # await message.channel.send(info['formats'][0]['url'])
        url2 = info['formats'][0]['url']
        # source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS, executable='data/ffmpeg/bin/ffmpeg.exe')
        vc.play(discord.FFmpegOpusAudio(executable=r"data/ffmpeg/bin/ffmpeg.exe", source=url2))
