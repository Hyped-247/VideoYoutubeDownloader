from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=okB3VsSiG5w')
videos = yt.streams.all()
video = videos[0]
video.download('/Users/mohammadmohjoub/Desktop')