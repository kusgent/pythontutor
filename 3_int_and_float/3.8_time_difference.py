# http://pythontutor.ru/lessons/int_and_float/problems/raznost_vremen/

h = int(input())
m = int(input())
s = int(input())
h1 = int(input())
m1 = int(input())
s1 = int(input())

x = h * 3600 + m * 60 + s
x1 = h1 * 3600 + m1 * 60 + s1

print(x1 - x)