my_list = [9, 8, 7, 6, 6, 5, 4]
new_element = int(input("Введите новый элемент списка (натуральное число): "))
i = 0
for n in my_list:
    if new_element <= n:
        i += 1
my_list.insert(i, float(new_element))
print(my_list)