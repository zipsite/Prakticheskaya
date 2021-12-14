from tkinter import *

def addList(event):
    lbox.insert(END, entry.get())
    entry.delete(0, END)

def copyInEntry(event):
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        entry.insert(0, lbox.get(i))

root = Tk()
root.title("Notes")

entry = Entry(root)
entry.bind('<Return>', addList)
entry.pack()

lbox = Listbox(root)
lbox.bind('<Double-Button-1>', copyInEntry)
lbox.pack()

root.mainloop()


