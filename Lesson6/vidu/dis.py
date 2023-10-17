# import cv2
# print(cv2.__version__)
# # 4.6.0
import cv2

# Reading the image using imread()
image = cv2.imread('dragon_ai.png')

# Trích xuất height và width của hình ảnh
h, w = image.shape[:2]

# Hiển thị height và width của hình ảnh
print(f"Height: {h}  Width: {w}")

# Trích xuất giá trị màu RGB của 1 pixel
(B, G, R) = image[100,100]

# Hiển thị giá trị màu RGB tại pixel đó
print(f"R = {R}   G = {G}   B = {B}")

# Trích xuất từng kênh màu của 1 pixel bất kỳ
# 0 là Blue, 1 Green, 2 Red
B = image[100, 100, 0]
G = image[100, 100, 1]
R = image[100, 100, 2]
print(f"B = {B}")
print(f"G = {G}")
print(f"R = {R}")

# Trích xuất vùng quan tâm (Region of Interest - ROI)
# height1:height2, width1:width2
roi = image[100:500, 200:700]
cv2.imwrite("roi.png",roi)

# Thay đổi kích thước mà vẫn duy trì tỷ lệ khung nhìn
ratio = 700 / w
# Tạo tuple của width và height
dimetions = (700, int(h * ratio))
# Resize image
resize_aspect = cv2.resize(image, dimetions)
cv2.imwrite("resize.png",resize_aspect)

# Xoay một hình ảnh
# Tính tọa độ tâm của hình ảnh
center = (w // 2, h // 2)
# Tạo một ma trận xoay
matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
# Thực hiện phép biến đổi affine
rotated = cv2.warpAffine(image, matrix, (w,h))
cv2.imwrite("rotated.png", rotated)

# Vẽ hình chữ nhật và hiển thị text
# là hành động in-place nên cần copy ảnh gốc
output = image.copy()
rectangle = cv2.rectangle(output, (1200, 900), (600,400), (0,0,0), 2)
text = cv2.putText(output, "Group 7 PMMNM", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 5,(255,255,255),2)
cv2.imwrite("output.png", output)