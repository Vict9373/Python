import json

with open('my_ex7.json', "w", encoding='utf-8') as write_file:
    with open('text_7.txt', encoding="utf-8") as obj:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in obj}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) >0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, write_file)