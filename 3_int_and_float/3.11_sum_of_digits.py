# http://pythontutor.ru/lessons/int_and_float/problems/sum_of_digits/

n = int(input())

a = n / 100
b = n / 10

print(int(a) + int((a - int(a)) * 10) + ((b - int(b)) * 10))