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
        self.import_btn = ttk.Button(self.f1_left, text="Import Data")
        self.import_btn.grid(row=0, column=0, padx=5, pady=5)
        self.clean_data_btn = ttk.Button(self.f1_left, text="Clearn Data")
        self.clean_data_btn.grid(row=1, column=0, padx=5, pady=5)

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