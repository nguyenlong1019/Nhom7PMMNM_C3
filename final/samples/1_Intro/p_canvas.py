'''
w = Canvas(master, option=value)

bd: to set the border width in pixels.
bg: to set the normal background color.
cursor: to set the cursor used in the canvas.
highlightcolor: to set the color shown in the focus highlight.
width: to set the width of the widget.
height: to set the height of the widget.
'''

from tkinter import *
root = Tk()
# tạo canvas vùng vẽ
w = Canvas(root, width=40, height=60, borderwidth=5, background="pink")
w.pack()

h_ = 20
w_ = 200
y = h_ // 2
# vẽ đường thẳng trên canvas
w.create_line(0, y, w_, y)

root.mainloop()