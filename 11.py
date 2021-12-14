from tkinter import *

def add():
	def draw():
		Cx1 = int(x1.get(1.0, 'end-1c'))
		Cx2 = int(x2.get(1.0, 'end-1c'))
		Cy1 = int(y1.get(1.0, 'end-1c'))
		Cy2 = int(y2.get(1.0, 'end-1c'))

		if r_var.get() == 0:
			rec = c.create_rectangle(Cx1, Cy1, Cx2, Cy2, fill = 'white')
		elif r_var.get() == 1:
			ova = c.create_oval(Cx1, Cy1, Cx2, Cy2, fill = 'white')

	a = Toplevel()
	a.title('Фигура')
	a.geometry('200x250+500+150')
	a['bg'] = 'white'
	a.resizable(False, False)

	f1 = Frame(a)
	f1.pack()

	f2 = Frame(a)
	f2.pack()

	f3 = Frame(a)
	f3.pack()
	
	f4 = Frame(a)
	f4.pack()

	x1 = Text(f1, width = '5', height = '1', bg = 'white')
	x1.pack(side = LEFT)
	y1 = Text(f1, width = '5', height = '1', bg = 'white')
	y1.pack(side = LEFT)

	x2 = Text(f2, width = '5', height = '1', bg = 'white')
	x2.pack(side = LEFT)
	y2 = Text(f2, width = '5', height = '1', bg = 'white')
	y2.pack(side = LEFT)

	r_var = IntVar()
	r_var.set(0)
	
	rect = Radiobutton(f3, text = "Прямоугольник", variable = r_var, value = 0, width = 15, bg = 'white')
	rect.pack()
	
	oval = Radiobutton(f4, text = "Овал", variable = r_var, value = 1, width = 15, bg = 'white')
	oval.pack()

	b = Button(a, text = 'Нарисовать', command = draw)
	b.pack()

root = Tk()
root.geometry('400x350+100+150')
root.resizable(False, False)
root.title("paint")
c = Canvas(root, width = 400, height = 320, bg = 'white')
c.pack()
Button(text="Добавить фигуру", width=20, command=add).pack()
root.mainloop()