from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Separator Widget")

# tạo một Separator giữa các widget
separator1 = ttk.Separator(root, orient="horizontal")
label1 = ttk.Label(root, text="Phía trên phân cách")
label2 = ttk.Label(root, text="Phía dưới phân cách")

label1.pack(pady=10)
separator1.pack(fill='x', pady=10)
label2.pack(pady=10)

# Tạo một Separator giữa các phần của giao diện người dùng
separator2 = ttk.Separator(root, orient="vertical")
frame1 = ttk.Frame(root, width=100, height=100, relief="solid", borderwidth=1) # relief dùng để định rõ kiểu của border như bodder solid, dashed, ... trong HTML, CSS
frame2 = ttk.Frame(root, width=100, height=100, relief="solid", borderwidth=1) 

frame1.pack(side="left", padx=10)
separator2.pack(side="left", fill="y", padx=10)
frame2.pack(side="left", padx=10)

root.mainloop()