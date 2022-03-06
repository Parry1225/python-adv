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

# video_path = '20211128/LLLOJj.mp4'
# if os.path.isfile(video_path):
#     clip = VideoFileClip(video_path)
# else:
#     exit()
# base_path = '20211226'
# new_file = "阿共的英摩"
# new_path = base_path + new_file + '.mp3'
# clip.audio.write_audiofile(new_path)
# print("Convert mp3 Success")


def hi_fun3():
    video_path = '20211128/LLLOJj.mp4'

    if os.path.isfile('20211128/lol.mp4'):
        clip = VideoFileClip('20211128/LLLOJj.mp4')
        # clip.preview()
        if state.get() == True:
            clip = clip.subclip(int(b.get()), int(c.get()))
        i = 0
        video_path = '20211128/'
        new_path = video_path+str(i)+'.mp4'
        while os.path.isfile(new_path):
            i += 1
            new_path = video_path+a.get()+str(i)+'.mp4'
        if state.get() == True:
            base_path = '20211226'
            new_file = a.get()
            new_path = base_path + new_file + '.mp3'
            clip.audio.write_audiofile(new_path)
        else:
            clip.write_videofile(new_path)
        print("Convert mp3 Success")
    else:
        exit()


def show_info():
    chk = state.get()
    if (chk):

        display2.grid(row=1, column=0)

        b.grid(row=1, column=1)

        display3.grid(row=2, column=0)

        c.grid(row=2, column=1)
    else:
        display2.grid_forget()
        b.grid_forget()
        display3.grid_forget()
        c.grid_forget()


win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")

box_labal = Label(win, text='labal info')

state = BooleanVar()
state.set(False)
box = Checkbutton(win, text='show mp3', var=state, command=show_info)
box.grid(sticky='w')
display1 = Label(win, text='輸入影片名稱', fg='black', bg="#FFFFFF")
display1.grid(row=0, column=1)
a = Entry(win)
a.grid(row=0, column=2)
display2 = Label(win, text='開始時間', fg='black', bg="#FFFFFF")
display3 = Label(win, text='結束時間', fg='black', bg="#FFFFFF")
b = Entry(win)
c = Entry(win)
btn = Button(win, text='開始切割', command=hi_fun3)
btn.grid(row=3, columnspan=2)
win.geometry('300x150')
win.mainloop()
