from random import randint

my_list = [randint(-1, 20) for _ in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Исходны список: {my_list}")
print(f"Новый список:, {new_list}")