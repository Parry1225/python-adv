
from tkinter import *


def hi_fun():
    print("you dide")
    display.config(text='GGG', fg='#FFFF30', bg="#5743AB")


def hi_fun2():
    print("you dide")
    display.config(text="", fg='#FFFFFF', bg="#FFFFFF")


win = Tk()
win.title('minecraft')
btn = Button(win, text="按了會GG", command=hi_fun)
btn.pack()
btn1 = Button(win, text="按了會???", command=hi_fun2)
btn1.pack()
display = Label(win, text="", fg='#FFFFFF', bg="#FFFFFF")
display.pack()
win.mainloop()
