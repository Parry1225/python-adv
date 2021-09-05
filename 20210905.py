
from tkinter import *
import datetime as dt


def hi_fun():
    time = str(dt.date.today())
    display.config(text=time, fg='#FFFF30', bg="#5743AB")


def hi_fun2():
    time = str(dt.datetime.now())
    # if display['text'] == time:

    #     print("you dide")
    display.config(text=time, fg='#FFFF30', bg="#5743AB")
    # elif display['text'] == time:

    #     print("you dide")
    #     display.config(text=time, fg='#FF0000', bg="#FFFFFF")


def hi_fun3():
    a = float(int(input_date.get())*2.54)
    display.config(text=str(a), fg='white')


win = Tk()
win.title('minecraft')
input_date = Entry(win)
input_date.pack()
btn = Button(win, text='XXXXX', command=hi_fun)
btn.pack()
btn2 = Button(win, text='YYYYY', command=hi_fun2)
btn2.pack()
btn3 = Button(win, text='ZZZZZ', command=hi_fun3)
btn3.pack()
display = Label(win, text='GGGGGG', fg='#FFFF30', bg="#5743AB")
display.pack()

win.mainloop()
