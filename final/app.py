from tkinter import *
from tkinter import ttk, filedialog, messagebox


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Analysis Application")
        self.root.geometry('1200x700')
        self.root.resizable(0, 0)
        self.make_center()
    
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

        self.f1_left = ttk.Frame(self.root)

        self.f2_left = ttk.Frame(self.root)

        self.f3_left = ttk.Frame(self.root)

        self.current_frame = self.frame1


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