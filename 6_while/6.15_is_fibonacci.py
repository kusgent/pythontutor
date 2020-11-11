# http://pythontutor.ru/lessons/while/problems/is_fibonacci/

n = int(input())
a, b = 0, 1
q = 1
while b < n:
    a, b = b, a + b
    q += 1
if n == 0:
    print(0)
elif n == 1:
    print('1 or 2')
elif n == b:
    print(q)
else:
    print(-1)