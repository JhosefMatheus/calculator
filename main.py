import tkinter as tk

window = tk.Tk()
window.title('Calculadora')
window.geometry('500x500')
window.resizable(False, False)

frame_a = tk.Frame(master=window, width=500, background='white')
frame_b = tk.Frame()

label = tk.Label(master=frame_a, text='0', bg='white')
label.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()
