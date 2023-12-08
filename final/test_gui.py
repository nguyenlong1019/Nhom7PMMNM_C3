# file này để thử nghiệm các giao diện


import tkinter as tk

class SwitchFramesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Switch Frames Example")
        self.master.geometry("400x300")

        self.frame1 = tk.Frame(self.master, bg="lightblue", width=400, height=300)
        self.frame1.place(x=0, y=0, relwidth=1, relheight=1)
        label1 = tk.Label(self.frame1, text="Frame 1 Content", font=("Helvetica", 14))
        label1.place(relx=0.5, rely=0.5, anchor="center")

        self.frame2 = tk.Frame(self.master, bg="lightgreen", width=400, height=300)
        label2 = tk.Label(self.frame2, text="Frame 2 Content", font=("Helvetica", 14))
        label2.place(relx=0.5, rely=0.5, anchor="center")

        self.current_frame = self.frame1

        self.switch_button = tk.Button(self.master, text="Switch Frames", command=self.switch_frames)
        self.switch_button.place(x=10, y=10)

    def switch_frames(self):
        if self.current_frame == self.frame1:
            self.frame1.place_forget()
            self.frame2.place(x=0, y=0, relwidth=1, relheight=1)
            self.current_frame = self.frame2
        else:
            self.frame2.place_forget()
            self.frame1.place(x=0, y=0, relwidth=1, relheight=1)
            self.current_frame = self.frame1

if __name__ == "__main__":
    root = tk.Tk()
    app = SwitchFramesApp(root)
    root.mainloop()
