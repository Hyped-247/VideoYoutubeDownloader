from pytube import YouTube
from tkinter import *



def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text=selection)


root = Tk()
root.title("Video Youtube Downloader") # set up the title.
var = IntVar()
# Keep the state Disabled until they start adding 
R1 = Radiobutton(root, text="Option 1", variable=var, value=1, command=sel, state=DISABLED).pack(anchor=E)
R2 = Radiobutton(root, text="Option 2", variable=var, value=2, command=sel).pack(anchor=E)
R3 = Radiobutton(root, text="Option 3", variable=var, value=3, command=sel).pack(anchor=E)
label = Label(root)
label.pack()
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


