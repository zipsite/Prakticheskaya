from tkinter import *

def righttran():
    select = list(lbox1.curselection())
    select.reverse()
    for i in select:
        lbox2.insert(END, lbox1.get(i))
        lbox1.delete(i)

def lefttran():
    select = list(lbox2.curselection())
    select.reverse()
    for i in select:
        lbox1.insert(END, lbox2.get(i))
        lbox2.delete(i)

root = Tk()

lbox1 = Listbox(selectmode=EXTENDED)
lbox1.pack(side=LEFT)

for i in ('apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple', 'tomato', 'milk'):
    lbox1.insert(END, i)


###
btnfr = Frame()
btnfr.pack(side=LEFT, padx=10)

rightbtn = Button(btnfr, text=">>>", command=righttran)
rightbtn.pack(fill=X)

leftbtn = Button(btnfr, text="<<<", command=lefttran)
leftbtn.pack(fill=X)

###
lbox2 = Listbox(selectmode=EXTENDED)
lbox2.pack(side=LEFT)

root.mainloop()


