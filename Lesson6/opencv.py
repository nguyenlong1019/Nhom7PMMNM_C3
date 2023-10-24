import cv2
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt


class ImageProcessingGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Xử lý ảnh")
        self.window.geometry("800x600")

        self.original_image = None
        self.processed_image = None

        self.create_widgets()

    def create_widgets(self):
        # Tạo nút chọn ảnh
        select_button = tk.Button(self.window, text="Chọn ảnh", command=self.select_image)
        select_button.pack(pady=10)

        # Tạo khung hiển thị ảnh
        self.image_frame = tk.Frame(self.window)
        self.image_frame.pack()

        # Tạo nút Zoom
        zoom_button = tk.Button(self.window, text="Zoom", command=self.zoom_image)
        zoom_button.pack(pady=10)

        # Tạo nút Xoay
        rotate_button = tk.Button(self.window, text="Xoay", command=self.rotate_image)
        rotate_button.pack(pady=10)

        # Tạo nút Chuẩn hóa
        normalize_button = tk.Button(self.window, text="Chuẩn hóa", command=self.normalize_image)
        normalize_button.pack(pady=10)

        # Tạo nút Tách biên
        edges_button = tk.Button(self.window, text="Tách biên", command=self.detect_edges)
        edges_button.pack(pady=10)

        # Tạo hộp thoại nhập thông số Zoom
        self.zoom_entry = tk.Entry(self.window)
        self.zoom_entry.pack()
        zoom_label = tk.Label(self.window, text="Nhập tỷ lệ Zoom (x, y):")
        zoom_label.pack()

        # Tạo hộp thoại nhập góc xoay
        self.rotate_entry = tk.Entry(self.window)
        self.rotate_entry.pack()
        rotate_label = tk.Label(self.window, text="Nhập góc xoay:")
        rotate_label.pack()

        # Tạo hộp thoại nhập ngưỡng tách biên
        self.threshold1_entry = tk.Entry(self.window)
        self.threshold1_entry.pack()
        threshold1_label = tk.Label(self.window, text="Ngưỡng 1:")
        threshold1_label.pack()

        self.threshold2_entry = tk.Entry(self.window)
        self.threshold2_entry.pack()
        threshold2_label = tk.Label(self.window, text="Ngưỡng 2:")
        threshold2_label.pack()

    def select_image(self):
        # Mở hộp thoại để chọn ảnh từ thiết bị
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg; *.jpeg; *.png; *.bmp')])

        # Kiểm tra xem người dùng đã chọn ảnh hay chưa
        if file_path:
            # Đọc ảnh từ đường dẫn đã chọn
            self.original_image = cv2.imread(file_path)

            # Chuyển đổi ảnh sang định dạng hỗ trợ Tkinter
            image = self.cv2_to_image(self.original_image)

            # Hiển thị ảnh ban đầu
            self.display_image(image)

    def zoom_image(self):
        # Lấy tỷ lệ zoom từ hộp thoại
        zoom_ratio = self.zoom_entry.get()
        zoom_ratio = zoom_ratio.split(',')
        if len(zoom_ratio) != 2:
            messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng tỷ lệ (x, y)")
            return

        try:
            zoom_ratio = float(zoom_ratio[0]), float(zoom_ratio[1])
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số cho tỷ lệ Zoom")
            return

        # Kiểm tra ảnh gốc đã được chọn
        if self.original_image is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh trước khi thực hiện Zoom")
            return

        # Thực hiện Zoom
        zoomed_image = cv2.resize(self.original_image, None,
                                 fx=zoom_ratio[0], fy=zoom_ratio[1], interpolation=cv2.INTER_LINEAR)

        # Chuyển đổi ảnh sau khi Zoom sang định dạng hỗ trợ Tkinter
        image = self.cv2_to_image(zoomed_image)

        # Hiển thị ảnh sau khi Zoom
        self.display_image(image)

    def rotate_image(self):
        # Lấy góc xoay từ hộp thoại
        rotate_angle = self.rotate_entry.get()

        try:
            rotate_angle = float(rotate_angle)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số cho góc xoay")
            return

        # Kiểm tra ảnh gốc đã được chọn
        if self.original_image is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh trước khi thực hiện Xoay")
            return

        # Thực hiện Xoay
        rotated_image = self.rotate(self.original_image, rotate_angle)

        # Chuyển đổi ảnh sau khi Xoay sang định dạng hỗ trợ Tkinter
        image = self.cv2_to_image(rotated_image)

        # Hiển thị ảnh sau khi Xoay
        self.display_image(image)

    def normalize_image(self):
        # Kiểm tra ảnh gốc đã được chọn
        if self.original_image is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh trước khi thực hiện Chuẩn hóa")
            return

        # Thực hiện Chuẩn hóa
        normalized_image = self.normalize(self.original_image)

        # Chuyển đổi ảnh sau khi Chuẩn hóa sang định dạng hỗ trợ Tkinter
        image = self.cv2_to_image(normalized_image)

        # Hiển thị ảnh sau khi Chuẩn hóa
        self.display_image(image)

    def detect_edges(self):
        # Lấy ngưỡng tách biên từ hộp thoại
        threshold1 = self.threshold1_entry.get()
        threshold2 = self.threshold2_entry.get()

        try:
            threshold1 = int(threshold1)
            threshold2 = int(threshold2)
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên cho ngưỡng")
            return

        # Kiểm tra ảnh gốc đã được chọn
        if self.original_image is None:
            messagebox.showerror("Lỗi", "Vui lòng chọn ảnh trước khi thực hiện Tách biên")
            return

        # Thực hiện Tách biên
        edges = self.detect_edges_canny(self.original_image, threshold1, threshold2)

        # Chuyển đổi ảnh sau khi Tách biên sang định dạng hỗ trợ Tkinter
        image = self.cv2_to_image(edges)

        # Hiển thị ảnh sau khi Tách biên
        self.display_image(image)

    def display_image(self, image):
        # Xóa ảnh hiện có trong khung hiển thị
        for widget in self.image_frame.winfo_children():
            widget.destroy()

        # Hiển thị ảnh mới trong khung hiển thị
        image_label = tk.Label(self.image_frame, image=image)
        image_label.image = image
        image_label.pack()

    def cv2_to_image(self, cv2_image):
        image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        return image

    def rotate(self, image, angle):
        rows, cols = image.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotated_image = cv2.warpAffine(image, M, (cols, rows))
        return rotated_image

    def normalize(self, image):
        normalized_image = np.zeros(image.shape, dtype=np.float32)
        normalized_image = cv2.normalize(image, normalized_image, 0, 255, cv2.NORM_MINMAX)
        normalized_image = normalized_image.astype(np.uint8)
        return normalized_image

    def detect_edges_canny(self, image, threshold1, threshold2):
        edges = cv2.Canny(image, threshold1, threshold2)
        return edges

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
        app = ImageProcessingGUI()
        app.run()
