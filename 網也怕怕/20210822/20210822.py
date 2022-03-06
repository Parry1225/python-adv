from tkinter import *


def movecan(event):
    key = event.keysym
    print(key)
    if key == "d":
        can.move(cir, 10, 0)
    elif key == "a":
        can.move(cir, -10, 0)
    elif key == "s":
        can.move(cir, 0, 10)
    elif key == "w":
        can.move(cir, 0, -10)


win = Tk()
win.title('minecraft')
can = Canvas(win, width=800, height=600)
can.pack()
omg = PhotoImage(file="20210822/crocodile2.gif")
my_omg = can.create_image(300, 300, image=omg)
win.iconbitmap("20210822/minecraft-pocket-edition_ccb06 (1).ico")
cir = can.create_oval(100, 100, 300, 300, fill="#FFFF67")
rect = can.create_rectangle(150, 150, 250, 250, fill="#29233B")
msg = can.create_text(150, 150, text="?????",
                      fill="#FFFF67", font=('Arial', 30))
can.bind_all('<Key>', movecan)
win.mainloop()
