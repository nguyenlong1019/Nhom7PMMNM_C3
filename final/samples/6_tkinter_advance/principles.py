'''
winfo_screenheight() // Returns screen height in pixels

winfo_screenmmheight() // Returns screen height in mm

winfo_screenwidth() // Returns screen width in pixels

winfo_screenmmwidth() // Returns screen width in mm


thay đổi text của label động bằng cách sử dụng biến ví dụ StringVar

đặt tiêu điểm vào widget

search string in text (có thể dùng như ctr + f để tìm text(highlight))

auto complete combobox (nên dùng trong BTL trong search :)

auto hidden scrollbar sẽ sử dụng khi kích thước cửa sổ thay đổi lớn hơn

xác thực trường văn bản để tránh người dùng nhập các giá trị không mong muốn ví dụ chỉ cho nhập số thì k đc nhập chữ
và cố tình nhập chữ vào cũng không có tác dụng.

biến trong tkinter dùng để lưu trữ và theo dõi dữ liệu động

các loại biến trong tkinter:
BooleanVar()
StringVar()
IntVar()
DoubleVar()

syntax:
var = Tkinter_variable(master, value = any_value)
https://www.geeksforgeeks.org/python-setting-and-retrieving-values-of-tkinter-variable/

sử dụng set() và get() với biến



adding style for ttk.Entry()
https://www.geeksforgeeks.org/tkinter-adding-style-to-the-input-text-using-ttk-entry-widget/



after() method in tkinter: hàm cho phép lên lịch gọi 1 hàm sau một khoảng thời gian nhất định
after(parent, ms, function = None, *args)
Parameters: 
parent: is the object of the widget or main window whichever is using this function. 
ms: is the time in milliseconds. 
function: which shall be called. 
*args: other options.

ví dụ sử dụng: tắt ứng dụng sau 1 khoảng thời gian nhất định, 

universal function (hàm phổ quát, hàm toàn cầu): hàm được thiết kế để hoạt động với nhiều loại dữ liệu khác nhau



destroy(): destroy để phá hủy ứng dụng (tắt ứng dụng)


Text detection sử dụng nltk, pandas, numpy, matplotlib để phân tích câu nhập vào


Kiểm tra một đối tượng có được hiển thị hay không?
winfo_ismaped(): phương thức này kiểm tra xem tiện tích có được hiển thị hay không?, phương thức này nó nâng cao
và kiểm soát theo quy tắc của tkinter chứ không theo quy tắc suy luận thông thường.
đọc thêm tại:
https://www.geeksforgeeks.org/python-winfo_ismapped-and-winfo_exist-in-tkinter/

winfo_exists(): kiểm tra xem tiện ích được chỉ định có tồn tại hay không? tức là tiện ích có bị hủy không?
Code sẽ hiểu đọc k hiểu được đâu :), chưa dùng nên chịu


Collapse: https://www.geeksforgeeks.org/collapsible-pane-in-tkinter-python/


Chọn nhiều lựa chọn cùng lúc: https://www.geeksforgeeks.org/creating-a-multiple-selection-using-tkinter/


Mã hóa sử dụng module có sẵn:
https://www.geeksforgeeks.org/cryptography-gui-using-python/

'''







# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import time

# toplevel window
root = Tk()

def forget(widget):
	widget.forget()
	print("After Forget method called. Is widget mapped? = ",
							bool(widget.winfo_ismapped()))

def retrieve(widget):
	widget.pack()
	print("After retrieval of widget. Is widget mapped? = ",
								bool(widget.winfo_ismapped()))

# Button widgets
b1 = Button(root, text = "Btn 1")
b1.pack()

# This is used to make widget invisible
b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
b2.pack()

# This will retrieve widget
b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1))
b3.pack()

# infinite loop, interrupted by keyboard or mouse
mainloop()
