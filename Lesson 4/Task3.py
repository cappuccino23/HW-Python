# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import randint

m = 2500

my_list = ''

for el in range(m):
    x = str(randint(0, 9))
    my_list = my_list + x

print(my_list)
