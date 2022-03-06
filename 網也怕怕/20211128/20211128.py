from pytube import YouTube
import ssl
from os import read
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
import pandas as pd
import datetime as dt
import numpy as np


def hi_fun3():
    ssl._create_default_https_context = ssl.create_default_context
    yt = YouTube(a.get())
    print('>>>> NOW1')
    video = yt.streams
    length = len(video)
    print(video)
    result = video.filter(progressive=True, subtype='mp4', res='720p')
    print(result[0])
    load_name = str("20211128/"+b.get()+".mp4")
    display3.config(text='電影名稱 = '+b.get(),
                    fg='black', bg="#FFFFFF")
    display4.config(text='電影時間 ='+str(yt.length)+"秒",
                    fg='black', bg="#FFFFFF")
    result[0].download(filename=load_name)
    print('>>>> NOW2')

# for i in range(length):
#     print(video[i])
# print('影片名稱', yt.title)
# print('影片作者', yt.author)
# print('影片長度', yt.length, "秒")
# print('縮圖網址:', yt.thumbnail_url)


win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")

display1 = Label(win, text='請輸入下載網址', fg='black', bg="#FFFFFF")
display1.grid(row=0, column=0)

a = Entry(win)
a.grid(row=0, column=1)

display2 = Label(win, text='請輸入影片名稱', fg='black', bg="#FFFFFF")
display2.grid(row=1, column=0)

b = Entry(win)
b.grid(row=1, column=1)

btn = Button(win, text='下載', command=hi_fun3)
btn.grid(row=2, columnspan=2)

display3 = Label(win, text='電影名稱 =', fg='black', bg="#FFFFFF")
display3.grid(row=3, column=0)

display4 = Label(win, text='電影時間 =', fg='black', bg="#FFFFFF")
display4.grid(row=4, column=0)


win.mainloop()
