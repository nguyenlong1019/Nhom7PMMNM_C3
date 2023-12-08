from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('500x500')

# ttk Button (themed tk)
btn = Button(root, text="Quit", command=quit)
btn.pack()

root.mainloop()