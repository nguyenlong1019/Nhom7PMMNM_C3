import csv
import os
import openpyxl

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


# en1 = Entry(width = 20,font =('Arial,Bold',12))
# en1.place(x=110,y=20)
# en2 = Entry(width = 20,font =('Arial,Bold',12))
# en2.place(x=110,y=50)
win.mainloop()


# if not os.path.exists("report.csv"):
#     file = open('report.csv', mode='w').close()
#     print("File đã tạo thành công!!!")
# else:
#     pass
    
title = "Báo cáo môn học Lập trình Python (FE6051)"
fields = ["Tổng Số SV", "Số SV điểm A (%)", "Số SV điểm F (%)", "Số điểm sinh viên đạt được nhiều nhất"]
data = [
    ["1000","34(3,4%)","19(1,9%)","C+"],
    ["","","","26/09/2023"],
    ["","","","Nguyễn Văn Long"]
]

with open(file='report.csv', mode='w', encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(title)
    csvwriter.writerow(fields)
    csvwriter.writerows(data)
    print("Xuất báo cáo thành công!!!")