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
    base_url = "https://data.epa.gov.tw/api/v1/"
    api_num = "aqx_p_432?"
    offset = "0"
    limit = "50"
    api_key = "9be7b239-557b-4c10-9775-78cadfc555e9"
    send_url = base_url
    send_url += api_num
    send_url += "offset=" + offset
    send_url += "&limit=" + limit
    send_url += "&api_key=" + api_key
    response = requests.get(send_url)
    info = response.json()
    SITYNAMMMMMMMMMM = []
    AQIII = []
    PM2_5555555 = []
    print(send_url)
    if "fields" in info.keys():
        UGBP = ''
        RT = ''
        for i in range(int(limit)):
            data = info["records"][i]["County"]
            if data == city.get():
                print("City="+info["records"][i]["County"])
                print("SiteName="+info["records"][i]["SiteName"])
                print("AQI="+info["records"][i]["AQI"])
                print("PM2.5="+info["records"][i]["PM2.5"])
                print("Status="+info["records"][i]["Status"]+"\n")
                AQIII.append(int(info["records"][i]["AQI"]))
                SITYNAMMMMMMMMMM.append(info["records"][i]["SiteName"])
                PM2_5555555.append(int(info["records"][i]["PM2.5"]))
                if info["records"][i]["Status"] == '良好':
                    RT = info["records"][i]["Status"]
                    UGBP += info["records"][i]["SiteName"]+"   AQI=" + \
                        info["records"][i]["AQI"]+"  PM2.5=" + \
                        info["records"][i]["PM2.5"]+"Status:" + \
                        RT + '\n'
    display2.config(text=UGBP)
    plt.plot(SITYNAMMMMMMMMMM, AQIII, "y-^", label="AQI")
    plt.plot(SITYNAMMMMMMMMMM, PM2_5555555, "y-^", label="PM2.5")
    plt.legend(loc="upper left")
    plt.show()


display2 = Label(win, text='', fg='black', bg="#FFFFFF")
display2.pack()
btn = Button(win, text='獲取城市空氣品質', command=hi_fun3)
btn.pack()
win.mainloop()
