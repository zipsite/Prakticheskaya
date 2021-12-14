from tkinter import *

# Функция окна добавления
def add():

    # Функция рисования фигур
    def draw():
        hx1 = int(x1.get(1.0, 'end-1c'))
        hx2 = int(x2.get(1.0, 'end-1c'))
        hy1 = int(y1.get(1.0, 'end-1c'))
        hy2 = int(y2.get(1.0, 'end-1c'))

        if radata.get() == 0:
            holst.create_rectangle(hx1, hy1, hx2, hy2, fill='white', outline='black')
        elif radata.get() == 1:
            holst.create_oval(hx1, hy1, hx2, hy2, fill='white', outline='black')

        #Закрытия окна добавления после выполнения рисования
        winSadd.destroy()

    # Добавления нового окна
    winSadd = Toplevel()
    winSadd.title('Фигура')
    
    cord = Frame(winSadd)
    cord.pack()

    # Поля ввода координат и надписи
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

    # Значение радиокнопки
    radata = IntVar()
    radata.set(0)

    # Радиокнопки
    rect = Radiobutton(winSadd, variable = radata, value = 0, width = 15, text = "Прямоугольник")
    rect.pack()
    oval = Radiobutton(winSadd, variable = radata, value = 1, width = 15, text = "Овал")
    oval.pack()

    # Кнопка 'Применить'
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