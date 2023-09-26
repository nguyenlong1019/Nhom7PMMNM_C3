# import pandas as pd
# from numpy import array
# import matplotlib.pyplot as plt
# import numpy as np
# import csv

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
      

import csv
import os
import openpyxl


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



