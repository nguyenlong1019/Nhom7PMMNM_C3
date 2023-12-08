'''
ttk : themed tkinter
là gói giao diện hiện đại trong tkinter

các ttk từ widgets cũ gồm Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton,
Scale, Scrollbar, Spinbox

sử dụng ttk.Style() để thay đổi style cho các widget thay vì các thuộc tính cũ của widget như bg, fg,...

ttk đi kèm với 18 widgets (tiện ích): gồm 12 cái cũ như trên và 6 cái mới: Combobox, Notebook, Progressbar, Separator,
Sizegrip và Treeview. 

ví dụ ttk code:

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")

Các widget chấp nhận các option tiêu chuẩn sau: 
class: chỉ định window class (thường là root)
cursor: chỉ định con trỏ chuột cho tiện ích
takefocus: chấp nhận tiêu điểm trong quá trình di chuyển bằng bàn phím hay không? 1 là có, 0 là không
style: style cho widget

Các tiện ích hỗ trợ điều khiển bằng thanh cuộn (Scrollbar) có các option
xscrollcommand: sử dụng thanh cuộn ngang (bao gồm Scrollbar.set())
yscrollcommand: sử dụng thanh cuộn dọc

Việc sử dụng các biến trong tkinter thích hợp hơn là fixed cứng

# https://docs.python.org/3/library/tkinter.ttk.html#module-tkinter.ttk
tham khảo thêm các option tại đường dẫn trên (python 3.10.7)

Đối với các Widget thì có 2 điều cần quan tâm là options (tham số, thuộc tính tùy chọn) và events (sự kiện trên widget)

Combobox: danh sách thả xuống
Spinbox: Entry cho phép chọn giá trị có sẵn (tăng giảm như tăng giảm tuổi,...)
Notebook: quản lý các collection window và hiển thị từng cửa sổ 1. Sử dụng notebook cho chuyển tab quá hay :)
Mỗi cửa sổ con được liên kết với 1 tab

Progressbar: hiện thị trạng thái, nó giống thanh tiến trình đã được bao nhiêu %, ...

Separator: hiển thị các thanh phân cách ngang dọc, có thể dùng để tạo lưới nhưng mà thôi Treeview ngon hơn :)

Sizegrip: còn được gọi là a grow box: cho phép người dùng thay đổi kích thước cửa sổ Toplevel bằng cách drag
Sizegrip còn bug: tiện ích chỉ hỗ trợ thay đổi kích thước đông nam (south east), 
Nếu vị trí của cấp trên cùng  (toplevel) được chỉ định so với bên phải hoặc dưới cùng của màn hình (ví dụ: ….), 
tiện ích Sizegrip sẽ không thay đổi kích thước cửa sổ.

Treeview: dạng bảng excel

Style: cách dùng tối ưu của style. Ngon khi dùng trong menu :)

Tiếp theo là các ví dụ widget mới
'''

# đến bài Add style to Button