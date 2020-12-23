from functools import reduce

def my_func(el_1, el_2):
    return el_1 * el_2

new_list = [el for el in range(100, 1001, 2)]
print(f"Список четных значений: {new_list}")
print(f"Результат перемножения элементов списка: {reduce(my_func, new_list)}")
