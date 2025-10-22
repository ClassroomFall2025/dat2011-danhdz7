#Viết một hàm để tính tiền nước sinh hoạt theo phương pháp lũy tiến. Tham số
#truyền vào hàm là số nước sử dụng trong tháng.
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500, 8800, 12000, 24000)
    if so_nuoc <= 10:
        tien_nuoc = so_nuoc * gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tien_nuoc = 10 * gia_ban_nuoc[0] + (so_nuoc- 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (so_nuoc - 20) * gia_ban_nuoc[2]
    else:
        tien_nuoc = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (so_nuoc - 30) * gia_ban_nuoc[3]
    return tien_nuoc

#Tính nguyên liệu làm bánh
def tinh_NL(sl_bdx, sl_btc, sl_bd):
    banh_dx = {"đường": 0.04, "đậu": 0.07}
    banh_tc  = {"đường": 0.06, "đậu": 0}
    banh_deo = {"đường": 0.05, "đậu": 0.02}
    nguyen_lieu = {}
    duong_hop_banh = sl_bdx * banh_dx["đường"] + sl_btc * banh_tc["đường"] + sl_bd * banh_deo["đường"]
    dau_hop_banh = sl_bdx * banh_dx["đậu"] + sl_btc * banh_tc["đậu"] + sl_bd * banh_deo["đậu"]
    nguyen_lieu["đường"] = duong_hop_banh
    nguyen_lieu["đậu"] = dau_hop_banh
    return nguyen_lieu
