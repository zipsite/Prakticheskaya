from tkinter import *
# Задание переменных (почему бы и нет)
sign = 'null'       # хранит знак
var1 = 0            # первое число
var2 = 0            # второе число
result = 0
debug_mem = 'null'  # значение для отладки


# функции кнопок
def btn_cliced_plus():
    global sign
    sign = "+"
def btn_cliced_minus():
    global sign
    sign = "-"
def btn_cliced_mnog():
    global sign
    sign = "*"
def btn_cliced_dell():
    global sign
    sign = "/"
def btn_cliced_clear():
    global sign, var1, var2
    sign = 'null'
    var1 = 0
    var2 = 0
def btn_cliced_result():
    global sign, var1, var2

    var1 = vvod1.get()
    var2 = vvod2.get()

    if sign == 'null':
        result = "введи знак"
    elif sign == "+":
        result = var1 + var2
    elif sign == "-":
        result = var1 - var2
    elif sign == "*":
        result = var1 * var2
    elif sign == "/":
        result = var1 / var2

    vvod3.insert(1, result)

# Свойства кнопок
root = Tk()
root.title("Калькулятор")

podpis1 = Label(root, text="Первое число")
podpis2 = Label(root, text="Второе число")
podpis3 = Label(root, text="Ответ")


vvod1 = Entry(root, width=20)
vvod2 = Entry(root, width=20)
vvod3 =Entry(root,)


plus = Button(root, command=btn_cliced_plus, text = "+")
minus = Button(root, command=btn_cliced_minus, text = "-")
mnog = Button(root, command=btn_cliced_mnog, text = "*")
dell = Button(root, command=btn_cliced_dell, text = "/")

clear = Button(root, command=btn_cliced_clear, text = "очистить")

result = Button(root, command=btn_cliced_result, text = "результат")

debug = Label(root,text = debug_mem)

# Вёрстка интерфейса
podpis1.grid(row = 1, column = 1, columnspan = 2)
vvod1.grid(row = 2, column = 1, columnspan = 2)

podpis2.grid(row = 1, column = 3, columnspan = 2)
vvod2.grid(row = 2, column = 3, columnspan = 2)

podpis3.grid(row = 3, column = 1, columnspan = 4)
vvod3.grid(row = 4, column = 1, columnspan = 4)

plus.grid(row = 5, column = 1)
minus.grid(row = 5, column = 2)
mnog.grid(row = 5, column = 3)
dell.grid(row = 5, column = 4)

clear.grid(row = 6, column = 1, columnspan = 2)
result.grid(row = 6, column = 3, columnspan = 2)

debug.grid(row = 7, column = 1, columnspan = 4)

root.mainloop()
