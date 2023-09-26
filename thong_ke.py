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
plt.pie(dulieusosanh, labels=kieusosanh,explode=myexplode, autopct='%1.1f%%')
plt.axis('equal') 


maxa = diemA.max()
i, = np.where(diemA == maxa)
print("=========")
print('lop co nhieu diem A la {0} co {1} sv dat diem A'.format(in_data[i,0],maxa))
fig2 = plt.figure()
plt.plot(range(len(diemA)),diemA,'r-',label="Diem A")
plt.plot(range(len(diemBc)),diemBc,'g-',label="Diem B +")
plt.xlabel('Lơp')
plt.ylabel(' So sv dat diem ')
plt.legend(loc='upper right')
plt.show()

      





