import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_chart():
    # Tạo một biểu đồ đơn giản để minh họa
    figure = Figure(figsize=(5, 4), dpi=100)
    subplot = figure.add_subplot(1, 1, 1)
    subplot.plot([1, 2, 3, 4, 5], [2, 3, 5, 7, 11], marker='o')

    # Hiển thị biểu đồ trên Canvas
    canvas = FigureCanvasTkAgg(figure, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Tạo Frame
frame = ttk.Frame(root)
frame.pack(expand=True, fill='both')

# Tạo nút để vẽ biểu đồ
draw_button = ttk.Button(frame, text="Vẽ Biểu Đồ", command=draw_chart)
draw_button.pack()

# Chạy ứng dụng
root.mainloop()
