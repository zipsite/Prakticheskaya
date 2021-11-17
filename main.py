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
filename.pack(side=LEFT)
openbtn = Button(root, text = "Открыть", command=openfile)
openbtn.pack(side=LEFT)
savebtn = Button(root, text = "Сохранить", command=savefile)
savebtn.pack(side=LEFT)
textpad = Text(root)
textpad.pack(side=BOTTOM)




root.mainloop()
