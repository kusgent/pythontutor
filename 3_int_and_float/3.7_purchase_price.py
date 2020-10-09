# http://pythontutor.ru/lessons/int_and_float/problems/purchase_price/

a = int(input())
b = int(input())
n = int(input())

s1 = a * 100 + b
s2 = s1 * n

print(s2 // 100, s2 % 100)