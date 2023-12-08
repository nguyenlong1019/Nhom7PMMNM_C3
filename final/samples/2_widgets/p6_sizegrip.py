import tkinter as tk
from tkinter import ttk

def on_resize(event):
    print(f"Window resized to {root.winfo_width()} x {root.winfo_height()}")

root = tk.Tk()
root.title("Sizegrip Example")

# Tạo một Frame
frame = ttk.Frame(root)
frame.pack(expand=True, fill="both")

# Thêm một Sizegrip
sizegrip = ttk.Sizegrip(frame)
sizegrip.grid(row=1, column=1, sticky="se")

# Thêm một Label để hiển thị kích thước cửa sổ
label = ttk.Label(frame, text="Resize the window to see the effect.")
label.grid(row=0, column=0, padx=10, pady=10)

# Gán sự kiện khi cửa sổ được thay đổi kích thước
root.bind("<Configure>", on_resize)

root.mainloop()
