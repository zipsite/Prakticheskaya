from tkinter import *
from tkinter import messagebox

# Задание переменных (почему бы и нет)
sign = 'null'           # хранит знак
var1 = int(0)           # первое число
var2 = int(0)           # второе число
result = int(0)         # хранит знак

# элементы интерфейса
name_window_error = "Ошебакак"
sign_error = "чел, ты Знак забыл..."
dell_minus_error = "Эта абоба не так работаит, читай матет=матику!"
empty_error = "А ты цыфры не забыл???"

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
    vvod1.delete(0, END)
    vvod2.delete(0, END)
    vvod3.delete(0, END)
def btn_cliced_result():
    global sign, var1, var2, empty_error,  sign_error, dell_minus_error, name_window_error

    # Очистка ответа
    vvod3.delete(0, END)

    # Проверка чтобы поля ввода не были пустыми и чтобы был поставлен знак
    if sign == 'null':
        messagebox.showinfo(name_window_error, sign_error)
    elif vvod1.get() and vvod2.get():
        var1 = int(vvod1.get())
        var2 = int(vvod2.get())
    else:
        messagebox.showinfo(name_window_error, empty_error)

    # Основная логика калькулятора
    if sign == "+":
        result = var1 + var2
    elif sign == "-":
        result = var1 - var2
    elif sign == "*":
        result = var1 * var2
    elif sign == "/":
        if var2 != 0:
            result = var1 / var2
        elif var2 == 0:
            messagebox.showinfo(name_window_error, dell_minus_error)

    # Вывод результата
    vvod3.insert(1, result)

    # Обнуление переменных и очистка полей
    sign = 'null'
    var1 = 0
    var2 = 0
    vvod1.delete(0, END)
    vvod2.delete(0, END)

# Свойства кнопок
root = Tk()
root.title("Калькулятор")

podpis1 = Label(root, text="Первое число")
podpis2 = Label(root, text="Второе число")
podpis3 = Label(root, text="Ответ")


vvod1 = Entry(root, width=20)
vvod2 = Entry(root, width=20)
vvod3 = Entry(root, width=40)


plus = Button(root, command=btn_cliced_plus, text = "+", width=10)
minus = Button(root, command=btn_cliced_minus, text = "-", width=10)
mnog = Button(root, command=btn_cliced_mnog, text = "*", width=10)
dell = Button(root, command=btn_cliced_dell, text = "/", width=10)

clear = Button(root, command=btn_cliced_clear, text = "очистить", width=20)

result = Button(root, command=btn_cliced_result, text = "результат", width=20)

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

root.mainloop()
