import numpy
from tkinter import *
from time import sleep

def GiaiPT():
    try:
        list1 = []
        list1.append([float(entry1.get()), float(entry2.get())])
        list1.append([float(entry3.get()), float(entry4.get())])
        
        A = numpy.array(list1)
        A1 = numpy.linalg.inv(A)

        list2 = [float(entry5.get()), float(entry6.get())]
        B = numpy.array(list2)
<<<<<<< HEAD
        # print(A)
        # print(B)
        X = numpy.dot(A1,B)
        
        # print(X)
        result.config(text="Result: {}".format(X))
=======
        X = numpy.dot(A1,B)
        result.config(text="Result: {}".format(X))
        """List3 = []
        List3.append([float(entry1.get()), float(entry2.get()), float(entry5.get())])
        List3.append([float(entry3.get()), float(entry4.get()), float(entry6.get())])
        C = numpy.array(List3)
        if(numpy.linalg.matrix_rank(A)<numpy.linalg.matrix_rank(C)):
            print("vo nghiem")
        else:
            if(numpy.linalg.matrix_rank(A)==numpy.linalg.matrix_rank(C)):
                X = numpy.dot(A1,B)
                result.config(text="Result: {}".format(X))
            else:
                print("vo so")"""
                

>>>>>>> f735587eb75a7e43f150c404364510ef81b2b139
        
    except ValueError:
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry4.delete(0, 'end')
        entry5.delete(0, 'end')
        entry6.delete(0, 'end')
        result.config(text="Vui Long Nhap So !!")
<<<<<<< HEAD
        
=======
>>>>>>> f735587eb75a7e43f150c404364510ef81b2b139

    

window = Tk()
window.geometry("1000x500")
window.title("Giai He Phuong Trinh N An")
window.configure(background="#EBE4D1")

content = Label(window, text="Ax + By = E\n Cx + Dy = F")
content.grid(row=0, column=0, padx=10, pady=10)

label1 = Label(window, text="Nhap A")
label1.grid(row=1, column=1, padx=10, pady=10)
label2 = Label(window, text="Nhap B")
label2.grid(row=1, column=2, padx=10, pady=10)
label3 = Label(window, text="Nhap C")
label3.grid(row=1, column=3, padx=10, pady=10)
label4 = Label(window, text="Nhap D")
label4.grid(row=1, column=4, padx=10, pady=10)

entry1 = Entry(window)
entry1.grid(row=2, column=1, padx=10, pady=10)
entry2 = Entry(window)
entry2.grid(row=2, column=2, padx=10, pady=10)
entry3 = Entry(window)
entry3.grid(row=2, column=3, padx=10, pady=10)
entry4 = Entry(window)
entry4.grid(row=2, column=4, padx=10, pady=10)


label5 = Label(window, text="Nhap E")
label5.grid(row=3, column=1, padx=10, pady=10)
label6 = Label(window, text="Nhap F")
label6.grid(row=3, column=2, padx=10, pady=10)

entry5 = Entry(window)
entry5.grid(row=4, column=1, padx=10, pady=10)
entry6 = Entry(window)
entry6.grid(row=4, column=2, padx=10, pady=10)

button = Button(window, text="Submit", command=GiaiPT)
button.grid(row=5, column=1, padx=10, pady=10)

result = Label(window, text="Result: ")
result.grid(row=6, column=1, padx=10, pady=10)


window.mainloop()


#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn

# A = np.array([(1,2),(3,4)])
# B = np.array([5,6])
# A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
# print(A)
# print(B)
# print(A1)
# X = np.dot(A1,B)
# print('Nghiem cua he:',X)
