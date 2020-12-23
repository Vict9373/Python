from sys import argv


def income():
    try:
        time, rate, bonus = map(float, argv[1:])
        print("Заработная плата: ", time)
        print("Часовая ставка: ", rate)
        print("Премия ", bonus)
        print(f"Income - {time * rate + bonus}")
    except ValueError:
        print(("Необходимо вести 3 числа"))


income()