import tkinter as tk
from calculator import *

# !inicializando a classe calculator
calculator = Calculator()

# !configurações com relação a janela
w = 500
h = 500

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
label_screen = tk.Label(master=window,
                        text='0',
                        font='Arial 20')

label_screen.pack()

# !botões
btn_0 = tk.Button(master=window, 
                text='0', 
                command=lambda:calculator.button_click(btn_0.cget('text'), label_screen))

btn_1 = tk.Button(master=window, 
                text='1',
                command=lambda:calculator.button_click(btn_1.cget('text'), label_screen))

btn_2 = tk.Button(master=window, 
                text='2',
                command=lambda:calculator.button_click(btn_2.cget('text'), label_screen))

btn_3 = tk.Button(master=window, 
                text='3',
                command=lambda:calculator.button_click(btn_3.cget('text'), label_screen))

btn_4 = tk.Button(master=window, 
                text='4',
                command=lambda:calculator.button_click(btn_4.cget('text'), label_screen))

btn_5 = tk.Button(master=window, 
                text='5',
                command=lambda:calculator.button_click(btn_5.cget('text'), label_screen))

btn_6 = tk.Button(master=window, 
                text='6',
                command=lambda:calculator.button_click(btn_6.cget('text'), label_screen))

btn_7 = tk.Button(master=window, 
                text='7',
                command=lambda:calculator.button_click(btn_7.cget('text'), label_screen))

btn_8 = tk.Button(master=window, 
                text='8',
                command=lambda:calculator.button_click(btn_8.cget('text'), label_screen))

btn_9 = tk.Button(master=window, 
                text='9',
                command=lambda:calculator.button_click(btn_9.cget('text'), label_screen))

btn_equal = tk.Button(master=window, 
                    text='=',
                    command=lambda:calculator.button_click(btn_equal.cget('text'), label_screen))
btn_sum = tk.Button(master=window, 
                    text='+',
                    command=lambda:calculator.button_click(btn_sum.cget('text'), label_screen))
btn_dif = tk.Button(master=window, 
                    text='-',
                    command=lambda:calculator.button_click(btn_dif.cget('text'), label_screen))
btn_prod = tk.Button(master=window, 
                    text='x',
                    command=lambda:calculator.button_click(btn_prod.cget('text'), label_screen))
btn_div = tk.Button(master=window, 
                    text='/',
                    command=lambda:calculator.button_click(btn_div.cget('text'), label_screen))
btn_sqrt = tk.Button(master=window, 
                    text=u'\u221a',
                    command=lambda:calculator.button_click(btn_sqrt.cget('text'), label_screen))
btn_pow = tk.Button(master=window, 
                    text='x²',
                    command=lambda:calculator.button_click(btn_pow.cget('text'), label_screen))
btn_frac = tk.Button(master=window, 
                    text='1/x',
                    command=lambda:calculator.button_click(btn_frac.cget('text'), label_screen))
btn_percent = tk.Button(master=window, 
                        text='%',
                        command=lambda:calculator.button_click(btn_percent.cget('text'), label_screen))
btn_ce = tk.Button(master=window, 
                text='CE',
                command=lambda:calculator.button_click(btn_ce.cget('text'), label_screen))
btn_c = tk.Button(master=window, 
                text='C',
                command=lambda:calculator.button_click(btn_c.cget('text'), label_screen))
btn_backspace = tk.Button(master=window, 
                        text=u'\u2190',
                        command=lambda:calculator.button_click(btn_backspace.cget('text'), label_screen))
btn_negate = tk.Button(master=window, 
                    text='-/+',
                    command=lambda:calculator.button_click())
btn_point = tk.Button(master=window, 
                    text=',',
                    command=lambda:calculator.button_click())

btn_0.pack()
btn_1.pack()
btn_2.pack()
btn_3.pack()
btn_4.pack()
btn_5.pack()
btn_6.pack()
btn_7.pack()
btn_8.pack()
btn_9.pack()

btn_equal.pack()
btn_sum.pack()
btn_dif.pack()
btn_prod.pack()
btn_div.pack()
btn_sqrt.pack()
btn_pow.pack()
btn_frac.pack()
btn_percent.pack()
btn_ce.pack()
btn_c.pack()
btn_backspace.pack()
btn_negate.pack()
btn_point.pack()

window.mainloop()
