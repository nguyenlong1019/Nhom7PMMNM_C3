'''
w = Menu(master, option=value)
dùng để tạo menu

title: To set the title of the widget.
activebackground: to set the background color when widget is under the cursor.
activeforeground: to set the foreground color when widget is under the cursor.
bg: to set the normal background color.
command: to call a function.
font: to set the font on the button label.
image: to set the image on the widget.

'''

from tkinter import *

root = Tk()

# tạo menu
menu = Menu(root)

# add menu vào root
root.config(menu=menu)

# tạo một menu và thêm vào menu cha
file_menu = Menu(menu) # menu is parent

# menu cha add phần tử menu con
menu.add_cascade(label='File', menu=file_menu)

# menu con thêm các file
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# tạo menu help mới
help_menu = Menu(menu)

# add vào menu cha
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')

root.mainloop()