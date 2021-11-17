from tkinter import *

def openfile():
    global filename, textpad

    textpad.delete(1.0, END)

    name = str(filename.get())

    file = open(name, "r")

    bufer = file.read()

    textpad.insert(1.0, bufer)

    file.close()

def savefile():
    global filename, textpad

    name = str(filename.get())

    file = open(name, "w")

    bufer = textpad.get(1.0, END)

    file.write(bufer)
    file.close()

root = Tk()
root.title("aboba")

filename = Entry(root)
filename.grid(row=1,column=1)
openbtn = Button(root, text = "Открыть", command=openfile)
openbtn.grid(row=1, column=2)
savebtn = Button(root, text = "Сохранить", command=savefile)
savebtn.grid(row=1, column=3)
textpad = Text(root)
textpad.grid(row=2, columnspan=3, column=1)

root.mainloop()
