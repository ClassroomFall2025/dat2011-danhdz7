import csv
class TaiKhoan:
    def __init__(self,  soTaiKhoan=None, ten=None, loai=None, soDu=None):
        if soTaiKhoan is None:
            self.soTaiKhoan = input("Nhập số tài khoản: ")
            self.ten = input("Nhập tên chủ tài khoản: ")
            self.loai = input("Nhập loại tài khoản (Tiết kiệm / Thanh toán): ")
            self.soDu = float(input("Nhập số dư ban đầu: "))
        else:
            # Nếu truyền đủ 4 tham số thì dùng giá trị đó
            self.soTaiKhoan = soTaiKhoan
            self.ten = ten
            self.loai = loai
            self.soDu = soDu
    def hienThiTaiKhoan (self):
        print(f"Số tài khoản: {self.soTaiKhoan}, Tên: {self.ten}, Loại: {self.loai}, Số dư: {self.soDu} VND")
    def guiTien(self, soTien):
        self.soDu += soTien
        print(f"Đã nạp {soTien} VND vào tài khoản {self.soTaiKhoan}. Số dư hiện tại: {self.soDu} VND")
    def rutTien(self, soTien):
        if soTien > self.soDu:
            print(f"Số dư không đủ để rút !")
        else:
            self.soDu -= soTien
            print(f"Rút thành công {soTien:,.0f} VND. Số dư còn lại: {self.soDu:,.0f} VND")
    def toDict(self):
        return {
            "soTaiKhoan": self.soTaiKhoan,
            "ten": self.ten,
            "loai": self.loai,
            "soDu": self.soDu
        }
def docTaiKhoanTuSV(tenFile="taikhoan.csv"):
    danhsach = []
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            for line in f:
                soTaiKhoan, ten, loai, soDu = line.strip().split(",")
                taiKhoan = TaiKhoan(soTaiKhoan, ten, loai, float(soDu))
                danhsach.append(taiKhoan)
    except FileNotFoundError:
        pass
    return danhsach
def ghiTaiKhoanVaoCSV(danhSach, tenFile="taikhoan.csv"):
    with open(tenFile, "w", encoding="utf-8") as f:
        for taiKhoan in danhSach:
            f.write(f"{taiKhoan.soTaiKhoan},{taiKhoan.ten},{taiKhoan.loai},{taiKhoan.soDu}\n")
    print("Đã ghi danh sách tài khoản vào file CSV.")
def taoTaiKhoanMoi(danhsach):
    soTaiKhoan = input("Nhập số tài khoản: ")
    ten = input("Nhập tên chủ tài khoản: ")
    loai = input("Nhập loại tài khoản (Tiết kiệm/Thanh toán): ")
    soDu = float(input("Nhập số dư ban đầu: "))
    taiKhoanMoi = TaiKhoan(soTaiKhoan, ten, loai, soDu)
    danhsach.append(taiKhoanMoi)
    ghiTaiKhoanVaoCSV(danhsach)
    print("Tài khoản mới đã được tạo và lưu vào file CSV.")

def guiTien(danhsach):
    soTaiKhoan = input("Nhập số tài khoản để nạp tiền: ")
    soTien = float(input("Nhập số tiền cần nạp: "))
    for taiKhoan in danhsach:
        if taiKhoan.soTaiKhoan == soTaiKhoan:
            taiKhoan.guiTien(soTien)
            ghiTaiKhoanVaoCSV(danhsach)
            return
    print("Số tài khoản không tồn tại.")

def rutTien(danhsach):
    soTaiKhoan = input("Nhập số tài khoản để rút tiền: ")
    for taiKhoan in danhsach:
        if taiKhoan.soTaiKhoan == soTaiKhoan:
            soTien = float(input("Nhập số tiền cần rút: "))
            taiKhoan.rutTien(soTien)
            ghiTaiKhoanVaoCSV(danhsach)
            return
    print("Số tài khoản không tồn tại.")
def kiemTraSoDu(danhsach):
    soTaiKhoan = input("Nhập số tài khoản để kiểm tra số dư: ")
    for taiKhoan in danhsach:
        if taiKhoan.soTaiKhoan == soTaiKhoan:
            print(f"Số dư hiện tại của tài khoản {soTaiKhoan} là: {taiKhoan.soDu:,.0f} VND")
            return
    print("Số tài khoản không tồn tại.")
