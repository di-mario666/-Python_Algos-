"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

a = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {a}')

max_index = 0
for i in a:
    if a.count(max_index) < a.count(i):
        max_index = a.index(i)

print(f'Число {a[max_index]}, встречается {a.count(max_index)} раза')