# http://pythontutor.ru/lessons/inout_and_arithmetic_operations/problems/electronic_watch/

n = int(input())
a = (n % 1440) // 60
b = (n % 1440) % 60
print(a, b)