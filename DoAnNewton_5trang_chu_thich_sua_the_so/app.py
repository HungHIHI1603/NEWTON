import tkinter as tk
from tkinter import ttk, messagebox
import math
from data import (
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    TAYLOR, HAM_XAP_XI, DIEU_KIEN, NEWTON, KY_HIEU,
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    UNG_DUNG_TEN, UNG_DUNG_GIAI_THICH, UNG_DUNG_HAM,
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    UNG_DUNG_DAO_HAM_1, UNG_DUNG_DAO_HAM_2, UNG_DUNG_LIEN_HE
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)
# Tác dụng: Nhập các hàm hoặc thành phần cần dùng từ mô-đun khác.
from model import tinh_newton, tao_ham


# Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
def fmt(value):
    # Tác dụng: Trả kết quả của hàm về nơi gọi.
    return f"{value:.8g}"


def ve_do_thi(canvas, expression, x0, x_star, variable="x",
              # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
              positive=False, iterations=None, volume=None):
    """Ve do thi ham muc tieu, diem dau va diem toi uu."""
    canvas.delete("all")
    # Tác dụng: Gọi chức năng của thư viện giao diện để hiển thị hoặc xử lý thao tác người dùng.
    canvas.update_idletasks()
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    width = max(canvas.winfo_width(), 720)
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    height = max(canvas.winfo_height(), 320)

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    _, _, _, f, _, _ = tao_ham(
        expression, variable, "positive" if positive else None
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    lo = min(x0, x_star) - 2.5
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    hi = max(x0, x_star) + 2.5
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if positive:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        lo = max(0.05, min(x0, x_star) * 0.35)
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        hi = max(x0, x_star) * 1.6 + 0.5
    # Tác dụng: Kiểm tra điều kiện tiếp theo nếu nhánh trước không đúng.
    elif hi - lo < 5:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        mid = (lo + hi) / 2
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        lo, hi = mid - 2.5, mid + 2.5

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    xs = [lo + (hi - lo) * i / 350 for i in range(351)]
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    ys = []
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for value in xs:
        # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
        try:
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            y = float(f(value))
            ys.append(y if math.isfinite(y) else float("nan"))
        # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
        except Exception:
            ys.append(float("nan"))
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    valid = [y for y in ys if math.isfinite(y)]
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if len(valid) < 2:
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        return

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    ymin, ymax = min(valid), max(valid)
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if ymax - ymin < 1e-12:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        ymin -= 1
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        ymax += 1
    # Tác dụng: Thực hiện nhánh thay thế khi các điều kiện trước không đúng.
    else:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        pad = (ymax - ymin) * 0.12
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        ymin -= pad
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        ymax += pad

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    left, right, top, bottom = 70, 25, 35, 48

    # Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
    def px(value):
        # Tác dụng: Trả kết quả của hàm về nơi gọi.
        return left + (value - lo) / (hi - lo) * (width - left - right)

    # Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
    def py(value):
        # Tác dụng: Trả kết quả của hàm về nơi gọi.
        return height - bottom - (value - ymin) / (ymax - ymin) * (height - top - bottom)

    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for i in range(6):
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        xv = lo + (hi - lo) * i / 5
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        yv = ymin + (ymax - ymin) * i / 5
        canvas.create_line(px(xv), py(ymin), px(xv), py(ymax), fill="#e4e8ee")
        canvas.create_text(px(xv), height - 22, text=f"{xv:.3g}", font=("Arial", 8))
        canvas.create_line(px(lo), py(yv), px(hi), py(yv), fill="#e4e8ee")
        canvas.create_text(34, py(yv), text=f"{yv:.3g}", font=("Arial", 8))

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    points = []
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for xv, yv in zip(xs, ys):
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if math.isfinite(yv):
            # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
            points.extend((px(xv), py(yv)))
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if len(points) >= 4:
        canvas.create_line(*points, fill="#1769aa", width=2, smooth=True)

    # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
    try:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        y0 = float(f(x0))
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        ys_star = float(f(x_star))
        # Tác dụng: Vẽ thành phần đồ họa lên vùng Canvas.
        canvas.create_oval(px(x0)-6, py(y0)-6, px(x0)+6, py(y0)+6,
                           fill="#f59e0b", outline="")
        # Tác dụng: Vẽ thành phần đồ họa lên vùng Canvas.
        canvas.create_text(px(x0), py(y0)-18, text=f"x₀={fmt(x0)}",
                           fill="#9a5b00", font=("Arial", 9, "bold"))
        # Tác dụng: Vẽ thành phần đồ họa lên vùng Canvas.
        canvas.create_oval(px(x_star)-7, py(ys_star)-7, px(x_star)+7, py(ys_star)+7,
                           fill="#dc2626", outline="")
        # Tác dụng: Vẽ thành phần đồ họa lên vùng Canvas.
        canvas.create_text(px(x_star)+45, py(ys_star)-18, text=f"x*={fmt(x_star)}",
                           fill="#b91c1c", font=("Arial", 9, "bold"))
    # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
    except Exception:
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        pass

    # Tác dụng: Vẽ thành phần đồ họa lên vùng Canvas.
    canvas.create_text(width/2, 14, text=f"Đồ thị hàm mục tiêu theo biến {variable}",
                       font=("Arial", 10, "bold"))


# Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
def fill_tree(tree, rows, headers):
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for item in tree.get_children():
        # Tác dụng: Xóa nội dung cũ trước khi hiển thị nội dung mới.
        tree.delete(item)
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for row in rows:
        tree.insert("", "end", values=row)


# Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
def run_general():
    # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
    try:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        expr = general_expr.get().strip()
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        x0 = float(general_x0.get())
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        rows, steps, f1_sym, f2_sym = tinh_newton(expr, x0, max_lap=60)
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        _, _, _, f, f1, f2 = tao_ham(expr)
    # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
    except Exception as exc:
        messagebox.showerror("Không tính được", str(exc))
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        return

    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    fill_tree(general_table, [
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        (k, fmt(x), fmt(fx), fmt(d1), fmt(d2))
        # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
        for k, x, fx, d1, d2 in rows
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    ], None)

    # Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
    general_derivatives.config(
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        text=f"f(x) = {expr}\nf'(x) = {f1_sym}\nf''(x) = {f2_sym}"
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )
    general_steps.delete("1.0", "end")
    general_steps.insert("end", "ÁP DỤNG CÔNG THỨC NEWTON THEO SLIDE\n")
    general_steps.insert("end", NEWTON + "\n\n")
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for step in steps:
        general_steps.insert("end", step + "\n")
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    k, x_star, fx_star, d1, d2 = rows[-1]
    # Tác dụng: Đưa nội dung mặc định hoặc kết quả vào thành phần giao diện.
    general_steps.insert(
        "end",
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        f"\nKẾT QUẢ\nx* ≈ {fmt(x_star)}\nf(x*) ≈ {fmt(fx_star)}"
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        f"\nf'(x*) ≈ {fmt(d1)}\nf''(x*) ≈ {fmt(d2)}\n"
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if abs(d1) <= 1e-6 and d2 > 0:
        general_steps.insert("end", "Kết luận: đạt điều kiện cực tiểu địa phương.\n")
    # Tác dụng: Thực hiện nhánh thay thế khi các điều kiện trước không đúng.
    else:
        general_steps.insert("end", "Chưa đủ điều kiện kết luận cực tiểu tại điểm dừng.\n")

    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    ve_do_thi(general_chart, expr, x0, x_star)
    # Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
    general_status.config(text=f"Đã tính xong: x* ≈ {fmt(x_star)}; f(x*) ≈ {fmt(fx_star)}")


# Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
def run_application():
    # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
    try:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        volume = float(volume_entry.get())
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        r0 = float(radius_entry.get())
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if volume <= 0:
            raise ValueError("Thể tích V phải lớn hơn 0.")
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if r0 <= 0:
            raise ValueError("Bán kính ban đầu r₀ phải lớn hơn 0.")

        # Dien tich toan phan hinh tru, giu the tich V co dinh.
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        expression = f"2*pi*r**2 + 2*({volume})/r"
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        rows, steps, f1_sym, f2_sym = tinh_newton(
            expression, r0, bien="r", max_lap=60, positive=True
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        )
        _, _, _, area, d1, d2 = tao_ham(expression, "r", "positive")
    # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
    except Exception as exc:
        messagebox.showerror("Không tính được ứng dụng", str(exc))
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        return

    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    fill_tree(application_table, [
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        (k, fmt(r), fmt(s), fmt(d1v), fmt(d2v))
        # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
        for k, r, s, d1v, d2v in rows
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    ], None)

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    k, r_star, s_star, d1_star, d2_star = rows[-1]
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    height_cylinder = volume / (math.pi * r_star**2)
    # Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
    application_result.config(
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        text=(
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            f"Bán kính tối ưu r* = {fmt(r_star)} cm\n"
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            f"Chiều cao tương ứng h = {fmt(height_cylinder)} cm\n"
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            f"Diện tích vật liệu nhỏ nhất S(r*) = {fmt(s_star)} cm²\n"
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            f"S'(r*) = {fmt(d1_star)}; S''(r*) = {fmt(d2_star)}"
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        )
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )

    application_steps.delete("1.0", "end")
    application_steps.insert("end", "BÀI TOÁN ỨNG DỤNG: TIẾT KIỆM VẬT LIỆU LÀM HỘP TRỤ\n\n")
    application_steps.insert("end", f"Thể tích cố định V = {fmt(volume)} cm³\n")
    application_steps.insert("end", "Hàm mục tiêu:\nS(r) = 2*pi*r² + 2*V/r\n")
    application_steps.insert("end", "Đạo hàm bậc nhất:\nS'(r) = 4*pi*r - 2*V/r²\n")
    application_steps.insert("end", "Đạo hàm bậc hai:\nS''(r) = 4*pi + 4*V/r³\n\n")
    application_steps.insert("end", "Công thức Newton đúng theo slide:\n" + NEWTON.replace("x", "r") + "\n\n")
    application_steps.insert("end", "THẾ SỐ TỪNG LẦN LẶP\n")
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for step in steps:
        application_steps.insert("end", step.replace("x_", "r_") + "\n")
    application_steps.insert("end", "\nKẾT QUẢ VÀ Ý NGHĨA\n")
    # Tác dụng: Đưa nội dung mặc định hoặc kết quả vào thành phần giao diện.
    application_steps.insert(
        "end",
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        f"Với V = {fmt(volume)} cm³, bán kính tối ưu là {fmt(r_star)} cm.\n"
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        f"Chiều cao tương ứng là {fmt(height_cylinder)} cm.\n"
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        f"Diện tích vật liệu nhỏ nhất là {fmt(s_star)} cm².\n"
        "Điều này giúp chọn kích thước hộp trụ dùng ít vật liệu nhất khi thể tích không đổi.\n"
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )

    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    ve_do_thi(
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        application_chart, expression, r0, r_star,
        variable="r", positive=True
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )
    # Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
    application_status.config(
        text="Đã hoàn tất: giữ nguyên thể tích, Newton tìm bán kính làm diện tích vật liệu nhỏ nhất."
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )


# Tác dụng: Định nghĩa hàm; phần thân bên dưới thực hiện chức năng được nêu trong tên hàm.
def compare_starts():
    # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
    try:
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        expr = general_expr.get().strip()
        starts = [float(v.strip()) for v in compare_entry.get().split(",") if v.strip()]
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if not starts:
            raise ValueError("Nhập các giá trị x₀, ví dụ: -2, 0, 5.")
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if len(starts) > 8:
            raise ValueError("Chỉ nhập tối đa 8 giá trị.")
    # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
    except Exception as exc:
        messagebox.showerror("Dữ liệu chưa đúng", str(exc))
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        return

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    output = []
    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for x0 in starts:
        # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
        try:
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            rows, _, _, _ = tinh_newton(expr, x0, max_lap=60)
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            k, xstar, fx, d1, d2 = rows[-1]
            note = "Cực tiểu địa phương" if abs(d1) <= 1e-6 and d2 > 0 else "Cần kiểm tra thêm"
            # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
            output.append((fmt(x0), fmt(xstar), fmt(fx), len(rows)-1, note))
        # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
        except Exception as exc:
            output.append((fmt(x0), "—", "—", "—", str(exc)[:30]))
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    fill_tree(compare_table, output, None)
    # Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
    compare_note.config(
        text="Mỗi dòng là một lần chạy riêng. Hàm mục tiêu và công thức Newton không đổi; chỉ thay giá trị ban đầu."
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    )


# --------------------- GIAO DIỆN ---------------------
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
root = tk.Tk()
root.title("Đồ án Đề tài 2 – Phương pháp Newton")
root.geometry("1180x820")
# Tác dụng: Thiết lập tiêu đề hoặc kích thước cửa sổ ứng dụng.
root.minsize(980, 700)

# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
style = ttk.Style()
# Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
try:
    style.theme_use("clam")
# Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
except Exception:
    # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
    pass
style.configure("Treeview", rowheight=23, font=("Arial", 9))
style.configure("Treeview.Heading", font=("Arial", 9, "bold"))
style.configure("TNotebook.Tab", padding=(13, 7), font=("Arial", 9, "bold"))

# Tác dụng: Gọi chức năng của thư viện giao diện để hiển thị hoặc xử lý thao tác người dùng.
tk.Label(
    root, text="ĐỀ TÀI 2 – TÌM HIỂU VÀ CÀI ĐẶT ỨNG DỤNG TỐI ƯU HÓA BẬC HAI – NEWTON",
    font=("Arial", 14, "bold"), fg="#17365d"
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
).pack(pady=(10, 5))

# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=6)

# TRANG 1: TONG QUAN
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
page1 = ttk.Frame(notebook)
notebook.add(page1, text="1. TỔNG QUAN")
tk.Label(page1, text="PHƯƠNG PHÁP NEWTON – TỐI ƯU HÓA BẬC HAI",
         font=("Arial", 15, "bold"), fg="#17365d").pack(pady=(25, 12))
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
tk.Label(page1, text=(
    "Mục tiêu: tìm điểm cực tiểu của hàm mục tiêu bằng phương pháp Newton.\n\n"
    "Ý tưởng theo bài giảng: xấp xỉ hàm mục tiêu bằng hàm bậc hai tại điểm hiện tại,\n"
    "sau đó tìm điểm làm đạo hàm của hàm xấp xỉ bằng 0.\n\n"
    "Chương trình thực hiện: nhập dữ liệu → tính đạo hàm → lặp Newton →\n"
    "hiển thị bảng tính, phép thế số, kết quả và đồ thị."
), font=("Arial", 11), justify="center").pack(pady=12)
tk.Label(page1, text="CÔNG THỨC LẶP CHÍNH", font=("Arial", 11, "bold")).pack(pady=(24, 6))
tk.Label(page1, text="xₙ₊₁ = xₙ − f′(xₙ) / f″(xₙ)",
         font=("Cambria Math", 18, "bold"), fg="#1769aa").pack(pady=8)
tk.Label(page1, text="Nguồn lý thuyết: Bài giảng Nhập môn Tối ưu hóa, Buổi 7, Mục 8, trang 3–4.",
         font=("Arial", 10, "italic")).pack(pady=10)

# TRANG 2: TINH NEWTON
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
page2 = ttk.Frame(notebook)
notebook.add(page2, text="2. TÍNH NEWTON")
input_box = ttk.LabelFrame(page2, text="ĐẦU VÀO")
input_box.pack(fill="x", padx=10, pady=8)
tk.Label(input_box, text="Hàm mục tiêu f(x):").grid(row=0, column=0, padx=7, pady=8)
general_expr = tk.Entry(input_box, width=30, font=("Consolas", 10))
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
general_expr.grid(row=0, column=1, padx=5, pady=8)
general_expr.insert(0, "x**2 - 4*x + 6")
tk.Label(input_box, text="Giá trị ban đầu x₀:").grid(row=0, column=2, padx=(15, 5), pady=8)
general_x0 = tk.Entry(input_box, width=9, font=("Consolas", 10))
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
general_x0.grid(row=0, column=3, padx=5, pady=8)
general_x0.insert(0, "6")
tk.Button(input_box, text="TÍNH NEWTON", command=run_general,
          bg="#1769aa", fg="white", font=("Arial", 10, "bold"),
          # Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
          padx=10, pady=4).grid(row=0, column=4, padx=10)

general_derivatives = tk.Label(page2, text="Đạo hàm sẽ hiển thị sau khi tính.",
                               justify="left", anchor="w", font=("Consolas", 9),
                               padx=8, pady=5, relief="groove")
general_derivatives.pack(fill="x", padx=10, pady=4)

table_box = ttk.LabelFrame(page2, text="BẢNG CÁC BƯỚC LẶP")
table_box.pack(fill="x", padx=10, pady=5)
general_cols = ("k", "x", "fx", "f1", "f2")
general_table = ttk.Treeview(table_box, columns=general_cols, show="headings", height=5)
# Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
for col, title, width in [
    ("k", "Lần lặp k", 90), ("x", "xₖ", 170), ("fx", "f(xₖ)", 170),
    ("f1", "f'(xₖ)", 170), ("f2", "f''(xₖ)", 170)
# Tác dụng: Bắt đầu một khối lệnh; các dòng thụt vào bên dưới thuộc khối này.
]:
    # Tác dụng: Thiết lập tiêu đề hoặc cách hiển thị cột trong bảng.
    general_table.heading(col, text=title)
    general_table.column(col, width=width, anchor="center")
general_table.pack(fill="x", padx=5, pady=5)

general_status = tk.Label(page2, text="Nhập hàm và x₀, sau đó bấm TÍNH NEWTON.",
                          anchor="w", fg="#334155")
general_status.pack(fill="x", padx=12, pady=5)

# TRANG 3: DO THI VA PHEP THE
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
page3 = ttk.Frame(notebook)
notebook.add(page3, text="3. ĐỒ THỊ & PHÉP TÍNH")
tk.Label(page3, text="ĐỒ THỊ HÀM MỤC TIÊU", font=("Arial", 11, "bold"),
         fg="#17365d").pack(pady=(8, 2))
general_chart = tk.Canvas(page3, bg="white", height=330,
                          highlightthickness=1, highlightbackground="#cbd5e1")
general_chart.pack(fill="both", expand=True, padx=10, pady=6)
steps_box = ttk.LabelFrame(page3, text="PHÉP THẾ SỐ TỪNG LẦN LẶP")
steps_box.pack(fill="both", expand=True, padx=10, pady=6)
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
steps_frame = tk.Frame(steps_box)
steps_frame.pack(fill="both", expand=True)
general_steps = tk.Text(steps_frame, height=9, wrap="word",
                        font=("Consolas", 9), padx=8, pady=6)
general_scroll = ttk.Scrollbar(steps_frame, orient="vertical", command=general_steps.yview)
# Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
general_steps.configure(yscrollcommand=general_scroll.set)
general_steps.pack(side="left", fill="both", expand=True)
general_scroll.pack(side="right", fill="y")

# TRANG 4: UNG DUNG MO RONG
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
page4 = ttk.Frame(notebook)
notebook.add(page4, text="4. ỨNG DỤNG MỞ RỘNG")
tk.Label(page4, text=UNG_DUNG_TEN.upper(), font=("Arial", 12, "bold"),
         fg="#17365d", wraplength=1000).pack(anchor="w", padx=12, pady=(10, 5))
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
tk.Label(page4, text=UNG_DUNG_GIAI_THICH, wraplength=1050,
         justify="left").pack(anchor="w", padx=12, pady=4)
tk.Label(page4, text=UNG_DUNG_LIEN_HE, font=("Consolas", 9),
         wraplength=1050, justify="left").pack(anchor="w", padx=12, pady=4)

app_input = ttk.LabelFrame(page4, text="DỮ LIỆU ĐẦU VÀO")
app_input.pack(fill="x", padx=12, pady=6)
tk.Label(app_input, text="Thể tích cố định V (cm³):").grid(row=0, column=0, padx=6, pady=7)
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
volume_entry = tk.Entry(app_input, width=12)
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
volume_entry.grid(row=0, column=1, padx=5, pady=7)
volume_entry.insert(0, "1000")
tk.Label(app_input, text="Bán kính ban đầu r₀ (cm):").grid(row=0, column=2, padx=(18, 5), pady=7)
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
radius_entry = tk.Entry(app_input, width=12)
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
radius_entry.grid(row=0, column=3, padx=5, pady=7)
radius_entry.insert(0, "8")
tk.Button(app_input, text="TỐI ƯU KÍCH THƯỚC", command=run_application,
          bg="#256b45", fg="white", font=("Arial", 10, "bold"),
          # Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
          padx=10, pady=4).grid(row=0, column=4, padx=10, pady=5)

application_result = tk.Label(page4, text="Kết quả tối ưu sẽ hiển thị tại đây.",
                              justify="left", anchor="w", font=("Arial", 10, "bold"),
                              padx=8, pady=7, relief="groove")
application_result.pack(fill="x", padx=12, pady=5)

app_table_box = ttk.LabelFrame(page4, text="BẢNG LẶP NEWTON CHO BÀI TOÁN ỨNG DỤNG")
app_table_box.pack(fill="x", padx=12, pady=5)
app_cols = ("k", "r", "area", "d1", "d2")
application_table = ttk.Treeview(app_table_box, columns=app_cols, show="headings", height=4)
# Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
for col, title, width in [
    ("k", "Lần lặp k", 90), ("r", "rₖ (cm)", 160), ("area", "S(rₖ) (cm²)", 180),
    ("d1", "S'(rₖ)", 170), ("d2", "S''(rₖ)", 170)
# Tác dụng: Bắt đầu một khối lệnh; các dòng thụt vào bên dưới thuộc khối này.
]:
    # Tác dụng: Thiết lập tiêu đề hoặc cách hiển thị cột trong bảng.
    application_table.heading(col, text=title)
    application_table.column(col, width=width, anchor="center")
application_table.pack(fill="x", padx=5, pady=5)

# Tạo khung chứa phần trình bày phép thế số của bài toán ứng dụng.
application_steps_box = ttk.LabelFrame(page4, text="CÁC BƯỚC TÍNH VÀ THẾ SỐ NEWTON")
application_steps_box.pack(fill="x", padx=12, pady=5)

# Tạo vùng văn bản để hiển thị công thức, phép thế số và kết quả từng bước.
application_steps = tk.Text(
    application_steps_box, height=7, wrap="word", font=("Consolas", 9),
    padx=8, pady=5
)

# Tạo thanh cuộn dọc để xem toàn bộ nội dung nếu văn bản dài.
application_steps_scroll = ttk.Scrollbar(
    application_steps_box, orient="vertical", command=application_steps.yview
)

# Liên kết thanh cuộn với vùng văn bản.
application_steps.configure(yscrollcommand=application_steps_scroll.set)

# Đặt vùng văn bản ở bên trái và cho phép giãn theo chiều ngang.
application_steps.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Đặt thanh cuộn ở bên phải vùng văn bản.
application_steps_scroll.pack(side="right", fill="y", padx=(0, 5), pady=5)

app_chart_box = ttk.LabelFrame(page4, text="ĐỒ THỊ DIỆN TÍCH VẬT LIỆU")
app_chart_box.pack(fill="both", expand=True, padx=12, pady=5)
application_chart = tk.Canvas(app_chart_box, bg="white", height=230,
                              highlightthickness=1, highlightbackground="#cbd5e1")
application_chart.pack(fill="both", expand=True, padx=5, pady=5)
application_status = tk.Label(page4, text="Ứng dụng thực tế: giữ V cố định, tìm r để S(r) nhỏ nhất.",
                              anchor="w", fg="#334155")
application_status.pack(fill="x", padx=12, pady=4)

# TRANG 5: CONG THUC VA MO RONG SO SANH
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
page5 = ttk.Frame(notebook)
notebook.add(page5, text="5. CÔNG THỨC SLIDE")
tk.Label(page5, text="CÔNG THỨC THEO SLIDE BUỔI 7 – MỤC 8, TRANG 3–4",
         font=("Arial", 11, "bold"), fg="#17365d").pack(anchor="w", padx=12, pady=8)
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
formula_frame = tk.Frame(page5)
formula_frame.pack(fill="both", expand=True, padx=10, pady=5)
formula_text = tk.Text(formula_frame, wrap="word", font=("Consolas", 10), padx=10, pady=8)
formula_scroll = ttk.Scrollbar(formula_frame, orient="vertical", command=formula_text.yview)
# Tác dụng: Cập nhật thuộc tính hoặc nội dung hiển thị của giao diện.
formula_text.configure(yscrollcommand=formula_scroll.set)
formula_text.pack(side="left", fill="both", expand=True)
formula_scroll.pack(side="right", fill="y")
formula_text.insert("end", "TRANG 3 – KHAI TRIỂN TAYLOR BẬC HAI\n" + TAYLOR + "\n\n")
formula_text.insert("end", "TRANG 3 – HÀM XẤP XỈ BẬC HAI\n" + HAM_XAP_XI + "\n\n")
formula_text.insert("end", "TRANG 3 – ĐIỀU KIỆN ĐẠO HÀM BẰNG 0\n" + DIEU_KIEN + "\n\n")
formula_text.insert("end", "TRANG 3–4 VÀ TRANG 4 – CÔNG THỨC LẶP NEWTON\n" + NEWTON + "\n\n")
formula_text.insert("end", "Ý NGHĨA KÝ HIỆU\n")
# Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
for item in KY_HIEU:
    formula_text.insert("end", "• " + item + "\n")
formula_text.configure(state="disabled")

# Them phan so sanh gia tri khoi tao trong cung trang cong thuc.
compare_box = ttk.LabelFrame(page5, text="THỬ NGHIỆM THAY ĐỔI GIÁ TRỊ BAN ĐẦU")
compare_box.pack(fill="x", padx=10, pady=6)
tk.Label(compare_box, text="Các x₀ (cách nhau bằng dấu phẩy):").grid(row=0, column=0, padx=6, pady=6)
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
compare_entry = tk.Entry(compare_box, width=25)
# Tác dụng: Đặt thành phần giao diện vào cửa sổ và xác định cách bố trí.
compare_entry.grid(row=0, column=1, padx=5, pady=6)
compare_entry.insert(0, "-2, 0, 5")
tk.Button(compare_box, text="SO SÁNH", command=compare_starts).grid(row=0, column=2, padx=8, pady=6)
compare_cols = ("x0", "xstar", "fx", "count", "note")
# Tác dụng: tăng chiều cao bảng lên 8 dòng để nhìn thấy đủ các giá trị x0, kể cả -2.
compare_table = ttk.Treeview(compare_box, columns=compare_cols, show="headings", height=8)
# Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
for col, title, width in [
    ("x0", "x₀", 100), ("xstar", "x* tìm được", 140),
    ("fx", "f(x*)", 140), ("count", "Số lần lặp", 120), ("note", "Nhận xét", 240)
# Tác dụng: Bắt đầu một khối lệnh; các dòng thụt vào bên dưới thuộc khối này.
]:
    # Tác dụng: Thiết lập tiêu đề hoặc cách hiển thị cột trong bảng.
    compare_table.heading(col, text=title)
    compare_table.column(col, width=width, anchor="center")
compare_table.grid(row=1, column=0, columnspan=3, sticky="ew", padx=6, pady=5)
compare_note = tk.Label(compare_box, text="Phần so sánh chỉ thay đổi x₀; hàm mục tiêu và công thức Newton giữ nguyên.",
                        anchor="w", justify="left")
compare_note.grid(row=2, column=0, columnspan=3, sticky="w", padx=6, pady=5)

# Chay san vi du minh hoa o trang 2 va ung dung mo rong.
# Tác dụng: Lên lịch gọi hàm sau một khoảng thời gian tính bằng mili giây.
root.after(350, run_general)
# Tác dụng: Lên lịch gọi hàm sau một khoảng thời gian tính bằng mili giây.
root.after(500, run_application)
# Tác dụng: Khởi chạy vòng lặp sự kiện để cửa sổ tiếp tục hoạt động và nhận thao tác.
root.mainloop()
