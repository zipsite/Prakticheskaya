from tkinter import *

class ColBlock:
    def __init__(self, master, code, color):
        self.b = Button(master, activebackground=code ,bg=code, width=3, command=self.shcolor)
        self.b.pack(side = LEFT, padx=1, pady=1)
        self.code = code
        self.color = color
    def shcolor(self):
        vid["text"] = self.color
        pole.delete(0, END)
        pole.insert(0, self.code)

root = Tk()
#root.geometry("150x225+100+100")
#root.resizable(width=False, height=False)

vid = Label(root, width=20)
vid.pack(padx=1, pady=3)
pole = Entry(root, width=20, justify='center')
pole.pack(padx=1, pady=3)


red = ColBlock(root, '#ff0000', "красный")
orange = ColBlock(root, '#ff7d00', "оранжевый")
yelloy = ColBlock(root, '#ffff00', "жёлтый")
green = ColBlock(root, '#00ff00', "зелёный")
blue = ColBlock(root, '#007dff', "голубой")
dblue = ColBlock(root, '#0000ff', "синий")
violet = ColBlock(root, '#7d00ff', "фиолетовый")

root.mainloop()
