import yt_dlp

ydl_opts = {
    'format': 'bestaudio',
    'outtmpl': 'song.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info('https://www.youtube.com/watch?v=qGS4G93Q0GI', download=True)
    song_url = info['url']
    print(song_url)
