# chuoi = "trung tâm tin học"
# print(chuoi.capitalize())  # Trung tâm tin học
# print(chuoi.upper())       # TRUNG TÂM TIN HỌC
# chuoi_2 ="TRUNG TÂM TIN HỌC"
# print(chuoi_2.lower())     # trung tâm tin học
# chuoi = "trung Tâm Tin học"
# print(chuoi.capitalize())  # Trung tâm tin học



# chuoi_1 = "trung tâm tin học abc"
# chuoi_2 = "khoa học tự nhiên"
# print(len(chuoi))
# print(chuoi.center(60, '*'))
# print(chuoi.center(60))
# print(chuoi.center(10))
# print(chuoi.center(len(chuoi) + 20))
# print(chuoi_1.ljust(30, "-"), chuoi_2.ljust(40, '-'))
# print(chuoi_2.ljust(30, "-"), chuoi_1.ljust(40, '-'))
# print(chuoi_1.rjust(30, "-"), chuoi_2.rjust(40, '-'))
# print(chuoi_2.rjust(30, "-"), chuoi_1.rjust(40, '-'))


# chuoi = "trung tâm tin học khoa học tự nhiên"
# chuoi_con = "ng"
# print(chuoi.count(chuoi_con))



# chuoi = "trung tâm tin học khoa học tự nhiên"
# chuoi_con = "ng"
# print(chuoi.find(chuoi_con))


# gia_tri = input('Nhập số: ')
# if gia_tri.isdigit():
#     print(int(gia_tri) + 10)
# else:
#     print("Dữ liệu không hợp lệ.")


# chuoi = "trung tâm tin học khoa học tự nhiên"
# cat_chuoi = chuoi.split()
# print(len(cat_chuoi))
# print(cat_chuoi)

# cat_chuoi = chuoi.split('n')
# print(len(cat_chuoi))
# print(cat_chuoi)


# cat_chuoi = chuoi.split(' ', 3)
# print(len(cat_chuoi))
# print(cat_chuoi)


# chuoi = "trung tâm tin học khoa học tự nhiên"
# Hãy xử lý in hoa các ký tự đầu tiên của từng từ trong chuỗi
# => Trung Tâm Tin Học Khoa Học Tự Nhiên
# cat_chuoi = chuoi.split()
# chuoi_xu_ly = ''
# for phan_tu in cat_chuoi:
#     chuoi_xu_ly += phan_tu.capitalize() + " "
# print(chuoi_xu_ly.strip())
# print(chuoi.title())



# Xử lý cắt chuỗi họ tên
ho_ten = "Nguyễn Thị Bé Ba"
'''
Họ: Nguyễn
Tên: Ba
Tên đệm: Thị Bé
'''
cat_chuoi = ho_ten.split()

# Họ
ho = cat_chuoi[0]
print("Họ:", ho)

# Tên
# ten = cat_chuoi[len(cat_chuoi) - 1]
ten = cat_chuoi[-1]
print("Tên:", ten)

# Tên đệm
list_con = cat_chuoi[1:-1]

# Cách 1
# ten_dem = ''
# for phan_tu in list_con:
#     ten_dem += phan_tu + " "
# print("Tên đệm:", ten_dem)

# Cách 2
ten_dem = " ".join(list_con)
print("Tên đệm:", ten_dem)


