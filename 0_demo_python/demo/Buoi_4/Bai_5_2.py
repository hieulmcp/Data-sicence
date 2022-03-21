n = int(input("Nhập n: "))
x = int(input("Nhập x: "))


S = 1
i = 1
while i <= n:
    S *= (x * x + 1)
    i += 1
print("S =", S)

