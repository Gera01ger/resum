import  tkinter as tk
from random import randint, choice
from tkinter import messagebox
import re

a = 100
b = 90.66


def Raschet():
	symma = entry.get()
	c = float(symma) * a / b
	tk.messagebox.askokcancel(title = 'Нужно закинуть на киви:', message=f"{c:.0f} рубля(-ей)")

window = tk.Tk()

window.configure(background = 'AntiqueWhite1')

window.update_idletasks()

w, h, sx, sy = map(int, re.split('x|\+', window.winfo_geometry()))
sw = (window.winfo_rootx() - sx) * 2 + w
sh = (window.winfo_rooty() - sy) + (window.winfo_rootx() - sx) + h
sx = (window.winfo_screenwidth() - sw) // 2
sy = (window.winfo_screenheight() - sh) // 2
window.wm_geometry('+%d+%d' % (sx, sy))

window.resizable(width = False, height = False)


window.title("Калькулятор процентов QIWI -> Steam(Россия)")

window["bg"] = "black"

idea = tk.Label(window, text = "Сколько нужно на баланс Steam", font = ("Arial bold", 15), fg = "White", bg = "black")
idea.pack()

idea3 = tk.Label(window,fg = "black", bg = "black")
idea3.pack()

entry = tk.Entry(window)
entry.pack()

idea2 = tk.Label(window,fg = "black", bg = "black")
idea2.pack()

btn = tk.Button(window, text = "Рассчитать",command = Raschet, width = '40', height = "2", fg = 'black', bg = 'white')
btn.pack()





window.mainloop()

