goods =[]
parametr = {"Название", "Цена", "Количество", "Ед.измерения"}
analitycs = {"Название": [], "Цена": [], "Количество": [], "Ед.измерения": []}
num = 0
while True:
    if input("Для выхода из программы нажмите "Q", для продолжения "Enter":").upper() == "Q":
        break
    num += 1
    for f in parametr.keys():
        new_par = input(f"Введите параметр"{f}": ")
        parametr[f] = int(new_par) if f == "Цена" or f == "Количество" else new_par
        analitycs[f].append(parametr[f])
goods.append((num, parametr))
print(f"\nСтруктура товаров\n{goods}")
print(f"\nТекущая аналитика по товарам:\n {"*" * 30 }")
for key, value in analitycs.items():
    print(f"{key[:25]:>30}: {value}")
print ("*" * 30)