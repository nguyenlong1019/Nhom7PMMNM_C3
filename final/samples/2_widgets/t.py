from pulp import *

def solve_transportation_problem(A, B, C, don_hang_tai_kho, chi_phi_van_chuyen, phat_het_hang, cam_duong):
    # Tạo mô hình tối ưu
    model = LpProblem("TransportationProblem", LpMinimize)

    # Tạo biến quyết định
    x = LpVariable.dicts("x", ((i, j) for i in range(B) for j in range(A)), 0, None, LpInteger)

    # Hàm mục tiêu
    model += lpSum([x[i, j] * chi_phi_van_chuyen[i][j] for i in range(B) for j in range(A)])

    # Ràng buộc
    for i in range(B):
        model += lpSum([x[i, j] for j in range(A)]) <= C

    for j in range(A):
        model += lpSum([x[i, j] for i in range(B)]) >= don_hang_tai_kho[j]

    # Tình huống phát hết hàng
    if phat_het_hang:
        for i in range(B):
            model += lpSum([x[i, j] for j in range(A)]) == C

    # Đường đang bị cấm
    if cam_duong:
        for j in cam_duong:
            model += lpSum([x[i, j] for i in range(B)]) == 0

    # Giải bài toán
    model.solve()

    # In kết quả
    print(f"Status: {LpStatus[model.status]}")
    for i in range(B):
        for j in range(A):
            print(f"Nhan vien {i+1} giao {int(value(x[i, j]))} don hang tai kho {j+1}")

    print(f"Chi phi toi uu: {value(model.objective)}")

# Dữ liệu đầu vào
A = 3  # Số lượng kho hàng
B = 2  # Số lượng nhân viên giao hàng
C = 2  # Số lượng đơn hàng mỗi nhân viên
don_hang_tai_kho = [3, 4, 2]  # Số lượng đơn hàng tại mỗi kho
chi_phi_van_chuyen = [
    [2, 4, 1],  # Chi phí vận chuyển từ nhân viên i đến kho j
    [3, 1, 5],
]

# Phát hết hàng
phat_het_hang = True

# Đường đang bị cấm
cam_duong = [2]

# Giải bài toán
solve_transportation_problem(A, B, C, don_hang_tai_kho, chi_phi_van_chuyen, phat_het_hang, cam_duong)
