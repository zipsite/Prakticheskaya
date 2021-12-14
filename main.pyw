from tkinter import *

def add():
    def draw():
        hx1 = int(x1.get(1.0, 'end-1c'))
        hx2 = int(x2.get(1.0, 'end-1c'))
        hy1 = int(y1.get(1.0, 'end-1c'))
        hy2 = int(y2.get(1.0, 'end-1c'))

        if radata.get() == 0:
            rec = holst.create_rectangle(hx1, hy1, hx2, hy2, fill='white', outline='black')
        elif radata.get() == 1:
            ova = holst.create_oval(hx1, hy1, hx2, hy2, fill='white', outline='black')

    winSadd = Toplevel()
    winSadd.geometry('200x200')
    winSadd.title('Фигура')
    
    cord = Frame(winSadd)
    cord.pack()

    Label(cord, text='x1').grid(row=1, column=1)
    x1 = Text(cord, width = '5', height = '1', bg = 'white')
    x1.grid(row=1, column=2)

    Label(cord, text='y1').grid(row=1, column=3)
    y1 = Text(cord, width = '5', height = '1', bg = 'white')
    y1.grid(row=1, column=4)

    Label(cord, text='x2').grid(row=2, column=1)
    x2 = Text(cord, width = '5', height = '1', bg = 'white')
    x2.grid(row=2, column=2)

    Label(cord, text='y2').grid(row=2, column=3)
    y2 = Text(cord, width = '5', height = '1', bg = 'white')
    y2.grid(row=2, column=4)

    radata = IntVar()
    radata.set(0)
    rect = Radiobutton(winSadd, text = "Прямоугольник", variable = radata, value = 0, width = 15, bg = 'white')
    rect.pack()
    oval = Radiobutton(winSadd, text = "Овал", variable = radata, value = 1, width = 15, bg = 'white')
    oval.pack()

    entbtn = Button(winSadd, text="Применить", command=draw)
    entbtn.pack()

root = Tk()
root.title("paint?")
root.geometry('300x350')
root.resizable(False, False)

holst = Canvas(root, width=300, height=300, bg='white')
holst.pack()

add = Button(root, text="Добавить", command=add)
add.pack()

root.mainloop()