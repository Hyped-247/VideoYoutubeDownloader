from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))
videos = yt.streams.all()
print(videos)

if videos.count() > 0:
	pass
