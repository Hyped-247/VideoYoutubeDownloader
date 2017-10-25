from pytube import YouTube
from tkinter import *
# ==================================================Settings==================================================
root = Tk()
root.title("Video Youtube Downloader") # set up the title and size.
root.geometry('800x500') # set up the size
root.resizable(width=False, height=False)

# ==================================================Frames=====================================================
top = Frame(root, width=800, height=50)
top.pack(side=TOP)
bottom = Frame(root, width=800, height=50)
bottom.pack(side=BOTTOM)
left = Frame(root,  width=600, height=400)
left.pack(side=LEFT)
right = Frame(root, width=250, height=400)
right.pack(side=RIGHT)
# ==================================================Functions===================================================

def clear_all():
    clear_url()
    clear_path()


def clear_url():
    url_text.set("")


def clear_path():
    path_text.set("")


def download_video(url):
    youtube_url = str(url)
    if youtube_url.startswith("https://www.youtube.com/"):
        yt = YouTube(youtube_url)
        videos = yt.streams.filter(adaptive=True).all()
        if videos.count () > 0:
            video = videos[quality.get()]
            video.download(path_text)
        else:
            print("There are no videos to download...")
            
    else:
        # tell the user that this is is no a url.
        print("Please enter a correct url... ")



# ==================================================Buttons======================================
btn_clear_url = Button(right, text="Clear Url", font=('arial', 25, 'bold'), command=lambda: clear_url())\
    .grid(row=1, columns=1)
btn_clear_path = Button(right, text="Clear Path", font=('arial', 25, 'bold'), command=lambda: clear_path())\
    .grid(row=3, columns=1)
btn_clear_all = Button(right, text="Clear all", font=('arial', 25, 'bold'),
                       command=lambda: clear_all())\
    .grid(row=5, columns=1)
btn_down_video = Button(right,  text="Download Video", font=('arial', 22, 'bold')
                        , command=lambda: download_video(url_text)).grid(row=7, columns=1)
# ==================================================Labels========================================
# This is the top lable
top_lable = Label(top,  font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5, anchor='w')
top_lable.grid(row=0, columns=1)

# This is the bottom lable
bottom_lable = Label(bottom, font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5, anchor='w')
bottom_lable.grid(row=0, columns=1)

# This is the left lable

# This is for the url
url_lable = Label(left, font=('arial', 20, 'bold'), text="Url: ",  anchor='w')
url_lable.grid(row=0, columns=1)

# This is for the path
path_lable = Label(left, font=('arial', 20, 'bold'), text="Path: ",  anchor='w')
path_lable.grid(row=1, columns=1)


# ==================================================Variables===================================
path_text = StringVar()
url_text = StringVar()
video_nummber = StringVar()
quality = StringVar()
# ==================================================Radiobutton===================================

btn1_data = Radiobutton(root, text="Good Quality", padx=40, font=('bold', 20), variable=quality, value="1")
btn1_data.pack (anchor=E)

btn2_data = Radiobutton(root, text="Good Quality", padx=40, font=('bold', 20), variable=quality, value="2")
btn2_data.pack (anchor=E)
# ==================================================Entry=======================================
# The width should be 37
url = Entry(left, font=('arial', 20, 'bold'), width=37, textvariable=url_text, bd=8, insertwidth=7,
            bg="powder blue")
url.grid(row=0,  column=1, sticky=E+S)
path = Entry(left, font=('arial', 20, 'bold'), width=37, textvariable=path_text, bd=8, insertwidth=7,bg="powder blue")
path.grid(row=1, column=1, sticky=E+S)


root.mainloop()
