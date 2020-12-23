text = input("Введите фразу: ").split()
for i, word in enumerate(text, 1):
    print(f"{i} {word[:10]}")