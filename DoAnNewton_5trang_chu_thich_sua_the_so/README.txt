DO AN DE TAI 2 - PHUONG PHAP NEWTON

Cau truc 3 file chinh:
- app.py: giao dien 5 trang rieng.
- model.py: tinh dao ham va lap theo cong thuc Newton trong slide.
- data.py: luu cong thuc slide va mo ta bai toan ung dung.
- requirements.txt: thu vien can cai.

Cai dat (mo Terminal/PowerShell tai thu muc Do_an_Newton):
    pip install -r requirements.txt

Chay:
    python app.py

5 trang trong chuong trinh:
1. Tong quan: muc tieu va cong thuc chinh.
2. Tinh Newton: nhap ham f(x), gia tri ban dau x0, xem dao ham va bang lap.
3. Do thi & phep tinh: xem do thi va phep the so tung lan lap.
4. Ung dung mo rong: bai toan toi thieu vat lieu lam hop tru co the tich co dinh.
5. Cong thuc slide: cac cong thuc theo slide Buoi 7, Muc 8, trang 3-4; co them
   thu nghiem thay doi x0.

UNG DUNG MO RONG:
Hop tru co the tich V co dinh.
V = pi*r^2*h => h = V/(pi*r^2)
S(r) = 2*pi*r^2 + 2*V/r
S'(r) = 4*pi*r - 2*V/r^2
S''(r) = 4*pi + 4*V/r^3
Ap dung nguyen cong thuc Newton trong slide, chi doi ten bien x thanh r:
r_(n+1) = r_n - S'(r_n)/S''(r_n)

Luu y:
- Don vi the tich nhap la cm^3; ban kinh va chieu cao la cm; dien tich la cm^2.
- Bai toan ung dung giu the tich V co dinh va tim ban kinh lam dien tich vat lieu nho nhat.
- Can nhap r0 > 0.
- Cac gia tri dien san la du lieu minh hoa de chay thu, co the thay doi.

Da kiem tra tinh toan: V=1000 cm3, ban kinh ban dau 8 cm. Ket qua phai thoa S'(r*) gan 0 va S''(r*) > 0.


GHI CHU BAN SUA:
- Bảng so sánh được tăng chiều cao để nhìn thấy đủ các dòng, gồm cả x0 = -2.
- Phép thế số hiển thị rõ công thức tổng quát theo slide trước khi thay số cụ thể.
- Các dòng lệnh Python trong 3 file chính có chú thích tác dụng; nội dung chuỗi giao diện được giữ nguyên để tránh làm hỏng chương trình.
