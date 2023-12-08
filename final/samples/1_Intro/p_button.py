'''
    btn = Button(root, option=value), root là tên phần tử cha (bình thường là tên cửa sổ), các option có thể như sau:
    activebackground: để đặt màu nền khi con trỏ ở trên Button (màu bg) khi con trỏ nhấn button
    activeforeground: để đặt màu nền trước khi con trỏ ở trên Button (màu chữ)
    bg: set background chuẩn cho Button
    command: gọi đến hàm
    font: set font cho Button
    image: set image cho Button
    width: set width cho Button
    height: set height cho Button
'''

from tkinter import *
from tkinter import font

root = Tk()

custom_font = font.Font(family="Helvetica", size=14, weight="bold", slant="italic")

root.title("Button")
btn = Button(root, text="Quit", command=quit, activeforeground="yellow", activebackground="red", width=10, height=10, font=custom_font)
btn.pack()

root.mainloop()