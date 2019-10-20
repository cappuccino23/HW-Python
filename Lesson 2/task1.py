__author__ = 'Киселева Александра'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список, элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
from random import randint

lst = []
d = 0

my_list = [randint(-100, 100) for i in range(10)]

print('1. Список произвольных целых чисел от -100 до 100:\n', my_list)

for el in my_list:

    if el > 0:
        d = round(math.sqrt(el), 6)
        c = d**2 - (el)
        if c == 0:
            lst.append(int(d))

if lst:
    print('\nСписок, элементами которого являются квадратные корни чисел из первого списка:\n', lst)
else:
    print('Целочисленных квадратных корней нет')