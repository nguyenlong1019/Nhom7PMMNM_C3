# sử dụng askcolor

from tkinter import *
from tkinter import colorchooser, ttk


def choose_color():
    color_code = colorchooser.askcolor()
    print(color_code) # ((134, 187, 143), '#86bb8f')


root = Tk()
btn = ttk.Button(root, text='Choose Color', command=choose_color)
btn.pack()

root.geometry('400x400')
root.mainloop()