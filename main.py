from tkinter import *

# Перенос элемента в правый список
def righttran():
    select = list(lbox1.curselection())
    select.reverse()
    for i in select:
        lbox2.insert(END, lbox1.get(i))
        lbox1.delete(i)

# Перенос элемента в левый список
def lefttran():
    select = list(lbox2.curselection())
    select.reverse()
    for i in select:
        lbox1.insert(END, lbox2.get(i))
        lbox2.delete(i)

root = Tk()

# Первый список
lbox1 = Listbox(selectmode=EXTENDED)
lbox1.pack(side=LEFT)

# Добавление в список элементов
for i in ('apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple', 'tomato', 'milk'):
    lbox1.insert(END, i)

# Фрейм с переносящими кнопками
btnfr = Frame()
btnfr.pack(side=LEFT, padx=10)

rightbtn = Button(btnfr, text=">>>", command=righttran)
rightbtn.pack(fill=X)

leftbtn = Button(btnfr, text="<<<", command=lefttran)
leftbtn.pack(fill=X)

# Второй список
lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=LEFT)

root.mainloop()


