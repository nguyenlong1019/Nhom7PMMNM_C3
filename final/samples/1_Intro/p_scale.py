'''
Scale: thanh trượt đồ họa cho phép chọn giá trị

w = Scale(master, option=value)

cursor: To change the cursor pattern when the mouse is over the widget.
activebackground: To set the background of the widget when mouse is over the widget.
bg: to set the normal background color.
orient: Set it to HORIZONTAL or VERTICAL according to the requirement.
from_: To set the value of one end of the scale range.
to: To set the value of the other end of the scale range.
image: to set the image on the widget.
width: to set the width of the widget.
'''

from tkinter import *

root = Tk()
widget = Scale(root, from_=0, to=24)
widget.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()

root.mainloop()