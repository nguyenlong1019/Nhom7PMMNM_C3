import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk

# Hàm mở tệp văn bản
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete('1.0', tk.END)
            text.insert(tk.END, file.read())

# Hàm lưu tệp văn bản
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get('1.0', tk.END))

# Hàm thoát ứng dụng
def exit_app():
    if messagebox.askyesno("Thoát", "Bạn có muốn thoát ứng dụng không?"):
        root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Word đơn giản")

# Tạo menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Mở", command=open_file)
file_menu.add_command(label="Lưu", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Thoát", command=exit_app)

# Tạo thanh cuộn và vùng văn bản
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text.pack(fill=tk.BOTH, expand=1)

scrollbar.config(command=text.yview)

# Khởi chạy ứng dụng
root.mainloop()
