from tkinter import *
from tkinter import ttk
from time import sleep


def start_progress():
    progress["maximum"] = 100
    for i in range(100):
        sleep(0.05) # mô phỏng công việc diễn ra
        progress["value"] = i
        progress.update()

    # tkinter cho phép truy cập các option bằng cách này
    progress["value"] = 0 # reset giá trị sau khi hoàn thành


root = Tk()
root.title("Progress Bar")

# tạo progressbar
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")

# tạo button để kích hoạt Progressbar 
start_button = ttk.Button(root, text="Start Progress", command=start_progress)

# Đặt Progressbar và Button 
progress.pack(pady=20)
start_button.pack(pady=10)

root.mainloop()
