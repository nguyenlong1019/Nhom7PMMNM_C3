'''
Cấu trúc phân lớp

Kỹ thuật máy tính
    Kỹ thuật phần mềm
        Lập trình web
        Lập trình android
        Lập trình ứng dụng (C#)
    Khoa học máy tính
        Lập trình Python
        Học máy và trí tuệ nhân tạo
        Lập trình Java
    An toàn thông tin
        Lập trình C++
        Cấu trúc dữ liệu và giải thuật
        Mật mã học

'''


from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Treeview")

ttk.Label(root, text="Treeview (hierarchical)").pack()

# tạo treeview
treeview = ttk.Treeview(root)
treeview.pack()

# thêm mục gốc vào parent
# parent, index, item id (iid)
treeview.insert(parent='', index='0', iid='item1', text="Kỹ thuật máy tính")

# thêm các mục con 
treeview.insert(parent='', index='1', iid='item2', text="Kỹ thuật phần mềm")  # parent='' mục mới là mục gốc
treeview.insert(parent='', index='2', iid='item3', text="Khoa học máy tính")
treeview.insert(parent='', index=END, iid='item4', text="An toàn thông tin")

# thêm các mục con của "Kỹ thuật phần mềm"
treeview.insert(parent='item2', index=END, iid='item2.1', text="Lập trình web")
treeview.insert(parent='item2', index=END, iid='item2.2', text="Lập trình android")
treeview.insert(parent='item2', index=END, iid='item2.3', text="Lập trình ứng dụng (C#)")

# thêm các mục con của "Khoa học máy tính"
treeview.insert(parent='item3', index=END, iid='item3.1', text="Lập trình Python")
treeview.insert(parent='item3', index=END, iid='item3.2', text="Học máy và trí tuệ nhân tạo")
treeview.insert(parent='item3', index=END, iid='item3.3', text="Lập trình Java")

# thêm các mục con của "An toàn thông tin"
treeview.insert(parent='item4', index=END, iid="item4.1", text="Lập trình C++")
treeview.insert(parent='item4', index=END, iid="item4.2", text="Cấu trúc dữ liệu và giải thuật")
treeview.insert(parent='item4', index=END, iid="item4.3", text="Mật mã học")

# di chuyển item2, item3, item4 vào item1
treeview.move(item='item2',parent='item1',index=END)
treeview.move(item='item3',parent='item1',index=END)
treeview.move(item='item4',parent='item1',index=END)

root.mainloop()
