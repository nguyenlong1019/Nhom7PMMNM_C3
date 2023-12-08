'''
    w = MenuButton(master, option=value)

    là một phần của Menu
    activebackground: To set the background when mouse is over the widget.
    activeforeground: To set the foreground when mouse is over the widget.
    bg: to set the normal background color.
    bd: to set the size of border around the indicator.
    cursor: To appear the cursor when the mouse over the menubutton.
    image: to set the image on the widget.
    width: to set the width of the widget.
    height: to set the height of the widget.
    highlightcolor: To set the color of the focus highlight when widget has to be focused.
'''

from tkinter import *

root = Tk()
mb = Menubutton(root, text='Menu App')
mb.grid()

# tạo một thuộc tính menu mới cho mb, tearoff là một tùy chọn được sử dụng khi tạo Menu
# nếu tearoff = 1 sẽ có đường kẻ gạch (nét đứt - tear-off), bằng 0 sẽ không hiển thị
mb.menu = Menu(mb, tearoff=1)

# gán menu con cho Menu button
mb["menu"] = mb.menu

# tạo một biến kiểu IntVar() để lữu trữ trạng thái của Check button "Contact"
cVar = IntVar()
# tạo một biến kiểu IntVar() để lữu trữ trạng thái của Check button "About"
aVar = IntVar()

# thêm Check button vào menu con
mb.menu.add_checkbutton(label="Contact", variable=cVar)

mb.menu.add_checkbutton(label="About", variable=aVar)

mb.pack()

root.mainloop()










