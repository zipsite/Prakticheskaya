from tkinter import *

sign = 'null'

chislo = str(' ')

def summ():
    debug.configure(text="+")

def minuss():
    global sign
    sign = "-"

    debug.configure(text="-")
def mnoge():
    global sign
    sign = "*"

    debug.configure(text="*")
def dell():
    global sign
    sign = "/"

    debug.configure(text="/")
def clear():
    print (u"Клик!")

    debug.configure(text="C")

def result():
    chislo = str (vvod1.get())
    debug.configure(text=chislo)
    

    




root = Tk()
root.title("Калькулятор")

podpis1 = Label(root, text="Первое число")
podpis2 = Label(root, text="Второе число")
podpis3 = Label(root, text="Ответ")


vvod1 = Entry(root, width=20)
vvod2 = Entry(root, width=20)
vvod3 =Entry(root,)


plus = Button(root, command=summ, text = "+")
minus = Button(root, command=minuss, text = "-")
umnog = Button(root, command=mnoge, text = "*")
deleniye = Button(root, command=dell, text = "/") 

clear = Button(root, command=clear, text = "очистить")

result = Button(root, command=result, text = "результат")

debug = Label(root,text = "bbb")












podpis1.grid(row = 1, column = 1, columnspan = 2)
vvod1.grid(row = 2, column = 1, columnspan = 2)

podpis2.grid(row = 1, column = 3, columnspan = 2)
vvod2.grid(row = 2, column = 3, columnspan = 2)

podpis3.grid(row = 3, column = 1, columnspan = 4)
vvod3.grid(row = 4, column = 1, columnspan = 4)

plus.grid(row = 5, column = 1)
minus.grid(row = 5, column = 2)
umnog.grid(row = 5, column = 3)
deleniye.grid(row = 5, column = 4)

clear.grid(row = 6, column = 1, columnspan = 2)
result.grid(row = 6, column = 3, columnspan = 2)

debug.grid(row = 7, column = 1, columnspan = 4)





root.mainloop()
