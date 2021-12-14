from tkinter import *

root = Tk()

c = Canvas(root, width= 200, height=200, bg='white')
c.pack()

c.create_oval(150,10, 180, 40, fill='yellow', outline="yellow")
c.create_polygon(60,100, 150,100, 150,180, 60,180, fill="lightblue", outline="lightblue")
c.create_polygon(100,60, 40,100, 170,100, fill="lightblue", outline="lightblue")

for i in range(0, 250, 5):
    c.create_arc(0+i, 500, 40+i, 150, width=2, start=100, extent=-50, style=ARC, outline="green")

root.mainloop()