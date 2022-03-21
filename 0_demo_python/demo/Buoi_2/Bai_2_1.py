so_luong = int(input("Nhập số lượng: "))
don_gia = int(input("Nhập đơn giá: "))
thanh_tien = so_luong * don_gia
print("Thành tiền = %i * %i = %i" %(so_luong, don_gia, thanh_tien))
print("Thành tiền = %i * %s = %s" %(so_luong, "{:,}".format(don_gia), "{:,}".format(thanh_tien)))


# print(type("{:,}".format(don_gia))  # => str
# "{:,}".format(thanh_tien)
