'''
Message đề cập đến văn bản nhiều dòng và không thể chỉnh sửa nó.

w = Message(master, option=value)

bd: to set the border around the indicator.
bg: to set the normal background color.
font: to set the font on the button label.
image: to set the image on the widget.
width: to set the width of the widget.
height: to set the height of the widget.
'''

# code from geeksforgeeks

from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
main.mainloop( )
