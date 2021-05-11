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

# !botões
btn_0 = tk.Button(master=window, 
                text='0', 
                command=lambda:calculator.button_click(btn_0.cget('text')))

btn_1 = tk.Button(master=window, 
                text='1',
                command=lambda:calculator.button_click(btn_1.cget('text')))

btn_2 = tk.Button(master=window, 
                text='2',
                command=lambda:calculator.button_click(btn_2.cget('text')))

btn_3 = tk.Button(master=window, 
                text='3',
                command=lambda:calculator.button_click(btn_3.cget('text')))

btn_4 = tk.Button(master=window, 
                text='4',
                command=lambda:calculator.button_click(btn_4.cget('text')))

btn_5 = tk.Button(master=window, 
                text='5',
                command=lambda:calculator.button_click(btn_5.cget('text')))

btn_6 = tk.Button(master=window, 
                text='6',
                command=lambda:calculator.button_click(btn_6.cget('text')))

btn_7 = tk.Button(master=window, 
                text='7',
                command=lambda:calculator.button_click(btn_7.cget('text')))

btn_8 = tk.Button(master=window, 
                text='8',
                command=lambda:calculator.button_click(btn_8.cget('text')))

btn_9 = tk.Button(master=window, 
                text='9',
                command=lambda:calculator.button_click(btn_9.cget('text')))

btn_equal = tk.Button(master=window, 
                    text='=',
                    command=lambda:calculator.button_click(btn_equal.cget('text')))
btn_sum = tk.Button(master=window, 
                    text='+',
                    command=lambda:calculator.button_click(btn_sum.cget('text')))
btn_dif = tk.Button(master=window, 
                    text='-',
                    command=lambda:calculator.button_click(btn_dif.cget('text')))
btn_prod = tk.Button(master=window, 
                    text='x',
                    command=lambda:calculator.button_click(btn_prod.cget('text')))
btn_div = tk.Button(master=window, 
                    text='/',
                    command=lambda:calculator.button_click(btn_div.cget('text')))
btn_sqrt = tk.Button(master=window, 
                    text=u'\u221a',
                    command=lambda:calculator.button_click(btn_sqrt.cget('text')))
btn_pow = tk.Button(master=window, 
                    text='x²',
                    command=lambda:calculator.button_click(btn_pow.cget('text')))
btn_frac = tk.Button(master=window, 
                    text='1/x',
                    command=lambda:calculator.button_click(btn_frac.cget('text')))
btn_percent = tk.Button(master=window, 
                        text='%',
                        command=lambda:calculator.button_click(btn_percent.cget('text')))
btn_ce = tk.Button(master=window, 
                text='CE',
                command=lambda:calculator.button_click(btn_ce.cget('text')))
btn_c = tk.Button(master=window, 
                text='C',
                command=lambda:calculator.button_click(btn_c.cget('text')))
btn_backspace = tk.Button(master=window, 
                        text=u'\u2190',
                        command=lambda:calculator.button_click(btn_backspace.cget('text')))
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
