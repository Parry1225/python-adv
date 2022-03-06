import matplotlib.pyplot as plt
# listx = [1, 2, 3, 4, 5, 6]
# listy = [10, 20, 30, 40, 50, 60]
# plt.plot(listx, listy)
# plt.show()
import requests
import json
from tkinter import *
import datetime as dt
win = Tk()
win.title('minecraft')
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")


def hi_fun3():
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "lat=" + lat.get()
    send_url += "&lon=" + lon.get()
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    response = requests.get(send_url)
    info = json.loads(response.text)
    days = [display1.config, display2.config, display3.config,
            display4.config, display5.config, display6.config, display7.config]
    temps__ = []
    try:
        if info["lat"] != "":

            for i in range(7):
                temps = info["daily"][i]["temp"]["day"]
                days[i](text="Day%d Temp=%s C" % (i, temps))
                temps__.append(temps)
            plt.plot(range(1, 8), temps__)
            plt.show()
    except:
        print(" Request Fail ")


api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
exclude = "minutely,hourly"
lat = Entry(win)
lat.pack()
lon = Entry(win)
lon.pack()
display1 = Label(win, text='date1:', fg='black', bg="#FFFFFF")
display2 = Label(win, text='date2:', fg='black', bg="#FFFFFF")
display3 = Label(win, text='date3:', fg='black', bg="#FFFFFF")
display4 = Label(win, text='date4:', fg='black', bg="#FFFFFF")
display5 = Label(win, text='date5:', fg='black', bg="#FFFFFF")
display6 = Label(win, text='date6:', fg='black', bg="#FFFFFF")
display7 = Label(win, text='date7:', fg='black', bg="#FFFFFF")
display1.pack()
display2.pack()
display3.pack()
display4.pack()
display5.pack()
display6.pack()
display7.pack()
btn = Button(win, text='獲取未來7天天氣', command=hi_fun3)
btn.pack()
win.mainloop()
