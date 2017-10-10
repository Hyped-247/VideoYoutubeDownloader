from pytube import YouTube
from tkinter import *


def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text=selection)


root = Tk()
root.title("Video Youtube Downloader").minsize(880, 880).maxsize(880, 880) # set up the title and size.
root.configure(background='white') # set up background.
var = IntVar()
label = Label(root, "Enter the video link: ").pack(side=LEFT)

yt = YouTube(str(input("Enter the video link: ")))
videos = yt.get_videos()


s = 1
for v in reversed(videos):
    # Keep the state Disabled until they start adding.
    Radiobutton(root, text=str(v), padx=40, font=('bold', 20), variable=var, value=s, command=sel).pack(anchor=E)
    s += 1

root.mainloop()


def get_video():
    yt = YouTube(str(input("Enter the video link: ")))
    videos = yt.get_videos()

    s = 1
    for v in videos:
        print(str(s)+". "+str(v))
        s += 1

    n = int(input("Enter the number of the video: "))
    vid = videos[n-1]

    destination = str(input("Enter the destination: "))
    vid.download(destination)

    print(yt.filename+"\nHas been successfully downloaded")
get_video()