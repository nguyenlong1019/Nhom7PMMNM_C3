'''
w = RadioButton(master, option=value)

activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set the normal background color.
command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the label in characters.
height: to set the height of the label in characters.
'''

from tkinter import *
root = Tk()
v = IntVar()

# anchor là tham số neo, W: west, có thể có các giá trị khác theo các hướng đông (E - east), Nam (S - south), bắc (N - north), ngoài ra còn các hướng đông bắc, đông nam, tây bắc, tây nam, ...
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()
