__author__ = 'Киселева Александра'

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Ведите коэффициент a: '))
b = int(input('Ведите коэффициент b: '))
c = int(input('Ведите коэффициент c: '))

if a == 0:

    if b != 0:

        x = -c / b
        print('При a = 0, уравнение имеет 1 решение: х = ', x)

    else:
        print('Уравнение не имеет действительных корней')

else:

    A = 2 * a
    D = (b ** 2) - (2 * A * c)

    if D > 0:

        sqrt = math.sqrt(D)

        x1 = (-b + sqrt) / A
        x2 = (-b - sqrt) / A
        print('Уравнение имеет 2 корня x1 = {}, x2 = {}'.format(x1, x2))

    elif D == 0:
        x = -b / (2 * a)
        print('Уравнение имеет 1 корень', x)

    else:
        print('Уравнение не имеет действительных корней')
