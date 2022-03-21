import time
from datetime import datetime
import calendar



# ================ TIME
# a = time.time()
# print(a)
# for i in range(10):
#     print(i)
# b = time.time()
# print(b - a)


# c = time.time()
# d = time.localtime(c)
# print(d.tm_year)
# print(d[0])
# print("%i-%i-%i %i:%i:%i" % (d.tm_mday, d.tm_mon, d.tm_year, d.tm_hour, d.tm_min, d.tm_sec))



# c = time.time()
# d = time.localtime(c)
# e = time.asctime(d)
# print(e)



n = int(input("Nhập n: "))
for i in range(n, 0, -1):
    print(i)
    time.sleep(1)
else:
    print("Start !!!")



# ten_may = input("Input your computer name: ")
# for i in range(10, 101, 10):
#     print("Hacking " + ten_may + " " + str(i) + "% ...")
#     time.sleep(3)
# else:
#     print("Successful !!!")



# ===================== DATETIME
# ngay_hien_hanh = datetime.now()
# print(ngay_hien_hanh)
# print(ngay_hien_hanh.strftime('%d-%m-%Y %H:%M:%S'))


# dt = datetime(2021, 3, 18, 20, 13, 18, 123456)
# print(dt)
# print(dt.strftime('%d-%m-%Y %H:%M:%S'))



# ===================== CALENDAR
# nam = 2020
# print(calendar.isleap(nam))



'''
thang = ?
nam = ?

1. Tháng <thang> năm <nam> có <bao nhiêu> ngày?
2. Năm <nam> có phải là năm nhuận không?
3. Thứ của ngày cuối cùng trong tháng <thang>/<nam> là <thứ mấy>?
'''

# thang = int(input("Nhập tháng: "))
# nam = int(input("Nhập năm: "))

# # 1
# # so_ngay = calendar.monthrange(nam, thang)[1]
# dt = calendar.monthrange(nam, thang)
# so_ngay = dt[1]
# print("Tháng %i năm %i có %i ngày" % (thang, nam, so_ngay))

# # 2
# if calendar.isleap(nam):
#     print("Năm %i là năm nhuần" % nam)
# else:
#     print("Năm %i không là năm nhuần" % nam)

# 3
# thu = calendar.weekday(nam, thang, so_ngay)
# if thu == 0:
#     chuoi_thu = "Thứ hai"
# elif thu == 1:
#     chuoi_thu = "Thứ ba"
# elif thu == 2:
#     chuoi_thu = "Thứ tư"
# elif thu == 3:
#     chuoi_thu = "Thứ năm"
# elif thu == 4:
#     chuoi_thu = "Thứ sáu"
# elif thu == 5:
#     chuoi_thu = "Thứ bảy"
# else:
#     chuoi_thu = "Chủ nhật"
    
# print("Thứ của ngày cuối cùng trong tháng %i năm %i là %s" % (thang, nam, chuoi_thu))

