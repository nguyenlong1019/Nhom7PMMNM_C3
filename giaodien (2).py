# import pandas as pd
# from numpy import array
# import matplotlib.pyplot as plt
# import numpy as np
# df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
# in_data = array(df.iloc[:,:])
# print(in_data)
# print('Tong so sinh vien di thi :')
# tongsv= in_data[:,1]
# print(np.sum(tongsv))
# diemA = in_data[:,3]
# diemBc = in_data[:,4]
# print('Tong sv:',tongsv)
# maxa = diemA.max()
# i, = np.where(diemA == maxa)
# print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
# plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
# plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
# plt.xlabel('Lơp')
# plt.ylabel(' So sv dat diem ')
# plt.legend(loc='upper right')
# plt.show()

from tkinter import *
import tkinter

win=Tk()
win.title("bao cao")
win.geometry("800x450")
lb1 = Label(font =('Arial,Bold',20), text ='BÁO CÁO MÔN HỌC')
lb1.place(x=320,y=10)
lb2 = Label(font =('Arial,Bold',12), text =' Báo cáo môn học Lập trình Python (FE5051) ')
lb2.place(x=10,y=80)
lb3 = Label(font =('Arial,Bold',12), text =' Thiết kế báo cáo dạng bảng ')
lb3.place(x=10,y=110)
lb4 = Label(font =('Arial,Bold',12), text =' .... ')
lb4.place(x=10,y=140)
lb5 = Label(font =('Arial,Bold',12), text =' .... ')
lb5.place(x=10,y=170)
lb6 = Label(font =('Arial,Bold',12), text =' Kết luận:  ')
lb6.place(x=10,y=200)
lb7 = Label(font =('Arial,Bold',12), text =' Ngày ... tháng ... năm ...')
lb7.place(x=578,y=260)
lb8 = Label(font =('Arial,Bold',12), text =' Người báo cáo ')
lb8.place(x=600,y=310)

button1=Button(text="Xuất file Excel")
button1.place(x=30,y=260)
button1=Button(text="Xuất file PDF ??? ")
button1.place(x=30,y=290)

win.mainloop()












