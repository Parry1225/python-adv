
from tkinter import *


def hi_fun():
    print("you dide")
    display.config(text="", fg='#FFFFFF', bg="#FFFFFF")


win = Tk()
win.title('minecraft')
btn = Button(win, text="按了會GG", command=hi_fun)
btn.pack()
display = Label(win, text='GGG', fg='#FFFF30', bg="#5743AB")
display.pack()
win.mainloop()
