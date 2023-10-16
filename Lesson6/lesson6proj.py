import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import numpy as np

class ImageCompressor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compressor")
        
        self.image_path = None
        self.compressed_image = None
        self.resolution_image = None
        self.compression_factor = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        # Chọn ảnh
        self.select_button = tk.Button(self.root, text="Chọn ảnh", command=self.select_image)
        self.select_button.pack(pady=10)
        
        # Nén ảnh
        self.compress_button = tk.Button(self.root, text="Nén ảnh", command=self.show_compression_options)
        self.compress_button.pack(pady=10)
        
        # Tăng độ phân giải
        self.increase_resolution_button = tk.Button(self.root, text="Tăng độ phân giải", command=self.show_resolution_options)
        self.increase_resolution_button.pack(pady=10)
        
        # Lưu ảnh
        self.save_button = tk.Button(self.root, text="Lưu ảnh", command=self.save_image)
        self.save_button.pack(pady=10)
        
    def select_image(self):
        self.image_path = filedialog.askopenfilename(initialdir="/", title="Chọn ảnh", filetypes=(("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*")))
        if self.image_path:
            self.show_image(self.image_path)
        
    def show_image(self, path):
        img = Image.open(path)
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)
        
        if hasattr(self, 'image_label'):
            self.image_label.pack_forget()
        
        self.image_label = tk.Label(self.root, image=img)
        self.image_label.image = img
        self.image_label.pack()
        
    def show_compression_options(self):
        self.compression_frame = tk.Frame(self.root)
        self.compression_frame.pack(pady=10)
        
        self.compression_slider = tk.Scale(self.compression_frame, from_=10, to=100, orient=tk.HORIZONTAL)
        self.compression_slider.pack()
        self.compression_slider.set(0)
        
        self.compress_execute_button = tk.Button(self.compression_frame, text="Thực thi", command=self.compress_image)
        self.compress_execute_button.pack(pady=10)
    
        
    def compress_image(self):
        self.compression_frame.pack_forget()
        
        self.compression_factor = self.compression_slider.get()
        
        if self.image_path:
            img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.compressed_image = f"compressed_{img_name}"
                
                width = int(img.shape[1] * self.compression_factor / 100)
                height = int(img.shape[0] * self.compression_factor / 100)
                dim = (width, height)
                
                resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
                cv2.imwrite(self.compressed_image, resized_img)
                
                self.show_image(self.compressed_image)
                messagebox.showinfo("Thông báo", "Ảnh đã được nén thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi nén!")
    
    def show_resolution_options(self):
        self.resolution_frame = tk.Frame(self.root)
        self.resolution_frame.pack(pady=10)

        self.resolution_slider = tk.Scale(self.resolution_frame, from_=3, to=10, orient=tk.HORIZONTAL)
        self.resolution_slider.pack()
        self.resolution_slider.set(0)

        self.resolution_execute_button = tk.Button(self.resolution_frame, text="Thực thi", command=self.increase_resolution)
        self.resolution_execute_button.pack(pady=10)
          
    def increase_resolution(self):
        self.resolution_frame.pack_forget()
        
        self.scale_factor = self.resolution_slider.get()    
    
        if self.image_path:
            img = cv2.imread(self.image_path)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.resolution_image = f"resolution_{img_name}"
                
                # Tăng độ phân giải lên mức tối đa có thể tăng được
                 # Tăng độ phân giải gấp đôi
                width = int(img.shape[1] * self.scale_factor)
                height = int(img.shape[0] * self.scale_factor)
                dim = (width, height)
                
                resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
                
                # Áp dụng phép làm mịn (blurring)
                blurred_img = cv2.GaussianBlur(resized_img, (5, 5), 0)
                
                # Tăng cường độ sắc nét (sharpening)
                kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
                sharpened_img = cv2.filter2D(blurred_img, -1, kernel)
                
                cv2.imwrite(self.resolution_image, sharpened_img)
                
                self.show_image(self.resolution_image)
                messagebox.showinfo("Thông báo", "Ảnh đã được nén thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi tăng độ phân giải!")

    def save_image(self):
        if self.compressed_image or self.resolution_image:
            file_path = filedialog.asksaveasfilename(initialdir="/", title="Lưu ảnh", defaultextension=".jpg", filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
            if file_path:
                if self.compressed_image:
                    cv2.imwrite(file_path, cv2.imread(self.compressed_image))
                    messagebox.showinfo("Thông báo", "Ảnh đã được lưu thành công!")
                elif self.resolution_image:
                    cv2.imwrite(file_path, cv2.imread(self.resolution_image))
                    messagebox.showinfo("Thông báo", "Ảnh đã được lưu thành công!")
            else:
                messagebox.showerror("Lỗi", "Hãy chọn vị trí lưu ảnh!")
        else:
            messagebox.showerror("Lỗi", "Không có ảnh để lưu!")
            
            
root = tk.Tk()
app = ImageCompressor(root)
root.mainloop()