def hienThiTatCa(danhsach):
    for taiKhoan in danhsach:
        taiKhoan.hienThiTaiKhoan()
def xoaTaiKhoan(danhsach):
    soTaiKhoan = input("Nhập số tài khoản cần xóa: ")
    for tk in danhsach:
        if tk.soTaiKhoan == soTaiKhoan:
            danhsach.remove(tk)
            ghiTaiKhoanVaoCSV(danhsach)
            print(f"Đã xóa tài khoản {soTaiKhoan}.")
            return
    print("Số tài khoản không tồn tại.")
def chinh_sua_taikhoan(danhsach):
    soTaiKhoan = input("Nhập số tài khoản cần chỉnh sửa: ")
    for tk in danhsach:
        if tk.soTaiKhoan == soTaiKhoan:
            print("Nhập thông tin mới (để trống nếu không muốn thay đổi):")
            ten_moi = input(f"Tên hiện tại ({tk.ten}): ") or tk.ten
            loai_moi = input(f"Loại hiện tại ({tk.loai}): ") or tk.loai
            soDu_moi_input = input(f"Số dư hiện tại ({tk.soDu}): ")
            soDu_moi = float(soDu_moi_input) if soDu_moi_input else tk.soDu

            tk.ten = ten_moi
            tk.loai = loai_moi
            tk.soDu = soDu_moi

            ghiTaiKhoanVaoCSV(danhsach)
            print(f"Đã cập nhật thông tin tài khoản {soTaiKhoan}.")
            return
    print("Số tài khoản không tồn tại.")
def tim_kiem_theo_ten(danhsach):
    ten_tim_kiem = input("Nhập tên chủ tài khoản cần tìm: ").lower()
    ket_qua = [tk for tk in danhsach if ten_tim_kiem in tk.ten.lower()]
    if ket_qua:
        print(f"Tìm thấy {len(ket_qua)} tài khoản:")
        for tk in ket_qua:
            tk.hienThiTaiKhoan()
    else:
        print("Không tìm thấy tài khoản nào với tên đã nhập.")
def xuat_bao_cao(danhsach):
    print("\n--- BÁO CÁO TÀI KHOẢN NGÂN HÀNG ---")
    print(f"{'Số Tài Khoản':15} {'Tên Chủ Tài Khoản':25} {'Loại Tài Khoản':15} {'Số Dư (VND)':15}")
    print("-" * 70)
    for tk in danhsach:
        print(f"{tk.soTaiKhoan:15} {tk.ten:25} {tk.loai:15} {tk.soDu:15,.0f}")
def sao_luu_du_lieu(danhsach, tenFile="taikhoan_backup.csv"):
    with open(tenFile, "w", encoding="utf-8") as f:
        for taiKhoan in danhsach:
            f.write(f"{taiKhoan.soTaiKhoan},{taiKhoan.ten},{taiKhoan.loai},{taiKhoan.soDu}\n")
    print(f"Đã sao lưu dữ liệu tài khoản vào file {tenFile}.")
def khoi_phuc_du_lieu(tenFile="taikhoan_backup.csv"):
    danhsach = []
    try:
        with open(tenFile, "r", encoding="utf-8") as f:
            for line in f:
                soTaiKhoan, ten, loai, soDu = line.strip().split(",")
                taiKhoan = TaiKhoan(soTaiKhoan, ten, loai, float(soDu))
                danhsach.append(taiKhoan)
        print(f"Đã khôi phục dữ liệu tài khoản từ file {tenFile}.")
    except FileNotFoundError:
        print(f"File {tenFile} không tồn tại.")
    return danhsach
def menu():
    print("\n===== HỆ THỐNG QUẢN LÝ NGÂN HÀNG =====")
    print("1. Tạo tài khoản mới")
    print("2. Gửi tiền")
    print("3. Rút tiền")
    print("4. Kiểm tra số dư")
    print("5. Danh sách tất cả tài khoản")
    print("6. Xóa tài khoản")
    print("7. Chỉnh sửa thông tin tài khoản")
    print("8. Tìm kiếm tài khoản theo tên chủ tài khoản")
    print("9. Xuất báo cáo tài khoản")
    print("10. Sao lưu dữ liệu tài khoản")
    print("11. Khôi phục dữ liệu tài khoản")
    print("0. Thoát")