# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# values = [25, 40, 30, 20, 70, 40, 55, 65]

# plt.bar(categories, values, color='skyblue')
# plt.xlabel('Thể Loại')
# plt.ylabel('Số Lượng')
# plt.title('Biểu Đồ Cột')
# plt.show()





import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt 

def plot_bar_chart():
    # categories = ['Mitsubishi', 'Vinfast Lux sa 2.0', 'VietNamHanoi', 'ChuongMyHaNoi', 'DaiHocCongNghiep', 'QQQQQQQQQQQQQQ', 'G', 'H']
    values = [25, 40, 30, 20, 70, 40, 55, 22]
    categories = [35, 44, 32, 99, 56, 84, 57, 63]

    # Tạo một đối tượng Figure
    fig = Figure(figsize=(6, 4), tight_layout=True)
    ax = fig.add_subplot(111)

    colormap = plt.get_cmap('viridis')
    # Vẽ biểu đồ cột
    ax.barh(categories, values, color=colormap(values))
    ax.set_xlabel('Thể Loại')
    ax.set_ylabel('Số Lượng')
    ax.set_title('Biểu Đồ Cột')
    # ax.set_yticks([])

    # Tạo đối tượng FigureCanvasTkAgg và liên kết với cửa sổ Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.place(x=0,y=0,width=400,height=400)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title('Biểu Đồ Cột trong Tkinter')
root.geometry('500x500')

# Gọi hàm vẽ biểu đồ
plot_bar_chart()

# Hiển thị cửa sổ Tkinter
root.mainloop()


