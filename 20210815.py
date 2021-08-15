
from tkinter import *


def hi_fun():
    frog = True
    if display['text'] == "red":

        print("you dide")
        display.config(text="gread", fg='#FFFF30', bg="#5743AB")
    elif display['text'] == "gread":

        print("you dide")
        display.config(text="red", fg='#FF0000', bg="#FFFFFF")


win = Tk()
win.title('minecraft')
btn = Button(win, text="按了會GG", command=hi_fun)
btn.pack()
display = Label(win, text='red', fg='#FFFF30', bg="#5743AB")
display.pack()
win.mainloop()
