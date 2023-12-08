from tkinter import *
from tkinter import ttk, filedialog, messagebox


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Analysis Application")
        self.root.geometry('1200x600')
        self.root.resizable(0, 0)
        self.make_center()

        


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