from tkinter import *

def editSize(event):
    pole['width'] = vvod1.get(1.0, END)
    pole['height'] = vvod2.get(1.0, END)

def focIn(event):
    pole['bg'] = 'white'
def focOut(event):
    pole['bg'] = 'lightgrey'
    
root = Tk()
root.title("WTF")

top = Frame(root)
top.pack(fill=X, padx=3, pady=3)

vvod1 = Text(top, width = 3, height = 1)
vvod1.pack(side=LEFT, padx=3, pady=3)

vvod2 = Text(top, width = 3, height = 1)
vvod2.pack(side=LEFT, padx=3, pady=3)

edit = Button(top, text = "Изменить")
edit.bind('<Button-1>', editSize)
edit.pack(side=LEFT, padx=3, pady=3)

textpad = Frame(root)
textpad.pack()
pole = Text(textpad, width = 50, height = 20, bg = 'lightgrey')
pole.bind('<FocusIn>', focIn)
pole.bind('<FocusOut>', focOut)
pole.pack()

root.bind('<Return>', editSize)

root.mainloop()