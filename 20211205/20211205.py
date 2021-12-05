import os
from moviepy.editor import *
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
import time


def hi_fun3():
    if os.path.isfile('20211128/lol.mp4'):
        clip = VideoFileClip('20211128/lol.mp4')
        # clip.preview()
        clip = clip.subclip(int(b.get()), int(c.get()))
        i = 0
        video_path = '20211128/'
        new_path = video_path+str(i)+'.mp4'
        while os.path.isfile(new_path):
            i += 1
            new_path = video_path+a.get()+str(i)+'.mp4'
        if state.get() == True:
            clip.write_gif(new_path)
        else:
            clip.write_videofile(new_path)
        display4.config(text='切割完畢', fg='black', bg="#FFFFFF")
    else:
        exit()


win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")

display1 = Label(win, text='請輸影片名稱', fg='black', bg="#FFFFFF")
display1.grid(row=0, column=0)

a = Entry(win)
a.grid(row=0, column=1)

display2 = Label(win, text='開始時間', fg='black', bg="#FFFFFF")
display2.grid(row=1, column=0)

b = Entry(win)
b.grid(row=1, column=1)

display3 = Label(win, text='結束時間', fg='black', bg="#FFFFFF")
display3.grid(row=2, column=0)

c = Entry(win)
c.grid(row=2, column=1)

btn = Button(win, text='開始切割', command=hi_fun3)
btn.grid(row=3, columnspan=2)

display4 = Label(win, text='請切割', fg='black', bg="#FFFFFF")
display4.grid(row=4, columnspan=2)

state = BooleanVar()
state.set(True)
chk = Checkbutton(win, text='gif', var=state)
chk.grid(row=4, column=0)

win.mainloop()
