"""
@author Mohammad Mahjoub
@date Nov, 9, 2017
"""

from pytube import YouTube
from tkinter import *
# ==================================================Settings=====================
root = Tk()
root.title("Video Youtube Downloader")  # set up the title and size.
root.geometry('800x500')  # set up the size
color = 'gray77'
root.configure(bg=color)
root.resizable(width=False, height=False)
# ==================================================Variables=====================
quality = IntVar()

# ==================================================Frames========================
top = Frame(root, width=800, height=50, bg=color)
top.pack(side=TOP)
bottom = Frame(root, width=800, height=50, bg=color)
bottom.pack(side=BOTTOM)
left = Frame(root,  width=600, height=400, bg=color)
left.pack(side=LEFT)
right = Frame(root, width=250, height=400, bg=color)
right.pack(side=RIGHT)
# ==================================================Functions======================


def clear_all():
    clear_url()
    clear_path()


def clear_url():
    url.delete(0, 'end')


def clear_path():
    path.delete(0, 'end')


def download_video():
    youtube_url = str(url.get().strip())
    if youtube_url.startswith('https://www.youtube.com/'):
        yt = YouTube(youtube_url)
        videos = yt.streams.all()
        if quality.get() == 0:
            video = videos[0]
        else:
            video = videos[len(videos) - 1]
        video.download(str(path.get().strip()))  # download the video..
        clear_all()
    else:
        # ==================================================Update User========================
        info = "# You might forgot to enter a correct Url or path or haven't checked the Quality"
        user_update = Label(bottom, font=('arial', 20, 'bold'), text=info, bd=5, anchor='w', bg=color)
        user_update.grid(row=0, columns=1)


# ==================================================Buttons=================
btn_clear_url = Button(right, text="Clear Url", font=('arial', 25, 'bold'),
                       command=lambda: clear_url(), highlightbackground=color).grid(row=1, columns=1)
btn_clear_path = Button(right, text="Clear Path", font=('arial', 25, 'bold'),
                        command=lambda: clear_path(), highlightbackground=color).grid(row=3, columns=1)
btn_clear_all = Button(right, text="Clear all", font=('arial', 25, 'bold'),
                       command=lambda: clear_all(), highlightbackground=color).grid(row=5, columns=1)
btn_down_video = Button(right,  text="Download Video", font=('arial', 22, 'bold'),
                        command=lambda: download_video(), highlightbackground=color).grid(row=7, columns=1)
# ==================================================Labels===============
# This is the top lable
top_lable = Label(top,  font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5,
                  anchor='w', bg=color)
top_lable.grid(row=0, columns=1)
# This is the bottom lable
bottom_lable = Label(bottom, font=('arial', 20, 'bold'), text="YouTube Videos Downloader", bd=5, anchor='w', bg=color)
bottom_lable.grid(row=0, columns=1)
# This is for the url
url_lable = Label(left, font=('arial', 20, 'bold'), text="Url: ",  anchor='w', bg=color)
url_lable.grid(row=1, columns=1)
# This is for the path
path_lable = Label(left, font=('arial', 20, 'bold'), text="Path: ",  anchor='w', bg=color)
path_lable.grid(row=2, columns=1)
# ==================================================Entry================
url = Entry(left, font=('arial', 20, 'bold'), width=37, bd=8, insertwidth=7)
url.grid(row=1,  column=1, sticky=E+S)
path = Entry(left, font=('arial', 20, 'bold'), width=37, bd=8, insertwidth=7)
path.grid(row=2, column=1, sticky=E+S)
# ==================================================Radiobutton============
btn1_data = Radiobutton(left, text="Good Quality",  font=('arial', 20, 'bold'), variable=quality,  value=0, bg=color)
btn1_data.grid(row=0,  column=1, sticky=W)
btn2_data = Radiobutton(left, text="Bad Quality",  font=('arial', 20, 'bold'), variable=quality, value=1, bg=color)
btn2_data.grid(row=0,  column=1)


root.mainloop()
# Youtube Url: https://www.youtube.com/watch?v=okB3VsSiG5w
# file path: /Users/mohammad/Desktop
