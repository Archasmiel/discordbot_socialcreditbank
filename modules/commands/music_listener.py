from discord.ext import commands
import modules.commands.DiscordUtilsModified as Library

music = Library.Music()


class Music(commands.Cog):

    @staticmethod
    def count_queue_size(ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            return 0
        return len(player.current_queue())

    def __init__(self, client, db):
        self.client = client
        self.db = db

    @commands.command()
    async def helpmusic(self, ctx):
        await ctx.send(f'$joinbot - перекидывание бота по каналам\n'
                       f'$play <url> - проигрывание песни из ссылки (если бота нету то добавит его в канал с автором) '
                       f'(добавляет не плейлист а только 1 песню)\n'
                       f'$pause - остановить проигрывание\n'
                       f'$resume - продолжить проигрывание\n'
                       f'$leave - выкинуть бота из канала\n'
                       f'$queue - список плейлиста ботика\n'
                       f'$nowplays - что сейчас играет в боте\n'
                       )

    @commands.command()
    async def joinbot(self, ctx):
        if ctx.author.voice is None:
            return await ctx.send('**Ты не в голосовом канале, дружище.**')

        voice_channel_member = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel_member.connect()
            return await ctx.send(f'Подключился в канал **{voice_channel_member}**.')
        else:
            if voice_channel_member.id is not ctx.guild.me.voice.channel.id:
                await ctx.voice_client.move_to(voice_channel_member)
                return await ctx.send(f'Переключился в канал **{voice_channel_member}**.')
            await ctx.send(f'**Я уже нахожусь в твоём голосовом канале.**')

    @commands.command()
    async def leave(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        if ctx.voice_client is None:
            return await ctx.send(f'**Я не могу ливнуть если я не в голосовом канале.**')
        print([str(i) for i in music.players])
        await ctx.send(f'Вышел из **{ctx.guild.me.voice.channel}**.')
        await ctx.voice_client.disconnect()
        music.players.remove(player)

    @commands.command()
    async def pause(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f'Приостановил проигрывание **{song.name}**.')

    @commands.command()
    async def resume(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f'Продолжаю проигрывание **{song.name}**.')

    @commands.command()
    async def nowplays(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            return await ctx.send(f'**Текущего трека нету, поскольку нету активного пригрывателя на сервере.**')
        await ctx.send(''.join([f'**{song.name if i == 0 else ""}**\n'
                                for i, song in enumerate(player.current_queue())]))

    @commands.command()
    async def queue(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            return await ctx.send(f'**Списка музыки нету, поскольку нету активного пригрывателя на сервере.**')
        await ctx.send(''.join([f'**[ {i if i != 0 else "текущий"} ]: {song.name}**\n'
                                for i, song in enumerate(player.current_queue())]))

    @commands.command()
    async def play(self, ctx, *, url):

        if ctx.author.voice is None:
            return await ctx.send('**Ты не в голосовом канале, дружище.**')

        voice_channel_member = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel_member.connect()
            await ctx.send(f'Подключился в канал **{voice_channel_member}**.')
        else:
            if voice_channel_member.id is not ctx.guild.me.voice.channel.id:
                await ctx.voice_client.move_to(voice_channel_member)
                await ctx.send(f'Переключился в канал **{voice_channel_member}**.')

        player = music.get_player(guild_id=ctx.guild.id)

        url = url.split('&')[0]

        if ctx.voice_client is None:
            return await ctx.send(f'**Я не в голосовом канале и не могу создать проигрыватель.**')

        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)

        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f'Начинаю проигрывать **{song.name}**.')
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f'Добавил песню **{song.name}** в плейлист c индексом.')
