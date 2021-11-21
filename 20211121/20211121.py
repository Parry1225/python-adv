from os import read
import matplotlib.pyplot as plt
import requests
import json
from tkinter import *
import pandas as pd
import datetime as dt
import numpy as np


def uuh(dat):
    for item in dat:
        height = item.get_height()
        plt.text(item.get_x()+item.get_width()/2,
                 height, str(height), ha="center")


base_url = 'https://tw.global.nba.com/stats2/scores/daily.json?'
contry = 'TW'
date = '2021-11-1'
locale = 'zh_TW'
tz = '%2B8'
send_url = base_url
send_url += '?countryCode='+contry
send_url += '&gameData=' + date
send_url += "&locale" + locale
send_url += "&tz=" + tz
response = requests.get(send_url)
info = response.json()
winhome = 0
home___away = 0
homewin_list = []
awaywin_list = []
game_data = []


for i in info["payload"]["date"]["games"]:
    print('cust:{}'.format(i["boxscore"]["awayScore"]))
    print('home:{}'.format(i["boxscore"]["homeScore"]))
    if i["boxscore"]["homeScore"] >= i["boxscore"]["homeScore"]:
        print('主場勝')
        winhome += 1

    else:
        print('客場勝')
        home___away += 1

homewin_list.append(winhome)
awaywin_list.append(home___away)
game_data.append(date)
index = np.arange(len(game_data))
fig, ax = plt.subplots()
A = ax.bar(index, homewin_list, label="豬場勝", width=0.25)
B = ax.bar(index + 0.25, awaywin_list, label="客場勝", width=0.25)

ax.set_xticks(index)
ax.set_xticklabels(game_data)

df = pd.DataFrame(None, columns=["日期", "主場勝", "客場勝"])
df = df.append({'日期': date, '主場勝': winhome,
               '客場勝': home___away}, ignore_index=True)
uuh(A)
uuh(B)
df.to_csv("20211121/20211121.csv")


plt.legend(loc="upper left")
plt.show()
