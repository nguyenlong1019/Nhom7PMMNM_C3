'''
w = TopLevel(master, option=value)

bg: to set the normal background color.
bd: to set the size of border around the indicator.
cursor: To appear the cursor when the mouse over the menubutton.
width: to set the width of the widget.
height: to set the height of the widget.
''' 

from tkinter import *
root = Tk()
root.title('Main')

top = Toplevel()
top.title('Sub')

top.mainloop()