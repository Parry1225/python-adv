import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
import datetime as dt
win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")
display1 = Label(win, text='請書入城市', fg='black', bg="#FFFFFF")
display1.pack()
city = Entry(win)
city.pack()


def hi_fun3():
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
            l.append(info['retVal'][i]['sna'])
            X.append(int(info['retVal'][i]['tot']))
            M.append(int(info['retVal'][i]['sbi']))
            display2.config(text=YT)
    plt.plot(l, X, "y-^", label="???")
    plt.plot(l, M, "y-^", label="....")
    plt.legend(loc="upper left")
    plt.show()


def hi_fun2():
    display2.config(text='')


display2 = Label(win, text='', fg='black', bg="#FFFFFF")
display2.pack()
btn = Button(win, text='獲取YouBike資訊', command=hi_fun3)
btn.pack()
btn2 = Button(win, text='清除YouBike資訊', command=hi_fun2)
btn2.pack()
win.mainloop()
