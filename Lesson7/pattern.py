


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt

#----------------------------------
# Tran Ba Quang
#----------------------------------
def select_image():
    global img_label1, img_original
    
    # Chọn ảnh từ hộp thoại
    file_path = filedialog.askopenfilename()
    
    # Kiểm tra xem người dùng đã chọn ảnh hay chưa
    if file_path:
        # Đọc ảnh
        img = Image.open(file_path)
        img.thumbnail((400,400))
        
        # Chuyển đổi ảnh từ OpenCV sang định dạng hỗ trợ Tkinter
        # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img)
        
        # Cập nhật ảnh gốc lên giao diện
        img_label1.configure(image=img_tk)
        img_label1.image = img_tk
        img_original = img
        
        plt.show(img_rgb)
def save_image():
    global img_original
    
    # Kiểm tra xem đã có ảnh gốc hay chưa
    if img_original is None:
        return
    
    # Chọn vị trí lưu tệp ảnh
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    
    # Kiểm tra xem người dùng đã chọn vị trí lưu hay chưa
    if file_path:
        # Lưu ảnh gốc
        cv2.imwrite(file_path, img_original)
        print("Lưu thành công!")


#----------------------------------
# Nguyen Van Long
#----------------------------------



root = Tk()
root.title("Group 7")
root.geometry("1400x650")

custom = ttk.Frame(root)
custom.grid(row=0, column=0, padx=10, pady=10)

x_label = ttk.Label(custom, text="Nhập kích cỡ ma trận vuông:")
x_label.grid(row=0, column=0, padx=10, pady=10)
# y_label = ttk.Label(custom, text="Tọa độ y:")
# y_label.grid(row=0, column=1, padx=10, pady=10)

x_under = ttk.Entry(custom)
x_under.grid(row=1, column=0, padx=5, pady=5)
# y_under = ttk.Entry(custom)
# y_under.grid(row=1, column=1, padx=5, pady=5)

# scale = ttk.Scale(custom, from_=9, to=36)
# scale.grid(row=2, column=0, padx=5, pady=5)
# scale.set(9)

read_img = ttk.Button(custom, text="Open Image", command=select_image)
read_img.grid(row=3, column=0, padx=10, pady=10)
save_image = ttk.Button(custom, text="Save", command=None)
save_image.grid(row=3, column=1, padx=10, pady=10)

def event_mouse(event):
    x = event.x 
    y = event.y
    print(x,y)

root.bind("<Button-1>", event_mouse)

display = ttk.LabelFrame(root, text="Image")
display.grid(row=1,column=0,padx=10,pady=10)
img_label1 = ttk.Label(image=None)
img_label1.grid(row=1,column=0,padx=5,pady=5)




root.mainloop()
