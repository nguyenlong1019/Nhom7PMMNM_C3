from tkinter import *
from tkinter import ttk, filedialog, messagebox
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Analysis Application")
        self.root.geometry('1200x700')
        self.root.resizable(0, 0)
        self.make_center()

        #---------------------------------
        # Developed By Nguyen Van Long 
        #---------------------------------

        # style for all interfaces in project
        self.style = ttk.Style()

        # style name, options
        # Frame 1 Left
        self.style.configure(style="F1L.TFrame", background="#fff")
        # Frame 1 Right, Raw Data
        self.style.configure(style="F1R.RD.TFrame", background='#FFF7D4')

        # Frame 1 Left
        self.f1_left = ttk.Frame(self.root, style="F1L.TFrame")
        self.f1_left.place(x=0, y=0, width=200, height=700)
        
        # Button dùng để nhập file
        self.import_btn = ttk.Button(self.f1_left, text="Import Data")
        self.import_btn.place(x=10, y=10)
        
        # Button dùng để làm sạch data
        self.clean_data_btn = ttk.Button(self.f1_left, text="Clearn Data")
        self.clean_data_btn.place(x=10, y=50)

        self.style.configure(style="CC.TFrame", background='#F3F8FF')

        # Frame này để thực hiện khi người dùng muốn trực quan hóa dữ liệu,
        # Người dùng sẽ chọn các trường để phân tích
        self.choose_chart_frm = ttk.Frame(self.f1_left, style='CC.TFrame')
        self.choose_chart_frm.place(x=10, y=100, width=180, height=500)

        self.number_of_chart = ttk.Scale(self.choose_chart_frm, orient="horizontal", from_=1, to=10, command=self.on_scale_change)
        self.number_of_chart.place(x=5,y=5)
        self.number_of_chart_label = ttk.Label(self.choose_chart_frm, text="Charts: ")
        self.number_of_chart_label.place(x=5,y=35)
        self.create_form_btn = ttk.Button(self.choose_chart_frm, text="Create")
        self.create_form_btn.place(x=100, y=35)

        # KHOAI V
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################
        #######################################################

        # Button để quit app
        self.quit_btn = ttk.Button(self.f1_left, text="Quit", command='quit')
        self.quit_btn.place(x=10, y=660)
        
        # Button để gửi phản hồi về ứng dụng đến nhà phát triển
        self.feedback_btn = ttk.Button(self.f1_left, text="Feedback")
        self.feedback_btn.place(x=100, y=660)

        self.separator_left = ttk.Separator(self.f1_left, orient='vertical')
        self.separator_left.place(x=195, y=0, width=5, height=700)

        # Frame 2 Right
        self.f1_right = ttk.Frame(self.root)
        self.f1_right.place(x=200, y=0, width=1000, height=700)

        # Frame to contain the raw data table
        self.raw_data_frm = ttk.Frame(self.f1_right)
        self.raw_data_frm.place(x=0, y=0, width=1000, height=300)

        # selectmode = 'extended' enable choose multiple at a time
        self.raw_data_table = ttk.Treeview(self.raw_data_frm, selectmode='extended')
        self.raw_data_table.place(x=0, y=0, width=950, height=250)

        # Vertical Scrollbar
        self.v_scrollbar_rdt = ttk.Scrollbar(self.raw_data_frm, orient='vertical', command=self.raw_data_table.yview)
        self.raw_data_table.configure(yscrollcommand=self.v_scrollbar_rdt.set)
        self.v_scrollbar_rdt.place(x=950, y=0, width=50, height=250)

        # Horizontal Scrollbar
        self.h_scrollbar_rdt = ttk.Scrollbar(self.raw_data_frm, orient='horizontal', command=self.raw_data_table.xview)
        self.raw_data_table.configure(xscrollcommand=self.h_scrollbar_rdt.set)
        self.h_scrollbar_rdt.place(x=0,y=250, width=950, height=30)

        self.separator_rdt = ttk.Separator(self.raw_data_frm, orient='horizontal')
        self.separator_rdt.place(x=0, y=290, width=1000, height=10)

        # define number of columns, max columns = 10
        self.raw_data_table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

        # define heading
        self.raw_data_table["show"] = 'headings'

        # "n": hướng bắc (căn về phía bên trên)
        # "s": hướng nam (căn về phía bên dưới
        # "e": hướng đông (căn về phía bên phải)
        # "w": hướng tây (căn về phía bên trái)
        # "ne": hướng đông bắc (căn về phía trên bên phải)
        # "nw": hướng tây bắc (căn về phía trên bên trái)
        # "se": hướng đông nam (căn về phía dưới bên phải)
        # "sw": hướng tây nam (căn về phía dưới bên trái)
        # "c" hoặc "center": căn chính giữa
        self.raw_data_table.column("1", anchor='c')
        self.raw_data_table.column("2", anchor='c')
        self.raw_data_table.column("3", anchor='c')
        self.raw_data_table.column("4", anchor='c')
        self.raw_data_table.column("5", anchor='c')
        self.raw_data_table.column("6", anchor='c')
        self.raw_data_table.column("7", anchor='c')
        self.raw_data_table.column("8", anchor='c')
        self.raw_data_table.column("9", anchor='c')
        self.raw_data_table.column("10", anchor='c')

        self.raw_data_table.heading("1", text="")
        self.raw_data_table.heading("2", text="")
        self.raw_data_table.heading("3", text="")
        self.raw_data_table.heading("4", text="")
        self.raw_data_table.heading("5", text="")
        self.raw_data_table.heading("6", text="")
        self.raw_data_table.heading("7", text="")
        self.raw_data_table.heading("8", text="")
        self.raw_data_table.heading("9", text="")
        self.raw_data_table.heading("10", text="")

        for i in range(100):
            self.raw_data_table.insert(parent="", index="end", iid=f"item{i}", values=("", "", "", "", "", "", "", "", "", ""))
            pass

        # Frame to contain the clean data table
        self.clean_data_frm = ttk.Frame(self.f1_right)
        self.clean_data_frm.place(x=0, y=300, width=1000, height=400)

        self.clean_data_table = ttk.Treeview(self.clean_data_frm, selectmode='extended')
        self.clean_data_table.place(x=0, y=0, width=950, height=300)

        # Vertical Scrollbar
        self.v_scrollbar_cdt = ttk.Scrollbar(self.clean_data_frm, orient='vertical', command=self.clean_data_table.yview)
        self.clean_data_table.configure(yscrollcommand=self.v_scrollbar_cdt.set)
        self.v_scrollbar_cdt.place(x=950, y=0, width=50, height=300)

        # Horizontal Scrollbar
        self.h_scrollbar_cdt = ttk.Scrollbar(self.clean_data_frm, orient='horizontal', command=self.clean_data_table.xview)
        self.clean_data_table.configure(xscrollcommand=self.h_scrollbar_cdt.set)
        self.h_scrollbar_cdt.place(x=0,y=300, width=950, height=20)

        # define number of columns, max columns = 10
        self.clean_data_table["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

        # define heading
        self.clean_data_table["show"] = 'headings'

        self.clean_data_table.column("1", anchor='c')
        self.clean_data_table.column("2", anchor='c')
        self.clean_data_table.column("3", anchor='c')
        self.clean_data_table.column("4", anchor='c')
        self.clean_data_table.column("5", anchor='c')
        self.clean_data_table.column("6", anchor='c')
        self.clean_data_table.column("7", anchor='c')
        self.clean_data_table.column("8", anchor='c')
        self.clean_data_table.column("9", anchor='c')
        self.clean_data_table.column("10", anchor='c')

        self.clean_data_table.heading("1", text="")
        self.clean_data_table.heading("2", text="")
        self.clean_data_table.heading("3", text="")
        self.clean_data_table.heading("4", text="")
        self.clean_data_table.heading("5", text="")
        self.clean_data_table.heading("6", text="")
        self.clean_data_table.heading("7", text="")
        self.clean_data_table.heading("8", text="")
        self.clean_data_table.heading("9", text="")
        self.clean_data_table.heading("10", text="")

        for i in range(100):
            self.clean_data_table.insert(parent="", index="end", iid=f"item{i}", values=("", "", "", "", "", "", "", "", "", ""))
            pass

        # Button để chuyển sang trang trực quan hóa dữ liệu
        self.visualization_btn = ttk.Button(self.clean_data_frm, text="Visualization")
        self.visualization_btn.place(x=10, y=360)

        # Button để download clean data
        self.download_clean_data = ttk.Button(self.clean_data_frm, text="Download Clean Data")
        self.download_clean_data.place(x=100, y=360)


    def on_scale_change(self,value):
        print(f"Giá trị: {int(float(value))}")
        self.number_of_chart_label.configure(text=f"Charts: {int(float(value))}")
    

        #---------------------------------
        # Developed By Nguyen Van Long 
        #---------------------------------
    
        #--------------------------------- 
        # Test Code From Nguyen Van Long
        #---------------------------------
        '''
        self.style = ttk.Style()
        self.style.configure(style="LS.TFrame", background="yellow")
        self.style.configure(style="RS.TFrame", background="red")
        self.style.configure(style="T.TFrame", background="blue")
        self.style.configure(style="B.TFrame", background="pink")

        self.left_side = ttk.Frame(self.root, style="LS.TFrame")
        self.left_side.place(x = 0, y = 0, width=200, height=700)

        # self.txt = ttk.Label(self.left_side, text="Hello")
        # self.txt.grid(row=0, column=0, padx=5, pady=5)

        self.right_side = ttk.Frame(self.root, style="RS.TFrame")
        self.right_side.place(x = 200, y = 0, width=1000, height=700)

        self.top_part = ttk.Frame(self.right_side, style="T.TFrame")
        self.top_part.place(x = 0, y = 0, width=1000, height=300)

        self.raw_data_sheet = ttk.Treeview(self.right_side)
        self.raw_data_sheet.grid(row=0, column=0, padx=5, padx=5)

        self.bottom_part = ttk.Frame(self.right_side, style="B.TFrame")
        self.bottom_part.place(x = 0, y = 300, width=1000, height=400)


        print(f"{self.root.winfo_height()} {self.root.winfo_width()}")
        '''


        '''
        Developed by Nguyen Van Long


        self.style = ttk.Style()
        self.style.configure(style="F1.TFrame", background='black')
        self.style.configure(style="F2.TFrame", background='yellow')
        self.style.configure(style="F3.TFrame", background='blue')

        self.f1_left = ttk.Frame(self.root, style="F1.TFrame")
        self.f1_left.place(x=0, y=0, width=200, height=700)

        self.f2_left = ttk.Frame(self.root, style="F2.TFrame")
        #self.f2_left.place(x=0, y=0, width=200, height=700)

        self.f3_left = ttk.Frame(self.root, style="F3.TFrame")
        #self.f3_left.place(x=0, y=0, width=200, height=700)

        self.current_frame = self.f1_left

        self.btn_sw = ttk.Button(self.root, text="Switch", command=self.switch_frames)
        self.btn_sw.place(x=300, y=300)


    def switch_frames(self):
        if self.current_frame == self.f1_left:
            self.f1_left.place_forget()
            self.f3_left.place_forget()
            self.f2_left.place(x=0, y=0, width=200, height=700)
            self.current_frame = self.f2_left
        elif self.current_frame == self.f2_left:
            self.f1_left.place_forget()
            self.f2_left.place_forget()
            self.f3_left.place(x=0, y=0, width=200, height=700)
            self.current_frame = self.f3_left
        elif self.current_frame == self.f3_left:
            self.f2_left.place_forget()
            self.f3_left.place_forget()
            self.f1_left.place(x=0, y=0, width=200, height=700)
            self.current_frame = self.f1_left


        '''



    def make_center(self):
        self.root.update_idletasks()
        width = self.root.winfo_width() # width of root
        height = self.root.winfo_height() # height of root

        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)

        self.root.geometry(f"{width}x{height}+{x}+{y}")
        return


if __name__ == '__main__':
    app = App()
    app.root.mainloop()