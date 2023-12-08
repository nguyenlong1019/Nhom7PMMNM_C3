'''
Syntax:
    w = CheckButton(master, option=value)

    text: set text
    activebackground: to set the background color when widget is under the cursor.
    activeforeground: to set the foreground color when widget is under the cursor.
    bg: to set the normal background color.
    command: to call a function.
    font: to set the font on the button label.
    image: to set the image on the widget.
'''

from tkinter import *

root = Tk()
root.title("Checkbutton widget")
c_btn = Checkbutton(root, text="Hello")
c_btn.pack()
root.mainloop()

