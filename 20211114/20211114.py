from os import read
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
import pandas as pd
import datetime as dt


def rwe():
    df = pd.read_csv("20211114/20211112.csv")
    nunb = int(city2.get())
    Position = df.loc[:, "Position"]
    Total = df.loc[:, "Total"]
    remain = df.loc[:, "Remain"]
    display3.config(text='顯示圖表')
    A = plt.bar(Position[:nunb], Total[:nunb], label="???")
    B = plt.bar(Position[:nunb], remain[:nunb], label="....")
    uuh(A)
    uuh(B)
    plt.legend(loc="upper left")
    plt.show()


def uuh(dat):
    for item in dat:
        height = item.get_height()
        plt.text(item.get_x()+item.get_width()/2,
                 height, str(height), ha="center")


def hi_fun3():
    df = pd.DataFrame(None, columns=["Position", "Total", "Remain"])
    lollo = 0
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"
    response = requests.get(base_url)
    info = response.json()
    YT = ""
    l = []
    X = []
    M = []
    for i in info['retVal']:
        if info['retVal'][i]['sarea'] == city.get():
            YT += '地區:'+info['retVal'][i]['sarea'] + \
                '地點:' + info['retVal'][i]['sna'] + \
                '總共出量:'+info['retVal'][i]['tot'] + \
                '剩餘車輛:'+info['retVal'][i]['sbi']+'\n'
            position = (info['retVal'][i]['sna'])
            l.append(position)
            total_bike = (int(info['retVal'][i]['tot']))
            X.append(total_bike)
            remain_bike = (int(info['retVal'][i]['sbi']))
            M.append(remain_bike)
            df.loc[i] = [position, total_bike, remain_bike]
            display2.config(text=YT)
            lollo += 1

    df.to_csv("20211114/20211112.csv")


def hi_fun2():
    display2.config(text='')


win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")
display1 = Label(win, text='請書入城市', fg='black', bg="#FFFFFF")
display1.pack()
city = Entry(win)
city.pack()
city2 = Entry(win)
city2.pack()
display2 = Label(win, text='', fg='black', bg="#FFFFFF")
display2.pack()
display3 = Label(win, text='', fg='black', bg="#FFFFFF")
display3.pack()
btn = Button(win, text='獲取YouBike資訊', command=hi_fun3)
btn.pack()
btn2 = Button(win, text='清除YouBike資訊', command=hi_fun2)
btn2.pack()
btn3 = Button(win, text='顯示表格', command=rwe)
btn3.pack()
win.mainloop()
