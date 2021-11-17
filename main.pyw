from tkinter import *

class ColBlock:
    def __init__(self, master, code, color):
        self.b = Button(master, text=color, activebackground=code ,bg=code, width=20, command=self.shcolor)
        self.b.pack()
        self.code = code
        self.color = color
    def shcolor(self):
        vid["text"] = self.color
        pole.delete(0, END)
        pole.insert(0, self.code)

root = Tk()
root.geometry("150x225+100+100")
root.resizable(width=False, height=False)

vid = Label(root, width=20)
vid.pack()
pole = Entry(root, width=20, justify='center')
pole.pack()


red = ColBlock(root, '#ff0000', "красный")
orange = ColBlock(root, '#ff7d00', "оранжевый")
yelloy = ColBlock(root, '#ffff00', "жёлтый")
green = ColBlock(root, '#00ff00', "зелёный")
blue = ColBlock(root, '#007dff', "голубой")
dblue = ColBlock(root, '#0000ff', "синий")
violet = ColBlock(root, '#7d00ff', "фиолетовый")

root.mainloop()
