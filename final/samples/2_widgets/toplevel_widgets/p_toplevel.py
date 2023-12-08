'''
Dùng để tạo một cửa sổ (window) nẳm trên tất cả các cửa sổ window khác.
Dùng để cung cấp một số thông tin bổ sung cho người dùng

toplevel = Toplevel(root, bg, fg, bd, height, width, font, ..)

Optional parameters :
    root = root window(optional) 
    bg = background colour 
    fg = foreground colour 
    bd = border 
    height = height of the widget. 
    width = width of the widget. 
    font = Font type of the text. 
    cursor = cursor that appears on the widget which can be an arrow, a dot etc. 

Common methods:
    iconify: turns the windows into icon. (biến cửa sổ thành biểu tượng)
    deiconify: turns back the icon into window. (biến biểu tượng thành cửa sổ)
    state: returns the current state of window. (trả về trạng thái hiện tại của cửa số, ví dụ có thể dùng để đóng mở, kiểm tra đóng mở)
    withdraw: removes the window from the screen. (xóa cửa sổ khỏi màn hình)
    title: defines title for window.
    frame: returns a window identifier which is system specific. (trả về mã định danh cửa sổ dành riêng cho hệ thống)

https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/
'''

