import math


a, b, c = eval(input("Nhập a, b, c: "))

if a == 0:
    if b != 0:
        x = -c / b
        print("Phương trình có nghiệm x =", x)
    else:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
else:
    delta = math.pow(b, 2) - 4 * a * c 
    if delta < 0:
        print("Phương trình vô nghiệm.")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có 2 nghiệm:")
        print("x1 =", x1)
        print("x2 =", x2)
