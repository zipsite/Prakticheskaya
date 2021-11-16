from tkinter import *
from tkinter.ttk import *


class Sign:
    def __init__(self, master, t, c):
        self.s = Button(master, command=self.calc, text=t).grid(row=2, column=c, sticky=W + E + N + S)
        self.t = t

    def calc(self):
        global vvod1, vvod2
        sign = self.t
        result['text'] = "Ответ: "

        if sign == 'null':
            result['text'] = "error"
        elif vvod1.get() and vvod2.get():
            one = int(vvod1.get())
            two = int(vvod2.get())
            if sign == '+':
                result['text'] += str(one + two)
            elif sign == '-':
                result['text'] += str(one - two)
            elif sign == '*':
                result['text'] += str(one * two)
            elif sign == '/':
                if two != 0:
                    result['text'] += str(one / two)
                elif two == 0:
                    result['text'] = "error"
        else:
            result['text'] = "error"

        vvod1.delete(0, END)
        vvod2.delete(0, END)


root = Tk()
root.title("Calculator")

vvod1 = Entry(root)
vvod1.grid(row=1, columnspan=2, column=1, sticky=W + E + N + S)
vvod2 = Entry(root)
vvod2.grid(row=1, columnspan=2, column=3, sticky=W + E + N + S)

plus = Sign(root, "+", c=1)
minus = Sign(root, "-", c=2)
umn = Sign(root, "*", c=3)
dell = Sign(root, "/", c=4)

result = Label(root, width=20, text="Ответ: ")
result.grid(row=3, columnspan=4, column=1, sticky=W + E + N + S)
root.mainloop()
