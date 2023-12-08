'''
w = Listbox(master, option=value)

highlightcolor: To set the color of the focus highlight when widget has to be focused.
bg: to set the normal background color.
bd: to set the border width in pixels.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the widget.
height: to set the height of the widget.
'''

from tkinter import *

root = Tk()
lb1 = Listbox(root)
lb1.insert(1, "Python")
lb1.insert(2, "C++")
lb1.insert(3, "JavaScript")
lb1.insert(4, "HTML5 CSS3")
lb1.insert(5, "Java")
lb1.insert(6, "C#")
lb1.insert(7, "PHP")
lb1.insert(8, "R")
lb1.insert(9, "SQL server - MySQL - SQLite - MongoDB")
lb1.pack()
root.mainloop()