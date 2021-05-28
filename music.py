import youtube_dl

class Video:
    def __init__(self, link ):
        ytdl = youtube_dl.YoutubeDL()
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]
