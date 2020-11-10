# http://pythontutor.ru/lessons/while/problems/kth_fibonacci/

n = int(input())
a = 0
b = 1
if n == 0:
    f = 0
elif n == 1:
    f = 1
for i in range(2, n + 1):
    f = a + b
    if i != n:
        a, b = b, f
print(f)