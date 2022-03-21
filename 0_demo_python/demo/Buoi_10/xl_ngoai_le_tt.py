# a = 12
# b = int(input("Nhập b: "))
# thuong = a / b
# print("Thương =", thuong)


# try:
#     a = 12
#     b = int(input("Nhập b: "))
#     thuong = a / b
#     print("Thương =", thuong)
# except ZeroDivisionError:
#     print("Lỗi chia cho 0 rồi")
# except ValueError:
#     print("Nhập số dùm đi")
# except Exception as loi_chung:  # luôn đặt ở sau những except khác
#     print("Lỗi rồi")
#     print("Nhãn lỗi:", type(loi_chung).__name__)
#     print("Mô tả:", loi_chung)


# try:
#     a = 12
#     b = int(input("Nhập b: "))
#     thuong = a / b
# except ZeroDivisionError:
#     print("Lỗi chia cho 0 rồi")
# except ValueError:
#     print("Nhập số dùm đi")
# except Exception as loi_chung:  # luôn đặt ở sau những except khác
#     print("Lỗi rồi")
#     print("Nhãn lỗi:", type(loi_chung).__name__)
#     print("Mô tả:", loi_chung)
# else:
#     print("Thương =", thuong)




# try:
#     a = 12
#     b = int(input("Nhập b: "))
#     thuong = a / b
# except (ZeroDivisionError, ValueError):
#     print("Lỗi chung")
# except Exception as loi_chung:  # luôn đặt ở sau những except khác
#     print("Lỗi rồi")
#     print("Nhãn lỗi:", type(loi_chung).__name__)
#     print("Mô tả:", loi_chung)
# else:
#     print("Thương =", thuong)



# try:
#     a = 12
#     b = int(input("Nhập b: "))
#     thuong = a / b
# except ZeroDivisionError:
#     print("Lỗi chia cho 0")
# except Exception as loi_chung:  # luôn đặt ở sau những except khác
#     print("Lỗi rồi")
#     print("Nhãn lỗi:", type(loi_chung).__name__)
#     print("Mô tả:", loi_chung)
# else:
#     print("Thương =", thuong)
# finally:
#     print('Tổng =', a + b)
#     print('Hiệu =', a - b)
#     print('Tích =', a * b)
    



# try:
#     a = 12
#     b = int(input("Nhập b: "))
#     if b == 0:
#         raise ZeroDivisionError('Lỗi chia cho 0')
#     thuong = a / b
# except ZeroDivisionError as loi_1:
#     print(loi_1)
# except Exception as loi_chung:  # luôn đặt ở sau những except khác
#     print("Lỗi rồi")
#     print("Nhãn lỗi:", type(loi_chung).__name__)
#     print("Mô tả:", loi_chung)
# else:
#     print("Thương =", thuong)
# finally:
#     print('Tổng =', a + b)
#     print('Hiệu =', a - b)
#     print('Tích =', a * b)



class LoiChiaChoKhong(ZeroDivisionError):
    def __init__(self, _thong_bao):
        self.a = _thong_bao

class LoiGiaTri(ValueError):
    def __init__(self, _thong_bao):
        self.a = _thong_bao


try:
    a = 12
    b = int(input("Nhập b: "))
    if b == 0:
        raise LoiChiaChoKhong('Lỗi chia cho 0')
    thuong = a / b
except LoiChiaChoKhong as loi_1:
    print(loi_1)
except Exception as loi_chung:  # luôn đặt ở sau những except khác
    print("Lỗi rồi")
    print("Nhãn lỗi:", type(loi_chung).__name__)
    print("Mô tả:", loi_chung)
else:
    print("Thương =", thuong)
finally:
    print('Tổng =', a + b)
    print('Hiệu =', a - b)
    print('Tích =', a * b)