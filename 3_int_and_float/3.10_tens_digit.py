# http://pythontutor.ru/lessons/int_and_float/problems/tens_digit/

n = int(input())

a = (n + 100) / 100
b = a - int(a)
print(int(b * 10))