
# img=cv2.imread('dragon_ai.png',cv2.IMREAD_UNCHANGED)
# half=cv2.resize(img, (0,0),fx=0.1,fy=0.1)
# bigger=cv2.resize(img,(1050,1610))
# stretch_near=cv2.resize(img, (780,540),interpolation=cv2.INTER_LINEAR)
# Titles=["Original", "Half", "Bigger","Interpolation Nearest"]
# images=[img,half,bigger,stretch_near]
# count=4
# for i in range(count):
#   plt.subplot(2,2,i+1)
#   plt.title(Titles[i])
#   plt.imshow(images[i])
# plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('dragon_ai.png')
h, w = img.shape[:2]
a, b = [int(x) for x in input().split()]
# print(a,b)
output = cv2.resize(img, (a*w, b*h), interpolation=cv2.INTER_LINEAR)
images = [img, output]
titles = ["Input", "Output"]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
plt.show()

# from tkinter import *
# from tkinter import ttk, filedialog

# root = Tk()
# root.title("Group 7")
# root.geometry('500x500')


#Hienthi 1 ảnh cv2.imshow()
#Luu 1 anh cv2.imwrite()