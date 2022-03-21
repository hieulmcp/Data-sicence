A = 0
chuoi_A = ''

B = 0
chuoi_B = ''

E = 0
chuoi_E = ''


n = int(input("Nhập n: "))
i = 1
while i <= n:
    # Tính A
    if i % 2 != 0:
        A += i
        chuoi_A += str(i) + " + "

    # Tính B
    if i % 2 == 0:
        B += i
        chuoi_B += str(i) + " + "

    # Tính E
    if i < 2:
        # print("Số %i không là số nguyên tố" % n)
        pass
    else:
        for j in range(2, i):
            if i % j == 0:
                # print("Số %i không là số nguyên tố" % n)
                break
        else:
            # print("Số %i là số nguyên tố" % n)
            E += i
            chuoi_E += str(i) + " + "

    # Bước nhảy
    i += 1
else:
    print("A =", chuoi_A.strip('+ '), "=", A)
    print("B =", chuoi_B.strip('+ '), "=", B)
    print("E =", chuoi_E.strip('+ '), "=", E)


