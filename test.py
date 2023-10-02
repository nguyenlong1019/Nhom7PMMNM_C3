import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('diemPython.csv',index_col=0,header = 0)

in_data = array(df.iloc[:,:])
print(in_data)
print('Tong so lop :')
solop = in_data[:,0]
print(len(solop))
print('Tong so sinh vien di thi :')
tongsv= in_data[:,1]
print(np.sum(tongsv))
diemA = in_data[:,3]
diemBc = in_data[:,4]
print('Tong sv:',tongsv)
print("bang thong ke moi")
in_datanew = np.delete(in_data,2,axis=1)
print(in_datanew)
kieusosanh = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
dulieusosanh = np.array([np.sum(in_data[:,3]),np.sum(in_data[:,4]),np.sum(in_data[:,5])
                        ,np.sum(in_data[:,6]),np.sum(in_data[:,7]),np.sum(in_data[:,8])
                        ,np.sum(in_data[:,9]),np.sum(in_data[:,10])])
myexplode = [0.2,0,0,0,0,0,0,0.2]
fig1 = plt.figure()
plt.pie(dulieusosanh, labels=kieusosanh,wedgeprops={'edgecolor':'white','linewidth':1.5},explode=myexplode, autopct='%1.1f%%')
plt.title("Tỉ lệ điểm của tất cả các lớp")
plt.legend(loc='upper left',bbox_to_anchor=(0.9, 1.1))
plt.axis('equal') 

maxa = diemA.max()
i, = np.where(diemA == maxa)
print("=========")
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))

dict1 = dict(zip(kieusosanh,dulieusosanh))
timmax = max(dict1.values())
maxkey = [key for key, value in dict1.items() if value == timmax][0]
print(f"Số điểm sinh viên đạt được nhiều nhất: {maxkey}")

fig2 = plt.figure()
kieusosanh1 = ["L1","L2","TX1","TX2","CK"]
Solieu = np.array([np.sum(in_data[:,11]),np.sum(in_data[:,12]),np.sum(in_data[:,13]),np.sum(in_data[:,14]),np.sum(in_data[:,15])])
plt.bar(kieusosanh1, Solieu,width=0.3)
plt.title("Tổng các cơ số điểm")
plt.xlabel("Loại bài thi")
plt.ylabel("Số sinh viên đạt")

plt.show()