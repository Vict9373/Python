f = open("Text5_1.txt", 'w')
print("Введите данные, для перехода к следующей строке нажмите Enter, для завершения ввода нажмите Enter на пустой строке")
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()

