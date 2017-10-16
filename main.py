from pytube import YouTube
from tkinter import *

# ==================================================Settings=======================================================
root = Tk()
root.title("Video Youtube Downloader") # set up the title and size.
root.geometry('800x500') # set up the size
#root.configure(background='white') # set up background.
root.resizable(width=False, height=False)
# ==================================================Veribles=======================================================
url_text = StringVar()
path_text = StringVar()
operator = ""
# ==================================================Frames=======================================================
top = Frame(root, width=800, height=50,  bg='yellow')
top.pack(side=TOP)
bottom = Frame(root, width=800, height=50,  bg='red')
bottom.pack(side=BOTTOM)
left = Frame(root,  width=600, height=400, bg='black')
left.pack(side=LEFT)
right = Frame(root, width=250, height=400)
right.pack(side=RIGHT)
# ==================================================Functions=======================================================
def url_video(link):
    global operator
    operator+=str(link)



def clear_all():
    pass

def clear_url():
    pass

def clear_path():
    pass





# ==================================================Buttons=======================================================
btn_clear_url = Button(right, text="Clear Url" ,font=('arial', 25, 'bold')).grid(row=1, columns=1)
btn_clear_path = Button(right, text="Clear Path", font=('arial', 25, 'bold')).grid(row=3, columns=1)
btn_clear_all = Button(right, text="Clear all", font=('arial', 25, 'bold')).grid(row=5, columns=1)
btn_down_video = Button(right,  text="Download Video", font=('arial', 22, 'bold')).grid(row=7, columns=1)
# ==================================================Labels=======================================================
title = Label(top,  font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5, anchor='w')
title.grid(row=0, columns=1)
feedback = Label(bottom, font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5, anchor='w')
feedback.grid(row=0, columns=1)
# ==================================================Entry=======================================================
url = Entry(left, font=('arial', 20, 'bold'), width=35, textvariable=url_text, bd=8, insertwidth=7,
                   bg="powder blue", command=lambda: url_video())  # style='calc.TButton'
url.grid(row=3, columns=1)
path = Entry(left, font=('arial', 20, 'bold'),width=35, textvariable=path_text, bd=8, insertwidth=7,
                   bg="powder blue")
path.grid(row=1,  sticky=W+N)






"""
url = IntVar()


Label(root, text="Enter url: ").pack(side=LEFT)
Label(root, text="Enter path: ").pack(side=LEFT)
Entry(root, bd=3).pack(side=LEFT)
Entry(root, bd=3).pack(side=LEFT)




yt = YouTube(str(input("Enter the video link: ")))
videos = yt.get_videos()


s = 1
for v in reversed(videos):
    # Keep the state Disabled until they start adding.
    Radiobutton(root, text=str(v), padx=40, font=('bold', 20), variable=var, value=s, command=sel).pack(anchor=E)
    s += 1




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
#get_video()
"""""

root.mainloop()