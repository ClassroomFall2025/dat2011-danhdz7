class San_Pham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.__ten_san_pham = ten_san_pham
        self.__gia = gia
        self.__giam_gia = giam_gia
    #get
    def get_ten(self):
        return self.__ten_san_pham
    def get_gia(self):
        return self.__gia
    def get_giam_gia(self):
        return self.__giam_gia
    
    #set
    def set_ten(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham
    def set_gia(self, gia):
        self.__gia = gia
    def set_giam_gia(self, giam_gia):
        self.__giam_gia = giam_gia

    def thue_NK(self):
        return self.__gia * 0.1
    
    #bai2    
    def nhap_tt_sp(self):
        self.__ten_san_pham = input("tên sản phẩm:")
        self.__gia = float(input("gia"))
        self.__giam_gia = float(input("giảm giá"))

    def xuat_tt_sp(self):
        print(f"Sản phẩm {self.__ten_san_pham} có giá {self.__gia} và được giảm giá {self.__giam_gia} và thuế nhập khẩu: {self.thue_NK()}")
    
    def __str__(self):
        print(f"Sản phẩm {self.__ten_san_pham} có giá {self.__gia} và được giảm giá {self.__giam_gia} và thuế NK: {self.thue_NK()}")