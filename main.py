# Hàm cộng hai số
def cong(a, b):
    return a + b

# Hàm trừ hai số
def tru(a, b):
    return a - b

# Nhập hai số từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

# Gọi hàm
tong = cong(a, b)
hieu = tru(a, b)

# In kết quả
print("Tổng của hai số là:", tong)
print("Hiệu của hai số là:", hieu)