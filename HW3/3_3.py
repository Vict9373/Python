def my_func():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    if a >= c and b >= c:
        return a + b
    elif a > b and b < c:
        return a + c
    else:
        return b + c


print(my_func())