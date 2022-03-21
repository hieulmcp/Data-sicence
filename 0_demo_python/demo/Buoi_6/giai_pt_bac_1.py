# ax + b = 0
# - Nếu a != 0           => Phương trình có 1 nghiệm x = -b/a
# - Nếu a = 0 và b = 0   => Phương trình có vô số nghiệm
# - Nếu a = 0 và b != 0  => Phương trình vô nghiệm

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))


if a != 0:
    x = -b / a
    print("Phương trình có nghiệm x =", x)
else:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")



if a != 0:
    x = -b / a
    print("Phương trình có nghiệm x =", x)
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm.")
else:
    print("Phương trình vô nghiệm.")