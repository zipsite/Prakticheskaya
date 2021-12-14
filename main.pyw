from tkinter import *



def add():
    def draw():
        hx1 = int(x1.get(1.0, 'end-1c'))
        hx2 = int(x2.get(1.0, 'end-1c'))
        hy1 = int(y1.get(1.0, 'end-1c'))
        hy2 = int(y2.get(1.0, 'end-1c'))

        if r_var.get() == 0:
            holst.create_rectangle(hx1, hy1, hx2, hy2, outline='black')
        elif r_var.get() == 1:
            holst.create_oval(hx1, hy1, hx2, hy2, outline='black')
    winSadd = Toplevel()
    winSadd.geometry('200x200')
    winSadd.title('Фигура')
    winSadd.geometry('200x250+500+150')
    winSadd.resizable(False, False)
    
    entbtn = Button(win, text="Применить")
    entbtn.pack()

    winSadd.mainloop()

root = Tk()
root.title("paint?")
root.geometry('300x400')
root.resizable(False, False)

holst = Canvas(root, width=300, height=300)
holst.pack()

add = Button(root, text="Добавить", command=addwin)
add.pack()

root.mainloop()