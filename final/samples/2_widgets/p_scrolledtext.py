import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage

def insert_image():
    image_path = "test_ratio.png"  # Đường dẫn đến hình ảnh của bạn
    img = PhotoImage(file=image_path)
    text.image_create(tk.END, image=img)

root = tk.Tk()
root.title("Text with Image Example")

# Tạo một widget Text
text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
text.pack(padx=10, pady=10)

# Thêm nút để chèn hình ảnh
insert_button = tk.Button(root, text="Insert Image", command=insert_image)
insert_button.pack(pady=10)

root.mainloop()
