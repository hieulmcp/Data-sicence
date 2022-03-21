# ĐỌC

# f = open('files/vi_du_1.txt')  # Đường dẫn tương đối
# f = open('C:\\tap_tin\\vi_du_1.txt')  # Đường dẫn tuyệt đối
# noi_dung = f.read()
# print(noi_dung)
# f.close()



# GHI
# f = open('files/vi_du_2.txt', 'a')
# noi_dung = '\nTest thu lan 5'
# f.write(noi_dung)
# f.close()



def doc_file_txt(duong_dan):
    f = open(duong_dan, 'r', encoding='utf-8')
    noi_dung = f.read()
    f.close()
    return noi_dung


def ghi_file_txt(duong_dan, quyen, noi_dung):
    f = open(duong_dan, quyen, encoding='utf-8')
    f.write(noi_dung)
    f.close()
    return


# path = 'files/vi_du_2.txt'

# # ĐỌC
# du_lieu = doc_file_txt(path)
# print(du_lieu)





# # GHI
# content = 'Test thu'
# ghi_file_txt(path, 'a', content)



# VD THÊM
# def doc_file_txt(duong_dan):
#     f = open(duong_dan) 
#     for dong in f:
#         print(dong)
#     f.close()
#     return
# path = 'files/vi_du_1.txt'
# doc_file_txt(path)




f = open('files/vi_du_1.txt')
print(f.read())
f.seek(0, 0)
print(f.read())
# print(f.tell())
f.close()