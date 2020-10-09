# http://pythontutor.ru/lessons/int_and_float/problems/last_digit/

import math

n = int(input('Введите натуральное число: '))

x = n/10

y = x - math.floor(x)

print(y*10)