n = int(input("Nhập n: "))

# Cách 1
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# else:
#     if count == 2:
#         print("Số %i là số nguyên tố" % n)
#     else:
#         print("Số %i không là số nguyên tố" % n)


# Cách 2
if n < 2:
    print("Số %i không là số nguyên tố" % n)
else:
    for i in range(2, n):
        if n % i == 0:
            print("Số %i không là số nguyên tố" % n)
            break
    else:
        print("Số %i là số nguyên tố" % n)

