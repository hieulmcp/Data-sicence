# Nếu số lượng >= 5, giảm 10% / thành tiền
# Ngược lại không giảm


so_luong = int(input("Nhập số lượng: "))
don_gia = int(input("Nhập đơn giá: "))
thanh_tien = so_luong * don_gia

if so_luong >= 5:
    print("-" * 10)
    print("Thành tiền:", "{:,}".format(thanh_tien))
    tien_giam = thanh_tien * 0.1  # 10%
    thanh_tien -= tien_giam #  thanh_tien = thanh_tien - tien_giam
    # print("Tiền giảm (10%):", "{:,}".format(tien_giam))
    print("Tiền giảm (10%%): %s" % "{:,}".format(tien_giam))
    print("TIỀN PHẢI TRẢ:", "{:,}".format(thanh_tien)) 
else:
    print("Thành tiền:", "{:,}".format(thanh_tien))
    print("Tiền giảm (10%): 0")
    print("TIỀN PHẢI TRẢ:", "{:,}".format(thanh_tien))



