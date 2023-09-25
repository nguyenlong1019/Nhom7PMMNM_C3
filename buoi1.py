import numpy as np
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox

def solve_equation():
    try:
        n = int(entry_n.get())
        A = []
        b = []

        for i in range(n):
            row = []
            for j in range(n):
                a_ij = float(entry_a[i][j].get())
                row.append(a_ij)
            A.append(row)
            b_i = float(entry_b[i].get())
            b.append(b_i)

        A = np.array(A)
        b = np.array(b)

        x = np.linalg.solve(A, b)
        result_label.config(text=f"Nghiệm của hệ phương trình: {x}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên và số thực hợp lệ.")
    except np.linalg.LinAlgError:
        messagebox.showerror("Lỗi", "Hệ phương trình không có nghiệm hoặc có vô số nghiệm.")

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Giải hệ phương trình")

# Tạo và hiển thị các widget
label_n = Label(root, text="Nhập số ẩn n:")
label_n.pack()
entry_n = Entry(root)
entry_n.pack()

entry_a = []
entry_b = []

def create_entries():
    global n
    n = int(entry_n.get())
    
    for i in range(n):
        row_frame = tk.Frame(root)
        row_frame.pack()
        row_entries = []
        for j in range(n):
            label = Label(row_frame, text=f"a[{i+1}][{j+1}]:")
            label.pack(side=tk.LEFT)
            entry = Entry(row_frame)
            entry.pack(side=tk.LEFT)
            row_entries.append(entry)
        entry_a.append(row_entries)

    for i in range(n):
        label_b = Label(root, text=f"b[{i+1}]:")
        label_b.pack()
        entry = Entry(root)
        entry.pack()
        entry_b.append(entry)

create_button = Button(root, text="Tạo", command=create_entries)
create_button.pack()

solve_button = Button(root, text="Giải", command=solve_equation)
solve_button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
