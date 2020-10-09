# http://pythontutor.ru/lessons/int_and_float/problems/watch_3/

a = float(input())

s = (43200 * a) / 360
h = s // 3600
m = s % 3600 // 60

print(h, m, int(s % 60))