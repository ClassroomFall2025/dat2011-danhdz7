#bài 4

import sinhvienpoly as svpl

class QuanLySinhVien:
    #khởi tạo danh sách sinh viên ban đầu rỗng
    def __init__(self):
        self.dssv = []

    # phương thức nhập danh sách sinh viên
    def nhap_dssv(self):
        while True:
            ho_ten_sv = input("nhập họ tên sinh viên:")
            nganh_hoc = input("Nhập ngành học sinh viên")
            if nganh_hoc.lower() == "it":
                java = float(input("điểm java: "))
                html = float(input("điểm html: "))
                css = float(input("điểm css: "))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, java, html, css)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "biz":
                marketing = float(input("điểm marketing: "))
                sales = float(input("điểm sales "))
                sv = svpl.SinhVienIT(ho_ten_sv, nganh_hoc, marketing, sales)
                self.dssv.append(sv)
            elif nganh_hoc.lower() == "exit":
                print("\nKết thúc nhập thông tin sinh viên !!! \n")
                break
            else:
                print("Nhập sai nhập lại \n!!!")
        return self.dssv
    def xuat_dssv(self):
            if not self.dssv:
                print("Danh sách sinh viên rỗng !!!")
            else:
                print(f'{"Tên sinh viên"}, {"Ngành học"}, {"Điểm"}, {"Học lực"}')
                for sv in self.dssv:
                    sv.xuat_dssv()

    def xuat_dssv_gioi(self):
        print("\n--- DANH SÁCH SINH VIÊN GIỎI ---")
        gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
        if not gioi:
            print("Không có sinh viên giỏi.")
        else:
            print(f"{'Họ Tên':20} | {'Ngành':8} | {'Điểm':6} | {'Học lực':10}")
            print("-" * 55)
            for sv in gioi:
                sv.xuat_dssv()

    def sap_xep_dssv(self):
        if not self.dssv:
            print("❌ Danh sách sinh viên rỗng, không thể sắp xếp!")
            return
        self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
        print("\n✅ Đã sắp xếp danh sách sinh viên theo điểm (cao → thấp):")
        self.xuat_dssv()

    # def xuat_dssv_gioi(self):
    #     print("\n--- DANH SÁCH SINH VIÊN GIỎI ---")
    #     gioi = [sv for sv in self.dssv if sv.get_hoc_luc() == "Giỏi"]
    #     if not gioi:
    #         print("Không có sinh viên giỏi.")
    #     else:
    #         for sv in gioi:
    #             sv.xuat_dssv()
    # def sap_xep_dssv(self):
    #     if not self.dssv:
    #         print(" Danh sách sinh viên rỗng, không thể sắp xếp!")
    #         return
    #     self.dssv.sort(key=lambda sv: sv.get_diem(), reverse=True)
    #     print("\n Đã sắp xếp danh sách sinh viên theo điểm (cao → thấp):")
    #     self.xuat_dssv()
