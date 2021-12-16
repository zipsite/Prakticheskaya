from tkinter import *

# Изменяет размер окна
def editSize(event):
    pole['width'] = int(vvod1.get(1.0, END))
    pole['height'] = int(vvod2.get(1.0, END))

# Меняет текстовое поле на белое при фокусе на него
def focIn(event):
    pole['bg'] = 'white'

# Меняет текстовое поле на белое при потери фокуса
def focOut(event):
    pole['bg'] = 'lightgrey'

# Создание главного окна
root = Tk()
root.title("Resize")

# Фрейм для верхних кнопок
top = Frame(root)
top.pack(fill=X, padx=3, pady=3)

# Поля ввода
vvod1 = Text(top, width = 3, height = 1)
vvod1.pack(side=LEFT, padx=3, pady=3)
vvod2 = Text(top, width = 3, height = 1)
vvod2.pack(side=LEFT, padx=3, pady=3)

# Кнопка (зачем НАСТОЛЬКО подробно?)
edit = Button(top, text = "Изменить")
edit.bind('<Button-1>', editSize)
edit.pack(side=LEFT, padx=3, pady=3)

# Текстовое поле и реакция на фокус/потерю фокуса
pole = Text(root, width = 50, height = 20, bg = 'lightgrey')
pole.bind('<FocusIn>', focIn)
pole.bind('<FocusOut>', focOut)
pole.pack()

# Обработка нажатия клавиши Enter
root.bind('<Return>', editSize)

root.mainloop()