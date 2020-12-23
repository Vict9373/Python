from itertools import count, cycle
from math import factorial

print('Введите целое число, для начала генерации нажмите Enter, для выхода из программы нажмите "q"')
for i in count(int(input("Введите стартовое число: "))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Программа повторяет элементы списка. Нажмите Enter для продолжения или "Q" для выхода и программы')
new_list = input("Введите список, разделяя элементы пробелом: ").split()
iter = cycle(new_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()
