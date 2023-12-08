'''
Binding Functions in Tkinter (liên kết hàm đến widget, hàm để xử lý các sự kiện (event))
có thể liên kết hàm và phương thức của Python với một sự kiện trên tiện ích (widget)

Ví dụ có thể liên kết các sự kiện di chuột vào, ra khỏi đối tượng
Sự kiện chuột click (chuột phải trái, double click), sự kiện bàn phím

cú pháp binding functions và widget
widget.bind(event, handler)

list events in tkinter
https://manpages.debian.org/bookworm/tk8.6-doc/bind.3tk.en.html


Một số event thường dùng

Sự kiện Chuột:

<Button-1>: Click chuột trái.
<Button-2>: Click nút trung (nếu có).
<Button-3>: Click chuột phải.
<B1-Motion>: Di chuyển chuột khi giữ nút trái.
<Enter>: Di chuyển chuột vào widget.
<Leave>: Di chuyển chuột ra khỏi widget.
Sự kiện Phím:

<KeyPress>: Bất kỳ phím nào được nhấn.
<KeyRelease>: Bất kỳ phím nào được nhả ra sau khi đã được nhấn.
<Key>: Sự kiện cụ thể cho một phím cụ thể (ví dụ: <KeyPress-a>).
Sự kiện Cửa sổ:

<Configure>: Khi cỡ của cửa sổ thay đổi.
<FocusIn> và <FocusOut>: Khi widget nhận hoặc mất focus.
Sự kiện Thời gian:

<Motion>: Sự kiện xảy ra khi di chuyển chuột.
<ButtonPress> và <ButtonRelease>: Sự kiện xảy ra khi một nút chuột được nhấn hoặc nhả ra.
Sự kiện Mô-đun:

<Control-KeyPress>: Khi bất kỳ phím nào được nhấn và đồng thời giữ phím Control.
Sự kiện Chuột vào/huỷ chọn:

<Enter> và <Leave>: Khi chuột vào hoặc rời khỏi widget.
'''

import tkinter as tk

def on_button_click(event):
    print("Button clicked")

root = tk.Tk()

button = tk.Button(root, text="Click me")
button.pack()

# Liên kết sự kiện chuột click với hàm on_button_click
button.bind("<Button-1>", on_button_click)

root.mainloop()
