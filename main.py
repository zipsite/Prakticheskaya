from tkinter import *
from random import *

def fart(event):
    xc = randint(0, 1000)
    yc = randint(0, 1000)

    rsize = str(xc+100)+"x"+str(yc+100)

    root.geometry(rsize)
    popbtn.place(x=xc, y=yc, width=50, height=50)

root = Tk()
root.title("Precol Randomniy")

img = PhotoImage(file='smile.png')

popbtn = Label(root, image=img)
popbtn.place(x=75, y=75, width=50, height=50)

root.bind("<Button-1>", fart)

root.mainloop()