ho_ten = "Nguyễn Văn A"     # str
tuoi = 30                   # int
dtb = 8.52125552            # float

# Tên tôi là: Nguyễn Văn A
# Tuổi: 30
# Điểm trung bình: 8.52125552

# Cách 1
# print("Tên tôi là: %s" % ho_ten)
# print("Tuổi: %i" % tuoi)
# print("Điểm trung bình: %f" % dtb)


# Cách 2
print("Tên tôi là: %s \nTuổi: %i \nĐiểm trung bình: %.2f" % (ho_ten, tuoi, dtb))


# Cách 3
print("Tên tôi là: " + ho_ten + "\nTuổi: " + str(tuoi) + "\nĐiểm trung bình: " + str(round(dtb, 2)))


# Cách 4
print("Tên tôi là:", ho_ten, "\nTuổi:", tuoi, "\nĐiểm trung bình:", round(dtb, 2))


# Cách 5
print("Tên tôi là: {} \nTuổi: {} \nĐiểm trung bình: {}".format(ho_ten, tuoi, round(dtb, 2)))


# Cách 6
print(f"Tên tôi là: {ho_ten} \nTuổi: {tuoi} \nĐiểm trung bình: {round(dtb, 2)}")


