def task3():
    salary = {}
    try:
        with open('text_3.txt', 'r', encoding='utf-8') as file:
            for line in file:
                salary[line.split()[0]] = float(line.split()[1])
        print('Меньше 20 000 получают:')
        for name, sal in salary.items():
            if sal < 20000:
                print(name)
        print(f'Средняя зарплата равна {sum(salary.values()) / len(salary)}')
    except IOError:
        print('Что то пошло не так')
    except:
        print('Ошибка')
