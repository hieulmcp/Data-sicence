dieu_kien = True

while dieu_kien:
    chuc_nang = int(input("Bạn muốn làm gì?\n1. In hình tam giác\n2. In hình chữ nhật\n3. Countdown\nMời bạn chọn: "))

    if chuc_nang == 1:
        n = int(input("Nhập n: "))
        for i in range(1, n + 1):
            print("*  " * i)

    elif chuc_nang == 2:
        cd = int(input("Nhập chiều dài: "))
        cr = int(input("Nhập chiều rộng: "))
        for i in range(cr):
            print("*  " * cd)

    elif chuc_nang == 3:
        n = int(input("Nhập n: "))
        while n >= 1:
            print(n)
            n -= 1
        else:
            print("Start!!!")

    else:
        print("Dữ liệu nhập không hợp lệ. Vui lòng nhập 1, 2 hoặc 3.")


    tiep_tuc = input("Bạn có muốn tiếp tục thực hiện chức năng? (y/n)\nMời bạn chọn: ")
    if tiep_tuc == 'y' or tiep_tuc == 'Y':
        dieu_kien = True
    else:
        dieu_kien = False

