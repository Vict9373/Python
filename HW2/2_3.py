month = int(input("Введите порядковый номер месяца (от 1 до 12): "))
season_dict = {0: "Зима", 1: "Весна", 2: "Лето", 3: "Осень", 4: "Зима"}
season_list = ["Зима", "Весна", "Лето", "Осень", "Зима"]
if 0 < int(month) <= 12:
    print(f"Словарь сезонов - {season_dict[int(month) // 3]}")
    print(f"Список сезонов - {season_list[int(month) // 3]}")

