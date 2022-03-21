import csv


# # ĐỌC VÀ XỬ LÝ DỮ LIỆU
# data = []
# f = open('files/ds_khach_hang.csv', encoding='UTF-8')
# for dong in csv.reader(f):
#     # print(dong[0].title())
#     dong[0] = dong[0].title()
#     data.append(dong)
# print(data)
# f.close()



# # GHI => TRƯỚC KHI GHI PHẢI TẠO DỮ LIỆU DẠNG [[], [], [], ...]
# f = open('files/ds_khach_hang_edited.csv', 'w', encoding='utf-8', newline='')
# for dong in data:
#     csv.writer(f).writerow(dong)
# f.close()
    



# ======== HỌC SINH 
data = []
f = open('files/hoc_sinh.csv', encoding='utf-8')
for dong in csv.reader(f):
    dtb = (float(dong[2]) + float(dong[3]) + float(dong[4])) / 3
    dong.append(round(dtb, 1))
    data.append(dong)
f.close()


f = open('files/ket_qua.csv', 'w', encoding='utf-8', newline='')
for dong in data:
    csv.writer(f).writerow(dong)
f.close()
