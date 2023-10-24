import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

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
        self.compress_button = tk.Button(self.root, text="Phóng thu", command=self.show_compression_options)
        self.compress_button.pack(pady=10)
        
        # Tăng độ phân giải
        self.increase_resolution_button = tk.Button(self.root, text="Xoay ảnh", command=self.show_resolution_options)
        self.increase_resolution_button.pack(pady=10)
        
        # Tăng độ phân giải
        self.chuanhoa_button = tk.Button(self.root, text="Chuẩn hoá", command=self.show_chuanhoa_options)
        self.chuanhoa_button.pack(pady=10)
        
        # Tăng độ phân giải
        self.tachbien_button = tk.Button(self.root, text="Tách biên", command=self.show_tachbien_options)
        self.tachbien_button.pack(pady=10)
        
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
        
        self.compression_slider = tk.Scale(self.compression_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.compression_slider.pack()
        self.compression_slider.set(1)
        
        self.compression_slider2 = tk.Scale(self.compression_frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.compression_slider2.pack()
        self.compression_slider2.set(1)
        
        self.compress_execute_button = tk.Button(self.compression_frame, text="Thực thi", command=self.compress_image)
        self.compress_execute_button.pack(pady=10)
    
        
    def compress_image(self):
        self.compression_frame.pack_forget()
        
        self.compression_factor = self.compression_slider.get()
        self.compression_factor2 = self.compression_slider2.get()
        if self.image_path:
            img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.compressed_image = f"compressed_{img_name}"
                
                h, w = img.shape[:2]
                a = int(self.compression_factor)
                b = int(self.compression_factor2)
                
                output = cv2.resize(img, (a*w, b*h), interpolation=cv2.INTER_LINEAR)
                cv2.imshow("Image1", img)
                cv2.imshow("Image2", output)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                messagebox.showinfo("Thông báo", "Ảnh đã được phóng thu thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi nén!")
    
    def show_resolution_options(self):
        self.resolution_frame = tk.Frame(self.root)
        self.resolution_frame.pack(pady=10)

        self.resolution_slider = tk.Scale(self.resolution_frame, from_=-180, to=180, orient=tk.HORIZONTAL)
        self.resolution_slider.pack()
        self.resolution_slider.set(0)
        
        self.resolution_slider2 = tk.Scale(self.resolution_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.resolution_slider2.pack()
        self.resolution_slider2.set(1)

        self.resolution_execute_button = tk.Button(self.resolution_frame, text="Thực thi", command=self.increase_resolution)
        self.resolution_execute_button.pack(pady=10)
          
    def increase_resolution(self):
        self.resolution_frame.pack_forget()
        
        self.scale_factor = self.resolution_slider.get()    
        self.scale_factor2 = self.resolution_slider2.get()    
        if self.image_path:
            img = cv2.imread(self.image_path)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.resolution_image = f"resolution_{img_name}"
                
                angle = int(self.scale_factor)
                scale = int(self.scale_factor2)
                
                # Trích xuất height và width của hình ảnh
                h, w = img.shape[:2]

                # Hiển thị height và width của hình ảnh
                print(f"Height: {h}  Width: {w}")

                # Trích xuất vùng quan tâm (Region of Interest - ROI)
                # height1:height2, width1:width2
                roi = img[100:500, 200:700]
                cv2.imwrite("roi.png",roi)

                # Thay đổi kích thước mà vẫn duy trì tỷ lệ khung nhìn
                ratio = 700 / w

                # Tạo tuple của width và height
                dimetions = (700, int(h * ratio))

                # Resize image
                resize_aspect = cv2.resize(img, dimetions)
                cv2.imwrite("resize.png",resize_aspect)

                # Xoay một hình ảnh
                # Tính tọa độ tâm của hình ảnh
                center = (w // 2, h // 2)

                # Tạo một ma trận xoay
                matrix = cv2.getRotationMatrix2D(center, angle=angle, scale=scale)

                # Thực hiện phép biến đổi affine
                rotated = cv2.warpAffine(img, matrix, (w,h))
                cv2.imwrite("rotated.png", rotated)
                cv2.imshow("Image111", img)
                cv2.imshow("Image222", rotated)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                messagebox.showinfo("Thông báo", "Ảnh đã được nén thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi tăng độ phân giải!")
            
    def show_chuanhoa_options(self):
        self.chuanhoa_frame = tk.Frame(self.root)
        self.chuanhoa_frame.pack(pady=10)

        self.chuanhoa_execute_button = tk.Button(self.chuanhoa_frame, text="Thực thi", command=self.chuanhoa_solution)
        self.chuanhoa_execute_button.pack(pady=10)
    
        
    def chuanhoa_solution(self):
        self.chuanhoa_frame.pack_forget()
        
        if self.image_path:
            img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.chuanhoas_image = f"chuanhoas_{img_name}"
                
                final = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
                cv2.imwrite("rotated1.png", final)
                gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                cv2.imwrite("rotated2.png", gray)
                final1 = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
                cv2.imwrite("rotated3.png", final1) 
                cv2.imshow("RGB Image", img)
                cv2.imshow("RGB Image1", final)
                cv2.imshow("Grayscale Image", gray)
                cv2.imshow("RGB Image2", final1)
                # Vẽ hình chữ nhật và hiển thị text
                # là hành động in-place nên cần copy ảnh gốc
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                messagebox.showinfo("Thông báo", "Ảnh đã được phóng thu thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi nén!")
            
    def show_tachbien_options(self):
        self.tachbien_frame = tk.Frame(self.root)
        self.tachbien_frame.pack(pady=10)
        
        self.tachbien_slider = tk.Scale(self.tachbien_frame, from_=0, to=1000, orient=tk.HORIZONTAL)
        self.tachbien_slider.pack()
        self.tachbien_slider.set(1)
        
        self.tachbien_slider2 = tk.Scale(self.tachbien_frame, from_=0, to=1000, orient=tk.HORIZONTAL)
        self.tachbien_slider2.pack()
        self.tachbien_slider2.set(1)
        
        self.tachbien_execute_button = tk.Button(self.tachbien_frame, text="Thực thi", command=self.tachbien_solution)
        self.tachbien_execute_button.pack(pady=10)
    
        
    def tachbien_solution(self):
        self.tachbien_frame.pack_forget()
        
        self.tachbien_factor = self.tachbien_slider.get()
        self.tachbien_factor2 = self.tachbien_slider2.get()
        if self.image_path:
            img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
            if img is not None:
                img_name = self.image_path.split("/")[-1]
                self.tachbiens_image = f"tachbiens_{img_name}"
                
                h, w = img.shape[:2]
                a = int(self.tachbien_factor)
                b = int(self.tachbien_factor2)
                image1_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                edges = cv2.Canny(image=image1_rgb,threshold1=a,threshold2=b)
                cv2.imshow("Image1111", img)
                cv2.imshow("Image2222", edges)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                messagebox.showinfo("Thông báo", "Ảnh đã được phóng thu thành công!")
            else:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
        else:
            messagebox.showerror("Lỗi", "Hãy chọn ảnh trước khi nén!")
            
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