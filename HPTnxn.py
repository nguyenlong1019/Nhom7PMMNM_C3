#Bài toán yêu cầu giải hệ phương trình n ẩn n phương trình
import numpy as np
import tkinter as tk
from tkinter import messagebox, ttk

def GIAI_PT():
    num_variables = int(num_variables_entry.get())

    if num_variables < 2:
        messagebox.showerror("Error", "Nhập số ẩn lớn hơn 1.")
        return

    coefficients = []
    constants = []

    for i in range(num_variables):
        equation_coeffs = []
        for j in range(num_variables):
            coeff = float(entry_vars[j][i].get())
            equation_coeffs.append(coeff)
        equation_const = float(const_vars[i].get())
        coefficients.append(equation_coeffs)
        constants.append(equation_const)

    try:
        A = np.array(coefficients)
        B = np.array(constants)
        rank_A = np.linalg.matrix_rank(A)
        rank_A1 = np.linalg.matrix_rank(np.column_stack((A, B)))

        if rank_A < rank_A1:
            messagebox.showinfo("Nghiệm", "Hệ phương trình vô nghiệm.")
        elif rank_A == rank_A1 and rank_A < num_variables:
            messagebox.showinfo("Nghiệm", "Hệ phương trình vô số nghiệm.")
        else:
            solution = np.linalg.solve(coefficients_matrix, B)
            messagebox.showinfo("Nghiệm", f"Nghiệm của hệ phương trình là: {solution}")
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "Xảy ra lỗi khi giải hệ phương trình.")

def Tao_Bang():
    num_variables = int(num_variables_entry.get())

    if num_variables < 2:
        messagebox.showerror("Error", "Nhập số ẩn lớn hơn 1.")
        return

    # Clear previous inputs
    for frame in equation_frame.winfo_children():
        frame.destroy()

    entry_vars.clear()
    const_vars.clear()

    # Create input fields for coefficients and constants
    for i in range(num_variables):
        entry_frame = ttk.Frame(equation_frame)
        entry_frame.grid(row=i, column=0, padx=5, pady=5)

        const_frame = ttk.Frame(equation_frame)
        const_frame.grid(row=i, column=1, padx=5, pady=5)

        equation_coeffs = []
        for j in range(num_variables):
            coeff_entry = ttk.Entry(entry_frame, width=8)
            coeff_entry.grid(row=i, column=j, padx=3, pady=3)
            equation_coeffs.append(coeff_entry)

        constant_entry = ttk.Entry(const_frame, width=8)
        constant_entry.grid(row=i, column=0, padx=3, pady=3)

        entry_vars.append(equation_coeffs)
        const_vars.append(constant_entry)

def Xoa_ALL():
    for equation_coeffs in entry_vars:
        for coeff_entry in equation_coeffs:
            coeff_entry.delete(0, tk.END)

    for constant_entry in const_vars:
        constant_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Linear Equations Solver")

# Number of variables input
num_variables_label = ttk.Label(root, text="Số ẩn:")
num_variables_label.pack(padx=5, pady=5)

num_variables_entry = ttk.Entry(root, width=5)
num_variables_entry.pack(padx=5, pady=5)

create_button = ttk.Button(root, text="Tạo bảng", command=Tao_Bang)
create_button.pack(padx=5, pady=5)

# Equation input fields
equation_frame = ttk.Frame(root)
equation_frame.pack(padx=5, pady=5)

entry_vars = []
const_vars = []

solve_button = ttk.Button(root, text="Giải", command=GIAI_PT)
solve_button.pack(padx=5, pady=5)

clear_button = ttk.Button(root, text="Clear All", command=Xoa_ALL)
clear_button.pack(padx=5, pady=5)

root.mainloop()
