from dataclasses import dataclass
from typing import List
import csv, os

FILE = "nhanvien.csv"
HEADERS = ["Loai","Ma","HoTen","Luong","DoanhSo","HoaHong","TrachNhiem","ThuNhap"]

@dataclass
class NhanVien:
    ma:str; ho_ten:str; luong:float
    def getThuNhap(self): return self.luong
    def loai(self): return "HanhChinh"
    def to_row(self): return {"Loai":self.loai(),"Ma":self.ma,"HoTen":self.ho_ten,
        "Luong":self.luong,"DoanhSo":"","HoaHong":"","TrachNhiem":"","ThuNhap":self.getThuNhap()}

@dataclass
class TiepThi(NhanVien):
    doanh_so:float; hoa_hong:float
    def getThuNhap(self): return self.luong+self.doanh_so*self.hoa_hong
    def loai(self): return "TiepThi"
    def to_row(self): return {"Loai":self.loai(),"Ma":self.ma,"HoTen":self.ho_ten,
        "Luong":self.luong,"DoanhSo":self.doanh_so,"HoaHong":self.hoa_hong,
        "TrachNhiem":"","ThuNhap":self.getThuNhap()}

@dataclass
class TruongPhong(NhanVien):
    trach_nhiem:float
    def getThuNhap(self): return self.luong+self.trach_nhiem
    def loai(self): return "TruongPhong"
    def to_row(self): return {"Loai":self.loai(),"Ma":self.ma,"HoTen":self.ho_ten,
        "Luong":self.luong,"DoanhSo":"","HoaHong":"","TrachNhiem":self.trach_nhiem,
        "ThuNhap":self.getThuNhap()}

def ensure_file():
    if not os.path.exists(FILE):
        with open(FILE,"w",encoding="utf-8-sig",newline="") as f:
            csv.DictWriter(f,fieldnames=HEADERS).writeheader()

def read_all()->List[NhanVien]:
    ensure_file(); ds=[]
    with open(FILE,"r",encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                loai=r["Loai"]; ma=r["Ma"].strip(); ten=r["HoTen"].strip()
                luong=float(r["Luong"]or 0)
                if loai=="TiepThi":
                    ds.append(TiepThi(ma,ten,luong,float(r["DoanhSo"]or 0),float(r["HoaHong"]or 0)))
                elif loai=="TruongPhong":
                    ds.append(TruongPhong(ma,ten,luong,float(r["TrachNhiem"]or 0)))
                else: ds.append(NhanVien(ma,ten,luong))
            except: continue
    return ds

def write_all(ds): 
    with open(FILE,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=HEADERS); w.writeheader(); w.writerows([x.to_row() for x in ds])

def input_float(msg,b=False,d=None):
    while True:
        s=input(msg).strip()
        if b and s=="": return d
        try: return float(s)
        except: print("Sai định dạng.")

def split_name(n): p=n.split(); return (p[-1].lower()," ".join(p[:-1]).lower()) if p else ("","")
def find(ds,ma): 
    for i,n in enumerate(ds):
        if n.ma.lower()==ma.lower(): return i

def print_table(ds,t=None):
    if t: print("\n"+t)
    if not ds: return print("(Không có dữ liệu)")
    print(f"{'Ma':<8}{'Loai':<12}{'HoTen':<25}{'Luong':>10}{'Phu/DS*HH':>14}{'ThuNhap':>12}")
    for n in ds:
        p="-"
        if isinstance(n,TiepThi): p=f"{n.doanh_so:.1f}*{n.hoa_hong:.2f}"
        if isinstance(n,TruongPhong): p=f"+{n.trach_nhiem:.2f}"
        print(f"{n.ma:<8}{n.loai():<12}{n.ho_ten:<25}{n.luong:>10.2f}{p:>14}{n.getThuNhap():>12.2f}")

def nhap_nv():
    l=input("Loại(1.HC/2.TT/3.TP): ").strip()
    ma,ten=input("Mã: ").strip(),input("Họ tên: ").strip()
    luong=input_float("Lương: ")
    if l=="2": return TiepThi(ma,ten,luong,input_float("Doanh số: "),input_float("Hoa hồng: "))
    if l=="3": return TruongPhong(ma,ten,luong,input_float("Trách nhiệm: "))
    return NhanVien(ma,ten,luong)

def y1(): 
    n=int(input("Số lượng: ")); ds=read_all()
    for _ in range(n): ds.append(nhap_nv())
    write_all(ds)

def y2(): print_table(read_all(),"DANH SÁCH NHÂN VIÊN")
def y3():
    ds=read_all(); k=input("Mã cần tìm: ").strip()
    i=find(ds,k); print_table([ds[i]],f"KẾT QUẢ: {k}") if i!=None else print("Không thấy.")
def y4():
    ds=read_all(); k=input("Mã cần xóa: ").strip()
    i=find(ds,k)
    if i!=None: ds.pop(i); write_all(ds); print("Đã xóa.")
    else: print("Không thấy.")
def y5():
    ds=read_all(); k=input("Mã cần cập nhật: ").strip()
    i=find(ds,k)
    if i==None: return print("Không thấy.")
    n=ds[i]; ten=input(f"Họ tên[{n.ho_ten}]: ").strip() or n.ho_ten
    luong=input_float(f"Lương[{n.luong}]: ",True,n.luong)
    if isinstance(n,TiepThi):
        ds[i]=TiepThi(n.ma,ten,luong,
            input_float(f"DS[{n.doanh_so}]: ",True,n.doanh_so),
            input_float(f"HH[{n.hoa_hong}]: ",True,n.hoa_hong))
    elif isinstance(n,TruongPhong):
        ds[i]=TruongPhong(n.ma,ten,luong,
            input_float(f"TN[{n.trach_nhiem}]: ",True,n.trach_nhiem))
    else: ds[i]=NhanVien(n.ma,ten,luong)
    write_all(ds); print("Đã cập nhật.")
def y6():
    mn=input_float("Min: "); mx=input_float("Max: ")
    if mn>mx: mn,mx=mx,mn
    print_table([n for n in read_all() if mn<=n.luong<=mx],f"LƯƠNG [{mn}-{mx}]")
def y7(): print_table(sorted(read_all(),key=lambda x:split_name(x.ho_ten)),"SẮP XẾP HỌ TÊN")
def y8(): print_table(sorted(read_all(),key=lambda x:x.getThuNhap(),reverse=True),"THU NHẬP ↓")
def y9(): print_table(sorted(read_all(),key=lambda x:x.getThuNhap(),reverse=True)[:5],"TOP 5 THU NHẬP")

def menu():
    f={"1":y1,"2":y2,"3":y3,"4":y4,"5":y5,"6":y6,"7":y7,"8":y8,"9":y9}
    while True:
        print("""
MENU
1.Nhập & lưu  2.Xuất DS  3.Tìm  4.Xóa
5.Sửa  6.Tìm theo lương  7.Sắp xếp tên
8.Sắp xếp TN  9.Top5  0.Thoát""")
        c=input("Chọn: ").strip()
        if c=="0": break
        f.get(c,lambda:print("Sai chọn."))()

if __name__=="__main__":
    ensure_file(); menu()
