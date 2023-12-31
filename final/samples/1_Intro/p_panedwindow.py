'''
PanedWindow là thùng chứa tiện ích được sử dụng để xử lý số lượng pane (khung) được sắp xếp trong đó

w = PannedWindow(master, option=value)

bg: to set the normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
width: to set the width of the widget.
height: to set the height of the widget.
'''

from tkinter import *
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

mainloop()
