list_a = list(input('Введите числа без пробелов: '))
for i in range(1, len(list_a), 2):
    list_a[i-1], list_a[i] = list_a[i], list_a[i-1]
print("Измененный список: ", list_a)