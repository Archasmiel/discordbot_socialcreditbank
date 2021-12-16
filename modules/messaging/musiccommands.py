import discord
import yt_dlp

FFMPEG_OPTIONS = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
FFMPEG_PATH = "data/ffmpeg/bin/ffmpeg.exe"
YDL_CFG = {
        'format': 'bestaudio',
        'outtmpl': 'song.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'weba',
            'preferredquality': '192',
        }],
    }


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

    vc = message.author.guild.voice_client

    with yt_dlp.YoutubeDL(YDL_CFG) as ydl:
        info = ydl.extract_info(link, download=False)

        # await message.channel.send(info['formats'][0]['url'])
        song_url = info['url']
        source = await discord.FFmpegOpusAudio.from_probe(song_url, before_options=FFMPEG_OPTIONS, executable=FFMPEG_PATH)
        vc.play(source)
