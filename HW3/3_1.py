def div(*args):
    try:
        arg_1 = int(input("Введите делимое: "))
        arg_2 = int(input("Введите делитель: "))
        res = arg_1 / arg_2
    except ValueError:
        return "Необходимо ввести только числа!"
    except ZeroDivisionError:
        return "На 0 делить нельзя!"

    return res


print(f"Результат:  {div()}")