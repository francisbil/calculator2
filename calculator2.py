from tkinter import *

root = Tk()
root.title("Calculator")

frame = Frame(root)
frame.pack(fill='both', expand=True)

for i in range(0,5):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

e = Entry(frame, width=42, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, pady=10, sticky='nsew')

def button(symbol):
    e.insert(END, str(symbol))

def clear():
    e.delete(0, END)

def equals():
    answer = eval(e.get())
    e.delete(0, END)
    e.insert(0, answer)

def delete():
    text = e.get()
    e.delete(0, END)
    e.insert(0, text[:-1])

button_1 = Button(frame, text='1', padx=30, pady=20, command=lambda: button(1))
button_2 = Button(frame, text='2', padx=30, pady=20, command=lambda: button(2))
button_3 = Button(frame, text='3', padx=30, pady=20, command=lambda: button(3))
button_4 = Button(frame, text='4', padx=30, pady=20, command=lambda: button(4))
button_5 = Button(frame, text='5', padx=30, pady=20, command=lambda: button(5))
button_6 = Button(frame, text='6', padx=30, pady=20, command=lambda: button(6))
button_7 = Button(frame, text='7', padx=30, pady=20, command=lambda: button(7))
button_8 = Button(frame, text='8', padx=30, pady=20, command=lambda: button(8))
button_9 = Button(frame, text='9', padx=30, pady=20, command=lambda: button(9))
button_0 = Button(frame, text='0', padx=30, pady=20, command=lambda: button(0))

button_equals = Button(frame, text='=', padx=29, pady=20, command=equals)
button_clear = Button(frame, text='CLEAR', padx=12, pady=20, command=clear)
button_delete = Button(frame, text='DEL', padx=23, pady=20, command=delete)

button_plus = Button(frame, text='+', padx=30, pady=20, command=lambda: button('+'))
button_minus = Button(frame, text='-', padx=30, pady=20, command=lambda: button('-'))
button_mult = Button(frame, text='*', padx=32, pady=20, command=lambda: button('*'))
button_div = Button(frame, text='/', padx=30, pady=20, command=lambda: button('/'))
button_leftpar = Button(frame, text='(', padx=33, pady=20, command=lambda: button('('))
button_rightpar = Button(frame, text=')', padx=30, pady=20, command=lambda: button(')'))
button_dot = Button(frame, text='.', padx=31, pady=20, command=lambda: button('.'))


button_1.grid(row=3, column=0, sticky='nsew')
button_2.grid(row=3, column=1, sticky='nsew')
button_3.grid(row=3, column=2, sticky='nsew')
button_4.grid(row=2, column=0, sticky='nsew')
button_5.grid(row=2, column=1, sticky='nsew')
button_6.grid(row=2, column=2, sticky='nsew')
button_7.grid(row=1, column=0, sticky='nsew')
button_8.grid(row=1, column=1, sticky='nsew')
button_9.grid(row=1, column=2, sticky='nsew')
button_0.grid(row=4, column=0, sticky='nsew')

button_equals.grid(row=4, column=2, sticky='nsew')
button_clear.grid(row=1, column=4, sticky='nsew')
button_delete.grid(row=1, column=3, sticky='nsew')

button_plus.grid(row=2, column=3, sticky='nsew')
button_minus.grid(row=2, column=4, sticky='nsew')
button_mult.grid(row=3, column=3, sticky='nsew')
button_div.grid(row=3, column=4, sticky='nsew')
button_leftpar.grid(row=4, column=3, sticky='nsew')
button_rightpar.grid(row=4, column=4, sticky='nsew')
button_dot.grid(row=4, column=1, sticky='nsew')

root.mainloop()
