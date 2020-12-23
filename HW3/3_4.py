def my_pow(x, y):
    if y < 0:
        x = 1.0/x
        y = -y
    res = 1
    while y > 0:
        res = res * x
        y = y-1
    return res


print(my_pow(int(input("Введите x: ")), float(input("Введите y: "))))