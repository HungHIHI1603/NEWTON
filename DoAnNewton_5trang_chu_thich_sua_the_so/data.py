# -*- coding: utf-8 -*-
"""
DATA: Cong thuc va du lieu cua do an Newton.
Phan ly thuyet duoc trinh bay theo slide Buoi 7, Muc 8, trang 3-4.
"""

# Slide trang 3: khai trien Taylor bac hai tai x = x_n.
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
TAYLOR = (
    "f(x) = f(x_n) + f'(x_n)(x - x_n) "
    "+ 1/2! f''(x_n)(x - x_n)^2"
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)

# Slide trang 3: dang ham xap xi bac hai sau khi sap xep.
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
HAM_XAP_XI = (
    "f(x) = 1/2 f''(x_n)x^2 "
    "+ [f'(x_n) - f''(x_n)x_n]x + C"
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)

# Slide trang 3: dieu kien dao ham cua ham xap xi bang 0.
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
DIEU_KIEN = (
    "f''(x_n)x = f''(x_n)x_n - f'(x_n)"
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)

# Slide trang 3-4 va trang 4: cong thuc lap Newton.
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
NEWTON = (
    "x_(n+1) = x_n - f'(x_n) / f''(x_n)"
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)

# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
KY_HIEU = [
    "x_(n+1): gia tri xap xi tiep theo cua diem toi han",
    "x_n: gia tri xap xi hien tai",
    "f'(x_n): dao ham bac nhat tai x_n",
    "f''(x_n): dao ham bac hai tai x_n (Hessian trong truong hop mot bien)",
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
]

# Bai toan mo rong ung dung thuc te: toi thieu vat lieu lam hop tru.
UNG_DUNG_TEN = "Toi thieu dien tich vat lieu lam hop tru hinh tru co the tich co dinh"
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
UNG_DUNG_GIAI_THICH = (
    "Mot co so san xuat can lam hop hinh tru co the tich co dinh. "
    "De tiet kiem vat lieu, ta tim ban kinh day r sao cho dien tich toan phan "
    "cua hop tru nho nhat. The tich V duoc giu co dinh."
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)
UNG_DUNG_HAM = "S(r) = 2*pi*r^2 + 2*V/r"
UNG_DUNG_DAO_HAM_1 = "S'(r) = 4*pi*r - 2*V/r^2"
UNG_DUNG_DAO_HAM_2 = "S''(r) = 4*pi + 4*V/r^3"
# Tác dụng: Gán giá trị hoặc kết quả tính toán cho biến để dùng ở các bước tiếp theo.
UNG_DUNG_LIEN_HE = (
    "V = pi*r^2*h  =>  h = V/(pi*r^2); "
    "S = 2*pi*r^2 + 2*pi*r*h = 2*pi*r^2 + 2*V/r"
# Tác dụng: Thực hiện câu lệnh xử lý dữ liệu hoặc điều khiển chương trình tại bước này.
)
