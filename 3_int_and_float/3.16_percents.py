# http://pythontutor.ru/lessons/int_and_float/problems/percents/

p = int(input())
x = int(input())
y = int(input())

a = x * 100 + y
d = a + a * (p / 100)

print(d // 100, int(d % 100))