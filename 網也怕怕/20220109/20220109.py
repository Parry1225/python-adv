import os
from tkinter import font
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


def get_cut():
    red_val = sel.get()
    print(red_val)
    status.config(text=str(red_val))


def hi_fun3():
    video_path = str(a.get())

    if os.path.isfile(video_path):
        clip = VideoFileClip(video_path)
        clip = clip.subclip(int(b.get()), int(c.get()))
        i = 0
        new_path = d.get()+str(i)+'.mp4'
        while os.path.isfile(new_path):
            i += 1
        if sel.get() == 0:
            clip.write_videofile(d.get()+str(i)+'.mp4')
        elif sel.get() == 1:
            clip.write_gif(d.get()+str(i)+'.gif')
        else:
            clip.audio.write_audiofile(d.get()+str(i)+'.mp3')
    else:
        exit()


win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")
sel = IntVar()
sel.set(1)
display1 = Label(win, text='輸入檔案名稱', fg='black', bg="#FFFFFF")
display1.grid(row=0, column=0)
a = Entry(win)
a.grid(row=0, column=2)
display2 = Label(win, text='開始擷取時間', fg='black', bg="#FFFFFF")
display2.grid(row=1, column=0)
b = Entry(win)
b.grid(row=1, column=2)
display3 = Label(win, text='結束擷取時間', fg='black', bg="#FFFFFF")
display3.grid(row=2, column=0)
c = Entry(win)
c.grid(row=2, column=2)
display4 = Label(win, text='輸出檔案名稱', fg='black', bg="#FFFFFF")
display4.grid(row=7, column=0)
d = Entry(win)
d.grid(row=7, column=2)
rad1 = Radiobutton(win, text='mp4', var=sel, command=get_cut, value=0)
rad1.grid(row=5, column=0)
rad2 = Radiobutton(win, text='gif', var=sel, command=get_cut, value=1)
rad2.grid(row=5, column=1)
rad3 = Radiobutton(win, text='mp3', var=sel, command=get_cut, value=2)
rad3.grid(row=5, column=2)
status = Label(win, font=('Arial', 12))
status.grid(row=6, columnspan=3, sticky="we")
btn = Button(win, text='擷取', command=hi_fun3)
btn.grid(row=8, columnspan=1)
win.mainloop()
