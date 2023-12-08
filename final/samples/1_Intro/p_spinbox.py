'''
Spinbox là tiện ích của entry, giá trị được thay bằng giá trị cố định

w = SpinBox(master, option=value)

bg: to set the normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
command: To call a function.
width: to set the width of the widget.
activebackground: To set the background when mouse is over the widget.
disabledbackground: To disable the background when mouse is over the widget.
from_: To set the value of one end of the range.
to: To set the value of the other end of the range.
'''

from tkinter import *
root = Tk()
w = Spinbox(root, from_=0, to=100)
w.pack()
root.mainloop()
