__author__ = 'Киселева Александра'

# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]

from random import randint

my_list = [randint(0, 100) for i in range(30)]
#my_list = [1, 2, 4, 6, 8, 5, 6, 2, 5, 2, 9, 11, 0, 7]

print('Список, заполненный произвольными целыми числами:')
for i in my_list:
   print(i, end=' ')

#создаем словарь, в котором количество вхождений элементов в строке не больше 1
mlst = dict((x, my_list.count(x)) for x in my_list if my_list.count(x) == 1)

print('\nСписок из уникальных элементов первого:')
for key in mlst:
   print(key, end=' ')
