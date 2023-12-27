from tkinter import *
from tkinter import ttk

# nên học về binding functions để hiểu hơn về sự kiện (events)
def on_tab_selected(event):
    selected_tab = notebook.index(notebook.select())
    print(f"Tab {selected_tab + 1} selected")


root = Tk()
root.title("Notebook")

# tạo đối tượng Notebook
notebook = ttk.Notebook(root)

# tạo các tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# thêm các tab vào notebook
# notebook.add(tab1, text="Tab 1")
# notebook.add(tab2, text="Tab 2")
# notebook.add(tab3, text="Tab 3")

notebook.add(tab1)
notebook.add(tab2)
notebook.add(tab3)

# đặt sự kiện khi tab được chọn
notebook.bind("<<NotebookTabChanged>>", on_tab_selected)

# Label và Button trong Tab 1
label1 = ttk.Label(tab1, text="This is Tab 1")
label1.pack(padx=10, pady=10)
button1 = ttk.Button(tab1, text="Click Me")
button1.pack(padx=10, pady=10)

# Entry và Checkbox trong Tab 2
entry2 = ttk.Entry(tab2)
entry2.pack(padx=10, pady=10)
checkbox2 = ttk.Checkbutton(tab2, text="Check Me")
checkbox2.pack(padx=10, pady=10)

# Text và Combobox trong Tab 3
text3 = Text(tab3, width=40, height=10)
text3.pack(padx=10, pady=10)
combobox3 = ttk.Combobox(tab3, values=["Option 1", "Option 2", "Option 3"])
combobox3.pack(padx=10, pady=10)

# Hiển thị Notebook
notebook.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()