from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))
videos = yt.streams.filter(adaptive=True).all()

if videos.count() > 0:
	pass

s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))
vid = videos[n-1]

destination = str(input("Enter the destination: "))
vid.download(destination)

print(yt.title+"\nHas been successfully downloaded")
