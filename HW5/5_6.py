import re

sum_hours ={}

with open('text_6.txt') as file:
    for line in file.readlines():
        sum_hours[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(sum_hours)