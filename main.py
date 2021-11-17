from tkinter import *

def clic():
    if rlink.get() == 0:
        info['text'] = "Реальный абобус"
    elif rlink.get() == 1:
        info['text'] = "Просто Петя"
    elif rlink.get() == 2:
        info['text'] = "Реальная беброчка"

root = Tk()
root.title("aboba")

rlink = IntVar()
rlink.set(0)

r1 = Radiobutton(text='Вася', variable=rlink, value=0, indicatoron=0, width=10, height=3, command=clic)
r1.grid(row=1,column=1)
r2 = Radiobutton(text='Петя', variable=rlink, value=1, indicatoron=0, width=10, height=3, command=clic)
r2.grid(row=2,column=1)
r3 = Radiobutton(text='Маша', variable=rlink, value=2, indicatoron=0, width=10, height=3, command=clic)
r3.grid(row=3,column=1)
info = Label(width=30, height=3)
info.grid(row=1,column=2)

root.mainloop()