# http://pythontutor.ru/lessons/int_and_float/problems/watch_1/

h = int(input())
m = int(input())
s = int(input())

h1 = 360 / 12 # градусов в 1 часу
h2 = h + m / 60 + s / 3600

print(h1 * h2)