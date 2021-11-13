from tkinter import *

root = Tk()

e = Entry(width=20)
b = Button(text="Преобразовать")
a = Button(root, text = "+")
d = Button(root, text = "-")
c = Button(root, text = "*")
h = Button(root, text = "/")  
l = Label(bg='black', fg='white', width=20)

def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)

b.bind('<Button-1>', strToSortlist)

a.pack()
d.pack()
e.pack()
b.pack()
l.pack()
root.mainloop()
