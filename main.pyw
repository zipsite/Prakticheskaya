from tkinter import *

root = Tk()

c = Canvas(root, width= 200, height=200, bg='white')
c.pack()

c.create_oval(150,10, 180, 40, fill='yellow', outline="yellow")

c.create_polygon(60,100, 150,100, 150,180, 60,180, fill="blue", outline="blue")
c.create_polygon(100,60, 40,100, 170,100, fill="blue", outline="blue")
root.mainloop()