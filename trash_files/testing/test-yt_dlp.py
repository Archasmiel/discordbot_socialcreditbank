import yt_dlp

ydl_opts = {
    'format': 'bestaudio',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

links = [f'https://www.youtube.com/watch?v=xzVZq5-J9uo',
         ]

for link in links:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link.split('&')[0], download=True)
        song_url = info['url']
