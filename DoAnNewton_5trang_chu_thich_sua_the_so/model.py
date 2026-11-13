# -*- coding: utf-8 -*-
"""MODEL: tinh dao ham va lap Newton theo cong thuc slide trang 4."""
# Tác dụng: Nhập thư viện để sử dụng các chức năng có sẵn.
import math
# Tác dụng: Nhập thư viện để sử dụng các chức năng có sẵn.
import sympy as sp


def tao_ham(bieu_thuc, bien="x", bien_phu=None):
    """Tao ham va hai dao ham tu bieu thuc nhap vao."""
    symbol = sp.Symbol(bien, positive=True) if bien_phu == "positive" else sp.Symbol(bien)
    # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
    try:
        f_sym = sp.sympify(bieu_thuc, locals={bien: symbol, "pi": sp.pi})
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        f1_sym = sp.diff(f_sym, symbol)
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        f2_sym = sp.diff(f_sym, symbol, 2)
        f = sp.lambdify(symbol, f_sym, modules=["math"])
        f1 = sp.lambdify(symbol, f1_sym, modules=["math"])
        f2 = sp.lambdify(symbol, f2_sym, modules=["math"])
    # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
    except Exception as exc:
        # Tác dụng: Chủ động phát sinh lỗi với thông báo phù hợp.
        raise ValueError(f"Khong doc duoc bieu thuc: {exc}")
    # Tác dụng: Trả kết quả của hàm về nơi gọi.
    return f_sym, f1_sym, f2_sym, f, f1, f2


def tinh_newton(bieu_thuc, x0, bien="x", max_lap=50, eps=1e-8, positive=False):
    """
    Lap Newton dung nguyen cong thuc slide:
    x_(n+1) = x_n - f'(x_n)/f''(x_n)
    """
    bien_phu = "positive" if positive else None
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    _, f1_sym, f2_sym, f, f1, f2 = tao_ham(bieu_thuc, bien, bien_phu)
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    x = float(x0)
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if not math.isfinite(x):
        raise ValueError("Gia tri ban dau phai la so huu han.")
    # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
    if positive and x <= 0:
        raise ValueError("Ban kinh r phai lon hon 0.")

    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    bang = []
    # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
    phep_the = []

    # Tác dụng: Lặp qua từng phần tử hoặc từng lần lặp để xử lý dữ liệu.
    for k in range(max_lap + 1):
        # Tác dụng: Bắt đầu vùng có thể phát sinh lỗi để xử lý an toàn.
        try:
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            fx = float(f(x))
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            d1 = float(f1(x))
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            d2 = float(f2(x))
        # Tác dụng: Bắt lỗi để chương trình thông báo thay vì dừng đột ngột.
        except (ValueError, ZeroDivisionError, OverflowError) as exc:
            # Tác dụng: Chủ động phát sinh lỗi với thông báo phù hợp.
            raise ValueError(f"Khong tinh duoc tai x = {x}: {exc}")

        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if not all(math.isfinite(v) for v in (fx, d1, d2)):
            # Tác dụng: Chủ động phát sinh lỗi với thông báo phù hợp.
            raise ValueError(f"Gia tri khong huu han tai x = {x}.")
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        bang.append((k, x, fx, d1, d2))

        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if abs(d1) <= eps:
            # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
            break
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if k == max_lap:
            # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
            break
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if abs(d2) <= 1e-14:
            raise ValueError("f''(x_n) bang 0 hoac qua gan 0, khong the chia.")

        # Cong thuc lap dung nguyen van theo slide cua giang vien.
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        x_moi = x - d1 / d2
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        phep_the.append(
            # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
            f"x_({k+1}) = x_{k} - f'(x_{k})/f''(x_{k}) = {x:.8g} - ({d1:.8g})/({d2:.8g}) = {x_moi:.8g}"
        # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
        )
        # Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
        x = x_moi
        # Tác dụng: Kiểm tra điều kiện trước khi thực hiện nhánh lệnh.
        if positive and x <= 0:
            # Tác dụng: Chủ động phát sinh lỗi với thông báo phù hợp.
            raise ValueError(
                "Buoc lap tao ra r <= 0. Hay chon ban kinh ban dau khac."
            # Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
            )

    # Tác dụng: Trả kết quả của hàm về nơi gọi.
    return bang, phep_the, f1_sym, f2_sym
