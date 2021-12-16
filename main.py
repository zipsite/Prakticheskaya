from tkinter import *

def click(event):
    holst.x = event.x + holst.radius
    holst.y = event.y + holst.radius
    holst.radius = 30
    anim()


def anim():
    x = holst.coords(holst.ball)[2] 
    y = holst.coords(holst.ball)[3]

    if holst.x == x and holst.y == y:
        return
    elif holst.x < x:
        holst.move(holst.ball,-1, 0)
    elif holst.x > x:
        holst.move(holst.ball, 1, 0)
    elif holst.y < y:
        holst.move(holst.ball, 0,-1)
    elif holst.y > y:
        holst.move(holst.ball, 0, 1)

    root.after(5, anim)

root = Tk()
root.title("circle")
root.geometry('300x300')
root.resizable(False, False)

holst = Canvas(width=300, height=300, bg='white')
holst.radius = 30

holst.ball = holst.create_oval(0, 150, holst.radius*2, 150+holst.radius*2, fill='lightblue', outline='lightblue')
holst.bind('<Button-1>', click)
holst.pack()

root.mainloop()