from tkinter import *

# Добавление в список элементов
def addList(event):
    lbox.insert(END, entry.get())
    entry.delete(0, END)

# Копирование элемента из списка в поле ввода
def copyInEntry(event):
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        entry.insert(0, lbox.get(i))
        lbox.delete(i)

root = Tk()
root.title("Notes")

entry = Entry(root)
entry.bind('<Return>', addList)
entry.pack()

lbox = Listbox(root)
lbox.bind('<Double-Button-1>', copyInEntry)
lbox.pack()

root.mainloop()


