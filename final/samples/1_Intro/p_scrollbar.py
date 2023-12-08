'''
w = Scrollbar(master, option=value)

width: to set the width of the widget.
activebackground: To set the background when mouse is over the widget.
bg: to set the normal background color.
bd: to set the size of border around the indicator.

tham số cursor nhận các giá trị sau: arrow (mũi tên - mặc định), circle, dot, cross (chữ thập), hand1, hand2 (bàn tay)
plus (dấu cộng), watch, xterm (chữ x)
'''

from tkinter import *
root = Tk()
scorllbar = Scrollbar(root)
scorllbar.pack(side=RIGHT, fill=Y)

list1 = Listbox(root, yscrollcommand=scorllbar.set)
for line in range(100):
    list1.insert(END, f"This is line number {line + 1}")
list1.pack(side=LEFT, fill=BOTH)
scorllbar.config(command=list1.yview)

root.mainloop()