from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# Функции открытия и сохранения файла
def openfile():
    global textpad
    filename = askopenfilename()
    name = str(filename)
    file = open(name, "r", encoding='UTF-8')
    bufer = file.read()
    text.delete(1.0, END)
    text.insert(1.0, bufer)
    file.close()

def savefile():
    global text
    filename = asksaveasfilename()
    name = str(filename)
    file = open(name, "w", encoding='UTF-8')
    bufer = text.get(1.0, END)
    file.write(bufer)
    file.close()

def clear():
    text.delete(1.0, END)


def spawn(event):
    popmenu.post(event.x_root, event.y_root)

# Главное окно
root = Tk()
root.title("Блохнот")

mainmenu = Menu(root)
root.config(menu=mainmenu)

mainmenu.add_command(label="Открыть", command=openfile)
mainmenu.add_command(label="Сохранить", command=savefile)

popmenu = Menu(tearoff=0)
popmenu.add_command(label='Очистить', command=clear)

# Фрейм текстового поля
textpad = Frame(root)
textpad.pack()

# Конфиги текстового поля и скроллбаров
text = Text(textpad, width = 50, height = 20, wrap=NONE)
scroll = Scrollbar(textpad, command=text.yview)
scroll2 = Scrollbar(orient=HORIZONTAL, command=text.xview)


text.bind('<Button-3>', spawn)
# Расположение текстового поля и скролл баров
text.pack(side=LEFT)
scroll.pack(side=LEFT, fill = Y)
scroll2.pack(side=BOTTOM, fill=X)

# Подключение скролл баров к текстовому полю
text.config(yscrollcommand=scroll.set)
text.config(xscrollcommand=scroll2.set)

root.mainloop()
