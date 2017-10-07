from pytube import YouTube
from tkinter import *

class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.url = Entry()
        self.url.pack()

        self.path = Entry() # This creates a place to pass information
        self.path.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("Enter Video url:")


        # tell the entry widget to watch this variable
        self.url["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.url.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->",
              self.contents.get())

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("VideoYoutubeDownloader")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()




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


