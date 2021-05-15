import tkinter as tk
from calculator import *

# !inicializando a classe calculator
calculator = Calculator()

# !configurações com relação a janela
w = 500
h = 250

window = tk.Tk()
window.iconbitmap('icons/icon.ico')
window.title('Calculadora')

w_screen = window.winfo_screenwidth()
h_screen = window.winfo_screenheight()

position_x = (w_screen/2) - (w/2)
position_y = (h_screen/2) - (h/2)

window.geometry(f'{w}x{h}+{int(position_x)}+{int(position_y)}')
window.resizable(False, False)
window['bg'] = '#808080'

# !labels
label_screen = tk.Label(
    master=window,
    text='0',
    font='Arial 20',
    bd=4,
    relief='sunken',
    width=w,
    anchor='e'
)

label_screen.pack()

# !botões
btn_0 = tk.Button(
    master=window, 
    text='0', 
    command=lambda:calculator.button_click(btn_0.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=36,
    height=2
)

btn_1 = tk.Button(
    master=window, 
    text='1',
    command=lambda:calculator.button_click(btn_1.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_2 = tk.Button(
    master=window, 
    text='2',
    command=lambda:calculator.button_click(btn_2.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_3 = tk.Button(
    master=window, 
    text='3',
    command=lambda:calculator.button_click(btn_3.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_4 = tk.Button(
    master=window, 
    text='4',
    command=lambda:calculator.button_click(btn_4.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_5 = tk.Button(
    master=window, 
    text='5',
    command=lambda:calculator.button_click(btn_5.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_6 = tk.Button(
    master=window, 
    text='6',
    command=lambda:calculator.button_click(btn_6.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_7 = tk.Button(
    master=window, 
    text='7',
    command=lambda:calculator.button_click(btn_7.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_8 = tk.Button(
    master=window, 
    text='8',
    command=lambda:calculator.button_click(btn_8.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_9 = tk.Button(
    master=window, 
    text='9',
    command=lambda:calculator.button_click(btn_9.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=10,
    height=2
)

btn_equal = tk.Button(
    master=window, 
    text='=',
    command=lambda:calculator.button_click(btn_equal.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=29,
    height=2
)

btn_sum = tk.Button(
    master=window, 
    text='+',
    command=lambda:calculator.button_click(btn_sum.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=13,
    height=2
)

btn_dif = tk.Button(
    master=window, 
    text='-',
    command=lambda:calculator.button_click(btn_dif.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=13,
    height=2
)

btn_prod = tk.Button(
    master=window, 
    text='x',
    command=lambda:calculator.button_click(btn_prod.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=13,
    height=2
)

btn_div = tk.Button(
    master=window, 
    text='/',
    command=lambda:calculator.button_click(btn_div.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=13,
    height=2
)

btn_backspace = tk.Button(
    master=window, 
    text=u'\u2190',
    command=lambda:calculator.button_click(btn_backspace.cget('text'), label_screen),
    bd=4,
    relief='raised',
    width=29,
    height=2
)

btn_0.place(x=7, y=200)
btn_1.place(x=7, y=150)
btn_2.place(x=97, y=150)
btn_3.place(x=187, y=150)
btn_4.place(x=7, y=100)
btn_5.place(x=97, y=100)
btn_6.place(x=187, y=100)
btn_7.place(x=7, y=50)
btn_8.place(x=97, y=50)
btn_9.place(x=187, y=50)

btn_equal.place(x=277, y=200)
btn_sum.place(x=277, y=100)
btn_dif.place(x=390, y=100)
btn_prod.place(x=277, y=150)
btn_div.place(x=390, y=150)
btn_backspace.place(x=277, y=50)

window.mainloop()
