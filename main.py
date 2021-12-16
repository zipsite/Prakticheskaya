from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

# Функции открытия и сохранения файла
def openfile():
    filename = askopenfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")))
    name = str(filename)
    file = open(name, "r", encoding='UTF-8')
    bufer = file.read()
    text.delete(1.0, END)
    text.insert(1.0, bufer)
    file.close()

def savefile():
    filename = asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")))
    name = str(filename)
    file = open(name, "w", encoding='UTF-8')
    bufer = text.get(1.0, END)
    file.write(bufer)
    file.close()

def clear():
    textpad.delete(1.0, END)

# Главное окно
root = Tk()
root.title("Блохнот")

# Фрейм для кнопок и поля ввода имени файла
topbtn = Frame(root)
topbtn.pack(fill=X, expand=True)

# Конфиги виджетов
openbtn = Button(topbtn, width = 15, text = "Открыть", command=openfile)
savebtn = Button(topbtn, width = 15, text = "Сохранить", command=savefile)
clearbtn = Button(topbtn, width = 15, text = "Очистить", command=clear)

# Расположение виджетов
openbtn.pack(side = LEFT, padx=1, pady=1)
savebtn.pack(side = LEFT, padx=1, pady=1)
clearbtn.pack(side = LEFT, padx=1, pady=1)

# Фрейм текстового поля
textpad = Frame(root)
textpad.pack()

# Конфиги текстового поля и скроллбаров
text = Text(textpad, width = 50, height = 20, wrap=NONE)
scroll = Scrollbar(textpad, command=text.yview)
scroll2 = Scrollbar(orient=HORIZONTAL, command=text.xview)

# Расположение текстового поля и скролл баров
text.pack(side=LEFT)
scroll.pack(side=LEFT, fill = Y)
scroll2.pack(side=BOTTOM, fill=X)

# Подключение скролл баров к текстовому полю
text.config(yscrollcommand=scroll.set)
text.config(xscrollcommand=scroll2.set)

root.mainloop()
